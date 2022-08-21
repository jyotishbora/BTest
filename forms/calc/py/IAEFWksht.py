from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Acct_Calculation():
    if GetBool(IAEFWksht.IsStateRPT) == True and GetBool(USWRALApp.StateRTDD) == True and GetBool(IAEFWksht.DirDeposit) == True:
        ReturnVal = GetString(USWRALApp.StateAccount)
    elif  ( GetBool(IAEFWksht.DirDeposit) == True and GetCurrency(IAEFWksht.Refund) > 0 )  or  ( GetBool(IAEFWksht.EFW) == True and GetCurrency(IAEFWksht.AmtOwed) > 0 ) :
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

def ACH_Calculation():
    if GetNumber(IAEFWksht.Yes) == 1:
        ReturnVal = 0
    elif GetBool(IAEFWksht.EFW) == True and GetCurrency(IAEFWksht.AmtOwed) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Address_Calculation():
    ReturnVal = GetString(IAF1040.Add) + ' ' + GetString(IAF1040.CityComb)

def AIAWH_Calculation():
    ReturnVal = GetCurrency(IAF1040.AIATaxWith)

def AmtOwed_Calculation():
    ReturnVal = GetCurrency(IAF1040.TotDue)

def ANet_Calculation():
    ReturnVal = GetCurrency(IAF1040.ANet)

def AskBankInfo_Calculation():
    if GetCurrency(IAEFWksht.AmtOwed) > 0:
        ReturnVal = 1
    elif GetBool(IAEFWksht.IsStateRPT) == True and GetBool(USWEFQual.FilingSO) == True:
        ReturnVal = 0
    elif GetCurrency(IAEFWksht.Refund) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def AskDebitCard_Calculation():
    if IsPreparer() == True:
        ReturnVal = 0
    elif GetBool(USWBankProd.HaveBankConsent) == False:
        ReturnVal = 0
        # Do not offer state debit card on linked returns using Republic Direct Deposit RT
    elif GetBool(USWBankProd.DebitCardReturn) == False and GetBool(USWBankProd.RPTReturn) == True:
        ReturnVal = 0
        # Do not offer state debit card on state only returns using Republic Direct Deposit RT
    elif GetBool(USWBankProd.IsStateRPT) == True and GetBool(USWRALApp.StateRTDD) == True:
        ReturnVal = 0
    elif GetCurrency(IAEFWksht.Refund) < Decimal("10000"):
        ReturnVal = 1
    else:
        ReturnVal = 0

def AskDriverLic_Calculation():
    if GetBool(USWEFOptions.PiggyBackIA) == True or GetBool(USWEFOptions.SOIA) == True or GetBool(USWEFOptions.SOIAX) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

def AskFedStateBank_Calculation():
    if GetBool(IAEFWksht.PrepBPTrans) == True:
        ReturnVal = 1
    elif IsPreparer() == True and GetBool(USWBasicInfo.BankProd) == True:
        ReturnVal = 0
    elif GetBool(USWBankProd.IsStateRPT) == True and GetBool(USWEFQual.FilingSO) == True:
        ReturnVal = 0
    elif GetCurrency(IAEFWksht.Refund) > 0 and GetBool(USWEFWksht.refundbox) == True:
        if GetBool(USWBasicInfo.DebitCard) == True and GetBool(IAEFWksht.AskDebitCard) == False:
            ReturnVal = 0
        elif GetBool(IAEFWksht.DebitCard) == True and GetBool(IAEFWksht.AskDebitCard) == False:
            ReturnVal = 0
        elif GetBool(USWBasicInfo.DebitCard) == True and GetBool(IAEFWksht.DebitCard) == True:
            ReturnVal = 1
        elif GetBool(USWBasicInfo.DirectDepY) == True and GetBool(IAEFWksht.DirDeposit) == True:
            if GetString(USF8888.Account1) == GetString(IAEFWksht.Acct):
                ReturnVal = 1
            else:
                ReturnVal = 0
        elif GetBool(USWBasicInfo.DirectDepN) == True and GetBool(IAEFWksht.NoDDEFW) == True:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def AskSORTDC_Calculation():
    if GetBool(USWEFOptions.SOIA) == False:
        ReturnVal = 0
    elif IsPreparer() == True:
        ReturnVal = 0
    elif GetBool(USWBankProd.HaveBankConsent) == False:
        ReturnVal = 0
    elif GetCurrency(IAEFWksht.Refund) < Decimal("10000"):
        ReturnVal = 1
    else:
        ReturnVal = 0

def AskStateRT_Calculation():
    if GetBool(USWEFOptions.SOIAX) == True:
        ReturnVal = 0
    elif GetCurrency(IAEFWksht.Refund) >= Decimal("75"):
        ReturnVal = 1
    else:
        ReturnVal = 0

def ATTax_Calculation():
    if GetBool(IARequired.LowInc) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(IAF1040.ATotIATax)

def BankName_Calculation():
    if ( GetBool(IAEFWksht.DirDeposit) == True and GetCurrency(IAEFWksht.Refund) > 0 )  or  ( GetBool(IAEFWksht.EFW) == True and GetCurrency(IAEFWksht.AmtOwed) > 0 ) :
        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)
        while count <= MaxAcct:
            if GetString(USWBankAcct.BankAcct, count) != '':
                if IsStrEqual(GetString(IAEFWksht.Acct), GetString(USWBankAcct.BankAcct, count)):
                    ReturnVal = GetString(USWBankAcct.BankName, count)
                    count = 99
            count = count + 1
        ReturnVal = ''
    else:
        ReturnVal = ''

def BankProDisCd_Calculation():
    Submission = String()

    TempStr = String()
    #Bank Product Disbursement Declaration
    #0 = Did Not Select bank product Option; 1 = Selected Debit Card Option; 2 = Selected Direct Depoist to the Bank; 3 = Requestd a Check;
    #Parameter 6 = Refund Owe Method: 0-No method; 1-AmEx debit card; 2-State issued debit card; 3-Direct deposit no Republic Bank; 4-Direct deposit through Republic Bank; 5-Paper check (refund); 6-AmEx debit card through Republic; 10-Direct debit; 11-Credit card; 12-Paper check (owe); 13-IRS EFTPS
    TempStr = GetString(IAEFWksht.EFSubmission)
    Submission = GetParam(TempStr, 1, '|')
    if GetParam(Submission, 6, ';') == '0':
        ReturnVal = '0'
    elif GetParam(Submission, 6, ';') == '1':
        ReturnVal = '1'
    elif GetParam(Submission, 6, ';') == '2':
        ReturnVal = '3'
    elif GetParam(Submission, 6, ';') == '3':
        ReturnVal = '2'
    elif GetParam(Submission, 6, ';') == '4':
        ReturnVal = '2'
    elif GetParam(Submission, 6, ';') == '5':
        ReturnVal = '3'
    elif GetParam(Submission, 6, ';') == '6':
        ReturnVal = '1'
    else:
        ReturnVal = '0'

def BIAWH_Calculation():
    ReturnVal = GetCurrency(IAF1040.BIATaxWith)

def BNet_Calculation():
    ReturnVal = GetCurrency(IAF1040.BNet)

def BP_Calculation():
    if GetBool(IAEFWksht.PrepBPTrans) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

def BTTax_Calculation():
    if GetBool(IARequired.LowInc) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(IAF1040.BTotIATax)

def CompStateEFQA_Calculation():
    # If not filing Iowa return, always return False
    if GetBool(USWEFOptions.PiggyBackIA) == False and GetBool(USWEFOptions.SOIA) == False and GetBool(USWEFOptions.SOIAX) == False:
        ReturnVal = 0
    elif GetCurrency(IAEFWksht.Refund) > 0:
        if GetBool(IAEFWksht.PrepRevQA) == False:
            ReturnVal = 1
        elif IsPreparer() == True and GetBool(IAEFWksht.PrepBPTrans) == True:
            ReturnVal = 0
        elif GetBool(USWBankProd.DebitCardReturn) == True and GetBool(IAEFWksht.DebitCard) == False and GetBool(IAEFWksht.DirDeposit) == False and GetBool(IAEFWksht.NoDDEFW) == False:
            ReturnVal = 1
        elif GetBool(IAEFWksht.DirDeposit) == False and GetBool(IAEFWksht.NoDDEFW) == False:
            ReturnVal = 1
        elif GetBool(USWBankProd.DebitCardReturn) == False and GetBool(IAEFWksht.DirDeposit) == False and GetBool(IAEFWksht.NoDDEFW) == False:
            ReturnVal = 1
        elif GetBool(IAEFWksht.DirDeposit) == True and GetNumber(USFInterview.ValidBankAccts) == 0:
            ReturnVal = 1
        else:
            ReturnVal = 0
    elif GetCurrency(IAEFWksht.AmtOwed) > 0:
        if GetBool(IAEFWksht.PrepRevQA) == False:
            ReturnVal = 1
        elif GetBool(IAEFWksht.EFW) == False and GetBool(IAEFWksht.NoDDEFW) == False:
            ReturnVal = 1
        elif GetBool(IAEFWksht.EFW) == True and GetNumber(USFInterview.ValidBankAccts) == 0:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def DANChange_Calculation():
    ReturnVal = GetString(IAEFWksht.DirDepDan) + '|'

def DC_Calculation():
    if GetBool(IAEFWksht.PrepBPTrans) == True:
        ReturnVal = 0
    elif GetBool(IAEFWksht.DebitCard) == True and GetCurrency(IAEFWksht.Refund) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def DD_Calculation():
    if GetNumber(IAEFWksht.Yes) == 1:
        ReturnVal = 0
    elif GetBool(IAEFWksht.PrepBPTrans) == True:
        ReturnVal = 0
    elif GetBool(IAEFWksht.DirDeposit) == True and GetCurrency(IAEFWksht.Refund) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def DebitCard_Calculation():
    if GetBool(IAEFWksht.IsStateRPT) == True:
        if GetBool(USWRALApp.StateRTDC) == True and GetBool(IAEFWksht.AskDebitCard) == True:
            ReturnVal = 1
        else:
            ReturnVal = 0
    elif GetBool(USWBasicInfo.DebitCard) == True and GetCurrency(USF1040.RefundOwe) > 0 and GetBool(IAEFWksht.AskDebitCard) == True:
        if GetCurrency(IAEFWksht.Refund) > 0:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def Desc_Calculation():
    ReturnVal = GetString(IARequired.CombNames)

def DirDepChecking_Calculation():
    if ( GetBool(IAEFWksht.DirDeposit) == True and GetCurrency(IAEFWksht.Refund) > 0 )  or  ( GetBool(IAEFWksht.EFW) == True and GetCurrency(IAEFWksht.AmtOwed) > 0 ) :
        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)
        while count <= MaxAcct:
            if GetString(USWBankAcct.BankAcct, count) != '':
                if IsStrEqual(GetString(IAEFWksht.Acct), GetString(USWBankAcct.BankAcct, count)):
                    ReturnVal = GetBool(USWBankAcct.Checking, count)
                    count = 99
            count = count + 1
        ReturnVal = 0
    else:
        ReturnVal = 0

def DirDepDan_Calculation():
    if ( GetBool(IAEFWksht.DirDeposit) == True and GetCurrency(IAEFWksht.Refund) > 0 )  or  ( GetBool(IAEFWksht.EFW) == True and GetCurrency(IAEFWksht.AmtOwed) > 0 ) :
        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)
        while count <= MaxAcct:
            if GetString(USWBankAcct.BankAcct, count) != '':
                if IsStrEqual(GetString(IAEFWksht.Acct), GetString(USWBankAcct.BankAcct, count)):
                    ReturnVal = GetString(USWBankAcct.AcctNum, count)
                    count = 99
            count = count + 1
        ReturnVal = ''
    else:
        ReturnVal = ''

def DirDeposit_Calculation():
    if GetBool(IAEFWksht.IsStateRPT) == True:
        if GetBool(USWRALApp.StateRTDD) == True:
            ReturnVal = 1
        else:
            ReturnVal = 0
    elif GetBool(USWBasicInfo.DirectDepY) == True and GetCurrency(USF1040.RefundOwe) > 0:
        if GetCurrency(IAEFWksht.Refund) > 0:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def DirDepRTN_Calculation():
    if ( GetBool(IAEFWksht.DirDeposit) == True and GetCurrency(IAEFWksht.Refund) > 0 )  or  ( GetBool(IAEFWksht.EFW) == True and GetCurrency(IAEFWksht.AmtOwed) > 0 ) :
        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)
        while count <= MaxAcct:
            if GetString(USWBankAcct.BankAcct, count) != '':
                if IsStrEqual(GetString(IAEFWksht.Acct), GetString(USWBankAcct.BankAcct, count)):
                    ReturnVal = GetString(USWBankAcct.RTN, count)
                    count = 99
            count = count + 1
        ReturnVal = ''
    else:
        ReturnVal = ''

def DirDepSavings_Calculation():
    if ( GetBool(IAEFWksht.DirDeposit) == True and GetCurrency(IAEFWksht.Refund) > 0 )  or  ( GetBool(IAEFWksht.EFW) == True and GetCurrency(IAEFWksht.AmtOwed) > 0 ) :
        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)
        while count <= MaxAcct:
            if GetString(USWBankAcct.BankAcct, count) != '':
                if IsStrEqual(GetString(IAEFWksht.Acct), GetString(USWBankAcct.BankAcct, count)):
                    ReturnVal = GetBool(USWBankAcct.Savings, count)
                    count = 99
            count = count + 1
        ReturnVal = 0
    else:
        ReturnVal = 0

def DirDepTrigger_Calculation():
    if GetNumber(IAEFWksht.EFDDCode) == 1:
        ReturnVal = 1
    else:
        ReturnVal = 0

def DirectDepY_Calculation():
    if GetBool(IAEFWksht.DD) == True:
        if GetBool(USWBankProd.RPTReturn) == True and GetBool(IAEFWksht.SameFedBank) == True:
            ReturnVal = 1
        elif GetBool(IAEFWksht.IsStateRPT) == True:
            ReturnVal = 1
        else:
            ReturnVal = 0
    elif GetBool(IAEFWksht.DC) == True:
        if GetBool(USWBankProd.RPTReturn) == True:
            ReturnVal = 1
        elif GetBool(IAEFWksht.IsStateRPT) == True:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def EFAvailable_Calculation():
    if GetBool(IA1040X.EFAmend) == True:
        ReturnVal = 'IAX,2, Amended|'
    else:
        ReturnVal = 'IA,0,|'

def EFChecking_Calculation():
    if GetBool(IAEFWksht.PrepBPTrans) == True:
        ReturnVal = GetBool(USWEFWkSht2.DirDepChk)
    elif GetBool(IAEFWksht.DebitCard) == True and GetCurrency(IAEFWksht.Refund) > 0:
        ReturnVal = 1
    elif GetNumber(IAEFWksht.EFDDCode) != 0:
        ReturnVal = GetBool(IAEFWksht.DirDepChecking)
    else:
        ReturnVal = 0

def EFDan_Calculation():
    if GetBool(IAEFWksht.PrepBPTrans) == True:
        ReturnVal = GetString(USWEFWkSht2.DirDepDan)
    elif GetBool(IAEFWksht.DebitCard) == True and GetCurrency(IAEFWksht.Refund) > 0:
        ReturnVal = GetString(USWDebitCard.AcctNum)
    elif GetNumber(IAEFWksht.EFDDCode) != 0:
        ReturnVal = GetString(IAEFWksht.DirDepDan)
    else:
        ReturnVal = ''

def EFDDCode_Calculation():
    if GetBool(IAEFWksht.PrepBPTrans) == True:
        ReturnVal = 1
    elif GetBool(IAEFWksht.DebitCard) == True and GetCurrency(IAEFWksht.Refund) > 0:
        ReturnVal = 1
    elif GetNumber(IAEFWksht.Yes) == 1:
        ReturnVal = 0
    elif GetBool(IAEFWksht.DirDeposit) == True and GetCurrency(IAEFWksht.Refund) > 0:
        ReturnVal = 1
    elif GetBool(IAEFWksht.EFW) == True and GetCurrency(IAEFWksht.AmtOwed) > 0:
        ReturnVal = 2
    else:
        ReturnVal = 0

def EFDedCode_Calculation():
    if GetBool(IARequired.LowInc) == True:
        ReturnVal = ''
    elif GetBool(IAF1040.ItemCheck) == True:
        ReturnVal = '1'
    else:
        ReturnVal = '3'

def EFEFWAmt_Calculation():
    if GetNumber(IAEFWksht.EFDDCode) == 2:
        ReturnVal = GetCurrency(IAEFWksht.AmtOwed)
    else:
        ReturnVal = 0

def EFEFWDate_Calculation():
    if GetNumber(IAEFWksht.EFDDCode) == 2:
        ReturnVal = GetString(IAEFWksht.EFWDate)
    else:
        ReturnVal = ''

def EFRtn_Calculation():
    if GetBool(IAEFWksht.PrepBPTrans) == True:
        ReturnVal = GetString(USWEFWkSht2.DirDepRTN)
    elif GetBool(IAEFWksht.DebitCard) == True and GetCurrency(IAEFWksht.Refund) > 0:
        ReturnVal = GetString(USWDebitCard.RTN)
    elif GetNumber(IAEFWksht.EFDDCode) != 0:
        ReturnVal = GetString(IAEFWksht.DirDepRTN)
    else:
        ReturnVal = ''

def EFSavings_Calculation():
    if GetBool(IAEFWksht.PrepBPTrans) == True:
        ReturnVal = GetBool(USWEFWkSht2.DirDepSav)
    elif GetBool(IAEFWksht.DebitCard) == True and GetCurrency(IAEFWksht.Refund) > 0:
        ReturnVal = 0
    elif GetNumber(IAEFWksht.EFDDCode) != 0:
        ReturnVal = GetBool(IAEFWksht.DirDepSavings)
    else:
        ReturnVal = 0

def EFSpInit_Calculation():
    if GetBool(IAF1040.MFJ) == True or GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetString(USWBasicInfo.SpInit)
    else:
        ReturnVal = ''

def EFSpLast_Calculation():
    if GetBool(IAF1040.MFJ) == True or GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetString(USWBasicInfo.SPLast)
    else:
        ReturnVal = ''

def EFSpouseFirst_Calculation():
    if GetBool(IAF1040.MFJ) == True or GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetString(USWBasicInfo.SpouseFirst)
    else:
        ReturnVal = ''

def EFSpSuffix_Calculation():
    if GetBool(IAF1040.MFJ) == True or GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetString(USWBasicInfo.SPSuffix)
    else:
        ReturnVal = ''

def EFStRefund_Calculation():
    if GetBool(USWEFOptions.PiggyBackIA) == True:
        if GetCurrency(IAEFWksht.Refund) > 0:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def EFSubmission_Calculation():
    RefOweMethod = String()
    # General Guideline to follow (use | bar if more than 1 return can be filed)
    # Parameter 1 = Module Name
    # Parameter 2 = Return Type: 0-Return; 1-Extension; 2-Amended; 3-Special1; 4-SpecialTaxpayer; 5-SpecialTaxpayerExtension; 6-SpecialSpouse; 7-SpecialSpouseExtension; 8-NewYorkLLC; 9-Special
    # Parameter 3 = EF Type: 0-Legacy; 1-Qualifies for MeF (used if state supports legacy); 2-Must Be MeF (always used if state does not support legacy)
    # Parameter 4 = Fed XML Version: 0-Send no federal XML; 1-Send accepted federal; 2-Send federal XML used to complete state return
    # Parameter 5 = Special Description: description for special returns, if none space
    # Parameter 6 = Refund Owe Method: 0-No method; 1-AmEx debit card; 2-State issued debit card; 3-Direct deposit no Republic Bank; 4-Direct deposit through Republic Bank; 5-Paper check (refund); 6-AmEx debit card through Republic; 10-Direct debit; 11-Credit card; 12-Paper check (owe); 13-IRS EFTPS
    if GetBool(USWEFOptions.PiggyBackIA) == True or GetBool(USWEFOptions.SOIA) == True:
        if GetCurrency(IAF1040.RefBalDue) == 0:
            RefOweMethod = '0'
        elif GetBool(IAEFWksht.PrepBPTrans) == True:
            RefOweMethod = '4'
        elif GetBool(IAEFWksht.DC) == True:
            if GetBool(USWBankProd.RPTReturn) == True:
                RefOweMethod = '6'
            elif GetBool(IAEFWksht.IsStateRPT) == True:
                RefOweMethod = '6'
            else:
                RefOweMethod = '1'
        elif GetBool(IAEFWksht.DD) == True:
            if GetBool(USWBankProd.RPTReturn) == True and GetBool(IAEFWksht.SameFedBank) == True:
                RefOweMethod = '4'
            elif GetBool(IAEFWksht.IsStateRPT) == True:
                RefOweMethod = '4'
            else:
                RefOweMethod = '3'
        elif GetCurrency(IAF1040.RefBalDue) > 0:
            RefOweMethod = '5'
        elif GetString(IAEFWksht.EFDDCode) == '2':
            RefOweMethod = '10'
        else:
            RefOweMethod = '12'
    elif GetBool(USWEFOptions.SOIAX) == True:
        if GetCurrency(IAF1040.RefBalDue) == 0:
            RefOweMethod = '0'
        elif GetBool(IAEFWksht.DD) == True:
            RefOweMethod = '3'
        elif GetCurrency(IAF1040.RefBalDue) > 0:
            RefOweMethod = '5'
        elif GetString(IAEFWksht.EFDDCode) == '2':
            RefOweMethod = '10'
        else:
            RefOweMethod = '12'
    else:
        RefOweMethod = '0'
    if GetBool(USWEFOptions.PiggyBackIA) == True or GetBool(USWEFOptions.SOIA) == True:
        ReturnVal = 'IA;0;2;2; ;' + RefOweMethod + '|'
    elif GetBool(USWEFOptions.SOIAX) == True:
        ReturnVal = 'IA;2;2;2;Amended;' + RefOweMethod + '|'
    else:
        ReturnVal = ''

def EROAddress_Calculation():
    if IsPreparer() == True:
        ReturnVal = GetString(USWBasicInfo.EROAddress)
    else:
        ReturnVal = ''

def EROCityComb_Calculation():
    if IsPreparer() == False:
        ReturnVal = ''
    elif Trim(GetString(USWBasicInfo.EROForCtry)) != '':
        if Trim(GetString(USWBasicInfo.EROForProvince)) != '' and Trim(GetString(USWBasicInfo.EROForPC)) != '':
            ReturnVal = GetString(USWBasicInfo.EROCity) + ', ' + GetString(USWBasicInfo.EROForProvince) + ', ' + GetString(USWBasicInfo.EROForPC) + ', ' + GetString(USWBasicInfo.EROForCtry)
        elif Trim(GetString(USWBasicInfo.EROForProvince)) != '':
            ReturnVal = GetString(USWBasicInfo.EROCity) + ', ' + GetString(USWBasicInfo.EROForProvince) + ', ' + GetString(USWBasicInfo.EROForCtry)
        elif Trim(GetString(USWBasicInfo.EROForPC)) != '':
            ReturnVal = GetString(USWBasicInfo.EROCity) + ', ' + GetString(USWBasicInfo.EROForPC) + ', ' + GetString(USWBasicInfo.EROForCtry)
        else:
            ReturnVal = GetString(USWBasicInfo.EROCity) + ', ' + GetString(USWBasicInfo.EROForCtry)
    elif Trim(GetString(USWBasicInfo.EROCity)) != '':
        ReturnVal = GetString(USWBasicInfo.EROCity) + ', ' + GetString(USWBasicInfo.StateAbbERO) + ' ' + GetString(USWBasicInfo.EROZip)
    else:
        ReturnVal = GetString(USWBasicInfo.StateAbbERO) + ' ' + GetString(USWBasicInfo.EROZip)

def EROEIN_Calculation():
    if IsPreparer() == True:
        ReturnVal = GetString(USWBasicInfo.EROEIN)
    else:
        ReturnVal = ''

def EROFirmName_Calculation():
    if IsPreparer() == True:
        ReturnVal = GetString(USWBasicInfo.EROFirmName)
    else:
        ReturnVal = ''

def EROPhone_Calculation():
    if IsPreparer() == False:
        ReturnVal = ''
    elif Trim(GetString(USWBasicInfo.EROPhone)) != '':
        ReturnVal = GetString(USWBasicInfo.EROPhone)
    else:
        ReturnVal = GetString(USWBasicInfo.EROForPhone)

def EROPrep_Calculation():
    if IsPreparer() == True:
        ReturnVal = GetBool(USWBasicInfo.PaidPrepY)
    else:
        ReturnVal = 0

def EROSE_Calculation():
    if IsPreparer() == True:
        ReturnVal = GetBool(USWBasicInfo.EROSelfEmp)
    else:
        ReturnVal = 0

def EROSSN_Calculation():
    EROPTIN = String()
    EROPTIN = LetterStr(GetString(USWBasicInfo.EROSSN))
    if IsPreparer() == True and IsStrEqual(EROPTIN, 'P'):
        ReturnVal = GetString(USWBasicInfo.EROSSN)
    else:
        ReturnVal = ''

def Exist_Calculation():
    ReturnVal = 1

def FedChecking_Calculation():
    if GetCurrency(USWBasicInfo.WithdrawalAmt) > 0 and GetDate(USWBasicInfo.withdrawldate) != '':
        ReturnVal = GetBool(USWBasicInfo.ACHChecking)
    else:
        ReturnVal = GetBool(USF8888.EFChecking(0))

def FedDAN_Calculation():
    if GetCurrency(USWBasicInfo.WithdrawalAmt) > 0 and GetDate(USWBasicInfo.withdrawldate) != '':
        ReturnVal = GetString(USWBasicInfo.ACHDAN)
    else:
        ReturnVal = GetString(USF8888.EFAcctNum(0))

def FedRTN_Calculation():
    if GetCurrency(USWBasicInfo.WithdrawalAmt) > 0 and GetDate(USWBasicInfo.withdrawldate) != '':
        ReturnVal = GetString(USWBasicInfo.ACHRTN)
    else:
        ReturnVal = GetString(USF8888.EFRtn(0))

def FedSavings_Calculation():
    if GetCurrency(USWBasicInfo.WithdrawalAmt) > 0 and GetDate(USWBasicInfo.withdrawldate) != '':
        ReturnVal = GetBool(USWBasicInfo.ACHSavings)
    else:
        ReturnVal = GetBool(USF8888.EFSaveAcct(0))

def FedTrans_Calculation():
    #If (GetBool(IAEFWksht.DirDeposit) = True And GetCurrency(IAEFWksht.Refund) > 0) Or (GetBool(IAEFWksht.EFW) = True And GetCurrency(IAEFWksht.AmtOwed) > 0) Then
    #    If GetBool(IAEFWksht.TransInfo) = True Then
    #        ReturnVal = 1
    #    Else
    #        ReturnVal = 0
    #    End If
    #Else
    ReturnVal = 0
    #End If

def FinTransTrigger_Calculation():
    if GetNumber(IAEFWksht.EFDDCode) != 0:
        ReturnVal = 1
    elif GetNumber(IAEstimates.EstEFW, 1) > 0 or GetNumber(IAEstimates.EstEFW, 2) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def ForCity_Calculation():
    ReturnVal = GetString(USWBasicInfo.ForCity)

def ForCountry_Calculation():
    ReturnVal = GetString(USWBasicInfo.ForCountry)

def ForStreet_Calculation():
    ReturnVal = GetString(USWBasicInfo.ForStreet)

def IsStateRPT_Calculation():
    if GetBool(IAEFWksht.AskStateRT) == False:
        ReturnVal = 0
    elif GetBool(USWBankProd.ClearedInvoiceFees) == True:
        ReturnVal = 0
    elif GetBool(USWRALApp.StateRTDC) == True and GetBool(IAEFWksht.AskSORTDC) == False:
        ReturnVal = 0
    elif GetBool(USWBankProd.StateRPT) == True and GetBool(USWBankProd.StateBankAgree) == True and GetBool(USWBankProd.StateBankAgree2) == True and GetCurrency(IAEFWksht.Refund) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def MeFPrepInfo_Calculation():
    if IsPreparer() == True:
        if GetBool(USWBasicInfo.NoPrep) == False:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def MeFSP137_Calculation():
    if GetNumber(IA137.MEF137SP, FieldCopies(IA137.Spouse)) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def MeFTP137_Calculation():
    if GetNumber(IA137.MEF137TP, FieldCopies(IA137.Taxpayer)) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Need8453_Calculation():
    ReturnVal = 1

def No_Calculation():
    if ( GetBool(IAEFWksht.DirDeposit) == True and GetCurrency(IAEFWksht.Refund) > 0 )  or  ( GetBool(IAEFWksht.EFW) == True and GetCurrency(IAEFWksht.AmtOwed) > 0 ) :
        if GetBool(IAEFWksht.Yes) == True:
            ReturnVal = 0
        else:
            ReturnVal = 1
    else:
        ReturnVal = 0

def NoBankSel_Calculation():
    if GetBool(IAEFWksht.DirDeposit) == True or GetBool(IAEFWksht.EFW):
        if Trim(GetString(IAEFWksht.Acct)) == '':
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def NoBankSelInt_Calculation():
    if ( GetBool(IAEFWksht.DirDeposit) == True )  or  ( GetBool(IAEFWksht.EFW) == True ) :
        if GetBool(USTopicList.HaveBankWSSend) == False:
            ReturnVal = 0
        elif Trim(GetString(IAEFWksht.Acct)) == '':
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def NoDDEFW_Calculation():
    if GetBool(IAEFWksht.IsStateRPT) == True:
        ReturnVal = 0
    elif GetBool(USWBasicInfo.DirectDepN) == True and GetCurrency(USF1040.RefundOwe) > 0:
        if GetCurrency(IAEFWksht.Refund) > 0:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def NonForCity_Calculation():
    ReturnVal = GetString(USWBasicInfo.NonForCity)

def NonForState_Calculation():
    ReturnVal = GetString(USWBasicInfo.NonForState)

def NonForStreet_Calculation():
    ReturnVal = GetString(USWBasicInfo.NonForStreet)

def NonForZip_Calculation():
    ReturnVal = GetString(USWBasicInfo.NonForZip)

def PC_Calculation():
    if GetCurrency(IAEFWksht.Refund) == 0:
        ReturnVal = 0
    elif GetBool(IAEFWksht.DD) == False and GetBool(IAEFWksht.BP) == False and GetBool(IAEFWksht.DC) == False:
        ReturnVal = 1
    else:
        ReturnVal = 0

def PrBankName_Calculation():
    if GetNumber(IAEFWksht.EFDDCode) != 0 and GetBool(IAEFWksht.DebitCard) == False and GetBool(IAEFWksht.PrepBPTrans) == False:
        ReturnVal = GetString(IAEFWksht.BankName)
    else:
        ReturnVal = ''

def PrChecking_Calculation():
    if GetNumber(IAEFWksht.EFDDCode) != 0 and GetBool(IAEFWksht.DebitCard) == False and GetBool(IAEFWksht.PrepBPTrans) == False:
        ReturnVal = GetBool(IAEFWksht.DirDepChecking)
    else:
        ReturnVal = 0

def PrDAN_Calculation():
    if GetNumber(IAEFWksht.EFDDCode) != 0 and GetBool(IAEFWksht.DebitCard) == False and GetBool(IAEFWksht.PrepBPTrans) == False:
        ReturnVal = GetString(IAEFWksht.DirDepDan)
    else:
        ReturnVal = ''

def PrepAddress_Calculation():
    if IsPreparer() == True:
        if GetBool(IAEFWksht.EROPrep) == False:
            ReturnVal = GetString(USWBasicInfo.PrepAdd)
        else:
            ReturnVal = ''
    else:
        ReturnVal = ''

def PrepBPTrans_Calculation():
    if GetBool(USWRALApp.RepRouteState) == False:
        ReturnVal = 0
    elif IsPreparer() == False:
        ReturnVal = 0
    elif GetBool(USWBasicInfo.BankProd) == True and GetCurrency(USF1040.RefundOwe) > 0:
        if GetBool(USWBankProd.Republic) == True and GetBool(IAEFWksht.EFStRefund) == True:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def PrepCityComb_Calculation():
    if IsPreparer() == True:
        if GetBool(IAEFWksht.EROPrep) == False:
            ReturnVal = GetString(USWBasicInfo.CombPrepCityStZipFor)
        else:
            ReturnVal = ''
    else:
        ReturnVal = ''

def PrepEIN_Calculation():
    if IsPreparer() == True:
        if GetBool(IAEFWksht.EROPrep) == False:
            ReturnVal = GetString(USWBasicInfo.PrepEIN)
        else:
            ReturnVal = ''
    else:
        ReturnVal = ''

def PrepFirmName_Calculation():
    if IsPreparer() == True:
        if GetBool(IAEFWksht.EROPrep) == False:
            ReturnVal = GetString(USWBasicInfo.PrepName)
        else:
            ReturnVal = ''
    else:
        ReturnVal = ''

def PrepPhone_Calculation():
    if IsPreparer() == True:
        if GetBool(IAEFWksht.EROPrep) == False:
            ReturnVal = GetString(IAF1040.PrepPhone)
        else:
            ReturnVal = ''
    else:
        ReturnVal = ''

def PrepSE_Calculation():
    if IsPreparer() == True:
        if GetBool(IAEFWksht.EROPrep) == False:
            ReturnVal = GetBool(USWBasicInfo.SelfEm)
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def PrepSSN_Calculation():
    if IsPreparer() == True:
        if GetBool(IAEFWksht.EROPrep) == False:
            ReturnVal = GetString(USWBasicInfo.PrepSSN)
        else:
            ReturnVal = ''
    else:
        ReturnVal = ''

def PrERODate_Calculation():
    if GetBool(IAEFWksht.EROPrep) == True:
        ReturnVal = GetString(USWBasicInfo.PrPrepDate)
    else:
        ReturnVal = ''

def PrEROSig_Calculation():
    if GetBool(IAEFWksht.EROPrep) == True:
        ReturnVal = GetString(USWBasicInfo.PrPrepSig)
    else:
        ReturnVal = ''

def PrintReturn_Calculation():
    PrintList_Clear(PrintList_EF)
    if Trim(GetString(IAEFWksht.EFSubmission)) != '':
        if GetBool(IA1040X.EFAmend) == True:
            PrintList_AddHTML(PrintList_EF, EFReturnType_AmendedReturn, 'E-filing Instructions', 'ia instructions/IAWEFFilingInst.htm')
            if GetBool(IAEFWksht.Need8453) == True:
                PrintList_AddCustom(PrintList_EF, EFReturnType_AmendedReturn, 'Form 8453', 'PrintEFileForms')
            PrintList_AddReturn(PrintList_EF, EFReturnType_AmendedReturn, 'Amended Return')
        else:
            PrintList_AddHTML(PrintList_EF, EFReturnType_Return, 'E-filing Instructions', 'ia instructions/IAWEFFilingInst.htm')
            if GetBool(IAEFWksht.Need8453) == True:
                PrintList_AddCustom(PrintList_EF, EFReturnType_Return, 'Form 8453', 'PrintEFileForms')
            PrintList_AddReturn(PrintList_EF, EFReturnType_Return, 'Return')
    ReturnVal = ''

def PrPrepDate_Calculation():
    if IsPreparer() == True:
        if GetBool(IAEFWksht.EROPrep) == False:
            ReturnVal = GetString(USWBasicInfo.PrPrepDate)
        else:
            ReturnVal = ''
    else:
        ReturnVal = ''

def PrPrepSig_Calculation():
    if IsPreparer() == True:
        if GetBool(IAEFWksht.EROPrep) == False:
            ReturnVal = GetString(USWBasicInfo.PrPrepSig)
        else:
            ReturnVal = ''
    else:
        ReturnVal = ''

def PrRtn_Calculation():
    if GetNumber(IAEFWksht.EFDDCode) != 0 and GetBool(IAEFWksht.DebitCard) == False and GetBool(IAEFWksht.PrepBPTrans) == False:
        ReturnVal = GetString(IAEFWksht.DirDepRTN)
    else:
        ReturnVal = ''

def PrSavings_Calculation():
    if GetNumber(IAEFWksht.EFDDCode) != 0 and GetBool(IAEFWksht.DebitCard) == False and GetBool(IAEFWksht.PrepBPTrans) == False:
        ReturnVal = GetBool(IAEFWksht.DirDepSavings)
    else:
        ReturnVal = 0

def QnAFedBank_Calculation():
    #If GetBool(IAEFWksht.AskFedStateBank) = True Then
    #    ReturnVal = 0
    #ElseIf (GetBool(IAEFWksht.DirDeposit) = True And GetCurrency(IAEFWksht.Refund) > 0) Or (GetBool(IAEFWksht.EFW) = True And GetCurrency(IAEFWksht.AmtOwed) > 0) Then
    #    If GetBool(IAEFWksht.TransInfo) = True Then
    #        ReturnVal = 1
    #    ElseIf Trim(GetString(IAEFWksht.FedRTN)) <> "" And Trim(GetString(IAEFWksht.FedDAN)) <> "" Then
    #        ReturnVal = 1
    #    Else
    #        ReturnVal = 0
    #    End If
    #Else
    ReturnVal = 0
    #End If

def RefProdCIPInd_Calculation():
    Submission = String()

    TempStr = String()
    TempStr = GetString(IAEFWksht.EFSubmission)
    Submission = GetParam(TempStr, 1, '|')
    if GetParam(Submission, 6, ';') == '0':
        ReturnVal = '0'
    elif GetParam(Submission, 6, ';') == '1':
        if Trim(GetString(USWDebitCard.IDNumber)) != '':
            ReturnVal = '1'
        else:
            ReturnVal = '2'
    elif GetParam(Submission, 6, ';') == '3':
        ReturnVal = '0'
    elif GetParam(Submission, 6, ';') == '4':
        ReturnVal = '1'
    elif GetParam(Submission, 6, ';') == '5':
        ReturnVal = '0'
    elif GetParam(Submission, 6, ';') == '6':
        ReturnVal = '1'
    else:
        ReturnVal = '0'

def RefProdInd_Calculation():
    Submission = String()

    TempStr = String()
    TempStr = GetString(IAEFWksht.EFSubmission)
    Submission = GetParam(TempStr, 1, '|')
    if GetParam(Submission, 6, ';') == '0':
        ReturnVal = '0'
    elif GetParam(Submission, 6, ';') == '1':
        ReturnVal = '2'
    elif GetParam(Submission, 6, ';') == '2':
        ReturnVal = '0'
    elif GetParam(Submission, 6, ';') == '3':
        ReturnVal = '0'
    elif GetParam(Submission, 6, ';') == '4':
        ReturnVal = '2'
    elif GetParam(Submission, 6, ';') == '5':
        ReturnVal = '0'
    elif GetParam(Submission, 6, ';') == '6':
        ReturnVal = '2'
    else:
        ReturnVal = '0'

def Refund_Calculation():
    ReturnVal = GetCurrency(IAF1040.Refund)

def RefundDelay_Calculation():
    #this was set to 1 in 2017 will need to verify again for 2018 before shipping
    ReturnVal = 0

def RTNChange_Calculation():
    ReturnVal = GetString(IAEFWksht.DirDepRTN) + '|'

def SameFedBank_Calculation():
    SameRTN = Integer()

    SameDAN = Integer()

    SameType = Integer()
    if GetString(IAEFWksht.FedRTN) == GetString(IAEFWksht.DirDepRTN):
        SameRTN = 1
    else:
        SameRTN = 0
    if GetString(IAEFWksht.FedDAN) == GetString(IAEFWksht.DirDepDan):
        SameDAN = 1
    else:
        SameDAN = 0
    if GetBool(IAEFWksht.FedChecking) == True and GetBool(IAEFWksht.DirDepChecking) == True:
        SameType = 1
    elif GetBool(IAEFWksht.FedSavings) == True and GetBool(IAEFWksht.DirDepSavings) == True:
        SameType = 1
    else:
        SameType = 0
    if GetBool(USWBasicInfo.DirectDepY) == True and GetCurrency(USF1040.RefundOwe) > 0:
        if SameRTN + SameDAN + SameType == 3:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def SPCombName_Calculation():
    ReturnVal = GetString(IARequired.SPCombName)

def SpSSN_Calculation():
    ReturnVal = GetString(IAF1040.SpouseSSN)

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

def StateDCReturn_Calculation():
    if GetBool(USWEFOptions.PiggyBackIA) == True or GetBool(USWEFOptions.SOIA) == True or GetBool(USWEFOptions.SOIAX) == True:
        if GetBool(IAEFWksht.DebitCard) == True and GetCurrency(IAEFWksht.Refund) > 0 and GetBool(IAEFWksht.AskDebitCard) == True:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def TPCombName_Calculation():
    ReturnVal = GetString(IARequired.TPCombName)

def UBATrig_Calculation():
    if GetString(IAEFWksht.BankProDisCd) == '1':
        ReturnVal = 1
    elif GetString(IAEFWksht.BankProDisCd) == '2':
        ReturnVal = 1
    else:
        ReturnVal = 0

def UltDAN_Calculation():
    if GetBool(IAEFWksht.PrepBPTrans) == True:
        ReturnVal = GetString(USWRALApp.PrepBPDAN)
    else:
        ReturnVal = GetString(IAEFWksht.EFDan)

def UltRTN_Calculation():
    if GetBool(IAEFWksht.PrepBPTrans) == True:
        ReturnVal = GetString(USWRALApp.PrepBPRTN)
    else:
        ReturnVal = GetString(IAEFWksht.EFRtn)

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
    if GetCurrency(IAEFWksht.Refund) > 0:
        if GetBool(IA1040X.EFAmend) == True:
            RefOweText = 'Iowa Amended Refund'
        else:
            RefOweText = 'Iowa Refund'
        if GetBool(IAEFWksht.BP) == True:
            DispMethText = 'Republic Bank Product'
        elif GetBool(IAEFWksht.DD) == True:
            DispMethText = 'Direct Deposit'
            Routing = 'RTN: ' + GetString(IAEFWksht.EFRtn)
            AcctNum = 'Acct #: ' + GetString(IAEFWksht.EFDan)
            if GetBool(IAEFWksht.EFChecking) == True:
                BankType = 'Type: Checking'
            else:
                BankType = 'Type: Savings'
        elif GetBool(IAEFWksht.DC) == True:
            DispMethText = 'American Express Serve Card'
        else:
            DispMethText = 'Paper Check'
        ReturnVal = RefOweText + '/Refund Method: ' + DispMethText + '/' + Routing + '/' + AcctNum + '/' + BankType
    elif GetCurrency(IAEFWksht.AmtOwed) > 0:
        if GetBool(IA1040X.EFAmend) == True:
            RefOweText = 'Iowa Amended Balance Due'
        else:
            RefOweText = 'Iowa Balance Due'
        if GetBool(IAEFWksht.ACH) == True:
            DispMethText = 'Direct Withdrawal'
            Routing = 'RTN: ' + GetString(IAEFWksht.EFRtn)
            AcctNum = 'Acct #: ' + GetString(IAEFWksht.EFDan)
            if GetBool(IAEFWksht.EFChecking) == True:
                BankType = 'Type: Checking'
            else:
                BankType = 'Type: Savings'
            EffDate = 'Withdrawal Date: ' + GetVerboseDate(GetDate(IAEFWksht.EFEFWDate))
        else:
            DispMethText = 'Paper Check'
        ReturnVal = RefOweText + '/Payment Method: ' + DispMethText + '/' + Routing + '/' + AcctNum + '/' + BankType + '/' + EffDate
    else:
        if GetBool(IA1040X.EFAmend) == True:
            ReturnVal = 'Iowa:  No Refund or Balance Due on Amended Return'
        else:
            ReturnVal = 'Iowa:  No Refund or Balance Due'

def Yes_Calculation():
    if ( GetBool(IAEFWksht.DirDeposit) == True and GetCurrency(IAEFWksht.Refund) > 0 )  or  ( GetBool(IAEFWksht.EFW) == True and GetCurrency(IAEFWksht.AmtOwed) > 0 ) :
        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)
        while count <= MaxAcct:
            if GetString(USWBankAcct.BankAcct, count) != '':
                if IsStrEqual(GetString(IAEFWksht.Acct), GetString(USWBankAcct.BankAcct, count)):
                    ReturnVal = GetBool(USWBankAcct.IAT, count)
                    count = 99
            count = count + 1
        ReturnVal = 0
    else:
        ReturnVal = 0

