from forms.out import IAF1040
from forms.out import IAFIRECR
from forms.out import IAREQUIRED
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Description_Calculation():
    Total = Currency()
    Total = get_currency(IAFIRECR.SPTotCr) + get_currency(IAFIRECR.TPTotCr)
    return CStr(Total)

def MobDisQual_Calculation():
    if get_currency(IAFIRECR.SPTotCr) + get_currency(IAFIRECR.TPTotCr) > 0:
        return 1
    else:
        return 0

def Names_Calculation():
    return get_string(IAREQUIRED.CombNames)

def SPName_Calculation():
    return get_string(USWBasicInfo.SPCommon)

def SPTotCr_Calculation():
    # updated for 2018
    if get_bool(IAFIRECR.SPQual) == True and get_bool(IAREQUIRED.AskSpouse) == True:
        return min_value(Decimal("100"), c_dollar(get_float(IAFIRECR.SPMonths) * 834))
    else:
        return 0

def SSN_Calculation():
    return get_string(IAF1040.SSN)

def TPName_Calculation():
    return get_string(USWBasicInfo.TPCommon)

def TPTotCr_Calculation():
    # updated for 2018
    if get_bool(IAFIRECR.TPQual) == True:
        return min_value(Decimal("100"), c_dollar(get_float(IAFIRECR.TPMonths) * 834))
    else:
        return 0


