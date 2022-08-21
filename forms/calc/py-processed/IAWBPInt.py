from forms.out import IAF1040
from forms.out import IAREQUIRED
from forms.out import IASCHB
from forms.out import IAWBBUMP
from forms.out import IAWBPINT
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Desc_Calculation():
    return CStr(get_currency(IAWBPINT.TotalInterest)) + ' Additional Interest'

def ExemptInt_Calculation(Index):
    Stuff = Integer()

    MoStuff = Integer()

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
    MoStuff = Index + get_number(IAWBPINT.Offset)
    if get_number(IASCHB.TotINTCopies) == 7:
        return 0
    elif ResSFM > MoStuff:
        return 0
    elif ResSFM + OthSFM > MoStuff:
        Stuff = ( MoStuff )  - ResSFM
        return 0
    elif ResSFM + OthSFM + OID > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM
        return Round(get_currency(USD1099OID.USInt, ( get_number(IAWBBUMP.OID(Stuff)) ))) + Round(get_currency(USD1099OID.StExempt, ( get_number(IAWBBUMP.OID(Stuff)) ))) + Round(get_currency(USD1099OID.Nominee, ( get_number(IAWBBUMP.OID(Stuff)) ))) + max_value(0, Round(get_currency(USD1099OID.BOIDAdjAmt, ( get_number(IAWBBUMP.OID(Stuff)) ))))
    elif ResSFM + OthSFM + OID + INT1099 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID
        return Round(get_currency(USD1099INT.USInt, ( get_number(IAWBBUMP.INT(Stuff)) ))) + Round(get_currency(USD1099INT.Nominee, ( get_number(IAWBBUMP.INT(Stuff)) ))) + Round(get_currency(USD1099INT.AccruedInt, ( get_number(IAWBBUMP.INT(Stuff)) ))) + Round(get_currency(USD1099INT.ABP, ( get_number(IAWBBUMP.INT(Stuff)) ))) + Round(get_currency(USD1099INT.StateExmpt, ( get_number(IAWBBUMP.INT(Stuff)) )))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099
        return get_currency(USDPartK1.NetStTEI, ( get_number(IAWBBUMP.PartK1(Stuff)) )) + get_currency(USDPartK1.FedStTEI, ( get_number(IAWBBUMP.PartK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1
        return get_currency(USDSCorpK1.NetStTEI, ( get_number(IAWBBUMP.SCorpK1(Stuff)) )) + get_currency(USDSCorpK1.FedStTEI, ( get_number(IAWBBUMP.SCorpK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1
        return get_currency(USDEstK1.NetStTEI, ( get_number(IAWBBUMP.EstK1(Stuff)) )) + get_currency(USDEstK1.FedStTEI, ( get_number(IAWBBUMP.EstK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1
        return 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc
        return 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt)
        return 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) + get_bool(IASCHB.TPContigentPay) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt) - get_bool(IASCHB.JtAccMktDiscInt)
        return 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) + get_bool(IASCHB.TPContigentPay) + get_bool(IASCHB.SPContigentPay) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt) - get_bool(IASCHB.JtAccMktDiscInt) - get_bool(IASCHB.TPContigentPay)
        return 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) + get_bool(IASCHB.TPContigentPay) + get_bool(IASCHB.SPContigentPay) + get_bool(IASCHB.JtContigentPay) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt) - get_bool(IASCHB.JtAccMktDiscInt) - get_bool(IASCHB.TPContigentPay) - get_bool(IASCHB.SPContigentPay)
        return 0
    else:
        return 0

def Exist_Calculation():
    return 1

def IJ1_Calculation(Index):
    Stuff = Integer()

    MoStuff = Integer()

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
    MoStuff = Index + get_number(IAWBPINT.Offset)
    if get_number(IASCHB.TotINTCopies) == 7:
        return 0
    elif ResSFM > MoStuff:
        return get_bool(USDSFM.Joint, get_number(IAWBBUMP.ResSFM(MoStuff)))
    elif ResSFM + OthSFM > MoStuff:
        Stuff = ( MoStuff )  - ResSFM
        return get_bool(USDSFM.Joint, ( get_number(IAWBBUMP.OthSFM(Stuff)) ))
    elif ResSFM + OthSFM + OID > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM
        return get_bool(USD1099OID.Joint, ( get_number(IAWBBUMP.OID(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID
        return get_bool(USD1099INT.Joint, ( get_number(IAWBBUMP.Int(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099
        return get_bool(USDPartK1.Joint, ( get_number(IAWBBUMP.PartK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1
        return get_bool(USDSCorpK1.Joint, ( get_number(IAWBBUMP.SCorpK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1
        return get_bool(USDEstK1.Joint, ( get_number(IAWBBUMP.EstK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1
        return 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc
        return 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt)
        return 1
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) + get_bool(IASCHB.TPContigentPay) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt) - get_bool(IASCHB.JtAccMktDiscInt)
        return 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) + get_bool(IASCHB.TPContigentPay) + get_bool(IASCHB.SPContigentPay) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt) - get_bool(IASCHB.JtAccMktDiscInt) - get_bool(IASCHB.TPContigentPay)
        return 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) + get_bool(IASCHB.TPContigentPay) + get_bool(IASCHB.SPContigentPay) + get_bool(IASCHB.JtContigentPay) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt) - get_bool(IASCHB.JtAccMktDiscInt) - get_bool(IASCHB.TPContigentPay) - get_bool(IASCHB.SPContigentPay)
        return 1
    else:
        return 0

def IntAcctOwner_Calculation(Index):
    if get_bool(IAWBPINT.ITp1(Index)) == True:
        return 'Taxpayer'
    elif get_bool(IAWBPINT.ISp1(Index)) == True:
        return 'Spouse'
    elif get_bool(IAWBPINT.IJ1(Index)) == True:
        return 'Joint'
    else:
        return ''

def Interest_Calculation(Index):
    Stuff = Integer()

    MoStuff = Integer()

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
    MoStuff = Index + get_number(IAWBPINT.Offset)
    if get_number(IASCHB.TotINTCopies) == 7:
        return 0
    elif ResSFM > MoStuff:
        return Round(get_currency(USDSFM.Interest, get_number(IAWBBUMP.ResSFM(MoStuff))))
    elif ResSFM + OthSFM > MoStuff:
        Stuff = ( MoStuff )  - ResSFM
        return Round(get_currency(USDSFM.Interest, ( get_number(IAWBBUMP.OthSFM(Stuff)) )))
    elif ResSFM + OthSFM + OID > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM
        return get_currency(USD1099OID.BAmt, ( get_number(IAWBBUMP.OID(Stuff)) )) + Round(get_currency(USD1099OID.TaxExempt, ( get_number(IAWBBUMP.OID(Stuff)) ))) - min_value(0, Round(get_currency(USD1099OID.BOIDAdjAmt, ( get_number(IAWBBUMP.OID(Stuff)) ))))
    elif ResSFM + OthSFM + OID + INT1099 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID
        return get_currency(USD1099INT.BAmtEF, ( get_number(IAWBBUMP.INT(Stuff)) )) + get_currency(USD1099INT.FedExmpt, ( get_number(IAWBBUMP.INT(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099
        return get_currency(USDPartK1.HaveInt, ( get_number(IAWBBUMP.PartK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1
        return get_currency(USDSCorpK1.HaveInt, ( get_number(IAWBBUMP.SCorpK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1
        return get_currency(USDEstK1.HaveInt, ( get_number(IAWBBUMP.EstK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1
        return get_currency(IASCHB.TPAccMktDiscInt)
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc
        return get_currency(IASCHB.SPAccMktDiscInt)
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt)
        return get_currency(IASCHB.JtAccMktDiscInt)
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) + get_bool(IASCHB.TPContigentPay) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt) - get_bool(IASCHB.JtAccMktDiscInt)
        return get_currency(IASCHB.TPContigentPay)
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) + get_bool(IASCHB.TPContigentPay) + get_bool(IASCHB.SPContigentPay) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt) - get_bool(IASCHB.JtAccMktDiscInt) - get_bool(IASCHB.TPContigentPay)
        return get_currency(IASCHB.SPContigentPay)
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) + get_bool(IASCHB.TPContigentPay) + get_bool(IASCHB.SPContigentPay) + get_bool(IASCHB.JtContigentPay) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt) - get_bool(IASCHB.JtAccMktDiscInt) - get_bool(IASCHB.TPContigentPay) - get_bool(IASCHB.SPContigentPay)
        return get_currency(IASCHB.JtContigentPay)
    else:
        return 0

def IntNoPayer_Calculation():
    count = Variant()

    Iter = Integer()
    count = 0
    Iter = 0
    while Iter < 22:
        if get_currency(IAWBPINT.Interest(Iter)) > 0 and trim(get_string(IAWBPINT.Payer(Iter))) == '':
            count = count + 1
        Iter = Iter + 1
    if get_bool(IAWBPINT.Print) == True and count > 0:
        return 1
    else:
        return 0

def ISp1_Calculation(Index):
    Stuff = Integer()

    MoStuff = Integer()

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
    MoStuff = Index + get_number(IAWBPINT.Offset)
    if get_number(IASCHB.TotINTCopies) == 7:
        return 0
    elif ResSFM > MoStuff:
        return get_bool(USDSFM.Spouse, get_number(IAWBBUMP.ResSFM(MoStuff)))
    elif ResSFM + OthSFM > MoStuff:
        Stuff = ( MoStuff )  - ResSFM
        return get_bool(USDSFM.Spouse, ( get_number(IAWBBUMP.OthSFM(Stuff)) ))
    elif ResSFM + OthSFM + OID > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM
        return get_bool(USD1099OID.Spouse, ( get_number(IAWBBUMP.OID(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID
        return get_bool(USD1099INT.Spouse, ( get_number(IAWBBUMP.Int(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099
        return get_bool(USDPartK1.Spouse, ( get_number(IAWBBUMP.PartK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1
        return get_bool(USDSCorpK1.Spouse, ( get_number(IAWBBUMP.SCorpK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1
        return get_bool(USDEstK1.Spouse, ( get_number(IAWBBUMP.EstK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1
        return 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc
        return 1
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt)
        return 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) + get_bool(IASCHB.TPContigentPay) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt) - get_bool(IASCHB.JtAccMktDiscInt)
        return 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) + get_bool(IASCHB.TPContigentPay) + get_bool(IASCHB.SPContigentPay) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt) - get_bool(IASCHB.JtAccMktDiscInt) - get_bool(IASCHB.TPContigentPay)
        return 1
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) + get_bool(IASCHB.TPContigentPay) + get_bool(IASCHB.SPContigentPay) + get_bool(IASCHB.JtContigentPay) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt) - get_bool(IASCHB.JtAccMktDiscInt) - get_bool(IASCHB.TPContigentPay) - get_bool(IASCHB.SPContigentPay)
        return 0
    else:
        return 0

def ITp1_Calculation(Index):
    Stuff = Integer()

    MoStuff = Integer()

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
    MoStuff = Index + get_number(IAWBPINT.Offset)
    if get_number(IASCHB.TotINTCopies) == 7:
        return 0
    elif ResSFM > MoStuff:
        return get_bool(USDSFM.Taxpayer, get_number(IAWBBUMP.ResSFM(MoStuff)))
    elif ResSFM + OthSFM > MoStuff:
        Stuff = ( MoStuff )  - ResSFM
        return get_bool(USDSFM.Taxpayer, ( get_number(IAWBBUMP.OthSFM(Stuff)) ))
    elif ResSFM + OthSFM + OID > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM
        return get_bool(USD1099OID.Taxpayer, ( get_number(IAWBBUMP.OID(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID
        return get_bool(USD1099INT.Taxpayer, ( get_number(IAWBBUMP.Int(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099
        return get_bool(USDPartK1.Taxpayer, ( get_number(IAWBBUMP.PartK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1
        return get_bool(USDSCorpK1.Taxpayer, ( get_number(IAWBBUMP.SCorpK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1
        return get_bool(USDEstK1.Taxpayer, ( get_number(IAWBBUMP.EstK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1
        return 1
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc
        return 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt)
        return 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) + get_bool(IASCHB.TPContigentPay) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt) - get_bool(IASCHB.JtAccMktDiscInt)
        return 1
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) + get_bool(IASCHB.TPContigentPay) + get_bool(IASCHB.SPContigentPay) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt) - get_bool(IASCHB.JtAccMktDiscInt) - get_bool(IASCHB.TPContigentPay)
        return 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) + get_bool(IASCHB.TPContigentPay) + get_bool(IASCHB.SPContigentPay) + get_bool(IASCHB.JtContigentPay) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt) - get_bool(IASCHB.JtAccMktDiscInt) - get_bool(IASCHB.TPContigentPay) - get_bool(IASCHB.SPContigentPay)
        return 0
    else:
        return 0

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
    elif GetCopy() == 11:
        return 226
    else:
        return 248

def Payer_Calculation(Index):
    Stuff = Integer()

    MoStuff = Integer()

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
    MoStuff = Index + get_number(IAWBPINT.Offset)
    if get_number(IASCHB.TotINTCopies) == 7:
        return ''
    elif ResSFM > MoStuff:
        return get_string(USDSFM.NameAdd, get_number(IAWBBUMP.ResSFM(MoStuff)))
    elif ResSFM + OthSFM > MoStuff:
        Stuff = ( MoStuff )  - ResSFM
        return get_string(USDSFM.PayerName, ( get_number(IAWBBUMP.OthSFM(Stuff)) ))
    elif ResSFM + OthSFM + OID > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM
        return get_string(USD1099OID.PayerName, ( get_number(IAWBBUMP.OID(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID
        return get_string(USD1099INT.PayerName, ( get_number(IAWBBUMP.INT(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099
        return get_string(USDPartK1.CoName, ( get_number(IAWBBUMP.PartK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1
        return get_string(USDSCorpK1.CoName, ( get_number(IAWBBUMP.SCorpK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1
        return get_string(USDEstK1.TrustName, ( get_number(IAWBBUMP.EstK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1
        return 'Accrued Market Discount'
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc
        return 'Accrued Market Discount'
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt)
        return 'Accrued Market Discount'
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) + get_bool(IASCHB.TPContigentPay) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt) - get_bool(IASCHB.JtAccMktDiscInt)
        return 'Contingent Payment Debt Instrument'
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) + get_bool(IASCHB.TPContigentPay) + get_bool(IASCHB.SPContigentPay) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt) - get_bool(IASCHB.JtAccMktDiscInt) - get_bool(IASCHB.TPContigentPay)
        return 'Contingent Payment Debt Instrument'
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + get_bool(IASCHB.SPAccMktDiscInt) + get_bool(IASCHB.JtAccMktDiscInt) + get_bool(IASCHB.TPContigentPay) + get_bool(IASCHB.SPContigentPay) + get_bool(IASCHB.JtContigentPay) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - get_bool(IASCHB.SPAccMktDiscInt) - get_bool(IASCHB.JtAccMktDiscInt) - get_bool(IASCHB.TPContigentPay) - get_bool(IASCHB.SPContigentPay)
        return 'Contingent Payment Debt Instrument'
    else:
        return ''

def Print_Calculation():
    if get_number(IASCHB.PrintIAB) == 1 and get_currency(IAWBPINT.TotalInterest) != 0:
        return 1
    else:
        return 0

def SSN_Calculation():
    return get_string(IAF1040.SSN)

def TaxInt_Calculation(Index):
    return max_value(0, get_currency(IAWBPINT.Interest(Index)) - get_currency(IAWBPINT.ExemptInt(Index)))

def TotalExemptInt_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 22:
        SubTot = SubTot + get_currency(IAWBPINT.ExemptInt(count))
        count = count + 1
    return SubTot

def TotalInterest_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 22:
        SubTot = SubTot + get_currency(IAWBPINT.Interest(count))
        count = count + 1
    return SubTot

def TotalTaxInt_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 22:
        SubTot = SubTot + get_currency(IAWBPINT.TaxInt(count))
        count = count + 1
    return SubTot


