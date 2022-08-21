from forms.out import IAADDDEP
from forms.out import IACHILDCREDIT
from forms.out import IAF1040
from forms.out import IAF126
from forms.out import IANROTHADJ
from forms.out import IAOTHADJ
from forms.out import IAREQUIRED
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def ChDepCr_Calculation():
    return c_dollar(get_float(IACHILDCREDIT.FedCredit) * get_float(IACHILDCREDIT.Percent))

def Credit_Calculation(Index):
    if get_currency(IACHILDCREDIT.TotNI) < Decimal("45000") and trim(get_string(IACHILDCREDIT.DepName(Index))) != '':
        return c_dollar(CDbl(min_value(get_currency(IACHILDCREDIT.Expenses(Index)), Decimal("1000"))) * 0.25)
    else:
        return 0

def DepName_Calculation(Index):
    count = Integer()

    Hold = String()
    count = 0
    Hold = ''
    if get_number(IAADDDEP.FDepAge(0)) > 2 and get_number(IAADDDEP.FDepAge(0)) < 7:
        if Index == count:
            Hold = get_string(IAADDDEP.FDepName(0)) + ' ' + get_string(IAADDDEP.FDepLast(0))
            count = 99
        else:
            count = count + 1
    if get_number(IAADDDEP.FDepAge(1)) > 2 and get_number(IAADDDEP.FDepAge(1)) < 7:
        if Index == count:
            Hold = get_string(IAADDDEP.FDepName(1)) + ' ' + get_string(IAADDDEP.FDepLast(1))
            count = 99
        else:
            count = count + 1
    if get_number(IAADDDEP.FDepAge(2)) > 2 and get_number(IAADDDEP.FDepAge(2)) < 7:
        if Index == count:
            Hold = get_string(IAADDDEP.FDepName(2)) + ' ' + get_string(IAADDDEP.FDepLast(2))
            count = 99
        else:
            count = count + 1
    if get_number(IAADDDEP.FDepAge(3)) > 2 and get_number(IAADDDEP.FDepAge(3)) < 7:
        if Index == count:
            Hold = get_string(IAADDDEP.FDepName(3)) + ' ' + get_string(IAADDDEP.FDepLast(3))
            count = 99
        else:
            count = count + 1
    if get_number(IAADDDEP.FDepAge(4)) > 2 and get_number(IAADDDEP.FDepAge(4)) < 7:
        if Index == count:
            Hold = get_string(IAADDDEP.FDepName(4)) + ' ' + get_string(IAADDDEP.FDepLast(4))
            count = 99
        else:
            count = count + 1
    if get_number(IAADDDEP.FDepAge(5)) > 2 and get_number(IAADDDEP.FDepAge(5)) < 7:
        if Index == count:
            Hold = get_string(IAADDDEP.FDepName(5)) + ' ' + get_string(IAADDDEP.FDepLast(5))
            count = 99
        else:
            count = count + 1
    if get_number(IAADDDEP.FDepAge(6)) > 2 and get_number(IAADDDEP.FDepAge(6)) < 7:
        if Index == count:
            Hold = get_string(IAADDDEP.FDepName(6)) + ' ' + get_string(IAADDDEP.FDepLast(6))
            count = 99
        else:
            count = count + 1
    if get_number(IAADDDEP.FDepAge(7)) > 2 and get_number(IAADDDEP.FDepAge(7)) < 7:
        if Index == count:
            Hold = get_string(IAADDDEP.FDepName(7)) + ' ' + get_string(IAADDDEP.FDepLast(7))
            count = 99
        else:
            count = count + 1
    if get_number(IAADDDEP.FDepAge(8)) > 2 and get_number(IAADDDEP.FDepAge(8)) < 7:
        if Index == count:
            Hold = get_string(IAADDDEP.FDepName(8)) + ' ' + get_string(IAADDDEP.FDepLast(8))
            count = 99
        else:
            count = count + 1
    if get_number(IAADDDEP.FDepAge(9)) > 2 and get_number(IAADDDEP.FDepAge(9)) < 7:
        if Index == count:
            Hold = get_string(IAADDDEP.FDepName(9)) + ' ' + get_string(IAADDDEP.FDepLast(9))
            count = 99
        else:
            count = count + 1
    if get_number(IAADDDEP.FDepAge(10)) > 2 and get_number(IAADDDEP.FDepAge(10)) < 7:
        if Index == count:
            Hold = get_string(IAADDDEP.FDepName(10)) + ' ' + get_string(IAADDDEP.FDepLast(10))
            count = 99
        else:
            count = count + 1
    if get_number(IAADDDEP.FDepAge(11)) > 2 and get_number(IAADDDEP.FDepAge(11)) < 7:
        if Index == count:
            Hold = get_string(IAADDDEP.FDepName(11)) + ' ' + get_string(IAADDDEP.FDepLast(11))
            count = 99
        else:
            count = count + 1
    if get_number(IAADDDEP.FDepAge(12)) > 2 and get_number(IAADDDEP.FDepAge(12)) < 7:
        if Index == count:
            Hold = get_string(IAADDDEP.FDepName(12)) + ' ' + get_string(IAADDDEP.FDepLast(12))
            count = 99
        else:
            count = count + 1
    if get_number(IAADDDEP.FDepAge(13)) > 2 and get_number(IAADDDEP.FDepAge(13)) < 7:
        if Index == count:
            Hold = get_string(IAADDDEP.FDepName(13)) + ' ' + get_string(IAADDDEP.FDepLast(13))
            count = 99
        else:
            count = count + 1
    if get_number(IAADDDEP.FDepAge(14)) > 2 and get_number(IAADDDEP.FDepAge(14)) < 7:
        if Index == count:
            Hold = get_string(IAADDDEP.FDepName(14)) + ' ' + get_string(IAADDDEP.FDepLast(14))
            count = 99
        else:
            count = count + 1
    return Hold

def Description_Calculation():
    TotCR = Currency()
    if get_bool(IAF1040.ChildCareCk) == True:
        TotCR = get_currency(IACHILDCREDIT.TotChDepCr)
    elif get_bool(IAF1040.EarlyChildCk) == True:
        TotCR = get_currency(IACHILDCREDIT.TotCR)
    else:
        TotCR = 0
    return CStr(TotCR)

def FedCredit_Calculation():
    return get_currency(USF2441.TentCred)

def MFSProRate_Calculation():
    if IAFS() == 4:
        if get_currency(IAF1040.SpIncome) < 0 and get_currency(IAF1040.ANet) < 0:
            if get_currency(IAF1040.SpIncome) < get_currency(IAF1040.ANet):
                return 0
            else:
                return 1
        elif get_currency(IAF1040.SpIncome) < 0:
            return 0
        elif get_currency(IAF1040.SpIncome) > 0 and get_currency(IACHILDCREDIT.MFSTotNet) <= 0:
            return 1
        elif get_currency(IACHILDCREDIT.MFSTotNet) == 0:
            return 0
        else:
            return max_value(0, ( min_value(1, get_float(IAF1040.SpIncome) / get_float(IACHILDCREDIT.MFSTotNet)) ))
    else:
        return 0

def MFSTotNet_Calculation():
    if get_bool(IAF1040.MFS) == True:
        return get_currency(IAF1040.ANet) + get_currency(IAOTHADJ.TIANOL) + get_currency(IAF1040.SpIncome)
    else:
        return 0

def Names_Calculation():
    return get_string(IAREQUIRED.CombNames)

def Percent_Calculation():
    if get_currency(IACHILDCREDIT.TotNI) > Decimal("44999"):
        return 0
    elif get_currency(IACHILDCREDIT.TotNI) > Decimal("39999"):
        return 0.3
    elif get_currency(IACHILDCREDIT.TotNI) > Decimal("34999"):
        return 0.4
    elif get_currency(IACHILDCREDIT.TotNI) > Decimal("24999"):
        return 0.5
    elif get_currency(IACHILDCREDIT.TotNI) > Decimal("19999"):
        return 0.55
    elif get_currency(IACHILDCREDIT.TotNI) > Decimal("9999"):
        return 0.65
    else:
        return 0.75

def PYNRChDepCr_Calculation():
    return min_value(get_currency(IACHILDCREDIT.ChDepCr), ( c_dollar(get_float(IACHILDCREDIT.ChDepCr) * get_float(IACHILDCREDIT.PYNRPercent)) ))

def PYNRPercent_Calculation():
    if get_currency(IACHILDCREDIT.TotNI) > 0:
        return min_value(1, max_value(0, CDbl(get_currency(IACHILDCREDIT.PYNRTotNI)) / CDbl(get_currency(IACHILDCREDIT.TotNI))))
    else:
        return 0

def PYNRTotNI_Calculation():
    if get_bool(IAF126.TpPYNR) == True or get_bool(IAF126.SpPYNR):
        return get_currency(IACHILDCREDIT.TPNRIncome) + get_currency(IACHILDCREDIT.SPNRIncome)
    else:
        return 0

def SChild_Calculation():
    if get_bool(IAF1040.MFS) == True:
        return c_dollar(get_float(IACHILDCREDIT.TotChDepCr) * get_float(IACHILDCREDIT.MFSProRate))
    else:
        return c_dollar(get_float(IACHILDCREDIT.TotChDepCr) * get_float(IAREQUIRED.BProRate))

def SEarly_Calculation():
    if get_bool(IAF1040.MFS) == True:
        return c_dollar(get_float(IACHILDCREDIT.TotCR) * get_float(IACHILDCREDIT.MFSProRate))
    else:
        return c_dollar(get_float(IACHILDCREDIT.TotCR) * get_float(IAREQUIRED.BProRate))

def SPNRIncome_Calculation():
    if get_bool(IAF1040.MFS) == True:
        return get_currency(IAF1040.SpIncome)
    elif get_bool(IAF126.SpPYNR) == True:
        return get_currency(IAF126.BNet) + get_currency(IANROTHADJ.SIANOL)
    else:
        return get_currency(IAF1040.BNet) + get_currency(IAOTHADJ.SIANOL)

def SSN_Calculation():
    return get_string(IAF1040.SSN)

def TChild_Calculation():
    return get_currency(IACHILDCREDIT.TotChDepCr) - get_currency(IACHILDCREDIT.SChild)

def TEarly_Calculation():
    return get_currency(IACHILDCREDIT.TotCR) - get_currency(IACHILDCREDIT.SEarly)

def TotChDepCr_Calculation():
    if get_bool(IAF126.TpPYNR) == True or get_bool(IAF126.SpPYNR):
        return get_currency(IACHILDCREDIT.PYNRChDepCr)
    else:
        return get_currency(IACHILDCREDIT.ChDepCr)

def TotCR_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 15:
        SubTot = SubTot + get_currency(IACHILDCREDIT.Credit(count))
        count = count + 1
    return SubTot

def TotNI_Calculation():
    if get_bool(IAF1040.MFS) == True:
        return get_currency(IACHILDCREDIT.MFSTotNet)
    else:
        return get_currency(IAREQUIRED.TotNI) + get_currency(IAOTHADJ.TIANOL) + get_currency(IAOTHADJ.SIANOL)

def TPNRIncome_Calculation():
    if get_bool(IAF126.TpPYNR) == True:
        return get_currency(IAF126.ANet) + get_currency(IANROTHADJ.TIANOL)
    else:
        return get_currency(IAF1040.ANet) + get_currency(IAOTHADJ.TIANOL)


