from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def AdjBal_Calculation():
    ReturnVal = GetCurrency(IAEstimates.Balance) + GetCurrency(IAEstimates.OthTax)

def AskSp_Calculation():
    if GetBool(IAF1040.CombMFS) == True or GetBool(IAF1040.MFJ) == True:
        if GetCurrency(IAEstimates.Overpayment) > 0 and GetBool(IAEstimates.Taxpayer) == True:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def AskStillPay_Calculation():
    if GetBool(IAEstimates.StillPay) == True:
        ReturnVal = 1
    elif GetBool(IAEstimates.Print) == False:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Balance_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAEstimates.IATax) - GetCurrency(IAEstimates.NonrefCr))

def Common_Calculation():
    ReturnVal = GetString(USWBasicInfo.TPCommon)

def DDAcct_Calculation():
    if GetBool(IAEstimates.DirectDebEst) == True and  ( GetCurrency(IAEstimates.Est1Amt) == 0 and GetCurrency(IAEstimates.Est2Amt) == 0 and GetCurrency(IAEstimates.Est3Amt) == 0 and GetCurrency(IAEstimates.Est4Amt) == 0 ) :
        ReturnVal = ''
    elif  ( GetBool(IAEstimates.DirectDebEst) == True and  ( GetCurrency(IAEstimates.Est1Amt) > 0 or GetCurrency(IAEstimates.Est2Amt) > 0 or GetCurrency(IAEstimates.Est3Amt) > 0 or GetCurrency(IAEstimates.Est4Amt) > 0 ) ) :
        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)
        Acct = ''
        while count <= MaxAcct:
            if GetString(USWBankAcct.BankAcct, count) != '':
                if GetBool(USWBankAcct.Default, count) == True:
                    ReturnVal = GetString(USWBankAcct.BankAcct, count)
                    count = 99
            count = count + 1
        ReturnVal = ''
    else:
        ReturnVal = ''

def Description_Calculation():
    if GetBool(IAEstimates.Taxpayer) == True:
        ReturnVal = GetString(IAEstimates.Common)
    elif GetBool(IAEstimates.Spouse) == True:
        ReturnVal = GetString(IAEstimates.SpouseCommon)
    else:
        ReturnVal = GetString(IAEstimates.JtCommon)

def Est1Amt_Calculation():
    if GetBool(IAEstimates.Est1) == True:
        ReturnVal = GetCurrency(IAEstimates.V1PayAmt1)
    else:
        ReturnVal = 0

def Est1Date_Calculation():
    if GetBool(IAEstimates.Est1) == True:
        ReturnVal = MakeDate(4, 30, YearNumber + 1)
    else:
        ReturnVal = ''

def Est2Amt_Calculation():
    if GetBool(IAEstimates.Est2) == True:
        ReturnVal = GetCurrency(IAEstimates.V2PayAmt1)
    else:
        ReturnVal = 0

def Est2Date_Calculation():
    if GetBool(IAEstimates.Est2) == True:
        ReturnVal = MakeDate(7, 1, YearNumber + 1)
    else:
        ReturnVal = ''

def Est3Amt_Calculation():
    if GetBool(IAEstimates.Est3) == True:
        ReturnVal = GetCurrency(IAEstimates.V3PayAmt1)
    else:
        ReturnVal = 0

def Est3Date_Calculation():
    if GetBool(IAEstimates.Est3) == True:
        ReturnVal = MakeDate(9, 30, YearNumber + 1)
    else:
        ReturnVal = ''

def Est4Amt_Calculation():
    if GetBool(IAEstimates.Est4) == True:
        ReturnVal = GetCurrency(IAEstimates.V4PayAmt1)
    else:
        ReturnVal = 0

def Est4Date_Calculation():
    if GetBool(IAEstimates.Est4) == True:
        ReturnVal = MakeDate(1, 31, YearNumber + 2)
    else:
        ReturnVal = ''

def EstAcctNum_Calculation():
    if GetBool(IAEstimates.DirectDebEst) == True and  ( GetCurrency(IAEstimates.Est1Amt) == 0 and GetCurrency(IAEstimates.Est2Amt) == 0 and GetCurrency(IAEstimates.Est3Amt) == 0 and GetCurrency(IAEstimates.Est4Amt) == 0 ) :
        ReturnVal = ''
    elif  ( GetBool(IAEstimates.DirectDebEst) == True and  ( GetCurrency(IAEstimates.Est1Amt) > 0 or GetCurrency(IAEstimates.Est2Amt) > 0 or GetCurrency(IAEstimates.Est3Amt) > 0 or GetCurrency(IAEstimates.Est4Amt) > 0 ) ) :
        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)
        while count <= MaxAcct:
            if GetString(USWBankAcct.BankAcct, count) != '':
                if IsStrEqual(GetString(IAEstimates.DDAcct), GetString(USWBankAcct.BankAcct, count)):
                    ReturnVal = GetString(USWBankAcct.AcctNum, count)
                    count = 99
            count = count + 1
        ReturnVal = ''
    else:
        ReturnVal = ''

def EstAcctNum2_Calculation(Index):
    ReturnVal = GetString(IAEstimates.EstAcctNum)

def EstChecking_Calculation():
    if GetBool(IAEstimates.DirectDebEst) == True and  ( GetCurrency(IAEstimates.Est1Amt) == 0 and GetCurrency(IAEstimates.Est2Amt) == 0 and GetCurrency(IAEstimates.Est3Amt) == 0 and GetCurrency(IAEstimates.Est4Amt) == 0 ) :
        ReturnVal = 0
    elif  ( GetBool(IAEstimates.DirectDebEst) == True and  ( GetCurrency(IAEstimates.Est1Amt) > 0 or GetCurrency(IAEstimates.Est2Amt) > 0 or GetCurrency(IAEstimates.Est3Amt) > 0 or GetCurrency(IAEstimates.Est4Amt) > 0 ) ) :
        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)
        while count <= MaxAcct:
            if GetString(USWBankAcct.BankAcct, count) != '':
                if IsStrEqual(GetString(IAEstimates.DDAcct), GetString(USWBankAcct.BankAcct, count)):
                    ReturnVal = GetBool(USWBankAcct.Checking, count)
                    count = 99
            count = count + 1
        ReturnVal = 0
    else:
        ReturnVal = 0

def EstChecking2_Calculation(Index):
    ReturnVal = GetBool(IAEstimates.EstChecking)

def EstDed_Calculation():
    # updated for 2018
    if GetBool(IAEstimates.Joint) == True:
        ReturnVal = Decimal("5120")
    else:
        ReturnVal = Decimal("2080")

def EstEFW_Calculation():
    if GetBool(IAEstimates.EstIAT) == True:
        ReturnVal = 0
    elif GetBool(IAEstimates.DirectDebEst) == True:
        if GetBool(IAEstimates.EstPay1) == True or GetBool(IAEstimates.EstPay2) == True or GetBool(IAEstimates.EstPay3) == True or GetBool(IAEstimates.EstPay4) == True:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def EstIAT_Calculation():
    if GetBool(IAEstimates.DirectDebEst) == True and  ( GetCurrency(IAEstimates.Est1Amt) == 0 and GetCurrency(IAEstimates.Est2Amt) == 0 and GetCurrency(IAEstimates.Est3Amt) == 0 and GetCurrency(IAEstimates.Est4Amt) == 0 ) :
        ReturnVal = 0
    elif  ( GetBool(IAEstimates.DirectDebEst) == True and  ( GetCurrency(IAEstimates.Est1Amt) > 0 or GetCurrency(IAEstimates.Est2Amt) > 0 or GetCurrency(IAEstimates.Est3Amt) > 0 or GetCurrency(IAEstimates.Est4Amt) > 0 ) ) :
        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)
        while count <= MaxAcct:
            if GetString(USWBankAcct.BankAcct, count) != '':
                if IsStrEqual(GetString(IAEstimates.DDAcct), GetString(USWBankAcct.BankAcct, count)):
                    ReturnVal = GetBool(USWBankAcct.IAT, count)
                    count = 99
            count = count + 1
        ReturnVal = 0
    else:
        ReturnVal = 0

def EstIATNo_Calculation():
    ReturnVal = GetBool(IAEstimates.EstEFW)

def EstPay1_Calculation():
    if GetBool(IAEstimates.Est1) == True and GetCurrency(IAEstimates.Est1Amt) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def EstPay2_Calculation():
    if GetBool(IAEstimates.Est2) == True and GetCurrency(IAEstimates.Est2Amt) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def EstPay3_Calculation():
    if GetBool(IAEstimates.Est3) == True and GetCurrency(IAEstimates.Est3Amt) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def EstPay4_Calculation():
    if GetBool(IAEstimates.Est4) == True and GetCurrency(IAEstimates.Est4Amt) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def EstRTN_Calculation():
    if GetBool(IAEstimates.DirectDebEst) == True and  ( GetCurrency(IAEstimates.Est1Amt) == 0 and GetCurrency(IAEstimates.Est2Amt) == 0 and GetCurrency(IAEstimates.Est3Amt) == 0 and GetCurrency(IAEstimates.Est4Amt) == 0 ) :
        ReturnVal = ''
    elif  ( GetBool(IAEstimates.DirectDebEst) == True and  ( GetCurrency(IAEstimates.Est1Amt) > 0 or GetCurrency(IAEstimates.Est2Amt) > 0 or GetCurrency(IAEstimates.Est3Amt) > 0 or GetCurrency(IAEstimates.Est4Amt) > 0 ) ) :
        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)
        while count <= MaxAcct:
            if GetString(USWBankAcct.BankAcct, count) != '':
                if IsStrEqual(GetString(IAEstimates.DDAcct), GetString(USWBankAcct.BankAcct, count)):
                    ReturnVal = GetString(USWBankAcct.RTN, count)
                    count = 99
            count = count + 1
        ReturnVal = ''
    else:
        ReturnVal = ''

def EstRTN2_Calculation(Index):
    ReturnVal = GetString(IAEstimates.EstRTN)

def EstSavings_Calculation():
    if GetBool(IAEstimates.DirectDebEst) == True and  ( GetCurrency(IAEstimates.Est1Amt) == 0 and GetCurrency(IAEstimates.Est2Amt) == 0 and GetCurrency(IAEstimates.Est3Amt) == 0 and GetCurrency(IAEstimates.Est4Amt) == 0 ) :
        ReturnVal = 0
    elif  ( GetBool(IAEstimates.DirectDebEst) == True and  ( GetCurrency(IAEstimates.Est1Amt) > 0 or GetCurrency(IAEstimates.Est2Amt) > 0 or GetCurrency(IAEstimates.Est3Amt) > 0 or GetCurrency(IAEstimates.Est4Amt) > 0 ) ) :
        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)
        while count <= MaxAcct:
            if GetString(USWBankAcct.BankAcct, count) != '':
                if IsStrEqual(GetString(IAEstimates.DDAcct), GetString(USWBankAcct.BankAcct, count)):
                    ReturnVal = GetBool(USWBankAcct.Savings, count)
                    count = 99
            count = count + 1
        ReturnVal = 0
    else:
        ReturnVal = 0

def EstSavings2_Calculation(Index):
    ReturnVal = GetBool(IAEstimates.EstSavings)

def Exist_Calculation():
    ReturnVal = 1

def GrossIncOption_Calculation():
    if GetBool(IAEstimates.Gross) == True:
        ReturnVal = CDollar(GetFloat(IAEstimates.Gross5) * 0.05)
    else:
        ReturnVal = 0

def IANetInc_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAEstimates.NetInc) - GetCurrency(IAEstimates.FedTaxPd))

def IATax_Calculation():
    if GetFloat(IAEstimates.NRIAPer) < 1:
        ReturnVal = CDollar(GetFloat(IAEstimates.NetTax) * GetFloat(IAEstimates.NRIAPer))
    else:
        ReturnVal = GetCurrency(IAEstimates.NetTax)

def JtCommon_Calculation():
    ReturnVal = GetString(USWBasicInfo.CombFirst)

def MainName_Calculation():
    if GetBool(IAEstimates.Taxpayer) == True:
        ReturnVal = GetString(IARequired.TPComb)
    elif GetBool(IAEstimates.Spouse) == True:
        ReturnVal = GetString(IARequired.SPComb)
    else:
        ReturnVal = GetString(IARequired.JTComb)

def Names_Calculation():
    if GetBool(IAEstimates.Spouse) == True:
        ReturnVal = GetString(IARequired.SPCombName)
    elif GetBool(IAEstimates.Taxpayer) == True:
        ReturnVal = GetString(IARequired.TPCombName)
    else:
        ReturnVal = GetString(IARequired.CombNames)

def NetTax_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAEstimates.TotEstLiab) - GetCurrency(IAEstimates.TotCr))

def NoBankSel3_Calculation():
    if GetBool(IAEstimates.DirectDebEst) == True:
        if Trim(GetString(IAEstimates.DDAcct)) == '':
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def NoBankSelInt3_Calculation():
    if GetBool(IAEstimates.DirectDebEst) == True and  ( GetCurrency(IAEstimates.Est1Amt) > 0 or GetCurrency(IAEstimates.Est2Amt) > 0 or GetCurrency(IAEstimates.Est3Amt) > 0 or GetCurrency(IAEstimates.Est4Amt) > 0 ) :
        if GetBool(USTopicList.HaveBankWSSend) == False:
            ReturnVal = 0
        elif Trim(GetString(IAEstimates.DDAcct)) == '':
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def NRIAPer_Calculation():
    if GetCurrency(IAEstimates.NetInc) == 0:
        ReturnVal = 0
    elif GetCurrency(IAEstimates.NRIAInc) == 0:
        ReturnVal = 1
    else:
        ReturnVal = MinValue(1, Round(( GetFloat(IAEstimates.NRIAInc) / GetFloat(IAEstimates.NetInc) )  * 10000) / 10000)

def Overpayment_Calculation():
    if GetCurrency(IAF1040.OVerPaid) > 0:
        if GetBool(IAEstimates.Spouse) == False:
            ReturnVal = MaxValue(0, GetCurrency(IAF1040.OVerPaid) - GetCurrency(IAF1040.Penalty))
        elif GetBool(IAEstimates.Spouse) == True and GetBool(IAEstimates.Taxpayer, 1) == False and GetBool(IAEstimates.Taxpayer, 2) == False:
            ReturnVal = MaxValue(0, GetCurrency(IAF1040.OVerPaid) - GetCurrency(IAF1040.Penalty))
        else:
            ReturnVal = MinValue(MaxValue(0, ( GetCurrency(IAF1040.OVerPaid) )  - GetCurrency(IAF1040.Penalty)), GetCurrency(IAEstimates.SpOvpd, FieldCopies(IAEstimates.Taxpayer)))
    else:
        ReturnVal = 0

def Owner_Calculation():
    if GetBool(IAEstimates.Taxpayer) == True and Trim(GetString(USWBasicInfo.FirstName)) == '':
        ReturnVal = 'the taxpayer'
    elif GetBool(IAEstimates.Taxpayer) == True:
        ReturnVal = GetString(USWBasicInfo.FirstName)
    elif GetBool(IAEstimates.Spouse) == True and Trim(GetString(USWBasicInfo.SpouseFirst)) == '':
        ReturnVal = 'the spouse'
    elif GetBool(IAEstimates.Spouse) == True:
        ReturnVal = GetString(USWBasicInfo.SpouseFirst)
    else:
        ReturnVal = 'the taxpayer and spouse'

def Payments_Calculation():
    ReturnVal = GetCurrency(IAEstimates.V1PayAmt1) + GetCurrency(IAEstimates.V2PayAmt1) + GetCurrency(IAEstimates.V3PayAmt1) + GetCurrency(IAEstimates.V4PayAmt1)

def Print_Calculation():
    if GetCurrency(IAEstimates.TaxDue) > 0:
        if GetCurrency(IAEstimates.V1PayAmt1) + GetCurrency(IAEstimates.V2PayAmt1) + GetCurrency(IAEstimates.V3PayAmt1) + GetCurrency(IAEstimates.V4PayAmt1):
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def PYTaxOption_Calculation():
    TotTax = Currency()

    SubTot = Currency()
    if GetBool(IAEstimates.Spouse) == True:
        TotTax = GetCurrency(IAF1040.BBal4)
    elif GetBool(IAEstimates.Taxpayer) == True:
        TotTax = GetCurrency(IAF1040.ABal4)
    else:
        TotTax = GetCurrency(IAF1040.ABal4) + GetCurrency(IAF1040.BBal4)
    if GetCurrency(IARequired.IAAGI) > Decimal("150000"):
        SubTot = CDollar(( TotTax )  * 1.1)
    else:
        SubTot = TotTax
    if GetBool(IAEstimates.PYTax) == True:
        ReturnVal = MaxValue(0, SubTot - GetCurrency(IAEstimates.PYCredits))
    else:
        ReturnVal = 0

def Quarter_Calculation():
    ReturnVal = CDollar(GetFloat(IAEstimates.TaxDue) * 0.25)

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
    L16 = GetCurrency(IAEstimates.Roundup10)
    R25 = GetCurrency(IAEstimates.Roundup25)
    R50 = GetCurrency(IAEstimates.Roundup50)
    R100 = GetCurrency(IAEstimates.Roundup100)
    Drop = CLng(L16 / Decimal("40"))
    Drop25 = CLng(R25 / Decimal("100"))
    Drop50 = CLng(R50 / Decimal("200"))
    Drop100 = CLng(R100 / Decimal("400"))
    Payment = ( CCur(Drop) * Decimal("40") )  + Decimal("40")
    Payment25 = ( CCur(Drop25) * Decimal("100") )  + Decimal("100")
    Payment50 = ( CCur(Drop50) * Decimal("200") )  + Decimal("200")
    Payment100 = ( CCur(Drop100) * Decimal("400") )  + Decimal("400")
    if GetBool(IAEstimates.Round10) == True:
        if ( L16 % Decimal("40") )  == 0:
            ReturnVal = Round(CDollar(CDbl(L16) * 0.25))
        else:
            ReturnVal = Round(CDollar(CDbl(Payment) * 0.25))
    elif GetBool(IAEstimates.Round25) == True:
        if ( R25 % Decimal("100") )  == 0:
            ReturnVal = Round(CDollar(CDbl(R25) * 0.25))
        else:
            ReturnVal = Round(CDollar(CDbl(Payment25) * 0.25))
    elif GetBool(IAEstimates.Round50) == True:
        if ( R50 % Decimal("200") )  == 0:
            ReturnVal = Round(CDollar(CDbl(R50) * 0.25))
        else:
            ReturnVal = Round(CDollar(CDbl(Payment50) * 0.25))
    elif GetBool(IAEstimates.Round100) == True:
        if ( R100 % Decimal("400") )  == 0:
            ReturnVal = Round(CDollar(CDbl(R100) * 0.25))
        else:
            ReturnVal = Round(CDollar(CDbl(Payment100) * 0.25))
    else:
        ReturnVal = Round(CDollar(GetFloat(IAEstimates.TaxDue) * 0.25))

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
    L16 = GetCurrency(IAEstimates.Roundup10) - GetCurrency(IAEstimates.V1Pay)
    R25 = GetCurrency(IAEstimates.Roundup25) - GetCurrency(IAEstimates.V1Pay)
    R50 = GetCurrency(IAEstimates.Roundup50) - GetCurrency(IAEstimates.V1Pay)
    R100 = GetCurrency(IAEstimates.Roundup100) - GetCurrency(IAEstimates.V1Pay)
    Drop = CLng(L16 / Decimal("30"))
    Drop25 = CLng(R25 / Decimal("75"))
    Drop50 = CLng(R50 / Decimal("150"))
    Drop100 = CLng(R100 / Decimal("300"))
    Payment = ( CCur(Drop) * Decimal("30") )  + Decimal("30")
    Payment25 = ( CCur(Drop25) * Decimal("75") )  + Decimal("75")
    Payment50 = ( CCur(Drop50) * Decimal("150") )  + Decimal("150")
    Payment100 = ( CCur(Drop100) * Decimal("300") )  + Decimal("300")
    if GetBool(IAEstimates.Round10) == True:
        if ( L16 % Decimal("30") )  == 0:
            ReturnVal = Round(CDollar(CDbl(L16) * 0.333333))
        else:
            ReturnVal = Round(CDollar(CDbl(Payment) * 0.333333))
    elif GetBool(IAEstimates.Round25) == True:
        if ( R25 % Decimal("75") )  == 0:
            ReturnVal = Round(CDollar(CDbl(R25) * 0.333333))
        else:
            ReturnVal = Round(CDollar(CDbl(Payment25) * 0.333333))
    elif GetBool(IAEstimates.Round50) == True:
        if ( R50 % Decimal("150") )  == 0:
            ReturnVal = Round(CDollar(CDbl(R50) * 0.333333))
        else:
            ReturnVal = Round(CDollar(CDbl(Payment50) * 0.333333))
    elif GetBool(IAEstimates.Round100) == True:
        if ( R100 % Decimal("300") )  == 0:
            ReturnVal = Round(CDollar(CDbl(R100) * 0.333333))
        else:
            ReturnVal = Round(CDollar(CDbl(Payment100) * 0.333333))
    else:
        ReturnVal = Round(CDollar(CDbl(GetCurrency(IAEstimates.TaxDue) - GetCurrency(IAEstimates.V1Pay)) * 0.333333))

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
    L16 = GetCurrency(IAEstimates.Roundup10) - GetCurrency(IAEstimates.V1Pay) - GetCurrency(IAEstimates.V2Pay)
    R25 = GetCurrency(IAEstimates.Roundup25) - GetCurrency(IAEstimates.V1Pay) - GetCurrency(IAEstimates.V2Pay)
    R50 = GetCurrency(IAEstimates.Roundup50) - GetCurrency(IAEstimates.V1Pay) - GetCurrency(IAEstimates.V2Pay)
    R100 = GetCurrency(IAEstimates.Roundup100) - GetCurrency(IAEstimates.V1Pay) - GetCurrency(IAEstimates.V2Pay)
    Drop = CLng(L16 / Decimal("20"))
    Drop25 = CLng(R25 / Decimal("50"))
    Drop50 = CLng(R50 / Decimal("100"))
    Drop100 = CLng(R100 / Decimal("200"))
    Payment = ( CCur(Drop) * Decimal("20") )  + Decimal("20")
    Payment25 = ( CCur(Drop25) * Decimal("50") )  + Decimal("50")
    Payment50 = ( CCur(Drop50) * Decimal("100") )  + Decimal("100")
    Payment100 = ( CCur(Drop100) * Decimal("200") )  + Decimal("200")
    if GetBool(IAEstimates.Round10) == True:
        if ( L16 % Decimal("20") )  == 0:
            ReturnVal = Round(CDollar(CDbl(L16) * 0.5))
        else:
            ReturnVal = Round(CDollar(CDbl(Payment) * 0.5))
    elif GetBool(IAEstimates.Round25) == True:
        if ( R25 % Decimal("50") )  == 0:
            ReturnVal = Round(CDollar(CDbl(R25) * 0.5))
        else:
            ReturnVal = Round(CDollar(CDbl(Payment25) * 0.5))
    elif GetBool(IAEstimates.Round50) == True:
        if ( R50 % Decimal("100") )  == 0:
            ReturnVal = Round(CDollar(CDbl(R50) * 0.5))
        else:
            ReturnVal = Round(CDollar(CDbl(Payment50) * 0.5))
    elif GetBool(IAEstimates.Round100) == True:
        if ( R100 % Decimal("200") )  == 0:
            ReturnVal = Round(CDollar(CDbl(R100) * 0.5))
        else:
            ReturnVal = Round(CDollar(CDbl(Payment100) * 0.5))
    else:
        ReturnVal = Round(CDollar(CDbl(GetCurrency(IAEstimates.TaxDue) - GetCurrency(IAEstimates.V1Pay) - GetCurrency(IAEstimates.V2Pay)) * 0.5))

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
    L16 = GetCurrency(IAEstimates.Roundup10) - GetCurrency(IAEstimates.V1Pay) - GetCurrency(IAEstimates.V2Pay) - GetCurrency(IAEstimates.V3Pay)
    R25 = GetCurrency(IAEstimates.Roundup25) - GetCurrency(IAEstimates.V1Pay) - GetCurrency(IAEstimates.V2Pay) - GetCurrency(IAEstimates.V3Pay)
    R50 = GetCurrency(IAEstimates.Roundup50) - GetCurrency(IAEstimates.V1Pay) - GetCurrency(IAEstimates.V2Pay) - GetCurrency(IAEstimates.V3Pay)
    R100 = GetCurrency(IAEstimates.Roundup100) - GetCurrency(IAEstimates.V1Pay) - GetCurrency(IAEstimates.V2Pay) - GetCurrency(IAEstimates.V3Pay)
    Drop = CLng(L16 / Decimal("10"))
    Drop25 = CLng(R25 / Decimal("25"))
    Drop50 = CLng(R50 / Decimal("50"))
    Drop100 = CLng(R100 / Decimal("100"))
    Payment = ( CCur(Drop) * Decimal("10") )  + Decimal("10")
    Payment25 = ( CCur(Drop25) * Decimal("10") )  + Decimal("10")
    Payment50 = ( CCur(Drop50) * Decimal("10") )  + Decimal("10")
    Payment100 = ( CCur(Drop100) * Decimal("100") )  + Decimal("100")
    if GetBool(IAEstimates.Round10) == True:
        if ( L16 % Decimal("10") )  == 0:
            ReturnVal = L16
        else:
            ReturnVal = Round(Payment)
    elif GetBool(IAEstimates.Round25) == True:
        if ( R25 % Decimal("25") )  == 0:
            ReturnVal = R25
        else:
            ReturnVal = Round(Payment25)
    elif GetBool(IAEstimates.Round50) == True:
        if ( R50 % Decimal("50") )  == 0:
            ReturnVal = R50
        else:
            ReturnVal = Round(Payment50)
    elif GetBool(IAEstimates.Round100) == True:
        if ( R100 % Decimal("100") )  == 0:
            ReturnVal = R100
        else:
            ReturnVal = Round(Payment100)
    else:
        ReturnVal = Round(GetCurrency(IAEstimates.TaxDue) - GetCurrency(IAEstimates.V1Pay) - GetCurrency(IAEstimates.V2Pay) - GetCurrency(IAEstimates.V3Pay))

def Roundup10_Calculation():
    Required = Currency()

    Drop = Integer()

    Payment = Currency()
    Required = GetCurrency(IAEstimates.TaxDue)
    Drop = CLng(Required / Decimal("40"))
    Payment = ( CCur(Drop) * Decimal("40") )  + Decimal("40")
    if GetBool(IAEstimates.Round10) == True:
        if ( Required % Decimal("40") )  == 0:
            ReturnVal = Required
        else:
            ReturnVal = Payment
    else:
        ReturnVal = GetCurrency(IAEstimates.TaxDue)

def Roundup100_Calculation():
    Required = Currency()

    Drop = Integer()

    Payment = Currency()
    Required = GetCurrency(IAEstimates.TaxDue)
    Drop = CLng(GetFloat(IAEstimates.TaxDue) / 40000)
    Payment = ( CCur(Drop) * Decimal("400") )  + Decimal("400")
    if GetBool(IAEstimates.Round100) == True:
        if ( Required % Decimal("400") )  == 0:
            ReturnVal = Required
        else:
            ReturnVal = Payment
    else:
        ReturnVal = GetCurrency(IAEstimates.TaxDue)

def Roundup25_Calculation():
    Required = Currency()

    Drop = Integer()

    Payment = Currency()
    Required = GetCurrency(IAEstimates.TaxDue)
    Drop = CLng(GetFloat(IAEstimates.TaxDue) / 10000)
    Payment = ( CCur(Drop) * Decimal("100") )  + Decimal("100")
    if GetBool(IAEstimates.Round25) == True:
        if ( Required % Decimal("100") )  == 0:
            ReturnVal = Required
        else:
            ReturnVal = Payment
    else:
        ReturnVal = GetCurrency(IAEstimates.TaxDue)

def Roundup50_Calculation():
    Required = Currency()

    Drop = Integer()

    Payment = Currency()
    Required = GetCurrency(IAEstimates.TaxDue)
    Drop = CLng(CDbl(Required) / 20000)
    Payment = ( CCur(Drop) * Decimal("200") )  + Decimal("200")
    if GetBool(IAEstimates.Round50) == True:
        if ( Required % Decimal("200") )  == 0:
            ReturnVal = Required
        else:
            ReturnVal = Payment
    else:
        ReturnVal = GetCurrency(IAEstimates.TaxDue)

def SpouseCommon_Calculation():
    ReturnVal = GetString(USWBasicInfo.SPCommon)

def SSN_Calculation():
    if GetBool(IAEstimates.Spouse) == True:
        ReturnVal = GetString(IAF1040.SpouseSSN)
    else:
        ReturnVal = GetString(IAF1040.SSN)

def Tax_Calculation():
    ReturnVal = NextYearTax(GetCurrency(IAEstimates.TaxInc))

def TaxDue_Calculation():
    if GetBool(IAEstimates.Gross) == True:
        ReturnVal = GetCurrency(IAEstimates.GrossIncOption)
    elif GetBool(IAEstimates.PYTax) == True:
        ReturnVal = GetCurrency(IAEstimates.PYTaxOption)
    elif GetCurrency(IAEstimates.TotEstTax) > Decimal("200") or GetBool(IAEstimates.StillPay) == True:
        ReturnVal = GetCurrency(IAEstimates.TotEstTax)
    else:
        ReturnVal = 0

def TaxInc_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAEstimates.IANetInc) - GetCurrency(IAEstimates.EstDed))

def Taxpayer_Calculation():
    ReturnVal = 1

def TotApplied_Calculation():
    ReturnVal = ( GetCurrency(IAEstimates.V1Apply) + GetCurrency(IAEstimates.V2Apply) + GetCurrency(IAEstimates.V3Apply) + GetCurrency(IAEstimates.V4Apply) )

def TotCr_Calculation():
    if GetBool(IAEstimates.Joint) == True:
        ReturnVal = Decimal("80")
    else:
        ReturnVal = Decimal("40")

def TotEstimate_Calculation():
    ReturnVal = GetCurrency(IAEstimates.V1Pay) + GetCurrency(IAEstimates.V2Pay) + GetCurrency(IAEstimates.V3Pay) + GetCurrency(IAEstimates.V4Pay)

def TotEstLiab_Calculation():
    ReturnVal = GetCurrency(IAEstimates.Tax) + GetCurrency(IAEstimates.MinTax) + GetCurrency(IAEstimates.LSD)

def TotEstTax_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAEstimates.AdjBal) - GetCurrency(IAEstimates.IACr))

def TotNetTax2_Calculation():
    if GetBool(IAEstimates.Taxpayer) == False:
        ReturnVal = GetCurrency(IAEstimates.Overpayment)
    else:
        ReturnVal = MaxValue(0, GetCurrency(IAEstimates.Overpayment) - GetCurrency(IAEstimates.SpOvpd))

def V1Apply_Calculation():
    Smaller = Currency()
    Smaller = MinValue(GetCurrency(IAEstimates.TotNetTax2), GetCurrency(IAEstimates.SpecAmt))
    if GetBool(IAEstimates.Refund) == True:
        ReturnVal = 0
    elif GetBool(IAEstimates.ApplySpecific) == True and GetCurrency(IAEstimates.TaxDue) == 0:
        ReturnVal = Smaller
    elif GetBool(IAEstimates.ApplySpecific) == True:
        ReturnVal = MinValue(Smaller, GetCurrency(IAEstimates.V1Pay))
    else:
        ReturnVal = MinValue(GetCurrency(IAEstimates.TotNetTax2), GetCurrency(IAEstimates.V1Pay))

def V1Pay_Calculation():
    ReturnVal = GetCurrency(IAEstimates.RndV1)

def V1PayAmt1_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAEstimates.V1Pay) - GetCurrency(IAEstimates.V1Apply))

def V2Apply_Calculation():
    Smaller = Currency()

    Limited = Currency()

    Limited2 = Currency()
    Smaller = MinValue(GetCurrency(IAEstimates.TotNetTax2), GetCurrency(IAEstimates.SpecAmt))
    Limited = MinValue(GetCurrency(IAEstimates.V2Pay), GetCurrency(IAEstimates.TotNetTax2) - GetCurrency(IAEstimates.V1Pay))
    Limited2 = MinValue(GetCurrency(IAEstimates.V2Pay), Smaller - GetCurrency(IAEstimates.V1Pay))
    if GetBool(IAEstimates.Refund) == True or GetBool(IAEstimates.FirstQt) == True:
        ReturnVal = 0
    elif GetBool(IAEstimates.ApplySpecific) == True:
        ReturnVal = MaxValue(0, Limited2)
    else:
        ReturnVal = MaxValue(0, Limited)

def V2Pay_Calculation():
    ReturnVal = GetCurrency(IAEstimates.RndV2)

def V2PayAmt1_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAEstimates.V2Pay) - GetCurrency(IAEstimates.V2Apply))

def V3Apply_Calculation():
    Smaller = Currency()

    Limited = Currency()

    Limited2 = Currency()
    Smaller = MinValue(GetCurrency(IAEstimates.TotNetTax2), GetCurrency(IAEstimates.SpecAmt))
    Limited = MinValue(GetCurrency(IAEstimates.V3Pay), GetCurrency(IAEstimates.TotNetTax2) - GetCurrency(IAEstimates.V1Pay) - GetCurrency(IAEstimates.V2Pay))
    Limited2 = MinValue(GetCurrency(IAEstimates.V3Pay), Smaller - GetCurrency(IAEstimates.V1Pay) - GetCurrency(IAEstimates.V2Pay))
    if GetBool(IAEstimates.Refund) == True or GetBool(IAEstimates.FirstQt) == True:
        ReturnVal = 0
    elif GetBool(IAEstimates.ApplySpecific) == True:
        ReturnVal = MaxValue(0, Limited2)
    else:
        ReturnVal = MaxValue(0, Limited)

def V3Pay_Calculation():
    ReturnVal = GetCurrency(IAEstimates.RndV3)

def V3PayAmt1_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAEstimates.V3Pay) - GetCurrency(IAEstimates.V3Apply))

def V4Apply_Calculation():
    Smaller = Currency()

    Limited = Currency()
    if GetBool(IAEstimates.Refund) == True or GetBool(IAEstimates.FirstQt) == True:
        ReturnVal = 0
    elif GetBool(IAEstimates.ApplyAll) == True:
        Limited = MaxValue(0, GetCurrency(IAEstimates.TotNetTax2) - GetCurrency(IAEstimates.V1Pay) - GetCurrency(IAEstimates.V2Pay) - GetCurrency(IAEstimates.V3Pay))
        ReturnVal = MinValue(GetCurrency(IAEstimates.V4Pay), Limited)
    elif GetBool(IAEstimates.ApplySpecific) == True:
        Smaller = MinValue(GetCurrency(IAEstimates.TotNetTax2), GetCurrency(IAEstimates.SpecAmt))
        ReturnVal = MaxValue(0, Smaller - GetCurrency(IAEstimates.V1Apply) - GetCurrency(IAEstimates.V2Apply) - GetCurrency(IAEstimates.V3Apply))
    else:
        ReturnVal = 0

def V4Pay_Calculation():
    ReturnVal = GetCurrency(IAEstimates.RndV4)

def V4PayAmt1_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAEstimates.V4Pay) - GetCurrency(IAEstimates.V4Apply))

