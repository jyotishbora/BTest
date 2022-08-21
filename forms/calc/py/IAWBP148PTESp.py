from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Desc_Calculation():
    ReturnVal = 'Additonal Entities'

def Names_Calculation():
    ReturnVal = GetString(IA148Sp.Names)

def Offset_Calculation():
    if GetCopy() == 1:
        ReturnVal = 5
    elif GetCopy() == 2:
        ReturnVal = 35
    elif GetCopy() == 3:
        ReturnVal = 65
    elif GetCopy() == 4:
        ReturnVal = 95
    else:
        ReturnVal = 125

def Print_Calculation():
    if GetBool(IA148Sp.Print) == False:
        ReturnVal = 0
    elif Trim(GetString(IAWBP148PTESp.PTEName(0))) != '' or Trim(GetString(IAWBP148PTESp.PTEEIN(0))) != '':
        ReturnVal = 1
    else:
        ReturnVal = 0

def PTEEIN_Calculation(Index):
    PTE = Integer()

    RefPTE = Integer()

    Stuff = Integer()

    Stuff2 = Integer()

    MoStuff = Integer()
    PTE = GetNumber(IA148BumpSp.TotPTE)
    RefPTE = GetNumber(IA148BumpSp.TotRefPTE)
    MoStuff = Index + GetNumber(IAWBP148PTESp.Offset)
    if GetNumber(IA148Sp.TotPTE) == 6:
        ReturnVal = ''
    elif PTE > MoStuff:
        Stuff2 = GetNumber(IA148BumpSp.PTEIndexNbr(MoStuff))
        ReturnVal = GetString(IA148BumpSp.PTEEIN(Stuff2))
    elif PTE + RefPTE > MoStuff:
        Stuff = ( MoStuff )  - PTE
        Stuff2 = GetNumber(IA148BumpSp.RefPTEIndexNbr(Stuff))
        ReturnVal = GetString(IA148BumpSp.RefPTEEIN(Stuff2))
    else:
        ReturnVal = ''

def PTEName_Calculation(Index):
    PTE = Integer()

    RefPTE = Integer()

    Stuff = Integer()

    Stuff2 = Integer()

    MoStuff = Integer()
    PTE = GetNumber(IA148BumpSp.TotPTE)
    RefPTE = GetNumber(IA148BumpSp.TotRefPTE)
    MoStuff = Index + GetNumber(IAWBP148PTESp.Offset)
    if GetNumber(IA148Sp.TotPTE) == 6:
        ReturnVal = ''
    elif PTE > MoStuff:
        Stuff2 = GetNumber(IA148BumpSp.PTEIndexNbr(MoStuff))
        ReturnVal = GetString(IA148BumpSp.PTEName(Stuff2))
    elif PTE + RefPTE > MoStuff:
        Stuff = ( MoStuff )  - PTE
        Stuff2 = GetNumber(IA148BumpSp.RefPTEIndexNbr(Stuff))
        ReturnVal = GetString(IA148BumpSp.RefPTEName(Stuff2))
    else:
        ReturnVal = ''

def SSN_Calculation():
    ReturnVal = GetString(IA148Sp.SSN)

def TPPerc_Calculation(Index):
    PTE = Integer()

    RefPTE = Integer()

    Stuff = Integer()

    Stuff2 = Integer()

    MoStuff = Integer()
    PTE = GetNumber(IA148BumpSp.TotPTE)
    RefPTE = GetNumber(IA148BumpSp.TotRefPTE)
    MoStuff = Index + GetNumber(IAWBP148PTESp.Offset)
    if GetNumber(IA148Sp.TotPTE) == 6:
        ReturnVal = 0
    elif PTE > MoStuff:
        Stuff2 = GetNumber(IA148BumpSp.PTEIndexNbr(MoStuff))
        ReturnVal = GetFloat(IA148BumpSp.TPPerc(Stuff2))
    elif PTE + RefPTE > MoStuff:
        Stuff = ( MoStuff )  - PTE
        Stuff2 = GetNumber(IA148BumpSp.RefPTEIndexNbr(Stuff))
        ReturnVal = GetFloat(IA148BumpSp.RefTPPerc(Stuff2))
    else:
        ReturnVal = 0

