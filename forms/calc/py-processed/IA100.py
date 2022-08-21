from forms.out import IA100
from forms.out import IAF1040
from forms.out import IAREQUIRED
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Common_Calculation():
    if get_bool(IAF1040.MFJ) == True:
        return get_string(USWBasicInfo.CombFirst)
    else:
        return get_string(USWBasicInfo.TPCommon)

def MEF100SP_Calculation():
    if get_bool(IA100.Spouse) == True and get_bool(IA100.Print) == True:
        return 1
    else:
        return 0

def MEF100TP_Calculation():
    if get_bool(IA100.Taxpayer) == True and get_bool(IA100.Print) == True:
        return 1
    else:
        return 0

def Names_Calculation():
    if get_bool(IA100.Spouse) == True:
        return get_string(IAREQUIRED.SPCombName)
    else:
        return get_string(IAREQUIRED.TPCombName)

def P2Gain_Calculation():
    return max_value(0, get_currency(IA100.P2SalesPx) - get_currency(IA100.P2Cost))

def P2TPSharePerc_Calculation():
    return get_float(IA100.P2TPShare) * 100

def Print_Calculation():
    if get_currency(IA100.P6CGD) > 0:
        return 1
    else:
        return 0

def SpouseCommon_Calculation():
    if get_bool(IAF1040.CombMFS) == True:
        return get_string(USWBasicInfo.SPCommon)
    else:
        return 'Not Applicable'

def SSN_Calculation():
    if get_bool(IA100.Spouse) == True:
        return get_string(IAF1040.SpouseSSN)
    else:
        return get_string(IAF1040.SSN)


