#include "StdAfx.h"
#include "TaxAct.CalcDll/Contract_TaxField.h"
#include "TaxAct.CalcDll/DllDataBuffer.h"

#include "Calcfld.h"

#include "icalcmgr.h"
#include "ICALCFRM.H"
#include "ICALCFLD.H"

DLL_EXPORT void DLL_CALL TaxField_Create(taxfieldtype_t type, TaxFieldHandle *out)
{
    ITaxField *result = CTaxField::Create(type);

    if (result)
    {
        *out = result->handle();
    }
}

DLL_EXPORT void DLL_CALL TaxField_Delete(const TaxFieldHandle *handle)
{
    ITaxField *self = (ITaxField*)handle->self;
    delete self;
}

DLL_EXPORT taxfieldid_t DLL_CALL TaxField_GetID(const TaxFieldHandle *handle)
{
    ITaxField *self = (ITaxField*)handle->self;
    return self->GetID();
}

DLL_EXPORT int DLL_CALL TaxField_GetIndex(const TaxFieldHandle *handle)
{
    ITaxField *self = (ITaxField*)handle->self;
    return self->GetIndex();
}

DLL_EXPORT taxfieldtype_t DLL_CALL TaxField_GetType(const TaxFieldHandle *handle)
{
    ITaxField *self = (ITaxField*)handle->self;

	auto type = self->GetType();
	// radio = checkbox+nonzero radio tag
	// radio is no longer directly set in mmf
	if (type == FLDTYPE_CHECK && self->GetForm() && self->GetForm()->GetRadioButtonGroup(self->GetID()) > 0)
	{
		type = FLDTYPE_RADIO;
	}

    return type;
}

DLL_EXPORT void DLL_CALL TaxField_GetTypeAsString(const TaxFieldHandle *handle, const DllDataBufferHandle *out)
{
	ITaxField *self = (ITaxField*)handle->self;

	TaxAct::CalcDll::DllDataBuffer result(out, false);
	
	std::map<WORD, std::string> typeMap = {
		{ FLDTYPE_CURRENCY, "currency" },
		{ FLDTYPE_NUMBER, "number" },
		{ FLDTYPE_DATE, "date" },
		{ FLDTYPE_FLOAT, "float" },
		{ FLDTYPE_RADIO, "radio" },
		{ FLDTYPE_CHECK, "checkbox" },
		{ FLDTYPE_STRING, "string" },
		{ FLDTYPE_SSN, "ssn" },
		{ FLDTYPE_EIN, "ein" },
		{ FLDTYPE_PHONE, "phone" },
		{ FLDTYPE_LIST, "list" },
		{ FLDTYPE_DYNALIST, "dynalist" }
	};

	// use above call that handles radio translation!
	auto type = TaxField_GetType(handle);
	std::string typeStr;

	auto iter = typeMap.find(type);
	if (iter != typeMap.end())
	{
		typeStr = iter->second;
	}
	result.SetString(typeStr);
}

DLL_EXPORT void DLL_CALL TaxField_GetForm(const TaxFieldHandle *handle, TaxFormHandle *out)
{
    ITaxField *self = (ITaxField*)handle->self;
    ITaxForm *result = self->GetForm();

    if (result)
    {
        *out = result->handle();
    }
}

DLL_EXPORT bool DLL_CALL TaxField_GetStatus(const TaxFieldHandle *handle, taxfieldflag_t status)
{
    ITaxField *self = (ITaxField*)handle->self;
    return self->GetStatus(status);
}

DLL_EXPORT void DLL_CALL TaxField_SetStatus(const TaxFieldHandle *handle, taxfieldflag_t status, bool set)
{
    ITaxField *self = (ITaxField*)handle->self;
    self->SetStatus(status, set);
}

DLL_EXPORT void DLL_CALL TaxField_Calculate(const TaxFieldHandle *handle)
{
    ITaxField *self = (ITaxField*)handle->self;
    self->Calculate();
}

DLL_EXPORT int DLL_CALL TaxField_GetNumber(const TaxFieldHandle *handle)
{
    ITaxField *self = (ITaxField*)handle->self;
    return self->GetNumber();
}

DLL_EXPORT int64_t DLL_CALL TaxField_GetCurrency(const TaxFieldHandle *handle)
{
    ITaxField *self = (ITaxField*)handle->self;
    return self->GetCurrency();
}

DLL_EXPORT double DLL_CALL TaxField_GetFloat(const TaxFieldHandle *handle)
{
    ITaxField *self = (ITaxField*)handle->self;
    return self->GetFloat();
}

DLL_EXPORT bool DLL_CALL TaxField_GetBool(const TaxFieldHandle *handle)
{
    ITaxField *self = (ITaxField*)handle->self;
    return self->GetBool();
}

DLL_EXPORT int DLL_CALL TaxField_GetDate(const TaxFieldHandle *handle)
{
    ITaxField *self = (ITaxField*)handle->self;
    return self->GetDate();
}

DLL_EXPORT void DLL_CALL TaxField_GetString(const TaxFieldHandle *handle, const DllDataBufferHandle *out)
{
    ITaxField *self = (ITaxField*)handle->self;

    TaxAct::CalcDll::DllDataBuffer result(out, false);

    std::vector<char> buffer;
    buffer.resize(self->GetStringLength() + 1);
    self->GetString(buffer.data(), buffer.size());

    result.SetString(buffer.data());
}

DLL_EXPORT void DLL_CALL TaxField_SetNumber(const TaxFieldHandle *handle, int value)
{
    ITaxField *self = (ITaxField*)handle->self;
    self->SetNumber(value);
}

DLL_EXPORT void DLL_CALL TaxField_SetCurrency(const TaxFieldHandle *handle, int64_t value)
{
    ITaxField *self = (ITaxField*)handle->self;
    self->SetCurrency(value);
}

DLL_EXPORT void DLL_CALL TaxField_SetFloat(const TaxFieldHandle *handle, double value)
{
    ITaxField *self = (ITaxField*)handle->self;
    self->SetFloat(value);
}

DLL_EXPORT void DLL_CALL TaxField_SetBool(const TaxFieldHandle *handle, bool value)
{
    ITaxField *self = (ITaxField*)handle->self;
    self->SetBool(value);
}

DLL_EXPORT void DLL_CALL TaxField_SetDate(const TaxFieldHandle *handle, int value)
{
    ITaxField *self = (ITaxField*)handle->self;
    self->SetDate(value);
}

DLL_EXPORT void DLL_CALL TaxField_SetString(const TaxFieldHandle *handle, const char *value)
{
    ITaxField *self = (ITaxField*)handle->self;
    self->SetString(value);
}

DLL_EXPORT long DLL_CALL TaxField_GetMinNumber(const TaxFieldHandle* handle)
{
	ITaxField* self = (ITaxField*)handle->self;
	return self->GetMinNumber();
}

DLL_EXPORT long DLL_CALL TaxField_GetMaxNumber(const TaxFieldHandle* handle)
{
	ITaxField* self = (ITaxField*)handle->self;
	return self->GetMaxNumber();
}

DLL_EXPORT int64_t DLL_CALL TaxField_GetMinCurrency(const TaxFieldHandle* handle)
{
	ITaxField* self = (ITaxField*)handle->self;
	return self->GetMinCurrency();
}

DLL_EXPORT int64_t DLL_CALL TaxField_GetMaxCurrency(const TaxFieldHandle* handle)
{
	ITaxField* self = (ITaxField*)handle->self;
	return self->GetMaxCurrency();
}

DLL_EXPORT double DLL_CALL TaxField_GetMinFloat(const TaxFieldHandle* handle)
{
	ITaxField* self = (ITaxField*)handle->self;
	return self->GetMinFloat();
}

DLL_EXPORT double DLL_CALL TaxField_GetMaxFloat(const TaxFieldHandle* handle)
{
	ITaxField* self = (ITaxField*)handle->self;
	return self->GetMaxFloat();
}

DLL_EXPORT int DLL_CALL TaxField_GetMaxLength(const TaxFieldHandle* handle)
{
	ITaxField* self = (ITaxField*)handle->self;
	return self->GetMaxLength();
}

DLL_EXPORT int DLL_CALL TaxField_GetListTotal(const TaxFieldHandle* handle)
{
	ITaxField* self = (ITaxField*)handle->self;
	return self->GetListTotal();
}

DLL_EXPORT void DLL_CALL TaxField_GetListString(const TaxFieldHandle* handle, const int index, const DllDataBufferHandle* out)
{
	ITaxField* self = (ITaxField*)handle->self;

	TaxAct::CalcDll::DllDataBuffer result(out, false);

	std::vector<char> buffer;
	buffer.resize(256);
	self->GetListString(index, buffer.data(), buffer.size());

	result.SetString(buffer.data());
}

DLL_EXPORT void DLL_CALL TaxField_GetListStringDisplay(const TaxFieldHandle* handle, const int index, const DllDataBufferHandle* out)
{
	ITaxField* self = (ITaxField*)handle->self;

	TaxAct::CalcDll::DllDataBuffer result(out, false);

	std::vector<char> buffer;
	buffer.resize(256);
	self->GetListStringDisplay(index, buffer.data(), buffer.size());

	result.SetString(buffer.data());
}

DLL_EXPORT void DLL_CALL TaxField_GetListStringTitle(const TaxFieldHandle* handle, const DllDataBufferHandle* out)
{
	ITaxField* self = (ITaxField*)handle->self;

	TaxAct::CalcDll::DllDataBuffer result(out, false);

	std::vector<char> buffer;
	buffer.resize(256);
	self->GetListStringTitle(buffer.data(), buffer.size());

	result.SetString(buffer.data());
}

DLL_EXPORT long DLL_CALL TaxField_GetMinDate(const TaxFieldHandle* handle)
{
	ITaxField* self = (ITaxField*)handle->self;
	return self->GetMinDate();
}

DLL_EXPORT long DLL_CALL TaxField_GetMaxDate(const TaxFieldHandle* handle)
{
	ITaxField* self = (ITaxField*)handle->self;
	return self->GetMaxDate();
}

DLL_EXPORT long DLL_CALL TaxField_GetDefYear(const TaxFieldHandle* handle)
{
	ITaxField* self = (ITaxField*)handle->self;
	return self->GetDefYear();
}

DLL_EXPORT uint16_t DLL_CALL TaxField_GetStringType(const TaxFieldHandle* handle)
{
	ITaxField* self = (ITaxField*)handle->self;
	return self->GetStringType();
}

DLL_EXPORT void DLL_CALL TaxField_GetStringTypeAsString(const TaxFieldHandle *handle, const DllDataBufferHandle *out)
{
	ITaxField *self = (ITaxField*)handle->self;

	TaxAct::CalcDll::DllDataBuffer result(out, false);

	std::map<WORD, std::string> subtypeMap = {
		{ STRINGTYPE_NONE, "none" },
		{ STRINGTYPE_BLOCKNUMBERS, "nonumbers" },
		{ STRINGTYPE_NUMBERSONLY, "numbersonly" },
		{ STRINGTYPE_ZIPCODE, "zipcode" },
		{ STRINGTYPE_ALPHAONLY, "alphaonly" },
		{ STRINGTYPE_EMAIL, "email" },
		{ STRINGTYPE_PIN, "pin" },
		{ STRINGTYPE_ALPHANUMERIC, "alphanumeric" },
		{ STRINGTYPE_PASSWORD, "password" },
		{ STRINGTYPE_PTIN, "ptin" },
		{ STRINGTYPE_ALPHANUMERIC_4_4_4_4, "alphanumeric_4_4_4_4" },
		{ STRINGTYPE_RTN, "rtn" }
	};

	auto type = self->GetStringType();
	std::string subtypeStr;
	auto iter = subtypeMap.find(type);
	if (iter != subtypeMap.end())
	{
		subtypeStr = iter->second;
	}
	result.SetString(subtypeStr);
}

DLL_EXPORT int DLL_CALL TaxField_GetListIndex(const TaxFieldHandle* handle)
{
    ITaxField *self = (ITaxField*)handle->self;
    return self->GetListIndex();
}
DLL_EXPORT void DLL_CALL TaxField_SetListIndex(const TaxFieldHandle *handle, int iIndex)
{
    ITaxField *self = (ITaxField *)handle->self;
    return self->SetListIndex(iIndex);
}