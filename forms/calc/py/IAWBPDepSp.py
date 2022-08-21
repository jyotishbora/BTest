from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def AccFedDep_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + GetNumber(IAWBPDepSp.Offset)
    if GetNumber(IA4562Sp.DepSeeAttBool) == 0:
        ReturnVal = 0
    elif GetNumber(IA4562Sp.StateDeprNbr) > Stuff:
        ReturnVal = GetCurrency(IAWDepr.SPAccFedDep, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))
    else:
        ReturnVal = 0

def AccIADep_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + GetNumber(IAWBPDepSp.Offset)
    if GetNumber(IA4562Sp.DepSeeAttBool) == 0:
        ReturnVal = 0
    elif GetNumber(IA4562Sp.StateDeprNbr) > Stuff:
        ReturnVal = GetCurrency(IAWDepr.SPAccIADep, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))
    else:
        ReturnVal = 0

def Basis_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + GetNumber(IAWBPDepSp.Offset)
    if GetNumber(IA4562Sp.DepSeeAttBool) == 0:
        ReturnVal = 0
    elif GetNumber(IA4562Sp.StateDeprNbr) > Stuff:
        ReturnVal = GetCurrency(IAWDepr.SPBasis, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))
    else:
        ReturnVal = 0

def DateServ_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + GetNumber(IAWBPDepSp.Offset)
    if GetNumber(IA4562Sp.DepSeeAttBool) == 0:
        ReturnVal = ''
    elif GetNumber(IA4562Sp.StateDeprNbr) > Stuff:
        ReturnVal = GetString(IAWDepr.DateServ, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))
    else:
        ReturnVal = ''

def Desc_Calculation():
    ReturnVal = GetString(IAWBPDepSp.Names)

def Fed179_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + GetNumber(IAWBPDepSp.Offset)
    if GetNumber(IA4562Sp.DepSeeAttBool) == 0:
        ReturnVal = 0
    elif GetNumber(IA4562Sp.StateDeprNbr) > Stuff:
        ReturnVal = GetCurrency(IAWDepr.SPFed179, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))
    else:
        ReturnVal = 0

def FedDepDed_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + GetNumber(IAWBPDepSp.Offset)
    if GetNumber(IA4562Sp.DepSeeAttBool) == 0:
        ReturnVal = 0
    elif GetNumber(IA4562Sp.StateDeprNbr) > Stuff:
        ReturnVal = GetCurrency(IAWDepr.SPFedDepDed, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))
    else:
        ReturnVal = 0

def IA179_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + GetNumber(IAWBPDepSp.Offset)
    if GetNumber(IA4562Sp.DepSeeAttBool) == 0:
        ReturnVal = 0
    elif GetNumber(IA4562Sp.StateDeprNbr) > Stuff:
        ReturnVal = GetCurrency(IAWDepr.SPIA179, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))
    else:
        ReturnVal = 0

def Life_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + GetNumber(IAWBPDepSp.Offset)
    if GetNumber(IA4562Sp.DepSeeAttBool) == 0:
        ReturnVal = ''
    elif GetNumber(IA4562Sp.StateDeprNbr) > Stuff:
        ReturnVal = GetString(IAWDepr.Life, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))
    else:
        ReturnVal = ''

def MACRSIA_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + GetNumber(IAWBPDepSp.Offset)
    if GetNumber(IA4562Sp.DepSeeAttBool) == 0:
        ReturnVal = 0
    elif GetNumber(IA4562Sp.StateDeprNbr) > Stuff:
        ReturnVal = GetCurrency(IAWDepr.SPMACRSIA, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))
    else:
        ReturnVal = 0

def Names_Calculation():
    ReturnVal = GetString(IA4562Sp.Names)

def Offset_Calculation():
    if GetCopy() == 1:
        ReturnVal = 3 - GetNumber(IA4562PIV.SpCopy)
    elif GetCopy() == 2:
        ReturnVal = 32 - GetNumber(IA4562PIV.SpCopy)
    elif GetCopy() == 3:
        ReturnVal = 61 - GetNumber(IA4562PIV.SpCopy)
    elif GetCopy() == 4:
        ReturnVal = 90 - GetNumber(IA4562PIV.SpCopy)
    elif GetCopy() == 5:
        ReturnVal = 119 - GetNumber(IA4562PIV.SpCopy)
    elif GetCopy() == 6:
        ReturnVal = 148 - GetNumber(IA4562PIV.SpCopy)
    elif GetCopy() == 7:
        ReturnVal = 177 - GetNumber(IA4562PIV.SpCopy)
    elif GetCopy() == 8:
        ReturnVal = 206 - GetNumber(IA4562PIV.SpCopy)
    elif GetCopy() == 9:
        ReturnVal = 235 - GetNumber(IA4562PIV.SpCopy)
    elif GetCopy() == 10:
        ReturnVal = 264 - GetNumber(IA4562PIV.SpCopy)
    elif GetCopy() == 11:
        ReturnVal = 293 - GetNumber(IA4562PIV.SpCopy)
    elif GetCopy() == 12:
        ReturnVal = 322 - GetNumber(IA4562PIV.SpCopy)
    elif GetCopy() == 13:
        ReturnVal = 351 - GetNumber(IA4562PIV.SpCopy)
    elif GetCopy() == 14:
        ReturnVal = 380 - GetNumber(IA4562PIV.SpCopy)
    elif GetCopy() == 15:
        ReturnVal = 409 - GetNumber(IA4562PIV.SpCopy)
    elif GetCopy() == 16:
        ReturnVal = 438 - GetNumber(IA4562PIV.SpCopy)
    elif GetCopy() == 17:
        ReturnVal = 467 - GetNumber(IA4562PIV.SpCopy)
    elif GetCopy() == 18:
        ReturnVal = 496 - GetNumber(IA4562PIV.SpCopy)
    elif GetCopy() == 19:
        ReturnVal = 525 - GetNumber(IA4562PIV.SpCopy)
    else:
        ReturnVal = 554 - GetNumber(IA4562PIV.SpCopy)

def PropDesc_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + GetNumber(IAWBPDepSp.Offset)
    if GetNumber(IA4562Sp.DepSeeAttBool) == 0:
        ReturnVal = ''
    elif GetNumber(IA4562Sp.StateDeprNbr) > Stuff:
        ReturnVal = GetString(IAWDepr.PropDesc, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))
    else:
        ReturnVal = ''

def PrWBPDep_Calculation():
    if GetCurrency(IAWBPDepSp.TotFed179) != 0:
        ReturnVal = 1
    elif GetCurrency(IAWBPDepSp.TotFDD) != 0:
        ReturnVal = 1
    elif GetCurrency(IAWBPDepSp.TotIA179) != 0:
        ReturnVal = 1
    elif GetCurrency(IAWBPDepSp.TotMACRS) != 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def SSN_Calculation():
    ReturnVal = GetString(IA4562Sp.SSN)

def TotFDD_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 29:
        SubTot = SubTot + GetCurrency(IAWBPDepSp.FedDepDed(count))
        count = count + 1
    ReturnVal = SubTot

def TotFed179_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 29:
        SubTot = SubTot + GetCurrency(IAWBPDepSp.Fed179(count))
        count = count + 1
    ReturnVal = SubTot

def TotIA179_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 29:
        SubTot = SubTot + GetCurrency(IAWBPDepSp.IA179(count))
        count = count + 1
    ReturnVal = SubTot

def TotMACRS_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 29:
        SubTot = SubTot + GetCurrency(IAWBPDepSp.MACRSIA(count))
        count = count + 1
    ReturnVal = SubTot

