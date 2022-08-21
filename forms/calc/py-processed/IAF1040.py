from forms.out import IA1040X
from forms.out import IA130
from forms.out import IA148SP
from forms.out import IA2210
from forms.out import IA2210AN
from forms.out import IA2210ANSP
from forms.out import IA2210SP
from forms.out import IA6251
from forms.out import IA6251SP
from forms.out import IAADDFEDTAX
from forms.out import IACHILDCREDIT
from forms.out import IAEFWKSHT
from forms.out import IAESTIMATES
from forms.out import IAF1040
from forms.out import IAF126
from forms.out import IAFEDEST
from forms.out import IAFEDREF
from forms.out import IAFIRECR
from forms.out import IAOTHADJ
from forms.out import IAREQUIRED
from forms.out import IASCHA
from forms.out import IASETAX
from forms.out import IASTATEEST
from forms.out import IATUITION
from forms.out import IAWHEALTH
from forms.out import IAWKALTTAX
from forms.out import IAWKSSB
from forms.out import IAWOTHINC
from forms.out import IAWPENEXC
from forms.out import USF4972SPOUSE
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def AAlimony_Calculation():
    if IAFS() == 3:
        return get_currency(USWRec.TAlimony)
    else:
        return get_currency(USWRec.TotAlimony)

def AAlimonyP_Calculation():
    if IAFS() == 3:
        return get_currency(USWRec.TAlimonyAdj)
    else:
        return get_currency(USWRec.TotAlimonyAdj)

def AAltTax_Calculation():
    # 1st condition added for situation when MFS return and reporting spouse income causes an alternate tax calculation yet taxpayer has zero income
    # See saved return IA MFS Alternate Tax Issue.ta2
    if get_bool(IAF1040.MFS) == True and get_currency(IAF1040.ATaxInc) == 0:
        return 0
    elif  ( get_currency(IAWKALTTAX.Mult) < get_currency(IAWKALTTAX.Tables) )  and get_bool(IAWKALTTAX.Qualify) == True:
        return get_currency(IAF1040.ATax)
    else:
        return get_currency(IAF1040.ARegTax)

def AApply99_Calculation():
    return max_value(0, get_currency(IAESTIMATES.TotApplied) - get_currency(IAF1040.BApply99))

def ABal1_Calculation():
    if IAFS() == 1 and get_bool(IAF1040.DepY) == False:
        return get_currency(IAREQUIRED.TaxReduction)
    else:
        return max_value(0, get_currency(IAF1040.ATotIATax) - get_currency(IAF1040.ACredits))

def ABal2_Calculation():
    return max_value(0, get_currency(IAF1040.ABal1) - get_currency(IAF1040.ACrNon))

def ABal4_Calculation():
    return max_value(0, get_currency(IAF1040.ABal3) - get_currency(IAF1040.AOthIACr))

def ABal36_Calculation():
    return get_currency(IAF1040.ABalance)

def ABal3_Calculation():
    return max_value(0, get_currency(IAF1040.ABal2) - get_currency(IAF1040.AOutState))

def ABalance_Calculation():
    return get_currency(IAF1040.ATotTax) - get_currency(IAF1040.AFedDed)

def ABusInc_Calculation():
    if IAFS() == 3:
        return get_currency(USWRec.TBusiness)
    else:
        return get_currency(USWRec.TotBusiness)

def ABusIncL_Calculation():
    if IAFS() == 3:
        return get_currency(USWRec.THalfSe)
    else:
        return get_currency(USWRec.TotHalfSE)

def ACapGain_Calculation():
    CapGain = Currency()
    if get_bool(USWResidency.F1040NR) == False:
        CapGain = get_currency(USF1040.CapGain)
    else:
        CapGain = get_currency(USF1040NR.CapGain)
    if IAFS() == 3:
        return CapGain - get_currency(IAF1040.BCapGain)
    else:
        return CapGain

def AChild_Calculation():
    if get_bool(IAF1040.ChildCareCk) == True:
        return get_currency(IACHILDCREDIT.TChild)
    elif get_bool(IAF1040.EarlyChildCk) == True:
        return get_currency(IACHILDCREDIT.TEarly)
    else:
        return 0

def ACredits_Calculation():
    return get_currency(IAF1040.AExemCr) + get_currency(IAF1040.ATuit) + get_currency(IAF1040.AVolFireCr)

def ACrNon_Calculation():
    return get_currency(IAF126.ACredit)

def ActNum_Calculation():
    if get_bool(IAEFWKSHT.PrepBPTrans) == True:
        return ''
    elif get_bool(IAEFWKSHT.DirDeposit) == True and get_bool(IAEFWKSHT.Yes) == False and get_currency(IAEFWKSHT.Refund) > 0:
        return get_string(IAEFWKSHT.DirDepDan)
    else:
        return ''

def Add_Calculation():
    return get_string(USWBasicInfo.HomeComb)

def ADedBox_Calculation():
    Itemized = Currency()

    Deduction = Currency()
    # updated for 2018
    if get_bool(IAF1040.CombMFS) == True or get_bool(IAF1040.MFS) == True:
        Itemized = get_currency(IASCHA.YouPC)
    else:
        Itemized = get_currency(IASCHA.Item)
    if get_bool(IAF1040.ItemCheck) == True:
        Deduction = Itemized
    elif IAFS() == 2 or IAFS() == 5 or IAFS() == 6:
        Deduction = min_value(Decimal("5000"), get_currency(IAF1040.ABal36))
    else:
        Deduction = min_value(Decimal("2030"), get_currency(IAF1040.ABal36))
    return max_value(0, Deduction)

def ADividend_Calculation():
    if IAFS() == 3:
        return get_currency(IAREQUIRED.TotTPDiv)
    else:
        return get_currency(IAREQUIRED.TotDiv)

def AEst_Calculation():
    if get_bool(IA1040X.EFAmend) == True:
        return max_value(0, get_currency(IASTATEEST.TotIAEst) - get_currency(IASTATEEST.SPIAEst)) + get_currency(IA1040X.TotPrevTax)
    else:
        return max_value(0, get_currency(IASTATEEST.TotIAEst) - get_currency(IASTATEEST.SPIAEst))

def AEstTax_Calculation():
    if IAFS() == 3:
        return get_currency(IAFEDEST.TPTotEst)
    else:
        return get_currency(IAFEDEST.TPTotEst) + get_currency(IAFEDEST.SPTotEst)

def AExemCr_Calculation():
    return get_currency(IAF1040.ExempA)

def AFarm_Calculation():
    if IAFS() == 3:
        return get_currency(USWRec.TFarm)
    else:
        return get_currency(USWRec.TotFarm)

def AFedDed_Calculation():
    return get_currency(IAF1040.ATaxWith) + get_currency(IAF1040.AEstTax) + get_currency(IAF1040.APrior)

def AFedTax_Calculation():
    return get_currency(IAF1040.ARefund) + get_currency(IAF1040.ASelf)

def AFuel_Calculation():
    return get_currency(IASch4136.TotCr, FieldCopies(IASch4136.Taxpayer))

def AGamble_Calculation():
    if get_bool(USWResidency.F1040NR) == True:
        return get_currency(USSchNEC.Gambling130) + get_currency(USSchNEC.Gambling1Oth) + get_currency(USSchNEC.Gambling10) + get_currency(USSchNEC.Gambling230) + get_currency(USSchNEC.Gambling2Oth)
    elif IAFS() == 3:
        return get_currency(USWOthInc.TPOth3)
    else:
        return get_currency(USWOthInc.TotGamb)

def AGross_Calculation():
    return get_currency(IAF1040.AWages) + get_currency(IAF1040.AInterest) + get_currency(IAF1040.ADividend) + get_currency(IAF1040.AAlimony) + get_currency(IAF1040.ABusInc) + get_currency(IAF1040.ACapGain) + get_currency(IAF1040.AOthGain) + get_currency(IAF1040.AIRA) + get_currency(IAF1040.APensions) + get_currency(IAF1040.ARents) + get_currency(IAF1040.AFarm) + get_currency(IAF1040.AUnemp) + get_currency(IAF1040.AGamble) + get_currency(IAF1040.AOtherInc)

def AHealth_Calculation():
    if IAFS() == 3:
        return get_currency(IAWHEALTH.TPTotal)
    else:
        return get_currency(IAWHEALTH.TPTotal) + get_currency(IAWHEALTH.SPTotal)

def AIAMin_Calculation():
    return get_currency(IA6251.TotAMT)

def AIATaxWith_Calculation():
    if IAFS() == 3:
        return get_currency(IAREQUIRED.TIAW2WH) + get_currency(IAREQUIRED.TPW2GWH) + get_currency(IAREQUIRED.Tot1042S) + get_currency(IAREQUIRED.TPCapGainWH) + get_currency(IAREQUIRED.TPDivWH) + get_currency(IAREQUIRED.TPUnemWH) + get_currency(IAREQUIRED.TPIntWH) + get_currency(IAREQUIRED.TPKWH) + get_currency(IAREQUIRED.TPMiscWH) + get_currency(IAREQUIRED.TPOIDWH) + get_currency(IAREQUIRED.T1099rWH) + get_currency(IAREQUIRED.TpOthIncWH)
    else:
        return get_currency(IAREQUIRED.TotIAW2WH) + get_currency(IAREQUIRED.TotW2GWH) + get_currency(IAREQUIRED.Tot1042S) + get_currency(IAREQUIRED.TotCapGainWH) + get_currency(IAREQUIRED.TotDivWH) + get_currency(IAREQUIRED.TotUnemWH) + get_currency(IAREQUIRED.TotIntWH) + get_currency(IAREQUIRED.TotKWH) + get_currency(IAREQUIRED.TotMiscWH) + get_currency(IAREQUIRED.TotOIDWH) + get_currency(IAREQUIRED.Tot1099rWH) + get_currency(IAREQUIRED.TotOthIncWH)

def AIEIC_Calculation():
    if IAFS() == 3 or IAFS() == 4:
        return get_currency(IAREQUIRED.TIAEic)
    else:
        return get_currency(IAREQUIRED.IAEic)

def AInterest_Calculation():
    if IAFS() == 3:
        return get_currency(IAREQUIRED.TotTPInt)
    else:
        return get_currency(IAREQUIRED.TotInt)

def AIRA_Calculation():
    if IAFS() == 3:
        return get_currency(IAWPENEXC.TPIRA)
    else:
        return get_currency(IAWPENEXC.TPIRA) + get_currency(IAWPENEXC.SPIRA)

def AKeogh_Calculation():
    if IAFS() == 3:
        return get_currency(USWRec.TKeough) + get_currency(IAREQUIRED.TIRA)
    else:
        return get_currency(USWRec.TotKeough) + get_currency(USWRec.TotIRAAdj)

def ALump_Calculation():
    if IAFS() == 3:
        return c_dollar(get_float(USF4972.Tax) * 0.25)
    else:
        return c_dollar(get_float(USF4972.Tax) * 0.25) + c_dollar(get_float(USF4972SPOUSE.Tax) * 0.25)

def AMove_Calculation():
    if IAFS() == 3:
        return get_currency(IAREQUIRED.TMove)
    else:
        return get_currency(IAREQUIRED.TotMove)

def ANet_Calculation():
    return get_currency(IAF1040.AGross) - get_currency(IAF1040.ATotAdj)

def AOthAdj_Calculation():
    if IAFS() == 3:
        return get_currency(IAOTHADJ.TPTot)
    else:
        return get_currency(IAOTHADJ.TPTot) + get_currency(IAOTHADJ.SPTot)

def AOtherInc_Calculation():
    if IAFS() == 3:
        return get_currency(IAWOTHINC.TPTot)
    else:
        return get_currency(IAWOTHINC.TPTot) + get_currency(IAWOTHINC.SPTot)

def AOthGain_Calculation():
    if IAFS() == 3:
        return get_currency(USWRec.TOthGain)
    else:
        return get_currency(USWRec.TotOthGain)

def AOthIACr_Calculation():
    return get_currency(IA148.TotNonRefCr)

def AOthRefCr_Calculation():
    return get_currency(IA148.TotRefCr)

def AOutState_Calculation():
    return get_currency(IA130.TPCredit)

def APenalty_Calculation():
    if IAFS() == 3:
        return get_currency(USWRec.TEarlyPen)
    else:
        return get_currency(USWRec.TotEarlyPen)

def APenExcl_Calculation():
    if IAFS() == 3:
        return get_currency(IAWPENEXC.TPPenExc)
    else:
        return get_currency(IAWPENEXC.TPPenExc) + get_currency(IAWPENEXC.SPPenExc)

def APensions_Calculation():
    if IAFS() == 3:
        return get_currency(IAWPENEXC.TPPensions)
    else:
        return get_currency(IAWPENEXC.TPPensions) + get_currency(IAWPENEXC.SPPensions)

def APrior_Calculation():
    if IAFS() == 3:
        return get_currency(IAADDFEDTAX.TPTotal)
    else:
        return get_currency(IAADDFEDTAX.TPTotal) + get_currency(IAADDFEDTAX.SPTotal)

def ARefund_Calculation():
    if IAFS() == 3:
        return get_currency(IAFEDREF.TPST)
    else:
        return get_currency(IAFEDREF.SPST) + get_currency(IAFEDREF.TPST)

def ARegTax_Calculation():
    Mid = Currency()

    MidInt = Long()

    TotTaxInc = Currency()
    # updated for 2018
    TotTaxInc = get_currency(IAF1040.ATaxInc)
    if TotTaxInc > Decimal("95650"):
        Mid = TotTaxInc
    elif TotTaxInc > Decimal("150"):
        MidInt = CLng(( TotTaxInc - Decimal("1") )  / Decimal("50"))
        Mid = ( CCur(MidInt) * Decimal("50") )  + Decimal("25")
    else:
        Mid = Decimal("0")
    return Tax(Mid)

def ARents_Calculation():
    if IAFS() == 3:
        return get_currency(USWRec.TRental)
    else:
        return get_currency(USWRec.TotRental)

def ARepSSB_Calculation():
    if IAFS() == 3:
        return get_currency(IAWKSSB.TPRepSSB)
    else:
        return get_currency(IAWKSSB.ReportSSB)

def ASch_Calculation():
    return c_dollar(get_float(IAF1040.ABal4) * get_float(IAF1040.SchRate))

def ASelf_Calculation():
    if IAFS() == 3:
        return get_currency(IASETAX.TPTotal)
    else:
        return get_currency(IASETAX.TPTotal) + get_currency(IASETAX.SPTotal)

def ATax_Calculation():
    if get_number(IAWKALTTAX.ProRate) == 1:
        return get_currency(IAWKALTTAX.ATax)
    else:
        return get_currency(IAWKALTTAX.Lesser)

def ATaxB4Cont_Calculation():
    return get_currency(IAF1040.ABal4) + get_currency(IAF1040.ASch)

def ATaxInc_Calculation():
    return max_value(0, get_currency(IAF1040.ABal36) - get_currency(IAF1040.ADedBox))

def ATaxWith_Calculation():
    TotWH = Currency()
    if get_bool(USWResidency.F1040NR) == True:
        TotWH = get_currency(USF1040NR.WHW2) + get_currency(USF1040NR.WH8805) + get_currency(USF1040NR.WH8288A) + get_currency(USF1040NR.WH1042S)
    else:
        TotWH = get_currency(USF1040.WH) + Round(get_currency(USDW2AS.ASWH, FieldCopies(USDW2AS.Taxpayer))) + Round(get_currency(USDW2VI.VIWH, FieldCopies(USDW2VI.Taxpayer)))
    if IAFS() == 3:
        return max_value(0, TotWH - get_currency(IAF1040.BTaxWith))
    else:
        return TotWH

def ATot67_Calculation():
    return get_currency(IAF1040.AFuel) + get_currency(IAF1040.AChild) + get_currency(IAF1040.AIEIC) + get_currency(IAF1040.AOthRefCr) + get_currency(IAF1040.AIATaxWith) + get_currency(IAF1040.AEst)

def ATotAdj_Calculation():
    return get_currency(IAF1040.AKeogh) + get_currency(IAF1040.ABusIncL) + get_currency(IAF1040.AHealth) + get_currency(IAF1040.APenalty) + get_currency(IAF1040.AAlimonyP) + get_currency(IAF1040.APenExcl) + get_currency(IAF1040.AMove) + get_currency(IAF1040.AGainDed) + get_currency(IAF1040.AOthAdj)

def ATotIATax_Calculation():
    return get_currency(IAF1040.AAltTax) + get_currency(IAF1040.ALump) + get_currency(IAF1040.AIAMin)

def ATotTax_Calculation():
    return get_currency(IAF1040.ANet) + get_currency(IAF1040.AFedTax)

def ATuit_Calculation():
    if IAFS() == 3:
        return get_currency(IATUITION.TTuit)
    else:
        return get_currency(IATUITION.TotCr)

def AUnemp_Calculation():
    if IAFS() == 3:
        return max_value(0, get_currency(USWRec.TUnem) - Round(get_currency(USWUnempl.RRBSub, FieldCopies(USWUnempl.Taxpayer))))
    else:
        return max_value(0, get_currency(USWRec.TotUnem) - Round(get_currency(USWUnempl.RRBSub)))

def AVolFireCr_Calculation():
    if IAFS() == 3:
        return get_currency(IAFIRECR.TPTotCr)
    else:
        return get_currency(IAFIRECR.TPTotCr) + get_currency(IAFIRECR.SPTotCr)

def AWages_Calculation():
    if IAFS() == 3:
        return get_currency(USWRec.TWages)
    else:
        return get_currency(USWRec.TotWages)

def BAlimony_Calculation():
    if IAFS() == 3:
        return get_currency(USWRec.SAlimony)
    else:
        return 0

def BAlimonyP_Calculation():
    if IAFS() == 3:
        return get_currency(USWRec.SAlimonyAdj)
    else:
        return 0

def BAltTax_Calculation():
    if IAFS() == 3:
        if ( get_currency(IAWKALTTAX.Mult) < get_currency(IAWKALTTAX.Tables) )  and get_bool(IAWKALTTAX.Qualify) == True:
            return get_currency(IAF1040.BTax)
        else:
            return get_currency(IAF1040.BRegTax)
    else:
        return 0

def BApply99_Calculation():
    return min_value(get_currency(IAF1040.OVerPaid), get_currency(IAESTIMATES.TotApplied, FieldCopies(IAESTIMATES.Spouse)))

def BBal1_Calculation():
    return max_value(0, get_currency(IAF1040.BTotIATax) - get_currency(IAF1040.BCredits))

def BBal2_Calculation():
    return max_value(0, get_currency(IAF1040.BBal1) - get_currency(IAF1040.BCrNon))

def BBal4_Calculation():
    return max_value(0, get_currency(IAF1040.BBal3) - get_currency(IAF1040.BOthIACr))

def BBal36_Calculation():
    return get_currency(IAF1040.BBalance)

def BBal3_Calculation():
    return max_value(0, get_currency(IAF1040.BBal2) - get_currency(IAF1040.BOutState))

def BBalance_Calculation():
    return get_currency(IAF1040.BTotTax) - get_currency(IAF1040.BFedDed)

def BBusInc_Calculation():
    if IAFS() == 3:
        return get_currency(USWRec.SBusiness)
    else:
        return 0

def BBusIncL_Calculation():
    if IAFS() == 3:
        return get_currency(USWRec.SHalfSe)
    else:
        return 0

def BCapGain_Calculation():
    if IAFS() == 3:
        if get_currency(USWDRec.CapGain) < Decimal("0"):
            return get_currency(IAREQUIRED.SLimLoss)
        else:
            return get_currency(USWDRec.SCapGain)
    else:
        return 0

def BChild_Calculation():
    if IAFS() == 3:
        if get_bool(IAF1040.ChildCareCk) == True:
            return get_currency(IACHILDCREDIT.SChild)
        elif get_bool(IAF1040.EarlyChildCk) == True:
            return get_currency(IACHILDCREDIT.SEarly)
        else:
            return 0
    else:
        return 0

def BCredits_Calculation():
    return get_currency(IAF1040.BExemCr) + get_currency(IAF1040.BTuit) + get_currency(IAF1040.BVolFireCr)

def BCrNon_Calculation():
    if IAFS() == 3:
        if get_bool(IAF126.SpNonRes) == True or get_bool(IAF126.SpPYRes) == True:
            return get_currency(IAF126.BCredit)
        else:
            return 0
    else:
        return 0

def BDedBox_Calculation():
    Deduction = Currency()
    # updated for 2018
    if IAFS() == 3:
        if get_bool(IAF1040.ItemCheck) == True:
            Deduction = get_currency(IASCHA.SpPro)
        else:
            Deduction = min_value(Decimal("2030"), get_currency(IAF1040.BBal36))
    else:
        Deduction = 0
    return max_value(0, Deduction)

def BDividend_Calculation():
    if IAFS() == 3:
        return get_currency(IAREQUIRED.TotSPDiv)
    else:
        return 0

def BEst_Calculation():
    if IAFS() == 3:
        return get_currency(IASTATEEST.SPIAEst)
    else:
        return 0

def BEstTax_Calculation():
    if IAFS() == 3:
        return get_currency(IAFEDEST.SPTotEst)
    else:
        return 0

def BExemCr_Calculation():
    return get_currency(IAF1040.ExempB)

def BFarm_Calculation():
    if IAFS() == 3:
        return get_currency(USWRec.SFarm)
    else:
        return 0

def BFedDed_Calculation():
    return get_currency(IAF1040.BTaxWith) + get_currency(IAF1040.BEstTax) + get_currency(IAF1040.BPrior)

def BFedTax_Calculation():
    return get_currency(IAF1040.BRefund) + get_currency(IAF1040.BSelf)

def BFuel_Calculation():
    if IAFS() == 3:
        return get_currency(IASch4136.TotCr, FieldCopies(IASch4136.Spouse))
    else:
        return 0

def BGamble_Calculation():
    if IAFS() == 3 and get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.SPOth3)
    else:
        return 0

def BGross_Calculation():
    return get_currency(IAF1040.BWages) + get_currency(IAF1040.BInterest) + get_currency(IAF1040.BDividend) + get_currency(IAF1040.BAlimony) + get_currency(IAF1040.BBusInc) + get_currency(IAF1040.BCapGain) + get_currency(IAF1040.BOthGain) + get_currency(IAF1040.BIRA) + get_currency(IAF1040.BPensions) + get_currency(IAF1040.BRents) + get_currency(IAF1040.BFarm) + get_currency(IAF1040.BUnemp) + get_currency(IAF1040.BGamble) + get_currency(IAF1040.BOtherInc)

def BHealth_Calculation():
    if IAFS() == 3:
        return get_currency(IAWHEALTH.SPTotal)
    else:
        return 0

def BIAMin_Calculation():
    return get_currency(IA6251SP.TotAMT)

def BIATaxWith_Calculation():
    if IAFS() == 3:
        return get_currency(IAREQUIRED.SIAW2WH) + get_currency(IAREQUIRED.SPW2GWH) + get_currency(IAREQUIRED.SPCapGainWH) + get_currency(IAREQUIRED.SPDivWH) + get_currency(IAREQUIRED.SPUnemWH) + get_currency(IAREQUIRED.SPIntWH) + get_currency(IAREQUIRED.SPKWH) + get_currency(IAREQUIRED.SPMiscWH) + get_currency(IAREQUIRED.SPOIDWH) + get_currency(IAREQUIRED.S1099RWH) + get_currency(IAREQUIRED.SPOthIncWH)
    else:
        return 0

def BIEIC_Calculation():
    if IAFS() == 3:
        return get_currency(IAREQUIRED.SIaEIC)
    else:
        return 0

def BInterest_Calculation():
    if IAFS() == 3:
        return get_currency(IAREQUIRED.TotSPInt)
    else:
        return 0

def BIRA_Calculation():
    if IAFS() == 3:
        return get_currency(IAWPENEXC.SPIRA)
    else:
        return 0

def BKeogh_Calculation():
    if IAFS() == 3:
        return get_currency(USWRec.SKeough) + get_currency(IAREQUIRED.SIRA)
    else:
        return 0

def BLump_Calculation():
    if IAFS() == 3:
        return c_dollar(get_float(USF4972SPOUSE.Tax) * 0.25)
    else:
        return 0

def BMove_Calculation():
    if IAFS() == 3:
        return get_currency(IAREQUIRED.SMove)
    else:
        return 0

def BNet_Calculation():
    return get_currency(IAF1040.BGross) - get_currency(IAF1040.BTotAdj)

def BOthAdj_Calculation():
    if IAFS() == 3:
        return get_currency(IAOTHADJ.SPTot)
    else:
        return 0

def BOtherInc_Calculation():
    if IAFS() == 3:
        return get_currency(IAWOTHINC.SPTot)
    else:
        return 0

def BOthGain_Calculation():
    if IAFS() == 3:
        return get_currency(USWRec.SOthGain)
    else:
        return 0

def BOthIACr_Calculation():
    return get_currency(IA148SP.TotNonRefCr)

def BOthRefCr_Calculation():
    return get_currency(IA148SP.TotRefCr)

def BOutState_Calculation():
    if IAFS() == 3:
        return get_currency(IA130.SPCredit)
    else:
        return 0

def BPenalty_Calculation():
    if IAFS() == 3:
        return get_currency(USWRec.SEarlyPen)
    else:
        return 0

def BPenExcl_Calculation():
    if IAFS() == 3:
        return get_currency(IAWPENEXC.SPPenExc)
    else:
        return 0

def BPensions_Calculation():
    if IAFS() == 3:
        return get_currency(IAWPENEXC.SPPensions)
    else:
        return 0

def BPrior_Calculation():
    if IAFS() == 3:
        return get_currency(IAADDFEDTAX.SPTotal)
    else:
        return 0

def BRefund_Calculation():
    if IAFS() == 3:
        return get_currency(IAFEDREF.SPST)
    else:
        return 0

def BRegTax_Calculation():
    Mid = Currency()

    MidInt = Long()

    TotTaxInc = Currency()
    # updated for 2018
    if get_bool(IAF1040.MFS) == True:
        TotTaxInc = get_currency(IAF1040.SpTaxInc)
    else:
        TotTaxInc = get_currency(IAF1040.BTaxInc)
    if TotTaxInc > Decimal("95650"):
        Mid = TotTaxInc
    elif TotTaxInc > Decimal("150"):
        MidInt = CLng(( TotTaxInc - Decimal("1") )  / Decimal("50"))
        Mid = ( CCur(MidInt) * Decimal("50") )  + Decimal("25")
    else:
        Mid = Decimal("0")
    return Tax(Mid)

def BRents_Calculation():
    if IAFS() == 3:
        return get_currency(USWRec.SRental)
    else:
        return 0

def BRepSSB_Calculation():
    if IAFS() == 3:
        return get_currency(IAWKSSB.SPRepSSB)
    else:
        return 0

def BSch_Calculation():
    return c_dollar(get_float(IAF1040.BBal4) * get_float(IAF1040.SchRate))

def BSelf_Calculation():
    if IAFS() == 3:
        return get_currency(IASETAX.SPTotal)
    else:
        return 0

def BTax_Calculation():
    if IAFS() == 3:
        return get_currency(IAWKALTTAX.BTax)
    else:
        return 0

def BTaxB4Cont_Calculation():
    return get_currency(IAF1040.BBal4) + get_currency(IAF1040.BSch)

def BTaxInc_Calculation():
    return max_value(0, get_currency(IAF1040.BBal36) - get_currency(IAF1040.BDedBox))

def BTaxWith_Calculation():
    JT = Currency()

    SPW2 = Currency()

    SP = Currency()
    JT = c_dollar(CDbl(Round(get_currency(USD1099INT.WH, FieldCopies(USD1099INT.Joint))) + Round(get_currency(USD1099K.WH, FieldCopies(USD1099K.Joint))) + Round(get_currency(USD1099OID.WH, FieldCopies(USD1099OID.Joint))) + Round(get_currency(USD1099MISC.WH, FieldCopies(USD1099MISC.Joint))) + Round(get_currency(USD1099DIV.WH, FieldCopies(USD1099DIV.Joint))) + Round(get_currency(USDCapGain.WH2, FieldCopies(USDCapGain.Joint))) + Round(get_currency(USDPartK1.BackupWith, FieldCopies(USDPartK1.Joint))) + Round(get_currency(USDSCorpK1.BackupWith, FieldCopies(USDSCorpK1.Joint))) + Round(get_currency(USDEstK1.BackupWith, FieldCopies(USDEstK1.Joint)))) * 0.5)
    SPW2 = Round(get_currency(USDW2.WH, FieldCopies(USDW2.Spouse))) + Round(get_currency(USDW2AS.ASWH, FieldCopies(USDW2AS.Spouse))) + Round(get_currency(USDW2CM.CNMIWH, FieldCopies(USDW2CM.Spouse))) + Round(get_currency(USDW2GU.GuamWH, FieldCopies(USDW2GU.Spouse))) + Round(get_currency(USDW2VI.VIWH, FieldCopies(USDW2VI.Spouse)))
    SP = Round(get_currency(USD1099INT.WH, FieldCopies(USD1099INT.Spouse))) + Round(get_currency(USD1099K.WH, FieldCopies(USD1099K.Spouse))) + Round(get_currency(USD1099OID.WH, FieldCopies(USD1099OID.Spouse))) + Round(get_currency(USD1099DIV.WH, FieldCopies(USD1099DIV.Spouse))) + Round(get_currency(USD1099R.WH, FieldCopies(USD1099R.Spouse))) + Round(get_currency(USD1099MISC.WH, FieldCopies(USD1099MISC.Spouse))) + Round(get_currency(USWUnempl.TPFedWH, FieldCopies(USWUnempl.Spouse))) + Round(get_currency(USDW2G.WH, FieldCopies(USDW2G.Spouse))) + Round(get_currency(USDCapGain.WH2, FieldCopies(USDCapGain.Spouse))) + Round(get_currency(USDRRB1099R.WH, FieldCopies(USDRRB1099R.Spouse))) + Round(get_currency(USDPartK1.BackupWith, FieldCopies(USDPartK1.Spouse))) + Round(get_currency(USDSCorpK1.BackupWith, FieldCopies(USDSCorpK1.Spouse))) + Round(get_currency(USDEstK1.BackupWith, FieldCopies(USDEstK1.Spouse)))
    if IAFS() == 3:
        return JT + SPW2 + SP + get_currency(USWSSBDetail.SPFedWH) + get_currency(USWRec.SPTotAddMedTaxWH)
    else:
        return 0

def BTot67_Calculation():
    return get_currency(IAF1040.BFuel) + get_currency(IAF1040.BChild) + get_currency(IAF1040.BIEIC) + get_currency(IAF1040.BOthRefCr) + get_currency(IAF1040.BIATaxWith) + get_currency(IAF1040.BEst)

def BTotAdj_Calculation():
    return get_currency(IAF1040.BKeogh) + get_currency(IAF1040.BBusIncL) + get_currency(IAF1040.BHealth) + get_currency(IAF1040.BPenalty) + get_currency(IAF1040.BAlimonyP) + get_currency(IAF1040.BPenExcl) + get_currency(IAF1040.BMove) + get_currency(IAF1040.BGainDed) + get_currency(IAF1040.BOthAdj)

def BTotIATax_Calculation():
    return get_currency(IAF1040.BAltTax) + get_currency(IAF1040.BLump) + get_currency(IAF1040.BIAMin)

def BTotTax_Calculation():
    return get_currency(IAF1040.BNet) + get_currency(IAF1040.BFedTax)

def BTuit_Calculation():
    if IAFS() == 3:
        return get_currency(IATUITION.STuit)
    else:
        return 0

def BUnemp_Calculation():
    if IAFS() == 3:
        return max_value(0, get_currency(USWRec.SUnem) - Round(get_currency(USWUnempl.RRBSub, FieldCopies(USWUnempl.Spouse))))
    else:
        return 0

def BVolFireCr_Calculation():
    if IAFS() == 3:
        return get_currency(IAFIRECR.SPTotCr)
    else:
        return 0

def BWages_Calculation():
    if IAFS() == 3:
        return get_currency(USWRec.SWages)
    else:
        return 0

def Checking_Calculation():
    if get_bool(IAEFWKSHT.PrepBPTrans) == True:
        return 0
    elif get_bool(IAEFWKSHT.DirDeposit) == True and get_bool(IAEFWKSHT.Yes) == False and get_currency(IAEFWKSHT.Refund) > 0:
        return get_bool(IAEFWKSHT.DirDepChecking)
    else:
        return 0

def ChildCareCk_Calculation():
    if get_currency(IACHILDCREDIT.TotChDepCr) != 0 and get_currency(IACHILDCREDIT.TotChDepCr) >= get_currency(IACHILDCREDIT.TotCr):
        return 1
    else:
        return 0

def CityComb_Calculation():
    if trim(get_string(USWBasicInfo.ForCountry)) != '':
        return get_string(USWBasicInfo.City) + ', ' + get_string(USWBasicInfo.ForeignCtry) + ' ' + get_string(USWBasicInfo.ForeignPC)
    else:
        return get_string(USWBasicInfo.CityComb)

def CombMFS_Calculation():
    if FedFS() == 2 and  ( get_currency(USWRec.TAGI) > Decimal("2632") )  and  ( get_currency(USWRec.SAGI) > Decimal("2632") ) :
        return 1
    else:
        return 0

def CountyNo_Calculation():
    return get_string(USZIA1040.IAPYCounty)

def DateDuePaid_Calculation():
    return MakeDate(4, 30, YearNumber + 1)

def DC1_Calculation():
    if IAFS() == 3:
        return max_value(0, get_number(USWAddDep.GrandTotDeps) - get_number(IAF1040.DC2))
    else:
        return get_number(USWAddDep.GrandTotDeps)

def DC2_Calculation():
    if IAFS() == 3:
        return CLng(Round(get_number(USWAddDep.GrandTotDeps) * get_float(IAREQUIRED.BProRate)))
    else:
        return 0

def DepN_Calculation():
    if get_bool(IAF1040.Single) == True:
        if get_bool(USWBasicInfo.Dopr) == True:
            return 0
        else:
            return 1
    else:
        return 0

def DepNames_Calculation():
    if get_number(IAF1040.DC1) > 0 or get_number(IAF1040.DC2) > 0:
        if get_number(IAREQUIRED.DepLength) > 23:
            return 'See Attached'
        else:
            return get_string(IAREQUIRED.DepNames)
    else:
        return ''

def DepY_Calculation():
    if get_bool(IAF1040.Single) == True:
        if get_bool(USWBasicInfo.Dopr) == True:
            return 1
        else:
            return 0
    else:
        return 0

def Desc_Calculation():
    return get_string(IAREQUIRED.CombNames)

def EarlyChildCk_Calculation():
    if get_bool(IAF1040.ChildCareCk) == True:
        return 0
    elif get_currency(IACHILDCREDIT.TotCr) != 0:
        return 1
    else:
        return 0

def Email_Calculation():
    return get_string(USWBasicInfo.email)

def ExempA_Calculation():
    return get_currency(IAF1040.TotPCa) + get_currency(IAF1040.TotPCb) + get_currency(IAF1040.TotDC1)

def ExempB_Calculation():
    return get_currency(IAF1040.TotPC2a) + get_currency(IAF1040.TotPC2b) + get_currency(IAF1040.TotDC2)

def Exist_Calculation():
    return 1

def FirmID_Calculation():
    return get_string(USWBasicInfo.PrepEIN)

def FirstName_Calculation():
    return get_string(USWBasicInfo.TPFnI)

def HOH_Calculation():
    if FedFS() == 4:
        return 1
    else:
        return 0

def HOHDep_Calculation():
    return get_string(USWBasicInfo.L3Name)

def HOHSSN_Calculation():
    if get_bool(USF1040.HOH) == True:
        return get_string(USF1040.L3SSN)
    else:
        return ''

def ItemCheck_Calculation():
    # updated for 2018
    if get_bool(IAF1040.MFSItm) == True and IAFS() == 4:
        return 1
    elif IAFS() == 3:
        if get_currency(IASCHA.Item) > Decimal("4060"):
            return 1
        else:
            return 0
    elif IAFS() == 2 or IAFS() == 5 or IAFS() == 6:
        if get_currency(IASCHA.Item) > Decimal("5000"):
            return 1
        else:
            return 0
    elif get_currency(IASCHA.Item) > Decimal("2030"):
        return 1
    else:
        return 0

def LastName_Calculation():
    return get_string(USWBasicInfo.LastName)

def LowInc_Calculation():
    if get_bool(IAREQUIRED.LowInc) == True:
        return 'LOW INCOME EXEMPTION'
    else:
        return ''

def MFJ_Calculation():
    if FedFS() == 2:
        if ( get_currency(USWRec.TAGI) < Decimal("2633") )  or  ( get_currency(USWRec.SAGI) < Decimal("2633") ) :
            return 1
        else:
            return 0
    else:
        return 0

def MFS_Calculation():
    if FedFS() == 3:
        return 1
    else:
        return 0

def MFSItm_Calculation():
    if get_bool(USF1040.MfsItm) == True and IAFS() == 4:
        return 1
    else:
        return 0

def MFSName_Calculation():
    if get_bool(IAF1040.MFS) == True:
        if trim(get_string(USWBasicInfo.L2Name)) != '':
            return get_string(USWBasicInfo.L2Name)
        else:
            return get_string(USWBasicInfo.SPFnI) + ' ' + get_string(USWBasicInfo.SpouseLast)
    else:
        return ''

def MFSSSN_Calculation():
    if get_bool(IAF1040.MFS) == True:
        return get_string(USWBasicInfo.SpouseSSN)
    else:
        return ''

def Over65_Calculation():
    SixtyFive = Long()

    SPSixtyFive = Long()
    if get_number(USWBasicInfo.TPAgeRec) >= 65:
        SixtyFive = 1
    else:
        SixtyFive = 0
    if get_number(USWBasicInfo.SPAgeRec) >= 65 and get_bool(IAREQUIRED.AskSpouse) == True:
        SPSixtyFive = 1
    else:
        SPSixtyFive = 0
    if SixtyFive + SPSixtyFive > 0:
        return 1
    else:
        return 0

def OVerPaid_Calculation():
    if get_bool(IA1040X.EFAmend) == True:
        return max_value(0, get_currency(IAF1040.TotCredit) - get_currency(IA1040X.PrevOP) - get_currency(IAF1040.TotTaxCont))
    else:
        return max_value(0, get_currency(IAF1040.TotCredit) - get_currency(IAF1040.TotTaxCont))

def Owe_Calculation():
    if get_bool(IA1040X.EFAmend) == True:
        if ( get_currency(IAF1040.Penalty) + get_currency(IA1040X.PrevOP) + get_currency(IAF1040.TotTaxCont) )  - get_currency(IAF1040.TotCredit) > 0:
            return max_value(0, get_currency(IAF1040.TotTaxCont) + get_currency(IA1040X.PrevOP) - get_currency(IAF1040.TotCredit))
        else:
            return 0
    else:
        if ( get_currency(IAF1040.Penalty) + get_currency(IAF1040.TotTaxCont) )  - get_currency(IAF1040.TotCredit) > 0:
            return max_value(0, get_currency(IAF1040.TotTaxCont) - get_currency(IAF1040.TotCredit))
        else:
            return 0

def PC1a_Calculation():
    if IAFS() == 2:
        return 2
    elif IAFS() == 5:
        return 2
    else:
        return 1

def PC1b_Calculation():
    SixtyFive = Long()

    Blind = Long()
    if IAFS() == 2:
        SixtyFive = get_bool(USWBasicInfo.SixtyFive) + get_bool(USWBasicInfo.Spouse65)
        Blind = get_bool(USWBasicInfo.Blind) + get_bool(USWBasicInfo.SpBlind)
    else:
        SixtyFive = get_bool(USWBasicInfo.SixtyFive)
        Blind = get_bool(USWBasicInfo.Blind)
    return Blind + SixtyFive

def PC2a_Calculation():
    if IAFS() == 3:
        return 1
    else:
        return 0

def PC2b_Calculation():
    if IAFS() == 3:
        return get_bool(USWBasicInfo.Spouse65) + get_bool(USWBasicInfo.SpBlind)
    else:
        return 0

def Penalty_Calculation():
    if get_bool(IA1040X.EFAmend) == True:
        return 0
    else:
        return get_currency(IA2210.Penalty) + get_currency(IA2210SP.Penalty)

def PenInt_Calculation():
    if get_currency(IAF1040.Owe) > 0:
        return get_currency(IAF1040.Pen74) + get_currency(IAF1040.Int74)
    else:
        return 0

def Phone_Calculation():
    return get_string(USWBasicInfo.Dayphone)

def PrepID_Calculation():
    return get_string(USWBasicInfo.PrepSSN)

def PrepPhone_Calculation():
    if trim(get_string(USWBasicInfo.PrepPhone)) != '':
        return get_string(USWBasicInfo.PrepPhone)
    else:
        return get_string(USWBasicInfo.PrepForPhone)

def QualWidow_Calculation():
    if FedFS() == 5:
        return 1
    else:
        return 0

def RefBalDue_Calculation():
    return Round(get_currency(IAF1040.Refund) - get_currency(IAF1040.TotDue))

def Refund_Calculation():
    return max_value(0, get_currency(IAF1040.OVerPaid) - get_currency(IAF1040.BApply99) - get_currency(IAF1040.AApply99) - get_currency(IAF1040.Penalty))

def Route_Calculation():
    if get_bool(IAEFWKSHT.PrepBPTrans) == True:
        return ''
    elif get_bool(IAEFWKSHT.DirDeposit) == True and get_bool(IAEFWKSHT.Yes) == False and get_currency(IAEFWKSHT.Refund) > 0:
        return get_string(IAEFWKSHT.DirDepRTN)
    else:
        return ''

def SaveCheck_Calculation():
    if get_bool(IAEFWKSHT.PrepBPTrans) == True:
        return 0
    elif get_bool(IAEFWKSHT.DirDeposit) == True and get_bool(IAEFWKSHT.Yes) == False and get_currency(IAEFWKSHT.Refund) > 0:
        return get_bool(IAEFWKSHT.DirDepSavings)
    else:
        return 0

def SchNo_Calculation():
    return get_string(USZIA1040.IAPYSchool)

def SchRate_Calculation():
    return SchSurtaxRate(get_number(IAF1040.SchNo))

def Single_Calculation():
    if FedFS() == 1:
        return 1
    else:
        return 0

def SPDateDeath_Calculation():
    if get_bool(IAF1040.SPDeceased) == True:
        return get_string(USWBasicInfo.SpDeath)
    else:
        return ''

def SPDeceased_Calculation():
    if get_bool(USWBasicInfo.SpDeceased) == True and get_bool(IAREQUIRED.AskSpouse) == True:
        return 1
    else:
        return 0

def SpouseFirst_Calculation():
    if get_bool(IAF1040.MFJ) == True or get_bool(IAF1040.CombMFS) == True:
        return get_string(USWBasicInfo.SPFnI)
    else:
        return ''

def SpouseLast_Calculation():
    if get_bool(IAF1040.MFJ) == True or get_bool(IAF1040.CombMFS) == True:
        return get_string(USWBasicInfo.SpouseLast)
    else:
        return ''

def SpouseSSN_Calculation():
    if get_bool(IAF1040.MFJ) == True or get_bool(IAF1040.CombMFS) == True:
        return get_string(USWBasicInfo.SpouseSSN)
    else:
        return ''

def SSN_Calculation():
    return get_string(USWBasicInfo.SSN)

def StadCheck_Calculation():
    if get_bool(IAF1040.ItemCheck) == True:
        return 0
    else:
        return 1

def TaxRed_Calculation():
    if get_bool(IAREQUIRED.LowInc) == True:
        return ''
    elif IAFS() != 1 or get_bool(IAF1040.DepY) == True:
        return ''
    elif get_currency(IAF1040.ABal1) < get_currency(IAREQUIRED.TentTax):
        return 'tax reduction'
    else:
        return ''

def TotalTax_Calculation():
    if get_bool(IAREQUIRED.LowInc) == True:
        return 0
    else:
        return get_currency(IAF1040.BTaxB4Cont) + get_currency(IAF1040.ATaxB4Cont)

def TotContrib_Calculation():
    return get_currency(IAF1040.Wild) + get_currency(IAF1040.Fair) + get_currency(IAF1040.FFVet) + get_currency(IAF1040.ChildAbuse)

def TotCredit_Calculation():
    return get_currency(IAF1040.BTot67) + get_currency(IAF1040.ATot67)

def TotDC1_Calculation():
    return c_dollar(get_float(IAF1040.DC1) * 4000)

def TotDC2_Calculation():
    if get_bool(IAF1040.CombMFS) == True:
        return c_dollar(get_float(IAF1040.DC2) * 4000)
    else:
        return 0

def TotDue_Calculation():
    if get_currency(IAF1040.Refund) > 0:
        return 0
    elif get_currency(IAF1040.Refund) == 0 and get_currency(IAF1040.OVerPaid) > 0:
        if get_bool(IA1040X.EFAmend) == True:
            return max_value(0, ( get_currency(IAF1040.TotTaxCont) + get_currency(IA1040X.PrevOP) + get_currency(IAF1040.Penalty) + get_currency(IAF1040.PenInt) )  - get_currency(IAF1040.TotCredit))
        else:
            return max_value(0, ( get_currency(IAF1040.TotTaxCont) + get_currency(IAF1040.Penalty) + get_currency(IAF1040.PenInt) )  - get_currency(IAF1040.TotCredit))
    else:
        return get_currency(IAF1040.Owe) + get_currency(IAF1040.Penalty) + get_currency(IAF1040.PenInt)

def TotPC2a_Calculation():
    return c_dollar(get_float(IAF1040.PC2a) * 4000)

def TotPC2b_Calculation():
    return c_dollar(get_float(IAF1040.PC2b) * 2000)

def TotPCa_Calculation():
    return c_dollar(get_float(IAF1040.PC1a) * 4000)

def TotPCb_Calculation():
    return c_dollar(get_float(IAF1040.PC1b) * 2000)

def TotTaxCont_Calculation():
    return get_currency(IAF1040.TotalTax) + get_currency(IAF1040.TotContrib)

def TPDateDeath_Calculation():
    if get_bool(IAF1040.TPDeceased) == True:
        return get_string(USWBasicInfo.YouDeath)
    else:
        return ''

def TPDeceased_Calculation():
    if get_bool(USWBasicInfo.TpDeceased) == True:
        return 1
    else:
        return 0

def UsedAI_Calculation():
    if get_bool(IA2210AN.Print) == True:
        return 1
    elif get_bool(IA2210ANSP.Print) == True:
        return 1
    else:
        return 0


