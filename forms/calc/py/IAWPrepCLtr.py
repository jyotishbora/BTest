from vb2py.vbfunctions import *
from vb2py.vbdebug import *
import datetime



def AddComm1_Calculation():
    if Trim(GetString(IAWPrepCLtr.Comm1)) != '':
        ReturnVal = 1
    else:
        ReturnVal = 0

def AddComm2_Calculation():
    if Trim(GetString(IAWPrepCLtr.Comm2)) != '':
        ReturnVal = 1
    else:
        ReturnVal = 0

def AddComm3_Calculation():
    if Trim(GetString(IAWPrepCLtr.Comm3)) != '':
        ReturnVal = 1
    else:
        ReturnVal = 0

def AddComm4_Calculation():
    if Trim(GetString(IAWPrepCLtr.Comm4)) != '':
        ReturnVal = 1
    else:
        ReturnVal = 0

def AddComm5_Calculation():
    if Trim(GetString(IAWPrepCLtr.Comm5)) != '':
        ReturnVal = 1
    else:
        ReturnVal = 0

def AddComm6_Calculation():
    if Trim(GetString(IAWPrepCLtr.Comm6)) != '':
        ReturnVal = 1
    else:
        ReturnVal = 0

def C1EstInfo_Calculation():
    if GetBool(IAWPrepCLtr.NEst) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetBool(IAFilingInst.C1EstInfo)

def C2EstInfo_Calculation():
    if GetBool(IAWPrepCLtr.NEst) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetBool(IAFilingInst.C2EstInfo)

def Comm1_Calculation():
    ReturnVal = GetString(USWPrepMasterLet.StComm1)

def Comm2_Calculation():
    ReturnVal = GetString(USWPrepMasterLet.StComm2)

def Comm3_Calculation():
    ReturnVal = GetString(USWPrepMasterLet.StComm3)

def Comm4_Calculation():
    ReturnVal = GetString(USWPrepMasterLet.StComm4)

def Comm5_Calculation():
    ReturnVal = GetString(USWPrepMasterLet.StComm5)

def Comm6_Calculation():
    ReturnVal = GetString(USWPrepMasterLet.StComm6)

def Date_Calculation():
    ReturnVal = GetString(USWPrepCLtr.Date)

def EFAccept_Calculation():
    if GetBool(IAWPrepCLtr.EFRet) == True:
        if GetBool(USWPrepCLtr.Transmit) == True:
            ReturnVal = 0
        elif GetBool(USWPrepCLtr.WasTran) == True:
            ReturnVal = 0
        elif GetBool(USWPrepCLtr.F8879) == True:
            ReturnVal = 0
        else:
            ReturnVal = 1
    else:
        ReturnVal = 0

def EFDate_Calculation():
    ReturnVal = GetString(IAWPrepCLtr.StSubmitDate)

def EFRet_Calculation():
    if GetBool(IAWPrepCLtr.PaperRet) == True:
        ReturnVal = 0
    else:
        ReturnVal = 1

def EFTrans_Calculation():
    if GetBool(IAWPrepCLtr.EFRet) == True:
        if GetBool(USWPrepCLtr.Transmit) == True:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def EFWasTran_Calculation():
    if GetBool(IAWPrepCLtr.EFRet) == True:
        if GetBool(USWPrepCLtr.WasTran) == True:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def EstInfo_Calculation():
    if GetBool(IAWPrepCLtr.NEst) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetBool(IAFilingInst.EstInfo)

def Exist_Calculation():
    ReturnVal = 1

def Names_Calculation():
    ReturnVal = GetString(USWPrepCLtr.Names)

def NEst_Calculation():
    if GetBool(IAEstimates.Print, 1) == False and GetBool(IAEstimates.Print, 2) == False:
        ReturnVal = 1
    else:
        ReturnVal = 0

def PaperAdd1_Calculation():
    if GetBool(IAWPrepCLtr.PaperRet) == True:
        ReturnVal = GetString(IAFilingInst.IRSAdd1) + '<br>' + GetString(IAFilingInst.IRSAdd2) + '<br>' + GetString(IAFilingInst.IRSAdd3)
    elif GetBool(IAWPrepCLtr.EFRet) == True and GetNumber(IA1040V.PrVou) == 1:
        ReturnVal = GetString(IAFilingInst.IRSAdd1) + '<br>' + GetString(IAFilingInst.IRSAdd2) + '<br>' + GetString(IAFilingInst.IRSAdd3)
    else:
        ReturnVal = ''

def PaperRet_Calculation():
    if GetBool(USWEFQual.QualifiesForEF) == False:
        ReturnVal = 1
    elif GetBool(IAWEFQual.NotQualifyEF) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

def PrepPaymentDate_Calculation():
    ReturnVal = GetVerboseDate(GetDate(IAEFWksht.EFEFWDate))

def Refund_Calculation():
    ReturnVal = GetBool(USWPrepCLtr.Refund)

def Ret1_Calculation():
    if GetBool(IAWPrepCLtr.EFRet) == True:
        ReturnVal = 'Please find enclosed a copy of your ' + YearString + ' Iowa income tax return for your records.'
    else:
        ReturnVal = 'Please find enclosed your ' + YearString + ' Iowa income tax return as well as a copy for your records.'

def Ret2_Calculation():
    if GetBool(IAWPrepCLtr.EFRet) == True and GetBool(USWPrepCLtr.NA) == True:
        ReturnVal = 'Your Iowa return was electronically transmitted to the Iowa Department of Revenue;'
    elif GetBool(IAWPrepCLtr.EFWasTran) == True:
        ReturnVal = 'Your Iowa return was electronically transmitted to the Iowa Department of Revenue on ' + GetString(IAWPrepCLtr.VerbEFDate) + ';'
    elif GetBool(IAWPrepCLtr.EFAccept) == True:
        ReturnVal = 'Your Iowa return was electronically filed and accepted by the Iowa Department of Revenue on ' + GetString(IAWPrepCLtr.VerbEFDate) + ';'
    elif GetBool(IAWPrepCLtr.EFTrans) == True:
        ReturnVal = 'Your Iowa return will be electronically transmitted to the Iowa Department of Revenue on ' + GetString(IAWPrepCLtr.VerbEFDate) + ';'
    elif GetBool(IAWPrepCLtr.EFRet) == True:
        ReturnVal = 'Your Iowa return will be electronically transmitted to the Iowa Department of Revenue;'
    else:
        ReturnVal = 'Your Iowa return is due ' + GetString(IAWPrepCLtr.VerbStDate) + '.'

def Ret3_Calculation():
    if GetBool(IAWPrepCLtr.EFRet) == True:
        ReturnVal = 'therefore, do not mail your Iowa Form 1040 to the Iowa Department of Revenue.'
    else:
        ReturnVal = 'Please sign and date your Iowa Form 1040.'

def Ret3a_Calculation():
    if GetBool(IAWPrepCLtr.PaperRet) == True and GetNumber(IA1040V.PrVou) == 1:
        ReturnVal = 'Mail your Iowa Form 1040, Iowa payment voucher, payment and required attachments to:'
    elif GetBool(IAWPrepCLtr.PaperRet) == True:
        ReturnVal = 'Mail your Iowa Form 1040 and required attachments to:'
    elif GetBool(IAWPrepCLtr.EFRet) == True and GetNumber(IA1040V.PrVou) == 1 and GetDate(IAWPrepCLtr.Date) > GetDate(IAWPrepCLtr.StDueDate):
        ReturnVal = 'Mail your payment and Iowa payment voucher (Form IA 1040-V) to:'
    elif GetBool(IAWPrepCLtr.EFRet) == True and GetNumber(IA1040V.PrVou) == 1:
        ReturnVal = 'Mail your payment and Iowa payment voucher (Form IA 1040-V) by ' + GetString(IAWPrepCLtr.VerbStDate) + ' to:'
    else:
        ReturnVal = ''

def Ret4_Calculation():
    ReturnVal = GetString(IAWPrepCLtr.PaperAdd1)

def Ret7_Calculation():
    if GetCurrency(IAF1040.RefBalDue) < 0:
        ReturnVal = 'The amount you owe on your Iowa return is '
    else:
        ReturnVal = 'The amount you overpaid on your Iowa return is '

def Ret7Amount_Calculation():
    if GetCurrency(IAF1040.RefBalDue) < 0:
        ReturnVal = GetCurrency(IAF1040.TotDue)
    else:
        ReturnVal = GetCurrency(IAF1040.OVerPaid)

def Ret8_Calculation():
    if GetBool(IAWPrepCLtr.EFRet) == True and GetCurrency(IAF1040.RefBalDue) < 0 and GetString(IAEFWksht.EFDDCode) == '2':
        ReturnVal = 'Your payment is scheduled to be withdrawn from your bank account on ' + GetString(IAWPrepCLtr.PrepPaymentDate) + '.'
    elif GetCurrency(IAF1040.RefBalDue) < 0:
        ReturnVal = 'Make your check or money order payable to \' Treasurer - State of Iowa \'.'
    else:
        ReturnVal = 'The amount of overpayment applied to your ' + NextYearString + ' estimates is '

def Ret8Amount_Calculation():
    ReturnVal = GetCurrency(IARequired.TotApplied)

def Ret8Trig_Calculation():
    if GetCurrency(IAF1040.RefBalDue) < 0:
        ReturnVal = 0
    else:
        ReturnVal = 1

def Ret9_Calculation():
    # balance due
    if GetBool(IAWPrepCLtr.EFRet) == True and GetString(IAEFWksht.EFDDCode) == '2':
        ReturnVal = ''
    elif GetCurrency(IAF1040.RefBalDue) < 0:
        ReturnVal = 'Write \'' + YearString + ' Form 1040\' on your check.'
        # refund
    elif GetBool(IAWPrepCLtr.EFRet) == True and GetBool(IAWPrepCLtr.Refund) == True and GetBool(IAEFWksht.PrepBPTrans) == True:
        ReturnVal = 'The amount to be refunded to you is '
    elif GetBool(IAWPrepCLtr.EFRet) == True and GetBool(IAWPrepCLtr.Refund) == True and GetString(IAEFWksht.EFDDCode) == '1':
        ReturnVal = 'The amount to be refunded to you by direct deposit is '
    elif GetBool(IAWPrepCLtr.Refund) == True and GetCurrency(IAF1040.Refund) > 0 and Trim(GetString(IAF1040.ActNum)) != '':
        ReturnVal = 'The amount to be refunded to you by direct deposit is '
    elif GetBool(IAWPrepCLtr.Refund) == True and GetCurrency(IAF1040.Refund) > 0:
        ReturnVal = 'The amount to be refunded to you by paper check is '
    else:
        ReturnVal = 'The amount to be refunded to you is '

def Ret9Amount_Calculation():
    ReturnVal = GetCurrency(IAF1040.Refund)

def StateEF_Calculation():
    TempStr = String()

    TempCount = Long()

    TempHold = Long()

    Submission = String()
    TempStr = GetString(USWEFOptions.EFSubmissionHistory)
    TempCount = 1
    TempHold = 0
    Submission = GetParam(TempStr, TempCount, '|')
    while Submission != '':
        if GetParam(Submission, 1, ';') == 'IA' and GetParam(Submission, 2, ';') == '0':
            ReturnVal = 1
        TempCount = TempCount + 1
        Submission = GetParam(TempStr, TempCount, '|')
    ReturnVal = 0

def StDueDate_Calculation():
    ReturnVal = datetime.datetime(4, 30, 2019)

def StSubmitDate_Calculation():
    TempStr = String()

    TempCount = Long()

    TempHold = Long()

    Submission = String()
    TempStr = GetString(USWEFOptions.EFSubmissionHistory)
    TempCount = 1
    TempHold = 0
    Submission = GetParam(TempStr, TempCount, '|')
    while Submission != '':
        if GetParam(Submission, 1, ';') == 'IA' and GetParam(Submission, 2, ';') == '0':
            ReturnVal = GetParam(Submission, 4, ';')
        TempCount = TempCount + 1
        Submission = GetParam(TempStr, TempCount, '|')
    ReturnVal = ''

def VerbDate_Calculation():
    ReturnVal = GetVerboseDate(GetDate(IAWPrepCLtr.Date))

def VerbEFDate_Calculation():
    ReturnVal = GetVerboseDate(GetDate(IAWPrepCLtr.EFDate))

def VerbStDate_Calculation():
    ReturnVal = GetVerboseDate(GetDate(IAWPrepCLtr.StDueDate))

def YEst_Calculation():
    if GetBool(IAEstimates.Print, 1) == True or GetBool(IAEstimates.Print, 2) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

