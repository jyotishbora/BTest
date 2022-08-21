from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Attach1_Calculation():
    ReturnVal = 'Please include a complete copy of your federal return. '

def Attach2_Calculation():
    if GetBool(IAFilingInst.AttWHStmt) == True:
        ReturnVal = 'Please attach state copies of W-2(s), W-2G(s) and/or 1099(s) showing Iowa tax withheld.'
    else:
        ReturnVal = ''

def Attach3_Calculation():
    if GetNumber(IAFilingInst.OtherState) > 0:
        ReturnVal = 'Please attach a copy of the other state return for Schedule IA 130.'
    else:
        ReturnVal = ''

def Attach4_Calculation():
    if GetBool(IA148.Print) == True or GetBool(IA148Sp.Print) == True:
        ReturnVal = 'Please attach all supporting forms for the credits claimed on Schedule IA 148.'
    else:
        ReturnVal = ''

def AttWHStmt_Calculation():
    if GetCurrency(IAF1040.AIATaxWith) > 0:
        ReturnVal = 1
    elif GetCurrency(IAF1040.BIATaxWith) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def C1Est1_Calculation():
    ReturnVal = GetBool(IAEstimates.EstPay1, 1)

def C1Est2_Calculation():
    ReturnVal = GetBool(IAEstimates.EstPay2, 1)

def C1Est3_Calculation():
    ReturnVal = GetBool(IAEstimates.EstPay3, 1)

def C1Est4_Calculation():
    ReturnVal = GetBool(IAEstimates.EstPay4, 1)

def C1EstInfo_Calculation():
    if GetBool(IAEstimates.Print, 1) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

def C1EstInfoDirDeb_Calculation():
    if GetBool(IAEstimates.Print, 1) == True and GetBool(IAEstimates.EstEFW, 1) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

def C1Owner_Calculation():
    if GetBool(IAEstimates.Print, 1) == True and GetBool(IAEstimates.Print, 2) == True:
        ReturnVal = ' for ' + GetString(IAEstimates.Owner, 1)
    else:
        ReturnVal = ''

def C1Q1_Calculation():
    ReturnVal = GetCurrency(IAEstimates.V1PayAmt1, 1)

def C1Q1WithDate_Calculation():
    ReturnVal = GetVerboseDate(GetDate(IAEstimates.Est1Date, 1))

def C1Q2_Calculation():
    ReturnVal = GetCurrency(IAEstimates.V2PayAmt1, 1)

def C1Q2WithDate_Calculation():
    ReturnVal = GetVerboseDate(GetDate(IAEstimates.Est2Date, 1))

def C1Q3_Calculation():
    ReturnVal = GetCurrency(IAEstimates.V3PayAmt1, 1)

def C1Q3WithDate_Calculation():
    ReturnVal = GetVerboseDate(GetDate(IAEstimates.Est3Date, 1))

def C1Q4_Calculation():
    ReturnVal = GetCurrency(IAEstimates.V4PayAmt1, 1)

def C1Q4WithDate_Calculation():
    ReturnVal = GetVerboseDate(GetDate(IAEstimates.Est4Date, 1))

def C2Est1_Calculation():
    ReturnVal = GetBool(IAEstimates.EstPay1, 2)

def C2Est2_Calculation():
    ReturnVal = GetBool(IAEstimates.EstPay2, 2)

def C2Est3_Calculation():
    ReturnVal = GetBool(IAEstimates.EstPay3, 2)

def C2Est4_Calculation():
    ReturnVal = GetBool(IAEstimates.EstPay4, 2)

def C2EstInfo_Calculation():
    if GetBool(IAEstimates.Print, 2) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

def C2EstInfoDirDeb_Calculation():
    if GetBool(IAEstimates.Print, 2) == True and GetBool(IAEstimates.EstEFW, 2) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

def C2Owner_Calculation():
    if GetBool(IAEstimates.Print, 1) == True and GetBool(IAEstimates.Print, 2) == True:
        ReturnVal = ' for ' + GetString(IAEstimates.Owner, 2)
    else:
        ReturnVal = ''

def C2Q1_Calculation():
    ReturnVal = GetCurrency(IAEstimates.V1PayAmt1, 2)

def C2Q1WithDate_Calculation():
    ReturnVal = GetVerboseDate(GetDate(IAEstimates.Est1Date, 2))

def C2Q2_Calculation():
    ReturnVal = GetCurrency(IAEstimates.V2PayAmt1, 2)

def C2Q2WithDate_Calculation():
    ReturnVal = GetVerboseDate(GetDate(IAEstimates.Est2Date, 2))

def C2Q3_Calculation():
    ReturnVal = GetCurrency(IAEstimates.V3PayAmt1, 2)

def C2Q3WithDate_Calculation():
    ReturnVal = GetVerboseDate(GetDate(IAEstimates.Est3Date, 2))

def C2Q4_Calculation():
    ReturnVal = GetCurrency(IAEstimates.V4PayAmt1, 2)

def C2Q4WithDate_Calculation():
    ReturnVal = GetVerboseDate(GetDate(IAEstimates.Est4Date, 2))

def DueDate_Calculation():
    ReturnVal = 'April 30, 2019'

def EitherDirDeb_Calculation():
    if GetNumber(IAFilingInst.C1EstInfoDirDeb) == 1 or GetNumber(IAFilingInst.C2EstInfoDirDeb) == 1:
        ReturnVal = 1
    else:
        ReturnVal = 0

def EstAdd1_Calculation():
    ReturnVal = 'Iowa Department of Revenue<br>PO Box 10466 <br>Des Moines, IA 50306-0466'

def EstInfo_Calculation():
    if GetBool(IAFilingInst.C1EstInfo) == True:
        ReturnVal = 1
    elif GetBool(IAFilingInst.C2EstInfo) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

def IRSAdd1_Calculation():
    ReturnVal = 'Iowa Income Tax Document Processing'

def IRSAdd2_Calculation():
    ReturnVal = 'PO Box 9187'

def IRSAdd3_Calculation():
    ReturnVal = 'Des Moines, IA  50306-9187'

def Names_Calculation():
    ReturnVal = GetString(IARequired.CombNames)

def OtherState_Calculation():
    if GetCurrency(IAF1040.AOutState) > 0 or GetCurrency(IAF1040.BOutState) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Pay1_Calculation():
    if GetCurrency(IAF1040.RefBalDue) < 0:
        ReturnVal = 'The balance due on your Iowa return is ' + GetString(IAF1040.TotDue)
    else:
        ReturnVal = 'The overpayment on your return is ' + GetString(IAF1040.OVerPaid)

def Pay2_Calculation():
    if GetCurrency(IAF1040.RefBalDue) < 0:
        ReturnVal = 'Make your check payable to: Treasurer, State of Iowa'
    else:
        ReturnVal = 'The amount of overpayment applied to your 2019 estimates is ' + GetString(IARequired.TotApplied)

def Pay3_Calculation():
    if GetCurrency(IAF1040.RefBalDue) < 0:
        ReturnVal = 'Write \'2018 Form 1040\' on your check.'
    else:
        ReturnVal = 'The amount to be refunded to you is ' + GetString(IAF1040.Refund) + '.'

def Pay4_Calculation():
    if GetCurrency(IAF1040.RefBalDue) <= 0:
        ReturnVal = ''
    elif Trim(GetString(IAF1040.ActNum)) != '':
        ReturnVal = 'You have elected to receive your refund via direct deposit.'
    else:
        ReturnVal = 'You have elected to receive your refund on a paper check.'

def Q1Date_Calculation():
    ReturnVal = 'April 30, 2019'

def Q2Date_Calculation():
    ReturnVal = 'July 1, 2019'

def Q3Date_Calculation():
    ReturnVal = 'September 30, 2019'

def Q4Date_Calculation():
    ReturnVal = 'January 31, 2020'

