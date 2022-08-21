from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Desc_Calculation():
    ReturnVal = CStr(GetCurrency(IAWBPInt.TotalInterest)) + ' Additional Interest'

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
    ResSFM = GetNumber(IAWBBump.ResSFMNbr)
    OthSFM = GetNumber(IAWBBump.OthSFMNbr)
    OID = GetNumber(IAWBBump.OIDNbr)
    INT1099 = GetNumber(IAWBBump.INTNbr)
    PartK1 = GetNumber(IAWBBump.PartK1Nbr)
    SCorpK1 = GetNumber(IAWBBump.SCorpK1Nbr)
    EstK1 = GetNumber(IAWBBump.EstK1Nbr)
    TPAccMktDisc = GetBool(IASchB.TPAccMktDiscInt)
    MoStuff = Index + GetNumber(IAWBPInt.Offset)
    if GetNumber(IASchB.TotINTCopies) == 7:
        ReturnVal = 0
    elif ResSFM > MoStuff:
        ReturnVal = 0
    elif ResSFM + OthSFM > MoStuff:
        Stuff = ( MoStuff )  - ResSFM
        ReturnVal = 0
    elif ResSFM + OthSFM + OID > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM
        ReturnVal = Round(GetCurrency(USD1099OID.USInt, ( GetNumber(IAWBBump.OID(Stuff)) ))) + Round(GetCurrency(USD1099OID.StExempt, ( GetNumber(IAWBBump.OID(Stuff)) ))) + Round(GetCurrency(USD1099OID.Nominee, ( GetNumber(IAWBBump.OID(Stuff)) ))) + MaxValue(0, Round(GetCurrency(USD1099OID.BOIDAdjAmt, ( GetNumber(IAWBBump.OID(Stuff)) ))))
    elif ResSFM + OthSFM + OID + INT1099 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID
        ReturnVal = Round(GetCurrency(USD1099INT.USInt, ( GetNumber(IAWBBump.INT(Stuff)) ))) + Round(GetCurrency(USD1099INT.Nominee, ( GetNumber(IAWBBump.INT(Stuff)) ))) + Round(GetCurrency(USD1099INT.AccruedInt, ( GetNumber(IAWBBump.INT(Stuff)) ))) + Round(GetCurrency(USD1099INT.ABP, ( GetNumber(IAWBBump.INT(Stuff)) ))) + Round(GetCurrency(USD1099INT.StateExmpt, ( GetNumber(IAWBBump.INT(Stuff)) )))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099
        ReturnVal = GetCurrency(USDPartK1.NetStTEI, ( GetNumber(IAWBBump.PartK1(Stuff)) )) + GetCurrency(USDPartK1.FedStTEI, ( GetNumber(IAWBBump.PartK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1
        ReturnVal = GetCurrency(USDSCorpK1.NetStTEI, ( GetNumber(IAWBBump.SCorpK1(Stuff)) )) + GetCurrency(USDSCorpK1.FedStTEI, ( GetNumber(IAWBBump.SCorpK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1
        ReturnVal = GetCurrency(USDEstK1.NetStTEI, ( GetNumber(IAWBBump.EstK1(Stuff)) )) + GetCurrency(USDEstK1.FedStTEI, ( GetNumber(IAWBBump.EstK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1
        ReturnVal = 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc
        ReturnVal = 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt)
        ReturnVal = 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt)
        ReturnVal = 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay)
        ReturnVal = 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) + GetBool(IASchB.JtContigentPay) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay) - GetBool(IASchB.SPContigentPay)
        ReturnVal = 0
    else:
        ReturnVal = 0

def Exist_Calculation():
    ReturnVal = 1

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
    ResSFM = GetNumber(IAWBBump.ResSFMNbr)
    OthSFM = GetNumber(IAWBBump.OthSFMNbr)
    OID = GetNumber(IAWBBump.OIDNbr)
    INT1099 = GetNumber(IAWBBump.INTNbr)
    PartK1 = GetNumber(IAWBBump.PartK1Nbr)
    SCorpK1 = GetNumber(IAWBBump.SCorpK1Nbr)
    EstK1 = GetNumber(IAWBBump.EstK1Nbr)
    TPAccMktDisc = GetBool(IASchB.TPAccMktDiscInt)
    MoStuff = Index + GetNumber(IAWBPInt.Offset)
    if GetNumber(IASchB.TotINTCopies) == 7:
        ReturnVal = 0
    elif ResSFM > MoStuff:
        ReturnVal = GetBool(USDSFM.Joint, GetNumber(IAWBBump.ResSFM(MoStuff)))
    elif ResSFM + OthSFM > MoStuff:
        Stuff = ( MoStuff )  - ResSFM
        ReturnVal = GetBool(USDSFM.Joint, ( GetNumber(IAWBBump.OthSFM(Stuff)) ))
    elif ResSFM + OthSFM + OID > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM
        ReturnVal = GetBool(USD1099OID.Joint, ( GetNumber(IAWBBump.OID(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID
        ReturnVal = GetBool(USD1099INT.Joint, ( GetNumber(IAWBBump.Int(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099
        ReturnVal = GetBool(USDPartK1.Joint, ( GetNumber(IAWBBump.PartK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1
        ReturnVal = GetBool(USDSCorpK1.Joint, ( GetNumber(IAWBBump.SCorpK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1
        ReturnVal = GetBool(USDEstK1.Joint, ( GetNumber(IAWBBump.EstK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1
        ReturnVal = 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc
        ReturnVal = 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt)
        ReturnVal = 1
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt)
        ReturnVal = 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay)
        ReturnVal = 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) + GetBool(IASchB.JtContigentPay) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay) - GetBool(IASchB.SPContigentPay)
        ReturnVal = 1
    else:
        ReturnVal = 0

def IntAcctOwner_Calculation(Index):
    if GetBool(IAWBPInt.ITp1(Index)) == True:
        ReturnVal = 'Taxpayer'
    elif GetBool(IAWBPInt.ISp1(Index)) == True:
        ReturnVal = 'Spouse'
    elif GetBool(IAWBPInt.IJ1(Index)) == True:
        ReturnVal = 'Joint'
    else:
        ReturnVal = ''

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
    ResSFM = GetNumber(IAWBBump.ResSFMNbr)
    OthSFM = GetNumber(IAWBBump.OthSFMNbr)
    OID = GetNumber(IAWBBump.OIDNbr)
    INT1099 = GetNumber(IAWBBump.INTNbr)
    PartK1 = GetNumber(IAWBBump.PartK1Nbr)
    SCorpK1 = GetNumber(IAWBBump.SCorpK1Nbr)
    EstK1 = GetNumber(IAWBBump.EstK1Nbr)
    TPAccMktDisc = GetBool(IASchB.TPAccMktDiscInt)
    MoStuff = Index + GetNumber(IAWBPInt.Offset)
    if GetNumber(IASchB.TotINTCopies) == 7:
        ReturnVal = 0
    elif ResSFM > MoStuff:
        ReturnVal = Round(GetCurrency(USDSFM.Interest, GetNumber(IAWBBump.ResSFM(MoStuff))))
    elif ResSFM + OthSFM > MoStuff:
        Stuff = ( MoStuff )  - ResSFM
        ReturnVal = Round(GetCurrency(USDSFM.Interest, ( GetNumber(IAWBBump.OthSFM(Stuff)) )))
    elif ResSFM + OthSFM + OID > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM
        ReturnVal = GetCurrency(USD1099OID.BAmt, ( GetNumber(IAWBBump.OID(Stuff)) )) + Round(GetCurrency(USD1099OID.TaxExempt, ( GetNumber(IAWBBump.OID(Stuff)) ))) - MinValue(0, Round(GetCurrency(USD1099OID.BOIDAdjAmt, ( GetNumber(IAWBBump.OID(Stuff)) ))))
    elif ResSFM + OthSFM + OID + INT1099 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID
        ReturnVal = GetCurrency(USD1099INT.BAmtEF, ( GetNumber(IAWBBump.INT(Stuff)) )) + GetCurrency(USD1099INT.FedExmpt, ( GetNumber(IAWBBump.INT(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099
        ReturnVal = GetCurrency(USDPartK1.HaveInt, ( GetNumber(IAWBBump.PartK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1
        ReturnVal = GetCurrency(USDSCorpK1.HaveInt, ( GetNumber(IAWBBump.SCorpK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1
        ReturnVal = GetCurrency(USDEstK1.HaveInt, ( GetNumber(IAWBBump.EstK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1
        ReturnVal = GetCurrency(IASchB.TPAccMktDiscInt)
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc
        ReturnVal = GetCurrency(IASchB.SPAccMktDiscInt)
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt)
        ReturnVal = GetCurrency(IASchB.JtAccMktDiscInt)
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt)
        ReturnVal = GetCurrency(IASchB.TPContigentPay)
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay)
        ReturnVal = GetCurrency(IASchB.SPContigentPay)
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) + GetBool(IASchB.JtContigentPay) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay) - GetBool(IASchB.SPContigentPay)
        ReturnVal = GetCurrency(IASchB.JtContigentPay)
    else:
        ReturnVal = 0

def IntNoPayer_Calculation():
    count = Variant()

    Iter = Integer()
    count = 0
    Iter = 0
    while Iter < 22:
        if GetCurrency(IAWBPInt.Interest(Iter)) > 0 and Trim(GetString(IAWBPInt.Payer(Iter))) == '':
            count = count + 1
        Iter = Iter + 1
    if GetBool(IAWBPInt.Print) == True and count > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

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
    ResSFM = GetNumber(IAWBBump.ResSFMNbr)
    OthSFM = GetNumber(IAWBBump.OthSFMNbr)
    OID = GetNumber(IAWBBump.OIDNbr)
    INT1099 = GetNumber(IAWBBump.INTNbr)
    PartK1 = GetNumber(IAWBBump.PartK1Nbr)
    SCorpK1 = GetNumber(IAWBBump.SCorpK1Nbr)
    EstK1 = GetNumber(IAWBBump.EstK1Nbr)
    TPAccMktDisc = GetBool(IASchB.TPAccMktDiscInt)
    MoStuff = Index + GetNumber(IAWBPInt.Offset)
    if GetNumber(IASchB.TotINTCopies) == 7:
        ReturnVal = 0
    elif ResSFM > MoStuff:
        ReturnVal = GetBool(USDSFM.Spouse, GetNumber(IAWBBump.ResSFM(MoStuff)))
    elif ResSFM + OthSFM > MoStuff:
        Stuff = ( MoStuff )  - ResSFM
        ReturnVal = GetBool(USDSFM.Spouse, ( GetNumber(IAWBBump.OthSFM(Stuff)) ))
    elif ResSFM + OthSFM + OID > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM
        ReturnVal = GetBool(USD1099OID.Spouse, ( GetNumber(IAWBBump.OID(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID
        ReturnVal = GetBool(USD1099INT.Spouse, ( GetNumber(IAWBBump.Int(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099
        ReturnVal = GetBool(USDPartK1.Spouse, ( GetNumber(IAWBBump.PartK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1
        ReturnVal = GetBool(USDSCorpK1.Spouse, ( GetNumber(IAWBBump.SCorpK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1
        ReturnVal = GetBool(USDEstK1.Spouse, ( GetNumber(IAWBBump.EstK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1
        ReturnVal = 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc
        ReturnVal = 1
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt)
        ReturnVal = 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt)
        ReturnVal = 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay)
        ReturnVal = 1
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) + GetBool(IASchB.JtContigentPay) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay) - GetBool(IASchB.SPContigentPay)
        ReturnVal = 0
    else:
        ReturnVal = 0

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
    ResSFM = GetNumber(IAWBBump.ResSFMNbr)
    OthSFM = GetNumber(IAWBBump.OthSFMNbr)
    OID = GetNumber(IAWBBump.OIDNbr)
    INT1099 = GetNumber(IAWBBump.INTNbr)
    PartK1 = GetNumber(IAWBBump.PartK1Nbr)
    SCorpK1 = GetNumber(IAWBBump.SCorpK1Nbr)
    EstK1 = GetNumber(IAWBBump.EstK1Nbr)
    TPAccMktDisc = GetBool(IASchB.TPAccMktDiscInt)
    MoStuff = Index + GetNumber(IAWBPInt.Offset)
    if GetNumber(IASchB.TotINTCopies) == 7:
        ReturnVal = 0
    elif ResSFM > MoStuff:
        ReturnVal = GetBool(USDSFM.Taxpayer, GetNumber(IAWBBump.ResSFM(MoStuff)))
    elif ResSFM + OthSFM > MoStuff:
        Stuff = ( MoStuff )  - ResSFM
        ReturnVal = GetBool(USDSFM.Taxpayer, ( GetNumber(IAWBBump.OthSFM(Stuff)) ))
    elif ResSFM + OthSFM + OID > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM
        ReturnVal = GetBool(USD1099OID.Taxpayer, ( GetNumber(IAWBBump.OID(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID
        ReturnVal = GetBool(USD1099INT.Taxpayer, ( GetNumber(IAWBBump.Int(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099
        ReturnVal = GetBool(USDPartK1.Taxpayer, ( GetNumber(IAWBBump.PartK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1
        ReturnVal = GetBool(USDSCorpK1.Taxpayer, ( GetNumber(IAWBBump.SCorpK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1
        ReturnVal = GetBool(USDEstK1.Taxpayer, ( GetNumber(IAWBBump.EstK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1
        ReturnVal = 1
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc
        ReturnVal = 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt)
        ReturnVal = 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt)
        ReturnVal = 1
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay)
        ReturnVal = 0
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) + GetBool(IASchB.JtContigentPay) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay) - GetBool(IASchB.SPContigentPay)
        ReturnVal = 0
    else:
        ReturnVal = 0

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
    elif GetCopy() == 11:
        ReturnVal = 226
    else:
        ReturnVal = 248

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
    ResSFM = GetNumber(IAWBBump.ResSFMNbr)
    OthSFM = GetNumber(IAWBBump.OthSFMNbr)
    OID = GetNumber(IAWBBump.OIDNbr)
    INT1099 = GetNumber(IAWBBump.INTNbr)
    PartK1 = GetNumber(IAWBBump.PartK1Nbr)
    SCorpK1 = GetNumber(IAWBBump.SCorpK1Nbr)
    EstK1 = GetNumber(IAWBBump.EstK1Nbr)
    TPAccMktDisc = GetBool(IASchB.TPAccMktDiscInt)
    MoStuff = Index + GetNumber(IAWBPInt.Offset)
    if GetNumber(IASchB.TotINTCopies) == 7:
        ReturnVal = ''
    elif ResSFM > MoStuff:
        ReturnVal = GetString(USDSFM.NameAdd, GetNumber(IAWBBump.ResSFM(MoStuff)))
    elif ResSFM + OthSFM > MoStuff:
        Stuff = ( MoStuff )  - ResSFM
        ReturnVal = GetString(USDSFM.PayerName, ( GetNumber(IAWBBump.OthSFM(Stuff)) ))
    elif ResSFM + OthSFM + OID > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM
        ReturnVal = GetString(USD1099OID.PayerName, ( GetNumber(IAWBBump.OID(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID
        ReturnVal = GetString(USD1099INT.PayerName, ( GetNumber(IAWBBump.INT(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099
        ReturnVal = GetString(USDPartK1.CoName, ( GetNumber(IAWBBump.PartK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1
        ReturnVal = GetString(USDSCorpK1.CoName, ( GetNumber(IAWBBump.SCorpK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1
        ReturnVal = GetString(USDEstK1.TrustName, ( GetNumber(IAWBBump.EstK1(Stuff)) ))
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1
        ReturnVal = 'Accrued Market Discount'
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc
        ReturnVal = 'Accrued Market Discount'
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt)
        ReturnVal = 'Accrued Market Discount'
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt)
        ReturnVal = 'Contingent Payment Debt Instrument'
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay)
        ReturnVal = 'Contingent Payment Debt Instrument'
    elif ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) + GetBool(IASchB.JtContigentPay) > MoStuff:
        Stuff = ( MoStuff )  - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay) - GetBool(IASchB.SPContigentPay)
        ReturnVal = 'Contingent Payment Debt Instrument'
    else:
        ReturnVal = ''

def Print_Calculation():
    if GetNumber(IASchB.PrintIAB) == 1 and GetCurrency(IAWBPInt.TotalInterest) != 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

def TaxInt_Calculation(Index):
    ReturnVal = MaxValue(0, GetCurrency(IAWBPInt.Interest(Index)) - GetCurrency(IAWBPInt.ExemptInt(Index)))

def TotalExemptInt_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 22:
        SubTot = SubTot + GetCurrency(IAWBPInt.ExemptInt(count))
        count = count + 1
    ReturnVal = SubTot

def TotalInterest_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 22:
        SubTot = SubTot + GetCurrency(IAWBPInt.Interest(count))
        count = count + 1
    ReturnVal = SubTot

def TotalTaxInt_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 22:
        SubTot = SubTot + GetCurrency(IAWBPInt.TaxInt(count))
        count = count + 1
    ReturnVal = SubTot

