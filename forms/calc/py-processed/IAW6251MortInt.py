from forms.out import IAF1040
from forms.out import IAREQUIRED
from forms.out import IASCHA
from forms.out import IAW6251MORTINT
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def AMTInt_Calculation():
    if get_bool(USWResidency.F1040NR) == True:
        return 0
    elif get_bool(IAF1040.ItemCheck) == True:
        return min_value(get_currency(IAW6251MORTINT.TotMortInt), get_currency(IAW6251MORTINT.MortInt98) + get_currency(IAW6251MORTINT.RefinInt) + get_currency(IAW6251MORTINT.OthInt))
    else:
        return 0

def Desc_Calculation():
    return CStr(get_currency(IAW6251MORTINT.AMTInt))

def Exist_Calculation():
    return 1

def MortInt_Calculation():
    if get_bool(USWResidency.F1040NR) == True:
        return 0
    elif get_bool(IAF1040.ItemCheck) == True:
        return get_currency(IASCHA.Mort)
    else:
        return 0

def MortInt98_Calculation():
    if get_bool(IAF1040.ItemCheck) == True:
        return get_currency(USD1098.StateAdj)
    else:
        return 0

def MtgePrem_Calculation():
    if get_bool(USWResidency.F1040NR) == True:
        return 0
    elif get_bool(IAF1040.ItemCheck) == True:
        return get_currency(IASCHA.MtgePrem)
    else:
        return 0

def Names_Calculation():
    return get_string(IAREQUIRED.CombNames)

def Points_Calculation():
    if get_bool(USWResidency.F1040NR) == True:
        return 0
    elif get_bool(IAF1040.ItemCheck) == True:
        return get_currency(IASCHA.PtsNot)
    else:
        return 0

def Sfm_Calculation():
    if get_bool(USWResidency.F1040NR) == True:
        return 0
    elif get_bool(IAF1040.ItemCheck) == True:
        return get_currency(IASCHA.MortNot)
    else:
        return 0

def SSN_Calculation():
    return get_string(IAF1040.SSN)

def TotMortInt_Calculation():
    if get_bool(USWResidency.F1040NR) == True:
        return 0
    elif get_bool(IAF1040.ItemCheck) == True:
        return get_currency(IAW6251MORTINT.MortInt) + get_currency(IAW6251MORTINT.Sfm) + get_currency(IAW6251MORTINT.Points) + get_currency(IAW6251MORTINT.MtgePrem)
    else:
        return 0


