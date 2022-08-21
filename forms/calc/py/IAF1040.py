from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def AAlimony_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(USWRec.TAlimony)
    else:
        ReturnVal = GetCurrency(USWRec.TotAlimony)

def AAlimonyP_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(USWRec.TAlimonyAdj)
    else:
        ReturnVal = GetCurrency(USWRec.TotAlimonyAdj)

def AAltTax_Calculation():
    # 1st condition added for situation when MFS return and reporting spouse income causes an alternate tax calculation yet taxpayer has zero income
    # See saved return IA MFS Alternate Tax Issue.ta2
    if GetBool(IAF1040.MFS) == True and GetCurrency(IAF1040.ATaxInc) == 0:
        ReturnVal = 0
    elif  ( GetCurrency(IAWkAltTax.Mult) < GetCurrency(IAWkAltTax.Tables) )  and GetBool(IAWkAltTax.Qualify) == True:
        ReturnVal = GetCurrency(IAF1040.ATax)
    else:
        ReturnVal = GetCurrency(IAF1040.ARegTax)

def AApply99_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAEstimates.TotApplied) - GetCurrency(IAF1040.BApply99))

def ABal1_Calculation():
    if IAFS() == 1 and GetBool(IAF1040.DepY) == False:
        ReturnVal = GetCurrency(IARequired.TaxReduction)
    else:
        ReturnVal = MaxValue(0, GetCurrency(IAF1040.ATotIATax) - GetCurrency(IAF1040.ACredits))

def ABal2_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAF1040.ABal1) - GetCurrency(IAF1040.ACrNon))

def ABal4_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAF1040.ABal3) - GetCurrency(IAF1040.AOthIACr))

def ABal36_Calculation():
    ReturnVal = GetCurrency(IAF1040.ABalance)

def ABal3_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAF1040.ABal2) - GetCurrency(IAF1040.AOutState))

def ABalance_Calculation():
    ReturnVal = GetCurrency(IAF1040.ATotTax) - GetCurrency(IAF1040.AFedDed)

def ABusInc_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(USWRec.TBusiness)
    else:
        ReturnVal = GetCurrency(USWRec.TotBusiness)

def ABusIncL_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(USWRec.THalfSe)
    else:
        ReturnVal = GetCurrency(USWRec.TotHalfSE)

def ACapGain_Calculation():
    CapGain = Currency()
    if GetBool(USWResidency.F1040NR) == False:
        CapGain = GetCurrency(USF1040.CapGain)
    else:
        CapGain = GetCurrency(USF1040NR.CapGain)
    if IAFS() == 3:
        ReturnVal = CapGain - GetCurrency(IAF1040.BCapGain)
    else:
        ReturnVal = CapGain

def AChild_Calculation():
    if GetBool(IAF1040.ChildCareCk) == True:
        ReturnVal = GetCurrency(IAChildCredit.TChild)
    elif GetBool(IAF1040.EarlyChildCk) == True:
        ReturnVal = GetCurrency(IAChildCredit.TEarly)
    else:
        ReturnVal = 0

def ACredits_Calculation():
    ReturnVal = GetCurrency(IAF1040.AExemCr) + GetCurrency(IAF1040.ATuit) + GetCurrency(IAF1040.AVolFireCr)

def ACrNon_Calculation():
    ReturnVal = GetCurrency(IAF126.ACredit)

def ActNum_Calculation():
    if GetBool(IAEFWksht.PrepBPTrans) == True:
        ReturnVal = ''
    elif GetBool(IAEFWksht.DirDeposit) == True and GetBool(IAEFWksht.Yes) == False and GetCurrency(IAEFWksht.Refund) > 0:
        ReturnVal = GetString(IAEFWksht.DirDepDan)
    else:
        ReturnVal = ''

def Add_Calculation():
    ReturnVal = GetString(USWBasicInfo.HomeComb)

def ADedBox_Calculation():
    Itemized = Currency()

    Deduction = Currency()
    # updated for 2018
    if GetBool(IAF1040.CombMFS) == True or GetBool(IAF1040.MFS) == True:
        Itemized = GetCurrency(IASchA.YouPC)
    else:
        Itemized = GetCurrency(IASchA.Item)
    if GetBool(IAF1040.ItemCheck) == True:
        Deduction = Itemized
    elif IAFS() == 2 or IAFS() == 5 or IAFS() == 6:
        Deduction = MinValue(Decimal("5000"), GetCurrency(IAF1040.ABal36))
    else:
        Deduction = MinValue(Decimal("2030"), GetCurrency(IAF1040.ABal36))
    ReturnVal = MaxValue(0, Deduction)

def ADividend_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IARequired.TotTPDiv)
    else:
        ReturnVal = GetCurrency(IARequired.TotDiv)

def AEst_Calculation():
    if GetBool(IA1040X.EFAmend) == True:
        ReturnVal = MaxValue(0, GetCurrency(IAStateEst.TotIAEst) - GetCurrency(IAStateEst.SPIAEst)) + GetCurrency(IA1040X.TotPrevTax)
    else:
        ReturnVal = MaxValue(0, GetCurrency(IAStateEst.TotIAEst) - GetCurrency(IAStateEst.SPIAEst))

def AEstTax_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IAFedEst.TPTotEst)
    else:
        ReturnVal = GetCurrency(IAFedEst.TPTotEst) + GetCurrency(IAFedEst.SPTotEst)

def AExemCr_Calculation():
    ReturnVal = GetCurrency(IAF1040.ExempA)

def AFarm_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(USWRec.TFarm)
    else:
        ReturnVal = GetCurrency(USWRec.TotFarm)

def AFedDed_Calculation():
    ReturnVal = GetCurrency(IAF1040.ATaxWith) + GetCurrency(IAF1040.AEstTax) + GetCurrency(IAF1040.APrior)

def AFedTax_Calculation():
    ReturnVal = GetCurrency(IAF1040.ARefund) + GetCurrency(IAF1040.ASelf)

def AFuel_Calculation():
    ReturnVal = GetCurrency(IASch4136.TotCr, FieldCopies(IASch4136.Taxpayer))

def AGamble_Calculation():
    if GetBool(USWResidency.F1040NR) == True:
        ReturnVal = GetCurrency(USSchNEC.Gambling130) + GetCurrency(USSchNEC.Gambling1Oth) + GetCurrency(USSchNEC.Gambling10) + GetCurrency(USSchNEC.Gambling230) + GetCurrency(USSchNEC.Gambling2Oth)
    elif IAFS() == 3:
        ReturnVal = GetCurrency(USWOthInc.TPOth3)
    else:
        ReturnVal = GetCurrency(USWOthInc.TotGamb)

def AGross_Calculation():
    ReturnVal = GetCurrency(IAF1040.AWages) + GetCurrency(IAF1040.AInterest) + GetCurrency(IAF1040.ADividend) + GetCurrency(IAF1040.AAlimony) + GetCurrency(IAF1040.ABusInc) + GetCurrency(IAF1040.ACapGain) + GetCurrency(IAF1040.AOthGain) + GetCurrency(IAF1040.AIRA) + GetCurrency(IAF1040.APensions) + GetCurrency(IAF1040.ARents) + GetCurrency(IAF1040.AFarm) + GetCurrency(IAF1040.AUnemp) + GetCurrency(IAF1040.AGamble) + GetCurrency(IAF1040.AOtherInc)

def AHealth_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IAWHealth.TPTotal)
    else:
        ReturnVal = GetCurrency(IAWHealth.TPTotal) + GetCurrency(IAWHealth.SPTotal)

def AIAMin_Calculation():
    ReturnVal = GetCurrency(IA6251.TotAMT)

def AIATaxWith_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IARequired.TIAW2WH) + GetCurrency(IARequired.TPW2GWH) + GetCurrency(IARequired.Tot1042S) + GetCurrency(IARequired.TPCapGainWH) + GetCurrency(IARequired.TPDivWH) + GetCurrency(IARequired.TPUnemWH) + GetCurrency(IARequired.TPIntWH) + GetCurrency(IARequired.TPKWH) + GetCurrency(IARequired.TPMiscWH) + GetCurrency(IARequired.TPOIDWH) + GetCurrency(IARequired.T1099rWH) + GetCurrency(IARequired.TpOthIncWH)
    else:
        ReturnVal = GetCurrency(IARequired.TotIAW2WH) + GetCurrency(IARequired.TotW2GWH) + GetCurrency(IARequired.Tot1042S) + GetCurrency(IARequired.TotCapGainWH) + GetCurrency(IARequired.TotDivWH) + GetCurrency(IARequired.TotUnemWH) + GetCurrency(IARequired.TotIntWH) + GetCurrency(IARequired.TotKWH) + GetCurrency(IARequired.TotMiscWH) + GetCurrency(IARequired.TotOIDWH) + GetCurrency(IARequired.Tot1099rWH) + GetCurrency(IARequired.TotOthIncWH)

def AIEIC_Calculation():
    if IAFS() == 3 or IAFS() == 4:
        ReturnVal = GetCurrency(IARequired.TIAEic)
    else:
        ReturnVal = GetCurrency(IARequired.IAEic)

def AInterest_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IARequired.TotTPInt)
    else:
        ReturnVal = GetCurrency(IARequired.TotInt)

def AIRA_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IAWPenExc.TPIRA)
    else:
        ReturnVal = GetCurrency(IAWPenExc.TPIRA) + GetCurrency(IAWPenExc.SPIRA)

def AKeogh_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(USWRec.TKeough) + GetCurrency(IARequired.TIRA)
    else:
        ReturnVal = GetCurrency(USWRec.TotKeough) + GetCurrency(USWRec.TotIRAAdj)

def ALump_Calculation():
    if IAFS() == 3:
        ReturnVal = CDollar(GetFloat(USF4972.Tax) * 0.25)
    else:
        ReturnVal = CDollar(GetFloat(USF4972.Tax) * 0.25) + CDollar(GetFloat(USF4972Spouse.Tax) * 0.25)

def AMove_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IARequired.TMove)
    else:
        ReturnVal = GetCurrency(IARequired.TotMove)

def ANet_Calculation():
    ReturnVal = GetCurrency(IAF1040.AGross) - GetCurrency(IAF1040.ATotAdj)

def AOthAdj_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IAOthAdj.TPTot)
    else:
        ReturnVal = GetCurrency(IAOthAdj.TPTot) + GetCurrency(IAOthAdj.SPTot)

def AOtherInc_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IAWOthInc.TPTot)
    else:
        ReturnVal = GetCurrency(IAWOthInc.TPTot) + GetCurrency(IAWOthInc.SPTot)

def AOthGain_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(USWRec.TOthGain)
    else:
        ReturnVal = GetCurrency(USWRec.TotOthGain)

def AOthIACr_Calculation():
    ReturnVal = GetCurrency(IA148.TotNonRefCr)

def AOthRefCr_Calculation():
    ReturnVal = GetCurrency(IA148.TotRefCr)

def AOutState_Calculation():
    ReturnVal = GetCurrency(IA130.TPCredit)

def APenalty_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(USWRec.TEarlyPen)
    else:
        ReturnVal = GetCurrency(USWRec.TotEarlyPen)

def APenExcl_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IAWPenExc.TPPenExc)
    else:
        ReturnVal = GetCurrency(IAWPenExc.TPPenExc) + GetCurrency(IAWPenExc.SPPenExc)

def APensions_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IAWPenExc.TPPensions)
    else:
        ReturnVal = GetCurrency(IAWPenExc.TPPensions) + GetCurrency(IAWPenExc.SPPensions)

def APrior_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IAAddFedTax.TPTotal)
    else:
        ReturnVal = GetCurrency(IAAddFedTax.TPTotal) + GetCurrency(IAAddFedTax.SPTotal)

def ARefund_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IAFedRef.TPST)
    else:
        ReturnVal = GetCurrency(IAFedRef.SPST) + GetCurrency(IAFedRef.TPST)

def ARegTax_Calculation():
    Mid = Currency()

    MidInt = Long()

    TotTaxInc = Currency()
    # updated for 2018
    TotTaxInc = GetCurrency(IAF1040.ATaxInc)
    if TotTaxInc > Decimal("95650"):
        Mid = TotTaxInc
    elif TotTaxInc > Decimal("150"):
        MidInt = CLng(( TotTaxInc - Decimal("1") )  / Decimal("50"))
        Mid = ( CCur(MidInt) * Decimal("50") )  + Decimal("25")
    else:
        Mid = Decimal("0")
    ReturnVal = Tax(Mid)

def ARents_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(USWRec.TRental)
    else:
        ReturnVal = GetCurrency(USWRec.TotRental)

def ARepSSB_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IAWkSSB.TPRepSSB)
    else:
        ReturnVal = GetCurrency(IAWkSSB.ReportSSB)

def ASch_Calculation():
    ReturnVal = CDollar(GetFloat(IAF1040.ABal4) * GetFloat(IAF1040.SchRate))

def ASelf_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IASETax.TPTotal)
    else:
        ReturnVal = GetCurrency(IASETax.TPTotal) + GetCurrency(IASETax.SPTotal)

def ATax_Calculation():
    if GetNumber(IAWkAltTax.ProRate) == 1:
        ReturnVal = GetCurrency(IAWkAltTax.ATax)
    else:
        ReturnVal = GetCurrency(IAWkAltTax.Lesser)

def ATaxB4Cont_Calculation():
    ReturnVal = GetCurrency(IAF1040.ABal4) + GetCurrency(IAF1040.ASch)

def ATaxInc_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAF1040.ABal36) - GetCurrency(IAF1040.ADedBox))

def ATaxWith_Calculation():
    TotWH = Currency()
    if GetBool(USWResidency.F1040NR) == True:
        TotWH = GetCurrency(USF1040NR.WHW2) + GetCurrency(USF1040NR.WH8805) + GetCurrency(USF1040NR.WH8288A) + GetCurrency(USF1040NR.WH1042S)
    else:
        TotWH = GetCurrency(USF1040.WH) + Round(GetCurrency(USDW2AS.ASWH, FieldCopies(USDW2AS.Taxpayer))) + Round(GetCurrency(USDW2VI.VIWH, FieldCopies(USDW2VI.Taxpayer)))
    if IAFS() == 3:
        ReturnVal = MaxValue(0, TotWH - GetCurrency(IAF1040.BTaxWith))
    else:
        ReturnVal = TotWH

def ATot67_Calculation():
    ReturnVal = GetCurrency(IAF1040.AFuel) + GetCurrency(IAF1040.AChild) + GetCurrency(IAF1040.AIEIC) + GetCurrency(IAF1040.AOthRefCr) + GetCurrency(IAF1040.AIATaxWith) + GetCurrency(IAF1040.AEst)

def ATotAdj_Calculation():
    ReturnVal = GetCurrency(IAF1040.AKeogh) + GetCurrency(IAF1040.ABusIncL) + GetCurrency(IAF1040.AHealth) + GetCurrency(IAF1040.APenalty) + GetCurrency(IAF1040.AAlimonyP) + GetCurrency(IAF1040.APenExcl) + GetCurrency(IAF1040.AMove) + GetCurrency(IAF1040.AGainDed) + GetCurrency(IAF1040.AOthAdj)

def ATotIATax_Calculation():
    ReturnVal = GetCurrency(IAF1040.AAltTax) + GetCurrency(IAF1040.ALump) + GetCurrency(IAF1040.AIAMin)

def ATotTax_Calculation():
    ReturnVal = GetCurrency(IAF1040.ANet) + GetCurrency(IAF1040.AFedTax)

def ATuit_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IATuition.TTuit)
    else:
        ReturnVal = GetCurrency(IATuition.TotCr)

def AUnemp_Calculation():
    if IAFS() == 3:
        ReturnVal = MaxValue(0, GetCurrency(USWRec.TUnem) - Round(GetCurrency(USWUnempl.RRBSub, FieldCopies(USWUnempl.Taxpayer))))
    else:
        ReturnVal = MaxValue(0, GetCurrency(USWRec.TotUnem) - Round(GetCurrency(USWUnempl.RRBSub)))

def AVolFireCr_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IAFireCr.TPTotCr)
    else:
        ReturnVal = GetCurrency(IAFireCr.TPTotCr) + GetCurrency(IAFireCr.SPTotCr)

def AWages_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(USWRec.TWages)
    else:
        ReturnVal = GetCurrency(USWRec.TotWages)

def BAlimony_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(USWRec.SAlimony)
    else:
        ReturnVal = 0

def BAlimonyP_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(USWRec.SAlimonyAdj)
    else:
        ReturnVal = 0

def BAltTax_Calculation():
    if IAFS() == 3:
        if ( GetCurrency(IAWkAltTax.Mult) < GetCurrency(IAWkAltTax.Tables) )  and GetBool(IAWkAltTax.Qualify) == True:
            ReturnVal = GetCurrency(IAF1040.BTax)
        else:
            ReturnVal = GetCurrency(IAF1040.BRegTax)
    else:
        ReturnVal = 0

def BApply99_Calculation():
    ReturnVal = MinValue(GetCurrency(IAF1040.OVerPaid), GetCurrency(IAEstimates.TotApplied, FieldCopies(IAEstimates.Spouse)))

def BBal1_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAF1040.BTotIATax) - GetCurrency(IAF1040.BCredits))

def BBal2_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAF1040.BBal1) - GetCurrency(IAF1040.BCrNon))

def BBal4_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAF1040.BBal3) - GetCurrency(IAF1040.BOthIACr))

def BBal36_Calculation():
    ReturnVal = GetCurrency(IAF1040.BBalance)

def BBal3_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAF1040.BBal2) - GetCurrency(IAF1040.BOutState))

def BBalance_Calculation():
    ReturnVal = GetCurrency(IAF1040.BTotTax) - GetCurrency(IAF1040.BFedDed)

def BBusInc_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(USWRec.SBusiness)
    else:
        ReturnVal = 0

def BBusIncL_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(USWRec.SHalfSe)
    else:
        ReturnVal = 0

def BCapGain_Calculation():
    if IAFS() == 3:
        if GetCurrency(USWDRec.CapGain) < Decimal("0"):
            ReturnVal = GetCurrency(IARequired.SLimLoss)
        else:
            ReturnVal = GetCurrency(USWDRec.SCapGain)
    else:
        ReturnVal = 0

def BChild_Calculation():
    if IAFS() == 3:
        if GetBool(IAF1040.ChildCareCk) == True:
            ReturnVal = GetCurrency(IAChildCredit.SChild)
        elif GetBool(IAF1040.EarlyChildCk) == True:
            ReturnVal = GetCurrency(IAChildCredit.SEarly)
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def BCredits_Calculation():
    ReturnVal = GetCurrency(IAF1040.BExemCr) + GetCurrency(IAF1040.BTuit) + GetCurrency(IAF1040.BVolFireCr)

def BCrNon_Calculation():
    if IAFS() == 3:
        if GetBool(IAF126.SpNonRes) == True or GetBool(IAF126.SpPYRes) == True:
            ReturnVal = GetCurrency(IAF126.BCredit)
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def BDedBox_Calculation():
    Deduction = Currency()
    # updated for 2018
    if IAFS() == 3:
        if GetBool(IAF1040.ItemCheck) == True:
            Deduction = GetCurrency(IASchA.SpPro)
        else:
            Deduction = MinValue(Decimal("2030"), GetCurrency(IAF1040.BBal36))
    else:
        Deduction = 0
    ReturnVal = MaxValue(0, Deduction)

def BDividend_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IARequired.TotSPDiv)
    else:
        ReturnVal = 0

def BEst_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IAStateEst.SPIAEst)
    else:
        ReturnVal = 0

def BEstTax_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IAFedEst.SPTotEst)
    else:
        ReturnVal = 0

def BExemCr_Calculation():
    ReturnVal = GetCurrency(IAF1040.ExempB)

def BFarm_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(USWRec.SFarm)
    else:
        ReturnVal = 0

def BFedDed_Calculation():
    ReturnVal = GetCurrency(IAF1040.BTaxWith) + GetCurrency(IAF1040.BEstTax) + GetCurrency(IAF1040.BPrior)

def BFedTax_Calculation():
    ReturnVal = GetCurrency(IAF1040.BRefund) + GetCurrency(IAF1040.BSelf)

def BFuel_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IASch4136.TotCr, FieldCopies(IASch4136.Spouse))
    else:
        ReturnVal = 0

def BGamble_Calculation():
    if IAFS() == 3 and GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.SPOth3)
    else:
        ReturnVal = 0

def BGross_Calculation():
    ReturnVal = GetCurrency(IAF1040.BWages) + GetCurrency(IAF1040.BInterest) + GetCurrency(IAF1040.BDividend) + GetCurrency(IAF1040.BAlimony) + GetCurrency(IAF1040.BBusInc) + GetCurrency(IAF1040.BCapGain) + GetCurrency(IAF1040.BOthGain) + GetCurrency(IAF1040.BIRA) + GetCurrency(IAF1040.BPensions) + GetCurrency(IAF1040.BRents) + GetCurrency(IAF1040.BFarm) + GetCurrency(IAF1040.BUnemp) + GetCurrency(IAF1040.BGamble) + GetCurrency(IAF1040.BOtherInc)

def BHealth_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IAWHealth.SPTotal)
    else:
        ReturnVal = 0

def BIAMin_Calculation():
    ReturnVal = GetCurrency(IA6251Sp.TotAMT)

def BIATaxWith_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IARequired.SIAW2WH) + GetCurrency(IARequired.SPW2GWH) + GetCurrency(IARequired.SPCapGainWH) + GetCurrency(IARequired.SPDivWH) + GetCurrency(IARequired.SPUnemWH) + GetCurrency(IARequired.SPIntWH) + GetCurrency(IARequired.SPKWH) + GetCurrency(IARequired.SPMiscWH) + GetCurrency(IARequired.SPOIDWH) + GetCurrency(IARequired.S1099RWH) + GetCurrency(IARequired.SPOthIncWH)
    else:
        ReturnVal = 0

def BIEIC_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IARequired.SIaEIC)
    else:
        ReturnVal = 0

def BInterest_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IARequired.TotSPInt)
    else:
        ReturnVal = 0

def BIRA_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IAWPenExc.SPIRA)
    else:
        ReturnVal = 0

def BKeogh_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(USWRec.SKeough) + GetCurrency(IARequired.SIRA)
    else:
        ReturnVal = 0

def BLump_Calculation():
    if IAFS() == 3:
        ReturnVal = CDollar(GetFloat(USF4972Spouse.Tax) * 0.25)
    else:
        ReturnVal = 0

def BMove_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IARequired.SMove)
    else:
        ReturnVal = 0

def BNet_Calculation():
    ReturnVal = GetCurrency(IAF1040.BGross) - GetCurrency(IAF1040.BTotAdj)

def BOthAdj_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IAOthAdj.SPTot)
    else:
        ReturnVal = 0

def BOtherInc_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IAWOthInc.SPTot)
    else:
        ReturnVal = 0

def BOthGain_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(USWRec.SOthGain)
    else:
        ReturnVal = 0

def BOthIACr_Calculation():
    ReturnVal = GetCurrency(IA148Sp.TotNonRefCr)

def BOthRefCr_Calculation():
    ReturnVal = GetCurrency(IA148Sp.TotRefCr)

def BOutState_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IA130.SPCredit)
    else:
        ReturnVal = 0

def BPenalty_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(USWRec.SEarlyPen)
    else:
        ReturnVal = 0

def BPenExcl_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IAWPenExc.SPPenExc)
    else:
        ReturnVal = 0

def BPensions_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IAWPenExc.SPPensions)
    else:
        ReturnVal = 0

def BPrior_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IAAddFedTax.SPTotal)
    else:
        ReturnVal = 0

def BRefund_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IAFedRef.SPST)
    else:
        ReturnVal = 0

def BRegTax_Calculation():
    Mid = Currency()

    MidInt = Long()

    TotTaxInc = Currency()
    # updated for 2018
    if GetBool(IAF1040.MFS) == True:
        TotTaxInc = GetCurrency(IAF1040.SpTaxInc)
    else:
        TotTaxInc = GetCurrency(IAF1040.BTaxInc)
    if TotTaxInc > Decimal("95650"):
        Mid = TotTaxInc
    elif TotTaxInc > Decimal("150"):
        MidInt = CLng(( TotTaxInc - Decimal("1") )  / Decimal("50"))
        Mid = ( CCur(MidInt) * Decimal("50") )  + Decimal("25")
    else:
        Mid = Decimal("0")
    ReturnVal = Tax(Mid)

def BRents_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(USWRec.SRental)
    else:
        ReturnVal = 0

def BRepSSB_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IAWkSSB.SPRepSSB)
    else:
        ReturnVal = 0

def BSch_Calculation():
    ReturnVal = CDollar(GetFloat(IAF1040.BBal4) * GetFloat(IAF1040.SchRate))

def BSelf_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IASETax.SPTotal)
    else:
        ReturnVal = 0

def BTax_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IAWkAltTax.BTax)
    else:
        ReturnVal = 0

def BTaxB4Cont_Calculation():
    ReturnVal = GetCurrency(IAF1040.BBal4) + GetCurrency(IAF1040.BSch)

def BTaxInc_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAF1040.BBal36) - GetCurrency(IAF1040.BDedBox))

def BTaxWith_Calculation():
    JT = Currency()

    SPW2 = Currency()

    SP = Currency()
    JT = CDollar(CDbl(Round(GetCurrency(USD1099INT.WH, FieldCopies(USD1099INT.Joint))) + Round(GetCurrency(USD1099K.WH, FieldCopies(USD1099K.Joint))) + Round(GetCurrency(USD1099OID.WH, FieldCopies(USD1099OID.Joint))) + Round(GetCurrency(USD1099MISC.WH, FieldCopies(USD1099MISC.Joint))) + Round(GetCurrency(USD1099DIV.WH, FieldCopies(USD1099DIV.Joint))) + Round(GetCurrency(USDCapGain.WH2, FieldCopies(USDCapGain.Joint))) + Round(GetCurrency(USDPartK1.BackupWith, FieldCopies(USDPartK1.Joint))) + Round(GetCurrency(USDSCorpK1.BackupWith, FieldCopies(USDSCorpK1.Joint))) + Round(GetCurrency(USDEstK1.BackupWith, FieldCopies(USDEstK1.Joint)))) * 0.5)
    SPW2 = Round(GetCurrency(USDW2.WH, FieldCopies(USDW2.Spouse))) + Round(GetCurrency(USDW2AS.ASWH, FieldCopies(USDW2AS.Spouse))) + Round(GetCurrency(USDW2CM.CNMIWH, FieldCopies(USDW2CM.Spouse))) + Round(GetCurrency(USDW2GU.GuamWH, FieldCopies(USDW2GU.Spouse))) + Round(GetCurrency(USDW2VI.VIWH, FieldCopies(USDW2VI.Spouse)))
    SP = Round(GetCurrency(USD1099INT.WH, FieldCopies(USD1099INT.Spouse))) + Round(GetCurrency(USD1099K.WH, FieldCopies(USD1099K.Spouse))) + Round(GetCurrency(USD1099OID.WH, FieldCopies(USD1099OID.Spouse))) + Round(GetCurrency(USD1099DIV.WH, FieldCopies(USD1099DIV.Spouse))) + Round(GetCurrency(USD1099R.WH, FieldCopies(USD1099R.Spouse))) + Round(GetCurrency(USD1099MISC.WH, FieldCopies(USD1099MISC.Spouse))) + Round(GetCurrency(USWUnempl.TPFedWH, FieldCopies(USWUnempl.Spouse))) + Round(GetCurrency(USDW2G.WH, FieldCopies(USDW2G.Spouse))) + Round(GetCurrency(USDCapGain.WH2, FieldCopies(USDCapGain.Spouse))) + Round(GetCurrency(USDRRB1099R.WH, FieldCopies(USDRRB1099R.Spouse))) + Round(GetCurrency(USDPartK1.BackupWith, FieldCopies(USDPartK1.Spouse))) + Round(GetCurrency(USDSCorpK1.BackupWith, FieldCopies(USDSCorpK1.Spouse))) + Round(GetCurrency(USDEstK1.BackupWith, FieldCopies(USDEstK1.Spouse)))
    if IAFS() == 3:
        ReturnVal = JT + SPW2 + SP + GetCurrency(USWSSBDetail.SPFedWH) + GetCurrency(USWRec.SPTotAddMedTaxWH)
    else:
        ReturnVal = 0

def BTot67_Calculation():
    ReturnVal = GetCurrency(IAF1040.BFuel) + GetCurrency(IAF1040.BChild) + GetCurrency(IAF1040.BIEIC) + GetCurrency(IAF1040.BOthRefCr) + GetCurrency(IAF1040.BIATaxWith) + GetCurrency(IAF1040.BEst)

def BTotAdj_Calculation():
    ReturnVal = GetCurrency(IAF1040.BKeogh) + GetCurrency(IAF1040.BBusIncL) + GetCurrency(IAF1040.BHealth) + GetCurrency(IAF1040.BPenalty) + GetCurrency(IAF1040.BAlimonyP) + GetCurrency(IAF1040.BPenExcl) + GetCurrency(IAF1040.BMove) + GetCurrency(IAF1040.BGainDed) + GetCurrency(IAF1040.BOthAdj)

def BTotIATax_Calculation():
    ReturnVal = GetCurrency(IAF1040.BAltTax) + GetCurrency(IAF1040.BLump) + GetCurrency(IAF1040.BIAMin)

def BTotTax_Calculation():
    ReturnVal = GetCurrency(IAF1040.BNet) + GetCurrency(IAF1040.BFedTax)

def BTuit_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IATuition.STuit)
    else:
        ReturnVal = 0

def BUnemp_Calculation():
    if IAFS() == 3:
        ReturnVal = MaxValue(0, GetCurrency(USWRec.SUnem) - Round(GetCurrency(USWUnempl.RRBSub, FieldCopies(USWUnempl.Spouse))))
    else:
        ReturnVal = 0

def BVolFireCr_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IAFireCr.SPTotCr)
    else:
        ReturnVal = 0

def BWages_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(USWRec.SWages)
    else:
        ReturnVal = 0

def Checking_Calculation():
    if GetBool(IAEFWksht.PrepBPTrans) == True:
        ReturnVal = 0
    elif GetBool(IAEFWksht.DirDeposit) == True and GetBool(IAEFWksht.Yes) == False and GetCurrency(IAEFWksht.Refund) > 0:
        ReturnVal = GetBool(IAEFWksht.DirDepChecking)
    else:
        ReturnVal = 0

def ChildCareCk_Calculation():
    if GetCurrency(IAChildCredit.TotChDepCr) != 0 and GetCurrency(IAChildCredit.TotChDepCr) >= GetCurrency(IAChildCredit.TotCr):
        ReturnVal = 1
    else:
        ReturnVal = 0

def CityComb_Calculation():
    if Trim(GetString(USWBasicInfo.ForCountry)) != '':
        ReturnVal = GetString(USWBasicInfo.City) + ', ' + GetString(USWBasicInfo.ForeignCtry) + ' ' + GetString(USWBasicInfo.ForeignPC)
    else:
        ReturnVal = GetString(USWBasicInfo.CityComb)

def CombMFS_Calculation():
    if FedFS() == 2 and  ( GetCurrency(USWRec.TAGI) > Decimal("2632") )  and  ( GetCurrency(USWRec.SAGI) > Decimal("2632") ) :
        ReturnVal = 1
    else:
        ReturnVal = 0

def CountyNo_Calculation():
    ReturnVal = GetString(USZIA1040.IAPYCounty)

def DateDuePaid_Calculation():
    ReturnVal = MakeDate(4, 30, YearNumber + 1)

def DC1_Calculation():
    if IAFS() == 3:
        ReturnVal = MaxValue(0, GetNumber(USWAddDep.GrandTotDeps) - GetNumber(IAF1040.DC2))
    else:
        ReturnVal = GetNumber(USWAddDep.GrandTotDeps)

def DC2_Calculation():
    if IAFS() == 3:
        ReturnVal = CLng(Round(GetNumber(USWAddDep.GrandTotDeps) * GetFloat(IARequired.BProRate)))
    else:
        ReturnVal = 0

def DepN_Calculation():
    if GetBool(IAF1040.Single) == True:
        if GetBool(USWBasicInfo.Dopr) == True:
            ReturnVal = 0
        else:
            ReturnVal = 1
    else:
        ReturnVal = 0

def DepNames_Calculation():
    if GetNumber(IAF1040.DC1) > 0 or GetNumber(IAF1040.DC2) > 0:
        if GetNumber(IARequired.DepLength) > 23:
            ReturnVal = 'See Attached'
        else:
            ReturnVal = GetString(IARequired.DepNames)
    else:
        ReturnVal = ''

def DepY_Calculation():
    if GetBool(IAF1040.Single) == True:
        if GetBool(USWBasicInfo.Dopr) == True:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def Desc_Calculation():
    ReturnVal = GetString(IARequired.CombNames)

def EarlyChildCk_Calculation():
    if GetBool(IAF1040.ChildCareCk) == True:
        ReturnVal = 0
    elif GetCurrency(IAChildCredit.TotCr) != 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Email_Calculation():
    ReturnVal = GetString(USWBasicInfo.email)

def ExempA_Calculation():
    ReturnVal = GetCurrency(IAF1040.TotPCa) + GetCurrency(IAF1040.TotPCb) + GetCurrency(IAF1040.TotDC1)

def ExempB_Calculation():
    ReturnVal = GetCurrency(IAF1040.TotPC2a) + GetCurrency(IAF1040.TotPC2b) + GetCurrency(IAF1040.TotDC2)

def Exist_Calculation():
    ReturnVal = 1

def FirmID_Calculation():
    ReturnVal = GetString(USWBasicInfo.PrepEIN)

def FirstName_Calculation():
    ReturnVal = GetString(USWBasicInfo.TPFnI)

def HOH_Calculation():
    if FedFS() == 4:
        ReturnVal = 1
    else:
        ReturnVal = 0

def HOHDep_Calculation():
    ReturnVal = GetString(USWBasicInfo.L3Name)

def HOHSSN_Calculation():
    if GetBool(USF1040.HOH) == True:
        ReturnVal = GetString(USF1040.L3SSN)
    else:
        ReturnVal = ''

def ItemCheck_Calculation():
    # updated for 2018
    if GetBool(IAF1040.MFSItm) == True and IAFS() == 4:
        ReturnVal = 1
    elif IAFS() == 3:
        if GetCurrency(IASchA.Item) > Decimal("4060"):
            ReturnVal = 1
        else:
            ReturnVal = 0
    elif IAFS() == 2 or IAFS() == 5 or IAFS() == 6:
        if GetCurrency(IASchA.Item) > Decimal("5000"):
            ReturnVal = 1
        else:
            ReturnVal = 0
    elif GetCurrency(IASchA.Item) > Decimal("2030"):
        ReturnVal = 1
    else:
        ReturnVal = 0

def LastName_Calculation():
    ReturnVal = GetString(USWBasicInfo.LastName)

def LowInc_Calculation():
    if GetBool(IARequired.LowInc) == True:
        ReturnVal = 'LOW INCOME EXEMPTION'
    else:
        ReturnVal = ''

def MFJ_Calculation():
    if FedFS() == 2:
        if ( GetCurrency(USWRec.TAGI) < Decimal("2633") )  or  ( GetCurrency(USWRec.SAGI) < Decimal("2633") ) :
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def MFS_Calculation():
    if FedFS() == 3:
        ReturnVal = 1
    else:
        ReturnVal = 0

def MFSItm_Calculation():
    if GetBool(USF1040.MfsItm) == True and IAFS() == 4:
        ReturnVal = 1
    else:
        ReturnVal = 0

def MFSName_Calculation():
    if GetBool(IAF1040.MFS) == True:
        if Trim(GetString(USWBasicInfo.L2Name)) != '':
            ReturnVal = GetString(USWBasicInfo.L2Name)
        else:
            ReturnVal = GetString(USWBasicInfo.SPFnI) + ' ' + GetString(USWBasicInfo.SpouseLast)
    else:
        ReturnVal = ''

def MFSSSN_Calculation():
    if GetBool(IAF1040.MFS) == True:
        ReturnVal = GetString(USWBasicInfo.SpouseSSN)
    else:
        ReturnVal = ''

def Over65_Calculation():
    SixtyFive = Long()

    SPSixtyFive = Long()
    if GetNumber(USWBasicInfo.TPAgeRec) >= 65:
        SixtyFive = 1
    else:
        SixtyFive = 0
    if GetNumber(USWBasicInfo.SPAgeRec) >= 65 and GetBool(IARequired.AskSpouse) == True:
        SPSixtyFive = 1
    else:
        SPSixtyFive = 0
    if SixtyFive + SPSixtyFive > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def OVerPaid_Calculation():
    if GetBool(IA1040X.EFAmend) == True:
        ReturnVal = MaxValue(0, GetCurrency(IAF1040.TotCredit) - GetCurrency(IA1040X.PrevOP) - GetCurrency(IAF1040.TotTaxCont))
    else:
        ReturnVal = MaxValue(0, GetCurrency(IAF1040.TotCredit) - GetCurrency(IAF1040.TotTaxCont))

def Owe_Calculation():
    if GetBool(IA1040X.EFAmend) == True:
        if ( GetCurrency(IAF1040.Penalty) + GetCurrency(IA1040X.PrevOP) + GetCurrency(IAF1040.TotTaxCont) )  - GetCurrency(IAF1040.TotCredit) > 0:
            ReturnVal = MaxValue(0, GetCurrency(IAF1040.TotTaxCont) + GetCurrency(IA1040X.PrevOP) - GetCurrency(IAF1040.TotCredit))
        else:
            ReturnVal = 0
    else:
        if ( GetCurrency(IAF1040.Penalty) + GetCurrency(IAF1040.TotTaxCont) )  - GetCurrency(IAF1040.TotCredit) > 0:
            ReturnVal = MaxValue(0, GetCurrency(IAF1040.TotTaxCont) - GetCurrency(IAF1040.TotCredit))
        else:
            ReturnVal = 0

def PC1a_Calculation():
    if IAFS() == 2:
        ReturnVal = 2
    elif IAFS() == 5:
        ReturnVal = 2
    else:
        ReturnVal = 1

def PC1b_Calculation():
    SixtyFive = Long()

    Blind = Long()
    if IAFS() == 2:
        SixtyFive = GetBool(USWBasicInfo.SixtyFive) + GetBool(USWBasicInfo.Spouse65)
        Blind = GetBool(USWBasicInfo.Blind) + GetBool(USWBasicInfo.SpBlind)
    else:
        SixtyFive = GetBool(USWBasicInfo.SixtyFive)
        Blind = GetBool(USWBasicInfo.Blind)
    ReturnVal = Blind + SixtyFive

def PC2a_Calculation():
    if IAFS() == 3:
        ReturnVal = 1
    else:
        ReturnVal = 0

def PC2b_Calculation():
    if IAFS() == 3:
        ReturnVal = GetBool(USWBasicInfo.Spouse65) + GetBool(USWBasicInfo.SpBlind)
    else:
        ReturnVal = 0

def Penalty_Calculation():
    if GetBool(IA1040X.EFAmend) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(IA2210.Penalty) + GetCurrency(IA2210Sp.Penalty)

def PenInt_Calculation():
    if GetCurrency(IAF1040.Owe) > 0:
        ReturnVal = GetCurrency(IAF1040.Pen74) + GetCurrency(IAF1040.Int74)
    else:
        ReturnVal = 0

def Phone_Calculation():
    ReturnVal = GetString(USWBasicInfo.Dayphone)

def PrepID_Calculation():
    ReturnVal = GetString(USWBasicInfo.PrepSSN)

def PrepPhone_Calculation():
    if Trim(GetString(USWBasicInfo.PrepPhone)) != '':
        ReturnVal = GetString(USWBasicInfo.PrepPhone)
    else:
        ReturnVal = GetString(USWBasicInfo.PrepForPhone)

def QualWidow_Calculation():
    if FedFS() == 5:
        ReturnVal = 1
    else:
        ReturnVal = 0

def RefBalDue_Calculation():
    ReturnVal = Round(GetCurrency(IAF1040.Refund) - GetCurrency(IAF1040.TotDue))

def Refund_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAF1040.OVerPaid) - GetCurrency(IAF1040.BApply99) - GetCurrency(IAF1040.AApply99) - GetCurrency(IAF1040.Penalty))

def Route_Calculation():
    if GetBool(IAEFWksht.PrepBPTrans) == True:
        ReturnVal = ''
    elif GetBool(IAEFWksht.DirDeposit) == True and GetBool(IAEFWksht.Yes) == False and GetCurrency(IAEFWksht.Refund) > 0:
        ReturnVal = GetString(IAEFWksht.DirDepRTN)
    else:
        ReturnVal = ''

def SaveCheck_Calculation():
    if GetBool(IAEFWksht.PrepBPTrans) == True:
        ReturnVal = 0
    elif GetBool(IAEFWksht.DirDeposit) == True and GetBool(IAEFWksht.Yes) == False and GetCurrency(IAEFWksht.Refund) > 0:
        ReturnVal = GetBool(IAEFWksht.DirDepSavings)
    else:
        ReturnVal = 0

def SchNo_Calculation():
    ReturnVal = GetString(USZIA1040.IAPYSchool)

def SchRate_Calculation():
    ReturnVal = SchSurtaxRate(GetNumber(IAF1040.SchNo))

def Single_Calculation():
    if FedFS() == 1:
        ReturnVal = 1
    else:
        ReturnVal = 0

def SPDateDeath_Calculation():
    if GetBool(IAF1040.SPDeceased) == True:
        ReturnVal = GetString(USWBasicInfo.SpDeath)
    else:
        ReturnVal = ''

def SPDeceased_Calculation():
    if GetBool(USWBasicInfo.SpDeceased) == True and GetBool(IARequired.AskSpouse) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

def SpouseFirst_Calculation():
    if GetBool(IAF1040.MFJ) == True or GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetString(USWBasicInfo.SPFnI)
    else:
        ReturnVal = ''

def SpouseLast_Calculation():
    if GetBool(IAF1040.MFJ) == True or GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetString(USWBasicInfo.SpouseLast)
    else:
        ReturnVal = ''

def SpouseSSN_Calculation():
    if GetBool(IAF1040.MFJ) == True or GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetString(USWBasicInfo.SpouseSSN)
    else:
        ReturnVal = ''

def SSN_Calculation():
    ReturnVal = GetString(USWBasicInfo.SSN)

def StadCheck_Calculation():
    if GetBool(IAF1040.ItemCheck) == True:
        ReturnVal = 0
    else:
        ReturnVal = 1

def TaxRed_Calculation():
    if GetBool(IARequired.LowInc) == True:
        ReturnVal = ''
    elif IAFS() != 1 or GetBool(IAF1040.DepY) == True:
        ReturnVal = ''
    elif GetCurrency(IAF1040.ABal1) < GetCurrency(IARequired.TentTax):
        ReturnVal = 'tax reduction'
    else:
        ReturnVal = ''

def TotalTax_Calculation():
    if GetBool(IARequired.LowInc) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(IAF1040.BTaxB4Cont) + GetCurrency(IAF1040.ATaxB4Cont)

def TotContrib_Calculation():
    ReturnVal = GetCurrency(IAF1040.Wild) + GetCurrency(IAF1040.Fair) + GetCurrency(IAF1040.FFVet) + GetCurrency(IAF1040.ChildAbuse)

def TotCredit_Calculation():
    ReturnVal = GetCurrency(IAF1040.BTot67) + GetCurrency(IAF1040.ATot67)

def TotDC1_Calculation():
    ReturnVal = CDollar(GetFloat(IAF1040.DC1) * 4000)

def TotDC2_Calculation():
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = CDollar(GetFloat(IAF1040.DC2) * 4000)
    else:
        ReturnVal = 0

def TotDue_Calculation():
    if GetCurrency(IAF1040.Refund) > 0:
        ReturnVal = 0
    elif GetCurrency(IAF1040.Refund) == 0 and GetCurrency(IAF1040.OVerPaid) > 0:
        if GetBool(IA1040X.EFAmend) == True:
            ReturnVal = MaxValue(0, ( GetCurrency(IAF1040.TotTaxCont) + GetCurrency(IA1040X.PrevOP) + GetCurrency(IAF1040.Penalty) + GetCurrency(IAF1040.PenInt) )  - GetCurrency(IAF1040.TotCredit))
        else:
            ReturnVal = MaxValue(0, ( GetCurrency(IAF1040.TotTaxCont) + GetCurrency(IAF1040.Penalty) + GetCurrency(IAF1040.PenInt) )  - GetCurrency(IAF1040.TotCredit))
    else:
        ReturnVal = GetCurrency(IAF1040.Owe) + GetCurrency(IAF1040.Penalty) + GetCurrency(IAF1040.PenInt)

def TotPC2a_Calculation():
    ReturnVal = CDollar(GetFloat(IAF1040.PC2a) * 4000)

def TotPC2b_Calculation():
    ReturnVal = CDollar(GetFloat(IAF1040.PC2b) * 2000)

def TotPCa_Calculation():
    ReturnVal = CDollar(GetFloat(IAF1040.PC1a) * 4000)

def TotPCb_Calculation():
    ReturnVal = CDollar(GetFloat(IAF1040.PC1b) * 2000)

def TotTaxCont_Calculation():
    ReturnVal = GetCurrency(IAF1040.TotalTax) + GetCurrency(IAF1040.TotContrib)

def TPDateDeath_Calculation():
    if GetBool(IAF1040.TPDeceased) == True:
        ReturnVal = GetString(USWBasicInfo.YouDeath)
    else:
        ReturnVal = ''

def TPDeceased_Calculation():
    if GetBool(USWBasicInfo.TpDeceased) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

def UsedAI_Calculation():
    if GetBool(IA2210An.Print) == True:
        ReturnVal = 1
    elif GetBool(IA2210AnSp.Print) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

