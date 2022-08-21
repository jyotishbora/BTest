// field objects for calculations

#ifndef CALCFLD_H
#define CALCFLD_H

#include "ICALCFLD.H"
#include "Calcform.h"
#include "Calcfunc.h"
#include "TAXDATE.H"
#include "Taxstr.h"
#include "rapidjson/document.h"
#include "DetailsTypes.h"

typedef struct tagUpdateObj
{
    tagUpdateObj* pNext;
    ITaxFormManager* pFormMgr;
    CALCEXPUPDATEFUNC pfnUpdate;
} UPDATEOBJ;

class CTaxField : public ITaxField
{
public:
    CTaxField();
    virtual ~CTaxField();

    static CTaxField *Create(WORD type);

    virtual WORD GetID() override;
    virtual WORD GetIndex() override;
    virtual WORD GetType() override;
    virtual ITaxForm* GetForm() override;

    virtual BOOL GetStatus(DWORD dwStatus) override;
    virtual void SetStatus(DWORD dwStatus, BOOL bSet) override;

    virtual void Calculate() = 0;
    virtual void Update();

    virtual void Clear() = 0;
    virtual BOOL IsEmpty() = 0;

    virtual LONG GetNumber() = 0;
    virtual TAXCURRENCY GetCurrency() = 0;
    virtual DOUBLE GetFloat() = 0;
    virtual BOOL GetBool() = 0;
    virtual CTaxDate GetCalcDate() = 0;
    virtual CTaxString GetString() = 0;
    virtual void SetNumber(LONG lValue) = 0;
    virtual void SetCurrency(TAXCURRENCY currValue) = 0;
    virtual void SetFloat(DOUBLE dValue) = 0;
    virtual void SetBool(BOOL bValue) = 0;
    virtual void SetDate(LONG dateValue) = 0;
    virtual void SetString(LPCSTR szStr) = 0;

    virtual LONG GetDate() final;
    virtual void GetString(LPSTR szStr, size_t iSize) final;

    virtual LONG GetMinNumber() override;
    virtual LONG GetMaxNumber() override;
    virtual TAXCURRENCY GetMinCurrency() override;
    virtual TAXCURRENCY GetMaxCurrency() override;
    virtual int GetFMVStatus() override;
    virtual DOUBLE GetMinFloat() override;
    virtual DOUBLE GetMaxFloat() override;
    virtual size_t GetDataSize();
    virtual void GetData(void *lpData);
    virtual void SetData(const void *lpData);
    virtual int GetStringLength() override;
    virtual int GetMaxLength() override;
    virtual int GetListIndex() override;
    virtual int GetListTotal() override;
    virtual void GetListString(int iIndex, LPSTR szStr, size_t iSize) override;
    virtual void GetListStringDisplay(int iIndex, LPSTR szStr, size_t iSize) override;
    virtual void GetListStringTitle(LPSTR szStr, size_t iSize) override;
    virtual void SetListIndex(int iIndex) override;
    virtual void SetListTitle(LPCSTR szTitle);
    virtual void SetListItem(LPCSTR szDisplay, LPCSTR szValue = NULL);
    virtual void AttachExternalUpdate(ITaxFormManager* pFormMgr, CALCEXPUPDATEFUNC pfnUpdate) override;
    virtual LONG GetMinCalcDate();
    virtual LONG GetMaxCalcDate();
    virtual LONG GetMinDate() override;
    virtual LONG GetMaxDate() override;
    virtual LONG GetDefYear() override;
    virtual WORD GetStringType() override;
    virtual int GetIndexOfStr(LPCSTR szStr) override;

    virtual void clearLedgerDetails() override final;
    virtual void clearDetailsNote() override final;

    virtual BOOL setLedgerDetailsLine(const int line, LPCSTR date, LPCSTR desc, LPCSTR amount, BOOL imported) override final;
    virtual void setDetailsNote(LPCSTR szNote) override final;

    virtual BOOL hasLedgerDetails() override final;
    virtual BOOL hasDetailsNote() override final;

    virtual stDetailRec* getLedgerDetails() override final;
    virtual LPCSTR getDetailsNote() override final;

    virtual bool ReadJson(rapidjson::Value& in);
    virtual bool ImportPYJson(rapidjson::Value& in, DWORD importFlags);
    virtual bool HasJsonData();
    virtual bool WriteJson(rapidjson::Writer<rapidjson::StringBuffer>& out) = 0;

    virtual TaxFieldHandle handle() override;

    void DetachExternalUpdate(ITaxFormManager* pFormMgr);
    void ExternalUpdate();
    void InitStatus(DWORD dwStatus);
    void SetStatusData(DWORD dwStatus);
    DWORD GetStatusData();

public:
    WORD m_wID;
    WORD m_wIndex;
    WORD m_wType;
    DWORD m_dwStatus;
    CTaxForm* m_pForm;
    CALCUPDATEFUNC m_pfnUpdate;
    UPDATEOBJ* m_pUpdate;

protected:
    bool ReadJson(rapidjson::Value& in, bool readFlags, bool readDetails, bool readValue);

    bool WriteJsonDetails(rapidjson::Writer<rapidjson::StringBuffer>& out);

    CTaxString m_detailsNote;
    std::unique_ptr<stDetailRec> m_detailsLedger;

    void *m_ownerDll; // HMODULE that created this object
};

class CTaxNumberFld : public CTaxField
{
public:
    CTaxNumberFld();

    BOOL Init(WORD wIndex, WORD wLastIndex, DWORD dwStatus, LONG lDefValue, LONG lMinValue, LONG lMaxValue,
                      CALCLONGFUNC pfnCalc, CALCUPDATEFUNC pfnUpdate);

    virtual void Calculate() override;
    virtual void Clear() override;

    virtual LONG GetNumber() override;
    virtual TAXCURRENCY GetCurrency() override;
    virtual DOUBLE GetFloat() override;
    virtual BOOL GetBool() override;
    virtual CTaxDate GetCalcDate() override;
    virtual CTaxString GetString() override;
    virtual void SetNumber(LONG lValue) override;
    virtual void SetCurrency(TAXCURRENCY currValue) override;
    virtual void SetFloat(DOUBLE dValue) override;
    virtual void SetBool(BOOL bValue) override;
    virtual void SetDate(LONG dateValue) override;
    virtual void SetString(LPCSTR szStr) override;

    virtual LONG GetMinNumber() override;
    virtual LONG GetMaxNumber() override;
    virtual int GetMaxLength() override;
    virtual size_t GetDataSize() override;
    virtual void GetData(void *lpData) override;
    virtual void SetData(const void *lpData) override;
    virtual BOOL IsEmpty() override;

    virtual bool WriteJson(rapidjson::Writer<rapidjson::StringBuffer>& out) override;

protected:
    LONG m_lValue;
    LONG m_lMinValue;
    LONG m_lMaxValue;
    CALCLONGFUNC m_pfnCalc;
};

class CTaxCurrencyFld : public CTaxField
{
public:
    CTaxCurrencyFld();

    BOOL Init(WORD wIndex, WORD wLastIndex, DWORD dwStatus, TAXCURRENCY currDefValue, TAXCURRENCY currMinValue, TAXCURRENCY currMaxValue,
                      int nFMVStatus, CALCCURRENCYFUNC pfnCalc, CALCUPDATEFUNC pfnUpdate);

    virtual void Calculate() override;
    virtual void Clear() override;

    virtual LONG GetNumber() override;
    virtual TAXCURRENCY GetCurrency() override;
    virtual DOUBLE GetFloat() override;
    virtual BOOL GetBool() override;
    virtual CTaxDate GetCalcDate() override;
    virtual CTaxString GetString() override;
    virtual void SetNumber(LONG lValue) override;
    virtual void SetCurrency(TAXCURRENCY currValue) override;
    virtual void SetFloat(DOUBLE dValue) override;
    virtual void SetBool(BOOL bValue) override;
    virtual void SetDate(LONG dateValue) override;
    virtual void SetString(LPCSTR szStr) override;

    virtual TAXCURRENCY GetMinCurrency() override;
    virtual TAXCURRENCY GetMaxCurrency() override;
    virtual int GetFMVStatus() override;
    virtual int GetMaxLength() override;
    virtual size_t GetDataSize() override;
    virtual void GetData(void *lpData) override;
    virtual void SetData(const void *lpData) override;
    virtual BOOL IsEmpty() override;

    virtual bool WriteJson(rapidjson::Writer<rapidjson::StringBuffer>& out) override;

protected:
    TAXCURRENCY m_currValue;
    TAXCURRENCY m_currMinValue;
    TAXCURRENCY m_currMaxValue;
    int m_nFMVStatus;
    CALCCURRENCYFUNC m_pfnCalc;
};

class CTaxFloatFld : public CTaxField
{
public:
    CTaxFloatFld();

    BOOL Init(WORD wIndex, WORD wLastIndex, DWORD dwStatus, DOUBLE dDefValue, DOUBLE dMinValue, DOUBLE dMaxValue,
                      LONG maxLength, CALCDOUBLEFUNC pfnCalc, CALCUPDATEFUNC pfnUpdate);

    virtual void Calculate() override;
    virtual void Clear() override;

    virtual LONG GetNumber() override;
    virtual TAXCURRENCY GetCurrency() override;
    virtual DOUBLE GetFloat() override;
    virtual BOOL GetBool() override;
    virtual CTaxDate GetCalcDate() override;
    virtual CTaxString GetString() override;
    virtual void SetNumber(LONG lValue) override;
    virtual void SetCurrency(TAXCURRENCY currValue) override;
    virtual void SetFloat(DOUBLE dValue) override;
    virtual void SetBool(BOOL bValue) override;
    virtual void SetDate(LONG dateValue) override;
    virtual void SetString(LPCSTR szStr) override;

    virtual DOUBLE GetMinFloat() override;
    virtual DOUBLE GetMaxFloat() override;
    virtual int GetMaxLength() override;
    virtual size_t GetDataSize() override;
    virtual void GetData(void *lpData) override;
    virtual void SetData(const void *lpData) override;
    virtual BOOL IsEmpty() override;

    virtual bool WriteJson(rapidjson::Writer<rapidjson::StringBuffer>& out) override;

protected:
    DOUBLE m_dValue;
    DOUBLE m_dMinValue;
    DOUBLE m_dMaxValue;
    LONG m_maxLength; // This is actually used as max digits of precision
    CALCDOUBLEFUNC m_pfnCalc;
};

class CTaxBoolFld : public CTaxField
{
public:
    CTaxBoolFld();

    BOOL Init(WORD wIndex, WORD wLastIndex, DWORD dwStatus, BOOL bDefValue,
                      CALCBOOLFUNC pfnCalc, CALCUPDATEFUNC pfnUpdate);

    virtual void Calculate() override;
    virtual void Clear() override;

    virtual LONG GetNumber() override;
    virtual TAXCURRENCY GetCurrency() override;
    virtual DOUBLE GetFloat() override;
    virtual BOOL GetBool() override;
    virtual CTaxDate GetCalcDate() override;
    virtual CTaxString GetString() override;
    virtual void SetNumber(LONG lValue) override;
    virtual void SetCurrency(TAXCURRENCY currValue) override;
    virtual void SetFloat(DOUBLE dValue) override;
    virtual void SetBool(BOOL bValue) override;
    virtual void SetDate(LONG dateValue) override;
    virtual void SetString(LPCSTR szStr) override;

    virtual size_t GetDataSize() override;
    virtual void GetData(void *lpData) override;
    virtual void SetData(const void *lpData) override;
    virtual BOOL IsEmpty() override;

    virtual bool WriteJson(rapidjson::Writer<rapidjson::StringBuffer>& out) override;

protected:
    BOOL m_bValue;
    CALCBOOLFUNC m_pfnCalc;
};

class CTaxDateFld : public CTaxField
{
public:
    CTaxDateFld();

    BOOL Init(WORD wIndex, WORD wLastIndex, DWORD dwStatus, int iDefDay, int iDefMonth, int iDefYear,
                      int iMinDay, int iMinMonth, int iMinYear, int iMaxDay, int iMaxMonth, int iMaxYear,
                      CTaxString strDefYear, CALCDATEFUNC pfnCalc, CALCUPDATEFUNC pfnUpdate);

    virtual void Calculate() override;
    virtual void Clear() override;

    virtual LONG GetNumber() override;
    virtual TAXCURRENCY GetCurrency() override;
    virtual DOUBLE GetFloat() override;
    virtual BOOL GetBool() override;
    virtual CTaxDate GetCalcDate() override;
    virtual CTaxString GetString() override;
    virtual void SetNumber(LONG lValue) override;
    virtual void SetCurrency(TAXCURRENCY currValue) override;
    virtual void SetFloat(DOUBLE dValue) override;
    virtual void SetBool(BOOL bValue) override;
    virtual void SetDate(LONG dateValue) override;
    virtual void SetString(LPCSTR szStr) override;

    virtual size_t GetDataSize() override;
    virtual void GetData(void *lpData) override;
    virtual void SetData(const void *lpData) override;
    virtual BOOL IsEmpty() override;
    virtual LONG GetMinCalcDate() override;
    virtual LONG GetMaxCalcDate() override;
    virtual LONG GetDefYear() override;
    virtual int GetMaxLength() override;

    virtual bool WriteJson(rapidjson::Writer<rapidjson::StringBuffer>& out) override;

protected:
    CTaxDate m_dateValue;
    CTaxDate m_minDate;
    CTaxDate m_maxDate;
    LONG m_lDefYear;
    CALCDATEFUNC m_pfnCalc;
};

class CTaxStringFld : public CTaxField
{
public:
    CTaxStringFld();

    BOOL Init(WORD wIndex, WORD wLastIndex, DWORD dwStatus, LPCSTR szDefValue, WORD type, LONG maxLength,
                      CALCSTRINGFUNC pfnCalc, CALCUPDATEFUNC pfnUpdate);

    virtual void Calculate() override;
    virtual void Clear() override;

    virtual LONG GetNumber() override;
    virtual TAXCURRENCY GetCurrency() override;
    virtual DOUBLE GetFloat() override;
    virtual BOOL GetBool() override;
    virtual CTaxDate GetCalcDate() override;
    virtual CTaxString GetString() override;
    virtual void SetNumber(LONG lValue) override;
    virtual void SetCurrency(TAXCURRENCY currValue) override;
    virtual void SetFloat(DOUBLE dValue) override;
    virtual void SetBool(BOOL bValue) override;
    virtual void SetDate(LONG dateValue) override;
    virtual void SetString(LPCSTR szStr) override;

    virtual size_t GetDataSize() override;
    virtual void GetData(void *lpData) override;
    virtual void SetData(const void *lpData) override;
    virtual int GetStringLength() override;
    virtual BOOL IsEmpty() override;
    virtual WORD GetStringType() override;
    virtual int GetMaxLength() override;

    virtual bool WriteJson(rapidjson::Writer<rapidjson::StringBuffer>& out) override;

protected:
    CTaxString m_strValue;
    CALCSTRINGFUNC m_pfnCalc;
    WORD m_StringType;
    LONG m_maxLength;
};

class CTaxListFld : public CTaxStringFld
{
public:
    CTaxListFld();

    BOOL Init(WORD wIndex, WORD wLastIndex, DWORD dwStatus, LPCSTR szDefValue, WORD wListID,
                      CALCSTRINGFUNC pfnCalc, CALCUPDATEFUNC pfnUpdate);

    // this just calls the first Init()
    // it exists so that calling Init with wListID=0 resolves to that version
    // otherwise the compiler gives an 'ambiguous overload' error because both WORD and LPCSTR are valid conversions for 0
    BOOL Init(WORD wIndex, WORD wLastIndex, DWORD dwStatus, LPCSTR szDefValue, int wListID,
        CALCSTRINGFUNC pfnCalc, CALCUPDATEFUNC pfnUpdate);

    BOOL Init(WORD wIndex, WORD wLastIndex, DWORD dwStatus, LPCSTR szDefValue, LPCSTR fedPicklistID,
                      CALCSTRINGFUNC pfnCalc, CALCUPDATEFUNC pfnUpdate);

    virtual void Calculate() override;
    virtual void Clear() override;

    virtual void SetString(LPCSTR szStr) override;
    virtual int GetListIndex() override;
    virtual int GetListTotal() override;
    virtual void GetListString(int iIndex, LPSTR szStr, size_t iSize) override;
    virtual void GetListStringDisplay(int iIndex, LPSTR szStr, size_t iSize) override;
    virtual void GetListStringTitle(LPSTR szStr, size_t iSize) override;
    virtual void SetListIndex(int iIndex) override;
    virtual void SetListString(LPCSTR szStr);
    virtual size_t GetDataSize() override;
    virtual void GetData(void *lpData) override;
    virtual void SetData(const void *lpData) override;
    virtual int GetIndexOfStr(LPCSTR szStr) override;

    void CopyValueFrom(const CTaxListFld *other);

    virtual bool ReadJson(rapidjson::Value& in) override;
    virtual bool ImportPYJson(rapidjson::Value& in, DWORD importFlags) override;
    virtual bool HasJsonData();
    virtual bool WriteJson(rapidjson::Writer<rapidjson::StringBuffer>& out) override;

protected:
    CTaxString m_strDisplay;
    WORD m_wListID;
    bool m_isFedListID;
    PicklistInfo m_listData;

    PicklistInfo GetListData();
};

class CTaxDynaListFld : public CTaxListFld
{
public:
    CTaxDynaListFld();
    virtual ~CTaxDynaListFld();

    BOOL Init(WORD wIndex, WORD wLastIndex, DWORD dwStatus, LPCSTR szDefValue,
                      CALCSTRINGFUNC pfnCalc, CALCUPDATEFUNC pfnUpdate, CALCDYNALISTFUNC pfnListCalc);

    virtual void Calculate() override;
    void ClearListData();
    virtual void SetListTitle(LPCSTR szTitle) override;
    virtual void SetListItem(LPCSTR szDisplay, LPCSTR szValue = NULL) override;

protected:
    CALCDYNALISTFUNC m_pfnListCalc;
};

class CTaxOldListFld : public CTaxListFld
{
public:
    virtual size_t GetDataSize() override;
    virtual void GetData(void *lpData) override;
    virtual void SetData(const void *lpData) override;
};

#endif // CALCFLD_H
