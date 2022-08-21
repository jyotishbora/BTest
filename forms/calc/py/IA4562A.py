from vb2py.vbfunctions import *
from vb2py.vbdebug import *
import datetime



def AccFedDep_Calculation(Index):
    Stuff = Long()
    Stuff = GetNumber(IA4562A.StateDeprCopyNbr(Index))
    if GetNumber(IA4562A.StateDeprNbr) > Index:
        ReturnVal = GetCurrency(USW2106Veh.AccumFed, Stuff)
    else:
        ReturnVal = 0

def AccIADep_Calculation(Index):
    Stuff = Long()
    #will need to review next year to make sure prior depr brings forward the limitied IA lux limits
    Stuff = GetNumber(IA4562A.StateDeprCopyNbr(Index))
    if GetNumber(IA4562A.StateDeprNbr) > Index:
        if GetBool(USW2106Veh.New, Stuff) == True:
            if GetCurrency(USW2106Veh.LuxLimState2, Stuff) == 0 and GetCurrency(USW2106Veh.PerLimState2, Stuff) == 0:
                ReturnVal = GetCurrency(USW2106Veh.AccumState, Stuff)
            else:
                ReturnVal = GetCurrency(USW2106Veh.PriorState) + MinValue(GetCurrency(USW2106Veh.DeprNoBonus), GetCurrency(USW2106Veh.PerLimState2, Stuff))
        else:
            ReturnVal = GetCurrency(USW2106Veh.AccumState, Stuff)
    else:
        ReturnVal = 0

def Basis_Calculation(Index):
    Stuff = Long()
    Stuff = GetNumber(IA4562A.StateDeprCopyNbr(Index))
    if GetNumber(IA4562A.StateDeprNbr) > Index:
        ReturnVal = GetCurrency(USW2106Veh.Basis, Stuff)
    else:
        ReturnVal = 0

def DateServ_Calculation(Index):
    Stuff = Long()
    Stuff = GetNumber(IA4562A.StateDeprCopyNbr(Index))
    if GetNumber(IA4562A.StateDeprNbr) > Index:
        ReturnVal = GetString(USW2106Veh.Date, Stuff)
    else:
        ReturnVal = ''

def DepAdj_Calculation():
    ReturnVal = GetCurrency(IA4562A.TotColF) - GetCurrency(IA4562A.TotColI)

def Desc_Calculation():
    ReturnVal = GetString(USF2106.Desc, ParentCopy())

def DisAdj_Calculation(Index):
    ReturnVal = GetCurrency(IA4562A.DisIADep(Index)) - GetCurrency(IA4562A.DisFedDep(Index))

def EFSP_Calculation():
    if GetBool(IA4562A.PrIA4562A) == True:
        if GetBool(IAF1040.CombMFS) == False:
            ReturnVal = 0
        elif GetBool(IA4562A.Spouse) == True:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def EFSPDisp_Calculation():
    if GetBool(IA4562A.PrIA4562A) == True and GetCurrency(IA4562A.TotDisAdj) != 0:
        if GetBool(IAF1040.CombMFS) == False:
            ReturnVal = 0
        elif GetBool(IA4562A.Spouse) == True:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def EFTPJoint_Calculation():
    if GetBool(IA4562A.PrIA4562A) == True:
        if GetBool(IAF1040.CombMFS) == False:
            ReturnVal = 1
        elif GetBool(IA4562A.Taxpayer) == True:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def EFTPJointDisp_Calculation():
    if GetBool(IA4562A.PrIA4562A) == True and GetCurrency(IA4562A.TotDisAdj) != 0:
        if GetBool(IAF1040.CombMFS) == False:
            ReturnVal = 1
        elif GetBool(IA4562A.Taxpayer) == True:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def EmpBusType_Calculation():
    if GetBool(USF2106.QPA, ParentCopy()) == True or GetBool(USF2106.FBO, ParentCopy()) == True or GetBool(USF2106.NatG, ParentCopy()) == True:
        ReturnVal = '1040'
    elif GetBool(USF2106.Disable, ParentCopy()) == True:
        ReturnVal = '27'
    else:
        ReturnVal = '20'

def Exist_Calculation():
    ReturnVal = 1

def Fed179_Calculation(Index):
    Stuff = Long()
    Stuff = GetNumber(IA4562A.StateDeprCopyNbr(Index))
    if GetNumber(IA4562A.StateDeprNbr) > Index:
        if GetBool(USW2106Veh.New, Stuff) == True:
            ReturnVal = GetCurrency(USW2106Veh.Sec179Calc, Stuff)
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def FedDepDed_Calculation(Index):
    Stuff = Long()
    Stuff = GetNumber(IA4562A.StateDeprCopyNbr(Index))
    if GetNumber(IA4562A.StateDeprNbr) > Index:
        if GetBool(USW2106Veh.New, Stuff) == True:
            ReturnVal = GetCurrency(USW2106Veh.Bonus, Stuff) + MaxValue(0, GetCurrency(USW2106Veh.TotDepr, Stuff) - GetCurrency(USW2106Veh.Sec179, Stuff) - GetCurrency(USW2106Veh.Bonus, Stuff))
        else:
            ReturnVal = GetCurrency(USW2106Veh.TotDepr, Stuff)
    else:
        ReturnVal = 0

def IA179_Calculation(Index):
    Stuff = Long()
    # Iowa not yet coupled with increased Section 179 expensing for 2017
    Stuff = GetNumber(IA4562A.StateDeprCopyNbr(Index))
    if GetNumber(IA4562A.StateDeprNbr) > Index:
        if GetBool(USW2106Veh.New, Stuff) == True:
            if GetCurrency(USW2106Veh.LuxLimState2, Stuff) == 0 and GetCurrency(USW2106Veh.PerLimState2, Stuff) == 0:
                ReturnVal = GetCurrency(USW2106Veh.StateSec179Calc, Stuff)
            else:
                ReturnVal = MinValue(GetCurrency(USW2106Veh.StateSec179Calc, Stuff), GetCurrency(USW2106Veh.PerLimState2, Stuff))
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def Life_Calculation(Index):
    if GetString(IA4562A.DateServ(Index)) != '':
        ReturnVal = '5'
    else:
        ReturnVal = ''

def MACRSIA_Calculation(Index):
    Stuff = Long()
    #will need to review this next year for the state basis brought forward when hit the lower IA lux limits, will .DeprNoBonus still be valid
    Stuff = GetNumber(IA4562A.StateDeprCopyNbr(Index))
    if GetNumber(IA4562A.StateDeprNbr) > Index:
        if GetBool(USW2106Veh.New, Stuff) == True:
            if GetCurrency(USW2106Veh.LuxLimState2, Stuff) == 0 and GetCurrency(USW2106Veh.PerLimState2, Stuff) == 0:
                ReturnVal = MaxValue(0, GetCurrency(USW2106Veh.DeprNoBonus, Stuff) - GetCurrency(USW2106Veh.StateSec179, Stuff))
            else:
                ReturnVal = MaxValue(0, MinValue(GetCurrency(USW2106Veh.DeprNoBonus, Stuff), GetCurrency(USW2106Veh.PerLimState2, Stuff)) - GetCurrency(IA4562A.IA179(Index)))
        else:
            ReturnVal = GetCurrency(USW2106Veh.DeprNoBonus, Stuff)
    else:
        ReturnVal = 0

def Names_Calculation():
    ReturnVal = GetString(USF2106.FirstName, ParentCopy())

def Owner_Calculation():
    if GetBool(IA4562A.Taxpayer) == True and Trim(GetString(USWBasicInfo.FirstName)) == '':
        ReturnVal = 'the taxpayer'
    elif GetBool(IA4562A.Taxpayer) == True:
        ReturnVal = GetString(USWBasicInfo.FirstName)
    elif GetBool(IA4562A.Spouse) == True and Trim(GetString(USWBasicInfo.SpouseFirst)) == '':
        ReturnVal = 'the spouse'
    else:
        ReturnVal = GetString(USWBasicInfo.SpouseFirst)

def PrIA4562A_Calculation():
    if GetCurrency(IA4562A.TotFed179) != 0:
        ReturnVal = 1
    elif GetCurrency(IA4562A.TotFDD) != 0:
        ReturnVal = 1
    elif GetCurrency(IA4562A.TotIA179) != 0:
        ReturnVal = 1
    elif GetCurrency(IA4562A.TotMACRS) != 0:
        ReturnVal = 1
    elif GetCurrency(IA4562A.TotDisAdj) != 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def PropDesc_Calculation(Index):
    Stuff = Long()
    Stuff = GetNumber(IA4562A.StateDeprCopyNbr(Index))
    if GetNumber(IA4562A.StateDeprNbr) > Index:
        ReturnVal = GetString(USW2106Veh.Occupation, Stuff) + ' Vehicle'
    else:
        ReturnVal = ''

def Spouse_Calculation():
    if GetBool(USF2106.Spouse, ParentCopy()) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

def SSN_Calculation():
    ReturnVal = GetString(USF2106.SSN, ParentCopy())

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
            if ( GetBool(USW2106Veh.BonusYes, DeprCount) == True or GetBool(USW2106Veh.IAFedStSec179, DeprCount) == True or GetBool(USW2106Veh.IAUsingLuxLim, DeprCount) == True )  and GetBool(USW2106Veh.Qualifies, DeprCount) == True:
                if ( GetDate(USW2106Veh.Date, DeprCount) > datetime.datetime(9, 10, 2001) and GetDate(USW2106Veh.Date, DeprCount) < datetime.datetime(5, 6, 2003) )  or  ( GetDate(USW2106Veh.Date, DeprCount) > datetime.datetime(12, 31, 2007) and GetDate(USW2106Veh.Date, DeprCount) < MakeDate(1, 1, YearNumber + 1) ) :
                    if listedcount == Index:
                        ReturnVal = DeprCount
                    else:
                        listedcount = listedcount + 1
    ReturnVal = 0

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
            if ( GetBool(USW2106Veh.BonusYes, DeprCount) == True or GetBool(USW2106Veh.IAFedStSec179, DeprCount) == True or GetBool(USW2106Veh.IAUsingLuxLim, DeprCount) == True )  and GetBool(USW2106Veh.Qualifies, DeprCount) == True:
                if ( GetDate(USW2106Veh.Date, DeprCount) > datetime.datetime(9, 10, 2001) and GetDate(USW2106Veh.Date, DeprCount) < datetime.datetime(5, 6, 2003) )  or  ( GetDate(USW2106Veh.Date, DeprCount) > datetime.datetime(12, 31, 2007) and GetDate(USW2106Veh.Date, DeprCount) < MakeDate(1, 1, YearNumber + 1) ) :
                    Total = Total + 1
                else:
                    Total = Total
        DeprCount = DeprCount + 1
    ReturnVal = Total

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
            if GetBool(USW2106Veh.BonusYes, DeprCount) == True and GetString(USW2106Veh.DisposeDate, DeprCount) != '' and  ( ( GetDate(USW2106Veh.Date, DeprCount) > datetime.datetime(9, 10, 2001) and GetDate(USW2106Veh.Date, DeprCount) < datetime.datetime(5, 6, 2003) )  or  ( GetDate(USW2106Veh.Date, DeprCount) > datetime.datetime(12, 31, 2007) and GetDate(USW2106Veh.Date, DeprCount) < MakeDate(1, 1, YearNumber + 1) ) ) :
                Total = Total + 1
            else:
                Total = Total
        DeprCount = DeprCount + 1
    ReturnVal = Total

def Taxpayer_Calculation():
    if GetBool(USF2106.Taxpayer, ParentCopy()) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

def TotColF_Calculation():
    ReturnVal = GetCurrency(IA4562A.TotFed179) + GetCurrency(IA4562A.TotFDD)

def TotFed179_Calculation():
    ReturnVal = GetCurrency(IA4562A.Fed179(0)) + GetCurrency(IA4562A.Fed179(1)) + GetCurrency(IA4562A.Fed179(2)) + GetCurrency(IA4562A.Fed179(3))

def TotIA179_Calculation():
    ReturnVal = GetCurrency(IA4562A.IA179(0)) + GetCurrency(IA4562A.IA179(1)) + GetCurrency(IA4562A.IA179(2)) + GetCurrency(IA4562A.IA179(3))

def TotP2ColF_Calculation():
    ReturnVal = GetCurrency(IA4562A.TotDisAdj)

def TotColI_Calculation():
    ReturnVal = GetCurrency(IA4562A.TotIA179) + GetCurrency(IA4562A.TotMACRS)

def TotDepAdj_Calculation():
    ReturnVal = GetCurrency(IA4562A.DepAdj) + GetCurrency(IA4562A.TotP2ColF)

def TotDisAdj_Calculation():
    ReturnVal = GetCurrency(IA4562A.DisAdj(0)) + GetCurrency(IA4562A.DisAdj(1)) + GetCurrency(IA4562A.DisAdj(2)) + GetCurrency(IA4562A.DisAdj(3))

def TotDisFedDep_Calculation():
    ReturnVal = GetCurrency(IA4562A.DisFedDep(0)) + GetCurrency(IA4562A.DisFedDep(1)) + GetCurrency(IA4562A.DisFedDep(2)) + GetCurrency(IA4562A.DisFedDep(3))

def TotDisIADep_Calculation():
    ReturnVal = GetCurrency(IA4562A.DisIADep(0)) + GetCurrency(IA4562A.DisIADep(1)) + GetCurrency(IA4562A.DisIADep(2)) + GetCurrency(IA4562A.DisIADep(3))

def TotFDD_Calculation():
    ReturnVal = GetCurrency(IA4562A.FedDepDed(0)) + GetCurrency(IA4562A.FedDepDed(1)) + GetCurrency(IA4562A.FedDepDed(2)) + GetCurrency(IA4562A.FedDepDed(3))

def TotMACRS_Calculation():
    ReturnVal = GetCurrency(IA4562A.MACRSIA(0)) + GetCurrency(IA4562A.MACRSIA(1)) + GetCurrency(IA4562A.MACRSIA(2)) + GetCurrency(IA4562A.MACRSIA(3))

