#include "StdAfx.h"
#include "CalcResource.h"

#include "CalcStaticData.h"
#include "CALCINFO.H"
#include "Calcmgr.h"
#include "Calcfunc.h"

CALC_EXPORT void GetModuleName(LPSTR szName)
{
    strcpy_s(szName, std::char_traits<char>::length(MODULE_NAME) + 1, MODULE_NAME);
}

CALC_EXPORT void GetModuleDateTime(LPSTR szDateTime)
{
    strcpy_s(szDateTime, std::char_traits<char>::length(MODULE_DATETIME) + 1, MODULE_DATETIME);
}

CALC_EXPORT void GetModuleTitle(LPSTR szTitle)
{
    strcpy_s(szTitle, std::char_traits<char>::length(MODULE_TITLE ) + 1, MODULE_TITLE);
}

CALC_EXPORT WORD GetTotalForms()
{
    return FORM_TOTALFORMS;
}

CALC_EXPORT WORD GetTotalFields(WORD wFormID)
{
    ASSERT(wFormID > 0);
    return g_calcStaticData.forms[wFormID - 1].totalFields;
}

CALC_EXPORT BOOL GetStatus(WORD wFormID, DWORD dwStatus)
{
    ASSERT(wFormID > 0);
    return ((g_calcStaticData.forms[wFormID - 1].flags & dwStatus) == dwStatus);
}

CALC_EXPORT WORD GetFormListOrder(WORD wFormID, DWORD dwListStatus)
{
    if (!GetStatus(wFormID, dwListStatus))
    {
        return 0;
    }

    return g_calcStaticData.forms[wFormID - 1].listOrder;
}

CALC_EXPORT void GetFormName(LPSTR szName, WORD wFormID)
{
    ASSERT(wFormID > 0);
    const char *name = g_calcStaticData.forms[wFormID - 1].name.c_str();
    strcpy_s(szName, std::char_traits<char>::length(name) + 1, name);
}

CALC_EXPORT void GetFieldName(LPSTR szName, WORD wFormID, WORD wFieldID)
{
    ASSERT(wFormID > 0);
    ASSERT(wFieldID > 0);
    const char *name = g_calcStaticData.forms[wFormID - 1].fields[wFieldID - 1].name.c_str();
    strcpy_s(szName, std::char_traits<char>::length(name) + 1, name);
}

CALC_EXPORT void GetShortFormName(LPSTR szName, WORD wFormID)
{
    ASSERT(wFormID > 0);
    const char *name = g_calcStaticData.forms[wFormID - 1].shortName.c_str();
    strcpy_s(szName, std::char_traits<char>::length(name) + 1, name);
}

CALC_EXPORT void GetLongFormName(LPSTR szName, WORD wFormID)
{
    ASSERT(wFormID > 0);
    const char *name = g_calcStaticData.forms[wFormID - 1].longName.c_str();
    strcpy_s(szName, std::char_traits<char>::length(name) + 1, name);
}

CALC_EXPORT void GetTabName(LPSTR szName, WORD wFormID)
{
    ASSERT(wFormID > 0);
    const char* name = g_calcStaticData.forms[wFormID - 1].tabName.c_str();
    strcpy_s(szName, std::char_traits<char>::length(name) + 1, name);
}

CALC_EXPORT WORD GetDescriptionFieldID(WORD wFormID)
{
    ASSERT(wFormID > 0);
    return g_calcStaticData.forms[wFormID - 1].descriptionFieldID;
}

CALC_EXPORT WORD GetProDescriptionFieldID(WORD wFormID)
{
    ASSERT(wFormID > 0);
    return g_calcStaticData.forms[wFormID - 1].proDescriptionFieldID;
}

CALC_EXPORT bool GetFormFieldMapJson(DllStringBuffer *out)
{
    if (out)
    {
        out->SetData(GetFormFieldMapJson().c_str());
        return true;
    }

    return false;
}

CALC_EXPORT bool GetCustomFieldMapJson(DllStringBuffer *out)
{
    if (out)
    {
        out->SetData(GetCustomFieldMapJson().c_str());
        return true;
    }

    return false;
}

CALC_EXPORT Tax::DisabledFeaturesCore* CreateDisabledFeaturesCore()
{
    Tax::DisabledFeaturesCore* result = new Tax::DisabledFeaturesCore();
    if (result->loadFeatures(g_calcStaticData.fedDisabledFeatureFile))
    {
        return result;
    }
    else
    {
        DeleteDisabledFeaturesCore(result);
        return nullptr;
    }
}

CALC_EXPORT void DeleteDisabledFeaturesCore(Tax::DisabledFeaturesCore* obj)
{
    delete obj;
}
