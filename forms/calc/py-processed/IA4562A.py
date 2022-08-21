from forms.out import IA4562A
from forms.out import IAF1040
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *
import datetime



def AccFedDep_Calculation(Index):
    Stuff = Long()
    Stuff = get_number(IA4562A.StateDeprCopyNbr(Index))
    if get_number(IA4562A.StateDeprNbr) > Index:
        return get_currency(USW2106Veh.AccumFed, Stuff)
    else:
        return 0

def AccIADep_Calculation(Index):
    Stuff = Long()
    #will need to review next year to make sure prior depr brings forward the limitied IA lux limits
    Stuff = get_number(IA4562A.StateDeprCopyNbr(Index))
    if get_number(IA4562A.StateDeprNbr) > Index:
        if get_bool(USW2106Veh.New, Stuff) == True:
            if get_currency(USW2106Veh.LuxLimState2, Stuff) == 0 and get_currency(USW2106Veh.PerLimState2, Stuff) == 0:
                return get_currency(USW2106Veh.AccumState, Stuff)
            else:
                return get_currency(USW2106Veh.PriorState) + min_value(get_currency(USW2106Veh.DeprNoBonus), get_currency(USW2106Veh.PerLimState2, Stuff))
        else:
            return get_currency(USW2106Veh.AccumState, Stuff)
    else:
        return 0

def Basis_Calculation(Index):
    Stuff = Long()
    Stuff = get_number(IA4562A.StateDeprCopyNbr(Index))
    if get_number(IA4562A.StateDeprNbr) > Index:
        return get_currency(USW2106Veh.Basis, Stuff)
    else:
        return 0

def DateServ_Calculation(Index):
    Stuff = Long()
    Stuff = get_number(IA4562A.StateDeprCopyNbr(Index))
    if get_number(IA4562A.StateDeprNbr) > Index:
        return get_string(USW2106Veh.Date, Stuff)
    else:
        return ''

def DepAdj_Calculation():
    return get_currency(IA4562A.TotColF) - get_currency(IA4562A.TotColI)

def Desc_Calculation():
    return get_string(USF2106.Desc, ParentCopy())

def DisAdj_Calculation(Index):
    return get_currency(IA4562A.DisIADep(Index)) - get_currency(IA4562A.DisFedDep(Index))

def EFSP_Calculation():
    if get_bool(IA4562A.PrIA4562A) == True:
        if get_bool(IAF1040.CombMFS) == False:
            return 0
        elif get_bool(IA4562A.Spouse) == True:
            return 1
        else:
            return 0
    else:
        return 0

def EFSPDisp_Calculation():
    if get_bool(IA4562A.PrIA4562A) == True and get_currency(IA4562A.TotDisAdj) != 0:
        if get_bool(IAF1040.CombMFS) == False:
            return 0
        elif get_bool(IA4562A.Spouse) == True:
            return 1
        else:
            return 0
    else:
        return 0

def EFTPJoint_Calculation():
    if get_bool(IA4562A.PrIA4562A) == True:
        if get_bool(IAF1040.CombMFS) == False:
            return 1
        elif get_bool(IA4562A.Taxpayer) == True:
            return 1
        else:
            return 0
    else:
        return 0

def EFTPJointDisp_Calculation():
    if get_bool(IA4562A.PrIA4562A) == True and get_currency(IA4562A.TotDisAdj) != 0:
        if get_bool(IAF1040.CombMFS) == False:
            return 1
        elif get_bool(IA4562A.Taxpayer) == True:
            return 1
        else:
            return 0
    else:
        return 0

def EmpBusType_Calculation():
    if get_bool(USF2106.QPA, ParentCopy()) == True or get_bool(USF2106.FBO, ParentCopy()) == True or get_bool(USF2106.NatG, ParentCopy()) == True:
        return '1040'
    elif get_bool(USF2106.Disable, ParentCopy()) == True:
        return '27'
    else:
        return '20'

def Exist_Calculation():
    return 1

def Fed179_Calculation(Index):
    Stuff = Long()
    Stuff = get_number(IA4562A.StateDeprCopyNbr(Index))
    if get_number(IA4562A.StateDeprNbr) > Index:
        if get_bool(USW2106Veh.New, Stuff) == True:
            return get_currency(USW2106Veh.Sec179Calc, Stuff)
        else:
            return 0
    else:
        return 0

def FedDepDed_Calculation(Index):
    Stuff = Long()
    Stuff = get_number(IA4562A.StateDeprCopyNbr(Index))
    if get_number(IA4562A.StateDeprNbr) > Index:
        if get_bool(USW2106Veh.New, Stuff) == True:
            return get_currency(USW2106Veh.Bonus, Stuff) + max_value(0, get_currency(USW2106Veh.TotDepr, Stuff) - get_currency(USW2106Veh.Sec179, Stuff) - get_currency(USW2106Veh.Bonus, Stuff))
        else:
            return get_currency(USW2106Veh.TotDepr, Stuff)
    else:
        return 0

def IA179_Calculation(Index):
    Stuff = Long()
    # Iowa not yet coupled with increased Section 179 expensing for 2017
    Stuff = get_number(IA4562A.StateDeprCopyNbr(Index))
    if get_number(IA4562A.StateDeprNbr) > Index:
        if get_bool(USW2106Veh.New, Stuff) == True:
            if get_currency(USW2106Veh.LuxLimState2, Stuff) == 0 and get_currency(USW2106Veh.PerLimState2, Stuff) == 0:
                return get_currency(USW2106Veh.StateSec179Calc, Stuff)
            else:
                return min_value(get_currency(USW2106Veh.StateSec179Calc, Stuff), get_currency(USW2106Veh.PerLimState2, Stuff))
        else:
            return 0
    else:
        return 0

def Life_Calculation(Index):
    if get_string(IA4562A.DateServ(Index)) != '':
        return '5'
    else:
        return ''

def MACRSIA_Calculation(Index):
    Stuff = Long()
    #will need to review this next year for the state basis brought forward when hit the lower IA lux limits, will .DeprNoBonus still be valid
    Stuff = get_number(IA4562A.StateDeprCopyNbr(Index))
    if get_number(IA4562A.StateDeprNbr) > Index:
        if get_bool(USW2106Veh.New, Stuff) == True:
            if get_currency(USW2106Veh.LuxLimState2, Stuff) == 0 and get_currency(USW2106Veh.PerLimState2, Stuff) == 0:
                return max_value(0, get_currency(USW2106Veh.DeprNoBonus, Stuff) - get_currency(USW2106Veh.StateSec179, Stuff))
            else:
                return max_value(0, min_value(get_currency(USW2106Veh.DeprNoBonus, Stuff), get_currency(USW2106Veh.PerLimState2, Stuff)) - get_currency(IA4562A.IA179(Index)))
        else:
            return get_currency(USW2106Veh.DeprNoBonus, Stuff)
    else:
        return 0

def Names_Calculation():
    return get_string(USF2106.FirstName, ParentCopy())

def Owner_Calculation():
    if get_bool(IA4562A.Taxpayer) == True and trim(get_string(USWBasicInfo.FirstName)) == '':
        return 'the taxpayer'
    elif get_bool(IA4562A.Taxpayer) == True:
        return get_string(USWBasicInfo.FirstName)
    elif get_bool(IA4562A.Spouse) == True and trim(get_string(USWBasicInfo.SpouseFirst)) == '':
        return 'the spouse'
    else:
        return get_string(USWBasicInfo.SpouseFirst)

def PrIA4562A_Calculation():
    if get_currency(IA4562A.TotFed179) != 0:
        return 1
    elif get_currency(IA4562A.TotFDD) != 0:
        return 1
    elif get_currency(IA4562A.TotIA179) != 0:
        return 1
    elif get_currency(IA4562A.TotMACRS) != 0:
        return 1
    elif get_currency(IA4562A.TotDisAdj) != 0:
        return 1
    else:
        return 0

def PropDesc_Calculation(Index):
    Stuff = Long()
    Stuff = get_number(IA4562A.StateDeprCopyNbr(Index))
    if get_number(IA4562A.StateDeprNbr) > Index:
        return get_string(USW2106Veh.Occupation, Stuff) + ' Vehicle'
    else:
        return ''

def Spouse_Calculation():
    if get_bool(USF2106.Spouse, ParentCopy()) == True:
        return 1
    else:
        return 0

def SSN_Calculation():
    return get_string(USF2106.SSN, ParentCopy())

def StateDeprCopyNbr_Calculation(Index):
    F2106 = Long()

    DeprCount = Long()

    MaxDepr = Long()

    listedcount = Long()
    F2106 = GetParentCopy(USF2106)
    listedcount = 0
    MaxDepr = GetAllCopies(USW2106Veh)
    DeprCount = 0
    while DeprCount < MaxDepr:
        DeprCount = DeprCount + 1
        if GetParentCopy(USF2106, USW2106Veh, DeprCount) == F2106:
            if ( get_bool(USW2106Veh.BonusYes, DeprCount) == True or get_bool(USW2106Veh.IAFedStSec179, DeprCount) == True or get_bool(USW2106Veh.IAUsingLuxLim, DeprCount) == True )  and get_bool(USW2106Veh.Qualifies, DeprCount) == True:
                if ( GetDate(USW2106Veh.Date, DeprCount) > datetime.datetime(9, 10, 2001) and GetDate(USW2106Veh.Date, DeprCount) < datetime.datetime(5, 6, 2003) )  or  ( GetDate(USW2106Veh.Date, DeprCount) > datetime.datetime(12, 31, 2007) and GetDate(USW2106Veh.Date, DeprCount) < MakeDate(1, 1, YearNumber + 1) ) :
                    if listedcount == Index:
                        return DeprCount
                    else:
                        listedcount = listedcount + 1
    return 0

def StateDeprNbr_Calculation():
    DeprCount = Long()

    F2106 = Long()

    MaxDepr = Long()

    Total = Integer()
    DeprCount = 1
    F2106 = GetParentCopy(USF2106)
    MaxDepr = GetAllCopies(USW2106Veh)
    Total = 0
    while DeprCount <= MaxDepr:
        if GetParentCopy(USF2106, USW2106Veh, DeprCount) == F2106:
            if ( get_bool(USW2106Veh.BonusYes, DeprCount) == True or get_bool(USW2106Veh.IAFedStSec179, DeprCount) == True or get_bool(USW2106Veh.IAUsingLuxLim, DeprCount) == True )  and get_bool(USW2106Veh.Qualifies, DeprCount) == True:
                if ( GetDate(USW2106Veh.Date, DeprCount) > datetime.datetime(9, 10, 2001) and GetDate(USW2106Veh.Date, DeprCount) < datetime.datetime(5, 6, 2003) )  or  ( GetDate(USW2106Veh.Date, DeprCount) > datetime.datetime(12, 31, 2007) and GetDate(USW2106Veh.Date, DeprCount) < MakeDate(1, 1, YearNumber + 1) ) :
                    Total = Total + 1
                else:
                    Total = Total
        DeprCount = DeprCount + 1
    return Total

def StateDispNbr_Calculation():
    DeprCount = Long()

    F2106 = Long()

    MaxDepr = Long()

    Total = Integer()
    #for 2018 make no change since need to ask or alert if had depr adjustment in prior year and need to make and entry for catch-up depr. May need to see next year if should exclude 2018 veh that were not reported on IA4562A since was just on IA 2106
    DeprCount = 1
    F2106 = GetParentCopy(USF2106)
    MaxDepr = GetAllCopies(USW2106Veh)
    Total = 0
    while DeprCount <= MaxDepr:
        if GetParentCopy(USF2106, USW2106Veh, DeprCount) == F2106:
            if get_bool(USW2106Veh.BonusYes, DeprCount) == True and get_string(USW2106Veh.DisposeDate, DeprCount) != '' and  ( ( GetDate(USW2106Veh.Date, DeprCount) > datetime.datetime(9, 10, 2001) and GetDate(USW2106Veh.Date, DeprCount) < datetime.datetime(5, 6, 2003) )  or  ( GetDate(USW2106Veh.Date, DeprCount) > datetime.datetime(12, 31, 2007) and GetDate(USW2106Veh.Date, DeprCount) < MakeDate(1, 1, YearNumber + 1) ) ) :
                Total = Total + 1
            else:
                Total = Total
        DeprCount = DeprCount + 1
    return Total

def Taxpayer_Calculation():
    if get_bool(USF2106.Taxpayer, ParentCopy()) == True:
        return 1
    else:
        return 0

def TotColF_Calculation():
    return get_currency(IA4562A.TotFed179) + get_currency(IA4562A.TotFDD)

def TotFed179_Calculation():
    return get_currency(IA4562A.Fed179(0)) + get_currency(IA4562A.Fed179(1)) + get_currency(IA4562A.Fed179(2)) + get_currency(IA4562A.Fed179(3))

def TotIA179_Calculation():
    return get_currency(IA4562A.IA179(0)) + get_currency(IA4562A.IA179(1)) + get_currency(IA4562A.IA179(2)) + get_currency(IA4562A.IA179(3))

def TotP2ColF_Calculation():
    return get_currency(IA4562A.TotDisAdj)

def TotColI_Calculation():
    return get_currency(IA4562A.TotIA179) + get_currency(IA4562A.TotMACRS)

def TotDepAdj_Calculation():
    return get_currency(IA4562A.DepAdj) + get_currency(IA4562A.TotP2ColF)

def TotDisAdj_Calculation():
    return get_currency(IA4562A.DisAdj(0)) + get_currency(IA4562A.DisAdj(1)) + get_currency(IA4562A.DisAdj(2)) + get_currency(IA4562A.DisAdj(3))

def TotDisFedDep_Calculation():
    return get_currency(IA4562A.DisFedDep(0)) + get_currency(IA4562A.DisFedDep(1)) + get_currency(IA4562A.DisFedDep(2)) + get_currency(IA4562A.DisFedDep(3))

def TotDisIADep_Calculation():
    return get_currency(IA4562A.DisIADep(0)) + get_currency(IA4562A.DisIADep(1)) + get_currency(IA4562A.DisIADep(2)) + get_currency(IA4562A.DisIADep(3))

def TotFDD_Calculation():
    return get_currency(IA4562A.FedDepDed(0)) + get_currency(IA4562A.FedDepDed(1)) + get_currency(IA4562A.FedDepDed(2)) + get_currency(IA4562A.FedDepDed(3))

def TotMACRS_Calculation():
    return get_currency(IA4562A.MACRSIA(0)) + get_currency(IA4562A.MACRSIA(1)) + get_currency(IA4562A.MACRSIA(2)) + get_currency(IA4562A.MACRSIA(3))


