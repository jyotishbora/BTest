from forms.out import IA148BUMPSP
from forms.out import IA148SP
from forms.out import IAWBP148PTESP
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Desc_Calculation():
    return 'Additonal Entities'

def Names_Calculation():
    return get_string(IA148SP.Names)

def Offset_Calculation():
    if GetCopy() == 1:
        return 5
    elif GetCopy() == 2:
        return 35
    elif GetCopy() == 3:
        return 65
    elif GetCopy() == 4:
        return 95
    else:
        return 125

def Print_Calculation():
    if get_bool(IA148SP.Print) == False:
        return 0
    elif trim(get_string(IAWBP148PTESP.PTEName(0))) != '' or trim(get_string(IAWBP148PTESP.PTEEIN(0))) != '':
        return 1
    else:
        return 0

def PTEEIN_Calculation(Index):
    PTE = Integer()

    RefPTE = Integer()

    Stuff = Integer()

    Stuff2 = Integer()

    MoStuff = Integer()
    PTE = get_number(IA148BUMPSP.TotPTE)
    RefPTE = get_number(IA148BUMPSP.TotRefPTE)
    MoStuff = Index + get_number(IAWBP148PTESP.Offset)
    if get_number(IA148SP.TotPTE) == 6:
        return ''
    elif PTE > MoStuff:
        Stuff2 = get_number(IA148BUMPSP.PTEIndexNbr(MoStuff))
        return get_string(IA148BUMPSP.PTEEIN(Stuff2))
    elif PTE + RefPTE > MoStuff:
        Stuff = ( MoStuff )  - PTE
        Stuff2 = get_number(IA148BUMPSP.RefPTEIndexNbr(Stuff))
        return get_string(IA148BUMPSP.RefPTEEIN(Stuff2))
    else:
        return ''

def PTEName_Calculation(Index):
    PTE = Integer()

    RefPTE = Integer()

    Stuff = Integer()

    Stuff2 = Integer()

    MoStuff = Integer()
    PTE = get_number(IA148BUMPSP.TotPTE)
    RefPTE = get_number(IA148BUMPSP.TotRefPTE)
    MoStuff = Index + get_number(IAWBP148PTESP.Offset)
    if get_number(IA148SP.TotPTE) == 6:
        return ''
    elif PTE > MoStuff:
        Stuff2 = get_number(IA148BUMPSP.PTEIndexNbr(MoStuff))
        return get_string(IA148BUMPSP.PTEName(Stuff2))
    elif PTE + RefPTE > MoStuff:
        Stuff = ( MoStuff )  - PTE
        Stuff2 = get_number(IA148BUMPSP.RefPTEIndexNbr(Stuff))
        return get_string(IA148BUMPSP.RefPTEName(Stuff2))
    else:
        return ''

def SSN_Calculation():
    return get_string(IA148SP.SSN)

def TPPerc_Calculation(Index):
    PTE = Integer()

    RefPTE = Integer()

    Stuff = Integer()

    Stuff2 = Integer()

    MoStuff = Integer()
    PTE = get_number(IA148BUMPSP.TotPTE)
    RefPTE = get_number(IA148BUMPSP.TotRefPTE)
    MoStuff = Index + get_number(IAWBP148PTESP.Offset)
    if get_number(IA148SP.TotPTE) == 6:
        return 0
    elif PTE > MoStuff:
        Stuff2 = get_number(IA148BUMPSP.PTEIndexNbr(MoStuff))
        return get_float(IA148BUMPSP.TPPerc(Stuff2))
    elif PTE + RefPTE > MoStuff:
        Stuff = ( MoStuff )  - PTE
        Stuff2 = get_number(IA148BUMPSP.RefPTEIndexNbr(Stuff))
        return get_float(IA148BUMPSP.RefTPPerc(Stuff2))
    else:
        return 0


