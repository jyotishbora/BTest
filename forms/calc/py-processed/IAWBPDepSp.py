from forms.out import IA4562PIV
from forms.out import IA4562SP
from forms.out import IAWBPDEPSP
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def AccFedDep_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + get_number(IAWBPDEPSP.Offset)
    if get_number(IA4562SP.DepSeeAttBool) == 0:
        return 0
    elif get_number(IA4562SP.StateDeprNbr) > Stuff:
        return get_currency(IAWDepr.SPAccFedDep, get_number(IA4562SP.StateDeprCopyNbr(Stuff)))
    else:
        return 0

def AccIADep_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + get_number(IAWBPDEPSP.Offset)
    if get_number(IA4562SP.DepSeeAttBool) == 0:
        return 0
    elif get_number(IA4562SP.StateDeprNbr) > Stuff:
        return get_currency(IAWDepr.SPAccIADep, get_number(IA4562SP.StateDeprCopyNbr(Stuff)))
    else:
        return 0

def Basis_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + get_number(IAWBPDEPSP.Offset)
    if get_number(IA4562SP.DepSeeAttBool) == 0:
        return 0
    elif get_number(IA4562SP.StateDeprNbr) > Stuff:
        return get_currency(IAWDepr.SPBasis, get_number(IA4562SP.StateDeprCopyNbr(Stuff)))
    else:
        return 0

def DateServ_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + get_number(IAWBPDEPSP.Offset)
    if get_number(IA4562SP.DepSeeAttBool) == 0:
        return ''
    elif get_number(IA4562SP.StateDeprNbr) > Stuff:
        return get_string(IAWDepr.DateServ, get_number(IA4562SP.StateDeprCopyNbr(Stuff)))
    else:
        return ''

def Desc_Calculation():
    return get_string(IAWBPDEPSP.Names)

def Fed179_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + get_number(IAWBPDEPSP.Offset)
    if get_number(IA4562SP.DepSeeAttBool) == 0:
        return 0
    elif get_number(IA4562SP.StateDeprNbr) > Stuff:
        return get_currency(IAWDepr.SPFed179, get_number(IA4562SP.StateDeprCopyNbr(Stuff)))
    else:
        return 0

def FedDepDed_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + get_number(IAWBPDEPSP.Offset)
    if get_number(IA4562SP.DepSeeAttBool) == 0:
        return 0
    elif get_number(IA4562SP.StateDeprNbr) > Stuff:
        return get_currency(IAWDepr.SPFedDepDed, get_number(IA4562SP.StateDeprCopyNbr(Stuff)))
    else:
        return 0

def IA179_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + get_number(IAWBPDEPSP.Offset)
    if get_number(IA4562SP.DepSeeAttBool) == 0:
        return 0
    elif get_number(IA4562SP.StateDeprNbr) > Stuff:
        return get_currency(IAWDepr.SPIA179, get_number(IA4562SP.StateDeprCopyNbr(Stuff)))
    else:
        return 0

def Life_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + get_number(IAWBPDEPSP.Offset)
    if get_number(IA4562SP.DepSeeAttBool) == 0:
        return ''
    elif get_number(IA4562SP.StateDeprNbr) > Stuff:
        return get_string(IAWDepr.Life, get_number(IA4562SP.StateDeprCopyNbr(Stuff)))
    else:
        return ''

def MACRSIA_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + get_number(IAWBPDEPSP.Offset)
    if get_number(IA4562SP.DepSeeAttBool) == 0:
        return 0
    elif get_number(IA4562SP.StateDeprNbr) > Stuff:
        return get_currency(IAWDepr.SPMACRSIA, get_number(IA4562SP.StateDeprCopyNbr(Stuff)))
    else:
        return 0

def Names_Calculation():
    return get_string(IA4562SP.Names)

def Offset_Calculation():
    if GetCopy() == 1:
        return 3 - get_number(IA4562PIV.SpCopy)
    elif GetCopy() == 2:
        return 32 - get_number(IA4562PIV.SpCopy)
    elif GetCopy() == 3:
        return 61 - get_number(IA4562PIV.SpCopy)
    elif GetCopy() == 4:
        return 90 - get_number(IA4562PIV.SpCopy)
    elif GetCopy() == 5:
        return 119 - get_number(IA4562PIV.SpCopy)
    elif GetCopy() == 6:
        return 148 - get_number(IA4562PIV.SpCopy)
    elif GetCopy() == 7:
        return 177 - get_number(IA4562PIV.SpCopy)
    elif GetCopy() == 8:
        return 206 - get_number(IA4562PIV.SpCopy)
    elif GetCopy() == 9:
        return 235 - get_number(IA4562PIV.SpCopy)
    elif GetCopy() == 10:
        return 264 - get_number(IA4562PIV.SpCopy)
    elif GetCopy() == 11:
        return 293 - get_number(IA4562PIV.SpCopy)
    elif GetCopy() == 12:
        return 322 - get_number(IA4562PIV.SpCopy)
    elif GetCopy() == 13:
        return 351 - get_number(IA4562PIV.SpCopy)
    elif GetCopy() == 14:
        return 380 - get_number(IA4562PIV.SpCopy)
    elif GetCopy() == 15:
        return 409 - get_number(IA4562PIV.SpCopy)
    elif GetCopy() == 16:
        return 438 - get_number(IA4562PIV.SpCopy)
    elif GetCopy() == 17:
        return 467 - get_number(IA4562PIV.SpCopy)
    elif GetCopy() == 18:
        return 496 - get_number(IA4562PIV.SpCopy)
    elif GetCopy() == 19:
        return 525 - get_number(IA4562PIV.SpCopy)
    else:
        return 554 - get_number(IA4562PIV.SpCopy)

def PropDesc_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + get_number(IAWBPDEPSP.Offset)
    if get_number(IA4562SP.DepSeeAttBool) == 0:
        return ''
    elif get_number(IA4562SP.StateDeprNbr) > Stuff:
        return get_string(IAWDepr.PropDesc, get_number(IA4562SP.StateDeprCopyNbr(Stuff)))
    else:
        return ''

def PrWBPDep_Calculation():
    if get_currency(IAWBPDEPSP.TotFed179) != 0:
        return 1
    elif get_currency(IAWBPDEPSP.TotFDD) != 0:
        return 1
    elif get_currency(IAWBPDEPSP.TotIA179) != 0:
        return 1
    elif get_currency(IAWBPDEPSP.TotMACRS) != 0:
        return 1
    else:
        return 0

def SSN_Calculation():
    return get_string(IA4562SP.SSN)

def TotFDD_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 29:
        SubTot = SubTot + get_currency(IAWBPDEPSP.FedDepDed(count))
        count = count + 1
    return SubTot

def TotFed179_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 29:
        SubTot = SubTot + get_currency(IAWBPDEPSP.Fed179(count))
        count = count + 1
    return SubTot

def TotIA179_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 29:
        SubTot = SubTot + get_currency(IAWBPDEPSP.IA179(count))
        count = count + 1
    return SubTot

def TotMACRS_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 29:
        SubTot = SubTot + get_currency(IAWBPDEPSP.MACRSIA(count))
        count = count + 1
    return SubTot


