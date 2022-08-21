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
    return max_value(0, get_currency(IA6251.AMTTaxInc) - get_currency(IA6251.Exemption2))

def AdjAMTInc2_Calculation():
    return max_value(0, get_currency(IA6251.AMTTaxInc) - get_currency(IA6251.AdjExempt))

def AdjExempt_Calculation():
    return max_value(0, get_currency(IA6251.Exemption1) - get_currency(IA6251.Multiply1))

def AdjGain_Calculation():
    return get_currency(USF6251.AdjGain)

def Alert10_Calculation():
    if get_bool(IAF1040.CombMFS) == True:
        if get_bool(IA6251SP.SpUserMod) == True:
            return 0
        elif get_currency(USF6251.AMT) > 0:
            return 1
        elif get_bool(IA6251.EFile) == True or get_bool(IA6251SP.EFile) == True:
            return 1
        else:
            return 0
    else:
        return 0

def Alert20_Calculation():
    #no AMT on bonus depr assets, believe there could be on 2018 nonconforming assets so should factor in IAWDepr.IANonConformDiffs
    if get_number(IA6251.DoNotComplete) == 1:
        return 0
    elif get_bool(IAWDepr.FedStSec179) > 0 or get_bool(IAWDepr.IANonConformDiffs) > 0:
        return 1
    else:
        return 0

def Alert30_Calculation():
    if get_number(IA6251.DoNotComplete) == 1:
        return 0
    elif get_bool(IAF1040.CombMFS) == True and  ( get_bool(IAWDepr.FedStSec179) > 0 or get_bool(IAWDepr.IANonConformDiffs) > 0 ) :
        return 1
    else:
        return 0

def Alert40_Calculation():
    MortIntAdj = Currency()
    MortIntAdj = get_currency(IAW6251MORTINT.MortInt98) + get_currency(IAW6251MORTINT.RefinInt) + get_currency(IAW6251MORTINT.OthInt)
    if get_bool(IAW6251MORTINT.OffMort) == False and get_currency(IAW6251MORTINT.TotMortInt) != 0 and MortIntAdj == 0:
        return 1
    else:
        return 0

def AMT_Calculation():
    return max_value(0, get_currency(IA6251.TentAMT) - get_currency(IA6251.RegTax))

def AMTInc_Calculation():
    return get_currency(IA6251.Med) + get_currency(IA6251.Taxes) + get_currency(IA6251.Int) + get_currency(IA6251.MiscDed) + get_currency(IA6251.ItmLimit) + get_currency(IA6251.TaxRfd) + get_currency(IA6251.InvInt) + get_currency(IA6251.Sec1202) + get_currency(IA6251.ISO) + get_currency(IA6251.Est) + get_currency(IA6251.LargePart) + get_currency(IA6251.AdjGain) + get_currency(IA6251.Post86Depr) + get_currency(IA6251.PALS) + get_currency(IA6251.LossLim) + get_currency(IA6251.Circ) + get_currency(IA6251.LTContr) + get_currency(IA6251.Mining) + get_currency(IA6251.Research) + get_currency(IA6251.Install) + get_currency(IA6251.RelAdj)

def AMTTaxInc_Calculation():
    return max_value(0, get_currency(IA6251.Subtotal) - get_currency(IA6251.LimAMTNOL))

def AskDepr_Calculation():
    #no AMT on bonus depr assets, believe there could be on 2018 nonconforming assets so should factor in IAWDepr.IANonConformDiffs
    if get_bool(IAWDepr.FedStSec179) > 0 or get_bool(IAWDepr.IANonConformDiffs) > 0:
        return 1
    else:
        return 0

def AskMortInt_Calculation():
    if get_bool(USWResidency.F1040NR) == True:
        return 0
    elif get_bool(IAF1040.ItemCheck) == True:
        if get_currency(IASCHA.Mort) != 0 or get_currency(IASCHA.MortNot) != 0 or get_currency(IASCHA.PtsNot) != 0 or get_currency(IASCHA.MtgePrem) != 0:
            return 1
        else:
            return 0
    else:
        return 0

def Circ_Calculation():
    return get_currency(USF6251.Circ)

def Description_Calculation():
    Total = Currency()
    Total = get_currency(IA6251.TotAMT)
    return CStr(Total) + ' AMT'

def DoNotComplete_Calculation():
    if IAFS() == 1:
        if get_bool(IAF1040.Over65) == True and get_currency(IAF1040.ANet) <= Decimal("24000"):
            return 1
        elif get_currency(IAF1040.ANet) <= Decimal("9000"):
            return 1
        else:
            return 0
    elif get_bool(IAF1040.Over65) == True and get_currency(IAREQUIRED.TotNI) <= Decimal("32000"):
        return 1
    elif get_currency(IAREQUIRED.TotNI) <= Decimal("13500"):
        return 1
    else:
        return 0

def EFile_Calculation():
    if get_number(IA6251.DoNotComplete) == 1:
        return 0
    elif get_bool(IA6251.Print) == True:
        return 1
    elif get_currency(IA6251.Med) != 0:
        return 1
    elif get_currency(IA6251.Taxes) != 0:
        return 1
    elif get_currency(IA6251.Int) != 0:
        return 1
    elif get_currency(IA6251.MiscDed) != 0:
        return 1
    elif get_currency(IA6251.ItmLimit) != 0:
        return 1
    elif get_currency(IA6251.TaxRfd) != 0:
        return 1
    elif get_currency(IA6251.InvInt) != 0:
        return 1
    elif get_currency(IA6251.Sec1202) != 0:
        return 1
    elif get_currency(IA6251.ISO) != 0:
        return 1
    elif get_currency(IA6251.Est) != 0:
        return 1
    elif get_currency(IA6251.LargePart) != 0:
        return 1
    elif get_currency(IA6251.AdjGain) != 0:
        return 1
    elif get_currency(IA6251.Post86Depr) != 0:
        return 1
    elif get_currency(IA6251.PALS) != 0:
        return 1
    elif get_currency(IA6251.LossLim) != 0:
        return 1
    elif get_currency(IA6251.Circ) != 0:
        return 1
    elif get_currency(IA6251.LTContr) != 0:
        return 1
    elif get_currency(IA6251.Mining) != 0:
        return 1
    elif get_currency(IA6251.Research) != 0:
        return 1
    elif get_currency(IA6251.Install) != 0:
        return 1
    elif get_currency(IA6251.RelAdj) != 0:
        return 1
    else:
        return 0

def Est_Calculation():
    return get_currency(USF6251.Est)

def Exemption1_Calculation():
    if get_bool(IAF1040.MFJ) == True:
        return Decimal("35000")
    elif get_bool(IAF1040.CombMFS) == True or get_bool(IAF1040.MFS) == True:
        return Decimal("17500")
    else:
        return Decimal("26000")

def Exemption2_Calculation():
    if get_bool(IAF1040.MFJ) == True:
        return Decimal("150000")
    elif get_bool(IAF1040.CombMFS) == True or get_bool(IAF1040.MFS) == True:
        return Decimal("75000")
    else:
        return Decimal("112500")

def Install_Calculation():
    return get_currency(USF6251.Install) * - 1

def Int_Calculation():
    if get_bool(IAF1040.CombMFS) == True and get_bool(IAF1040.ItemCheck) == True:
        return c_dollar(get_float(IASCHA.Perc) * get_float(IAW6251MORTINT.AMTInt))
    elif get_bool(IAF1040.ItemCheck) == True:
        return get_currency(IAW6251MORTINT.AMTInt)
    else:
        return 0

def InvInt_Calculation():
    if get_bool(IAF1040.CombMFS) == True and get_bool(IAF1040.ItemCheck) == True:
        return c_dollar(get_float(IASCHA.Perc) * get_float(USF6251.InvInt))
    elif get_bool(IAF1040.ItemCheck) == True:
        return get_currency(USF6251.InvInt)
    else:
        return 0

def ISO_Calculation():
    return get_currency(USF6251.ISO)

def ItmLimit_Calculation():
    if get_bool(IAF1040.CombMFS) == True and get_bool(IAF1040.ItemCheck) == True:
        return c_dollar(get_float(IASCHA.Perc) * get_float(IAWITMDED.Limit)) * - 1
    elif get_bool(IAF1040.ItemCheck) == True:
        return get_currency(IAWITMDED.Limit) * - 1
    else:
        return 0

def LargePart_Calculation():
    return get_currency(USF6251.LargePart)

def LimAMTNOL_Calculation():
    TEst = Currency()

    Unlim = Currency()

    AMTL = Currency()
    TEst = get_currency(IA6251.Subtotal)
    Unlim = Abs(get_currency(IA6251.AMTNOL))
    if TEst > 0:
        AMTL = min_value(Unlim, c_dollar(CDbl(TEst) * 0.9))
    else:
        AMTL = 0
    return AMTL

def LossLim_Calculation():
    return get_currency(USF6251.LossLim)

def LTContr_Calculation():
    return get_currency(USF6251.LTContr)

def Med_Calculation():
    return 0

def Mining_Calculation():
    return get_currency(USF6251.Mining)

def MiscDed_Calculation():
    if get_bool(IAF1040.CombMFS) == True and get_bool(IAF1040.ItemCheck) == True:
        return c_dollar(get_float(IASCHA.Perc) * get_float(IASCHA.AllowExp))
    elif get_bool(IAF1040.ItemCheck) == True:
        return get_currency(IASCHA.AllowExp)
    else:
        return 0

def Multiply1_Calculation():
    return c_dollar(get_float(IA6251.AdjAMTInc1) * 0.25)

def Names_Calculation():
    if get_bool(IAF1040.CombMFS) == True:
        return get_string(IAREQUIRED.TPCombName)
    else:
        return get_string(IAREQUIRED.CombNames)

def NOL_Calculation():
    if get_bool(IAF1040.CombMFS) == True:
        return get_currency(IAOTHADJ.TIANOL)
    else:
        return get_currency(IAOTHADJ.TIANOL) + get_currency(IAOTHADJ.SIANOL)

def PALS_Calculation():
    return get_currency(USF6251.PALs)

def Post86Depr_Calculation():
    #review new line 13 instructions and determine if we need to make an adjustment for any IA depr differences or if we should add an alert and note in Q&A
    #For 2017 added alerts and Q&A for taxpayer and spouse 6251
    return get_currency(USF6251.Post86Depr)

def PrInstall_Calculation():
    return Abs(get_currency(IA6251.Install))

def Print_Calculation():
    if get_currency(IA6251.TotAMT) > 0:
        return 1
    else:
        return 0

def PrItmLimit_Calculation():
    return Abs(get_currency(IA6251.ItmLimit))

def PrTaxRfd_Calculation():
    return Abs(get_currency(IA6251.TaxRfd))

def PYNRAMT_Calculation():
    return max_value(0, c_dollar(get_float(IA6251.AMT) * get_float(IA6251.PYNRRatio)))

def PYNRAMTIncNI_Calculation():
    if get_bool(IAF126.TpPYNR) == True:
        return max_value(0, get_currency(IAF126.ANet) + get_currency(IA6251.PYNRAMTInc))
    else:
        return 0

def PYNRRatio_Calculation():
    if get_currency(IA6251.TotAMTInc) == 0:
        return 0
    else:
        return min_value(1, Round(get_float(IA6251.PYNRAMTIncNI) / get_float(IA6251.TotAMTInc), 3))

def RegTax_Calculation():
    return max_value(0, get_currency(IAF1040.AAltTax) - get_currency(IAF1040.AExemCr))

def RelAdj_Calculation():
    #need to verify if should remove fed 6251 line 3 amounts for .F461 and .F8990 and .stdDed, seems like should remove since these were not preference items in the past and are only being made on federal due to TCJA and both of these are Iowa nonconformity items.
    #.LargePart is on line 11 of IA 6251
    return get_currency(USF6251.RelAdj) - get_currency(USF6251.LargePart) - get_currency(USF6251.F461) - get_currency(USF6251.F8990) - get_currency(USF6251.StdDed)

def Research_Calculation():
    return get_currency(USF6251.Research)

def Sec1202_Calculation():
    return get_currency(USF6251.Sec1202)

def SSN_Calculation():
    return get_string(IAF1040.SSN)

def Subtotal_Calculation():
    return get_currency(IA6251.AMTInc) + get_currency(IA6251.TaxInc) + get_currency(IA6251.NOL)

def Taxes_Calculation():
    if get_bool(IAF1040.CombMFS) == True and get_bool(IAF1040.ItemCheck) == True:
        return c_dollar(get_float(IASCHA.Perc) * get_float(IASCHA.TaxPd))
    elif get_bool(IAF1040.ItemCheck) == True:
        return get_currency(IASCHA.TaxPd)
    else:
        return 0

def TaxInc_Calculation():
    return get_currency(IAF1040.ATaxInc)

def TaxRfd_Calculation():
    return get_currency(IAF1040.ARefund) * - 1

def TentAMT_Calculation():
    return c_dollar(get_float(IA6251.AdjAMTInc2) * 0.067)

def TotAMT_Calculation():
    if get_number(IA6251.DoNotComplete) == 1:
        return 0
    elif get_bool(IAF126.TpPYNR) == True:
        return get_currency(IA6251.PYNRAMT)
    else:
        return get_currency(IA6251.AMT)

def TotAMTInc_Calculation():
    if get_bool(IAF126.TpPYNR) == True:
        return max_value(0, get_currency(IAF126.AAllSource) + get_currency(IA6251.AMTInc))
    else:
        return 0


