// form object for calculations

#ifndef CALCFORM_H
#define CALCFORM_H

#include "ICALCFRM.H"
#include "Calcmgr.h"
#include "rapidjson/document.h"

typedef struct tagUpdateFormObj
{
    tagUpdateFormObj* pNext;
    ITaxFormManager* pFormMgr;
    CALCEXPFORMUPDATEFUNC pfnUpdate;
} UPDATEFORMOBJ;

// CTaxForm declaration

class CTaxForm : public ITaxForm
{
public:
    CTaxForm();
    virtual ~CTaxForm();
    BOOL Init(WORD wFormID, CTaxFormManager* pFormMgr);
    virtual WORD GetID() override;
    virtual WORD GetCopyID() override;
    virtual WORD GetCopyIndex() override;
    virtual ITaxForm* GetParent() override;
    virtual void SetParent(ITaxForm* pParent, BOOL bCalculate = TRUE) override;
    virtual size_t GetDataSize() override;
    virtual void GetData(void *lpData) override;
    virtual void SetData(const void *lpData) override;
    void ImportData(const void *lpData, BOOL bState);
    virtual void GetName(LPSTR szName) override;
    virtual BOOL GetStatus(DWORD dwStatus) override;
    virtual void SetStatus(DWORD dwStatus, BOOL bSet) override;
    virtual WORD GetTotalFields() override;
    virtual ITaxField* GetField(WORD wFieldID) override;
    virtual void GetDescription(LPSTR szDesc, size_t iSize) override;
    virtual void GetProDescription(LPSTR szDesc, size_t iSize) override;
    virtual void CalculateAllFields() override;
    virtual void UpdateAllFields() override;
    virtual void SetRadioButton(WORD wFieldID, BOOL bCalculate = TRUE) override;
    virtual void SetRadioOverride(WORD wFieldID) override;
    virtual void ClearRadioOverride(WORD wFieldID) override;
    virtual WORD GetRadioButtonGroup(WORD wFieldID) override;
    virtual ITaxFormManager* GetFormManager() override;
    CTaxField* GetCalcField(WORD wFieldID);
    CTaxField* GetCalcFieldSafeIndex(WORD wFieldID, WORD wIndex);
    void Update();
    virtual void AttachExternalUpdate(ITaxFormManager* pFormMgr, CALCEXPFORMUPDATEFUNC pfnUpdate) override;
    void ExternalUpdate();
    void DetachExternalUpdate(ITaxFormManager* pFormMgr);
    virtual WORD GetTriggerFormID() override;
    virtual char *GetTriggerFieldName() override;
    virtual WORD GetTriggerFormCopyID() override;
    virtual WORD GetTriggerFieldIndex() override;
    virtual void SetTriggerValues(WORD wFormID, WORD wFormCopyID, LPSTR szFieldName, WORD wFieldIndex) override;

    virtual bool ReadJson(const char *in) override;
    virtual bool WriteJson(DllStringBuffer *out) override;

    void SetStatusData(DWORD dwStatus);
    DWORD GetStatusData();
    bool ReadJson(rapidjson::Value& in);
    bool WriteJson(rapidjson::Writer<rapidjson::StringBuffer>& out);

    virtual TaxFormHandle handle() override;

public:
    WORD m_wID;
    WORD m_wCopyID;
    DWORD m_dwStatus;
    WORD m_wTotalFields;
    CTaxField** m_pFields;
    CTaxFormManager* m_pFormMgr;
    WORD m_wParentFormID;
    WORD m_wParentCopyID;
    ITaxForm* m_pParent;
#ifdef CALCSTATE
    WORD m_wFedParentFormID;
#endif
    CALCFORMUPDATEFUNC m_pfnUpdate;
    UPDATEFORMOBJ* m_pUpdate;

private:
    const RadioGroupInfo *GetRadioGroupForField(WORD fieldID);

    char m_strFormCreationTriggerFieldName [64];
    WORD m_wFormCreationTriggerFieldIndex;
    WORD m_wFormCreationTriggerFormID;
    WORD m_wFormCreationTriggerFormCopyID;

    void *m_ownerDll; // HMODULE that created this object
};

#endif
