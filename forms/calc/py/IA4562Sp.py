from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def AccFedDep_Calculation(Index):
    Stuff = Integer()
    Stuff = Index - GetNumber(IA4562PIV.SpCopy)
    if GetNumber(IA4562PIV.SpCopy) == 1 and Index == 0:
        ReturnVal = 0
    elif GetNumber(IA4562Sp.DepSeeAttBool) == 1 and Index == 3:
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(IAWDepr.SPAccFedDep, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))

def AccIADep_Calculation(Index):
    Stuff = Integer()
    Stuff = Index - GetNumber(IA4562PIV.SpCopy)
    if GetNumber(IA4562PIV.SpCopy) == 1 and Index == 0:
        ReturnVal = 0
    elif GetNumber(IA4562Sp.DepSeeAttBool) == 1 and Index == 3:
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(IAWDepr.SPAccIADep, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))

def Basis_Calculation(Index):
    Stuff = Integer()
    Stuff = Index - GetNumber(IA4562PIV.SpCopy)
    if GetNumber(IA4562PIV.SpCopy) == 1 and Index == 0:
        ReturnVal = 0
    elif GetNumber(IA4562Sp.DepSeeAttBool) == 1 and Index == 3:
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(IAWDepr.SPBasis, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))

def CrBPDep1_Calculation():
    if ( GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy) )  > 4:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDep10_Calculation():
    if ( GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy) )  > 264:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDep11_Calculation():
    if ( GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy) )  > 293:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDep12_Calculation():
    if ( GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy) )  > 322:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDep13_Calculation():
    if ( GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy) )  > 351:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDep14_Calculation():
    if ( GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy) )  > 380:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDep15_Calculation():
    if ( GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy) )  > 409:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDep16_Calculation():
    if ( GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy) )  > 438:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDep17_Calculation():
    if ( GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy) )  > 467:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDep18_Calculation():
    if ( GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy) )  > 496:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDep19_Calculation():
    if ( GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy) )  > 525:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDep2_Calculation():
    if ( GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy) )  > 32:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDep20_Calculation():
    if ( GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy) )  > 554:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDep3_Calculation():
    if ( GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy) )  > 61:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDep4_Calculation():
    if ( GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy) )  > 90:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDep5_Calculation():
    if ( GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy) )  > 119:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDep6_Calculation():
    if ( GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy) )  > 148:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDep7_Calculation():
    if ( GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy) )  > 177:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDep8_Calculation():
    if ( GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy) )  > 206:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDep9_Calculation():
    if ( GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy) )  > 235:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDisp1_Calculation():
    if GetNumber(IA4562Sp.StateDispNbr) > 4:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDisp10_Calculation():
    if GetNumber(IA4562Sp.StateDispNbr) > 264:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDisp11_Calculation():
    if GetNumber(IA4562Sp.StateDispNbr) > 293:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDisp12_Calculation():
    if GetNumber(IA4562Sp.StateDispNbr) > 322:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDisp13_Calculation():
    if GetNumber(IA4562Sp.StateDispNbr) > 351:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDisp14_Calculation():
    if GetNumber(IA4562Sp.StateDispNbr) > 380:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDisp15_Calculation():
    if GetNumber(IA4562Sp.StateDispNbr) > 409:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDisp16_Calculation():
    if GetNumber(IA4562Sp.StateDispNbr) > 438:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDisp17_Calculation():
    if GetNumber(IA4562Sp.StateDispNbr) > 467:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDisp18_Calculation():
    if GetNumber(IA4562Sp.StateDispNbr) > 496:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDisp19_Calculation():
    if GetNumber(IA4562Sp.StateDispNbr) > 525:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDisp2_Calculation():
    if GetNumber(IA4562Sp.StateDispNbr) > 32:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDisp20_Calculation():
    if GetNumber(IA4562Sp.StateDispNbr) > 554:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDisp3_Calculation():
    if GetNumber(IA4562Sp.StateDispNbr) > 61:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDisp4_Calculation():
    if GetNumber(IA4562Sp.StateDispNbr) > 90:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDisp5_Calculation():
    if GetNumber(IA4562Sp.StateDispNbr) > 119:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDisp6_Calculation():
    if GetNumber(IA4562Sp.StateDispNbr) > 148:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDisp7_Calculation():
    if GetNumber(IA4562Sp.StateDispNbr) > 177:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDisp8_Calculation():
    if GetNumber(IA4562Sp.StateDispNbr) > 206:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDisp9_Calculation():
    if GetNumber(IA4562Sp.StateDispNbr) > 235:
        ReturnVal = 1
    else:
        ReturnVal = 0

def DateServ_Calculation(Index):
    Stuff = Integer()
    Stuff = Index - GetNumber(IA4562PIV.SpCopy)
    if GetNumber(IA4562PIV.SpCopy) == 1 and Index == 0:
        ReturnVal = ''
    elif GetNumber(IA4562Sp.DepSeeAttBool) == 1 and Index == 3:
        ReturnVal = ''
    else:
        ReturnVal = GetString(IAWDepr.DateServ, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))

def DepAdj_Calculation():
    ReturnVal = GetCurrency(IA4562Sp.TotColF) - GetCurrency(IA4562Sp.TotColI)

def DepSeeAttBool_Calculation():
    if ( GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy) )  > 4:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Desc_Calculation():
    Total = Currency()
    Total = GetCurrency(IA4562Sp.TotDepAdj)
    ReturnVal = CStr(Total) + ' Adjustment'

def DisAdj_Calculation(Index):
    if GetNumber(IA4562Sp.DisSeeAttBool) == 1 and Index == 3:
        ReturnVal = GetCurrency(IAWBPDispSp.TotDisAdj)
    else:
        ReturnVal = GetCurrency(IA4562Sp.DisIADep(Index)) - GetCurrency(IA4562Sp.DisFedDep(Index))

def DisDTServ_Calculation(Index):
    if GetNumber(IA4562Sp.DisSeeAttBool) == 1 and Index == 3:
        ReturnVal = ''
    else:
        ReturnVal = GetString(IAWDepr.DateServ, GetNumber(IA4562Sp.StateDispCopyNbr(Index)))

def DisDTSld_Calculation(Index):
    if GetNumber(IA4562Sp.DisSeeAttBool) == 1 and Index == 3:
        ReturnVal = ''
    else:
        ReturnVal = GetString(IAWDepr.DisDTSld, GetNumber(IA4562Sp.StateDispCopyNbr(Index)))

def DisFedDep_Calculation(Index):
    if GetNumber(IA4562Sp.DisSeeAttBool) == 1 and Index == 3:
        ReturnVal = GetCurrency(IAWBPDispSp.TotDisFedDep)
    else:
        ReturnVal = GetCurrency(IAWDepr.SPDisFedDep, GetNumber(IA4562Sp.StateDispCopyNbr(Index)))

def DisIADep_Calculation(Index):
    if GetNumber(IA4562Sp.DisSeeAttBool) == 1 and Index == 3:
        ReturnVal = GetCurrency(IAWBPDispSp.TotDisIADep)
    else:
        ReturnVal = GetCurrency(IAWDepr.SPDisIADep, GetNumber(IA4562Sp.StateDispCopyNbr(Index)))

def DisPropDesc_Calculation(Index):
    if GetNumber(IA4562Sp.DisSeeAttBool) == 1 and Index == 3:
        ReturnVal = 'See Stmt Att.'
    else:
        ReturnVal = GetString(IAWDepr.PropDesc, GetNumber(IA4562Sp.StateDispCopyNbr(Index)))

def DisSeeAttBool_Calculation():
    if GetNumber(IA4562Sp.StateDispNbr) > 4:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Fed179_Calculation(Index):
    Stuff = Integer()
    Stuff = Index - GetNumber(IA4562PIV.SpCopy)
    if GetNumber(IA4562PIV.SpCopy) == 1 and Index == 0:
        ReturnVal = GetCurrency(IA4562PIV.SPLine1)
    elif GetNumber(IA4562Sp.DepSeeAttBool) == 1 and Index == 3:
        ReturnVal = GetCurrency(IAWBPDepSp.TotFed179)
    else:
        ReturnVal = GetCurrency(IAWDepr.SPFed179, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))

def FedDepDed_Calculation(Index):
    Stuff = Integer()
    Stuff = Index - GetNumber(IA4562PIV.SpCopy)
    if GetNumber(IA4562PIV.SpCopy) == 1 and Index == 0:
        ReturnVal = 0
    elif GetNumber(IA4562Sp.DepSeeAttBool) == 1 and Index == 3:
        ReturnVal = GetCurrency(IAWBPDepSp.TotFDD)
    else:
        ReturnVal = GetCurrency(IAWDepr.SPFedDepDed, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))

def IA179_Calculation(Index):
    Stuff = Integer()
    Stuff = Index - GetNumber(IA4562PIV.SpCopy)
    if GetNumber(IA4562PIV.SpCopy) == 1 and Index == 0:
        ReturnVal = GetCurrency(IA4562PIV.SPPartIV179)
    elif GetNumber(IA4562Sp.DepSeeAttBool) == 1 and Index == 3:
        ReturnVal = GetCurrency(IAWBPDepSp.TotIA179)
    else:
        ReturnVal = GetCurrency(IAWDepr.SPIA179, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))

def Life_Calculation(Index):
    Stuff = Integer()
    Stuff = Index - GetNumber(IA4562PIV.SpCopy)
    if GetNumber(IA4562PIV.SpCopy) == 1 and Index == 0:
        ReturnVal = ''
    elif GetNumber(IA4562Sp.DepSeeAttBool) == 1 and Index == 3:
        ReturnVal = ''
    else:
        ReturnVal = GetString(IAWDepr.Life, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))

def MACRSIA_Calculation(Index):
    Stuff = Integer()
    Stuff = Index - GetNumber(IA4562PIV.SpCopy)
    if GetNumber(IA4562PIV.SpCopy) == 1 and Index == 0:
        ReturnVal = 0
    elif GetNumber(IA4562Sp.DepSeeAttBool) == 1 and Index == 3:
        ReturnVal = GetCurrency(IAWBPDepSp.TotMACRS)
    else:
        ReturnVal = GetCurrency(IAWDepr.SPMACRSIA, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))

def Names_Calculation():
    ReturnVal = GetString(IARequired.SPCombName)

def PrIA4562_Calculation():
    if GetCurrency(IA4562Sp.TotFed179) != 0:
        ReturnVal = 1
    elif GetCurrency(IA4562Sp.TotFDD) != 0:
        ReturnVal = 1
    elif GetCurrency(IA4562Sp.TotIA179) != 0:
        ReturnVal = 1
    elif GetCurrency(IA4562Sp.TotMACRS) != 0:
        ReturnVal = 1
    elif GetCurrency(IA4562Sp.TotDisAdj) != 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def PropDesc_Calculation(Index):
    Stuff = Integer()
    Stuff = Index - GetNumber(IA4562PIV.SpCopy)
    if GetNumber(IA4562PIV.SpCopy) == 1 and Index == 0:
        ReturnVal = GetString(IA4562PIV.SPPropDescr)
    elif GetNumber(IA4562Sp.DepSeeAttBool) == 1 and Index == 3:
        ReturnVal = 'See Stmt Att.'
    else:
        ReturnVal = GetString(IAWDepr.PropDesc, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SpouseSSN)

def StateDeprCopyNbr_Calculation(Index):
    count = Long()

    max = Long()

    listedcount = Long()
    listedcount = 0
    max = GetAllCopies(IAWDepr)
    count = 0
    while count < max:
        count = count + 1
        if GetBool(IAWDepr.SpCopy, count) == True:
            if listedcount == Index:
                ReturnVal = count
            else:
                listedcount = listedcount + 1
    ReturnVal = 0

def StateDeprNbr_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Integer()
    Lim = GetAllCopies(IAWDepr)
    count = 1
    Total = 0
    while count <= Lim:
        if GetBool(IAWDepr.SpCopy, count) == True:
            Total = Total + 1
        else:
            Total = Total
        count = count + 1
    ReturnVal = Total

def StateDispCopyNbr_Calculation(Index):
    count = Long()

    max = Long()

    listedcount = Long()
    listedcount = 0
    max = GetAllCopies(IAWDepr)
    count = 0
    while count < max:
        count = count + 1
        if GetBool(IAWDepr.SpCopyDisp, count) == True:
            if listedcount == Index:
                ReturnVal = count
            else:
                listedcount = listedcount + 1
    ReturnVal = 0

def StateDispNbr_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Integer()
    Lim = GetAllCopies(IAWDepr)
    count = 1
    Total = 0
    while count <= Lim:
        if GetBool(IAWDepr.SpCopyDisp, count) == True:
            Total = Total + 1
        else:
            Total = Total
        count = count + 1
    ReturnVal = Total

def TotColF_Calculation():
    ReturnVal = GetCurrency(IA4562Sp.TotFed179) + GetCurrency(IA4562Sp.TotFDD)

def TotFed179_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 4:
        SubTot = SubTot + GetCurrency(IA4562Sp.Fed179(count))
        count = count + 1
    ReturnVal = SubTot

def TotIA179_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 4:
        SubTot = SubTot + GetCurrency(IA4562Sp.IA179(count))
        count = count + 1
    ReturnVal = SubTot

def TotP2ColF_Calculation():
    ReturnVal = GetCurrency(IA4562Sp.TotDisAdj)

def TotColI_Calculation():
    ReturnVal = GetCurrency(IA4562Sp.TotIA179) + GetCurrency(IA4562Sp.TotMACRS)

def TotDepAdj_Calculation():
    ReturnVal = GetCurrency(IA4562Sp.DepAdj) + GetCurrency(IA4562Sp.TotP2ColF)

def TotDisAdj_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 4:
        SubTot = SubTot + GetCurrency(IA4562Sp.DisAdj(count))
        count = count + 1
    ReturnVal = SubTot

def TotDisFedDep_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 4:
        SubTot = SubTot + GetCurrency(IA4562Sp.DisFedDep(count))
        count = count + 1
    ReturnVal = SubTot

def TotDisIADep_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 4:
        SubTot = SubTot + GetCurrency(IA4562Sp.DisIADep(count))
        count = count + 1
    ReturnVal = SubTot

def TotFDD_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 4:
        SubTot = SubTot + GetCurrency(IA4562Sp.FedDepDed(count))
        count = count + 1
    ReturnVal = SubTot

def TotMACRS_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 4:
        SubTot = SubTot + GetCurrency(IA4562Sp.MACRSIA(count))
        count = count + 1
    ReturnVal = SubTot

