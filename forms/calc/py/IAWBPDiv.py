from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Desc_Calculation():
    ReturnVal = CStr(GetCurrency(IAWBPDiv.TotalDividend)) + ' Additional Dividends'

def DivAcctOwner_Calculation(Index):
    if GetBool(IAWBPDiv.DTp1(Index)) == True:
        ReturnVal = 'Taxpayer'
    elif GetBool(IAWBPDiv.DSp1(Index)) == True:
        ReturnVal = 'Spouse'
    elif GetBool(IAWBPDiv.DJ1(Index)) == True:
        ReturnVal = 'Joint'
    else:
        ReturnVal = ''

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
    DIV = GetNumber(IAWBBump.DIVNbr)
    PartK1 = GetNumber(IAWBBump.PartK1DivNbr)
    SCorpK1 = GetNumber(IAWBBump.SCorpK1DivNbr)
    EstK1 = GetNumber(IAWBBump.EstK1DivNbr)
    F5471 = GetNumber(IAWBBump.F5471Nbr)
    F8621 = GetNumber(IAWBBump.F8621Nbr)
    F8814 = GetNumber(IAWBBump.F8814Nbr)
    MoStuff = Index + GetNumber(IAWBPDiv.Offset)
    if GetNumber(IASchB.TotDIVCopies) == 7:
        ReturnVal = 0
    elif DIV > MoStuff:
        ReturnVal = Round(GetCurrency(USD1099DIV.ORDDIV, GetNumber(IAWBBump.DIV(MoStuff)))) + Round(GetCurrency(USD1099DIV.FedExmpt, GetNumber(IAWBBump.DIV(MoStuff))))
    elif DIV + PartK1 > MoStuff:
        Stuff = ( MoStuff )  - DIV
        ReturnVal = GetCurrency(USDPartK1.Dividends, ( GetNumber(IAWBBump.PartK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1
        ReturnVal = GetCurrency(USDSCorpK1.Dividends, ( GetNumber(IAWBBump.SCorpK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1
        ReturnVal = GetCurrency(USDEstK1.Dividends, ( GetNumber(IAWBBump.EstK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1 - EstK1
        ReturnVal = GetCurrency(USW5471SchI.DivOrd, ( GetNumber(IAWBBump.F5471(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471
        ReturnVal = GetCurrency(USF8621.DivTo1040, ( GetNumber(IAWBBump.F8621(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 + F8814 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471 - F8621
        ReturnVal = GetCurrency(USF8814.L6XL7, ( GetNumber(IAWBBump.F8814(Stuff)) ))
    else:
        ReturnVal = 0

def DivNoPayer_Calculation():
    count = Variant()

    Iter = Integer()
    count = 0
    Iter = 0
    while Iter < 22:
        if GetCurrency(IAWBPDiv.Dividend(Iter)) > 0 and Trim(GetString(IAWBPDiv.DivPayer(Iter))) == '':
            count = count + 1
        Iter = Iter + 1
    if GetBool(IAWBPDiv.Print) == True and count > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

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
    DIV = GetNumber(IAWBBump.DIVNbr)
    PartK1 = GetNumber(IAWBBump.PartK1DivNbr)
    SCorpK1 = GetNumber(IAWBBump.SCorpK1DivNbr)
    EstK1 = GetNumber(IAWBBump.EstK1DivNbr)
    F5471 = GetNumber(IAWBBump.F5471Nbr)
    F8621 = GetNumber(IAWBBump.F8621Nbr)
    F8814 = GetNumber(IAWBBump.F8814Nbr)
    MoStuff = Index + GetNumber(IAWBPDiv.Offset)
    if GetNumber(IASchB.TotDIVCopies) == 7:
        ReturnVal = ''
    elif DIV > MoStuff:
        ReturnVal = GetString(USD1099DIV.PayerName, GetNumber(IAWBBump.DIV(MoStuff)))
    elif DIV + PartK1 > MoStuff:
        Stuff = ( MoStuff )  - DIV
        ReturnVal = GetString(USDPartK1.CoName, ( GetNumber(IAWBBump.PartK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1
        ReturnVal = GetString(USDSCorpK1.CoName, ( GetNumber(IAWBBump.SCorpK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1
        ReturnVal = GetString(USDEstK1.TrustName, ( GetNumber(IAWBBump.EstK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1 - EstK1
        ReturnVal = 'Form 5471'
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471
        ReturnVal = 'Form 8621 - ' + GetString(USF8621.CoName, ( GetNumber(IAWBBump.F8621(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 + F8814 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471 - F8621
        ReturnVal = 'Form 8814 - ' + GetString(USF8814.ChName, ( GetNumber(IAWBBump.F8814(Stuff)) ))
    else:
        ReturnVal = ''

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
    DIV = GetNumber(IAWBBump.DIVNbr)
    PartK1 = GetNumber(IAWBBump.PartK1DivNbr)
    SCorpK1 = GetNumber(IAWBBump.SCorpK1DivNbr)
    EstK1 = GetNumber(IAWBBump.EstK1DivNbr)
    F5471 = GetNumber(IAWBBump.F5471Nbr)
    F8621 = GetNumber(IAWBBump.F8621Nbr)
    F8814 = GetNumber(IAWBBump.F8814Nbr)
    MoStuff = Index + GetNumber(IAWBPDiv.Offset)
    if GetNumber(IASchB.TotDIVCopies) == 7:
        ReturnVal = 0
    elif DIV > MoStuff:
        ReturnVal = GetBool(USD1099DIV.Joint, GetNumber(IAWBBump.DIV(MoStuff)))
    elif DIV + PartK1 > MoStuff:
        Stuff = ( MoStuff )  - DIV
        ReturnVal = GetBool(USDPartK1.Joint, ( GetNumber(IAWBBump.PartK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1
        ReturnVal = GetBool(USDSCorpK1.Joint, ( GetNumber(IAWBBump.SCorpK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1
        ReturnVal = GetBool(USDEstK1.Joint, ( GetNumber(IAWBBump.EstK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1 - EstK1
        ReturnVal = 0
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471
        ReturnVal = GetBool(USF8621.Joint, ( GetNumber(IAWBBump.F8621(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 + F8814 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471 - F8621
        if GetBool(USWBasicInfo.JointCalc) == True:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

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
    DIV = GetNumber(IAWBBump.DIVNbr)
    PartK1 = GetNumber(IAWBBump.PartK1DivNbr)
    SCorpK1 = GetNumber(IAWBBump.SCorpK1DivNbr)
    EstK1 = GetNumber(IAWBBump.EstK1DivNbr)
    F5471 = GetNumber(IAWBBump.F5471Nbr)
    F8621 = GetNumber(IAWBBump.F8621Nbr)
    F8814 = GetNumber(IAWBBump.F8814Nbr)
    MoStuff = Index + GetNumber(IAWBPDiv.Offset)
    if GetNumber(IASchB.TotDIVCopies) == 7:
        ReturnVal = 0
    elif DIV > MoStuff:
        ReturnVal = GetBool(USD1099DIV.Spouse, GetNumber(IAWBBump.DIV(MoStuff)))
    elif DIV + PartK1 > MoStuff:
        Stuff = ( MoStuff )  - DIV
        ReturnVal = GetBool(USDPartK1.Spouse, ( GetNumber(IAWBBump.PartK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1
        ReturnVal = GetBool(USDSCorpK1.Spouse, ( GetNumber(IAWBBump.SCorpK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1
        ReturnVal = GetBool(USDEstK1.Spouse, ( GetNumber(IAWBBump.EstK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1 - EstK1
        if GetString(USW5471SchI.SchISSN, ( GetNumber(IAWBBump.F5471(Stuff)) )) == GetString(USWBasicInfo.SpouseSSN):
            ReturnVal = 1
        else:
            ReturnVal = 0
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471
        ReturnVal = GetBool(USF8621.Spouse, ( GetNumber(IAWBBump.F8621(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 + F8814 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471 - F8621
        ReturnVal = 0
    else:
        ReturnVal = 0

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
    DIV = GetNumber(IAWBBump.DIVNbr)
    PartK1 = GetNumber(IAWBBump.PartK1DivNbr)
    SCorpK1 = GetNumber(IAWBBump.SCorpK1DivNbr)
    EstK1 = GetNumber(IAWBBump.EstK1DivNbr)
    F5471 = GetNumber(IAWBBump.F5471Nbr)
    F8621 = GetNumber(IAWBBump.F8621Nbr)
    F8814 = GetNumber(IAWBBump.F8814Nbr)
    MoStuff = Index + GetNumber(IAWBPDiv.Offset)
    if GetNumber(IASchB.TotDIVCopies) == 7:
        ReturnVal = 0
    elif DIV > MoStuff:
        ReturnVal = GetBool(USD1099DIV.Taxpayer, GetNumber(IAWBBump.DIV(MoStuff)))
    elif DIV + PartK1 > MoStuff:
        Stuff = ( MoStuff )  - DIV
        ReturnVal = GetBool(USDPartK1.Taxpayer, ( GetNumber(IAWBBump.PartK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1
        ReturnVal = GetBool(USDSCorpK1.Taxpayer, ( GetNumber(IAWBBump.SCorpK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1
        ReturnVal = GetBool(USDEstK1.Taxpayer, ( GetNumber(IAWBBump.EstK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1 - EstK1
        if GetString(USW5471SchI.SchISSN, ( GetNumber(IAWBBump.F5471(Stuff)) )) == GetString(USWBasicInfo.SSN):
            ReturnVal = 1
        else:
            ReturnVal = 0
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471
        ReturnVal = GetBool(USF8621.Taxpayer, ( GetNumber(IAWBBump.F8621(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 + F8814 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471 - F8621
        if GetBool(USWBasicInfo.JointCalc) == True:
            ReturnVal = 0
        else:
            ReturnVal = 1
    else:
        ReturnVal = 0

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
    DIV = GetNumber(IAWBBump.DIVNbr)
    PartK1 = GetNumber(IAWBBump.PartK1DivNbr)
    SCorpK1 = GetNumber(IAWBBump.SCorpK1DivNbr)
    EstK1 = GetNumber(IAWBBump.EstK1DivNbr)
    F5471 = GetNumber(IAWBBump.F5471Nbr)
    F8621 = GetNumber(IAWBBump.F8621Nbr)
    F8814 = GetNumber(IAWBBump.F8814Nbr)
    MoStuff = Index + GetNumber(IAWBPDiv.Offset)
    if GetNumber(IASchB.TotDIVCopies) == 7:
        ReturnVal = 0
    elif DIV > MoStuff:
        ReturnVal = Round(GetCurrency(USD1099DIV.Nominee, GetNumber(IAWBBump.DIV(MoStuff)))) + Round(GetCurrency(USD1099DIV.StExmpt, GetNumber(IAWBBump.DIV(MoStuff)))) + Round(GetCurrency(USD1099DIV.FedStExmpt, GetNumber(IAWBBump.DIV(MoStuff)))) + Round(GetCurrency(USD1099DIV.Restricted, GetNumber(IAWBBump.DIV(MoStuff))))
    elif DIV + PartK1 > MoStuff:
        Stuff = ( MoStuff )  - DIV
        ReturnVal = GetCurrency(USDPartK1.NetStTED, ( GetNumber(IAWBBump.PartK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1
        ReturnVal = GetCurrency(USDSCorpK1.NetStTED, ( GetNumber(IAWBBump.SCorpK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1
        ReturnVal = GetCurrency(USDEstK1.NetStTED, ( GetNumber(IAWBBump.EstK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1 - EstK1
        ReturnVal = 0
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471
        ReturnVal = 0
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 + F8814 > MoStuff:
        Stuff = ( MoStuff )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471 - F8621
        ReturnVal = 0
    else:
        ReturnVal = 0

def Exist_Calculation():
    ReturnVal = 1

def Names_Calculation():
    ReturnVal = GetString(IARequired.CombNames)

def Offset_Calculation():
    if GetCopy() == 1:
        ReturnVal = 6
    elif GetCopy() == 2:
        ReturnVal = 28
    elif GetCopy() == 3:
        ReturnVal = 50
    elif GetCopy() == 4:
        ReturnVal = 72
    elif GetCopy() == 5:
        ReturnVal = 94
    elif GetCopy() == 6:
        ReturnVal = 116
    elif GetCopy() == 7:
        ReturnVal = 138
    elif GetCopy() == 8:
        ReturnVal = 160
    elif GetCopy() == 9:
        ReturnVal = 182
    elif GetCopy() == 10:
        ReturnVal = 204
    else:
        ReturnVal = 226

def Print_Calculation():
    if GetNumber(IASchB.PrintIAB) == 1 and GetCurrency(IAWBPDiv.TotalDividend) != 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

def TaxDiv_Calculation(Index):
    ReturnVal = MaxValue(0, GetCurrency(IAWBPDiv.Dividend(Index)) - GetCurrency(IAWBPDiv.ExemptDiv(Index)))

def TotalDividend_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 22:
        SubTot = SubTot + GetCurrency(IAWBPDiv.Dividend(count))
        count = count + 1
    ReturnVal = SubTot

def TotalExemptDiv_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 22:
        SubTot = SubTot + GetCurrency(IAWBPDiv.ExemptDiv(count))
        count = count + 1
    ReturnVal = SubTot

def TotalTaxDiv_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 22:
        SubTot = SubTot + GetCurrency(IAWBPDiv.TaxDiv(count))
        count = count + 1
    ReturnVal = SubTot

