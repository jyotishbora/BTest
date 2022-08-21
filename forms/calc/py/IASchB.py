from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def AccMktDiscIntCopies_Calculation():
    TPAccMktDiscInt = Integer()

    SPAccMktDiscInt = Integer()

    JTAccMktDiscInt = Integer()
    if GetCurrency(IASchB.TPAccMktDiscInt) > 0:
        TPAccMktDiscInt = 1
    else:
        TPAccMktDiscInt = 0
    if GetCurrency(IASchB.SPAccMktDiscInt) > 0:
        SPAccMktDiscInt = 1
    else:
        SPAccMktDiscInt = 0
    if GetCurrency(IASchB.JtAccMktDiscInt) > 0:
        JTAccMktDiscInt = 1
    else:
        JTAccMktDiscInt = 0
    ReturnVal = TPAccMktDiscInt + SPAccMktDiscInt + JTAccMktDiscInt

def ContigentPayCopies_Calculation():
    TPContigentPay = Integer()

    SPContigentPay = Integer()

    JTContigentPay = Integer()
    if GetCurrency(IASchB.TPContigentPay) > 0:
        TPContigentPay = 1
    else:
        TPContigentPay = 0
    if GetCurrency(IASchB.SPContigentPay) > 0:
        SPContigentPay = 1
    else:
        SPContigentPay = 0
    if GetCurrency(IASchB.JtContigentPay) > 0:
        JTContigentPay = 1
    else:
        JTContigentPay = 0
    ReturnVal = TPContigentPay + SPContigentPay + JTContigentPay

def CrBP11_Calculation():
    if GetNumber(IASchB.TotINTCopies) > 226:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBP12_Calculation():
    if GetNumber(IASchB.TotINTCopies) > 248:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBP1_Calculation():
    if GetNumber(IASchB.TotINTCopies) > 7:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBP10_Calculation():
    if GetNumber(IASchB.TotINTCopies) > 204:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBP2_Calculation():
    if GetNumber(IASchB.TotINTCopies) > 28:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBP3_Calculation():
    if GetNumber(IASchB.TotINTCopies) > 50:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBP4_Calculation():
    if GetNumber(IASchB.TotINTCopies) > 72:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBP5_Calculation():
    if GetNumber(IASchB.TotINTCopies) > 94:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBP6_Calculation():
    if GetNumber(IASchB.TotINTCopies) > 116:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBP7_Calculation():
    if GetNumber(IASchB.TotINTCopies) > 138:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBP8_Calculation():
    if GetNumber(IASchB.TotINTCopies) > 160:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBP9_Calculation():
    if GetNumber(IASchB.TotINTCopies) > 182:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDiv10_Calculation():
    if GetNumber(IASchB.TotDIVCopies) > 204:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDiv11_Calculation():
    if GetNumber(IASchB.TotDIVCopies) > 226:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDiv1_Calculation():
    if GetNumber(IASchB.TotDIVCopies) > 7:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDiv2_Calculation():
    if GetNumber(IASchB.TotDIVCopies) > 28:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDiv3_Calculation():
    if GetNumber(IASchB.TotDIVCopies) > 50:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDiv4_Calculation():
    if GetNumber(IASchB.TotDIVCopies) > 72:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDiv5_Calculation():
    if GetNumber(IASchB.TotDIVCopies) > 94:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDiv6_Calculation():
    if GetNumber(IASchB.TotDIVCopies) > 116:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDiv7_Calculation():
    if GetNumber(IASchB.TotDIVCopies) > 138:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDiv8_Calculation():
    if GetNumber(IASchB.TotDIVCopies) > 160:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrBPDiv9_Calculation():
    if GetNumber(IASchB.TotDIVCopies) > 182:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Desc_Calculation():
    ReturnVal = GetString(IARequired.CombNames)

def DivAcctOwner_Calculation(Index):
    if GetBool(IASchB.DTp1(Index)) == True:
        ReturnVal = 'Taxpayer'
    elif GetBool(IASchB.DSp1(Index)) == True:
        ReturnVal = 'Spouse'
    elif GetBool(IASchB.DJ1(Index)) == True:
        ReturnVal = 'Joint'
    else:
        ReturnVal = ''

def Dividend_Calculation(Index):
    Stuff = Integer()

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
    if Index == 6 and GetNumber(IASchB.TotDIVCopies) > 7:
        ReturnVal = GetCurrency(IAWBPDiv.TotalDividend)
    elif DIV > Index:
        ReturnVal = Round(GetCurrency(USD1099DIV.ORDDIV, GetNumber(IAWBBump.DIV(Index)))) + Round(GetCurrency(USD1099DIV.FedExmpt, GetNumber(IAWBBump.DIV(Index))))
    elif DIV + PartK1 > Index:
        Stuff = ( Index )  - DIV
        ReturnVal = GetCurrency(USDPartK1.Dividends, ( GetNumber(IAWBBump.PartK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 > Index:
        Stuff = ( Index )  - DIV - PartK1
        ReturnVal = GetCurrency(USDSCorpK1.Dividends, ( GetNumber(IAWBBump.SCorpK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1
        ReturnVal = GetCurrency(USDEstK1.Dividends, ( GetNumber(IAWBBump.EstK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1 - EstK1
        ReturnVal = GetCurrency(USW5471SchI.DivOrd, ( GetNumber(IAWBBump.F5471(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471
        ReturnVal = GetCurrency(USF8621.DivTo1040, ( GetNumber(IAWBBump.F8621(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 + F8814 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471 - F8621
        ReturnVal = GetCurrency(USF8814.L6XL7, ( GetNumber(IAWBBump.F8814(Stuff)) ))
    else:
        ReturnVal = 0

def DivPayer_Calculation(Index):
    Stuff = Integer()

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
    if Index == 6 and GetNumber(IASchB.TotDIVCopies) > 7:
        ReturnVal = 'See Statement Attached'
    elif DIV > Index:
        ReturnVal = GetString(USD1099DIV.PayerName, GetNumber(IAWBBump.DIV(Index)))
    elif DIV + PartK1 > Index:
        Stuff = ( Index )  - DIV
        ReturnVal = GetString(USDPartK1.CoName, ( GetNumber(IAWBBump.PartK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 > Index:
        Stuff = ( Index )  - DIV - PartK1
        ReturnVal = GetString(USDSCorpK1.CoName, ( GetNumber(IAWBBump.SCorpK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1
        ReturnVal = GetString(USDEstK1.TrustName, ( GetNumber(IAWBBump.EstK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1 - EstK1
        ReturnVal = 'Form 5471'
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471
        ReturnVal = 'Form 8621 - ' + GetString(USF8621.CoName, ( GetNumber(IAWBBump.F8621(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 + F8814 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471 - F8621
        ReturnVal = 'Form 8814 - ' + GetString(USF8814.ChName, ( GetNumber(IAWBBump.F8814(Stuff)) ))
    else:
        ReturnVal = ''

def DJ1_Calculation(Index):
    Stuff = Integer()

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
    if Index == 6 and GetNumber(IASchB.TotDIVCopies) > 7:
        ReturnVal = 0
    elif DIV > Index:
        ReturnVal = GetBool(USD1099DIV.Joint, GetNumber(IAWBBump.DIV(Index)))
    elif DIV + PartK1 > Index:
        Stuff = ( Index )  - DIV
        ReturnVal = GetBool(USDPartK1.Joint, ( GetNumber(IAWBBump.PartK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 > Index:
        Stuff = ( Index )  - DIV - PartK1
        ReturnVal = GetBool(USDSCorpK1.Joint, ( GetNumber(IAWBBump.SCorpK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1
        ReturnVal = GetBool(USDEstK1.Joint, ( GetNumber(IAWBBump.EstK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1 - EstK1
        ReturnVal = 0
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471
        ReturnVal = GetBool(USF8621.Joint, ( GetNumber(IAWBBump.F8621(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 + F8814 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471 - F8621
        if GetBool(USWBasicInfo.JointCalc) == True:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def DSp1_Calculation(Index):
    Stuff = Integer()

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
    if Index == 6 and GetNumber(IASchB.TotDIVCopies) > 7:
        ReturnVal = 0
    elif DIV > Index:
        ReturnVal = GetBool(USD1099DIV.Spouse, GetNumber(IAWBBump.DIV(Index)))
    elif DIV + PartK1 > Index:
        Stuff = ( Index )  - DIV
        ReturnVal = GetBool(USDPartK1.Spouse, ( GetNumber(IAWBBump.PartK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 > Index:
        Stuff = ( Index )  - DIV - PartK1
        ReturnVal = GetBool(USDSCorpK1.Spouse, ( GetNumber(IAWBBump.SCorpK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1
        ReturnVal = GetBool(USDEstK1.Spouse, ( GetNumber(IAWBBump.EstK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1 - EstK1
        if GetString(USW5471SchI.SchISSN, ( GetNumber(IAWBBump.F5471(Stuff)) )) == GetString(USWBasicInfo.SpouseSSN):
            ReturnVal = 1
        else:
            ReturnVal = 0
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471
        ReturnVal = GetBool(USF8621.Spouse, ( GetNumber(IAWBBump.F8621(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 + F8814 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471 - F8621
        ReturnVal = 0
    else:
        ReturnVal = 0

def DTp1_Calculation(Index):
    Stuff = Integer()

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
    if Index == 6 and GetNumber(IASchB.TotDIVCopies) > 7:
        ReturnVal = 0
    elif DIV > Index:
        ReturnVal = GetBool(USD1099DIV.Taxpayer, GetNumber(IAWBBump.DIV(Index)))
    elif DIV + PartK1 > Index:
        Stuff = ( Index )  - DIV
        ReturnVal = GetBool(USDPartK1.Taxpayer, ( GetNumber(IAWBBump.PartK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 > Index:
        Stuff = ( Index )  - DIV - PartK1
        ReturnVal = GetBool(USDSCorpK1.Taxpayer, ( GetNumber(IAWBBump.SCorpK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1
        ReturnVal = GetBool(USDEstK1.Taxpayer, ( GetNumber(IAWBBump.EstK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1 - EstK1
        if GetString(USW5471SchI.SchISSN, ( GetNumber(IAWBBump.F5471(Stuff)) )) == GetString(USWBasicInfo.SSN):
            ReturnVal = 1
        else:
            ReturnVal = 0
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471
        ReturnVal = GetBool(USF8621.Taxpayer, ( GetNumber(IAWBBump.F8621(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 + F8814 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471 - F8621
        if GetBool(USWBasicInfo.JointCalc) == True:
            ReturnVal = 0
        else:
            ReturnVal = 1
    else:
        ReturnVal = 0

def ExemptDiv_Calculation(Index):
    Stuff = Integer()

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
    if Index == 6 and GetNumber(IASchB.TotDIVCopies) > 7:
        ReturnVal = GetCurrency(IAWBPDiv.TotalExemptDiv)
    elif DIV > Index:
        ReturnVal = Round(GetCurrency(USD1099DIV.Nominee, GetNumber(IAWBBump.DIV(Index)))) + Round(GetCurrency(USD1099DIV.StExmpt, GetNumber(IAWBBump.DIV(Index)))) + Round(GetCurrency(USD1099DIV.FedStExmpt, GetNumber(IAWBBump.DIV(Index)))) + Round(GetCurrency(USD1099DIV.Restricted, GetNumber(IAWBBump.DIV(Index))))
    elif DIV + PartK1 > Index:
        Stuff = ( Index )  - DIV
        ReturnVal = GetCurrency(USDPartK1.NetStTED, ( GetNumber(IAWBBump.PartK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 > Index:
        Stuff = ( Index )  - DIV - PartK1
        ReturnVal = GetCurrency(USDSCorpK1.NetStTED, ( GetNumber(IAWBBump.SCorpK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1
        ReturnVal = GetCurrency(USDEstK1.NetStTED, ( GetNumber(IAWBBump.EstK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1 - EstK1
        ReturnVal = 0
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471
        ReturnVal = 0
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 + F8814 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471 - F8621
        ReturnVal = 0
    else:
        ReturnVal = 0

def ExemptInt_Calculation(Index):
    Stuff = Integer()

    ResSFM = Integer()

    OthSFM = Integer()

    OID = Integer()

    INT1099 = Integer()

    PartK1 = Integer()

    SCorpK1 = Integer()

    EstK1 = Integer()

    TPAccMktDisc = Boolean()
    ResSFM = GetNumber(IAWBBump.ResSFMNbr)
    OthSFM = GetNumber(IAWBBump.OthSFMNbr)
    OID = GetNumber(IAWBBump.OIDNbr)
    INT1099 = GetNumber(IAWBBump.INTNbr)
    PartK1 = GetNumber(IAWBBump.PartK1Nbr)
    SCorpK1 = GetNumber(IAWBBump.SCorpK1Nbr)
    EstK1 = GetNumber(IAWBBump.EstK1Nbr)
    TPAccMktDisc = GetBool(IASchB.TPAccMktDiscInt)
    if Index == 6 and GetNumber(IASchB.TotINTCopies) > 7:
        ReturnVal = GetCurrency(IAWBPInt.TotalExemptInt)
    elif ResSFM > Index:
        ReturnVal = 0
    elif ResSFM + OthSFM > Index:
        Stuff = ( Index )  - ResSFM
        ReturnVal = 0
    elif ResSFM + OthSFM + OID > Index:
        Stuff = ( Index )  - ResSFM - OthSFM
        ReturnVal = Round(GetCurrency(USD1099OID.USInt, ( GetNumber(IAWBBump.OID(Stuff)) ))) + Round(GetCurrency(USD1099OID.StExempt, ( GetNumber(IAWBBump.OID(Stuff)) ))) + Round(GetCurrency(USD1099OID.Nominee, ( GetNumber(IAWBBump.OID(Stuff)) ))) + MaxValue(0, Round(GetCurrency(USD1099OID.BOIDAdjAmt, ( GetNumber(IAWBBump.OID(Stuff)) ))))
    elif ResSFM + OthSFM + OID + INT1099 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID
        ReturnVal = Round(GetCurrency(USD1099INT.USInt, ( GetNumber(IAWBBump.INT(Stuff)) ))) + Round(GetCurrency(USD1099INT.Nominee, ( GetNumber(IAWBBump.INT(Stuff)) ))) + Round(GetCurrency(USD1099INT.AccruedInt, ( GetNumber(IAWBBump.INT(Stuff)) ))) + Round(GetCurrency(USD1099INT.ABP, ( GetNumber(IAWBBump.INT(Stuff)) ))) + Round(GetCurrency(USD1099INT.StateExmpt, ( GetNumber(IAWBBump.INT(Stuff)) )))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099
        ReturnVal = GetCurrency(USDPartK1.NetStTEI, ( GetNumber(IAWBBump.PartK1(Stuff)) )) + GetCurrency(USDPartK1.FedStTEI, ( GetNumber(IAWBBump.PartK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1
        ReturnVal = GetCurrency(USDSCorpK1.NetStTEI, ( GetNumber(IAWBBump.SCorpK1(Stuff)) )) + GetCurrency(USDSCorpK1.FedStTEI, ( GetNumber(IAWBBump.SCorpK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1
        ReturnVal = GetCurrency(USDEstK1.NetStTEI, ( GetNumber(IAWBBump.EstK1(Stuff)) )) + GetCurrency(USDEstK1.FedStTEI, ( GetNumber(IAWBBump.EstK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + GetBool(IASchB.TPAccMktDiscInt) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1
        ReturnVal = 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - GetBool(IASchB.TPAccMktDiscInt)
        ReturnVal = 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt)
        ReturnVal = 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt)
        ReturnVal = 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay)
        ReturnVal = 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) + GetBool(IASchB.JtContigentPay) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay) - GetBool(IASchB.SPContigentPay)
        ReturnVal = 0
    else:
        ReturnVal = 0

def IJ1_Calculation(Index):
    Stuff = Integer()

    ResSFM = Integer()

    OthSFM = Integer()

    OID = Integer()

    INT1099 = Integer()

    PartK1 = Integer()

    SCorpK1 = Integer()

    EstK1 = Integer()

    TPAccMktDisc = Boolean()
    ResSFM = GetNumber(IAWBBump.ResSFMNbr)
    OthSFM = GetNumber(IAWBBump.OthSFMNbr)
    OID = GetNumber(IAWBBump.OIDNbr)
    INT1099 = GetNumber(IAWBBump.INTNbr)
    PartK1 = GetNumber(IAWBBump.PartK1Nbr)
    SCorpK1 = GetNumber(IAWBBump.SCorpK1Nbr)
    EstK1 = GetNumber(IAWBBump.EstK1Nbr)
    TPAccMktDisc = GetBool(IASchB.TPAccMktDiscInt)
    if Index == 6 and GetNumber(IASchB.TotINTCopies) > 7:
        ReturnVal = 0
    elif ResSFM > Index:
        ReturnVal = GetBool(USDSFM.Joint, GetNumber(IAWBBump.ResSFM(Index)))
    elif ResSFM + OthSFM > Index:
        Stuff = ( Index )  - ResSFM
        ReturnVal = GetBool(USDSFM.Joint, ( GetNumber(IAWBBump.OthSFM(Stuff)) ))
    elif ResSFM + OthSFM + OID > Index:
        Stuff = ( Index )  - ResSFM - OthSFM
        ReturnVal = GetBool(USD1099OID.Joint, ( GetNumber(IAWBBump.OID(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID
        ReturnVal = GetBool(USD1099INT.Joint, ( GetNumber(IAWBBump.Int(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099
        ReturnVal = GetBool(USDPartK1.Joint, ( GetNumber(IAWBBump.PartK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1
        ReturnVal = GetBool(USDSCorpK1.Joint, ( GetNumber(IAWBBump.SCorpK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1
        ReturnVal = GetBool(USDEstK1.Joint, ( GetNumber(IAWBBump.EstK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1
        ReturnVal = 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc
        ReturnVal = 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt)
        ReturnVal = 1
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt)
        ReturnVal = 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay)
        ReturnVal = 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) + GetBool(IASchB.JtContigentPay) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay) - GetBool(IASchB.SPContigentPay)
        ReturnVal = 1
    else:
        ReturnVal = 0

def IntAcctOwner_Calculation(Index):
    if GetBool(IASchB.ITp1(Index)) == True:
        ReturnVal = 'Taxpayer'
    elif GetBool(IASchB.ISp1(Index)) == True:
        ReturnVal = 'Spouse'
    elif GetBool(IASchB.IJ1(Index)) == True:
        ReturnVal = 'Joint'
    else:
        ReturnVal = ''

def Interest_Calculation(Index):
    Stuff = Integer()

    ResSFM = Integer()

    OthSFM = Integer()

    OID = Integer()

    INT1099 = Integer()

    PartK1 = Integer()

    SCorpK1 = Integer()

    EstK1 = Integer()

    TPAccMktDisc = Boolean()
    ResSFM = GetNumber(IAWBBump.ResSFMNbr)
    OthSFM = GetNumber(IAWBBump.OthSFMNbr)
    OID = GetNumber(IAWBBump.OIDNbr)
    INT1099 = GetNumber(IAWBBump.INTNbr)
    PartK1 = GetNumber(IAWBBump.PartK1Nbr)
    SCorpK1 = GetNumber(IAWBBump.SCorpK1Nbr)
    EstK1 = GetNumber(IAWBBump.EstK1Nbr)
    TPAccMktDisc = GetBool(IASchB.TPAccMktDiscInt)
    if Index == 6 and GetNumber(IASchB.TotINTCopies) > 7:
        ReturnVal = GetCurrency(IAWBPInt.TotalInterest)
    elif ResSFM > Index:
        ReturnVal = Round(GetCurrency(USDSFM.Interest, GetNumber(IAWBBump.ResSFM(Index))))
    elif ResSFM + OthSFM > Index:
        Stuff = ( Index )  - ResSFM
        ReturnVal = Round(GetCurrency(USDSFM.Interest, ( GetNumber(IAWBBump.OthSFM(Stuff)) )))
    elif ResSFM + OthSFM + OID > Index:
        Stuff = ( Index )  - ResSFM - OthSFM
        ReturnVal = GetCurrency(USD1099OID.BAmt, ( GetNumber(IAWBBump.OID(Stuff)) )) + Round(GetCurrency(USD1099OID.TaxExempt, ( GetNumber(IAWBBump.OID(Stuff)) ))) - MinValue(0, Round(GetCurrency(USD1099OID.BOIDAdjAmt, ( GetNumber(IAWBBump.OID(Stuff)) ))))
    elif ResSFM + OthSFM + OID + INT1099 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID
        ReturnVal = GetCurrency(USD1099INT.BAmtEF, ( GetNumber(IAWBBump.INT(Stuff)) )) + GetCurrency(USD1099INT.FedExmpt, ( GetNumber(IAWBBump.INT(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099
        ReturnVal = GetCurrency(USDPartK1.HaveInt, ( GetNumber(IAWBBump.PartK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1
        ReturnVal = GetCurrency(USDSCorpK1.HaveInt, ( GetNumber(IAWBBump.SCorpK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1
        ReturnVal = GetCurrency(USDEstK1.HaveInt, ( GetNumber(IAWBBump.EstK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1
        ReturnVal = GetCurrency(IASchB.TPAccMktDiscInt)
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc
        ReturnVal = GetCurrency(IASchB.SPAccMktDiscInt)
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt)
        ReturnVal = GetCurrency(IASchB.JtAccMktDiscInt)
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt)
        ReturnVal = GetCurrency(IASchB.TPContigentPay)
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay)
        ReturnVal = GetCurrency(IASchB.SPContigentPay)
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) + GetBool(IASchB.JtContigentPay) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay) - GetBool(IASchB.SPContigentPay)
        ReturnVal = GetCurrency(IASchB.JtContigentPay)
    else:
        ReturnVal = 0

def ISp1_Calculation(Index):
    Stuff = Integer()

    ResSFM = Integer()

    OthSFM = Integer()

    OID = Integer()

    INT1099 = Integer()

    PartK1 = Integer()

    SCorpK1 = Integer()

    EstK1 = Integer()

    TPAccMktDisc = Boolean()
    ResSFM = GetNumber(IAWBBump.ResSFMNbr)
    OthSFM = GetNumber(IAWBBump.OthSFMNbr)
    OID = GetNumber(IAWBBump.OIDNbr)
    INT1099 = GetNumber(IAWBBump.INTNbr)
    PartK1 = GetNumber(IAWBBump.PartK1Nbr)
    SCorpK1 = GetNumber(IAWBBump.SCorpK1Nbr)
    EstK1 = GetNumber(IAWBBump.EstK1Nbr)
    TPAccMktDisc = GetBool(IASchB.TPAccMktDiscInt)
    if Index == 6 and GetNumber(IASchB.TotINTCopies) > 7:
        ReturnVal = 0
    elif ResSFM > Index:
        ReturnVal = GetBool(USDSFM.Spouse, GetNumber(IAWBBump.ResSFM(Index)))
    elif ResSFM + OthSFM > Index:
        Stuff = ( Index )  - ResSFM
        ReturnVal = GetBool(USDSFM.Spouse, ( GetNumber(IAWBBump.OthSFM(Stuff)) ))
    elif ResSFM + OthSFM + OID > Index:
        Stuff = ( Index )  - ResSFM - OthSFM
        ReturnVal = GetBool(USD1099OID.Spouse, ( GetNumber(IAWBBump.OID(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID
        ReturnVal = GetBool(USD1099INT.Spouse, ( GetNumber(IAWBBump.Int(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099
        ReturnVal = GetBool(USDPartK1.Spouse, ( GetNumber(IAWBBump.PartK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1
        ReturnVal = GetBool(USDSCorpK1.Spouse, ( GetNumber(IAWBBump.SCorpK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1
        ReturnVal = GetBool(USDEstK1.Spouse, ( GetNumber(IAWBBump.EstK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1
        ReturnVal = 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc
        ReturnVal = 1
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt)
        ReturnVal = 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt)
        ReturnVal = 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay)
        ReturnVal = 1
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) + GetBool(IASchB.JtContigentPay) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay) - GetBool(IASchB.SPContigentPay)
        ReturnVal = 0
    else:
        ReturnVal = 0

def ITp1_Calculation(Index):
    Stuff = Integer()

    ResSFM = Integer()

    OthSFM = Integer()

    OID = Integer()

    INT1099 = Integer()

    PartK1 = Integer()

    SCorpK1 = Integer()

    EstK1 = Integer()

    TPAccMktDisc = Boolean()
    ResSFM = GetNumber(IAWBBump.ResSFMNbr)
    OthSFM = GetNumber(IAWBBump.OthSFMNbr)
    OID = GetNumber(IAWBBump.OIDNbr)
    INT1099 = GetNumber(IAWBBump.INTNbr)
    PartK1 = GetNumber(IAWBBump.PartK1Nbr)
    SCorpK1 = GetNumber(IAWBBump.SCorpK1Nbr)
    EstK1 = GetNumber(IAWBBump.EstK1Nbr)
    TPAccMktDisc = GetBool(IASchB.TPAccMktDiscInt)
    if Index == 6 and GetNumber(IASchB.TotINTCopies) > 7:
        ReturnVal = 0
    elif ResSFM > Index:
        ReturnVal = GetBool(USDSFM.Taxpayer, GetNumber(IAWBBump.ResSFM(Index)))
    elif ResSFM + OthSFM > Index:
        Stuff = ( Index )  - ResSFM
        ReturnVal = GetBool(USDSFM.Taxpayer, ( GetNumber(IAWBBump.OthSFM(Stuff)) ))
    elif ResSFM + OthSFM + OID > Index:
        Stuff = ( Index )  - ResSFM - OthSFM
        ReturnVal = GetBool(USD1099OID.Taxpayer, ( GetNumber(IAWBBump.OID(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID
        ReturnVal = GetBool(USD1099INT.Taxpayer, ( GetNumber(IAWBBump.Int(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099
        ReturnVal = GetBool(USDPartK1.Taxpayer, ( GetNumber(IAWBBump.PartK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1
        ReturnVal = GetBool(USDSCorpK1.Taxpayer, ( GetNumber(IAWBBump.SCorpK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1
        ReturnVal = GetBool(USDEstK1.Taxpayer, ( GetNumber(IAWBBump.EstK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1
        ReturnVal = 1
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc
        ReturnVal = 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt)
        ReturnVal = 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt)
        ReturnVal = 1
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay)
        ReturnVal = 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) + GetBool(IASchB.JtContigentPay) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay) - GetBool(IASchB.SPContigentPay)
        ReturnVal = 0
    else:
        ReturnVal = 0

def JtAccMktDiscInt_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Currency()
    Lim = GetAllCopies(USDCapGain)
    count = 1
    Total = 0
    while count <= Lim:
        if GetBool(USDCapGain.Joint, count) == True and GetCurrency(USDCapGain.IntIncome, count) > 0:
            Total = Total + GetCurrency(USDCapGain.IntIncome, count)
        else:
            Total = Total
        count = count + 1
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = Total
    else:
        ReturnVal = 0

def JtContigentPay_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Currency()
    Lim = GetAllCopies(USDCapGain)
    count = 1
    Total = 0
    while count <= Lim:
        if GetBool(USDCapGain.Joint, count) == True and GetBool(USDCapGain.Ordinary, count) == True:
            Total = Total + GetCurrency(USDCapGain.OrdGain, count) - GetCurrency(USDCapGain.OrdLoss, count)
        else:
            Total = Total
        count = count + 1
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = Total
    else:
        ReturnVal = 0

def Names_Calculation():
    ReturnVal = GetString(IARequired.CombNames)

def Payer_Calculation(Index):
    Stuff = Integer()

    ResSFM = Integer()

    OthSFM = Integer()

    OID = Integer()

    INT1099 = Integer()

    PartK1 = Integer()

    SCorpK1 = Integer()

    EstK1 = Integer()

    TPAccMktDisc = Boolean()
    ResSFM = GetNumber(IAWBBump.ResSFMNbr)
    OthSFM = GetNumber(IAWBBump.OthSFMNbr)
    OID = GetNumber(IAWBBump.OIDNbr)
    INT1099 = GetNumber(IAWBBump.INTNbr)
    PartK1 = GetNumber(IAWBBump.PartK1Nbr)
    SCorpK1 = GetNumber(IAWBBump.SCorpK1Nbr)
    EstK1 = GetNumber(IAWBBump.EstK1Nbr)
    TPAccMktDisc = GetBool(IASchB.TPAccMktDiscInt)
    if Index == 6 and GetNumber(IASchB.TotINTCopies) > 7:
        ReturnVal = 'See Statement Attached'
    elif ResSFM > Index:
        ReturnVal = GetString(USDSFM.NameAdd, GetNumber(IAWBBump.ResSFM(Index)))
    elif ResSFM + OthSFM > Index:
        Stuff = ( Index )  - ResSFM
        ReturnVal = GetString(USDSFM.PayerName, ( GetNumber(IAWBBump.OthSFM(Stuff)) ))
    elif ResSFM + OthSFM + OID > Index:
        Stuff = ( Index )  - ResSFM - OthSFM
        ReturnVal = GetString(USD1099OID.PayerName, ( GetNumber(IAWBBump.OID(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID
        ReturnVal = GetString(USD1099INT.PayerName, ( GetNumber(IAWBBump.Int(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099
        ReturnVal = GetString(USDPartK1.CoName, ( GetNumber(IAWBBump.PartK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1
        ReturnVal = GetString(USDSCorpK1.CoName, ( GetNumber(IAWBBump.SCorpK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1
        ReturnVal = GetString(USDEstK1.TrustName, ( GetNumber(IAWBBump.EstK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1
        ReturnVal = 'Accrued Market Discount'
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc
        ReturnVal = 'Accrued Market Discount'
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt)
        ReturnVal = 'Accrued Market Discount'
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt)
        ReturnVal = 'Contingent Payment Debt Instrument'
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay)
        ReturnVal = 'Contingent Payment Debt Instrument'
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) + GetBool(IASchB.JtContigentPay) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay) - GetBool(IASchB.SPContigentPay)
        ReturnVal = 'Contingent Payment Debt Instrument'
    else:
        ReturnVal = ''

def PrintIAB_Calculation():
    if GetCurrency(IASchB.TotalInterest) > Decimal("1500") or GetCurrency(IASchB.TotalDividend) > Decimal("1500"):
        ReturnVal = 1
    else:
        ReturnVal = 0

def SPAccMktDiscInt_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Currency()
    Lim = GetAllCopies(USDCapGain)
    count = 1
    Total = 0
    while count <= Lim:
        if GetBool(USDCapGain.Spouse, count) == True and GetCurrency(USDCapGain.IntIncome, count) > 0:
            Total = Total + GetCurrency(USDCapGain.IntIncome, count)
        else:
            Total = Total
        count = count + 1
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = Total
    else:
        ReturnVal = 0

def SPContigentPay_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Currency()
    Lim = GetAllCopies(USDCapGain)
    count = 1
    Total = 0
    while count <= Lim:
        if GetBool(USDCapGain.Spouse, count) == True and GetBool(USDCapGain.Ordinary, count) == True:
            Total = Total + GetCurrency(USDCapGain.OrdGain, count) - GetCurrency(USDCapGain.OrdLoss, count)
        else:
            Total = Total
        count = count + 1
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = Total
    else:
        ReturnVal = 0

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

def TaxDiv_Calculation(Index):
    ReturnVal = MaxValue(0, GetCurrency(IASchB.Dividend(Index)) - GetCurrency(IASchB.ExemptDiv(Index)))

def TaxInt_Calculation(Index):
    ReturnVal = MaxValue(0, GetCurrency(IASchB.Interest(Index)) - GetCurrency(IASchB.ExemptInt(Index)))

def TotAccMktDiscInt_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Currency()
    Lim = GetAllCopies(USDCapGain)
    count = 1
    Total = 0
    while count <= Lim:
        if GetCurrency(USDCapGain.IntIncome, count) > 0:
            Total = Total + GetCurrency(USDCapGain.IntIncome, count)
        else:
            Total = Total
        count = count + 1
    ReturnVal = Round(Total)

def TotalDividend_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 7:
        SubTot = SubTot + GetCurrency(IASchB.Dividend(count))
        count = count + 1
    ReturnVal = SubTot

def TotalExemptDiv_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 7:
        SubTot = SubTot + GetCurrency(IASchB.ExemptDiv(count))
        count = count + 1
    ReturnVal = SubTot

def TotalExemptInt_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 7:
        SubTot = SubTot + GetCurrency(IASchB.ExemptInt(count))
        count = count + 1
    ReturnVal = SubTot

def TotalInterest_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 7:
        SubTot = SubTot + GetCurrency(IASchB.Interest(count))
        count = count + 1
    ReturnVal = SubTot

def TotalTaxDiv_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 7:
        SubTot = SubTot + GetCurrency(IASchB.TaxDiv(count))
        count = count + 1
    ReturnVal = SubTot

def TotalTaxInt_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 7:
        SubTot = SubTot + GetCurrency(IASchB.TaxInt(count))
        count = count + 1
    ReturnVal = SubTot

def TotContigentPay_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Currency()
    Lim = GetAllCopies(USDCapGain)
    count = 1
    Total = 0
    while count <= Lim:
        if GetBool(USDCapGain.Ordinary, count) == True:
            Total = Total + GetCurrency(USDCapGain.OrdGain, count) - GetCurrency(USDCapGain.OrdLoss, count)
        else:
            Total = Total
        count = count + 1
    ReturnVal = Round(Total)

def TotDIVCopies_Calculation():
    ReturnVal = GetNumber(IAWBBump.DIVNbr) + GetNumber(IAWBBump.PartK1DivNbr) + GetNumber(IAWBBump.SCorpK1DivNbr) + GetNumber(IAWBBump.EstK1DivNbr) + GetNumber(IAWBBump.F5471Nbr) + GetNumber(IAWBBump.F8621Nbr) + GetNumber(IAWBBump.F8814Nbr)

def TotINTCopies_Calculation():
    ReturnVal = GetNumber(IAWBBump.ResSFMNbr) + GetNumber(IAWBBump.OthSFMNbr) + GetNumber(IAWBBump.OIDNbr) + GetNumber(IAWBBump.INTNbr) + GetNumber(IAWBBump.PartK1Nbr) + GetNumber(IAWBBump.SCorpK1Nbr) + GetNumber(IAWBBump.EstK1Nbr) + GetNumber(IASchB.AccMktDiscIntCopies) + GetNumber(IASchB.ContigentPayCopies)

def TPAccMktDiscInt_Calculation():
    ReturnVal = GetCurrency(IASchB.TotAccMktDiscInt) - GetCurrency(IASchB.SPAccMktDiscInt) - GetCurrency(IASchB.JtAccMktDiscInt)

def TPContigentPay_Calculation():
    ReturnVal = GetCurrency(IASchB.TotContigentPay) - GetCurrency(IASchB.SPContigentPay) - GetCurrency(IASchB.JtContigentPay)

