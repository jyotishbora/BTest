from forms.out import IA1040X
from forms.out import IA137
from forms.out import IAEFWKSHT
from forms.out import IAESTIMATES
from forms.out import IAF1040
from forms.out import IAREQUIRED
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Acct_Calculation():
    if get_bool(IAEFWKSHT.IsStateRPT) == True and get_bool(USWRALApp.StateRTDD) == True and get_bool(IAEFWKSHT.DirDeposit) == True:
        return get_string(USWRALApp.StateAccount)
    elif  ( get_bool(IAEFWKSHT.DirDeposit) == True and get_currency(IAEFWKSHT.Refund) > 0 )  or  ( get_bool(IAEFWKSHT.EFW) == True and get_currency(IAEFWKSHT.AmtOwed) > 0 ) :
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

def ACH_Calculation():
    if get_number(IAEFWKSHT.Yes) == 1:
        return 0
    elif get_bool(IAEFWKSHT.EFW) == True and get_currency(IAEFWKSHT.AmtOwed) > 0:
        return 1
    else:
        return 0

def Address_Calculation():
    return get_string(IAF1040.Add) + ' ' + get_string(IAF1040.CityComb)

def AIAWH_Calculation():
    return get_currency(IAF1040.AIATaxWith)

def AmtOwed_Calculation():
    return get_currency(IAF1040.TotDue)

def ANet_Calculation():
    return get_currency(IAF1040.ANet)

def AskBankInfo_Calculation():
    if get_currency(IAEFWKSHT.AmtOwed) > 0:
        return 1
    elif get_bool(IAEFWKSHT.IsStateRPT) == True and get_bool(USWEFQual.FilingSO) == True:
        return 0
    elif get_currency(IAEFWKSHT.Refund) > 0:
        return 1
    else:
        return 0

def AskDebitCard_Calculation():
    if IsPreparer() == True:
        return 0
    elif get_bool(USWBankProd.HaveBankConsent) == False:
        return 0
        # Do not offer state debit card on linked returns using Republic Direct Deposit RT
    elif get_bool(USWBankProd.DebitCardReturn) == False and get_bool(USWBankProd.RPTReturn) == True:
        return 0
        # Do not offer state debit card on state only returns using Republic Direct Deposit RT
    elif get_bool(USWBankProd.IsStateRPT) == True and get_bool(USWRALApp.StateRTDD) == True:
        return 0
    elif get_currency(IAEFWKSHT.Refund) < Decimal("10000"):
        return 1
    else:
        return 0

def AskDriverLic_Calculation():
    if get_bool(USWEFOptions.PiggyBackIA) == True or get_bool(USWEFOptions.SOIA) == True or get_bool(USWEFOptions.SOIAX) == True:
        return 1
    else:
        return 0

def AskFedStateBank_Calculation():
    if get_bool(IAEFWKSHT.PrepBPTrans) == True:
        return 1
    elif IsPreparer() == True and get_bool(USWBasicInfo.BankProd) == True:
        return 0
    elif get_bool(USWBankProd.IsStateRPT) == True and get_bool(USWEFQual.FilingSO) == True:
        return 0
    elif get_currency(IAEFWKSHT.Refund) > 0 and get_bool(USWEFWksht.refundbox) == True:
        if get_bool(USWBasicInfo.DebitCard) == True and get_bool(IAEFWKSHT.AskDebitCard) == False:
            return 0
        elif get_bool(IAEFWKSHT.DebitCard) == True and get_bool(IAEFWKSHT.AskDebitCard) == False:
            return 0
        elif get_bool(USWBasicInfo.DebitCard) == True and get_bool(IAEFWKSHT.DebitCard) == True:
            return 1
        elif get_bool(USWBasicInfo.DirectDepY) == True and get_bool(IAEFWKSHT.DirDeposit) == True:
            if get_string(USF8888.Account1) == get_string(IAEFWKSHT.Acct):
                return 1
            else:
                return 0
        elif get_bool(USWBasicInfo.DirectDepN) == True and get_bool(IAEFWKSHT.NoDDEFW) == True:
            return 1
        else:
            return 0
    else:
        return 0

def AskSORTDC_Calculation():
    if get_bool(USWEFOptions.SOIA) == False:
        return 0
    elif IsPreparer() == True:
        return 0
    elif get_bool(USWBankProd.HaveBankConsent) == False:
        return 0
    elif get_currency(IAEFWKSHT.Refund) < Decimal("10000"):
        return 1
    else:
        return 0

def AskStateRT_Calculation():
    if get_bool(USWEFOptions.SOIAX) == True:
        return 0
    elif get_currency(IAEFWKSHT.Refund) >= Decimal("75"):
        return 1
    else:
        return 0

def ATTax_Calculation():
    if get_bool(IAREQUIRED.LowInc) == True:
        return 0
    else:
        return get_currency(IAF1040.ATotIATax)

def BankName_Calculation():
    if ( get_bool(IAEFWKSHT.DirDeposit) == True and get_currency(IAEFWKSHT.Refund) > 0 )  or  ( get_bool(IAEFWKSHT.EFW) == True and get_currency(IAEFWKSHT.AmtOwed) > 0 ) :
        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)
        while count <= MaxAcct:
            if get_string(USWBankAcct.BankAcct, count) != '':
                if IsStrEqual(get_string(IAEFWKSHT.Acct), get_string(USWBankAcct.BankAcct, count)):
                    return get_string(USWBankAcct.BankName, count)
                    count = 99
            count = count + 1
        return ''
    else:
        return ''

def BankProDisCd_Calculation():
    Submission = String()

    TempStr = String()
    #Bank Product Disbursement Declaration
    #0 = Did Not Select bank product Option; 1 = Selected Debit Card Option; 2 = Selected Direct Depoist to the Bank; 3 = Requestd a Check;
    #Parameter 6 = Refund Owe Method: 0-No method; 1-AmEx debit card; 2-State issued debit card; 3-Direct deposit no Republic Bank; 4-Direct deposit through Republic Bank; 5-Paper check (refund); 6-AmEx debit card through Republic; 10-Direct debit; 11-Credit card; 12-Paper check (owe); 13-IRS EFTPS
    TempStr = get_string(IAEFWKSHT.EFSubmission)
    Submission = GetParam(TempStr, 1, '|')
    if GetParam(Submission, 6, ';') == '0':
        return '0'
    elif GetParam(Submission, 6, ';') == '1':
        return '1'
    elif GetParam(Submission, 6, ';') == '2':
        return '3'
    elif GetParam(Submission, 6, ';') == '3':
        return '2'
    elif GetParam(Submission, 6, ';') == '4':
        return '2'
    elif GetParam(Submission, 6, ';') == '5':
        return '3'
    elif GetParam(Submission, 6, ';') == '6':
        return '1'
    else:
        return '0'

def BIAWH_Calculation():
    return get_currency(IAF1040.BIATaxWith)

def BNet_Calculation():
    return get_currency(IAF1040.BNet)

def BP_Calculation():
    if get_bool(IAEFWKSHT.PrepBPTrans) == True:
        return 1
    else:
        return 0

def BTTax_Calculation():
    if get_bool(IAREQUIRED.LowInc) == True:
        return 0
    else:
        return get_currency(IAF1040.BTotIATax)

def CompStateEFQA_Calculation():
    # If not filing Iowa return, always return False
    if get_bool(USWEFOptions.PiggyBackIA) == False and get_bool(USWEFOptions.SOIA) == False and get_bool(USWEFOptions.SOIAX) == False:
        return 0
    elif get_currency(IAEFWKSHT.Refund) > 0:
        if get_bool(IAEFWKSHT.PrepRevQA) == False:
            return 1
        elif IsPreparer() == True and get_bool(IAEFWKSHT.PrepBPTrans) == True:
            return 0
        elif get_bool(USWBankProd.DebitCardReturn) == True and get_bool(IAEFWKSHT.DebitCard) == False and get_bool(IAEFWKSHT.DirDeposit) == False and get_bool(IAEFWKSHT.NoDDEFW) == False:
            return 1
        elif get_bool(IAEFWKSHT.DirDeposit) == False and get_bool(IAEFWKSHT.NoDDEFW) == False:
            return 1
        elif get_bool(USWBankProd.DebitCardReturn) == False and get_bool(IAEFWKSHT.DirDeposit) == False and get_bool(IAEFWKSHT.NoDDEFW) == False:
            return 1
        elif get_bool(IAEFWKSHT.DirDeposit) == True and get_number(USFInterview.ValidBankAccts) == 0:
            return 1
        else:
            return 0
    elif get_currency(IAEFWKSHT.AmtOwed) > 0:
        if get_bool(IAEFWKSHT.PrepRevQA) == False:
            return 1
        elif get_bool(IAEFWKSHT.EFW) == False and get_bool(IAEFWKSHT.NoDDEFW) == False:
            return 1
        elif get_bool(IAEFWKSHT.EFW) == True and get_number(USFInterview.ValidBankAccts) == 0:
            return 1
        else:
            return 0
    else:
        return 0

def DANChange_Calculation():
    return get_string(IAEFWKSHT.DirDepDan) + '|'

def DC_Calculation():
    if get_bool(IAEFWKSHT.PrepBPTrans) == True:
        return 0
    elif get_bool(IAEFWKSHT.DebitCard) == True and get_currency(IAEFWKSHT.Refund) > 0:
        return 1
    else:
        return 0

def DD_Calculation():
    if get_number(IAEFWKSHT.Yes) == 1:
        return 0
    elif get_bool(IAEFWKSHT.PrepBPTrans) == True:
        return 0
    elif get_bool(IAEFWKSHT.DirDeposit) == True and get_currency(IAEFWKSHT.Refund) > 0:
        return 1
    else:
        return 0

def DebitCard_Calculation():
    if get_bool(IAEFWKSHT.IsStateRPT) == True:
        if get_bool(USWRALApp.StateRTDC) == True and get_bool(IAEFWKSHT.AskDebitCard) == True:
            return 1
        else:
            return 0
    elif get_bool(USWBasicInfo.DebitCard) == True and get_currency(USF1040.RefundOwe) > 0 and get_bool(IAEFWKSHT.AskDebitCard) == True:
        if get_currency(IAEFWKSHT.Refund) > 0:
            return 1
        else:
            return 0
    else:
        return 0

def Desc_Calculation():
    return get_string(IAREQUIRED.CombNames)

def DirDepChecking_Calculation():
    if ( get_bool(IAEFWKSHT.DirDeposit) == True and get_currency(IAEFWKSHT.Refund) > 0 )  or  ( get_bool(IAEFWKSHT.EFW) == True and get_currency(IAEFWKSHT.AmtOwed) > 0 ) :
        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)
        while count <= MaxAcct:
            if get_string(USWBankAcct.BankAcct, count) != '':
                if IsStrEqual(get_string(IAEFWKSHT.Acct), get_string(USWBankAcct.BankAcct, count)):
                    return get_bool(USWBankAcct.Checking, count)
                    count = 99
            count = count + 1
        return 0
    else:
        return 0

def DirDepDan_Calculation():
    if ( get_bool(IAEFWKSHT.DirDeposit) == True and get_currency(IAEFWKSHT.Refund) > 0 )  or  ( get_bool(IAEFWKSHT.EFW) == True and get_currency(IAEFWKSHT.AmtOwed) > 0 ) :
        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)
        while count <= MaxAcct:
            if get_string(USWBankAcct.BankAcct, count) != '':
                if IsStrEqual(get_string(IAEFWKSHT.Acct), get_string(USWBankAcct.BankAcct, count)):
                    return get_string(USWBankAcct.AcctNum, count)
                    count = 99
            count = count + 1
        return ''
    else:
        return ''

def DirDeposit_Calculation():
    if get_bool(IAEFWKSHT.IsStateRPT) == True:
        if get_bool(USWRALApp.StateRTDD) == True:
            return 1
        else:
            return 0
    elif get_bool(USWBasicInfo.DirectDepY) == True and get_currency(USF1040.RefundOwe) > 0:
        if get_currency(IAEFWKSHT.Refund) > 0:
            return 1
        else:
            return 0
    else:
        return 0

def DirDepRTN_Calculation():
    if ( get_bool(IAEFWKSHT.DirDeposit) == True and get_currency(IAEFWKSHT.Refund) > 0 )  or  ( get_bool(IAEFWKSHT.EFW) == True and get_currency(IAEFWKSHT.AmtOwed) > 0 ) :
        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)
        while count <= MaxAcct:
            if get_string(USWBankAcct.BankAcct, count) != '':
                if IsStrEqual(get_string(IAEFWKSHT.Acct), get_string(USWBankAcct.BankAcct, count)):
                    return get_string(USWBankAcct.RTN, count)
                    count = 99
            count = count + 1
        return ''
    else:
        return ''

def DirDepSavings_Calculation():
    if ( get_bool(IAEFWKSHT.DirDeposit) == True and get_currency(IAEFWKSHT.Refund) > 0 )  or  ( get_bool(IAEFWKSHT.EFW) == True and get_currency(IAEFWKSHT.AmtOwed) > 0 ) :
        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)
        while count <= MaxAcct:
            if get_string(USWBankAcct.BankAcct, count) != '':
                if IsStrEqual(get_string(IAEFWKSHT.Acct), get_string(USWBankAcct.BankAcct, count)):
                    return get_bool(USWBankAcct.Savings, count)
                    count = 99
            count = count + 1
        return 0
    else:
        return 0

def DirDepTrigger_Calculation():
    if get_number(IAEFWKSHT.EFDDCode) == 1:
        return 1
    else:
        return 0

def DirectDepY_Calculation():
    if get_bool(IAEFWKSHT.DD) == True:
        if get_bool(USWBankProd.RPTReturn) == True and get_bool(IAEFWKSHT.SameFedBank) == True:
            return 1
        elif get_bool(IAEFWKSHT.IsStateRPT) == True:
            return 1
        else:
            return 0
    elif get_bool(IAEFWKSHT.DC) == True:
        if get_bool(USWBankProd.RPTReturn) == True:
            return 1
        elif get_bool(IAEFWKSHT.IsStateRPT) == True:
            return 1
        else:
            return 0
    else:
        return 0

def EFAvailable_Calculation():
    if get_bool(IA1040X.EFAmend) == True:
        return 'IAX,2, Amended|'
    else:
        return 'IA,0,|'

def EFChecking_Calculation():
    if get_bool(IAEFWKSHT.PrepBPTrans) == True:
        return get_bool(USWEFWkSht2.DirDepChk)
    elif get_bool(IAEFWKSHT.DebitCard) == True and get_currency(IAEFWKSHT.Refund) > 0:
        return 1
    elif get_number(IAEFWKSHT.EFDDCode) != 0:
        return get_bool(IAEFWKSHT.DirDepChecking)
    else:
        return 0

def EFDan_Calculation():
    if get_bool(IAEFWKSHT.PrepBPTrans) == True:
        return get_string(USWEFWkSht2.DirDepDan)
    elif get_bool(IAEFWKSHT.DebitCard) == True and get_currency(IAEFWKSHT.Refund) > 0:
        return get_string(USWDebitCard.AcctNum)
    elif get_number(IAEFWKSHT.EFDDCode) != 0:
        return get_string(IAEFWKSHT.DirDepDan)
    else:
        return ''

def EFDDCode_Calculation():
    if get_bool(IAEFWKSHT.PrepBPTrans) == True:
        return 1
    elif get_bool(IAEFWKSHT.DebitCard) == True and get_currency(IAEFWKSHT.Refund) > 0:
        return 1
    elif get_number(IAEFWKSHT.Yes) == 1:
        return 0
    elif get_bool(IAEFWKSHT.DirDeposit) == True and get_currency(IAEFWKSHT.Refund) > 0:
        return 1
    elif get_bool(IAEFWKSHT.EFW) == True and get_currency(IAEFWKSHT.AmtOwed) > 0:
        return 2
    else:
        return 0

def EFDedCode_Calculation():
    if get_bool(IAREQUIRED.LowInc) == True:
        return ''
    elif get_bool(IAF1040.ItemCheck) == True:
        return '1'
    else:
        return '3'

def EFEFWAmt_Calculation():
    if get_number(IAEFWKSHT.EFDDCode) == 2:
        return get_currency(IAEFWKSHT.AmtOwed)
    else:
        return 0

def EFEFWDate_Calculation():
    if get_number(IAEFWKSHT.EFDDCode) == 2:
        return get_string(IAEFWKSHT.EFWDate)
    else:
        return ''

def EFRtn_Calculation():
    if get_bool(IAEFWKSHT.PrepBPTrans) == True:
        return get_string(USWEFWkSht2.DirDepRTN)
    elif get_bool(IAEFWKSHT.DebitCard) == True and get_currency(IAEFWKSHT.Refund) > 0:
        return get_string(USWDebitCard.RTN)
    elif get_number(IAEFWKSHT.EFDDCode) != 0:
        return get_string(IAEFWKSHT.DirDepRTN)
    else:
        return ''

def EFSavings_Calculation():
    if get_bool(IAEFWKSHT.PrepBPTrans) == True:
        return get_bool(USWEFWkSht2.DirDepSav)
    elif get_bool(IAEFWKSHT.DebitCard) == True and get_currency(IAEFWKSHT.Refund) > 0:
        return 0
    elif get_number(IAEFWKSHT.EFDDCode) != 0:
        return get_bool(IAEFWKSHT.DirDepSavings)
    else:
        return 0

def EFSpInit_Calculation():
    if get_bool(IAF1040.MFJ) == True or get_bool(IAF1040.CombMFS) == True:
        return get_string(USWBasicInfo.SpInit)
    else:
        return ''

def EFSpLast_Calculation():
    if get_bool(IAF1040.MFJ) == True or get_bool(IAF1040.CombMFS) == True:
        return get_string(USWBasicInfo.SPLast)
    else:
        return ''

def EFSpouseFirst_Calculation():
    if get_bool(IAF1040.MFJ) == True or get_bool(IAF1040.CombMFS) == True:
        return get_string(USWBasicInfo.SpouseFirst)
    else:
        return ''

def EFSpSuffix_Calculation():
    if get_bool(IAF1040.MFJ) == True or get_bool(IAF1040.CombMFS) == True:
        return get_string(USWBasicInfo.SPSuffix)
    else:
        return ''

def EFStRefund_Calculation():
    if get_bool(USWEFOptions.PiggyBackIA) == True:
        if get_currency(IAEFWKSHT.Refund) > 0:
            return 1
        else:
            return 0
    else:
        return 0

def EFSubmission_Calculation():
    RefOweMethod = String()
    # General Guideline to follow (use | bar if more than 1 return can be filed)
    # Parameter 1 = Module Name
    # Parameter 2 = Return Type: 0-Return; 1-Extension; 2-Amended; 3-Special1; 4-SpecialTaxpayer; 5-SpecialTaxpayerExtension; 6-SpecialSpouse; 7-SpecialSpouseExtension; 8-NewYorkLLC; 9-Special
    # Parameter 3 = EF Type: 0-Legacy; 1-Qualifies for MeF (used if state supports legacy); 2-Must Be MeF (always used if state does not support legacy)
    # Parameter 4 = Fed XML Version: 0-Send no federal XML; 1-Send accepted federal; 2-Send federal XML used to complete state return
    # Parameter 5 = Special Description: description for special returns, if none space
    # Parameter 6 = Refund Owe Method: 0-No method; 1-AmEx debit card; 2-State issued debit card; 3-Direct deposit no Republic Bank; 4-Direct deposit through Republic Bank; 5-Paper check (refund); 6-AmEx debit card through Republic; 10-Direct debit; 11-Credit card; 12-Paper check (owe); 13-IRS EFTPS
    if get_bool(USWEFOptions.PiggyBackIA) == True or get_bool(USWEFOptions.SOIA) == True:
        if get_currency(IAF1040.RefBalDue) == 0:
            RefOweMethod = '0'
        elif get_bool(IAEFWKSHT.PrepBPTrans) == True:
            RefOweMethod = '4'
        elif get_bool(IAEFWKSHT.DC) == True:
            if get_bool(USWBankProd.RPTReturn) == True:
                RefOweMethod = '6'
            elif get_bool(IAEFWKSHT.IsStateRPT) == True:
                RefOweMethod = '6'
            else:
                RefOweMethod = '1'
        elif get_bool(IAEFWKSHT.DD) == True:
            if get_bool(USWBankProd.RPTReturn) == True and get_bool(IAEFWKSHT.SameFedBank) == True:
                RefOweMethod = '4'
            elif get_bool(IAEFWKSHT.IsStateRPT) == True:
                RefOweMethod = '4'
            else:
                RefOweMethod = '3'
        elif get_currency(IAF1040.RefBalDue) > 0:
            RefOweMethod = '5'
        elif get_string(IAEFWKSHT.EFDDCode) == '2':
            RefOweMethod = '10'
        else:
            RefOweMethod = '12'
    elif get_bool(USWEFOptions.SOIAX) == True:
        if get_currency(IAF1040.RefBalDue) == 0:
            RefOweMethod = '0'
        elif get_bool(IAEFWKSHT.DD) == True:
            RefOweMethod = '3'
        elif get_currency(IAF1040.RefBalDue) > 0:
            RefOweMethod = '5'
        elif get_string(IAEFWKSHT.EFDDCode) == '2':
            RefOweMethod = '10'
        else:
            RefOweMethod = '12'
    else:
        RefOweMethod = '0'
    if get_bool(USWEFOptions.PiggyBackIA) == True or get_bool(USWEFOptions.SOIA) == True:
        return 'IA;0;2;2; ;' + RefOweMethod + '|'
    elif get_bool(USWEFOptions.SOIAX) == True:
        return 'IA;2;2;2;Amended;' + RefOweMethod + '|'
    else:
        return ''

def EROAddress_Calculation():
    if IsPreparer() == True:
        return get_string(USWBasicInfo.EROAddress)
    else:
        return ''

def EROCityComb_Calculation():
    if IsPreparer() == False:
        return ''
    elif trim(get_string(USWBasicInfo.EROForCtry)) != '':
        if trim(get_string(USWBasicInfo.EROForProvince)) != '' and trim(get_string(USWBasicInfo.EROForPC)) != '':
            return get_string(USWBasicInfo.EROCity) + ', ' + get_string(USWBasicInfo.EROForProvince) + ', ' + get_string(USWBasicInfo.EROForPC) + ', ' + get_string(USWBasicInfo.EROForCtry)
        elif trim(get_string(USWBasicInfo.EROForProvince)) != '':
            return get_string(USWBasicInfo.EROCity) + ', ' + get_string(USWBasicInfo.EROForProvince) + ', ' + get_string(USWBasicInfo.EROForCtry)
        elif trim(get_string(USWBasicInfo.EROForPC)) != '':
            return get_string(USWBasicInfo.EROCity) + ', ' + get_string(USWBasicInfo.EROForPC) + ', ' + get_string(USWBasicInfo.EROForCtry)
        else:
            return get_string(USWBasicInfo.EROCity) + ', ' + get_string(USWBasicInfo.EROForCtry)
    elif trim(get_string(USWBasicInfo.EROCity)) != '':
        return get_string(USWBasicInfo.EROCity) + ', ' + get_string(USWBasicInfo.StateAbbERO) + ' ' + get_string(USWBasicInfo.EROZip)
    else:
        return get_string(USWBasicInfo.StateAbbERO) + ' ' + get_string(USWBasicInfo.EROZip)

def EROEIN_Calculation():
    if IsPreparer() == True:
        return get_string(USWBasicInfo.EROEIN)
    else:
        return ''

def EROFirmName_Calculation():
    if IsPreparer() == True:
        return get_string(USWBasicInfo.EROFirmName)
    else:
        return ''

def EROPhone_Calculation():
    if IsPreparer() == False:
        return ''
    elif trim(get_string(USWBasicInfo.EROPhone)) != '':
        return get_string(USWBasicInfo.EROPhone)
    else:
        return get_string(USWBasicInfo.EROForPhone)

def EROPrep_Calculation():
    if IsPreparer() == True:
        return get_bool(USWBasicInfo.PaidPrepY)
    else:
        return 0

def EROSE_Calculation():
    if IsPreparer() == True:
        return get_bool(USWBasicInfo.EROSelfEmp)
    else:
        return 0

def EROSSN_Calculation():
    EROPTIN = String()
    EROPTIN = LetterStr(get_string(USWBasicInfo.EROSSN))
    if IsPreparer() == True and IsStrEqual(EROPTIN, 'P'):
        return get_string(USWBasicInfo.EROSSN)
    else:
        return ''

def Exist_Calculation():
    return 1

def FedChecking_Calculation():
    if get_currency(USWBasicInfo.WithdrawalAmt) > 0 and GetDate(USWBasicInfo.withdrawldate) != '':
        return get_bool(USWBasicInfo.ACHChecking)
    else:
        return get_bool(USF8888.EFChecking(0))

def FedDAN_Calculation():
    if get_currency(USWBasicInfo.WithdrawalAmt) > 0 and GetDate(USWBasicInfo.withdrawldate) != '':
        return get_string(USWBasicInfo.ACHDAN)
    else:
        return get_string(USF8888.EFAcctNum(0))

def FedRTN_Calculation():
    if get_currency(USWBasicInfo.WithdrawalAmt) > 0 and GetDate(USWBasicInfo.withdrawldate) != '':
        return get_string(USWBasicInfo.ACHRTN)
    else:
        return get_string(USF8888.EFRtn(0))

def FedSavings_Calculation():
    if get_currency(USWBasicInfo.WithdrawalAmt) > 0 and GetDate(USWBasicInfo.withdrawldate) != '':
        return get_bool(USWBasicInfo.ACHSavings)
    else:
        return get_bool(USF8888.EFSaveAcct(0))

def FedTrans_Calculation():
    #If (get_bool(IAEFWKSHT.DirDeposit) = True And get_currency(IAEFWKSHT.Refund) > 0) Or (get_bool(IAEFWKSHT.EFW) = True And get_currency(IAEFWKSHT.AmtOwed) > 0) Then
    #    If get_bool(IAEFWKSHT.TransInfo) = True Then
    #        return 1
    #    Else
    #        return 0
    #    End If
    #Else
    return 0
    #End If

def FinTransTrigger_Calculation():
    if get_number(IAEFWKSHT.EFDDCode) != 0:
        return 1
    elif get_number(IAESTIMATES.EstEFW, 1) > 0 or get_number(IAESTIMATES.EstEFW, 2) > 0:
        return 1
    else:
        return 0

def ForCity_Calculation():
    return get_string(USWBasicInfo.ForCity)

def ForCountry_Calculation():
    return get_string(USWBasicInfo.ForCountry)

def ForStreet_Calculation():
    return get_string(USWBasicInfo.ForStreet)

def IsStateRPT_Calculation():
    if get_bool(IAEFWKSHT.AskStateRT) == False:
        return 0
    elif get_bool(USWBankProd.ClearedInvoiceFees) == True:
        return 0
    elif get_bool(USWRALApp.StateRTDC) == True and get_bool(IAEFWKSHT.AskSORTDC) == False:
        return 0
    elif get_bool(USWBankProd.StateRPT) == True and get_bool(USWBankProd.StateBankAgree) == True and get_bool(USWBankProd.StateBankAgree2) == True and get_currency(IAEFWKSHT.Refund) > 0:
        return 1
    else:
        return 0

def MeFPrepInfo_Calculation():
    if IsPreparer() == True:
        if get_bool(USWBasicInfo.NoPrep) == False:
            return 1
        else:
            return 0
    else:
        return 0

def MeFSP137_Calculation():
    if get_number(IA137.MEF137SP, FieldCopies(IA137.Spouse)) > 0:
        return 1
    else:
        return 0

def MeFTP137_Calculation():
    if get_number(IA137.MEF137TP, FieldCopies(IA137.Taxpayer)) > 0:
        return 1
    else:
        return 0

def Need8453_Calculation():
    return 1

def No_Calculation():
    if ( get_bool(IAEFWKSHT.DirDeposit) == True and get_currency(IAEFWKSHT.Refund) > 0 )  or  ( get_bool(IAEFWKSHT.EFW) == True and get_currency(IAEFWKSHT.AmtOwed) > 0 ) :
        if get_bool(IAEFWKSHT.Yes) == True:
            return 0
        else:
            return 1
    else:
        return 0

def NoBankSel_Calculation():
    if get_bool(IAEFWKSHT.DirDeposit) == True or get_bool(IAEFWKSHT.EFW):
        if trim(get_string(IAEFWKSHT.Acct)) == '':
            return 1
        else:
            return 0
    else:
        return 0

def NoBankSelInt_Calculation():
    if ( get_bool(IAEFWKSHT.DirDeposit) == True )  or  ( get_bool(IAEFWKSHT.EFW) == True ) :
        if get_bool(USTopicList.HaveBankWSSend) == False:
            return 0
        elif trim(get_string(IAEFWKSHT.Acct)) == '':
            return 1
        else:
            return 0
    else:
        return 0

def NoDDEFW_Calculation():
    if get_bool(IAEFWKSHT.IsStateRPT) == True:
        return 0
    elif get_bool(USWBasicInfo.DirectDepN) == True and get_currency(USF1040.RefundOwe) > 0:
        if get_currency(IAEFWKSHT.Refund) > 0:
            return 1
        else:
            return 0
    else:
        return 0

def NonForCity_Calculation():
    return get_string(USWBasicInfo.NonForCity)

def NonForState_Calculation():
    return get_string(USWBasicInfo.NonForState)

def NonForStreet_Calculation():
    return get_string(USWBasicInfo.NonForStreet)

def NonForZip_Calculation():
    return get_string(USWBasicInfo.NonForZip)

def PC_Calculation():
    if get_currency(IAEFWKSHT.Refund) == 0:
        return 0
    elif get_bool(IAEFWKSHT.DD) == False and get_bool(IAEFWKSHT.BP) == False and get_bool(IAEFWKSHT.DC) == False:
        return 1
    else:
        return 0

def PrBankName_Calculation():
    if get_number(IAEFWKSHT.EFDDCode) != 0 and get_bool(IAEFWKSHT.DebitCard) == False and get_bool(IAEFWKSHT.PrepBPTrans) == False:
        return get_string(IAEFWKSHT.BankName)
    else:
        return ''

def PrChecking_Calculation():
    if get_number(IAEFWKSHT.EFDDCode) != 0 and get_bool(IAEFWKSHT.DebitCard) == False and get_bool(IAEFWKSHT.PrepBPTrans) == False:
        return get_bool(IAEFWKSHT.DirDepChecking)
    else:
        return 0

def PrDAN_Calculation():
    if get_number(IAEFWKSHT.EFDDCode) != 0 and get_bool(IAEFWKSHT.DebitCard) == False and get_bool(IAEFWKSHT.PrepBPTrans) == False:
        return get_string(IAEFWKSHT.DirDepDan)
    else:
        return ''

def PrepAddress_Calculation():
    if IsPreparer() == True:
        if get_bool(IAEFWKSHT.EROPrep) == False:
            return get_string(USWBasicInfo.PrepAdd)
        else:
            return ''
    else:
        return ''

def PrepBPTrans_Calculation():
    if get_bool(USWRALApp.RepRouteState) == False:
        return 0
    elif IsPreparer() == False:
        return 0
    elif get_bool(USWBasicInfo.BankProd) == True and get_currency(USF1040.RefundOwe) > 0:
        if get_bool(USWBankProd.Republic) == True and get_bool(IAEFWKSHT.EFStRefund) == True:
            return 1
        else:
            return 0
    else:
        return 0

def PrepCityComb_Calculation():
    if IsPreparer() == True:
        if get_bool(IAEFWKSHT.EROPrep) == False:
            return get_string(USWBasicInfo.CombPrepCityStZipFor)
        else:
            return ''
    else:
        return ''

def PrepEIN_Calculation():
    if IsPreparer() == True:
        if get_bool(IAEFWKSHT.EROPrep) == False:
            return get_string(USWBasicInfo.PrepEIN)
        else:
            return ''
    else:
        return ''

def PrepFirmName_Calculation():
    if IsPreparer() == True:
        if get_bool(IAEFWKSHT.EROPrep) == False:
            return get_string(USWBasicInfo.PrepName)
        else:
            return ''
    else:
        return ''

def PrepPhone_Calculation():
    if IsPreparer() == True:
        if get_bool(IAEFWKSHT.EROPrep) == False:
            return get_string(IAF1040.PrepPhone)
        else:
            return ''
    else:
        return ''

def PrepSE_Calculation():
    if IsPreparer() == True:
        if get_bool(IAEFWKSHT.EROPrep) == False:
            return get_bool(USWBasicInfo.SelfEm)
        else:
            return 0
    else:
        return 0

def PrepSSN_Calculation():
    if IsPreparer() == True:
        if get_bool(IAEFWKSHT.EROPrep) == False:
            return get_string(USWBasicInfo.PrepSSN)
        else:
            return ''
    else:
        return ''

def PrERODate_Calculation():
    if get_bool(IAEFWKSHT.EROPrep) == True:
        return get_string(USWBasicInfo.PrPrepDate)
    else:
        return ''

def PrEROSig_Calculation():
    if get_bool(IAEFWKSHT.EROPrep) == True:
        return get_string(USWBasicInfo.PrPrepSig)
    else:
        return ''

def PrintReturn_Calculation():
    PrintList_Clear(PrintList_EF)
    if trim(get_string(IAEFWKSHT.EFSubmission)) != '':
        if get_bool(IA1040X.EFAmend) == True:
            PrintList_AddHTML(PrintList_EF, EFReturnType_AmendedReturn, 'E-filing Instructions', 'ia instructions/IAWEFFilingInst.htm')
            if get_bool(IAEFWKSHT.Need8453) == True:
                PrintList_AddCustom(PrintList_EF, EFReturnType_AmendedReturn, 'Form 8453', 'PrintEFileForms')
            PrintList_AddReturn(PrintList_EF, EFReturnType_AmendedReturn, 'Amended Return')
        else:
            PrintList_AddHTML(PrintList_EF, EFReturnType_Return, 'E-filing Instructions', 'ia instructions/IAWEFFilingInst.htm')
            if get_bool(IAEFWKSHT.Need8453) == True:
                PrintList_AddCustom(PrintList_EF, EFReturnType_Return, 'Form 8453', 'PrintEFileForms')
            PrintList_AddReturn(PrintList_EF, EFReturnType_Return, 'Return')
    return ''

def PrPrepDate_Calculation():
    if IsPreparer() == True:
        if get_bool(IAEFWKSHT.EROPrep) == False:
            return get_string(USWBasicInfo.PrPrepDate)
        else:
            return ''
    else:
        return ''

def PrPrepSig_Calculation():
    if IsPreparer() == True:
        if get_bool(IAEFWKSHT.EROPrep) == False:
            return get_string(USWBasicInfo.PrPrepSig)
        else:
            return ''
    else:
        return ''

def PrRtn_Calculation():
    if get_number(IAEFWKSHT.EFDDCode) != 0 and get_bool(IAEFWKSHT.DebitCard) == False and get_bool(IAEFWKSHT.PrepBPTrans) == False:
        return get_string(IAEFWKSHT.DirDepRTN)
    else:
        return ''

def PrSavings_Calculation():
    if get_number(IAEFWKSHT.EFDDCode) != 0 and get_bool(IAEFWKSHT.DebitCard) == False and get_bool(IAEFWKSHT.PrepBPTrans) == False:
        return get_bool(IAEFWKSHT.DirDepSavings)
    else:
        return 0

def QnAFedBank_Calculation():
    #If get_bool(IAEFWKSHT.AskFedStateBank) = True Then
    #    return 0
    #ElseIf (get_bool(IAEFWKSHT.DirDeposit) = True And get_currency(IAEFWKSHT.Refund) > 0) Or (get_bool(IAEFWKSHT.EFW) = True And get_currency(IAEFWKSHT.AmtOwed) > 0) Then
    #    If get_bool(IAEFWKSHT.TransInfo) = True Then
    #        return 1
    #    ElseIf trim(get_string(IAEFWKSHT.FedRTN)) <> "" And trim(get_string(IAEFWKSHT.FedDAN)) <> "" Then
    #        return 1
    #    Else
    #        return 0
    #    End If
    #Else
    return 0
    #End If

def RefProdCIPInd_Calculation():
    Submission = String()

    TempStr = String()
    TempStr = get_string(IAEFWKSHT.EFSubmission)
    Submission = GetParam(TempStr, 1, '|')
    if GetParam(Submission, 6, ';') == '0':
        return '0'
    elif GetParam(Submission, 6, ';') == '1':
        if trim(get_string(USWDebitCard.IDNumber)) != '':
            return '1'
        else:
            return '2'
    elif GetParam(Submission, 6, ';') == '3':
        return '0'
    elif GetParam(Submission, 6, ';') == '4':
        return '1'
    elif GetParam(Submission, 6, ';') == '5':
        return '0'
    elif GetParam(Submission, 6, ';') == '6':
        return '1'
    else:
        return '0'

def RefProdInd_Calculation():
    Submission = String()

    TempStr = String()
    TempStr = get_string(IAEFWKSHT.EFSubmission)
    Submission = GetParam(TempStr, 1, '|')
    if GetParam(Submission, 6, ';') == '0':
        return '0'
    elif GetParam(Submission, 6, ';') == '1':
        return '2'
    elif GetParam(Submission, 6, ';') == '2':
        return '0'
    elif GetParam(Submission, 6, ';') == '3':
        return '0'
    elif GetParam(Submission, 6, ';') == '4':
        return '2'
    elif GetParam(Submission, 6, ';') == '5':
        return '0'
    elif GetParam(Submission, 6, ';') == '6':
        return '2'
    else:
        return '0'

def Refund_Calculation():
    return get_currency(IAF1040.Refund)

def RefundDelay_Calculation():
    #this was set to 1 in 2017 will need to verify again for 2018 before shipping
    return 0

def RTNChange_Calculation():
    return get_string(IAEFWKSHT.DirDepRTN) + '|'

def SameFedBank_Calculation():
    SameRTN = Integer()

    SameDAN = Integer()

    SameType = Integer()
    if get_string(IAEFWKSHT.FedRTN) == get_string(IAEFWKSHT.DirDepRTN):
        SameRTN = 1
    else:
        SameRTN = 0
    if get_string(IAEFWKSHT.FedDAN) == get_string(IAEFWKSHT.DirDepDan):
        SameDAN = 1
    else:
        SameDAN = 0
    if get_bool(IAEFWKSHT.FedChecking) == True and get_bool(IAEFWKSHT.DirDepChecking) == True:
        SameType = 1
    elif get_bool(IAEFWKSHT.FedSavings) == True and get_bool(IAEFWKSHT.DirDepSavings) == True:
        SameType = 1
    else:
        SameType = 0
    if get_bool(USWBasicInfo.DirectDepY) == True and get_currency(USF1040.RefundOwe) > 0:
        if SameRTN + SameDAN + SameType == 3:
            return 1
        else:
            return 0
    else:
        return 0

def SPCombName_Calculation():
    return get_string(IAREQUIRED.SPCombName)

def SpSSN_Calculation():
    return get_string(IAF1040.SpouseSSN)

def SSN_Calculation():
    return get_string(IAF1040.SSN)

def StateDCReturn_Calculation():
    if get_bool(USWEFOptions.PiggyBackIA) == True or get_bool(USWEFOptions.SOIA) == True or get_bool(USWEFOptions.SOIAX) == True:
        if get_bool(IAEFWKSHT.DebitCard) == True and get_currency(IAEFWKSHT.Refund) > 0 and get_bool(IAEFWKSHT.AskDebitCard) == True:
            return 1
        else:
            return 0
    else:
        return 0

def TPCombName_Calculation():
    return get_string(IAREQUIRED.TPCombName)

def UBATrig_Calculation():
    if get_string(IAEFWKSHT.BankProDisCd) == '1':
        return 1
    elif get_string(IAEFWKSHT.BankProDisCd) == '2':
        return 1
    else:
        return 0

def UltDAN_Calculation():
    if get_bool(IAEFWKSHT.PrepBPTrans) == True:
        return get_string(USWRALApp.PrepBPDAN)
    else:
        return get_string(IAEFWKSHT.EFDan)

def UltRTN_Calculation():
    if get_bool(IAEFWKSHT.PrepBPTrans) == True:
        return get_string(USWRALApp.PrepBPRTN)
    else:
        return get_string(IAEFWKSHT.EFRtn)

def ViewBankInfo_Calculation():
    RefOweText = String()

    DispMethText = String()

    Routing = String()

    AcctNum = String()

    BankType = String()

    EffDate = String()
    RefOweText = ''
    DispMethText = ''
    Routing = ''
    AcctNum = ''
    BankType = ''
    EffDate = ''
    if get_currency(IAEFWKSHT.Refund) > 0:
        if get_bool(IA1040X.EFAmend) == True:
            RefOweText = 'Iowa Amended Refund'
        else:
            RefOweText = 'Iowa Refund'
        if get_bool(IAEFWKSHT.BP) == True:
            DispMethText = 'Republic Bank Product'
        elif get_bool(IAEFWKSHT.DD) == True:
            DispMethText = 'Direct Deposit'
            Routing = 'RTN: ' + get_string(IAEFWKSHT.EFRtn)
            AcctNum = 'Acct #: ' + get_string(IAEFWKSHT.EFDan)
            if get_bool(IAEFWKSHT.EFChecking) == True:
                BankType = 'Type: Checking'
            else:
                BankType = 'Type: Savings'
        elif get_bool(IAEFWKSHT.DC) == True:
            DispMethText = 'American Express Serve Card'
        else:
            DispMethText = 'Paper Check'
        return RefOweText + '/Refund Method: ' + DispMethText + '/' + Routing + '/' + AcctNum + '/' + BankType
    elif get_currency(IAEFWKSHT.AmtOwed) > 0:
        if get_bool(IA1040X.EFAmend) == True:
            RefOweText = 'Iowa Amended Balance Due'
        else:
            RefOweText = 'Iowa Balance Due'
        if get_bool(IAEFWKSHT.ACH) == True:
            DispMethText = 'Direct Withdrawal'
            Routing = 'RTN: ' + get_string(IAEFWKSHT.EFRtn)
            AcctNum = 'Acct #: ' + get_string(IAEFWKSHT.EFDan)
            if get_bool(IAEFWKSHT.EFChecking) == True:
                BankType = 'Type: Checking'
            else:
                BankType = 'Type: Savings'
            EffDate = 'Withdrawal Date: ' + GetVerboseDate(GetDate(IAEFWKSHT.EFEFWDate))
        else:
            DispMethText = 'Paper Check'
        return RefOweText + '/Payment Method: ' + DispMethText + '/' + Routing + '/' + AcctNum + '/' + BankType + '/' + EffDate
    else:
        if get_bool(IA1040X.EFAmend) == True:
            return 'Iowa:  No Refund or Balance Due on Amended Return'
        else:
            return 'Iowa:  No Refund or Balance Due'

def Yes_Calculation():
    if ( get_bool(IAEFWKSHT.DirDeposit) == True and get_currency(IAEFWKSHT.Refund) > 0 )  or  ( get_bool(IAEFWKSHT.EFW) == True and get_currency(IAEFWKSHT.AmtOwed) > 0 ) :
        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)
        while count <= MaxAcct:
            if get_string(USWBankAcct.BankAcct, count) != '':
                if IsStrEqual(get_string(IAEFWKSHT.Acct), get_string(USWBankAcct.BankAcct, count)):
                    return get_bool(USWBankAcct.IAT, count)
                    count = 99
            count = count + 1
        return 0
    else:
        return 0


