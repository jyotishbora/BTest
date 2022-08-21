from forms.out import IA1040X
from forms.out import IA2210
from forms.out import IA2210AN
from forms.out import IA2210SP
from forms.out import IAF1040
from forms.out import IAPENALTY
from forms.out import IAREQUIRED
from forms.out import IASTATEEST
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Alert10_Calculation():
    if get_currency(IA2210.Penalty) > 0 and get_currency(IA2210.PYTax) == 0 and get_bool(IA2210.PYZero) == False:
        return 1
    else:
        return 0

def Alert20_Calculation():
    if get_currency(IA2210SP.Penalty) > 0 and get_currency(IA2210SP.PYTax) == 0 and get_bool(IA2210SP.PYZero) == False:
        return 1
    else:
        return 0

def Amt8_Calculation():
    return c_dollar(get_float(IA2210.Bal) * 0.9)

def Bal_Calculation():
    return max_value(0, get_currency(IA2210.CYTax) - get_currency(IA2210.TotCr))

def ChildC_Calculation():
    return get_currency(IAF1040.AChild)

def CYTax_Calculation():
    return get_currency(IAF1040.ABal4)

def Description_Calculation():
    return CStr(get_currency(IA2210.Penalty)) + ' Penalty'

def EFile_Calculation():
    if get_bool(IA1040X.EFAmend) == True:
        return 0
    elif get_bool(IA2210.Print) == True:
        return 1
    elif get_currency(IA2210.Amt8) >= Decimal("200"):
        return 1
    else:
        return 0

def EFStQ1_Calculation():
    return get_currency(IASTATEEST.TPStApply) + get_currency(IASTATEEST.TPStQ1)

def ExpPenalty_Calculation():
    if get_currency(IA2210.Penalty) > 0:
        return 1
    else:
        return 0

def Fuel_Calculation():
    return get_currency(IAF1040.AFuel)

def IAEIC_Calculation():
    return get_currency(IAF1040.AIEIC)

def Names_Calculation():
    if get_bool(IAF1040.CombMFS) == True:
        return get_string(IAREQUIRED.TPCombName)
    else:
        return get_string(IAREQUIRED.CombNames)

def NoPen_Calculation():
    return get_bool(USWPrepMnNm.AlwaysState2210)

def Penalty_Calculation():
    if get_bool(IA2210.NoPen) == True:
        return 0
    else:
        return get_currency(IAPENALTY.TotPen)

def Print_Calculation():
    if get_bool(IA2210.AnInc) == True:
        return 1
    elif get_currency(IA2210.Penalty) > 0:
        return 1
    else:
        return 0

def PYTax_Calculation():
    PYAGILimit = Currency()

    AGI = Currency()

    AGIBonus = Currency()
    if get_bool(USWSpouse.MFS) == True and get_bool(USWSpouse.NonRes) == False:
        PYAGILimit = Decimal("75000")
    else:
        PYAGILimit = Decimal("150000")
    if get_bool(USWSpouse.NonRes) == True:
        AGI = get_currency(USWRec.PYAGINR)
    elif IAFS() != 3:
        AGI = get_currency(USWRec.PYTAGI)
    else:
        AGI = get_currency(USWRec.PYAGI)
    if IAFS() != 3:
        AGIBonus = AGI + get_currency(USZIA1040.IATotBonus) + get_currency(USZIA1040.IATotBonusSp)
    else:
        AGIBonus = AGI + get_currency(USZIA1040.IATotBonus)
    if AGIBonus > PYAGILimit:
        return c_dollar(get_float(USZIA1040.IA2210PYTax) * 1.1)
    else:
        return get_currency(USZIA1040.IA2210PYTax)

def Q1AnInc_Calculation():
    if get_bool(IA2210.AnInc) == True:
        return get_currency(IA2210AN.Q1AIInstall)
    else:
        return 0

def Q1DaysB_Calculation():
    if get_currency(IA2210.Penalty) > 0:
        return 'See'
    else:
        return ''

def Q1Est_Calculation():
    return get_currency(IA2210.Q1WH) + get_currency(IASTATEEST.TPStApply) + get_currency(IASTATEEST.TPStQ1)

def Q1Install_Calculation():
    return c_dollar(get_float(IA2210.Small) * 0.25)

def Q1Ln11_Calculation():
    if get_bool(IA2210.AnInc) == True:
        return get_currency(IA2210.Q1AnInc)
    else:
        return get_currency(IA2210.Q1Install)

def Q1Ln19a_Calculation():
    if get_currency(IA2210.Penalty) > 0:
        return 'Worksheet'
    else:
        return ''

def Q1Ln19B_Calculation():
    if get_currency(IA2210.Penalty) > 0:
        return 'Attached'
    else:
        return ''

def Q1Undpay_Calculation():
    if get_currency(IA2210.Q1Est) < get_currency(IA2210.Q1Ln11):
        return get_currency(IA2210.Q1Ln11) - get_currency(IA2210.Q1Est)
    else:
        return 0

def Q1WH_Calculation():
    return c_dollar(CDbl(get_currency(IAF1040.AIATaxWith)) * 0.25)

def Q2AnInc_Calculation():
    if get_bool(IA2210.AnInc) == True:
        return get_currency(IA2210AN.Q2AIInstall)
    else:
        return 0

def Q2est_Calculation():
    return get_currency(IA2210.Q2WH) + get_currency(IASTATEEST.TPStQ2)

def Q2Install_Calculation():
    return c_dollar(CDbl(get_currency(IA2210.Small) - get_currency(IA2210.Q1Install)) * 0.3333)

def Q2Ln11_Calculation():
    if get_bool(IA2210.AnInc) == True:
        return get_currency(IA2210.Q2AnInc)
    else:
        return get_currency(IA2210.Q2Install)

def Q2WH_Calculation():
    return c_dollar(CDbl(get_currency(IAF1040.AIATaxWith) - get_currency(IA2210.Q1WH)) * 0.3333)

def Q3AnInc_Calculation():
    if get_bool(IA2210.AnInc) == True:
        return get_currency(IA2210AN.Q3AIInstall)
    else:
        return 0

def Q3Est_Calculation():
    return get_currency(IA2210.Q3WH) + get_currency(IASTATEEST.TPStQ3)

def Q3Install_Calculation():
    return c_dollar(CDbl(get_currency(IA2210.Small) - get_currency(IA2210.Q1Install) - get_currency(IA2210.Q2Install)) * 0.5)

def Q3Ln11_Calculation():
    if get_bool(IA2210.AnInc) == True:
        return get_currency(IA2210.Q3AnInc)
    else:
        return get_currency(IA2210.Q3Install)

def Q3WH_Calculation():
    return c_dollar(CDbl(get_currency(IAF1040.AIATaxWith) - get_currency(IA2210.Q1WH) - get_currency(IA2210.Q2WH)) * 0.5)

def Q4AnInc_Calculation():
    if get_bool(IA2210.AnInc) == True:
        return get_currency(IA2210AN.Q4AIInstall)
    else:
        return 0

def Q4Est_Calculation():
    return get_currency(IA2210.Q4WH) + get_currency(IASTATEEST.TPStQ4)

def Q4Install_Calculation():
    return get_currency(IA2210.Small) - get_currency(IA2210.Q1Install) - get_currency(IA2210.Q2Install) - get_currency(IA2210.Q3Install)

def Q4Ln11_Calculation():
    if get_bool(IA2210.AnInc) == True:
        return get_currency(IA2210.Q4AnInc)
    else:
        return get_currency(IA2210.Q4Install)

def Q4WH_Calculation():
    return get_currency(IAF1040.AIATaxWith) - get_currency(IA2210.Q1WH) - get_currency(IA2210.Q2WH) - get_currency(IA2210.Q3WH)

def RefundCr_Calculation():
    return get_currency(IAF1040.AOthRefCr)

def Small_Calculation():
    if get_bool(IA2210.NoPen) == True:
        return 0
    elif get_currency(IA2210.Amt8) < Decimal("200"):
        return 0
    elif get_bool(IA2210.PYZero) == True:
        return 0
    elif get_currency(IA2210.PYTax) == 0:
        return get_currency(IA2210.Amt8)
    else:
        return min_value(get_currency(IA2210.Amt8), get_currency(IA2210.PYTax))

def SSN_Calculation():
    return get_string(IAF1040.SSN)

def TotCr_Calculation():
    return get_currency(IA2210.Fuel) + get_currency(IA2210.ChildC) + get_currency(IA2210.IAEIC) + get_currency(IA2210.RefundCr)


