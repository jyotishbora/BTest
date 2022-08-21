// CTaxField Implementation

#include "StdAfx.h"
#include "IAppObj.h"
#include "Calcmgr.h"
#include "Calcfld.h"
#include "CalcProductFlags.h"
#include "xstring.h"
#include "Misc_CommonCurrency.h"
#include "TaxAct.CalcDll/DllImpl.h"

void HandleMathException(ITaxField *field, std::runtime_error& e)
{
    char szForm[16];
    char szField[16];
    char szMsg[256];

    field->GetForm()->GetFormManager()->GetFormName(szForm, field->GetForm()->GetID());
    field->GetForm()->GetFormManager()->GetFieldName(szField, field->GetForm()->GetID(), field->GetID());
    sprintf_s(szMsg, "An exception has occurred calculating form %s field %s. what() = %s",
                szForm, szField, e.what());

    field->GetForm()->GetFormManager()->WriteLog(szMsg);
}

void HandleMathException(ITaxField *field)
{
    char szForm[16];
    char szField[16];
    char szMsg[256];

    field->GetForm()->GetFormManager()->GetFormName(szForm, field->GetForm()->GetID());
    field->GetForm()->GetFormManager()->GetFieldName(szField, field->GetForm()->GetID(), field->GetID());
    sprintf_s(szMsg, "A math exception has occurred calculating form %s field %s.",
                szForm, szField);

    field->GetForm()->GetFormManager()->WriteLog(szMsg);
}

CTaxString FormatCurrency(TAXCURRENCY value)
{
    char szNumber[64];

    if (value >= 0)
    {
        sprintf_s(szNumber, "$%lli.%02lli", value / 100, value % 100);
    }
    else
    {
        sprintf_s(szNumber, "-$%lli.%02lli", (value * -1) / 100, (value * -1) % 100);
    }

    return szNumber;
}

TAXCURRENCY ParseCurrency(const char *str)
{
    if (strchr(str, '$'))
    {
        std::string numberStr;

        bool inFracPart = false;
        int fracDigits = 0;
        for (const char *pStr = str; *pStr; pStr++)
        {
            if (isdigit(*pStr) || (*pStr == '-'))
            {
                if (inFracPart)
                {
                    numberStr += *pStr;
                    fracDigits++;

                    if (fracDigits >= 2)
                    {
                        break;
                    }
                }
                else
                {
                    numberStr += *pStr;
                }
            }
            else if (*pStr == '.')
            {
                inFracPart = true;
            }
        }

        while (fracDigits < 2)
        {
            numberStr += '0';
            fracDigits++;
        }

        return std::strtoll(numberStr.c_str(), nullptr, 10);
    }
    else
    {
        return std::strtoll(str, nullptr, 10);
    }
}

void SetAsciiStr(CTaxString& dest, const char *source)
{
    // optimize assuming we don't have any non-ascii characters
    size_t asciiLen = 0;
    bool hasNonAscii = false;

    const char *c = source;
    while (*c)
    {
        if (__isascii(*c))
        {
            asciiLen++;
        }
        else
        {
            hasNonAscii = true;
        }

        c++;
    }

    if (hasNonAscii)
    {
        std::string buf;
        buf.reserve(asciiLen);

        const char *c = source;
        while (*c)
        {
            if (__isascii(*c))
            {
                buf.push_back(*c);
            }

            c++;
        }

        dest = buf.c_str();
    }
    else
    {
        dest = source;
    }
}

CTaxField::CTaxField()
{
    m_wID = 0;
    m_wIndex = 0;
    m_wType = 0;
    m_dwStatus = 0;
    m_pForm = NULL;
    m_pfnUpdate = NULL;
    m_pUpdate = NULL;
    m_ownerDll = TaxAct::CalcDll::CurrentModuleHandle();
}

CTaxField::~CTaxField()
{
    UPDATEOBJ* pUpdate, *pTemp;

    for (pUpdate = m_pUpdate; pUpdate;)
    {
        pTemp = pUpdate->pNext;
        delete pUpdate;
        pUpdate = pTemp;
    }
}

CTaxField *CTaxField::Create(WORD type)
{
    CTaxField *result = nullptr;

    switch (type)
    {
    case FLDTYPE_NUMBER:
        result = new(std::nothrow) CTaxNumberFld;
        break;

    case FLDTYPE_CURRENCY:
        result = new(std::nothrow) CTaxCurrencyFld;
        break;

    case FLDTYPE_FLOAT:
        result = new(std::nothrow) CTaxFloatFld;
        break;

    case FLDTYPE_RADIO:
    case FLDTYPE_CHECK:
        result = new(std::nothrow) CTaxBoolFld;
        break;

    case FLDTYPE_DATE:
        result = new(std::nothrow) CTaxDateFld;
        break;

    case FLDTYPE_STRING:
    case FLDTYPE_SSN:
    case FLDTYPE_EIN:
    case FLDTYPE_PHONE:
        result = new(std::nothrow) CTaxStringFld;
        break;

    case FLDTYPE_OLDLIST:
        result = new(std::nothrow) CTaxOldListFld;
        break;

    case FLDTYPE_LIST:
        result = new(std::nothrow) CTaxListFld;
        break;

    case FLDTYPE_DYNALIST:
        result = new(std::nothrow) CTaxDynaListFld;
        break;

    default:
        break;
    }

    if (result)
    {
        result->m_wType = type;
    }

    return result;
}

WORD CTaxField::GetID()
{
    return m_wID;
}

WORD CTaxField::GetIndex()
{
    return m_wIndex;
}

WORD CTaxField::GetType()
{
    return m_wType;
}

ITaxForm* CTaxField::GetForm()
{
    return m_pForm;
}

BOOL CTaxField::GetStatus(DWORD dwStatus)
{
    return ((m_dwStatus & dwStatus) == dwStatus);
}

void CTaxField::SetStatus(DWORD dwStatus, BOOL bSet)
{
    if (bSet)
    {
        m_dwStatus |= dwStatus;
    }
    else
    {
        m_dwStatus &= ~dwStatus;
    }
}

void CTaxField::InitStatus(DWORD dwStatus)
{
    m_dwStatus = dwStatus;

    if (m_pForm->m_pFormMgr->HasProductFlag(PRODUCTFLAG_ISSTANDARD))
    {
        if ((GetStatus(FLDSTATUS_PREPARERONLY) || GetStatus(FLDSTATUS_PREPARERONLYINFO)) &&
            GetStatus(FLDSTATUS_CALC))
        {
            SetStatus(FLDSTATUS_CALC, FALSE);
            SetStatus(FLDSTATUS_DEFCALC, FALSE);
        }
    }

    if (!m_pForm->m_pFormMgr->HasProductFlag(PRODUCTFLAG_ISPREPARER))
    {
        if (GetStatus(FLDSTATUS_PREPARERONLY) || GetStatus(FLDSTATUS_PREPARERONLYINFO))
        {
            SetStatus(FLDSTATUS_PROTECTED, TRUE);
        }
    }
}

void CTaxField::SetStatusData(DWORD dwStatus)
{
    m_dwStatus = (m_dwStatus & FLDSTATUS_MASK_STATIC) | (dwStatus & FLDSTATUS_MASK_DYNAMIC);
}

DWORD CTaxField::GetStatusData()
{
    return (m_dwStatus & FLDSTATUS_MASK_DYNAMIC);
}

void CTaxField::Update()
{
    if (m_pfnUpdate)
    {
        (*m_pfnUpdate)(m_pForm->m_pFormMgr, m_pForm, this);
    }

    ExternalUpdate();
}

LONG CTaxField::GetDate()
{
    CTaxDate dateValue;
    dateValue = GetCalcDate();
    return (LONG)dateValue;
}

void CTaxField::GetString(LPSTR szStr, size_t iSize)
{
    CTaxString str(GetString());

    int signedStrLength = str.GetLength();
    size_t strLength;

    if (signedStrLength < 0)
    {
        //this really shouldn't ever happen
        //but 0 is preferable to wrapping around the size_t because of a negative value
        strLength = 0;
    }
    else
    {
        strLength = static_cast<size_t>(signedStrLength);
    }

    if (strLength < iSize)
    {
        strcpy_s(szStr, iSize, (LPCSTR)str);
    }
    else
    {
        *szStr = '\0';
    }
}

LONG CTaxField::GetMinNumber()
{
    return 0;
}

LONG CTaxField::GetMaxNumber()
{
    return 0;
}

TAXCURRENCY CTaxField::GetMinCurrency()
{
    return 0;
}

TAXCURRENCY CTaxField::GetMaxCurrency()
{
    return 0;
}

int CTaxField::GetFMVStatus()
{
    return 0;
}

DOUBLE CTaxField::GetMinFloat()
{
    return 0.0;
}

DOUBLE CTaxField::GetMaxFloat()
{
    return 0.0;
}

size_t CTaxField::GetDataSize()
{
    return 0;
}

void CTaxField::GetData(void *lpData)
{
}

void CTaxField::SetData(const void *lpData)
{
}

int CTaxField::GetStringLength()
{
    return GetString().GetLength();
}

int CTaxField::GetMaxLength()
{
    return 0;
}

int CTaxField::GetListIndex()
{
    return -1;
}

int CTaxField::GetListTotal()
{
    return 0;
}

void CTaxField::GetListString(int iIndex, LPSTR szStr, size_t iSize)
{
    *szStr = '\0';
}

void CTaxField::GetListStringDisplay(int iIndex, LPSTR szStr, size_t iSize)
{
    *szStr = '\0';
}

void CTaxField::GetListStringTitle(LPSTR szStr, size_t iSize)
{
    *szStr = '\0';
}

void CTaxField::SetListIndex(int iIndex)
{
}

void CTaxField::SetListTitle(LPCSTR szTitle)
{
}

void CTaxField::SetListItem(LPCSTR szDisplay, LPCSTR szValue)
{
}

void CTaxField::AttachExternalUpdate(ITaxFormManager* pFormMgr, CALCEXPUPDATEFUNC pfnUpdate)
{
    UPDATEOBJ* pUpdate, *pNew;

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

    if (pNew = new(std::nothrow) UPDATEOBJ)
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

LONG CTaxField::GetMinCalcDate()
{
    CTaxDate dateEmpty;
    return (LONG)dateEmpty;
}

LONG CTaxField::GetMaxCalcDate()
{
    CTaxDate dateEmpty;
    return (LONG)dateEmpty;
}

LONG CTaxField::GetMinDate()
{
    return GetMinCalcDate();
}

LONG CTaxField::GetMaxDate()
{
    return GetMaxCalcDate();
}

LONG CTaxField::GetDefYear()
{
    return 0;
}

WORD CTaxField::GetStringType()
{
    return 0;
}

int CTaxField::GetIndexOfStr(LPCSTR szStr)
{
    return -1;
}

void CTaxField::DetachExternalUpdate(ITaxFormManager* pFormMgr)
{
    UPDATEOBJ* pUpdate, *pPrev;

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

void CTaxField::ExternalUpdate()
{
    UPDATEOBJ* pUpdate;

    for (pUpdate = m_pUpdate; pUpdate; pUpdate = pUpdate->pNext)
    {
        (*pUpdate->pfnUpdate)(pUpdate->pFormMgr, m_pForm, this);
    }
}

bool CTaxField::WriteJsonDetails(rapidjson::Writer<rapidjson::StringBuffer>& out)
{
    //outer object must be started by caller!
    if (hasDetailsNote() || hasLedgerDetails())
    {
        out.Key("Details");
        out.StartObject();

        if (hasDetailsNote())
        {
            out.Key("Note");
            out.String(m_detailsNote);
        }

        if (hasLedgerDetails())
        {
            out.Key("Ledger");
            out.StartArray();
            for (unsigned i = 0; i < m_detailsLedger.get()->byNumOfLines; ++i)
            {
                out.StartObject();

                out.Key("Date");
                out.Int(m_detailsLedger.get()->recDetails[i].lDate);

                out.Key("Imported");
                out.Bool(m_detailsLedger.get()->recDetails[i].imported == TRUE ? true : false);

                std::string str(m_detailsLedger.get()->recDetails[i].szDesc, sizeof(m_detailsLedger.get()->recDetails[i].szDesc));;
                out.Key("Desc");
                out.String(str.c_str());

                out.Key("Amount");
                out.Int64(m_detailsLedger.get()->recDetails[i].tcAmount);

                out.EndObject();
            }
            out.EndArray();
        }

        out.EndObject();
    }
    return true;
}

bool CTaxField::ReadJson(rapidjson::Value& in)
{
    return ReadJson(in, true, true, true);
}

bool CTaxField::ImportPYJson(rapidjson::Value& in, DWORD importFlags)
{
    bool readDetails = false;
    bool is_USSCHA_CASH50 = false;

    ITaxFormManager* pFormMgr = m_pForm->m_pFormMgr;
    WORD idUSSCHA = pFormMgr->GetFormID("USSCHA");
    if (m_pForm->GetID() == idUSSCHA)
    {
        WORD idCASH50 = pFormMgr->GetFieldID(idUSSCHA, "CASH50");
        if (GetID() == idCASH50)
        {
            is_USSCHA_CASH50 = true;
        }
    }

    if (importFlags & PYIMPORT_CASHCON_DETAILS)
    {
        auto findDetails = in.FindMember("Details");
        if (findDetails != in.MemberEnd())
        {
            // import line items for USSCHA.CASH50
            if (is_USSCHA_CASH50)
            {
                readDetails = true;
            }
        }
    }

    bool result = ReadJson(in, false, readDetails, true);

    if (is_USSCHA_CASH50)
    {
        if (readDetails && m_detailsLedger)
        {
            for (int i = 0; i < m_detailsLedger->byNumOfLines; i++)
            {
                m_detailsLedger->recDetails[i].imported = TRUE;

                // we only want to import the descriptions
                m_detailsLedger->recDetails[i].lDate = CTaxDate();
                m_detailsLedger->recDetails[i].tcAmount = 0;
            }
        }

        // don't actually import the value
        SetCurrency(0);
    }

    return result;
}

bool CTaxField::ReadJson(rapidjson::Value& in, bool readFlags, bool readDetails, bool readValue)
{
    if (readFlags)
    {
        auto findFlags = in.FindMember("Flags");
        if (findFlags != in.MemberEnd())
        {
            SetStatusData(findFlags->value.GetUint());
        }
    }

    if (readDetails)
    {
        auto findDetails = in.FindMember("Details");
        if (findDetails != in.MemberEnd())
        {
            auto findNote = findDetails->value.FindMember("Note");
            if (findNote != findDetails->value.MemberEnd())
            {
                m_detailsNote = findNote->value.GetString();
            }

            auto findLedger = findDetails->value.FindMember("Ledger");
            if (findLedger != findDetails->value.MemberEnd())
            {
                m_detailsLedger.reset(new stDetailRec);
                for (auto iter = findLedger->value.Begin(); iter != findLedger->value.End(); iter++)
                {
                    // use current byNumOfLines and increment after instead of - 1 all over
                    m_detailsLedger.get()->recDetails[m_detailsLedger.get()->byNumOfLines].lDate = CTaxDate((*iter)["Date"].GetInt());
                    m_detailsLedger.get()->recDetails[m_detailsLedger.get()->byNumOfLines].imported = (*iter)["Imported"].GetBool();
                    m_detailsLedger.get()->recDetails[m_detailsLedger.get()->byNumOfLines].tcAmount = (*iter)["Amount"].GetInt64();
                    Tax::xstring xdesc = (*iter)["Desc"].GetString();
                    strcpy_s(m_detailsLedger.get()->recDetails[m_detailsLedger.get()->byNumOfLines].szDesc, xdesc);
                    ++(m_detailsLedger.get()->byNumOfLines);
                }
            }
        }
    }

    if (readValue)
    {
        auto findValue = in.FindMember("Value");
        if (findValue != in.MemberEnd())
        {
            WORD typeHint = 0;

            auto findTypeHint = in.FindMember("TypeHint");
            if (findTypeHint != in.MemberEnd())
            {
                typeHint = findTypeHint->value.GetUint();
            }

            if (findValue->value.IsBool())
            {
                SetBool(findValue->value.GetBool());
            }
            else if (findValue->value.IsInt())
            {
                if (typeHint == FLDTYPE_CURRENCY)
                {
                    SetCurrency(findValue->value.GetInt());
                }
                else
                {
                    SetNumber(findValue->value.GetInt());
                }
            }
            else if (findValue->value.IsInt64())
            {
                SetCurrency(findValue->value.GetInt64());
            }
            else if (findValue->value.IsDouble())
            {
                SetFloat(findValue->value.GetDouble());
            }
            else if (findValue->value.IsString())
            {
                if (typeHint == FLDTYPE_DATE)
                {
                    CTaxDate date(findValue->value.GetString());
                    SetDate(date);
                }
                else
                {
                    SetString(findValue->value.GetString());
                }
            }
            else if (findValue->value.IsNull())
            {
                Clear();
            }
            else
            {
                ASSERT(FALSE); // unknown json data type
                return false;
            }
        }
        else
        {
            Clear();
        }
    }

    return true;
}

bool CTaxField::HasJsonData()
{
    return (GetStatusData() != 0) || (!IsEmpty());
}

void CTaxField::clearLedgerDetails()
{
    m_detailsLedger.reset();

    // if note also cleared, set HASDETAILS status false
    if (!hasDetailsNote())
    {
        SetStatus(FLDSTATUS_HASDETAILS, FALSE);
    }
}

void CTaxField::clearDetailsNote()
{
    m_detailsNote.Empty();

    // if ledger also cleared, set HASDETAILS status false
    if (!hasLedgerDetails())
    {
        SetStatus(FLDSTATUS_HASDETAILS, FALSE);
    }
}

BOOL CTaxField::setLedgerDetailsLine(const int line, LPCSTR date, LPCSTR desc, LPCSTR amount, BOOL imported)
{
    BOOL success = FALSE;
    if (line > 0 && line <= kMAXLINES)
    {
        if (m_detailsLedger.get() == nullptr)
        {
            m_detailsLedger.reset(new stDetailRec);
        }
        // if this is the max line, set number of lines accordingly
        if (line > m_detailsLedger.get()->byNumOfLines)
        {
            m_detailsLedger.get()->byNumOfLines = (BYTE)line;
        }
        m_detailsLedger.get()->recDetails[line - 1] = stDetails();
        
        Tax::xstring xdate = date;
        Tax::xstring xdesc = desc;
        m_detailsLedger.get()->recDetails[line - 1].lDate = xdate;
        strcpy_s(m_detailsLedger.get()->recDetails[line - 1].szDesc, xdesc);
        Tax::xstring tmp = amount;
        tmp.Replace(".", "");
        tmp.Replace(",", "");

        m_detailsLedger.get()->recDetails[line - 1].imported = imported;

        if (GetType() == FLDTYPE_CURRENCY)
        {
            m_detailsLedger.get()->recDetails[line - 1].tcAmount = StringToCurrency(tmp) / 100;
        }
        else
        {
            m_detailsLedger.get()->recDetails[line - 1].tcAmount = strtol(tmp, nullptr, 10);
        }

        SetStatus(FLDSTATUS_HASDETAILS, TRUE);

        success = TRUE;
    }
    return success;
}

void CTaxField::setDetailsNote(LPCSTR szNote)
{	
    m_detailsNote = szNote;
    SetStatus(FLDSTATUS_HASDETAILS, TRUE);
}

BOOL CTaxField::hasLedgerDetails()
{
    return (m_detailsLedger.get() && m_detailsLedger->byNumOfLines > 0);
}

BOOL CTaxField::hasDetailsNote()
{
    return (!m_detailsNote.IsEmpty());
}

stDetailRec* CTaxField::getLedgerDetails()
{
    return m_detailsLedger.get();
}

LPCSTR CTaxField::getDetailsNote()
{
    return m_detailsNote;
}

TaxFieldHandle CTaxField::handle()
{
    TaxFieldHandle result;
    result.dll = m_ownerDll;
    result.self = reinterpret_cast<TaxFieldInternalType*>(this);
    return result;
}

CTaxNumberFld::CTaxNumberFld()
{
    m_lValue = 0;
    m_lMinValue = 0;
    m_lMaxValue = 0;
    m_pfnCalc = NULL;
}

BOOL CTaxNumberFld::Init(WORD wIndex, WORD wLastIndex, DWORD dwStatus, LONG lDefValue, LONG lMinValue, LONG lMaxValue,
                         CALCLONGFUNC pfnCalc, CALCUPDATEFUNC pfnUpdate)
{
    m_wIndex = wIndex;
    InitStatus(dwStatus);
    m_lValue = lDefValue;
    m_lMinValue = lMinValue;
    m_lMaxValue = lMaxValue;
    m_pfnCalc = pfnCalc;
    m_pfnUpdate = pfnUpdate;

    if ((m_lMinValue == 0) && (m_lMaxValue == 0))
    {
        m_lMinValue = CALC_MIN_LONG;
        m_lMaxValue = CALC_MAX_LONG;
    }

    if (wIndex != wLastIndex)
    {
        return ((CTaxNumberFld*)m_pForm->GetField(m_wID + 1))->Init(wIndex + 1, wLastIndex, dwStatus, lDefValue, lMinValue, lMaxValue, pfnCalc, pfnUpdate);
    }

    return TRUE;
}

void CTaxNumberFld::Calculate()
{
    LONG lValue;

    try
    {
        if (((m_dwStatus & FLDSTATUS_CALC) != 0) &&
            ((m_dwStatus & FLDSTATUS_OVERRIDDEN) == 0) &&
            (((m_dwStatus & FLDSTATUS_DEFCALC) == 0) ||
             ((m_dwStatus & FLDSTATUS_MODIFIED) == 0)))
        {
            if ((lValue = (*m_pfnCalc)(m_pForm->m_pFormMgr, m_pForm, this)) == m_lValue)
            {
                return;
            }

            m_lValue = lValue;
        }

        Update();
    }
    catch (std::runtime_error& e)
    {
        HandleMathException(this, e);
    }
    catch (...)
    {
        HandleMathException(this);
    }
}

void CTaxNumberFld::Clear()
{
    m_lValue = 0;
}

LONG CTaxNumberFld::GetNumber()
{
    return m_lValue;
}

TAXCURRENCY CTaxNumberFld::GetCurrency()
{
    return (TAXCURRENCY)m_lValue;
}

DOUBLE CTaxNumberFld::GetFloat()
{
    return (DOUBLE)m_lValue;
}

BOOL CTaxNumberFld::GetBool()
{
    return (m_lValue != 0);
}

CTaxDate CTaxNumberFld::GetCalcDate()
{
    return CTaxDate(m_lValue);
}

CTaxString CTaxNumberFld::GetString()
{
    char szNumber[64];
    CTaxString str;

    sprintf_s(szNumber, "%li", m_lValue);
    str = szNumber;
    return str;
}

void CTaxNumberFld::SetNumber(LONG lValue)
{
    m_lValue = lValue;
}

void CTaxNumberFld::SetCurrency(TAXCURRENCY currValue)
{
    m_lValue = (LONG)currValue;
}

void CTaxNumberFld::SetFloat(DOUBLE dValue)
{
    m_lValue = DblToLong(dValue);
}

void CTaxNumberFld::SetBool(BOOL bValue)
{
    m_lValue = (LONG)bValue;
}

void CTaxNumberFld::SetDate(LONG dateValue)
{
    m_lValue = dateValue;
}

void CTaxNumberFld::SetString(LPCSTR szStr)
{
    m_lValue = std::strtol(szStr, nullptr, 10);
}

LONG CTaxNumberFld::GetMinNumber()
{
    return m_lMinValue;
}

LONG CTaxNumberFld::GetMaxNumber()
{
    return m_lMaxValue;
}

int CTaxNumberFld::GetMaxLength()
{
    return MAXLENGTH_NUMBER;
}

size_t CTaxNumberFld::GetDataSize()
{
    return sizeof(m_dwStatus) + sizeof(m_lValue);
}

void CTaxNumberFld::GetData(void *lpData)
{
    LPSTR lpTemp = (LPSTR)lpData;
    *((DWORD*)lpTemp) = m_dwStatus;
    lpTemp += sizeof(m_dwStatus);
    *((LONG*)lpTemp) = m_lValue;
}

void CTaxNumberFld::SetData(const void *lpData)
{
    LPSTR lpTemp = (LPSTR)lpData;
    SetStatusData(*((DWORD*)lpTemp));
    lpTemp += sizeof(m_dwStatus);
    m_lValue = *((LONG*)lpTemp);
}

BOOL CTaxNumberFld::IsEmpty()
{
    return (m_lValue == 0);
}

bool CTaxNumberFld::WriteJson(rapidjson::Writer<rapidjson::StringBuffer>& out)
{
    out.StartObject();

    DWORD flags = GetStatusData();
    if (flags)
    {
        out.Key("Flags");
        out.Uint(flags);
    }

    if (!IsEmpty())
    {
        out.Key("Value");
        out.Int(m_lValue);
    }

    WriteJsonDetails(out);

    out.EndObject();

    return true;
}

CTaxCurrencyFld::CTaxCurrencyFld()
{
    m_currValue = 0;
    m_currMinValue = 0;
    m_currMaxValue = 0;
    m_nFMVStatus = 0;
    m_pfnCalc = NULL;
}

BOOL CTaxCurrencyFld::Init(WORD wIndex, WORD wLastIndex, DWORD dwStatus, TAXCURRENCY currDefValue, TAXCURRENCY currMinValue, TAXCURRENCY currMaxValue,
                           int nFMVStatus, CALCCURRENCYFUNC pfnCalc, CALCUPDATEFUNC pfnUpdate)
{
    m_wIndex = wIndex;
    InitStatus(dwStatus);
    m_currValue = currDefValue;
    m_currMinValue = currMinValue;
    m_currMaxValue = currMaxValue;
    m_nFMVStatus = nFMVStatus;
    m_pfnCalc = pfnCalc;
    m_pfnUpdate = pfnUpdate;

    if ((m_currMinValue == 0) && (m_currMaxValue == 0))
    {
        m_currMinValue = CALC_MIN_CURRENCY;
        m_currMaxValue = CALC_MAX_CURRENCY;
    }

    if (wIndex != wLastIndex)
    {
        return ((CTaxCurrencyFld*)m_pForm->GetField(m_wID + 1))->Init(wIndex + 1, wLastIndex, dwStatus, currDefValue, currMinValue, currMaxValue, nFMVStatus, pfnCalc, pfnUpdate);
    }

    return TRUE;
}

void CTaxCurrencyFld::Calculate()
{
    TAXCURRENCY currValue;

    try
    {
        if (((m_dwStatus & FLDSTATUS_CALC) != 0) &&
            ((m_dwStatus & FLDSTATUS_OVERRIDDEN) == 0) &&
            (((m_dwStatus & FLDSTATUS_DEFCALC) == 0) ||
             ((m_dwStatus & FLDSTATUS_MODIFIED) == 0)))
        {
            if ((currValue = (*m_pfnCalc)(m_pForm->m_pFormMgr, m_pForm, this)) == m_currValue)
            {
                return;
            }

            m_currValue = currValue;
        }

        Update();
    }
    catch (std::runtime_error& e)
    {
        HandleMathException(this, e);
    }
    catch (...)
    {
        HandleMathException(this);
    }
}

void CTaxCurrencyFld::Clear()
{
    m_currValue = 0;
}

LONG CTaxCurrencyFld::GetNumber()
{
    return (LONG)m_currValue;
}

TAXCURRENCY CTaxCurrencyFld::GetCurrency()
{
    return m_currValue;
}

DOUBLE CTaxCurrencyFld::GetFloat()
{
    return (DOUBLE)m_currValue;
}

BOOL CTaxCurrencyFld::GetBool()
{
    return (m_currValue != 0);
}

CTaxDate CTaxCurrencyFld::GetCalcDate()
{
    return CTaxDate(static_cast<LONG>(m_currValue));
}

CTaxString CTaxCurrencyFld::GetString()
{
    return FormatCurrency(m_currValue);
}

void CTaxCurrencyFld::SetNumber(LONG lValue)
{
    m_currValue = (TAXCURRENCY)lValue;
}

void CTaxCurrencyFld::SetCurrency(TAXCURRENCY currValue)
{
    m_currValue = currValue;
}

void CTaxCurrencyFld::SetFloat(DOUBLE dValue)
{
    m_currValue = DblToCurr(dValue);
}

void CTaxCurrencyFld::SetBool(BOOL bValue)
{
    m_currValue = (TAXCURRENCY)bValue;
}

void CTaxCurrencyFld::SetDate(LONG dateValue)
{
    m_currValue = (TAXCURRENCY)dateValue;
}

void CTaxCurrencyFld::SetString(LPCSTR szStr)
{
    m_currValue = ParseCurrency(szStr);
}

TAXCURRENCY CTaxCurrencyFld::GetMinCurrency()
{
    return m_currMinValue;
}

TAXCURRENCY CTaxCurrencyFld::GetMaxCurrency()
{
    return m_currMaxValue;
}

int CTaxCurrencyFld::GetFMVStatus()
{
    return m_nFMVStatus;
}

int CTaxCurrencyFld::GetMaxLength()
{
    return MAXLENGTH_CURRENCY;
}

size_t CTaxCurrencyFld::GetDataSize()
{
    return sizeof(m_dwStatus) + sizeof(m_currValue);
}

void CTaxCurrencyFld::GetData(void *lpData)
{
    LPSTR lpTemp = (LPSTR)lpData;
    *((DWORD*)lpTemp) = m_dwStatus;
    lpTemp += sizeof(m_dwStatus);
    *((TAXCURRENCY*)lpTemp) = m_currValue;
}

void CTaxCurrencyFld::SetData(const void *lpData)
{
    LPSTR lpTemp = (LPSTR)lpData;
    SetStatusData(*((DWORD*)lpTemp));
    lpTemp += sizeof(m_dwStatus);
    m_currValue = *((TAXCURRENCY*)lpTemp);
}

BOOL CTaxCurrencyFld::IsEmpty()
{
    return (m_currValue == 0);
}

bool CTaxCurrencyFld::WriteJson(rapidjson::Writer<rapidjson::StringBuffer>& out)
{
    out.StartObject();

    DWORD flags = GetStatusData();
    if (flags)
    {
        out.Key("Flags");
        out.Uint(flags);
    }

    if (!IsEmpty())
    {
        out.Key("TypeHint");
        out.Uint(m_wType);

        out.Key("Value");
        out.Int64(m_currValue);
    }

    WriteJsonDetails(out);

    out.EndObject();

    return true;
}

CTaxFloatFld::CTaxFloatFld()
{
    m_dValue = 0.0;
    m_dMinValue = 0.0;
    m_dMaxValue = 0.0;
    m_maxLength = 0;
    m_pfnCalc = NULL;
}

BOOL CTaxFloatFld::Init(WORD wIndex, WORD wLastIndex, DWORD dwStatus, DOUBLE dDefValue, DOUBLE dMinValue, DOUBLE dMaxValue,
                        LONG maxLength, CALCDOUBLEFUNC pfnCalc, CALCUPDATEFUNC pfnUpdate)
{
    m_wIndex = wIndex;
    InitStatus(dwStatus);
    m_dValue = dDefValue;
    m_dMinValue = dMinValue;
    m_dMaxValue = dMaxValue;
    m_maxLength = maxLength;
    m_pfnCalc = pfnCalc;
    m_pfnUpdate = pfnUpdate;

    if ((m_dMinValue == 0.0) && (m_dMaxValue == 0.0))
    {
        m_dMinValue = CALC_MIN_DOUBLE;
        m_dMaxValue = CALC_MAX_DOUBLE;
    }

    if (m_maxLength == 0)
    {
        m_maxLength = MAXLENGTH_FLOAT;
    }

    if (wIndex != wLastIndex)
    {
        return ((CTaxFloatFld*)m_pForm->GetField(m_wID + 1))->Init(wIndex + 1, wLastIndex, dwStatus, dDefValue, dMinValue, dMaxValue, maxLength, pfnCalc, pfnUpdate);
    }

    return TRUE;
}

void CTaxFloatFld::Calculate()
{
    DOUBLE dValue;

    try
    {
        if (((m_dwStatus & FLDSTATUS_CALC) != 0) &&
            ((m_dwStatus & FLDSTATUS_OVERRIDDEN) == 0) &&
            (((m_dwStatus & FLDSTATUS_DEFCALC) == 0) ||
             ((m_dwStatus & FLDSTATUS_MODIFIED) == 0)))
        {
            if ((dValue = (*m_pfnCalc)(m_pForm->m_pFormMgr, m_pForm, this)) == m_dValue)
            {
                return;
            }

            m_dValue = dValue;
        }

        Update();
    }
    catch (std::runtime_error& e)
    {
        HandleMathException(this, e);
    }
    catch (...)
    {
        HandleMathException(this);
    }
}

void CTaxFloatFld::Clear()
{
    m_dValue = 0.0;
}

LONG CTaxFloatFld::GetNumber()
{
    return DblToLong(m_dValue);
}

TAXCURRENCY CTaxFloatFld::GetCurrency()
{
    return DblToCurr(m_dValue);
}

DOUBLE CTaxFloatFld::GetFloat()
{
    return m_dValue;
}

BOOL CTaxFloatFld::GetBool()
{
    return (m_dValue != 0.0);
}

CTaxDate CTaxFloatFld::GetCalcDate()
{
    return CTaxDate(DblToLong(m_dValue));
}

CTaxString CTaxFloatFld::GetString()
{
    char szNumber[64];

    sprintf_s(szNumber, "%.6f", m_dValue);
    CTaxString str = szNumber;
    return str;
}

void CTaxFloatFld::SetNumber(LONG lValue)
{
    m_dValue = (DOUBLE)lValue;
}

void CTaxFloatFld::SetCurrency(TAXCURRENCY currValue)
{
    m_dValue = (DOUBLE)currValue;
}

void CTaxFloatFld::SetFloat(DOUBLE dValue)
{
    m_dValue = dValue;
}

void CTaxFloatFld::SetBool(BOOL bValue)
{
    m_dValue = (DOUBLE)bValue;
}

void CTaxFloatFld::SetDate(LONG dateValue)
{
    m_dValue = (DOUBLE)dateValue;
}

void CTaxFloatFld::SetString(LPCSTR szStr)
{
    m_dValue = std::strtod(szStr, nullptr);
}

DOUBLE CTaxFloatFld::GetMinFloat()
{
    return m_dMinValue;
}

DOUBLE CTaxFloatFld::GetMaxFloat()
{
    return m_dMaxValue;
}

int CTaxFloatFld::GetMaxLength()
{
    return m_maxLength;
}

size_t CTaxFloatFld::GetDataSize()
{
    return sizeof(m_dwStatus) + sizeof(m_dValue);
}

void CTaxFloatFld::GetData(void *lpData)
{
    LPSTR lpTemp = (LPSTR)lpData;
    *((DWORD*)lpTemp) = m_dwStatus;
    lpTemp += sizeof(m_dwStatus);
    *((DOUBLE*)lpTemp) = m_dValue;
}

void CTaxFloatFld::SetData(const void *lpData)
{
    LPSTR lpTemp = (LPSTR)lpData;
    SetStatusData(*((DWORD*)lpTemp));
    lpTemp += sizeof(m_dwStatus);
    m_dValue = *((DOUBLE*)lpTemp);
}

BOOL CTaxFloatFld::IsEmpty()
{
    return (m_dValue == 0.0);
}

bool CTaxFloatFld::WriteJson(rapidjson::Writer<rapidjson::StringBuffer>& out)
{
    out.StartObject();

    DWORD flags = GetStatusData();
    if (flags)
    {
        out.Key("Flags");
        out.Uint(flags);
    }

    if (!IsEmpty())
    {
        out.Key("Value");
        out.Double(m_dValue);
    }

    WriteJsonDetails(out);

    out.EndObject();

    return true;
}

CTaxBoolFld::CTaxBoolFld()
{
    m_bValue = FALSE;
    m_pfnCalc = NULL;
}

BOOL CTaxBoolFld::Init(WORD wIndex, WORD wLastIndex, DWORD dwStatus, BOOL bDefValue,
                       CALCBOOLFUNC pfnCalc, CALCUPDATEFUNC pfnUpdate)
{
    m_wIndex = wIndex;
    InitStatus(dwStatus);
    m_bValue = bDefValue;
    m_pfnCalc = pfnCalc;
    m_pfnUpdate = pfnUpdate;

    if (wIndex != wLastIndex)
    {
        return ((CTaxBoolFld*)m_pForm->GetField(m_wID + 1))->Init(wIndex + 1, wLastIndex, dwStatus, bDefValue, pfnCalc, pfnUpdate);
    }

    return TRUE;
}

void CTaxBoolFld::Calculate()
{
    BOOL bValue;

    try
    {
        if (((m_dwStatus & FLDSTATUS_CALC) != 0) &&
            ((m_dwStatus & FLDSTATUS_OVERRIDDEN) == 0) &&
            (((m_dwStatus & FLDSTATUS_DEFCALC) == 0) ||
             ((m_dwStatus & FLDSTATUS_MODIFIED) == 0)))
        {
            if ((bValue = (*m_pfnCalc)(m_pForm->m_pFormMgr, m_pForm, this)) == m_bValue)
            {
                return;
            }

            m_bValue = bValue;
        }

        Update();
    }
    catch (std::runtime_error& e)
    {
        HandleMathException(this, e);
    }
    catch (...)
    {
        HandleMathException(this);
    }
}

void CTaxBoolFld::Clear()
{
    m_bValue = FALSE;
}

LONG CTaxBoolFld::GetNumber()
{
    return (LONG)m_bValue;
}

TAXCURRENCY CTaxBoolFld::GetCurrency()
{
    return (TAXCURRENCY)m_bValue;
}

DOUBLE CTaxBoolFld::GetFloat()
{
    return (DOUBLE)m_bValue;
}

BOOL CTaxBoolFld::GetBool()
{
    return m_bValue;
}

CTaxDate CTaxBoolFld::GetCalcDate()
{
    return CTaxDate();
}

CTaxString CTaxBoolFld::GetString()
{
    CTaxString str;

    if (m_bValue)
    {
        str = "X";
    }
    else
    {
        str = "";
    }

    return str;
}

void CTaxBoolFld::SetNumber(LONG lValue)
{
    m_bValue = (lValue != 0);
}

void CTaxBoolFld::SetCurrency(TAXCURRENCY currValue)
{
    m_bValue = (currValue != 0);
}

void CTaxBoolFld::SetFloat(DOUBLE dValue)
{
    m_bValue = (dValue != 0.0);
}

void CTaxBoolFld::SetBool(BOOL bValue)
{
    m_bValue = bValue;
}

void CTaxBoolFld::SetDate(LONG dateValue)
{
    m_bValue = (dateValue != 0);
}

void CTaxBoolFld::SetString(LPCSTR szStr)
{

    m_bValue = (std::char_traits<char>::length(szStr) > 0);
}

size_t CTaxBoolFld::GetDataSize()
{
    return sizeof(m_dwStatus) + sizeof(m_bValue);
}

void CTaxBoolFld::GetData(void *lpData)
{
    LPSTR lpTemp = (LPSTR)lpData;
    *((DWORD*)lpTemp) = m_dwStatus;
    lpTemp += sizeof(m_dwStatus);
    *((BOOL*)lpTemp) = m_bValue;
}

void CTaxBoolFld::SetData(const void *lpData)
{
    LPSTR lpTemp = (LPSTR)lpData;
    SetStatusData(*((DWORD*)lpTemp));
    lpTemp += sizeof(m_dwStatus);
    m_bValue = *((BOOL*)lpTemp);
}

BOOL CTaxBoolFld::IsEmpty()
{
    return (m_bValue == 0);
}

bool CTaxBoolFld::WriteJson(rapidjson::Writer<rapidjson::StringBuffer>& out)
{
    out.StartObject();

    DWORD flags = GetStatusData();
    if (flags)
    {
        out.Key("Flags");
        out.Uint(flags);
    }

    if (!IsEmpty())
    {
        out.Key("Value");
        out.Bool(m_bValue != 0);
    }

    WriteJsonDetails(out);

    out.EndObject();

    return true;
}

CTaxDateFld::CTaxDateFld()
{
    m_pfnCalc = NULL;
}

BOOL CTaxDateFld::Init(WORD wIndex, WORD wLastIndex, DWORD dwStatus, int iDefDay, int iDefMonth, int iDefYear,
                       int iMinDay, int iMinMonth, int iMinYear, int iMaxDay, int iMaxMonth, int iMaxYear,
                       CTaxString strDefYear, CALCDATEFUNC pfnCalc, CALCUPDATEFUNC pfnUpdate)
{
    m_wIndex = wIndex;
    InitStatus(dwStatus);
    m_dateValue = CTaxDate(iDefDay, iDefMonth, iDefYear);
    m_minDate = CTaxDate(iMinDay, iMinMonth, iMinYear);
    m_maxDate = CTaxDate(iMaxDay, iMaxMonth, iMaxYear);

    if (m_minDate.IsEmpty() || (m_minDate < CTaxDate("01/01/1900")))
    {
        m_minDate = "01/01/1900";
    }

    if (m_maxDate.IsEmpty() || (m_maxDate > CTaxDate("12/31/2099")))
    {
        m_maxDate = "12/31/2099";
    }

    m_lDefYear = std::strtol(strDefYear, nullptr, 10);
    m_pfnCalc = pfnCalc;
    m_pfnUpdate = pfnUpdate;

    if (wIndex != wLastIndex)
        return ((CTaxDateFld*)m_pForm->GetField(m_wID + 1))->Init(wIndex + 1, wLastIndex, dwStatus, iDefDay, iDefMonth, iDefYear,
                iMinDay, iMinMonth, iMinYear, iMaxDay, iMaxMonth, iMaxYear,
                strDefYear, pfnCalc, pfnUpdate);

    return TRUE;
}

void CTaxDateFld::Calculate()
{
    CTaxDate dateValue;

    try
    {
        if (((m_dwStatus & FLDSTATUS_CALC) != 0) &&
            ((m_dwStatus & FLDSTATUS_OVERRIDDEN) == 0) &&
            (((m_dwStatus & FLDSTATUS_DEFCALC) == 0) ||
             ((m_dwStatus & FLDSTATUS_MODIFIED) == 0)))
        {
            if ((dateValue = (*m_pfnCalc)(m_pForm->m_pFormMgr, m_pForm, this)) == m_dateValue)
            {
                return;
            }

            m_dateValue = dateValue;
        }

        Update();
    }
    catch (std::runtime_error& e)
    {
        HandleMathException(this, e);
    }
    catch (...)
    {
        HandleMathException(this);
    }
}

void CTaxDateFld::Clear()
{
    m_dateValue.SetDate((LONG)0);
}

LONG CTaxDateFld::GetNumber()
{
    return (LONG)m_dateValue;
}

CTaxDate CTaxDateFld::GetCalcDate()
{
    return m_dateValue;
}

TAXCURRENCY CTaxDateFld::GetCurrency()
{
    return static_cast<TAXCURRENCY>(GetNumber());
}

DOUBLE CTaxDateFld::GetFloat()
{
    return static_cast<DOUBLE>(GetNumber());
}

BOOL CTaxDateFld::GetBool()
{
    return m_dateValue.IsValid();
}

CTaxString CTaxDateFld::GetString()
{
    return m_dateValue.GetTaxString();
}

void CTaxDateFld::SetNumber(LONG lValue)
{
    m_dateValue.SetDate(lValue);
}

void CTaxDateFld::SetCurrency(TAXCURRENCY currValue)
{
    m_dateValue.SetDate(static_cast<LONG>(currValue));
}

void CTaxDateFld::SetFloat(DOUBLE dValue)
{
    m_dateValue.SetDate(static_cast<LONG>(dValue));
}

void CTaxDateFld::SetBool(BOOL bValue)
{
}

void CTaxDateFld::SetDate(LONG dateValue)
{
    m_dateValue.SetDate(dateValue);
}

void CTaxDateFld::SetString(LPCSTR szStr)
{
    m_dateValue.SetDate(szStr);
}

size_t CTaxDateFld::GetDataSize()
{
    return sizeof(m_dwStatus) + sizeof(LONG);
}

void CTaxDateFld::GetData(void *lpData)
{
    LPSTR lpTemp = (LPSTR)lpData;
    *((DWORD*)lpTemp) = m_dwStatus;
    lpTemp += sizeof(m_dwStatus);
    *((LONG*)lpTemp) = (LONG)m_dateValue;
}

void CTaxDateFld::SetData(const void *lpData)
{
    LPSTR lpTemp = (LPSTR)lpData;
    SetStatusData(*((DWORD*)lpTemp));
    lpTemp += sizeof(m_dwStatus);
    m_dateValue.SetDate(*((LONG*)lpTemp));
}

BOOL CTaxDateFld::IsEmpty()
{
    return m_dateValue.IsEmpty();
}

bool CTaxDateFld::WriteJson(rapidjson::Writer<rapidjson::StringBuffer>& out)
{
    out.StartObject();

    DWORD flags = GetStatusData();
    if (flags)
    {
        out.Key("Flags");
        out.Uint(flags);
    }

    if (!IsEmpty())
    {
        out.Key("TypeHint");
        out.Uint(m_wType);

        CTaxString value = m_dateValue.GetTaxString();
        out.Key("Value");
        out.String(value, value.GetLength(), true);
    }

    WriteJsonDetails(out);

    out.EndObject();

    return true;
}

LONG CTaxDateFld::GetMinCalcDate()
{
    return (LONG)m_minDate;
}

LONG CTaxDateFld::GetMaxCalcDate()
{
    return (LONG)m_maxDate;
}

LONG CTaxDateFld::GetDefYear()
{
    return m_lDefYear;
}

int CTaxDateFld::GetMaxLength()
{
    return MAXLENGTH_DATE;
}

CTaxStringFld::CTaxStringFld()
{
    m_pfnCalc = NULL;
    m_StringType = 0;
    m_maxLength = 0;
}

BOOL CTaxStringFld::Init(WORD wIndex, WORD wLastIndex, DWORD dwStatus, LPCSTR szDefValue, WORD type, LONG maxLength,
                         CALCSTRINGFUNC pfnCalc, CALCUPDATEFUNC pfnUpdate)
{
    m_wIndex = wIndex;
    InitStatus(dwStatus);
    m_strValue = szDefValue;
    m_StringType = type;
    m_maxLength = maxLength;
    m_pfnCalc = pfnCalc;
    m_pfnUpdate = pfnUpdate;

    switch (GetType())
    {
    case FLDTYPE_SSN:
        m_maxLength = MAXLENGTH_SSN;
        break;
    case FLDTYPE_EIN:
        m_maxLength = MAXLENGTH_EIN;
        break;
    case FLDTYPE_PHONE:
        m_maxLength = MAXLENGTH_PHONE;
        break;
    default:
        if (GetStringType() == STRINGTYPE_ZIPCODE)
            m_maxLength = MAXLENGTH_ZIPCODE;
        else if (GetStringType() == STRINGTYPE_PIN)
            m_maxLength = MAXLENGTH_PIN;
        else if (m_maxLength == 0)
            m_maxLength = MAXLENGTH_STRING_DEFAULT;
        break;
    }

    if (wIndex != wLastIndex)
    {
        return ((CTaxStringFld*)m_pForm->GetField(m_wID + 1))->Init(wIndex + 1, wLastIndex, dwStatus, szDefValue, type, maxLength, pfnCalc, pfnUpdate);
    }

    return TRUE;
}

void CTaxStringFld::Calculate()
{
    try
    {
        if (((m_dwStatus & FLDSTATUS_CALC) != 0) &&
            ((m_dwStatus & FLDSTATUS_OVERRIDDEN) == 0) &&
            (((m_dwStatus & FLDSTATUS_DEFCALC) == 0) ||
             ((m_dwStatus & FLDSTATUS_MODIFIED) == 0)))
        {
            CTaxString strValue((*m_pfnCalc)(m_pForm->m_pFormMgr, m_pForm, this));

            if (strValue == m_strValue)
            {
                return;
            }

            SetAsciiStr(m_strValue, strValue);
        }

        Update();
    }
    catch (std::runtime_error& e)
    {
        HandleMathException(this, e);
    }
    catch (...)
    {
        HandleMathException(this);
    }
}

void CTaxStringFld::Clear()
{
    m_strValue.Empty();
}

LONG CTaxStringFld::GetNumber()
{
    return std::strtol(m_strValue, nullptr, 10);
}

TAXCURRENCY CTaxStringFld::GetCurrency()
{
    return ParseCurrency(m_strValue);
}

DOUBLE CTaxStringFld::GetFloat()
{
    return std::strtod(m_strValue, nullptr);
}

BOOL CTaxStringFld::GetBool()
{
    return (m_strValue.GetLength() > 0);
}

CTaxDate CTaxStringFld::GetCalcDate()
{
    return CTaxDate((LPCSTR)m_strValue);
}

CTaxString CTaxStringFld::GetString()
{
    return m_strValue;
}

void CTaxStringFld::SetNumber(LONG lValue)
{
    char szNumber[64];

    sprintf_s(szNumber, "%li", lValue);
    m_strValue = szNumber;
}

void CTaxStringFld::SetCurrency(TAXCURRENCY currValue)
{
    m_strValue = FormatCurrency(currValue);
}

void CTaxStringFld::SetFloat(DOUBLE dValue)
{
    char szNumber[64];

    sprintf_s(szNumber, "%.6f", dValue);
    m_strValue = szNumber;
}

void CTaxStringFld::SetBool(BOOL bValue)
{
    if (bValue)
    {
        m_strValue = "X";
    }
    else
    {
        m_strValue = "";
    }
}

void CTaxStringFld::SetDate(LONG dateValue)
{
    CTaxDate dateTemp;

    dateTemp.SetDate(dateValue);
    m_strValue = dateTemp.GetTaxString();
}

void CTaxStringFld::SetString(LPCSTR szStr)
{
    SetAsciiStr(m_strValue, szStr);
}

size_t CTaxStringFld::GetDataSize()
{
    return sizeof(m_dwStatus) + m_strValue.GetLength() + 1;
}

void CTaxStringFld::GetData(void *lpData)
{
    LPSTR lpTemp = (LPSTR)lpData;
    *((DWORD*)lpTemp) = m_dwStatus;
    lpTemp += sizeof(m_dwStatus);
    strcpy_s(lpTemp, m_strValue.GetLength() + 1, m_strValue);
}

void CTaxStringFld::SetData(const void *lpData)
{
    LPSTR lpTemp = (LPSTR)lpData;
    SetStatusData(*((DWORD*)lpTemp));
    lpTemp += sizeof(m_dwStatus);
    m_strValue = lpTemp;
}

int CTaxStringFld::GetStringLength()
{
    return m_strValue.GetLength();
}

BOOL CTaxStringFld::IsEmpty()
{
    return m_strValue.IsEmpty();
}

bool CTaxStringFld::WriteJson(rapidjson::Writer<rapidjson::StringBuffer>& out)
{
    out.StartObject();

    DWORD flags = GetStatusData();
    if (flags)
    {
        out.Key("Flags");
        out.Uint(flags);
    }

    if (!IsEmpty())
    {
        out.Key("Value");
        out.String(m_strValue, m_strValue.GetLength(), true);
    }

    WriteJsonDetails(out);

    out.EndObject();

    return true;
}

WORD CTaxStringFld::GetStringType()
{
    return m_StringType;
}

int CTaxStringFld::GetMaxLength()
{
    return m_maxLength;
}

CTaxListFld::CTaxListFld()
{
    m_wListID = 0;
    m_isFedListID = false;
}

BOOL CTaxListFld::Init(WORD wIndex, WORD wLastIndex, DWORD dwStatus, LPCSTR szDefValue, WORD wListID,
                       CALCSTRINGFUNC pfnCalc, CALCUPDATEFUNC pfnUpdate)
{
    m_wIndex = wIndex;
    InitStatus(dwStatus);
    m_strValue = szDefValue;
    m_pfnCalc = pfnCalc;
    m_pfnUpdate = pfnUpdate;
    m_wListID = wListID;
    m_listData = GetListData();

    if (wIndex != wLastIndex)
    {
        return ((CTaxListFld*)m_pForm->GetField(m_wID + 1))->Init(wIndex + 1, wLastIndex, dwStatus, szDefValue, wListID, pfnCalc, pfnUpdate);
    }

    return TRUE;
}

BOOL CTaxListFld::Init(WORD wIndex, WORD wLastIndex, DWORD dwStatus, LPCSTR szDefValue, int wListID,
    CALCSTRINGFUNC pfnCalc, CALCUPDATEFUNC pfnUpdate)
{
    return Init(wIndex, wLastIndex, dwStatus, szDefValue, static_cast<WORD>(wListID), pfnCalc, pfnUpdate);
}

BOOL CTaxListFld::Init(WORD wIndex, WORD wLastIndex, DWORD dwStatus, LPCSTR szDefValue, LPCSTR fedPicklistID,
                       CALCSTRINGFUNC pfnCalc, CALCUPDATEFUNC pfnUpdate)
{
    m_wIndex = wIndex;
    InitStatus(dwStatus);
    m_strValue = szDefValue;
    m_pfnCalc = pfnCalc;
    m_pfnUpdate = pfnUpdate;

#ifdef CALCSTATE
    WORD fedListID = m_pForm->m_pFormMgr->m_pFedFormMgr->GetPicklistId(fedPicklistID);
#else
    WORD fedListID = m_pForm->m_pFormMgr->GetPicklistId(fedPicklistID);
#endif

    if (fedListID)
    {
        m_isFedListID = true;
        m_wListID = fedListID;
        m_listData = GetListData();
    }

    if (wIndex != wLastIndex)
    {
        return ((CTaxListFld*)m_pForm->GetField(m_wID + 1))->Init(wIndex + 1, wLastIndex, dwStatus, szDefValue, fedPicklistID, pfnCalc, pfnUpdate);
    }

    return TRUE;
}

void CTaxListFld::Calculate()
{
    CTaxString strValue;

    try
    {
        if (((m_dwStatus & FLDSTATUS_CALC) != 0) &&
            ((m_dwStatus & FLDSTATUS_OVERRIDDEN) == 0) &&
            (((m_dwStatus & FLDSTATUS_DEFCALC) == 0) ||
             ((m_dwStatus & FLDSTATUS_MODIFIED) == 0)))
        {
            if (((strValue = (*m_pfnCalc)(m_pForm->m_pFormMgr, m_pForm, this)) == m_strValue) ||
                (!m_strDisplay.IsEmpty() && (strValue == m_strDisplay)))
            {
                return;
            }

            SetListString(strValue);
        }

        Update();
    }
    catch (std::runtime_error& e)
    {
        HandleMathException(this, e);
    }
    catch (...)
    {
        HandleMathException(this);
    }
}

void CTaxListFld::Clear()
{
    m_strValue.Empty();
    m_strDisplay.Empty();
}

void CTaxListFld::SetString(LPCSTR szStr)
{
    SetAsciiStr(m_strValue, szStr);
    m_strDisplay.Empty();
}

int CTaxListFld::GetListIndex()
{
    if (m_strValue.IsEmpty())
    {
        return -1;
    }

    if (!m_strDisplay.IsEmpty())
    {
        for (unsigned int i = 0; i < m_listData.items.size(); i++)
        {
            if (m_strDisplay == m_listData.items[i].display.c_str())
            {
                return i;
            }
        }
    }

    for (unsigned int i = 0; i < m_listData.items.size(); i++)
    {
        if (m_strValue == m_listData.items[i].value.c_str())
        {
            return i;
        }
    }

    return -1;
}

int CTaxListFld::GetListTotal()
{
    return static_cast<int>(m_listData.items.size());
}

void CTaxListFld::GetListString(int iIndex, LPSTR szStr, size_t iSize)
{
    *szStr = '\0';

    if ((iIndex >= 0) && (static_cast<unsigned int>(iIndex) < m_listData.items.size()))
    {
        if (m_listData.items[iIndex].value.length() < iSize)
        {
            strcpy_s(szStr, iSize, m_listData.items[iIndex].value.c_str());
        }
    }
}

void CTaxListFld::GetListStringDisplay(int iIndex, LPSTR szStr, size_t iSize)
{
    *szStr = '\0';

    if ((iIndex >= 0) && (static_cast<unsigned int>(iIndex) < m_listData.items.size()))
    {
        if (m_listData.items[iIndex].display.length() < iSize)
        {
            strcpy_s(szStr, iSize, m_listData.items[iIndex].display.c_str());
        }
    }
}

void CTaxListFld::GetListStringTitle(LPSTR szStr, size_t iSize)
{
    if (m_listData.title.length() < iSize)
    {
        strcpy_s(szStr, iSize, m_listData.title.c_str());
    }
}

PicklistInfo CTaxListFld::GetListData()
{
    XStream::xstream xs;

    if (m_isFedListID)
    {
#ifdef CALCSTATE
        xs.resize(m_pForm->m_pFormMgr->m_pFedFormMgr->GetPicklistDataSize(m_wListID));
        m_pForm->m_pFormMgr->m_pFedFormMgr->GetPicklistData(m_wListID, xs.data());
#else
        xs.resize(m_pForm->m_pFormMgr->GetPicklistDataSize(m_wListID));
        m_pForm->m_pFormMgr->GetPicklistData(m_wListID, xs.data());
#endif
    }
    else
    {
        xs.resize(m_pForm->m_pFormMgr->GetPicklistDataSize(m_wListID));
        m_pForm->m_pFormMgr->GetPicklistData(m_wListID, xs.data());
    }

    PicklistInfo result;

    if (!xs.empty())
    {
        xs >> result;
    }

    return result;
}

void CTaxListFld::SetListIndex(int iIndex)
{
    if ((iIndex >= 0) && (static_cast<unsigned int>(iIndex) < m_listData.items.size()))
    {
        m_strValue = m_listData.items[iIndex].value.c_str();
        m_strDisplay = m_listData.items[iIndex].display.c_str();
    }
    else
    {
        m_strValue.Empty();
        m_strDisplay.Empty();
        return;
    }
}

void CTaxListFld::SetListString(LPCSTR szStr)
{
    if (*szStr != '\0')
    {
        for (unsigned int i = 0; i < m_listData.items.size(); i++)
        {
            if ((strcmp(m_listData.items[i].display.c_str(), szStr) == 0) || 
                (strcmp(m_listData.items[i].value.c_str(), szStr) == 0))
            {
                m_strDisplay = m_listData.items[i].display.c_str();
                m_strValue = m_listData.items[i].value.c_str();
                return;
            }
        }
    }

    m_strDisplay.Empty();
    m_strValue.Empty();
}

size_t CTaxListFld::GetDataSize()
{
    return sizeof(m_dwStatus) + m_strValue.GetLength() + 1 + m_strDisplay.GetLength() + 1;
}

void CTaxListFld::GetData(void *lpData)
{
    LPSTR lpTemp = (LPSTR)lpData;
    *((DWORD*)lpTemp) = m_dwStatus;
    lpTemp += sizeof(m_dwStatus);
    strcpy_s(lpTemp, m_strValue.GetLength() + 1, m_strValue);
    lpTemp += m_strValue.GetLength() + 1;
    strcpy_s(lpTemp, m_strDisplay.GetLength() + 1, m_strDisplay);
}

void CTaxListFld::SetData(const void *lpData)
{
    LPSTR lpTemp = (LPSTR)lpData;
    SetStatusData(*((DWORD*)lpTemp));
    lpTemp += sizeof(m_dwStatus);
    m_strValue = lpTemp;
    lpTemp += m_strValue.GetLength() + 1;
    m_strDisplay = lpTemp;
}

bool CTaxListFld::ReadJson(rapidjson::Value& in)
{
    if (!CTaxField::ReadJson(in))
    {
        return false;
    }

    auto findDisplay = in.FindMember("Display");
    if (findDisplay != in.MemberEnd())
    {
        m_strDisplay = findDisplay->value.GetString();
    }
    else
    {
        m_strDisplay = "";
    }

    return true;
}

bool CTaxListFld::ImportPYJson(rapidjson::Value& in, DWORD importFlags)
{
    if (!CTaxField::ImportPYJson(in, importFlags))
    {
        return false;
    }

    auto findDisplay = in.FindMember("Display");
    if (findDisplay != in.MemberEnd())
    {
        m_strDisplay = findDisplay->value.GetString();
    }
    else
    {
        m_strDisplay = "";
    }

    return true;
}

bool CTaxListFld::HasJsonData()
{
    return (CTaxField::HasJsonData()) || (!m_strDisplay.IsEmpty());
}

bool CTaxListFld::WriteJson(rapidjson::Writer<rapidjson::StringBuffer>& out)
{
    out.StartObject();

    DWORD flags = GetStatusData();
    if (flags)
    {
        out.Key("Flags");
        out.Uint(flags);
    }

    if (!IsEmpty())
    {
        out.Key("Value");
        out.String(m_strValue, m_strValue.GetLength(), true);
    }

    if (!m_strDisplay.IsEmpty())
    {
        out.Key("Display");
        out.String(m_strDisplay, m_strDisplay.GetLength(), true);
    }

    WriteJsonDetails(out);

    out.EndObject();

    return true;
}

int CTaxListFld::GetIndexOfStr(LPCSTR szStr)
{
    for (unsigned int i = 0; i < m_listData.items.size(); i++)
    {
        if (_stricmp(szStr, m_listData.items[i].value.c_str()) == 0)
        {
            return i;
        }
    }

    return -1;
}

void CTaxListFld::CopyValueFrom(const CTaxListFld *other)
{
    m_strValue = other->m_strValue;
    m_strDisplay = other->m_strDisplay;
}

CTaxDynaListFld::CTaxDynaListFld()
{
    m_pfnListCalc = NULL;
}

CTaxDynaListFld::~CTaxDynaListFld()
{
    ClearListData();
}

void CTaxDynaListFld::ClearListData()
{
    m_listData = PicklistInfo();
}

BOOL CTaxDynaListFld::Init(WORD wIndex, WORD wLastIndex, DWORD dwStatus, LPCSTR szDefValue,
                           CALCSTRINGFUNC pfnCalc, CALCUPDATEFUNC pfnUpdate, CALCDYNALISTFUNC pfnListCalc)
{
    m_wIndex = wIndex;
    InitStatus(dwStatus);
    m_strValue = szDefValue;
    m_pfnCalc = pfnCalc;
    m_pfnUpdate = pfnUpdate;
    m_pfnListCalc = pfnListCalc;

    if (wIndex != wLastIndex)
    {
        return ((CTaxDynaListFld*)m_pForm->GetField(m_wID + 1))->Init(wIndex + 1, wLastIndex, dwStatus, szDefValue, pfnCalc, pfnUpdate, pfnListCalc);
    }

    return TRUE;
}

void CTaxDynaListFld::Calculate()
{
    CTaxString strValue;

    try
    {
        (*m_pfnListCalc)(m_pForm->m_pFormMgr, m_pForm, this);

        if (!m_strValue.IsEmpty())
        {
            SetListString(m_strValue);
        }

        if (((m_dwStatus & FLDSTATUS_CALC) != 0) &&
            ((m_dwStatus & FLDSTATUS_OVERRIDDEN) == 0) &&
            (((m_dwStatus & FLDSTATUS_DEFCALC) == 0) ||
             ((m_dwStatus & FLDSTATUS_MODIFIED) == 0)))
        {
            if (((strValue = (*m_pfnCalc)(m_pForm->m_pFormMgr, m_pForm, this)) == m_strValue) ||
                (!m_strDisplay.IsEmpty() && (strValue == m_strDisplay)))
            {
                return;
            }

            SetListString(strValue);
        }

        Update();
    }
    catch (std::runtime_error& e)
    {
        HandleMathException(this, e);
    }
    catch (...)
    {
        HandleMathException(this);
    }
}

void CTaxDynaListFld::SetListTitle(LPCSTR szTitle)
{
    ClearListData();

    m_listData.title = szTitle;
    m_listData.items.clear();
}

void CTaxDynaListFld::SetListItem(LPCSTR szDisplay, LPCSTR szValue)
{
    PicklistItemInfo toAdd;
    toAdd.display = szDisplay;

    if (szValue)
    {
        toAdd.value = szValue;
    }
    else
    {
        toAdd.value = szDisplay;
    }

    m_listData.items.push_back(toAdd);
}

size_t CTaxOldListFld::GetDataSize()
{
    return sizeof(m_dwStatus) + m_strValue.GetLength() + 1;
}

void CTaxOldListFld::GetData(void *lpData)
{
    LPSTR lpTemp = (LPSTR)lpData;
    *((DWORD*)lpTemp) = m_dwStatus;
    lpTemp += sizeof(m_dwStatus);
    strcpy_s(lpTemp, m_strValue.GetLength() + 1, m_strValue);
}

void CTaxOldListFld::SetData(const void *lpData)
{
    LPSTR lpTemp = (LPSTR)lpData;
    SetStatusData(*((DWORD*)lpTemp));
    lpTemp += sizeof(m_dwStatus);
    m_strValue = lpTemp;
}
