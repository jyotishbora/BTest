from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def AdjAMTInc1_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA6251.AMTTaxInc) - GetCurrency(IA6251.Exemption2))

def AdjAMTInc2_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA6251.AMTTaxInc) - GetCurrency(IA6251.AdjExempt))

def AdjExempt_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA6251.Exemption1) - GetCurrency(IA6251.Multiply1))

def AdjGain_Calculation():
    ReturnVal = GetCurrency(USF6251.AdjGain)

def Alert10_Calculation():
    if GetBool(IAF1040.CombMFS) == True:
        if GetBool(IA6251Sp.SpUserMod) == True:
            ReturnVal = 0
        elif GetCurrency(USF6251.AMT) > 0:
            ReturnVal = 1
        elif GetBool(IA6251.EFile) == True or GetBool(IA6251Sp.EFile) == True:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def Alert20_Calculation():
    #no AMT on bonus depr assets, believe there could be on 2018 nonconforming assets so should factor in IAWDepr.IANonConformDiffs
    if GetNumber(IA6251.DoNotComplete) == 1:
        ReturnVal = 0
    elif GetBool(IAWDepr.FedStSec179) > 0 or GetBool(IAWDepr.IANonConformDiffs) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert30_Calculation():
    if GetNumber(IA6251.DoNotComplete) == 1:
        ReturnVal = 0
    elif GetBool(IAF1040.CombMFS) == True and  ( GetBool(IAWDepr.FedStSec179) > 0 or GetBool(IAWDepr.IANonConformDiffs) > 0 ) :
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert40_Calculation():
    MortIntAdj = Currency()
    MortIntAdj = GetCurrency(IAW6251MortInt.MortInt98) + GetCurrency(IAW6251MortInt.RefinInt) + GetCurrency(IAW6251MortInt.OthInt)
    if GetBool(IAW6251MortInt.OffMort) == False and GetCurrency(IAW6251MortInt.TotMortInt) != 0 and MortIntAdj == 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def AMT_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA6251.TentAMT) - GetCurrency(IA6251.RegTax))

def AMTInc_Calculation():
    ReturnVal = GetCurrency(IA6251.Med) + GetCurrency(IA6251.Taxes) + GetCurrency(IA6251.Int) + GetCurrency(IA6251.MiscDed) + GetCurrency(IA6251.ItmLimit) + GetCurrency(IA6251.TaxRfd) + GetCurrency(IA6251.InvInt) + GetCurrency(IA6251.Sec1202) + GetCurrency(IA6251.ISO) + GetCurrency(IA6251.Est) + GetCurrency(IA6251.LargePart) + GetCurrency(IA6251.AdjGain) + GetCurrency(IA6251.Post86Depr) + GetCurrency(IA6251.PALS) + GetCurrency(IA6251.LossLim) + GetCurrency(IA6251.Circ) + GetCurrency(IA6251.LTContr) + GetCurrency(IA6251.Mining) + GetCurrency(IA6251.Research) + GetCurrency(IA6251.Install) + GetCurrency(IA6251.RelAdj)

def AMTTaxInc_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA6251.Subtotal) - GetCurrency(IA6251.LimAMTNOL))

def AskDepr_Calculation():
    #no AMT on bonus depr assets, believe there could be on 2018 nonconforming assets so should factor in IAWDepr.IANonConformDiffs
    if GetBool(IAWDepr.FedStSec179) > 0 or GetBool(IAWDepr.IANonConformDiffs) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def AskMortInt_Calculation():
    if GetBool(USWResidency.F1040NR) == True:
        ReturnVal = 0
    elif GetBool(IAF1040.ItemCheck) == True:
        if GetCurrency(IASchA.Mort) != 0 or GetCurrency(IASchA.MortNot) != 0 or GetCurrency(IASchA.PtsNot) != 0 or GetCurrency(IASchA.MtgePrem) != 0:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def Circ_Calculation():
    ReturnVal = GetCurrency(USF6251.Circ)

def Description_Calculation():
    Total = Currency()
    Total = GetCurrency(IA6251.TotAMT)
    ReturnVal = CStr(Total) + ' AMT'

def DoNotComplete_Calculation():
    if IAFS() == 1:
        if GetBool(IAF1040.Over65) == True and GetCurrency(IAF1040.ANet) <= Decimal("24000"):
            ReturnVal = 1
        elif GetCurrency(IAF1040.ANet) <= Decimal("9000"):
            ReturnVal = 1
        else:
            ReturnVal = 0
    elif GetBool(IAF1040.Over65) == True and GetCurrency(IARequired.TotNI) <= Decimal("32000"):
        ReturnVal = 1
    elif GetCurrency(IARequired.TotNI) <= Decimal("13500"):
        ReturnVal = 1
    else:
        ReturnVal = 0

def EFile_Calculation():
    if GetNumber(IA6251.DoNotComplete) == 1:
        ReturnVal = 0
    elif GetBool(IA6251.Print) == True:
        ReturnVal = 1
    elif GetCurrency(IA6251.Med) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251.Taxes) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251.Int) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251.MiscDed) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251.ItmLimit) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251.TaxRfd) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251.InvInt) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251.Sec1202) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251.ISO) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251.Est) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251.LargePart) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251.AdjGain) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251.Post86Depr) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251.PALS) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251.LossLim) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251.Circ) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251.LTContr) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251.Mining) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251.Research) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251.Install) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251.RelAdj) != 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Est_Calculation():
    ReturnVal = GetCurrency(USF6251.Est)

def Exemption1_Calculation():
    if GetBool(IAF1040.MFJ) == True:
        ReturnVal = Decimal("35000")
    elif GetBool(IAF1040.CombMFS) == True or GetBool(IAF1040.MFS) == True:
        ReturnVal = Decimal("17500")
    else:
        ReturnVal = Decimal("26000")

def Exemption2_Calculation():
    if GetBool(IAF1040.MFJ) == True:
        ReturnVal = Decimal("150000")
    elif GetBool(IAF1040.CombMFS) == True or GetBool(IAF1040.MFS) == True:
        ReturnVal = Decimal("75000")
    else:
        ReturnVal = Decimal("112500")

def Install_Calculation():
    ReturnVal = GetCurrency(USF6251.Install) * - 1

def Int_Calculation():
    if GetBool(IAF1040.CombMFS) == True and GetBool(IAF1040.ItemCheck) == True:
        ReturnVal = CDollar(GetFloat(IASchA.Perc) * GetFloat(IAW6251MortInt.AMTInt))
    elif GetBool(IAF1040.ItemCheck) == True:
        ReturnVal = GetCurrency(IAW6251MortInt.AMTInt)
    else:
        ReturnVal = 0

def InvInt_Calculation():
    if GetBool(IAF1040.CombMFS) == True and GetBool(IAF1040.ItemCheck) == True:
        ReturnVal = CDollar(GetFloat(IASchA.Perc) * GetFloat(USF6251.InvInt))
    elif GetBool(IAF1040.ItemCheck) == True:
        ReturnVal = GetCurrency(USF6251.InvInt)
    else:
        ReturnVal = 0

def ISO_Calculation():
    ReturnVal = GetCurrency(USF6251.ISO)

def ItmLimit_Calculation():
    if GetBool(IAF1040.CombMFS) == True and GetBool(IAF1040.ItemCheck) == True:
        ReturnVal = CDollar(GetFloat(IASchA.Perc) * GetFloat(IAWItmDed.Limit)) * - 1
    elif GetBool(IAF1040.ItemCheck) == True:
        ReturnVal = GetCurrency(IAWItmDed.Limit) * - 1
    else:
        ReturnVal = 0

def LargePart_Calculation():
    ReturnVal = GetCurrency(USF6251.LargePart)

def LimAMTNOL_Calculation():
    TEst = Currency()

    Unlim = Currency()

    AMTL = Currency()
    TEst = GetCurrency(IA6251.Subtotal)
    Unlim = Abs(GetCurrency(IA6251.AMTNOL))
    if TEst > 0:
        AMTL = MinValue(Unlim, CDollar(CDbl(TEst) * 0.9))
    else:
        AMTL = 0
    ReturnVal = AMTL

def LossLim_Calculation():
    ReturnVal = GetCurrency(USF6251.LossLim)

def LTContr_Calculation():
    ReturnVal = GetCurrency(USF6251.LTContr)

def Med_Calculation():
    ReturnVal = 0

def Mining_Calculation():
    ReturnVal = GetCurrency(USF6251.Mining)

def MiscDed_Calculation():
    if GetBool(IAF1040.CombMFS) == True and GetBool(IAF1040.ItemCheck) == True:
        ReturnVal = CDollar(GetFloat(IASchA.Perc) * GetFloat(IASchA.AllowExp))
    elif GetBool(IAF1040.ItemCheck) == True:
        ReturnVal = GetCurrency(IASchA.AllowExp)
    else:
        ReturnVal = 0

def Multiply1_Calculation():
    ReturnVal = CDollar(GetFloat(IA6251.AdjAMTInc1) * 0.25)

def Names_Calculation():
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetString(IARequired.TPCombName)
    else:
        ReturnVal = GetString(IARequired.CombNames)

def NOL_Calculation():
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetCurrency(IAOthAdj.TIANOL)
    else:
        ReturnVal = GetCurrency(IAOthAdj.TIANOL) + GetCurrency(IAOthAdj.SIANOL)

def PALS_Calculation():
    ReturnVal = GetCurrency(USF6251.PALs)

def Post86Depr_Calculation():
    #review new line 13 instructions and determine if we need to make an adjustment for any IA depr differences or if we should add an alert and note in Q&A
    #For 2017 added alerts and Q&A for taxpayer and spouse 6251
    ReturnVal = GetCurrency(USF6251.Post86Depr)

def PrInstall_Calculation():
    ReturnVal = Abs(GetCurrency(IA6251.Install))

def Print_Calculation():
    if GetCurrency(IA6251.TotAMT) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def PrItmLimit_Calculation():
    ReturnVal = Abs(GetCurrency(IA6251.ItmLimit))

def PrTaxRfd_Calculation():
    ReturnVal = Abs(GetCurrency(IA6251.TaxRfd))

def PYNRAMT_Calculation():
    ReturnVal = MaxValue(0, CDollar(GetFloat(IA6251.AMT) * GetFloat(IA6251.PYNRRatio)))

def PYNRAMTIncNI_Calculation():
    if GetBool(IAF126.TpPYNR) == True:
        ReturnVal = MaxValue(0, GetCurrency(IAF126.ANet) + GetCurrency(IA6251.PYNRAMTInc))
    else:
        ReturnVal = 0

def PYNRRatio_Calculation():
    if GetCurrency(IA6251.TotAMTInc) == 0:
        ReturnVal = 0
    else:
        ReturnVal = MinValue(1, Round(GetFloat(IA6251.PYNRAMTIncNI) / GetFloat(IA6251.TotAMTInc), 3))

def RegTax_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAF1040.AAltTax) - GetCurrency(IAF1040.AExemCr))

def RelAdj_Calculation():
    #need to verify if should remove fed 6251 line 3 amounts for .F461 and .F8990 and .stdDed, seems like should remove since these were not preference items in the past and are only being made on federal due to TCJA and both of these are Iowa nonconformity items.
    #.LargePart is on line 11 of IA 6251
    ReturnVal = GetCurrency(USF6251.RelAdj) - GetCurrency(USF6251.LargePart) - GetCurrency(USF6251.F461) - GetCurrency(USF6251.F8990) - GetCurrency(USF6251.StdDed)

def Research_Calculation():
    ReturnVal = GetCurrency(USF6251.Research)

def Sec1202_Calculation():
    ReturnVal = GetCurrency(USF6251.Sec1202)

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

def Subtotal_Calculation():
    ReturnVal = GetCurrency(IA6251.AMTInc) + GetCurrency(IA6251.TaxInc) + GetCurrency(IA6251.NOL)

def Taxes_Calculation():
    if GetBool(IAF1040.CombMFS) == True and GetBool(IAF1040.ItemCheck) == True:
        ReturnVal = CDollar(GetFloat(IASchA.Perc) * GetFloat(IASchA.TaxPd))
    elif GetBool(IAF1040.ItemCheck) == True:
        ReturnVal = GetCurrency(IASchA.TaxPd)
    else:
        ReturnVal = 0

def TaxInc_Calculation():
    ReturnVal = GetCurrency(IAF1040.ATaxInc)

def TaxRfd_Calculation():
    ReturnVal = GetCurrency(IAF1040.ARefund) * - 1

def TentAMT_Calculation():
    ReturnVal = CDollar(GetFloat(IA6251.AdjAMTInc2) * 0.067)

def TotAMT_Calculation():
    if GetNumber(IA6251.DoNotComplete) == 1:
        ReturnVal = 0
    elif GetBool(IAF126.TpPYNR) == True:
        ReturnVal = GetCurrency(IA6251.PYNRAMT)
    else:
        ReturnVal = GetCurrency(IA6251.AMT)

def TotAMTInc_Calculation():
    if GetBool(IAF126.TpPYNR) == True:
        ReturnVal = MaxValue(0, GetCurrency(IAF126.AAllSource) + GetCurrency(IA6251.AMTInc))
    else:
        ReturnVal = 0

