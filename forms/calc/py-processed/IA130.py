from forms.out import IA130
from forms.out import IAF1040
from forms.out import IAF126
from forms.out import IAREQUIRED
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Alert10_Calculation():
    if get_bool(IA130.MEF130TP) == True and trim(get_string(IA130.EFTPState)) == '':
        return 1
    else:
        return 0

def Alert20_Calculation():
    if get_bool(IA130.MEF130SP) == True and trim(get_string(IA130.EFTPState)) == '':
        return 1
    else:
        return 0

def Common_Calculation():
    if get_bool(IAF1040.MFJ) == True:
        return get_string(USWBasicInfo.CombFirst)
    else:
        return get_string(USWBasicInfo.TPCommon)

def Credit_Calculation():
    return get_currency(IA130.Small) + get_currency(IA130.PY130Cr)

def Description_Calculation():
    Total = Currency()
    Total = get_currency(IA130.Small) + get_currency(IA130.PY130Cr)
    return CStr(Total) + ' Credit'

def Div_Calculation():
    TopLim = Double()
    if get_currency(IA130.Inc15) == 0:
        return 0
    else:
        TopLim = min_value(1, Round(get_float(IA130.GrInc) / get_float(IA130.Inc15), 3))
        return max_value(0, TopLim)

def EFTPState_Calculation():
    if trim(get_string(IA130.YouFC)) != '':
        return ForeignCode(trim(get_string(IA130.YouFC)))
    else:
        return get_string(IA130.YouState)

def Exist_Calculation():
    return 1

def Inc15_Calculation():
    if get_bool(IA130.TPRes) == True:
        return get_currency(IAF1040.AGross)
    elif get_bool(IA130.TPPY) == True:
        return get_currency(IAF126.GrossInc)
    elif get_bool(IA130.SPRes) == True:
        return get_currency(IAF1040.BGross)
    elif get_bool(IA130.SPPY) == True:
        return get_currency(IAF126.BGross)
    else:
        return 0

def MEF130SP_Calculation():
    if get_bool(IA130.SPRes) == True and get_currency(IA130.Small) != 0:
        return 1
    elif get_bool(IA130.SPPY) == True and get_currency(IA130.PY130Cr) != 0:
        return 1
    else:
        return 0

def MEF130TP_Calculation():
    if get_bool(IA130.TPRes) == True and get_currency(IA130.Small) != 0:
        return 1
    elif get_bool(IA130.TPPY) == True and get_currency(IA130.PY130Cr) != 0:
        return 1
    else:
        return 0

def Mult_Calculation():
    return c_dollar(get_float(IA130.Div) * get_float(IA130.Tax55))

def Names_Calculation():
    if get_bool(IAF1040.CombMFS) == True:
        if get_bool(IA130.Spouse) == True:
            return get_string(IAREQUIRED.SPCombName)
        else:
            return get_string(IAREQUIRED.TPCombName)
    else:
        return get_string(IAREQUIRED.CombNames)

def PartYear_Calculation():
    if get_number(IA130.TPPY) > 0 or get_number(IA130.SPPY) > 0:
        return 1
    else:
        return 0

def PrintMe_Calculation():
    if get_currency(IA130.Small) + get_currency(IA130.PY130Cr) > 0:
        return 1
    else:
        return 0

def PY130Cr_Calculation():
    if get_bool(IA130.TPPY) == True or get_bool(IA130.SPPY) == True:
        return min_value(get_currency(IA130.Mult), get_currency(IA130.PYTax))
    else:
        return 0

def PYPer_Calculation():
    TopLim = Double()
    if get_bool(IA130.TPPY) == True or get_bool(IA130.SPPY) == True:
        if get_float(IA130.PYSmall) == 0:
            return 0
        else:
            TopLim = min_value(1, Round(get_float(IA130.GrInc) / get_float(IA130.PYSmall), 3))
            return max_value(0, TopLim)
    else:
        return 0

def PYTax_Calculation():
    if get_bool(IA130.TPPY) == True or get_bool(IA130.SPPY) == True:
        return c_dollar(get_float(IA130.OthTax) * get_float(IA130.PYPer))
    else:
        return 0

def Small_Calculation():
    if get_bool(IA130.TPRes) == True or get_bool(IA130.SPRes) == True:
        return min_value(get_currency(IA130.Mult), get_currency(IA130.OthTax))
    else:
        return 0

def SPCredit_Calculation():
    if get_number(IA130.SPRes) > 0 or get_number(IA130.SPPY) > 0:
        return get_currency(IA130.Small) + get_currency(IA130.PY130Cr)
    else:
        return 0

def SpouseCommon_Calculation():
    if get_bool(IAF1040.CombMFS) == True:
        return get_string(USWBasicInfo.SPCommon)
    else:
        return 'Not Applicable'

def SPPY_Calculation():
    if get_bool(IAF1040.CombMFS) == True and get_bool(IAF126.SpPYRes) == True and get_bool(IA130.Spouse) == True:
        return 1
    else:
        return 0

def SPRes_Calculation():
    if get_bool(IAF1040.CombMFS) == True and get_bool(IA130.Spouse) == True:
        if get_bool(IAF126.Exist) == False:
            return 1
        elif get_bool(IAF126.SpRes) == True:
            return 1
        else:
            return 0
    else:
        return 0

def SSN_Calculation():
    if get_bool(IA130.Spouse) == True:
        return get_string(IAF1040.SpouseSSN)
    else:
        return get_string(IAF1040.SSN)

def Tax55_Calculation():
    if get_bool(IA130.TPRes) == True or get_bool(IA130.TPPY) == True:
        return max_value(0, get_currency(IAF1040.ABal2) -  ( get_currency(IAF1040.ALump) + get_currency(IAF1040.AIAMin) ))
    elif get_bool(IA130.SPRes) == True or get_bool(IA130.SPPY) == True:
        return max_value(0, get_currency(IAF1040.BBal2) -  ( get_currency(IAF1040.BLump) + get_currency(IAF1040.BIAMin) ))
    else:
        return 0

def TPCredit_Calculation():
    if get_number(IA130.TPRes) > 0 or get_number(IA130.TPPY) > 0:
        return get_currency(IA130.Small) + get_currency(IA130.PY130Cr)
    else:
        return 0

def TPPY_Calculation():
    if get_bool(IA130.Spouse) == True:
        return 0
    elif get_bool(IAF1040.MFJ) == True:
        if get_bool(IAF126.TpPYRes) == True or get_bool(IAF126.SpPYRes) == True:
            return 1
        else:
            return 0
    elif get_bool(IAF126.TpPYRes) == True:
        return 1
    else:
        return 0

def TPRes_Calculation():
    Only1NR = Long()
    if get_bool(IAF126.TpNonRes) == True and get_bool(IAF126.SPRes) == True:
        Only1NR = 1
    elif get_bool(IAF126.TPRes) == True and get_bool(IAF126.SpNonRes) == True:
        Only1NR = 1
    else:
        Only1NR = 0
    if get_bool(IA130.Spouse) == True:
        return 0
    elif get_bool(IAF126.Exist) == False:
        return 1
    elif get_bool(IAF1040.MFJ) == True and Only1NR == 1:
        return 1
    elif get_bool(IAF1040.MFJ) == True and get_bool(IAF126.TPRes) == True and get_bool(IAF126.SPRes) == True:
        return 1
    elif get_bool(IAF1040.MFJ) != True and get_bool(IAF126.TPRes) == True:
        return 1
    else:
        return 0


