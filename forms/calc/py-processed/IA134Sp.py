from forms.out import IA134SP
from forms.out import IA148SP
from forms.out import IAF1040
from forms.out import IAOTHADJ
from forms.out import IAREQUIRED
from forms.out import IAWBP148SP
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Alert10_Calculation():
    if get_number(IA134SP.Print) > 0:
        if trim(get_string(IA134SP.SCorpName)) == '':
            return 1
        elif get_string(IA134SP.SCorpEIN) == '':
            return 1
        else:
            return 0
    else:
        return 0

def Alert20_Calculation():
    if get_number(IA134SP.Print) > 0:
        if get_currency(IA134SP.StateAdj) != 0 and trim(get_string(IA134SP.StateAdjExpl)) == '':
            return 1
        else:
            return 0
    else:
        return 0

def Alert30_Calculation():
    if get_number(IA134SP.Print) > 0:
        if get_currency(IA134SP.FedRegTax) == 0:
            return 1
        else:
            return 0
    else:
        return 0

def BiggerInc_Calculation():
    return max_value(get_currency(IA134SP.IASourceInc), get_currency(IA134SP.NetDist))

def Credit_Calculation():
    return c_dollar(( ( ( Round(get_float(IA134SP.CreditPercent) * 100) )  / 100 )  * get_float(IA134SP.NetTax) )  / 100)

def CreditPercent_Calculation():
    if get_float(IA134SP.BusRatio) > 0:
        return max_value(0, 100 - get_float(IA134SP.TaxPercent))
    else:
        return 0

def Description_Calculation():
    Total = Currency()
    Total = get_currency(IA134SP.Credit)
    return CStr(Total) + ' Credit'

def Dividends_Calculation():
    return get_currency(USDSCorpK1.Dividends, ParentCopy()) -  ( c_dollar(get_float(USDSCorpK1.Dividends, ParentCopy()) * get_float(IA134SP.TPRatio)) )

def Exist_Calculation():
    return 1

def FedAGI_Calculation():
    if get_float(IA134SP.BusRatio) > 0:
        if get_bool(IAF1040.CombMFS) == True:
            return get_currency(USWRec.SAGI)
        else:
            return 0
    else:
        return 0

def FedTax_Calculation():
    return get_currency(IA134SP.K1FedTax)

def IAApportion_Calculation():
    return c_dollar(( ( ( Round(get_float(IA134SP.IABusRatio) * 100) )  / 100 )  * get_float(IA134SP.NetIAInc) )  / 100)

def IABusRatio_Calculation():
    return get_float(IA134SP.BusRatio) * 100

def IAInc_Calculation():
    if get_float(IA134SP.BusRatio) > 0:
        if get_bool(IAF1040.CombMFS) == True:
            return get_currency(IAF1040.BNet) + get_currency(IAOTHADJ.SIANOL)
        else:
            return 0
    else:
        return 0

def IASCorpInc_Calculation():
    if get_float(IA134SP.BusRatio) > 0:
        return get_currency(IA134SP.K1Inc) + get_currency(IA134SP.StateAdj)
    else:
        return 0

def IASourceInc_Calculation():
    if get_float(IA134SP.BusRatio) > 0:
        return get_currency(IA134SP.IAApportion) + get_currency(IA134SP.IANonBusInc)
    else:
        return 0

def Interest_Calculation():
    return get_currency(USDSCorpK1.Interest, ParentCopy()) -  ( c_dollar(get_float(USDSCorpK1.Interest, ParentCopy()) * get_float(IA134SP.TPRatio)) )

def IntSCorp_Calculation():
    if trim(get_string(IA134SP.SCorpName)) != '':
        return get_string(IA134SP.SCorpName)
    else:
        return 'this S corporation'

def K1FedTax_Calculation():
    return max_value(0, get_currency(IA134SP.K1Tax) - get_currency(IA134SP.K1FedCredits))

def K1Inc_Calculation():
    return get_currency(IA134SP.TotInc) - get_currency(IA134SP.TotDed)

def K1Inc2_Calculation():
    return get_currency(IA134SP.K1Inc)

def K1IncPercent_Calculation():
    return get_float(IA134SP.K1IncRatio) * 100

def K1IncRatio_Calculation():
    TopLim = Double()
    if get_float(IA134SP.BusRatio) == 0:
        return 0
    elif get_float(IA134SP.FedAGI) <= 0:
        return 1
    else:
        TopLim = min_value(1, Round(get_float(IA134SP.K1Inc2) / get_float(IA134SP.FedAGI), 6))
        return max_value(0, TopLim)

def K1Tax_Calculation():
    return Round(c_dollar(get_float(IA134SP.NetFedTax) *  ( get_float(IA134SP.K1IncPercent) / 100 )))

def LtGain_Calculation():
    return get_currency(USDSCorpK1.LtGain, ParentCopy()) -  ( c_dollar(get_float(USDSCorpK1.LtGain, ParentCopy()) * get_float(IA134SP.TPRatio)) )

def Names_Calculation():
    return get_string(IAREQUIRED.SPCombName)

def NetDist_Calculation():
    if get_float(IA134SP.BusRatio) > 0:
        return max_value(0, get_currency(IA134SP.Distributions) - get_currency(IA134SP.FedTax))
    else:
        return 0

def NetFedTax_Calculation():
    return get_currency(IA134SP.FedRegTax) + get_currency(IA134SP.FedAMT)

def NetIAInc_Calculation():
    if get_float(IA134SP.BusRatio) > 0:
        return get_currency(IA134SP.IASCorpInc) - get_currency(IA134SP.NonBusInc)
    else:
        return 0

def NetTax_Calculation():
    if get_float(IA134SP.BusRatio) > 0:
        return get_currency(IAF1040.BTotIATax)
    else:
        return 0

def Numerator_Calculation():
    return get_currency(IA134SP.BiggerInc) + get_currency(IA134SP.Remainder)

def Ordinary_Calculation():
    return get_currency(USDSCorpK1.OrdAmt, ParentCopy()) -  ( c_dollar(get_float(USDSCorpK1.OrdAmt, ParentCopy()) * get_float(IA134SP.TPRatio)) )

def OthDed_Calculation():
    return get_currency(USDSCorpK1.SCOthDed, ParentCopy()) -  ( c_dollar(get_float(USDSCorpK1.SCOthDed, ParentCopy()) * get_float(IA134SP.TPRatio)) )

def OtherInc_Calculation():
    PortInc = Currency()

    Sec1256 = Currency()

    MineCost = Currency()

    OthInc = Currency()
    PortInc = get_currency(USDSCorpK1.PortInc, ParentCopy()) -  ( c_dollar(get_float(USDSCorpK1.PortInc, ParentCopy()) * get_float(IA134SP.TPRatio)) )
    Sec1256 = get_currency(USDSCorpK1.Sec1256, ParentCopy()) -  ( c_dollar(get_float(USDSCorpK1.Sec1256, ParentCopy()) * get_float(IA134SP.TPRatio)) )
    MineCost = get_currency(USDSCorpK1.MineCost, ParentCopy()) -  ( c_dollar(get_float(USDSCorpK1.MineCost, ParentCopy()) * get_float(IA134SP.TPRatio)) )
    OthInc = get_currency(USDSCorpK1.OthInc, ParentCopy()) -  ( c_dollar(get_float(USDSCorpK1.OthInc, ParentCopy()) * get_float(IA134SP.TPRatio)) )
    return PortInc + Sec1256 + MineCost + OthInc

def Print_Calculation():
    if get_bool(IAF1040.CombMFS) == False:
        return 0
    elif get_currency(IA134SP.Credit) > 0:
        return 1
    else:
        return 0

def RealEstate_Calculation():
    return get_currency(USDSCorpK1.RentAmt, ParentCopy()) -  ( c_dollar(get_float(USDSCorpK1.RentAmt, ParentCopy()) * get_float(IA134SP.TPRatio)) )

def Remainder_Calculation():
    return get_currency(IA134SP.IAInc) - get_currency(IA134SP.IASCorpInc)

def Rental_Calculation():
    return get_currency(USDSCorpK1.Rental, ParentCopy()) -  ( c_dollar(get_float(USDSCorpK1.Rental, ParentCopy()) * get_float(IA134SP.TPRatio)) )

def Royalties_Calculation():
    return get_currency(USDSCorpK1.Royalties, ParentCopy()) -  ( c_dollar(get_float(USDSCorpK1.Royalties, ParentCopy()) * get_float(IA134SP.TPRatio)) )

def SCorpEIN_Calculation():
    return get_string(USDSCorpK1.EIN, ParentCopy())

def SCorpName_Calculation():
    return get_string(USDSCorpK1.CoName, ParentCopy())

def Sec1231_Calculation():
    return get_currency(USDSCorpK1.Sec1231, ParentCopy()) -  ( c_dollar(get_float(USDSCorpK1.Sec1231, ParentCopy()) * get_float(IA134SP.TPRatio)) )

def Sec179_Calculation():
    return get_currency(USDSCorpK1.Sec179, ParentCopy()) -  ( c_dollar(get_float(USDSCorpK1.Sec179, ParentCopy()) * get_float(IA134SP.TPRatio)) )

def SPApplied_Calculation():
    count = Integer()

    count2 = Integer()
    count = 0
    while count <= 9:
        if get_string(IA148SP.NonRefCode(count)) == '11' and get_currency(IA148SP.CYCredit(count)) == get_currency(IA134SP.Credit):
            return get_currency(IA148SP.ArrayNonRefCr(count))
        count = count + 1
    count2 = 0
    while count <= 28:
        if get_string(IAWBP148SP.NonRefCode(count2)) == '11' and get_currency(IAWBP148SP.CYCredit(count2)) == get_currency(IA134SP.Credit):
            return get_currency(IAWBP148SP.ArrayNonRefCr(count2))
        count = count + 1
    return 0

def SPExpired_Calculation():
    count = Integer()

    count2 = Integer()
    count = 0
    while count <= 9:
        if get_string(IA148SP.NonRefCode(count)) == '11' and get_currency(IA148SP.CYCredit(count)) == get_currency(IA134SP.Credit):
            return get_currency(IA148SP.ExpCr(count))
        count = count + 1
    count2 = 0
    while count <= 28:
        if get_string(IAWBP148SP.NonRefCode(count2)) == '11' and get_currency(IAWBP148SP.CYCredit(count2)) == get_currency(IA134SP.Credit):
            return get_currency(IAWBP148SP.ExpCr(count2))
        count = count + 1
    return 0

def SSN_Calculation():
    return get_string(IAF1040.SpouseSSN)

def StGain_Calculation():
    return get_currency(USDSCorpK1.StGain, ParentCopy()) -  ( c_dollar(get_float(USDSCorpK1.StGain, ParentCopy()) * get_float(IA134SP.TPRatio)) )

def TaxPercent_Calculation():
    return get_float(IA134SP.TaxRatio) * 100

def TaxRatio_Calculation():
    TopLim = Double()
    if get_float(IA134SP.BusRatio) == 0:
        return 0
    elif get_float(IA134SP.IAInc) == 0:
        return 1
    else:
        TopLim = min_value(1, Round(get_float(IA134SP.Numerator) / get_float(IA134SP.IAInc), 6))
        return max_value(0, TopLim)

def TotDed_Calculation():
    if get_float(IA134SP.BusRatio) > 0:
        return get_currency(IA134SP.Sec179) + get_currency(IA134SP.OthDed)
    else:
        return 0

def TotInc_Calculation():
    if get_float(IA134SP.BusRatio) > 0:
        return get_currency(IA134SP.Ordinary) + get_currency(IA134SP.RealEstate) + get_currency(IA134SP.Rental) + get_currency(IA134SP.Interest) + get_currency(IA134SP.Dividends) + get_currency(IA134SP.Royalties) + get_currency(IA134SP.StGain) + get_currency(IA134SP.LtGain) + get_currency(IA134SP.Sec1231) + get_currency(IA134SP.OtherInc)
    else:
        return 0

def TPRatio_Calculation():
    if get_bool(IAF1040.CombMFS) == True and get_bool(USDSCorpK1.Joint, ParentCopy()) == True:
        return 0.5
    elif get_bool(IAF1040.CombMFS) == True and get_bool(USDSCorpK1.Spouse, ParentCopy()) == True:
        return 0
    else:
        return 1


