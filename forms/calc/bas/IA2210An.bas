Private Sub AskItmDed_Calculation()
    If GetBool(IAF1040.ItemCheck) = True Then
        ReturnVal = 1
    ElseIf GetCurrency(IA2210An.Q1ItmDed) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA2210An.Q2ItmDed) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA2210An.Q3ItmDed) <> 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Description_Calculation()
    ReturnVal = GetString(IA2210An.Names)
End Sub

Private Sub Names_Calculation()
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetString(IARequired.TPCombName)
    Else
        ReturnVal = GetString(IARequired.CombNames)
    End If
End Sub

Private Sub Print_Calculation()
    If GetBool(IA2210.AnInc) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q1AIInstall_Calculation()
    ReturnVal = MinValue(GetCurrency(IA2210An.Q1BalDue), GetCurrency(IA2210An.Q1TotPay))
End Sub

Private Sub Q1AnFedPay_Calculation()
    ReturnVal = CDollar(GetFloat(IA2210An.Q1FedPay) * 4#)
End Sub

Private Sub Q1AnInc_Calculation()
    ReturnVal = CDollar(GetFloat(IA2210An.Q1NetInc) * 4#)
End Sub

Private Sub Q1AnItmDed_Calculation()
    If GetBool(IAF1040.ItemCheck) = True Then
        ReturnVal = CDollar(GetFloat(IA2210An.Q1ItmDed) * 4#)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q1Balance_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA2210An.Q1TotTax) - GetCurrency(IA2210An.Q1ExemCr) - GetCurrency(IA2210An.Q1NonRefCr) - GetCurrency(IA2210An.Q1RefCr))
End Sub

Private Sub Q1BalDue_Calculation()
    ReturnVal = GetCurrency(IA2210An.Q1PerTax)
End Sub

Private Sub Q1Deduct_Calculation()
    ReturnVal = MaxValue(GetCurrency(IA2210An.Q1AnItmDed), GetCurrency(IA2210An.Q1StndDed))
End Sub

Private Sub Q1ExemCr_Calculation()
    ReturnVal = GetCurrency(IAF1040.AExemCr)
End Sub

Private Sub Q1PerTax_Calculation()
    ReturnVal = CDollar(GetFloat(IA2210An.Q1Balance) * 0.225)
End Sub

Private Sub Q1ReqPay_Calculation()
    ReturnVal = GetCurrency(IA2210.Q1Install)
End Sub

Private Sub Q1StndDed_Calculation()
' updated for 2018
    If IAFS() = 2 Or IAFS() = 5 Or IAFS() = 6 Then
        ReturnVal = 5000@
    Else
        ReturnVal = 2030@
    End If
End Sub

Private Sub Q1Tax_Calculation()
' updated for 2018

    Dim Mid As Currency
    Dim MidInt As Long
    Dim TotTaxInc As Currency
    
    TotTaxInc = GetCurrency(IA2210An.Q1TaxInc)
    
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

Private Sub Q1TaxInc_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA2210An.Q1AnInc) - GetCurrency(IA2210An.Q1AnFedPay) - GetCurrency(IA2210An.Q1Deduct))
End Sub

Private Sub Q1TotPay_Calculation()
    ReturnVal = GetCurrency(IA2210An.Q1ReqPay)
End Sub

Private Sub Q1TotTax_Calculation()
    ReturnVal = GetCurrency(IA2210An.Q1Tax) + GetCurrency(IA2210An.Q1OthTax)
End Sub

Private Sub Q1Unpay_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA2210An.Q1TotPay) - GetCurrency(IA2210An.Q1BalDue))
End Sub

Private Sub Q2AIInstall_Calculation()
    ReturnVal = MinValue(GetCurrency(IA2210An.Q2BalDue), GetCurrency(IA2210An.Q2TotPay))
End Sub

Private Sub Q2AnFedPay_Calculation()
    ReturnVal = CDollar(GetFloat(IA2210An.Q2FedPay) * 2.4)
End Sub

Private Sub Q2AnInc_Calculation()
    ReturnVal = CDollar(GetFloat(IA2210An.Q2NetInc) * 2.4)
End Sub

Private Sub Q2AnItmDed_Calculation()
    If GetBool(IAF1040.ItemCheck) = True Then
        ReturnVal = CDollar(GetFloat(IA2210An.Q2ItmDed) * 2.4)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q2Balance_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA2210An.Q2TotTax) - GetCurrency(IA2210An.Q2ExemCr) - GetCurrency(IA2210An.Q2NonRefCr) - GetCurrency(IA2210An.Q2RefCr))
End Sub

Private Sub Q2BalDue_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA2210An.Q2PerTax) - GetCurrency(IA2210An.Q2PQInst))
End Sub

Private Sub Q2Deduct_Calculation()
    ReturnVal = MaxValue(GetCurrency(IA2210An.Q2AnItmDed), GetCurrency(IA2210An.Q2StndDed))
End Sub

Private Sub Q2ExemCr_Calculation()
    ReturnVal = GetCurrency(IA2210An.Q1ExemCr)
End Sub

Private Sub Q2PerTax_Calculation()
    ReturnVal = CDollar(GetFloat(IA2210An.Q2Balance) * 0.45)
End Sub

Private Sub Q2PQInst_Calculation()
    ReturnVal = GetCurrency(IA2210An.Q1AIInstall)
End Sub

Private Sub Q2PQUnpay_Calculation()
    ReturnVal = GetCurrency(IA2210An.Q1Unpay)
End Sub

Private Sub Q2ReqPay_Calculation()
    ReturnVal = GetCurrency(IA2210.Q2Install)
End Sub

Private Sub Q2StndDed_Calculation()
    ReturnVal = GetCurrency(IA2210An.Q1StndDed)
End Sub

Private Sub Q2Tax_Calculation()
' updated for 2018

    Dim Mid As Currency
    Dim MidInt As Long
    Dim TotTaxInc As Currency
    
    TotTaxInc = GetCurrency(IA2210An.Q2TaxInc)
    
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

Private Sub Q2TaxInc_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA2210An.Q2AnInc) - GetCurrency(IA2210An.Q2AnFedPay) - GetCurrency(IA2210An.Q2Deduct))
End Sub

Private Sub Q2TotPay_Calculation()
    ReturnVal = GetCurrency(IA2210An.Q2ReqPay) + GetCurrency(IA2210An.Q2PQUnpay)
End Sub

Private Sub Q2TotTax_Calculation()
    ReturnVal = GetCurrency(IA2210An.Q2Tax) + GetCurrency(IA2210An.Q2OthTax)
End Sub

Private Sub Q2Unpay_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA2210An.Q2TotPay) - GetCurrency(IA2210An.Q2BalDue))
End Sub

Private Sub Q3AIInstall_Calculation()
    ReturnVal = MinValue(GetCurrency(IA2210An.Q3BalDue), GetCurrency(IA2210An.Q3TotPay))
End Sub

Private Sub Q3AnFedPay_Calculation()
    ReturnVal = CDollar(GetFloat(IA2210An.Q3FedPay) * 1.5)
End Sub

Private Sub Q3AnInc_Calculation()
    ReturnVal = CDollar(GetFloat(IA2210An.Q3NetInc) * 1.5)
End Sub

Private Sub Q3AnItmDed_Calculation()
    If GetBool(IAF1040.ItemCheck) = True Then
        ReturnVal = CDollar(GetFloat(IA2210An.Q3ItmDed) * 1.5)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q3Balance_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA2210An.Q3TotTax) - GetCurrency(IA2210An.Q3ExemCr) - GetCurrency(IA2210An.Q3NonRefCr) - GetCurrency(IA2210An.Q3RefCr))
End Sub

Private Sub Q3BalDue_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA2210An.Q3PerTax) - GetCurrency(IA2210An.Q3PQInst))
End Sub

Private Sub Q3Deduct_Calculation()
    ReturnVal = MaxValue(GetCurrency(IA2210An.Q3AnItmDed), GetCurrency(IA2210An.Q3StndDed))
End Sub

Private Sub Q3ExemCr_Calculation()
    ReturnVal = GetCurrency(IA2210An.Q1ExemCr)
End Sub

Private Sub Q3PerTax_Calculation()
    ReturnVal = CDollar(GetFloat(IA2210An.Q3Balance) * 0.675)
End Sub

Private Sub Q3PQInst_Calculation()
    ReturnVal = GetCurrency(IA2210An.Q1AIInstall) + GetCurrency(IA2210An.Q2AIInstall)
End Sub

Private Sub Q3PQUnpay_Calculation()
    ReturnVal = GetCurrency(IA2210An.Q2Unpay)
End Sub

Private Sub Q3ReqPay_Calculation()
    ReturnVal = GetCurrency(IA2210.Q3Install)
End Sub

Private Sub Q3StndDed_Calculation()
    ReturnVal = GetCurrency(IA2210An.Q1StndDed)
End Sub

Private Sub Q3Tax_Calculation()
' updated for 2018

    Dim Mid As Currency
    Dim MidInt As Long
    Dim TotTaxInc As Currency
    
    TotTaxInc = GetCurrency(IA2210An.Q3TaxInc)
    
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

Private Sub Q3TaxInc_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA2210An.Q3AnInc) - GetCurrency(IA2210An.Q3AnFedPay) - GetCurrency(IA2210An.Q3Deduct))
End Sub

Private Sub Q3TotPay_Calculation()
    ReturnVal = GetCurrency(IA2210An.Q3ReqPay) + GetCurrency(IA2210An.Q3PQUnpay)
End Sub

Private Sub Q3TotTax_Calculation()
    ReturnVal = GetCurrency(IA2210An.Q3Tax) + GetCurrency(IA2210An.Q3OthTax)
End Sub

Private Sub Q3Unpay_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA2210An.Q3TotPay) - GetCurrency(IA2210An.Q3BalDue))
End Sub

Private Sub Q4AIInstall_Calculation()
    ReturnVal = MinValue(GetCurrency(IA2210An.Q4BalDue), GetCurrency(IA2210An.Q4TotPay))
End Sub

Private Sub Q4AnFedPay_Calculation()
    ReturnVal = GetCurrency(IA2210An.Q4FedPay)
End Sub

Private Sub Q4AnInc_Calculation()
    ReturnVal = GetCurrency(IA2210An.Q4NetInc)
End Sub

Private Sub Q4AnItmDed_Calculation()
    ReturnVal = GetCurrency(IA2210An.Q4ItmDed)
End Sub

Private Sub Q4Balance_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA2210An.Q4TotTax) - GetCurrency(IA2210An.Q4ExemCr) - GetCurrency(IA2210An.Q4NonRefCr) - GetCurrency(IA2210An.Q4RefCr))
End Sub

Private Sub Q4BalDue_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA2210An.Q4PerTax) - GetCurrency(IA2210An.Q4PQInst))
End Sub

Private Sub Q4Deduct_Calculation()
    ReturnVal = MaxValue(GetCurrency(IA2210An.Q4AnItmDed), GetCurrency(IA2210An.Q4StndDed))
End Sub

Private Sub Q4ExemCr_Calculation()
    ReturnVal = GetCurrency(IA2210An.Q1ExemCr)
End Sub

Private Sub Q4FedPay_Calculation()
    ReturnVal = GetCurrency(IAF1040.AFedDed) - GetCurrency(IAF1040.AFedTax)
End Sub

Private Sub Q4ItmDed_Calculation()
    If GetBool(IAF1040.ItemCheck) = True Then
        ReturnVal = GetCurrency(IAF1040.ADedBox)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q4NetInc_Calculation()
    ReturnVal = GetCurrency(IAF1040.ANet)
End Sub

Private Sub Q4NonRefCr_Calculation()
    ReturnVal = GetCurrency(IAF1040.ATuit) + GetCurrency(IAF1040.AVolFireCr) + GetCurrency(IAF1040.ACrNon) + GetCurrency(IAF1040.AOutState) + GetCurrency(IAF1040.AOthIACr)
End Sub

Private Sub Q4OthTax_Calculation()
    ReturnVal = GetCurrency(IAF1040.ALump) + GetCurrency(IAF1040.AIAMin)
End Sub

Private Sub Q4PerTax_Calculation()
    ReturnVal = CDollar(GetFloat(IA2210An.Q4Balance) * 0.9)
End Sub

Private Sub Q4PQInst_Calculation()
    ReturnVal = GetCurrency(IA2210An.Q1AIInstall) + GetCurrency(IA2210An.Q2AIInstall) + GetCurrency(IA2210An.Q3AIInstall)
End Sub

Private Sub Q4PQUnpay_Calculation()
    ReturnVal = GetCurrency(IA2210An.Q3Unpay)
End Sub

Private Sub Q4RefCr_Calculation()
    ReturnVal = GetCurrency(IAF1040.AFuel) + GetCurrency(IAF1040.AChild) + GetCurrency(IAF1040.AIEIC) + GetCurrency(IAF1040.AOthRefCr)
End Sub

Private Sub Q4ReqPay_Calculation()
    ReturnVal = GetCurrency(IA2210.Q4Install)
End Sub

Private Sub Q4StndDed_Calculation()
    ReturnVal = GetCurrency(IA2210An.Q1StndDed)
End Sub

Private Sub Q4Tax_Calculation()
' updated for 2018

    Dim Mid As Currency
    Dim MidInt As Long
    Dim TotTaxInc As Currency
    
    TotTaxInc = GetCurrency(IA2210An.Q4TaxInc)
    
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

Private Sub Q4TaxInc_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA2210An.Q4AnInc) - GetCurrency(IA2210An.Q4AnFedPay) - GetCurrency(IA2210An.Q4Deduct))
End Sub

Private Sub Q4TotPay_Calculation()
    ReturnVal = GetCurrency(IA2210An.Q4ReqPay) + GetCurrency(IA2210An.Q4PQUnpay)
End Sub

Private Sub Q4TotTax_Calculation()
    ReturnVal = GetCurrency(IA2210An.Q4Tax) + GetCurrency(IA2210An.Q4OthTax)
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

