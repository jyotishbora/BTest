#include "StdAfx.h"
#include "TaxAct.CalcDll/Contract_TaxForm.h"
#include "TaxAct.CalcDll/DllDataBuffer.h"

#include "Calcform.h"

#include "icalcmgr.h"
#include "ICALCFRM.H"
#include "ICALCFLD.H"

DLL_EXPORT void DLL_CALL TaxForm_Create(TaxFormHandle *out)
{
    ITaxForm *result = new CTaxForm();

    if (result)
    {
        *out = result->handle();
    }
}

DLL_EXPORT void DLL_CALL TaxForm_Delete(const TaxFormHandle *handle)
{
    ITaxForm *self = (ITaxForm*)handle->self;
    delete self;
}

DLL_EXPORT void DLL_CALL TaxForm_GetFormManager(const TaxFormHandle *handle, TaxFormManagerHandle *out)
{
    ITaxForm *self = (ITaxForm*)handle->self;
    ITaxFormManager *result = self->GetFormManager();

    if (result)
    {
        *out = result->handle();
    }
}

DLL_EXPORT taxformid_t DLL_CALL TaxForm_GetID(const TaxFormHandle *handle)
{
    ITaxForm *self = (ITaxForm*)handle->self;
    return self->GetID();
}

DLL_EXPORT taxformid_t DLL_CALL TaxForm_GetCopyID(const TaxFormHandle *handle)
{
    ITaxForm *self = (ITaxForm*)handle->self;
    return self->GetCopyID();
}

DLL_EXPORT int DLL_CALL TaxForm_GetCopyIndex(const TaxFormHandle *handle)
{
    ITaxForm *self = (ITaxForm*)handle->self;
    return self->GetCopyIndex();
}

DLL_EXPORT void DLL_CALL TaxForm_GetParent(const TaxFormHandle *handle, TaxFormHandle *out)
{
    ITaxForm *self = (ITaxForm*)handle->self;
    ITaxForm *result = self->GetParent();

    if (result)
    {
        *out = result->handle();
    }
}

DLL_EXPORT bool DLL_CALL TaxForm_GetStatus(const TaxFormHandle *handle, taxformflag_t status)
{
    ITaxForm *self = (ITaxForm*)handle->self;
    return self->GetStatus(status);
}

DLL_EXPORT void DLL_CALL TaxForm_SetStatus(const TaxFormHandle *handle, taxformflag_t status, bool set)
{
    ITaxForm *self = (ITaxForm*)handle->self;
    self->SetStatus(status, set);
}

DLL_EXPORT int DLL_CALL TaxForm_GetTotalFields(const TaxFormHandle *handle)
{
    ITaxForm *self = (ITaxForm*)handle->self;
    return self->GetTotalFields();
}

DLL_EXPORT void DLL_CALL TaxForm_GetField(const TaxFormHandle *handle, taxfieldid_t fieldID, TaxFieldHandle *out)
{
    ITaxForm *self = (ITaxForm*)handle->self;
    ITaxField *result = self->GetField(fieldID);

    if (result)
    {
        *out = result->handle();
    }
}

DLL_EXPORT void DLL_CALL TaxForm_CalculateAllFields(const TaxFormHandle *handle)
{
    ITaxForm *self = (ITaxForm*)handle->self;
    self->CalculateAllFields();
}

DLL_EXPORT uint16_t DLL_CALL TaxForm_GetRadioButtonGroup(const TaxFormHandle *handle, const taxfieldid_t fieldId)
{
	ITaxForm *self = (ITaxForm*)handle->self;
	return self->GetRadioButtonGroup(fieldId);
}

DLL_EXPORT void DLL_CALL TaxForm_GetDescription(const TaxFormHandle* handle, const DllDataBufferHandle* out)
{
	ITaxForm* self = (ITaxForm*)handle->self;

	char buffer[256];

	self->GetDescription(buffer, 256);

	TaxAct::CalcDll::DllDataBuffer result(out, false);
	result.SetString(buffer);
}