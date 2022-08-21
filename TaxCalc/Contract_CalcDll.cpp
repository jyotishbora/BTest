#include "StdAfx.h"
#include "TaxAct.CalcDll/Contract_CalcDll.h"
#include "TaxAct.CalcDll/DllDataBuffer.h"
#include "TaxAct.CalcDll/DllDataBufferImpl.h"

#include "CALCINFO.H"
#include "CommonConst.h"
#include "CalcStaticData.h"
#include <map>
#include <string>

DLL_EXPORT bool DLL_CALL CalcDll_InitStaticData(const char *filename)
{
    return InitStaticData(filename);
}

#define STR_CONST_PAIR(Name) {#Name, Name}

DLL_EXPORT taxformcopy_t DLL_CALL CalcDll_GetFormCopyConstant(const char *name)
{
    static const std::map<std::string, WORD> g_formCopyConstants = {
        STR_CONST_PAIR(COPY_NEW),
        STR_CONST_PAIR(COPY_CURRENT),
        STR_CONST_PAIR(COPY_REFERENCE),
        STR_CONST_PAIR(COPY_ALLCOPIES),
        STR_CONST_PAIR(COPY_EXISTCOPIES),
        STR_CONST_PAIR(COPY_ALLCHILDCOPIES),
        STR_CONST_PAIR(COPY_EXISTCHILDCOPIES),
        STR_CONST_PAIR(COPY_CHILD),
        STR_CONST_PAIR(COPY_PARENT),
        STR_CONST_PAIR(COPY_USER),
    };

    auto find = g_formCopyConstants.find(name);
    if (find != g_formCopyConstants.end())
    {
        return find->second;
    }
    else
    {
        return 0;
    }
}

DLL_EXPORT taxformflag_t DLL_CALL CalcDll_GetFormFlagConstant(const char *name)
{
    static const std::map<std::string, DWORD> g_formFlagConstants = {
        STR_CONST_PAIR(FORMSTATUS_TEMPORARY),
        STR_CONST_PAIR(FORMSTATUS_REQUIRED),
        STR_CONST_PAIR(FORMSTATUS_LISTFORMS),
        STR_CONST_PAIR(FORMSTATUS_LISTDOCUMENTS),
        STR_CONST_PAIR(FORMSTATUS_LISTWORKSHEETS),
        STR_CONST_PAIR(FORMSTATUS_AUTOCREATE),
        STR_CONST_PAIR(FORMSTATUS_LISTHIDDEN),
        STR_CONST_PAIR(FORMSTATUS_HASTRIGGERFIELD),
        STR_CONST_PAIR(FORMSTATUS_PREPARER),
        STR_CONST_PAIR(FORMSTATUS_PRINT),
        STR_CONST_PAIR(FORMSTATUS_LISTPLANNERS),
        STR_CONST_PAIR(FORMSTATUS_DLXPREPARER),
        STR_CONST_PAIR(FORMSTATUS_FREETOPRINT),
        STR_CONST_PAIR(FORMSTATUS_LISTINFORMATION),
        STR_CONST_PAIR(FORMSTATUS_REFERENCE),
        STR_CONST_PAIR(FORMSTATUS_OPENED),
        STR_CONST_PAIR(FORMSTATUS_MODIFIED),
        STR_CONST_PAIR(FORMSTATUS_IMPORTED),
        STR_CONST_PAIR(FORMSTATUS_USERMODIFIED),
        STR_CONST_PAIR(FORMSTATUS_ONLINEFILLABLE),
        STR_CONST_PAIR(FORMSTATUS_PDFIMPORTED),
        STR_CONST_PAIR(FORMSTATUS_OCRIMPORTED),
    };

    auto find = g_formFlagConstants.find(name);
    if (find != g_formFlagConstants.end())
    {
        return find->second;
    }
    else
    {
        return 0;
    }
}

DLL_EXPORT taxfieldtype_t DLL_CALL CalcDll_GetFieldTypeConstant(const char *name)
{
    static const std::map<std::string, WORD> g_fieldTypeConstants = {
        STR_CONST_PAIR(FLDTYPE_CURRENCY),
        STR_CONST_PAIR(FLDTYPE_NUMBER),
        STR_CONST_PAIR(FLDTYPE_DATE),
        STR_CONST_PAIR(FLDTYPE_FLOAT),
        STR_CONST_PAIR(FLDTYPE_RADIO),
        STR_CONST_PAIR(FLDTYPE_CHECK),
        STR_CONST_PAIR(FLDTYPE_STRING),
        STR_CONST_PAIR(FLDTYPE_SSN),
        STR_CONST_PAIR(FLDTYPE_EIN),
        STR_CONST_PAIR(FLDTYPE_PHONE),
        STR_CONST_PAIR(FLDTYPE_OLDLIST),
        STR_CONST_PAIR(FLDTYPE_LIST),
        STR_CONST_PAIR(FLDTYPE_DYNALIST),
    };

    auto find = g_fieldTypeConstants.find(name);
    if (find != g_fieldTypeConstants.end())
    {
        return find->second;
    }
    else
    {
        return 0;
    }
}

DLL_EXPORT taxfieldflag_t DLL_CALL CalcDll_GetFieldFlagConstant(const char *name)
{
    static const std::map<std::string, DWORD> g_fieldFlagConstants = {
        STR_CONST_PAIR(FLDSTATUS_PROTECTED),
        STR_CONST_PAIR(FLDSTATUS_CALC),
        STR_CONST_PAIR(FLDSTATUS_DEFCALC),
        STR_CONST_PAIR(FLDSTATUS_HIDDEN),
        STR_CONST_PAIR(FLDSTATUS_SPAWN),
        STR_CONST_PAIR(FLDSTATUS_STOREPENNIES),
        STR_CONST_PAIR(FLDSTATUS_ROUNDPENNIES),
        STR_CONST_PAIR(FLDSTATUS_FORCEPENNIES),
        STR_CONST_PAIR(FLDSTATUS_TEMPORARY),
        STR_CONST_PAIR(FLDSTATUS_PREPARERONLY),
        STR_CONST_PAIR(FLDSTATUS_NOSTRINGS),
        STR_CONST_PAIR(FLDSTATUS_CREATEFORM),
        STR_CONST_PAIR(FLDSTATUS_EFILEDETAILS),
        STR_CONST_PAIR(FLDSTATUS_QUICKENTRY),
        STR_CONST_PAIR(FLDSTATUS_SPAWNLINK),
        STR_CONST_PAIR(FLDSTATUS_PREPARERONLYINFO),
        STR_CONST_PAIR(FLDSTATUS_QUICKCONVERT),
        STR_CONST_PAIR(FLDSTATUS_OVERRIDDEN),
        STR_CONST_PAIR(FLDSTATUS_MODIFIED),
        STR_CONST_PAIR(FLDSTATUS_ESTIMATE),
        STR_CONST_PAIR(FLDSTATUS_IMPORTED),
        STR_CONST_PAIR(FLDSTATUS_USERMODIFIED),
        STR_CONST_PAIR(FLDSTATUS_PDFIMPORTED),
        STR_CONST_PAIR(FLDSTATUS_HASDETAILS),
    };

    auto find = g_fieldFlagConstants.find(name);
    if (find != g_fieldFlagConstants.end())
    {
        return find->second;
    }
    else
    {
        return 0;
    }
}

DLL_EXPORT void DLL_CALL CalcDll_GetModuleName(const DllDataBufferHandle *out)
{
    TaxAct::CalcDll::DllDataBuffer buffer(out, false);
    buffer.LoadFromHandle(out->dll);
    buffer.SetString(MODULE_NAME);
}

DLL_EXPORT void DLL_CALL CalcDll_GetModuleDateTime(const DllDataBufferHandle *out)
{
    TaxAct::CalcDll::DllDataBuffer buffer(out, false);
    buffer.SetString(MODULE_DATETIME);
}

DLL_EXPORT void DLL_CALL CalcDll_GetModuleTitle(const DllDataBufferHandle *out)
{
    TaxAct::CalcDll::DllDataBuffer buffer(out, false);
    buffer.SetString(MODULE_TITLE);
}

DLL_EXPORT void DLL_CALL CalcDll_GetTaxYear(const DllDataBufferHandle *out)
{
    TaxAct::CalcDll::DllDataBuffer buffer(out, false);
    buffer.SetString(kAPP_YEAR);
}

DLL_EXPORT void DLL_CALL CalcDll_GetTaxType(const DllDataBufferHandle *out)
{
    TaxAct::CalcDll::DllDataBuffer buffer(out, false);

#if CALC1040
    buffer.SetString("1040");
#elif CALCPARTNER
    buffer.SetString("1065");
#elif CALCCCORP
    buffer.SetString("1120");
#elif CALCSCORP
    buffer.SetString("1120S");
#elif CALCESTATES
    buffer.SetString("1041");
#elif CALCEXEMPT
    buffer.SetString("990");
#else
    buffer.SetString("");
#endif
}

DLL_EXPORT bool DLL_CALL CalcDll_IsFederal()
{
#ifdef CALCFEDERAL
    return true;
#else
    return false;
#endif
}

DLL_EXPORT bool DLL_CALL CalcDll_IsState()
{
#ifdef CALCSTATE
    return true;
#else
    return false;
#endif
}

DLL_EXPORT int DLL_CALL CalcDll_GetTotalForms()
{
    return FORM_TOTALFORMS;
}

DLL_EXPORT taxformid_t DLL_CALL CalcDll_GetFormID(const char *formName)
{
    return GetCachedFormID(formName);
}

DLL_EXPORT void DLL_CALL CalcDll_GetFormName(taxformid_t formID, const DllDataBufferHandle *out)
{
    ASSERT(formID > 0);
    if (formID > 0)
    {
        TaxAct::CalcDll::DllDataBuffer buffer(out, false);
        buffer.SetString(g_calcStaticData.forms[formID - 1].name.c_str());
    }
}

DLL_EXPORT int DLL_CALL CalcDll_GetFormTotalFields(taxformid_t formID)
{
    ASSERT(formID > 0);
    if (formID > 0)
    {
        return g_calcStaticData.forms[formID - 1].totalFields;
    }

    return 0;
}

DLL_EXPORT taxfieldid_t DLL_CALL CalcDll_GetFieldID(taxformid_t formID, const char *fieldName, int fieldIndex)
{
    return GetCachedFieldID(formID, fieldName, fieldIndex);
}

DLL_EXPORT void DLL_CALL CalcDll_GetFieldName(taxformid_t formID, taxfieldid_t fieldID, const DllDataBufferHandle *out)
{
    ASSERT(formID > 0);
    ASSERT(fieldID > 0);
    if ((formID > 0) && (fieldID > 0))
    {
        TaxAct::CalcDll::DllDataBuffer buffer(out, false);
        buffer.SetString(g_calcStaticData.forms[formID - 1].fields[fieldID - 1].name.c_str());
    }
}

DLL_EXPORT void DLL_CALL CalcDll_GetFormFieldMapJson(const DllDataBufferHandle *out)
{
    TaxAct::CalcDll::DllDataBuffer buffer(out, false);
    buffer.SetString(GetFormFieldMapJson());
}

DLL_EXPORT void DLL_CALL CalcDll_GetCustomFieldMapJson(const DllDataBufferHandle *out)
{
    TaxAct::CalcDll::DllDataBuffer buffer(out, false);
    buffer.SetString(GetCustomFieldMapJson());
}

void CalcDll_ExportDllDataBuffer()
{
    // placeholder so the linker includes DllDataBuffer callbacks
    DllDataBufferImpl impl;
}
