from forms.out import IAF1040
from forms.out import IAREQUIRED
from forms.out import IASCHB
from forms.out import IAWBBUMP
from forms.out import IAWBPDIV
from forms.out import IAWBPINT
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def AccMktDiscIntCopies_Calculation():
    TPAccMktDiscInt = Integer()

    SPAccMktDiscInt = Integer()

    JTAccMktDiscInt = Integer()
    if get_currency(IASCHB.TPAccMktDiscInt) > 0:
        TPAccMktDiscInt = 1
    else:
        TPAccMktDiscInt = 0
    if get_currency(IASCHB.SPAccMktDiscInt) > 0:
        SPAccMktDiscInt = 1
    else:
        SPAccMktDiscInt = 0
    if get_currency(IASCHB.JtAccMktDiscInt) > 0:
        JTAccMktDiscInt = 1
    else:
        JTAccMktDiscInt = 0
    return TPAccMktDiscInt + SPAccMktDiscInt + JTAccMktDiscInt

def ContigentPayCopies_Calculation():
    TPContigentPay = Integer()

    SPContigentPay = Integer()

    JTContigentPay = Integer()
    if get_currency(IASCHB.TPContigentPay) > 0:
        TPContigentPay = 1
    else:
        TPContigentPay = 0
    if get_currency(IASCHB.SPContigentPay) > 0:
        SPContigentPay = 1
    else:
        SPContigentPay = 0
    if get_currency(IASCHB.JtContigentPay) > 0:
        JTContigentPay = 1
    else:
        JTContigentPay = 0
    return TPContigentPay + SPContigentPay + JTContigentPay

def CrBP11_Calculation():
    if get_number(IASCHB.TotINTCopies) > 226:
        return 1
    else:
        return 0

def CrBP12_Calculation():
    if get_number(IASCHB.TotINTCopies) > 248:
        return 1
    else:
        return 0

def CrBP1_Calculation():
    if get_number(IASCHB.TotINTCopies) > 7:
        return 1
    else:
        return 0

def CrBP10_Calculation():
    if get_number(IASCHB.TotINTCopies) > 204:
        return 1
    else:
        return 0

def CrBP2_Calculation():
    if get_number(IASCHB.TotINTCopies) > 28:
        return 1
    else:
        return 0

def CrBP3_Calculation():
    if get_number(IASCHB.TotINTCopies) > 50:
        return 1
    else:
        return 0

def CrBP4_Calculation():
    if get_number(IASCHB.TotINTCopies) > 72:
        return 1
    else:
        return 0

def CrBP5_Calculation():
    if get_number(IASCHB.TotINTCopies) > 94:
        return 1
    else:
        return 0

def CrBP6_Calculation():
    if get_number(IASCHB.TotINTCopies) > 116:
        return 1
    else:
        return 0

def CrBP7_Calculation():
    if get_number(IASCHB.TotINTCopies) > 138:
        return 1
    else:
        return 0

def CrBP8_Calculation():
    if get_number(IASCHB.TotINTCopies) > 160:
        return 1
    else:
        return 0

def CrBP9_Calculation():
    if get_number(IASCHB.TotINTCopies) > 182:
        return 1
    else:
        return 0

def CrBPDiv10_Calculation():
    if get_number(IASCHB.TotDIVCopies) > 204:
        return 1
    else:
        return 0

def CrBPDiv11_Calculation():
    if get_number(IASCHB.TotDIVCopies) > 226:
        return 1
    else:
        return 0

def CrBPDiv1_Calculation():
    if get_number(IASCHB.TotDIVCopies) > 7:
        return 1
    else:
        return 0

def CrBPDiv2_Calculation():
    if get_number(IASCHB.TotDIVCopies) > 28:
        return 1
    else:
        return 0

def CrBPDiv3_Calculation():
    if get_number(IASCHB.TotDIVCopies) > 50:
        return 1
    else:
        return 0

def CrBPDiv4_Calculation():
    if get_number(IASCHB.TotDIVCopies) > 72:
        return 1
    else:
        return 0

def CrBPDiv5_Calculation():
    if get_number(IASCHB.TotDIVCopies) > 94:
        return 1
    else:
        return 0

def CrBPDiv6_Calculation():
    if get_number(IASCHB.TotDIVCopies) > 116:
        return 1
    else:
        return 0

def CrBPDiv7_Calculation():
    if get_number(IASCHB.TotDIVCopies) > 138:
        return 1
    else:
        return 0

def CrBPDiv8_Calculation():
    if get_number(IASCHB.TotDIVCopies) > 160:
        return 1
    else:
        return 0

def CrBPDiv9_Calculation():
    if get_number(IASCHB.TotDIVCopies) > 182:
        return 1
    else:
        return 0

def Desc_Calculation():
    return get_string(IAREQUIRED.CombNames)

def DivAcctOwner_Calculation(Index):
    if get_bool(IASCHB.DTp1(Index)) == True:
        return 'Taxpayer'
    elif get_bool(IASCHB.DSp1(Index)) == True:
        return 'Spouse'
    elif get_bool(IASCHB.DJ1(Index)) == True:
        return 'Joint'
    else:
        return ''

def Dividend_Calculation(Index):
    Stuff = Integer()

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
    if Index == 6 and get_number(IASCHB.TotDIVCopies) > 7:
        return get_currency(IAWBPDIV.TotalDividend)
    elif DIV > Index:
        return Round(get_currency(USD1099DIV.ORDDIV, get_number(IAWBBUMP.DIV(Index)))) + Round(get_currency(USD1099DIV.FedExmpt, get_number(IAWBBUMP.DIV(Index))))
    elif DIV + PartK1 > Index:
        Stuff = ( Index )  - DIV
        return get_currency(USDPartK1.Dividends, ( get_number(IAWBBUMP.PartK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 > Index:
        Stuff = ( Index )  - DIV - PartK1
        return get_currency(USDSCorpK1.Dividends, ( get_number(IAWBBUMP.SCorpK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1
        return get_currency(USDEstK1.Dividends, ( get_number(IAWBBUMP.EstK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1 - EstK1
        return get_currency(USW5471SchI.DivOrd, ( get_number(IAWBBUMP.F5471(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471
        return get_currency(USF8621.DivTo1040, ( get_number(IAWBBUMP.F8621(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 + F8814 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471 - F8621
        return get_currency(USF8814.L6XL7, ( get_number(IAWBBUMP.F8814(Stuff)) ))
    else:
        return 0

def DivPayer_Calculation(Index):
    Stuff = Integer()

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
    if Index == 6 and get_number(IASCHB.TotDIVCopies) > 7:
        return 'See Statement Attached'
    elif DIV > Index:
        return get_string(USD1099DIV.PayerName, get_number(IAWBBUMP.DIV(Index)))
    elif DIV + PartK1 > Index:
        Stuff = ( Index )  - DIV
        return get_string(USDPartK1.CoName, ( get_number(IAWBBUMP.PartK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 > Index:
        Stuff = ( Index )  - DIV - PartK1
        return get_string(USDSCorpK1.CoName, ( get_number(IAWBBUMP.SCorpK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1
        return get_string(USDEstK1.TrustName, ( get_number(IAWBBUMP.EstK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1 - EstK1
        return 'Form 5471'
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471
        return 'Form 8621 - ' + get_string(USF8621.CoName, ( get_number(IAWBBUMP.F8621(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 + F8814 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471 - F8621
        return 'Form 8814 - ' + get_string(USF8814.ChName, ( get_number(IAWBBUMP.F8814(Stuff)) ))
    else:
        return ''

def DJ1_Calculation(Index):
    Stuff = Integer()

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
    if Index == 6 and get_number(IASCHB.TotDIVCopies) > 7:
        return 0
    elif DIV > Index:
        return get_bool(USD1099DIV.Joint, get_number(IAWBBUMP.DIV(Index)))
    elif DIV + PartK1 > Index:
        Stuff = ( Index )  - DIV
        return get_bool(USDPartK1.Joint, ( get_number(IAWBBUMP.PartK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 > Index:
        Stuff = ( Index )  - DIV - PartK1
        return get_bool(USDSCorpK1.Joint, ( get_number(IAWBBUMP.SCorpK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1
        return get_bool(USDEstK1.Joint, ( get_number(IAWBBUMP.EstK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1 - EstK1
        return 0
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471
        return get_bool(USF8621.Joint, ( get_number(IAWBBUMP.F8621(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 + F8814 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471 - F8621
        if get_bool(USWBasicInfo.JointCalc) == True:
            return 1
        else:
            return 0
    else:
        return 0

def DSp1_Calculation(Index):
    Stuff = Integer()

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
    if Index == 6 and get_number(IASCHB.TotDIVCopies) > 7:
        return 0
    elif DIV > Index:
        return get_bool(USD1099DIV.Spouse, get_number(IAWBBUMP.DIV(Index)))
    elif DIV + PartK1 > Index:
        Stuff = ( Index )  - DIV
        return get_bool(USDPartK1.Spouse, ( get_number(IAWBBUMP.PartK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 > Index:
        Stuff = ( Index )  - DIV - PartK1
        return get_bool(USDSCorpK1.Spouse, ( get_number(IAWBBUMP.SCorpK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1
        return get_bool(USDEstK1.Spouse, ( get_number(IAWBBUMP.EstK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1 - EstK1
        if get_string(USW5471SchI.SchISSN, ( get_number(IAWBBUMP.F5471(Stuff)) )) == get_string(USWBasicInfo.SpouseSSN):
            return 1
        else:
            return 0
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471
        return get_bool(USF8621.Spouse, ( get_number(IAWBBUMP.F8621(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 + F8814 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471 - F8621
        return 0
    else:
        return 0

def DTp1_Calculation(Index):
    Stuff = Integer()

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
    if Index == 6 and get_number(IASCHB.TotDIVCopies) > 7:
        return 0
    elif DIV > Index:
        return get_bool(USD1099DIV.Taxpayer, get_number(IAWBBUMP.DIV(Index)))
    elif DIV + PartK1 > Index:
        Stuff = ( Index )  - DIV
        return get_bool(USDPartK1.Taxpayer, ( get_number(IAWBBUMP.PartK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 > Index:
        Stuff = ( Index )  - DIV - PartK1
        return get_bool(USDSCorpK1.Taxpayer, ( get_number(IAWBBUMP.SCorpK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1
        return get_bool(USDEstK1.Taxpayer, ( get_number(IAWBBUMP.EstK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1 - EstK1
        if get_string(USW5471SchI.SchISSN, ( get_number(IAWBBUMP.F5471(Stuff)) )) == get_string(USWBasicInfo.SSN):
            return 1
        else:
            return 0
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471
        return get_bool(USF8621.Taxpayer, ( get_number(IAWBBUMP.F8621(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 + F8814 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471 - F8621
        if get_bool(USWBasicInfo.JointCalc) == True:
            return 0
        else:
            return 1
    else:
        return 0

def ExemptDiv_Calculation(Index):
    Stuff = Integer()

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
    if Index == 6 and get_number(IASCHB.TotDIVCopies) > 7:
        return get_currency(IAWBPDIV.TotalExemptDiv)
    elif DIV > Index:
        return Round(get_currency(USD1099DIV.Nominee, get_number(IAWBBUMP.DIV(Index)))) + Round(get_currency(USD1099DIV.StExmpt, get_number(IAWBBUMP.DIV(Index)))) + Round(get_currency(USD1099DIV.FedStExmpt, get_number(IAWBBUMP.DIV(Index)))) + Round(get_currency(USD1099DIV.Restricted, get_number(IAWBBUMP.DIV(Index))))
    elif DIV + PartK1 > Index:
        Stuff = ( Index )  - DIV
        return get_currency(USDPartK1.NetStTED, ( get_number(IAWBBUMP.PartK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 > Index:
        Stuff = ( Index )  - DIV - PartK1
        return get_currency(USDSCorpK1.NetStTED, ( get_number(IAWBBUMP.SCorpK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1
        return get_currency(USDEstK1.NetStTED, ( get_number(IAWBBUMP.EstK1Div(Stuff)) ))
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1 - EstK1
        return 0
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471
        return 0
    elif DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 + F8814 > Index:
        Stuff = ( Index )  - DIV - PartK1 - SCorpK1 - EstK1 - F5471 - F8621
        return 0
    else:
        return 0

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
    ResSFM = get_number(IAWBBUMP.ResSFMNbr)
    OthSFM = get_number(IAWBBUMP.OthSFMNbr)
    OID = get_number(IAWBBUMP.OIDNbr)
    INT1099 = get_number(IAWBBUMP.INTNbr)
    PartK1 = get_number(IAWBBUMP.PartK1Nbr)
    SCorpK1 = get_number(IAWBBUMP.SCorpK1Nbr)
    EstK1 = get_number(IAWBBUMP.EstK1Nbr)
    TPAccMktDisc = get_bool(IASCHB.TPAccMktDiscInt)
    if Index == 6 and get_number(IASCHB.TotINTCopies) > 7:
        return get_currency(IAWBPINT.TotalExemptInt)
    elif ResSFM > Index:
        return 0
    elif ResSFM + OthSFM > Index:
        Stuff = ( Index )  - ResSFM
        return 0
    elif ResSFM + OthSFM + OID > Index:
        Stuff = ( Index )  - ResSFM - OthSFM
        return Round(get_currency(USD1099OID.USInt, ( get_number(IAWBBUMP.OID(Stuff)) ))) + Round(get_currency(USD1099OID.StExempt, ( get_number(IAWBBUMP.OID(Stuff)) ))) + Round(get_currency(USD1099OID.Nominee, ( get_number(IAWBBUMP.OID(Stuff)) ))) + max_value(0, Round(get_currency(USD1099OID.BOIDAdjAmt, ( get_number(IAWBBUMP.OID(Stuff)) ))))
    elif ResSFM + OthSFM + OID + INT1099 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID
        return Round(get_currency(USD1099INT.USInt, ( get_number(IAWBBUMP.INT(Stuff)) ))) + Round(get_currency(USD1099INT.Nominee, ( get_number(IAWBBUMP.INT(Stuff)) ))) + Round(get_currency(USD1099INT.AccruedInt, ( get_number(IAWBBUMP.INT(Stuff)) ))) + Round(get_currency(USD1099INT.ABP, ( get_number(IAWBBUMP.INT(Stuff)) ))) + Round(get_currency(USD1099INT.StateExmpt, ( get_number(IAWBBUMP.INT(Stuff)) )))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099
        return get_currency(USDPartK1.NetStTEI, ( get_number(IAWBBUMP.PartK1(Stuff)) )) + get_currency(USDPartK1.FedStTEI, ( get_number(IAWBBUMP.PartK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1
        return get_currency(USDSCorpK1.NetStTEI, ( get_number(IAWBBUMP.SCorpK1(Stuff)) )) + get_currency(USDSCorpK1.FedStTEI, ( get_number(IAWBBUMP.SCorpK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1
        return get_currency(USDEstK1.NetStTEI, ( get_number(IAWBBUMP.EstK1(Stuff)) )) + get_currency(USDEstK1.FedStTEI, ( get_number(IAWBBUMP.EstK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + get_bool(IASCHB.TPAccMktDiscInt) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1
        return 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - get_bool(IASCHB.TPAccMktDiscInt)
        return 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt)
        return 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) + get_bool(IASCHB.TPContigentPay) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt) - get_bool(IASCHB.JtAccMktDiscInt)
        return 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) + get_bool(IASCHB.TPContigentPay) + get_bool(IASCHB.SPContigentPay) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt) - get_bool(IASCHB.JtAccMktDiscInt) - get_bool(IASCHB.TPContigentPay)
        return 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) + get_bool(IASCHB.TPContigentPay) + get_bool(IASCHB.SPContigentPay) + get_bool(IASCHB.JtContigentPay) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt) - get_bool(IASCHB.JtAccMktDiscInt) - get_bool(IASCHB.TPContigentPay) - get_bool(IASCHB.SPContigentPay)
        return 0
    else:
        return 0

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
    ResSFM = get_number(IAWBBUMP.ResSFMNbr)
    OthSFM = get_number(IAWBBUMP.OthSFMNbr)
    OID = get_number(IAWBBUMP.OIDNbr)
    INT1099 = get_number(IAWBBUMP.INTNbr)
    PartK1 = get_number(IAWBBUMP.PartK1Nbr)
    SCorpK1 = get_number(IAWBBUMP.SCorpK1Nbr)
    EstK1 = get_number(IAWBBUMP.EstK1Nbr)
    TPAccMktDisc = get_bool(IASCHB.TPAccMktDiscInt)
    if Index == 6 and get_number(IASCHB.TotINTCopies) > 7:
        return 0
    elif ResSFM > Index:
        return get_bool(USDSFM.Joint, get_number(IAWBBUMP.ResSFM(Index)))
    elif ResSFM + OthSFM > Index:
        Stuff = ( Index )  - ResSFM
        return get_bool(USDSFM.Joint, ( get_number(IAWBBUMP.OthSFM(Stuff)) ))
    elif ResSFM + OthSFM + OID > Index:
        Stuff = ( Index )  - ResSFM - OthSFM
        return get_bool(USD1099OID.Joint, ( get_number(IAWBBUMP.OID(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID
        return get_bool(USD1099INT.Joint, ( get_number(IAWBBUMP.Int(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099
        return get_bool(USDPartK1.Joint, ( get_number(IAWBBUMP.PartK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1
        return get_bool(USDSCorpK1.Joint, ( get_number(IAWBBUMP.SCorpK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1
        return get_bool(USDEstK1.Joint, ( get_number(IAWBBUMP.EstK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1
        return 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc
        return 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt)
        return 1
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) + get_bool(IASCHB.TPContigentPay) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt) - get_bool(IASCHB.JtAccMktDiscInt)
        return 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) + get_bool(IASCHB.TPContigentPay) + get_bool(IASCHB.SPContigentPay) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt) - get_bool(IASCHB.JtAccMktDiscInt) - get_bool(IASCHB.TPContigentPay)
        return 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) + get_bool(IASCHB.TPContigentPay) + get_bool(IASCHB.SPContigentPay) + get_bool(IASCHB.JtContigentPay) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt) - get_bool(IASCHB.JtAccMktDiscInt) - get_bool(IASCHB.TPContigentPay) - get_bool(IASCHB.SPContigentPay)
        return 1
    else:
        return 0

def IntAcctOwner_Calculation(Index):
    if get_bool(IASCHB.ITp1(Index)) == True:
        return 'Taxpayer'
    elif get_bool(IASCHB.ISp1(Index)) == True:
        return 'Spouse'
    elif get_bool(IASCHB.IJ1(Index)) == True:
        return 'Joint'
    else:
        return ''

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
    ResSFM = get_number(IAWBBUMP.ResSFMNbr)
    OthSFM = get_number(IAWBBUMP.OthSFMNbr)
    OID = get_number(IAWBBUMP.OIDNbr)
    INT1099 = get_number(IAWBBUMP.INTNbr)
    PartK1 = get_number(IAWBBUMP.PartK1Nbr)
    SCorpK1 = get_number(IAWBBUMP.SCorpK1Nbr)
    EstK1 = get_number(IAWBBUMP.EstK1Nbr)
    TPAccMktDisc = get_bool(IASCHB.TPAccMktDiscInt)
    if Index == 6 and get_number(IASCHB.TotINTCopies) > 7:
        return get_currency(IAWBPINT.TotalInterest)
    elif ResSFM > Index:
        return Round(get_currency(USDSFM.Interest, get_number(IAWBBUMP.ResSFM(Index))))
    elif ResSFM + OthSFM > Index:
        Stuff = ( Index )  - ResSFM
        return Round(get_currency(USDSFM.Interest, ( get_number(IAWBBUMP.OthSFM(Stuff)) )))
    elif ResSFM + OthSFM + OID > Index:
        Stuff = ( Index )  - ResSFM - OthSFM
        return get_currency(USD1099OID.BAmt, ( get_number(IAWBBUMP.OID(Stuff)) )) + Round(get_currency(USD1099OID.TaxExempt, ( get_number(IAWBBUMP.OID(Stuff)) ))) - min_value(0, Round(get_currency(USD1099OID.BOIDAdjAmt, ( get_number(IAWBBUMP.OID(Stuff)) ))))
    elif ResSFM + OthSFM + OID + INT1099 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID
        return get_currency(USD1099INT.BAmtEF, ( get_number(IAWBBUMP.INT(Stuff)) )) + get_currency(USD1099INT.FedExmpt, ( get_number(IAWBBUMP.INT(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099
        return get_currency(USDPartK1.HaveInt, ( get_number(IAWBBUMP.PartK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1
        return get_currency(USDSCorpK1.HaveInt, ( get_number(IAWBBUMP.SCorpK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1
        return get_currency(USDEstK1.HaveInt, ( get_number(IAWBBUMP.EstK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1
        return get_currency(IASCHB.TPAccMktDiscInt)
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc
        return get_currency(IASCHB.SPAccMktDiscInt)
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt)
        return get_currency(IASCHB.JtAccMktDiscInt)
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) + get_bool(IASCHB.TPContigentPay) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt) - get_bool(IASCHB.JtAccMktDiscInt)
        return get_currency(IASCHB.TPContigentPay)
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) + get_bool(IASCHB.TPContigentPay) + get_bool(IASCHB.SPContigentPay) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt) - get_bool(IASCHB.JtAccMktDiscInt) - get_bool(IASCHB.TPContigentPay)
        return get_currency(IASCHB.SPContigentPay)
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) + get_bool(IASCHB.TPContigentPay) + get_bool(IASCHB.SPContigentPay) + get_bool(IASCHB.JtContigentPay) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt) - get_bool(IASCHB.JtAccMktDiscInt) - get_bool(IASCHB.TPContigentPay) - get_bool(IASCHB.SPContigentPay)
        return get_currency(IASCHB.JtContigentPay)
    else:
        return 0

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
    ResSFM = get_number(IAWBBUMP.ResSFMNbr)
    OthSFM = get_number(IAWBBUMP.OthSFMNbr)
    OID = get_number(IAWBBUMP.OIDNbr)
    INT1099 = get_number(IAWBBUMP.INTNbr)
    PartK1 = get_number(IAWBBUMP.PartK1Nbr)
    SCorpK1 = get_number(IAWBBUMP.SCorpK1Nbr)
    EstK1 = get_number(IAWBBUMP.EstK1Nbr)
    TPAccMktDisc = get_bool(IASCHB.TPAccMktDiscInt)
    if Index == 6 and get_number(IASCHB.TotINTCopies) > 7:
        return 0
    elif ResSFM > Index:
        return get_bool(USDSFM.Spouse, get_number(IAWBBUMP.ResSFM(Index)))
    elif ResSFM + OthSFM > Index:
        Stuff = ( Index )  - ResSFM
        return get_bool(USDSFM.Spouse, ( get_number(IAWBBUMP.OthSFM(Stuff)) ))
    elif ResSFM + OthSFM + OID > Index:
        Stuff = ( Index )  - ResSFM - OthSFM
        return get_bool(USD1099OID.Spouse, ( get_number(IAWBBUMP.OID(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID
        return get_bool(USD1099INT.Spouse, ( get_number(IAWBBUMP.Int(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099
        return get_bool(USDPartK1.Spouse, ( get_number(IAWBBUMP.PartK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1
        return get_bool(USDSCorpK1.Spouse, ( get_number(IAWBBUMP.SCorpK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1
        return get_bool(USDEstK1.Spouse, ( get_number(IAWBBUMP.EstK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1
        return 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc
        return 1
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt)
        return 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) + get_bool(IASCHB.TPContigentPay) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt) - get_bool(IASCHB.JtAccMktDiscInt)
        return 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) + get_bool(IASCHB.TPContigentPay) + get_bool(IASCHB.SPContigentPay) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt) - get_bool(IASCHB.JtAccMktDiscInt) - get_bool(IASCHB.TPContigentPay)
        return 1
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) + get_bool(IASCHB.TPContigentPay) + get_bool(IASCHB.SPContigentPay) + get_bool(IASCHB.JtContigentPay) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt) - get_bool(IASCHB.JtAccMktDiscInt) - get_bool(IASCHB.TPContigentPay) - get_bool(IASCHB.SPContigentPay)
        return 0
    else:
        return 0

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
    ResSFM = get_number(IAWBBUMP.ResSFMNbr)
    OthSFM = get_number(IAWBBUMP.OthSFMNbr)
    OID = get_number(IAWBBUMP.OIDNbr)
    INT1099 = get_number(IAWBBUMP.INTNbr)
    PartK1 = get_number(IAWBBUMP.PartK1Nbr)
    SCorpK1 = get_number(IAWBBUMP.SCorpK1Nbr)
    EstK1 = get_number(IAWBBUMP.EstK1Nbr)
    TPAccMktDisc = get_bool(IASCHB.TPAccMktDiscInt)
    if Index == 6 and get_number(IASCHB.TotINTCopies) > 7:
        return 0
    elif ResSFM > Index:
        return get_bool(USDSFM.Taxpayer, get_number(IAWBBUMP.ResSFM(Index)))
    elif ResSFM + OthSFM > Index:
        Stuff = ( Index )  - ResSFM
        return get_bool(USDSFM.Taxpayer, ( get_number(IAWBBUMP.OthSFM(Stuff)) ))
    elif ResSFM + OthSFM + OID > Index:
        Stuff = ( Index )  - ResSFM - OthSFM
        return get_bool(USD1099OID.Taxpayer, ( get_number(IAWBBUMP.OID(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID
        return get_bool(USD1099INT.Taxpayer, ( get_number(IAWBBUMP.Int(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099
        return get_bool(USDPartK1.Taxpayer, ( get_number(IAWBBUMP.PartK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1
        return get_bool(USDSCorpK1.Taxpayer, ( get_number(IAWBBUMP.SCorpK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1
        return get_bool(USDEstK1.Taxpayer, ( get_number(IAWBBUMP.EstK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1
        return 1
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc
        return 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt)
        return 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) + get_bool(IASCHB.TPContigentPay) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt) - get_bool(IASCHB.JtAccMktDiscInt)
        return 1
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) + get_bool(IASCHB.TPContigentPay) + get_bool(IASCHB.SPContigentPay) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt) - get_bool(IASCHB.JtAccMktDiscInt) - get_bool(IASCHB.TPContigentPay)
        return 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) + get_bool(IASCHB.TPContigentPay) + get_bool(IASCHB.SPContigentPay) + get_bool(IASCHB.JtContigentPay) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt) - get_bool(IASCHB.JtAccMktDiscInt) - get_bool(IASCHB.TPContigentPay) - get_bool(IASCHB.SPContigentPay)
        return 0
    else:
        return 0

def JtAccMktDiscInt_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Currency()
    Lim = GetAllCopies(USDCapGain)
    count = 1
    Total = 0
    while count <= Lim:
        if get_bool(USDCapGain.Joint, count) == True and get_currency(USDCapGain.IntIncome, count) > 0:
            Total = Total + get_currency(USDCapGain.IntIncome, count)
        else:
            Total = Total
        count = count + 1
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return Total
    else:
        return 0

def JtContigentPay_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Currency()
    Lim = GetAllCopies(USDCapGain)
    count = 1
    Total = 0
    while count <= Lim:
        if get_bool(USDCapGain.Joint, count) == True and get_bool(USDCapGain.Ordinary, count) == True:
            Total = Total + get_currency(USDCapGain.OrdGain, count) - get_currency(USDCapGain.OrdLoss, count)
        else:
            Total = Total
        count = count + 1
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return Total
    else:
        return 0

def Names_Calculation():
    return get_string(IAREQUIRED.CombNames)

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
    ResSFM = get_number(IAWBBUMP.ResSFMNbr)
    OthSFM = get_number(IAWBBUMP.OthSFMNbr)
    OID = get_number(IAWBBUMP.OIDNbr)
    INT1099 = get_number(IAWBBUMP.INTNbr)
    PartK1 = get_number(IAWBBUMP.PartK1Nbr)
    SCorpK1 = get_number(IAWBBUMP.SCorpK1Nbr)
    EstK1 = get_number(IAWBBUMP.EstK1Nbr)
    TPAccMktDisc = get_bool(IASCHB.TPAccMktDiscInt)
    if Index == 6 and get_number(IASCHB.TotINTCopies) > 7:
        return 'See Statement Attached'
    elif ResSFM > Index:
        return get_string(USDSFM.NameAdd, get_number(IAWBBUMP.ResSFM(Index)))
    elif ResSFM + OthSFM > Index:
        Stuff = ( Index )  - ResSFM
        return get_string(USDSFM.PayerName, ( get_number(IAWBBUMP.OthSFM(Stuff)) ))
    elif ResSFM + OthSFM + OID > Index:
        Stuff = ( Index )  - ResSFM - OthSFM
        return get_string(USD1099OID.PayerName, ( get_number(IAWBBUMP.OID(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID
        return get_string(USD1099INT.PayerName, ( get_number(IAWBBUMP.Int(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099
        return get_string(USDPartK1.CoName, ( get_number(IAWBBUMP.PartK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1
        return get_string(USDSCorpK1.CoName, ( get_number(IAWBBUMP.SCorpK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1
        return get_string(USDEstK1.TrustName, ( get_number(IAWBBUMP.EstK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1
        return 'Accrued Market Discount'
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc
        return 'Accrued Market Discount'
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt)
        return 'Accrued Market Discount'
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) + get_bool(IASCHB.TPContigentPay) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt) - get_bool(IASCHB.JtAccMktDiscInt)
        return 'Contingent Payment Debt Instrument'
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) + get_bool(IASCHB.TPContigentPay) + get_bool(IASCHB.SPContigentPay) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt) - get_bool(IASCHB.JtAccMktDiscInt) - get_bool(IASCHB.TPContigentPay)
        return 'Contingent Payment Debt Instrument'
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) + get_bool(IASCHB.TPContigentPay) + get_bool(IASCHB.SPContigentPay) + get_bool(IASCHB.JtContigentPay) > Index:
        Stuff = ( Index )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt) - get_bool(IASCHB.JtAccMktDiscInt) - get_bool(IASCHB.TPContigentPay) - get_bool(IASCHB.SPContigentPay)
        return 'Contingent Payment Debt Instrument'
    else:
        return ''

def PrintIAB_Calculation():
    if get_currency(IASCHB.TotalInterest) > Decimal("1500") or get_currency(IASCHB.TotalDividend) > Decimal("1500"):
        return 1
    else:
        return 0

def SPAccMktDiscInt_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Currency()
    Lim = GetAllCopies(USDCapGain)
    count = 1
    Total = 0
    while count <= Lim:
        if get_bool(USDCapGain.Spouse, count) == True and get_currency(USDCapGain.IntIncome, count) > 0:
            Total = Total + get_currency(USDCapGain.IntIncome, count)
        else:
            Total = Total
        count = count + 1
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return Total
    else:
        return 0

def SPContigentPay_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Currency()
    Lim = GetAllCopies(USDCapGain)
    count = 1
    Total = 0
    while count <= Lim:
        if get_bool(USDCapGain.Spouse, count) == True and get_bool(USDCapGain.Ordinary, count) == True:
            Total = Total + get_currency(USDCapGain.OrdGain, count) - get_currency(USDCapGain.OrdLoss, count)
        else:
            Total = Total
        count = count + 1
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return Total
    else:
        return 0

def SSN_Calculation():
    return get_string(IAF1040.SSN)

def TaxDiv_Calculation(Index):
    return max_value(0, get_currency(IASCHB.Dividend(Index)) - get_currency(IASCHB.ExemptDiv(Index)))

def TaxInt_Calculation(Index):
    return max_value(0, get_currency(IASCHB.Interest(Index)) - get_currency(IASCHB.ExemptInt(Index)))

def TotAccMktDiscInt_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Currency()
    Lim = GetAllCopies(USDCapGain)
    count = 1
    Total = 0
    while count <= Lim:
        if get_currency(USDCapGain.IntIncome, count) > 0:
            Total = Total + get_currency(USDCapGain.IntIncome, count)
        else:
            Total = Total
        count = count + 1
    return Round(Total)

def TotalDividend_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 7:
        SubTot = SubTot + get_currency(IASCHB.Dividend(count))
        count = count + 1
    return SubTot

def TotalExemptDiv_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 7:
        SubTot = SubTot + get_currency(IASCHB.ExemptDiv(count))
        count = count + 1
    return SubTot

def TotalExemptInt_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 7:
        SubTot = SubTot + get_currency(IASCHB.ExemptInt(count))
        count = count + 1
    return SubTot

def TotalInterest_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 7:
        SubTot = SubTot + get_currency(IASCHB.Interest(count))
        count = count + 1
    return SubTot

def TotalTaxDiv_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 7:
        SubTot = SubTot + get_currency(IASCHB.TaxDiv(count))
        count = count + 1
    return SubTot

def TotalTaxInt_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 7:
        SubTot = SubTot + get_currency(IASCHB.TaxInt(count))
        count = count + 1
    return SubTot

def TotContigentPay_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Currency()
    Lim = GetAllCopies(USDCapGain)
    count = 1
    Total = 0
    while count <= Lim:
        if get_bool(USDCapGain.Ordinary, count) == True:
            Total = Total + get_currency(USDCapGain.OrdGain, count) - get_currency(USDCapGain.OrdLoss, count)
        else:
            Total = Total
        count = count + 1
    return Round(Total)

def TotDIVCopies_Calculation():
    return get_number(IAWBBUMP.DIVNbr) + get_number(IAWBBUMP.PartK1DivNbr) + get_number(IAWBBUMP.SCorpK1DivNbr) + get_number(IAWBBUMP.EstK1DivNbr) + get_number(IAWBBUMP.F5471Nbr) + get_number(IAWBBUMP.F8621Nbr) + get_number(IAWBBUMP.F8814Nbr)

def TotINTCopies_Calculation():
    return get_number(IAWBBUMP.ResSFMNbr) + get_number(IAWBBUMP.OthSFMNbr) + get_number(IAWBBUMP.OIDNbr) + get_number(IAWBBUMP.INTNbr) + get_number(IAWBBUMP.PartK1Nbr) + get_number(IAWBBUMP.SCorpK1Nbr) + get_number(IAWBBUMP.EstK1Nbr) + get_number(IASCHB.AccMktDiscIntCopies) + get_number(IASCHB.ContigentPayCopies)

def TPAccMktDiscInt_Calculation():
    return get_currency(IASCHB.TotAccMktDiscInt) - get_currency(IASCHB.SPAccMktDiscInt) - get_currency(IASCHB.JtAccMktDiscInt)

def TPContigentPay_Calculation():
    return get_currency(IASCHB.TotContigentPay) - get_currency(IASCHB.SPContigentPay) - get_currency(IASCHB.JtContigentPay)


