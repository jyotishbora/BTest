from forms.out import IAF1040
from forms.out import IAF126
from forms.out import IAFEDREF
from forms.out import IAREQUIRED
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *
import datetime



def Description_Calculation():
    Total = Currency()
    Total = get_currency(IAFEDREF.TPST) + get_currency(IAFEDREF.SPST)
    return CStr(Total)

def Names_Calculation():
    return get_string(IAREQUIRED.CombNames)

def NetRef_Calculation():
    if get_bool(IAFEDREF.PYNR) == True:
        return 0
    else:
        return max_value(0, get_currency(IAFEDREF.PyRef) - get_currency(IAFEDREF.PYEIC) - get_currency(IAFEDREF.PYAddCTC) - get_currency(IAFEDREF.PYRefHopeCr) - get_currency(IAFEDREF.PYPTC))

def PYAddCTC_Calculation():
    if get_bool(USWSpouse.NonRes) == True:
        return get_currency(USWRec.PYAddCTCNR)
    else:
        return get_currency(USWRec.PYAddCTC)

def PYEIC_Calculation():
    return get_currency(USWRec.PYEIC)

def PYNR_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        if ( get_bool(IAF126.TpPYRes) == True and GetDate(IAF126.TpDateIn) > datetime.datetime(12, 31, 2017) )  and  ( get_bool(IAF126.SpPYRes) == True and GetDate(IAF126.SpDateIn) > datetime.datetime(12, 31, 2017) ) :
            return 1
        else:
            return 0
    elif  ( get_bool(IAF126.TpPYRes) == True and GetDate(IAF126.TpDateIn) > datetime.datetime(12, 31, 2017) ) :
        return 1
    else:
        return 0

def PYPTC_Calculation():
    if get_bool(USWSpouse.NonRes) == True:
        return get_currency(USWRec.PYNPTCNR)
    else:
        return get_currency(USWRec.PYNPTC)

def PyRef_Calculation():
    if get_bool(USWSpouse.NonRes) == True:
        return get_currency(USWRec.PYRefNR)
    else:
        return get_currency(USWRec.PYRef)

def PYRefHopeCr_Calculation():
    return get_currency(USWRec.PYRefHopeCr)

def SPName_Calculation():
    return get_string(USWBasicInfo.SPCommon)

def SPST_Calculation():
    return c_dollar(get_float(IAREQUIRED.PYRatio) * get_float(IAFEDREF.NetRef))

def SSN_Calculation():
    return get_string(IAF1040.SSN)

def TPName_Calculation():
    return get_string(USWBasicInfo.TPCommon)

def TPST_Calculation():
    return max_value(0, get_currency(IAFEDREF.NetRef) - get_currency(IAFEDREF.SPST))


