from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Credit_Calculation(Index):
    if Trim(GetString(IATuition.DepName(Index))) != '':
        ReturnVal = CDollar(CDbl(MinValue(GetCurrency(IATuition.Expenses(Index)), Decimal("1000"))) * 0.25)
    else:
        ReturnVal = 0

def DepName_Calculation(Index):
    count = Integer()

    Hold = String()
    count = 0
    Hold = ''
    if GetNumber(IAAddDep.FDepAge(0)) > 0 and GetNumber(IAAddDep.FDepAge(0)) < 20:
        if Index == count:
            Hold = GetString(IAAddDep.FDepName(0)) + ' ' + GetString(IAAddDep.FDepLast(0))
            count = 99
        else:
            count = count + 1
    if GetNumber(IAAddDep.FDepAge(1)) > 0 and GetNumber(IAAddDep.FDepAge(1)) < 20:
        if Index == count:
            Hold = GetString(IAAddDep.FDepName(1)) + ' ' + GetString(IAAddDep.FDepLast(1))
            count = 99
        else:
            count = count + 1
    if GetNumber(IAAddDep.FDepAge(2)) > 0 and GetNumber(IAAddDep.FDepAge(2)) < 20:
        if Index == count:
            Hold = GetString(IAAddDep.FDepName(2)) + ' ' + GetString(IAAddDep.FDepLast(2))
            count = 99
        else:
            count = count + 1
    if GetNumber(IAAddDep.FDepAge(3)) > 0 and GetNumber(IAAddDep.FDepAge(3)) < 20:
        if Index == count:
            Hold = GetString(IAAddDep.FDepName(3)) + ' ' + GetString(IAAddDep.FDepLast(3))
            count = 99
        else:
            count = count + 1
    if GetNumber(IAAddDep.FDepAge(4)) > 0 and GetNumber(IAAddDep.FDepAge(4)) < 20:
        if Index == count:
            Hold = GetString(IAAddDep.FDepName(4)) + ' ' + GetString(IAAddDep.FDepLast(4))
            count = 99
        else:
            count = count + 1
    if GetNumber(IAAddDep.FDepAge(5)) > 0 and GetNumber(IAAddDep.FDepAge(5)) < 20:
        if Index == count:
            Hold = GetString(IAAddDep.FDepName(5)) + ' ' + GetString(IAAddDep.FDepLast(5))
            count = 99
        else:
            count = count + 1
    if GetNumber(IAAddDep.FDepAge(6)) > 0 and GetNumber(IAAddDep.FDepAge(6)) < 20:
        if Index == count:
            Hold = GetString(IAAddDep.FDepName(6)) + ' ' + GetString(IAAddDep.FDepLast(6))
            count = 99
        else:
            count = count + 1
    if GetNumber(IAAddDep.FDepAge(7)) > 0 and GetNumber(IAAddDep.FDepAge(7)) < 20:
        if Index == count:
            Hold = GetString(IAAddDep.FDepName(7)) + ' ' + GetString(IAAddDep.FDepLast(7))
            count = 99
        else:
            count = count + 1
    if GetNumber(IAAddDep.FDepAge(8)) > 0 and GetNumber(IAAddDep.FDepAge(8)) < 20:
        if Index == count:
            Hold = GetString(IAAddDep.FDepName(8)) + ' ' + GetString(IAAddDep.FDepLast(8))
            count = 99
        else:
            count = count + 1
    if GetNumber(IAAddDep.FDepAge(9)) > 0 and GetNumber(IAAddDep.FDepAge(9)) < 20:
        if Index == count:
            Hold = GetString(IAAddDep.FDepName(9)) + ' ' + GetString(IAAddDep.FDepLast(9))
            count = 99
        else:
            count = count + 1
    if GetNumber(IAAddDep.FDepAge(10)) > 0 and GetNumber(IAAddDep.FDepAge(10)) < 20:
        if Index == count:
            Hold = GetString(IAAddDep.FDepName(10)) + ' ' + GetString(IAAddDep.FDepLast(10))
            count = 99
        else:
            count = count + 1
    if GetNumber(IAAddDep.FDepAge(11)) > 0 and GetNumber(IAAddDep.FDepAge(11)) < 20:
        if Index == count:
            Hold = GetString(IAAddDep.FDepName(11)) + ' ' + GetString(IAAddDep.FDepLast(11))
            count = 99
        else:
            count = count + 1
    if GetNumber(IAAddDep.FDepAge(12)) > 0 and GetNumber(IAAddDep.FDepAge(12)) < 20:
        if Index == count:
            Hold = GetString(IAAddDep.FDepName(12)) + ' ' + GetString(IAAddDep.FDepLast(12))
            count = 99
        else:
            count = count + 1
    if GetNumber(IAAddDep.FDepAge(13)) > 0 and GetNumber(IAAddDep.FDepAge(13)) < 20:
        if Index == count:
            Hold = GetString(IAAddDep.FDepName(13)) + ' ' + GetString(IAAddDep.FDepLast(13))
            count = 99
        else:
            count = count + 1
    if GetNumber(IAAddDep.FDepAge(14)) > 0 and GetNumber(IAAddDep.FDepAge(14)) < 20:
        if Index == count:
            Hold = GetString(IAAddDep.FDepName(14)) + ' ' + GetString(IAAddDep.FDepLast(14))
            count = 99
        else:
            count = count + 1
    ReturnVal = Hold

def Description_Calculation():
    ReturnVal = CStr(GetCurrency(IATuition.TotCR))

def Names_Calculation():
    ReturnVal = GetString(IARequired.CombNames)

def Spouse_Calculation(Index):
    if Trim(GetString(IATuition.DepName(Index))) != '':
        if GetBool(IAF1040.CombMFS) == False:
            ReturnVal = 0
        elif GetNumber(IAF1040.DC2) == 0:
            ReturnVal = 0
        elif GetNumber(IAF1040.DC2) > Index:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

def STuit_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 15:
        if GetBool(IATuition.Spouse(count)) == True:
            SubTot = SubTot + GetCurrency(IATuition.Credit(count))
        else:
            SubTot = SubTot
        count = count + 1
    if GetBool(IAF1040.CombMFS) == True and GetNumber(IAF1040.DC2) > 0:
        ReturnVal = SubTot
    else:
        ReturnVal = 0

def Taxpayer_Calculation(Index):
    if Trim(GetString(IATuition.DepName(Index))) != '' and GetBool(IATuition.Spouse(Index)) == False:
        ReturnVal = 1
    else:
        ReturnVal = 0

def TotCR_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 15:
        SubTot = SubTot + GetCurrency(IATuition.Credit(count))
        count = count + 1
    ReturnVal = SubTot

def TotExp_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 15:
        SubTot = SubTot + GetCurrency(IATuition.Expenses(count))
        count = count + 1
    ReturnVal = SubTot

def TTuit_Calculation():
    ReturnVal = GetCurrency(IATuition.TotCR) - GetCurrency(IATuition.STuit)

