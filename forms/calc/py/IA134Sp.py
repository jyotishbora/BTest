from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Alert10_Calculation():
    if GetNumber(IA134Sp.Print) > 0:
        if Trim(GetString(IA134Sp.SCorpName)) == '':
            ReturnVal = 1
        elif GetString(IA134Sp.SCorpEIN) == '':
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def Alert20_Calculation():
    if GetNumber(IA134Sp.Print) > 0:
        if GetCurrency(IA134Sp.StateAdj) != 0 and Trim(GetString(IA134Sp.StateAdjExpl)) == '':
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def Alert30_Calculation():
    if GetNumber(IA134Sp.Print) > 0:
        if GetCurrency(IA134Sp.FedRegTax) == 0:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def BiggerInc_Calculation():
    ReturnVal = MaxValue(GetCurrency(IA134Sp.IASourceInc), GetCurrency(IA134Sp.NetDist))

def Credit_Calculation():
    ReturnVal = CDollar(( ( ( Round(GetFloat(IA134Sp.CreditPercent) * 100) )  / 100 )  * GetFloat(IA134Sp.NetTax) )  / 100)

def CreditPercent_Calculation():
    if GetFloat(IA134Sp.BusRatio) > 0:
        ReturnVal = MaxValue(0, 100 - GetFloat(IA134Sp.TaxPercent))
    else:
        ReturnVal = 0

def Description_Calculation():
    Total = Currency()
    Total = GetCurrency(IA134Sp.Credit)
    ReturnVal = CStr(Total) + ' Credit'

def Dividends_Calculation():
    ReturnVal = GetCurrency(USDSCorpK1.Dividends, ParentCopy()) -  ( CDollar(GetFloat(USDSCorpK1.Dividends, ParentCopy()) * GetFloat(IA134Sp.TPRatio)) )

def Exist_Calculation():
    ReturnVal = 1

def FedAGI_Calculation():
    if GetFloat(IA134Sp.BusRatio) > 0:
        if GetBool(IAF1040.CombMFS) == True:
            ReturnVal = GetCurrency(USWRec.SAGI)
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def FedTax_Calculation():
    ReturnVal = GetCurrency(IA134Sp.K1FedTax)

def IAApportion_Calculation():
    ReturnVal = CDollar(( ( ( Round(GetFloat(IA134Sp.IABusRatio) * 100) )  / 100 )  * GetFloat(IA134Sp.NetIAInc) )  / 100)

def IABusRatio_Calculation():
    ReturnVal = GetFloat(IA134Sp.BusRatio) * 100

def IAInc_Calculation():
    if GetFloat(IA134Sp.BusRatio) > 0:
        if GetBool(IAF1040.CombMFS) == True:
            ReturnVal = GetCurrency(IAF1040.BNet) + GetCurrency(IAOthAdj.SIANOL)
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def IASCorpInc_Calculation():
    if GetFloat(IA134Sp.BusRatio) > 0:
        ReturnVal = GetCurrency(IA134Sp.K1Inc) + GetCurrency(IA134Sp.StateAdj)
    else:
        ReturnVal = 0

def IASourceInc_Calculation():
    if GetFloat(IA134Sp.BusRatio) > 0:
        ReturnVal = GetCurrency(IA134Sp.IAApportion) + GetCurrency(IA134Sp.IANonBusInc)
    else:
        ReturnVal = 0

def Interest_Calculation():
    ReturnVal = GetCurrency(USDSCorpK1.Interest, ParentCopy()) -  ( CDollar(GetFloat(USDSCorpK1.Interest, ParentCopy()) * GetFloat(IA134Sp.TPRatio)) )

def IntSCorp_Calculation():
    if Trim(GetString(IA134Sp.SCorpName)) != '':
        ReturnVal = GetString(IA134Sp.SCorpName)
    else:
        ReturnVal = 'this S corporation'

def K1FedTax_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA134Sp.K1Tax) - GetCurrency(IA134Sp.K1FedCredits))

def K1Inc_Calculation():
    ReturnVal = GetCurrency(IA134Sp.TotInc) - GetCurrency(IA134Sp.TotDed)

def K1Inc2_Calculation():
    ReturnVal = GetCurrency(IA134Sp.K1Inc)

def K1IncPercent_Calculation():
    ReturnVal = GetFloat(IA134Sp.K1IncRatio) * 100

def K1IncRatio_Calculation():
    TopLim = Double()
    if GetFloat(IA134Sp.BusRatio) == 0:
        ReturnVal = 0
    elif GetFloat(IA134Sp.FedAGI) <= 0:
        ReturnVal = 1
    else:
        TopLim = MinValue(1, Round(GetFloat(IA134Sp.K1Inc2) / GetFloat(IA134Sp.FedAGI), 6))
        ReturnVal = MaxValue(0, TopLim)

def K1Tax_Calculation():
    ReturnVal = Round(CDollar(GetFloat(IA134Sp.NetFedTax) *  ( GetFloat(IA134Sp.K1IncPercent) / 100 )))

def LtGain_Calculation():
    ReturnVal = GetCurrency(USDSCorpK1.LtGain, ParentCopy()) -  ( CDollar(GetFloat(USDSCorpK1.LtGain, ParentCopy()) * GetFloat(IA134Sp.TPRatio)) )

def Names_Calculation():
    ReturnVal = GetString(IARequired.SPCombName)

def NetDist_Calculation():
    if GetFloat(IA134Sp.BusRatio) > 0:
        ReturnVal = MaxValue(0, GetCurrency(IA134Sp.Distributions) - GetCurrency(IA134Sp.FedTax))
    else:
        ReturnVal = 0

def NetFedTax_Calculation():
    ReturnVal = GetCurrency(IA134Sp.FedRegTax) + GetCurrency(IA134Sp.FedAMT)

def NetIAInc_Calculation():
    if GetFloat(IA134Sp.BusRatio) > 0:
        ReturnVal = GetCurrency(IA134Sp.IASCorpInc) - GetCurrency(IA134Sp.NonBusInc)
    else:
        ReturnVal = 0

def NetTax_Calculation():
    if GetFloat(IA134Sp.BusRatio) > 0:
        ReturnVal = GetCurrency(IAF1040.BTotIATax)
    else:
        ReturnVal = 0

def Numerator_Calculation():
    ReturnVal = GetCurrency(IA134Sp.BiggerInc) + GetCurrency(IA134Sp.Remainder)

def Ordinary_Calculation():
    ReturnVal = GetCurrency(USDSCorpK1.OrdAmt, ParentCopy()) -  ( CDollar(GetFloat(USDSCorpK1.OrdAmt, ParentCopy()) * GetFloat(IA134Sp.TPRatio)) )

def OthDed_Calculation():
    ReturnVal = GetCurrency(USDSCorpK1.SCOthDed, ParentCopy()) -  ( CDollar(GetFloat(USDSCorpK1.SCOthDed, ParentCopy()) * GetFloat(IA134Sp.TPRatio)) )

def OtherInc_Calculation():
    PortInc = Currency()

    Sec1256 = Currency()

    MineCost = Currency()

    OthInc = Currency()
    PortInc = GetCurrency(USDSCorpK1.PortInc, ParentCopy()) -  ( CDollar(GetFloat(USDSCorpK1.PortInc, ParentCopy()) * GetFloat(IA134Sp.TPRatio)) )
    Sec1256 = GetCurrency(USDSCorpK1.Sec1256, ParentCopy()) -  ( CDollar(GetFloat(USDSCorpK1.Sec1256, ParentCopy()) * GetFloat(IA134Sp.TPRatio)) )
    MineCost = GetCurrency(USDSCorpK1.MineCost, ParentCopy()) -  ( CDollar(GetFloat(USDSCorpK1.MineCost, ParentCopy()) * GetFloat(IA134Sp.TPRatio)) )
    OthInc = GetCurrency(USDSCorpK1.OthInc, ParentCopy()) -  ( CDollar(GetFloat(USDSCorpK1.OthInc, ParentCopy()) * GetFloat(IA134Sp.TPRatio)) )
    ReturnVal = PortInc + Sec1256 + MineCost + OthInc

def Print_Calculation():
    if GetBool(IAF1040.CombMFS) == False:
        ReturnVal = 0
    elif GetCurrency(IA134Sp.Credit) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def RealEstate_Calculation():
    ReturnVal = GetCurrency(USDSCorpK1.RentAmt, ParentCopy()) -  ( CDollar(GetFloat(USDSCorpK1.RentAmt, ParentCopy()) * GetFloat(IA134Sp.TPRatio)) )

def Remainder_Calculation():
    ReturnVal = GetCurrency(IA134Sp.IAInc) - GetCurrency(IA134Sp.IASCorpInc)

def Rental_Calculation():
    ReturnVal = GetCurrency(USDSCorpK1.Rental, ParentCopy()) -  ( CDollar(GetFloat(USDSCorpK1.Rental, ParentCopy()) * GetFloat(IA134Sp.TPRatio)) )

def Royalties_Calculation():
    ReturnVal = GetCurrency(USDSCorpK1.Royalties, ParentCopy()) -  ( CDollar(GetFloat(USDSCorpK1.Royalties, ParentCopy()) * GetFloat(IA134Sp.TPRatio)) )

def SCorpEIN_Calculation():
    ReturnVal = GetString(USDSCorpK1.EIN, ParentCopy())

def SCorpName_Calculation():
    ReturnVal = GetString(USDSCorpK1.CoName, ParentCopy())

def Sec1231_Calculation():
    ReturnVal = GetCurrency(USDSCorpK1.Sec1231, ParentCopy()) -  ( CDollar(GetFloat(USDSCorpK1.Sec1231, ParentCopy()) * GetFloat(IA134Sp.TPRatio)) )

def Sec179_Calculation():
    ReturnVal = GetCurrency(USDSCorpK1.Sec179, ParentCopy()) -  ( CDollar(GetFloat(USDSCorpK1.Sec179, ParentCopy()) * GetFloat(IA134Sp.TPRatio)) )

def SPApplied_Calculation():
    count = Integer()

    count2 = Integer()
    count = 0
    while count <= 9:
        if GetString(IA148Sp.NonRefCode(count)) == '11' and GetCurrency(IA148Sp.CYCredit(count)) == GetCurrency(IA134Sp.Credit):
            ReturnVal = GetCurrency(IA148Sp.ArrayNonRefCr(count))
        count = count + 1
    count2 = 0
    while count <= 28:
        if GetString(IAWBP148Sp.NonRefCode(count2)) == '11' and GetCurrency(IAWBP148Sp.CYCredit(count2)) == GetCurrency(IA134Sp.Credit):
            ReturnVal = GetCurrency(IAWBP148Sp.ArrayNonRefCr(count2))
        count = count + 1
    ReturnVal = 0

def SPExpired_Calculation():
    count = Integer()

    count2 = Integer()
    count = 0
    while count <= 9:
        if GetString(IA148Sp.NonRefCode(count)) == '11' and GetCurrency(IA148Sp.CYCredit(count)) == GetCurrency(IA134Sp.Credit):
            ReturnVal = GetCurrency(IA148Sp.ExpCr(count))
        count = count + 1
    count2 = 0
    while count <= 28:
        if GetString(IAWBP148Sp.NonRefCode(count2)) == '11' and GetCurrency(IAWBP148Sp.CYCredit(count2)) == GetCurrency(IA134Sp.Credit):
            ReturnVal = GetCurrency(IAWBP148Sp.ExpCr(count2))
        count = count + 1
    ReturnVal = 0

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SpouseSSN)

def StGain_Calculation():
    ReturnVal = GetCurrency(USDSCorpK1.StGain, ParentCopy()) -  ( CDollar(GetFloat(USDSCorpK1.StGain, ParentCopy()) * GetFloat(IA134Sp.TPRatio)) )

def TaxPercent_Calculation():
    ReturnVal = GetFloat(IA134Sp.TaxRatio) * 100

def TaxRatio_Calculation():
    TopLim = Double()
    if GetFloat(IA134Sp.BusRatio) == 0:
        ReturnVal = 0
    elif GetFloat(IA134Sp.IAInc) == 0:
        ReturnVal = 1
    else:
        TopLim = MinValue(1, Round(GetFloat(IA134Sp.Numerator) / GetFloat(IA134Sp.IAInc), 6))
        ReturnVal = MaxValue(0, TopLim)

def TotDed_Calculation():
    if GetFloat(IA134Sp.BusRatio) > 0:
        ReturnVal = GetCurrency(IA134Sp.Sec179) + GetCurrency(IA134Sp.OthDed)
    else:
        ReturnVal = 0

def TotInc_Calculation():
    if GetFloat(IA134Sp.BusRatio) > 0:
        ReturnVal = GetCurrency(IA134Sp.Ordinary) + GetCurrency(IA134Sp.RealEstate) + GetCurrency(IA134Sp.Rental) + GetCurrency(IA134Sp.Interest) + GetCurrency(IA134Sp.Dividends) + GetCurrency(IA134Sp.Royalties) + GetCurrency(IA134Sp.StGain) + GetCurrency(IA134Sp.LtGain) + GetCurrency(IA134Sp.Sec1231) + GetCurrency(IA134Sp.OtherInc)
    else:
        ReturnVal = 0

def TPRatio_Calculation():
    if GetBool(IAF1040.CombMFS) == True and GetBool(USDSCorpK1.Joint, ParentCopy()) == True:
        ReturnVal = 0.5
    elif GetBool(IAF1040.CombMFS) == True and GetBool(USDSCorpK1.Spouse, ParentCopy()) == True:
        ReturnVal = 0
    else:
        ReturnVal = 1

