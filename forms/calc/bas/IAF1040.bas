Private Sub AAlimony_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(USWRec.TAlimony)
    Else
        ReturnVal = GetCurrency(USWRec.TotAlimony)
    End If
End Sub

Private Sub AAlimonyP_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(USWRec.TAlimonyAdj)
    Else
        ReturnVal = GetCurrency(USWRec.TotAlimonyAdj)
    End If
End Sub

Private Sub AAltTax_Calculation()
' 1st condition added for situation when MFS return and reporting spouse income causes an alternate tax calculation yet taxpayer has zero income
' See saved return IA MFS Alternate Tax Issue.ta2
    If GetBool(IAF1040.MFS) = True And GetCurrency(IAF1040.ATaxInc) = 0 Then
        ReturnVal = 0
    ElseIf (GetCurrency(IAWkAltTax.Mult) < GetCurrency(IAWkAltTax.Tables)) And GetBool(IAWkAltTax.Qualify) = True Then
        ReturnVal = GetCurrency(IAF1040.ATax)
    Else
        ReturnVal = GetCurrency(IAF1040.ARegTax)
    End If
End Sub

Private Sub AApply99_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAEstimates.TotApplied) - GetCurrency(IAF1040.BApply99))
End Sub

Private Sub ABal1_Calculation()
    If IAFS() = 1 And GetBool(IAF1040.DepY) = False Then
        ReturnVal = GetCurrency(IARequired.TaxReduction)
    Else
        ReturnVal = MaxValue(0, GetCurrency(IAF1040.ATotIATax) - GetCurrency(IAF1040.ACredits))
    End If
End Sub

Private Sub ABal2_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAF1040.ABal1) - GetCurrency(IAF1040.ACrNon))
End Sub

Private Sub ABal4_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAF1040.ABal3) - GetCurrency(IAF1040.AOthIACr))
End Sub

Private Sub ABal36_Calculation()
    ReturnVal = GetCurrency(IAF1040.ABalance)
End Sub

Private Sub ABal3_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAF1040.ABal2) - GetCurrency(IAF1040.AOutState))
End Sub

Private Sub ABalance_Calculation()
    ReturnVal = GetCurrency(IAF1040.ATotTax) - GetCurrency(IAF1040.AFedDed)
End Sub

Private Sub ABusInc_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(USWRec.TBusiness)
    Else
        ReturnVal = GetCurrency(USWRec.TotBusiness)
    End If
End Sub

Private Sub ABusIncL_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(USWRec.THalfSe)
    Else
        ReturnVal = GetCurrency(USWRec.TotHalfSE)
    End If
End Sub

Private Sub ACapGain_Calculation()
    Dim CapGain As Currency
    
    If GetBool(USWResidency.F1040NR) = False Then
        CapGain = GetCurrency(USF1040.CapGain)
    Else
        CapGain = GetCurrency(USF1040NR.CapGain)
    End If
    
    If IAFS() = 3 Then
        ReturnVal = CapGain - GetCurrency(IAF1040.BCapGain)
    Else
        ReturnVal = CapGain
    End If
End Sub

Private Sub AChild_Calculation()
    If GetBool(IAF1040.ChildCareCk) = True Then
        ReturnVal = GetCurrency(IAChildCredit.TChild)
    ElseIf GetBool(IAF1040.EarlyChildCk) = True Then
        ReturnVal = GetCurrency(IAChildCredit.TEarly)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub ACredits_Calculation()
    ReturnVal = GetCurrency(IAF1040.AExemCr) + GetCurrency(IAF1040.ATuit) + GetCurrency(IAF1040.AVolFireCr)
End Sub

Private Sub ACrNon_Calculation()
    ReturnVal = GetCurrency(IAF126.ACredit)
End Sub

Private Sub ActNum_Calculation()
    If GetBool(IAEFWksht.PrepBPTrans) = True Then
        ReturnVal = ""
    ElseIf GetBool(IAEFWksht.DirDeposit) = True And GetBool(IAEFWksht.Yes) = False And GetCurrency(IAEFWksht.Refund) > 0 Then
        ReturnVal = GetString(IAEFWksht.DirDepDan)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub Add_Calculation()
    ReturnVal = GetString(USWBasicInfo.HomeComb)
End Sub

Private Sub ADedBox_Calculation()
' updated for 2018
    
    Dim Itemized As Currency
    Dim Deduction As Currency
    
    If GetBool(IAF1040.CombMFS) = True Or GetBool(IAF1040.MFS) = True Then
        Itemized = GetCurrency(IASchA.YouPC)
    Else
        Itemized = GetCurrency(IASchA.Item)
    End If

    If GetBool(IAF1040.ItemCheck) = True Then
        Deduction = Itemized
    ElseIf IAFS() = 2 Or IAFS() = 5 Or IAFS() = 6 Then
        Deduction = MinValue(5000@, GetCurrency(IAF1040.ABal36))
    Else
        Deduction = MinValue(2030@, GetCurrency(IAF1040.ABal36))
    End If
    
    ReturnVal = MaxValue(0, Deduction)
End Sub

Private Sub ADividend_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IARequired.TotTPDiv)
    Else
        ReturnVal = GetCurrency(IARequired.TotDiv)
    End If
End Sub

Private Sub AEst_Calculation()
    If GetBool(IA1040X.EFAmend) = True Then
        ReturnVal = MaxValue(0, GetCurrency(IAStateEst.TotIAEst) - GetCurrency(IAStateEst.SPIAEst)) + GetCurrency(IA1040X.TotPrevTax)
    Else
        ReturnVal = MaxValue(0, GetCurrency(IAStateEst.TotIAEst) - GetCurrency(IAStateEst.SPIAEst))
    End If
End Sub

Private Sub AEstTax_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IAFedEst.TPTotEst)
    Else
        ReturnVal = GetCurrency(IAFedEst.TPTotEst) + GetCurrency(IAFedEst.SPTotEst)
    End If
End Sub

Private Sub AExemCr_Calculation()
    ReturnVal = GetCurrency(IAF1040.ExempA)
End Sub

Private Sub AFarm_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(USWRec.TFarm)
    Else
        ReturnVal = GetCurrency(USWRec.TotFarm)
    End If
End Sub

Private Sub AFedDed_Calculation()
    ReturnVal = GetCurrency(IAF1040.ATaxWith) + GetCurrency(IAF1040.AEstTax) + GetCurrency(IAF1040.APrior)
End Sub

Private Sub AFedTax_Calculation()
    ReturnVal = GetCurrency(IAF1040.ARefund) + GetCurrency(IAF1040.ASelf)
End Sub

Private Sub AFuel_Calculation()
    ReturnVal = GetCurrency(IASch4136.TotCr, FieldCopies(IASch4136.Taxpayer))
End Sub

Private Sub AGamble_Calculation()
    If GetBool(USWResidency.F1040NR) = True Then
        ReturnVal = GetCurrency(USSchNEC.Gambling130) + GetCurrency(USSchNEC.Gambling1Oth) + GetCurrency(USSchNEC.Gambling10) + GetCurrency(USSchNEC.Gambling230) + GetCurrency(USSchNEC.Gambling2Oth)
    ElseIf IAFS() = 3 Then
        ReturnVal = GetCurrency(USWOthInc.TPOth3)
    Else
        ReturnVal = GetCurrency(USWOthInc.TotGamb)
    End If
End Sub

Private Sub AGross_Calculation()
    ReturnVal = GetCurrency(IAF1040.AWages) + GetCurrency(IAF1040.AInterest) + GetCurrency(IAF1040.ADividend) + GetCurrency(IAF1040.AAlimony) + GetCurrency(IAF1040.ABusInc) + GetCurrency(IAF1040.ACapGain) + GetCurrency(IAF1040.AOthGain) + GetCurrency(IAF1040.AIRA) + GetCurrency(IAF1040.APensions) + GetCurrency(IAF1040.ARents) + GetCurrency(IAF1040.AFarm) + GetCurrency(IAF1040.AUnemp) + GetCurrency(IAF1040.AGamble) + GetCurrency(IAF1040.AOtherInc)
End Sub

Private Sub AHealth_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IAWHealth.TPTotal)
    Else
        ReturnVal = GetCurrency(IAWHealth.TPTotal) + GetCurrency(IAWHealth.SPTotal)
    End If
End Sub

Private Sub AIAMin_Calculation()
    ReturnVal = GetCurrency(IA6251.TotAMT)
End Sub

Private Sub AIATaxWith_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IARequired.TIAW2WH) + GetCurrency(IARequired.TPW2GWH) + GetCurrency(IARequired.Tot1042S) + GetCurrency(IARequired.TPCapGainWH) + GetCurrency(IARequired.TPDivWH) + GetCurrency(IARequired.TPUnemWH) + GetCurrency(IARequired.TPIntWH) + GetCurrency(IARequired.TPKWH) + GetCurrency(IARequired.TPMiscWH) + GetCurrency(IARequired.TPOIDWH) + GetCurrency(IARequired.T1099rWH) + GetCurrency(IARequired.TpOthIncWH)
    Else
        ReturnVal = GetCurrency(IARequired.TotIAW2WH) + GetCurrency(IARequired.TotW2GWH) + GetCurrency(IARequired.Tot1042S) + GetCurrency(IARequired.TotCapGainWH) + GetCurrency(IARequired.TotDivWH) + GetCurrency(IARequired.TotUnemWH) + GetCurrency(IARequired.TotIntWH) + GetCurrency(IARequired.TotKWH) + GetCurrency(IARequired.TotMiscWH) + GetCurrency(IARequired.TotOIDWH) + GetCurrency(IARequired.Tot1099rWH) + GetCurrency(IARequired.TotOthIncWH)
    End If
End Sub

Private Sub AIEIC_Calculation()
    If IAFS() = 3 Or IAFS() = 4 Then
        ReturnVal = GetCurrency(IARequired.TIAEic)
    Else
        ReturnVal = GetCurrency(IARequired.IAEic)
    End If
End Sub

Private Sub AInterest_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IARequired.TotTPInt)
    Else
        ReturnVal = GetCurrency(IARequired.TotInt)
    End If
End Sub

Private Sub AIRA_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IAWPenExc.TPIRA)
    Else
        ReturnVal = GetCurrency(IAWPenExc.TPIRA) + GetCurrency(IAWPenExc.SPIRA)
    End If
End Sub

Private Sub AKeogh_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(USWRec.TKeough) + GetCurrency(IARequired.TIRA)
    Else
        ReturnVal = GetCurrency(USWRec.TotKeough) + GetCurrency(USWRec.TotIRAAdj)
    End If
End Sub

Private Sub ALump_Calculation()
    If IAFS() = 3 Then
        ReturnVal = CDollar(GetFloat(USF4972.Tax) * 0.25)
    Else
        ReturnVal = CDollar(GetFloat(USF4972.Tax) * 0.25) + CDollar(GetFloat(USF4972Spouse.Tax) * 0.25)
    End If
End Sub

Private Sub AMove_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IARequired.TMove)
    Else
        ReturnVal = GetCurrency(IARequired.TotMove)
    End If
End Sub

Private Sub ANet_Calculation()
    ReturnVal = GetCurrency(IAF1040.AGross) - GetCurrency(IAF1040.ATotAdj)
End Sub

Private Sub AOthAdj_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IAOthAdj.TPTot)
    Else
        ReturnVal = GetCurrency(IAOthAdj.TPTot) + GetCurrency(IAOthAdj.SPTot)
    End If
End Sub

Private Sub AOtherInc_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IAWOthInc.TPTot)
    Else
        ReturnVal = GetCurrency(IAWOthInc.TPTot) + GetCurrency(IAWOthInc.SPTot)
    End If
End Sub

Private Sub AOthGain_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(USWRec.TOthGain)
    Else
        ReturnVal = GetCurrency(USWRec.TotOthGain)
    End If
End Sub

Private Sub AOthIACr_Calculation()
    ReturnVal = GetCurrency(IA148.TotNonRefCr)
End Sub

Private Sub AOthRefCr_Calculation()
    ReturnVal = GetCurrency(IA148.TotRefCr)
End Sub

Private Sub AOutState_Calculation()
    ReturnVal = GetCurrency(IA130.TPCredit)
End Sub

Private Sub APenalty_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(USWRec.TEarlyPen)
    Else
        ReturnVal = GetCurrency(USWRec.TotEarlyPen)
    End If
End Sub

Private Sub APenExcl_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IAWPenExc.TPPenExc)
    Else
        ReturnVal = GetCurrency(IAWPenExc.TPPenExc) + GetCurrency(IAWPenExc.SPPenExc)
    End If
End Sub

Private Sub APensions_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IAWPenExc.TPPensions)
    Else
        ReturnVal = GetCurrency(IAWPenExc.TPPensions) + GetCurrency(IAWPenExc.SPPensions)
    End If
End Sub

Private Sub APrior_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IAAddFedTax.TPTotal)
    Else
        ReturnVal = GetCurrency(IAAddFedTax.TPTotal) + GetCurrency(IAAddFedTax.SPTotal)
    End If
End Sub

Private Sub ARefund_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IAFedRef.TPST)
    Else
        ReturnVal = GetCurrency(IAFedRef.SPST) + GetCurrency(IAFedRef.TPST)
    End If
End Sub

Private Sub ARegTax_Calculation()
' updated for 2018

    Dim Mid As Currency
    Dim MidInt As Long
    Dim TotTaxInc As Currency
    
    TotTaxInc = GetCurrency(IAF1040.ATaxInc)
    
    If TotTaxInc > 95650@ Then
        Mid = TotTaxInc
    ElseIf TotTaxInc > 150@ Then
        MidInt = CLng((TotTaxInc - 1@) / 50@)
        Mid = (CCur(MidInt) * 50@) + 25@
    Else
        Mid = 0@
    End If

    ReturnVal = Tax(Mid)

End Sub

Private Sub ARents_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(USWRec.TRental)
    Else
        ReturnVal = GetCurrency(USWRec.TotRental)
    End If
End Sub

Private Sub ARepSSB_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IAWkSSB.TPRepSSB)
    Else
        ReturnVal = GetCurrency(IAWkSSB.ReportSSB)
    End If
End Sub

Private Sub ASch_Calculation()
    ReturnVal = CDollar(GetFloat(IAF1040.ABal4) * GetFloat(IAF1040.SchRate))
End Sub

Private Sub ASelf_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IASETax.TPTotal)
    Else
        ReturnVal = GetCurrency(IASETax.TPTotal) + GetCurrency(IASETax.SPTotal)
    End If
End Sub

Private Sub ATax_Calculation()
    If GetNumber(IAWkAltTax.ProRate) = 1 Then
        ReturnVal = GetCurrency(IAWkAltTax.ATax)
    Else
        ReturnVal = GetCurrency(IAWkAltTax.Lesser)
    End If
End Sub

Private Sub ATaxB4Cont_Calculation()
    ReturnVal = GetCurrency(IAF1040.ABal4) + GetCurrency(IAF1040.ASch)
End Sub

Private Sub ATaxInc_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAF1040.ABal36) - GetCurrency(IAF1040.ADedBox))
End Sub

Private Sub ATaxWith_Calculation()
    Dim TotWH As Currency
    
    If GetBool(USWResidency.F1040NR) = True Then
        TotWH = GetCurrency(USF1040NR.WHW2) + GetCurrency(USF1040NR.WH8805) + GetCurrency(USF1040NR.WH8288A) + GetCurrency(USF1040NR.WH1042S)
    Else
        TotWH = GetCurrency(USF1040.WH) + Round(GetCurrency(USDW2AS.ASWH, FieldCopies(USDW2AS.Taxpayer))) + Round(GetCurrency(USDW2VI.VIWH, FieldCopies(USDW2VI.Taxpayer)))
    End If
    
    If IAFS() = 3 Then
        ReturnVal = MaxValue(0, TotWH - GetCurrency(IAF1040.BTaxWith))
    Else
        ReturnVal = TotWH
    End If
End Sub

Private Sub ATot67_Calculation()
    ReturnVal = GetCurrency(IAF1040.AFuel) + GetCurrency(IAF1040.AChild) + GetCurrency(IAF1040.AIEIC) + GetCurrency(IAF1040.AOthRefCr) + GetCurrency(IAF1040.AIATaxWith) + GetCurrency(IAF1040.AEst)
End Sub

Private Sub ATotAdj_Calculation()
    ReturnVal = GetCurrency(IAF1040.AKeogh) + GetCurrency(IAF1040.ABusIncL) + GetCurrency(IAF1040.AHealth) + GetCurrency(IAF1040.APenalty) + GetCurrency(IAF1040.AAlimonyP) + GetCurrency(IAF1040.APenExcl) + GetCurrency(IAF1040.AMove) + GetCurrency(IAF1040.AGainDed) + GetCurrency(IAF1040.AOthAdj)
End Sub

Private Sub ATotIATax_Calculation()
    ReturnVal = GetCurrency(IAF1040.AAltTax) + GetCurrency(IAF1040.ALump) + GetCurrency(IAF1040.AIAMin)
End Sub

Private Sub ATotTax_Calculation()
    ReturnVal = GetCurrency(IAF1040.ANet) + GetCurrency(IAF1040.AFedTax)
End Sub

Private Sub ATuit_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IATuition.TTuit)
    Else
        ReturnVal = GetCurrency(IATuition.TotCr)
    End If
End Sub

Private Sub AUnemp_Calculation()
    If IAFS() = 3 Then
        ReturnVal = MaxValue(0, GetCurrency(USWRec.TUnem) - Round(GetCurrency(USWUnempl.RRBSub, FieldCopies(USWUnempl.Taxpayer))))
    Else
        ReturnVal = MaxValue(0, GetCurrency(USWRec.TotUnem) - Round(GetCurrency(USWUnempl.RRBSub)))
    End If
End Sub

Private Sub AVolFireCr_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IAFireCr.TPTotCr)
    Else
        ReturnVal = GetCurrency(IAFireCr.TPTotCr) + GetCurrency(IAFireCr.SPTotCr)
    End If
End Sub

Private Sub AWages_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(USWRec.TWages)
    Else
        ReturnVal = GetCurrency(USWRec.TotWages)
    End If
End Sub

Private Sub BAlimony_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(USWRec.SAlimony)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BAlimonyP_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(USWRec.SAlimonyAdj)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BAltTax_Calculation()
    If IAFS() = 3 Then
        If (GetCurrency(IAWkAltTax.Mult) < GetCurrency(IAWkAltTax.Tables)) And GetBool(IAWkAltTax.Qualify) = True Then
            ReturnVal = GetCurrency(IAF1040.BTax)
        Else
            ReturnVal = GetCurrency(IAF1040.BRegTax)
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BApply99_Calculation()
    ReturnVal = MinValue(GetCurrency(IAF1040.OVerPaid), GetCurrency(IAEstimates.TotApplied, FieldCopies(IAEstimates.Spouse)))
End Sub

Private Sub BBal1_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAF1040.BTotIATax) - GetCurrency(IAF1040.BCredits))
End Sub

Private Sub BBal2_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAF1040.BBal1) - GetCurrency(IAF1040.BCrNon))
End Sub

Private Sub BBal4_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAF1040.BBal3) - GetCurrency(IAF1040.BOthIACr))
End Sub

Private Sub BBal36_Calculation()
    ReturnVal = GetCurrency(IAF1040.BBalance)
End Sub

Private Sub BBal3_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAF1040.BBal2) - GetCurrency(IAF1040.BOutState))
End Sub

Private Sub BBalance_Calculation()
    ReturnVal = GetCurrency(IAF1040.BTotTax) - GetCurrency(IAF1040.BFedDed)
End Sub

Private Sub BBusInc_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(USWRec.SBusiness)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BBusIncL_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(USWRec.SHalfSe)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BCapGain_Calculation()
    If IAFS() = 3 Then
        If GetCurrency(USWDRec.CapGain) < 0@ Then
            ReturnVal = GetCurrency(IARequired.SLimLoss)
        Else
            ReturnVal = GetCurrency(USWDRec.SCapGain)
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BChild_Calculation()
    If IAFS() = 3 Then
        If GetBool(IAF1040.ChildCareCk) = True Then
            ReturnVal = GetCurrency(IAChildCredit.SChild)
        ElseIf GetBool(IAF1040.EarlyChildCk) = True Then
            ReturnVal = GetCurrency(IAChildCredit.SEarly)
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BCredits_Calculation()
    ReturnVal = GetCurrency(IAF1040.BExemCr) + GetCurrency(IAF1040.BTuit) + GetCurrency(IAF1040.BVolFireCr)
End Sub

Private Sub BCrNon_Calculation()
    If IAFS() = 3 Then
        If GetBool(IAF126.SpNonRes) = True Or GetBool(IAF126.SpPYRes) = True Then
            ReturnVal = GetCurrency(IAF126.BCredit)
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BDedBox_Calculation()
' updated for 2018

Dim Deduction As Currency

    If IAFS() = 3 Then
        If GetBool(IAF1040.ItemCheck) = True Then
            Deduction = GetCurrency(IASchA.SpPro)
        Else
            Deduction = MinValue(2030@, GetCurrency(IAF1040.BBal36))
        End If
    Else
        Deduction = 0
    End If
    
    ReturnVal = MaxValue(0, Deduction)
    
End Sub

Private Sub BDividend_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IARequired.TotSPDiv)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BEst_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IAStateEst.SPIAEst)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BEstTax_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IAFedEst.SPTotEst)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BExemCr_Calculation()
    ReturnVal = GetCurrency(IAF1040.ExempB)
End Sub

Private Sub BFarm_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(USWRec.SFarm)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BFedDed_Calculation()
    ReturnVal = GetCurrency(IAF1040.BTaxWith) + GetCurrency(IAF1040.BEstTax) + GetCurrency(IAF1040.BPrior)
End Sub

Private Sub BFedTax_Calculation()
    ReturnVal = GetCurrency(IAF1040.BRefund) + GetCurrency(IAF1040.BSelf)
End Sub

Private Sub BFuel_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IASch4136.TotCr, FieldCopies(IASch4136.Spouse))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BGamble_Calculation()
    If IAFS() = 3 And GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.SPOth3)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BGross_Calculation()
    ReturnVal = GetCurrency(IAF1040.BWages) + GetCurrency(IAF1040.BInterest) + GetCurrency(IAF1040.BDividend) + GetCurrency(IAF1040.BAlimony) + GetCurrency(IAF1040.BBusInc) + GetCurrency(IAF1040.BCapGain) + GetCurrency(IAF1040.BOthGain) + GetCurrency(IAF1040.BIRA) + GetCurrency(IAF1040.BPensions) + GetCurrency(IAF1040.BRents) + GetCurrency(IAF1040.BFarm) + GetCurrency(IAF1040.BUnemp) + GetCurrency(IAF1040.BGamble) + GetCurrency(IAF1040.BOtherInc)
End Sub

Private Sub BHealth_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IAWHealth.SPTotal)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BIAMin_Calculation()
    ReturnVal = GetCurrency(IA6251Sp.TotAMT)
End Sub

Private Sub BIATaxWith_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IARequired.SIAW2WH) + GetCurrency(IARequired.SPW2GWH) + GetCurrency(IARequired.SPCapGainWH) + GetCurrency(IARequired.SPDivWH) + GetCurrency(IARequired.SPUnemWH) + GetCurrency(IARequired.SPIntWH) + GetCurrency(IARequired.SPKWH) + GetCurrency(IARequired.SPMiscWH) + GetCurrency(IARequired.SPOIDWH) + GetCurrency(IARequired.S1099RWH) + GetCurrency(IARequired.SPOthIncWH)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BIEIC_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IARequired.SIaEIC)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BInterest_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IARequired.TotSPInt)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BIRA_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IAWPenExc.SPIRA)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BKeogh_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(USWRec.SKeough) + GetCurrency(IARequired.SIRA)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BLump_Calculation()
    If IAFS() = 3 Then
        ReturnVal = CDollar(GetFloat(USF4972Spouse.Tax) * 0.25)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BMove_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IARequired.SMove)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BNet_Calculation()
    ReturnVal = GetCurrency(IAF1040.BGross) - GetCurrency(IAF1040.BTotAdj)
End Sub

Private Sub BOthAdj_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IAOthAdj.SPTot)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BOtherInc_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IAWOthInc.SPTot)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BOthGain_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(USWRec.SOthGain)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BOthIACr_Calculation()
    ReturnVal = GetCurrency(IA148Sp.TotNonRefCr)
End Sub

Private Sub BOthRefCr_Calculation()
    ReturnVal = GetCurrency(IA148Sp.TotRefCr)
End Sub

Private Sub BOutState_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IA130.SPCredit)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BPenalty_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(USWRec.SEarlyPen)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BPenExcl_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IAWPenExc.SPPenExc)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BPensions_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IAWPenExc.SPPensions)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BPrior_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IAAddFedTax.SPTotal)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BRefund_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IAFedRef.SPST)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BRegTax_Calculation()
' updated for 2018

    Dim Mid As Currency
    Dim MidInt As Long
    Dim TotTaxInc As Currency
    
    If GetBool(IAF1040.MFS) = True Then
        TotTaxInc = GetCurrency(IAF1040.SpTaxInc)
    Else
        TotTaxInc = GetCurrency(IAF1040.BTaxInc)
    End If
    
    If TotTaxInc > 95650@ Then
        Mid = TotTaxInc
    ElseIf TotTaxInc > 150@ Then
        MidInt = CLng((TotTaxInc - 1@) / 50@)
        Mid = (CCur(MidInt) * 50@) + 25@
    Else
        Mid = 0@
    End If
    
    ReturnVal = Tax(Mid)

End Sub

Private Sub BRents_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(USWRec.SRental)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BRepSSB_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IAWkSSB.SPRepSSB)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BSch_Calculation()
    ReturnVal = CDollar(GetFloat(IAF1040.BBal4) * GetFloat(IAF1040.SchRate))
End Sub

Private Sub BSelf_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IASETax.SPTotal)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BTax_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IAWkAltTax.BTax)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BTaxB4Cont_Calculation()
    ReturnVal = GetCurrency(IAF1040.BBal4) + GetCurrency(IAF1040.BSch)
End Sub

Private Sub BTaxInc_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAF1040.BBal36) - GetCurrency(IAF1040.BDedBox))
End Sub

Private Sub BTaxWith_Calculation()
    Dim JT As Currency
    Dim SPW2 As Currency
    Dim SP As Currency
    
    JT = CDollar(CDbl(Round(GetCurrency(USD1099INT.WH, FieldCopies(USD1099INT.Joint))) + Round(GetCurrency(USD1099K.WH, FieldCopies(USD1099K.Joint))) + Round(GetCurrency(USD1099OID.WH, FieldCopies(USD1099OID.Joint))) + Round(GetCurrency(USD1099MISC.WH, FieldCopies(USD1099MISC.Joint))) + Round(GetCurrency(USD1099DIV.WH, FieldCopies(USD1099DIV.Joint))) + Round(GetCurrency(USDCapGain.WH2, FieldCopies(USDCapGain.Joint))) + Round(GetCurrency(USDPartK1.BackupWith, FieldCopies(USDPartK1.Joint))) + Round(GetCurrency(USDSCorpK1.BackupWith, FieldCopies(USDSCorpK1.Joint))) + Round(GetCurrency(USDEstK1.BackupWith, FieldCopies(USDEstK1.Joint)))) * 0.5)
    SPW2 = Round(GetCurrency(USDW2.WH, FieldCopies(USDW2.Spouse))) + Round(GetCurrency(USDW2AS.ASWH, FieldCopies(USDW2AS.Spouse))) + Round(GetCurrency(USDW2CM.CNMIWH, FieldCopies(USDW2CM.Spouse))) + Round(GetCurrency(USDW2GU.GuamWH, FieldCopies(USDW2GU.Spouse))) + Round(GetCurrency(USDW2VI.VIWH, FieldCopies(USDW2VI.Spouse)))
    SP = Round(GetCurrency(USD1099INT.WH, FieldCopies(USD1099INT.Spouse))) + Round(GetCurrency(USD1099K.WH, FieldCopies(USD1099K.Spouse))) + Round(GetCurrency(USD1099OID.WH, FieldCopies(USD1099OID.Spouse))) + Round(GetCurrency(USD1099DIV.WH, FieldCopies(USD1099DIV.Spouse))) + Round(GetCurrency(USD1099R.WH, FieldCopies(USD1099R.Spouse))) + Round(GetCurrency(USD1099MISC.WH, FieldCopies(USD1099MISC.Spouse))) + Round(GetCurrency(USWUnempl.TPFedWH, FieldCopies(USWUnempl.Spouse))) + Round(GetCurrency(USDW2G.WH, FieldCopies(USDW2G.Spouse))) + Round(GetCurrency(USDCapGain.WH2, FieldCopies(USDCapGain.Spouse))) + Round(GetCurrency(USDRRB1099R.WH, FieldCopies(USDRRB1099R.Spouse))) + Round(GetCurrency(USDPartK1.BackupWith, FieldCopies(USDPartK1.Spouse))) + Round(GetCurrency(USDSCorpK1.BackupWith, FieldCopies(USDSCorpK1.Spouse))) + Round(GetCurrency(USDEstK1.BackupWith, FieldCopies(USDEstK1.Spouse)))
    
    If IAFS() = 3 Then
        ReturnVal = JT + SPW2 + SP + GetCurrency(USWSSBDetail.SPFedWH) + GetCurrency(USWRec.SPTotAddMedTaxWH)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BTot67_Calculation()
    ReturnVal = GetCurrency(IAF1040.BFuel) + GetCurrency(IAF1040.BChild) + GetCurrency(IAF1040.BIEIC) + GetCurrency(IAF1040.BOthRefCr) + GetCurrency(IAF1040.BIATaxWith) + GetCurrency(IAF1040.BEst)
End Sub

Private Sub BTotAdj_Calculation()
    ReturnVal = GetCurrency(IAF1040.BKeogh) + GetCurrency(IAF1040.BBusIncL) + GetCurrency(IAF1040.BHealth) + GetCurrency(IAF1040.BPenalty) + GetCurrency(IAF1040.BAlimonyP) + GetCurrency(IAF1040.BPenExcl) + GetCurrency(IAF1040.BMove) + GetCurrency(IAF1040.BGainDed) + GetCurrency(IAF1040.BOthAdj)
End Sub

Private Sub BTotIATax_Calculation()
    ReturnVal = GetCurrency(IAF1040.BAltTax) + GetCurrency(IAF1040.BLump) + GetCurrency(IAF1040.BIAMin)
End Sub

Private Sub BTotTax_Calculation()
    ReturnVal = GetCurrency(IAF1040.BNet) + GetCurrency(IAF1040.BFedTax)
End Sub

Private Sub BTuit_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IATuition.STuit)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BUnemp_Calculation()
    If IAFS() = 3 Then
        ReturnVal = MaxValue(0, GetCurrency(USWRec.SUnem) - Round(GetCurrency(USWUnempl.RRBSub, FieldCopies(USWUnempl.Spouse))))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BVolFireCr_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IAFireCr.SPTotCr)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BWages_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(USWRec.SWages)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Checking_Calculation()
    If GetBool(IAEFWksht.PrepBPTrans) = True Then
        ReturnVal = 0
    ElseIf GetBool(IAEFWksht.DirDeposit) = True And GetBool(IAEFWksht.Yes) = False And GetCurrency(IAEFWksht.Refund) > 0 Then
        ReturnVal = GetBool(IAEFWksht.DirDepChecking)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub ChildCareCk_Calculation()
    If GetCurrency(IAChildCredit.TotChDepCr) <> 0 And GetCurrency(IAChildCredit.TotChDepCr) >= GetCurrency(IAChildCredit.TotCr) Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CityComb_Calculation()
    If Trim(GetString(USWBasicInfo.ForCountry)) <> "" Then
        ReturnVal = GetString(USWBasicInfo.City) & ", " & GetString(USWBasicInfo.ForeignCtry) & " " & GetString(USWBasicInfo.ForeignPC)
    Else
        ReturnVal = GetString(USWBasicInfo.CityComb)
    End If
End Sub

Private Sub CombMFS_Calculation()
    If FedFS() = 2 And (GetCurrency(USWRec.TAGI) > 2632@) And (GetCurrency(USWRec.SAGI) > 2632@) Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CountyNo_Calculation()
    ReturnVal = GetString(USZIA1040.IAPYCounty)
End Sub

Private Sub DateDuePaid_Calculation()
    ReturnVal = MakeDate(4, 30, YearNumber + 1)
End Sub

Private Sub DC1_Calculation()
    If IAFS() = 3 Then
        ReturnVal = MaxValue(0, GetNumber(USWAddDep.GrandTotDeps) - GetNumber(IAF1040.DC2))
    Else
        ReturnVal = GetNumber(USWAddDep.GrandTotDeps)
    End If
End Sub

Private Sub DC2_Calculation()
    If IAFS() = 3 Then
        ReturnVal = CLng(Round(GetNumber(USWAddDep.GrandTotDeps) * GetFloat(IARequired.BProRate)))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub DepN_Calculation()
    If GetBool(IAF1040.Single) = True Then
        If GetBool(USWBasicInfo.Dopr) = True Then
            ReturnVal = 0
        Else
            ReturnVal = 1
        End If
    Else
        ReturnVal = 0
    End If

End Sub

Private Sub DepNames_Calculation()
    If GetNumber(IAF1040.DC1) > 0 Or GetNumber(IAF1040.DC2) > 0 Then
        If GetNumber(IARequired.DepLength) > 23 Then
            ReturnVal = "See Attached"
        Else
            ReturnVal = GetString(IARequired.DepNames)
        End If
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub DepY_Calculation()
    If GetBool(IAF1040.Single) = True Then
        If GetBool(USWBasicInfo.Dopr) = True Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Desc_Calculation()
    ReturnVal = GetString(IARequired.CombNames)
End Sub

Private Sub EarlyChildCk_Calculation()
    If GetBool(IAF1040.ChildCareCk) = True Then
        ReturnVal = 0
    ElseIf GetCurrency(IAChildCredit.TotCr) <> 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Email_Calculation()
    ReturnVal = GetString(USWBasicInfo.email)
End Sub

Private Sub ExempA_Calculation()
    ReturnVal = GetCurrency(IAF1040.TotPCa) + GetCurrency(IAF1040.TotPCb) + GetCurrency(IAF1040.TotDC1)
End Sub

Private Sub ExempB_Calculation()
    ReturnVal = GetCurrency(IAF1040.TotPC2a) + GetCurrency(IAF1040.TotPC2b) + GetCurrency(IAF1040.TotDC2)
End Sub

Private Sub Exist_Calculation()
    ReturnVal = 1
End Sub

Private Sub FirmID_Calculation()
    ReturnVal = GetString(USWBasicInfo.PrepEIN)
End Sub

Private Sub FirstName_Calculation()
    ReturnVal = GetString(USWBasicInfo.TPFnI)
End Sub

Private Sub HOH_Calculation()
    If FedFS() = 4 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub HOHDep_Calculation()
    ReturnVal = GetString(USWBasicInfo.L3Name)
End Sub

Private Sub HOHSSN_Calculation()
    If GetBool(USF1040.HOH) = True Then
        ReturnVal = GetString(USF1040.L3SSN)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub ItemCheck_Calculation()
' updated for 2018

    If GetBool(IAF1040.MFSItm) = True And IAFS() = 4 Then
        ReturnVal = 1
    ElseIf IAFS() = 3 Then
        If GetCurrency(IASchA.Item) > 4060@ Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    ElseIf IAFS() = 2 Or IAFS() = 5 Or IAFS() = 6 Then
        If GetCurrency(IASchA.Item) > 5000@ Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    ElseIf GetCurrency(IASchA.Item) > 2030@ Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub LastName_Calculation()
    ReturnVal = GetString(USWBasicInfo.LastName)
End Sub

Private Sub LowInc_Calculation()
    If GetBool(IARequired.LowInc) = True Then
        ReturnVal = "LOW INCOME EXEMPTION"
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub MFJ_Calculation()
    If FedFS() = 2 Then
        If (GetCurrency(USWRec.TAGI) < 2633@) Or (GetCurrency(USWRec.SAGI) < 2633@) Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub MFS_Calculation()
    If FedFS() = 3 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub MFSItm_Calculation()
    If GetBool(USF1040.MfsItm) = True And IAFS() = 4 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub MFSName_Calculation()
    If GetBool(IAF1040.MFS) = True Then
        If Trim(GetString(USWBasicInfo.L2Name)) <> "" Then
            ReturnVal = GetString(USWBasicInfo.L2Name)
        Else
            ReturnVal = GetString(USWBasicInfo.SPFnI) & " " & GetString(USWBasicInfo.SpouseLast)
        End If
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub MFSSSN_Calculation()
    If GetBool(IAF1040.MFS) = True Then
        ReturnVal = GetString(USWBasicInfo.SpouseSSN)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub Over65_Calculation()
    Dim SixtyFive As Long
    Dim SPSixtyFive As Long
    
    If GetNumber(USWBasicInfo.TPAgeRec) >= 65 Then
        SixtyFive = 1
    Else
        SixtyFive = 0
    End If
    
    If GetNumber(USWBasicInfo.SPAgeRec) >= 65 And GetBool(IARequired.AskSpouse) = True Then
        SPSixtyFive = 1
    Else
        SPSixtyFive = 0
    End If
    
    If SixtyFive + SPSixtyFive > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub OVerPaid_Calculation()
    If GetBool(IA1040X.EFAmend) = True Then
        ReturnVal = MaxValue(0, GetCurrency(IAF1040.TotCredit) - GetCurrency(IA1040X.PrevOP) - GetCurrency(IAF1040.TotTaxCont))
    Else
        ReturnVal = MaxValue(0, GetCurrency(IAF1040.TotCredit) - GetCurrency(IAF1040.TotTaxCont))
    End If
End Sub

Private Sub Owe_Calculation()
    If GetBool(IA1040X.EFAmend) = True Then
        If (GetCurrency(IAF1040.Penalty) + GetCurrency(IA1040X.PrevOP) + GetCurrency(IAF1040.TotTaxCont)) - GetCurrency(IAF1040.TotCredit) > 0 Then
            ReturnVal = MaxValue(0, GetCurrency(IAF1040.TotTaxCont) + GetCurrency(IA1040X.PrevOP) - GetCurrency(IAF1040.TotCredit))
        Else
            ReturnVal = 0
        End If
    Else
        If (GetCurrency(IAF1040.Penalty) + GetCurrency(IAF1040.TotTaxCont)) - GetCurrency(IAF1040.TotCredit) > 0 Then
            ReturnVal = MaxValue(0, GetCurrency(IAF1040.TotTaxCont) - GetCurrency(IAF1040.TotCredit))
        Else
            ReturnVal = 0
        End If
    End If
End Sub

Private Sub PC1a_Calculation()
    If IAFS() = 2 Then
        ReturnVal = 2
    ElseIf IAFS() = 5 Then
        ReturnVal = 2
    Else
        ReturnVal = 1
    End If
End Sub

Private Sub PC1b_Calculation()
    Dim SixtyFive As Long
    Dim Blind As Long
    
    If IAFS() = 2 Then
        SixtyFive = GetBool(USWBasicInfo.SixtyFive) + GetBool(USWBasicInfo.Spouse65)
        Blind = GetBool(USWBasicInfo.Blind) + GetBool(USWBasicInfo.SpBlind)
    Else
        SixtyFive = GetBool(USWBasicInfo.SixtyFive)
        Blind = GetBool(USWBasicInfo.Blind)
    End If
    
    ReturnVal = Blind + SixtyFive
    
End Sub

Private Sub PC2a_Calculation()
    If IAFS() = 3 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PC2b_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetBool(USWBasicInfo.Spouse65) + GetBool(USWBasicInfo.SpBlind)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Penalty_Calculation()
    If GetBool(IA1040X.EFAmend) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(IA2210.Penalty) + GetCurrency(IA2210Sp.Penalty)
    End If
End Sub

Private Sub PenInt_Calculation()
    If GetCurrency(IAF1040.Owe) > 0 Then
        ReturnVal = GetCurrency(IAF1040.Pen74) + GetCurrency(IAF1040.Int74)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Phone_Calculation()
    ReturnVal = GetString(USWBasicInfo.Dayphone)
End Sub

Private Sub PrepID_Calculation()
    ReturnVal = GetString(USWBasicInfo.PrepSSN)
End Sub

Private Sub PrepPhone_Calculation()
    If Trim(GetString(USWBasicInfo.PrepPhone)) <> "" Then
        ReturnVal = GetString(USWBasicInfo.PrepPhone)
    Else
        ReturnVal = GetString(USWBasicInfo.PrepForPhone)
    End If
End Sub

Private Sub QualWidow_Calculation()
    If FedFS() = 5 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub RefBalDue_Calculation()
    ReturnVal = Round(GetCurrency(IAF1040.Refund) - GetCurrency(IAF1040.TotDue))
End Sub

Private Sub Refund_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAF1040.OVerPaid) - GetCurrency(IAF1040.BApply99) - GetCurrency(IAF1040.AApply99) - GetCurrency(IAF1040.Penalty))
End Sub

Private Sub Route_Calculation()
    If GetBool(IAEFWksht.PrepBPTrans) = True Then
        ReturnVal = ""
    ElseIf GetBool(IAEFWksht.DirDeposit) = True And GetBool(IAEFWksht.Yes) = False And GetCurrency(IAEFWksht.Refund) > 0 Then
        ReturnVal = GetString(IAEFWksht.DirDepRTN)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub SaveCheck_Calculation()
    If GetBool(IAEFWksht.PrepBPTrans) = True Then
        ReturnVal = 0
    ElseIf GetBool(IAEFWksht.DirDeposit) = True And GetBool(IAEFWksht.Yes) = False And GetCurrency(IAEFWksht.Refund) > 0 Then
        ReturnVal = GetBool(IAEFWksht.DirDepSavings)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SchNo_Calculation()
    ReturnVal = GetString(USZIA1040.IAPYSchool)
End Sub

Private Sub SchRate_Calculation()
    ReturnVal = SchSurtaxRate(GetNumber(IAF1040.SchNo))
End Sub

Private Sub Single_Calculation()
    If FedFS() = 1 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPDateDeath_Calculation()
    If GetBool(IAF1040.SPDeceased) = True Then
        ReturnVal = GetString(USWBasicInfo.SpDeath)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub SPDeceased_Calculation()
    If GetBool(USWBasicInfo.SpDeceased) = True And GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SpouseFirst_Calculation()
    If GetBool(IAF1040.MFJ) = True Or GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetString(USWBasicInfo.SPFnI)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub SpouseLast_Calculation()
    If GetBool(IAF1040.MFJ) = True Or GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetString(USWBasicInfo.SpouseLast)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub SpouseSSN_Calculation()
    If GetBool(IAF1040.MFJ) = True Or GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetString(USWBasicInfo.SpouseSSN)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(USWBasicInfo.SSN)
End Sub

Private Sub StadCheck_Calculation()
    If GetBool(IAF1040.ItemCheck) = True Then
        ReturnVal = 0
    Else
        ReturnVal = 1
    End If
End Sub

Private Sub TaxRed_Calculation()
    If GetBool(IARequired.LowInc) = True Then
        ReturnVal = ""
    ElseIf IAFS() <> 1 Or GetBool(IAF1040.DepY) = True Then
        ReturnVal = ""
    ElseIf GetCurrency(IAF1040.ABal1) < GetCurrency(IARequired.TentTax) Then
        ReturnVal = "tax reduction"
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub TotalTax_Calculation()
    If GetBool(IARequired.LowInc) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(IAF1040.BTaxB4Cont) + GetCurrency(IAF1040.ATaxB4Cont)
    End If
End Sub

Private Sub TotContrib_Calculation()
    ReturnVal = GetCurrency(IAF1040.Wild) + GetCurrency(IAF1040.Fair) + GetCurrency(IAF1040.FFVet) + GetCurrency(IAF1040.ChildAbuse)
End Sub

Private Sub TotCredit_Calculation()
    ReturnVal = GetCurrency(IAF1040.BTot67) + GetCurrency(IAF1040.ATot67)
End Sub

Private Sub TotDC1_Calculation()
    ReturnVal = CDollar(GetFloat(IAF1040.DC1) * 4000#)
End Sub

Private Sub TotDC2_Calculation()
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = CDollar(GetFloat(IAF1040.DC2) * 4000#)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TotDue_Calculation()
    If GetCurrency(IAF1040.Refund) > 0 Then
        ReturnVal = 0
    ElseIf GetCurrency(IAF1040.Refund) = 0 And GetCurrency(IAF1040.OVerPaid) > 0 Then
        If GetBool(IA1040X.EFAmend) = True Then
            ReturnVal = MaxValue(0, (GetCurrency(IAF1040.TotTaxCont) + GetCurrency(IA1040X.PrevOP) + GetCurrency(IAF1040.Penalty) + GetCurrency(IAF1040.PenInt)) - GetCurrency(IAF1040.TotCredit))
        Else
            ReturnVal = MaxValue(0, (GetCurrency(IAF1040.TotTaxCont) + GetCurrency(IAF1040.Penalty) + GetCurrency(IAF1040.PenInt)) - GetCurrency(IAF1040.TotCredit))
        End If
    Else
        ReturnVal = GetCurrency(IAF1040.Owe) + GetCurrency(IAF1040.Penalty) + GetCurrency(IAF1040.PenInt)
    End If
End Sub

Private Sub TotPC2a_Calculation()
    ReturnVal = CDollar(GetFloat(IAF1040.PC2a) * 4000#)
End Sub

Private Sub TotPC2b_Calculation()
    ReturnVal = CDollar(GetFloat(IAF1040.PC2b) * 2000#)
End Sub

Private Sub TotPCa_Calculation()
    ReturnVal = CDollar(GetFloat(IAF1040.PC1a) * 4000#)
End Sub

Private Sub TotPCb_Calculation()
    ReturnVal = CDollar(GetFloat(IAF1040.PC1b) * 2000#)
End Sub

Private Sub TotTaxCont_Calculation()
    ReturnVal = GetCurrency(IAF1040.TotalTax) + GetCurrency(IAF1040.TotContrib)
End Sub

Private Sub TPDateDeath_Calculation()
   If GetBool(IAF1040.TPDeceased) = True Then
        ReturnVal = GetString(USWBasicInfo.YouDeath)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub TPDeceased_Calculation()
    If GetBool(USWBasicInfo.TpDeceased) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub UsedAI_Calculation()
    If GetBool(IA2210An.Print) = True Then
        ReturnVal = 1
    ElseIf GetBool(IA2210AnSp.Print) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

