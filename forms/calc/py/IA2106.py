from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def AnotherVN_Calculation(Index):
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetBool(USF2106.AnotherVN(Index), ParentCopy())

def AnotherVY_Calculation(Index):
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetBool(USF2106.AnotherVY(Index), ParentCopy())

def Common_Calculation():
    ReturnVal = GetString(USWBasicInfo.TPCommon)

def Description_Calculation():
    ReturnVal = GetString(IA2106.FirstName)

def DOT_Calculation():
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetBool(USF2106.DOT, ParentCopy())

def DOTMeals_Calculation():
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        if GetBool(IA2106.DOT) == True:
            ReturnVal = GetCurrency(USF2106.DOTMeals, ParentCopy())
        else:
            ReturnVal = 0

def EmpExp_Calculation():
    #should clergy be factored in, see 2017 Fed 2106 line 10 calc, would need checkbox and ClergyExp added to 2018 fed 2106 state section and interviewed (looks like these fields were added to fed in 2014)
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(IA2106.LimMEColA) + GetCurrency(IA2106.LimMEColB)

def EvidenceN_Calculation(Index):
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetBool(USF2106.EvidenceN(Index), ParentCopy())

def EvidenceY_Calculation(Index):
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetBool(USF2106.EvidenceY(Index), ParentCopy())

def Exist_Calculation():
    ReturnVal = 1

def Fed2106_Calculation():
    ReturnVal = 'BEGIN HERE: Open federal Form 2106       Click on the folder to open the supporting document.'

def FedLn4_Calculation():
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(USF2106.TotBusExp, ParentCopy())

def FirstName_Calculation():
    if GetBool(IA2106.Spouse) == True:
        ReturnVal = GetString(IAF1040.SpouseFirst)
    else:
        ReturnVal = GetString(IAF1040.FirstName)

def IAExcessReim_Calculation():
    if GetCurrency(IA2106.TotColA) - GetCurrency(IA2106.UnreimColA) < 0:
        ReturnVal = Abs(GetCurrency(IA2106.TotColA) - GetCurrency(IA2106.UnreimColA))
    else:
        ReturnVal = 0

def IAStateDeprAdj_Calculation():
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(USF2106.IAStateDeprAdj, ParentCopy()) * - 1

def IAWages_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2106.IAExcessReim) - GetCurrency(IA2106.Wages))

def LastName_Calculation():
    if GetBool(IA2106.Spouse) == True:
        ReturnVal = GetString(IAF1040.SpouseLast)
    else:
        ReturnVal = GetString(IAF1040.LastName)

def LimMEColA_Calculation():
    if GetCurrency(IA2106.NetColA) > 0:
        ReturnVal = GetCurrency(IA2106.NetColA)
    else:
        ReturnVal = 0

def LimMEColB_Calculation():
    DOTMeals = Currency()

    OthMeals = Currency()
    DOTMeals = MaxValue(0, GetCurrency(IA2106.DOTMeals) - GetCurrency(IA2106.ReimbDOT))
    OthMeals = MaxValue(0, GetCurrency(IA2106.OthMeals) - GetCurrency(IA2106.ReimbOth))
    if DOTMeals + OthMeals > 0:
        if GetBool(IA2106.DOT) == True:
            ReturnVal = CDollar(CDbl(DOTMeals) * 0.8) + CDollar(CDbl(OthMeals) * 0.5)
        else:
            ReturnVal = CDollar(CDbl(OthMeals) * 0.5)
    else:
        ReturnVal = 0

def Meals_Calculation():
    if GetBool(IA2106.DOT) == True:
        ReturnVal = GetCurrency(IA2106.DOTMeals) + GetCurrency(IA2106.OthMeals)
    else:
        ReturnVal = GetCurrency(IA2106.OthMeals)

def NetColA_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2106.TotColA) - GetCurrency(IA2106.UnreimColA))

def NetColB_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2106.TotColB) - GetCurrency(IA2106.UnReimColB))

def Occupation_Calculation():
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = ''
    else:
        ReturnVal = GetString(USF2106.Occupation, ParentCopy())

def OffN_Calculation(Index):
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetBool(USF2106.OffN(Index), ParentCopy())

def OffY_Calculation(Index):
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetBool(USF2106.OffY(Index), ParentCopy())

def OthMeals_Calculation():
    TotMeals = Currency()
    TotMeals = GetCurrency(USF2106.Meals, ParentCopy())
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = MaxValue(0, ( TotMeals - GetCurrency(IA2106.DOTMeals) ))

def Parking_Calculation():
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(USF2106.Parking, ParentCopy())

def PAvgComm_Calculation(Index):
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetNumber(USF2106.PAvgComm(Index), ParentCopy())

def PBasis_Calculation(Index):
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(USF2106.PBasis(Index), ParentCopy())

def PBusMiles_Calculation(Index):
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetNumber(USF2106.PBusMiles(Index), ParentCopy())

def PBusPer_Calculation(Index):
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetFloat(USF2106.PBusPer(Index), ParentCopy())

def PCommute_Calculation(Index):
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetNumber(USF2106.PCommute(Index), ParentCopy())

def PDate_Calculation(Index):
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = ''
    else:
        ReturnVal = GetString(USF2106.PDate(Index), ParentCopy())

def PDepr_Calculation(Index):
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(IA2106.PTotDepr(Index))

def PDeprBasis_Calculation(Index):
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = MaxValue(0, CDollar(GetFloat(IA2106.PBasis(Index)) * GetFloat(IA2106.PBusPer(Index))) - GetCurrency(USF2106.PStateSec179(Index), ParentCopy()))

def PDeprVeh_Calculation(Index):
    #need to make sure sec179 is included, IA 2106 does not have a line for State sec179 and does not address in the instructions, seems this filed will have to show the depr basis x rate plus 179.
    #Verified below is calling USW2106Veh.DeprNoBonus which includes depr x bus per. plus state 179
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(USF2106.PDeprVehState(Index), ParentCopy())

def PExp_Calculation(Index):
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(USF2106.PExp(Index), ParentCopy())

def PGas_Calculation(Index):
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(USF2106.PGas(Index), ParentCopy())

def PInclusion_Calculation(Index):
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(USF2106.PInclusion(Index), ParentCopy())

def PLuxLim_Calculation(Index):
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(USF2106.LuxLimState2(Index), ParentCopy())

def PMethod_Calculation(Index):
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = ''
    else:
        ReturnVal = GetString(USF2106.PMethod(Index), ParentCopy())

def PNetRent_Calculation(Index):
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(USF2106.PNetRent(Index), ParentCopy())

def POthMiles_Calculation(Index):
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetNumber(USF2106.POthMiles(Index), ParentCopy())

def PPerExp_Calculation(Index):
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(USF2106.PPerExp(Index), ParentCopy())

def PPerLim_Calculation(Index):
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(USF2106.PerLimState2(Index), ParentCopy())

def PRate_Calculation(Index):
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = ''
    else:
        ReturnVal = GetString(USF2106.PRate(Index), ParentCopy())

def PRent_Calculation(Index):
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(USF2106.PRent(Index), ParentCopy())

def PrintMe_Calculation():
    if GetCurrency(IA2106.EmpExp) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def PrintPg21_Calculation():
    if GetCurrency(IA2106.PStandard(0)) > Decimal("0") or GetCurrency(IA2106.PTotAct(0)) > Decimal("0"):
        ReturnVal = 1
    else:
        ReturnVal = 0

def PrintPg22_Calculation():
    if GetCurrency(IA2106.PStandard(1)) > Decimal("0") or GetCurrency(IA2106.PTotAct(1)) > Decimal("0"):
        ReturnVal = 1
    else:
        ReturnVal = 0

def PrintPg23_Calculation():
    if GetCurrency(IA2106.PStandard(2)) > Decimal("0") or GetCurrency(IA2106.PTotAct(2)) > Decimal("0"):
        ReturnVal = 1
    else:
        ReturnVal = 0

def PrintPg24_Calculation():
    if GetCurrency(IA2106.PStandard(3)) > Decimal("0") or GetCurrency(IA2106.PTotAct(3)) > Decimal("0"):
        ReturnVal = 1
    else:
        ReturnVal = 0

def PStandard_Calculation(Index):
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(USF2106.PStandard(Index), ParentCopy())

def PTotAct_Calculation(Index):
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    elif GetCurrency(IA2106.PStandard(Index)) == 0:
        ReturnVal = GetCurrency(IA2106.PPerExp(Index)) + GetCurrency(IA2106.PDepr(Index))
    else:
        ReturnVal = 0

def PTotDepr_Calculation(Index):
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    elif GetCurrency(IA2106.PLuxLim(Index)) == 0 and GetCurrency(IA2106.PPerLim(Index)) == 0:
        ReturnVal = GetCurrency(IA2106.PDeprVeh(Index))
    else:
        ReturnVal = MinValue(GetCurrency(IA2106.PDeprVeh(Index)), GetCurrency(IA2106.PPerLim(Index)))

def PTotMiles_Calculation(Index):
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetNumber(USF2106.PTotMiles(Index), ParentCopy())

def PValue_Calculation(Index):
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(USF2106.PValue(Index), ParentCopy())

def FedQualifies_Calculation():
    ReturnVal = GetBool(USF2106.Qualifies, ParentCopy())

def ReimbDOT_Calculation():
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        if GetBool(IA2106.DOT) == True:
            ReturnVal = GetCurrency(USF2106.ReimbDOT, ParentCopy())
        else:
            ReturnVal = 0

def ReimbOth_Calculation():
    TotReimb = Currency()
    TotReimb = GetCurrency(USF2106.UnReimColB, ParentCopy())
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = MaxValue(0, ( TotReimb - GetCurrency(IA2106.ReimbDOT) ))

def SchAAMt_Calculation():
    ReturnVal = GetCurrency(IA2106.EmpExp)

def Spouse_Calculation():
    ReturnVal = GetBool(USF2106.Spouse, ParentCopy())

def SpouseCommon_Calculation():
    ReturnVal = GetString(USWBasicInfo.SPCommon)

def SSN_Calculation():
    if GetBool(IA2106.Spouse) == True:
        ReturnVal = GetString(IAF1040.SpouseSSN)
    else:
        ReturnVal = GetString(IAF1040.SSN)

def Taxpayer_Calculation():
    ReturnVal = GetBool(USF2106.Taxpayer, ParentCopy())

def TotBusExp_Calculation():
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(IA2106.FedLn4) + GetCurrency(IA2106.IAStateDeprAdj)

def TotColA_Calculation():
    ReturnVal = GetCurrency(IA2106.VehExp) + GetCurrency(IA2106.Parking) + GetCurrency(IA2106.Travel) + GetCurrency(IA2106.TotBusExp)

def TotColB_Calculation():
    ReturnVal = GetCurrency(IA2106.Meals)

def Travel_Calculation():
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(USF2106.Travel, ParentCopy())

def UnreimColA_Calculation():
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(USF2106.UnreimColA, ParentCopy())

def UnReimColB_Calculation():
    if GetBool(IA2106.DOT) == True:
        ReturnVal = GetCurrency(IA2106.ReimbDOT) + GetCurrency(IA2106.ReimbOth)
    else:
        ReturnVal = GetCurrency(IA2106.ReimbOth)

def VehExp_Calculation():
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(IA2106.PStandard(0)) + GetCurrency(IA2106.PStandard(1)) + GetCurrency(IA2106.PStandard(2)) + GetCurrency(IA2106.PStandard(3)) + GetCurrency(IA2106.PTotAct(0)) + GetCurrency(IA2106.PTotAct(1)) + GetCurrency(IA2106.PTotAct(2)) + GetCurrency(IA2106.PTotAct(3))

def Wages_Calculation():
    ReturnVal = GetCurrency(USF2106.Wages, ParentCopy())

def WrittenN_Calculation(Index):
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetBool(USF2106.WrittenN(Index), ParentCopy())

def WrittenY_Calculation(Index):
    if GetBool(IA2106.FedQualifies) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetBool(USF2106.WrittenY(Index), ParentCopy())

def YrMakeModel_Calculation(Index):
    ReturnVal = GetString(IA2106.Year(Index)) + ' ' + GetString(IA2106.Make(Index)) + ' ' + GetString(IA2106.Model(Index))

