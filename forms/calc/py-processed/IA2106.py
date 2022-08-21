from forms.out import IA2106
from forms.out import IAF1040
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def AnotherVN_Calculation(Index):
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return get_bool(USF2106.AnotherVN(Index), ParentCopy())

def AnotherVY_Calculation(Index):
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return get_bool(USF2106.AnotherVY(Index), ParentCopy())

def Common_Calculation():
    return get_string(USWBasicInfo.TPCommon)

def Description_Calculation():
    return get_string(IA2106.FirstName)

def DOT_Calculation():
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return get_bool(USF2106.DOT, ParentCopy())

def DOTMeals_Calculation():
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        if get_bool(IA2106.DOT) == True:
            return get_currency(USF2106.DOTMeals, ParentCopy())
        else:
            return 0

def EmpExp_Calculation():
    #should clergy be factored in, see 2017 Fed 2106 line 10 calc, would need checkbox and ClergyExp added to 2018 fed 2106 state section and interviewed (looks like these fields were added to fed in 2014)
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return get_currency(IA2106.LimMEColA) + get_currency(IA2106.LimMEColB)

def EvidenceN_Calculation(Index):
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return get_bool(USF2106.EvidenceN(Index), ParentCopy())

def EvidenceY_Calculation(Index):
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return get_bool(USF2106.EvidenceY(Index), ParentCopy())

def Exist_Calculation():
    return 1

def Fed2106_Calculation():
    return 'BEGIN HERE: Open federal Form 2106       Click on the folder to open the supporting document.'

def FedLn4_Calculation():
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return get_currency(USF2106.TotBusExp, ParentCopy())

def FirstName_Calculation():
    if get_bool(IA2106.Spouse) == True:
        return get_string(IAF1040.SpouseFirst)
    else:
        return get_string(IAF1040.FirstName)

def IAExcessReim_Calculation():
    if get_currency(IA2106.TotColA) - get_currency(IA2106.UnreimColA) < 0:
        return Abs(get_currency(IA2106.TotColA) - get_currency(IA2106.UnreimColA))
    else:
        return 0

def IAStateDeprAdj_Calculation():
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return get_currency(USF2106.IAStateDeprAdj, ParentCopy()) * - 1

def IAWages_Calculation():
    return max_value(0, get_currency(IA2106.IAExcessReim) - get_currency(IA2106.Wages))

def LastName_Calculation():
    if get_bool(IA2106.Spouse) == True:
        return get_string(IAF1040.SpouseLast)
    else:
        return get_string(IAF1040.LastName)

def LimMEColA_Calculation():
    if get_currency(IA2106.NetColA) > 0:
        return get_currency(IA2106.NetColA)
    else:
        return 0

def LimMEColB_Calculation():
    DOTMeals = Currency()

    OthMeals = Currency()
    DOTMeals = max_value(0, get_currency(IA2106.DOTMeals) - get_currency(IA2106.ReimbDOT))
    OthMeals = max_value(0, get_currency(IA2106.OthMeals) - get_currency(IA2106.ReimbOth))
    if DOTMeals + OthMeals > 0:
        if get_bool(IA2106.DOT) == True:
            return c_dollar(CDbl(DOTMeals) * 0.8) + c_dollar(CDbl(OthMeals) * 0.5)
        else:
            return c_dollar(CDbl(OthMeals) * 0.5)
    else:
        return 0

def Meals_Calculation():
    if get_bool(IA2106.DOT) == True:
        return get_currency(IA2106.DOTMeals) + get_currency(IA2106.OthMeals)
    else:
        return get_currency(IA2106.OthMeals)

def NetColA_Calculation():
    return max_value(0, get_currency(IA2106.TotColA) - get_currency(IA2106.UnreimColA))

def NetColB_Calculation():
    return max_value(0, get_currency(IA2106.TotColB) - get_currency(IA2106.UnReimColB))

def Occupation_Calculation():
    if get_bool(IA2106.FedQualifies) == True:
        return ''
    else:
        return get_string(USF2106.Occupation, ParentCopy())

def OffN_Calculation(Index):
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return get_bool(USF2106.OffN(Index), ParentCopy())

def OffY_Calculation(Index):
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return get_bool(USF2106.OffY(Index), ParentCopy())

def OthMeals_Calculation():
    TotMeals = Currency()
    TotMeals = get_currency(USF2106.Meals, ParentCopy())
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return max_value(0, ( TotMeals - get_currency(IA2106.DOTMeals) ))

def Parking_Calculation():
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return get_currency(USF2106.Parking, ParentCopy())

def PAvgComm_Calculation(Index):
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return get_number(USF2106.PAvgComm(Index), ParentCopy())

def PBasis_Calculation(Index):
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return get_currency(USF2106.PBasis(Index), ParentCopy())

def PBusMiles_Calculation(Index):
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return get_number(USF2106.PBusMiles(Index), ParentCopy())

def PBusPer_Calculation(Index):
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return get_float(USF2106.PBusPer(Index), ParentCopy())

def PCommute_Calculation(Index):
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return get_number(USF2106.PCommute(Index), ParentCopy())

def PDate_Calculation(Index):
    if get_bool(IA2106.FedQualifies) == True:
        return ''
    else:
        return get_string(USF2106.PDate(Index), ParentCopy())

def PDepr_Calculation(Index):
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return get_currency(IA2106.PTotDepr(Index))

def PDeprBasis_Calculation(Index):
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return max_value(0, c_dollar(get_float(IA2106.PBasis(Index)) * get_float(IA2106.PBusPer(Index))) - get_currency(USF2106.PStateSec179(Index), ParentCopy()))

def PDeprVeh_Calculation(Index):
    #need to make sure sec179 is included, IA 2106 does not have a line for State sec179 and does not address in the instructions, seems this filed will have to show the depr basis x rate plus 179.
    #Verified below is calling USW2106Veh.DeprNoBonus which includes depr x bus per. plus state 179
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return get_currency(USF2106.PDeprVehState(Index), ParentCopy())

def PExp_Calculation(Index):
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return get_currency(USF2106.PExp(Index), ParentCopy())

def PGas_Calculation(Index):
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return get_currency(USF2106.PGas(Index), ParentCopy())

def PInclusion_Calculation(Index):
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return get_currency(USF2106.PInclusion(Index), ParentCopy())

def PLuxLim_Calculation(Index):
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return get_currency(USF2106.LuxLimState2(Index), ParentCopy())

def PMethod_Calculation(Index):
    if get_bool(IA2106.FedQualifies) == True:
        return ''
    else:
        return get_string(USF2106.PMethod(Index), ParentCopy())

def PNetRent_Calculation(Index):
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return get_currency(USF2106.PNetRent(Index), ParentCopy())

def POthMiles_Calculation(Index):
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return get_number(USF2106.POthMiles(Index), ParentCopy())

def PPerExp_Calculation(Index):
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return get_currency(USF2106.PPerExp(Index), ParentCopy())

def PPerLim_Calculation(Index):
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return get_currency(USF2106.PerLimState2(Index), ParentCopy())

def PRate_Calculation(Index):
    if get_bool(IA2106.FedQualifies) == True:
        return ''
    else:
        return get_string(USF2106.PRate(Index), ParentCopy())

def PRent_Calculation(Index):
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return get_currency(USF2106.PRent(Index), ParentCopy())

def PrintMe_Calculation():
    if get_currency(IA2106.EmpExp) > 0:
        return 1
    else:
        return 0

def PrintPg21_Calculation():
    if get_currency(IA2106.PStandard(0)) > Decimal("0") or get_currency(IA2106.PTotAct(0)) > Decimal("0"):
        return 1
    else:
        return 0

def PrintPg22_Calculation():
    if get_currency(IA2106.PStandard(1)) > Decimal("0") or get_currency(IA2106.PTotAct(1)) > Decimal("0"):
        return 1
    else:
        return 0

def PrintPg23_Calculation():
    if get_currency(IA2106.PStandard(2)) > Decimal("0") or get_currency(IA2106.PTotAct(2)) > Decimal("0"):
        return 1
    else:
        return 0

def PrintPg24_Calculation():
    if get_currency(IA2106.PStandard(3)) > Decimal("0") or get_currency(IA2106.PTotAct(3)) > Decimal("0"):
        return 1
    else:
        return 0

def PStandard_Calculation(Index):
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return get_currency(USF2106.PStandard(Index), ParentCopy())

def PTotAct_Calculation(Index):
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    elif get_currency(IA2106.PStandard(Index)) == 0:
        return get_currency(IA2106.PPerExp(Index)) + get_currency(IA2106.PDepr(Index))
    else:
        return 0

def PTotDepr_Calculation(Index):
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    elif get_currency(IA2106.PLuxLim(Index)) == 0 and get_currency(IA2106.PPerLim(Index)) == 0:
        return get_currency(IA2106.PDeprVeh(Index))
    else:
        return min_value(get_currency(IA2106.PDeprVeh(Index)), get_currency(IA2106.PPerLim(Index)))

def PTotMiles_Calculation(Index):
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return get_number(USF2106.PTotMiles(Index), ParentCopy())

def PValue_Calculation(Index):
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return get_currency(USF2106.PValue(Index), ParentCopy())

def FedQualifies_Calculation():
    return get_bool(USF2106.Qualifies, ParentCopy())

def ReimbDOT_Calculation():
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        if get_bool(IA2106.DOT) == True:
            return get_currency(USF2106.ReimbDOT, ParentCopy())
        else:
            return 0

def ReimbOth_Calculation():
    TotReimb = Currency()
    TotReimb = get_currency(USF2106.UnReimColB, ParentCopy())
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return max_value(0, ( TotReimb - get_currency(IA2106.ReimbDOT) ))

def SchAAMt_Calculation():
    return get_currency(IA2106.EmpExp)

def Spouse_Calculation():
    return get_bool(USF2106.Spouse, ParentCopy())

def SpouseCommon_Calculation():
    return get_string(USWBasicInfo.SPCommon)

def SSN_Calculation():
    if get_bool(IA2106.Spouse) == True:
        return get_string(IAF1040.SpouseSSN)
    else:
        return get_string(IAF1040.SSN)

def Taxpayer_Calculation():
    return get_bool(USF2106.Taxpayer, ParentCopy())

def TotBusExp_Calculation():
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return get_currency(IA2106.FedLn4) + get_currency(IA2106.IAStateDeprAdj)

def TotColA_Calculation():
    return get_currency(IA2106.VehExp) + get_currency(IA2106.Parking) + get_currency(IA2106.Travel) + get_currency(IA2106.TotBusExp)

def TotColB_Calculation():
    return get_currency(IA2106.Meals)

def Travel_Calculation():
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return get_currency(USF2106.Travel, ParentCopy())

def UnreimColA_Calculation():
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return get_currency(USF2106.UnreimColA, ParentCopy())

def UnReimColB_Calculation():
    if get_bool(IA2106.DOT) == True:
        return get_currency(IA2106.ReimbDOT) + get_currency(IA2106.ReimbOth)
    else:
        return get_currency(IA2106.ReimbOth)

def VehExp_Calculation():
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return get_currency(IA2106.PStandard(0)) + get_currency(IA2106.PStandard(1)) + get_currency(IA2106.PStandard(2)) + get_currency(IA2106.PStandard(3)) + get_currency(IA2106.PTotAct(0)) + get_currency(IA2106.PTotAct(1)) + get_currency(IA2106.PTotAct(2)) + get_currency(IA2106.PTotAct(3))

def Wages_Calculation():
    return get_currency(USF2106.Wages, ParentCopy())

def WrittenN_Calculation(Index):
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return get_bool(USF2106.WrittenN(Index), ParentCopy())

def WrittenY_Calculation(Index):
    if get_bool(IA2106.FedQualifies) == True:
        return 0
    else:
        return get_bool(USF2106.WrittenY(Index), ParentCopy())

def YrMakeModel_Calculation(Index):
    return get_string(IA2106.Year(Index)) + ' ' + get_string(IA2106.Make(Index)) + ' ' + get_string(IA2106.Model(Index))


