from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Alert10_Calculation():
    if GetBool(IA4562PIV.SpecElectYes) == False and GetCurrency(IA4562PIV.Total179) > Decimal("70000"):
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert20_Calculation():
    if GetBool(IA4562PIV.UsingSpecElec) == True:
        if ( GetCurrency(IA4562PIV.TPFed1065) + GetCurrency(IA4562PIV.SPFed1065) + GetCurrency(IA4562PIV.TPFed1120S) + GetCurrency(IA4562PIV.SPFed1120S) )  > Decimal("0"):
            if ( GetCurrency(IA4562PIV.TPIA1065) + GetCurrency(IA4562PIV.SPIA1065) + GetCurrency(IA4562PIV.TPIA1120S) + GetCurrency(IA4562PIV.SPIA1120S) )  == Decimal("0"):
                ReturnVal = 1
            else:
                ReturnVal = 0
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def Alert30_Calculation():
    if GetBool(IA4562PIV.UsingSpecElec) == True:
        if ( GetCurrency(USWDepr.IACYSec179Rep) + GetCurrency(USF4562.StateTotCySec1792106, 1) )  > 0:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def CarryOver179Yr1_Calculation():
    ReturnVal = MaxValue(0, ( GetCurrency(IA4562PIV.Excess179) - GetCurrency(IA4562PIV.CarryOver179Yr2) - GetCurrency(IA4562PIV.CarryOver179Yr3) - GetCurrency(IA4562PIV.CarryOver179Yr4) - GetCurrency(IA4562PIV.CarryOver179Yr5) ))

def CarryOver179Yr2_Calculation():
    ReturnVal = CDollar(GetFloat(IA4562PIV.Excess179) * 0.2)

def CarryOver179Yr3_Calculation():
    ReturnVal = CDollar(GetFloat(IA4562PIV.Excess179) * 0.2)

def CarryOver179Yr4_Calculation():
    ReturnVal = CDollar(GetFloat(IA4562PIV.Excess179) * 0.2)

def CarryOver179Yr5_Calculation():
    ReturnVal = CDollar(GetFloat(IA4562PIV.Excess179) * 0.2)

def Desc_Calculation():
    Total = Currency()
    Total = GetCurrency(IA4562PIV.Excess179)
    ReturnVal = CStr(Total) + ' Special Election Deduction'

def Excess179_Calculation():
    if GetBool(IA4562PIV.SpecElectYes) == True:
        ReturnVal = MaxValue(0, ( GetCurrency(IA4562PIV.Total179) - GetCurrency(IA4562PIV.Limit) ))
    else:
        ReturnVal = Decimal("0")

def Exist_Calculation():
    ReturnVal = 1

def IASec179NoK1s_Calculation():
    ReturnVal = GetCurrency(USWDepr.IACYSec179Rep) + GetCurrency(USF4562.StateTotCySec1792106, 1)

def Limit_Calculation():
    if GetBool(IA4562PIV.SpecElectYes) == True:
        ReturnVal = Decimal("70000")
    else:
        ReturnVal = Decimal("0")

def Names_Calculation():
    ReturnVal = GetString(IARequired.CombNames)

def PrIA4562PIV_Calculation():
    if GetCurrency(IA4562PIV.TPPartIV179) != 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def PrIA4562PIVSP_Calculation():
    if GetCurrency(IA4562PIV.SPPartIV179) != 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Print_Calculation():
    if GetCurrency(IA4562PIV.Excess179) != 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def SPAccFedDep_Calculation():
    ReturnVal = 0

def SPAccIADep_Calculation():
    ReturnVal = 0

def SPBasis_Calculation():
    ReturnVal = 0

def SPCarryOver179Yr1_Calculation():
    if GetBool(IA4562PIV.UsingSpecElec) == False:
        ReturnVal = 0
    elif GetBool(IAF1040.CombMFS) == True:
        ReturnVal = CDollar(GetFloat(IA4562PIV.CarryOver179Yr1) * GetFloat(IA4562PIV.SPRatio))
    else:
        ReturnVal = 0

def SPCarryOver179Yr2_Calculation():
    if GetBool(IA4562PIV.UsingSpecElec) == False:
        ReturnVal = 0
    elif GetBool(IAF1040.CombMFS) == True:
        ReturnVal = CDollar(GetFloat(IA4562PIV.CarryOver179Yr2) * GetFloat(IA4562PIV.SPRatio))
    else:
        ReturnVal = 0

def SPCarryOver179Yr3_Calculation():
    if GetBool(IA4562PIV.UsingSpecElec) == False:
        ReturnVal = 0
    elif GetBool(IAF1040.CombMFS) == True:
        ReturnVal = CDollar(GetFloat(IA4562PIV.CarryOver179Yr3) * GetFloat(IA4562PIV.SPRatio))
    else:
        ReturnVal = 0

def SPCarryOver179Yr4_Calculation():
    if GetBool(IA4562PIV.UsingSpecElec) == False:
        ReturnVal = 0
    elif GetBool(IAF1040.CombMFS) == True:
        ReturnVal = CDollar(GetFloat(IA4562PIV.CarryOver179Yr4) * GetFloat(IA4562PIV.SPRatio))
    else:
        ReturnVal = 0

def SPCarryOver179Yr5_Calculation():
    if GetBool(IA4562PIV.UsingSpecElec) == False:
        ReturnVal = 0
    elif GetBool(IAF1040.CombMFS) == True:
        ReturnVal = CDollar(GetFloat(IA4562PIV.CarryOver179Yr5) * GetFloat(IA4562PIV.SPRatio))
    else:
        ReturnVal = 0

def SpCopy_Calculation():
    if GetCurrency(IA4562PIV.SPPartIV179) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def SPDateServ_Calculation():
    ReturnVal = MakeDate(12, 31, YearNumber)

def SPExcess179_Calculation():
    if GetBool(IA4562PIV.UsingSpecElec) == False:
        ReturnVal = 0
    elif GetBool(IAF1040.CombMFS) == True:
        ReturnVal = CDollar(GetFloat(IA4562PIV.Excess179) * GetFloat(IA4562PIV.SPRatio))
    else:
        ReturnVal = 0

def SPFed1065_Calculation():
    ReturnVal = GetCurrency(USDPartK1.Sec179, FieldCopies(USDPartK1.Spouse)) + MaxValue(0, GetCurrency(USDPartK1.Sec179, FieldCopies(USDPartK1.Joint)) - CDollar(GetFloat(USDPartK1.Sec179, FieldCopies(USDPartK1.Joint)) * 0.5))

def SPFed1120S_Calculation():
    ReturnVal = GetCurrency(USDSCorpK1.Sec179, FieldCopies(USDSCorpK1.Spouse)) + MaxValue(0, GetCurrency(USDSCorpK1.Sec179, FieldCopies(USDSCorpK1.Joint)) - CDollar(GetFloat(USDSCorpK1.Sec179, FieldCopies(USDSCorpK1.Joint)) * 0.5))

def SPFedDepDed_Calculation():
    ReturnVal = 0

def SPLife_Calculation():
    ReturnVal = '0'

def SPLine1_Calculation():
    if GetBool(IA4562PIV.UsingSpecElec) == False:
        ReturnVal = 0
    elif GetBool(IAF1040.CombMFS) == True:
        ReturnVal = CDollar(GetFloat(IA4562PIV.Total179) * GetFloat(IA4562PIV.SPRatio))
    else:
        ReturnVal = 0

def SPLine1a_Calculation():
    if GetBool(IA4562PIV.UsingSpecElec) == False:
        ReturnVal = 0
    elif GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetCurrency(IA4562PIV.SPIA1065)
    else:
        ReturnVal = 0

def SPLine1b_Calculation():
    if GetBool(IA4562PIV.UsingSpecElec) == False:
        ReturnVal = 0
    elif GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetCurrency(IA4562PIV.SPFed1065)
    else:
        ReturnVal = 0

def SPLine1c_Calculation():
    if GetBool(IA4562PIV.UsingSpecElec) == False:
        ReturnVal = 0
    elif GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetCurrency(IA4562PIV.SPIA1120S)
    else:
        ReturnVal = 0

def SPLine1d_Calculation():
    if GetBool(IA4562PIV.UsingSpecElec) == False:
        ReturnVal = 0
    elif GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetCurrency(IA4562PIV.SPFed1120S)
    else:
        ReturnVal = 0

def SPMACRSIA_Calculation():
    ReturnVal = 0

def SPName_Calculation():
    ReturnVal = GetString(IARequired.SPCombName)

def SPPartIV179_Calculation():
    if GetBool(IA4562PIV.UsingSpecElec) == False:
        ReturnVal = 0
    elif GetBool(IAF1040.CombMFS) == True:
        ReturnVal = CDollar(GetFloat(IA4562PIV.Limit) * GetFloat(IA4562PIV.SPRatio))
    else:
        ReturnVal = 0

def SPPropDescr_Calculation():
    if GetCurrency(IA4562PIV.SPPartIV179) > 0:
        ReturnVal = 'Part IV'
    else:
        ReturnVal = ''

def SPRatio_Calculation():
    if GetCurrency(IA4562PIV.Tot179Nolimit) == 0:
        ReturnVal = 0
    else:
        ReturnVal = MaxValue(0, ( MinValue(1, GetFloat(IA4562PIV.SPTot179) / GetFloat(IA4562PIV.Tot179Nolimit)) ))

def SPSSN_Calculation():
    ReturnVal = GetString(IAF1040.SpouseSSN)

def SPTot179_Calculation():
    ReturnVal = GetCurrency(IA4562PIV.SPIA1065) + GetCurrency(IA4562PIV.SPFed1065) + GetCurrency(IA4562PIV.SPIA1120S) + GetCurrency(IA4562PIV.SPFed1120S)

def SPTotAdj_Calculation():
    ReturnVal = GetCurrency(IA4562PIV.SPLine1) - GetCurrency(IA4562PIV.SPPartIV179)

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

def Tot179Nolimit_Calculation():
    ReturnVal = GetCurrency(IA4562PIV.TPTot179) + GetCurrency(IA4562PIV.SPTot179)

def Total179_Calculation():
    Tot = Currency()
    Tot = GetCurrency(IA4562PIV.TotIA1065) + GetCurrency(IA4562PIV.TotFed1065) + GetCurrency(IA4562PIV.TotIA1120S) + GetCurrency(IA4562PIV.TotFed1120S)
    ReturnVal = MinValue(Tot, Decimal("1000000"))

def TotFed1065_Calculation():
    ReturnVal = GetCurrency(IA4562PIV.TPFed1065) + GetCurrency(IA4562PIV.SPFed1065)

def TotFed1120S_Calculation():
    ReturnVal = GetCurrency(IA4562PIV.TPFed1120S) + GetCurrency(IA4562PIV.SPFed1120S)

def TotIA1065_Calculation():
    ReturnVal = GetCurrency(IA4562PIV.TPIA1065) + GetCurrency(IA4562PIV.SPIA1065)

def TotIA1120S_Calculation():
    ReturnVal = GetCurrency(IA4562PIV.TPIA1120S) + GetCurrency(IA4562PIV.SPIA1120S)

def TPAccFedDep_Calculation():
    ReturnVal = 0

def TPAccIADep_Calculation():
    ReturnVal = 0

def TPBasis_Calculation():
    ReturnVal = 0

def TPCarryOver179Yr1_Calculation():
    if GetBool(IA4562PIV.UsingSpecElec) == False:
        ReturnVal = 0
    elif GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetCurrency(IA4562PIV.CarryOver179Yr1) - GetCurrency(IA4562PIV.SPCarryOver179Yr1)
    else:
        ReturnVal = GetCurrency(IA4562PIV.CarryOver179Yr1)

def TPCarryOver179Yr2_Calculation():
    if GetBool(IA4562PIV.UsingSpecElec) == False:
        ReturnVal = 0
    elif GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetCurrency(IA4562PIV.CarryOver179Yr2) - GetCurrency(IA4562PIV.SPCarryOver179Yr2)
    else:
        ReturnVal = GetCurrency(IA4562PIV.CarryOver179Yr2)

def TPCarryOver179Yr3_Calculation():
    if GetBool(IA4562PIV.UsingSpecElec) == False:
        ReturnVal = 0
    elif GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetCurrency(IA4562PIV.CarryOver179Yr3) - GetCurrency(IA4562PIV.SPCarryOver179Yr3)
    else:
        ReturnVal = GetCurrency(IA4562PIV.CarryOver179Yr3)

def TPCarryOver179Yr4_Calculation():
    if GetBool(IA4562PIV.UsingSpecElec) == False:
        ReturnVal = 0
    elif GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetCurrency(IA4562PIV.CarryOver179Yr4) - GetCurrency(IA4562PIV.SPCarryOver179Yr4)
    else:
        ReturnVal = GetCurrency(IA4562PIV.CarryOver179Yr4)

def TPCarryOver179Yr5_Calculation():
    if GetBool(IA4562PIV.UsingSpecElec) == False:
        ReturnVal = 0
    elif GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetCurrency(IA4562PIV.CarryOver179Yr5) - GetCurrency(IA4562PIV.SPCarryOver179Yr5)
    else:
        ReturnVal = GetCurrency(IA4562PIV.CarryOver179Yr5)

def TpCopy_Calculation():
    if GetCurrency(IA4562PIV.TPPartIV179) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def TPDateServ_Calculation():
    ReturnVal = MakeDate(12, 31, YearNumber)

def TPExcess179_Calculation():
    if GetBool(IA4562PIV.UsingSpecElec) == False:
        ReturnVal = 0
    elif GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetCurrency(IA4562PIV.Excess179) - GetCurrency(IA4562PIV.SPExcess179)
    else:
        ReturnVal = GetCurrency(IA4562PIV.Excess179)

def TPFed1065_Calculation():
    ReturnVal = GetCurrency(USDPartK1.Sec179, FieldCopies(USDPartK1.Taxpayer)) + CDollar(GetFloat(USDPartK1.Sec179, FieldCopies(USDPartK1.Joint)) * 0.5)

def TPFed1120S_Calculation():
    ReturnVal = GetCurrency(USDSCorpK1.Sec179, FieldCopies(USDSCorpK1.Taxpayer)) + CDollar(GetFloat(USDSCorpK1.Sec179, FieldCopies(USDSCorpK1.Joint)) * 0.5)

def TPFedDepDed_Calculation():
    ReturnVal = 0

def TPLife_Calculation():
    ReturnVal = '0'

def TPLine1_Calculation():
    if GetBool(IA4562PIV.UsingSpecElec) == False:
        ReturnVal = 0
    elif GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetCurrency(IA4562PIV.Total179) - GetCurrency(IA4562PIV.SPLine1)
    else:
        ReturnVal = GetCurrency(IA4562PIV.Total179)

def TPLine1a_Calculation():
    if GetBool(IA4562PIV.UsingSpecElec) == False:
        ReturnVal = 0
    elif GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetCurrency(IA4562PIV.TPIA1065)
    else:
        ReturnVal = GetCurrency(IA4562PIV.TotIA1065)

def TPLine1b_Calculation():
    if GetBool(IA4562PIV.UsingSpecElec) == False:
        ReturnVal = 0
    elif GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetCurrency(IA4562PIV.TPFed1065)
    else:
        ReturnVal = GetCurrency(IA4562PIV.TotFed1065)

def TPLine1c_Calculation():
    if GetBool(IA4562PIV.UsingSpecElec) == False:
        ReturnVal = 0
    elif GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetCurrency(IA4562PIV.TPIA1120S)
    else:
        ReturnVal = GetCurrency(IA4562PIV.TotIA1120S)

def TPLine1d_Calculation():
    if GetBool(IA4562PIV.UsingSpecElec) == False:
        ReturnVal = 0
    elif GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetCurrency(IA4562PIV.TPFed1120S)
    else:
        ReturnVal = GetCurrency(IA4562PIV.TotFed1120S)

def TPMACRSIA_Calculation():
    ReturnVal = 0

def TPorJTName_Calculation():
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetString(IARequired.TPCombName)
    else:
        ReturnVal = GetString(IARequired.CombNames)

def TPorJTSSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

def TPPartIV179_Calculation():
    if GetBool(IA4562PIV.UsingSpecElec) == False:
        ReturnVal = 0
    elif GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetCurrency(IA4562PIV.Limit) - GetCurrency(IA4562PIV.SPPartIV179)
    else:
        ReturnVal = GetCurrency(IA4562PIV.Limit)

def TPPropDescr_Calculation():
    if GetCurrency(IA4562PIV.TPPartIV179) > 0:
        ReturnVal = 'Part IV'
    else:
        ReturnVal = ''

def TPTot179_Calculation():
    ReturnVal = GetCurrency(IA4562PIV.TPIA1065) + GetCurrency(IA4562PIV.TPFed1065) + GetCurrency(IA4562PIV.TPIA1120S) + GetCurrency(IA4562PIV.TPFed1120S)

def TPTotAdj_Calculation():
    ReturnVal = GetCurrency(IA4562PIV.TPLine1) - GetCurrency(IA4562PIV.TPPartIV179)

def UsingSpecElec_Calculation():
    if GetBool(IA4562PIV.SpecElectYes) == True and GetCurrency(IA4562PIV.Excess179) > Decimal("0"):
        ReturnVal = 1
    else:
        ReturnVal = 0

