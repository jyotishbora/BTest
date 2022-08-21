#include "StdAfx.h"
#include "TaxAct.CalcDll/Contract_TaxFormManager.h"
#include "TaxAct.CalcDll/DllDataBuffer.h"

#include "Calcmgr.h"

#include "icalcmgr.h"
#include "ICALCFRM.H"
#include "ICALCFLD.H"
#include "AutoAttachments.h"

DLL_EXPORT void DLL_CALL TaxFormManager_Create(TaxFormManagerHandle *out)
{
    ITaxFormManager *result = new CTaxFormManager();

    if (result)
    {
        *out = result->handle();
    }
}

DLL_EXPORT void DLL_CALL TaxFormManager_Delete(const TaxFormManagerHandle *handle)
{
    ITaxFormManager *self = (ITaxFormManager*)handle->self;
    delete self;
}

DLL_EXPORT bool DLL_CALL TaxFormManager_Init(const TaxFormManagerHandle *handle)
{
    ITaxFormManager *self = (ITaxFormManager*)handle->self;
    return self->Init();
}

DLL_EXPORT bool DLL_CALL TaxFormManager_InitForms(const TaxFormManagerHandle *handle)
{
    ITaxFormManager *self = (ITaxFormManager*)handle->self;
    return self->InitForms();
}

DLL_EXPORT void DLL_CALL TaxFormManager_DeleteForms(const TaxFormManagerHandle *handle)
{
    ITaxFormManager *self = (ITaxFormManager*)handle->self;
    self->DeleteForms();
}

DLL_EXPORT void DLL_CALL TaxFormManager_CreateForm(const TaxFormManagerHandle *handle, taxformid_t formID, bool calculate, const TaxFormHandle *parent, TaxFormHandle *out)
{
    ITaxFormManager *self = (ITaxFormManager*)handle->self;

    ITaxForm *pForm = nullptr;
    if (parent)
    {
        pForm = (ITaxForm *)parent->self;
    }

    ITaxForm *result = self->CreateForm(formID, calculate, pForm);

    if (result)
    {
        *out = result->handle();
    }
}

DLL_EXPORT void DLL_CALL TaxFormManager_GetForm(const TaxFormManagerHandle *handle, taxformid_t formID, taxformcopy_t formCopyID, TaxFormHandle *out)
{
    ITaxFormManager *self = (ITaxFormManager*)handle->self;
    ITaxForm *result = self->GetForm(formID, formCopyID);

    if (result)
    {
        *out = result->handle();
    }
}

DLL_EXPORT void DLL_CALL TaxFormManager_GetFormByIndex(const TaxFormManagerHandle *handle, taxformid_t formID, int formIndex, TaxFormHandle *out)
{
    ITaxFormManager *self = (ITaxFormManager*)handle->self;
    ITaxForm *result = self->GetFormByIndex(formID, formIndex);

    if (result)
    {
        *out = result->handle();
    }
}

DLL_EXPORT int DLL_CALL TaxFormManager_GetFormTotalCopies(const TaxFormManagerHandle *handle, taxformid_t formID)
{
    ITaxFormManager *self = (ITaxFormManager*)handle->self;
    return self->GetTotalCopies(formID);
}

DLL_EXPORT void DLL_CALL TaxFormManager_DeleteFormAndChildForms(const TaxFormManagerHandle *handle, const TaxFormHandle *form, bool suspendCalculations)
{
    ITaxFormManager *self = (ITaxFormManager*)handle->self;

    ITaxForm *pForm = nullptr;
    if (form)
    {
        pForm = (ITaxForm *)form->self;
    }

    self->DeleteFormAndChildForms(pForm, suspendCalculations);
}

DLL_EXPORT void DLL_CALL TaxFormManager_CalculateAllForms(const TaxFormManagerHandle *handle)
{
    ITaxFormManager *self = (ITaxFormManager*)handle->self;
    self->CalculateAllForms();
}

DLL_EXPORT void DLL_CALL TaxFormManager_AttachFederalFormMgr(const TaxFormManagerHandle *handle, const TaxFormManagerHandle *formMgr)
{
    ITaxFormManager *self = (ITaxFormManager*)handle->self;

    ITaxFormManager *pFormMgr = nullptr;
    if (formMgr)
    {
        pFormMgr = (ITaxFormManager *)formMgr->self;
    }

    self->AttachFederalFormMgr(pFormMgr);
}

DLL_EXPORT void DLL_CALL TaxFormManager_GetFederalFormMgr(const TaxFormManagerHandle *handle, TaxFormManagerHandle *out)
{
    ITaxFormManager *self = (ITaxFormManager*)handle->self;
    ITaxFormManager *result = self->GetFedFormManager();

    if (result)
    {
        *out = result->handle();
    }
}

DLL_EXPORT void DLL_CALL TaxFormManager_AttachStateFormMgr(const TaxFormManagerHandle *handle, const TaxFormManagerHandle *formMgr)
{
    ITaxFormManager *self = (ITaxFormManager*)handle->self;

    ITaxFormManager *pFormMgr = nullptr;
    if (formMgr)
    {
        pFormMgr = (ITaxFormManager *)formMgr->self;
    }

    self->AttachStateFormMgr(pFormMgr);
}

DLL_EXPORT void DLL_CALL TaxFormManager_DetachStateFormMgr(const TaxFormManagerHandle *handle, const TaxFormManagerHandle *formMgr)
{
    ITaxFormManager *self = (ITaxFormManager*)handle->self;

    ITaxFormManager *pFormMgr = nullptr;
    if (formMgr)
    {
        pFormMgr = (ITaxFormManager *)formMgr->self;
    }

    self->DetachStateFormMgr(pFormMgr);
}

DLL_EXPORT void DLL_CALL TaxFormManager_GetCustomField(const TaxFormManagerHandle *handle, const char *name, TaxFieldHandle *out)
{
    ITaxFormManager *self = (ITaxFormManager*)handle->self;
    ITaxField *result = self->GetCustomField(name);

    if (result)
    {
        *out = result->handle();
    }
}

DLL_EXPORT void DLL_CALL TaxFormManager_GetCustomFieldByIndex(const TaxFormManagerHandle *handle, const char *name, int formIndex, TaxFieldHandle *out)
{
    ITaxFormManager *self = (ITaxFormManager*)handle->self;
    ITaxField *result = self->GetCustomFieldByIndex(name, formIndex);

    if (result)
    {
        *out = result->handle();
    }
}

DLL_EXPORT void DLL_CALL TaxFormManager_ClearProductFlags(const TaxFormManagerHandle *handle)
{
    ITaxFormManager *self = (ITaxFormManager*)handle->self;
    self->ClearProductFlags();
}

DLL_EXPORT void DLL_CALL TaxFormManager_AddProductFlag(const TaxFormManagerHandle *handle, const char *str)
{
    ITaxFormManager *self = (ITaxFormManager*)handle->self;
    self->AddProductFlag(str);
}

DLL_EXPORT bool DLL_CALL TaxFormManager_HasProductFlag(const TaxFormManagerHandle *handle, const char *str)
{
    ITaxFormManager *self = (ITaxFormManager*)handle->self;
    return self->HasProductFlag(str);
}

DLL_EXPORT void DLL_CALL TaxFormManager_ClearPricingInfo(const TaxFormManagerHandle *handle)
{
    ITaxFormManager *self = (ITaxFormManager*)handle->self;
    self->ClearPricingInfo();
}

DLL_EXPORT void DLL_CALL TaxFormManager_SetPricingInfo(const TaxFormManagerHandle *handle, const char *str, long long amt)
{
    ITaxFormManager *self = (ITaxFormManager*)handle->self;
    self->SetPricingInfo(str, amt);
}

DLL_EXPORT long long DLL_CALL TaxFormManager_GetPricingInfo(const TaxFormManagerHandle *handle, const char *str)
{
    ITaxFormManager *self = (ITaxFormManager*)handle->self;
    return self->GetPricingInfo(str);
}

DLL_EXPORT bool DLL_CALL TaxFormManager_ReadJson(const TaxFormManagerHandle *handle, const char *in)
{
    ITaxFormManager *self = (ITaxFormManager*)handle->self;
    return self->ReadJson(in);
}

DLL_EXPORT bool DLL_CALL TaxFormManager_WriteJson(const TaxFormManagerHandle *handle, const DllDataBufferHandle *out)
{
    ITaxFormManager *self = (ITaxFormManager*)handle->self;

    std::unique_ptr<DllStringBuffer> buffer(CreateDllStringBuffer());

    if (self->WriteJson(buffer.get()))
    {
        TaxAct::CalcDll::DllDataBuffer result(out, false);
        result.SetString(buffer->GetData());
        return true;
    }

    return false;
}

DLL_EXPORT bool DLL_CALL TaxFormManager_GetMathGlobalConstList(const TaxFormManagerHandle* handle,
                                                      const DllDataBufferHandle* out)
{
	ITaxFormManager *self = (ITaxFormManager*)handle->self;

	std::unique_ptr<DllStringBuffer> buffer(CreateDllStringBuffer());

	self->getMathGlobalConstList(*buffer);
	if (buffer.get())
	{
		TaxAct::CalcDll::DllDataBuffer result(out, false);
		result.SetString(buffer->GetData());
		return true;
	}
	return false;
}

DLL_EXPORT bool DLL_CALL TaxFormManager_HasParent(const TaxFormManagerHandle* handle, taxformid_t formId)
{
	ITaxFormManager* self = (ITaxFormManager*)handle->self;
	return self->HasParent(formId);
}

DLL_EXPORT bool DLL_CALL TaxFormManager_HasFedParent(const TaxFormManagerHandle* handle, taxformid_t formId)
{
	ITaxFormManager* self = (ITaxFormManager*)handle->self;
	return self->HasFedParent(formId);
}

DLL_EXPORT void DLL_CALL TaxFormManager_GetFormShortName(const TaxFormManagerHandle* handle, taxformid_t formId, const DllDataBufferHandle* out)
{
	ITaxFormManager* self = (ITaxFormManager*)handle->self;

	char buffer[256];

	self->GetShortFormName(buffer, formId);

	TaxAct::CalcDll::DllDataBuffer result(out, false);
	result.SetString(buffer);
}

DLL_EXPORT void DLL_CALL TaxFormManager_GetFormLongName(const TaxFormManagerHandle* handle, taxformid_t formId, const DllDataBufferHandle* out)
{
	ITaxFormManager* self = (ITaxFormManager*)handle->self;

	char buffer[256];

	self->GetLongFormName(buffer, formId);

	TaxAct::CalcDll::DllDataBuffer result(out, false);
	result.SetString(buffer);
}

DLL_EXPORT void DLL_CALL TaxFormManager_GetTabName(const TaxFormManagerHandle* handle, taxformid_t formId, const DllDataBufferHandle* out)
{
    ITaxFormManager* self = (ITaxFormManager*)handle->self;

    char buffer[256];

    self->GetTabName(buffer, formId);

    TaxAct::CalcDll::DllDataBuffer result(out, false);
    result.SetString(buffer);
}

DLL_EXPORT int DLL_CALL TaxFormManager_GetFedMaxChildCopies(const TaxFormManagerHandle *handle, taxformid_t formID, taxformid_t parentFormID)
{
	ITaxFormManager *self = (ITaxFormManager*)handle->self;
	return self->GetFedMaxChildCopies(parentFormID, formID);

}

DLL_EXPORT int DLL_CALL TaxFormManager_GetMaxChildCopies(const TaxFormManagerHandle *handle, taxformid_t formID, taxformid_t parentFormID)
{
	ITaxFormManager *self = (ITaxFormManager*)handle->self;
	return self->GetMaxChildCopies(parentFormID, formID);
}

DLL_EXPORT int DLL_CALL TaxFormManager_GetMaxCopies(const TaxFormManagerHandle *handle, taxformid_t formID)
{
	ITaxFormManager *self = (ITaxFormManager*)handle->self;
	return self->GetMaxCopies(formID);
}

DLL_EXPORT void DLL_CALL TaxFormManager_GetChildCopy(const TaxFormManagerHandle *handle, taxformid_t formID, const TaxFormHandle *parent, int copyID, TaxFormHandle *out)
{
	ITaxFormManager *self = (ITaxFormManager*)handle->self;
	ITaxForm *formParent = (ITaxForm*)parent->self;
	ITaxForm *result = self->GetChildCopy(formParent, formID, copyID);

	if (result)
	{
		*out = result->handle();
	}
}

DLL_EXPORT bool DLL_CALL TaxFormManager_IsChildForm(const TaxFormManagerHandle *handle, taxformid_t parentFormID, taxformid_t formID)
{
	ITaxFormManager *self = (ITaxFormManager*)handle->self;
	return self->IsChildForm(parentFormID, formID);
}

DLL_EXPORT bool DLL_CALL TaxFormManager_IsFedChildForm(const TaxFormManagerHandle *handle, taxformid_t parentFormID, taxformid_t formID)
{
	ITaxFormManager *self = (ITaxFormManager*)handle->self;
	return self->IsFedChildForm(parentFormID, formID);
}

DLL_EXPORT int DLL_CALL TaxFormManager_GetTotalChildCopies(const TaxFormManagerHandle *handle, const TaxFormHandle *parent, taxformid_t childFormID)
{
	ITaxFormManager *self = (ITaxFormManager*)handle->self;
	ITaxForm *pForm = nullptr;
	if (parent)
	{
		pForm = (ITaxForm *)parent->self;
	}

	return self->GetTotalChildCopies(pForm, childFormID);
}

DLL_EXPORT void DLL_CALL TaxFormManager_SetLogCallback(const TaxFormManagerHandle *handle, TaxFormManagerLogCallback fn, void *userData)
{
    ITaxFormManager *self = (ITaxFormManager*)handle->self;
    self->SetLogCallback(fn, userData);
}

DLL_EXPORT bool DLL_CALL TaxFormManager_WriteLog(const TaxFormManagerHandle *handle, const char *msg)
{
    ITaxFormManager *self = (ITaxFormManager*)handle->self;
    return self->WriteLog(msg);
}

DLL_EXPORT bool DLL_CALL TaxFormManager_ParseAutoAttachments(const TaxFormManagerHandle *handle, int returnType, const DllDataBufferHandle *out)
{
    ITaxFormManager *self = (ITaxFormManager*)handle->self;

    auto result = ParseAutoAttachments(self, (EfReturnType)returnType);

    rapidjson::StringBuffer buffer;
    rapidjson::Writer<rapidjson::StringBuffer> json(buffer);

    json.StartArray();

    for (const auto& item : result)
    {
        item.writeJson(json);
    }

    json.EndArray();

    TaxAct::CalcDll::DllDataBuffer outJson(out, false);
    outJson.SetString(buffer.GetString());

    return true;
}
