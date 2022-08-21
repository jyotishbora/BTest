from forms.out import IA2210
from forms.out import IA2210AN
from forms.out import IAF1040
from forms.out import IAREQUIRED
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def AskItmDed_Calculation():
    if get_bool(IAF1040.ItemCheck) == True:
        return 1
    elif get_currency(IA2210AN.Q1ItmDed) != 0:
        return 1
    elif get_currency(IA2210AN.Q2ItmDed) != 0:
        return 1
    elif get_currency(IA2210AN.Q3ItmDed) != 0:
        return 1
    else:
        return 0

def Description_Calculation():
    return get_string(IA2210AN.Names)

def Names_Calculation():
    if get_bool(IAF1040.CombMFS) == True:
        return get_string(IAREQUIRED.TPCombName)
    else:
        return get_string(IAREQUIRED.CombNames)

def Print_Calculation():
    if get_bool(IA2210.AnInc) == True:
        return 1
    else:
        return 0

def Q1AIInstall_Calculation():
    return min_value(get_currency(IA2210AN.Q1BalDue), get_currency(IA2210AN.Q1TotPay))

def Q1AnFedPay_Calculation():
    return c_dollar(get_float(IA2210AN.Q1FedPay) * 4)

def Q1AnInc_Calculation():
    return c_dollar(get_float(IA2210AN.Q1NetInc) * 4)

def Q1AnItmDed_Calculation():
    if get_bool(IAF1040.ItemCheck) == True:
        return c_dollar(get_float(IA2210AN.Q1ItmDed) * 4)
    else:
        return 0

def Q1Balance_Calculation():
    return max_value(0, get_currency(IA2210AN.Q1TotTax) - get_currency(IA2210AN.Q1ExemCr) - get_currency(IA2210AN.Q1NonRefCr) - get_currency(IA2210AN.Q1RefCr))

def Q1BalDue_Calculation():
    return get_currency(IA2210AN.Q1PerTax)

def Q1Deduct_Calculation():
    return max_value(get_currency(IA2210AN.Q1AnItmDed), get_currency(IA2210AN.Q1StndDed))

def Q1ExemCr_Calculation():
    return get_currency(IAF1040.AExemCr)

def Q1PerTax_Calculation():
    return c_dollar(get_float(IA2210AN.Q1Balance) * 0.225)

def Q1ReqPay_Calculation():
    return get_currency(IA2210.Q1Install)

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
    TotTaxInc = get_currency(IA2210AN.Q1TaxInc)
    if TotTaxInc > Decimal("95650"):
        Mid = TotTaxInc
    elif TotTaxInc > Decimal("150"):
        MidInt = CLng(( TotTaxInc - Decimal("1") )  / Decimal("50"))
        Mid = ( CCur(MidInt) * Decimal("50") )  + Decimal("25")
    else:
        Mid = Decimal("0")
    return Tax(Mid)

def Q1TaxInc_Calculation():
    return max_value(0, get_currency(IA2210AN.Q1AnInc) - get_currency(IA2210AN.Q1AnFedPay) - get_currency(IA2210AN.Q1Deduct))

def Q1TotPay_Calculation():
    return get_currency(IA2210AN.Q1ReqPay)

def Q1TotTax_Calculation():
    return get_currency(IA2210AN.Q1Tax) + get_currency(IA2210AN.Q1OthTax)

def Q1Unpay_Calculation():
    return max_value(0, get_currency(IA2210AN.Q1TotPay) - get_currency(IA2210AN.Q1BalDue))

def Q2AIInstall_Calculation():
    return min_value(get_currency(IA2210AN.Q2BalDue), get_currency(IA2210AN.Q2TotPay))

def Q2AnFedPay_Calculation():
    return c_dollar(get_float(IA2210AN.Q2FedPay) * 2.4)

def Q2AnInc_Calculation():
    return c_dollar(get_float(IA2210AN.Q2NetInc) * 2.4)

def Q2AnItmDed_Calculation():
    if get_bool(IAF1040.ItemCheck) == True:
        return c_dollar(get_float(IA2210AN.Q2ItmDed) * 2.4)
    else:
        return 0

def Q2Balance_Calculation():
    return max_value(0, get_currency(IA2210AN.Q2TotTax) - get_currency(IA2210AN.Q2ExemCr) - get_currency(IA2210AN.Q2NonRefCr) - get_currency(IA2210AN.Q2RefCr))

def Q2BalDue_Calculation():
    return max_value(0, get_currency(IA2210AN.Q2PerTax) - get_currency(IA2210AN.Q2PQInst))

def Q2Deduct_Calculation():
    return max_value(get_currency(IA2210AN.Q2AnItmDed), get_currency(IA2210AN.Q2StndDed))

def Q2ExemCr_Calculation():
    return get_currency(IA2210AN.Q1ExemCr)

def Q2PerTax_Calculation():
    return c_dollar(get_float(IA2210AN.Q2Balance) * 0.45)

def Q2PQInst_Calculation():
    return get_currency(IA2210AN.Q1AIInstall)

def Q2PQUnpay_Calculation():
    return get_currency(IA2210AN.Q1Unpay)

def Q2ReqPay_Calculation():
    return get_currency(IA2210.Q2Install)

def Q2StndDed_Calculation():
    return get_currency(IA2210AN.Q1StndDed)

def Q2Tax_Calculation():
    Mid = Currency()

    MidInt = Long()

    TotTaxInc = Currency()
    # updated for 2018
    TotTaxInc = get_currency(IA2210AN.Q2TaxInc)
    if TotTaxInc > Decimal("95650"):
        Mid = TotTaxInc
    elif TotTaxInc > Decimal("150"):
        MidInt = CLng(( TotTaxInc - Decimal("1") )  / Decimal("50"))
        Mid = ( CCur(MidInt) * Decimal("50") )  + Decimal("25")
    else:
        Mid = Decimal("0")
    return Tax(Mid)

def Q2TaxInc_Calculation():
    return max_value(0, get_currency(IA2210AN.Q2AnInc) - get_currency(IA2210AN.Q2AnFedPay) - get_currency(IA2210AN.Q2Deduct))

def Q2TotPay_Calculation():
    return get_currency(IA2210AN.Q2ReqPay) + get_currency(IA2210AN.Q2PQUnpay)

def Q2TotTax_Calculation():
    return get_currency(IA2210AN.Q2Tax) + get_currency(IA2210AN.Q2OthTax)

def Q2Unpay_Calculation():
    return max_value(0, get_currency(IA2210AN.Q2TotPay) - get_currency(IA2210AN.Q2BalDue))

def Q3AIInstall_Calculation():
    return min_value(get_currency(IA2210AN.Q3BalDue), get_currency(IA2210AN.Q3TotPay))

def Q3AnFedPay_Calculation():
    return c_dollar(get_float(IA2210AN.Q3FedPay) * 1.5)

def Q3AnInc_Calculation():
    return c_dollar(get_float(IA2210AN.Q3NetInc) * 1.5)

def Q3AnItmDed_Calculation():
    if get_bool(IAF1040.ItemCheck) == True:
        return c_dollar(get_float(IA2210AN.Q3ItmDed) * 1.5)
    else:
        return 0

def Q3Balance_Calculation():
    return max_value(0, get_currency(IA2210AN.Q3TotTax) - get_currency(IA2210AN.Q3ExemCr) - get_currency(IA2210AN.Q3NonRefCr) - get_currency(IA2210AN.Q3RefCr))

def Q3BalDue_Calculation():
    return max_value(0, get_currency(IA2210AN.Q3PerTax) - get_currency(IA2210AN.Q3PQInst))

def Q3Deduct_Calculation():
    return max_value(get_currency(IA2210AN.Q3AnItmDed), get_currency(IA2210AN.Q3StndDed))

def Q3ExemCr_Calculation():
    return get_currency(IA2210AN.Q1ExemCr)

def Q3PerTax_Calculation():
    return c_dollar(get_float(IA2210AN.Q3Balance) * 0.675)

def Q3PQInst_Calculation():
    return get_currency(IA2210AN.Q1AIInstall) + get_currency(IA2210AN.Q2AIInstall)

def Q3PQUnpay_Calculation():
    return get_currency(IA2210AN.Q2Unpay)

def Q3ReqPay_Calculation():
    return get_currency(IA2210.Q3Install)

def Q3StndDed_Calculation():
    return get_currency(IA2210AN.Q1StndDed)

def Q3Tax_Calculation():
    Mid = Currency()

    MidInt = Long()

    TotTaxInc = Currency()
    # updated for 2018
    TotTaxInc = get_currency(IA2210AN.Q3TaxInc)
    if TotTaxInc > Decimal("95650"):
        Mid = TotTaxInc
    elif TotTaxInc > Decimal("150"):
        MidInt = CLng(( TotTaxInc - Decimal("1") )  / Decimal("50"))
        Mid = ( CCur(MidInt) * Decimal("50") )  + Decimal("25")
    else:
        Mid = Decimal("0")
    return Tax(Mid)

def Q3TaxInc_Calculation():
    return max_value(0, get_currency(IA2210AN.Q3AnInc) - get_currency(IA2210AN.Q3AnFedPay) - get_currency(IA2210AN.Q3Deduct))

def Q3TotPay_Calculation():
    return get_currency(IA2210AN.Q3ReqPay) + get_currency(IA2210AN.Q3PQUnpay)

def Q3TotTax_Calculation():
    return get_currency(IA2210AN.Q3Tax) + get_currency(IA2210AN.Q3OthTax)

def Q3Unpay_Calculation():
    return max_value(0, get_currency(IA2210AN.Q3TotPay) - get_currency(IA2210AN.Q3BalDue))

def Q4AIInstall_Calculation():
    return min_value(get_currency(IA2210AN.Q4BalDue), get_currency(IA2210AN.Q4TotPay))

def Q4AnFedPay_Calculation():
    return get_currency(IA2210AN.Q4FedPay)

def Q4AnInc_Calculation():
    return get_currency(IA2210AN.Q4NetInc)

def Q4AnItmDed_Calculation():
    return get_currency(IA2210AN.Q4ItmDed)

def Q4Balance_Calculation():
    return max_value(0, get_currency(IA2210AN.Q4TotTax) - get_currency(IA2210AN.Q4ExemCr) - get_currency(IA2210AN.Q4NonRefCr) - get_currency(IA2210AN.Q4RefCr))

def Q4BalDue_Calculation():
    return max_value(0, get_currency(IA2210AN.Q4PerTax) - get_currency(IA2210AN.Q4PQInst))

def Q4Deduct_Calculation():
    return max_value(get_currency(IA2210AN.Q4AnItmDed), get_currency(IA2210AN.Q4StndDed))

def Q4ExemCr_Calculation():
    return get_currency(IA2210AN.Q1ExemCr)

def Q4FedPay_Calculation():
    return get_currency(IAF1040.AFedDed) - get_currency(IAF1040.AFedTax)

def Q4ItmDed_Calculation():
    if get_bool(IAF1040.ItemCheck) == True:
        return get_currency(IAF1040.ADedBox)
    else:
        return 0

def Q4NetInc_Calculation():
    return get_currency(IAF1040.ANet)

def Q4NonRefCr_Calculation():
    return get_currency(IAF1040.ATuit) + get_currency(IAF1040.AVolFireCr) + get_currency(IAF1040.ACrNon) + get_currency(IAF1040.AOutState) + get_currency(IAF1040.AOthIACr)

def Q4OthTax_Calculation():
    return get_currency(IAF1040.ALump) + get_currency(IAF1040.AIAMin)

def Q4PerTax_Calculation():
    return c_dollar(get_float(IA2210AN.Q4Balance) * 0.9)

def Q4PQInst_Calculation():
    return get_currency(IA2210AN.Q1AIInstall) + get_currency(IA2210AN.Q2AIInstall) + get_currency(IA2210AN.Q3AIInstall)

def Q4PQUnpay_Calculation():
    return get_currency(IA2210AN.Q3Unpay)

def Q4RefCr_Calculation():
    return get_currency(IAF1040.AFuel) + get_currency(IAF1040.AChild) + get_currency(IAF1040.AIEIC) + get_currency(IAF1040.AOthRefCr)

def Q4ReqPay_Calculation():
    return get_currency(IA2210.Q4Install)

def Q4StndDed_Calculation():
    return get_currency(IA2210AN.Q1StndDed)

def Q4Tax_Calculation():
    Mid = Currency()

    MidInt = Long()

    TotTaxInc = Currency()
    # updated for 2018
    TotTaxInc = get_currency(IA2210AN.Q4TaxInc)
    if TotTaxInc > Decimal("95650"):
        Mid = TotTaxInc
    elif TotTaxInc > Decimal("150"):
        MidInt = CLng(( TotTaxInc - Decimal("1") )  / Decimal("50"))
        Mid = ( CCur(MidInt) * Decimal("50") )  + Decimal("25")
    else:
        Mid = Decimal("0")
    return Tax(Mid)

def Q4TaxInc_Calculation():
    return max_value(0, get_currency(IA2210AN.Q4AnInc) - get_currency(IA2210AN.Q4AnFedPay) - get_currency(IA2210AN.Q4Deduct))

def Q4TotPay_Calculation():
    return get_currency(IA2210AN.Q4ReqPay) + get_currency(IA2210AN.Q4PQUnpay)

def Q4TotTax_Calculation():
    return get_currency(IA2210AN.Q4Tax) + get_currency(IA2210AN.Q4OthTax)

def SSN_Calculation():
    return get_string(IAF1040.SSN)


