Private Sub AdjAMTInc1_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA6251.AMTTaxInc) - GetCurrency(IA6251.Exemption2))
End Sub

Private Sub AdjAMTInc2_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA6251.AMTTaxInc) - GetCurrency(IA6251.AdjExempt))
End Sub

Private Sub AdjExempt_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA6251.Exemption1) - GetCurrency(IA6251.Multiply1))
End Sub

Private Sub AdjGain_Calculation()
    ReturnVal = GetCurrency(USF6251.AdjGain)
End Sub

Private Sub Alert10_Calculation()
    If GetBool(IAF1040.CombMFS) = True Then
        If GetBool(IA6251Sp.SpUserMod) = True Then
            ReturnVal = 0
        ElseIf GetCurrency(USF6251.AMT) > 0 Then
            ReturnVal = 1
        ElseIf GetBool(IA6251.EFile) = True Or GetBool(IA6251Sp.EFile) = True Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert20_Calculation()
'no AMT on bonus depr assets, believe there could be on 2018 nonconforming assets so should factor in IAWDepr.IANonConformDiffs
    If GetNumber(IA6251.DoNotComplete) = 1 Then
        ReturnVal = 0
    ElseIf GetBool(IAWDepr.FedStSec179) > 0 Or GetBool(IAWDepr.IANonConformDiffs) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert30_Calculation()
    If GetNumber(IA6251.DoNotComplete) = 1 Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.CombMFS) = True And (GetBool(IAWDepr.FedStSec179) > 0 Or GetBool(IAWDepr.IANonConformDiffs) > 0) Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert40_Calculation()
    Dim MortIntAdj As Currency
    
    MortIntAdj = GetCurrency(IAW6251MortInt.MortInt98) + GetCurrency(IAW6251MortInt.RefinInt) + GetCurrency(IAW6251MortInt.OthInt)
    
    If GetBool(IAW6251MortInt.OffMort) = False And GetCurrency(IAW6251MortInt.TotMortInt) <> 0 And MortIntAdj = 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AMT_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA6251.TentAMT) - GetCurrency(IA6251.RegTax))
End Sub

Private Sub AMTInc_Calculation()
    ReturnVal = GetCurrency(IA6251.Med) + GetCurrency(IA6251.Taxes) + GetCurrency(IA6251.Int) + GetCurrency(IA6251.MiscDed) + GetCurrency(IA6251.ItmLimit) + GetCurrency(IA6251.TaxRfd) + GetCurrency(IA6251.InvInt) + GetCurrency(IA6251.Sec1202) + GetCurrency(IA6251.ISO) + GetCurrency(IA6251.Est) + GetCurrency(IA6251.LargePart) + GetCurrency(IA6251.AdjGain) + GetCurrency(IA6251.Post86Depr) + GetCurrency(IA6251.PALS) + GetCurrency(IA6251.LossLim) + GetCurrency(IA6251.Circ) + GetCurrency(IA6251.LTContr) + GetCurrency(IA6251.Mining) + GetCurrency(IA6251.Research) + GetCurrency(IA6251.Install) + GetCurrency(IA6251.RelAdj)
End Sub

Private Sub AMTTaxInc_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA6251.Subtotal) - GetCurrency(IA6251.LimAMTNOL))
End Sub

Private Sub AskDepr_Calculation()
'no AMT on bonus depr assets, believe there could be on 2018 nonconforming assets so should factor in IAWDepr.IANonConformDiffs
    If GetBool(IAWDepr.FedStSec179) > 0 Or GetBool(IAWDepr.IANonConformDiffs) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AskMortInt_Calculation()
    If GetBool(USWResidency.F1040NR) = True Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.ItemCheck) = True Then
        If GetCurrency(IASchA.Mort) <> 0 Or GetCurrency(IASchA.MortNot) <> 0 Or GetCurrency(IASchA.PtsNot) <> 0 Or GetCurrency(IASchA.MtgePrem) <> 0 Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Circ_Calculation()
    ReturnVal = GetCurrency(USF6251.Circ)
End Sub

Private Sub Description_Calculation()
    Dim Total As Currency
    
    Total = GetCurrency(IA6251.TotAMT)
    
    ReturnVal = CStr(Total) & " AMT"
End Sub

Private Sub DoNotComplete_Calculation()
    If IAFS() = 1 Then
        If GetBool(IAF1040.Over65) = True And GetCurrency(IAF1040.ANet) <= 24000@ Then
            ReturnVal = 1
        ElseIf GetCurrency(IAF1040.ANet) <= 9000@ Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    ElseIf GetBool(IAF1040.Over65) = True And GetCurrency(IARequired.TotNI) <= 32000@ Then
        ReturnVal = 1
    ElseIf GetCurrency(IARequired.TotNI) <= 13500@ Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub EFile_Calculation()
    If GetNumber(IA6251.DoNotComplete) = 1 Then
        ReturnVal = 0
    ElseIf GetBool(IA6251.Print) = True Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251.Med) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251.Taxes) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251.Int) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251.MiscDed) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251.ItmLimit) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251.TaxRfd) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251.InvInt) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251.Sec1202) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251.ISO) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251.Est) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251.LargePart) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251.AdjGain) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251.Post86Depr) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251.PALS) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251.LossLim) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251.Circ) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251.LTContr) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251.Mining) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251.Research) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251.Install) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251.RelAdj) <> 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Est_Calculation()
    ReturnVal = GetCurrency(USF6251.Est)
End Sub

Private Sub Exemption1_Calculation()
    If GetBool(IAF1040.MFJ) = True Then
        ReturnVal = 35000@
    ElseIf GetBool(IAF1040.CombMFS) = True Or GetBool(IAF1040.MFS) = True Then
        ReturnVal = 17500@
    Else
        ReturnVal = 26000@
    End If
End Sub

Private Sub Exemption2_Calculation()
    If GetBool(IAF1040.MFJ) = True Then
        ReturnVal = 150000@
    ElseIf GetBool(IAF1040.CombMFS) = True Or GetBool(IAF1040.MFS) = True Then
        ReturnVal = 75000@
    Else
        ReturnVal = 112500@
    End If
End Sub

Private Sub Install_Calculation()
    ReturnVal = GetCurrency(USF6251.Install) *  -1
End Sub

Private Sub Int_Calculation()
    If GetBool(IAF1040.CombMFS) = True And GetBool(IAF1040.ItemCheck) = True Then
        ReturnVal = CDollar(GetFloat(IASchA.Perc) * GetFloat(IAW6251MortInt.AMTInt))
    ElseIf GetBool(IAF1040.ItemCheck) = True Then
        ReturnVal = GetCurrency(IAW6251MortInt.AMTInt)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub InvInt_Calculation()
    If GetBool(IAF1040.CombMFS) = True And GetBool(IAF1040.ItemCheck) = True Then
        ReturnVal = CDollar(GetFloat(IASchA.Perc) * GetFloat(USF6251.InvInt))
    ElseIf GetBool(IAF1040.ItemCheck) = True Then
        ReturnVal = GetCurrency(USF6251.InvInt)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub ISO_Calculation()
    ReturnVal = GetCurrency(USF6251.ISO)
End Sub

Private Sub ItmLimit_Calculation()
    If GetBool(IAF1040.CombMFS) = True And GetBool(IAF1040.ItemCheck) = True Then
        ReturnVal = CDollar(GetFloat(IASchA.Perc) * GetFloat(IAWItmDed.Limit)) *  -1
    ElseIf GetBool(IAF1040.ItemCheck) = True Then
        ReturnVal = GetCurrency(IAWItmDed.Limit) *  -1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub LargePart_Calculation()
    ReturnVal = GetCurrency(USF6251.LargePart)
End Sub

Private Sub LimAMTNOL_Calculation()
    Dim TEst As Currency
    Dim Unlim As Currency
    Dim AMTL As Currency
    
    TEst = GetCurrency(IA6251.Subtotal)
    Unlim = Abs(GetCurrency(IA6251.AMTNOL))
    
    If TEst > 0 Then
        AMTL = MinValue(Unlim, CDollar(CDbl(TEst) * 0.9))
    Else
        AMTL = 0
    End If
    
    ReturnVal = AMTL
End Sub

Private Sub LossLim_Calculation()
    ReturnVal = GetCurrency(USF6251.LossLim)
End Sub

Private Sub LTContr_Calculation()
    ReturnVal = GetCurrency(USF6251.LTContr)
End Sub

Private Sub Med_Calculation()
    ReturnVal = 0
End Sub

Private Sub Mining_Calculation()
    ReturnVal = GetCurrency(USF6251.Mining)
End Sub

Private Sub MiscDed_Calculation()
    If GetBool(IAF1040.CombMFS) = True And GetBool(IAF1040.ItemCheck) = True Then
        ReturnVal = CDollar(GetFloat(IASchA.Perc) * GetFloat(IASchA.AllowExp))
    ElseIf GetBool(IAF1040.ItemCheck) = True Then
        ReturnVal = GetCurrency(IASchA.AllowExp)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Multiply1_Calculation()
    ReturnVal = CDollar(GetFloat(IA6251.AdjAMTInc1) * 0.25)
End Sub

Private Sub Names_Calculation()
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetString(IARequired.TPCombName)
    Else
        ReturnVal = GetString(IARequired.CombNames)
    End If
End Sub

Private Sub NOL_Calculation()
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetCurrency(IAOthAdj.TIANOL)
    Else
        ReturnVal = GetCurrency(IAOthAdj.TIANOL) + GetCurrency(IAOthAdj.SIANOL)
    End If
End Sub

Private Sub PALS_Calculation()
    ReturnVal = GetCurrency(USF6251.PALs)
End Sub

Private Sub Post86Depr_Calculation()
'review new line 13 instructions and determine if we need to make an adjustment for any IA depr differences or if we should add an alert and note in Q&A
'For 2017 added alerts and Q&A for taxpayer and spouse 6251
    ReturnVal = GetCurrency(USF6251.Post86Depr)
End Sub

Private Sub PrInstall_Calculation()
    ReturnVal = Abs(GetCurrency(IA6251.Install))
End Sub

Private Sub Print_Calculation()
    If GetCurrency(IA6251.TotAMT) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PrItmLimit_Calculation()
    ReturnVal = Abs(GetCurrency(IA6251.ItmLimit))
End Sub

Private Sub PrTaxRfd_Calculation()
    ReturnVal = Abs(GetCurrency(IA6251.TaxRfd))
End Sub

Private Sub PYNRAMT_Calculation()
    ReturnVal = MaxValue(0, CDollar(GetFloat(IA6251.AMT) * GetFloat(IA6251.PYNRRatio)))
End Sub

Private Sub PYNRAMTIncNI_Calculation()
    If GetBool(IAF126.TpPYNR) = True Then
        ReturnVal = MaxValue(0, GetCurrency(IAF126.ANet) + GetCurrency(IA6251.PYNRAMTInc))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PYNRRatio_Calculation()
    If GetCurrency(IA6251.TotAMTInc) = 0 Then
        ReturnVal = 0
    Else
        ReturnVal = MinValue(1#, Round(GetFloat(IA6251.PYNRAMTIncNI) / GetFloat(IA6251.TotAMTInc), 3))
    End If
End Sub

Private Sub RegTax_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAF1040.AAltTax) - GetCurrency(IAF1040.AExemCr))
End Sub

Private Sub RelAdj_Calculation()
'need to verify if should remove fed 6251 line 3 amounts for .F461 and .F8990 and .stdDed, seems like should remove since these were not preference items in the past and are only being made on federal due to TCJA and both of these are Iowa nonconformity items.
'.LargePart is on line 11 of IA 6251
    ReturnVal = GetCurrency(USF6251.RelAdj) - GetCurrency(USF6251.LargePart) - GetCurrency(USF6251.F461) - GetCurrency(USF6251.F8990) - GetCurrency(USF6251.StdDed)
End Sub

Private Sub Research_Calculation()
    ReturnVal = GetCurrency(USF6251.Research)
End Sub

Private Sub Sec1202_Calculation()
    ReturnVal = GetCurrency(USF6251.Sec1202)
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

Private Sub Subtotal_Calculation()
    ReturnVal = GetCurrency(IA6251.AMTInc) + GetCurrency(IA6251.TaxInc) + GetCurrency(IA6251.NOL)
End Sub

Private Sub Taxes_Calculation()
    If GetBool(IAF1040.CombMFS) = True And GetBool(IAF1040.ItemCheck) = True Then
        ReturnVal = CDollar(GetFloat(IASchA.Perc) * GetFloat(IASchA.TaxPd))
    ElseIf GetBool(IAF1040.ItemCheck) = True Then
        ReturnVal = GetCurrency(IASchA.TaxPd)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TaxInc_Calculation()
    ReturnVal = GetCurrency(IAF1040.ATaxInc)
End Sub

Private Sub TaxRfd_Calculation()
    ReturnVal = GetCurrency(IAF1040.ARefund) *  -1
End Sub

Private Sub TentAMT_Calculation()
    ReturnVal = CDollar(GetFloat(IA6251.AdjAMTInc2) * 0.067)
End Sub

Private Sub TotAMT_Calculation()
    If GetNumber(IA6251.DoNotComplete) = 1 Then
        ReturnVal = 0
    ElseIf GetBool(IAF126.TpPYNR) = True Then
        ReturnVal = GetCurrency(IA6251.PYNRAMT)
    Else
        ReturnVal = GetCurrency(IA6251.AMT)
    End If
End Sub

Private Sub TotAMTInc_Calculation()
    If GetBool(IAF126.TpPYNR) = True Then
        ReturnVal = MaxValue(0, GetCurrency(IAF126.AAllSource) + GetCurrency(IA6251.AMTInc))
    Else
        ReturnVal = 0
    End If
End Sub

