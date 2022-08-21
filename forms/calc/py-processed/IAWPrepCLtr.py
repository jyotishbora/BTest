from forms.out import IA1040V
from forms.out import IAEFWKSHT
from forms.out import IAESTIMATES
from forms.out import IAF1040
from forms.out import IAFILINGINST
from forms.out import IAREQUIRED
from forms.out import IAWEFQUAL
from forms.out import IAWPREPCLTR
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *
import datetime



def AddComm1_Calculation():
    if trim(get_string(IAWPREPCLTR.Comm1)) != '':
        return 1
    else:
        return 0

def AddComm2_Calculation():
    if trim(get_string(IAWPREPCLTR.Comm2)) != '':
        return 1
    else:
        return 0

def AddComm3_Calculation():
    if trim(get_string(IAWPREPCLTR.Comm3)) != '':
        return 1
    else:
        return 0

def AddComm4_Calculation():
    if trim(get_string(IAWPREPCLTR.Comm4)) != '':
        return 1
    else:
        return 0

def AddComm5_Calculation():
    if trim(get_string(IAWPREPCLTR.Comm5)) != '':
        return 1
    else:
        return 0

def AddComm6_Calculation():
    if trim(get_string(IAWPREPCLTR.Comm6)) != '':
        return 1
    else:
        return 0

def C1EstInfo_Calculation():
    if get_bool(IAWPREPCLTR.NEst) == True:
        return 0
    else:
        return get_bool(IAFILINGINST.C1EstInfo)

def C2EstInfo_Calculation():
    if get_bool(IAWPREPCLTR.NEst) == True:
        return 0
    else:
        return get_bool(IAFILINGINST.C2EstInfo)

def Comm1_Calculation():
    return get_string(USWPrepMasterLet.StComm1)

def Comm2_Calculation():
    return get_string(USWPrepMasterLet.StComm2)

def Comm3_Calculation():
    return get_string(USWPrepMasterLet.StComm3)

def Comm4_Calculation():
    return get_string(USWPrepMasterLet.StComm4)

def Comm5_Calculation():
    return get_string(USWPrepMasterLet.StComm5)

def Comm6_Calculation():
    return get_string(USWPrepMasterLet.StComm6)

def Date_Calculation():
    return get_string(USWPrepCLtr.Date)

def EFAccept_Calculation():
    if get_bool(IAWPREPCLTR.EFRet) == True:
        if get_bool(USWPrepCLtr.Transmit) == True:
            return 0
        elif get_bool(USWPrepCLtr.WasTran) == True:
            return 0
        elif get_bool(USWPrepCLtr.F8879) == True:
            return 0
        else:
            return 1
    else:
        return 0

def EFDate_Calculation():
    return get_string(IAWPREPCLTR.StSubmitDate)

def EFRet_Calculation():
    if get_bool(IAWPREPCLTR.PaperRet) == True:
        return 0
    else:
        return 1

def EFTrans_Calculation():
    if get_bool(IAWPREPCLTR.EFRet) == True:
        if get_bool(USWPrepCLtr.Transmit) == True:
            return 1
        else:
            return 0
    else:
        return 0

def EFWasTran_Calculation():
    if get_bool(IAWPREPCLTR.EFRet) == True:
        if get_bool(USWPrepCLtr.WasTran) == True:
            return 1
        else:
            return 0
    else:
        return 0

def EstInfo_Calculation():
    if get_bool(IAWPREPCLTR.NEst) == True:
        return 0
    else:
        return get_bool(IAFILINGINST.EstInfo)

def Exist_Calculation():
    return 1

def Names_Calculation():
    return get_string(USWPrepCLtr.Names)

def NEst_Calculation():
    if get_bool(IAESTIMATES.Print, 1) == False and get_bool(IAESTIMATES.Print, 2) == False:
        return 1
    else:
        return 0

def PaperAdd1_Calculation():
    if get_bool(IAWPREPCLTR.PaperRet) == True:
        return get_string(IAFILINGINST.IRSAdd1) + '<br>' + get_string(IAFILINGINST.IRSAdd2) + '<br>' + get_string(IAFILINGINST.IRSAdd3)
    elif get_bool(IAWPREPCLTR.EFRet) == True and get_number(IA1040V.PrVou) == 1:
        return get_string(IAFILINGINST.IRSAdd1) + '<br>' + get_string(IAFILINGINST.IRSAdd2) + '<br>' + get_string(IAFILINGINST.IRSAdd3)
    else:
        return ''

def PaperRet_Calculation():
    if get_bool(USWEFQual.QualifiesForEF) == False:
        return 1
    elif get_bool(IAWEFQUAL.NotQualifyEF) == True:
        return 1
    else:
        return 0

def PrepPaymentDate_Calculation():
    return GetVerboseDate(GetDate(IAEFWKSHT.EFEFWDate))

def Refund_Calculation():
    return get_bool(USWPrepCLtr.Refund)

def Ret1_Calculation():
    if get_bool(IAWPREPCLTR.EFRet) == True:
        return 'Please find enclosed a copy of your ' + YearString + ' Iowa income tax return for your records.'
    else:
        return 'Please find enclosed your ' + YearString + ' Iowa income tax return as well as a copy for your records.'

def Ret2_Calculation():
    if get_bool(IAWPREPCLTR.EFRet) == True and get_bool(USWPrepCLtr.NA) == True:
        return 'Your Iowa return was electronically transmitted to the Iowa Department of Revenue;'
    elif get_bool(IAWPREPCLTR.EFWasTran) == True:
        return 'Your Iowa return was electronically transmitted to the Iowa Department of Revenue on ' + get_string(IAWPREPCLTR.VerbEFDate) + ';'
    elif get_bool(IAWPREPCLTR.EFAccept) == True:
        return 'Your Iowa return was electronically filed and accepted by the Iowa Department of Revenue on ' + get_string(IAWPREPCLTR.VerbEFDate) + ';'
    elif get_bool(IAWPREPCLTR.EFTrans) == True:
        return 'Your Iowa return will be electronically transmitted to the Iowa Department of Revenue on ' + get_string(IAWPREPCLTR.VerbEFDate) + ';'
    elif get_bool(IAWPREPCLTR.EFRet) == True:
        return 'Your Iowa return will be electronically transmitted to the Iowa Department of Revenue;'
    else:
        return 'Your Iowa return is due ' + get_string(IAWPREPCLTR.VerbStDate) + '.'

def Ret3_Calculation():
    if get_bool(IAWPREPCLTR.EFRet) == True:
        return 'therefore, do not mail your Iowa Form 1040 to the Iowa Department of Revenue.'
    else:
        return 'Please sign and date your Iowa Form 1040.'

def Ret3a_Calculation():
    if get_bool(IAWPREPCLTR.PaperRet) == True and get_number(IA1040V.PrVou) == 1:
        return 'Mail your Iowa Form 1040, Iowa payment voucher, payment and required attachments to:'
    elif get_bool(IAWPREPCLTR.PaperRet) == True:
        return 'Mail your Iowa Form 1040 and required attachments to:'
    elif get_bool(IAWPREPCLTR.EFRet) == True and get_number(IA1040V.PrVou) == 1 and GetDate(IAWPREPCLTR.Date) > GetDate(IAWPREPCLTR.StDueDate):
        return 'Mail your payment and Iowa payment voucher (Form IA 1040-V) to:'
    elif get_bool(IAWPREPCLTR.EFRet) == True and get_number(IA1040V.PrVou) == 1:
        return 'Mail your payment and Iowa payment voucher (Form IA 1040-V) by ' + get_string(IAWPREPCLTR.VerbStDate) + ' to:'
    else:
        return ''

def Ret4_Calculation():
    return get_string(IAWPREPCLTR.PaperAdd1)

def Ret7_Calculation():
    if get_currency(IAF1040.RefBalDue) < 0:
        return 'The amount you owe on your Iowa return is '
    else:
        return 'The amount you overpaid on your Iowa return is '

def Ret7Amount_Calculation():
    if get_currency(IAF1040.RefBalDue) < 0:
        return get_currency(IAF1040.TotDue)
    else:
        return get_currency(IAF1040.OVerPaid)

def Ret8_Calculation():
    if get_bool(IAWPREPCLTR.EFRet) == True and get_currency(IAF1040.RefBalDue) < 0 and get_string(IAEFWKSHT.EFDDCode) == '2':
        return 'Your payment is scheduled to be withdrawn from your bank account on ' + get_string(IAWPREPCLTR.PrepPaymentDate) + '.'
    elif get_currency(IAF1040.RefBalDue) < 0:
        return 'Make your check or money order payable to \' Treasurer - State of Iowa \'.'
    else:
        return 'The amount of overpayment applied to your ' + NextYearString + ' estimates is '

def Ret8Amount_Calculation():
    return get_currency(IAREQUIRED.TotApplied)

def Ret8Trig_Calculation():
    if get_currency(IAF1040.RefBalDue) < 0:
        return 0
    else:
        return 1

def Ret9_Calculation():
    # balance due
    if get_bool(IAWPREPCLTR.EFRet) == True and get_string(IAEFWKSHT.EFDDCode) == '2':
        return ''
    elif get_currency(IAF1040.RefBalDue) < 0:
        return 'Write \'' + YearString + ' Form 1040\' on your check.'
        # refund
    elif get_bool(IAWPREPCLTR.EFRet) == True and get_bool(IAWPREPCLTR.Refund) == True and get_bool(IAEFWKSHT.PrepBPTrans) == True:
        return 'The amount to be refunded to you is '
    elif get_bool(IAWPREPCLTR.EFRet) == True and get_bool(IAWPREPCLTR.Refund) == True and get_string(IAEFWKSHT.EFDDCode) == '1':
        return 'The amount to be refunded to you by direct deposit is '
    elif get_bool(IAWPREPCLTR.Refund) == True and get_currency(IAF1040.Refund) > 0 and trim(get_string(IAF1040.ActNum)) != '':
        return 'The amount to be refunded to you by direct deposit is '
    elif get_bool(IAWPREPCLTR.Refund) == True and get_currency(IAF1040.Refund) > 0:
        return 'The amount to be refunded to you by paper check is '
    else:
        return 'The amount to be refunded to you is '

def Ret9Amount_Calculation():
    return get_currency(IAF1040.Refund)

def StateEF_Calculation():
    TempStr = String()

    TempCount = Long()

    TempHold = Long()

    Submission = String()
    TempStr = get_string(USWEFOptions.EFSubmissionHistory)
    TempCount = 1
    TempHold = 0
    Submission = GetParam(TempStr, TempCount, '|')
    while Submission != '':
        if GetParam(Submission, 1, ';') == 'IA' and GetParam(Submission, 2, ';') == '0':
            return 1
        TempCount = TempCount + 1
        Submission = GetParam(TempStr, TempCount, '|')
    return 0

def StDueDate_Calculation():
    return datetime.datetime(4, 30, 2019)

def StSubmitDate_Calculation():
    TempStr = String()

    TempCount = Long()

    TempHold = Long()

    Submission = String()
    TempStr = get_string(USWEFOptions.EFSubmissionHistory)
    TempCount = 1
    TempHold = 0
    Submission = GetParam(TempStr, TempCount, '|')
    while Submission != '':
        if GetParam(Submission, 1, ';') == 'IA' and GetParam(Submission, 2, ';') == '0':
            return GetParam(Submission, 4, ';')
        TempCount = TempCount + 1
        Submission = GetParam(TempStr, TempCount, '|')
    return ''

def VerbDate_Calculation():
    return GetVerboseDate(GetDate(IAWPREPCLTR.Date))

def VerbEFDate_Calculation():
    return GetVerboseDate(GetDate(IAWPREPCLTR.EFDate))

def VerbStDate_Calculation():
    return GetVerboseDate(GetDate(IAWPREPCLTR.StDueDate))

def YEst_Calculation():
    if get_bool(IAESTIMATES.Print, 1) == True or get_bool(IAESTIMATES.Print, 2) == True:
        return 1
    else:
        return 0


