from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def AdjAMTInc1_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA6251Sp.AMTTaxInc) - GetCurrency(IA6251Sp.Exemption2))

def AdjAMTInc2_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA6251Sp.AMTTaxInc) - GetCurrency(IA6251Sp.AdjExempt))

def AdjExempt_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA6251Sp.Exemption1) - GetCurrency(IA6251Sp.Multiply1))

def AdjGain_Calculation():
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = MaxValue(0, GetCurrency(USF6251.AdjGain) - GetCurrency(IA6251.AdjGain))
    else:
        ReturnVal = 0

def AMT_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA6251Sp.TentAMT) - GetCurrency(IA6251Sp.RegTax))

def AMTInc_Calculation():
    ReturnVal = GetCurrency(IA6251Sp.Med) + GetCurrency(IA6251Sp.Taxes) + GetCurrency(IA6251Sp.Int) + GetCurrency(IA6251Sp.MiscDed) + GetCurrency(IA6251Sp.ItmLimit) + GetCurrency(IA6251Sp.TaxRfd) + GetCurrency(IA6251Sp.InvInt) + GetCurrency(IA6251Sp.Sec1202) + GetCurrency(IA6251Sp.ISO) + GetCurrency(IA6251Sp.Est) + GetCurrency(IA6251Sp.LargePart) + GetCurrency(IA6251Sp.AdjGain) + GetCurrency(IA6251Sp.Post86Depr) + GetCurrency(IA6251Sp.PALS) + GetCurrency(IA6251Sp.LossLim) + GetCurrency(IA6251Sp.Circ) + GetCurrency(IA6251Sp.LTContr) + GetCurrency(IA6251Sp.Mining) + GetCurrency(IA6251Sp.Research) + GetCurrency(IA6251Sp.Install) + GetCurrency(IA6251Sp.RelAdj)

def AMTTaxInc_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA6251Sp.Subtotal) - GetCurrency(IA6251Sp.LimAMTNOL))

def Circ_Calculation():
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = MaxValue(0, GetCurrency(USF6251.Circ) - GetCurrency(IA6251.Circ))
    else:
        ReturnVal = 0

def Description_Calculation():
    Total = Currency()
    Total = GetCurrency(IA6251Sp.TotAMT)
    ReturnVal = CStr(Total) + ' AMT'

def EFile_Calculation():
    if GetNumber(IA6251.DoNotComplete) == 1:
        ReturnVal = 0
    elif GetBool(IA6251Sp.Print) == True:
        ReturnVal = 1
    elif GetCurrency(IA6251Sp.Med) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251Sp.Taxes) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251Sp.Int) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251Sp.MiscDed) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251Sp.ItmLimit) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251Sp.TaxRfd) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251Sp.InvInt) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251Sp.Sec1202) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251Sp.ISO) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251Sp.Est) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251Sp.LargePart) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251Sp.AdjGain) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251Sp.Post86Depr) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251Sp.PALS) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251Sp.LossLim) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251Sp.Circ) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251Sp.LTContr) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251Sp.Mining) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251Sp.Research) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251Sp.Install) != 0:
        ReturnVal = 1
    elif GetCurrency(IA6251Sp.RelAdj) != 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Est_Calculation():
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = MaxValue(0, GetCurrency(USF6251.Est) - GetCurrency(IA6251.Est))
    else:
        ReturnVal = 0

def Exemption1_Calculation():
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = Decimal("17500")
    else:
        ReturnVal = 0

def Exemption2_Calculation():
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = Decimal("75000")
    else:
        ReturnVal = 0

def Install_Calculation():
    FedInstall = Currency()
    FedInstall = GetCurrency(USF6251.Install) * - 1
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = FedInstall - GetCurrency(IA6251.Install)
    else:
        ReturnVal = 0

def Int_Calculation():
    if GetBool(IAF1040.CombMFS) == True and GetBool(IAF1040.ItemCheck) == True:
        ReturnVal = MaxValue(0, GetCurrency(IAW6251MortInt.AMTInt) - GetCurrency(IA6251.Int))
    else:
        ReturnVal = 0

def InvInt_Calculation():
    if GetBool(IAF1040.CombMFS) == True and GetBool(IAF1040.ItemCheck) == True:
        ReturnVal = MaxValue(0, GetCurrency(USF6251.InvInt) - GetCurrency(IA6251.InvInt))
    else:
        ReturnVal = 0

def ISO_Calculation():
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = MaxValue(0, GetCurrency(USF6251.ISO) - GetCurrency(IA6251.ISO))
    else:
        ReturnVal = 0

def ItmLimit_Calculation():
    Limit = Currency()
    Limit = GetCurrency(IAWItmDed.Limit) * - 1
    if GetBool(IAF1040.CombMFS) == True and GetBool(IAF1040.ItemCheck) == True:
        ReturnVal = Limit - GetCurrency(IA6251.ItmLimit)
    else:
        ReturnVal = 0

def LargePart_Calculation():
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = MaxValue(0, GetCurrency(USF6251.LargePart) - GetCurrency(IA6251.LargePart))
    else:
        ReturnVal = 0

def LimAMTNOL_Calculation():
    TEst = Currency()

    Unlim = Currency()

    AMTL = Currency()
    TEst = GetCurrency(IA6251Sp.Subtotal)
    Unlim = Abs(GetCurrency(IA6251Sp.AMTNOL))
    if TEst > 0:
        AMTL = MinValue(Unlim, CDollar(CDbl(TEst) * 0.9))
    else:
        AMTL = 0
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = AMTL
    else:
        ReturnVal = 0

def LossLim_Calculation():
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = MaxValue(0, GetCurrency(USF6251.LossLim) - GetCurrency(IA6251.LossLim))
    else:
        ReturnVal = 0

def LTContr_Calculation():
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = MaxValue(0, GetCurrency(USF6251.LTContr) - GetCurrency(IA6251.LTContr))
    else:
        ReturnVal = 0

def Med_Calculation():
    ReturnVal = 0

def Mining_Calculation():
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = MaxValue(0, GetCurrency(USF6251.Mining) - GetCurrency(IA6251.Mining))
    else:
        ReturnVal = 0

def MiscDed_Calculation():
    if GetBool(IAF1040.CombMFS) == True and GetBool(IAF1040.ItemCheck) == True:
        ReturnVal = MaxValue(0, GetCurrency(IASchA.AllowExp) - GetCurrency(IA6251.MiscDed))
    else:
        ReturnVal = 0

def Multiply1_Calculation():
    ReturnVal = CDollar(GetFloat(IA6251Sp.AdjAMTInc1) * 0.25)

def Names_Calculation():
    ReturnVal = GetString(IARequired.SPCombName)

def NOL_Calculation():
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetCurrency(IAOthAdj.SIANOL)
    else:
        ReturnVal = 0

def PALS_Calculation():
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = MaxValue(0, GetCurrency(USF6251.PALS) - GetCurrency(IA6251.PALS))
    else:
        ReturnVal = 0

def Post86Depr_Calculation():
    #review new line 13 instructions and determine if we need to make an adjustment for any IA depr differences or if we should add an alert and note in Q&A
    #For 2017 changed to default calc this field and interview and added an alert
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = MaxValue(0, GetCurrency(USF6251.Post86Depr) - GetCurrency(IA6251.Post86Depr))
    else:
        ReturnVal = 0

def PrInstall_Calculation():
    ReturnVal = Abs(GetCurrency(IA6251Sp.Install))

def Print_Calculation():
    if GetBool(IAF1040.CombMFS) == False:
        ReturnVal = 0
    elif GetCurrency(IA6251Sp.TotAMT) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def PrItmLimit_Calculation():
    ReturnVal = Abs(GetCurrency(IA6251Sp.ItmLimit))

def PrTaxRfd_Calculation():
    ReturnVal = Abs(GetCurrency(IA6251Sp.TaxRfd))

def PYNRAMT_Calculation():
    ReturnVal = MaxValue(0, CDollar(GetFloat(IA6251Sp.AMT) * GetFloat(IA6251Sp.PYNRRatio)))

def PYNRAMTIncNI_Calculation():
    if GetBool(IAF126.SpPYNR) == True:
        ReturnVal = MaxValue(0, GetCurrency(IAF126.BNet) + GetCurrency(IA6251Sp.PYNRAMTInc))
    else:
        ReturnVal = 0

def PYNRRatio_Calculation():
    if GetCurrency(IA6251Sp.TotAMTInc) == 0:
        ReturnVal = 0
    else:
        ReturnVal = MinValue(1, Round(GetFloat(IA6251Sp.PYNRAMTIncNI) / GetFloat(IA6251Sp.TotAMTInc), 3))

def RegTax_Calculation():
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = MaxValue(0, GetCurrency(IAF1040.BAltTax) - GetCurrency(IAF1040.BExemCr))
    else:
        ReturnVal = 0

def RelAdj_Calculation():
    IARelAdj = Currency()
    IARelAdj = GetCurrency(USF6251.RelAdj) - GetCurrency(USF6251.LargePart) - GetCurrency(USF6251.F461) - GetCurrency(USF6251.F8990) - GetCurrency(USF6251.StdDed)
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = MaxValue(0, IARelAdj - GetCurrency(IA6251.RelAdj))
    else:
        ReturnVal = 0

def Research_Calculation():
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = MaxValue(0, GetCurrency(USF6251.Research) - GetCurrency(IA6251.Research))
    else:
        ReturnVal = 0

def Sec1202_Calculation():
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = MaxValue(0, GetCurrency(USF6251.Sec1202) - GetCurrency(IA6251.Sec1202))
    else:
        ReturnVal = 0

def SpUserMod_Calculation():
    if GetStatus(UserModifiedStatus) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SpouseSSN)

def Subtotal_Calculation():
    ReturnVal = GetCurrency(IA6251Sp.AMTInc) + GetCurrency(IA6251Sp.TaxInc) + GetCurrency(IA6251Sp.NOL)

def Taxes_Calculation():
    if GetBool(IAF1040.CombMFS) == True and GetBool(IAF1040.ItemCheck) == True:
        ReturnVal = MaxValue(0, GetCurrency(IASchA.TaxPd) - GetCurrency(IA6251.Taxes))
    else:
        ReturnVal = 0

def TaxInc_Calculation():
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetCurrency(IAF1040.BTaxInc)
    else:
        ReturnVal = 0

def TaxRfd_Calculation():
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetCurrency(IAF1040.BRefund) * - 1
    else:
        ReturnVal = 0

def TentAMT_Calculation():
    ReturnVal = CDollar(GetFloat(IA6251Sp.AdjAMTInc2) * 0.067)

def TotAMT_Calculation():
    if GetNumber(IA6251.DoNotComplete) == 1:
        ReturnVal = 0
    elif GetBool(IAF1040.CombMFS) == False:
        ReturnVal = 0
    elif GetBool(IAF126.SpPYNR) == True:
        ReturnVal = GetCurrency(IA6251Sp.PYNRAMT)
    else:
        ReturnVal = GetCurrency(IA6251Sp.AMT)

def TotAMTInc_Calculation():
    if GetBool(IAF126.SpPYNR) == True:
        ReturnVal = MaxValue(0, GetCurrency(IAF126.BAllSource) + GetCurrency(IA6251Sp.AMTInc))
    else:
        ReturnVal = 0

