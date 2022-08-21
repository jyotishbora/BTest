from forms.out import IAADDFEDTAX
from forms.out import IAF1040
from forms.out import IAREQUIRED
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Description_Calculation():
    Total = Currency()
    Total = get_currency(IAADDFEDTAX.TPTotal) + get_currency(IAADDFEDTAX.SPTotal)
    return CStr(Total)

def Exist_Calculation():
    return 1

def Names_Calculation():
    return get_string(IAREQUIRED.CombNames)

def NetDue_Calculation():
    if get_currency(USZIA1040.IAPYNetIncB) == 0 and get_currency(USZIA1040.IAPYNetIncA) == 0:
        return 0
    else:
        return max_value(0, get_currency(IAADDFEDTAX.PyDue) - get_currency(IAADDFEDTAX.PYPen))

def PyDue_Calculation():
    if get_bool(USWSpouse.NonRes) == True:
        return get_currency(USWRec.PYOweNR)
    else:
        return get_currency(USWRec.PYOwe)

def PYExt_Calculation():
    if get_bool(USWSpouse.NonRes) == True:
        return get_currency(USWRec.PYExtNR)
    else:
        return get_currency(USWRec.PYExt)

def PYPen_Calculation():
    if get_bool(USWSpouse.NonRes) == True:
        return get_currency(USWRec.PYPenaltyNR)
    else:
        return get_currency(USWRec.PYPenalty)

def SPBalDue_Calculation():
    return c_dollar(get_float(IAREQUIRED.PYRatio) * get_float(IAADDFEDTAX.NetDue))

def SPExcFICA_Calculation():
    return get_currency(USWFICA.SCredit)

def SPExt_Calculation():
    return c_dollar(get_float(IAREQUIRED.PYRatio) * get_float(IAADDFEDTAX.PYExt))

def SPName_Calculation():
    return get_string(USWBasicInfo.SPCommon)

def SPTotal_Calculation():
    return get_currency(IAADDFEDTAX.SPBalDue) + get_currency(IAADDFEDTAX.SPExt) + get_currency(IAADDFEDTAX.SPFuel) + get_currency(IAADDFEDTAX.SPExcFICA)

def SSN_Calculation():
    return get_string(IAF1040.SSN)

def TPBalDue_Calculation():
    return max_value(0, get_currency(IAADDFEDTAX.NetDue) - get_currency(IAADDFEDTAX.SPBalDue))

def TPExcFICA_Calculation():
    return get_currency(USWFICA.TCredit)

def TPExt_Calculation():
    return max_value(0, get_currency(IAADDFEDTAX.PYExt) - get_currency(IAADDFEDTAX.SPExt))

def TPFuel_Calculation():
    return max_value(0, get_currency(USF4136.TotalCredit) - get_currency(IAADDFEDTAX.SPFuel))

def TPName_Calculation():
    return get_string(USWBasicInfo.TPCommon)

def TPTotal_Calculation():
    return get_currency(IAADDFEDTAX.TPBalDue) + get_currency(IAADDFEDTAX.TPExt) + get_currency(IAADDFEDTAX.TPFuel) + get_currency(IAADDFEDTAX.TPExcFICA)


