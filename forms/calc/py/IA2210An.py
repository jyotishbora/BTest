from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def AskItmDed_Calculation():
    if GetBool(IAF1040.ItemCheck) == True:
        ReturnVal = 1
    elif GetCurrency(IA2210An.Q1ItmDed) != 0:
        ReturnVal = 1
    elif GetCurrency(IA2210An.Q2ItmDed) != 0:
        ReturnVal = 1
    elif GetCurrency(IA2210An.Q3ItmDed) != 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Description_Calculation():
    ReturnVal = GetString(IA2210An.Names)

def Names_Calculation():
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetString(IARequired.TPCombName)
    else:
        ReturnVal = GetString(IARequired.CombNames)

def Print_Calculation():
    if GetBool(IA2210.AnInc) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Q1AIInstall_Calculation():
    ReturnVal = MinValue(GetCurrency(IA2210An.Q1BalDue), GetCurrency(IA2210An.Q1TotPay))

def Q1AnFedPay_Calculation():
    ReturnVal = CDollar(GetFloat(IA2210An.Q1FedPay) * 4)

def Q1AnInc_Calculation():
    ReturnVal = CDollar(GetFloat(IA2210An.Q1NetInc) * 4)

def Q1AnItmDed_Calculation():
    if GetBool(IAF1040.ItemCheck) == True:
        ReturnVal = CDollar(GetFloat(IA2210An.Q1ItmDed) * 4)
    else:
        ReturnVal = 0

def Q1Balance_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2210An.Q1TotTax) - GetCurrency(IA2210An.Q1ExemCr) - GetCurrency(IA2210An.Q1NonRefCr) - GetCurrency(IA2210An.Q1RefCr))

def Q1BalDue_Calculation():
    ReturnVal = GetCurrency(IA2210An.Q1PerTax)

def Q1Deduct_Calculation():
    ReturnVal = MaxValue(GetCurrency(IA2210An.Q1AnItmDed), GetCurrency(IA2210An.Q1StndDed))

def Q1ExemCr_Calculation():
    ReturnVal = GetCurrency(IAF1040.AExemCr)

def Q1PerTax_Calculation():
    ReturnVal = CDollar(GetFloat(IA2210An.Q1Balance) * 0.225)

def Q1ReqPay_Calculation():
    ReturnVal = GetCurrency(IA2210.Q1Install)

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
    TotTaxInc = GetCurrency(IA2210An.Q1TaxInc)
    if TotTaxInc > Decimal("95650"):
        Mid = TotTaxInc
    elif TotTaxInc > Decimal("150"):
        MidInt = CLng(( TotTaxInc - Decimal("1") )  / Decimal("50"))
        Mid = ( CCur(MidInt) * Decimal("50") )  + Decimal("25")
    else:
        Mid = Decimal("0")
    ReturnVal = Tax(Mid)

def Q1TaxInc_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2210An.Q1AnInc) - GetCurrency(IA2210An.Q1AnFedPay) - GetCurrency(IA2210An.Q1Deduct))

def Q1TotPay_Calculation():
    ReturnVal = GetCurrency(IA2210An.Q1ReqPay)

def Q1TotTax_Calculation():
    ReturnVal = GetCurrency(IA2210An.Q1Tax) + GetCurrency(IA2210An.Q1OthTax)

def Q1Unpay_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2210An.Q1TotPay) - GetCurrency(IA2210An.Q1BalDue))

def Q2AIInstall_Calculation():
    ReturnVal = MinValue(GetCurrency(IA2210An.Q2BalDue), GetCurrency(IA2210An.Q2TotPay))

def Q2AnFedPay_Calculation():
    ReturnVal = CDollar(GetFloat(IA2210An.Q2FedPay) * 2.4)

def Q2AnInc_Calculation():
    ReturnVal = CDollar(GetFloat(IA2210An.Q2NetInc) * 2.4)

def Q2AnItmDed_Calculation():
    if GetBool(IAF1040.ItemCheck) == True:
        ReturnVal = CDollar(GetFloat(IA2210An.Q2ItmDed) * 2.4)
    else:
        ReturnVal = 0

def Q2Balance_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2210An.Q2TotTax) - GetCurrency(IA2210An.Q2ExemCr) - GetCurrency(IA2210An.Q2NonRefCr) - GetCurrency(IA2210An.Q2RefCr))

def Q2BalDue_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2210An.Q2PerTax) - GetCurrency(IA2210An.Q2PQInst))

def Q2Deduct_Calculation():
    ReturnVal = MaxValue(GetCurrency(IA2210An.Q2AnItmDed), GetCurrency(IA2210An.Q2StndDed))

def Q2ExemCr_Calculation():
    ReturnVal = GetCurrency(IA2210An.Q1ExemCr)

def Q2PerTax_Calculation():
    ReturnVal = CDollar(GetFloat(IA2210An.Q2Balance) * 0.45)

def Q2PQInst_Calculation():
    ReturnVal = GetCurrency(IA2210An.Q1AIInstall)

def Q2PQUnpay_Calculation():
    ReturnVal = GetCurrency(IA2210An.Q1Unpay)

def Q2ReqPay_Calculation():
    ReturnVal = GetCurrency(IA2210.Q2Install)

def Q2StndDed_Calculation():
    ReturnVal = GetCurrency(IA2210An.Q1StndDed)

def Q2Tax_Calculation():
    Mid = Currency()

    MidInt = Long()

    TotTaxInc = Currency()
    # updated for 2018
    TotTaxInc = GetCurrency(IA2210An.Q2TaxInc)
    if TotTaxInc > Decimal("95650"):
        Mid = TotTaxInc
    elif TotTaxInc > Decimal("150"):
        MidInt = CLng(( TotTaxInc - Decimal("1") )  / Decimal("50"))
        Mid = ( CCur(MidInt) * Decimal("50") )  + Decimal("25")
    else:
        Mid = Decimal("0")
    ReturnVal = Tax(Mid)

def Q2TaxInc_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2210An.Q2AnInc) - GetCurrency(IA2210An.Q2AnFedPay) - GetCurrency(IA2210An.Q2Deduct))

def Q2TotPay_Calculation():
    ReturnVal = GetCurrency(IA2210An.Q2ReqPay) + GetCurrency(IA2210An.Q2PQUnpay)

def Q2TotTax_Calculation():
    ReturnVal = GetCurrency(IA2210An.Q2Tax) + GetCurrency(IA2210An.Q2OthTax)

def Q2Unpay_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2210An.Q2TotPay) - GetCurrency(IA2210An.Q2BalDue))

def Q3AIInstall_Calculation():
    ReturnVal = MinValue(GetCurrency(IA2210An.Q3BalDue), GetCurrency(IA2210An.Q3TotPay))

def Q3AnFedPay_Calculation():
    ReturnVal = CDollar(GetFloat(IA2210An.Q3FedPay) * 1.5)

def Q3AnInc_Calculation():
    ReturnVal = CDollar(GetFloat(IA2210An.Q3NetInc) * 1.5)

def Q3AnItmDed_Calculation():
    if GetBool(IAF1040.ItemCheck) == True:
        ReturnVal = CDollar(GetFloat(IA2210An.Q3ItmDed) * 1.5)
    else:
        ReturnVal = 0

def Q3Balance_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2210An.Q3TotTax) - GetCurrency(IA2210An.Q3ExemCr) - GetCurrency(IA2210An.Q3NonRefCr) - GetCurrency(IA2210An.Q3RefCr))

def Q3BalDue_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2210An.Q3PerTax) - GetCurrency(IA2210An.Q3PQInst))

def Q3Deduct_Calculation():
    ReturnVal = MaxValue(GetCurrency(IA2210An.Q3AnItmDed), GetCurrency(IA2210An.Q3StndDed))

def Q3ExemCr_Calculation():
    ReturnVal = GetCurrency(IA2210An.Q1ExemCr)

def Q3PerTax_Calculation():
    ReturnVal = CDollar(GetFloat(IA2210An.Q3Balance) * 0.675)

def Q3PQInst_Calculation():
    ReturnVal = GetCurrency(IA2210An.Q1AIInstall) + GetCurrency(IA2210An.Q2AIInstall)

def Q3PQUnpay_Calculation():
    ReturnVal = GetCurrency(IA2210An.Q2Unpay)

def Q3ReqPay_Calculation():
    ReturnVal = GetCurrency(IA2210.Q3Install)

def Q3StndDed_Calculation():
    ReturnVal = GetCurrency(IA2210An.Q1StndDed)

def Q3Tax_Calculation():
    Mid = Currency()

    MidInt = Long()

    TotTaxInc = Currency()
    # updated for 2018
    TotTaxInc = GetCurrency(IA2210An.Q3TaxInc)
    if TotTaxInc > Decimal("95650"):
        Mid = TotTaxInc
    elif TotTaxInc > Decimal("150"):
        MidInt = CLng(( TotTaxInc - Decimal("1") )  / Decimal("50"))
        Mid = ( CCur(MidInt) * Decimal("50") )  + Decimal("25")
    else:
        Mid = Decimal("0")
    ReturnVal = Tax(Mid)

def Q3TaxInc_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2210An.Q3AnInc) - GetCurrency(IA2210An.Q3AnFedPay) - GetCurrency(IA2210An.Q3Deduct))

def Q3TotPay_Calculation():
    ReturnVal = GetCurrency(IA2210An.Q3ReqPay) + GetCurrency(IA2210An.Q3PQUnpay)

def Q3TotTax_Calculation():
    ReturnVal = GetCurrency(IA2210An.Q3Tax) + GetCurrency(IA2210An.Q3OthTax)

def Q3Unpay_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2210An.Q3TotPay) - GetCurrency(IA2210An.Q3BalDue))

def Q4AIInstall_Calculation():
    ReturnVal = MinValue(GetCurrency(IA2210An.Q4BalDue), GetCurrency(IA2210An.Q4TotPay))

def Q4AnFedPay_Calculation():
    ReturnVal = GetCurrency(IA2210An.Q4FedPay)

def Q4AnInc_Calculation():
    ReturnVal = GetCurrency(IA2210An.Q4NetInc)

def Q4AnItmDed_Calculation():
    ReturnVal = GetCurrency(IA2210An.Q4ItmDed)

def Q4Balance_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2210An.Q4TotTax) - GetCurrency(IA2210An.Q4ExemCr) - GetCurrency(IA2210An.Q4NonRefCr) - GetCurrency(IA2210An.Q4RefCr))

def Q4BalDue_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2210An.Q4PerTax) - GetCurrency(IA2210An.Q4PQInst))

def Q4Deduct_Calculation():
    ReturnVal = MaxValue(GetCurrency(IA2210An.Q4AnItmDed), GetCurrency(IA2210An.Q4StndDed))

def Q4ExemCr_Calculation():
    ReturnVal = GetCurrency(IA2210An.Q1ExemCr)

def Q4FedPay_Calculation():
    ReturnVal = GetCurrency(IAF1040.AFedDed) - GetCurrency(IAF1040.AFedTax)

def Q4ItmDed_Calculation():
    if GetBool(IAF1040.ItemCheck) == True:
        ReturnVal = GetCurrency(IAF1040.ADedBox)
    else:
        ReturnVal = 0

def Q4NetInc_Calculation():
    ReturnVal = GetCurrency(IAF1040.ANet)

def Q4NonRefCr_Calculation():
    ReturnVal = GetCurrency(IAF1040.ATuit) + GetCurrency(IAF1040.AVolFireCr) + GetCurrency(IAF1040.ACrNon) + GetCurrency(IAF1040.AOutState) + GetCurrency(IAF1040.AOthIACr)

def Q4OthTax_Calculation():
    ReturnVal = GetCurrency(IAF1040.ALump) + GetCurrency(IAF1040.AIAMin)

def Q4PerTax_Calculation():
    ReturnVal = CDollar(GetFloat(IA2210An.Q4Balance) * 0.9)

def Q4PQInst_Calculation():
    ReturnVal = GetCurrency(IA2210An.Q1AIInstall) + GetCurrency(IA2210An.Q2AIInstall) + GetCurrency(IA2210An.Q3AIInstall)

def Q4PQUnpay_Calculation():
    ReturnVal = GetCurrency(IA2210An.Q3Unpay)

def Q4RefCr_Calculation():
    ReturnVal = GetCurrency(IAF1040.AFuel) + GetCurrency(IAF1040.AChild) + GetCurrency(IAF1040.AIEIC) + GetCurrency(IAF1040.AOthRefCr)

def Q4ReqPay_Calculation():
    ReturnVal = GetCurrency(IA2210.Q4Install)

def Q4StndDed_Calculation():
    ReturnVal = GetCurrency(IA2210An.Q1StndDed)

def Q4Tax_Calculation():
    Mid = Currency()

    MidInt = Long()

    TotTaxInc = Currency()
    # updated for 2018
    TotTaxInc = GetCurrency(IA2210An.Q4TaxInc)
    if TotTaxInc > Decimal("95650"):
        Mid = TotTaxInc
    elif TotTaxInc > Decimal("150"):
        MidInt = CLng(( TotTaxInc - Decimal("1") )  / Decimal("50"))
        Mid = ( CCur(MidInt) * Decimal("50") )  + Decimal("25")
    else:
        Mid = Decimal("0")
    ReturnVal = Tax(Mid)

def Q4TaxInc_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2210An.Q4AnInc) - GetCurrency(IA2210An.Q4AnFedPay) - GetCurrency(IA2210An.Q4Deduct))

def Q4TotPay_Calculation():
    ReturnVal = GetCurrency(IA2210An.Q4ReqPay) + GetCurrency(IA2210An.Q4PQUnpay)

def Q4TotTax_Calculation():
    ReturnVal = GetCurrency(IA2210An.Q4Tax) + GetCurrency(IA2210An.Q4OthTax)

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

