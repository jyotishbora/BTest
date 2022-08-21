from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def AskItmDed_Calculation():
    if GetBool(IAF1040.ItemCheck) == True:
        ReturnVal = 1
    elif GetCurrency(IA2210AnSp.Q1ItmDed) != 0:
        ReturnVal = 1
    elif GetCurrency(IA2210AnSp.Q2ItmDed) != 0:
        ReturnVal = 1
    elif GetCurrency(IA2210AnSp.Q3ItmDed) != 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Description_Calculation():
    ReturnVal = GetString(IA2210AnSp.Names)

def Names_Calculation():
    ReturnVal = GetString(IARequired.SPCombName)

def Print_Calculation():
    if GetBool(IAF1040.CombMFS) == False:
        ReturnVal = 0
    elif GetBool(IA2210Sp.AnInc) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Q1AIInstall_Calculation():
    ReturnVal = MinValue(GetCurrency(IA2210AnSp.Q1BalDue), GetCurrency(IA2210AnSp.Q1TotPay))

def Q1AnFedPay_Calculation():
    ReturnVal = CDollar(GetFloat(IA2210AnSp.Q1FedPay) * 4)

def Q1AnInc_Calculation():
    ReturnVal = CDollar(GetFloat(IA2210AnSp.Q1NetInc) * 4)

def Q1AnItmDed_Calculation():
    if GetBool(IAF1040.ItemCheck) == True:
        ReturnVal = CDollar(GetFloat(IA2210AnSp.Q1ItmDed) * 4)
    else:
        ReturnVal = 0

def Q1Balance_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2210AnSp.Q1TotTax) - GetCurrency(IA2210AnSp.Q1ExemCr) - GetCurrency(IA2210AnSp.Q1NonRefCr) - GetCurrency(IA2210AnSp.Q1RefCr))

def Q1BalDue_Calculation():
    ReturnVal = GetCurrency(IA2210AnSp.Q1PerTax)

def Q1Deduct_Calculation():
    ReturnVal = MaxValue(GetCurrency(IA2210AnSp.Q1AnItmDed), GetCurrency(IA2210AnSp.Q1StndDed))

def Q1ExemCr_Calculation():
    ReturnVal = GetCurrency(IAF1040.BExemCr)

def Q1PerTax_Calculation():
    ReturnVal = CDollar(GetFloat(IA2210AnSp.Q1Balance) * 0.225)

def Q1ReqPay_Calculation():
    ReturnVal = GetCurrency(IA2210Sp.Q1Install)

def Q1StndDed_Calculation():
    # updated for 2018
    if IAFS() == 2 or IAFS() == 5 or IAFS() == 6:
        ReturnVal = Decimal("5000")
    else:
        ReturnVal = Decimal("2030")

def Q1Tax_Calculation():
    Mid = Currency()

    MidInt = Long()

    TotTaxInc = Currency()
    # updated for 2018
    TotTaxInc = GetCurrency(IA2210AnSp.Q1TaxInc)
    if TotTaxInc > Decimal("95650"):
        Mid = TotTaxInc
    elif TotTaxInc > Decimal("150"):
        MidInt = CLng(( TotTaxInc - Decimal("1") )  / Decimal("50"))
        Mid = ( CCur(MidInt) * Decimal("50") )  + Decimal("25")
    else:
        Mid = Decimal("0")
    ReturnVal = Tax(Mid)

def Q1TaxInc_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2210AnSp.Q1AnInc) - GetCurrency(IA2210AnSp.Q1AnFedPay) - GetCurrency(IA2210AnSp.Q1Deduct))

def Q1TotPay_Calculation():
    ReturnVal = GetCurrency(IA2210AnSp.Q1ReqPay)

def Q1TotTax_Calculation():
    ReturnVal = GetCurrency(IA2210AnSp.Q1Tax) + GetCurrency(IA2210AnSp.Q1OthTax)

def Q1Unpay_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2210AnSp.Q1TotPay) - GetCurrency(IA2210AnSp.Q1BalDue))

def Q2AIInstall_Calculation():
    ReturnVal = MinValue(GetCurrency(IA2210AnSp.Q2BalDue), GetCurrency(IA2210AnSp.Q2TotPay))

def Q2AnFedPay_Calculation():
    ReturnVal = CDollar(GetFloat(IA2210AnSp.Q2FedPay) * 2.4)

def Q2AnInc_Calculation():
    ReturnVal = CDollar(GetFloat(IA2210AnSp.Q2NetInc) * 2.4)

def Q2AnItmDed_Calculation():
    if GetBool(IAF1040.ItemCheck) == True:
        ReturnVal = CDollar(GetFloat(IA2210AnSp.Q2ItmDed) * 2.4)
    else:
        ReturnVal = 0

def Q2Balance_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2210AnSp.Q2TotTax) - GetCurrency(IA2210AnSp.Q2ExemCr) - GetCurrency(IA2210AnSp.Q2NonRefCr) - GetCurrency(IA2210AnSp.Q2RefCr))

def Q2BalDue_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2210AnSp.Q2PerTax) - GetCurrency(IA2210AnSp.Q2PQInst))

def Q2Deduct_Calculation():
    ReturnVal = MaxValue(GetCurrency(IA2210AnSp.Q2AnItmDed), GetCurrency(IA2210AnSp.Q2StndDed))

def Q2ExemCr_Calculation():
    ReturnVal = GetCurrency(IA2210AnSp.Q1ExemCr)

def Q2PerTax_Calculation():
    ReturnVal = CDollar(GetFloat(IA2210AnSp.Q2Balance) * 0.45)

def Q2PQInst_Calculation():
    ReturnVal = GetCurrency(IA2210AnSp.Q1AIInstall)

def Q2PQUnpay_Calculation():
    ReturnVal = GetCurrency(IA2210AnSp.Q1Unpay)

def Q2ReqPay_Calculation():
    ReturnVal = GetCurrency(IA2210Sp.Q2Install)

def Q2StndDed_Calculation():
    ReturnVal = GetCurrency(IA2210AnSp.Q1StndDed)

def Q2Tax_Calculation():
    Mid = Currency()

    MidInt = Long()

    TotTaxInc = Currency()
    # updated for 2018
    TotTaxInc = GetCurrency(IA2210AnSp.Q2TaxInc)
    if TotTaxInc > Decimal("95650"):
        Mid = TotTaxInc
    elif TotTaxInc > Decimal("150"):
        MidInt = CLng(( TotTaxInc - Decimal("1") )  / Decimal("50"))
        Mid = ( CCur(MidInt) * Decimal("50") )  + Decimal("25")
    else:
        Mid = Decimal("0")
    ReturnVal = Tax(Mid)

def Q2TaxInc_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2210AnSp.Q2AnInc) - GetCurrency(IA2210AnSp.Q2AnFedPay) - GetCurrency(IA2210AnSp.Q2Deduct))

def Q2TotPay_Calculation():
    ReturnVal = GetCurrency(IA2210AnSp.Q2ReqPay) + GetCurrency(IA2210AnSp.Q2PQUnpay)

def Q2TotTax_Calculation():
    ReturnVal = GetCurrency(IA2210AnSp.Q2Tax) + GetCurrency(IA2210AnSp.Q2OthTax)

def Q2Unpay_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2210AnSp.Q2TotPay) - GetCurrency(IA2210AnSp.Q2BalDue))

def Q3AIInstall_Calculation():
    ReturnVal = MinValue(GetCurrency(IA2210AnSp.Q3BalDue), GetCurrency(IA2210AnSp.Q3TotPay))

def Q3AnFedPay_Calculation():
    ReturnVal = CDollar(GetFloat(IA2210AnSp.Q3FedPay) * 1.5)

def Q3AnInc_Calculation():
    ReturnVal = CDollar(GetFloat(IA2210AnSp.Q3NetInc) * 1.5)

def Q3AnItmDed_Calculation():
    if GetBool(IAF1040.ItemCheck) == True:
        ReturnVal = CDollar(GetFloat(IA2210AnSp.Q3ItmDed) * 1.5)
    else:
        ReturnVal = 0

def Q3Balance_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2210AnSp.Q3TotTax) - GetCurrency(IA2210AnSp.Q3ExemCr) - GetCurrency(IA2210AnSp.Q3NonRefCr) - GetCurrency(IA2210AnSp.Q3RefCr))

def Q3BalDue_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2210AnSp.Q3PerTax) - GetCurrency(IA2210AnSp.Q3PQInst))

def Q3Deduct_Calculation():
    ReturnVal = MaxValue(GetCurrency(IA2210AnSp.Q3AnItmDed), GetCurrency(IA2210AnSp.Q3StndDed))

def Q3ExemCr_Calculation():
    ReturnVal = GetCurrency(IA2210AnSp.Q1ExemCr)

def Q3PerTax_Calculation():
    ReturnVal = CDollar(GetFloat(IA2210AnSp.Q3Balance) * 0.675)

def Q3PQInst_Calculation():
    ReturnVal = GetCurrency(IA2210AnSp.Q1AIInstall) + GetCurrency(IA2210AnSp.Q2AIInstall)

def Q3PQUnpay_Calculation():
    ReturnVal = GetCurrency(IA2210AnSp.Q2Unpay)

def Q3ReqPay_Calculation():
    ReturnVal = GetCurrency(IA2210Sp.Q3Install)

def Q3StndDed_Calculation():
    ReturnVal = GetCurrency(IA2210AnSp.Q1StndDed)

def Q3Tax_Calculation():
    Mid = Currency()

    MidInt = Long()

    TotTaxInc = Currency()
    # updated for 2018
    TotTaxInc = GetCurrency(IA2210AnSp.Q3TaxInc)
    if TotTaxInc > Decimal("95650"):
        Mid = TotTaxInc
    elif TotTaxInc > Decimal("150"):
        MidInt = CLng(( TotTaxInc - Decimal("1") )  / Decimal("50"))
        Mid = ( CCur(MidInt) * Decimal("50") )  + Decimal("25")
    else:
        Mid = Decimal("0")
    ReturnVal = Tax(Mid)

def Q3TaxInc_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2210AnSp.Q3AnInc) - GetCurrency(IA2210AnSp.Q3AnFedPay) - GetCurrency(IA2210AnSp.Q3Deduct))

def Q3TotPay_Calculation():
    ReturnVal = GetCurrency(IA2210AnSp.Q3ReqPay) + GetCurrency(IA2210AnSp.Q3PQUnpay)

def Q3TotTax_Calculation():
    ReturnVal = GetCurrency(IA2210AnSp.Q3Tax) + GetCurrency(IA2210AnSp.Q3OthTax)

def Q3Unpay_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2210AnSp.Q3TotPay) - GetCurrency(IA2210AnSp.Q3BalDue))

def Q4AIInstall_Calculation():
    ReturnVal = MinValue(GetCurrency(IA2210AnSp.Q4BalDue), GetCurrency(IA2210AnSp.Q4TotPay))

def Q4AnFedPay_Calculation():
    ReturnVal = GetCurrency(IA2210AnSp.Q4FedPay)

def Q4AnInc_Calculation():
    ReturnVal = GetCurrency(IA2210AnSp.Q4NetInc)

def Q4AnItmDed_Calculation():
    ReturnVal = GetCurrency(IA2210AnSp.Q4ItmDed)

def Q4Balance_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2210AnSp.Q4TotTax) - GetCurrency(IA2210AnSp.Q4ExemCr) - GetCurrency(IA2210AnSp.Q4NonRefCr) - GetCurrency(IA2210AnSp.Q4RefCr))

def Q4BalDue_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2210AnSp.Q4PerTax) - GetCurrency(IA2210AnSp.Q4PQInst))

def Q4Deduct_Calculation():
    ReturnVal = MaxValue(GetCurrency(IA2210AnSp.Q4AnItmDed), GetCurrency(IA2210AnSp.Q4StndDed))

def Q4ExemCr_Calculation():
    ReturnVal = GetCurrency(IA2210AnSp.Q1ExemCr)

def Q4FedPay_Calculation():
    ReturnVal = GetCurrency(IAF1040.BFedDed) - GetCurrency(IAF1040.BFedTax)

def Q4ItmDed_Calculation():
    if GetBool(IAF1040.ItemCheck) == True:
        ReturnVal = GetCurrency(IAF1040.BDedBox)
    else:
        ReturnVal = 0

def Q4NetInc_Calculation():
    ReturnVal = GetCurrency(IAF1040.BNet)

def Q4NonRefCr_Calculation():
    ReturnVal = GetCurrency(IAF1040.BTuit) + GetCurrency(IAF1040.BVolFireCr) + GetCurrency(IAF1040.BCrNon) + GetCurrency(IAF1040.BOutState) + GetCurrency(IAF1040.BOthIACr)

def Q4OthTax_Calculation():
    ReturnVal = GetCurrency(IAF1040.BLump) + GetCurrency(IAF1040.BIAMin)

def Q4PerTax_Calculation():
    ReturnVal = CDollar(GetFloat(IA2210AnSp.Q4Balance) * 0.9)

def Q4PQInst_Calculation():
    ReturnVal = GetCurrency(IA2210AnSp.Q1AIInstall) + GetCurrency(IA2210AnSp.Q2AIInstall) + GetCurrency(IA2210AnSp.Q3AIInstall)

def Q4PQUnpay_Calculation():
    ReturnVal = GetCurrency(IA2210AnSp.Q3Unpay)

def Q4RefCr_Calculation():
    ReturnVal = GetCurrency(IAF1040.BFuel) + GetCurrency(IAF1040.BChild) + GetCurrency(IAF1040.BIEIC) + GetCurrency(IAF1040.BOthRefCr)

def Q4ReqPay_Calculation():
    ReturnVal = GetCurrency(IA2210Sp.Q4Install)

def Q4StndDed_Calculation():
    ReturnVal = GetCurrency(IA2210AnSp.Q1StndDed)

def Q4Tax_Calculation():
    Mid = Currency()

    MidInt = Long()

    TotTaxInc = Currency()
    # updated for 2018
    TotTaxInc = GetCurrency(IA2210AnSp.Q4TaxInc)
    if TotTaxInc > Decimal("95650"):
        Mid = TotTaxInc
    elif TotTaxInc > Decimal("150"):
        MidInt = CLng(( TotTaxInc - Decimal("1") )  / Decimal("50"))
        Mid = ( CCur(MidInt) * Decimal("50") )  + Decimal("25")
    else:
        Mid = Decimal("0")
    ReturnVal = Tax(Mid)

def Q4TaxInc_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2210AnSp.Q4AnInc) - GetCurrency(IA2210AnSp.Q4AnFedPay) - GetCurrency(IA2210AnSp.Q4Deduct))

def Q4TotPay_Calculation():
    ReturnVal = GetCurrency(IA2210AnSp.Q4ReqPay) + GetCurrency(IA2210AnSp.Q4PQUnpay)

def Q4TotTax_Calculation():
    ReturnVal = GetCurrency(IA2210AnSp.Q4Tax) + GetCurrency(IA2210AnSp.Q4OthTax)

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SpouseSSN)

