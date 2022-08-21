from forms.out import IA1040X
from forms.out import IA2210
from forms.out import IA2210AN
from forms.out import IA2210ANSP
from forms.out import IA2210SP
from forms.out import IAF1040
from forms.out import IAPENALTY
from forms.out import IAPENALTYSP
from forms.out import IAREQUIRED
from forms.out import IASTATEEST
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Amt8_Calculation():
    return c_dollar(get_float(IA2210SP.Bal) * 0.9)

def Bal_Calculation():
    return max_value(0, get_currency(IA2210SP.CYTax) - get_currency(IA2210SP.TotCr))

def ChildC_Calculation():
    return get_currency(IAF1040.BChild)

def CYTax_Calculation():
    return get_currency(IAF1040.BBal4)

def Description_Calculation():
    return CStr(get_currency(IA2210SP.Penalty)) + ' Penalty'

def EFile_Calculation():
    if get_bool(IA1040X.EFAmend) == True:
        return 0
    elif get_bool(IAF1040.CombMFS) == False:
        return 0
    elif get_bool(IA2210SP.Print) == True:
        return 1
    elif get_currency(IA2210SP.Amt8) >= Decimal("200"):
        return 1
    else:
        return 0

def EFStQ1_Calculation():
    return get_currency(IASTATEEST.SPStApply) + get_currency(IASTATEEST.SPStQ1)

def ExpPenalty_Calculation():
    if get_currency(IA2210SP.Penalty) > 0:
        return 1
    else:
        return 0

def Fuel_Calculation():
    return get_currency(IAF1040.BFuel)

def IAEIC_Calculation():
    return get_currency(IAF1040.BIEIC)

def Names_Calculation():
    return get_string(IAREQUIRED.SPCombName)

def NoPen_Calculation():
    return get_bool(USWPrepMnNm.AlwaysState2210)

def Penalty_Calculation():
    if get_bool(IAF1040.CombMFS) == False:
        return 0
    elif get_bool(IA2210SP.NoPen) == True:
        return 0
    else:
        return get_currency(IAPENALTYSP.TotPen)

def Print_Calculation():
    if get_bool(IAF1040.CombMFS) == False:
        return 0
    elif get_bool(IA2210SP.AnInc) == True:
        return 1
    elif get_currency(IA2210SP.Penalty) > 0:
        return 1
    else:
        return 0

def PYTax_Calculation():
    AGIBonus = Currency()
    AGIBonus = get_currency(USWRec.PYSAGI) + get_currency(USZIA1040.IATotBonusSp)
    if get_bool(IAF1040.CombMFS) == False:
        return 0
    elif get_string(USZIA1040.IAPYFS) == get_string(IAREQUIRED.FilingStatus):
        if AGIBonus > Decimal("150000"):
            return c_dollar(get_float(USZIA1040.IA2210PYTaxSp) * 1.1)
        else:
            return get_currency(USZIA1040.IA2210PYTaxSp)
    else:
        return 0

def Q1AnInc_Calculation():
    if get_bool(IA2210SP.AnInc) == True:
        return get_currency(IA2210ANSP.Q1AIInstall)
    else:
        return 0

def Q1DaysB_Calculation():
    if get_currency(IA2210SP.Penalty) > 0:
        return 'See'
    else:
        return ''

def Q1Est_Calculation():
    return get_currency(IA2210SP.Q1WH) + get_currency(IASTATEEST.SPStApply) + get_currency(IASTATEEST.SPStQ1)

def Q1Install_Calculation():
    return c_dollar(get_float(IA2210SP.Small) * 0.25)

def Q1Ln11_Calculation():
    if get_bool(IA2210SP.AnInc) == True:
        return get_currency(IA2210SP.Q1AnInc)
    else:
        return get_currency(IA2210SP.Q1Install)

def Q1Ln19a_Calculation():
    if get_currency(IA2210SP.Penalty) > 0:
        return 'Worksheet'
    else:
        return ''

def Q1Ln19B_Calculation():
    if get_currency(IA2210SP.Penalty) > 0:
        return 'Attached'
    else:
        return ''

def Q1Undpay_Calculation():
    if get_currency(IA2210SP.Q1Est) < get_currency(IA2210SP.Q1Ln11):
        return get_currency(IA2210SP.Q1Ln11) - get_currency(IA2210SP.Q1Est)
    else:
        return 0

def Q1WH_Calculation():
    return c_dollar(CDbl(get_currency(IAF1040.BIATaxWith)) * 0.25)

def Q2AnInc_Calculation():
    if get_bool(IA2210SP.AnInc) == True:
        return get_currency(IA2210ANSP.Q2AIInstall)
    else:
        return 0

def Q2est_Calculation():
    return get_currency(IA2210SP.Q2WH) + get_currency(IASTATEEST.SPStQ2)

def Q2Install_Calculation():
    return c_dollar(CDbl(get_currency(IA2210SP.Small) - get_currency(IA2210SP.Q1Install)) * 0.3333)

def Q2Ln11_Calculation():
    if get_bool(IA2210SP.AnInc) == True:
        return get_currency(IA2210SP.Q2AnInc)
    else:
        return get_currency(IA2210SP.Q2Install)

def Q2WH_Calculation():
    return c_dollar(CDbl(get_currency(IAF1040.BIATaxWith) - get_currency(IA2210SP.Q1WH)) * 0.3333)

def Q3AnInc_Calculation():
    if get_bool(IA2210SP.AnInc) == True:
        return get_currency(IA2210ANSP.Q3AIInstall)
    else:
        return 0

def Q3Est_Calculation():
    return get_currency(IA2210SP.Q3WH) + get_currency(IASTATEEST.SPStQ3)

def Q3Install_Calculation():
    return c_dollar(CDbl(get_currency(IA2210SP.Small) - get_currency(IA2210SP.Q1Install) - get_currency(IA2210SP.Q2Install)) * 0.5)

def Q3Ln11_Calculation():
    if get_bool(IA2210SP.AnInc) == True:
        return get_currency(IA2210SP.Q3AnInc)
    else:
        return get_currency(IA2210SP.Q3Install)

def Q3WH_Calculation():
    return c_dollar(CDbl(get_currency(IAF1040.BIATaxWith) - get_currency(IA2210SP.Q1WH) - get_currency(IA2210SP.Q2WH)) * 0.5)

def Q4AnInc_Calculation():
    if get_bool(IA2210SP.AnInc) == True:
        return get_currency(IA2210ANSP.Q4AIInstall)
    else:
        return 0

def Q4Est_Calculation():
    return get_currency(IA2210SP.Q4WH) + get_currency(IASTATEEST.SPStQ4)

def Q4Install_Calculation():
    return get_currency(IA2210SP.Small) - get_currency(IA2210SP.Q1Install) - get_currency(IA2210SP.Q2Install) - get_currency(IA2210SP.Q3Install)

def Q4Ln11_Calculation():
    if get_bool(IA2210SP.AnInc) == True:
        return get_currency(IA2210SP.Q4AnInc)
    else:
        return get_currency(IA2210SP.Q4Install)

def Q4WH_Calculation():
    return get_currency(IAF1040.BIATaxWith) - get_currency(IA2210SP.Q1WH) - get_currency(IA2210SP.Q2WH) - get_currency(IA2210SP.Q3WH)

def RefundCr_Calculation():
    return get_currency(IAF1040.BOthRefCr)

def Small_Calculation():
    if get_bool(IAF1040.CombMFS) == False:
        return 0
    elif get_bool(IA2210SP.NoPen) == True:
        return 0
    elif get_currency(IA2210SP.Amt8) < Decimal("200"):
        return 0
    elif get_bool(IA2210SP.PYZero) == True:
        return 0
    elif get_currency(IA2210SP.PYTax) == 0:
        return get_currency(IA2210SP.Amt8)
    else:
        return min_value(get_currency(IA2210SP.Amt8), get_currency(IA2210SP.PYTax))

def SSN_Calculation():
    return get_string(IAF1040.SpouseSSN)

def TotCr_Calculation():
    return get_currency(IA2210SP.Fuel) + get_currency(IA2210SP.ChildC) + get_currency(IA2210SP.IAEIC) + get_currency(IA2210SP.RefundCr)


