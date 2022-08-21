from forms.out import IAF1040
from forms.out import IAREQUIRED
from forms.out import IASETAX
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Description_Calculation():
    Total = Currency()
    Total = get_currency(IASETAX.TPTotal) + get_currency(IASETAX.SPTotal)
    return CStr(Total)

def Exist_Calculation():
    return 1

def MobDisQual_Calculation():
    if get_currency(IASETAX.TPTotal) + get_currency(IASETAX.SPTotal) > 0:
        return 1
    else:
        return 0

def Names_Calculation():
    return get_string(IAREQUIRED.CombNames)

def SPHH_Calculation():
    if get_bool(USSchH.Taxpayer) == True:
        return 0
    elif get_bool(USWResidency.F1040NR) == True:
        return 0
    elif get_bool(USSchH.Spouse) == True:
        return get_currency(USW1040Supp.HTax)
    else:
        return c_dollar(get_float(USW1040Supp.HTax) * 0.5)

def SPName_Calculation():
    return get_string(USWBasicInfo.SPCommon)

def SPRetTax_Calculation():
    return get_currency(USF5329Spouse.TotAddTax)

def SPSE_Calculation():
    if get_bool(USSchSESpouse.ShortSE) == True:
        return get_currency(USSchSESpouse.ASETax)
    else:
        return get_currency(USSchSESpouse.BSETax)

def SPTipTax_Calculation():
    return get_currency(USF4137Spouse.AddLnTen) + get_currency(USF8919Spouse.TotTax)

def SPTotal_Calculation():
    return get_currency(IASETAX.SPRepayPTC) + get_currency(IASETAX.SPSE) + get_currency(IASETAX.SPTipTax) + get_currency(IASETAX.SPRetTax) + get_currency(IASETAX.SPHH) + get_currency(IASETAX.SPHomeBuyRepay) + get_currency(IASETAX.SpHlthCarePen) + get_currency(IASETAX.SPTotAddMedTax) + get_currency(IASETAX.SPOthTax)

def SSN_Calculation():
    return get_string(IAF1040.SSN)

def TPHH_Calculation():
    if get_bool(USWResidency.F1040NR) == True:
        return get_currency(USF1040NR.SchHTax)
    elif get_bool(USSchH.Spouse) == True:
        return 0
    else:
        return max_value(0, get_currency(USW1040Supp.HTax) - get_currency(IASETAX.SPHH))

def TPHlthCarePen_Calculation():
    if get_bool(USWResidency.F1040NR) == True:
        return 0
    else:
        return max_value(0, get_currency(USF1040.HlthCarePen) - get_currency(IASETAX.SpHlthCarePen))

def TPHomeBuyRepay_Calculation():
    if get_bool(USWResidency.F1040NR) == True:
        return get_currency(USF1040NR.HomeBuyRepay)
    else:
        return max_value(0, get_currency(USF1040.HomeBuyRepay) - get_currency(IASETAX.SPHomeBuyRepay))

def TPName_Calculation():
    return get_string(USWBasicInfo.TPCommon)

def TPOthTax_Calculation():
    return max_value(0, get_currency(USWOthTax.TotOthTax) - get_currency(IASETAX.SPOthTax))

def TPRepayPTC_Calculation():
    return max_value(0, get_currency(USF8962.PTCRepay) - get_currency(IASETAX.SPRepayPTC))

def TPRetTax_Calculation():
    return get_currency(USF5329.TotAddTax)

def TPSE_Calculation():
    if get_bool(USSchSE.ShortSE) == True:
        return get_currency(USSchSE.ASETax)
    else:
        return get_currency(USSchSE.BSETax)

def TPTipTax_Calculation():
    return get_currency(USF4137.AddLnTen) + get_currency(USF8919.TotTax)

def TPTotAddMedTax_Calculation():
    return max_value(0, get_currency(USF8959.TotAddMedTax) - get_currency(IASETAX.SPTotAddMedTax))

def TPTotal_Calculation():
    return get_currency(IASETAX.TPRepayPTC) + get_currency(IASETAX.TPSE) + get_currency(IASETAX.TPTipTax) + get_currency(IASETAX.TPRetTax) + get_currency(IASETAX.TPHH) + get_currency(IASETAX.TPHomeBuyRepay) + get_currency(IASETAX.TPHlthCarePen) + get_currency(IASETAX.TPTotAddMedTax) + get_currency(IASETAX.TPOthTax)


