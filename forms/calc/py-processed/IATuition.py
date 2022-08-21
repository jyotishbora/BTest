from forms.out import IAADDDEP
from forms.out import IAF1040
from forms.out import IAREQUIRED
from forms.out import IATUITION
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Credit_Calculation(Index):
    if trim(get_string(IATUITION.DepName(Index))) != '':
        return c_dollar(CDbl(min_value(get_currency(IATUITION.Expenses(Index)), Decimal("1000"))) * 0.25)
    else:
        return 0

def DepName_Calculation(Index):
    count = Integer()

    Hold = String()
    count = 0
    Hold = ''
    if get_number(IAADDDEP.FDepAge(0)) > 0 and get_number(IAADDDEP.FDepAge(0)) < 20:
        if Index == count:
            Hold = get_string(IAADDDEP.FDepName(0)) + ' ' + get_string(IAADDDEP.FDepLast(0))
            count = 99
        else:
            count = count + 1
    if get_number(IAADDDEP.FDepAge(1)) > 0 and get_number(IAADDDEP.FDepAge(1)) < 20:
        if Index == count:
            Hold = get_string(IAADDDEP.FDepName(1)) + ' ' + get_string(IAADDDEP.FDepLast(1))
            count = 99
        else:
            count = count + 1
    if get_number(IAADDDEP.FDepAge(2)) > 0 and get_number(IAADDDEP.FDepAge(2)) < 20:
        if Index == count:
            Hold = get_string(IAADDDEP.FDepName(2)) + ' ' + get_string(IAADDDEP.FDepLast(2))
            count = 99
        else:
            count = count + 1
    if get_number(IAADDDEP.FDepAge(3)) > 0 and get_number(IAADDDEP.FDepAge(3)) < 20:
        if Index == count:
            Hold = get_string(IAADDDEP.FDepName(3)) + ' ' + get_string(IAADDDEP.FDepLast(3))
            count = 99
        else:
            count = count + 1
    if get_number(IAADDDEP.FDepAge(4)) > 0 and get_number(IAADDDEP.FDepAge(4)) < 20:
        if Index == count:
            Hold = get_string(IAADDDEP.FDepName(4)) + ' ' + get_string(IAADDDEP.FDepLast(4))
            count = 99
        else:
            count = count + 1
    if get_number(IAADDDEP.FDepAge(5)) > 0 and get_number(IAADDDEP.FDepAge(5)) < 20:
        if Index == count:
            Hold = get_string(IAADDDEP.FDepName(5)) + ' ' + get_string(IAADDDEP.FDepLast(5))
            count = 99
        else:
            count = count + 1
    if get_number(IAADDDEP.FDepAge(6)) > 0 and get_number(IAADDDEP.FDepAge(6)) < 20:
        if Index == count:
            Hold = get_string(IAADDDEP.FDepName(6)) + ' ' + get_string(IAADDDEP.FDepLast(6))
            count = 99
        else:
            count = count + 1
    if get_number(IAADDDEP.FDepAge(7)) > 0 and get_number(IAADDDEP.FDepAge(7)) < 20:
        if Index == count:
            Hold = get_string(IAADDDEP.FDepName(7)) + ' ' + get_string(IAADDDEP.FDepLast(7))
            count = 99
        else:
            count = count + 1
    if get_number(IAADDDEP.FDepAge(8)) > 0 and get_number(IAADDDEP.FDepAge(8)) < 20:
        if Index == count:
            Hold = get_string(IAADDDEP.FDepName(8)) + ' ' + get_string(IAADDDEP.FDepLast(8))
            count = 99
        else:
            count = count + 1
    if get_number(IAADDDEP.FDepAge(9)) > 0 and get_number(IAADDDEP.FDepAge(9)) < 20:
        if Index == count:
            Hold = get_string(IAADDDEP.FDepName(9)) + ' ' + get_string(IAADDDEP.FDepLast(9))
            count = 99
        else:
            count = count + 1
    if get_number(IAADDDEP.FDepAge(10)) > 0 and get_number(IAADDDEP.FDepAge(10)) < 20:
        if Index == count:
            Hold = get_string(IAADDDEP.FDepName(10)) + ' ' + get_string(IAADDDEP.FDepLast(10))
            count = 99
        else:
            count = count + 1
    if get_number(IAADDDEP.FDepAge(11)) > 0 and get_number(IAADDDEP.FDepAge(11)) < 20:
        if Index == count:
            Hold = get_string(IAADDDEP.FDepName(11)) + ' ' + get_string(IAADDDEP.FDepLast(11))
            count = 99
        else:
            count = count + 1
    if get_number(IAADDDEP.FDepAge(12)) > 0 and get_number(IAADDDEP.FDepAge(12)) < 20:
        if Index == count:
            Hold = get_string(IAADDDEP.FDepName(12)) + ' ' + get_string(IAADDDEP.FDepLast(12))
            count = 99
        else:
            count = count + 1
    if get_number(IAADDDEP.FDepAge(13)) > 0 and get_number(IAADDDEP.FDepAge(13)) < 20:
        if Index == count:
            Hold = get_string(IAADDDEP.FDepName(13)) + ' ' + get_string(IAADDDEP.FDepLast(13))
            count = 99
        else:
            count = count + 1
    if get_number(IAADDDEP.FDepAge(14)) > 0 and get_number(IAADDDEP.FDepAge(14)) < 20:
        if Index == count:
            Hold = get_string(IAADDDEP.FDepName(14)) + ' ' + get_string(IAADDDEP.FDepLast(14))
            count = 99
        else:
            count = count + 1
    return Hold

def Description_Calculation():
    return CStr(get_currency(IATUITION.TotCR))

def Names_Calculation():
    return get_string(IAREQUIRED.CombNames)

def Spouse_Calculation(Index):
    if trim(get_string(IATUITION.DepName(Index))) != '':
        if get_bool(IAF1040.CombMFS) == False:
            return 0
        elif get_number(IAF1040.DC2) == 0:
            return 0
        elif get_number(IAF1040.DC2) > Index:
            return 1
        else:
            return 0
    else:
        return 0

def SSN_Calculation():
    return get_string(IAF1040.SSN)

def STuit_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 15:
        if get_bool(IATUITION.Spouse(count)) == True:
            SubTot = SubTot + get_currency(IATUITION.Credit(count))
        else:
            SubTot = SubTot
        count = count + 1
    if get_bool(IAF1040.CombMFS) == True and get_number(IAF1040.DC2) > 0:
        return SubTot
    else:
        return 0

def Taxpayer_Calculation(Index):
    if trim(get_string(IATUITION.DepName(Index))) != '' and get_bool(IATUITION.Spouse(Index)) == False:
        return 1
    else:
        return 0

def TotCR_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 15:
        SubTot = SubTot + get_currency(IATUITION.Credit(count))
        count = count + 1
    return SubTot

def TotExp_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 15:
        SubTot = SubTot + get_currency(IATUITION.Expenses(count))
        count = count + 1
    return SubTot

def TTuit_Calculation():
    return get_currency(IATUITION.TotCR) - get_currency(IATUITION.STuit)


