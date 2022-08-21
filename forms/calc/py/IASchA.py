from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def AddMilesDed_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IASchA.TotMilesDed) - GetCurrency(IASchA.SchAMilesDed))

def AdoptSub_Calculation():
    ReturnVal = MaxValue(0, CDollar(GetFloat(IAChildCredit.TotNI) * 0.03))

def AGI_Calculation():
    if GetCurrency(IASchA.MedExp) == 0:
        ReturnVal = 0
    else:
        ReturnVal = MaxValue(0, CDollar(GetFloat(IASchA.IAAGI) * 0.1))

def Alert10_Calculation():
    FedMedical = Currency()
    if GetBool(USWResidency.F1040NR) == False:
        FedMedical = GetCurrency(USSchA.MedExp)
    else:
        FedMedical = 0
    if GetCurrency(IASchA.MedExp) >= FedMedical and GetCurrency(IASchA.MedExp) > 0:
        if GetCurrency(IAF1040.BHealth) > 0 or GetCurrency(IAF1040.AHealth) > 0:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def Alert15_Calculation():
    if GetBool(IAF1040.ItemCheck) == True and GetCurrency(IASchA.Mort) > 0:
        if GetCurrency(USD1098.MortPrem) > Decimal("1000000"):
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def Alert20_Calculation():
    #add net nonconformity items? Next year could them factor in. If user imports we should import correct Iowa amounts, if we continue to also pull the federal carryover amounts should still bring up this alert
    #alert is saying to adjust carryover if had any nonconforming items last year, leave as only depr since othinc ws is only current year items, possibly factor in next year (either imported NC items/bonus and/or current year NC items)
    if GetCurrency(IASchA.Over) != 0 and GetCurrency(IAWOthInc.TotBonus) != 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert22_Calculation():
    TotCont = Currency()
    TotCont = GetCurrency(IAWContLimit.CY50Lim) + GetCurrency(IAWContLimit.CY30Lim) + GetCurrency(IAWContLimit.CY30LimCG) + GetCurrency(IAWContLimit.CY20Lim) + GetCurrency(IAWContLimit.CYNoLim)
    if TotCont > GetCurrency(IAWContLimit.CYTot):
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert24_Calculation():
    if GetCurrency(IAWContLimit.PY50Lim) < 0:
        ReturnVal = 1
    elif GetCurrency(IAWContLimit.PY30Lim) < 0:
        ReturnVal = 1
    elif GetCurrency(IAWContLimit.PY30LimCG) < 0:
        ReturnVal = 1
    elif GetCurrency(IAWContLimit.PY20Lim) < 0:
        ReturnVal = 1
    elif GetCurrency(IAWContLimit.PYNoLim) < 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert26_Calculation():
    if GetCurrency(IAWContLimit.NYTot) != 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert27_Calculation():
    if GetCurrency(IAWContLimit.CYQualLim) != 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert28_Calculation():
    if GetCurrency(IAWContLimit.CYQualLim) > GetCurrency(IASchA.Contrib):
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert30_Calculation():
    ReturnVal = 0

def Alert40_Calculation():
    if GetBool(IAF1040.ItemCheck) == True and GetCurrency(IASchA.OthMisc) > 0:
        if GetCurrency(IASchA.IAAdjOthMisc) != 0 and Trim(GetString(IASchA.IAAdjOthMiscDesc)) == '':
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def Alert50_Calculation():
    count = Variant()

    Iter = Integer()
    count = 0
    Iter = 0
    while Iter < 5:
        if GetCurrency(IASchA.DisableAmt(Iter)) > 0 and Trim(GetString(IASchA.DisableExp(Iter))) == '':
            count = count + 1
        Iter = Iter + 1
    if GetBool(IAF1040.ItemCheck) == True and count > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert60_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Integer()

    count2 = Integer()

    Lim2 = Integer()

    Total2 = Integer()
    Lim = GetAllCopies(IA177)
    count = 1
    Total = 0
    while count <= Lim:
        if GetCurrency(IA177.CYAdoptionTaxCr, count) > 0 and GetBool(IA177.Taxpayer, count) == True:
            Total = Total + 1
        else:
            Total = Total
        count = count + 1
    Lim2 = GetAllCopies(IA177)
    count2 = 1
    Total2 = 0
    while count2 <= Lim2:
        if GetCurrency(IA177.CYAdoptionTaxCr, count) > 0 and GetBool(IA177.Spouse, count2) == True:
            Total2 = Total2 + 1
        else:
            Total2 = Total2
        count2 = count2 + 1
    if GetCurrency(IASchA.TotAdoptAmt) > 0:
        if Total > 0:
            ReturnVal = 1
        elif Total2 > 0 and GetBool(IAF1040.CombMFS) == True:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def Alert70_Calculation():
    count = Variant()

    Iter = Integer()
    count = 0
    Iter = 0
    while Iter < 5:
        if GetCurrency(IASchA.AdoptAmt(Iter)) > 0 and Trim(GetString(IASchA.AdoptExp(Iter))) == '':
            count = count + 1
        Iter = Iter + 1
    if GetBool(IAF1040.ItemCheck) == True and GetCurrency(IASchA.AllowAdopt) > 0 and count > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert80_Calculation():
    if GetCurrency(IAWSchAPrint.GamblingLoss) >  ( GetCurrency(IAF1040.BGamble) + GetCurrency(IAF1040.AGamble) ) :
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert85_Calculation():
    if GetBool(IAF1040.ItemCheck) == True:
        if GetCurrency(IASchA.OthTax) != 0 and Trim(GetString(IASchA.OthList)) == '':
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def AllowAdopt_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IASchA.TotAdoptAmt) - GetCurrency(IASchA.AdoptSub))

def AllowExp_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IASchA.Expense) - GetCurrency(IASchA.Mult))

def CombOthExpDesc_Calculation():
    ReturnVal = GetString(IASchA.OthExpDesc(0)) + ' ' + GetString(IASchA.OthExpDesc(1)) + ' ' + GetString(IASchA.OthExpDesc(2)) + ' ' + GetString(IASchA.OthExpDesc(3)) + ' ' + GetString(IASchA.OthExpDesc(4)) + ' ' + GetString(IASchA.OthExpDesc(5)) + ' ' + GetString(IASchA.OthExpDesc(6)) + ' ' + GetString(IASchA.OthExpDesc(7)) + ' ' + GetString(IASchA.OthExpDesc(8)) + ' ' + GetString(IASchA.OthExpDesc(9)) + ' ' + GetString(IASchA.OthExpDesc(10)) + ' ' + GetString(IASchA.OthExpDesc(11)) + ' ' + GetString(IASchA.OthExpDesc(12)) + ' ' + GetString(IASchA.OthExpDesc(13)) + ' ' + GetString(IASchA.OthExpDesc(14)) + ' ' + GetString(IASchA.OthExpDesc(15)) + ' ' + GetString(IASchA.OthExpDesc(16)) + ' ' + GetString(IASchA.OthExpDesc(17)) + ' ' + GetString(IASchA.OthExpDesc(18)) + ' ' + GetString(IASchA.OthExpDesc(19)) + ' ' + GetString(IASchA.OthExpDesc(20)) + ' ' + GetString(IASchA.OthExpDesc(21)) + ' ' + GetString(IASchA.OthExpDesc(22)) + ' ' + GetString(IASchA.OthExpDesc(23)) + ' ' + GetString(IASchA.OthExpDesc(24))

def CombOthMiscDesc_Calculation():
    ReturnVal = GetString(IASchA.OthMiscDesc(0)) + ' ' + GetString(IASchA.OthMiscDesc(1)) + ' ' + GetString(IASchA.OthMiscDesc(2)) + ' ' + GetString(IASchA.OthMiscDesc(3)) + ' ' + GetString(IASchA.OthMiscDesc(4)) + ' ' + GetString(IASchA.OthMiscDesc(5)) + ' ' + GetString(IASchA.OthMiscDesc(6)) + ' ' + GetString(IASchA.OthMiscDesc(7)) + ' ' + GetString(IASchA.OthMiscDesc(8)) + ' ' + GetString(IASchA.OthMiscDesc(9))

def Contrib_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IASchA.TotContrib) - GetCurrency(IASchA.IAAdjContrib))

def Description_Calculation():
    ReturnVal = CStr(GetCurrency(IASchA.Item)) + ' Itemized Deductions'

def Exist_Calculation():
    ReturnVal = 1

def Expense_Calculation():
    ReturnVal = GetCurrency(IASchA.Unreimb) + GetCurrency(IASchA.TaxFee) + GetCurrency(IASchA.OthExp)

def GenSales_Calculation():
    #Iowa expanded instructions can only claim gen sales tax if itemize federally and elect to claim gen sales on fed. Leave calced.
    if GetBool(USWRec.ItmDdn) == True and GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetBool(USSchA.GenSales)
    else:
        ReturnVal = 0

def Gifts_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IASchA.TotNonCash) - GetCurrency(IASchA.IAAdjNonCash))

def Header1_Calculation():
    ReturnVal = 'IA 1040 Schedule A - Itemized Deductions - Line 21 Attachment'

def IAAGI_Calculation():
    ReturnVal = GetCurrency(IARequired.IAAGI)

def IATax_Calculation():
    IAWHEst = Currency()

    OthIAWH = Currency()
    IAWHEst = GetCurrency(IARequired.TotIAW2WH) + GetCurrency(IARequired.TotW2GWH) + GetCurrency(IARequired.Tot1042S) + GetCurrency(IARequired.TotCapGainWH) + GetCurrency(IARequired.TotDivWH) + GetCurrency(IARequired.TotUnemWH) + GetCurrency(IARequired.TotIntWH) + GetCurrency(IARequired.TotKWH) + GetCurrency(IARequired.TotMiscWH) + GetCurrency(IARequired.TotOIDWH) + GetCurrency(IARequired.Tot1099rWH) + GetCurrency(IARequired.TotOthIncWH) + GetCurrency(IARequired.TotCyLocEst) + GetCurrency(IARequired.TotCYIAEst)
    if GetBool(USWResidency.F1040NR) == False:
        OthIAWH = GetCurrency(USSchA.StateWH3) + GetCurrency(USSchA.StateWH4) + GetCurrency(USSchA.StateWH5)
    else:
        OthIAWH = GetCurrency(USSchANR.StateWH3) + GetCurrency(USSchANR.StateWH4) + GetCurrency(USSchANR.StateWH5)
    if GetBool(IAF126.TpPYNR) == True or GetBool(IAF126.SpPYNR) == True:
        ReturnVal = IAWHEst
    else:
        ReturnVal = MinValue(GetCurrency(IASchA.TotStTax), IAWHEst + OthIAWH)

def Income_Calculation():
    if GetBool(IASchA.GenSales) == True:
        ReturnVal = 0
    else:
        ReturnVal = 1

def Invest_Calculation():
    ReturnVal = GetCurrency(USSchA.InvInt)

def Item_Calculation():
    ReturnVal = GetCurrency(IASchA.TotDeductions) + GetCurrency(IASchA.TotOthDed)

def ListExp_Calculation():
    if GetCurrency(IASchA.OthExp) != 0:
        ReturnVal = GetString(IASchA.Ln21SeeAtt)
    else:
        ReturnVal = ''

def ListMisc_Calculation():
    if GetCurrency(IASchA.OthMisc) != 0:
        ReturnVal = GetString(IASchA.OthMiscDesc(0)) + ' ' + GetString(IASchA.OthMiscDesc(1)) + ' ' + GetString(IASchA.OthMiscDesc(2)) + ' ' + GetString(IASchA.OthMiscDesc(3)) + ' ' + GetString(IASchA.OthMiscDesc(4))
    else:
        ReturnVal = ''

def Ln21SeeAtt_Calculation():
    if GetCurrency(IASchA.OthLn21Amt(1)) != 0:
        ReturnVal = 'See Attached'
    else:
        ReturnVal = GetString(IASchA.OthExpDesc(0))

def MedDed_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = MaxValue(0, GetCurrency(IASchA.MedExp) - GetCurrency(IASchA.AGI))
    else:
        ReturnVal = 0

def MedExp_Calculation():
    HealthInsDed = Currency()
    #removed the prior year excess advanced PTC from the HealthInsDed since should not offset current year medical expenses
    #adjusted medical expense calc for PTC adjustment if claiming on IA 1040 line 18 (if not claiming on line 18 should follow federal treatment of PTC, if on 18 PTC handled on IA 1040)
    #change was made based on US 433238 see also CSS ticket 8605571
    HealthInsDed = GetCurrency(IAWHealth.TPInsPrem) + GetCurrency(IAWHealth.TPMedicare) + GetCurrency(IAWHealth.TPLTC) + GetCurrency(IAWHealth.SPInsPrem) + GetCurrency(IAWHealth.SPMedicare) + GetCurrency(IAWHealth.SPLTC)
    if GetBool(USWResidency.F1040NR) == False:
        if ( GetCurrency(IAWHealth.TPInsPrem) + GetCurrency(IAWHealth.SPInsPrem) )  == 0:
            ReturnVal = MaxValue(0, GetCurrency(USSchA.MedExp) - HealthInsDed)
        else:
            ReturnVal = MaxValue(0, MaxValue(0, GetCurrency(USSchA.MedExp) + GetCurrency(USWMedicalWS.PTCAdj)) - HealthInsDed)
    else:
        ReturnVal = 0

def Mort_Calculation():
    ReturnVal = GetCurrency(IASchA.MortFed) + GetCurrency(IASchA.MortAdj)

def MortAdj_Calculation():
    if GetBool(USWResidency.F1040NR) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(USD1098.StateAdj)

def MortFed_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USSchA.MortInt) + GetCurrency(USF8396.CrInt)
    else:
        ReturnVal = 0

def MortNot_Calculation():
    ReturnVal = GetCurrency(USSchA.Sfm)

def MtgePrem_Calculation():
    ReturnVal = GetCurrency(USSchA.MtgePrem)

def Mult_Calculation():
    if GetCurrency(IASchA.Expense) > 0:
        ReturnVal = MaxValue(0, CDollar(GetFloat(IASchA.IAAGI) * 0.02))
    else:
        ReturnVal = 0

def Names_Calculation():
    ReturnVal = GetString(IARequired.CombNames)

def OthExp_Calculation():
    ReturnVal = GetCurrency(IAWSchAPrint.TotExp)

def OthExpDesc_Calculation(Index):
    count = Integer()

    Hold = String()
    count = 0
    Hold = ''
    if GetCurrency(IAWSchAPrint.Legal) != 0:
        if Index == count:
            Hold = 'Legal Fees - Taxable Income'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.OthLegal) != 0:
        if Index == count:
            Hold = 'Other Legal Fees'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.Clerical) != 0:
        if Index == count:
            Hold = 'Clerical Help'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.Custodial) != 0:
        if Index == count:
            Hold = 'Custodial/Investment Fees'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.Invest) != 0:
        if Index == count:
            Hold = 'Investment Expenses Form 1099s'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.InsolventLoss) != 0:
        if Index == count:
            Hold = 'Insolvent Losses'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.CasualtyLoss) != 0:
        if Index == count:
            Hold = 'Form 4684'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.Appraisal) != 0:
        if Index == count:
            Hold = 'Appraisal Fees'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.DeprTot) != 0:
        if Index == count:
            Hold = 'Depreciation Computer'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.Amort) != 0:
        if Index == count:
            Hold = 'Amortization'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.ExcessDed) != 0:
        if Index == count:
            Hold = 'Excess K-1 Ded'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.Fees) != 0:
        if Index == count:
            Hold = 'Fees to Collect'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.Hobby) != 0 and GetBool(USWResidency.F1040NR) == False:
        if Index == count:
            Hold = 'Hobby Expenses'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.Indirect) != 0:
        if Index == count:
            Hold = 'Indirect Pass-through'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.REMIC) != 0:
        if Index == count:
            Hold = 'REMIC'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.IRALoss) != 0:
        if Index == count:
            Hold = 'IRA Loss'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.RepayInc) != 0:
        if Index == count:
            Hold = 'Income Repay'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.RepaySSB) != 0 and GetBool(USWResidency.F1040NR) == False:
        if Index == count:
            Hold = 'SSB Repay'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.SafeBox) != 0:
        if Index == count:
            Hold = 'Safe Deposit'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.ServiceCharge) != 0:
        if Index == count:
            Hold = 'Service Charges Div'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.TaxAdvice) != 0:
        if Index == count:
            Hold = 'Tax Advice'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.Trustee) != 0:
        if Index == count:
            Hold = 'Trustee\'s Fees IRA'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.CreditFees) != 0:
        if Index == count:
            Hold = 'Convenience Fee'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.OthExp) != 0:
        if Index == count:
            Hold = GetString(IAWSchAPrint.OtherText)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.OthExp2) != 0:
        if Index == count:
            Hold = GetString(IAWSchAPrint.OtherText2)
            count = 99
        else:
            count = count + 1
    ReturnVal = Hold

def OthList_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetString(USSchA.OtherTaxType)
    else:
        ReturnVal = ''

def OthLn21Amt_Calculation(Index):
    count = Integer()

    Hold = Currency()
    count = 0
    Hold = 0
    if GetCurrency(IAWSchAPrint.Legal) != 0:
        if Index == count:
            Hold = GetCurrency(IAWSchAPrint.Legal)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.OthLegal) != 0:
        if Index == count:
            Hold = GetCurrency(IAWSchAPrint.OthLegal)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.Clerical) != 0:
        if Index == count:
            Hold = GetCurrency(IAWSchAPrint.Clerical)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.Custodial) != 0:
        if Index == count:
            Hold = GetCurrency(IAWSchAPrint.Custodial)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.Invest) != 0:
        if Index == count:
            Hold = GetCurrency(IAWSchAPrint.Invest)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.InsolventLoss) != 0:
        if Index == count:
            Hold = GetCurrency(IAWSchAPrint.InsolventLoss)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.CasualtyLoss) != 0:
        if Index == count:
            Hold = GetCurrency(IAWSchAPrint.CasualtyLoss)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.Appraisal) != 0:
        if Index == count:
            Hold = GetCurrency(IAWSchAPrint.Appraisal)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.DeprTot) != 0:
        if Index == count:
            Hold = GetCurrency(IAWSchAPrint.DeprTot)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.Amort) != 0:
        if Index == count:
            Hold = GetCurrency(IAWSchAPrint.Amort)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.ExcessDed) != 0:
        if Index == count:
            Hold = GetCurrency(IAWSchAPrint.ExcessDed)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.Fees) != 0:
        if Index == count:
            Hold = GetCurrency(IAWSchAPrint.Fees)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.Hobby) != 0 and GetBool(USWResidency.F1040NR) == False:
        if Index == count:
            Hold = GetCurrency(IAWSchAPrint.Hobby)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.Indirect) != 0:
        if Index == count:
            Hold = GetCurrency(IAWSchAPrint.Indirect)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.REMIC) != 0:
        if Index == count:
            Hold = GetCurrency(IAWSchAPrint.REMIC)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.IRALoss) != 0:
        if Index == count:
            Hold = GetCurrency(IAWSchAPrint.IRALoss)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.RepayInc) != 0:
        if Index == count:
            Hold = GetCurrency(IAWSchAPrint.RepayInc)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.RepaySSB) != 0 and GetBool(USWResidency.F1040NR) == False:
        if Index == count:
            Hold = GetCurrency(IAWSchAPrint.RepaySSB)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.SafeBox) != 0:
        if Index == count:
            Hold = GetCurrency(IAWSchAPrint.SafeBox)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.ServiceCharge) != 0:
        if Index == count:
            Hold = GetCurrency(IAWSchAPrint.ServiceCharge)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.TaxAdvice) != 0:
        if Index == count:
            Hold = GetCurrency(IAWSchAPrint.TaxAdvice)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.Trustee) != 0:
        if Index == count:
            Hold = GetCurrency(IAWSchAPrint.Trustee)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.CreditFees) != 0:
        if Index == count:
            Hold = GetCurrency(IAWSchAPrint.CreditFees)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.OthExp) != 0:
        if Index == count:
            Hold = GetCurrency(IAWSchAPrint.OthExp)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.OthExp2) != 0:
        if Index == count:
            Hold = GetCurrency(IAWSchAPrint.OthExp2)
            count = 99
        else:
            count = count + 1
    ReturnVal = Hold

def OthMisc_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IASchA.TotOthMisc) + GetCurrency(IASchA.IAAdjOthMisc))

def OthMiscDesc_Calculation(Index):
    count = Integer()

    Hold = String()
    count = 0
    Hold = ''
    if GetCurrency(IAWSchAPrint.Form4684) != 0:
        if Index == count:
            Hold = 'Casualty and theft loss'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.GamblingLoss) != 0 and GetBool(USWResidency.F1040NR) == False:
        if Index == count:
            Hold = 'Gambling losses'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.K1DedPort) != 0:
        if Index == count:
            Hold = 'Schedule K-1'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.ImpWrkExp) != 0:
        if Index == count:
            Hold = 'Impairment-related work expenses'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.TotEstK1) != 0 and GetBool(USWResidency.F1040NR) == False:
        if Index == count:
            Hold = 'Federal estate tax'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.Repay) != 0:
        if Index == count:
            Hold = 'Claim repayments'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.Bond) != 0 and GetBool(USWResidency.F1040NR) == False:
        if Index == count:
            Hold = 'Amortizable bond premiums'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.Pension) != 0:
        if Index == count:
            Hold = 'Unrecovered pension investments'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWSchAPrint.Debt) != 0:
        if Index == count:
            Hold = 'Ordinary loss'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IASchA.IAAdjOthMisc) != 0:
        if Index == count:
            Hold = GetString(IASchA.IAAdjOthMiscDesc)
            count = 99
        else:
            count = count + 1
    ReturnVal = Hold

def OthTax_Calculation():
    #review to default calc - fed not allowing foreign taxes paid.
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USSchA.OtherTax)
    else:
        ReturnVal = 0

def Over_Calculation():
    ReturnVal = GetCurrency(IAWContLimit.PYTot)
    #If GetBool(USWResidency.F1040NR) = False Then
    #    ReturnVal = GetCurrency(USSchA.Carry)
    #Else
    #    ReturnVal = GetCurrency(USSchANR.Carry)
    #End If

def Perc_Calculation():
    TopLim = Double()
    if GetCurrency(IASchA.YouNet) < 0 and GetCurrency(IASchA.SpNet) < 0:
        if GetCurrency(IASchA.YouNet) < GetCurrency(IASchA.SpNet):
            ReturnVal = 0
        else:
            ReturnVal = 1
    elif GetCurrency(IASchA.YouNet) < 0:
        ReturnVal = 0
    elif GetCurrency(IASchA.YouNet) > 0 and GetCurrency(IASchA.TotNet) <= 0:
        ReturnVal = 1
    elif GetCurrency(IASchA.TotNet) == 0:
        ReturnVal = 0
    else:
        TopLim = MinValue(1, Round(GetFloat(IASchA.YouNet) / GetFloat(IASchA.TotNet), 3))
        ReturnVal = MaxValue(0, TopLim)

def PrintSchA_Calculation():
    if GetBool(IARequired.LowInc) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetNumber(IAF1040.ItemCheck)

def PrLn21SeeAtt_Calculation():
    if GetCurrency(IASchA.OthLn21Amt(1)) != 0 and GetNumber(IASchA.PrintSchA) == 1:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Prop_Calculation():
    ReturnVal = GetCurrency(USSchA.PerPropTax)

def PtsNot_Calculation():
    ReturnVal = GetCurrency(USSchA.Points)

def RealEst_Calculation():
    ReturnVal = GetCurrency(USSchA.RealTax)

def SalesTax_Calculation():
    ReturnVal = GetCurrency(USSchA.SalesTax)

def SchAMilesDed_Calculation():
    Con1 = Currency()
    #per fed, no change for 2018 remains at 14 cents
    if GetBool(USWResidency.F1040NR) == False:
        Con1 = CDollar(GetFloat(USSchA.ConMiles) * 14)
    else:
        Con1 = CDollar(GetFloat(USSchANR.ConMiles) * 14)
    ReturnVal = Con1

def SchoolTax_Calculation():
    if GetBool(IAF1040.MFJ) == True or GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetCurrency(USZIA1040.IAPYSurtaxA) + GetCurrency(USZIA1040.IAPYSurtaxB)
    else:
        ReturnVal = GetCurrency(USZIA1040.IAPYSurtaxA)

def SpNet_Calculation():
    if GetBool(IAF1040.CombMFS) == True or GetBool(IAF1040.MFS) == True:
        ReturnVal = GetCurrency(IAF1040.BNet)
    else:
        ReturnVal = 0

def SpPro_Calculation():
    if GetBool(IAF1040.CombMFS) == True or GetBool(IAF1040.MFS) == True:
        ReturnVal = MaxValue(0, GetCurrency(IASchA.Item) - GetCurrency(IASchA.YouPC))
    else:
        ReturnVal = 0

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

def StTax_Calculation():
    if GetBool(IASchA.GenSales) == True:
        ReturnVal = GetCurrency(IASchA.SalesTax)
    else:
        ReturnVal = GetCurrency(IASchA.TotIncTax)

def TaxFee_Calculation():
    ReturnVal = 0
    #If GetBool(USWResidency.F1040NR) = False Then
    #    ReturnVal = GetCurrency(USSchA.TaxPrep)
    #Else
    #    ReturnVal = GetCurrency(USSchANR.TaxPrep)
    #End If

def TaxPd_Calculation():
    ReturnVal = GetCurrency(IASchA.StTax) + GetCurrency(IASchA.RealEst) + GetCurrency(IASchA.Prop) + GetCurrency(IASchA.OthTax)

def Theft_Calculation():
    ReturnVal = GetCurrency(IA4684.SctATot)

def TotAdoptAmt_Calculation():
    ReturnVal = GetCurrency(IASchA.AdoptAmt(0)) + GetCurrency(IASchA.AdoptAmt(1)) + GetCurrency(IASchA.AdoptAmt(2)) + GetCurrency(IASchA.AdoptAmt(3)) + GetCurrency(IASchA.AdoptAmt(4))

def TotContrib_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USSchA.Cash)
    else:
        ReturnVal = GetCurrency(USSchANR.Cash)

def TotDeductions_Calculation():
    Limit = Currency()
    # updated for 2018 - RJ
    if FedFS() == 1:
        Limit = Decimal("266700")
    elif FedFS() == 3:
        Limit = Decimal("160000")
    elif FedFS() == 4:
        Limit = Decimal("293350")
    else:
        Limit = Decimal("320000")
    if GetCurrency(IASchA.IAAGI) > Limit:
        ReturnVal = GetCurrency(IAWItmDed.LimitDed)
    else:
        ReturnVal = GetCurrency(IASchA.OthMisc) + GetCurrency(IASchA.AllowExp) + GetCurrency(IASchA.Theft) + GetCurrency(IASchA.TotGifts) + GetCurrency(IASchA.TotInt) + GetCurrency(IASchA.TaxPd) + GetCurrency(IASchA.MedDed)

def TotDisableAmt_Calculation():
    TotDisable = Currency()
    TotDisable = GetCurrency(IASchA.DisableAmt(0)) + GetCurrency(IASchA.DisableAmt(1)) + GetCurrency(IASchA.DisableAmt(2)) + GetCurrency(IASchA.DisableAmt(3)) + GetCurrency(IASchA.DisableAmt(4))
    ReturnVal = MinValue(Decimal("5000"), TotDisable)

def TotGifts_Calculation():
    ReturnVal = GetCurrency(IAWContLimit.CYTotAfter)

def TotIncTax_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IASchA.TotStTax) + GetCurrency(IASchA.SchoolTax) - GetCurrency(IASchA.IATax))

def TotInt_Calculation():
    ReturnVal = GetCurrency(IASchA.Mort) + GetCurrency(IASchA.MortNot) + GetCurrency(IASchA.PtsNot) + GetCurrency(IASchA.Invest)

def TotMilesDed_Calculation():
    Con1 = Currency()
    if GetBool(USWResidency.F1040NR) == False:
        Con1 = CDollar(GetFloat(USSchA.ConMiles) * 39)
    else:
        Con1 = CDollar(GetFloat(USSchANR.ConMiles) * 39)
    ReturnVal = Con1

def TotNet_Calculation():
    ReturnVal = GetCurrency(IASchA.SpNet) + GetCurrency(IASchA.YouNet)

def TotNonCash_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USSchA.NonCash)
    else:
        ReturnVal = GetCurrency(USSchANR.NonCash)

def TotOthDed_Calculation():
    ReturnVal = GetCurrency(IASchA.TotDisableAmt) + GetCurrency(IASchA.AllowAdopt) + GetCurrency(IASchA.AddMilesDed)

def TotOthMisc_Calculation():
    ReturnVal = GetCurrency(IAWSchAPrint.TotOthDed)

def TotStTax_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = MaxValue(0, GetCurrency(USSchA.StateWH1) + GetCurrency(USSchA.StateWH2) + GetCurrency(USSchA.LocalWH) + GetCurrency(USSchA.StateWH3) + GetCurrency(USSchA.StateWH4) + GetCurrency(USSchA.StateWH5) - GetCurrency(USSchA.WHOff))
    else:
        ReturnVal = MaxValue(0, GetCurrency(USSchANR.StateWH1) + GetCurrency(USSchANR.StateWH2) + GetCurrency(USSchANR.LocalWH) + GetCurrency(USSchANR.StateWH3) + GetCurrency(USSchANR.StateWH4) + GetCurrency(USSchANR.StateWH5) - GetCurrency(USSchANR.WHOff))

def Unreimb_Calculation():
    ReturnVal = GetCurrency(IAWSchAPrint.TotOtherExp)

def YouNet_Calculation():
    if GetBool(IAF1040.CombMFS) == True or GetBool(IAF1040.MFS) == True:
        ReturnVal = GetCurrency(IAF1040.ANet)
    else:
        ReturnVal = 0

def YouPC_Calculation():
    ReturnVal = CDollar(GetFloat(IASchA.Perc) * GetFloat(IASchA.Item))

