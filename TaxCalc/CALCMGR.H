// form manager object for calculations

#ifndef CALCMGR_H
#define CALCMGR_H

#include "icalcmgr.h"
#include "CALCINFO.H"
#include "xstring.h"
#include "disabledFeaturesCore.h"
#include <set>
#include <map>
#include <vector>
#include <string>
#include <functional>
#include <memory>

#include "rapidjson/document.h"
#include "rapidjson/writer.h"
#include "OhioRita.h"

typedef std::vector<CTaxForm*> FORMSCONTAINER;
typedef std::vector<CTaxForm*>::iterator FORMSITERATOR;
typedef std::vector<WORD> FORMIDCONTAINER;

#ifdef CALCFEDERAL
typedef struct tagStateMgr
{
    tagStateMgr* pNext;
    ITaxFormManager* pFormMgr;
} STATEMGR;
#endif

class CTaxFormManager : public ITaxFormManager
{
public:
    FORMSCONTAINER* m_pForms[FORM_TOTALFORMS];
    ITaxAppObject* m_pAppObj;
    FORMIDCONTAINER m_DeletedChildFormIds;
    std::vector<PrintListItem> m_printLists[PRINTLIST_COUNT];
    
#ifdef CALCFEDERAL
    STATEMGR* m_pStateMgr;
#endif
#ifdef CALCSTATE
    ITaxFormManager* m_pFedFormMgr;
#endif

    CTaxFormManager();
    virtual ~CTaxFormManager();
    virtual BOOL Init() override;
    virtual void Delete() override;
    void Clear();
    virtual BOOL InitForms() override;
    virtual void DeleteForms() override;
    virtual WORD GetFormID(LPCSTR szForm) override;
    virtual WORD GetFieldID(WORD wFormID, LPCSTR szField, int iIndex = 0) override;
    virtual WORD GetFieldType(WORD wFormID, WORD wFieldID) override;
    virtual ITaxForm* CreateForm(WORD wFormID, BOOL bCalculate = TRUE, ITaxForm* pParent = NULL) override;
    virtual ITaxForm* GetForm(WORD wFormID, WORD wCopyID) override;
    virtual ITaxForm* GetFormByIndex(WORD wFormID, WORD wCopyIndex) override;
    virtual WORD GetTotalCopies(WORD wFormID) override;
    virtual WORD GetMaxCopies(WORD wFormID) override;
    virtual WORD GetTotalFields(WORD wFormID) override;
    virtual BOOL GetStatus(WORD wFormID, DWORD dwStatus) override;
    virtual WORD GetTotalForms() override;
    virtual BOOL IsFederal() override;
    virtual BOOL IsState() override;
	virtual BOOL isReturnFormPrintDisabled(const char* returnFormName) override;
    virtual void GetModuleName(LPSTR szName) override;
    virtual void GetModuleDateTime(LPSTR szDateTime) override;
    virtual void GetModuleTitle(LPSTR szName) override;
    virtual void GetFormName(LPSTR szName, WORD wFormID) override;
    virtual void GetFieldName(LPSTR szName, WORD wFormID, WORD wFieldID) override;
    virtual void GetShortFormName(LPSTR szName, WORD wFormID) override;
    virtual void GetLongFormName(LPSTR szName, WORD wFormID) override;
    virtual void GetTabName(LPSTR szName, WORD wFormID) override;
    virtual WORD GetFormListOrder(WORD wFormID, DWORD dwListStatus) override;
    virtual void CalculateAllForms() override;
    virtual WORD GetTotalSpawnForms(WORD wFormID, WORD wFieldID) override;
    virtual void GetSpawnForm(SPAWNINFO* pSpawn, WORD wFormID, WORD wFieldID, WORD wIndex) override;
    virtual ITaxField* GetCustomField(LPCSTR szName) override;
    virtual ITaxField* GetCustomFieldByIndex(LPCSTR szName, WORD wCopyIndex = 1) override;
    virtual void AttachFederalFormMgr(ITaxFormManager* pFormMgr) override;
    virtual void AttachStateFormMgr(ITaxFormManager* pFormMgr) override;
    virtual void DetachStateFormMgr(ITaxFormManager* pFormMgr) override;
    virtual void AttachExternalForm(ITaxForm* pForm) override;
    virtual void GetFederalDateTime(LPSTR szDateTime) override;
    virtual WORD GetTotalChildForms(ITaxForm* pParentForm) override;
    virtual ITaxForm* GetChildForm(ITaxForm* pParentForm, WORD wChildID) override;
    virtual void DeleteChildForms(ITaxForm* pParentForm) override;
    virtual void DeleteFormAndChildForms(ITaxForm* pParentForm, BOOL bSuspendCalculations = FALSE) override;
    virtual BOOL IsChildForm(WORD wParentFormID, WORD wChildFormID) override;
    virtual BOOL IsFedChildForm(WORD wFedParentFormID, WORD wChildFormID) override;
    virtual WORD GetMaxChildCopies(WORD wParentFormID, WORD wChildFormID) override;
    virtual WORD GetFedMaxChildCopies(WORD wFedParentFormID, WORD wChildFormID) override;
    virtual WORD GetTotalChildCopies(ITaxForm* pParentForm, WORD wChildFormID) override;
    virtual ITaxForm* GetChildCopy(ITaxForm* pParentForm, WORD wChildFormID, WORD wChildID) override;
    virtual BOOL HasParent(WORD wChildFormID) override;
    virtual BOOL HasFedParent(WORD wChildFormID) override;
    virtual void SaveConsent(const char *name, bool value);
    virtual BOOL HasConsent(LPCSTR consentName);
    virtual WORD GetTotalParents(WORD wChildFormID) override;
    virtual WORD GetParentFormID(WORD wChildFormID, WORD wIndex) override;
    virtual WORD GetTotalFedParents(WORD wChildFormID) override;
    virtual WORD GetFedParentFormID(WORD wChildFormID, WORD wIndex) override;
    virtual WORD GetTotalCreators(WORD wCreateFormID) override;
    virtual WORD GetCreatorFormID(WORD wCreateFormID, WORD wIndex) override;
    virtual WORD GetTotalFedCreators(WORD wCreateFormID) override;
    virtual WORD GetFedCreatorFormID(WORD wCreateFormID, WORD wIndex) override;
    void UpdateCreators(WORD wCreateFormID);
    virtual size_t GetModuleMapSize() override;
    virtual void GetModuleMap(void *lpData) override;
    virtual size_t GetFormMapSize(WORD wFormID) override;
    virtual void GetFormMap(void *lpData, WORD wFormID) override;
    virtual ITaxForm* CreateUpdatedForm(LPCSTR szForm, const void *pModuleMap, const void *pFedModuleMap, const void *pFormMap, const void *pData) override;
    virtual void GetFormInstructionTopic(LPSTR szTopic, WORD wFormID) override;
    virtual void GetFormTaxGuideTopic(LPSTR szTopic, WORD wFormID) override;
    virtual void AttachAppObject(ITaxAppObject* pAppObj) override;

    virtual ITaxForm* GetPrintForm(WORD wFormID, ITaxForm* pParentForm = NULL) override;
    virtual void DeletePrintForms() override;
    virtual BOOL HasMoreCopies(WORD wFormID) override;
    virtual void GetFormNewScript(LPSTR szScript, WORD wFormID) override;
    virtual void GetFormReviewScript(LPSTR szScript, WORD wFormID) override;
    virtual void GetFormExpertTopic(LPSTR szTopic, WORD wFormID) override;
    virtual void GetFormTaxTutorTopic(LPSTR szTopic, WORD wFormID) override;
    virtual void GetFieldInstructionTopic(LPSTR szTopic, WORD wFormID, WORD wFieldID) override;
    virtual void GetFieldDescription(LPSTR szTopic, WORD wFormID, WORD wFieldID) override;
    CTaxForm* GetCalcForm(WORD wFormID, WORD wCopyIndex);
    virtual void UpdateAppFormsTree(ITaxForm* pForm) override;
    virtual ITaxFormManager* GetFedFormManager() override;
    virtual ITaxFormManager* GetStateFormManager(LPCSTR szModName) override;
    virtual ITaxForm* GetStateFormByIndex(LPCSTR szForm, WORD wCopyIndex) override;
    virtual void UpdateExternalDeletedForm(LPCSTR szName, WORD wFormID) override;
    virtual void UpdateDeletedForm(WORD wFormID) override;
    virtual void UpdateDeletedChildForms() override;
    
    virtual bool PrintList_Exists(unsigned int listID) const override;
    virtual void PrintList_Clear(unsigned int listID) override;
    virtual void PrintList_Add(unsigned int listID, const PrintListItem& toAdd) override;
    virtual size_t PrintList_Size(unsigned int listID) const override;
    virtual const PrintListItem *PrintList_At(unsigned int listID, size_t index) const override;

    virtual WORD GetPicklistId(LPCSTR szName);
    virtual size_t GetPicklistDataSize(WORD id);
    virtual void GetPicklistData(WORD id, void *pData);

    virtual void CallCustomCalc(LPCSTR funcName, int nParameters, CalcVariant *result, CalcVariant *params) override;

    virtual bool ReadJson(const char *in) override;
    virtual bool ImportPYJson(const char *in, DWORD importFlags) override;
    virtual bool WriteJson(DllStringBuffer *out) override;

    virtual void ClearProductFlags() override;
    virtual void AddProductFlag(const char *str) override;
    virtual void RemoveProductFlag(const char *str) override;
    virtual bool HasProductFlag(const char *str) const override;

    virtual void ClearPricingInfo() override;
    virtual void SetPricingInfo(const char *str, TAXCURRENCY amt) override;
    virtual TAXCURRENCY GetPricingInfo(const char *str) const override;
    virtual void OnUpdatePricingInfo(OnUpdatePricingInfoCallback fn, void *userData) override;
    virtual void UpdatePricingInfo(const char *price) override;

    bool ReadJson(rapidjson::Value& in);
    bool ImportPYJson(rapidjson::Value& in, DWORD importFlags);
    bool WriteJson(rapidjson::Writer<rapidjson::StringBuffer>& out);

    virtual Tax::DisabledFeaturesCore* GetDisabledFeaturesCore() override;
    virtual Tax::OhioRita* GetOhioRita() override;

    virtual void SetLogCallback(TaxFormManagerLogCallback fn, void *userData) override;
    virtual bool WriteLog(const char *msg) override;

    virtual void getMathGlobalConstList(DllStringBuffer& out) override;

    virtual TaxFormManagerHandle handle() override;

private:
    std::set<Tax::xstring> m_productFlags;
    std::map<Tax::xstring, TAXCURRENCY> m_pricingInfo;
    std::unique_ptr<Tax::DisabledFeaturesCore> m_dfCore;
    std::unique_ptr<Tax::OhioRita> m_ohioRita;

    OnUpdatePricingInfoCallback m_updatePricingInfoCallback = nullptr;
    void *m_updatePricingInfoCallbackUserData = nullptr;

    TaxFormManagerLogCallback m_logCallback = nullptr;
    void *m_logCallbackUserData = nullptr;

    void SetFieldValue(CTaxForm * newForm, CTaxField * newField, CTaxField * oldField);

    void DeleteForm(ITaxForm* pForm, BOOL bSuspendCalculations = FALSE);
    std::map<std::string, bool> m_consent;

    std::vector<PYImportFieldInfo> GetImportInfo(const std::string& fromFormName, DWORD importFlags);

    void *m_ownerDll; // HMODULE that created this object
};

#endif // CALCMGR_H
