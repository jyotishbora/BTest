// functions for calculations

#include "StdAfx.h"
#include "Taxstr.h"
#include "TAXDATE.H"
#include "CALCINFO.H"
#include "Calcmgr.h"
#include "Calcform.h"
#include "Calcfld.h"
#include "Calcfunc.h"
#include "IAppObj.h"
#include "xstring.h"
#include "CalcStaticData.h"
#include "CalcProductFlags.h"
#include "CalcPricingInfo.h"

#include <algorithm>
#include <map>
#include <regex>

#ifdef CALCFEDERAL
#include "CALCPREMIUMSDATA.H"
#endif

#define kTESTCREDITCARD                 "4444222233331111"  //  TESTAPPROVED

// hacks for floating point inconsistencies

TAXCURRENCY DblToCurr(DOUBLE dValue)
{
#ifdef _DEBUG
    TAXCURRENCY currFudge, currCast, currStr;
    char szDbl[32];
    char szMsg[512];

    if (dValue < 0.0)
    {
        currFudge = (TAXCURRENCY)(dValue - CALC_FLOAT_FUDGEVAL);
    }
    else
    {
        currFudge = (TAXCURRENCY)(dValue + CALC_FLOAT_FUDGEVAL);
    }

    sprintf_s(szDbl, "%.6f", dValue);
    currStr = std::strtoll(szDbl, nullptr, 10);
    currCast = (TAXCURRENCY)dValue;

    if ((currCast != currFudge) || (currCast != currStr))
    {
        sprintf_s(szMsg, "Double to currency conversion inconsistency.\n"
                  "double = %.6f\n"
                  "currency (cast conversion) = %lli\n"
                  "currency (fudge conversion) = %lli (this value will be used)\n"
                  "currency (string conversion) = %lli\n",
                  dValue, currCast, currFudge, currStr);

        //WriteLog(szMsg);
    }

    return currFudge;
#else

    if (dValue < 0.0)
    {
        return (TAXCURRENCY)(dValue - CALC_FLOAT_FUDGEVAL);
    }

    return (TAXCURRENCY)(dValue + CALC_FLOAT_FUDGEVAL);
#endif
}

LONG DblToLong(DOUBLE dValue)
{
#ifdef _DEBUG
    LONG lFudge, lCast, lStr;
    char szDbl[32];
    char szMsg[BUFFER_SIZE];

    if (dValue < 0.0)
    {
        lFudge = (LONG)(dValue - CALC_FLOAT_FUDGEVAL);
    }
    else
    {
        lFudge = (LONG)(dValue + CALC_FLOAT_FUDGEVAL);
    }

    sprintf_s(szDbl, "%.6f", dValue);
    lStr = atol(szDbl);
    lCast = (LONG)dValue;

    if ((lCast != lFudge) || (lCast != lStr))
    {
        sprintf_s(szMsg, "Double to long conversion inconsistency.\n\n"
                  "double = %.6f\n"
                  "long (cast conversion) = %li\n"
                  "long (fudge conversion) = %li\n"
                  "long (string conversion) = %li",
                  dValue, lCast, lFudge, lStr);

        //WriteLog(szMsg);
    }

    return lFudge;
#else

    if (dValue < 0.0)
    {
        return (LONG)(dValue - CALC_FLOAT_FUDGEVAL);
    }

    return (LONG)(dValue + CALC_FLOAT_FUDGEVAL);
#endif
}

LONG MinValue(LONG lValue1, LONG lValue2)
{
    return std::min(lValue1, lValue2);
}

LONG MaxValue(LONG lValue1, LONG lValue2)
{
    return std::max(lValue1, lValue2);
}

TAXCURRENCY MinValue(TAXCURRENCY currValue1, TAXCURRENCY currValue2)
{
    return std::min(currValue1, currValue2);
}

TAXCURRENCY MaxValue(TAXCURRENCY currValue1, TAXCURRENCY currValue2)
{
    return std::max(currValue1, currValue2);
}

TAXCURRENCY MinValue(TAXCURRENCY currValue1, LONG currValue2)
{ 
    return MinValue(currValue1, static_cast<TAXCURRENCY>(currValue2)); 
}

TAXCURRENCY MaxValue(TAXCURRENCY currValue1, LONG currValue2)
{ 
    return MaxValue(currValue1, static_cast<TAXCURRENCY>(currValue2)); 
}

TAXCURRENCY MinValue(LONG currValue1, TAXCURRENCY currValue2)
{ 
    return MinValue(static_cast<TAXCURRENCY>(currValue1), currValue2); 
}

TAXCURRENCY MaxValue(LONG currValue1, TAXCURRENCY currValue2)
{ 
    return MaxValue(static_cast<TAXCURRENCY>(currValue1), currValue2); 
}

DOUBLE MinValue(DOUBLE dValue1, DOUBLE dValue2)
{
    return std::min(dValue1, dValue2);
}

DOUBLE MaxValue(DOUBLE dValue1, DOUBLE dValue2)
{
    return std::max(dValue1, dValue2);
}

DOUBLE MinValue(DOUBLE currValue1, LONG currValue2)
{
    return MinValue(currValue1, static_cast<DOUBLE>(currValue2)); 
}

DOUBLE MaxValue(DOUBLE currValue1, LONG currValue2)
{ 
    return MaxValue(currValue1, static_cast<DOUBLE>(currValue2)); 
}

DOUBLE MinValue(LONG currValue1, DOUBLE currValue2)
{ 
    return MinValue(static_cast<DOUBLE>(currValue1), currValue2); 
}

DOUBLE MaxValue(LONG currValue1, DOUBLE currValue2)
{ 
    return MaxValue(static_cast<DOUBLE>(currValue1), currValue2); 
}

LONG Abs(LONG lValue)
{
    if (lValue < 0)
    {
        return (lValue * -1);
    }

    return lValue;
}

TAXCURRENCY Abs(TAXCURRENCY currValue)
{
    if (currValue < 0)
    {
        return (currValue * -1);
    }

    return currValue;
}

DOUBLE Abs(DOUBLE dValue)
{
    return fabs(dValue);
}

TAXCURRENCY Round(TAXCURRENCY currValue)
{
    if (currValue < 0)
    {
        return (((currValue - 50) / 100) * 100);
    }

    return (((currValue + 50) / 100) * 100);
}

DOUBLE Round(DOUBLE dValue)
{
    if (dValue < 0.0)
    {
        return ceil(dValue - (0.5 + CALC_FLOAT_FUDGEVAL));
    }

    return floor(dValue + (0.5 + CALC_FLOAT_FUDGEVAL));
}

DOUBLE Round(DOUBLE dValue, int iPrecis)
{
    DOUBLE dPrecis = pow(10.0, (DOUBLE)iPrecis);
    dValue *= dPrecis;

    if (dValue < 0.0)
    {
        return ceil(dValue - (0.5 + CALC_FLOAT_FUDGEVAL)) / dPrecis;
    }

    return floor(dValue + (0.5 + CALC_FLOAT_FUDGEVAL)) / dPrecis;
}

LONG CLng(TAXCURRENCY currValue)
{
    return (LONG)currValue;
}

LONG CLng(DOUBLE dValue)
{
    return DblToLong(dValue);
}

LONG CLng(LPCSTR szValue)
{
    return atol(szValue);
}

TAXCURRENCY CCur(LONG lValue)
{
    return (TAXCURRENCY)lValue;
}

TAXCURRENCY CCur(DOUBLE dValue)
{
    return DblToCurr(dValue);
}

TAXCURRENCY CCur(LPCSTR szValue)
{
    std::string workString = szValue;

    // If more than 1 char in length we need to check for '$' and decimal point
    if (workString.length() > 1)
    {
        // Trim leading spaces. The atoi function can handle these but this makes our check for '$' much easier.
        std::size_t first = workString.find_first_not_of(' ');
        workString = workString.substr(first);

        // Remove dollar sign if present in first or second position (any other position is considered invalid)
        if (workString[0] == '$')
        {
            workString = workString.substr(1);
        }
        else if (workString[1] == '$' && (workString[0] == '-' || workString[0] == '+'))
        {
            // Assuming first char is '-' (or maybe '+') in this case.
            // If the first char is something else, the number will properly convert to 0 anyway.
            std::string leadingChar = workString.substr(0, 1);
            std::string restOfString = workString.substr(2);
            workString = leadingChar;
            workString.append(restOfString);
        }

        // Now look for a decimal point.  If found, assume this is representing dollars before AND cents after
        std::size_t decimalPointPosition = workString.find_first_of('.');
        if (decimalPointPosition != std::string::npos)
        {
            // Move decimal point to right 2 positions so the string represents number of cents.
            // We don't worry about digits after the 2 penny digits since the atoi64 function would stop at decimal point anyway.
            std::string dollars = workString.substr(0, decimalPointPosition);
            std::string pennies = workString.substr(decimalPointPosition + 1, 2);
            workString = dollars;
            workString.append(pennies);
        }
    }

    return std::strtoll(workString.c_str(), nullptr, 10);
}

DOUBLE CDbl(LONG lValue)
{
    return (DOUBLE)lValue;
}

DOUBLE CDbl(TAXCURRENCY currValue)
{
    return (DOUBLE)currValue;
}

DOUBLE CDbl(LPCSTR szValue)
{
    return atof(szValue);
}

CTaxDate CDate(LONG lValue)
{
    CTaxDate dateTemp;

    dateTemp.SetDate(lValue);
    return dateTemp;
}

CTaxDate CDate(LPCSTR szValue)
{
    CTaxDate dateTemp;

    dateTemp.SetDate(szValue);
    return dateTemp;
}

CTaxDate MakeDate(LONG lMonth, LONG lDay, LONG lYear)
{
    return CTaxDate(lDay, lMonth, lYear);
}

CTaxString CStr(LONG lValue)
{
    char szNumber[64];

    sprintf_s(szNumber, "%li", lValue);
    CTaxString strTemp = szNumber;
    return strTemp;
}

CTaxString CStr(TAXCURRENCY currValue)
{
    char szNumber[64];

    if (currValue >= 0)
    {
        sprintf_s(szNumber, "$%lli.%02lli", currValue / 100, currValue % 100);
    }
    else
    {
        sprintf_s(szNumber, "-$%lli.%02lli", (currValue * -1) / 100, (currValue * -1) % 100);
    }

    CTaxString strTemp = szNumber;
    return strTemp;
}

CTaxString CStr(DOUBLE dValue, LONG lPrecision /* = 4 */)
{
    char szNumber[64];
    char szTemp[64];

    sprintf_s(szTemp, "%%.%df", lPrecision);
    sprintf_s(szNumber, szTemp, dValue);
    CTaxString strTemp = szNumber;
    return strTemp;
}

CTaxString DblToStr(DOUBLE dValue, LONG lPrecision)
{
    return CStr(dValue, lPrecision);
}

CTaxString CStr(CTaxDate dateValue)
{
    return dateValue.GetTaxString();
}

CTaxString CStr(CTaxDate& dateValue)
{
    return dateValue.GetTaxString();
}

TAXCURRENCY CDollar(TAXCURRENCY currValue)
{
    return Round(currValue);
}

TAXCURRENCY CDollar(DOUBLE dValue)
{
    return Round(DblToCurr(dValue));
}

CTaxString Mid(LPCSTR szStr, int iStart, int iLength)
{
    CTaxString strTemp;

    strTemp.Empty();
    iStart--; // iStart is a one-based value
    INT_PTR iLen = std::char_traits<char>::length(szStr);

    for (INT_PTR i = iStart; (i < iLen) && (i < (iStart + iLength)); i++)
    {
        if (i >= 0)
        {
            strTemp += *(szStr + i);
        }
    }

    return strTemp;
}

CTaxString LetterStr(LPCSTR szStr)
{
    CTaxString strTemp;

    strTemp.Empty();

    for (LPCSTR pStr = szStr; *pStr != '\0'; pStr++)
    {
        if (isalpha((BYTE)*pStr))
        {
            strTemp += *pStr;
        }
    }

    return strTemp;
}

CTaxString NumberStr(LPCSTR szStr)
{
    CTaxString strTemp;

    strTemp.Empty();

    for (LPCSTR pStr = szStr; *pStr != '\0'; pStr++)
    {
        if (isdigit((BYTE)*pStr))
        {
            strTemp += *pStr;
        }
    }

    return strTemp;
}

CTaxString Trim(LPCSTR szStr)
{
    LPSTR pTempStr = _strdup(szStr);
    LPSTR pTemp;
    for (pTemp = pTempStr; (*pTemp != '\0') && ((UCHAR)*pTemp <= (UCHAR)' '); pTemp++);

    LPSTR pStr;
    for (pStr = (pTemp + (std::char_traits<char>::length(pTemp) - 1));
         (pStr != (pTemp - 1)) && ((UCHAR)*pStr <= (UCHAR)' '); *pStr = '\0', pStr--);

    CTaxString strTemp = pTemp;
    free(pTempStr);
    return strTemp;
}

CTaxString LTrim(LPCSTR szStr)
{
    LPSTR pTempStr = _strdup(szStr);

    LPSTR pTemp;
    for (pTemp = pTempStr; (*pTemp != '\0') && ((UCHAR)*pTemp <= (UCHAR)' '); pTemp++);

    CTaxString strTemp = pTemp;
    free(pTempStr);
    return strTemp;
}

CTaxString RTrim(LPCSTR szStr)
{
    LPSTR pTempStr = _strdup(szStr);
    for (LPSTR pStr = (pTempStr + (std::char_traits<char>::length(pTempStr) - 1));
         (pStr != (pTempStr - 1)) && ((UCHAR)*pStr <= (UCHAR)' '); *pStr = '\0', pStr--);

    CTaxString strTemp = pTempStr;
    free(pTempStr);
    return strTemp;
}

CTaxString LCase(LPCSTR szStr)
{
    CTaxString str;

    LPSTR pTempStr = _strdup(szStr);
    if (pTempStr)
    {
        _strlwr_s(pTempStr, std::char_traits<char>::length(pTempStr) + 1);
        str = pTempStr;
        free(pTempStr);
    }

    return str;
}

CTaxString UCase(LPCSTR szStr)
{
    CTaxString str;

    LPSTR pTempStr = _strdup(szStr);
    if (pTempStr)
    {
        _strupr_s(pTempStr, std::char_traits<char>::length(pTempStr) + 1);
        str = pTempStr;
        free(pTempStr);
    }

    return str;
}

BOOL IsStrEqual(LPCSTR szStr1, LPCSTR szStr2)
{
    return (_stricmp(szStr1, szStr2) == 0);
}

LONG FindInStr(LPCSTR szStr1, LPCSTR szStr2)
{
    const char* pStr = strstr(szStr1, szStr2);

    if (pStr == NULL)
    {
        return 0;
    }
    else
    {
        return (LONG)((std::char_traits<char>::length(szStr1) - std::char_traits<char>::length(pStr)) + 1);
    }
}

int GetIndexOfStr(ITaxFormManager* pFormMgr, WORD wFormID, WORD wFieldID, WORD wIndex, WORD wCopyID, LPCSTR szStr)
{
    int index(-1);
    ITaxForm* pForm(NULL);
    ITaxField* pField(NULL);

    switch (wCopyID)
    {
        case COPY_REFERENCE:
            for (WORD wCopy = 1; pForm = pFormMgr->GetFormByIndex(wFormID, wCopy); wCopy++)
            {
                if (pForm->GetStatus(FORMSTATUS_REFERENCE))
                {
                    pField = pForm->GetField(wFieldID + wIndex);
                    break;
                }
            }

            break;

        case 0:
            break;

        default: // normal copy number
            if (pForm = pFormMgr->GetFormByIndex(wFormID, wCopyID))
            {
                pField = pForm->GetField(wFieldID + wIndex);
            }
    }

    if (pField)
    {
        index = pField->GetIndexOfStr(szStr);
    }

    return index;
}

int GetIndexOfStr(ITaxForm* pForm, WORD wFieldID, WORD wIndex, LPCSTR szStr)
{
    int index(-1);
    ITaxField* pField(pForm->GetField(wFieldID + wIndex));

    if (pField)
    {
        index = pField->GetIndexOfStr(szStr);
    }

    return index;
}

CTaxString GetParam(LPCSTR szParams, int iParam, LPCSTR pSeparator)
{
    CTaxString str("");
    char cSeparator = ',';

    if (pSeparator)
    {
        cSeparator = *pSeparator;
    }

    if (szParams)
    {
        LPCSTR pParam;
        BOOL bInStr;
        INT_PTR i;
        for (pParam = szParams, i = 1, bInStr = FALSE;
             (i <= iParam) && (*pParam != '\0');
             pParam++)
        {
            if (!bInStr && (*pParam == cSeparator))
            {
                i++;

                // advance pointer if separated by spaces
                if (cSeparator == ' ')
                    for (; * (pParam + 1) == cSeparator; pParam++);
            }
            else if (*pParam == '"')
            {
                bInStr = !bInStr;
            }
            else if (i == iParam)
            {
                str += *pParam;
            }
        }
    }

    return str;
}

CTaxString SortString(LPCSTR szStr)
{
    std::vector<Tax::xstring> stringList;
    Tax::xstring(szStr).Split("|", stringList);

    //sort the vector
    std::sort(stringList.begin(), stringList.end());

    //dump sorted vector into string
    bool firstVal = true;
    CTaxString returnString("");
    for (const auto& str : stringList)
    {
        if (!firstVal)
        {
            returnString += "|";
        }

        returnString += str.c_str();
        firstVal = false;
    }

    return returnString;
}

CTaxString SortNumberString(LPCSTR szStr)
{
    std::vector<Tax::xstring> stringList;
    Tax::xstring(szStr).Split("|", stringList);

    // convert to ints
    // we're storing the ints next to the string so we can preseve formatting (e.g. leading 0's) of the original string
    std::vector<std::pair<int, Tax::xstring>> numberStringList;

    for (const auto& str : stringList)
    {
        numberStringList.push_back(std::make_pair(std::strtol(str.c_str(), nullptr, 10), str));
    }

    // sort
    std::sort(numberStringList.begin(), numberStringList.end(), 
        [](const auto& a, const auto& b)
        {
            return a.first < b.first;
        });

    //dump sorted vector into string
    bool firstVal = true;
    CTaxString returnString("");
    for (const auto& str : numberStringList)
    {
        if (!firstVal)
        {
            returnString += "|";
        }

        returnString += str.second.c_str();
        firstVal = false;
    }

    return returnString;
}

LONG Len(LPCSTR szValue)
{
    return (LONG)std::char_traits<char>::length(szValue);
}

LONG GetDay(const CTaxDate& dateValue)
{
    return dateValue.GetDay();
}

LONG GetMonth(const CTaxDate& dateValue)
{
    return dateValue.GetMonth();
}

LONG GetYear(const CTaxDate& dateValue)
{
    return dateValue.GetYear();
}

LONG GetDayOfWeek(const CTaxDate& dateValue)
{
    return dateValue.GetDayOfWeek();
}

LONG GetDayOfYear(const CTaxDate& dateValue)
{
    return dateValue.GetDayOfYear();
}

LONG DaysDiff(const CTaxDate& date1, const CTaxDate& date2)
{
    return (LONG)(date1 - date2);
}

LONG GetYearsPassed(const CTaxDate& date1, const CTaxDate& date2)
{
    if (date1 >= date2)
    {
        return 0;
    }
    else if (date2.GetMonth() > date1.GetMonth())
    {
        return (date2.GetYear() - date1.GetYear());
    }
    else if ((date2.GetMonth() == date1.GetMonth()) &&
             (date2.GetDay() >= date1.GetDay()))
    {
        return (date2.GetYear() - date1.GetYear());
    }
    else
    {
        return ((date2.GetYear() - date1.GetYear()) - 1);
    }
}

LONG GetMonthsPassed(const CTaxDate& date1, const CTaxDate& date2)
{
    if (date1 >= date2)
    {
        return 0;
    }

    LONG lYears = GetYearsPassed(date1, date2);
    LONG lMonths;

    if (date2.GetMonth() > date1.GetMonth())
    {
        lMonths = date2.GetMonth() - date1.GetMonth();
    }
    else
    {
        lMonths = date2.GetMonth() + (12 - date1.GetMonth());
    }

    if (date2.GetDay() < date1.GetDay())
    {
        lMonths--;
    }

    if (lMonths == 12) //we've already counted the 12 months in the GetYearsPassed function
    {
        lMonths = 0;
    }

    return ((12 * lYears) + lMonths);
}

CTaxString GetVerboseDate(const CTaxDate& dateValue)
{
    return dateValue.GetVerboseTaxString();
}

BOOL IsLeapYear(LONG lYear)
{
    if (((lYear % 4) == 0) &&
        (((lYear % 100) != 0) ||
         ((lYear % 400) == 0)))
    {
        return TRUE;
    }

    return FALSE;
}

void formatCC(char* source)
{
    char* i = source;
    char* j = source;
    while(*j != 0)
    {
        *i = *j++;
        if(*i != '-' && *i != ' ' )
            i++;
    }
    *i = 0;
}

BOOL IsValidCC(LPCSTR szCardType, LPCSTR szCardNumber, LPCSTR szCardCvvNumber)
{
    //Please note this is a port from the TaxACT Tax Project, ValidCreditCard in Misc.h, and Misc.cpp - please coordinate updates to both.
    BOOL valid = FALSE;

    char tempCardType[128];
    char tempCardNumber[128];
    char tempCardCvv[128];

    strcpy_s( tempCardType, strnlen_s(szCardType, sizeof(tempCardType)) + 1, szCardType );
    strcpy_s( tempCardNumber, strnlen_s(szCardNumber, sizeof(tempCardNumber)) + 1, szCardNumber );
    strcpy_s( tempCardCvv, strnlen_s(szCardCvvNumber, sizeof(tempCardCvv)) + 1, szCardCvvNumber );

    for( int i = 0; i < (int)std::char_traits<char>::length(szCardType); i++)
    {
        char c = tempCardType[i];
        tempCardType[i] = toupper((int)c);
    }

    //Remove "-" from Credit Card Number 
    //Remove " " from Credit Card Number
    //NumberStr(tempCardNumber, tempCardNumber);
    formatCC(tempCardNumber);

    CTaxString cardType = tempCardType;
    CTaxString cardNumber = tempCardNumber;
    CTaxString cardCvvNumber = tempCardCvv;

    if ((cardType.IsEmpty()) || (cardNumber.IsEmpty()) || (cardCvvNumber.GetLength() < 3))
    {
        return FALSE;
    }

    int creditCardLength1, creditCardLength2, prefixLength;
    CTaxString prefix1, prefix2, prefix3, prefix4, prefix5;

    if (cardType == "VISA")
    {
        creditCardLength1 = 13;
        creditCardLength2 = 16;
        prefixLength = 1;
        prefix1 = "4";
    }
    else if (cardType == "MASTERCARD")
    {
        creditCardLength1 = 16;
        creditCardLength2 =  0;
        prefixLength = 2;
        prefix1 = "51";
        prefix2 = "52";
        prefix3 = "53";
        prefix4 = "54";
        prefix5 = "55";
    }
    else if (cardType == "AMERICAN EXPRESS")
    {
        creditCardLength1 = 15;
        creditCardLength2 = 0;
        prefixLength = 2;
        prefix1 = "34";
        prefix2 = "37";
    }
    else if (cardType == "DISCOVER")
    {
        creditCardLength1 = 16;
        creditCardLength2 = 0;
        prefixLength = 4;
        prefix1 = "6011";
    }
    else
    {
        return FALSE;
    }

    if (!cardNumber.IsEmpty())
    {
        if (cardNumber == CTaxString(kTESTCREDITCARD))
        {
            valid = TRUE;
        }
        else
        {
            int nCardLength = cardNumber.GetLength();

            if ((nCardLength == creditCardLength1) || ((creditCardLength2 > 0) && (nCardLength == creditCardLength2)))
            {
                char temp[128] = {};

                memcpy_s(temp, sizeof(temp), tempCardNumber, prefixLength);
                if( strcmp( temp, prefix1 ) == 0 || 
                    strcmp( temp, prefix2 ) == 0 ||
                    strcmp( temp, prefix3 ) == 0 ||
                    strcmp( temp, prefix4 ) == 0 ||
                    strcmp( temp, prefix5 ) == 0 )
                {
                    long chkSumValue = 0;
                    int location = 0;
                    long sum = 0;

                    for (int x = 1; x <= nCardLength; ++x)
                    {
                        location = nCardLength - x + 1;
                        char ch = tempCardNumber[location - 1];

                        if (!isdigit(ch))
                        {
                            return FALSE;
                        }

                        if (x % 2 == 0)
                        {
                            sum = (ch - '0') * 2;
                            chkSumValue = chkSumValue + (sum % 10);

                            if (sum > 9)
                            {
                                chkSumValue = chkSumValue + 1;
                            }
                        }
                        else
                        {
                            chkSumValue = chkSumValue + (ch - '0');
                        }
                    }

                    if (chkSumValue % 10 == 0)
                    {
                        valid = TRUE;
                    }
                }
            }
        }
    }

    return(valid);
}

BOOL IsValidSSN(LPCSTR szStr)
{
    char szDigits[16];
    size_t iDigits;
    LPCSTR pStr;

    for (pStr = szStr, iDigits = 0; *pStr != '\0'; pStr++)
    {
        if (isdigit((BYTE)*pStr))
        {
            szDigits[iDigits] = *pStr;
            iDigits++;

            if (iDigits > 9)
            {
                return FALSE;
            }
        }
    }

    if (iDigits != 9)
    {
        return FALSE;
    }

    char szValue[16];
    strncpy_s(szValue, szDigits, 3);
    szValue[3] = '\0';
    int iValue = strtol(szValue, nullptr, 10);

    if ((iValue < 1) ||
        (iValue == 666) ||
        (iValue > 899))
    {
        return FALSE;
    }

    strncpy_s(szValue, szDigits + 3, 2);
    szValue[2] = '\0';
    iValue = strtol(szValue, nullptr, 10);

    if (iValue < 1)
    {
        return FALSE;
    }

    strncpy_s(szValue, szDigits + 5, 4);
    szValue[4] = '\0';
    iValue = strtol(szValue, nullptr, 10);

    if (iValue < 1)
    {
        return FALSE;
    }

    //added for efile alerts
    if ((strncmp(szDigits, "123456789", 9) == 0) ||
        (strncmp(szDigits, "987654321", 9) == 0) ||
        (strncmp(szDigits, "111111111", 9) == 0) ||
        (strncmp(szDigits, "222222222", 9) == 0) ||
        (strncmp(szDigits, "333333333", 9) == 0) ||
        (strncmp(szDigits, "444444444", 9) == 0) ||
        (strncmp(szDigits, "555555555", 9) == 0) ||
        (strncmp(szDigits, "666666666", 9) == 0) ||
        (strncmp(szDigits, "777777777", 9) == 0) ||
        (strncmp(szDigits, "888888888", 9) == 0) ||
        (strncmp(szDigits, "999999999", 9) == 0))
    {
        return FALSE;
    }

    return TRUE;
}

BOOL IsValidITIN(LPCSTR szStr)
{
    char szDigits[16];
    size_t iDigits;
    LPCSTR pStr;

    for (pStr = szStr, iDigits = 0; *pStr != '\0'; pStr++)
    {
        if (isdigit((BYTE)*pStr))
        {
            szDigits[iDigits] = *pStr;
            iDigits++;

            if (iDigits > 9)
            {
                return FALSE;
            }
        }
    }

    if (iDigits != 9)
    {
        return FALSE;
    }

    char szValue[16];
    strncpy_s(szValue, szDigits, 3);
    szValue[3] = '\0';
    int iValue = strtol(szValue, nullptr, 10);

    if (iValue < 900)
    {
        return FALSE;
    }

    strncpy_s(szValue, szDigits + 3, 2);
    szValue[2] = '\0';
    iValue = strtol(szValue, nullptr, 10);

    if ((iValue < 70) ||
        (iValue == 89) ||
        (iValue == 93))
    {
        return FALSE;
    }

    return TRUE;
}

BOOL IsValidATIN(LPCSTR szStr)
{
    char szDigits[16];
    size_t iDigits;
    LPCSTR pStr;

    for (pStr = szStr, iDigits = 0; *pStr != '\0'; pStr++)
    {
        if (isdigit((BYTE)*pStr))
        {
            szDigits[iDigits] = *pStr;
            iDigits++;

            if (iDigits > 9)
            {
                return FALSE;
            }
        }
    }

    if (iDigits != 9)
    {
        return FALSE;
    }

    char szValue[16];
    strncpy_s(szValue, szDigits, 3);
    szValue[3] = '\0';
    int iValue = strtol(szValue, nullptr, 10);

    if (iValue < 900)
    {
        return FALSE;
    }

    strncpy_s(szValue, szDigits + 3, 2);
    szValue[2] = '\0';
    iValue = strtol(szValue, nullptr, 10);

    if (iValue != 93)
    {
        return FALSE;
    }

    return TRUE;
}

BOOL IsValidID(LPCSTR szStr)
{
    return (IsValidSSN(szStr) || IsValidITIN(szStr) || IsValidATIN(szStr));
}

BOOL IsValidZIP(LPCSTR szStr, LPCSTR szState)
{
    char szDigits[16];
    size_t iDigits;
    LPCSTR pStr;

    for (pStr = szStr, iDigits = 0; *pStr != '\0'; pStr++)
    {
        if (isdigit((BYTE)*pStr))
        {
            szDigits[iDigits] = *pStr;
            iDigits++;

            if (iDigits > 9)
            {
                return FALSE;
            }
        }
    }

    if (iDigits != 5 && iDigits != 9)
    {
        return FALSE;
    }

    szDigits[5] = '\0';
    long lValue = atol(szDigits);

    if ((lValue % 100) == 0)
    {
        return FALSE;
    }

    char cState1 = toupper(*szState);
    char cState2 = toupper(*(szState + 1));

// military zip codes
    if ((cState1 == 'A') && (cState2 == 'A'))
    {
        return ((lValue >= 34000) && (lValue <= 34099));
    }

    if ((cState1 == 'A') && (cState2 == 'E'))
    {
        return ((lValue >= 9000) && (lValue <= 9999));
    }

    if ((cState1 == 'A') && (cState2 == 'P'))
    {
        return ((lValue >= 96200) && (lValue <= 96699));
    }

//possession zip codes
    if ((cState1 == 'A') && (cState2 == 'S'))
    {
        return (lValue == 96799);
    }

    if ((cState1 == 'F') && (cState2 == 'M'))
    {
        return ((lValue >= 96941) && (lValue <= 96944));
    }

    if ((cState1 == 'G') && (cState2 == 'U'))
    {
        return ((lValue >= 96910) && (lValue <= 96932));
    }

    if ((cState1 == 'M') && (cState2 == 'H'))
    {
        return ((lValue >= 96960) && (lValue <= 96970));
    }

    if ((cState1 == 'M') && (cState2 == 'P'))
    {
        return ((lValue >= 96950) && (lValue <= 96952));
    }

    if ((cState1 == 'P') && (cState2 == 'W'))
    {
        return ((lValue >= 96939) && (lValue <= 96940));
    }

    if ((cState1 == 'P') && (cState2 == 'R'))
        return (((lValue >= 600) && (lValue <= 799)) ||
                ((lValue >= 900) && (lValue <= 999)));

    if ((cState1 == 'V') && (cState2 == 'I'))
    {
        return ((lValue >= 800) && (lValue <= 899));
    }

// state zip codes
    if ((cState1 == 'A') && (cState2 == 'L'))
        return (((lValue >= 35000) && (lValue <= 35299)) ||
                ((lValue >= 35400) && (lValue <= 36999)));

    if ((cState1 == 'A') && (cState2 == 'K'))
    {
        return ((lValue >= 99500) && (lValue <= 99999));
    }

    if ((cState1 == 'A') && (cState2 == 'Z'))
        return (((lValue >= 85000) && (lValue <= 85399)) ||
                ((lValue >= 85500) && (lValue <= 85799)) ||
                ((lValue >= 85900) && (lValue <= 86099)) ||
                ((lValue >= 86300) && (lValue <= 86599)));

    if ((cState1 == 'A') && (cState2 == 'R'))
    {
        return ((lValue >= 71600) && (lValue <= 72999));
    }

    if ((cState1 == 'C') && (cState2 == 'A'))
        return (((lValue >= 90000) && (lValue <= 90899)) ||
                ((lValue >= 91000) && (lValue <= 92899)) ||
                ((lValue >= 93000) && (lValue <= 96199)));

    if ((cState1 == 'C') && (cState2 == 'O'))
    {
        return ((lValue >= 80000) && (lValue <= 81699));
    }

    if ((cState1 == 'C') && (cState2 == 'T'))
    {
        return (((lValue >= 6000) && (lValue <= 6389)) ||
                ((lValue >= 6391) && (lValue <= 6999)));
    }

    if ((cState1 == 'D') && (cState2 == 'E'))
    {
        return ((lValue >= 19700) && (lValue <= 19999));
    }

    if ((cState1 == 'D') && (cState2 == 'C'))
        return (((lValue >= 20000) && (lValue <= 20099)) ||
                ((lValue >= 20200) && (lValue <= 20587)) ||
                ((lValue >= 20589) && (lValue <= 20597)) ||
                ((lValue == 20599)) ||
                ((lValue >= 56900) && (lValue <= 56999)));

    if ((cState1 == 'F') && (cState2 == 'L'))
        return (((lValue >= 32000) && (lValue <= 33999)) ||
                ((lValue >= 34100) && (lValue <= 34299)) ||
                ((lValue >= 34400) && (lValue <= 34499)) ||
                ((lValue >= 34600) && (lValue <= 34799)) ||
                ((lValue >= 34900) && (lValue <= 34999)));

    if ((cState1 == 'G') && (cState2 == 'A'))
        return (((lValue >= 30000) && (lValue <= 31999)) ||
                ((lValue >= 39800) && (lValue <= 39999)));

    if ((cState1 == 'H') && (cState2 == 'I'))
    {
        return (((lValue >= 96701) && (lValue <= 96798)) ||
                ((lValue >= 96800) && (lValue <= 96899)));
    }

    if ((cState1 == 'I') && (cState2 == 'D'))
    {
        return (((lValue >= 83200) && (lValue <= 83413)) ||
                ((lValue >= 83415) && (lValue <= 83899)));
    }

    if ((cState1 == 'I') && (cState2 == 'L'))
        return (((lValue >= 60000) && (lValue <= 62099)) ||
                ((lValue >= 62200) && (lValue <= 62999)));

    if ((cState1 == 'I') && (cState2 == 'N'))
    {
        return ((lValue >= 46000) && (lValue <= 47999));
    }

    if ((cState1 == 'I') && (cState2 == 'A'))
        return (((lValue >= 50000) && (lValue <= 51699)) ||
                ((lValue >= 52000) && (lValue <= 52899)));

    if ((cState1 == 'K') && (cState2 == 'S'))
        return (((lValue >= 66000) && (lValue <= 66299)) ||
                ((lValue >= 66400) && (lValue <= 67999)));

    if ((cState1 == 'K') && (cState2 == 'Y'))
    {
        return (((lValue >= 40000) && (lValue <= 41899)) ||
                ((lValue >= 42000) && (lValue <= 42799)));
    }

    if ((cState1 == 'L') && (cState2 == 'A'))
        return (((lValue >= 70000) && (lValue <= 70199)) ||
                ((lValue >= 70300) && (lValue <= 70899)) ||
                ((lValue >= 71000) && (lValue <= 71499)));

    if ((cState1 == 'M') && (cState2 == 'E'))
    {
        return ((lValue >= 3900) && (lValue <= 4999));
    }

    if ((cState1 == 'M') && (cState2 == 'D'))
        return ((lValue == 20588) ||
                ((lValue >= 20600) && (lValue <= 21299)) ||
                ((lValue >= 21400) && (lValue <= 21999)));

    if ((cState1 == 'M') && (cState2 == 'A'))
        return (((lValue >= 1000) && (lValue <= 2799)) ||
                ((lValue >= 5500) && (lValue <= 5599)));

    if ((cState1 == 'M') && (cState2 == 'I'))
    {
        return ((lValue >= 48000) && (lValue <= 49999));
    }

    if ((cState1 == 'M') && (cState2 == 'N'))
        return (((lValue >= 55000) && (lValue <= 55199)) ||
                ((lValue >= 55300) && (lValue <= 56799)));

    if ((cState1 == 'M') && (cState2 == 'S'))
    {
        return ((lValue >= 38600) && (lValue <= 39799));
    }

    if ((cState1 == 'M') && (cState2 == 'O'))
        return (((lValue >= 63000) && (lValue <= 63199)) ||
                ((lValue >= 63300) && (lValue <= 64199)) ||
                ((lValue >= 64400) && (lValue <= 65899)));

    if ((cState1 == 'M') && (cState2 == 'T'))
    {
        return ((lValue >= 59000) && (lValue <= 59999));
    }

    if ((cState1 == 'N') && (cState2 == 'E'))
        return (((lValue >= 68000) && (lValue <= 68199)) ||
                ((lValue >= 68300) && (lValue <= 69399)));

    if ((cState1 == 'N') && (cState2 == 'V'))
        return (((lValue >= 88900) && (lValue <= 89199)) ||
                ((lValue >= 89300) && (lValue <= 89599)) ||
                ((lValue >= 89700) && (lValue <= 89899)));

    if ((cState1 == 'N') && (cState2 == 'H'))
    {
        return ((lValue >= 3000) && (lValue <= 3899));
    }

    if ((cState1 == 'N') && (cState2 == 'J'))
    {
        return ((lValue >= 7000) && (lValue <= 8999));
    }

    if ((cState1 == 'N') && (cState2 == 'M'))
        return (((lValue >= 87000) && (lValue <= 87199)) ||
                ((lValue >= 87300) && (lValue <= 88499)));

    if ((cState1 == 'N') && (cState2 == 'Y'))
        return (((lValue >= 500) && (lValue <= 599)) ||
                ((lValue == 6390)) ||
                ((lValue >= 10000) && (lValue <= 14999)));

    if ((cState1 == 'N') && (cState2 == 'C'))
    {
        return ((lValue >= 27000) && (lValue <= 28999));
    }

    if ((cState1 == 'N') && (cState2 == 'D'))
    {
        return ((lValue >= 58000) && (lValue <= 58899));
    }

    if ((cState1 == 'O') && (cState2 == 'H'))
    {
        return ((lValue >= 43000) && (lValue <= 45999));
    }

    if ((cState1 == 'O') && (cState2 == 'K'))
        return (((lValue >= 73000) && (lValue <= 73199)) ||
                ((lValue >= 73400) && (lValue <= 73959)) ||
                ((lValue >= 73961) && (lValue <= 74199)) ||
                ((lValue >= 74300) && (lValue <= 74999)));

    if ((cState1 == 'O') && (cState2 == 'R'))
    {
        return ((lValue >= 97000) && (lValue <= 97999));
    }

    if ((cState1 == 'P') && (cState2 == 'A'))
    {
        return ((lValue >= 15000) && (lValue <= 19699));
    }

    if ((cState1 == 'R') && (cState2 == 'I'))
    {
        return ((lValue >= 2800) && (lValue <= 2999));
    }

    if ((cState1 == 'S') && (cState2 == 'C'))
    {
        return ((lValue >= 29000) && (lValue <= 29999));
    }

    if ((cState1 == 'S') && (cState2 == 'D'))
    {
        return ((lValue >= 57000) && (lValue <= 57799));
    }

    if ((cState1 == 'T') && (cState2 == 'N'))
    {
        return ((lValue >= 37000) && (lValue <= 38599));
    }

    if ((cState1 == 'T') && (cState2 == 'X'))
        return (((lValue >= 73300) && (lValue <= 73399)) ||
                (lValue == 73960) ||
                ((lValue >= 75000) && (lValue <= 77099)) ||
                ((lValue >= 77200) && (lValue <= 79999)) ||
                ((lValue >= 88500) && (lValue <= 88599)));

    if ((cState1 == 'U') && (cState2 == 'T'))
    {
        return ((lValue >= 84000) && (lValue <= 84799));
    }

    if ((cState1 == 'V') && (cState2 == 'T'))
        return (((lValue >= 5000) && (lValue <= 5499)) ||
                ((lValue >= 5600) && (lValue <= 5999)));

    if ((cState1 == 'V') && (cState2 == 'A'))
        return (((lValue >= 20100) && (lValue <= 20199)) ||
                (lValue == 20598) ||
                ((lValue >= 22000) && (lValue <= 24699)));

    if ((cState1 == 'W') && (cState2 == 'A'))
        return (((lValue >= 98000) && (lValue <= 98699)) ||
                ((lValue >= 98800) && (lValue <= 99499)));

    if ((cState1 == 'W') && (cState2 == 'V'))
    {
        return ((lValue >= 24700) && (lValue <= 26899));
    }

    if ((cState1 == 'W') && (cState2 == 'I'))
        return (((lValue >= 53000) && (lValue <= 53299)) ||
                ((lValue >= 53400) && (lValue <= 53599)) ||
                ((lValue >= 53700) && (lValue <= 54999)));

    if ((cState1 == 'W') && (cState2 == 'Y'))
        return (((lValue >= 82000) && (lValue <= 83199)) ||
                ((lValue == 83414)));

    return FALSE;
}

BOOL IsValidForeignStateCode(LPCSTR szStr)
{
    for (size_t i = 0;  std::char_traits<char>::length(ForeignStateCodes[i]) > 0; i++)
    {
        if (_stricmp(szStr, ForeignStateCodes[i]) == 0)
        {
            return TRUE;
        }
    }

    return FALSE;
}

BOOL IsValidRTN(LPCSTR szStr)
{
    char szDigits[16];
    size_t iDigits;
    LPCSTR pStr;

    for (pStr = szStr, iDigits = 0; *pStr != '\0'; pStr++)
    {
        if (isdigit((BYTE)*pStr))
        {
            szDigits[iDigits] = *pStr;
            iDigits++;

            if (iDigits > 9)
            {
                return FALSE;
            }
        }
    }

    if (iDigits != 9)
    {
        return FALSE;
    }

    char szTemp[16];
    strncpy_s(szTemp, szDigits, 2);
    szTemp[2] = '\0';
    int iValue = strtol(szTemp, nullptr, 10);

    if (((iValue < 1) || (iValue > 12)) && ((iValue < 21) || (iValue > 32)))
    {
        return FALSE;
    }

    size_t i;
    for (i = 0, iValue = 0, pStr = szDigits; i < 8; i++, pStr++)
    {
        switch (i)
        {
            case 0:
            case 3:
            case 6:
                iValue += (*pStr - '0') * 3;
                break;

            case 1:
            case 4:
            case 7:
                iValue += (*pStr - '0') * 7;
                break;

            case 2:
            case 5:
                iValue += (*pStr - '0');
                break;
        }
    }

    if ((iValue = 10 - (iValue % 10)) == 10)
    {
        iValue = 0;
    }

    return (iValue == (*pStr - '0'));
}

BOOL IsValidDAN(LPCSTR szStr)
{
    size_t i, iZeros;
    LPCSTR pStr;

    for (pStr = szStr, i = 0, iZeros = 0; *pStr != '\0'; i++, pStr++)
    {
        if (!isalnum((BYTE)*pStr) && (*pStr != '-'))
        {
            return FALSE;
        }

        if (*pStr == '0')
        {
            iZeros++;
        }
    }

    return ((i > 0) && (i <= 17) && (i > iZeros));
}

BOOL IsValidEIN(LPCSTR szStr)
{
    size_t iDigits;
    LPCSTR pStr;
    char cPrefix[3];
    cPrefix[2] = '\0';

    for (pStr = szStr, iDigits = 0; *pStr != '\0'; pStr++)
    {
        if (isdigit((BYTE)*pStr))
        {
            if (iDigits < 2)
            {
                cPrefix[iDigits] = *pStr;
            }

            iDigits++;

            if (iDigits > 9)
            {
                return FALSE;
            }
        }
        else if (*pStr != '-')
        {
            return FALSE;
        }
    }

    if (iDigits != 9)
    {
        return FALSE;
    }

    //check invalid ranges
    int iPrefix = strtol(cPrefix, nullptr, 10);

    if ((iPrefix < 1) ||
        ((iPrefix > 6) && (iPrefix < 10)) ||
        ((iPrefix > 16) && (iPrefix < 20)) ||
        ((iPrefix > 27) && (iPrefix < 30)) ||
        ((iPrefix > 48) && (iPrefix < 50)) ||
        ((iPrefix > 77) && (iPrefix < 80)) ||
        ((iPrefix > 88) && (iPrefix < 90)))
    {
        return FALSE;
    }

    //check other specific invalid numbers
    CTaxString tempStr(szStr);
    tempStr = NumberStr(tempStr);
    if (tempStr == "111111111" ||
        tempStr == "222222222" ||
        tempStr == "333333333" ||
        tempStr == "444444444" ||
        tempStr == "555555555" ||
        tempStr == "666666666" ||
        tempStr == "777777777" ||
        tempStr == "888888888" ||
        tempStr == "999999999")
    {
        return FALSE;
    }

    return TRUE;
}

BOOL IsValidRBIN(LPCSTR szStr)
{
    std::regex re("^R" kAPP_NEXTYEARMOD10 "[A-Z0-9]{6}$", std::regex::icase);
    if (std::regex_match(szStr, re))
    {
        // Removed RBIN Check Digit Validation for 2019
        return true;

        //// checksum
        //// check all 8 digits
        //constexpr size_t length = 8;
        //char charArr[length + 1];
        //strcpy_s(charArr, szStr);

        ////Change the second char to a B
        //charArr[1] = 'B';

        //// 33 was added to the check digit value before it was converted to a character
        //// so the characters would be the last 10 of the upper-case ASCII characters.
        //// we need to convert that characters to an int and subtract 33 first.
        //// doing this 'shifts' the value back to the 'numeric' range in ASCII (from the upper-case range)
        //int lastDigit = static_cast<int>(charArr[length - 1]) - 33;

        ////replace the shifted check digit with the 'original' character.
        //charArr[length - 1] = static_cast<char>(lastDigit);

        //// this will be a running total
        //int sum = 0;

        //// loop through digits from right to left
        //for (int i = static_cast<int>(length) - 1; i >= 0; i--)
        //{
        //    int digit = static_cast<int>(charArr[i]) - 48;

        //    // weight will be the current digit's contribution to
        //    // the running total
        //    int weight;

        //    if (i % 2 == 0)
        //    {
        //        weight = (2 * digit) - static_cast<int>(digit / 5) * 9;
        //    }
        //    else
        //    {

        //        // even-positioned digits just contribute their ASCII
        //        // value minus 48
        //        weight = digit;
        //    }

        //    // keep a running total of weights
        //    sum += weight;
        //}

        //if (sum % 10 == 0)
        //{
        //    return true;
        //}
    }

    return false;
}

BOOL IsValidVINLengthAndChars(LPCSTR szStr)
{
    if (std::char_traits<char>::length(szStr) != 17)
    {
        return FALSE;
    }

    char szTemp[256];
    strcpy_s(szTemp, szStr);
    _strupr_s(szTemp);

    size_t iMult, iTotal;
    LPCSTR pStr;
    for (pStr = szTemp, iMult = 8, iTotal = 0; *pStr != '\0'; pStr++)
    {
        if (isalnum((BYTE)*pStr) == 0)
        {
            return FALSE;
        }

        if ((*pStr == 'I') ||
            (*pStr == 'O') ||
            (*pStr == 'Q'))
        {
            return FALSE;
        }
    }

    return TRUE;
}

BOOL IsValidVIN(LPCSTR szStr)
{
    if (std::char_traits<char>::length(szStr) != 17)
    {
        return FALSE;
    }

    char szTemp[256];
    strcpy_s(szTemp, szStr);
    _strupr_s(szTemp);

    size_t iMult, iTotal;
    LPCSTR pStr;
    for (pStr = szTemp, iMult = 8, iTotal = 0; *pStr != '\0'; pStr++)
    {
        if (isalnum((BYTE)*pStr) == 0)
        {
            return FALSE;
        }

        if ((*pStr == 'I') ||
            (*pStr == 'O') ||
            (*pStr == 'Q'))
        {
            return FALSE;
        }

        if (pStr != (szTemp + 8))
        {
            if ((*pStr >= 'A') && (*pStr <= 'H'))
            {
                iTotal += (((*pStr - 'A') + 1) * iMult);
            }
            else if ((*pStr >= 'J') && (*pStr <= 'P'))
            {
                iTotal += (((*pStr - 'J') + 1) * iMult);
            }
            else if (*pStr == 'R')
            {
                iTotal += (9 * iMult);
            }
            else if ((*pStr >= 'S') && (*pStr <= 'Z'))
            {
                iTotal += (((*pStr - 'S') + 2) * iMult);
            }
            else if ((*pStr >= '0') && (*pStr <= '9'))
            {
                iTotal += ((*pStr - '0') * iMult);
            }

            iMult--;

            if (iMult == 1)
            {
                iMult = 10;
            }
        }
    }

    iTotal %= 11;

    if (iTotal == 10)
    {
        return (*(szTemp + 8) == 'X');
    }

    return (*(szTemp + 8) == (char)('0' + iTotal));
}

BOOL IsValidEFileString(LPCSTR szStr)
{
    BOOL bNonZeros(FALSE);
    BOOL bAlphaNumeric(FALSE);

    for (LPCSTR pStr = szStr; *pStr != '\0'; pStr++)
    {
        if (isalnum((BYTE)*pStr))
        {
            bAlphaNumeric = TRUE;

            if (*pStr != '0')
            {
                bNonZeros = TRUE;
            }
        }

        if (bAlphaNumeric && bNonZeros)
        {
            break;
        }
    }

    return (bAlphaNumeric && bNonZeros);
}

BOOL IsValidRepublicIDNumber(LPCSTR szStr)
{
    Tax::xstring str = szStr;

    if (str.length() < 2 || str.length() > 20)
    {
        return FALSE;
    }

    if (std::count_if(str.begin(), str.end(), isdigit) < 1)
    {
        return FALSE;
    }

    if ((str.Find("123456789") != -1) ||
        (str.Find("987654321") != -1))
    {
        return FALSE;
    }

    if (!str.empty())
    {
        if (isdigit(str[0]))
        {
            if (Tax::xstring(str.length(), str[0]) == str) // if str is all the same digit
            {
                return FALSE;
            }
        }
    }

    return TRUE;
}

BOOL IsValidEmail(LPCSTR szStr)
{
    Tax::xstring email = szStr;
    email.MakeLower();

    int firstIndex = email.Find("@");
    int indexLastChar = static_cast<int>(email.size() - 1);

    if ((firstIndex < 0) ||              // Must have an "@"
        (firstIndex == 0) ||             // At least one char before the "@" 
        (firstIndex == indexLastChar))   // At least one char after the "@" 
    {
        return FALSE;
    }

    int secondIndex = email.Find("@", firstIndex + 1);
    if (secondIndex > 0)            // Can't have more than one "@"
    {
        return FALSE;
    }

    //Can't have two periods next to each other
    if (email.Find("..") >= 0)
    {
        return FALSE;
    }

    //Can't have a period right before the "@"
    if (email.Find(".@") >= 0)
    {
        return FALSE;
    }

    //Can't have a period right after the "@"
    if (email.Find("@.") >= 0)
    {
        return FALSE;
    }

    return TRUE;
}

CTaxString GetNameControl(LPCSTR szStr, LONG lLength)
{
    char szName[64];
    LPCSTR pStr;
    INT_PTR lCount;

    for (pStr = szStr, lCount = 0; *pStr != '\0'; pStr++)
    {
        if (isalpha((BYTE)*pStr) || (*pStr == '-'))
        {
            szName[lCount] = *pStr;
            lCount++;

            if (lCount == lLength)
            {
                break;
            }
        }
    }

    for (; lCount < lLength; lCount++)
    {
        szName[lCount] = ' ';
    }

    szName[lCount] = '\0';
    _strupr_s(szName);
    CTaxString strTemp = szName;
    return strTemp;
}

CTaxString GetCity(LPCSTR szCityStateZip)
{
    CTaxString str;

    CTaxString strCSZ = Trim(szCityStateZip);

    if (strCSZ.IsEmpty())
    {
        return str;
    }

    BOOL bCity, bState, bZip, bSep;
    LPCSTR pStr;
    size_t i;
    for (i = strCSZ.GetLength(), pStr = (LPCSTR)strCSZ + (i - 1), bCity = FALSE, bState = FALSE, bSep = FALSE, bZip = TRUE;
         i > 0; i--, pStr--)
    {
        if (bZip)
        {
            if (isdigit((BYTE)*pStr) || (*pStr == '-'))
                ;
            else if (isalpha((BYTE)*pStr))
            {
                bZip = FALSE;
                bState = TRUE;
            }
        }

        if (bState)
        {
            if (isalpha((BYTE)*pStr))
            {
                if (!bSep)
                    ;
                else
                {
                    bState = FALSE;
                    bSep = FALSE;
                    bCity = TRUE;
                }
            }
            else
            {
                bSep = TRUE;
            }
        }

        if (bCity)
        {
            LPSTR pTempStr = _strdup((LPCSTR)strCSZ);
            *(pTempStr + i) = '\0';
            str = pTempStr;
            free(pTempStr);
            break;
        }
    }

    return str;
}

CTaxString GetState(LPCSTR szCityStateZip)
{
    CTaxString str;

    CTaxString strCSZ = Trim(szCityStateZip);

    if (strCSZ.IsEmpty())
    {
        return str;
    }

    BOOL bState, bZip;
    LPCSTR pStr;
    size_t i, iLen;
    for (i = strCSZ.GetLength(), pStr = (LPCSTR)strCSZ + (i - 1), iLen = 0, bState = FALSE, bZip = TRUE;
         i > 0; i--, pStr--)
    {
        if (bZip)
        {
            if (isdigit((BYTE)*pStr) || (*pStr == '-'))
                ;
            else if (isalpha((BYTE)*pStr))
            {
                bZip = FALSE;
                bState = TRUE;
            }
        }

        if (bState)
        {
            if (isalpha((BYTE)*pStr))
            {
                iLen++;
            }
            else
            {
                if (iLen > 0)
                {
                    LPSTR pTempStr = _strdup(pStr + 1);
                    *(pTempStr + iLen) = '\0';
                    _strupr_s(pTempStr, iLen + 1);
                    str = pTempStr;
                    free(pTempStr);
                }

                break;
            }
        }
    }

    return str;
}

CTaxString GetZip(LPCSTR szCityStateZip)
{
    CTaxString str;

    CTaxString strCSZ = Trim(szCityStateZip);

    if (strCSZ.IsEmpty())
    {
        return str;
    }

    LPCSTR pStr;
    size_t i, iLen;
    for (i = strCSZ.GetLength(), pStr = (LPCSTR)strCSZ + (i - 1), iLen = 0;
         i > 0; i--, pStr--)
    {
        if (isdigit((BYTE)*pStr) || (*pStr == '-'))
        {
            iLen++;
        }
        else
        {
            if (iLen > 0)
            {
                LPSTR pTempStr = _strdup(pStr + 1);
                *(pTempStr + iLen) = '\0';
                str = pTempStr;
                free(pTempStr);
            }

            break;
        }
    }

    return str;
}

void TrimStr(LPSTR szStr)
{
    size_t iLen;
    LPSTR pStr;
    for (iLen = std::char_traits<char>::length(szStr), pStr = szStr + (iLen - 1);
         (iLen > 0) && (*pStr <= ' ');
         *pStr = '\0', pStr--, iLen--);
}

void ReplaceWord(LPSTR szStr, LPCSTR szFind, LPCSTR szReplace)
{
    char szTemp[256];
    LPSTR pFind;
    size_t iFind = std::char_traits<char>::length(szFind);
    size_t iReplace = std::char_traits<char>::length(szReplace);

    *szTemp = '\0';
    LPSTR pTemp = szTemp;
    LPSTR pStr = szStr;

    while (pFind = strstr(pStr, szFind))
    {
        if (((pFind == pStr) || (*(pFind - 1) == ' ')) &&
            ((*(pFind + iFind) == '\0') || (*(pFind + iFind) == ' ')))
        {
            size_t i = static_cast<size_t>(pFind - pStr);
            strncpy_s(pTemp, sizeof(szTemp) - std::char_traits<char>::length(szTemp), pStr, std::char_traits<char>::length(pStr));
            pTemp += i;
            strncpy_s(pTemp, sizeof(szTemp) - std::char_traits<char>::length(szTemp) + iFind, szReplace, iReplace);
            pTemp += iReplace;
        }
        else
        {
            size_t i = static_cast<size_t>(pFind - pStr) + iFind;
            strncpy_s(pTemp, sizeof(szTemp) - std::char_traits<char>::length(szTemp), pStr, i);
            pTemp += i;
        }

        pStr = pFind + iFind;
    }
    strcpy_s(pTemp, sizeof(szTemp) - std::char_traits<char>::length(szTemp), pStr);
    strcpy_s(szStr, BUFFER_SIZE, szTemp);
}

void ProcessLastName(LPSTR szName, int iSize)
{
    LPSTR pStr, pTemp;
    char szTemp[BUFFER_SIZE];

    for (pStr = szName, pTemp = szTemp; *pStr != '\0'; pStr++)
    {
        if (*pStr == ',')
        {
            *pStr = ' ';
        }

        if (!isalnum((BYTE)*pStr) && (*pStr != ' ') && (*pStr != '-'))
        {
            continue;
        }

        if ((*pStr == ' ') && ((pStr == szName) || (*(pStr - 1) == ' ')))
        {
            continue;
        }

        *pTemp = *pStr;
        pTemp++;
    }

    *pTemp = '\0';
    TrimStr(szTemp);
    ReplaceWord(szTemp, "2ND", "II");
    ReplaceWord(szTemp, "3RD", "III");
    ReplaceWord(szTemp, "4TH", "IV");
    ReplaceWord(szTemp, "5TH", "V");
    ReplaceWord(szTemp, "6TH", "VI");
    ReplaceWord(szTemp, "7TH", "VII");
    ReplaceWord(szTemp, "8TH", "VIII");
    ReplaceWord(szTemp, "9TH", "IX");
    ReplaceWord(szTemp, "2nd", "II");
    ReplaceWord(szTemp, "3rd", "III");
    ReplaceWord(szTemp, "4th", "IV");
    ReplaceWord(szTemp, "5th", "V");
    ReplaceWord(szTemp, "6th", "VI");
    ReplaceWord(szTemp, "7th", "VII");
    ReplaceWord(szTemp, "8th", "VIII");
    ReplaceWord(szTemp, "9th", "IX");
    ReplaceWord(szTemp, "111", "III");
    ReplaceWord(szTemp, "11", "II");
    ReplaceWord(szTemp, "2", "II");
    ReplaceWord(szTemp, "3", "III");
    ReplaceWord(szTemp, "4", "IV");
    ReplaceWord(szTemp, "5", "V");
    ReplaceWord(szTemp, "6", "VI");
    ReplaceWord(szTemp, "7", "VII");
    ReplaceWord(szTemp, "8", "VIII");
    ReplaceWord(szTemp, "9", "IX");
    strcpy_s(szName, iSize, szTemp);
}

CTaxString GetLastName(LPCSTR szName)
{
    LPSTR pTemp;
    char szTemp[BUFFER_SIZE];

    strcpy_s(szTemp, szName);

    if (pTemp = strrchr(szTemp, ','))
    {
        *pTemp = '\0';
    }

    ProcessLastName(szTemp, sizeof(szTemp));

    if (pTemp = strrchr(szTemp, ' '))
    {
        pTemp++;

        if ((_stricmp(pTemp, "II") == 0) ||
            (_stricmp(pTemp, "III") == 0) ||
            (_stricmp(pTemp, "IV") == 0) ||
            (_stricmp(pTemp, "V") == 0) ||
            (_stricmp(pTemp, "VI") == 0) ||
            (_stricmp(pTemp, "VII") == 0) ||
            (_stricmp(pTemp, "VIII") == 0) ||
            (_stricmp(pTemp, "IX") == 0) ||
            (_stricmp(pTemp, "JR") == 0) ||
            (_stricmp(pTemp, "SR") == 0))
        {
            pTemp--;
            *pTemp = '\0';
        }
    }

    CTaxString str = szTemp;
    return str;
}

CTaxString GetNameSuffix(LPCSTR szName)
{
    LPSTR pTemp;
    char szTemp[BUFFER_SIZE];
    CTaxString str;

    strcpy_s(szTemp, szName);
    ProcessLastName(szTemp, sizeof(szTemp));
    str.Empty();

    if (pTemp = strrchr(szTemp, ' '))
    {
        pTemp++;

        if ((_stricmp(pTemp, "II") == 0) ||
            (_stricmp(pTemp, "III") == 0) ||
            (_stricmp(pTemp, "IV") == 0) ||
            (_stricmp(pTemp, "V") == 0) ||
            (_stricmp(pTemp, "VI") == 0) ||
            (_stricmp(pTemp, "VII") == 0) ||
            (_stricmp(pTemp, "VIII") == 0) ||
            (_stricmp(pTemp, "IX") == 0) ||
            (_stricmp(pTemp, "JR") == 0) ||
            (_stricmp(pTemp, "SR") == 0))
        {
            str = pTemp;
        }
    }

    return str;
}

CTaxString GetFirstName(LPCSTR szFirstName)
{
    LPCSTR pStr;
    size_t i, iLen;
    BOOL bMI;
    char szTemp[BUFFER_SIZE];

    CTaxString str = Trim(szFirstName);
    strcpy_s(szTemp, str);
    str.Empty();
    for (i = std::char_traits<char>::length(szTemp), pStr = szTemp + (i - 1), iLen = 0, bMI = TRUE; i > 0; i--, pStr--)
    {
        if (bMI)
        {
            if (isalpha((BYTE)*pStr))
            {
                iLen++;
            }
            else if (iLen > 0)
            {
                bMI = FALSE;
            }
        }
        else
        {
            if (isalpha((BYTE)*pStr))
            {
                break;
            }
        }
    }

    if (!bMI && (iLen == 1))
    {
        szTemp[i] = '\0';
    }

    str = szTemp;
    return str;
}

CTaxString GetMiddleInitial(LPCSTR szFirstName)
{
    LPCSTR pStr;
    size_t i, iLen;
    char szTemp[BUFFER_SIZE];

    CTaxString str = Trim(szFirstName);
    strcpy_s(szTemp, str);
    str.Empty();
    for (i = std::char_traits<char>::length(szTemp), pStr = szTemp + (i - 1), iLen = 0; i > 0; i--, pStr--)
    {
        if (isalpha((BYTE)*pStr))
        {
            iLen++;
        }
        else if (iLen > 0)
        {
            break;
        }
    }

    if ((i > 0) && (iLen == 1))
    {
        str = *(pStr + 1);
    }

    return str;
}

TAXCURRENCY GetSalesTax(LPCSTR szState, LONG lExemptions, TAXCURRENCY currIncome)
{
    TAXCURRENCY currValue(0);

    const SalesTaxInfo *salesTaxInfo = nullptr;

    for (const auto& item : g_calcStaticData.salesTax)
    {
        if (item.name == szState)
        {
            salesTaxInfo = &item;
            break;
        }
    }

    if (salesTaxInfo)
    {
        if (lExemptions > 0)
        {
            size_t iExempt = std::min(lExemptions, (LONG)6);

            // bugbug - look at implementing raw data file to have max index and amount stepping
            //          info built into the file itself so the code is more robust when the tables
            //          change
            TAXCURRENCY currTemp;
            size_t iIncome;
            for (iIncome = 0, currTemp = 2000000; (iIncome < 18) && (currIncome >= currTemp); iIncome++)
            {
                if (currTemp >= 20000000)
                {
                    currTemp += 2500000;
                }
                else if (currTemp >= 10000000)
                {
                    currTemp += 2000000;
                }
                else
                {
                    currTemp += 1000000;
                }
            }

            currValue = TAXCURRENCY(salesTaxInfo->incomeBrackets[iIncome][iExempt - 1]) * 100;
        }
    }

    return currValue;
}


// app functions

//THESE FUNCTIONS ARE OBSOLETE AS OF TY2018 AND SHOULD BE REMOVED ONCE NO LONGER USED IN THE MATH

BOOL IsFree(CTaxFormManager* pFormMgr)
{
    return pFormMgr->HasProductFlag(PRODUCTFLAG_ISPKGFREE) || pFormMgr->HasProductFlag(PRODUCTFLAG_ISPKGFFA);
}

BOOL IsBasic(CTaxFormManager* pFormMgr)
{
    return pFormMgr->HasProductFlag(PRODUCTFLAG_ISPKGBASIC);
}

BOOL IsPlus(CTaxFormManager* pFormMgr)
{
    return pFormMgr->HasProductFlag(PRODUCTFLAG_ISPKGPLUS);
}

BOOL IsPremium(CTaxFormManager* pFormMgr)
{
    return pFormMgr->HasProductFlag(PRODUCTFLAG_ISPKGPREMIUM);
}


//returns true if any of the skus in the list are the current edition
BOOL IsSku(CTaxFormManager* pFormMgr, LPCSTR szSkuList)
{
    Tax::xstring skuList = szSkuList;

    size_t nTokenPos = 0;
    //This is written in a weird way to work around the "quirky" (buggy) behavior of xstring.
    if (skuList.find(",") > -1)
    {
        Tax::xstring sku = skuList.Tokenize(',', nTokenPos);

        while (!sku.IsEmpty())
        {
            sku.Replace(" ", "");
            sku = PRODUCTFLAG_ISPKGPREFIX + sku;
            if (pFormMgr->HasProductFlag(sku))
            {
                return TRUE;
            }
            nTokenPos++;
            sku = skuList.Tokenize(',', nTokenPos);
        }
    }
    else
    {
        Tax::xstring sku = szSkuList;
        sku = PRODUCTFLAG_ISPKGPREFIX + sku;
        if (pFormMgr->HasProductFlag(sku))
        {
            return TRUE;
        }
    }

    return FALSE;
}

BOOL IsPreparer(CTaxFormManager* pFormMgr)
{
    return pFormMgr->HasProductFlag(PRODUCTFLAG_ISPREPARER);
}

BOOL IsPrepEnterprise(CTaxFormManager* pFormMgr)
{
    return pFormMgr->HasProductFlag(PRODUCTFLAG_ISPREPENTERPRISE);
}

BOOL IsPreview(CTaxFormManager* pFormMgr)
{
    return pFormMgr->HasProductFlag(PRODUCTFLAG_ISPREVIEW);
}

BOOL IsOnline(CTaxFormManager* pFormMgr)
{
    return pFormMgr->HasProductFlag(PRODUCTFLAG_ISONLINE);
}

BOOL IsTablet(CTaxFormManager* pFormMgr)
{
    return pFormMgr->HasProductFlag(PRODUCTFLAG_ISTABLET);
}

BOOL IsPhone(CTaxFormManager* pFormMgr)
{
    return pFormMgr->HasProductFlag(PRODUCTFLAG_ISPHONE);
}

BOOL IsMobile(CTaxFormManager* pFormMgr)
{
    return (IsTablet(pFormMgr) || IsPhone(pFormMgr));
}

BOOL IsPrepDiscount(CTaxFormManager* pFormMgr)
{
    return pFormMgr->HasProductFlag(PRODUCTFLAG_ISPREPDISCOUNT);
}

TAXCURRENCY GetBankPrice(CTaxFormManager* pFormMgr)
{
    pFormMgr->UpdatePricingInfo(PRICINGINFO_BANKPRICE);
    return pFormMgr->GetPricingInfo(PRICINGINFO_BANKPRICE);
}

TAXCURRENCY GetBankTransFee(CTaxFormManager* pFormMgr)
{
    pFormMgr->UpdatePricingInfo(PRICINGINFO_BANKTRANSFEE);
    return pFormMgr->GetPricingInfo(PRICINGINFO_BANKTRANSFEE);
}

TAXCURRENCY GetMaxAuditMarkupPrice(CTaxFormManager* pFormMgr)
{
    pFormMgr->UpdatePricingInfo(PRICINGINFO_MAXAUDITMARKUPPRICE);
    return pFormMgr->GetPricingInfo(PRICINGINFO_MAXAUDITMARKUPPRICE);
}

TAXCURRENCY GetAuditPrice(CTaxFormManager* pFormMgr)
{
    pFormMgr->UpdatePricingInfo(PRICINGINFO_AUDITPRICE);
    return pFormMgr->GetPricingInfo(PRICINGINFO_AUDITPRICE);
}

TAXCURRENCY GetDasFee(CTaxFormManager* pFormMgr)
{
    pFormMgr->UpdatePricingInfo(PRICINGINFO_DASFEE);
    return pFormMgr->GetPricingInfo(PRICINGINFO_DASFEE);
}

TAXCURRENCY GetProductFees(CTaxFormManager* pFormMgr)
{
    pFormMgr->UpdatePricingInfo(PRICINGINFO_PRODUCTFEES);
    return pFormMgr->GetPricingInfo(PRICINGINFO_PRODUCTFEES);
}

TAXCURRENCY GetProductFeesAlwaysWithBank(CTaxFormManager* pFormMgr)
{
    pFormMgr->UpdatePricingInfo(PRICINGINFO_PRODUCTFEESALWAYSWITHBANK);
    return pFormMgr->GetPricingInfo(PRICINGINFO_PRODUCTFEESALWAYSWITHBANK);
}

BOOL HasBankQualifiedState(CTaxFormManager* pFormMgr)
{
    pFormMgr->UpdatePricingInfo(PRICINGINFO_HASBANKQUALIFIEDSTATE);
    return (pFormMgr->GetPricingInfo(PRICINGINFO_HASBANKQUALIFIEDSTATE) != 0);
}

// form functions

BOOL IsChildCopy(ITaxFormManager* pFormMgr, WORD wChildFormID, WORD wChildCopyID, ITaxForm* pParentForm)
{
    ITaxForm* pChild;

    if (pParentForm &&
        (pChild = pFormMgr->GetFormByIndex(wChildFormID, wChildCopyID)) &&
        (pChild->GetParent() == pParentForm))
    {
        return TRUE;
    }

    return FALSE;
}

BOOL IsParentCopy(ITaxFormManager* pFormMgr, WORD wParentFormID, WORD wParentCopyID, ITaxForm* pChildForm)
{
    ITaxForm* pParent;

    if (pChildForm &&
        (pParent = pFormMgr->GetFormByIndex(wParentFormID, wParentCopyID)) &&
        (pParent == pChildForm->GetParent()))
    {
        return TRUE;
    }

    return FALSE;
}

WORD GetAllCopies(ITaxFormManager* pFormMgr, WORD wFormID)
{
    return pFormMgr->GetTotalCopies(wFormID);
}

WORD GetStatusCopies(ITaxFormManager* pFormMgr, WORD wFormID, DWORD dwStatus)
{
    size_t wCount, wCopy;
    ITaxForm* pForm;

    for (wCount = 0, wCopy = 1; pForm = pFormMgr->GetFormByIndex(wFormID, static_cast<WORD>(wCopy)); wCopy++)
    {
        if (pForm->GetStatus(dwStatus))
        {
            wCount++;
        }
    }

    return static_cast<WORD>(wCount);
}

WORD GetChildCopies(ITaxFormManager* pFormMgr, WORD wChildFormID, ITaxForm* pParentForm)
{
    if (!pParentForm)
    {
        return 0;
    }

    size_t wCount, wCopy;
    ITaxForm* pChild;
    for (wCount = 0, wCopy = 1; pChild = pFormMgr->GetFormByIndex(wChildFormID, static_cast<WORD>(wCopy)); wCopy++)
    {
        if (pChild->GetParent() == pParentForm)
        {
            wCount++;
        }
    }

    return static_cast<WORD>(wCount);
}

WORD GetParentCopy(ITaxFormManager* pFormMgr, WORD wParentFormID, ITaxForm* pChildForm)
{
    ITaxForm* pParent;

    if (pChildForm &&
        (pParent = pChildForm->GetParent()) &&
        (pParent->GetFormManager() == pFormMgr) &&
        (pParent->GetID() == wParentFormID))
    {
        return pParent->GetCopyIndex();
    }

    return 0;
}

WORD GetFieldCopies(ITaxFormManager* pFormMgr, WORD wFormID, WORD wFieldID, WORD wIndex)
{
    size_t wCount, wCopy;
    ITaxForm* pForm;
    ITaxField* pField;

    for (wCount = 0, wCopy = 1; pForm = pFormMgr->GetFormByIndex(wFormID, static_cast<WORD>(wCopy)); wCopy++)
    {
        pField = pForm->GetField(wFieldID + wIndex);

        if (pField->GetBool())
        {
            wCount++;
        }
    }

    return static_cast<WORD>(wCount);
}

WORD ChildCopies(ITaxFormManager* pFormMgr, WORD wChildFormID, ITaxForm* pParentForm)
{
    if (!pParentForm)
    {
        return 0;
    }

    ITaxForm* pChild;
    for (size_t wCopy = 1; pChild = pFormMgr->GetFormByIndex(wChildFormID, static_cast<WORD>(wCopy)); wCopy++)
    {
        pChild->SetStatus(FORMSTATUS_REFERENCE, (pChild->GetParent() == pParentForm));
    }

    return COPY_REFERENCE;
}

WORD ParentCopy(ITaxFormManager* pFormMgr, WORD wParentFormID, ITaxForm* pChildForm)
{
    ITaxForm* pParent;

    if (pChildForm &&
        (pParent = pChildForm->GetParent()) &&
        (pParent->GetFormManager() == pFormMgr) &&
        (pParent->GetID() == wParentFormID))
    {
        return pParent->GetCopyIndex();
    }

    return 0;
}

WORD StatusCopies(ITaxFormManager* pFormMgr, WORD wFormID, DWORD dwStatus)
{
    ITaxForm* pForm;

    for (size_t wCopy = 1; pForm = pFormMgr->GetFormByIndex(wFormID, static_cast<WORD>(wCopy)); wCopy++)
    {
        if (pForm->GetStatus(dwStatus))
        {
            pForm->SetStatus(FORMSTATUS_REFERENCE, TRUE);
        }
    }

    return COPY_REFERENCE;
}

CTaxString GetStaticCopyStr(ITaxFormManager* pFormMgr, WORD wFormID, WORD wCopyIndex)
{
    CTaxString strCopy("");
    ITaxForm* pForm = pFormMgr->GetFormByIndex(wFormID, wCopyIndex);

    if (pForm)
    {
        char szCopy[16];
        sprintf_s(szCopy, "%i", pForm->GetCopyID());
        strCopy = szCopy;
    }

    return strCopy;
}

BOOL IsFeatureAvailable(CTaxFormManager* pFormMgr, LPCSTR szfeatureName)
{
    return pFormMgr->GetDisabledFeaturesCore()->isFeatureEnabled(szfeatureName);
}


CTaxString OhioRitaStr(ITaxFormManager* pFormMgr, LPCSTR city, LPCSTR dataname)
{
    Tax::OhioRita* ohioRita = pFormMgr->GetOhioRita();
    return ohioRita->getString(city, dataname);
}

DOUBLE OhioRitaDbl(ITaxFormManager* pFormMgr, LPCSTR city, LPCSTR dataname, LPCSTR date)
{
    Tax::OhioRita* ohioRita = pFormMgr->GetOhioRita();
    return ohioRita->getDouble(city, dataname, date);
}

BOOL OhioRitaBool(ITaxFormManager* pFormMgr, LPCSTR city, LPCSTR dataname)
{
    Tax::OhioRita* ohioRita = pFormMgr->GetOhioRita();
    return ohioRita->getBool(city, dataname);
}

BOOL HasConsent(CTaxFormManager* pFormMgr, LPCSTR consentName)
{
    return pFormMgr->HasConsent(consentName);
}

WORD FieldCopies(ITaxFormManager* pFormMgr, WORD wFormID, WORD wFieldID, WORD wIndex)
{
    ITaxForm* pForm;
    ITaxField* pField;

    for (size_t wCopy = 1; pForm = pFormMgr->GetFormByIndex(wFormID, static_cast<WORD>(wCopy)); wCopy++)
    {
        pField = pForm->GetField(wFieldID + wIndex);
        pForm->SetStatus(FORMSTATUS_REFERENCE, pField->GetBool());
    }

    return COPY_REFERENCE;
}

WORD GetCopy(ITaxForm* pForm)
{
    return pForm->GetCopyIndex();
}

BOOL GetStatus(DWORD dwStatus, ITaxForm* pForm)
{
    return pForm->GetStatus(dwStatus);
}

BOOL FieldUsingFMV(CTaxFormManager* pFormMgr, WORD wFormID, WORD wFieldID, WORD wIndex, WORD wCopyID)
{
    // deprecated: has been returning false for some time...stub until math uses are removed

    return FALSE;
}

LONG GetMod10CheckDigit(LPCSTR szStr)
{
    LPCSTR pStr;
    int i, j, k(0);

    for (pStr = szStr, i = 0, j = 0; *pStr != '\0'; pStr++, i++)
    {
        if (!isdigit((BYTE)*pStr))
        {
            i--;
            continue;
        }

        if ((i % 2) == 0)
        {
            j += (*pStr - '0');
        }
        else
        {
            k = (*pStr - '0') * 2;
            j += (k / 10) + (k % 10);
        }
    }

    if ((k = 10 - (j % 10)) == 10)
    {
        k = 0;
    }

    return k;
}

LONG GetAdventCheckDigit(LPCSTR szStr)
{
    int i(0), j(0), k(0);
    //start at the end of the string
    LPCSTR pStr = szStr + (std::char_traits<char>::length(szStr) - 1);

    //standard mod 10 calculation, except we are starting at the end of the string and moving towards the beginning
    for (; pStr >= szStr; pStr--, i++)
    {
        if ((i % 2) == 0)
        {
            j += (*pStr - '0');
        }
        else
        {
            k = (*pStr - '0') * 2;
            j += (k / 10) + (k % 10);
        }
    }

    if ((k = 10 - (j % 10)) == 10)
    {
        k = 0;
    }

    return k;
}

BOOL IsCreatedBy(ITaxForm* pForm, WORD wTriggerFormID, LPCSTR szTriggerFieldName, WORD wTriggerIndex)
{
    BOOL isCurrentFormCreatedByTrigger = FALSE;

    if (szTriggerFieldName && pForm)
    {
        isCurrentFormCreatedByTrigger = pForm->GetTriggerFormID() == wTriggerFormID &&
            _stricmp(szTriggerFieldName, pForm->GetTriggerFieldName()) == 0 &&
            pForm->GetTriggerFieldIndex() == wTriggerIndex;

    }

    return isCurrentFormCreatedByTrigger;
}

LONG GetNumber(ITaxFormManager* pFormMgr, WORD wFormID, WORD wFieldID, WORD wIndex, WORD wCopyID /* = COPY_ALLCOPIES */)
{
    ITaxForm* pForm;
    ITaxField* pField;
    LONG lValue = 0;
    size_t wCopy;

    switch (wCopyID)
    {
        case COPY_ALLCOPIES:
            for (wCopy = 1; pForm = pFormMgr->GetFormByIndex(wFormID, static_cast<WORD>(wCopy)); wCopy++)
            {
                pField = pForm->GetField(wFieldID + wIndex);
                lValue += pField->GetNumber();
            }

            break;

        case COPY_REFERENCE:
            for (wCopy = 1; pForm = pFormMgr->GetFormByIndex(wFormID, static_cast<WORD>(wCopy)); wCopy++)
            {
                if (pForm->GetStatus(FORMSTATUS_REFERENCE))
                {
                    pField = pForm->GetField(wFieldID + wIndex);
                    lValue += pField->GetNumber();
                }
            }

            break;

        case 0:
            break;

        default: // normal copy number
            if (pForm = pFormMgr->GetFormByIndex(wFormID, wCopyID))
            {
                pField = pForm->GetField(wFieldID + wIndex);
                lValue = pField->GetNumber();
            }
    }

    return lValue;
}

TAXCURRENCY GetCurrency(ITaxFormManager* pFormMgr, WORD wFormID, WORD wFieldID, WORD wIndex, WORD wCopyID /* = COPY_ALLCOPIES */)
{
    ITaxForm* pForm;
    ITaxField* pField;
    TAXCURRENCY currValue = 0;
    size_t wCopy;

    switch (wCopyID)
    {
        case COPY_ALLCOPIES:
            for (wCopy = 1; pForm = pFormMgr->GetFormByIndex(wFormID, static_cast<WORD>(wCopy)); wCopy++)
            {
                pField = pForm->GetField(wFieldID + wIndex);
                currValue += pField->GetCurrency();
            }

            break;

        case COPY_REFERENCE:
            for (wCopy = 1; pForm = pFormMgr->GetFormByIndex(wFormID, static_cast<WORD>(wCopy)); wCopy++)
            {
                if (pForm->GetStatus(FORMSTATUS_REFERENCE))
                {
                    pField = pForm->GetField(wFieldID + wIndex);
                    currValue += pField->GetCurrency();
                }
            }

            break;

        case 0:
            break;

        default: // normal copy number
            if (pForm = pFormMgr->GetFormByIndex(wFormID, wCopyID))
            {
                pField = pForm->GetField(wFieldID + wIndex);
                currValue = pField->GetCurrency();
            }
    }

    return currValue;
}

DOUBLE GetFloat(ITaxFormManager* pFormMgr, WORD wFormID, WORD wFieldID, WORD wIndex, WORD wCopyID /* = COPY_ALLCOPIES */)
{
    ITaxForm* pForm;
    ITaxField* pField;
    DOUBLE dValue = 0;
    size_t wCopy;

    switch (wCopyID)
    {
        case COPY_ALLCOPIES:
            for (wCopy = 1; pForm = pFormMgr->GetFormByIndex(wFormID, static_cast<WORD>(wCopy)); wCopy++)
            {
                pField = pForm->GetField(wFieldID + wIndex);
                dValue += pField->GetFloat();
            }

            break;

        case COPY_REFERENCE:
            for (wCopy = 1; pForm = pFormMgr->GetFormByIndex(wFormID, static_cast<WORD>(wCopy)); wCopy++)
            {
                if (pForm->GetStatus(FORMSTATUS_REFERENCE))
                {
                    pField = pForm->GetField(wFieldID + wIndex);
                    dValue += pField->GetFloat();
                }
            }

            break;

        case 0:
            break;

        default: // normal copy number
            if (pForm = pFormMgr->GetFormByIndex(wFormID, wCopyID))
            {
                pField = pForm->GetField(wFieldID + wIndex);
                dValue = pField->GetFloat();
            }
    }

    return dValue;
}

BOOL GetBool(ITaxFormManager* pFormMgr, WORD wFormID, WORD wFieldID, WORD wIndex, WORD wCopyID /* = COPY_ALLCOPIES */)
{
    ITaxForm* pForm;
    ITaxField* pField;
    BOOL bValue = 0;
    size_t wCopy;

    switch (wCopyID)
    {
        case COPY_ALLCOPIES:
            for (wCopy = 1; pForm = pFormMgr->GetFormByIndex(wFormID, static_cast<WORD>(wCopy)); wCopy++)
            {
                pField = pForm->GetField(wFieldID + wIndex);
                bValue += pField->GetBool();
            }

            break;

        case COPY_REFERENCE:
            for (wCopy = 1; pForm = pFormMgr->GetFormByIndex(wFormID, static_cast<WORD>(wCopy)); wCopy++)
            {
                if (pForm->GetStatus(FORMSTATUS_REFERENCE))
                {
                    pField = pForm->GetField(wFieldID + wIndex);
                    bValue += pField->GetBool();
                }
            }

            break;

        case 0:
            break;

        default: // normal copy number
            if (pForm = pFormMgr->GetFormByIndex(wFormID, wCopyID))
            {
                pField = pForm->GetField(wFieldID + wIndex);
                bValue = pField->GetBool();
            }
    }

    return bValue;
}

CTaxDate GetDate(ITaxFormManager* pFormMgr, WORD wFormID, WORD wFieldID, WORD wIndex, WORD wCopyID /* = COPY_ALLCOPIES */)
{
    ITaxForm* pForm;
    ITaxField* pField;
    CTaxDate dateValue;

    switch (wCopyID)
    {
        case COPY_ALLCOPIES:
            if (pForm = pFormMgr->GetFormByIndex(wFormID, 1))
            {
                pField = pForm->GetField(wFieldID + wIndex);
                dateValue.SetDate(pField->GetDate());
            }

            break;

        case COPY_REFERENCE:
            for (size_t wCopy = 1; pForm = pFormMgr->GetFormByIndex(wFormID, static_cast<WORD>(wCopy)); wCopy++)
            {
                if (pForm->GetStatus(FORMSTATUS_REFERENCE))
                {
                    pField = pForm->GetField(wFieldID + wIndex);
                    dateValue.SetDate(pField->GetDate());
                    break;
                }
            }

            break;

        case 0:
            break;

        default: // normal copy number
            if (pForm = pFormMgr->GetFormByIndex(wFormID, wCopyID))
            {
                pField = pForm->GetField(wFieldID + wIndex);
                dateValue.SetDate(pField->GetDate());
            }
    }

    return dateValue;
}

CTaxString GetString(ITaxFormManager* pFormMgr, WORD wFormID, WORD wFieldID, WORD wIndex, WORD wCopyID /* = COPY_ALLCOPIES */)
{
    ITaxForm* pForm;
    ITaxField* pField;
    int iLength;
    LPSTR pStr;
    CTaxString strValue;
    size_t wCopy;

    switch (wCopyID)
    {
        case COPY_ALLCOPIES:
            for (wCopy = 1; pForm = pFormMgr->GetFormByIndex(wFormID, static_cast<WORD>(wCopy)); wCopy++)
            {
                pField = pForm->GetField(wFieldID + wIndex);
                iLength = pField->GetStringLength() + 1;

                if (pStr = (LPSTR)malloc(iLength))
                {
                    pField->GetString(pStr, iLength);
                    strValue += pStr;
                    free(pStr);
                }
            }

            break;

        case COPY_REFERENCE:
            for (wCopy = 1; pForm = pFormMgr->GetFormByIndex(wFormID, static_cast<WORD>(wCopy)); wCopy++)
            {
                if (pForm->GetStatus(FORMSTATUS_REFERENCE))
                {
                    pField = pForm->GetField(wFieldID + wIndex);
                    iLength = pField->GetStringLength() + 1;

                    if (pStr = (LPSTR)malloc(iLength))
                    {
                        pField->GetString(pStr, iLength);
                        strValue += pStr;
                        free(pStr);
                    }
                }
            }

            break;

        case 0:
            break;

        default: // normal copy number
            if (pForm = pFormMgr->GetFormByIndex(wFormID, wCopyID))
            {
                pField = pForm->GetField(wFieldID + wIndex);
                iLength = pField->GetStringLength() + 1;

                if (pStr = (LPSTR)malloc(iLength))
                {
                    pField->GetString(pStr, iLength);
                    strValue = pStr;
                    free(pStr);
                }
            }
    }

    return strValue;
}

LONG GetIndex(ITaxFormManager* pFormMgr, WORD wFormID, WORD wFieldID, WORD wIndex, WORD wCopyID /* = COPY_ALLCOPIES */)
{
    ITaxForm* pForm;
    ITaxField* pField;
    LONG lValue = 0;
    size_t wCopy;

    switch (wCopyID)
    {
        case COPY_ALLCOPIES:
            for (wCopy = 1; pForm = pFormMgr->GetFormByIndex(wFormID, static_cast<WORD>(wCopy)); wCopy++)
            {
                pField = pForm->GetField(wFieldID + wIndex);
                lValue += pField->GetListIndex() + 1;
            }

            break;

        case COPY_REFERENCE:
            for (wCopy = 1; pForm = pFormMgr->GetFormByIndex(wFormID, static_cast<WORD>(wCopy)); wCopy++)
            {
                if (pForm->GetStatus(FORMSTATUS_REFERENCE))
                {
                    pField = pForm->GetField(wFieldID + wIndex);
                    lValue += pField->GetListIndex() + 1;
                }
            }

            break;

        case 0:
            break;

        default: // normal copy number
            if (pForm = pFormMgr->GetFormByIndex(wFormID, wCopyID))
            {
                pField = pForm->GetField(wFieldID + wIndex);
                lValue = pField->GetListIndex() + 1;
            }
    }

    return lValue;
}

LONG GetNumber(CTaxForm* pForm, WORD wFieldID, WORD wIndex)
{
    CTaxField* pField = pForm->GetCalcFieldSafeIndex(wFieldID, wIndex);
    return pField->GetNumber();
}

TAXCURRENCY GetCurrency(CTaxForm* pForm, WORD wFieldID, WORD wIndex)
{
    CTaxField* pField = pForm->GetCalcFieldSafeIndex(wFieldID, wIndex);
    return pField->GetCurrency();
}

DOUBLE GetFloat(CTaxForm* pForm, WORD wFieldID, WORD wIndex)
{
    CTaxField* pField = pForm->GetCalcFieldSafeIndex(wFieldID, wIndex);
    return pField->GetFloat();
}

BOOL GetBool(CTaxForm* pForm, WORD wFieldID, WORD wIndex)
{
    CTaxField* pField = pForm->GetCalcFieldSafeIndex(wFieldID, wIndex);
    return pField->GetBool();
}

CTaxDate GetDate(CTaxForm* pForm, WORD wFieldID, WORD wIndex)
{
    CTaxField* pField = pForm->GetCalcFieldSafeIndex(wFieldID, wIndex);
    return pField->GetCalcDate();
}

CTaxString GetString(CTaxForm* pForm, WORD wFieldID, WORD wIndex)
{
    CTaxField* pField = pForm->GetCalcFieldSafeIndex(wFieldID, wIndex);
    return pField->GetString();
}

LONG GetIndex(CTaxForm* pForm, WORD wFieldID, WORD wIndex)
{
    CTaxField* pField = pForm->GetCalcFieldSafeIndex(wFieldID, wIndex);
    return (pField->GetListIndex() + 1);
}

void UpdateField(ITaxForm* pForm, WORD wFieldID, WORD wIndex)
{
    ITaxField* pField = pForm->GetField(wFieldID + wIndex);
    pField->Calculate();
}

void UpdateField(ITaxFormManager* pFormMgr, WORD wFormID, WORD wFieldID, WORD wIndex)
{
    ITaxForm* pForm;
    ITaxField* pField;

    for (size_t wCopy = 1; pForm = pFormMgr->GetFormByIndex(wFormID, static_cast<WORD>(wCopy)); wCopy++)
    {
        pField = pForm->GetField(wFieldID + wIndex);
        pField->Calculate();
    }
}

void UpdateField(ITaxForm* pForm, WORD wFieldID, WORD wIndex, WORD wLastIndex)
{
    if (wIndex <= wLastIndex)
    {
        ITaxField* pField = pForm->GetField(wFieldID + wIndex);
        pField->Calculate();
    }
}

void UpdateField(ITaxFormManager* pFormMgr, WORD wFormID, WORD wFieldID, WORD wIndex, WORD wLastIndex)
{
    if (wIndex <= wLastIndex)
    {
        ITaxForm* pForm;
        ITaxField* pField;

        for (size_t wCopy = 1; pForm = pFormMgr->GetFormByIndex(wFormID, static_cast<WORD>(wCopy)); wCopy++)
        {
            pField = pForm->GetField(wFieldID + wIndex);
            pField->Calculate();
        }
    }
}

void UpdateField(WORD wFieldIndex, WORD wRefIndex, ITaxForm* pForm, WORD wFieldID, WORD wIndex)
{
    if (wFieldIndex == wRefIndex)
    {
        ITaxField* pField = pForm->GetField(wFieldID + wIndex);
        pField->Calculate();
    }
}

void UpdateField(ITaxFormManager* pFormMgr, WORD wFieldIndex, WORD wRefIndex, WORD wFormID, WORD wFieldID, WORD wIndex)
{
    if (wFieldIndex == wRefIndex)
    {
        ITaxForm* pForm;
        ITaxField* pField;

        for (size_t wCopy = 1; pForm = pFormMgr->GetFormByIndex(wFormID, static_cast<WORD>(wCopy)); wCopy++)
        {
            pField = pForm->GetField(wFieldID + wIndex);
            pField->Calculate();
        }
    }
}

void UpdateFieldArray(ITaxForm* pForm, WORD wFieldID, WORD wLastIndex)
{
    ITaxField* pField;

    for (size_t wIndex = 0; wIndex <= wLastIndex; wIndex++)
    {
        pField = pForm->GetField(wFieldID + static_cast<WORD>(wIndex));
        pField->Calculate();
    }
}

void UpdateFieldArray(ITaxFormManager* pFormMgr, WORD wFormID, WORD wFieldID, WORD wLastIndex)
{
    ITaxForm* pForm;
    ITaxField* pField;

    for (size_t wCopy = 1; pForm = pFormMgr->GetFormByIndex(wFormID, static_cast<WORD>(wCopy)); wCopy++)
    {
        for (size_t wIndex = 0; wIndex <= wLastIndex; wIndex++)
        {
            pField = pForm->GetField(wFieldID + static_cast<WORD>(wIndex));
            pField->Calculate();
        }
    }
}

void UpdateFieldArray(WORD wFieldIndex, WORD wRefIndex, ITaxForm* pForm, WORD wFieldID, WORD wLastIndex)
{
    if (wFieldIndex == wRefIndex)
    {
        ITaxField* pField;

        for (size_t wIndex = 0; wIndex <= wLastIndex; wIndex++)
        {
            pField = pForm->GetField(wFieldID + static_cast<WORD>(wIndex));
            pField->Calculate();
        }
    }
}

void UpdateFieldArray(ITaxFormManager* pFormMgr, WORD wFieldIndex, WORD wRefIndex, WORD wFormID, WORD wFieldID, WORD wLastIndex)
{
    if (wFieldIndex == wRefIndex)
    {
        ITaxForm* pForm;
        ITaxField* pField;

        for (size_t wCopy = 1; pForm = pFormMgr->GetFormByIndex(wFormID, static_cast<WORD>(wCopy)); wCopy++)
        {
            for (size_t wIndex = 0; wIndex <= wLastIndex; wIndex++)
            {
                pField = pForm->GetField(wFieldID + static_cast<WORD>(wIndex));
                pField->Calculate();
            }
        }
    }
}

// Set status - has trigger field
void CreateForm(ITaxFormManager* pFormMgr, ITaxForm* pForm, ITaxField* pField, WORD wIndex,
                WORD wFormID, WORD wCopyID, BOOL bChild /* = FALSE */)
{
    if ((pField->GetIndex() == wIndex) && pField->GetBool())
    {
        ITaxForm* pNewForm;

        if (bChild)
        {
            while ((pFormMgr->GetTotalChildCopies(pForm, wFormID) < wCopyID) &&
                   (pNewForm = pFormMgr->CreateForm(wFormID, TRUE, pForm)))
            {
                pNewForm->SetStatus(FORMSTATUS_MODIFIED, TRUE);
                pFormMgr->UpdateAppFormsTree(pNewForm);
            }
        }
        else
        {
            while ((pFormMgr->GetTotalCopies(wFormID) < wCopyID) &&
                   (pNewForm = pFormMgr->CreateForm(wFormID)))
            {
                pNewForm->SetStatus(FORMSTATUS_MODIFIED, TRUE);
                pFormMgr->UpdateAppFormsTree(pNewForm);
            }
        }
    }
}

// Set status - has trigger field
void CreateFormCopies(ITaxFormManager* pFormMgr, ITaxForm* pForm, ITaxField* pField, WORD wIndex,
                WORD wFormID, WORD wCopiesFormID, WORD wCopiesFieldID)
{
    if ((pField->GetIndex() == wIndex) && pField->GetBool())
    {
        WORD wTotal(0);
        ITaxField* pCopiesField(0);

        ITaxForm* pCopiesForm = pFormMgr->GetForm(wCopiesFormID, 1);
        if (pCopiesForm)
            pCopiesField = pCopiesForm->GetField(wCopiesFieldID);

        if (pCopiesField)
            wTotal = static_cast<WORD>(pCopiesField->GetNumber());

        ITaxForm* pNewForm;
        while ((pFormMgr->GetTotalCopies(wFormID) < wTotal) &&
                (pNewForm = pFormMgr->CreateForm(wFormID)))
        {
            pNewForm->SetStatus(FORMSTATUS_MODIFIED, TRUE);
            pFormMgr->UpdateAppFormsTree(pNewForm);
        }
    }
}

void CreateFormAll(ITaxFormManager* pFormMgr, ITaxForm* pForm, ITaxField* pField, WORD wIndex, WORD wFormID, WORD wCopyID, BOOL bChild,
                   WORD nAdditional, WORD *additionalForms, WORD *additionalCopies, WORD *additionalFields)
{
    for (size_t i = 0; i < nAdditional; i++)
    {
        ITaxForm *formToCheck = pFormMgr->GetForm(additionalForms[i], additionalCopies[i]);
        if (formToCheck)
        {
            ITaxField *fieldToCheck = formToCheck->GetField(additionalFields[i]);
            if (fieldToCheck)
            {
                if (i == 0)
                {
                    //override Form.Field to always be the first one in the list
                    //we're already checking every field here so this is only useful when bChild is true (as is CreateChildAll())
                    //we want to ensure we're creating the form as a child of the first form listed
                    pForm = formToCheck;
                    wCopyID = additionalCopies[i];
                    pField = fieldToCheck;
                    wIndex = fieldToCheck->GetIndex();
                }

                if (!fieldToCheck->GetBool())
                {
                    return;
                }
            }
        }
    }

    CreateForm(pFormMgr, pForm, pField, wIndex, wFormID, wCopyID, bChild);
}

void CreateFormUnique(ITaxFormManager* pFormMgr, ITaxForm* pForm, ITaxField* pField, WORD wIndex, WORD wFormID)
{
    if ((pField->GetIndex() == wIndex) && pField->GetBool())
    {
        // Default to creating the new form
        BOOL createNew = TRUE;

        char szFieldName[64];
        pFormMgr->GetFieldName(szFieldName, pForm->GetID(), pField->GetID());

        // Iterate through the already created forms and see if this trigger field already triggered creation of a form.
        WORD firstCopy(1);
        WORD lastCopy(pFormMgr->GetTotalCopies(wFormID));

        for (WORD currentCopy = firstCopy; currentCopy <= lastCopy && createNew; currentCopy++)
        {
            ITaxForm* pTempForm = pFormMgr->GetFormByIndex(wFormID, currentCopy);

            if (pTempForm)
            {
                if (IsCreatedBy(pTempForm, pForm->GetID(), szFieldName, wIndex))
                {
                    createNew = FALSE;
                }
            }
        }

        ITaxForm* pNewForm;

        // If createNew is TRUE, we should create the form and set the trigger of the new form to be the field we checked above.
        if (createNew && (pNewForm = pFormMgr->CreateForm(wFormID)))
        {
            pNewForm->SetTriggerValues(pForm->GetID(), pForm->GetCopyID(), szFieldName, wIndex);
            pNewForm->SetStatus(FORMSTATUS_MODIFIED, TRUE);
            pFormMgr->UpdateAppFormsTree(pNewForm);
        }
    }
}

void PrintList_Clear(ITaxFormManager *pFormMgr, unsigned int listID)
{
    pFormMgr->PrintList_Clear(listID);
}

void PrintList_AddReturn(ITaxFormManager *pFormMgr, unsigned int listID, unsigned int sublistID,
                         const CTaxString& title)
{
    PrintListItem toAdd(PrintListItem::Return, sublistID);
    toAdd.m_title = title;
    pFormMgr->PrintList_Add(listID, toAdd);
}

void PrintList_AddForm(ITaxFormManager *pFormMgr, unsigned int listID, unsigned int sublistID, 
                       const CTaxString& title, const CTaxString& name)
{
    PrintListItem toAdd(PrintListItem::Form, sublistID);
    toAdd.m_title = title;
    toAdd.m_id = name;
    pFormMgr->PrintList_Add(listID, toAdd);
}

void PrintList_AddHTML(ITaxFormManager *pFormMgr, unsigned int listID, unsigned int sublistID, 
                       const CTaxString& title, const CTaxString& url)
{
    PrintListItem toAdd(PrintListItem::HTML, sublistID);
    toAdd.m_title = title;
    toAdd.m_id = url;
    pFormMgr->PrintList_Add(listID, toAdd);
}

void PrintList_AddCustom(ITaxFormManager *pFormMgr, unsigned int listID, unsigned int sublistID,
                         const CTaxString& title, const CTaxString& func)
{
    PrintListItem toAdd(PrintListItem::Custom, sublistID);
    toAdd.m_title = title;
    toAdd.m_id = func;
    pFormMgr->PrintList_Add(listID, toAdd);
}

#ifdef CALCFEDERAL

BOOL IsChildCopy(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szChildFormName, WORD wChildCopyID, ITaxForm* pParentForm)
{
    ITaxFormManager* pStateMgr(pFormMgr->GetStateFormManager(szModName));

    if (pStateMgr && pParentForm)
    {
        WORD wChildFormID(pStateMgr->GetFormID(szChildFormName));

        if (wChildFormID > 0)
        {
            return IsChildCopy(pStateMgr, wChildFormID, wChildCopyID, pParentForm);
        }
    }

    return 0;
}

BOOL IsParentCopy(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szParentFormName, WORD wParentCopyID, ITaxForm* pChildForm)
{
    ITaxFormManager* pStateMgr(pFormMgr->GetStateFormManager(szModName));

    if (pStateMgr && pChildForm)
    {
        WORD wParentFormID(pStateMgr->GetFormID(szParentFormName));

        if (wParentFormID > 0)
        {
            return IsParentCopy(pStateMgr, wParentFormID, wParentCopyID, pChildForm);
        }
    }

    return 0;
}

WORD GetAllCopies(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szFormName)
{
    ITaxFormManager* pStateMgr(pFormMgr->GetStateFormManager(szModName));

    if (pStateMgr)
    {
        WORD wFormID(pStateMgr->GetFormID(szFormName));

        if (wFormID > 0)
        {
            return GetAllCopies(pStateMgr, wFormID);
        }
    }

    return 0;
}

WORD GetChildCopies(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szChildFormName, ITaxForm* pParentForm)
{
    ITaxFormManager* pStateMgr(pFormMgr->GetStateFormManager(szModName));

    if (pStateMgr && pParentForm)
    {
        WORD wChildFormID(pStateMgr->GetFormID(szChildFormName));

        if (wChildFormID > 0)
        {
            return GetChildCopies(pStateMgr, wChildFormID, pParentForm);
        }
    }

    return 0;
}

WORD GetParentCopy(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szParentFormName, ITaxForm* pChildForm)
{
    ITaxFormManager* pStateMgr(pFormMgr->GetStateFormManager(szModName));

    if (pStateMgr && pChildForm)
    {
        WORD wParentFormID(pStateMgr->GetFormID(szParentFormName));

        if (wParentFormID > 0)
        {
            return GetParentCopy(pStateMgr, wParentFormID, pChildForm);
        }
    }

    return 0;
}

WORD GetFieldCopies(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szFormName, LPCSTR szFieldName, WORD wIndex)
{
    ITaxFormManager* pStateMgr(pFormMgr->GetStateFormManager(szModName));

    if (pStateMgr)
    {
        WORD wFormID(pStateMgr->GetFormID(szFormName));

        if (wFormID > 0)
        {
            WORD wFieldID(pStateMgr->GetFieldID(wFormID, szFieldName));

            if (wFieldID > 0)
            {
                return GetFieldCopies(pStateMgr, wFormID, wFieldID, wIndex);
            }
        }
    }

    return 0;
}

WORD GetStatusCopies(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szFormName, DWORD dwStatus)
{
    ITaxFormManager* pStateMgr(pFormMgr->GetStateFormManager(szModName));

    if (pStateMgr)
    {
        WORD wFormID(pStateMgr->GetFormID(szFormName));

        if (wFormID > 0)
        {
            return GetStatusCopies(pStateMgr, wFormID, dwStatus);
        }
    }

    return 0;
}

WORD ChildCopies(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szChildFormName, ITaxForm* pParentForm)
{
    ITaxFormManager* pStateMgr(pFormMgr->GetStateFormManager(szModName));

    if (pStateMgr && pParentForm)
    {
        WORD wChildFormID(pStateMgr->GetFormID(szChildFormName));

        if (wChildFormID > 0)
        {
            return ChildCopies(pStateMgr, wChildFormID, pParentForm);
        }
    }

    return 0;
}

WORD ParentCopy(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szParentFormName, ITaxForm* pChildForm)
{
    ITaxFormManager* pStateMgr(pFormMgr->GetStateFormManager(szModName));

    if (pStateMgr && pChildForm)
    {
        WORD wParentFormID(pStateMgr->GetFormID(szParentFormName));

        if (wParentFormID > 0)
        {
            return ParentCopy(pStateMgr, wParentFormID, pChildForm);
        }
    }

    return 0;
}

WORD FieldCopies(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szFormName, LPCSTR szFieldName, WORD wIndex)
{
    ITaxFormManager* pStateMgr(pFormMgr->GetStateFormManager(szModName));

    if (pStateMgr)
    {
        WORD wFormID(pStateMgr->GetFormID(szFormName));

        if (wFormID > 0)
        {
            WORD wFieldID(pStateMgr->GetFieldID(wFormID, szFieldName));

            if (wFieldID > 0)
            {
                return FieldCopies(pStateMgr, wFormID, wFieldID, wIndex);
            }
        }
    }

    return 0;
}

WORD StatusCopies(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szFormName, DWORD dwStatus)
{
    ITaxFormManager* pStateMgr(pFormMgr->GetStateFormManager(szModName));

    if (pStateMgr)
    {
        WORD wFormID(pStateMgr->GetFormID(szFormName));

        if (wFormID > 0)
        {
            return StatusCopies(pStateMgr, wFormID, dwStatus);
        }
    }

    return 0;
}

CTaxString GetStaticCopyStr(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szFormName, WORD wCopyIndex)
{
    ITaxFormManager* pStateMgr(pFormMgr->GetStateFormManager(szModName));

    if (pStateMgr)
    {
        WORD wFormID(pStateMgr->GetFormID(szFormName));

        if (wFormID > 0)
        {
            return GetStaticCopyStr(pStateMgr, wFormID, wCopyIndex);
        }
    }

    return 0;
}

LONG GetNumber(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szFormName, LPCSTR szFieldName, WORD wIndex, WORD wCopyID /* = COPY_ALLCOPIES */)
{
    ITaxFormManager* pStateMgr(pFormMgr->GetStateFormManager(szModName));

    if (pStateMgr)
    {
        WORD wFormID(pStateMgr->GetFormID(szFormName));

        if (wFormID > 0)
        {
            WORD wFieldID(pStateMgr->GetFieldID(wFormID, szFieldName));

            if (wFieldID > 0)
            {
                return GetNumber(pStateMgr, wFormID, wFieldID, wIndex, wCopyID);
            }
        }
    }

    return 0;
}

TAXCURRENCY GetCurrency(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szFormName, LPCSTR szFieldName, WORD wIndex, WORD wCopyID /* = COPY_ALLCOPIES */)
{
    ITaxFormManager* pStateMgr(pFormMgr->GetStateFormManager(szModName));

    if (pStateMgr)
    {
        WORD wFormID(pStateMgr->GetFormID(szFormName));

        if (wFormID > 0)
        {
            WORD wFieldID(pStateMgr->GetFieldID(wFormID, szFieldName));

            if (wFieldID > 0)
            {
                return GetCurrency(pStateMgr, wFormID, wFieldID, wIndex, wCopyID);
            }
        }
    }

    return (TAXCURRENCY)(0);
}

DOUBLE GetFloat(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szFormName, LPCSTR szFieldName, WORD wIndex, WORD wCopyID /* = COPY_ALLCOPIES */)
{
    ITaxFormManager* pStateMgr(pFormMgr->GetStateFormManager(szModName));

    if (pStateMgr)
    {
        WORD wFormID(pStateMgr->GetFormID(szFormName));

        if (wFormID > 0)
        {
            WORD wFieldID(pStateMgr->GetFieldID(wFormID, szFieldName));

            if (wFieldID > 0)
            {
                return GetFloat(pStateMgr, wFormID, wFieldID, wIndex, wCopyID);
            }
        }
    }

    return 0.0;
}

BOOL GetBool(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szFormName, LPCSTR szFieldName, WORD wIndex, WORD wCopyID /* = COPY_ALLCOPIES */)
{
    ITaxFormManager* pStateMgr(pFormMgr->GetStateFormManager(szModName));

    if (pStateMgr)
    {
        WORD wFormID(pStateMgr->GetFormID(szFormName));

        if (wFormID > 0)
        {
            WORD wFieldID(pStateMgr->GetFieldID(wFormID, szFieldName));

            if (wFieldID > 0)
            {
                return GetBool(pStateMgr, wFormID, wFieldID, wIndex, wCopyID);
            }
        }
    }

    return 0;
}

CTaxDate GetDate(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szFormName, LPCSTR szFieldName, WORD wIndex, WORD wCopyID /* = COPY_ALLCOPIES */)
{
    ITaxFormManager* pStateMgr(pFormMgr->GetStateFormManager(szModName));

    if (pStateMgr)
    {
        WORD wFormID(pStateMgr->GetFormID(szFormName));

        if (wFormID > 0)
        {
            WORD wFieldID(pStateMgr->GetFieldID(wFormID, szFieldName));

            if (wFieldID > 0)
            {
                return GetDate(pStateMgr, wFormID, wFieldID, wIndex, wCopyID);
            }
        }
    }

    return CTaxDate();
}

CTaxString GetString(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szFormName, LPCSTR szFieldName, WORD wIndex, WORD wCopyID /* = COPY_ALLCOPIES */)
{
    ITaxFormManager* pStateMgr(pFormMgr->GetStateFormManager(szModName));

    if (pStateMgr)
    {
        WORD wFormID(pStateMgr->GetFormID(szFormName));

        if (wFormID > 0)
        {
            WORD wFieldID(pStateMgr->GetFieldID(wFormID, szFieldName));

            if (wFieldID > 0)
            {
                return GetString(pStateMgr, wFormID, wFieldID, wIndex, wCopyID);
            }
        }
    }

    return "";
}

LONG GetIndex(ITaxFormManager* pFormMgr, LPCSTR szModName, LPCSTR szFormName, LPCSTR szFieldName, WORD wIndex, WORD wCopyID /* = COPY_ALLCOPIES */)
{
    ITaxFormManager* pStateMgr(pFormMgr->GetStateFormManager(szModName));

    if (pStateMgr)
    {
        WORD wFormID(pStateMgr->GetFormID(szFormName));

        if (wFormID > 0)
        {
            WORD wFieldID(pStateMgr->GetFieldID(wFormID, szFieldName));

            if (wFieldID > 0)
            {
                return GetIndex(pStateMgr, wFormID, wFieldID, wIndex, wCopyID);
            }
        }
    }

    return 0;
}

//Helpers for AveragePremium data
unsigned long AveragePremium_GetStateIndex(LPCSTR state)
{
    for (size_t i=0; i<g_premiumsStateCount; i++)
    {
        if (_stricmp(state, g_premiumsStateData[i].m_state) == 0)
        {
            return static_cast<unsigned long>(i);
        }
    }

    ASSERT(FALSE && "Unknown state encountered in AveragePremium_GetStateIndex");
    return -1;
}

unsigned long AveragePremium_GetCountyIndex(LPCSTR state, LPCSTR county)
{
    unsigned long stateIndex = AveragePremium_GetStateIndex(state);
    if (stateIndex != -1)
    {
        unsigned long stateStart = g_premiumsStateData[stateIndex].m_startIndex;
        unsigned long stateEnd = stateStart + g_premiumsStateData[stateIndex].m_counties;

        for (size_t i=stateStart; i<stateEnd; i++)
        {
            if (_stricmp(county, g_premiumsCountyData[i].m_county) == 0)
            {
                ASSERT(_stricmp(state, g_premiumsCountyData[i].m_state) == 0); // check consistency

                return static_cast<unsigned long>(i);
            }
        }

        ASSERT(FALSE && "Unknown county encountered in AveragePremium_GetCountyIndex");
        return -1;
    }

    return -1;
}

//AveragePremium API
LONG AveragePremium_CountStates()
{
    return static_cast<LONG>(g_premiumsStateCount);
}

CTaxString AveragePremium_GetState(LONG index)
{
    ASSERT(index >= 0);
    ASSERT(static_cast<unsigned long>(index) < g_premiumsStateCount);

    return g_premiumsStateData[index].m_state;
}

LONG AveragePremium_CountCounties(LPCSTR state)
{
    ASSERT(state);

    unsigned long stateIndex = AveragePremium_GetStateIndex(state);
    if (stateIndex != -1)
    {
        return g_premiumsStateData[stateIndex].m_counties;
    }

    return 0;
}

CTaxString AveragePremium_GetCounty(LPCSTR state, LONG index)
{
    ASSERT(state);

    unsigned long stateIndex = AveragePremium_GetStateIndex(state);
    if (stateIndex != -1)
    {
        ASSERT(index >= 0);
        ASSERT(static_cast<unsigned long>(index) < g_premiumsStateData[stateIndex].m_counties);

        return g_premiumsCountyData[g_premiumsStateData[stateIndex].m_startIndex + index].m_county;
    }

    return "";
}

TAXCURRENCY AveragePremium_GetAmount(LPCSTR state, LPCSTR county, BOOL employeeOnly)
{
    ASSERT(state);
    ASSERT(county);

    unsigned long countyIndex = AveragePremium_GetCountyIndex(state, county);
    if (countyIndex != -1)
    {
        if (employeeOnly)
        {
            return g_premiumsCountyData[countyIndex].m_employeeOnlyDollars * 100;
        }
        else
        {
            return g_premiumsCountyData[countyIndex].m_familyDollars * 100;
        }
    }

    return 0;
}

#endif
