from forms.out import IACHILDCREDIT
from forms.out import IAF1040
from forms.out import IAF126
from forms.out import IAREQUIRED
from forms.out import IASCHA
from forms.out import IAWCONTLIMIT
from forms.out import IAWHEALTH
from forms.out import IAWITMDED
from forms.out import IAWOTHINC
from forms.out import IAWSCHAPRINT
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def AddMilesDed_Calculation():
    return max_value(0, get_currency(IASCHA.TotMilesDed) - get_currency(IASCHA.SchAMilesDed))

def AdoptSub_Calculation():
    return max_value(0, c_dollar(get_float(IACHILDCREDIT.TotNI) * 0.03))

def AGI_Calculation():
    if get_currency(IASCHA.MedExp) == 0:
        return 0
    else:
        return max_value(0, c_dollar(get_float(IASCHA.IAAGI) * 0.1))

def Alert10_Calculation():
    FedMedical = Currency()
    if get_bool(USWResidency.F1040NR) == False:
        FedMedical = get_currency(USSchA.MedExp)
    else:
        FedMedical = 0
    if get_currency(IASCHA.MedExp) >= FedMedical and get_currency(IASCHA.MedExp) > 0:
        if get_currency(IAF1040.BHealth) > 0 or get_currency(IAF1040.AHealth) > 0:
            return 1
        else:
            return 0
    else:
        return 0

def Alert15_Calculation():
    if get_bool(IAF1040.ItemCheck) == True and get_currency(IASCHA.Mort) > 0:
        if get_currency(USD1098.MortPrem) > Decimal("1000000"):
            return 1
        else:
            return 0
    else:
        return 0

def Alert20_Calculation():
    #add net nonconformity items? Next year could them factor in. If user imports we should import correct Iowa amounts, if we continue to also pull the federal carryover amounts should still bring up this alert
    #alert is saying to adjust carryover if had any nonconforming items last year, leave as only depr since othinc ws is only current year items, possibly factor in next year (either imported NC items/bonus and/or current year NC items)
    if get_currency(IASCHA.Over) != 0 and get_currency(IAWOTHINC.TotBonus) != 0:
        return 1
    else:
        return 0

def Alert22_Calculation():
    TotCont = Currency()
    TotCont = get_currency(IAWCONTLIMIT.CY50Lim) + get_currency(IAWCONTLIMIT.CY30Lim) + get_currency(IAWCONTLIMIT.CY30LimCG) + get_currency(IAWCONTLIMIT.CY20Lim) + get_currency(IAWCONTLIMIT.CYNoLim)
    if TotCont > get_currency(IAWCONTLIMIT.CYTot):
        return 1
    else:
        return 0

def Alert24_Calculation():
    if get_currency(IAWCONTLIMIT.PY50Lim) < 0:
        return 1
    elif get_currency(IAWCONTLIMIT.PY30Lim) < 0:
        return 1
    elif get_currency(IAWCONTLIMIT.PY30LimCG) < 0:
        return 1
    elif get_currency(IAWCONTLIMIT.PY20Lim) < 0:
        return 1
    elif get_currency(IAWCONTLIMIT.PYNoLim) < 0:
        return 1
    else:
        return 0

def Alert26_Calculation():
    if get_currency(IAWCONTLIMIT.NYTot) != 0:
        return 1
    else:
        return 0

def Alert27_Calculation():
    if get_currency(IAWCONTLIMIT.CYQualLim) != 0:
        return 1
    else:
        return 0

def Alert28_Calculation():
    if get_currency(IAWCONTLIMIT.CYQualLim) > get_currency(IASCHA.Contrib):
        return 1
    else:
        return 0

def Alert30_Calculation():
    return 0

def Alert40_Calculation():
    if get_bool(IAF1040.ItemCheck) == True and get_currency(IASCHA.OthMisc) > 0:
        if get_currency(IASCHA.IAAdjOthMisc) != 0 and trim(get_string(IASCHA.IAAdjOthMiscDesc)) == '':
            return 1
        else:
            return 0
    else:
        return 0

def Alert50_Calculation():
    count = Variant()

    Iter = Integer()
    count = 0
    Iter = 0
    while Iter < 5:
        if get_currency(IASCHA.DisableAmt(Iter)) > 0 and trim(get_string(IASCHA.DisableExp(Iter))) == '':
            count = count + 1
        Iter = Iter + 1
    if get_bool(IAF1040.ItemCheck) == True and count > 0:
        return 1
    else:
        return 0

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
        if get_currency(IA177.CYAdoptionTaxCr, count) > 0 and get_bool(IA177.Taxpayer, count) == True:
            Total = Total + 1
        else:
            Total = Total
        count = count + 1
    Lim2 = GetAllCopies(IA177)
    count2 = 1
    Total2 = 0
    while count2 <= Lim2:
        if get_currency(IA177.CYAdoptionTaxCr, count) > 0 and get_bool(IA177.Spouse, count2) == True:
            Total2 = Total2 + 1
        else:
            Total2 = Total2
        count2 = count2 + 1
    if get_currency(IASCHA.TotAdoptAmt) > 0:
        if Total > 0:
            return 1
        elif Total2 > 0 and get_bool(IAF1040.CombMFS) == True:
            return 1
        else:
            return 0
    else:
        return 0

def Alert70_Calculation():
    count = Variant()

    Iter = Integer()
    count = 0
    Iter = 0
    while Iter < 5:
        if get_currency(IASCHA.AdoptAmt(Iter)) > 0 and trim(get_string(IASCHA.AdoptExp(Iter))) == '':
            count = count + 1
        Iter = Iter + 1
    if get_bool(IAF1040.ItemCheck) == True and get_currency(IASCHA.AllowAdopt) > 0 and count > 0:
        return 1
    else:
        return 0

def Alert80_Calculation():
    if get_currency(IAWSCHAPRINT.GamblingLoss) >  ( get_currency(IAF1040.BGamble) + get_currency(IAF1040.AGamble) ) :
        return 1
    else:
        return 0

def Alert85_Calculation():
    if get_bool(IAF1040.ItemCheck) == True:
        if get_currency(IASCHA.OthTax) != 0 and trim(get_string(IASCHA.OthList)) == '':
            return 1
        else:
            return 0
    else:
        return 0

def AllowAdopt_Calculation():
    return max_value(0, get_currency(IASCHA.TotAdoptAmt) - get_currency(IASCHA.AdoptSub))

def AllowExp_Calculation():
    return max_value(0, get_currency(IASCHA.Expense) - get_currency(IASCHA.Mult))

def CombOthExpDesc_Calculation():
    return get_string(IASCHA.OthExpDesc(0)) + ' ' + get_string(IASCHA.OthExpDesc(1)) + ' ' + get_string(IASCHA.OthExpDesc(2)) + ' ' + get_string(IASCHA.OthExpDesc(3)) + ' ' + get_string(IASCHA.OthExpDesc(4)) + ' ' + get_string(IASCHA.OthExpDesc(5)) + ' ' + get_string(IASCHA.OthExpDesc(6)) + ' ' + get_string(IASCHA.OthExpDesc(7)) + ' ' + get_string(IASCHA.OthExpDesc(8)) + ' ' + get_string(IASCHA.OthExpDesc(9)) + ' ' + get_string(IASCHA.OthExpDesc(10)) + ' ' + get_string(IASCHA.OthExpDesc(11)) + ' ' + get_string(IASCHA.OthExpDesc(12)) + ' ' + get_string(IASCHA.OthExpDesc(13)) + ' ' + get_string(IASCHA.OthExpDesc(14)) + ' ' + get_string(IASCHA.OthExpDesc(15)) + ' ' + get_string(IASCHA.OthExpDesc(16)) + ' ' + get_string(IASCHA.OthExpDesc(17)) + ' ' + get_string(IASCHA.OthExpDesc(18)) + ' ' + get_string(IASCHA.OthExpDesc(19)) + ' ' + get_string(IASCHA.OthExpDesc(20)) + ' ' + get_string(IASCHA.OthExpDesc(21)) + ' ' + get_string(IASCHA.OthExpDesc(22)) + ' ' + get_string(IASCHA.OthExpDesc(23)) + ' ' + get_string(IASCHA.OthExpDesc(24))

def CombOthMiscDesc_Calculation():
    return get_string(IASCHA.OthMiscDesc(0)) + ' ' + get_string(IASCHA.OthMiscDesc(1)) + ' ' + get_string(IASCHA.OthMiscDesc(2)) + ' ' + get_string(IASCHA.OthMiscDesc(3)) + ' ' + get_string(IASCHA.OthMiscDesc(4)) + ' ' + get_string(IASCHA.OthMiscDesc(5)) + ' ' + get_string(IASCHA.OthMiscDesc(6)) + ' ' + get_string(IASCHA.OthMiscDesc(7)) + ' ' + get_string(IASCHA.OthMiscDesc(8)) + ' ' + get_string(IASCHA.OthMiscDesc(9))

def Contrib_Calculation():
    return max_value(0, get_currency(IASCHA.TotContrib) - get_currency(IASCHA.IAAdjContrib))

def Description_Calculation():
    return CStr(get_currency(IASCHA.Item)) + ' Itemized Deductions'

def Exist_Calculation():
    return 1

def Expense_Calculation():
    return get_currency(IASCHA.Unreimb) + get_currency(IASCHA.TaxFee) + get_currency(IASCHA.OthExp)

def GenSales_Calculation():
    #Iowa expanded instructions can only claim gen sales tax if itemize federally and elect to claim gen sales on fed. Leave calced.
    if get_bool(USWRec.ItmDdn) == True and get_bool(USWResidency.F1040NR) == False:
        return get_bool(USSchA.GenSales)
    else:
        return 0

def Gifts_Calculation():
    return max_value(0, get_currency(IASCHA.TotNonCash) - get_currency(IASCHA.IAAdjNonCash))

def Header1_Calculation():
    return 'IA 1040 Schedule A - Itemized Deductions - Line 21 Attachment'

def IAAGI_Calculation():
    return get_currency(IAREQUIRED.IAAGI)

def IATax_Calculation():
    IAWHEst = Currency()

    OthIAWH = Currency()
    IAWHEst = get_currency(IAREQUIRED.TotIAW2WH) + get_currency(IAREQUIRED.TotW2GWH) + get_currency(IAREQUIRED.Tot1042S) + get_currency(IAREQUIRED.TotCapGainWH) + get_currency(IAREQUIRED.TotDivWH) + get_currency(IAREQUIRED.TotUnemWH) + get_currency(IAREQUIRED.TotIntWH) + get_currency(IAREQUIRED.TotKWH) + get_currency(IAREQUIRED.TotMiscWH) + get_currency(IAREQUIRED.TotOIDWH) + get_currency(IAREQUIRED.Tot1099rWH) + get_currency(IAREQUIRED.TotOthIncWH) + get_currency(IAREQUIRED.TotCyLocEst) + get_currency(IAREQUIRED.TotCYIAEst)
    if get_bool(USWResidency.F1040NR) == False:
        OthIAWH = get_currency(USSchA.StateWH3) + get_currency(USSchA.StateWH4) + get_currency(USSchA.StateWH5)
    else:
        OthIAWH = get_currency(USSchANR.StateWH3) + get_currency(USSchANR.StateWH4) + get_currency(USSchANR.StateWH5)
    if get_bool(IAF126.TpPYNR) == True or get_bool(IAF126.SpPYNR) == True:
        return IAWHEst
    else:
        return min_value(get_currency(IASCHA.TotStTax), IAWHEst + OthIAWH)

def Income_Calculation():
    if get_bool(IASCHA.GenSales) == True:
        return 0
    else:
        return 1

def Invest_Calculation():
    return get_currency(USSchA.InvInt)

def Item_Calculation():
    return get_currency(IASCHA.TotDeductions) + get_currency(IASCHA.TotOthDed)

def ListExp_Calculation():
    if get_currency(IASCHA.OthExp) != 0:
        return get_string(IASCHA.Ln21SeeAtt)
    else:
        return ''

def ListMisc_Calculation():
    if get_currency(IASCHA.OthMisc) != 0:
        return get_string(IASCHA.OthMiscDesc(0)) + ' ' + get_string(IASCHA.OthMiscDesc(1)) + ' ' + get_string(IASCHA.OthMiscDesc(2)) + ' ' + get_string(IASCHA.OthMiscDesc(3)) + ' ' + get_string(IASCHA.OthMiscDesc(4))
    else:
        return ''

def Ln21SeeAtt_Calculation():
    if get_currency(IASCHA.OthLn21Amt(1)) != 0:
        return 'See Attached'
    else:
        return get_string(IASCHA.OthExpDesc(0))

def MedDed_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return max_value(0, get_currency(IASCHA.MedExp) - get_currency(IASCHA.AGI))
    else:
        return 0

def MedExp_Calculation():
    HealthInsDed = Currency()
    #removed the prior year excess advanced PTC from the HealthInsDed since should not offset current year medical expenses
    #adjusted medical expense calc for PTC adjustment if claiming on IA 1040 line 18 (if not claiming on line 18 should follow federal treatment of PTC, if on 18 PTC handled on IA 1040)
    #change was made based on US 433238 see also CSS ticket 8605571
    HealthInsDed = get_currency(IAWHEALTH.TPInsPrem) + get_currency(IAWHEALTH.TPMedicare) + get_currency(IAWHEALTH.TPLTC) + get_currency(IAWHEALTH.SPInsPrem) + get_currency(IAWHEALTH.SPMedicare) + get_currency(IAWHEALTH.SPLTC)
    if get_bool(USWResidency.F1040NR) == False:
        if ( get_currency(IAWHEALTH.TPInsPrem) + get_currency(IAWHEALTH.SPInsPrem) )  == 0:
            return max_value(0, get_currency(USSchA.MedExp) - HealthInsDed)
        else:
            return max_value(0, max_value(0, get_currency(USSchA.MedExp) + get_currency(USWMedicalWS.PTCAdj)) - HealthInsDed)
    else:
        return 0

def Mort_Calculation():
    return get_currency(IASCHA.MortFed) + get_currency(IASCHA.MortAdj)

def MortAdj_Calculation():
    if get_bool(USWResidency.F1040NR) == True:
        return 0
    else:
        return get_currency(USD1098.StateAdj)

def MortFed_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USSchA.MortInt) + get_currency(USF8396.CrInt)
    else:
        return 0

def MortNot_Calculation():
    return get_currency(USSchA.Sfm)

def MtgePrem_Calculation():
    return get_currency(USSchA.MtgePrem)

def Mult_Calculation():
    if get_currency(IASCHA.Expense) > 0:
        return max_value(0, c_dollar(get_float(IASCHA.IAAGI) * 0.02))
    else:
        return 0

def Names_Calculation():
    return get_string(IAREQUIRED.CombNames)

def OthExp_Calculation():
    return get_currency(IAWSCHAPRINT.TotExp)

def OthExpDesc_Calculation(Index):
    count = Integer()

    Hold = String()
    count = 0
    Hold = ''
    if get_currency(IAWSCHAPRINT.Legal) != 0:
        if Index == count:
            Hold = 'Legal Fees - Taxable Income'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.OthLegal) != 0:
        if Index == count:
            Hold = 'Other Legal Fees'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.Clerical) != 0:
        if Index == count:
            Hold = 'Clerical Help'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.Custodial) != 0:
        if Index == count:
            Hold = 'Custodial/Investment Fees'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.Invest) != 0:
        if Index == count:
            Hold = 'Investment Expenses Form 1099s'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.InsolventLoss) != 0:
        if Index == count:
            Hold = 'Insolvent Losses'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.CasualtyLoss) != 0:
        if Index == count:
            Hold = 'Form 4684'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.Appraisal) != 0:
        if Index == count:
            Hold = 'Appraisal Fees'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.DeprTot) != 0:
        if Index == count:
            Hold = 'Depreciation Computer'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.Amort) != 0:
        if Index == count:
            Hold = 'Amortization'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.ExcessDed) != 0:
        if Index == count:
            Hold = 'Excess K-1 Ded'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.Fees) != 0:
        if Index == count:
            Hold = 'Fees to Collect'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.Hobby) != 0 and get_bool(USWResidency.F1040NR) == False:
        if Index == count:
            Hold = 'Hobby Expenses'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.Indirect) != 0:
        if Index == count:
            Hold = 'Indirect Pass-through'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.REMIC) != 0:
        if Index == count:
            Hold = 'REMIC'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.IRALoss) != 0:
        if Index == count:
            Hold = 'IRA Loss'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.RepayInc) != 0:
        if Index == count:
            Hold = 'Income Repay'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.RepaySSB) != 0 and get_bool(USWResidency.F1040NR) == False:
        if Index == count:
            Hold = 'SSB Repay'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.SafeBox) != 0:
        if Index == count:
            Hold = 'Safe Deposit'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.ServiceCharge) != 0:
        if Index == count:
            Hold = 'Service Charges Div'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.TaxAdvice) != 0:
        if Index == count:
            Hold = 'Tax Advice'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.Trustee) != 0:
        if Index == count:
            Hold = 'Trustee\'s Fees IRA'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.CreditFees) != 0:
        if Index == count:
            Hold = 'Convenience Fee'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.OthExp) != 0:
        if Index == count:
            Hold = get_string(IAWSCHAPRINT.OtherText)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.OthExp2) != 0:
        if Index == count:
            Hold = get_string(IAWSCHAPRINT.OtherText2)
            count = 99
        else:
            count = count + 1
    return Hold

def OthList_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_string(USSchA.OtherTaxType)
    else:
        return ''

def OthLn21Amt_Calculation(Index):
    count = Integer()

    Hold = Currency()
    count = 0
    Hold = 0
    if get_currency(IAWSCHAPRINT.Legal) != 0:
        if Index == count:
            Hold = get_currency(IAWSCHAPRINT.Legal)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.OthLegal) != 0:
        if Index == count:
            Hold = get_currency(IAWSCHAPRINT.OthLegal)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.Clerical) != 0:
        if Index == count:
            Hold = get_currency(IAWSCHAPRINT.Clerical)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.Custodial) != 0:
        if Index == count:
            Hold = get_currency(IAWSCHAPRINT.Custodial)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.Invest) != 0:
        if Index == count:
            Hold = get_currency(IAWSCHAPRINT.Invest)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.InsolventLoss) != 0:
        if Index == count:
            Hold = get_currency(IAWSCHAPRINT.InsolventLoss)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.CasualtyLoss) != 0:
        if Index == count:
            Hold = get_currency(IAWSCHAPRINT.CasualtyLoss)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.Appraisal) != 0:
        if Index == count:
            Hold = get_currency(IAWSCHAPRINT.Appraisal)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.DeprTot) != 0:
        if Index == count:
            Hold = get_currency(IAWSCHAPRINT.DeprTot)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.Amort) != 0:
        if Index == count:
            Hold = get_currency(IAWSCHAPRINT.Amort)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.ExcessDed) != 0:
        if Index == count:
            Hold = get_currency(IAWSCHAPRINT.ExcessDed)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.Fees) != 0:
        if Index == count:
            Hold = get_currency(IAWSCHAPRINT.Fees)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.Hobby) != 0 and get_bool(USWResidency.F1040NR) == False:
        if Index == count:
            Hold = get_currency(IAWSCHAPRINT.Hobby)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.Indirect) != 0:
        if Index == count:
            Hold = get_currency(IAWSCHAPRINT.Indirect)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.REMIC) != 0:
        if Index == count:
            Hold = get_currency(IAWSCHAPRINT.REMIC)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.IRALoss) != 0:
        if Index == count:
            Hold = get_currency(IAWSCHAPRINT.IRALoss)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.RepayInc) != 0:
        if Index == count:
            Hold = get_currency(IAWSCHAPRINT.RepayInc)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.RepaySSB) != 0 and get_bool(USWResidency.F1040NR) == False:
        if Index == count:
            Hold = get_currency(IAWSCHAPRINT.RepaySSB)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.SafeBox) != 0:
        if Index == count:
            Hold = get_currency(IAWSCHAPRINT.SafeBox)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.ServiceCharge) != 0:
        if Index == count:
            Hold = get_currency(IAWSCHAPRINT.ServiceCharge)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.TaxAdvice) != 0:
        if Index == count:
            Hold = get_currency(IAWSCHAPRINT.TaxAdvice)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.Trustee) != 0:
        if Index == count:
            Hold = get_currency(IAWSCHAPRINT.Trustee)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.CreditFees) != 0:
        if Index == count:
            Hold = get_currency(IAWSCHAPRINT.CreditFees)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.OthExp) != 0:
        if Index == count:
            Hold = get_currency(IAWSCHAPRINT.OthExp)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.OthExp2) != 0:
        if Index == count:
            Hold = get_currency(IAWSCHAPRINT.OthExp2)
            count = 99
        else:
            count = count + 1
    return Hold

def OthMisc_Calculation():
    return max_value(0, get_currency(IASCHA.TotOthMisc) + get_currency(IASCHA.IAAdjOthMisc))

def OthMiscDesc_Calculation(Index):
    count = Integer()

    Hold = String()
    count = 0
    Hold = ''
    if get_currency(IAWSCHAPRINT.Form4684) != 0:
        if Index == count:
            Hold = 'Casualty and theft loss'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.GamblingLoss) != 0 and get_bool(USWResidency.F1040NR) == False:
        if Index == count:
            Hold = 'Gambling losses'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.K1DedPort) != 0:
        if Index == count:
            Hold = 'Schedule K-1'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.ImpWrkExp) != 0:
        if Index == count:
            Hold = 'Impairment-related work expenses'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.TotEstK1) != 0 and get_bool(USWResidency.F1040NR) == False:
        if Index == count:
            Hold = 'Federal estate tax'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.Repay) != 0:
        if Index == count:
            Hold = 'Claim repayments'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.Bond) != 0 and get_bool(USWResidency.F1040NR) == False:
        if Index == count:
            Hold = 'Amortizable bond premiums'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.Pension) != 0:
        if Index == count:
            Hold = 'Unrecovered pension investments'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWSCHAPRINT.Debt) != 0:
        if Index == count:
            Hold = 'Ordinary loss'
            count = 99
        else:
            count = count + 1
    if get_currency(IASCHA.IAAdjOthMisc) != 0:
        if Index == count:
            Hold = get_string(IASCHA.IAAdjOthMiscDesc)
            count = 99
        else:
            count = count + 1
    return Hold

def OthTax_Calculation():
    #review to default calc - fed not allowing foreign taxes paid.
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USSchA.OtherTax)
    else:
        return 0

def Over_Calculation():
    return get_currency(IAWCONTLIMIT.PYTot)
    #If get_bool(USWResidency.F1040NR) = False Then
    #    return get_currency(USSchA.Carry)
    #Else
    #    return get_currency(USSchANR.Carry)
    #End If

def Perc_Calculation():
    TopLim = Double()
    if get_currency(IASCHA.YouNet) < 0 and get_currency(IASCHA.SpNet) < 0:
        if get_currency(IASCHA.YouNet) < get_currency(IASCHA.SpNet):
            return 0
        else:
            return 1
    elif get_currency(IASCHA.YouNet) < 0:
        return 0
    elif get_currency(IASCHA.YouNet) > 0 and get_currency(IASCHA.TotNet) <= 0:
        return 1
    elif get_currency(IASCHA.TotNet) == 0:
        return 0
    else:
        TopLim = min_value(1, Round(get_float(IASCHA.YouNet) / get_float(IASCHA.TotNet), 3))
        return max_value(0, TopLim)

def PrintSchA_Calculation():
    if get_bool(IAREQUIRED.LowInc) == True:
        return 0
    else:
        return get_number(IAF1040.ItemCheck)

def PrLn21SeeAtt_Calculation():
    if get_currency(IASCHA.OthLn21Amt(1)) != 0 and get_number(IASCHA.PrintSchA) == 1:
        return 1
    else:
        return 0

def Prop_Calculation():
    return get_currency(USSchA.PerPropTax)

def PtsNot_Calculation():
    return get_currency(USSchA.Points)

def RealEst_Calculation():
    return get_currency(USSchA.RealTax)

def SalesTax_Calculation():
    return get_currency(USSchA.SalesTax)

def SchAMilesDed_Calculation():
    Con1 = Currency()
    #per fed, no change for 2018 remains at 14 cents
    if get_bool(USWResidency.F1040NR) == False:
        Con1 = c_dollar(get_float(USSchA.ConMiles) * 14)
    else:
        Con1 = c_dollar(get_float(USSchANR.ConMiles) * 14)
    return Con1

def SchoolTax_Calculation():
    if get_bool(IAF1040.MFJ) == True or get_bool(IAF1040.CombMFS) == True:
        return get_currency(USZIA1040.IAPYSurtaxA) + get_currency(USZIA1040.IAPYSurtaxB)
    else:
        return get_currency(USZIA1040.IAPYSurtaxA)

def SpNet_Calculation():
    if get_bool(IAF1040.CombMFS) == True or get_bool(IAF1040.MFS) == True:
        return get_currency(IAF1040.BNet)
    else:
        return 0

def SpPro_Calculation():
    if get_bool(IAF1040.CombMFS) == True or get_bool(IAF1040.MFS) == True:
        return max_value(0, get_currency(IASCHA.Item) - get_currency(IASCHA.YouPC))
    else:
        return 0

def SSN_Calculation():
    return get_string(IAF1040.SSN)

def StTax_Calculation():
    if get_bool(IASCHA.GenSales) == True:
        return get_currency(IASCHA.SalesTax)
    else:
        return get_currency(IASCHA.TotIncTax)

def TaxFee_Calculation():
    return 0
    #If get_bool(USWResidency.F1040NR) = False Then
    #    return get_currency(USSchA.TaxPrep)
    #Else
    #    return get_currency(USSchANR.TaxPrep)
    #End If

def TaxPd_Calculation():
    return get_currency(IASCHA.StTax) + get_currency(IASCHA.RealEst) + get_currency(IASCHA.Prop) + get_currency(IASCHA.OthTax)

def Theft_Calculation():
    return get_currency(IA4684.SctATot)

def TotAdoptAmt_Calculation():
    return get_currency(IASCHA.AdoptAmt(0)) + get_currency(IASCHA.AdoptAmt(1)) + get_currency(IASCHA.AdoptAmt(2)) + get_currency(IASCHA.AdoptAmt(3)) + get_currency(IASCHA.AdoptAmt(4))

def TotContrib_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USSchA.Cash)
    else:
        return get_currency(USSchANR.Cash)

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
    if get_currency(IASCHA.IAAGI) > Limit:
        return get_currency(IAWITMDED.LimitDed)
    else:
        return get_currency(IASCHA.OthMisc) + get_currency(IASCHA.AllowExp) + get_currency(IASCHA.Theft) + get_currency(IASCHA.TotGifts) + get_currency(IASCHA.TotInt) + get_currency(IASCHA.TaxPd) + get_currency(IASCHA.MedDed)

def TotDisableAmt_Calculation():
    TotDisable = Currency()
    TotDisable = get_currency(IASCHA.DisableAmt(0)) + get_currency(IASCHA.DisableAmt(1)) + get_currency(IASCHA.DisableAmt(2)) + get_currency(IASCHA.DisableAmt(3)) + get_currency(IASCHA.DisableAmt(4))
    return min_value(Decimal("5000"), TotDisable)

def TotGifts_Calculation():
    return get_currency(IAWCONTLIMIT.CYTotAfter)

def TotIncTax_Calculation():
    return max_value(0, get_currency(IASCHA.TotStTax) + get_currency(IASCHA.SchoolTax) - get_currency(IASCHA.IATax))

def TotInt_Calculation():
    return get_currency(IASCHA.Mort) + get_currency(IASCHA.MortNot) + get_currency(IASCHA.PtsNot) + get_currency(IASCHA.Invest)

def TotMilesDed_Calculation():
    Con1 = Currency()
    if get_bool(USWResidency.F1040NR) == False:
        Con1 = c_dollar(get_float(USSchA.ConMiles) * 39)
    else:
        Con1 = c_dollar(get_float(USSchANR.ConMiles) * 39)
    return Con1

def TotNet_Calculation():
    return get_currency(IASCHA.SpNet) + get_currency(IASCHA.YouNet)

def TotNonCash_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USSchA.NonCash)
    else:
        return get_currency(USSchANR.NonCash)

def TotOthDed_Calculation():
    return get_currency(IASCHA.TotDisableAmt) + get_currency(IASCHA.AllowAdopt) + get_currency(IASCHA.AddMilesDed)

def TotOthMisc_Calculation():
    return get_currency(IAWSCHAPRINT.TotOthDed)

def TotStTax_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return max_value(0, get_currency(USSchA.StateWH1) + get_currency(USSchA.StateWH2) + get_currency(USSchA.LocalWH) + get_currency(USSchA.StateWH3) + get_currency(USSchA.StateWH4) + get_currency(USSchA.StateWH5) - get_currency(USSchA.WHOff))
    else:
        return max_value(0, get_currency(USSchANR.StateWH1) + get_currency(USSchANR.StateWH2) + get_currency(USSchANR.LocalWH) + get_currency(USSchANR.StateWH3) + get_currency(USSchANR.StateWH4) + get_currency(USSchANR.StateWH5) - get_currency(USSchANR.WHOff))

def Unreimb_Calculation():
    return get_currency(IAWSCHAPRINT.TotOtherExp)

def YouNet_Calculation():
    if get_bool(IAF1040.CombMFS) == True or get_bool(IAF1040.MFS) == True:
        return get_currency(IAF1040.ANet)
    else:
        return 0

def YouPC_Calculation():
    return c_dollar(get_float(IASCHA.Perc) * get_float(IASCHA.Item))


