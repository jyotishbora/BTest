from forms.out import IAF1040
from forms.out import IAREQUIRED
from forms.out import IAWKALTTAX
from forms.out import USF4972SPOUSE
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def ATax_Calculation():
    if get_number(IAWKALTTAX.ProRate) == 1:
        return c_dollar(get_float(IAWKALTTAX.Lesser) * get_float(IAWKALTTAX.BProRate))
    else:
        return 0

def BProRate_Calculation():
    if get_number(IAWKALTTAX.ProRate) == 1:
        if get_currency(IAWKALTTAX.SPModNI) < 0 and get_currency(IAWKALTTAX.TPModNI) < 0:
            if get_currency(IAWKALTTAX.TPModNI) < get_currency(IAWKALTTAX.SPModNI):
                return 0
            else:
                return 1
        elif get_currency(IAWKALTTAX.TPModNI) < 0:
            return 0
        elif get_currency(IAWKALTTAX.TPModNI) > 0 and get_currency(IAWKALTTAX.TotAdjIANetInc) <= 0:
            return 1
        elif get_currency(IAWKALTTAX.TotAdjIANetInc) == 0:
            return 0
        else:
            return max_value(0, ( min_value(1, Round(get_float(IAWKALTTAX.TPModNI) / get_float(IAWKALTTAX.TotAdjIANetInc), 3)) ))
    else:
        return 0

def BTax_Calculation():
    if get_number(IAWKALTTAX.ProRate) == 1:
        return get_currency(IAWKALTTAX.Lesser) - get_currency(IAWKALTTAX.ATax)
    else:
        return 0

def Description_Calculation():
    return CStr(get_currency(IAWKALTTAX.Lesser))

def IncLimit_Calculation():
    if get_bool(IAF1040.Over65) == True:
        return Decimal("32000")
    else:
        return Decimal("13500")

def Lesser_Calculation():
    if get_bool(IAWKALTTAX.Qualify) == True:
        return min_value(get_currency(IAWKALTTAX.Mult), get_currency(IAWKALTTAX.Tables))
    else:
        return get_currency(IAWKALTTAX.Tables)

def Ln26_Calculation():
    return get_currency(IAWKALTTAX.TotSPLine1) + get_currency(IAWKALTTAX.TotLine1)

def LumpSum_Calculation():
    return get_currency(USF4972.TPCapGain) + get_currency(USF4972.TPTaxAmt)

def Mult_Calculation():
    return c_dollar(get_float(IAWKALTTAX.Sub1) * 0.0898)

def Names_Calculation():
    return get_string(IAREQUIRED.CombNames)

def NetInc_Calculation():
    return get_currency(IAF1040.ANet)

def PenExcl_Calculation():
    return get_currency(IAF1040.APenExcl)

def ProRate_Calculation():
    if IAFS() == 3 or IAFS() == 4:
        if ( get_currency(IAWKALTTAX.Mult) < get_currency(IAWKALTTAX.Tables) )  and get_bool(IAWKALTTAX.Qualify) == True:
            return 1
        else:
            return 0
    else:
        return 0

def Qualify_Calculation():
    NoMFSQual = Long()
    if get_currency(IAF1040.SpIncome) == 0 and get_bool(IAF1040.NoMFSInc) == False:
        NoMFSQual = 1
    else:
        NoMFSQual = 0
    if IAFS() == 1:
        return 0
    elif get_bool(IAREQUIRED.AskFilStat) == True and get_bool(IAWKALTTAX.NOL) == True:
        return 0
    elif IAFS() == 4 and NoMFSQual == 1:
        return 0
    else:
        return 1

def SPLumpSum_Calculation():
    #probably should ask for the form 4972 amounts on the IA 1040 under the filing status 4 section, however for the number of users that will fall in this situation not going to add this year.
    if IAFS() == 4:
        return 0
    else:
        return get_currency(USF4972SPOUSE.TPCapGain) + get_currency(USF4972SPOUSE.TPTaxAmt)

def SPModNI_Calculation():
    if get_number(IAWKALTTAX.ProRate) == 1:
        return get_currency(IAWKALTTAX.TotSPLine1)
    else:
        return 0

def SPNetInc_Calculation():
    if IAFS() == 4:
        return get_currency(IAF1040.SpIncome)
    else:
        return get_currency(IAF1040.BNet)

def SPPenExcl_Calculation():
    if IAFS() == 4:
        return get_currency(IAF1040.SpPenExcl)
    else:
        return get_currency(IAF1040.BPenExcl)

def SPSSB_Calculation():
    if IAFS() == 4:
        return get_currency(IAF1040.SpSSB)
    else:
        return get_currency(IAF1040.BRepSSB)

def SSB_Calculation():
    return get_currency(IAF1040.ARepSSB)

def SSN_Calculation():
    return get_string(IAF1040.SSN)

def Sub1_Calculation():
    return max_value(0, get_currency(IAWKALTTAX.Ln26) - get_currency(IAWKALTTAX.IncLimit))

def Tables_Calculation():
    return get_currency(IAF1040.ARegTax) + get_currency(IAF1040.BRegTax)

def TotAdjIANetInc_Calculation():
    return get_currency(IAWKALTTAX.SPModNI) + get_currency(IAWKALTTAX.TPModNI)

def TotLine1_Calculation():
    return get_currency(IAWKALTTAX.NetInc) + get_currency(IAWKALTTAX.PenExcl) + get_currency(IAWKALTTAX.SSB) + get_currency(IAWKALTTAX.LumpSum)

def TotSPLine1_Calculation():
    return get_currency(IAWKALTTAX.SPNetInc) + get_currency(IAWKALTTAX.SPPenExcl) + get_currency(IAWKALTTAX.SPSSB) + get_currency(IAWKALTTAX.SPLumpSum)

def TPModNI_Calculation():
    if get_number(IAWKALTTAX.ProRate) == 1:
        return get_currency(IAWKALTTAX.TotLine1)
    else:
        return 0


