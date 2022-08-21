from forms.out import IA2210
from forms.out import IA2210AN
from forms.out import IA2210ANSP
from forms.out import IA2210SP
from forms.out import IAF1040
from forms.out import IAREQUIRED
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def AskItmDed_Calculation():
    if get_bool(IAF1040.ItemCheck) == True:
        return 1
    elif get_currency(IA2210ANSP.Q1ItmDed) != 0:
        return 1
    elif get_currency(IA2210ANSP.Q2ItmDed) != 0:
        return 1
    elif get_currency(IA2210ANSP.Q3ItmDed) != 0:
        return 1
    else:
        return 0

def Description_Calculation():
    return get_string(IA2210ANSP.Names)

def Names_Calculation():
    return get_string(IAREQUIRED.SPCombName)

def Print_Calculation():
    if get_bool(IAF1040.CombMFS) == False:
        return 0
    elif get_bool(IA2210SP.AnInc) == True:
        return 1
    else:
        return 0

def Q1AIInstall_Calculation():
    return min_value(get_currency(IA2210ANSP.Q1BalDue), get_currency(IA2210ANSP.Q1TotPay))

def Q1AnFedPay_Calculation():
    return c_dollar(get_float(IA2210ANSP.Q1FedPay) * 4)

def Q1AnInc_Calculation():
    return c_dollar(get_float(IA2210ANSP.Q1NetInc) * 4)

def Q1AnItmDed_Calculation():
    if get_bool(IAF1040.ItemCheck) == True:
        return c_dollar(get_float(IA2210ANSP.Q1ItmDed) * 4)
    else:
        return 0

def Q1Balance_Calculation():
    return max_value(0, get_currency(IA2210ANSP.Q1TotTax) - get_currency(IA2210ANSP.Q1ExemCr) - get_currency(IA2210ANSP.Q1NonRefCr) - get_currency(IA2210ANSP.Q1RefCr))

def Q1BalDue_Calculation():
    return get_currency(IA2210ANSP.Q1PerTax)

def Q1Deduct_Calculation():
    return max_value(get_currency(IA2210ANSP.Q1AnItmDed), get_currency(IA2210ANSP.Q1StndDed))

def Q1ExemCr_Calculation():
    return get_currency(IAF1040.BExemCr)

def Q1PerTax_Calculation():
    return c_dollar(get_float(IA2210ANSP.Q1Balance) * 0.225)

def Q1ReqPay_Calculation():
    return get_currency(IA2210SP.Q1Install)

def Q1StndDed_Calculation():
    # updated for 2018
    if IAFS() == 2 or IAFS() == 5 or IAFS() == 6:
        return Decimal("5000")
    else:
        return Decimal("2030")

def Q1Tax_Calculation():
    Mid = Currency()

    MidInt = Long()

    TotTaxInc = Currency()
    # updated for 2018
    TotTaxInc = get_currency(IA2210ANSP.Q1TaxInc)
    if TotTaxInc > Decimal("95650"):
        Mid = TotTaxInc
    elif TotTaxInc > Decimal("150"):
        MidInt = CLng(( TotTaxInc - Decimal("1") )  / Decimal("50"))
        Mid = ( CCur(MidInt) * Decimal("50") )  + Decimal("25")
    else:
        Mid = Decimal("0")
    return Tax(Mid)

def Q1TaxInc_Calculation():
    return max_value(0, get_currency(IA2210ANSP.Q1AnInc) - get_currency(IA2210ANSP.Q1AnFedPay) - get_currency(IA2210ANSP.Q1Deduct))

def Q1TotPay_Calculation():
    return get_currency(IA2210ANSP.Q1ReqPay)

def Q1TotTax_Calculation():
    return get_currency(IA2210ANSP.Q1Tax) + get_currency(IA2210ANSP.Q1OthTax)

def Q1Unpay_Calculation():
    return max_value(0, get_currency(IA2210ANSP.Q1TotPay) - get_currency(IA2210ANSP.Q1BalDue))

def Q2AIInstall_Calculation():
    return min_value(get_currency(IA2210ANSP.Q2BalDue), get_currency(IA2210ANSP.Q2TotPay))

def Q2AnFedPay_Calculation():
    return c_dollar(get_float(IA2210ANSP.Q2FedPay) * 2.4)

def Q2AnInc_Calculation():
    return c_dollar(get_float(IA2210ANSP.Q2NetInc) * 2.4)

def Q2AnItmDed_Calculation():
    if get_bool(IAF1040.ItemCheck) == True:
        return c_dollar(get_float(IA2210ANSP.Q2ItmDed) * 2.4)
    else:
        return 0

def Q2Balance_Calculation():
    return max_value(0, get_currency(IA2210ANSP.Q2TotTax) - get_currency(IA2210ANSP.Q2ExemCr) - get_currency(IA2210ANSP.Q2NonRefCr) - get_currency(IA2210ANSP.Q2RefCr))

def Q2BalDue_Calculation():
    return max_value(0, get_currency(IA2210ANSP.Q2PerTax) - get_currency(IA2210ANSP.Q2PQInst))

def Q2Deduct_Calculation():
    return max_value(get_currency(IA2210ANSP.Q2AnItmDed), get_currency(IA2210ANSP.Q2StndDed))

def Q2ExemCr_Calculation():
    return get_currency(IA2210ANSP.Q1ExemCr)

def Q2PerTax_Calculation():
    return c_dollar(get_float(IA2210ANSP.Q2Balance) * 0.45)

def Q2PQInst_Calculation():
    return get_currency(IA2210ANSP.Q1AIInstall)

def Q2PQUnpay_Calculation():
    return get_currency(IA2210ANSP.Q1Unpay)

def Q2ReqPay_Calculation():
    return get_currency(IA2210SP.Q2Install)

def Q2StndDed_Calculation():
    return get_currency(IA2210ANSP.Q1StndDed)

def Q2Tax_Calculation():
    Mid = Currency()

    MidInt = Long()

    TotTaxInc = Currency()
    # updated for 2018
    TotTaxInc = get_currency(IA2210ANSP.Q2TaxInc)
    if TotTaxInc > Decimal("95650"):
        Mid = TotTaxInc
    elif TotTaxInc > Decimal("150"):
        MidInt = CLng(( TotTaxInc - Decimal("1") )  / Decimal("50"))
        Mid = ( CCur(MidInt) * Decimal("50") )  + Decimal("25")
    else:
        Mid = Decimal("0")
    return Tax(Mid)

def Q2TaxInc_Calculation():
    return max_value(0, get_currency(IA2210ANSP.Q2AnInc) - get_currency(IA2210ANSP.Q2AnFedPay) - get_currency(IA2210ANSP.Q2Deduct))

def Q2TotPay_Calculation():
    return get_currency(IA2210ANSP.Q2ReqPay) + get_currency(IA2210ANSP.Q2PQUnpay)

def Q2TotTax_Calculation():
    return get_currency(IA2210ANSP.Q2Tax) + get_currency(IA2210ANSP.Q2OthTax)

def Q2Unpay_Calculation():
    return max_value(0, get_currency(IA2210ANSP.Q2TotPay) - get_currency(IA2210ANSP.Q2BalDue))

def Q3AIInstall_Calculation():
    return min_value(get_currency(IA2210ANSP.Q3BalDue), get_currency(IA2210ANSP.Q3TotPay))

def Q3AnFedPay_Calculation():
    return c_dollar(get_float(IA2210ANSP.Q3FedPay) * 1.5)

def Q3AnInc_Calculation():
    return c_dollar(get_float(IA2210ANSP.Q3NetInc) * 1.5)

def Q3AnItmDed_Calculation():
    if get_bool(IAF1040.ItemCheck) == True:
        return c_dollar(get_float(IA2210ANSP.Q3ItmDed) * 1.5)
    else:
        return 0

def Q3Balance_Calculation():
    return max_value(0, get_currency(IA2210ANSP.Q3TotTax) - get_currency(IA2210ANSP.Q3ExemCr) - get_currency(IA2210ANSP.Q3NonRefCr) - get_currency(IA2210ANSP.Q3RefCr))

def Q3BalDue_Calculation():
    return max_value(0, get_currency(IA2210ANSP.Q3PerTax) - get_currency(IA2210ANSP.Q3PQInst))

def Q3Deduct_Calculation():
    return max_value(get_currency(IA2210ANSP.Q3AnItmDed), get_currency(IA2210ANSP.Q3StndDed))

def Q3ExemCr_Calculation():
    return get_currency(IA2210ANSP.Q1ExemCr)

def Q3PerTax_Calculation():
    return c_dollar(get_float(IA2210ANSP.Q3Balance) * 0.675)

def Q3PQInst_Calculation():
    return get_currency(IA2210ANSP.Q1AIInstall) + get_currency(IA2210ANSP.Q2AIInstall)

def Q3PQUnpay_Calculation():
    return get_currency(IA2210ANSP.Q2Unpay)

def Q3ReqPay_Calculation():
    return get_currency(IA2210SP.Q3Install)

def Q3StndDed_Calculation():
    return get_currency(IA2210ANSP.Q1StndDed)

def Q3Tax_Calculation():
    Mid = Currency()

    MidInt = Long()

    TotTaxInc = Currency()
    # updated for 2018
    TotTaxInc = get_currency(IA2210ANSP.Q3TaxInc)
    if TotTaxInc > Decimal("95650"):
        Mid = TotTaxInc
    elif TotTaxInc > Decimal("150"):
        MidInt = CLng(( TotTaxInc - Decimal("1") )  / Decimal("50"))
        Mid = ( CCur(MidInt) * Decimal("50") )  + Decimal("25")
    else:
        Mid = Decimal("0")
    return Tax(Mid)

def Q3TaxInc_Calculation():
    return max_value(0, get_currency(IA2210ANSP.Q3AnInc) - get_currency(IA2210ANSP.Q3AnFedPay) - get_currency(IA2210ANSP.Q3Deduct))

def Q3TotPay_Calculation():
    return get_currency(IA2210ANSP.Q3ReqPay) + get_currency(IA2210ANSP.Q3PQUnpay)

def Q3TotTax_Calculation():
    return get_currency(IA2210ANSP.Q3Tax) + get_currency(IA2210ANSP.Q3OthTax)

def Q3Unpay_Calculation():
    return max_value(0, get_currency(IA2210ANSP.Q3TotPay) - get_currency(IA2210ANSP.Q3BalDue))

def Q4AIInstall_Calculation():
    return min_value(get_currency(IA2210ANSP.Q4BalDue), get_currency(IA2210ANSP.Q4TotPay))

def Q4AnFedPay_Calculation():
    return get_currency(IA2210ANSP.Q4FedPay)

def Q4AnInc_Calculation():
    return get_currency(IA2210ANSP.Q4NetInc)

def Q4AnItmDed_Calculation():
    return get_currency(IA2210ANSP.Q4ItmDed)

def Q4Balance_Calculation():
    return max_value(0, get_currency(IA2210ANSP.Q4TotTax) - get_currency(IA2210ANSP.Q4ExemCr) - get_currency(IA2210ANSP.Q4NonRefCr) - get_currency(IA2210ANSP.Q4RefCr))

def Q4BalDue_Calculation():
    return max_value(0, get_currency(IA2210ANSP.Q4PerTax) - get_currency(IA2210ANSP.Q4PQInst))

def Q4Deduct_Calculation():
    return max_value(get_currency(IA2210ANSP.Q4AnItmDed), get_currency(IA2210ANSP.Q4StndDed))

def Q4ExemCr_Calculation():
    return get_currency(IA2210ANSP.Q1ExemCr)

def Q4FedPay_Calculation():
    return get_currency(IAF1040.BFedDed) - get_currency(IAF1040.BFedTax)

def Q4ItmDed_Calculation():
    if get_bool(IAF1040.ItemCheck) == True:
        return get_currency(IAF1040.BDedBox)
    else:
        return 0

def Q4NetInc_Calculation():
    return get_currency(IAF1040.BNet)

def Q4NonRefCr_Calculation():
    return get_currency(IAF1040.BTuit) + get_currency(IAF1040.BVolFireCr) + get_currency(IAF1040.BCrNon) + get_currency(IAF1040.BOutState) + get_currency(IAF1040.BOthIACr)

def Q4OthTax_Calculation():
    return get_currency(IAF1040.BLump) + get_currency(IAF1040.BIAMin)

def Q4PerTax_Calculation():
    return c_dollar(get_float(IA2210ANSP.Q4Balance) * 0.9)

def Q4PQInst_Calculation():
    return get_currency(IA2210ANSP.Q1AIInstall) + get_currency(IA2210ANSP.Q2AIInstall) + get_currency(IA2210ANSP.Q3AIInstall)

def Q4PQUnpay_Calculation():
    return get_currency(IA2210ANSP.Q3Unpay)

def Q4RefCr_Calculation():
    return get_currency(IAF1040.BFuel) + get_currency(IAF1040.BChild) + get_currency(IAF1040.BIEIC) + get_currency(IAF1040.BOthRefCr)

def Q4ReqPay_Calculation():
    return get_currency(IA2210SP.Q4Install)

def Q4StndDed_Calculation():
    return get_currency(IA2210ANSP.Q1StndDed)

def Q4Tax_Calculation():
    Mid = Currency()

    MidInt = Long()

    TotTaxInc = Currency()
    # updated for 2018
    TotTaxInc = get_currency(IA2210ANSP.Q4TaxInc)
    if TotTaxInc > Decimal("95650"):
        Mid = TotTaxInc
    elif TotTaxInc > Decimal("150"):
        MidInt = CLng(( TotTaxInc - Decimal("1") )  / Decimal("50"))
        Mid = ( CCur(MidInt) * Decimal("50") )  + Decimal("25")
    else:
        Mid = Decimal("0")
    return Tax(Mid)

def Q4TaxInc_Calculation():
    return max_value(0, get_currency(IA2210ANSP.Q4AnInc) - get_currency(IA2210ANSP.Q4AnFedPay) - get_currency(IA2210ANSP.Q4Deduct))

def Q4TotPay_Calculation():
    return get_currency(IA2210ANSP.Q4ReqPay) + get_currency(IA2210ANSP.Q4PQUnpay)

def Q4TotTax_Calculation():
    return get_currency(IA2210ANSP.Q4Tax) + get_currency(IA2210ANSP.Q4OthTax)

def SSN_Calculation():
    return get_string(IAF1040.SpouseSSN)


