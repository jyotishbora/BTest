from forms.out import IA4562PIV
from forms.out import IAF1040
from forms.out import IAREQUIRED
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Alert10_Calculation():
    if get_bool(IA4562PIV.SpecElectYes) == False and get_currency(IA4562PIV.Total179) > Decimal("70000"):
        return 1
    else:
        return 0

def Alert20_Calculation():
    if get_bool(IA4562PIV.UsingSpecElec) == True:
        if ( get_currency(IA4562PIV.TPFed1065) + get_currency(IA4562PIV.SPFed1065) + get_currency(IA4562PIV.TPFed1120S) + get_currency(IA4562PIV.SPFed1120S) )  > Decimal("0"):
            if ( get_currency(IA4562PIV.TPIA1065) + get_currency(IA4562PIV.SPIA1065) + get_currency(IA4562PIV.TPIA1120S) + get_currency(IA4562PIV.SPIA1120S) )  == Decimal("0"):
                return 1
            else:
                return 0
        else:
            return 0
    else:
        return 0

def Alert30_Calculation():
    if get_bool(IA4562PIV.UsingSpecElec) == True:
        if ( get_currency(USWDepr.IACYSec179Rep) + get_currency(USF4562.StateTotCySec1792106, 1) )  > 0:
            return 1
        else:
            return 0
    else:
        return 0

def CarryOver179Yr1_Calculation():
    return max_value(0, ( get_currency(IA4562PIV.Excess179) - get_currency(IA4562PIV.CarryOver179Yr2) - get_currency(IA4562PIV.CarryOver179Yr3) - get_currency(IA4562PIV.CarryOver179Yr4) - get_currency(IA4562PIV.CarryOver179Yr5) ))

def CarryOver179Yr2_Calculation():
    return c_dollar(get_float(IA4562PIV.Excess179) * 0.2)

def CarryOver179Yr3_Calculation():
    return c_dollar(get_float(IA4562PIV.Excess179) * 0.2)

def CarryOver179Yr4_Calculation():
    return c_dollar(get_float(IA4562PIV.Excess179) * 0.2)

def CarryOver179Yr5_Calculation():
    return c_dollar(get_float(IA4562PIV.Excess179) * 0.2)

def Desc_Calculation():
    Total = Currency()
    Total = get_currency(IA4562PIV.Excess179)
    return CStr(Total) + ' Special Election Deduction'

def Excess179_Calculation():
    if get_bool(IA4562PIV.SpecElectYes) == True:
        return max_value(0, ( get_currency(IA4562PIV.Total179) - get_currency(IA4562PIV.Limit) ))
    else:
        return Decimal("0")

def Exist_Calculation():
    return 1

def IASec179NoK1s_Calculation():
    return get_currency(USWDepr.IACYSec179Rep) + get_currency(USF4562.StateTotCySec1792106, 1)

def Limit_Calculation():
    if get_bool(IA4562PIV.SpecElectYes) == True:
        return Decimal("70000")
    else:
        return Decimal("0")

def Names_Calculation():
    return get_string(IAREQUIRED.CombNames)

def PrIA4562PIV_Calculation():
    if get_currency(IA4562PIV.TPPartIV179) != 0:
        return 1
    else:
        return 0

def PrIA4562PIVSP_Calculation():
    if get_currency(IA4562PIV.SPPartIV179) != 0:
        return 1
    else:
        return 0

def Print_Calculation():
    if get_currency(IA4562PIV.Excess179) != 0:
        return 1
    else:
        return 0

def SPAccFedDep_Calculation():
    return 0

def SPAccIADep_Calculation():
    return 0

def SPBasis_Calculation():
    return 0

def SPCarryOver179Yr1_Calculation():
    if get_bool(IA4562PIV.UsingSpecElec) == False:
        return 0
    elif get_bool(IAF1040.CombMFS) == True:
        return c_dollar(get_float(IA4562PIV.CarryOver179Yr1) * get_float(IA4562PIV.SPRatio))
    else:
        return 0

def SPCarryOver179Yr2_Calculation():
    if get_bool(IA4562PIV.UsingSpecElec) == False:
        return 0
    elif get_bool(IAF1040.CombMFS) == True:
        return c_dollar(get_float(IA4562PIV.CarryOver179Yr2) * get_float(IA4562PIV.SPRatio))
    else:
        return 0

def SPCarryOver179Yr3_Calculation():
    if get_bool(IA4562PIV.UsingSpecElec) == False:
        return 0
    elif get_bool(IAF1040.CombMFS) == True:
        return c_dollar(get_float(IA4562PIV.CarryOver179Yr3) * get_float(IA4562PIV.SPRatio))
    else:
        return 0

def SPCarryOver179Yr4_Calculation():
    if get_bool(IA4562PIV.UsingSpecElec) == False:
        return 0
    elif get_bool(IAF1040.CombMFS) == True:
        return c_dollar(get_float(IA4562PIV.CarryOver179Yr4) * get_float(IA4562PIV.SPRatio))
    else:
        return 0

def SPCarryOver179Yr5_Calculation():
    if get_bool(IA4562PIV.UsingSpecElec) == False:
        return 0
    elif get_bool(IAF1040.CombMFS) == True:
        return c_dollar(get_float(IA4562PIV.CarryOver179Yr5) * get_float(IA4562PIV.SPRatio))
    else:
        return 0

def SpCopy_Calculation():
    if get_currency(IA4562PIV.SPPartIV179) > 0:
        return 1
    else:
        return 0

def SPDateServ_Calculation():
    return MakeDate(12, 31, YearNumber)

def SPExcess179_Calculation():
    if get_bool(IA4562PIV.UsingSpecElec) == False:
        return 0
    elif get_bool(IAF1040.CombMFS) == True:
        return c_dollar(get_float(IA4562PIV.Excess179) * get_float(IA4562PIV.SPRatio))
    else:
        return 0

def SPFed1065_Calculation():
    return get_currency(USDPartK1.Sec179, FieldCopies(USDPartK1.Spouse)) + max_value(0, get_currency(USDPartK1.Sec179, FieldCopies(USDPartK1.Joint)) - c_dollar(get_float(USDPartK1.Sec179, FieldCopies(USDPartK1.Joint)) * 0.5))

def SPFed1120S_Calculation():
    return get_currency(USDSCorpK1.Sec179, FieldCopies(USDSCorpK1.Spouse)) + max_value(0, get_currency(USDSCorpK1.Sec179, FieldCopies(USDSCorpK1.Joint)) - c_dollar(get_float(USDSCorpK1.Sec179, FieldCopies(USDSCorpK1.Joint)) * 0.5))

def SPFedDepDed_Calculation():
    return 0

def SPLife_Calculation():
    return '0'

def SPLine1_Calculation():
    if get_bool(IA4562PIV.UsingSpecElec) == False:
        return 0
    elif get_bool(IAF1040.CombMFS) == True:
        return c_dollar(get_float(IA4562PIV.Total179) * get_float(IA4562PIV.SPRatio))
    else:
        return 0

def SPLine1a_Calculation():
    if get_bool(IA4562PIV.UsingSpecElec) == False:
        return 0
    elif get_bool(IAF1040.CombMFS) == True:
        return get_currency(IA4562PIV.SPIA1065)
    else:
        return 0

def SPLine1b_Calculation():
    if get_bool(IA4562PIV.UsingSpecElec) == False:
        return 0
    elif get_bool(IAF1040.CombMFS) == True:
        return get_currency(IA4562PIV.SPFed1065)
    else:
        return 0

def SPLine1c_Calculation():
    if get_bool(IA4562PIV.UsingSpecElec) == False:
        return 0
    elif get_bool(IAF1040.CombMFS) == True:
        return get_currency(IA4562PIV.SPIA1120S)
    else:
        return 0

def SPLine1d_Calculation():
    if get_bool(IA4562PIV.UsingSpecElec) == False:
        return 0
    elif get_bool(IAF1040.CombMFS) == True:
        return get_currency(IA4562PIV.SPFed1120S)
    else:
        return 0

def SPMACRSIA_Calculation():
    return 0

def SPName_Calculation():
    return get_string(IAREQUIRED.SPCombName)

def SPPartIV179_Calculation():
    if get_bool(IA4562PIV.UsingSpecElec) == False:
        return 0
    elif get_bool(IAF1040.CombMFS) == True:
        return c_dollar(get_float(IA4562PIV.Limit) * get_float(IA4562PIV.SPRatio))
    else:
        return 0

def SPPropDescr_Calculation():
    if get_currency(IA4562PIV.SPPartIV179) > 0:
        return 'Part IV'
    else:
        return ''

def SPRatio_Calculation():
    if get_currency(IA4562PIV.Tot179Nolimit) == 0:
        return 0
    else:
        return max_value(0, ( min_value(1, get_float(IA4562PIV.SPTot179) / get_float(IA4562PIV.Tot179Nolimit)) ))

def SPSSN_Calculation():
    return get_string(IAF1040.SpouseSSN)

def SPTot179_Calculation():
    return get_currency(IA4562PIV.SPIA1065) + get_currency(IA4562PIV.SPFed1065) + get_currency(IA4562PIV.SPIA1120S) + get_currency(IA4562PIV.SPFed1120S)

def SPTotAdj_Calculation():
    return get_currency(IA4562PIV.SPLine1) - get_currency(IA4562PIV.SPPartIV179)

def SSN_Calculation():
    return get_string(IAF1040.SSN)

def Tot179Nolimit_Calculation():
    return get_currency(IA4562PIV.TPTot179) + get_currency(IA4562PIV.SPTot179)

def Total179_Calculation():
    Tot = Currency()
    Tot = get_currency(IA4562PIV.TotIA1065) + get_currency(IA4562PIV.TotFed1065) + get_currency(IA4562PIV.TotIA1120S) + get_currency(IA4562PIV.TotFed1120S)
    return min_value(Tot, Decimal("1000000"))

def TotFed1065_Calculation():
    return get_currency(IA4562PIV.TPFed1065) + get_currency(IA4562PIV.SPFed1065)

def TotFed1120S_Calculation():
    return get_currency(IA4562PIV.TPFed1120S) + get_currency(IA4562PIV.SPFed1120S)

def TotIA1065_Calculation():
    return get_currency(IA4562PIV.TPIA1065) + get_currency(IA4562PIV.SPIA1065)

def TotIA1120S_Calculation():
    return get_currency(IA4562PIV.TPIA1120S) + get_currency(IA4562PIV.SPIA1120S)

def TPAccFedDep_Calculation():
    return 0

def TPAccIADep_Calculation():
    return 0

def TPBasis_Calculation():
    return 0

def TPCarryOver179Yr1_Calculation():
    if get_bool(IA4562PIV.UsingSpecElec) == False:
        return 0
    elif get_bool(IAF1040.CombMFS) == True:
        return get_currency(IA4562PIV.CarryOver179Yr1) - get_currency(IA4562PIV.SPCarryOver179Yr1)
    else:
        return get_currency(IA4562PIV.CarryOver179Yr1)

def TPCarryOver179Yr2_Calculation():
    if get_bool(IA4562PIV.UsingSpecElec) == False:
        return 0
    elif get_bool(IAF1040.CombMFS) == True:
        return get_currency(IA4562PIV.CarryOver179Yr2) - get_currency(IA4562PIV.SPCarryOver179Yr2)
    else:
        return get_currency(IA4562PIV.CarryOver179Yr2)

def TPCarryOver179Yr3_Calculation():
    if get_bool(IA4562PIV.UsingSpecElec) == False:
        return 0
    elif get_bool(IAF1040.CombMFS) == True:
        return get_currency(IA4562PIV.CarryOver179Yr3) - get_currency(IA4562PIV.SPCarryOver179Yr3)
    else:
        return get_currency(IA4562PIV.CarryOver179Yr3)

def TPCarryOver179Yr4_Calculation():
    if get_bool(IA4562PIV.UsingSpecElec) == False:
        return 0
    elif get_bool(IAF1040.CombMFS) == True:
        return get_currency(IA4562PIV.CarryOver179Yr4) - get_currency(IA4562PIV.SPCarryOver179Yr4)
    else:
        return get_currency(IA4562PIV.CarryOver179Yr4)

def TPCarryOver179Yr5_Calculation():
    if get_bool(IA4562PIV.UsingSpecElec) == False:
        return 0
    elif get_bool(IAF1040.CombMFS) == True:
        return get_currency(IA4562PIV.CarryOver179Yr5) - get_currency(IA4562PIV.SPCarryOver179Yr5)
    else:
        return get_currency(IA4562PIV.CarryOver179Yr5)

def TpCopy_Calculation():
    if get_currency(IA4562PIV.TPPartIV179) > 0:
        return 1
    else:
        return 0

def TPDateServ_Calculation():
    return MakeDate(12, 31, YearNumber)

def TPExcess179_Calculation():
    if get_bool(IA4562PIV.UsingSpecElec) == False:
        return 0
    elif get_bool(IAF1040.CombMFS) == True:
        return get_currency(IA4562PIV.Excess179) - get_currency(IA4562PIV.SPExcess179)
    else:
        return get_currency(IA4562PIV.Excess179)

def TPFed1065_Calculation():
    return get_currency(USDPartK1.Sec179, FieldCopies(USDPartK1.Taxpayer)) + c_dollar(get_float(USDPartK1.Sec179, FieldCopies(USDPartK1.Joint)) * 0.5)

def TPFed1120S_Calculation():
    return get_currency(USDSCorpK1.Sec179, FieldCopies(USDSCorpK1.Taxpayer)) + c_dollar(get_float(USDSCorpK1.Sec179, FieldCopies(USDSCorpK1.Joint)) * 0.5)

def TPFedDepDed_Calculation():
    return 0

def TPLife_Calculation():
    return '0'

def TPLine1_Calculation():
    if get_bool(IA4562PIV.UsingSpecElec) == False:
        return 0
    elif get_bool(IAF1040.CombMFS) == True:
        return get_currency(IA4562PIV.Total179) - get_currency(IA4562PIV.SPLine1)
    else:
        return get_currency(IA4562PIV.Total179)

def TPLine1a_Calculation():
    if get_bool(IA4562PIV.UsingSpecElec) == False:
        return 0
    elif get_bool(IAF1040.CombMFS) == True:
        return get_currency(IA4562PIV.TPIA1065)
    else:
        return get_currency(IA4562PIV.TotIA1065)

def TPLine1b_Calculation():
    if get_bool(IA4562PIV.UsingSpecElec) == False:
        return 0
    elif get_bool(IAF1040.CombMFS) == True:
        return get_currency(IA4562PIV.TPFed1065)
    else:
        return get_currency(IA4562PIV.TotFed1065)

def TPLine1c_Calculation():
    if get_bool(IA4562PIV.UsingSpecElec) == False:
        return 0
    elif get_bool(IAF1040.CombMFS) == True:
        return get_currency(IA4562PIV.TPIA1120S)
    else:
        return get_currency(IA4562PIV.TotIA1120S)

def TPLine1d_Calculation():
    if get_bool(IA4562PIV.UsingSpecElec) == False:
        return 0
    elif get_bool(IAF1040.CombMFS) == True:
        return get_currency(IA4562PIV.TPFed1120S)
    else:
        return get_currency(IA4562PIV.TotFed1120S)

def TPMACRSIA_Calculation():
    return 0

def TPorJTName_Calculation():
    if get_bool(IAF1040.CombMFS) == True:
        return get_string(IAREQUIRED.TPCombName)
    else:
        return get_string(IAREQUIRED.CombNames)

def TPorJTSSN_Calculation():
    return get_string(IAF1040.SSN)

def TPPartIV179_Calculation():
    if get_bool(IA4562PIV.UsingSpecElec) == False:
        return 0
    elif get_bool(IAF1040.CombMFS) == True:
        return get_currency(IA4562PIV.Limit) - get_currency(IA4562PIV.SPPartIV179)
    else:
        return get_currency(IA4562PIV.Limit)

def TPPropDescr_Calculation():
    if get_currency(IA4562PIV.TPPartIV179) > 0:
        return 'Part IV'
    else:
        return ''

def TPTot179_Calculation():
    return get_currency(IA4562PIV.TPIA1065) + get_currency(IA4562PIV.TPFed1065) + get_currency(IA4562PIV.TPIA1120S) + get_currency(IA4562PIV.TPFed1120S)

def TPTotAdj_Calculation():
    return get_currency(IA4562PIV.TPLine1) - get_currency(IA4562PIV.TPPartIV179)

def UsingSpecElec_Calculation():
    if get_bool(IA4562PIV.SpecElectYes) == True and get_currency(IA4562PIV.Excess179) > Decimal("0"):
        return 1
    else:
        return 0


