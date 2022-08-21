// CTaxForm implementation

#include "StdAfx.h"
#include "CALCINFO.H"
#include "Calcfld.h"
#include "Calcform.h"
#include "CalcStaticData.h"
#include "CalcSerializeUtils.h"
#include "TaxAct.CalcDll/DllImpl.h"

#include <algorithm>

#define FORMSTATUS_MASK (FORMSTATUS_OPENED|FORMSTATUS_MODIFIED|FORMSTATUS_IMPORTED|FORMSTATUS_USERMODIFIED)

CTaxForm::CTaxForm()
{
    m_wID = 0;
    m_wCopyID = 0;
    m_dwStatus = 0;
    m_wTotalFields = 0;
    m_wParentFormID = 0;
    m_wParentCopyID = 0;
    m_pParent = NULL;
#ifdef CALCSTATE
    m_wFedParentFormID = 0;
#endif
    m_pFields = NULL;
    m_pFormMgr = NULL;
    m_pfnUpdate = NULL;
    m_pUpdate = NULL;
    m_wFormCreationTriggerFormID = 0;
    m_wFormCreationTriggerFieldIndex = 0;
    m_wFormCreationTriggerFormCopyID = 0;
    m_strFormCreationTriggerFieldName[0] = '\0';

    m_ownerDll = TaxAct::CalcDll::CurrentModuleHandle();
}

CTaxForm::~CTaxForm()
{
    UPDATEFORMOBJ* pUpdate, *pTemp;

    for (pUpdate = m_pUpdate; pUpdate;)
    {
        pTemp = pUpdate->pNext;
        delete pUpdate;
        pUpdate = pTemp;
    }

    if (m_pFields)
    {
        CTaxField* pField;

        for (size_t wCount = 0; wCount < m_wTotalFields; wCount++)
        {
            pField = *(m_pFields + wCount);

            if (pField)
            {
                delete pField;
            }
        }

        delete [] m_pFields;
        m_pFields = NULL;
    }
}

BOOL CTaxForm::Init(WORD wFormID, CTaxFormManager* pFormMgr)
{
    m_wID = wFormID;
    m_pFormMgr = pFormMgr;
    m_dwStatus = g_calcStaticData.forms[wFormID - 1].flags;
    m_wTotalFields = g_calcStaticData.forms[wFormID - 1].totalFields;

    if (!(m_pFields = new(std::nothrow) CTaxField *[m_wTotalFields]))
    {
        return FALSE;
    }

    CTaxField* pField;
    WORD wType;
    memset(m_pFields, 0, m_wTotalFields * sizeof(CTaxField*));

    for (size_t wFieldID = 1; wFieldID <= m_wTotalFields; wFieldID++)
    {
        wType = m_pFormMgr->GetFieldType(m_wID, static_cast<WORD>(wFieldID));

        pField = CTaxField::Create(wType);

        if (!pField)
        {
            return FALSE;
        }

        pField->m_wID = static_cast<WORD>(wFieldID);
        pField->m_pForm = this;
        *(m_pFields + (wFieldID - 1)) = pField;
    }

    if (!(*FormInitFunc[wFormID - 1])(this))
    {
        return FALSE;
    }

    return TRUE;
}

ITaxForm* CTaxForm::GetParent()
{
    if (m_pParent)
    {
        return m_pParent;
    }

    if ((m_wParentFormID > 0) && (m_wParentCopyID > 0))
    {
        m_pParent = m_pFormMgr->GetForm(m_wParentFormID, m_wParentCopyID);
    }

#ifdef CALCSTATE
    else if ((m_wFedParentFormID > 0) && (m_wParentCopyID > 0))
    {
        m_pParent = m_pFormMgr->m_pFedFormMgr->GetForm(m_wFedParentFormID, m_wParentCopyID);
    }

#endif
    else
    {
        m_pParent = NULL;
    }

    return m_pParent;
}

void CTaxForm::SetParent(ITaxForm* pParent, BOOL bCalculate /* = TRUE */)
{
    if (pParent)
    {
        m_pParent = pParent;
#ifdef CALCSTATE

        if (pParent->GetFormManager()->IsFederal())
        {
            m_wFedParentFormID = pParent->GetID();
        }
        else
#endif
        m_wParentFormID = pParent->GetID();

        m_wParentCopyID = pParent->GetCopyID();
    }
    else
    {
        m_wParentFormID = 0;
        m_wParentCopyID = 0;
#ifdef CALCSTATE
        m_wFedParentFormID = 0;
#endif
    }

    if (bCalculate)
    {
        CalculateAllFields();
    }
}

WORD CTaxForm::GetID()
{
    return m_wID;
}
WORD CTaxForm::GetCopyID()
{
    return m_wCopyID;
}

WORD CTaxForm::GetCopyIndex()
{
    const FORMSCONTAINER* pForms = m_pFormMgr->m_pForms[m_wID - 1];

    if (m_pFormMgr->m_pForms[m_wID - 1] != NULL)
    {
        for (size_t w = 0; w < pForms->size(); w++)
        {
            if ((*pForms)[w] == this)
            {
                return (static_cast<WORD>(w) + 1);
            }
        }
    }

    return 0;
}

size_t CTaxForm::GetDataSize()
{
    size_t iSize = sizeof(m_wCopyID);
    iSize += sizeof(m_dwStatus);
    iSize += sizeof(m_wParentFormID);
    iSize += sizeof(m_wParentCopyID);
#ifdef CALCSTATE
    iSize += sizeof(m_wFedParentFormID);
#endif
    iSize += sizeof(m_wFormCreationTriggerFormID);
    iSize += sizeof(m_wFormCreationTriggerFormCopyID);
    iSize += std::char_traits<char>::length(m_strFormCreationTriggerFieldName) + 1;
    iSize += sizeof(m_wFormCreationTriggerFieldIndex);

    if (m_pFields)
    {
        CTaxField* pField;
        for (size_t wCount = 0; wCount < m_wTotalFields; wCount++)
        {
            pField = *(m_pFields + wCount);
            iSize += pField->GetDataSize();
        }
    }

    return iSize;
}

void CTaxForm::GetData(void *lpData)
{
    if (!m_pFields)
    {
        return;
    }

    SetStatus(FORMSTATUS_HASTRIGGERFIELD, TRUE);

    LPSTR lpTemp = (LPSTR)lpData;
    *((WORD*)lpTemp) = m_wCopyID;
    lpTemp += sizeof(m_wCopyID);
    *((DWORD*)lpTemp) = (m_dwStatus & ~(DWORD)FORMSTATUS_OPENED);  //bpj 9/11/2012 - Ensure the FORMSTATUS_OPENED is false on save of return.
    lpTemp += sizeof(m_dwStatus);
    *((WORD*)lpTemp) = m_wParentFormID;
    lpTemp += sizeof(m_wParentFormID);
    *((WORD*)lpTemp) = m_wParentCopyID;
    lpTemp += sizeof(m_wParentCopyID);
#ifdef CALCSTATE
    *((WORD*)lpTemp) = m_wFedParentFormID;
    lpTemp += sizeof(m_wFedParentFormID);
#endif
    *((WORD*)lpTemp) = m_wFormCreationTriggerFormID;
    lpTemp += sizeof(m_wFormCreationTriggerFormID);
    *((WORD*)lpTemp) = m_wFormCreationTriggerFormCopyID;
    lpTemp += sizeof(m_wFormCreationTriggerFormCopyID);
    strcpy_s(lpTemp, std::char_traits<char>::length(m_strFormCreationTriggerFieldName) + 1, m_strFormCreationTriggerFieldName);
    lpTemp += std::char_traits<char>::length(m_strFormCreationTriggerFieldName) + 1;
    *((WORD*)lpTemp) = m_wFormCreationTriggerFieldIndex;
    lpTemp += sizeof(m_wFormCreationTriggerFieldIndex);

    CTaxField* pField;
    for (size_t wCount = 0; wCount < m_wTotalFields; wCount++)
    {
        pField = *(m_pFields + wCount);
        pField->GetData(lpTemp);
        lpTemp += pField->GetDataSize();
    }
}

void CTaxForm::SetData(const void *lpData)
{
    if (!m_pFields)
    {
        return;
    }

    LPSTR lpTemp = (LPSTR)lpData;
    m_wCopyID = *((WORD*)lpTemp);
    lpTemp += sizeof(m_wCopyID);
    m_dwStatus = *((DWORD*)lpTemp);
    lpTemp += sizeof(m_dwStatus);
    m_wParentFormID = *((WORD*)lpTemp);
    lpTemp += sizeof(m_wParentFormID);
    m_wParentCopyID = *((WORD*)lpTemp);
    lpTemp += sizeof(m_wParentCopyID);

#ifdef CALCSTATE
    m_wFedParentFormID = *((WORD*)lpTemp);
    lpTemp += sizeof(m_wFedParentFormID);
#endif
    
    // Check if trigger bit is set in status, get the trigger form id and the trigger field id
    if (GetStatus(FORMSTATUS_HASTRIGGERFIELD))
    {
        m_wFormCreationTriggerFormID = *((WORD*)lpTemp);
        lpTemp += sizeof(m_wFormCreationTriggerFormID);
        m_wFormCreationTriggerFormCopyID = *((WORD*)lpTemp);
        lpTemp += sizeof(m_wFormCreationTriggerFormCopyID);
        strcpy_s(m_strFormCreationTriggerFieldName, std::min(std::char_traits<char>::length(lpTemp) + 1, sizeof(m_strFormCreationTriggerFieldName)), lpTemp);
        lpTemp += std::char_traits<char>::length(m_strFormCreationTriggerFieldName) + 1;
        m_wFormCreationTriggerFieldIndex = *((WORD*)lpTemp);
        lpTemp += sizeof(m_wFormCreationTriggerFieldIndex);
    }

    CTaxField* pField;
    for (size_t wCount = 0; wCount < m_wTotalFields; wCount++)
    {
        pField = *(m_pFields + wCount);
        pField->SetData(lpTemp);
        lpTemp += pField->GetDataSize();
    }
}

void CTaxForm::GetName(LPSTR szName)
{
    if (m_pFormMgr)
    {
        m_pFormMgr->GetFormName(szName, m_wID);
    }
}

void CTaxForm::ImportData(const void *lpData, BOOL bState)
{
    if (!m_pFields)
    {
        return;
    }

    LPSTR lpTemp = (LPSTR)lpData;
    m_wCopyID = *((WORD*)lpTemp);
    lpTemp += sizeof(m_wCopyID);
    m_dwStatus = *((DWORD*)lpTemp);
    lpTemp += sizeof(m_dwStatus);
    m_wParentFormID = *((WORD*)lpTemp);
    lpTemp += sizeof(m_wParentFormID);
    m_wParentCopyID = *((WORD*)lpTemp);
    lpTemp += sizeof(m_wParentCopyID);

    if (bState)
    {
        lpTemp += sizeof(m_wParentFormID);
    }

    // Check if trigger bit is set in status, get the trigger form id and the trigger field id
    if (GetStatus(FORMSTATUS_HASTRIGGERFIELD))
    {
        m_wFormCreationTriggerFormID = *((WORD*)lpTemp);
        lpTemp += sizeof(m_wFormCreationTriggerFormID);
        m_wFormCreationTriggerFormCopyID = *((WORD*)lpTemp);
        lpTemp += sizeof(m_wFormCreationTriggerFormCopyID);
        strcpy_s(m_strFormCreationTriggerFieldName, std::min(std::char_traits<char>::length(lpTemp) + 1, sizeof(m_strFormCreationTriggerFieldName)), lpTemp);
        lpTemp += std::char_traits<char>::length(m_strFormCreationTriggerFieldName) + 1;
        m_wFormCreationTriggerFieldIndex = *((WORD*)lpTemp);
        lpTemp += sizeof(m_wFormCreationTriggerFieldIndex);
    }

    CTaxField* pField;
    for (size_t wCount = 0; wCount < m_wTotalFields; wCount++)
    {
        pField = *(m_pFields + wCount);
        pField->SetData(lpTemp);
        lpTemp += pField->GetDataSize();
    }
}

BOOL CTaxForm::GetStatus(DWORD dwStatus)
{
    return ((m_dwStatus & dwStatus) == dwStatus);
}

void CTaxForm::SetStatus(DWORD dwStatus, BOOL bSet)
{
    DWORD dwPrevStatus = m_dwStatus & FORMSTATUS_MASK;

    if (bSet)
    {
        m_dwStatus |= dwStatus;
    }
    else
    {
        m_dwStatus &= ~dwStatus;
    }

    if (dwPrevStatus != (m_dwStatus & FORMSTATUS_MASK))
    {
        Update();
    }
}

WORD CTaxForm::GetTotalFields()
{
    return m_wTotalFields;
}

ITaxField* CTaxForm::GetField(WORD wFieldID)
{
    ASSERT((wFieldID > 0) && (wFieldID <= m_wTotalFields));

    if (!m_pFields || (wFieldID == 0) || (wFieldID > m_wTotalFields))
    {
        return NULL;
    }

    return (*(m_pFields + (wFieldID - 1)));
}

void CTaxForm::GetDescription(LPSTR szDesc, size_t iSize)
{
    *szDesc = '\0';

    WORD wFieldID = g_calcStaticData.forms[m_wID - 1].descriptionFieldID;

    if (wFieldID != 0)
    {
        ITaxField* pField = GetField(wFieldID);
        pField->GetString(szDesc, iSize);
    }
}

void CTaxForm::GetProDescription(LPSTR szDesc, size_t iSize)
{
    *szDesc = '\0';

    WORD wProFieldID = g_calcStaticData.forms[m_wID - 1].proDescriptionFieldID;
    WORD wFieldID = g_calcStaticData.forms[m_wID - 1].descriptionFieldID;

    if (wProFieldID != 0)
    {
        ITaxField* pField = GetField(wProFieldID);
        pField->GetString(szDesc, iSize);
    }
    else if (wFieldID != 0)
    {
        ITaxField* pField = GetField(wFieldID);
        pField->GetString(szDesc, iSize);
    }
}

void CTaxForm::CalculateAllFields()
{
    CTaxField* pField;
#ifdef __CALCTIMING
    DWORD dwTick1, dwTick2;
    char szForm[64];
    char szFld[64];
    char szStr[128];


    m_pFormMgr->GetFormName(szForm, m_wID);

    for (size_t wFieldID = 1; wFieldID <= m_wTotalFields; wFieldID++)
    {
        dwTick1 = GetTickCount();
        pField = GetCalcField(static_cast<WORD>(wFieldID));
        pField->Calculate();

        if (pField->GetStatus(FLDSTATUS_CREATEFORM))
        {
            pField->Update();
        }

        dwTick2 = GetTickCount();

        if ((dwTick2 - dwTick1) > 50)
        {
            m_pFormMgr->GetFieldName(szFld, m_wID, wFieldID);
            sprintf(szStr, "%-20s(%02u).%-20s(%02u)  %06ul CalculateAllFields\n", szForm, GetCopyID(), szFld, pField->GetIndex(), dwTick2 - dwTick1);
            OutputDebugString(szStr);
        }
    }

#else

    for (size_t wFieldID = 1; wFieldID <= m_wTotalFields; wFieldID++)
    {
        pField = GetCalcField(static_cast<WORD>(wFieldID));
        pField->Calculate();

        if (pField->GetStatus(FLDSTATUS_CREATEFORM))
        {
            pField->Update();
        }
    }

#endif
}

void CTaxForm::UpdateAllFields()
{
    CTaxField* pField;

    for (size_t wFieldID = 1; wFieldID <= m_wTotalFields; wFieldID++)
    {
        pField = GetCalcField(static_cast<WORD>(wFieldID));
        pField->Update();
    }

    Update();
}

const RadioGroupInfo *CTaxForm::GetRadioGroupForField(WORD fieldID)
{
    const RadioGroupInfo *radioGroup = nullptr;

    for (const auto& item : g_calcStaticData.forms[m_wID - 1].radioGroups)
    {
        auto findField = std::find(item.fieldIDs.begin(), item.fieldIDs.end(), fieldID);
        if (findField != item.fieldIDs.end())
        {
            radioGroup = &item;
            break;
        }
    }

    return radioGroup;
}

void CTaxForm::SetRadioButton(WORD wFieldID, BOOL bCalculate)
{
    const RadioGroupInfo *radioGroup = GetRadioGroupForField(wFieldID);

    if (radioGroup)
    {
        ITaxField *pField = nullptr;

        for (WORD fieldID: radioGroup->fieldIDs)
        {
            pField = GetField(fieldID);
            pField->SetBool((fieldID == wFieldID));

            if (bCalculate)
            {
                pField->SetStatus(FLDSTATUS_MODIFIED | FLDSTATUS_USERMODIFIED, TRUE);
            }
        }

        if (bCalculate)
        {
            if (!pField->GetStatus(FLDSTATUS_QUICKENTRY))
            {
                SetStatus(FORMSTATUS_MODIFIED, TRUE);
            }

            for (WORD fieldID : radioGroup->fieldIDs)
            {
                pField = GetField(fieldID);
                pField->Calculate();
            }
        }
    }
}

void CTaxForm::SetRadioOverride(WORD wFieldID)
{
    const RadioGroupInfo *radioGroup = GetRadioGroupForField(wFieldID);

    if (radioGroup)
    {
        for (WORD fieldID : radioGroup->fieldIDs)
        {
            ITaxField *pField = GetField(fieldID);
            pField->SetStatus(FLDSTATUS_OVERRIDDEN, TRUE);
        }
    }
}

void CTaxForm::ClearRadioOverride(WORD wFieldID)
{
    const RadioGroupInfo *radioGroup = GetRadioGroupForField(wFieldID);

    if (radioGroup)
    {
        for (WORD fieldID : radioGroup->fieldIDs)
        {
            ITaxField *pField = GetField(fieldID);
            pField->SetStatus(FLDSTATUS_OVERRIDDEN | FLDSTATUS_MODIFIED | FLDSTATUS_USERMODIFIED, FALSE);
        }

        for (WORD fieldID : radioGroup->fieldIDs)
        {
            ITaxField *pField = GetField(fieldID);
            pField->Calculate();
        }
    }
}

WORD CTaxForm::GetRadioButtonGroup(WORD wFieldID)
{
    WORD result = 0;

    for (const auto& item : g_calcStaticData.forms[m_wID - 1].radioGroups)
    {
        result++;

        auto findField = std::find(item.fieldIDs.begin(), item.fieldIDs.end(), wFieldID);
        if (findField != item.fieldIDs.end())
        {
            return result;
        }
    }

    return 0;
}

ITaxFormManager* CTaxForm::GetFormManager()
{
    return m_pFormMgr;
}

CTaxField* CTaxForm::GetCalcField(WORD wFieldID)
{
    return (CTaxField*)GetField(wFieldID);
}

CTaxField* CTaxForm::GetCalcFieldSafeIndex(WORD wFieldID, WORD wIndex)
{
    // short-circuit if wIndex is 0
    if (wIndex == 0)
    {
        return GetCalcField(wFieldID);
    }

    CTaxField* result = NULL;

#ifdef _DEBUG
    // check that the field names for the base (index 0) and our desired field is the same
    // this is similar to the check that CTaxFormManager::GetFieldID implements
    CTaxField* baseField = GetCalcField(wFieldID);
    CTaxField* indexedField = GetCalcField(wFieldID + wIndex);

    if (baseField && indexedField)
    {
        char baseName[64] = {};
        char indexedName[64] = {};

        m_pFormMgr->GetFieldName(baseName, GetID(), wFieldID);
        m_pFormMgr->GetFieldName(indexedName, GetID(), wFieldID + wIndex);

        int match = strcmp(baseName, indexedName);

        if (match == 0)
        {
            result = indexedField;
        }
        else
        {
            char szForm[64] = {};
            char szMsg[256] = {};

            m_pFormMgr->GetFormName(szForm, GetID());
            sprintf_s(szMsg, "Field index out-of-bounds: %s.%s(%d).",
                      szForm, baseName, wIndex);

            throw std::runtime_error(std::string(szMsg));
        }
    }

#else
    // todo: diagnostics here too?
    result = GetCalcField(wFieldID + wIndex);
#endif

    return result;
}

void CTaxForm::Update()
{
    if (m_pfnUpdate)
    {
        (*m_pfnUpdate)(m_pFormMgr);
    }

    ExternalUpdate();
}

void CTaxForm::AttachExternalUpdate(ITaxFormManager* pFormMgr, CALCEXPFORMUPDATEFUNC pfnUpdate)
{
    UPDATEFORMOBJ* pUpdate;

    for (pUpdate = m_pUpdate; pUpdate; pUpdate = pUpdate->pNext)
    {
        if (pUpdate->pFormMgr == pFormMgr)
        {
            return;
        }

        if (!pUpdate->pNext)
        {
            break;
        }
    }

    UPDATEFORMOBJ* pNew;
    if (pNew = new(std::nothrow) UPDATEFORMOBJ)
    {
        pNew->pNext = NULL;
        pNew->pFormMgr = pFormMgr;
        pNew->pfnUpdate = pfnUpdate;

        if (pUpdate)
        {
            pUpdate->pNext = pNew;
        }
        else
        {
            m_pUpdate = pNew;
        }
    }
}

void CTaxForm::DetachExternalUpdate(ITaxFormManager* pFormMgr)
{
    UPDATEFORMOBJ* pUpdate, *pPrev;

    for (pUpdate = m_pUpdate, pPrev = NULL; pUpdate;
         pPrev = pUpdate, pUpdate = pUpdate->pNext)
    {
        if (pUpdate->pFormMgr == pFormMgr)
        {
            if (pPrev)
            {
                pPrev->pNext = pUpdate->pNext;
            }
            else
            {
                m_pUpdate = pUpdate->pNext;
            }

            delete pUpdate;
            break;
        }
    }
}

WORD CTaxForm::GetTriggerFormID()
{ 
    return m_wFormCreationTriggerFormID; 
}

char *CTaxForm::GetTriggerFieldName()
{ 
    return m_strFormCreationTriggerFieldName; 
}

WORD CTaxForm::GetTriggerFormCopyID()
{ 
    return m_wFormCreationTriggerFormCopyID; 
}

WORD CTaxForm::GetTriggerFieldIndex()
{ 
    return m_wFormCreationTriggerFieldIndex; 
}

void CTaxForm::SetTriggerValues(WORD wFormID, WORD wFormCopyID, LPSTR szFieldName, WORD wFieldIndex)
{
    m_wFormCreationTriggerFormID = wFormID;
    strcpy_s(m_strFormCreationTriggerFieldName, sizeof m_strFormCreationTriggerFieldName, szFieldName);
    m_wFormCreationTriggerFormCopyID = wFormCopyID;
    m_wFormCreationTriggerFieldIndex = wFieldIndex;
}

void CTaxForm::ExternalUpdate()
{
    for (UPDATEFORMOBJ* pUpdate = m_pUpdate; pUpdate; pUpdate = pUpdate->pNext)
    {
        (*pUpdate->pfnUpdate)(pUpdate->pFormMgr);
    }
}

bool CTaxForm::ReadJson(const char *in)
{
    rapidjson::Document document;
    document.Parse(in);
    return ReadJson(document);
}

bool CTaxForm::WriteJson(DllStringBuffer *out)
{
    if (out)
    {
        rapidjson::StringBuffer buffer;
        buffer.Clear();
        rapidjson::Writer<rapidjson::StringBuffer> writer(buffer);

        if (WriteJson(writer))
        {
            out->SetData(buffer.GetString());
            return true;
        }
    }

    return false;
}

void CTaxForm::SetStatusData(DWORD dwStatus)
{
    m_dwStatus = (m_dwStatus & FORMSTATUS_MASK_STATIC) | (dwStatus & FORMSTATUS_MASK_DYNAMIC);
}

DWORD CTaxForm::GetStatusData()
{
    return m_dwStatus & FORMSTATUS_MASK_DYNAMIC;
}

bool CTaxForm::ReadJson(rapidjson::Value& in)
{
    auto findFlags = in.FindMember("Flags");
    if (findFlags != in.MemberEnd())
    {
        SetStatusData(findFlags->value.GetUint());
    }

    auto findParentForm = in.FindMember("ParentForm");
    if (findParentForm != in.MemberEnd())
    {
        JsonFormKey parentForm(findParentForm->value.GetString());
        m_wParentFormID = m_pFormMgr->GetFormID(parentForm.formName().c_str());
        m_wParentCopyID = parentForm.copyId();
    }

#ifdef CALCSTATE
    auto findFedParentForm = in.FindMember("FedParentForm");
    if (findFedParentForm != in.MemberEnd())
    {
        JsonFormKey fedParentForm(findFedParentForm->value.GetString());
        m_wFedParentFormID = m_pFormMgr->m_pFedFormMgr->GetFormID(fedParentForm.formName().c_str());
        m_wParentCopyID = fedParentForm.copyId();
    }
#endif

    auto findCreationTriggerForm = in.FindMember("CreationTriggerForm");
    if (findCreationTriggerForm != in.MemberEnd())
    {
        JsonFormKey creationTriggerForm(findCreationTriggerForm->value.GetString());
        m_wFormCreationTriggerFormID = m_pFormMgr->GetFormID(creationTriggerForm.formName().c_str());
        m_wFormCreationTriggerFormCopyID = creationTriggerForm.copyId();
    }

    auto findCreationTriggerField = in.FindMember("CreationTriggerField");
    if (findCreationTriggerField != in.MemberEnd())
    {
        JsonFieldKey creationTriggerField(findCreationTriggerField->value.GetString());
        strcpy_s(m_strFormCreationTriggerFieldName, creationTriggerField.fieldName().c_str());
        m_wFormCreationTriggerFieldIndex = creationTriggerField.index();
    }

    for (WORD fieldId = 0; fieldId < m_wTotalFields; fieldId++)
    {
        CTaxField *pField = *(m_pFields + fieldId);
        pField->Clear();
    }

    rapidjson::Value& fieldsList = in["Fields"];
    for (auto iter = fieldsList.MemberBegin(); iter != fieldsList.MemberEnd(); iter++)
    {
        JsonFieldKey fieldKey(iter->name.GetString());

        WORD fieldId = m_pFormMgr->GetFieldID(GetID(), fieldKey.fieldName().c_str(), fieldKey.index());

        if (fieldId)
        {
            CTaxField *pField = (CTaxField *)GetField(fieldId);
            if (pField)
            {
                pField->ReadJson(iter->value);
            }
        }
    }

    return true;
}

bool CTaxForm::WriteJson(rapidjson::Writer<rapidjson::StringBuffer>& out)
{
    out.StartObject();

    DWORD status = GetStatusData();
    if (status)
    {
        out.Key("Flags");
        out.Uint(status);
    }

    if (m_wParentFormID)
    {
        char parentFormName[128] = {};
        m_pFormMgr->GetFormName(parentFormName, m_wParentFormID);

        std::string parentFormKey = JsonFormKey(parentFormName, m_wParentCopyID).str();

        out.Key("ParentForm");
        out.String(parentFormKey.c_str(), static_cast<rapidjson::SizeType>(parentFormKey.length()), true);
    }

#ifdef CALCSTATE
    if (m_wFedParentFormID)
    {
        char fedParentFormName[128] = {};
        m_pFormMgr->m_pFedFormMgr->GetFormName(fedParentFormName, m_wFedParentFormID);

        std::string fedParentFormKey = JsonFormKey(fedParentFormName, m_wParentCopyID).str();

        out.Key("FedParentForm");
        out.String(fedParentFormKey.c_str(), static_cast<rapidjson::SizeType>(fedParentFormKey.length()), true);
    }
#endif

    if (m_wFormCreationTriggerFormID)
    {
        char creationTriggerFormName[128] = {};
        m_pFormMgr->GetFormName(creationTriggerFormName, m_wFormCreationTriggerFormID);

        std::string creationTriggerFormKey = JsonFormKey(creationTriggerFormName, m_wFormCreationTriggerFormCopyID).str();

        out.Key("CreationTriggerForm");
        out.String(creationTriggerFormKey.c_str(), static_cast<rapidjson::SizeType>(creationTriggerFormKey.length()), true);
    }

    if (m_strFormCreationTriggerFieldName[0] != '\0')
    {
        std::string creationTriggerFieldKey = JsonFieldKey(m_strFormCreationTriggerFieldName, m_wFormCreationTriggerFieldIndex).str();

        out.Key("CreationTriggerField");
        out.String(creationTriggerFieldKey.c_str(), static_cast<rapidjson::SizeType>(creationTriggerFieldKey.length()), true);
    }

    out.Key("Fields");
    out.StartObject();

    for (WORD fieldId = 0; fieldId < m_wTotalFields; fieldId++)
    {
        CTaxField *pField = *(m_pFields + fieldId);
        if (pField->HasJsonData())
        {
            char fieldName[128] = {};
            m_pFormMgr->GetFieldName(fieldName, GetID(), pField->GetID());
            std::string fieldKey = JsonFieldKey(fieldName, pField->GetIndex()).str();

            out.Key(fieldKey.c_str(), static_cast<rapidjson::SizeType>(fieldKey.length()), true);
            pField->WriteJson(out);
        }
    }

    out.EndObject();

    out.EndObject();

    return true;
}

TaxFormHandle CTaxForm::handle()
{
    TaxFormHandle result;
    result.dll = m_ownerDll;
    result.self = reinterpret_cast<TaxFormInternalType*>(this);
    return result;
}
