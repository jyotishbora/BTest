from forms.out import IA4562SP
from forms.out import IAWBPDISPSP
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Desc_Calculation():
    return get_string(IAWBPDISPSP.Names)

def DisAdj_Calculation(Index):
    return get_currency(IAWBPDISPSP.DisIADep(Index)) - get_currency(IAWBPDISPSP.DisFedDep(Index))

def DisDTServ_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + get_number(IAWBPDISPSP.Offset)
    if get_number(IA4562SP.StateDispNbr) > Stuff:
        return get_string(IAWDepr.DateServ, get_number(IA4562SP.StateDispCopyNbr(Stuff)))
    else:
        return ''

def DisDTSld_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + get_number(IAWBPDISPSP.Offset)
    if get_number(IA4562SP.StateDispNbr) > Stuff:
        return get_string(IAWDepr.DisDTSld, get_number(IA4562SP.StateDispCopyNbr(Stuff)))
    else:
        return ''

def DisFedDep_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + get_number(IAWBPDISPSP.Offset)
    if get_number(IA4562SP.StateDispNbr) > Stuff:
        return get_currency(IAWDepr.SPDisFedDep, get_number(IA4562SP.StateDispCopyNbr(Stuff)))
    else:
        return 0

def DisIADep_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + get_number(IAWBPDISPSP.Offset)
    if get_number(IA4562SP.StateDispNbr) > Stuff:
        return get_currency(IAWDepr.SPDisIADep, get_number(IA4562SP.StateDispCopyNbr(Stuff)))
    else:
        return 0

def DisPropDesc_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + get_number(IAWBPDISPSP.Offset)
    if get_number(IA4562SP.StateDispNbr) > Stuff:
        return get_string(IAWDepr.PropDesc, get_number(IA4562SP.StateDispCopyNbr(Stuff)))
    else:
        return ''

def Names_Calculation():
    return get_string(IA4562SP.Names)

def Offset_Calculation():
    if GetCopy() == 1:
        return 3
    elif GetCopy() == 2:
        return 32
    elif GetCopy() == 3:
        return 61
    elif GetCopy() == 4:
        return 90
    elif GetCopy() == 5:
        return 119
    elif GetCopy() == 6:
        return 148
    elif GetCopy() == 7:
        return 177
    elif GetCopy() == 8:
        return 206
    elif GetCopy() == 9:
        return 235
    elif GetCopy() == 10:
        return 264
    elif GetCopy() == 11:
        return 293
    elif GetCopy() == 12:
        return 322
    elif GetCopy() == 13:
        return 351
    elif GetCopy() == 14:
        return 380
    elif GetCopy() == 15:
        return 409
    elif GetCopy() == 16:
        return 438
    elif GetCopy() == 17:
        return 467
    elif GetCopy() == 18:
        return 496
    elif GetCopy() == 19:
        return 525
    else:
        return 554

def PrWBPDisp_Calculation():
    if get_currency(IAWBPDISPSP.TotDisAdj) != 0:
        return 1
    else:
        return 0

def SSN_Calculation():
    return get_string(IA4562SP.SSN)

def TotDisAdj_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 29:
        SubTot = SubTot + get_currency(IAWBPDISPSP.DisAdj(count))
        count = count + 1
    return SubTot

def TotDisFedDep_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 29:
        SubTot = SubTot + get_currency(IAWBPDISPSP.DisFedDep(count))
        count = count + 1
    return SubTot

def TotDisIADep_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 29:
        SubTot = SubTot + get_currency(IAWBPDISPSP.DisIADep(count))
        count = count + 1
    return SubTot


