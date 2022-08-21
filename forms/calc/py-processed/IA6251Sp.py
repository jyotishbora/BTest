from forms.out import IA6251
from forms.out import IA6251SP
from forms.out import IAF1040
from forms.out import IAF126
from forms.out import IAOTHADJ
from forms.out import IAREQUIRED
from forms.out import IASCHA
from forms.out import IAW6251MORTINT
from forms.out import IAWITMDED
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def AdjAMTInc1_Calculation():
    return max_value(0, get_currency(IA6251SP.AMTTaxInc) - get_currency(IA6251SP.Exemption2))

def AdjAMTInc2_Calculation():
    return max_value(0, get_currency(IA6251SP.AMTTaxInc) - get_currency(IA6251SP.AdjExempt))

def AdjExempt_Calculation():
    return max_value(0, get_currency(IA6251SP.Exemption1) - get_currency(IA6251SP.Multiply1))

def AdjGain_Calculation():
    if get_bool(IAF1040.CombMFS) == True:
        return max_value(0, get_currency(USF6251.AdjGain) - get_currency(IA6251.AdjGain))
    else:
        return 0

def AMT_Calculation():
    return max_value(0, get_currency(IA6251SP.TentAMT) - get_currency(IA6251SP.RegTax))

def AMTInc_Calculation():
    return get_currency(IA6251SP.Med) + get_currency(IA6251SP.Taxes) + get_currency(IA6251SP.Int) + get_currency(IA6251SP.MiscDed) + get_currency(IA6251SP.ItmLimit) + get_currency(IA6251SP.TaxRfd) + get_currency(IA6251SP.InvInt) + get_currency(IA6251SP.Sec1202) + get_currency(IA6251SP.ISO) + get_currency(IA6251SP.Est) + get_currency(IA6251SP.LargePart) + get_currency(IA6251SP.AdjGain) + get_currency(IA6251SP.Post86Depr) + get_currency(IA6251SP.PALS) + get_currency(IA6251SP.LossLim) + get_currency(IA6251SP.Circ) + get_currency(IA6251SP.LTContr) + get_currency(IA6251SP.Mining) + get_currency(IA6251SP.Research) + get_currency(IA6251SP.Install) + get_currency(IA6251SP.RelAdj)

def AMTTaxInc_Calculation():
    return max_value(0, get_currency(IA6251SP.Subtotal) - get_currency(IA6251SP.LimAMTNOL))

def Circ_Calculation():
    if get_bool(IAF1040.CombMFS) == True:
        return max_value(0, get_currency(USF6251.Circ) - get_currency(IA6251.Circ))
    else:
        return 0

def Description_Calculation():
    Total = Currency()
    Total = get_currency(IA6251SP.TotAMT)
    return CStr(Total) + ' AMT'

def EFile_Calculation():
    if get_number(IA6251.DoNotComplete) == 1:
        return 0
    elif get_bool(IA6251SP.Print) == True:
        return 1
    elif get_currency(IA6251SP.Med) != 0:
        return 1
    elif get_currency(IA6251SP.Taxes) != 0:
        return 1
    elif get_currency(IA6251SP.Int) != 0:
        return 1
    elif get_currency(IA6251SP.MiscDed) != 0:
        return 1
    elif get_currency(IA6251SP.ItmLimit) != 0:
        return 1
    elif get_currency(IA6251SP.TaxRfd) != 0:
        return 1
    elif get_currency(IA6251SP.InvInt) != 0:
        return 1
    elif get_currency(IA6251SP.Sec1202) != 0:
        return 1
    elif get_currency(IA6251SP.ISO) != 0:
        return 1
    elif get_currency(IA6251SP.Est) != 0:
        return 1
    elif get_currency(IA6251SP.LargePart) != 0:
        return 1
    elif get_currency(IA6251SP.AdjGain) != 0:
        return 1
    elif get_currency(IA6251SP.Post86Depr) != 0:
        return 1
    elif get_currency(IA6251SP.PALS) != 0:
        return 1
    elif get_currency(IA6251SP.LossLim) != 0:
        return 1
    elif get_currency(IA6251SP.Circ) != 0:
        return 1
    elif get_currency(IA6251SP.LTContr) != 0:
        return 1
    elif get_currency(IA6251SP.Mining) != 0:
        return 1
    elif get_currency(IA6251SP.Research) != 0:
        return 1
    elif get_currency(IA6251SP.Install) != 0:
        return 1
    elif get_currency(IA6251SP.RelAdj) != 0:
        return 1
    else:
        return 0

def Est_Calculation():
    if get_bool(IAF1040.CombMFS) == True:
        return max_value(0, get_currency(USF6251.Est) - get_currency(IA6251.Est))
    else:
        return 0

def Exemption1_Calculation():
    if get_bool(IAF1040.CombMFS) == True:
        return Decimal("17500")
    else:
        return 0

def Exemption2_Calculation():
    if get_bool(IAF1040.CombMFS) == True:
        return Decimal("75000")
    else:
        return 0

def Install_Calculation():
    FedInstall = Currency()
    FedInstall = get_currency(USF6251.Install) * - 1
    if get_bool(IAF1040.CombMFS) == True:
        return FedInstall - get_currency(IA6251.Install)
    else:
        return 0

def Int_Calculation():
    if get_bool(IAF1040.CombMFS) == True and get_bool(IAF1040.ItemCheck) == True:
        return max_value(0, get_currency(IAW6251MORTINT.AMTInt) - get_currency(IA6251.Int))
    else:
        return 0

def InvInt_Calculation():
    if get_bool(IAF1040.CombMFS) == True and get_bool(IAF1040.ItemCheck) == True:
        return max_value(0, get_currency(USF6251.InvInt) - get_currency(IA6251.InvInt))
    else:
        return 0

def ISO_Calculation():
    if get_bool(IAF1040.CombMFS) == True:
        return max_value(0, get_currency(USF6251.ISO) - get_currency(IA6251.ISO))
    else:
        return 0

def ItmLimit_Calculation():
    Limit = Currency()
    Limit = get_currency(IAWITMDED.Limit) * - 1
    if get_bool(IAF1040.CombMFS) == True and get_bool(IAF1040.ItemCheck) == True:
        return Limit - get_currency(IA6251.ItmLimit)
    else:
        return 0

def LargePart_Calculation():
    if get_bool(IAF1040.CombMFS) == True:
        return max_value(0, get_currency(USF6251.LargePart) - get_currency(IA6251.LargePart))
    else:
        return 0

def LimAMTNOL_Calculation():
    TEst = Currency()

    Unlim = Currency()

    AMTL = Currency()
    TEst = get_currency(IA6251SP.Subtotal)
    Unlim = Abs(get_currency(IA6251SP.AMTNOL))
    if TEst > 0:
        AMTL = min_value(Unlim, c_dollar(CDbl(TEst) * 0.9))
    else:
        AMTL = 0
    if get_bool(IAF1040.CombMFS) == True:
        return AMTL
    else:
        return 0

def LossLim_Calculation():
    if get_bool(IAF1040.CombMFS) == True:
        return max_value(0, get_currency(USF6251.LossLim) - get_currency(IA6251.LossLim))
    else:
        return 0

def LTContr_Calculation():
    if get_bool(IAF1040.CombMFS) == True:
        return max_value(0, get_currency(USF6251.LTContr) - get_currency(IA6251.LTContr))
    else:
        return 0

def Med_Calculation():
    return 0

def Mining_Calculation():
    if get_bool(IAF1040.CombMFS) == True:
        return max_value(0, get_currency(USF6251.Mining) - get_currency(IA6251.Mining))
    else:
        return 0

def MiscDed_Calculation():
    if get_bool(IAF1040.CombMFS) == True and get_bool(IAF1040.ItemCheck) == True:
        return max_value(0, get_currency(IASCHA.AllowExp) - get_currency(IA6251.MiscDed))
    else:
        return 0

def Multiply1_Calculation():
    return c_dollar(get_float(IA6251SP.AdjAMTInc1) * 0.25)

def Names_Calculation():
    return get_string(IAREQUIRED.SPCombName)

def NOL_Calculation():
    if get_bool(IAF1040.CombMFS) == True:
        return get_currency(IAOTHADJ.SIANOL)
    else:
        return 0

def PALS_Calculation():
    if get_bool(IAF1040.CombMFS) == True:
        return max_value(0, get_currency(USF6251.PALS) - get_currency(IA6251.PALS))
    else:
        return 0

def Post86Depr_Calculation():
    #review new line 13 instructions and determine if we need to make an adjustment for any IA depr differences or if we should add an alert and note in Q&A
    #For 2017 changed to default calc this field and interview and added an alert
    if get_bool(IAF1040.CombMFS) == True:
        return max_value(0, get_currency(USF6251.Post86Depr) - get_currency(IA6251.Post86Depr))
    else:
        return 0

def PrInstall_Calculation():
    return Abs(get_currency(IA6251SP.Install))

def Print_Calculation():
    if get_bool(IAF1040.CombMFS) == False:
        return 0
    elif get_currency(IA6251SP.TotAMT) > 0:
        return 1
    else:
        return 0

def PrItmLimit_Calculation():
    return Abs(get_currency(IA6251SP.ItmLimit))

def PrTaxRfd_Calculation():
    return Abs(get_currency(IA6251SP.TaxRfd))

def PYNRAMT_Calculation():
    return max_value(0, c_dollar(get_float(IA6251SP.AMT) * get_float(IA6251SP.PYNRRatio)))

def PYNRAMTIncNI_Calculation():
    if get_bool(IAF126.SpPYNR) == True:
        return max_value(0, get_currency(IAF126.BNet) + get_currency(IA6251SP.PYNRAMTInc))
    else:
        return 0

def PYNRRatio_Calculation():
    if get_currency(IA6251SP.TotAMTInc) == 0:
        return 0
    else:
        return min_value(1, Round(get_float(IA6251SP.PYNRAMTIncNI) / get_float(IA6251SP.TotAMTInc), 3))

def RegTax_Calculation():
    if get_bool(IAF1040.CombMFS) == True:
        return max_value(0, get_currency(IAF1040.BAltTax) - get_currency(IAF1040.BExemCr))
    else:
        return 0

def RelAdj_Calculation():
    IARelAdj = Currency()
    IARelAdj = get_currency(USF6251.RelAdj) - get_currency(USF6251.LargePart) - get_currency(USF6251.F461) - get_currency(USF6251.F8990) - get_currency(USF6251.StdDed)
    if get_bool(IAF1040.CombMFS) == True:
        return max_value(0, IARelAdj - get_currency(IA6251.RelAdj))
    else:
        return 0

def Research_Calculation():
    if get_bool(IAF1040.CombMFS) == True:
        return max_value(0, get_currency(USF6251.Research) - get_currency(IA6251.Research))
    else:
        return 0

def Sec1202_Calculation():
    if get_bool(IAF1040.CombMFS) == True:
        return max_value(0, get_currency(USF6251.Sec1202) - get_currency(IA6251.Sec1202))
    else:
        return 0

def SpUserMod_Calculation():
    if GetStatus(UserModifiedStatus) == True:
        return 1
    else:
        return 0

def SSN_Calculation():
    return get_string(IAF1040.SpouseSSN)

def Subtotal_Calculation():
    return get_currency(IA6251SP.AMTInc) + get_currency(IA6251SP.TaxInc) + get_currency(IA6251SP.NOL)

def Taxes_Calculation():
    if get_bool(IAF1040.CombMFS) == True and get_bool(IAF1040.ItemCheck) == True:
        return max_value(0, get_currency(IASCHA.TaxPd) - get_currency(IA6251.Taxes))
    else:
        return 0

def TaxInc_Calculation():
    if get_bool(IAF1040.CombMFS) == True:
        return get_currency(IAF1040.BTaxInc)
    else:
        return 0

def TaxRfd_Calculation():
    if get_bool(IAF1040.CombMFS) == True:
        return get_currency(IAF1040.BRefund) * - 1
    else:
        return 0

def TentAMT_Calculation():
    return c_dollar(get_float(IA6251SP.AdjAMTInc2) * 0.067)

def TotAMT_Calculation():
    if get_number(IA6251.DoNotComplete) == 1:
        return 0
    elif get_bool(IAF1040.CombMFS) == False:
        return 0
    elif get_bool(IAF126.SpPYNR) == True:
        return get_currency(IA6251SP.PYNRAMT)
    else:
        return get_currency(IA6251SP.AMT)

def TotAMTInc_Calculation():
    if get_bool(IAF126.SpPYNR) == True:
        return max_value(0, get_currency(IAF126.BAllSource) + get_currency(IA6251SP.AMTInc))
    else:
        return 0


