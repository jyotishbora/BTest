from forms.out import IAF1040
from forms.out import IAREQUIRED
from forms.out import IASCHB
from forms.out import IAWBBUMP
from forms.out import IAWBPDIV
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Desc_Calculation():
    return CStr(get_currency(IAWBPDIV.TotalDividend)) + ' Additional Dividends'

def DivAcctOwner_Calculation(Index):
    if get_bool(IAWBPDIV.DTp1(Index)) == True:
        return 'Taxpayer'
    elif get_bool(IAWBPDIV.DSp1(Index)) == True:
        return 'Spouse'
    elif get_bool(IAWBPDIV.DJ1(Index)) == True:
        return 'Joint'
    else:
        return ''

def Dividend_Calculation(Index):
    Stuff = Integer()

    MoStuff = Integer()

    DIV = Integer()

    PartK1 = Integer()

    SCorpK1 = Integer()

    EstK1 = Integer()

    F5471 = Integer()

    F8621 = Integer()

    F8814 = Integer()
    DIV = get_number(IAWBBUMP.DIVNbr)
    PartK1 = get_number(IAWBBUMP.PartK1DivNbr)
    SCorpK1 = get_number(IAWBBUMP.SCorpK1DivNbr)
    EstK1 = get_number(IAWBBUMP.EstK1DivNbr)
    F5471 = get_number(IAWBBUMP.F5471Nbr)
    F8621 = get_number(IAWBBUMP.F8621Nbr)
    F8814 = get_number(IAWBBUMP.F8814Nbr)
    MoStuff = Index + get_number(IAWBPDIV.Offset)
    if get_number(IASCHB.TotDIVCopies) == 7:
        return 0
    elif DIV > MoStuff:
        return Round(get_currency(USD1099DIV.ORDDIV, get_number(IAWBBUMP.DIV(MoStuff)))) + Round(get_currency(USD1099DIV.FedExmpt, get_number(IAWBBUMP.DIV(MoStuff))))
    elif DIV + PartK1 > MoStuff:
        Stuff = ( MoStuff )  - DIV
        return get_currency(USDPartK1.Dividends, ( get_number(IAWBBUMP.PartK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1
        return get_currency(USDSCorpK1.Dividends, ( get_number(IAWBBUMP.SCorpK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1
        return get_currency(USDEstK1.Dividends, ( get_number(IAWBBUMP.EstK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1 - EstK1
        return get_currency(USW5471SchI.DivOrd, ( get_number(IAWBBUMP.F5471(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471
        return get_currency(USF8621.DivTo1040, ( get_number(IAWBBUMP.F8621(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 + F8814 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471 - F8621
        return get_currency(USF8814.L6XL7, ( get_number(IAWBBUMP.F8814(Stuff)) ))
    else:
        return 0

def DivNoPayer_Calculation():
    count = Variant()

    Iter = Integer()
    count = 0
    Iter = 0
    while Iter < 22:
        if get_currency(IAWBPDIV.Dividend(Iter)) > 0 and trim(get_string(IAWBPDIV.DivPayer(Iter))) == '':
            count = count + 1
        Iter = Iter + 1
    if get_bool(IAWBPDIV.Print) == True and count > 0:
        return 1
    else:
        return 0

def DivPayer_Calculation(Index):
    Stuff = Integer()

    MoStuff = Integer()

    DIV = Integer()

    PartK1 = Integer()

    SCorpK1 = Integer()

    EstK1 = Integer()

    F5471 = Integer()

    F8621 = Integer()

    F8814 = Integer()
    DIV = get_number(IAWBBUMP.DIVNbr)
    PartK1 = get_number(IAWBBUMP.PartK1DivNbr)
    SCorpK1 = get_number(IAWBBUMP.SCorpK1DivNbr)
    EstK1 = get_number(IAWBBUMP.EstK1DivNbr)
    F5471 = get_number(IAWBBUMP.F5471Nbr)
    F8621 = get_number(IAWBBUMP.F8621Nbr)
    F8814 = get_number(IAWBBUMP.F8814Nbr)
    MoStuff = Index + get_number(IAWBPDIV.Offset)
    if get_number(IASCHB.TotDIVCopies) == 7:
        return ''
    elif DIV > MoStuff:
        return get_string(USD1099DIV.PayerName, get_number(IAWBBUMP.DIV(MoStuff)))
    elif DIV + PartK1 > MoStuff:
        Stuff = ( MoStuff )  - DIV
        return get_string(USDPartK1.CoName, ( get_number(IAWBBUMP.PartK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1
        return get_string(USDSCorpK1.CoName, ( get_number(IAWBBUMP.SCorpK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1
        return get_string(USDEstK1.TrustName, ( get_number(IAWBBUMP.EstK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1 - EstK1
        return 'Form 5471'
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471
        return 'Form 8621 - ' + get_string(USF8621.CoName, ( get_number(IAWBBUMP.F8621(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 + F8814 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471 - F8621
        return 'Form 8814 - ' + get_string(USF8814.ChName, ( get_number(IAWBBUMP.F8814(Stuff)) ))
    else:
        return ''

def DJ1_Calculation(Index):
    Stuff = Integer()

    MoStuff = Integer()

    DIV = Integer()

    PartK1 = Integer()

    SCorpK1 = Integer()

    EstK1 = Integer()

    F5471 = Integer()

    F8621 = Integer()

    F8814 = Integer()
    DIV = get_number(IAWBBUMP.DIVNbr)
    PartK1 = get_number(IAWBBUMP.PartK1DivNbr)
    SCorpK1 = get_number(IAWBBUMP.SCorpK1DivNbr)
    EstK1 = get_number(IAWBBUMP.EstK1DivNbr)
    F5471 = get_number(IAWBBUMP.F5471Nbr)
    F8621 = get_number(IAWBBUMP.F8621Nbr)
    F8814 = get_number(IAWBBUMP.F8814Nbr)
    MoStuff = Index + get_number(IAWBPDIV.Offset)
    if get_number(IASCHB.TotDIVCopies) == 7:
        return 0
    elif DIV > MoStuff:
        return get_bool(USD1099DIV.Joint, get_number(IAWBBUMP.DIV(MoStuff)))
    elif DIV + PartK1 > MoStuff:
        Stuff = ( MoStuff )  - DIV
        return get_bool(USDPartK1.Joint, ( get_number(IAWBBUMP.PartK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1
        return get_bool(USDSCorpK1.Joint, ( get_number(IAWBBUMP.SCorpK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1
        return get_bool(USDEstK1.Joint, ( get_number(IAWBBUMP.EstK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1 - EstK1
        return 0
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471
        return get_bool(USF8621.Joint, ( get_number(IAWBBUMP.F8621(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 + F8814 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471 - F8621
        if get_bool(USWBasicInfo.JointCalc) == True:
            return 1
        else:
            return 0
    else:
        return 0

def DSp1_Calculation(Index):
    Stuff = Integer()

    MoStuff = Integer()

    DIV = Integer()

    PartK1 = Integer()

    SCorpK1 = Integer()

    EstK1 = Integer()

    F5471 = Integer()

    F8621 = Integer()

    F8814 = Integer()
    DIV = get_number(IAWBBUMP.DIVNbr)
    PartK1 = get_number(IAWBBUMP.PartK1DivNbr)
    SCorpK1 = get_number(IAWBBUMP.SCorpK1DivNbr)
    EstK1 = get_number(IAWBBUMP.EstK1DivNbr)
    F5471 = get_number(IAWBBUMP.F5471Nbr)
    F8621 = get_number(IAWBBUMP.F8621Nbr)
    F8814 = get_number(IAWBBUMP.F8814Nbr)
    MoStuff = Index + get_number(IAWBPDIV.Offset)
    if get_number(IASCHB.TotDIVCopies) == 7:
        return 0
    elif DIV > MoStuff:
        return get_bool(USD1099DIV.Spouse, get_number(IAWBBUMP.DIV(MoStuff)))
    elif DIV + PartK1 > MoStuff:
        Stuff = ( MoStuff )  - DIV
        return get_bool(USDPartK1.Spouse, ( get_number(IAWBBUMP.PartK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1
        return get_bool(USDSCorpK1.Spouse, ( get_number(IAWBBUMP.SCorpK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1
        return get_bool(USDEstK1.Spouse, ( get_number(IAWBBUMP.EstK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1 - EstK1
        if get_string(USW5471SchI.SchISSN, ( get_number(IAWBBUMP.F5471(Stuff)) )) == get_string(USWBasicInfo.SpouseSSN):
            return 1
        else:
            return 0
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471
        return get_bool(USF8621.Spouse, ( get_number(IAWBBUMP.F8621(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 + F8814 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471 - F8621
        return 0
    else:
        return 0

def DTp1_Calculation(Index):
    Stuff = Integer()

    MoStuff = Integer()

    DIV = Integer()

    PartK1 = Integer()

    SCorpK1 = Integer()

    EstK1 = Integer()

    F5471 = Integer()

    F8621 = Integer()

    F8814 = Integer()
    DIV = get_number(IAWBBUMP.DIVNbr)
    PartK1 = get_number(IAWBBUMP.PartK1DivNbr)
    SCorpK1 = get_number(IAWBBUMP.SCorpK1DivNbr)
    EstK1 = get_number(IAWBBUMP.EstK1DivNbr)
    F5471 = get_number(IAWBBUMP.F5471Nbr)
    F8621 = get_number(IAWBBUMP.F8621Nbr)
    F8814 = get_number(IAWBBUMP.F8814Nbr)
    MoStuff = Index + get_number(IAWBPDIV.Offset)
    if get_number(IASCHB.TotDIVCopies) == 7:
        return 0
    elif DIV > MoStuff:
        return get_bool(USD1099DIV.Taxpayer, get_number(IAWBBUMP.DIV(MoStuff)))
    elif DIV + PartK1 > MoStuff:
        Stuff = ( MoStuff )  - DIV
        return get_bool(USDPartK1.Taxpayer, ( get_number(IAWBBUMP.PartK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1
        return get_bool(USDSCorpK1.Taxpayer, ( get_number(IAWBBUMP.SCorpK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1
        return get_bool(USDEstK1.Taxpayer, ( get_number(IAWBBUMP.EstK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1 - EstK1
        if get_string(USW5471SchI.SchISSN, ( get_number(IAWBBUMP.F5471(Stuff)) )) == get_string(USWBasicInfo.SSN):
            return 1
        else:
            return 0
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471
        return get_bool(USF8621.Taxpayer, ( get_number(IAWBBUMP.F8621(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 + F8814 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471 - F8621
        if get_bool(USWBasicInfo.JointCalc) == True:
            return 0
        else:
            return 1
    else:
        return 0

def ExemptDiv_Calculation(Index):
    Stuff = Integer()

    MoStuff = Integer()

    DIV = Integer()

    PartK1 = Integer()

    SCorpK1 = Integer()

    EstK1 = Integer()

    F5471 = Integer()

    F8621 = Integer()

    F8814 = Integer()
    DIV = get_number(IAWBBUMP.DIVNbr)
    PartK1 = get_number(IAWBBUMP.PartK1DivNbr)
    SCorpK1 = get_number(IAWBBUMP.SCorpK1DivNbr)
    EstK1 = get_number(IAWBBUMP.EstK1DivNbr)
    F5471 = get_number(IAWBBUMP.F5471Nbr)
    F8621 = get_number(IAWBBUMP.F8621Nbr)
    F8814 = get_number(IAWBBUMP.F8814Nbr)
    MoStuff = Index + get_number(IAWBPDIV.Offset)
    if get_number(IASCHB.TotDIVCopies) == 7:
        return 0
    elif DIV > MoStuff:
        return Round(get_currency(USD1099DIV.Nominee, get_number(IAWBBUMP.DIV(MoStuff)))) + Round(get_currency(USD1099DIV.StExmpt, get_number(IAWBBUMP.DIV(MoStuff)))) + Round(get_currency(USD1099DIV.FedStExmpt, get_number(IAWBBUMP.DIV(MoStuff)))) + Round(get_currency(USD1099DIV.Restricted, get_number(IAWBBUMP.DIV(MoStuff))))
    elif DIV + PartK1 > MoStuff:
        Stuff = ( MoStuff )  - DIV
        return get_currency(USDPartK1.NetStTED, ( get_number(IAWBBUMP.PartK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1
        return get_currency(USDSCorpK1.NetStTED, ( get_number(IAWBBUMP.SCorpK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1
        return get_currency(USDEstK1.NetStTED, ( get_number(IAWBBUMP.EstK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1 - EstK1
        return 0
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471
        return 0
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 + F8814 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471 - F8621
        return 0
    else:
        return 0

def Exist_Calculation():
    return 1

def Names_Calculation():
    return get_string(IAREQUIRED.CombNames)

def Offset_Calculation():
    if GetCopy() == 1:
        return 6
    elif GetCopy() == 2:
        return 28
    elif GetCopy() == 3:
        return 50
    elif GetCopy() == 4:
        return 72
    elif GetCopy() == 5:
        return 94
    elif GetCopy() == 6:
        return 116
    elif GetCopy() == 7:
        return 138
    elif GetCopy() == 8:
        return 160
    elif GetCopy() == 9:
        return 182
    elif GetCopy() == 10:
        return 204
    else:
        return 226

def Print_Calculation():
    if get_number(IASCHB.PrintIAB) == 1 and get_currency(IAWBPDIV.TotalDividend) != 0:
        return 1
    else:
        return 0

def SSN_Calculation():
    return get_string(IAF1040.SSN)

def TaxDiv_Calculation(Index):
    return max_value(0, get_currency(IAWBPDIV.Dividend(Index)) - get_currency(IAWBPDIV.ExemptDiv(Index)))

def TotalDividend_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 22:
        SubTot = SubTot + get_currency(IAWBPDIV.Dividend(count))
        count = count + 1
    return SubTot

def TotalExemptDiv_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 22:
        SubTot = SubTot + get_currency(IAWBPDIV.ExemptDiv(count))
        count = count + 1
    return SubTot

def TotalTaxDiv_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 22:
        SubTot = SubTot + get_currency(IAWBPDIV.TaxDiv(count))
        count = count + 1
    return SubTot


