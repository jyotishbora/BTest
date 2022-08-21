Private Sub AdjAMTInc1_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA6251Sp.AMTTaxInc) - GetCurrency(IA6251Sp.Exemption2))
End Sub

Private Sub AdjAMTInc2_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA6251Sp.AMTTaxInc) - GetCurrency(IA6251Sp.AdjExempt))
End Sub

Private Sub AdjExempt_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA6251Sp.Exemption1) - GetCurrency(IA6251Sp.Multiply1))
End Sub

Private Sub AdjGain_Calculation()
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = MaxValue(0, GetCurrency(USF6251.AdjGain) - GetCurrency(IA6251.AdjGain))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AMT_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA6251Sp.TentAMT) - GetCurrency(IA6251Sp.RegTax))
End Sub

Private Sub AMTInc_Calculation()
    ReturnVal = GetCurrency(IA6251Sp.Med) + GetCurrency(IA6251Sp.Taxes) + GetCurrency(IA6251Sp.Int) + GetCurrency(IA6251Sp.MiscDed) + GetCurrency(IA6251Sp.ItmLimit) + GetCurrency(IA6251Sp.TaxRfd) + GetCurrency(IA6251Sp.InvInt) + GetCurrency(IA6251Sp.Sec1202) + GetCurrency(IA6251Sp.ISO) + GetCurrency(IA6251Sp.Est) + GetCurrency(IA6251Sp.LargePart) + GetCurrency(IA6251Sp.AdjGain) + GetCurrency(IA6251Sp.Post86Depr) + GetCurrency(IA6251Sp.PALS) + GetCurrency(IA6251Sp.LossLim) + GetCurrency(IA6251Sp.Circ) + GetCurrency(IA6251Sp.LTContr) + GetCurrency(IA6251Sp.Mining) + GetCurrency(IA6251Sp.Research) + GetCurrency(IA6251Sp.Install) + GetCurrency(IA6251Sp.RelAdj)
End Sub

Private Sub AMTTaxInc_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA6251Sp.Subtotal) - GetCurrency(IA6251Sp.LimAMTNOL))
End Sub

Private Sub Circ_Calculation()
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = MaxValue(0, GetCurrency(USF6251.Circ) - GetCurrency(IA6251.Circ))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Description_Calculation()
    Dim Total As Currency
    
    Total = GetCurrency(IA6251Sp.TotAMT)
    
    ReturnVal = CStr(Total) & " AMT"
End Sub

Private Sub EFile_Calculation()
    If GetNumber(IA6251.DoNotComplete) = 1 Then
        ReturnVal = 0
    ElseIf GetBool(IA6251Sp.Print) = True Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251Sp.Med) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251Sp.Taxes) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251Sp.Int) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251Sp.MiscDed) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251Sp.ItmLimit) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251Sp.TaxRfd) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251Sp.InvInt) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251Sp.Sec1202) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251Sp.ISO) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251Sp.Est) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251Sp.LargePart) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251Sp.AdjGain) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251Sp.Post86Depr) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251Sp.PALS) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251Sp.LossLim) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251Sp.Circ) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251Sp.LTContr) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251Sp.Mining) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251Sp.Research) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251Sp.Install) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA6251Sp.RelAdj) <> 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Est_Calculation()
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = MaxValue(0, GetCurrency(USF6251.Est) - GetCurrency(IA6251.Est))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Exemption1_Calculation()
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = 17500@
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Exemption2_Calculation()
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = 75000@
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Install_Calculation()
    Dim FedInstall As Currency
    
    FedInstall = GetCurrency(USF6251.Install) *  -1

    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = FedInstall - GetCurrency(IA6251.Install)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Int_Calculation()
    If GetBool(IAF1040.CombMFS) = True And GetBool(IAF1040.ItemCheck) = True Then
        ReturnVal = MaxValue(0, GetCurrency(IAW6251MortInt.AMTInt) - GetCurrency(IA6251.Int))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub InvInt_Calculation()
    If GetBool(IAF1040.CombMFS) = True And GetBool(IAF1040.ItemCheck) = True Then
        ReturnVal = MaxValue(0, GetCurrency(USF6251.InvInt) - GetCurrency(IA6251.InvInt))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub ISO_Calculation()
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = MaxValue(0, GetCurrency(USF6251.ISO) - GetCurrency(IA6251.ISO))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub ItmLimit_Calculation()
    Dim Limit As Currency
    
    Limit = GetCurrency(IAWItmDed.Limit) *  -1

    If GetBool(IAF1040.CombMFS) = True And GetBool(IAF1040.ItemCheck) = True Then
        ReturnVal = Limit - GetCurrency(IA6251.ItmLimit)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub LargePart_Calculation()
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = MaxValue(0, GetCurrency(USF6251.LargePart) - GetCurrency(IA6251.LargePart))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub LimAMTNOL_Calculation()
    Dim TEst As Currency
    Dim Unlim As Currency
    Dim AMTL As Currency
    
    TEst = GetCurrency(IA6251Sp.Subtotal)
    Unlim = Abs(GetCurrency(IA6251Sp.AMTNOL))
    
    If TEst > 0 Then
        AMTL = MinValue(Unlim, CDollar(CDbl(TEst) * 0.9))
    Else
        AMTL = 0
    End If
    
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = AMTL
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub LossLim_Calculation()
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = MaxValue(0, GetCurrency(USF6251.LossLim) - GetCurrency(IA6251.LossLim))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub LTContr_Calculation()
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = MaxValue(0, GetCurrency(USF6251.LTContr) - GetCurrency(IA6251.LTContr))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Med_Calculation()
    ReturnVal = 0
End Sub

Private Sub Mining_Calculation()
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = MaxValue(0, GetCurrency(USF6251.Mining) - GetCurrency(IA6251.Mining))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub MiscDed_Calculation()
    If GetBool(IAF1040.CombMFS) = True And GetBool(IAF1040.ItemCheck) = True Then
        ReturnVal = MaxValue(0, GetCurrency(IASchA.AllowExp) - GetCurrency(IA6251.MiscDed))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Multiply1_Calculation()
    ReturnVal = CDollar(GetFloat(IA6251Sp.AdjAMTInc1) * 0.25)
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.SPCombName)
End Sub

Private Sub NOL_Calculation()
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetCurrency(IAOthAdj.SIANOL)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PALS_Calculation()
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = MaxValue(0, GetCurrency(USF6251.PALS) - GetCurrency(IA6251.PALS))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Post86Depr_Calculation()
'review new line 13 instructions and determine if we need to make an adjustment for any IA depr differences or if we should add an alert and note in Q&A
'For 2017 changed to default calc this field and interview and added an alert
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = MaxValue(0, GetCurrency(USF6251.Post86Depr) - GetCurrency(IA6251.Post86Depr))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PrInstall_Calculation()
    ReturnVal = Abs(GetCurrency(IA6251Sp.Install))
End Sub

Private Sub Print_Calculation()
    If GetBool(IAF1040.CombMFS) = False Then
        ReturnVal = 0
    ElseIf GetCurrency(IA6251Sp.TotAMT) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PrItmLimit_Calculation()
    ReturnVal = Abs(GetCurrency(IA6251Sp.ItmLimit))
End Sub

Private Sub PrTaxRfd_Calculation()
    ReturnVal = Abs(GetCurrency(IA6251Sp.TaxRfd))
End Sub

Private Sub PYNRAMT_Calculation()
    ReturnVal = MaxValue(0, CDollar(GetFloat(IA6251Sp.AMT) * GetFloat(IA6251Sp.PYNRRatio)))
End Sub

Private Sub PYNRAMTIncNI_Calculation()
    If GetBool(IAF126.SpPYNR) = True Then
        ReturnVal = MaxValue(0, GetCurrency(IAF126.BNet) + GetCurrency(IA6251Sp.PYNRAMTInc))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PYNRRatio_Calculation()
    If GetCurrency(IA6251Sp.TotAMTInc) = 0 Then
        ReturnVal = 0
    Else
        ReturnVal = MinValue(1#, Round(GetFloat(IA6251Sp.PYNRAMTIncNI) / GetFloat(IA6251Sp.TotAMTInc), 3))
    End If
End Sub

Private Sub RegTax_Calculation()
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = MaxValue(0, GetCurrency(IAF1040.BAltTax) - GetCurrency(IAF1040.BExemCr))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub RelAdj_Calculation()
    Dim IARelAdj As Currency
    
    IARelAdj = GetCurrency(USF6251.RelAdj) - GetCurrency(USF6251.LargePart) - GetCurrency(USF6251.F461) - GetCurrency(USF6251.F8990) - GetCurrency(USF6251.StdDed)
    
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = MaxValue(0, IARelAdj - GetCurrency(IA6251.RelAdj))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Research_Calculation()
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = MaxValue(0, GetCurrency(USF6251.Research) - GetCurrency(IA6251.Research))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Sec1202_Calculation()
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = MaxValue(0, GetCurrency(USF6251.Sec1202) - GetCurrency(IA6251.Sec1202))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SpUserMod_Calculation()
    If GetStatus(UserModifiedStatus) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SpouseSSN)
End Sub

Private Sub Subtotal_Calculation()
    ReturnVal = GetCurrency(IA6251Sp.AMTInc) + GetCurrency(IA6251Sp.TaxInc) + GetCurrency(IA6251Sp.NOL)
End Sub

Private Sub Taxes_Calculation()
    If GetBool(IAF1040.CombMFS) = True And GetBool(IAF1040.ItemCheck) = True Then
        ReturnVal = MaxValue(0, GetCurrency(IASchA.TaxPd) - GetCurrency(IA6251.Taxes))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TaxInc_Calculation()
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetCurrency(IAF1040.BTaxInc)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TaxRfd_Calculation()
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetCurrency(IAF1040.BRefund) *  -1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TentAMT_Calculation()
    ReturnVal = CDollar(GetFloat(IA6251Sp.AdjAMTInc2) * 0.067)
End Sub

Private Sub TotAMT_Calculation()
    If GetNumber(IA6251.DoNotComplete) = 1 Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.CombMFS) = False Then
        ReturnVal = 0
    ElseIf GetBool(IAF126.SpPYNR) = True Then
        ReturnVal = GetCurrency(IA6251Sp.PYNRAMT)
    Else
        ReturnVal = GetCurrency(IA6251Sp.AMT)
    End If
End Sub

Private Sub TotAMTInc_Calculation()
    If GetBool(IAF126.SpPYNR) = True Then
        ReturnVal = MaxValue(0, GetCurrency(IAF126.BAllSource) + GetCurrency(IA6251Sp.AMTInc))
    Else
        ReturnVal = 0
    End If
End Sub

