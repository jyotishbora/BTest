// CFormManager implementation

#include "StdAfx.h"
#include "CALCINFO.H"
#include "CalcStaticData.h"
#include "Calcform.h"
#include "Calcfld.h"
#include "IAppObj.h"
#include "Calcmgr.h"
#include "CALCEXT.H"
#include "CalcVariant.h"
#include "CUSTFUNC.H"
#include "CalcResource.h"
#include "CalcSerializeUtils.h"
#include "CalcProductFlags.h"
#include "rapidjson/writer.h"
#include "VersionNo.h"
#include <algorithm>
#include <map>
#include <vector>
#include <string>
#include "TaxAct.CalcDll/DllImpl.h"

extern "C"
CALC_EXPORT ITaxFormManager* CreateFormManager(void)
{
    return new(std::nothrow) CTaxFormManager;
}

extern "C"
CALC_EXPORT BOOL IsPreviewMath(void)
{
#ifdef PREVIEW
    return TRUE;
#else
    return FALSE;
#endif
}

CTaxFormManager::CTaxFormManager()
{
    memset(m_pForms, 0, sizeof(m_pForms));

#ifdef CALCFEDERAL
    m_pStateMgr = NULL;
#endif

#ifdef CALCSTATE
    m_pFedFormMgr = NULL;
#endif

    m_pAppObj = NULL;

    m_ownerDll = TaxAct::CalcDll::CurrentModuleHandle();
}

CTaxFormManager::~CTaxFormManager()
{
    Clear();
}

BOOL CTaxFormManager::Init()
{
#ifdef CALCFEDERAL
    m_dfCore.reset(CreateDisabledFeaturesCore());
    return m_dfCore != nullptr;
#else
    m_ohioRita.reset(new Tax::OhioRita());
    return m_ohioRita->load(g_calcStaticData.ohioRitaTaxInfo);
#endif
}

void CTaxFormManager::Delete()
{
    delete this;
}

void CTaxFormManager::Clear()
{
    DeleteForms();

#ifdef CALCFEDERAL
    STATEMGR* pStateMgr, *pTemp;

    for (pStateMgr = m_pStateMgr; pStateMgr;)
    {
        pTemp = pStateMgr->pNext;
        delete pStateMgr;
        pStateMgr = pTemp;
    }

    m_pStateMgr = NULL;
#endif
}

Tax::DisabledFeaturesCore* CTaxFormManager::GetDisabledFeaturesCore()
{
    return m_dfCore.get();
}

Tax::OhioRita* CTaxFormManager::GetOhioRita()
{
    return m_ohioRita.get();
}

void CTaxFormManager::SetLogCallback(TaxFormManagerLogCallback fn, void *userData)
{
    m_logCallback = fn;
    m_logCallbackUserData = userData;
}

bool CTaxFormManager::WriteLog(const char *msg)
{
    if (m_logCallback)
    {
        auto tempHandle = handle();
        m_logCallback(m_logCallbackUserData, &tempHandle, msg);
        return true;
    }

    return false;
}

BOOL CTaxFormManager::InitForms()
{
    Clear();

    // create required forms here
    for (size_t wFormID = 1; wFormID <= FORM_TOTALFORMS; wFormID++)
    {
        if (GetStatus(static_cast<WORD>(wFormID), FORMSTATUS_REQUIRED) && !CreateForm(static_cast<WORD>(wFormID)))
        {
            DeleteForms();
            return FALSE;
        }
    }

    return TRUE;
}

void CTaxFormManager::DeleteForms()
{
    FORMSCONTAINER* pForms;

    for (size_t wFormID = 1; wFormID <= FORM_TOTALFORMS; wFormID++)
    {
        pForms = m_pForms[wFormID - 1];

        if (pForms == NULL)
        {
            continue;
        }

        for (size_t w = 0; w < pForms->size(); w++)
        {
            delete(*pForms)[w];
        }

        pForms->clear();
        delete pForms;
    }

    memset(m_pForms, 0, sizeof(m_pForms));
}

WORD CTaxFormManager::GetFormID(LPCSTR szForm)
{
    return GetCachedFormID(szForm);
}

WORD CTaxFormManager::GetFieldID(WORD wFormID, LPCSTR szField, int iIndex)
{
    return GetCachedFieldID(wFormID, szField, static_cast<WORD>(iIndex));
}

WORD CTaxFormManager::GetFieldType(WORD wFormID, WORD wFieldID)
{
    return g_calcStaticData.forms[wFormID - 1].fields[wFieldID - 1].type;
}

ITaxForm* CTaxFormManager::CreateForm(WORD wFormID, BOOL bCalculate /* = TRUE */, ITaxForm* pParent /* = NULL */)
{
    ASSERT(wFormID > 0);

    if (wFormID == 0)
    {
        return NULL;
    }

    if (!HasProductFlag(PRODUCTFLAG_ISEFILE) && !HasMoreCopies(wFormID))
    {
        ASSERT(GetTotalCopies(wFormID) < GetMaxCopies(wFormID));
        return NULL;
    }

    CTaxForm* pNew;
    if (!(pNew = new(std::nothrow) CTaxForm))
    {
        return NULL;
    }

    FORMSCONTAINER* pForms = m_pForms[wFormID - 1];

    WORD wCopyID(1);
    if (pForms == NULL)
    {
        pForms = new(std::nothrow) FORMSCONTAINER;

        if (pForms == NULL)
        {
            return NULL;
        }

        m_pForms[wFormID - 1] = pForms;
    }
    else
    {
        CTaxForm* pTempForm(NULL);

        for (size_t i = 0; i < pForms->size(); i++)
        {
            pTempForm = (*pForms)[i];

            if (pTempForm && (pTempForm->m_wCopyID >= wCopyID))
            {
                wCopyID = pTempForm->m_wCopyID + 1;
            }
        }
    }

    pForms->push_back(pNew);
    pNew->m_wCopyID = wCopyID;

    if (!pNew->Init(wFormID, this))
    {
        pForms->pop_back();

        if (pForms->empty())
        {
            delete pForms;
            m_pForms[wFormID - 1] = NULL;
        }

        delete pNew;
        return NULL;
    }

    if (pParent)
    {
        pNew->SetParent(pParent, FALSE);
    }

    if (bCalculate)
    {
        pNew->CalculateAllFields();
        pNew->Update();
    }

#ifdef CALCFEDERAL
    for (STATEMGR* pStateMgr = m_pStateMgr; pStateMgr; pStateMgr = pStateMgr->pNext)
    {
        pStateMgr->pFormMgr->AttachExternalForm(pNew);
    }

#endif
#ifdef CALCSTATE
    m_pFedFormMgr->AttachExternalForm(pNew);
#endif
    if (bCalculate)
    {
        pNew->ExternalUpdate();

        CTaxField* pField;
        for (size_t wFieldID = 1; wFieldID <= pNew->m_wTotalFields; wFieldID++)
        {
            pField = pNew->GetCalcField(static_cast<WORD>(wFieldID));
            pField->ExternalUpdate();
        }
    }

    return pNew;
}

void CTaxFormManager::DeleteForm(ITaxForm* pForm, BOOL bSuspendCalculations /*= FALSE*/)
{
    if (!pForm)
    {
        return;
    }

    WORD wFormID = ((CTaxForm*)pForm)->m_wID;
    FORMSCONTAINER* pForms = m_pForms[wFormID - 1];

    if (pForms != NULL)
    {
        FORMSITERATOR it = std::find(pForms->begin(), pForms->end(), pForm);

        if (it != pForms->end())
        {
            delete *it;
            pForms->erase(it);

            if (pForms->empty())
            {
                delete pForms;
                m_pForms[wFormID - 1] = NULL;
            }
        }
    }

    if (!bSuspendCalculations)
    {
        UpdateDeletedChildForms();
        UpdateDeletedForm(wFormID);
#ifdef CALCFEDERAL
        for (STATEMGR* pStateMgr = m_pStateMgr; pStateMgr; pStateMgr = pStateMgr->pNext)
        {
            pStateMgr->pFormMgr->UpdateDeletedChildForms();
        }

#endif
        UpdateCreators(wFormID);
    }
}

void CTaxFormManager::UpdateDeletedChildForms()
{
    for (size_t i = 0; i < m_DeletedChildFormIds.size(); i++)
    {
        UpdateDeletedForm(m_DeletedChildFormIds[i]);
    }

    m_DeletedChildFormIds.clear();
}

void CTaxFormManager::UpdateDeletedForm(WORD wFormID)
{
    //bpj: added deleteform dependencies 7/13/2011
    //used to do CalculateAllForms on each module
    (FormDeleteFunc[wFormID - 1])(this);

    char szName[64];
    GetFormName(szName, wFormID);

#ifdef CALCFEDERAL
    for (STATEMGR* pStateMgr = m_pStateMgr; pStateMgr; pStateMgr = pStateMgr->pNext)
    {
        pStateMgr->pFormMgr->UpdateExternalDeletedForm(szName, wFormID);
    }
#endif

#ifdef CALCSTATE
    m_pFedFormMgr->UpdateExternalDeletedForm(szName, wFormID);
#endif
}

ITaxForm* CTaxFormManager::GetForm(WORD wFormID, WORD wCopyID)
{
    ASSERT(wFormID > 0);
    ASSERT(wCopyID > 0);

    if ((wFormID == 0) || (wCopyID == 0))
    {
        return NULL;
    }

    const FORMSCONTAINER* pForms = m_pForms[wFormID - 1];

    if (pForms != NULL)
    {
        for (size_t w = 0; w < pForms->size(); w++)
        {
            if (((*pForms)[w])->m_wCopyID == wCopyID)
            {
                return (*pForms)[w];
            }
        }
    }

    return NULL;
}

ITaxForm* CTaxFormManager::GetFormByIndex(WORD wFormID, WORD wCopyIndex)
{
    if ((wFormID > 0) && (wCopyIndex > 0) && (m_pForms[wFormID - 1] != NULL) && ((m_pForms[wFormID - 1])->size() >= wCopyIndex))
    {
        return (*(m_pForms[wFormID - 1]))[wCopyIndex - 1];
    }

    return NULL;
}

WORD CTaxFormManager::GetTotalCopies(WORD wFormID)
{
    ASSERT(wFormID > 0);

    if (wFormID == 0)
    {
        return 0;
    }

    if (m_pForms[wFormID - 1] != NULL)
    {
        return static_cast<WORD>(m_pForms[wFormID - 1]->size());
    }

    return 0;
}

WORD CTaxFormManager::GetMaxCopies(WORD wFormID)
{
    ASSERT(wFormID > 0);

    if (wFormID == 0)
    {
        return 0;
    }

    WORD wMaxCopies;
    if ((wMaxCopies = g_calcStaticData.forms[wFormID - 1].maxCopies) == 0)
    {
        wMaxCopies = 1;
    }

    return wMaxCopies;
}

WORD CTaxFormManager::GetTotalFields(WORD wFormID)
{
    return ::GetTotalFields(wFormID);
}

BOOL CTaxFormManager::GetStatus(WORD wFormID, DWORD dwStatus)
{
    return ::GetStatus(wFormID, dwStatus);
}

WORD CTaxFormManager::GetTotalForms()
{
    return ::GetTotalForms();
}

BOOL CTaxFormManager::IsFederal()
{
#ifdef CALCFEDERAL
    return TRUE;
#else
    return FALSE;
#endif
}

BOOL CTaxFormManager::IsState()
{
#ifdef CALCSTATE
    return TRUE;
#else
    return FALSE;
#endif
}

BOOL CTaxFormManager::isReturnFormPrintDisabled(const char* returnFormName)
{
    return m_dfCore->isReturnFormPrintDisabled(returnFormName);
}

void CTaxFormManager::GetModuleName(LPSTR szName)
{
    ::GetModuleName(szName);
}

void CTaxFormManager::GetModuleDateTime(LPSTR szDateTime)
{
    ::GetModuleDateTime(szDateTime);
}

void CTaxFormManager::GetModuleTitle(LPSTR szTitle)
{
    ::GetModuleTitle(szTitle);
}

void CTaxFormManager::GetFormName(LPSTR szName, WORD wFormID)
{
    ::GetFormName(szName, wFormID);
}

void CTaxFormManager::GetFieldName(LPSTR szName, WORD wFormID, WORD wFieldID)
{
    ::GetFieldName(szName, wFormID, wFieldID);
}

void CTaxFormManager::GetShortFormName(LPSTR szName, WORD wFormID)
{
    *szName = '\0';

    char bufName[128] = {};
    ::GetShortFormName(bufName, wFormID);

    if (strstr(bufName, "#") != nullptr)
    {
        int nParam(0);

        ITaxField *formShortDescField = nullptr;

        if (IsFederal())
        {
            formShortDescField = GetCustomField("FederalFormShortDesc");
        }
        else
        {
            formShortDescField = GetCustomField("StateFormShortDesc");
        }

        if (formShortDescField)
        {
            nParam = formShortDescField->GetNumber();
        }

        CTaxString actualName = GetParam(bufName, nParam + 1, "#");

        if (actualName.IsEmpty())
        {
            actualName = GetParam(bufName, 1, "#");
        }
        strcpy_s(szName, std::char_traits<char>::length(actualName) + 1, actualName);
    }
    else
    {
        strcpy_s(szName, std::char_traits<char>::length(bufName) + 1, bufName);
    }
}

void CTaxFormManager::GetLongFormName(LPSTR szName, WORD wFormID)
{
    ::GetLongFormName(szName, wFormID);
}

void CTaxFormManager::GetTabName(LPSTR szName, WORD wFormID)
{
    ::GetTabName(szName, wFormID);
}

WORD CTaxFormManager::GetFormListOrder(WORD wFormID, DWORD dwListStatus)
{
    return ::GetFormListOrder(wFormID, dwListStatus);
}

void CTaxFormManager::CalculateAllForms()
{
    const FORMSCONTAINER* pForms;

    for (size_t wFormID = 1; wFormID <= FORM_TOTALFORMS; wFormID++)
    {
        pForms = m_pForms[wFormID - 1];

        if (pForms != NULL)
        {
            for (size_t w = 0; w < pForms->size(); w++)
            {
                ((*pForms)[w])->CalculateAllFields();
            }
        }
    }
}

WORD CTaxFormManager::GetTotalSpawnForms(WORD wFormID, WORD wFieldID)
{
    WORD wTotal = 0;

    for (const auto& spawnInfo : g_calcStaticData.forms[wFormID - 1].spawnInfos)
    {
        if (spawnInfo.fieldID == wFieldID)
        {
            wTotal++;
        }
    }

    return wTotal;
}

void CTaxFormManager::GetSpawnForm(SPAWNINFO* pSpawn, WORD wFormID, WORD wFieldID, WORD wIndex)
{
    *pSpawn = SPAWNINFO();

    WORD wTotal = 0;

    for (const auto& spawnInfo : g_calcStaticData.forms[wFormID - 1].spawnInfos)
    {
        if (spawnInfo.fieldID == wFieldID)
        {
            wTotal++;
        }

        if (wTotal == wIndex)
        {
            pSpawn->wFieldID = spawnInfo.fieldID;
            pSpawn->wToFormID = spawnInfo.toFormID;
            pSpawn->wToCopyID = spawnInfo.toCopyID;
            pSpawn->wToFieldID = spawnInfo.toFieldID;
            pSpawn->wToChild = spawnInfo.toChild;
            pSpawn->wIsFed = spawnInfo.isFed;
            break;
        }
    }
}

CTaxForm* CTaxFormManager::GetCalcForm(WORD wFormID, WORD wCopyIndex)
{
    return (CTaxForm*)GetFormByIndex(wFormID, wCopyIndex);
}

ITaxField* CTaxFormManager::GetCustomField(LPCSTR szName)
{
    for (const auto& custom : g_calcStaticData.customFields)
    {
        if (_stricmp(custom.name.c_str(), szName) == 0)
        {
            ITaxForm* pForm;
            ITaxField* pField;
            if ((pForm = GetForm(custom.formID, 1)) && (pField = pForm->GetField(custom.fieldID)))
            {
                return pField;
            }
        }
    }

    return NULL;
}

ITaxField* CTaxFormManager::GetCustomFieldByIndex(LPCSTR szName, WORD wCopyIndex)
{
    for (const auto& custom : g_calcStaticData.customFields)
    {
        if (_stricmp(custom.name.c_str(), szName) == 0)
        {
            ITaxForm* pForm;
            ITaxField* pField;
            if ((pForm = GetFormByIndex(custom.formID, wCopyIndex)) && (pField = pForm->GetField(custom.fieldID)))
            {
                return pField;
            }
        }
    }

    return NULL;
}

void CTaxFormManager::AttachFederalFormMgr(ITaxFormManager* pFormMgr)
{
#ifdef CALCSTATE
    m_pFedFormMgr = pFormMgr;
    FORMSCONTAINER* pForms(NULL);

    for (size_t wFormID = 1; wFormID <= FORM_TOTALFORMS; wFormID++)
    {
        pForms = m_pForms[wFormID - 1];

        if (pForms != NULL)
        {
            for (size_t w = 0; w < pForms->size(); w++)
            {
                pFormMgr->AttachExternalForm((*pForms)[w]);
            }
        }
    }

#endif // CALCSTATE
}

void CTaxFormManager::AttachStateFormMgr(ITaxFormManager* pFormMgr)
{
#ifdef CALCFEDERAL
    STATEMGR* pStateMgr;

    for (pStateMgr = m_pStateMgr; pStateMgr; pStateMgr = pStateMgr->pNext)
    {
        if (pStateMgr->pFormMgr == pFormMgr)
        {
            return;
        }

        if (!pStateMgr->pNext)
        {
            break;
        }
    }

    STATEMGR* pNew;
    if (pNew = new(std::nothrow) STATEMGR)
    {
        pNew->pNext = NULL;
        pNew->pFormMgr = pFormMgr;

        if (pStateMgr)
        {
            pStateMgr->pNext = pNew;
        }
        else
        {
            m_pStateMgr = pNew;
        }
    }

    const FORMSCONTAINER* pForms;
    for (size_t wFormID = 1; wFormID <= FORM_TOTALFORMS; wFormID++)
    {
        pForms = m_pForms[wFormID - 1];

        if (pForms != NULL)
        {
            for (WORD w = 0; w < pForms->size(); w++)
            {
                pFormMgr->AttachExternalForm((*pForms)[w]);
            }
        }
    }

#endif // CALCFEDERAL
}

void CTaxFormManager::DetachStateFormMgr(ITaxFormManager* pFormMgr)
{
#ifdef CALCFEDERAL
    CTaxField* pField;
    const FORMSCONTAINER* pForms;

    for (size_t wFormID = 1; wFormID <= FORM_TOTALFORMS; wFormID++)
    {
        pForms = m_pForms[wFormID - 1];

        if (pForms == NULL)
        {
            continue;
        }

        for (size_t w = 0; w < pForms->size(); w++)
        {
            for (size_t wFieldID = 1; wFieldID <= (*pForms)[w]->m_wTotalFields; wFieldID++)
            {
                pField = (*pForms)[w]->GetCalcField(static_cast<WORD>(wFieldID));
                pField->DetachExternalUpdate(pFormMgr);
            }

            (*pForms)[w]->DetachExternalUpdate(pFormMgr);
        }
    }

    STATEMGR* pStateMgr, *pPrev;
    for (pStateMgr = m_pStateMgr, pPrev = NULL; pStateMgr;
         pPrev = pStateMgr, pStateMgr = pStateMgr->pNext)
    {
        if (pStateMgr->pFormMgr == pFormMgr)
        {
            if (pPrev)
            {
                pPrev->pNext = pStateMgr->pNext;
            }
            else
            {
                m_pStateMgr = pStateMgr->pNext;
            }

            delete pStateMgr;
            break;
        }
    }

#endif // CALCFEDERAL
}

void CTaxFormManager::AttachExternalForm(ITaxForm* pForm)
{
    AttachExtForm(this, pForm);
}

void CTaxFormManager::GetFederalDateTime(LPSTR szDateTime)
{
#ifdef CALCSTATE
    strcpy_s(szDateTime, strlen(MODULE_FED_DATETIME) + 1, MODULE_FED_DATETIME);
#else
    GetModuleDateTime(szDateTime);
#endif // CALCSTATE
}

void GetTotalChildForms(CTaxFormManager* pFormMgr, CTaxForm* pParentForm, WORD& wCount)
{
    const FORMSCONTAINER* pForms;

    for (size_t wFormID = 1; wFormID <= FORM_TOTALFORMS; wFormID++)
    {
        pForms = pFormMgr->m_pForms[wFormID - 1];

        if (pForms == NULL)
        {
            continue;
        }

        for (size_t w = 0; w < pForms->size(); w++)
        {
            if (pParentForm == (*pForms)[w]->GetParent())
            {
                wCount++;
            }
        }
    }

#ifdef CALCFEDERAL
    for (STATEMGR* pStateMgr = pFormMgr->m_pStateMgr; pStateMgr; pStateMgr = pStateMgr->pNext)
    {
        wCount += pStateMgr->pFormMgr->GetTotalChildForms(pParentForm);
    }

#endif

}

CTaxForm* GetChildForm(CTaxFormManager* pFormMgr, CTaxForm* pParentForm, WORD& wCount, WORD wChildID)
{
    const FORMSCONTAINER* pForms;

    for (size_t wFormID = 1; wFormID <= FORM_TOTALFORMS; wFormID++)
    {
        pForms = pFormMgr->m_pForms[wFormID - 1];

        if (pForms == NULL)
        {
            continue;
        }

        for (size_t w = 0; w < pForms->size(); w++)
        {
            if (pParentForm == (*pForms)[w]->GetParent())
            {
                wCount++;

                if (wCount == wChildID)
                {
                    return (*pForms)[w];
                }
            }
        }
    }

#ifdef CALCFEDERAL
    WORD wStateCount;

    for (STATEMGR* pStateMgr = pFormMgr->m_pStateMgr; pStateMgr; pStateMgr = pStateMgr->pNext)
    {
        wStateCount = pStateMgr->pFormMgr->GetTotalChildForms(pParentForm);

        if ((wCount + wStateCount) >= wChildID)
        {
            return (CTaxForm*)pStateMgr->pFormMgr->GetChildForm(pParentForm, wChildID - wCount);
        }

        wCount += wStateCount;
    }

#endif

    return NULL;
}

void DeleteChildForms(CTaxFormManager* pFormMgr, CTaxForm* pParentForm)
{
    FORMSCONTAINER* pForms;
    BOOL bFormDeleted(FALSE);

    for (size_t wFormID = 1; wFormID <= FORM_TOTALFORMS; wFormID++)
    {
        bFormDeleted = FALSE;
        pForms = pFormMgr->m_pForms[wFormID - 1];

        if (pForms == NULL)
        {
            continue;
        }

        for (FORMSITERATOR it = pForms->begin(); it < pForms->end();)
        {
            if (pParentForm == (*it)->GetParent())
            {
                ::DeleteChildForms(pFormMgr, *it);
                delete *it;
                it = pForms->erase(it);
                bFormDeleted = TRUE;
            }
            else
            {
                it++;
            }
        }

        if (pForms->empty())
        {
            delete pForms;
            pFormMgr->m_pForms[wFormID - 1] = NULL;
        }

        if (bFormDeleted)
        {
            if (std::find(pFormMgr->m_DeletedChildFormIds.begin(), pFormMgr->m_DeletedChildFormIds.end(), wFormID) == pFormMgr->m_DeletedChildFormIds.end())
            {
                pFormMgr->m_DeletedChildFormIds.push_back(static_cast<WORD>(wFormID));
            }
        }
    }

#ifdef CALCFEDERAL

    for (STATEMGR* pStateMgr = pFormMgr->m_pStateMgr; pStateMgr; pStateMgr = pStateMgr->pNext)
    {
        pStateMgr->pFormMgr->DeleteChildForms(pParentForm);
    }

#endif

}

WORD CTaxFormManager::GetTotalChildForms(ITaxForm* pParentForm)
{
    WORD wCount(0);

    ::GetTotalChildForms(this, (CTaxForm*)pParentForm, wCount);
    return wCount;
}

ITaxForm* CTaxFormManager::GetChildForm(ITaxForm* pParentForm, WORD wChildID)
{
    WORD wCount(0);

    return ::GetChildForm(this, (CTaxForm*)pParentForm, wCount, wChildID);
}

void CTaxFormManager::DeleteChildForms(ITaxForm* pParentForm)
{
    if (!pParentForm)
    {
        return;
    }

    ::DeleteChildForms(this, (CTaxForm*)pParentForm);
}

void CTaxFormManager::DeleteFormAndChildForms(ITaxForm* pParentForm, BOOL bSuspendCalculations /*= FALSE*/)
{
    if (!pParentForm)
    {
        return;
    }

    ::DeleteChildForms(this, (CTaxForm*)pParentForm);
    DeleteForm(pParentForm, bSuspendCalculations);
}

BOOL CTaxFormManager::IsChildForm(WORD wParentFormID, WORD wChildFormID)
{
    for (const auto& spawnInfo : g_calcStaticData.forms[wParentFormID - 1].spawnInfos)
    {
        if ((spawnInfo.toFormID == wChildFormID) && spawnInfo.toChild)
        {
            return TRUE;
        }
    }

    for (const auto& createInfo : g_calcStaticData.forms[wParentFormID - 1].createInfos)
    {
        if ((createInfo.createFormID == wChildFormID) && createInfo.createChild)
        {
            return TRUE;
        }
    }

    return FALSE;
}

BOOL CTaxFormManager::IsFedChildForm(WORD wFedParentFormID, WORD wChildFormID)
{
#ifdef CALCSTATE
    for (const auto& createInfo : g_calcStaticData.fedParentForms[wFedParentFormID - 1].createInfos)
    {
        if ((createInfo.createFormID == wChildFormID) && createInfo.createChild)
        {
            return TRUE;
        }
    }
#endif

    return FALSE;
}

WORD CTaxFormManager::GetMaxChildCopies(WORD wParentFormID, WORD wChildFormID)
{
    WORD wMax = 0;

    for (const auto& spawnInfo : g_calcStaticData.forms[wParentFormID - 1].spawnInfos)
    {
        if ((spawnInfo.toFormID == wChildFormID) && spawnInfo.toChild)
        {
            if ((spawnInfo.toCopyID == COPY_ALLCOPIES) ||
                (spawnInfo.toCopyID == COPY_EXISTCOPIES))
            {
                wMax = GetMaxCopies(spawnInfo.toFormID);
            }
            else
            {
                wMax = spawnInfo.toCopyID;
            }

            break;
        }
    }

    for (const auto& createInfo : g_calcStaticData.forms[wParentFormID - 1].createInfos)
    {
        if ((createInfo.createFormID == wChildFormID) && createInfo.createChild)
        {
            if (createInfo.createCopyID > wMax)
            {
                wMax = createInfo.createCopyID;
            }
        }
    }

    return wMax;
}

WORD CTaxFormManager::GetFedMaxChildCopies(WORD wFedParentFormID, WORD wChildFormID)
{
#ifdef CALCSTATE
    WORD wMax(0);

    for (const auto& createInfo: g_calcStaticData.fedParentForms[wFedParentFormID - 1].createInfos)
    {
        if ((createInfo.createFormID == wChildFormID) && createInfo.createChild)
        {
            if (createInfo.createCopyID > wMax)
            {
                wMax = createInfo.createCopyID;
            }
        }
    }

    return wMax;
#endif

    return 0;
}

WORD CTaxFormManager::GetTotalChildCopies(ITaxForm* pParentForm, WORD wChildFormID)
{
    const FORMSCONTAINER* pForms = m_pForms[wChildFormID - 1];

    if (pForms == NULL)
    {
        return 0;
    }

    WORD wCount(0);
    for (size_t w = 0; w < pForms->size(); w++)
    {
        if (pParentForm == (*pForms)[w]->GetParent())
        {
            wCount++;
        }
    }

    return wCount;
}

ITaxForm* CTaxFormManager::GetChildCopy(ITaxForm* pParentForm, WORD wChildFormID, WORD wChildID)
{
    const FORMSCONTAINER* pForms = m_pForms[wChildFormID - 1];

    if (pForms == NULL)
    {
        return NULL;
    }

    WORD wCount(0);
    for (size_t w = 0; w < pForms->size(); w++)
    {
        if (pParentForm == (*pForms)[w]->GetParent())
        {
            wCount++;

            if (wCount == wChildID)
            {
                return (*pForms)[w];
            }
        }
    }

    return NULL;
}

BOOL CTaxFormManager::HasParent(WORD wChildFormID)
{
    for (WORD wFormID = 1; wFormID <= FORM_TOTALFORMS; wFormID++)
    {
        for (const auto& spawnInfo: g_calcStaticData.forms[wFormID - 1].spawnInfos)
        {
            if ((spawnInfo.toFormID == wChildFormID) && spawnInfo.toChild)
            {
                return TRUE;
            }
        }

        for (const auto& createInfo : g_calcStaticData.forms[wFormID - 1].createInfos)
        {
            if ((createInfo.createFormID == wChildFormID) && createInfo.createChild)
            {
                return TRUE;
            }
        }
    }

    return FALSE;
}

BOOL CTaxFormManager::HasFedParent(WORD wChildFormID)
{
#ifdef CALCSTATE
    for (size_t wFormID = 1; wFormID <= FORM_FED_TOTALFORMS; wFormID++)
    {
        for (const auto& createInfo: g_calcStaticData.fedParentForms[wFormID - 1].createInfos)
        {
            if ((createInfo.createFormID == wChildFormID) && createInfo.createChild)
            {
                return TRUE;
            }
        }
    }
#endif

    return FALSE;
}

void CTaxFormManager::SaveConsent(const char *name, bool value) 
{
    m_consent[name] = value;
}

BOOL CTaxFormManager::HasConsent(LPCSTR consentName) 
{
    return  m_consent[consentName];
}

typedef BOOL FORMSBOOL[FORM_TOTALFORMS];

void GetSpawnAndCreateInfo(FORMSBOOL& bForms, WORD wTestFormID, BOOL bParent = TRUE)
{
    memset(bForms, 0, sizeof(FORMSBOOL));

    for (WORD wFormID = 1; wFormID <= FORM_TOTALFORMS; wFormID++)
    {
        if (bParent)
        {
            for (const auto& spawnInfo : g_calcStaticData.forms[wFormID - 1].spawnInfos)
            {
                if ((spawnInfo.toFormID == wTestFormID) && spawnInfo.toChild)
                {
                    bForms[wFormID - 1] = TRUE;
                    break;
                }
            }
        }

        if (bForms[wFormID - 1])
        {
            continue;
        }

        for (const auto& createInfo : g_calcStaticData.forms[wFormID - 1].createInfos)
        {
            if ((createInfo.createFormID == wTestFormID) && (!bParent || createInfo.createChild))
            {
                bForms[wFormID - 1] = TRUE;
                break;
            }
        }
    }
}

#ifdef CALCSTATE
typedef BOOL FEDFORMSBOOL[FORM_FED_TOTALFORMS];

void GetFedCreateInfo(FEDFORMSBOOL& bForms, WORD wTestFormID, BOOL bParent = TRUE)
{
    memset(bForms, 0, sizeof(bForms));

    for (size_t wFormID = 1; wFormID <= FORM_FED_TOTALFORMS; wFormID++)
    {
        for (const auto& createInfo : g_calcStaticData.fedParentForms[wFormID - 1].createInfos)
        {
            if ((createInfo.createFormID == wTestFormID) &&
                (!bParent || createInfo.createChild))
            {
                bForms[wFormID - 1] = TRUE;
                break;
            }
        }
    }
}
#endif

WORD CTaxFormManager::GetTotalParents(WORD wChildFormID)
{
    FORMSBOOL bForms;
    size_t wFormID, wCount;

    GetSpawnAndCreateInfo(bForms, wChildFormID);

    for (wFormID = 1, wCount = 0; wFormID <= FORM_TOTALFORMS; wFormID++)
    {
        if (bForms[wFormID - 1])
        {
            wCount++;
        }
    }

    return static_cast<WORD>(wCount);
}

WORD CTaxFormManager::GetParentFormID(WORD wChildFormID, WORD wIndex)
{
    FORMSBOOL bForms;
    size_t wFormID, wCount;

    GetSpawnAndCreateInfo(bForms, wChildFormID);

    for (wFormID = 1, wCount = 0; wFormID <= FORM_TOTALFORMS; wFormID++)
    {
        if (bForms[wFormID - 1])
        {
            wCount++;

            if (wCount == wIndex)
            {
                return static_cast<WORD>(wFormID);
            }
        }
    }

    return 0;
}

WORD CTaxFormManager::GetTotalFedParents(WORD wChildFormID)
{
#ifdef CALCSTATE
    FEDFORMSBOOL bForms;
    size_t wFormID, wCount;

    GetFedCreateInfo(bForms, wChildFormID);

    for (wFormID = 1, wCount = 0; wFormID <= FORM_FED_TOTALFORMS; wFormID++)
    {
        if (bForms[wFormID - 1])
        {
            wCount++;
        }
    }

    return static_cast<WORD>(wCount);
#else
    return 0;
#endif
}

WORD CTaxFormManager::GetFedParentFormID(WORD wChildFormID, WORD wIndex)
{
#ifdef CALCSTATE
    FEDFORMSBOOL bForms;
    size_t wFormID, wCount;

    GetFedCreateInfo(bForms, wChildFormID);

    for (wFormID = 1, wCount = 0; wFormID <= FORM_FED_TOTALFORMS; wFormID++)
    {
        if (bForms[wFormID - 1])
        {
            wCount++;

            if (wCount == wIndex)
            {
                return static_cast<WORD>(wFormID);
            }
        }
    }

    return static_cast<WORD>(wCount);
#else
    return 0;
#endif
}

WORD CTaxFormManager::GetTotalCreators(WORD wCreateFormID)
{
    FORMSBOOL bForms;
    size_t wFormID, wCount;

    GetSpawnAndCreateInfo(bForms, wCreateFormID, FALSE);

    for (wFormID = 1, wCount = 0; wFormID <= FORM_TOTALFORMS; wFormID++)
    {
        if (bForms[wFormID - 1])
        {
            wCount++;
        }
    }

    return static_cast<WORD>(wCount);
}

WORD CTaxFormManager::GetCreatorFormID(WORD wCreateFormID, WORD wIndex)
{
    FORMSBOOL bForms;
    size_t wFormID, wCount;

    GetSpawnAndCreateInfo(bForms, wCreateFormID, FALSE);

    for (wFormID = 1, wCount = 0; wFormID <= FORM_TOTALFORMS; wFormID++)
    {
        if (bForms[wFormID - 1])
        {
            wCount++;

            if (wCount == wIndex)
            {
                return static_cast<WORD>(wFormID);
            }
        }
    }

    return static_cast<WORD>(wCount);
}

WORD CTaxFormManager::GetTotalFedCreators(WORD wCreateFormID)
{
#ifdef CALCSTATE
    FEDFORMSBOOL bForms;
    size_t wFormID, wCount;

    GetFedCreateInfo(bForms, wCreateFormID, FALSE);

    for (wFormID = 1, wCount = 0; wFormID <= FORM_FED_TOTALFORMS; wFormID++)
    {
        if (bForms[wFormID - 1])
        {
            wCount++;
        }
    }

    return static_cast<WORD>(wCount);
#else
    return 0;
#endif
}

WORD CTaxFormManager::GetFedCreatorFormID(WORD wCreateFormID, WORD wIndex)
{
#ifdef CALCSTATE
    FEDFORMSBOOL bForms;
    size_t wFormID, wCount;

    GetFedCreateInfo(bForms, wCreateFormID, FALSE);

    for (wFormID = 1, wCount = 0; wFormID <= FORM_FED_TOTALFORMS; wFormID++)
    {
        if (bForms[wFormID - 1])
        {
            wCount++;

            if (wCount == wIndex)
            {
                return static_cast<WORD>(wFormID);
            }
        }
    }

#endif
    return 0;
}

void CTaxFormManager::UpdateCreators(WORD wCreateFormID)
{
    size_t wIndex, wTotal;
    WORD wFormID;
    const FORMSCONTAINER* pForms;

    for (wIndex = 1, wTotal = GetTotalCreators(wCreateFormID); wIndex <= wTotal; wIndex++)
    {
        wFormID = GetCreatorFormID(wCreateFormID, static_cast<WORD>(wIndex));

        if (wFormID > 0)
        {
            pForms = m_pForms[wFormID - 1];

            if (pForms == NULL)
            {
                continue;
            }

            for (size_t w = 0; w < pForms->size(); w++)
            {
                (*pForms)[w]->UpdateAllFields();
            }
        }
    }

#ifdef CALCSTATE
    ITaxForm* pForm;

    for (wIndex = 1, wTotal = GetTotalFedCreators(wCreateFormID);
         wIndex <= wTotal; wIndex++)
    {
        wFormID = GetFedCreatorFormID(wCreateFormID, static_cast<WORD>(wIndex));

        if (wFormID > 0)
        {
            for (WORD w = 1; pForm = m_pFedFormMgr->GetFormByIndex(wFormID, w); w++)
            {
                pForm->UpdateAllFields();
            }
        }
    }

#endif
}

size_t CTaxFormManager::GetModuleMapSize()
{
    char szForm[64];

    size_t iSize = sizeof(WORD);

    for (size_t wFormID = 1; wFormID <= FORM_TOTALFORMS; wFormID++)
    {
        GetFormName(szForm, static_cast<WORD>(wFormID));
        iSize += std::char_traits<char>::length(szForm) + 1;
    }

    iSize++;
    return iSize;
}

void CTaxFormManager::GetModuleMap(void *lpData)
{
    char szForm[64];

    LPSTR lpTemp = (LPSTR)lpData;
    *((LPWORD)lpTemp) = FORM_TOTALFORMS;
    lpTemp += sizeof(WORD);

    for (size_t wFormID = 1; wFormID <= FORM_TOTALFORMS; wFormID++)
    {
        GetFormName(szForm, static_cast<WORD>(wFormID));
        strcpy_s(lpTemp, std::char_traits<char>::length(szForm) + 1, szForm);
        lpTemp += std::char_traits<char>::length(szForm) + 1;
    }

    *lpTemp = '\0';
}

size_t CTaxFormManager::GetFormMapSize(WORD wFormID)
{
    char szField[64];

    size_t wTotalFields = GetTotalFields(wFormID);
    size_t iSize = (wTotalFields + 1) * sizeof(WORD);

    for (size_t wFieldID = 1; wFieldID <= wTotalFields; wFieldID++)
    {
        GetFieldName(szField, wFormID, static_cast<WORD>(wFieldID));
        iSize += std::char_traits<char>::length(szField) + 1;
    }

    iSize++;
    return iSize;
}

void CTaxFormManager::GetFormMap(void *lpData, WORD wFormID)
{
    char szField[64];

    LPSTR lpTemp = (LPSTR)lpData;
    WORD wTotalFields = GetTotalFields(wFormID);
    *((LPWORD)lpTemp) = wTotalFields;
    lpTemp += sizeof(WORD);

    for (size_t wFieldID = 1; wFieldID <= wTotalFields; wFieldID++)
    {
        *((LPWORD)lpTemp) = GetFieldType(wFormID, static_cast<WORD>(wFieldID));
        lpTemp += sizeof(WORD);
    }

    for (size_t wFieldID = 1; wFieldID <= wTotalFields; wFieldID++)
    {
        GetFieldName(szField, wFormID, static_cast<WORD>(wFieldID));
        strcpy_s(lpTemp, std::char_traits<char>::length(szField) + 1, szField);
        lpTemp += std::char_traits<char>::length(szField) + 1;
    }

    *lpTemp = '\0';
}

ITaxForm* CTaxFormManager::CreateUpdatedForm(LPCSTR szForm, const void *pModuleMap, const void *pFedModuleMap, const void *pFormMap, const void *pData)
{
    CTaxForm* pForm, *pOldForm;
    WORD wFormID, wFieldID, wOldFieldID, wIndex, wType;
    int i;
    CTaxField* pField, *pOldField;
    LPWORD pwTempType;
    LPCSTR pFormNames, pTempName, pPrevName;

    // setup map pointers
    LPCSTR pTempMap = (LPCSTR)pModuleMap;
    WORD wTotalForms = *((LPWORD)pTempMap);
    pTempMap += sizeof(WORD);
    pFormNames = pTempMap;
    pTempMap = (LPCSTR)pFormMap;
    WORD wTotalFields = *((LPWORD)pTempMap);
    pTempMap += sizeof(WORD);
    LPWORD pwTypes = (LPWORD)pTempMap;
    pTempMap += wTotalFields * sizeof(WORD);
    LPCSTR pFieldNames = pTempMap;

    for (wFormID = 1, pTempName = pFormNames; (pTempName != NULL) && (*pTempName != '\0');
         pTempName += std::char_traits<char>::length(pTempName) + 1, wFormID++)
    {
        if (_stricmp(pTempName, szForm) == 0)
        {
            break;
        }
    }

    if ((pTempName == NULL) || (*pTempName == '\0'))
    {
        return NULL;
    }

    // setup old form
    if (!(pOldForm = new(std::nothrow) CTaxForm))
    {
        return NULL;
    }

    pOldForm->m_wID = wFormID;
    pOldForm->m_wTotalFields = wTotalFields;

    if (!(pOldForm->m_pFields = new(std::nothrow) CTaxField *[wTotalFields]))
    {
        delete pOldForm;
        return NULL;
    }

    memset(pOldForm->m_pFields, 0, wTotalFields * sizeof(CTaxField*));

    for (wFieldID = 1, pwTempType = pwTypes,
         pTempName = pFieldNames, pPrevName = NULL;
         wFieldID <= wTotalFields;
         pPrevName = pTempName, pTempName += std::char_traits<char>::length(pTempName) + 1,
         pwTempType++, wFieldID++)
    {
        wType = *pwTempType;

        pField = CTaxField::Create(wType);

        if (!pField)
        {
            ASSERT(FALSE);
            delete pOldForm;
            return NULL;
        }

        pField->m_wID = wFieldID;

        if (pPrevName && (strcmp(pPrevName, pTempName) == 0))
        {
            wIndex++;
        }
        else
        {
            wIndex = 0;
        }

        pField->m_wIndex = wIndex;
        pField->m_pForm = pOldForm;
        *(pOldForm->m_pFields + (wFieldID - 1)) = pField;
    }

    pOldForm->SetData(pData);

    // setup new form
    if (!(wFormID = GetFormID(szForm)) ||
        !(pForm = (CTaxForm*)CreateForm(wFormID, FALSE)))
    {
        // form not found
        char szStr[128];
        sprintf_s(szStr, "Unable to update form %s\n", pTempName);
        WriteLog(szStr);

        delete pOldForm;
        return NULL;
    }

    pForm->m_wCopyID = pOldForm->m_wCopyID;
    pForm->m_dwStatus = (pForm->m_dwStatus & FORMSTATUS_MASK_STATIC) |
                        (pOldForm->m_dwStatus & FORMSTATUS_MASK_DYNAMIC);

    if (pOldForm->m_wParentFormID > 0)
    {
        for (wFormID = 1, pTempName = pFormNames; wFormID != pOldForm->m_wParentFormID;
             pTempName += std::char_traits<char>::length(pTempName) + 1, wFormID++);

        if (pForm->m_wParentFormID = GetFormID(pTempName))
        {
            pForm->m_wParentCopyID = pOldForm->m_wParentCopyID;
        }
    }

#ifdef CALCSTATE

    if (pOldForm->m_wFedParentFormID > 0)
    {
        pTempMap = (LPCSTR)pFedModuleMap;
        wTotalForms = *((LPWORD)pTempMap);
        pTempMap += sizeof(WORD);
        pFormNames = pTempMap;

        for (wFormID = 1, pTempName = pFormNames; wFormID != pOldForm->m_wFedParentFormID;
             pTempName += strlen(pTempName) + 1, wFormID++);

        if (pForm->m_wFedParentFormID = m_pFedFormMgr->GetFormID(pTempName))
        {
            pForm->m_wParentCopyID = pOldForm->m_wParentCopyID;
        }
    }

#endif

    for (wOldFieldID = 1, pTempName = pFieldNames; wOldFieldID <= wTotalFields;
         pTempName += std::char_traits<char>::length(pTempName) + 1, wOldFieldID++)
    {
        pOldField = pOldForm->GetCalcField(wOldFieldID);

        if (wFieldID = GetFieldID(pForm->m_wID, pTempName, pOldField->m_wIndex))
        {
            pField = pForm->GetCalcField(wFieldID);

            switch (pField->GetType())
            {
                case FLDTYPE_NUMBER:
                    pField->SetNumber(pOldField->GetNumber());
                    break;

                case FLDTYPE_CURRENCY:
                    pField->SetCurrency(pOldField->GetCurrency());
                    break;

                case FLDTYPE_FLOAT:
                    pField->SetFloat(pOldField->GetFloat());
                    break;

                case FLDTYPE_RADIO:
                case FLDTYPE_CHECK:
                    if (pOldField->GetBool())
                    {
                        if (pForm->GetRadioButtonGroup(pField->m_wID) > 0)
                        {
                            pForm->SetRadioButton(pField->m_wID, FALSE);
                        }
                        else
                        {
                            pField->SetBool(TRUE);
                        }
                    }
                    else
                    {
                        pField->SetBool(FALSE);
                    }

                    break;

                case FLDTYPE_DATE:
                    pField->SetDate(pOldField->GetDate());
                    break;

                case FLDTYPE_STRING:
                case FLDTYPE_SSN:
                case FLDTYPE_EIN:
                case FLDTYPE_PHONE:
                case FLDTYPE_OLDLIST:
                    pField->SetString(pOldField->GetString());
                    break;

                case FLDTYPE_LIST:
                case FLDTYPE_DYNALIST:
                {
                    if ((pOldField->GetType() == FLDTYPE_LIST) ||
                        (pOldField->GetType() == FLDTYPE_DYNALIST))
                    {
                        ((CTaxListFld*)pField)->CopyValueFrom((CTaxListFld*)pOldField);
                    }
                    else
                    {
                        pField->SetString(pOldField->GetString());
                    }

                    if (pField->GetType() != FLDTYPE_DYNALIST)
                    {
                        i = ((CTaxListFld*)pField)->GetListIndex();

                        if (i >= 0)
                        {
                            ((CTaxListFld*)pField)->SetListIndex(i);
                        }
                        else
                        {
                            pField->SetString("");
                        }
                    }

                    break;
                }
            }

            pField->m_dwStatus = (pField->m_dwStatus & FLDSTATUS_MASK_STATIC) |
                                 (pOldField->m_dwStatus & FLDSTATUS_MASK_DYNAMIC);
        }
        else
        {
            // field not found
            char szName[64];
            char szStr[128];

            GetFormName(szName, pForm->m_wID);
            sprintf_s(szStr, "Unable to update field for form %s field %s\n",
                      szName, pTempName);

            WriteLog(szStr);
        }
    }

    if (pOldForm->GetTriggerFormID() > 0)
    {
        WORD newTriggerFormId;

        for (wFormID = 1, pTempName = pFormNames; wFormID != pOldForm->GetTriggerFormID();
            pTempName += std::char_traits<char>::length(pTempName) + 1, wFormID++);

        if (newTriggerFormId = GetFormID(pTempName))
        {
            pForm->SetTriggerValues(newTriggerFormId, pOldForm->GetTriggerFormCopyID(), pOldForm->GetTriggerFieldName(), pOldForm->GetTriggerFieldIndex());
        }
    }

    delete pOldForm;
    return pForm;
}

void CTaxFormManager::GetFormInstructionTopic(LPSTR szTopic, WORD wFormID)
{
    auto& topic = g_calcStaticData.forms[wFormID - 1].instructionTopic;
    strcpy_s(szTopic, topic.length() + 1, topic.c_str());
}

void CTaxFormManager::GetFormTaxGuideTopic(LPSTR szTopic, WORD wFormID)
{
    auto& topic = g_calcStaticData.forms[wFormID - 1].guidanceTopic;
    strcpy_s(szTopic, topic.length() + 1, topic.c_str());
}

void CTaxFormManager::GetFormExpertTopic(LPSTR szTopic, WORD wFormID)
{
    *szTopic = '\0';
}

void CTaxFormManager::GetFormTaxTutorTopic(LPSTR szTopic, WORD wFormID)
{
    auto& topic = g_calcStaticData.forms[wFormID - 1].taxTutorTopic;
    strcpy_s(szTopic, topic.length() + 1, topic.c_str());
}

void CTaxFormManager::AttachAppObject(ITaxAppObject* pAppObj)
{
    m_pAppObj = pAppObj;
}

std::vector<PYImportFieldInfo> CTaxFormManager::GetImportInfo(const std::string& fromFormName, DWORD importFlags)
{
    std::vector<PYImportFieldInfo> result;

    for (const auto& info : g_calcStaticData.pyImports)
    {
        if (info.isStandard && ((importFlags & PYIMPORT_OLSTD) == 0))
        {
            continue;
        }

        if (info.fromFormName == fromFormName)
        {
            result.push_back(info);
        }
    }

    if ((importFlags & PYIMPORT_CASHCON_DETAILS) && (fromFormName == "USSCHA") && (GetFormID("USSCHA") > 0))
    {
        // hack alert
        // include CASH50 in the import so we can bring in details
        // see CTaxField::ImportPYJson
        PYImportFieldInfo toAdd;
        toAdd.fromFormName = "USSCHA";
        toAdd.fromFieldName = "CASH50";
        toAdd.toFormID = GetFormID("USSCHA");
        toAdd.toFieldID = GetFieldID(toAdd.toFormID, "CASH50");
        result.push_back(toAdd);
    }

    return result;
}

void CTaxFormManager::SetFieldValue(CTaxForm * newForm, CTaxField * newField, CTaxField * oldField)
{
    if (oldField && newField)
    {
        switch (newField->GetType())
        {
        case FLDTYPE_NUMBER:
            newField->SetNumber(oldField->GetNumber());
            break;

        case FLDTYPE_CURRENCY:
            newField->SetCurrency(oldField->GetCurrency());
            break;

        case FLDTYPE_FLOAT:
            newField->SetFloat(oldField->GetFloat());
            break;

        case FLDTYPE_RADIO:
        case FLDTYPE_CHECK:
            if (oldField->GetBool())
            {
                if (newForm->GetRadioButtonGroup(newField->m_wID) > 0)
                {
                    newForm->SetRadioButton(newField->m_wID, FALSE);
                }
                else
                {
                    newField->SetBool(TRUE);
                }
            }
            else
            {
                newField->SetBool(FALSE);
            }

            break;

        case FLDTYPE_DATE:
            newField->SetDate(oldField->GetDate());
            break;

        case FLDTYPE_STRING:
        case FLDTYPE_SSN:
        case FLDTYPE_EIN:
        case FLDTYPE_PHONE:
        case FLDTYPE_OLDLIST:
            newField->SetString(oldField->GetString());
            break;

        case FLDTYPE_LIST:
        case FLDTYPE_DYNALIST:
            if ((oldField->GetType() == FLDTYPE_LIST) ||
                (oldField->GetType() == FLDTYPE_DYNALIST))
            {
                ((CTaxListFld*)newField)->CopyValueFrom((CTaxListFld*)oldField);

                if (newField->GetType() != FLDTYPE_DYNALIST)
                {
                    int i = ((CTaxListFld*)newField)->GetListIndex();

                    if (i >= 0)
                    {
                        ((CTaxListFld*)newField)->SetListIndex(i);
                    }
                    else
                    {
                        newField->SetString("");
                    }
                }
            }
            else
            {
                newField->SetString(oldField->GetString());
            }

            break;
        }

        newField->SetStatus(FLDSTATUS_IMPORTED | FLDSTATUS_MODIFIED, TRUE);
        newForm->SetStatus(FORMSTATUS_IMPORTED | FORMSTATUS_MODIFIED, TRUE);
    }
}

ITaxForm* CTaxFormManager::GetPrintForm(WORD wFormID, ITaxForm* pParentForm /* = NULL */)
{
    ITaxForm* pForm;

    if (pParentForm)
    {
        if (!(pForm = GetChildCopy(pParentForm, wFormID, 1)))
        {
            pForm = CreateForm(wFormID, TRUE, pParentForm);
        }
    }
    else
    {
        if (!(pForm = GetForm(wFormID, 1)))
        {
            pForm = CreateForm(wFormID);
        }
    }

    return pForm;
}

void CTaxFormManager::DeletePrintForms()
{
    FORMSCONTAINER* pForms;

    for (size_t wFormID = 1; wFormID <= FORM_TOTALFORMS; wFormID++)
    {
        if (GetStatus(static_cast<WORD>(wFormID), FORMSTATUS_PRINT))
        {
            pForms = m_pForms[wFormID - 1];

            if (pForms == NULL)
            {
                continue;
            }

            for (WORD w = 0; w < pForms->size(); w++)
            {
                delete(*pForms)[w];
            }

            pForms->clear();
            delete pForms;
            m_pForms[wFormID - 1] = NULL;
        }
    }
}

BOOL CTaxFormManager::HasMoreCopies(WORD wFormID)
{
    return (GetStatus(wFormID, FORMSTATUS_PRINT) ||
            HasParent(wFormID) ||
            HasFedParent(wFormID) ||
            (GetTotalCopies(wFormID) < GetMaxCopies(wFormID)));
}

void CTaxFormManager::GetFormNewScript(LPSTR szScript, WORD wFormID)
{
    auto& script = g_calcStaticData.forms[wFormID - 1].newScript;
    strcpy_s(szScript, script.length() + 1, script.c_str());
}

void CTaxFormManager::GetFormReviewScript(LPSTR szScript, WORD wFormID)
{
    auto& script = g_calcStaticData.forms[wFormID - 1].reviewScript;
    strcpy_s(szScript, script.length() + 1, script.c_str());
}

void CTaxFormManager::GetFieldInstructionTopic(LPSTR szTopic, WORD wFormID, WORD wFieldID)
{
    auto& topic = g_calcStaticData.forms[wFormID - 1].fields[wFieldID - 1].instructionTopic;
    strcpy_s(szTopic, topic.length() + 1, topic.c_str());
}

void CTaxFormManager::GetFieldDescription(LPSTR szDescription, WORD wFormID, WORD wFieldID)
{
    auto& desc = g_calcStaticData.forms[wFormID - 1].fields[wFieldID - 1].description;
    strcpy_s(szDescription, desc.length() + 1, desc.c_str());
}

void CTaxFormManager::UpdateAppFormsTree(ITaxForm* pForm)
{
    if (m_pAppObj)
    {
        m_pAppObj->UpdateFormsTree(pForm);
    }
}

ITaxFormManager* CTaxFormManager::GetFedFormManager()
{
#ifdef CALCSTATE
    return m_pFedFormMgr;
#else
    return nullptr;
#endif
}

ITaxFormManager* CTaxFormManager::GetStateFormManager(LPCSTR szModName)
{
#ifdef CALCFEDERAL
    STATEMGR* mgr(m_pStateMgr);
    char szName[32];

    while (mgr)
    {
        mgr->pFormMgr->GetModuleName(szName);

        if (strcmp(szName, szModName) == 0)
        {
            return mgr->pFormMgr;
        }

        mgr = mgr->pNext;
    }

#endif
    return NULL;
}

ITaxForm* CTaxFormManager::GetStateFormByIndex(LPCSTR szForm, WORD wCopyIndex)
{
#ifdef CALCFEDERAL
    char cAbbr[3];
    strncpy_s(cAbbr, szForm, 2);
    ITaxFormManager* pStateMgr(GetStateFormManager(cAbbr));

    if (pStateMgr)
    {
        WORD wFormID(pStateMgr->GetFormID(szForm));

        if (wFormID)
        {
            return pStateMgr->GetFormByIndex(wFormID, wCopyIndex);
        }
    }

#endif
    return NULL;
}

void CTaxFormManager::UpdateExternalDeletedForm(LPCSTR szName, WORD wFormID)
{
    UpdateExtDeletedForm(this, szName, wFormID);
}

bool CTaxFormManager::PrintList_Exists(unsigned int listID) const
{
    return (listID <= PRINTLIST_COUNT && listID > 0);
}

void CTaxFormManager::PrintList_Clear(unsigned int listID)
{
    ASSERT(PrintList_Exists(listID));
    if (PrintList_Exists(listID))
    {
        m_printLists[listID-1].clear();
    }
}

void CTaxFormManager::PrintList_Add(unsigned int listID, const PrintListItem& toAdd)
{
    ASSERT(PrintList_Exists(listID));
    if (PrintList_Exists(listID))
    {
        m_printLists[listID-1].push_back(toAdd);
    }
}

size_t CTaxFormManager::PrintList_Size(unsigned int listID) const
{
    ASSERT(PrintList_Exists(listID));
    if (PrintList_Exists(listID))
    {
        return m_printLists[listID-1].size();
    }
    else
    {
        return 0;
    }
}

const PrintListItem *CTaxFormManager::PrintList_At(unsigned int listID, size_t index) const
{
    ASSERT(PrintList_Exists(listID));
    if (PrintList_Exists(listID))
    {
        return &m_printLists[listID-1].at(index);
    }
    else
    {
        return nullptr;
    }
}

WORD CTaxFormManager::GetPicklistId(LPCSTR szName)
{
    if (szName == NULL)
    {
        return 0;
    }

    size_t nPicklists = g_calcStaticData.picklists.size();

    for (WORD i = 1; i <= nPicklists; i++)
    {
        if (_stricmp(g_calcStaticData.picklists[i - 1].name.c_str(), szName) == 0)
        {
            return i;
        }
    }

    return 0;
}

size_t CTaxFormManager::GetPicklistDataSize(WORD id)
{
    if (id > 0 && id <= g_calcStaticData.picklists.size())
    {
        XStream::xstream xs;
        xs << g_calcStaticData.picklists[id - 1];
        return xs.size();
    }

    return 0;
}

void CTaxFormManager::GetPicklistData(WORD id, void *pData)
{
    if (id > 0 && id <= g_calcStaticData.picklists.size())
    {
        XStream::xstream xs;
        xs << g_calcStaticData.picklists[id - 1];
        memcpy_s(pData, xs.size(), xs.data(), xs.size());
    }
}

void CTaxFormManager::CallCustomCalc(LPCSTR funcName, int nParameters, CalcVariant *result, CalcVariant *params)
{
    *result = ::CallCustomCalc(this, funcName, nParameters, params);
}

bool CTaxFormManager::ReadJson(const char *in)
{
    rapidjson::Document document;
    document.Parse(in);
    return ReadJson(document);
}

bool CTaxFormManager::ImportPYJson(const char *in, DWORD importFlags)
{
    rapidjson::Document document;
    document.Parse(in);
    return ImportPYJson(document, importFlags);
}

bool CTaxFormManager::WriteJson(DllStringBuffer *out)
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

void CTaxFormManager::ClearProductFlags()
{
    m_productFlags.clear();
}

void CTaxFormManager::AddProductFlag(const char *str)
{
    Tax::xstring upperFlag = str;
    upperFlag.MakeUpper();

    m_productFlags.insert(upperFlag);
}

void CTaxFormManager::RemoveProductFlag(const char *str)
{
    Tax::xstring upperFlag = str;
    upperFlag.MakeUpper();

    m_productFlags.erase(upperFlag);
}

bool CTaxFormManager::HasProductFlag(const char *str) const
{
    Tax::xstring upperFlag = str;
    upperFlag.MakeUpper();

    return m_productFlags.count(upperFlag) > 0;
}

void CTaxFormManager::ClearPricingInfo()
{
    m_pricingInfo.clear();
}

void CTaxFormManager::SetPricingInfo(const char *str, TAXCURRENCY amt)
{
    Tax::xstring key = str;
    key.MakeUpper();

    m_pricingInfo[key] = amt;
}

TAXCURRENCY CTaxFormManager::GetPricingInfo(const char *str) const
{
    Tax::xstring key = str;
    key.MakeUpper();

    auto find = m_pricingInfo.find(key);
    if (find != m_pricingInfo.end())
    {
        return find->second;
    }

    return 0;
}

void CTaxFormManager::OnUpdatePricingInfo(OnUpdatePricingInfoCallback fn, void *userData)
{
    m_updatePricingInfoCallback = fn;
    m_updatePricingInfoCallbackUserData = userData;
}

void CTaxFormManager::UpdatePricingInfo(const char *price)
{
    if (m_updatePricingInfoCallback)
    {
        m_updatePricingInfoCallback(m_updatePricingInfoCallbackUserData, this, price);
    }
}

bool CTaxFormManager::ReadJson(rapidjson::Value& in)
{
    const char *version = in["Version"].GetString();
    const char *datetime = in["DateTime"].GetString();

    rapidjson::Value& formsList = in["Forms"];

    std::map<JsonFormKey, const char *> sortedFormKeys; // make sure we create forms in the correct order
    for (auto iter = formsList.MemberBegin(); iter != formsList.MemberEnd(); iter++)
    {
        sortedFormKeys.insert(sortedFormKeys.end(), std::make_pair(JsonFormKey(iter->name.GetString()), iter->name.GetString()));
    }

    for (auto iter: sortedFormKeys)
    {
        WORD formId = GetFormID(iter.first.formName().c_str());
        if (formId)
        {
            CTaxForm *pForm = (CTaxForm *)CreateForm(formId, FALSE);
            if (pForm)
            {
                pForm->m_wCopyID = iter.first.copyId();
                pForm->ReadJson(formsList[iter.second]);
            }
        }
    }

    // create additional required forms
    WORD totalForms = GetTotalForms();
    for (WORD formId = 1; formId <= totalForms; formId++)
    {
        if ((GetStatus(formId, FORMSTATUS_REQUIRED) != 0) && (GetTotalCopies(formId) == 0))
        {
            if (!CreateForm(formId, 0))
            {
                return false;
            }
        }
    }

    
    auto printListsObj = in.FindMember("printLists");
    if (printListsObj != in.MemberEnd())
    {
        int i(0);
        for (auto printLists = printListsObj->value.Begin(); printLists != printListsObj->value.End(); printLists++, i++)
        {
            if (i < PRINTLIST_COUNT)
            {
                m_printLists[i].clear();

                for (auto printListItems = printLists->Begin(); printListItems != printLists->End(); printListItems++)
                {
                    PrintListItem item;

                    auto id = printListItems->FindMember("id");
                    if (id != printListItems->MemberEnd())
                        item.m_id = id->value.GetString();

                    auto sublist = printListItems->FindMember("sublist");
                    if (sublist != printListItems->MemberEnd())
                        item.m_sublist = sublist->value.GetUint();

                    auto title = printListItems->FindMember("title");
                    if (title != printListItems->MemberEnd())
                        item.m_title = title->value.GetString();

                    auto type = printListItems->FindMember("type");
                    if (type != printListItems->MemberEnd())
                        item.m_type = (PrintListItem::Type) type->value.GetInt();

                    m_printLists[i].push_back(item);
                }
            }
        }
    }
    

    return true;
}

bool CTaxFormManager::ImportPYJson(rapidjson::Value& in, DWORD importFlags)
{
    const char *version = in["Version"].GetString();
    const char *datetime = in["DateTime"].GetString();

    rapidjson::Value& formsList = in["Forms"];

    std::map<JsonFormKey, const char *> sortedFormKeys; // make sure we create forms in the correct order
    for (auto iter = formsList.MemberBegin(); iter != formsList.MemberEnd(); iter++)
    {
        sortedFormKeys.insert(sortedFormKeys.end(), std::make_pair(JsonFormKey(iter->name.GetString()), iter->name.GetString()));
    }

    for (auto formKey : sortedFormKeys)
    {
        auto importInfoList = GetImportInfo(formKey.first.formName(), importFlags);
        if (importInfoList.empty())
        {
            continue;
        }

        rapidjson::Value& formData = formsList[formKey.second];

        std::unique_ptr<JsonFormKey> parentForm;

        auto findParentForm = formData.FindMember("ParentForm");
        if (findParentForm != formData.MemberEnd())
        {
            parentForm.reset(new JsonFormKey(findParentForm->value.GetString()));
        }

        rapidjson::Value& fieldsList = formData["Fields"];
        for (auto iterField = fieldsList.MemberBegin(); iterField != fieldsList.MemberEnd(); iterField++)
        {
            JsonFieldKey fieldKey(iterField->name.GetString());

            for (const auto& importInfo : importInfoList)
            {
                if (importInfo.fromFieldName != fieldKey.fieldName())
                {
                    continue;
                }

                bool fieldIsEmpty = true;

                auto findValue = iterField->value.FindMember("Value");
                if (findValue != iterField->value.MemberEnd())
                {
                    if (findValue->value.IsBool())
                    {
                        fieldIsEmpty = findValue->value.IsFalse();
                    }
                    else if (findValue->value.IsInt())
                    {
                        fieldIsEmpty = (findValue->value.GetInt() == 0);
                    }
                    else if (findValue->value.IsInt64())
                    {
                        fieldIsEmpty = (findValue->value.GetInt64() == 0);
                    }
                    else if (findValue->value.IsDouble())
                    {
                        fieldIsEmpty = (findValue->value.GetDouble() == 0.0);
                    }
                    else if (findValue->value.IsString())
                    {
                        fieldIsEmpty = (findValue->value.GetStringLength() == 0);
                    }
                }

                bool importToSameForm = false;

                char szFormName[128] = {};
                GetFormName(szFormName, importInfo.toFormID);

                if (formKey.first.formName() == szFormName)
                {
                    importToSameForm = true;
                }

                // find or create the form we're importing this data into
                CTaxForm *targetForm = nullptr;

                if (importToSameForm)
                {
                    targetForm = (CTaxForm*)GetForm(importInfo.toFormID, formKey.first.copyId());
                }
                else
                {
                    targetForm = (CTaxForm*)GetForm(importInfo.toFormID, 1);
                }

                if (!targetForm && !fieldIsEmpty)
                {
                    // break if no more copies are available
                    if (HasMoreCopies(importInfo.toFormID))
                    {
                        targetForm = (CTaxForm*)CreateForm(importInfo.toFormID, FALSE);
                    }
                }

                // set up parent form relationship
                if (targetForm && importToSameForm)
                {
                    targetForm->m_wCopyID = formKey.first.copyId();

                    if (parentForm && (targetForm->m_wParentFormID == 0))
                    {
                        targetForm->m_wParentFormID = GetFormID(parentForm->formName().c_str());
                        if (targetForm->m_wParentFormID)
                        {
                            targetForm->m_wParentCopyID = parentForm->copyId();

                            CTaxForm *targetParentForm = (CTaxForm*)GetForm(targetForm->m_wParentFormID, targetForm->m_wParentCopyID);
                            if (!targetParentForm)
                            {
                                targetParentForm = (CTaxForm*)CreateForm(targetForm->m_wParentFormID, FALSE);
                            }

                            if (!targetParentForm)
                            {
                                DeleteForm(targetForm);
                                continue;
                            }

                            targetParentForm->m_wCopyID = targetForm->m_wParentCopyID;
                        }
                    }
                }

                if (targetForm)
                {
                    // import the field data
                    CTaxField *targetField = targetForm->GetCalcField(importInfo.toFieldID + fieldKey.index());
                    if (targetField)
                    {
                        targetField->ImportPYJson(iterField->value, importFlags);
                        targetField->SetStatus(FLDSTATUS_IMPORTED | FLDSTATUS_MODIFIED, TRUE);
                        targetForm->SetStatus(FORMSTATUS_IMPORTED | FORMSTATUS_MODIFIED, TRUE);
                    }
                    else
                    {
                        // field not found
                        char szStr[128] = {};
                        sprintf_s(szStr, "Unable to import field for form %s field %s\n", formKey.first.formName().c_str(), fieldKey.fieldName().c_str());
                        WriteLog(szStr);
                    }
                }
            }
        }
    }

    return true;
}

bool CTaxFormManager::WriteJson(rapidjson::Writer<rapidjson::StringBuffer>& out)
{
    out.StartObject();

    out.Key("Version");
    out.String(VERSION_NO_STR);

    out.Key("DateTime");
    out.String(MODULE_DATETIME);

    out.Key("Forms");
    out.StartObject();

    WORD totalForms = GetTotalForms();
    for (WORD formId = 1; formId <= totalForms; formId++)
    {
        WORD totalCopies = GetTotalCopies(formId);
        for (WORD copyIndex = 1; copyIndex <= totalCopies; copyIndex++)
        {
            CTaxForm *pForm = (CTaxForm *)GetFormByIndex(formId, copyIndex);

            if (pForm)
            {
                char formName[128] = {};
                pForm->GetName(formName);
                std::string strFormKey = JsonFormKey(formName, pForm->GetCopyID()).str();

                out.Key(strFormKey.c_str(), static_cast<rapidjson::SizeType>(strFormKey.length()), true);
                pForm->WriteJson(out);
            }
        }
    }

    out.EndObject();

    out.Key("printLists");
    out.StartArray();
    for (unsigned int i(0); i < PRINTLIST_COUNT; i++)
    {
        out.StartArray();
        for (size_t x(0); x < m_printLists[i].size(); x++)
        {
            out.StartObject();
            out.Key("id");
            out.String(m_printLists[i][x].m_id);
            
            out.Key("sublist");
            out.Uint(m_printLists[i][x].m_sublist);

            out.Key("title");
            out.String(m_printLists[i][x].m_title);

            out.Key("type");
            out.Int(m_printLists[i][x].m_type);

            out.EndObject();
        }
        out.EndArray();
    }
    out.EndArray();

    out.EndObject();

    return true;
}

void CTaxFormManager::getMathGlobalConstList(DllStringBuffer& out)
{
    getGlobalConstList(out);
}

TaxFormManagerHandle CTaxFormManager::handle()
{
    TaxFormManagerHandle result;
    result.dll = m_ownerDll;
    result.self = reinterpret_cast<TaxFormManagerInternalType*>(this);
    return result;
}
