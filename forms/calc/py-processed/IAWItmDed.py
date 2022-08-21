from forms.out import IAF1040
from forms.out import IAREQUIRED
from forms.out import IASCHA
from forms.out import IAWITMDED
from forms.out import IAWSCHAPRINT
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def AGI_Calculation():
    return get_currency(IASCHA.IAAGI)

def AllowableDed2_Calculation():
    return get_currency(IAWITMDED.AllowableDed)

def AllowableDed_Calculation():
    return max_value(0, ( get_currency(IAWITMDED.IATotDed) - get_currency(IAWITMDED.Limit) ))

def Description_Calculation():
    return CStr(get_currency(IAWITMDED.LimitDed)) + ' Itemized Deductions'

def Divide_Calculation():
    if get_currency(IAWITMDED.Subtract2) == 0:
        return 0
    else:
        return Round(get_float(IAWITMDED.Subtract1) / get_float(IAWITMDED.Subtract2), 3)

def ExcInc_Calculation():
    return max_value(0, ( get_currency(IAWITMDED.AGI) - get_currency(IAWITMDED.IncLimit) ))

def IADedTax2_Calculation():
    return get_currency(IAWITMDED.IADedTax)

def IADedTax_Calculation():
    if get_bool(USWRec.ItmDdn) == True:
        if get_bool(USSchA.Income) == True or get_bool(USWResidency.F1040NR) == True:
            return max_value(0, get_currency(IASCHA.IATax))
        else:
            return 0
    else:
        return 0

def IATotDed2_Calculation():
    return get_currency(IAWITMDED.IATotDed)

def IATotDed_Calculation():
    return get_currency(IAWITMDED.TotDed) + get_currency(IAWITMDED.IADedTax)

def IncLimit_Calculation():
    # updated for 2018 - RJ
    if FedFS() == 1:
        return Decimal("266700")
    elif FedFS() == 3:
        return Decimal("160000")
    elif FedFS() == 4:
        return Decimal("293350")
    else:
        return Decimal("320000")

def Limit3_Calculation():
    return c_dollar(get_float(IAWITMDED.ExcInc) * 0.03)

def Limit80_Calculation():
    return c_dollar(get_float(IAWITMDED.PODed) * 0.8)

def Limit_Calculation():
    return min_value(get_currency(IAWITMDED.Limit80), get_currency(IAWITMDED.Limit3))

def LimitDed_Calculation():
    return max_value(0, ( get_currency(IAWITMDED.AllowableDed2) - get_currency(IAWITMDED.Multiply) ))

def Multiply_Calculation():
    return c_dollar(get_float(IAWITMDED.IADedTax2) * get_float(IAWITMDED.Divide))

def Names_Calculation():
    return get_string(IAREQUIRED.CombNames)

def No1_Calculation():
    if get_currency(IAWITMDED.NonPODed) < get_currency(IAWITMDED.IATotDed):
        return 0
    else:
        return 1

def No2_Calculation():
    if get_currency(IAWITMDED.IncLimit) < get_currency(IAWITMDED.AGI):
        return 0
    else:
        return 1

def NonPODed2_Calculation():
    return get_currency(IAWITMDED.NonPODed)

def NonPODed_Calculation():
    GamblingLoss = Currency()
    if get_bool(USWResidency.F1040NR) == True:
        GamblingLoss = 0
    else:
        GamblingLoss = get_currency(IAWSCHAPRINT.GamblingLoss)
    return get_currency(IASCHA.MedDed) + get_currency(IASCHA.Invest) + get_currency(IASCHA.Theft) + get_currency(IAWSCHAPRINT.Form4684) + GamblingLoss

def PODed_Calculation():
    return max_value(0, ( get_currency(IAWITMDED.IATotDed) - get_currency(IAWITMDED.NonPODed) ))

def SSN_Calculation():
    return get_string(IAF1040.SSN)

def Subtract1_Calculation():
    return max_value(0, ( get_currency(IAWITMDED.AllowableDed2) - get_currency(IAWITMDED.NonPODed2) ))

def Subtract2_Calculation():
    return max_value(0, ( get_currency(IAWITMDED.IATotDed2) - get_currency(IAWITMDED.NonPODed2) ))

def TotDed_Calculation():
    return get_currency(IASCHA.MedDed) + get_currency(IASCHA.TaxPd) + get_currency(IASCHA.TotInt) + get_currency(IASCHA.TotGifts) + get_currency(IASCHA.Theft) + get_currency(IASCHA.AllowExp) + get_currency(IASCHA.OthMisc)

def Yes1_Calculation():
    if get_bool(IAWITMDED.No1) == True:
        return 0
    else:
        return 1

def Yes2_Calculation():
    if get_bool(IAWITMDED.No2) == True:
        return 0
    else:
        return 1


