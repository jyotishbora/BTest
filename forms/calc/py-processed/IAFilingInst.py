from forms.out import IA148SP
from forms.out import IAESTIMATES
from forms.out import IAF1040
from forms.out import IAFILINGINST
from forms.out import IAREQUIRED
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Attach1_Calculation():
    return 'Please include a complete copy of your federal return. '

def Attach2_Calculation():
    if get_bool(IAFILINGINST.AttWHStmt) == True:
        return 'Please attach state copies of W-2(s), W-2G(s) and/or 1099(s) showing Iowa tax withheld.'
    else:
        return ''

def Attach3_Calculation():
    if get_number(IAFILINGINST.OtherState) > 0:
        return 'Please attach a copy of the other state return for Schedule IA 130.'
    else:
        return ''

def Attach4_Calculation():
    if get_bool(IA148.Print) == True or get_bool(IA148SP.Print) == True:
        return 'Please attach all supporting forms for the credits claimed on Schedule IA 148.'
    else:
        return ''

def AttWHStmt_Calculation():
    if get_currency(IAF1040.AIATaxWith) > 0:
        return 1
    elif get_currency(IAF1040.BIATaxWith) > 0:
        return 1
    else:
        return 0

def C1Est1_Calculation():
    return get_bool(IAESTIMATES.EstPay1, 1)

def C1Est2_Calculation():
    return get_bool(IAESTIMATES.EstPay2, 1)

def C1Est3_Calculation():
    return get_bool(IAESTIMATES.EstPay3, 1)

def C1Est4_Calculation():
    return get_bool(IAESTIMATES.EstPay4, 1)

def C1EstInfo_Calculation():
    if get_bool(IAESTIMATES.Print, 1) == True:
        return 1
    else:
        return 0

def C1EstInfoDirDeb_Calculation():
    if get_bool(IAESTIMATES.Print, 1) == True and get_bool(IAESTIMATES.EstEFW, 1) == True:
        return 1
    else:
        return 0

def C1Owner_Calculation():
    if get_bool(IAESTIMATES.Print, 1) == True and get_bool(IAESTIMATES.Print, 2) == True:
        return ' for ' + get_string(IAESTIMATES.Owner, 1)
    else:
        return ''

def C1Q1_Calculation():
    return get_currency(IAESTIMATES.V1PayAmt1, 1)

def C1Q1WithDate_Calculation():
    return GetVerboseDate(GetDate(IAESTIMATES.Est1Date, 1))

def C1Q2_Calculation():
    return get_currency(IAESTIMATES.V2PayAmt1, 1)

def C1Q2WithDate_Calculation():
    return GetVerboseDate(GetDate(IAESTIMATES.Est2Date, 1))

def C1Q3_Calculation():
    return get_currency(IAESTIMATES.V3PayAmt1, 1)

def C1Q3WithDate_Calculation():
    return GetVerboseDate(GetDate(IAESTIMATES.Est3Date, 1))

def C1Q4_Calculation():
    return get_currency(IAESTIMATES.V4PayAmt1, 1)

def C1Q4WithDate_Calculation():
    return GetVerboseDate(GetDate(IAESTIMATES.Est4Date, 1))

def C2Est1_Calculation():
    return get_bool(IAESTIMATES.EstPay1, 2)

def C2Est2_Calculation():
    return get_bool(IAESTIMATES.EstPay2, 2)

def C2Est3_Calculation():
    return get_bool(IAESTIMATES.EstPay3, 2)

def C2Est4_Calculation():
    return get_bool(IAESTIMATES.EstPay4, 2)

def C2EstInfo_Calculation():
    if get_bool(IAESTIMATES.Print, 2) == True:
        return 1
    else:
        return 0

def C2EstInfoDirDeb_Calculation():
    if get_bool(IAESTIMATES.Print, 2) == True and get_bool(IAESTIMATES.EstEFW, 2) == True:
        return 1
    else:
        return 0

def C2Owner_Calculation():
    if get_bool(IAESTIMATES.Print, 1) == True and get_bool(IAESTIMATES.Print, 2) == True:
        return ' for ' + get_string(IAESTIMATES.Owner, 2)
    else:
        return ''

def C2Q1_Calculation():
    return get_currency(IAESTIMATES.V1PayAmt1, 2)

def C2Q1WithDate_Calculation():
    return GetVerboseDate(GetDate(IAESTIMATES.Est1Date, 2))

def C2Q2_Calculation():
    return get_currency(IAESTIMATES.V2PayAmt1, 2)

def C2Q2WithDate_Calculation():
    return GetVerboseDate(GetDate(IAESTIMATES.Est2Date, 2))

def C2Q3_Calculation():
    return get_currency(IAESTIMATES.V3PayAmt1, 2)

def C2Q3WithDate_Calculation():
    return GetVerboseDate(GetDate(IAESTIMATES.Est3Date, 2))

def C2Q4_Calculation():
    return get_currency(IAESTIMATES.V4PayAmt1, 2)

def C2Q4WithDate_Calculation():
    return GetVerboseDate(GetDate(IAESTIMATES.Est4Date, 2))

def DueDate_Calculation():
    return 'April 30, 2019'

def EitherDirDeb_Calculation():
    if get_number(IAFILINGINST.C1EstInfoDirDeb) == 1 or get_number(IAFILINGINST.C2EstInfoDirDeb) == 1:
        return 1
    else:
        return 0

def EstAdd1_Calculation():
    return 'Iowa Department of Revenue<br>PO Box 10466 <br>Des Moines, IA 50306-0466'

def EstInfo_Calculation():
    if get_bool(IAFILINGINST.C1EstInfo) == True:
        return 1
    elif get_bool(IAFILINGINST.C2EstInfo) == True:
        return 1
    else:
        return 0

def IRSAdd1_Calculation():
    return 'Iowa Income Tax Document Processing'

def IRSAdd2_Calculation():
    return 'PO Box 9187'

def IRSAdd3_Calculation():
    return 'Des Moines, IA  50306-9187'

def Names_Calculation():
    return get_string(IAREQUIRED.CombNames)

def OtherState_Calculation():
    if get_currency(IAF1040.AOutState) > 0 or get_currency(IAF1040.BOutState) > 0:
        return 1
    else:
        return 0

def Pay1_Calculation():
    if get_currency(IAF1040.RefBalDue) < 0:
        return 'The balance due on your Iowa return is ' + get_string(IAF1040.TotDue)
    else:
        return 'The overpayment on your return is ' + get_string(IAF1040.OVerPaid)

def Pay2_Calculation():
    if get_currency(IAF1040.RefBalDue) < 0:
        return 'Make your check payable to: Treasurer, State of Iowa'
    else:
        return 'The amount of overpayment applied to your 2019 estimates is ' + get_string(IAREQUIRED.TotApplied)

def Pay3_Calculation():
    if get_currency(IAF1040.RefBalDue) < 0:
        return 'Write \'2018 Form 1040\' on your check.'
    else:
        return 'The amount to be refunded to you is ' + get_string(IAF1040.Refund) + '.'

def Pay4_Calculation():
    if get_currency(IAF1040.RefBalDue) <= 0:
        return ''
    elif trim(get_string(IAF1040.ActNum)) != '':
        return 'You have elected to receive your refund via direct deposit.'
    else:
        return 'You have elected to receive your refund on a paper check.'

def Q1Date_Calculation():
    return 'April 30, 2019'

def Q2Date_Calculation():
    return 'July 1, 2019'

def Q3Date_Calculation():
    return 'September 30, 2019'

def Q4Date_Calculation():
    return 'January 31, 2020'


