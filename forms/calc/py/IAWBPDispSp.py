from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Desc_Calculation():
    ReturnVal = GetString(IAWBPDispSp.Names)

def DisAdj_Calculation(Index):
    ReturnVal = GetCurrency(IAWBPDispSp.DisIADep(Index)) - GetCurrency(IAWBPDispSp.DisFedDep(Index))

def DisDTServ_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + GetNumber(IAWBPDispSp.Offset)
    if GetNumber(IA4562Sp.StateDispNbr) > Stuff:
        ReturnVal = GetString(IAWDepr.DateServ, GetNumber(IA4562Sp.StateDispCopyNbr(Stuff)))
    else:
        ReturnVal = ''

def DisDTSld_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + GetNumber(IAWBPDispSp.Offset)
    if GetNumber(IA4562Sp.StateDispNbr) > Stuff:
        ReturnVal = GetString(IAWDepr.DisDTSld, GetNumber(IA4562Sp.StateDispCopyNbr(Stuff)))
    else:
        ReturnVal = ''

def DisFedDep_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + GetNumber(IAWBPDispSp.Offset)
    if GetNumber(IA4562Sp.StateDispNbr) > Stuff:
        ReturnVal = GetCurrency(IAWDepr.SPDisFedDep, GetNumber(IA4562Sp.StateDispCopyNbr(Stuff)))
    else:
        ReturnVal = 0

def DisIADep_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + GetNumber(IAWBPDispSp.Offset)
    if GetNumber(IA4562Sp.StateDispNbr) > Stuff:
        ReturnVal = GetCurrency(IAWDepr.SPDisIADep, GetNumber(IA4562Sp.StateDispCopyNbr(Stuff)))
    else:
        ReturnVal = 0

def DisPropDesc_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + GetNumber(IAWBPDispSp.Offset)
    if GetNumber(IA4562Sp.StateDispNbr) > Stuff:
        ReturnVal = GetString(IAWDepr.PropDesc, GetNumber(IA4562Sp.StateDispCopyNbr(Stuff)))
    else:
        ReturnVal = ''

def Names_Calculation():
    ReturnVal = GetString(IA4562Sp.Names)

def Offset_Calculation():
    if GetCopy() == 1:
        ReturnVal = 3
    elif GetCopy() == 2:
        ReturnVal = 32
    elif GetCopy() == 3:
        ReturnVal = 61
    elif GetCopy() == 4:
        ReturnVal = 90
    elif GetCopy() == 5:
        ReturnVal = 119
    elif GetCopy() == 6:
        ReturnVal = 148
    elif GetCopy() == 7:
        ReturnVal = 177
    elif GetCopy() == 8:
        ReturnVal = 206
    elif GetCopy() == 9:
        ReturnVal = 235
    elif GetCopy() == 10:
        ReturnVal = 264
    elif GetCopy() == 11:
        ReturnVal = 293
    elif GetCopy() == 12:
        ReturnVal = 322
    elif GetCopy() == 13:
        ReturnVal = 351
    elif GetCopy() == 14:
        ReturnVal = 380
    elif GetCopy() == 15:
        ReturnVal = 409
    elif GetCopy() == 16:
        ReturnVal = 438
    elif GetCopy() == 17:
        ReturnVal = 467
    elif GetCopy() == 18:
        ReturnVal = 496
    elif GetCopy() == 19:
        ReturnVal = 525
    else:
        ReturnVal = 554

def PrWBPDisp_Calculation():
    if GetCurrency(IAWBPDispSp.TotDisAdj) != 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def SSN_Calculation():
    ReturnVal = GetString(IA4562Sp.SSN)

def TotDisAdj_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 29:
        SubTot = SubTot + GetCurrency(IAWBPDispSp.DisAdj(count))
        count = count + 1
    ReturnVal = SubTot

def TotDisFedDep_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 29:
        SubTot = SubTot + GetCurrency(IAWBPDispSp.DisFedDep(count))
        count = count + 1
    ReturnVal = SubTot

def TotDisIADep_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 29:
        SubTot = SubTot + GetCurrency(IAWBPDispSp.DisIADep(count))
        count = count + 1
    ReturnVal = SubTot

