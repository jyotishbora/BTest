from forms.out import IA4562PIV
from forms.out import IA4562SP
from forms.out import IAF1040
from forms.out import IAREQUIRED
from forms.out import IAWBPDEPSP
from forms.out import IAWBPDISPSP
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def AccFedDep_Calculation(Index):
    Stuff = Integer()
    Stuff = Index - get_number(IA4562PIV.SpCopy)
    if get_number(IA4562PIV.SpCopy) == 1 and Index == 0:
        return 0
    elif get_number(IA4562SP.DepSeeAttBool) == 1 and Index == 3:
        return 0
    else:
        return get_currency(IAWDepr.SPAccFedDep, get_number(IA4562SP.StateDeprCopyNbr(Stuff)))

def AccIADep_Calculation(Index):
    Stuff = Integer()
    Stuff = Index - get_number(IA4562PIV.SpCopy)
    if get_number(IA4562PIV.SpCopy) == 1 and Index == 0:
        return 0
    elif get_number(IA4562SP.DepSeeAttBool) == 1 and Index == 3:
        return 0
    else:
        return get_currency(IAWDepr.SPAccIADep, get_number(IA4562SP.StateDeprCopyNbr(Stuff)))

def Basis_Calculation(Index):
    Stuff = Integer()
    Stuff = Index - get_number(IA4562PIV.SpCopy)
    if get_number(IA4562PIV.SpCopy) == 1 and Index == 0:
        return 0
    elif get_number(IA4562SP.DepSeeAttBool) == 1 and Index == 3:
        return 0
    else:
        return get_currency(IAWDepr.SPBasis, get_number(IA4562SP.StateDeprCopyNbr(Stuff)))

def CrBPDep1_Calculation():
    if ( get_number(IA4562SP.StateDeprNbr) + get_number(IA4562PIV.SpCopy) )  > 4:
        return 1
    else:
        return 0

def CrBPDep10_Calculation():
    if ( get_number(IA4562SP.StateDeprNbr) + get_number(IA4562PIV.SpCopy) )  > 264:
        return 1
    else:
        return 0

def CrBPDep11_Calculation():
    if ( get_number(IA4562SP.StateDeprNbr) + get_number(IA4562PIV.SpCopy) )  > 293:
        return 1
    else:
        return 0

def CrBPDep12_Calculation():
    if ( get_number(IA4562SP.StateDeprNbr) + get_number(IA4562PIV.SpCopy) )  > 322:
        return 1
    else:
        return 0

def CrBPDep13_Calculation():
    if ( get_number(IA4562SP.StateDeprNbr) + get_number(IA4562PIV.SpCopy) )  > 351:
        return 1
    else:
        return 0

def CrBPDep14_Calculation():
    if ( get_number(IA4562SP.StateDeprNbr) + get_number(IA4562PIV.SpCopy) )  > 380:
        return 1
    else:
        return 0

def CrBPDep15_Calculation():
    if ( get_number(IA4562SP.StateDeprNbr) + get_number(IA4562PIV.SpCopy) )  > 409:
        return 1
    else:
        return 0

def CrBPDep16_Calculation():
    if ( get_number(IA4562SP.StateDeprNbr) + get_number(IA4562PIV.SpCopy) )  > 438:
        return 1
    else:
        return 0

def CrBPDep17_Calculation():
    if ( get_number(IA4562SP.StateDeprNbr) + get_number(IA4562PIV.SpCopy) )  > 467:
        return 1
    else:
        return 0

def CrBPDep18_Calculation():
    if ( get_number(IA4562SP.StateDeprNbr) + get_number(IA4562PIV.SpCopy) )  > 496:
        return 1
    else:
        return 0

def CrBPDep19_Calculation():
    if ( get_number(IA4562SP.StateDeprNbr) + get_number(IA4562PIV.SpCopy) )  > 525:
        return 1
    else:
        return 0

def CrBPDep2_Calculation():
    if ( get_number(IA4562SP.StateDeprNbr) + get_number(IA4562PIV.SpCopy) )  > 32:
        return 1
    else:
        return 0

def CrBPDep20_Calculation():
    if ( get_number(IA4562SP.StateDeprNbr) + get_number(IA4562PIV.SpCopy) )  > 554:
        return 1
    else:
        return 0

def CrBPDep3_Calculation():
    if ( get_number(IA4562SP.StateDeprNbr) + get_number(IA4562PIV.SpCopy) )  > 61:
        return 1
    else:
        return 0

def CrBPDep4_Calculation():
    if ( get_number(IA4562SP.StateDeprNbr) + get_number(IA4562PIV.SpCopy) )  > 90:
        return 1
    else:
        return 0

def CrBPDep5_Calculation():
    if ( get_number(IA4562SP.StateDeprNbr) + get_number(IA4562PIV.SpCopy) )  > 119:
        return 1
    else:
        return 0

def CrBPDep6_Calculation():
    if ( get_number(IA4562SP.StateDeprNbr) + get_number(IA4562PIV.SpCopy) )  > 148:
        return 1
    else:
        return 0

def CrBPDep7_Calculation():
    if ( get_number(IA4562SP.StateDeprNbr) + get_number(IA4562PIV.SpCopy) )  > 177:
        return 1
    else:
        return 0

def CrBPDep8_Calculation():
    if ( get_number(IA4562SP.StateDeprNbr) + get_number(IA4562PIV.SpCopy) )  > 206:
        return 1
    else:
        return 0

def CrBPDep9_Calculation():
    if ( get_number(IA4562SP.StateDeprNbr) + get_number(IA4562PIV.SpCopy) )  > 235:
        return 1
    else:
        return 0

def CrBPDisp1_Calculation():
    if get_number(IA4562SP.StateDispNbr) > 4:
        return 1
    else:
        return 0

def CrBPDisp10_Calculation():
    if get_number(IA4562SP.StateDispNbr) > 264:
        return 1
    else:
        return 0

def CrBPDisp11_Calculation():
    if get_number(IA4562SP.StateDispNbr) > 293:
        return 1
    else:
        return 0

def CrBPDisp12_Calculation():
    if get_number(IA4562SP.StateDispNbr) > 322:
        return 1
    else:
        return 0

def CrBPDisp13_Calculation():
    if get_number(IA4562SP.StateDispNbr) > 351:
        return 1
    else:
        return 0

def CrBPDisp14_Calculation():
    if get_number(IA4562SP.StateDispNbr) > 380:
        return 1
    else:
        return 0

def CrBPDisp15_Calculation():
    if get_number(IA4562SP.StateDispNbr) > 409:
        return 1
    else:
        return 0

def CrBPDisp16_Calculation():
    if get_number(IA4562SP.StateDispNbr) > 438:
        return 1
    else:
        return 0

def CrBPDisp17_Calculation():
    if get_number(IA4562SP.StateDispNbr) > 467:
        return 1
    else:
        return 0

def CrBPDisp18_Calculation():
    if get_number(IA4562SP.StateDispNbr) > 496:
        return 1
    else:
        return 0

def CrBPDisp19_Calculation():
    if get_number(IA4562SP.StateDispNbr) > 525:
        return 1
    else:
        return 0

def CrBPDisp2_Calculation():
    if get_number(IA4562SP.StateDispNbr) > 32:
        return 1
    else:
        return 0

def CrBPDisp20_Calculation():
    if get_number(IA4562SP.StateDispNbr) > 554:
        return 1
    else:
        return 0

def CrBPDisp3_Calculation():
    if get_number(IA4562SP.StateDispNbr) > 61:
        return 1
    else:
        return 0

def CrBPDisp4_Calculation():
    if get_number(IA4562SP.StateDispNbr) > 90:
        return 1
    else:
        return 0

def CrBPDisp5_Calculation():
    if get_number(IA4562SP.StateDispNbr) > 119:
        return 1
    else:
        return 0

def CrBPDisp6_Calculation():
    if get_number(IA4562SP.StateDispNbr) > 148:
        return 1
    else:
        return 0

def CrBPDisp7_Calculation():
    if get_number(IA4562SP.StateDispNbr) > 177:
        return 1
    else:
        return 0

def CrBPDisp8_Calculation():
    if get_number(IA4562SP.StateDispNbr) > 206:
        return 1
    else:
        return 0

def CrBPDisp9_Calculation():
    if get_number(IA4562SP.StateDispNbr) > 235:
        return 1
    else:
        return 0

def DateServ_Calculation(Index):
    Stuff = Integer()
    Stuff = Index - get_number(IA4562PIV.SpCopy)
    if get_number(IA4562PIV.SpCopy) == 1 and Index == 0:
        return ''
    elif get_number(IA4562SP.DepSeeAttBool) == 1 and Index == 3:
        return ''
    else:
        return get_string(IAWDepr.DateServ, get_number(IA4562SP.StateDeprCopyNbr(Stuff)))

def DepAdj_Calculation():
    return get_currency(IA4562SP.TotColF) - get_currency(IA4562SP.TotColI)

def DepSeeAttBool_Calculation():
    if ( get_number(IA4562SP.StateDeprNbr) + get_number(IA4562PIV.SpCopy) )  > 4:
        return 1
    else:
        return 0

def Desc_Calculation():
    Total = Currency()
    Total = get_currency(IA4562SP.TotDepAdj)
    return CStr(Total) + ' Adjustment'

def DisAdj_Calculation(Index):
    if get_number(IA4562SP.DisSeeAttBool) == 1 and Index == 3:
        return get_currency(IAWBPDISPSP.TotDisAdj)
    else:
        return get_currency(IA4562SP.DisIADep(Index)) - get_currency(IA4562SP.DisFedDep(Index))

def DisDTServ_Calculation(Index):
    if get_number(IA4562SP.DisSeeAttBool) == 1 and Index == 3:
        return ''
    else:
        return get_string(IAWDepr.DateServ, get_number(IA4562SP.StateDispCopyNbr(Index)))

def DisDTSld_Calculation(Index):
    if get_number(IA4562SP.DisSeeAttBool) == 1 and Index == 3:
        return ''
    else:
        return get_string(IAWDepr.DisDTSld, get_number(IA4562SP.StateDispCopyNbr(Index)))

def DisFedDep_Calculation(Index):
    if get_number(IA4562SP.DisSeeAttBool) == 1 and Index == 3:
        return get_currency(IAWBPDISPSP.TotDisFedDep)
    else:
        return get_currency(IAWDepr.SPDisFedDep, get_number(IA4562SP.StateDispCopyNbr(Index)))

def DisIADep_Calculation(Index):
    if get_number(IA4562SP.DisSeeAttBool) == 1 and Index == 3:
        return get_currency(IAWBPDISPSP.TotDisIADep)
    else:
        return get_currency(IAWDepr.SPDisIADep, get_number(IA4562SP.StateDispCopyNbr(Index)))

def DisPropDesc_Calculation(Index):
    if get_number(IA4562SP.DisSeeAttBool) == 1 and Index == 3:
        return 'See Stmt Att.'
    else:
        return get_string(IAWDepr.PropDesc, get_number(IA4562SP.StateDispCopyNbr(Index)))

def DisSeeAttBool_Calculation():
    if get_number(IA4562SP.StateDispNbr) > 4:
        return 1
    else:
        return 0

def Fed179_Calculation(Index):
    Stuff = Integer()
    Stuff = Index - get_number(IA4562PIV.SpCopy)
    if get_number(IA4562PIV.SpCopy) == 1 and Index == 0:
        return get_currency(IA4562PIV.SPLine1)
    elif get_number(IA4562SP.DepSeeAttBool) == 1 and Index == 3:
        return get_currency(IAWBPDEPSP.TotFed179)
    else:
        return get_currency(IAWDepr.SPFed179, get_number(IA4562SP.StateDeprCopyNbr(Stuff)))

def FedDepDed_Calculation(Index):
    Stuff = Integer()
    Stuff = Index - get_number(IA4562PIV.SpCopy)
    if get_number(IA4562PIV.SpCopy) == 1 and Index == 0:
        return 0
    elif get_number(IA4562SP.DepSeeAttBool) == 1 and Index == 3:
        return get_currency(IAWBPDEPSP.TotFDD)
    else:
        return get_currency(IAWDepr.SPFedDepDed, get_number(IA4562SP.StateDeprCopyNbr(Stuff)))

def IA179_Calculation(Index):
    Stuff = Integer()
    Stuff = Index - get_number(IA4562PIV.SpCopy)
    if get_number(IA4562PIV.SpCopy) == 1 and Index == 0:
        return get_currency(IA4562PIV.SPPartIV179)
    elif get_number(IA4562SP.DepSeeAttBool) == 1 and Index == 3:
        return get_currency(IAWBPDEPSP.TotIA179)
    else:
        return get_currency(IAWDepr.SPIA179, get_number(IA4562SP.StateDeprCopyNbr(Stuff)))

def Life_Calculation(Index):
    Stuff = Integer()
    Stuff = Index - get_number(IA4562PIV.SpCopy)
    if get_number(IA4562PIV.SpCopy) == 1 and Index == 0:
        return ''
    elif get_number(IA4562SP.DepSeeAttBool) == 1 and Index == 3:
        return ''
    else:
        return get_string(IAWDepr.Life, get_number(IA4562SP.StateDeprCopyNbr(Stuff)))

def MACRSIA_Calculation(Index):
    Stuff = Integer()
    Stuff = Index - get_number(IA4562PIV.SpCopy)
    if get_number(IA4562PIV.SpCopy) == 1 and Index == 0:
        return 0
    elif get_number(IA4562SP.DepSeeAttBool) == 1 and Index == 3:
        return get_currency(IAWBPDEPSP.TotMACRS)
    else:
        return get_currency(IAWDepr.SPMACRSIA, get_number(IA4562SP.StateDeprCopyNbr(Stuff)))

def Names_Calculation():
    return get_string(IAREQUIRED.SPCombName)

def PrIA4562_Calculation():
    if get_currency(IA4562SP.TotFed179) != 0:
        return 1
    elif get_currency(IA4562SP.TotFDD) != 0:
        return 1
    elif get_currency(IA4562SP.TotIA179) != 0:
        return 1
    elif get_currency(IA4562SP.TotMACRS) != 0:
        return 1
    elif get_currency(IA4562SP.TotDisAdj) != 0:
        return 1
    else:
        return 0

def PropDesc_Calculation(Index):
    Stuff = Integer()
    Stuff = Index - get_number(IA4562PIV.SpCopy)
    if get_number(IA4562PIV.SpCopy) == 1 and Index == 0:
        return get_string(IA4562PIV.SPPropDescr)
    elif get_number(IA4562SP.DepSeeAttBool) == 1 and Index == 3:
        return 'See Stmt Att.'
    else:
        return get_string(IAWDepr.PropDesc, get_number(IA4562SP.StateDeprCopyNbr(Stuff)))

def SSN_Calculation():
    return get_string(IAF1040.SpouseSSN)

def StateDeprCopyNbr_Calculation(Index):
    count = Long()

    max = Long()

    listedcount = Long()
    listedcount = 0
    max = GetAllCopies(IAWDepr)
    count = 0
    while count < max:
        count = count + 1
        if get_bool(IAWDepr.SpCopy, count) == True:
            if listedcount == Index:
                return count
            else:
                listedcount = listedcount + 1
    return 0

def StateDeprNbr_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Integer()
    Lim = GetAllCopies(IAWDepr)
    count = 1
    Total = 0
    while count <= Lim:
        if get_bool(IAWDepr.SpCopy, count) == True:
            Total = Total + 1
        else:
            Total = Total
        count = count + 1
    return Total

def StateDispCopyNbr_Calculation(Index):
    count = Long()

    max = Long()

    listedcount = Long()
    listedcount = 0
    max = GetAllCopies(IAWDepr)
    count = 0
    while count < max:
        count = count + 1
        if get_bool(IAWDepr.SpCopyDisp, count) == True:
            if listedcount == Index:
                return count
            else:
                listedcount = listedcount + 1
    return 0

def StateDispNbr_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Integer()
    Lim = GetAllCopies(IAWDepr)
    count = 1
    Total = 0
    while count <= Lim:
        if get_bool(IAWDepr.SpCopyDisp, count) == True:
            Total = Total + 1
        else:
            Total = Total
        count = count + 1
    return Total

def TotColF_Calculation():
    return get_currency(IA4562SP.TotFed179) + get_currency(IA4562SP.TotFDD)

def TotFed179_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 4:
        SubTot = SubTot + get_currency(IA4562SP.Fed179(count))
        count = count + 1
    return SubTot

def TotIA179_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 4:
        SubTot = SubTot + get_currency(IA4562SP.IA179(count))
        count = count + 1
    return SubTot

def TotP2ColF_Calculation():
    return get_currency(IA4562SP.TotDisAdj)

def TotColI_Calculation():
    return get_currency(IA4562SP.TotIA179) + get_currency(IA4562SP.TotMACRS)

def TotDepAdj_Calculation():
    return get_currency(IA4562SP.DepAdj) + get_currency(IA4562SP.TotP2ColF)

def TotDisAdj_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 4:
        SubTot = SubTot + get_currency(IA4562SP.DisAdj(count))
        count = count + 1
    return SubTot

def TotDisFedDep_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 4:
        SubTot = SubTot + get_currency(IA4562SP.DisFedDep(count))
        count = count + 1
    return SubTot

def TotDisIADep_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 4:
        SubTot = SubTot + get_currency(IA4562SP.DisIADep(count))
        count = count + 1
    return SubTot

def TotFDD_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 4:
        SubTot = SubTot + get_currency(IA4562SP.FedDepDed(count))
        count = count + 1
    return SubTot

def TotMACRS_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 4:
        SubTot = SubTot + get_currency(IA4562SP.MACRSIA(count))
        count = count + 1
    return SubTot


