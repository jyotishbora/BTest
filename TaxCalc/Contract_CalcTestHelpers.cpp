#include "StdAfx.h"
#include "TaxAct.CalcDll/Contract_CalcTestHelpers.h"
#include "TaxAct.CalcDll/DllDataBuffer.h"

#include "Calcfld.h"
#include "Calcform.h"

#include "rapidjson/document.h"
#include "rapidjson/writer.h"

DLL_EXPORT bool DLL_CALL CalcTestHelpers_ReadFormJson(const TaxFormHandle *form, const char *str)
{
    rapidjson::Document document;
    document.Parse(str);
    return ((CTaxForm *)form->self)->ReadJson(document);
}

DLL_EXPORT bool DLL_CALL CalcTestHelpers_WriteFormJson(const TaxFormHandle *form, const DllDataBufferHandle *out)
{
    rapidjson::StringBuffer buffer;
    buffer.Clear();
    rapidjson::Writer<rapidjson::StringBuffer> writer(buffer);

    if (!((CTaxForm *)form->self)->WriteJson(writer))
    {
        return false;
    }

    TaxAct::CalcDll::DllDataBuffer result(out, false);
    result.SetString(buffer.GetString());

    return true;
}

DLL_EXPORT bool DLL_CALL CalcTestHelpers_ReadFieldJson(const TaxFieldHandle *field, const char *str)
{
    rapidjson::Document document;
    document.Parse(str);
    return ((CTaxField *)field->self)->ReadJson(document);
}

DLL_EXPORT bool DLL_CALL CalcTestHelpers_WriteFieldJson(const TaxFieldHandle *field, const DllDataBufferHandle *out)
{
    rapidjson::StringBuffer buffer;
    buffer.Clear();
    rapidjson::Writer<rapidjson::StringBuffer> writer(buffer);

    if (!((CTaxField *)field->self)->WriteJson(writer))
    {
        return false;
    }

    TaxAct::CalcDll::DllDataBuffer result(out, false);
    result.SetString(buffer.GetString());

    return buffer.GetSize() + 1;
}

DLL_EXPORT void DLL_CALL CalcTestHelpers_RaiseError()
{
    // divide by zero
    volatile int n = 1;
    volatile int d = 0;
    volatile int f = n / d;
}
