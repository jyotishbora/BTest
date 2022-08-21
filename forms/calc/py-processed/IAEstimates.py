from forms.out import IAESTIMATES
from forms.out import IAF1040
from forms.out import IAREQUIRED
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def AdjBal_Calculation():
    return get_currency(IAESTIMATES.Balance) + get_currency(IAESTIMATES.OthTax)

def AskSp_Calculation():
    if get_bool(IAF1040.CombMFS) == True or get_bool(IAF1040.MFJ) == True:
        if get_currency(IAESTIMATES.Overpayment) > 0 and get_bool(IAESTIMATES.Taxpayer) == True:
            return 1
        else:
            return 0
    else:
        return 0

def AskStillPay_Calculation():
    if get_bool(IAESTIMATES.StillPay) == True:
        return 1
    elif get_bool(IAESTIMATES.Print) == False:
        return 1
    else:
        return 0

def Balance_Calculation():
    return max_value(0, get_currency(IAESTIMATES.IATax) - get_currency(IAESTIMATES.NonrefCr))

def Common_Calculation():
    return get_string(USWBasicInfo.TPCommon)

def DDAcct_Calculation():
    if get_bool(IAESTIMATES.DirectDebEst) == True and  ( get_currency(IAESTIMATES.Est1Amt) == 0 and get_currency(IAESTIMATES.Est2Amt) == 0 and get_currency(IAESTIMATES.Est3Amt) == 0 and get_currency(IAESTIMATES.Est4Amt) == 0 ) :
        return ''
    elif  ( get_bool(IAESTIMATES.DirectDebEst) == True and  ( get_currency(IAESTIMATES.Est1Amt) > 0 or get_currency(IAESTIMATES.Est2Amt) > 0 or get_currency(IAESTIMATES.Est3Amt) > 0 or get_currency(IAESTIMATES.Est4Amt) > 0 ) ) :
        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)
        Acct = ''
        while count <= MaxAcct:
            if get_string(USWBankAcct.BankAcct, count) != '':
                if get_bool(USWBankAcct.Default, count) == True:
                    return get_string(USWBankAcct.BankAcct, count)
                    count = 99
            count = count + 1
        return ''
    else:
        return ''

def Description_Calculation():
    if get_bool(IAESTIMATES.Taxpayer) == True:
        return get_string(IAESTIMATES.Common)
    elif get_bool(IAESTIMATES.Spouse) == True:
        return get_string(IAESTIMATES.SpouseCommon)
    else:
        return get_string(IAESTIMATES.JtCommon)

def Est1Amt_Calculation():
    if get_bool(IAESTIMATES.Est1) == True:
        return get_currency(IAESTIMATES.V1PayAmt1)
    else:
        return 0

def Est1Date_Calculation():
    if get_bool(IAESTIMATES.Est1) == True:
        return MakeDate(4, 30, YearNumber + 1)
    else:
        return ''

def Est2Amt_Calculation():
    if get_bool(IAESTIMATES.Est2) == True:
        return get_currency(IAESTIMATES.V2PayAmt1)
    else:
        return 0

def Est2Date_Calculation():
    if get_bool(IAESTIMATES.Est2) == True:
        return MakeDate(7, 1, YearNumber + 1)
    else:
        return ''

def Est3Amt_Calculation():
    if get_bool(IAESTIMATES.Est3) == True:
        return get_currency(IAESTIMATES.V3PayAmt1)
    else:
        return 0

def Est3Date_Calculation():
    if get_bool(IAESTIMATES.Est3) == True:
        return MakeDate(9, 30, YearNumber + 1)
    else:
        return ''

def Est4Amt_Calculation():
    if get_bool(IAESTIMATES.Est4) == True:
        return get_currency(IAESTIMATES.V4PayAmt1)
    else:
        return 0

def Est4Date_Calculation():
    if get_bool(IAESTIMATES.Est4) == True:
        return MakeDate(1, 31, YearNumber + 2)
    else:
        return ''

def EstAcctNum_Calculation():
    if get_bool(IAESTIMATES.DirectDebEst) == True and  ( get_currency(IAESTIMATES.Est1Amt) == 0 and get_currency(IAESTIMATES.Est2Amt) == 0 and get_currency(IAESTIMATES.Est3Amt) == 0 and get_currency(IAESTIMATES.Est4Amt) == 0 ) :
        return ''
    elif  ( get_bool(IAESTIMATES.DirectDebEst) == True and  ( get_currency(IAESTIMATES.Est1Amt) > 0 or get_currency(IAESTIMATES.Est2Amt) > 0 or get_currency(IAESTIMATES.Est3Amt) > 0 or get_currency(IAESTIMATES.Est4Amt) > 0 ) ) :
        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)
        while count <= MaxAcct:
            if get_string(USWBankAcct.BankAcct, count) != '':
                if IsStrEqual(get_string(IAESTIMATES.DDAcct), get_string(USWBankAcct.BankAcct, count)):
                    return get_string(USWBankAcct.AcctNum, count)
                    count = 99
            count = count + 1
        return ''
    else:
        return ''

def EstAcctNum2_Calculation(Index):
    return get_string(IAESTIMATES.EstAcctNum)

def EstChecking_Calculation():
    if get_bool(IAESTIMATES.DirectDebEst) == True and  ( get_currency(IAESTIMATES.Est1Amt) == 0 and get_currency(IAESTIMATES.Est2Amt) == 0 and get_currency(IAESTIMATES.Est3Amt) == 0 and get_currency(IAESTIMATES.Est4Amt) == 0 ) :
        return 0
    elif  ( get_bool(IAESTIMATES.DirectDebEst) == True and  ( get_currency(IAESTIMATES.Est1Amt) > 0 or get_currency(IAESTIMATES.Est2Amt) > 0 or get_currency(IAESTIMATES.Est3Amt) > 0 or get_currency(IAESTIMATES.Est4Amt) > 0 ) ) :
        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)
        while count <= MaxAcct:
            if get_string(USWBankAcct.BankAcct, count) != '':
                if IsStrEqual(get_string(IAESTIMATES.DDAcct), get_string(USWBankAcct.BankAcct, count)):
                    return get_bool(USWBankAcct.Checking, count)
                    count = 99
            count = count + 1
        return 0
    else:
        return 0

def EstChecking2_Calculation(Index):
    return get_bool(IAESTIMATES.EstChecking)

def EstDed_Calculation():
    # updated for 2018
    if get_bool(IAESTIMATES.Joint) == True:
        return Decimal("5120")
    else:
        return Decimal("2080")

def EstEFW_Calculation():
    if get_bool(IAESTIMATES.EstIAT) == True:
        return 0
    elif get_bool(IAESTIMATES.DirectDebEst) == True:
        if get_bool(IAESTIMATES.EstPay1) == True or get_bool(IAESTIMATES.EstPay2) == True or get_bool(IAESTIMATES.EstPay3) == True or get_bool(IAESTIMATES.EstPay4) == True:
            return 1
        else:
            return 0
    else:
        return 0

def EstIAT_Calculation():
    if get_bool(IAESTIMATES.DirectDebEst) == True and  ( get_currency(IAESTIMATES.Est1Amt) == 0 and get_currency(IAESTIMATES.Est2Amt) == 0 and get_currency(IAESTIMATES.Est3Amt) == 0 and get_currency(IAESTIMATES.Est4Amt) == 0 ) :
        return 0
    elif  ( get_bool(IAESTIMATES.DirectDebEst) == True and  ( get_currency(IAESTIMATES.Est1Amt) > 0 or get_currency(IAESTIMATES.Est2Amt) > 0 or get_currency(IAESTIMATES.Est3Amt) > 0 or get_currency(IAESTIMATES.Est4Amt) > 0 ) ) :
        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)
        while count <= MaxAcct:
            if get_string(USWBankAcct.BankAcct, count) != '':
                if IsStrEqual(get_string(IAESTIMATES.DDAcct), get_string(USWBankAcct.BankAcct, count)):
                    return get_bool(USWBankAcct.IAT, count)
                    count = 99
            count = count + 1
        return 0
    else:
        return 0

def EstIATNo_Calculation():
    return get_bool(IAESTIMATES.EstEFW)

def EstPay1_Calculation():
    if get_bool(IAESTIMATES.Est1) == True and get_currency(IAESTIMATES.Est1Amt) > 0:
        return 1
    else:
        return 0

def EstPay2_Calculation():
    if get_bool(IAESTIMATES.Est2) == True and get_currency(IAESTIMATES.Est2Amt) > 0:
        return 1
    else:
        return 0

def EstPay3_Calculation():
    if get_bool(IAESTIMATES.Est3) == True and get_currency(IAESTIMATES.Est3Amt) > 0:
        return 1
    else:
        return 0

def EstPay4_Calculation():
    if get_bool(IAESTIMATES.Est4) == True and get_currency(IAESTIMATES.Est4Amt) > 0:
        return 1
    else:
        return 0

def EstRTN_Calculation():
    if get_bool(IAESTIMATES.DirectDebEst) == True and  ( get_currency(IAESTIMATES.Est1Amt) == 0 and get_currency(IAESTIMATES.Est2Amt) == 0 and get_currency(IAESTIMATES.Est3Amt) == 0 and get_currency(IAESTIMATES.Est4Amt) == 0 ) :
        return ''
    elif  ( get_bool(IAESTIMATES.DirectDebEst) == True and  ( get_currency(IAESTIMATES.Est1Amt) > 0 or get_currency(IAESTIMATES.Est2Amt) > 0 or get_currency(IAESTIMATES.Est3Amt) > 0 or get_currency(IAESTIMATES.Est4Amt) > 0 ) ) :
        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)
        while count <= MaxAcct:
            if get_string(USWBankAcct.BankAcct, count) != '':
                if IsStrEqual(get_string(IAESTIMATES.DDAcct), get_string(USWBankAcct.BankAcct, count)):
                    return get_string(USWBankAcct.RTN, count)
                    count = 99
            count = count + 1
        return ''
    else:
        return ''

def EstRTN2_Calculation(Index):
    return get_string(IAESTIMATES.EstRTN)

def EstSavings_Calculation():
    if get_bool(IAESTIMATES.DirectDebEst) == True and  ( get_currency(IAESTIMATES.Est1Amt) == 0 and get_currency(IAESTIMATES.Est2Amt) == 0 and get_currency(IAESTIMATES.Est3Amt) == 0 and get_currency(IAESTIMATES.Est4Amt) == 0 ) :
        return 0
    elif  ( get_bool(IAESTIMATES.DirectDebEst) == True and  ( get_currency(IAESTIMATES.Est1Amt) > 0 or get_currency(IAESTIMATES.Est2Amt) > 0 or get_currency(IAESTIMATES.Est3Amt) > 0 or get_currency(IAESTIMATES.Est4Amt) > 0 ) ) :
        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)
        while count <= MaxAcct:
            if get_string(USWBankAcct.BankAcct, count) != '':
                if IsStrEqual(get_string(IAESTIMATES.DDAcct), get_string(USWBankAcct.BankAcct, count)):
                    return get_bool(USWBankAcct.Savings, count)
                    count = 99
            count = count + 1
        return 0
    else:
        return 0

def EstSavings2_Calculation(Index):
    return get_bool(IAESTIMATES.EstSavings)

def Exist_Calculation():
    return 1

def GrossIncOption_Calculation():
    if get_bool(IAESTIMATES.Gross) == True:
        return c_dollar(get_float(IAESTIMATES.Gross5) * 0.05)
    else:
        return 0

def IANetInc_Calculation():
    return max_value(0, get_currency(IAESTIMATES.NetInc) - get_currency(IAESTIMATES.FedTaxPd))

def IATax_Calculation():
    if get_float(IAESTIMATES.NRIAPer) < 1:
        return c_dollar(get_float(IAESTIMATES.NetTax) * get_float(IAESTIMATES.NRIAPer))
    else:
        return get_currency(IAESTIMATES.NetTax)

def JtCommon_Calculation():
    return get_string(USWBasicInfo.CombFirst)

def MainName_Calculation():
    if get_bool(IAESTIMATES.Taxpayer) == True:
        return get_string(IAREQUIRED.TPComb)
    elif get_bool(IAESTIMATES.Spouse) == True:
        return get_string(IAREQUIRED.SPComb)
    else:
        return get_string(IAREQUIRED.JTComb)

def Names_Calculation():
    if get_bool(IAESTIMATES.Spouse) == True:
        return get_string(IAREQUIRED.SPCombName)
    elif get_bool(IAESTIMATES.Taxpayer) == True:
        return get_string(IAREQUIRED.TPCombName)
    else:
        return get_string(IAREQUIRED.CombNames)

def NetTax_Calculation():
    return max_value(0, get_currency(IAESTIMATES.TotEstLiab) - get_currency(IAESTIMATES.TotCr))

def NoBankSel3_Calculation():
    if get_bool(IAESTIMATES.DirectDebEst) == True:
        if trim(get_string(IAESTIMATES.DDAcct)) == '':
            return 1
        else:
            return 0
    else:
        return 0

def NoBankSelInt3_Calculation():
    if get_bool(IAESTIMATES.DirectDebEst) == True and  ( get_currency(IAESTIMATES.Est1Amt) > 0 or get_currency(IAESTIMATES.Est2Amt) > 0 or get_currency(IAESTIMATES.Est3Amt) > 0 or get_currency(IAESTIMATES.Est4Amt) > 0 ) :
        if get_bool(USTopicList.HaveBankWSSend) == False:
            return 0
        elif trim(get_string(IAESTIMATES.DDAcct)) == '':
            return 1
        else:
            return 0
    else:
        return 0

def NRIAPer_Calculation():
    if get_currency(IAESTIMATES.NetInc) == 0:
        return 0
    elif get_currency(IAESTIMATES.NRIAInc) == 0:
        return 1
    else:
        return min_value(1, Round(( get_float(IAESTIMATES.NRIAInc) / get_float(IAESTIMATES.NetInc) )  * 10000) / 10000)

def Overpayment_Calculation():
    if get_currency(IAF1040.OVerPaid) > 0:
        if get_bool(IAESTIMATES.Spouse) == False:
            return max_value(0, get_currency(IAF1040.OVerPaid) - get_currency(IAF1040.Penalty))
        elif get_bool(IAESTIMATES.Spouse) == True and get_bool(IAESTIMATES.Taxpayer, 1) == False and get_bool(IAESTIMATES.Taxpayer, 2) == False:
            return max_value(0, get_currency(IAF1040.OVerPaid) - get_currency(IAF1040.Penalty))
        else:
            return min_value(max_value(0, ( get_currency(IAF1040.OVerPaid) )  - get_currency(IAF1040.Penalty)), get_currency(IAESTIMATES.SpOvpd, FieldCopies(IAESTIMATES.Taxpayer)))
    else:
        return 0

def Owner_Calculation():
    if get_bool(IAESTIMATES.Taxpayer) == True and trim(get_string(USWBasicInfo.FirstName)) == '':
        return 'the taxpayer'
    elif get_bool(IAESTIMATES.Taxpayer) == True:
        return get_string(USWBasicInfo.FirstName)
    elif get_bool(IAESTIMATES.Spouse) == True and trim(get_string(USWBasicInfo.SpouseFirst)) == '':
        return 'the spouse'
    elif get_bool(IAESTIMATES.Spouse) == True:
        return get_string(USWBasicInfo.SpouseFirst)
    else:
        return 'the taxpayer and spouse'

def Payments_Calculation():
    return get_currency(IAESTIMATES.V1PayAmt1) + get_currency(IAESTIMATES.V2PayAmt1) + get_currency(IAESTIMATES.V3PayAmt1) + get_currency(IAESTIMATES.V4PayAmt1)

def Print_Calculation():
    if get_currency(IAESTIMATES.TaxDue) > 0:
        if get_currency(IAESTIMATES.V1PayAmt1) + get_currency(IAESTIMATES.V2PayAmt1) + get_currency(IAESTIMATES.V3PayAmt1) + get_currency(IAESTIMATES.V4PayAmt1):
            return 1
        else:
            return 0
    else:
        return 0

def PYTaxOption_Calculation():
    TotTax = Currency()

    SubTot = Currency()
    if get_bool(IAESTIMATES.Spouse) == True:
        TotTax = get_currency(IAF1040.BBal4)
    elif get_bool(IAESTIMATES.Taxpayer) == True:
        TotTax = get_currency(IAF1040.ABal4)
    else:
        TotTax = get_currency(IAF1040.ABal4) + get_currency(IAF1040.BBal4)
    if get_currency(IAREQUIRED.IAAGI) > Decimal("150000"):
        SubTot = c_dollar(( TotTax )  * 1.1)
    else:
        SubTot = TotTax
    if get_bool(IAESTIMATES.PYTax) == True:
        return max_value(0, SubTot - get_currency(IAESTIMATES.PYCredits))
    else:
        return 0

def Quarter_Calculation():
    return c_dollar(get_float(IAESTIMATES.TaxDue) * 0.25)

def RndV1_Calculation():
    L16 = Currency()

    R25 = Currency()

    R50 = Currency()

    R100 = Currency()

    Drop = Integer()

    Drop25 = Integer()

    Drop50 = Integer()

    Drop100 = Integer()

    Payment = Currency()

    Payment25 = Currency()

    Payment50 = Currency()

    Payment100 = Currency()
    L16 = get_currency(IAESTIMATES.Roundup10)
    R25 = get_currency(IAESTIMATES.Roundup25)
    R50 = get_currency(IAESTIMATES.Roundup50)
    R100 = get_currency(IAESTIMATES.Roundup100)
    Drop = CLng(L16 / Decimal("40"))
    Drop25 = CLng(R25 / Decimal("100"))
    Drop50 = CLng(R50 / Decimal("200"))
    Drop100 = CLng(R100 / Decimal("400"))
    Payment = ( CCur(Drop) * Decimal("40") )  + Decimal("40")
    Payment25 = ( CCur(Drop25) * Decimal("100") )  + Decimal("100")
    Payment50 = ( CCur(Drop50) * Decimal("200") )  + Decimal("200")
    Payment100 = ( CCur(Drop100) * Decimal("400") )  + Decimal("400")
    if get_bool(IAESTIMATES.Round10) == True:
        if ( L16 % Decimal("40") )  == 0:
            return Round(c_dollar(CDbl(L16) * 0.25))
        else:
            return Round(c_dollar(CDbl(Payment) * 0.25))
    elif get_bool(IAESTIMATES.Round25) == True:
        if ( R25 % Decimal("100") )  == 0:
            return Round(c_dollar(CDbl(R25) * 0.25))
        else:
            return Round(c_dollar(CDbl(Payment25) * 0.25))
    elif get_bool(IAESTIMATES.Round50) == True:
        if ( R50 % Decimal("200") )  == 0:
            return Round(c_dollar(CDbl(R50) * 0.25))
        else:
            return Round(c_dollar(CDbl(Payment50) * 0.25))
    elif get_bool(IAESTIMATES.Round100) == True:
        if ( R100 % Decimal("400") )  == 0:
            return Round(c_dollar(CDbl(R100) * 0.25))
        else:
            return Round(c_dollar(CDbl(Payment100) * 0.25))
    else:
        return Round(c_dollar(get_float(IAESTIMATES.TaxDue) * 0.25))

def RndV2_Calculation():
    L16 = Currency()

    R25 = Currency()

    R50 = Currency()

    R100 = Currency()

    Drop = Integer()

    Drop25 = Integer()

    Drop50 = Integer()

    Drop100 = Integer()

    Payment = Currency()

    Payment25 = Currency()

    Payment50 = Currency()

    Payment100 = Currency()
    L16 = get_currency(IAESTIMATES.Roundup10) - get_currency(IAESTIMATES.V1Pay)
    R25 = get_currency(IAESTIMATES.Roundup25) - get_currency(IAESTIMATES.V1Pay)
    R50 = get_currency(IAESTIMATES.Roundup50) - get_currency(IAESTIMATES.V1Pay)
    R100 = get_currency(IAESTIMATES.Roundup100) - get_currency(IAESTIMATES.V1Pay)
    Drop = CLng(L16 / Decimal("30"))
    Drop25 = CLng(R25 / Decimal("75"))
    Drop50 = CLng(R50 / Decimal("150"))
    Drop100 = CLng(R100 / Decimal("300"))
    Payment = ( CCur(Drop) * Decimal("30") )  + Decimal("30")
    Payment25 = ( CCur(Drop25) * Decimal("75") )  + Decimal("75")
    Payment50 = ( CCur(Drop50) * Decimal("150") )  + Decimal("150")
    Payment100 = ( CCur(Drop100) * Decimal("300") )  + Decimal("300")
    if get_bool(IAESTIMATES.Round10) == True:
        if ( L16 % Decimal("30") )  == 0:
            return Round(c_dollar(CDbl(L16) * 0.333333))
        else:
            return Round(c_dollar(CDbl(Payment) * 0.333333))
    elif get_bool(IAESTIMATES.Round25) == True:
        if ( R25 % Decimal("75") )  == 0:
            return Round(c_dollar(CDbl(R25) * 0.333333))
        else:
            return Round(c_dollar(CDbl(Payment25) * 0.333333))
    elif get_bool(IAESTIMATES.Round50) == True:
        if ( R50 % Decimal("150") )  == 0:
            return Round(c_dollar(CDbl(R50) * 0.333333))
        else:
            return Round(c_dollar(CDbl(Payment50) * 0.333333))
    elif get_bool(IAESTIMATES.Round100) == True:
        if ( R100 % Decimal("300") )  == 0:
            return Round(c_dollar(CDbl(R100) * 0.333333))
        else:
            return Round(c_dollar(CDbl(Payment100) * 0.333333))
    else:
        return Round(c_dollar(CDbl(get_currency(IAESTIMATES.TaxDue) - get_currency(IAESTIMATES.V1Pay)) * 0.333333))

def RndV3_Calculation():
    L16 = Currency()

    R25 = Currency()

    R50 = Currency()

    R100 = Currency()

    Drop = Integer()

    Drop25 = Integer()

    Drop50 = Integer()

    Drop100 = Integer()

    Payment = Currency()

    Payment25 = Currency()

    Payment50 = Currency()

    Payment100 = Currency()
    L16 = get_currency(IAESTIMATES.Roundup10) - get_currency(IAESTIMATES.V1Pay) - get_currency(IAESTIMATES.V2Pay)
    R25 = get_currency(IAESTIMATES.Roundup25) - get_currency(IAESTIMATES.V1Pay) - get_currency(IAESTIMATES.V2Pay)
    R50 = get_currency(IAESTIMATES.Roundup50) - get_currency(IAESTIMATES.V1Pay) - get_currency(IAESTIMATES.V2Pay)
    R100 = get_currency(IAESTIMATES.Roundup100) - get_currency(IAESTIMATES.V1Pay) - get_currency(IAESTIMATES.V2Pay)
    Drop = CLng(L16 / Decimal("20"))
    Drop25 = CLng(R25 / Decimal("50"))
    Drop50 = CLng(R50 / Decimal("100"))
    Drop100 = CLng(R100 / Decimal("200"))
    Payment = ( CCur(Drop) * Decimal("20") )  + Decimal("20")
    Payment25 = ( CCur(Drop25) * Decimal("50") )  + Decimal("50")
    Payment50 = ( CCur(Drop50) * Decimal("100") )  + Decimal("100")
    Payment100 = ( CCur(Drop100) * Decimal("200") )  + Decimal("200")
    if get_bool(IAESTIMATES.Round10) == True:
        if ( L16 % Decimal("20") )  == 0:
            return Round(c_dollar(CDbl(L16) * 0.5))
        else:
            return Round(c_dollar(CDbl(Payment) * 0.5))
    elif get_bool(IAESTIMATES.Round25) == True:
        if ( R25 % Decimal("50") )  == 0:
            return Round(c_dollar(CDbl(R25) * 0.5))
        else:
            return Round(c_dollar(CDbl(Payment25) * 0.5))
    elif get_bool(IAESTIMATES.Round50) == True:
        if ( R50 % Decimal("100") )  == 0:
            return Round(c_dollar(CDbl(R50) * 0.5))
        else:
            return Round(c_dollar(CDbl(Payment50) * 0.5))
    elif get_bool(IAESTIMATES.Round100) == True:
        if ( R100 % Decimal("200") )  == 0:
            return Round(c_dollar(CDbl(R100) * 0.5))
        else:
            return Round(c_dollar(CDbl(Payment100) * 0.5))
    else:
        return Round(c_dollar(CDbl(get_currency(IAESTIMATES.TaxDue) - get_currency(IAESTIMATES.V1Pay) - get_currency(IAESTIMATES.V2Pay)) * 0.5))

def RndV4_Calculation():
    L16 = Currency()

    R25 = Currency()

    R50 = Currency()

    R100 = Currency()

    Drop = Integer()

    Drop25 = Integer()

    Drop50 = Integer()

    Drop100 = Integer()

    Payment = Currency()

    Payment25 = Currency()

    Payment50 = Currency()

    Payment100 = Currency()
    L16 = get_currency(IAESTIMATES.Roundup10) - get_currency(IAESTIMATES.V1Pay) - get_currency(IAESTIMATES.V2Pay) - get_currency(IAESTIMATES.V3Pay)
    R25 = get_currency(IAESTIMATES.Roundup25) - get_currency(IAESTIMATES.V1Pay) - get_currency(IAESTIMATES.V2Pay) - get_currency(IAESTIMATES.V3Pay)
    R50 = get_currency(IAESTIMATES.Roundup50) - get_currency(IAESTIMATES.V1Pay) - get_currency(IAESTIMATES.V2Pay) - get_currency(IAESTIMATES.V3Pay)
    R100 = get_currency(IAESTIMATES.Roundup100) - get_currency(IAESTIMATES.V1Pay) - get_currency(IAESTIMATES.V2Pay) - get_currency(IAESTIMATES.V3Pay)
    Drop = CLng(L16 / Decimal("10"))
    Drop25 = CLng(R25 / Decimal("25"))
    Drop50 = CLng(R50 / Decimal("50"))
    Drop100 = CLng(R100 / Decimal("100"))
    Payment = ( CCur(Drop) * Decimal("10") )  + Decimal("10")
    Payment25 = ( CCur(Drop25) * Decimal("10") )  + Decimal("10")
    Payment50 = ( CCur(Drop50) * Decimal("10") )  + Decimal("10")
    Payment100 = ( CCur(Drop100) * Decimal("100") )  + Decimal("100")
    if get_bool(IAESTIMATES.Round10) == True:
        if ( L16 % Decimal("10") )  == 0:
            return L16
        else:
            return Round(Payment)
    elif get_bool(IAESTIMATES.Round25) == True:
        if ( R25 % Decimal("25") )  == 0:
            return R25
        else:
            return Round(Payment25)
    elif get_bool(IAESTIMATES.Round50) == True:
        if ( R50 % Decimal("50") )  == 0:
            return R50
        else:
            return Round(Payment50)
    elif get_bool(IAESTIMATES.Round100) == True:
        if ( R100 % Decimal("100") )  == 0:
            return R100
        else:
            return Round(Payment100)
    else:
        return Round(get_currency(IAESTIMATES.TaxDue) - get_currency(IAESTIMATES.V1Pay) - get_currency(IAESTIMATES.V2Pay) - get_currency(IAESTIMATES.V3Pay))

def Roundup10_Calculation():
    Required = Currency()

    Drop = Integer()

    Payment = Currency()
    Required = get_currency(IAESTIMATES.TaxDue)
    Drop = CLng(Required / Decimal("40"))
    Payment = ( CCur(Drop) * Decimal("40") )  + Decimal("40")
    if get_bool(IAESTIMATES.Round10) == True:
        if ( Required % Decimal("40") )  == 0:
            return Required
        else:
            return Payment
    else:
        return get_currency(IAESTIMATES.TaxDue)

def Roundup100_Calculation():
    Required = Currency()

    Drop = Integer()

    Payment = Currency()
    Required = get_currency(IAESTIMATES.TaxDue)
    Drop = CLng(get_float(IAESTIMATES.TaxDue) / 40000)
    Payment = ( CCur(Drop) * Decimal("400") )  + Decimal("400")
    if get_bool(IAESTIMATES.Round100) == True:
        if ( Required % Decimal("400") )  == 0:
            return Required
        else:
            return Payment
    else:
        return get_currency(IAESTIMATES.TaxDue)

def Roundup25_Calculation():
    Required = Currency()

    Drop = Integer()

    Payment = Currency()
    Required = get_currency(IAESTIMATES.TaxDue)
    Drop = CLng(get_float(IAESTIMATES.TaxDue) / 10000)
    Payment = ( CCur(Drop) * Decimal("100") )  + Decimal("100")
    if get_bool(IAESTIMATES.Round25) == True:
        if ( Required % Decimal("100") )  == 0:
            return Required
        else:
            return Payment
    else:
        return get_currency(IAESTIMATES.TaxDue)

def Roundup50_Calculation():
    Required = Currency()

    Drop = Integer()

    Payment = Currency()
    Required = get_currency(IAESTIMATES.TaxDue)
    Drop = CLng(CDbl(Required) / 20000)
    Payment = ( CCur(Drop) * Decimal("200") )  + Decimal("200")
    if get_bool(IAESTIMATES.Round50) == True:
        if ( Required % Decimal("200") )  == 0:
            return Required
        else:
            return Payment
    else:
        return get_currency(IAESTIMATES.TaxDue)

def SpouseCommon_Calculation():
    return get_string(USWBasicInfo.SPCommon)

def SSN_Calculation():
    if get_bool(IAESTIMATES.Spouse) == True:
        return get_string(IAF1040.SpouseSSN)
    else:
        return get_string(IAF1040.SSN)

def Tax_Calculation():
    return NextYearTax(get_currency(IAESTIMATES.TaxInc))

def TaxDue_Calculation():
    if get_bool(IAESTIMATES.Gross) == True:
        return get_currency(IAESTIMATES.GrossIncOption)
    elif get_bool(IAESTIMATES.PYTax) == True:
        return get_currency(IAESTIMATES.PYTaxOption)
    elif get_currency(IAESTIMATES.TotEstTax) > Decimal("200") or get_bool(IAESTIMATES.StillPay) == True:
        return get_currency(IAESTIMATES.TotEstTax)
    else:
        return 0

def TaxInc_Calculation():
    return max_value(0, get_currency(IAESTIMATES.IANetInc) - get_currency(IAESTIMATES.EstDed))

def Taxpayer_Calculation():
    return 1

def TotApplied_Calculation():
    return ( get_currency(IAESTIMATES.V1Apply) + get_currency(IAESTIMATES.V2Apply) + get_currency(IAESTIMATES.V3Apply) + get_currency(IAESTIMATES.V4Apply) )

def TotCr_Calculation():
    if get_bool(IAESTIMATES.Joint) == True:
        return Decimal("80")
    else:
        return Decimal("40")

def TotEstimate_Calculation():
    return get_currency(IAESTIMATES.V1Pay) + get_currency(IAESTIMATES.V2Pay) + get_currency(IAESTIMATES.V3Pay) + get_currency(IAESTIMATES.V4Pay)

def TotEstLiab_Calculation():
    return get_currency(IAESTIMATES.Tax) + get_currency(IAESTIMATES.MinTax) + get_currency(IAESTIMATES.LSD)

def TotEstTax_Calculation():
    return max_value(0, get_currency(IAESTIMATES.AdjBal) - get_currency(IAESTIMATES.IACr))

def TotNetTax2_Calculation():
    if get_bool(IAESTIMATES.Taxpayer) == False:
        return get_currency(IAESTIMATES.Overpayment)
    else:
        return max_value(0, get_currency(IAESTIMATES.Overpayment) - get_currency(IAESTIMATES.SpOvpd))

def V1Apply_Calculation():
    Smaller = Currency()
    Smaller = min_value(get_currency(IAESTIMATES.TotNetTax2), get_currency(IAESTIMATES.SpecAmt))
    if get_bool(IAESTIMATES.Refund) == True:
        return 0
    elif get_bool(IAESTIMATES.ApplySpecific) == True and get_currency(IAESTIMATES.TaxDue) == 0:
        return Smaller
    elif get_bool(IAESTIMATES.ApplySpecific) == True:
        return min_value(Smaller, get_currency(IAESTIMATES.V1Pay))
    else:
        return min_value(get_currency(IAESTIMATES.TotNetTax2), get_currency(IAESTIMATES.V1Pay))

def V1Pay_Calculation():
    return get_currency(IAESTIMATES.RndV1)

def V1PayAmt1_Calculation():
    return max_value(0, get_currency(IAESTIMATES.V1Pay) - get_currency(IAESTIMATES.V1Apply))

def V2Apply_Calculation():
    Smaller = Currency()

    Limited = Currency()

    Limited2 = Currency()
    Smaller = min_value(get_currency(IAESTIMATES.TotNetTax2), get_currency(IAESTIMATES.SpecAmt))
    Limited = min_value(get_currency(IAESTIMATES.V2Pay), get_currency(IAESTIMATES.TotNetTax2) - get_currency(IAESTIMATES.V1Pay))
    Limited2 = min_value(get_currency(IAESTIMATES.V2Pay), Smaller - get_currency(IAESTIMATES.V1Pay))
    if get_bool(IAESTIMATES.Refund) == True or get_bool(IAESTIMATES.FirstQt) == True:
        return 0
    elif get_bool(IAESTIMATES.ApplySpecific) == True:
        return max_value(0, Limited2)
    else:
        return max_value(0, Limited)

def V2Pay_Calculation():
    return get_currency(IAESTIMATES.RndV2)

def V2PayAmt1_Calculation():
    return max_value(0, get_currency(IAESTIMATES.V2Pay) - get_currency(IAESTIMATES.V2Apply))

def V3Apply_Calculation():
    Smaller = Currency()

    Limited = Currency()

    Limited2 = Currency()
    Smaller = min_value(get_currency(IAESTIMATES.TotNetTax2), get_currency(IAESTIMATES.SpecAmt))
    Limited = min_value(get_currency(IAESTIMATES.V3Pay), get_currency(IAESTIMATES.TotNetTax2) - get_currency(IAESTIMATES.V1Pay) - get_currency(IAESTIMATES.V2Pay))
    Limited2 = min_value(get_currency(IAESTIMATES.V3Pay), Smaller - get_currency(IAESTIMATES.V1Pay) - get_currency(IAESTIMATES.V2Pay))
    if get_bool(IAESTIMATES.Refund) == True or get_bool(IAESTIMATES.FirstQt) == True:
        return 0
    elif get_bool(IAESTIMATES.ApplySpecific) == True:
        return max_value(0, Limited2)
    else:
        return max_value(0, Limited)

def V3Pay_Calculation():
    return get_currency(IAESTIMATES.RndV3)

def V3PayAmt1_Calculation():
    return max_value(0, get_currency(IAESTIMATES.V3Pay) - get_currency(IAESTIMATES.V3Apply))

def V4Apply_Calculation():
    Smaller = Currency()

    Limited = Currency()
    if get_bool(IAESTIMATES.Refund) == True or get_bool(IAESTIMATES.FirstQt) == True:
        return 0
    elif get_bool(IAESTIMATES.ApplyAll) == True:
        Limited = max_value(0, get_currency(IAESTIMATES.TotNetTax2) - get_currency(IAESTIMATES.V1Pay) - get_currency(IAESTIMATES.V2Pay) - get_currency(IAESTIMATES.V3Pay))
        return min_value(get_currency(IAESTIMATES.V4Pay), Limited)
    elif get_bool(IAESTIMATES.ApplySpecific) == True:
        Smaller = min_value(get_currency(IAESTIMATES.TotNetTax2), get_currency(IAESTIMATES.SpecAmt))
        return max_value(0, Smaller - get_currency(IAESTIMATES.V1Apply) - get_currency(IAESTIMATES.V2Apply) - get_currency(IAESTIMATES.V3Apply))
    else:
        return 0

def V4Pay_Calculation():
    return get_currency(IAESTIMATES.RndV4)

def V4PayAmt1_Calculation():
    return max_value(0, get_currency(IAESTIMATES.V4Pay) - get_currency(IAESTIMATES.V4Apply))


