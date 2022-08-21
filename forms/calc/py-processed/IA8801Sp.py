from forms.out import IA148SP
from forms.out import IA6251
from forms.out import IA6251SP
from forms.out import IA8801SP
from forms.out import IAF1040
from forms.out import IAF126
from forms.out import IAREQUIRED
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def AMTCR_Calculation():
    return min_value(get_currency(IA8801SP.MaxAMT), get_currency(IA8801SP.CYRegTax))

def ApporRegTx_Calculation():
    return get_currency(IA8801SP.CYTax) - get_currency(IA8801SP.PYNRCr)

def CYAMT_Calculation():
    if get_bool(IAF1040.CombMFS) == False:
        return 0
    elif get_bool(IAF126.SpPYNR) == True:
        return max_value(0, c_dollar(get_float(IA6251SP.TentAMT) * get_float(IA6251SP.PYNRRatio)))
    else:
        return get_currency(IA6251SP.TentAMT)

def CYCarryforward_Calculation():
    return max_value(0, get_currency(IA8801SP.TotalPYAMT) - get_currency(IA8801SP.AMTCR))

def CYRegTax_Calculation():
    if get_currency(IA8801SP.ExcRegTax) == 0:
        return 0
    else:
        return max_value(0, get_currency(IA8801SP.CYTax) - get_currency(IA8801SP.TotCr))

def CYTax_Calculation():
    if get_bool(IAF1040.CombMFS) == True:
        return get_currency(IAF1040.BAltTax)
    else:
        return 0

def Description_Calculation():
    Total = Currency()
    Total = get_currency(IA8801SP.AMTCR)
    return CStr(Total) + ' Credit'

def EFile_Calculation():
    if get_currency(IA8801SP.AMTCR) > 0:
        return 1
    else:
        return 0

def ExcRegTax_Calculation():
    return max_value(0, get_currency(IA8801SP.ApporRegTx) - get_currency(IA8801SP.CYAMT))

def MaxAMT_Calculation():
    return min_value(get_currency(IA8801SP.TotalPYAMT), get_currency(IA8801SP.ExcRegTax))

def Names_Calculation():
    return get_string(IAREQUIRED.SPCombName)

def Print_Calculation():
    if get_currency(IA8801SP.AMTCR) > 0 or get_currency(IA8801SP.CYCarryforward) > 0:
        return 1
    else:
        return 0

def PYAMT_Calculation():
    if get_bool(IAF1040.CombMFS) == False:
        return 0
    elif get_string(USZIA1040.IAPYFS) == get_string(IAREQUIRED.FilingStatus):
        return get_currency(USZIA1040.IAPYMinTaxB)
    else:
        return 0

def PYCarryforward_Calculation():
    return get_currency(USZIA1040.IAPY8801CFSp)

def PYNRCr_Calculation():
    if get_bool(IAF1040.CombMFS) == True:
        return get_currency(IAF1040.BCrNon)
    else:
        return 0

def SSN_Calculation():
    return get_string(IAF1040.SpouseSSN)

def Sum148Cr_Calculation():
    if get_currency(IA8801SP.ExcRegTax) == 0:
        return 0
    elif get_bool(IAF1040.CombMFS) == True:
        return get_currency(IA148SP.TotNonRefNo8801)
    else:
        return 0

def SumCr_Calculation():
    if get_currency(IA8801SP.ExcRegTax) == 0:
        return 0
    elif get_bool(IAF1040.CombMFS) == True:
        return get_currency(IAF1040.BCredits) + get_currency(IAF1040.BCrNon) + get_currency(IAF1040.BOutState)
    else:
        return 0

def TotalPYAMT_Calculation():
    if get_bool(IAF1040.CombMFS) == True:
        return get_currency(IA8801SP.PYAMT) + get_currency(IA8801SP.PYCarryforward)
    else:
        return 0

def TotCr_Calculation():
    return get_currency(IA8801SP.SumCr) + get_currency(IA8801SP.Sum148Cr)


