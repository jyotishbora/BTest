// functions for calculations

#ifndef CALCFUNC_H
#define CALCFUNC_H

#include "CALCDEFS.H"
#include "CommonConst.h"
#include "CalcVariant.h"

TAXCURRENCY DblToCurr(DOUBLE dValue);
LONG DblToLong(DOUBLE dValue);

LONG MinValue(LONG lValue1, LONG lValue2);
LONG MaxValue(LONG lValue1, LONG lValue2);

TAXCURRENCY MinValue(TAXCURRENCY currValue1, TAXCURRENCY currValue2);
TAXCURRENCY MaxValue(TAXCURRENCY currValue1, TAXCURRENCY currValue2);

TAXCURRENCY MinValue(TAXCURRENCY currValue1, LONG currValue2);
TAXCURRENCY MaxValue(TAXCURRENCY currValue1, LONG currValue2);
TAXCURRENCY MinValue(LONG currValue1, TAXCURRENCY currValue2);
TAXCURRENCY MaxValue(LONG currValue1, TAXCURRENCY currValue2);

DOUBLE MinValue(DOUBLE dValue1, DOUBLE dValue2);
DOUBLE MaxValue(DOUBLE dValue1, DOUBLE dValue2);

DOUBLE MinValue(DOUBLE currValue1, LONG currValue2);
DOUBLE MaxValue(DOUBLE currValue1, LONG currValue2);
DOUBLE MinValue(LONG currValue1, DOUBLE currValue2);
DOUBLE MaxValue(LONG currValue1, DOUBLE currValue2);

LONG Abs(LONG lValue);
TAXCURRENCY Abs(TAXCURRENCY currValue);
DOUBLE Abs(DOUBLE dValue);

TAXCURRENCY Round(TAXCURRENCY currValue);
DOUBLE Round(DOUBLE dValue);
DOUBLE Round(DOUBLE dValue, int iPrecis);

LONG CLng(TAXCURRENCY currValue);
LONG CLng(DOUBLE dValue);
LONG CLng(LPCSTR szValue);

TAXCURRENCY CCur(LONG lValue);
TAXCURRENCY CCur(DOUBLE dValue);
TAXCURRENCY CCur(LPCSTR szValue);

DOUBLE CDbl(LONG lValue);
DOUBLE CDbl(TAXCURRENCY currValue);
DOUBLE CDbl(LPCSTR szValue);

CTaxDate CDate(LONG lValue);
CTaxDate CDate(LPCSTR szValue);
CTaxDate MakeDate(LONG lMonth, LONG lDay, LONG lYear);

CTaxString CStr(LONG lValue);
CTaxString CStr(TAXCURRENCY currValue);
CTaxString CStr(DOUBLE dValue, LONG lPrecision = 4);
CTaxString DblToStr(DOUBLE dValue, LONG lPrecision);
CTaxString CStr(CTaxDate dateValue);
CTaxString CStr(CTaxDate& dateValue);

CTaxString Mid(LPCSTR szStr, int iStart, int iLength);
CTaxString LetterStr(LPCSTR szStr);
CTaxString NumberStr(LPCSTR szStr);
CTaxString Trim(LPCSTR szStr);
CTaxString LTrim(LPCSTR szStr);
CTaxString RTrim(LPCSTR szStr);
CTaxString LCase(LPCSTR szStr);
CTaxString UCase(LPCSTR szStr);
BOOL IsStrEqual(LPCSTR szStr1, LPCSTR szStr2);
LONG FindInStr(LPCSTR szStr1, LPCSTR szStr2);
int GetIndexOfStr(ITaxFormManager* pFormMgr, WORD wFormID, WORD wFieldID, WORD wIndex, WORD wCopyID, LPCSTR szStr);
int GetIndexOfStr(ITaxForm* pForm, WORD wFieldID, WORD wIndex, LPCSTR szStr);
CTaxString GetParam(LPCSTR szParams, int iParam, LPCSTR pSeparator);
CTaxString SortString(LPCSTR szStr);
CTaxString SortNumberString(LPCSTR szStr);

TAXCURRENCY CDollar(TAXCURRENCY currValue);
TAXCURRENCY CDollar(DOUBLE dValue);

LONG Len(LPCSTR szValue);

LONG GetDay(const CTaxDate& dateValue);
LONG GetMonth(const CTaxDate& dateValue);
LONG GetYear(const CTaxDate& dateValue);
LONG GetDayOfWeek(const CTaxDate& dateValue);
LONG GetDayOfYear(const CTaxDate& dateValue);
LONG DaysDiff(const CTaxDate& date1, const CTaxDate& date2);
LONG GetYearsPassed(const CTaxDate& date1, const CTaxDate& date2);
LONG GetMonthsPassed(const CTaxDate& date1, const CTaxDate& date2);
CTaxString GetVerboseDate(const CTaxDate& dateValue);

BOOL IsLeapYear(LONG lYear);

void formatCC(char* source);

BOOL IsValidCC(LPCSTR szCardType, LPCSTR szCardNumber, LPCSTR szCardCvvNumber);
BOOL IsValidSSN(LPCSTR szStr);
BOOL IsValidITIN(LPCSTR szStr);
BOOL IsValidATIN(LPCSTR szStr);
BOOL IsValidID(LPCSTR szStr);
BOOL IsValidZIP(LPCSTR szStr, LPCSTR szState);
BOOL IsValidForeignStateCode(LPCSTR szStr);
BOOL IsValidRTN(LPCSTR szStr);
BOOL IsValidDAN(LPCSTR szStr);
BOOL IsValidEIN(LPCSTR szStr);
BOOL IsValidRBIN(LPCSTR szStr);
BOOL IsValidVIN(LPCSTR szStr);
BOOL IsValidVINLengthAndChars(LPCSTR szStr);
BOOL IsValidEFileString(LPCSTR szStr);
BOOL IsValidRepublicIDNumber(LPCSTR szStr);
BOOL IsValidEmail(LPCSTR szStr);

CTaxString GetNameControl(LPCSTR szStr, LONG lLength);
CTaxString GetLastName(LPCSTR szName);
CTaxString GetNameSuffix(LPCSTR szName);
CTaxString GetFirstName(LPCSTR szFirstName);
CTaxString GetMiddleInitial(LPCSTR szFirstName);
TAXCURRENCY GetSalesTax(LPCSTR szState, LONG lExemptions, TAXCURRENCY currIncome);
CTaxString GetCity(LPCSTR szCityStateZip);
CTaxString GetState(LPCSTR szCityStateZip);
CTaxString GetZip(LPCSTR szCityStateZip);

BOOL IsFree(CTaxFormManager* pFormMgr);
BOOL IsBasic(CTaxFormManager* pFormMgr);
BOOL IsPlus(CTaxFormManager* pFormMgr);
BOOL IsPremium(CTaxFormManager* pFormMgr);
BOOL IsSku(CTaxFormManager* pFormMgr, LPCSTR szSkuList);
BOOL IsPreparer(CTaxFormManager* pFormMgr);
BOOL IsPrepEnterprise(CTaxFormManager* pFormMgr);
BOOL IsOnline(CTaxFormManager* pFormMgr);
BOOL IsTablet(CTaxFormManager* pFormMgr);
BOOL IsPhone(CTaxFormManager* pFormMgr);
BOOL IsMobile(CTaxFormManager* pFormMgr);
BOOL IsPreview(CTaxFormManager* pFormMgr);
BOOL IsPrepDiscount(CTaxFormManager* pFormMgr);
TAXCURRENCY GetBankPrice(CTaxFormManager* pFormMgr);
BOOL HasBankQualifiedState(CTaxFormManager* pFormMgr);
TAXCURRENCY GetMaxAuditMarkupPrice(CTaxFormManager* pFormMgr);
TAXCURRENCY GetBankTransFee(CTaxFormManager* pFormMgr);
TAXCURRENCY GetAuditPrice(CTaxFormManager* pFormMgr);
TAXCURRENCY GetDasFee(CTaxFormManager* pFormMgr);
TAXCURRENCY GetProductFees(CTaxFormManager* pFormMgr);
TAXCURRENCY GetProductFeesAlwaysWithBank(CTaxFormManager* pFormMgr);

BOOL IsChildCopy(ITaxFormManager* pFormMgr, WORD wChildFormID, WORD wChildCopyID, ITaxForm* pParentForm);
BOOL IsParentCopy(ITaxFormManager* pFormMgr, WORD wParentFormID, WORD wParentCopyID, ITaxForm* pChildForm);
WORD GetAllCopies(ITaxFormManager* pFormMgr, WORD wFormID);
WORD GetChildCopies(ITaxFormManager* pFormMgr, WORD wChildFormID, ITaxForm* pParentForm);
WORD GetParentCopy(ITaxFormManager* pFormMgr, WORD wParentFormID, ITaxForm* pChildForm);
WORD GetFieldCopies(ITaxFormManager* pFormMgr, WORD wFormID, WORD wFieldID, WORD wIndex);
WORD GetStatusCopies(ITaxFormManager* pFormMgr, WORD wFormID, DWORD dwStatus);
WORD ChildCopies(ITaxFormManager* pFormMgr, WORD wChildFormID, ITaxForm* pParentForm);
WORD ParentCopy(ITaxFormManager* pFormMgr, WORD wParentFormID, ITaxForm* pChildForm);
WORD FieldCopies(ITaxFormManager* pFormMgr, WORD wFormID, WORD wFieldID, WORD wIndex);
WORD StatusCopies(ITaxFormManager* pFormMgr, WORD wFormID, DWORD dwStatus);
CTaxString GetStaticCopyStr(ITaxFormManager* pFormMgr, WORD wFormID, WORD wCopyIndex);
BOOL IsFeatureAvailable(CTaxFormManager* pFormMgr, LPCSTR szfeatureName);
CTaxString OhioRitaStr(ITaxFormManager* pFormMgr, LPCSTR city, LPCSTR dataname);
DOUBLE OhioRitaDbl(ITaxFormManager* pFormMgr, LPCSTR city, LPCSTR dataname, LPCSTR date = "");
BOOL OhioRitaBool(ITaxFormManager* pFormMgr, LPCSTR city, LPCSTR dataname);

BOOL HasConsent(CTaxFormManager* pFormMgr, LPCSTR consentName);

WORD GetCopy(ITaxForm* pForm);

BOOL GetStatus(DWORD dwStatus, ITaxForm* pForm);

BOOL FieldUsingFMV(CTaxFormManager* pFormMgr, WORD wFormID, WORD wFieldID, WORD wIndex, WORD wCopyID = 1);

LONG GetMod10CheckDigit(LPCSTR szStr);
LONG GetAdventCheckDigit(LPCSTR szStr);

BOOL IsCreatedBy(ITaxForm* pForm, WORD wTriggerFormID, LPCSTR szTriggerFieldName, WORD wTriggerIndex);

LONG GetNumber(ITaxFormManager* pFormMgr, WORD wFormID, WORD wFieldID, WORD wIndex, WORD wCopyID = COPY_ALLCOPIES);
TAXCURRENCY GetCurrency(ITaxFormManager* pFormMgr, WORD wFormID, WORD wFieldID, WORD wIndex, WORD wCopyID = COPY_ALLCOPIES);
DOUBLE GetFloat(ITaxFormManager* pFormMgr, WORD wFormID, WORD wFieldID, WORD wIndex, WORD wCopyID = COPY_ALLCOPIES);
BOOL GetBool(ITaxFormManager* pFormMgr, WORD wFormID, WORD wFieldID, WORD wIndex, WORD wCopyID = COPY_ALLCOPIES);
CTaxDate GetDate(ITaxFormManager* pFormMgr, WORD wFormID, WORD wFieldID, WORD wIndex, WORD wCopyID = COPY_ALLCOPIES);
CTaxString GetString(ITaxFormManager* pFormMgr, WORD wFormID, WORD wFieldID, WORD wIndex, WORD wCopyID = COPY_ALLCOPIES);
LONG GetIndex(ITaxFormManager* pFormMgr, WORD wFormID, WORD wFieldID, WORD wIndex, WORD wCopyID = COPY_ALLCOPIES);

LONG GetNumber(CTaxForm* pForm, WORD wFieldID, WORD wIndex);
TAXCURRENCY GetCurrency(CTaxForm* pForm, WORD wFieldID, WORD wIndex);
DOUBLE GetFloat(CTaxForm* pForm, WORD wFieldID, WORD wIndex);
BOOL GetBool(CTaxForm* pForm, WORD wFieldID, WORD wIndex);
CTaxDate GetDate(CTaxForm* pForm, WORD wFieldID, WORD wIndex);
CTaxString GetString(CTaxForm* pForm, WORD wFieldID, WORD wIndex);
LONG GetIndex(CTaxForm* pForm, WORD wFieldID, WORD wIndex);

void UpdateField(ITaxForm* pForm, WORD wFieldID, WORD wIndex);
void UpdateField(ITaxFormManager* pFormMgr, WORD wFormID, WORD wFieldID, WORD wIndex);
void UpdateField(ITaxForm* pForm, WORD wFieldID, WORD wIndex, WORD wLastIndex);
void UpdateField(ITaxFormManager* pFormMgr, WORD wFormID, WORD wFieldID, WORD wIndex, WORD wLastIndex);
void UpdateField(WORD wFieldIndex, WORD wRefIndex, ITaxForm* pForm, WORD wFieldID, WORD wIndex);
void UpdateField(ITaxFormManager* pFormMgr, WORD wFieldIndex, WORD wRefIndex, WORD wFormID, WORD wFieldID, WORD wIndex);
void UpdateFieldArray(ITaxForm* pForm, WORD wFieldID, WORD wLastIndex);
void UpdateFieldArray(ITaxFormManager* pFormMgr, WORD wFormID, WORD wFieldID, WORD wLastIndex);
void UpdateFieldArray(WORD wFieldIndex, WORD wRefIndex, ITaxForm* pForm, WORD wFieldID, WORD wLastIndex);
void UpdateFieldArray(ITaxFormManager* pFormMgr, WORD wFieldIndex, WORD wRefIndex, WORD wFormID, WORD wFieldID, WORD wLastIndex);

void CreateForm(ITaxFormManager* pFormMgr, ITaxForm* pForm, ITaxField* pField, WORD wIndex, WORD wFormID, WORD wCopyID, BOOL bChild = FALSE);
void CreateFormCopies(ITaxFormManager* pFormMgr, ITaxForm* pForm, ITaxField* pField, WORD wIndex, WORD wFormID, WORD wCopiesFormID, WORD wCopiesFieldID);
void CreateFormAll(ITaxFormManager* pFormMgr, ITaxForm* pForm, ITaxField* pField, WORD wIndex, WORD wFormID, WORD wCopyID, BOOL bChild,
                   WORD nAdditional, WORD *additionalForms, WORD *additionalCopies, WORD *additionalFields);
void CreateFormUnique(ITaxFormManager* pFormMgr, ITaxForm* pForm, ITaxField* pField, WORD wIndex, WORD wFormID);

void PrintList_Clear(ITaxFormManager *pFormMgr, unsigned int listID);
void PrintList_AddReturn(ITaxFormManager *pFormMgr, unsigned int listID, unsigned int subListID,
                         const CTaxString& title);
void PrintList_AddForm(ITaxFormManager *pFormMgr, unsigned int listID, unsigned int subListID, 
                       const CTaxString& title, const CTaxString& name);
void PrintList_AddHTML(ITaxFormManager *pFormMgr, unsigned int listID, unsigned int subListID, 
                       const CTaxString& title, const CTaxString& url);
void PrintList_AddCustom(ITaxFormManager *pFormMgr, unsigned int listID, unsigned int subListID, 
                         const CTaxString& title, const CTaxString& func);

template<typename... T>
CalcVariant FedCustom(ITaxFormManager *pFormMgr, LPCSTR funcName, T... t)
{
    CalcVariant result;
    std::vector<CalcVariant> params{std::forward<T>(t)...};

#ifdef CALCSTATE
    pFormMgr->GetFedFormManager()->CallCustomCalc(funcName, params.size(), &result, params.data());
#else
    pFormMgr->CallCustomCalc(funcName, params.size(), &result, params.data());
#endif

    return result;
}

#ifdef CALCFEDERAL
BOOL IsChildCopy(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szChildFormName, WORD wChildCopyID, ITaxForm* pParentForm);
BOOL IsParentCopy(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szParentFormName, WORD wParentCopyID, ITaxForm* pChildForm);
WORD GetAllCopies(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szFormName);
WORD GetChildCopies(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szChildFormName, ITaxForm* pParentForm);
WORD GetParentCopy(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szParentFormName, ITaxForm* pChildForm);
WORD GetFieldCopies(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szFormName, LPCSTR szFieldName, WORD wIndex);
WORD GetStatusCopies(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szFormName, DWORD dwStatus);
WORD ChildCopies(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szChildFormName, ITaxForm* pParentForm);
WORD ParentCopy(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szParentFormName, ITaxForm* pChildForm);
WORD FieldCopies(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szFormName, LPCSTR szFieldName, WORD wIndex);
WORD StatusCopies(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szFormName, DWORD dwStatus);
CTaxString GetStaticCopyStr(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szFormName, WORD wCopyIndex);

LONG GetNumber(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szFormName, LPCSTR szFieldName, WORD wIndex, WORD wCopyID = COPY_ALLCOPIES);
TAXCURRENCY GetCurrency(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szFormName, LPCSTR szFieldName, WORD wIndex, WORD wCopyID = COPY_ALLCOPIES);
DOUBLE GetFloat(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szFormName, LPCSTR szFieldName, WORD wIndex, WORD wCopyID = COPY_ALLCOPIES);
BOOL GetBool(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szFormName, LPCSTR szFieldName, WORD wIndex, WORD wCopyID = COPY_ALLCOPIES);
CTaxDate GetDate(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szFormName, LPCSTR szFieldName, WORD wIndex, WORD wCopyID = COPY_ALLCOPIES);
CTaxString GetString(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szFormName, LPCSTR szFieldName, WORD wIndex, WORD wCopyID = COPY_ALLCOPIES);
LONG GetIndex(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szFormName, LPCSTR szFieldName, WORD wIndex, WORD wCopyID = COPY_ALLCOPIES);

LONG AveragePremium_CountStates();
CTaxString AveragePremium_GetState(LONG index);
LONG AveragePremium_CountCounties(LPCSTR state);
CTaxString AveragePremium_GetCounty(LPCSTR state, LONG index);
TAXCURRENCY AveragePremium_GetAmount(LPCSTR state, LPCSTR county, BOOL employeeOnly);
#endif

#ifdef CALCSTATE
/*
BOOL IsFedChildCopy(ITaxFormManager *pFormMgr, WORD wChildFormID, WORD wChildCopyID, ITaxForm *pParentForm);

BOOL IsFedParentCopy(ITaxFormManager *pFormMgr, WORD wParentFormID, WORD wParentCopyID, ITaxForm *pChildForm);

WORD GetFedAllCopies(ITaxFormManager *pFormMgr, WORD wFormID);

WORD GetFedChildCopies(ITaxFormManager *pFormMgr, WORD wChildFormID, ITaxForm *pParentForm);

WORD GetFedParentCopy(ITaxFormManager *pFormMgr, WORD wParentFormID, ITaxForm *pChildForm);

WORD GetFedFieldCopies(ITaxFormManager *pFormMgr, WORD wFormID, WORD wFieldID, WORD wIndex);

WORD GetFedStatusCopies(ITaxFormManager *pFormMgr, WORD wFormID, DWORD dwStatus);

WORD FedChildCopies(ITaxFormManager *pFormMgr, WORD wChildFormID, ITaxForm *pParentForm);

WORD FedParentCopy(ITaxFormManager *pFormMgr, WORD wParentFormID, ITaxForm *pChildForm);

WORD FedFieldCopies(ITaxFormManager *pFormMgr, WORD wFormID, WORD wFieldID, WORD wIndex);

WORD FedStatusCopies(ITaxFormManager *pFormMgr, WORD wFormID, DWORD dwStatus);

LONG GetFedNumber(ITaxFormManager *pFormMgr, WORD wFormID, WORD wFieldID, WORD wIndex, WORD wCopyID = COPY_ALLCOPIES);

TAXCURRENCY GetFedCurrency(ITaxFormManager *pFormMgr, WORD wFormID, WORD wFieldID, WORD wIndex, WORD wCopyID = COPY_ALLCOPIES);

DOUBLE GetFedFloat(ITaxFormManager *pFormMgr, WORD wFormID, WORD wFieldID, WORD wIndex, WORD wCopyID = COPY_ALLCOPIES);

BOOL GetFedBool(ITaxFormManager *pFormMgr, WORD wFormID, WORD wFieldID, WORD wIndex, WORD wCopyID = COPY_ALLCOPIES);

CTaxDate GetFedDate(ITaxFormManager *pFormMgr, WORD wFormID, WORD wFieldID, WORD wIndex, WORD wCopyID = COPY_ALLCOPIES);

CTaxString GetFedString(ITaxFormManager *pFormMgr, WORD wFormID, WORD wFieldID, WORD wIndex, WORD wCopyID = COPY_ALLCOPIES);

LONG GetFedIndex(ITaxFormManager *pFormMgr, WORD wFormID, WORD wFieldID, WORD wIndex, WORD wCopyID = COPY_ALLCOPIES);
*/
#endif // CALCSTATE

#endif // CALCFUNC_H
