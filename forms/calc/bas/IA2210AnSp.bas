Private Sub AskItmDed_Calculation()
    If GetBool(IAF1040.ItemCheck) = True Then
        ReturnVal = 1
    ElseIf GetCurrency(IA2210AnSp.Q1ItmDed) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA2210AnSp.Q2ItmDed) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA2210AnSp.Q3ItmDed) <> 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Description_Calculation()
    ReturnVal = GetString(IA2210AnSp.Names)
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.SPCombName)
End Sub

Private Sub Print_Calculation()
    If GetBool(IAF1040.CombMFS) = False Then
        ReturnVal = 0
    ElseIf GetBool(IA2210Sp.AnInc) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q1AIInstall_Calculation()
    ReturnVal = MinValue(GetCurrency(IA2210AnSp.Q1BalDue), GetCurrency(IA2210AnSp.Q1TotPay))
End Sub

Private Sub Q1AnFedPay_Calculation()
    ReturnVal = CDollar(GetFloat(IA2210AnSp.Q1FedPay) * 4#)
End Sub

Private Sub Q1AnInc_Calculation()
    ReturnVal = CDollar(GetFloat(IA2210AnSp.Q1NetInc) * 4#)
End Sub

Private Sub Q1AnItmDed_Calculation()
    If GetBool(IAF1040.ItemCheck) = True Then
        ReturnVal = CDollar(GetFloat(IA2210AnSp.Q1ItmDed) * 4#)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q1Balance_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA2210AnSp.Q1TotTax) - GetCurrency(IA2210AnSp.Q1ExemCr) - GetCurrency(IA2210AnSp.Q1NonRefCr) - GetCurrency(IA2210AnSp.Q1RefCr))
End Sub

Private Sub Q1BalDue_Calculation()
    ReturnVal = GetCurrency(IA2210AnSp.Q1PerTax)
End Sub

Private Sub Q1Deduct_Calculation()
    ReturnVal = MaxValue(GetCurrency(IA2210AnSp.Q1AnItmDed), GetCurrency(IA2210AnSp.Q1StndDed))
End Sub

Private Sub Q1ExemCr_Calculation()
    ReturnVal = GetCurrency(IAF1040.BExemCr)
End Sub

Private Sub Q1PerTax_Calculation()
    ReturnVal = CDollar(GetFloat(IA2210AnSp.Q1Balance) * 0.225)
End Sub

Private Sub Q1ReqPay_Calculation()
    ReturnVal = GetCurrency(IA2210Sp.Q1Install)
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
    
    TotTaxInc = GetCurrency(IA2210AnSp.Q1TaxInc)
    
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
    ReturnVal = MaxValue(0, GetCurrency(IA2210AnSp.Q1AnInc) - GetCurrency(IA2210AnSp.Q1AnFedPay) - GetCurrency(IA2210AnSp.Q1Deduct))
End Sub

Private Sub Q1TotPay_Calculation()
    ReturnVal = GetCurrency(IA2210AnSp.Q1ReqPay)
End Sub

Private Sub Q1TotTax_Calculation()
    ReturnVal = GetCurrency(IA2210AnSp.Q1Tax) + GetCurrency(IA2210AnSp.Q1OthTax)
End Sub

Private Sub Q1Unpay_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA2210AnSp.Q1TotPay) - GetCurrency(IA2210AnSp.Q1BalDue))
End Sub

Private Sub Q2AIInstall_Calculation()
    ReturnVal = MinValue(GetCurrency(IA2210AnSp.Q2BalDue), GetCurrency(IA2210AnSp.Q2TotPay))
End Sub

Private Sub Q2AnFedPay_Calculation()
    ReturnVal = CDollar(GetFloat(IA2210AnSp.Q2FedPay) * 2.4)
End Sub

Private Sub Q2AnInc_Calculation()
    ReturnVal = CDollar(GetFloat(IA2210AnSp.Q2NetInc) * 2.4)
End Sub

Private Sub Q2AnItmDed_Calculation()
    If GetBool(IAF1040.ItemCheck) = True Then
        ReturnVal = CDollar(GetFloat(IA2210AnSp.Q2ItmDed) * 2.4)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q2Balance_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA2210AnSp.Q2TotTax) - GetCurrency(IA2210AnSp.Q2ExemCr) - GetCurrency(IA2210AnSp.Q2NonRefCr) - GetCurrency(IA2210AnSp.Q2RefCr))
End Sub

Private Sub Q2BalDue_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA2210AnSp.Q2PerTax) - GetCurrency(IA2210AnSp.Q2PQInst))
End Sub

Private Sub Q2Deduct_Calculation()
    ReturnVal = MaxValue(GetCurrency(IA2210AnSp.Q2AnItmDed), GetCurrency(IA2210AnSp.Q2StndDed))
End Sub

Private Sub Q2ExemCr_Calculation()
    ReturnVal = GetCurrency(IA2210AnSp.Q1ExemCr)
End Sub

Private Sub Q2PerTax_Calculation()
    ReturnVal = CDollar(GetFloat(IA2210AnSp.Q2Balance) * 0.45)
End Sub

Private Sub Q2PQInst_Calculation()
    ReturnVal = GetCurrency(IA2210AnSp.Q1AIInstall)
End Sub

Private Sub Q2PQUnpay_Calculation()
    ReturnVal = GetCurrency(IA2210AnSp.Q1Unpay)
End Sub

Private Sub Q2ReqPay_Calculation()
    ReturnVal = GetCurrency(IA2210Sp.Q2Install)
End Sub

Private Sub Q2StndDed_Calculation()
    ReturnVal = GetCurrency(IA2210AnSp.Q1StndDed)
End Sub

Private Sub Q2Tax_Calculation()
' updated for 2018

    Dim Mid As Currency
    Dim MidInt As Long
    Dim TotTaxInc As Currency
    
    TotTaxInc = GetCurrency(IA2210AnSp.Q2TaxInc)
    
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
    ReturnVal = MaxValue(0, GetCurrency(IA2210AnSp.Q2AnInc) - GetCurrency(IA2210AnSp.Q2AnFedPay) - GetCurrency(IA2210AnSp.Q2Deduct))
End Sub

Private Sub Q2TotPay_Calculation()
    ReturnVal = GetCurrency(IA2210AnSp.Q2ReqPay) + GetCurrency(IA2210AnSp.Q2PQUnpay)
End Sub

Private Sub Q2TotTax_Calculation()
    ReturnVal = GetCurrency(IA2210AnSp.Q2Tax) + GetCurrency(IA2210AnSp.Q2OthTax)
End Sub

Private Sub Q2Unpay_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA2210AnSp.Q2TotPay) - GetCurrency(IA2210AnSp.Q2BalDue))
End Sub

Private Sub Q3AIInstall_Calculation()
    ReturnVal = MinValue(GetCurrency(IA2210AnSp.Q3BalDue), GetCurrency(IA2210AnSp.Q3TotPay))
End Sub

Private Sub Q3AnFedPay_Calculation()
    ReturnVal = CDollar(GetFloat(IA2210AnSp.Q3FedPay) * 1.5)
End Sub

Private Sub Q3AnInc_Calculation()
    ReturnVal = CDollar(GetFloat(IA2210AnSp.Q3NetInc) * 1.5)
End Sub

Private Sub Q3AnItmDed_Calculation()
    If GetBool(IAF1040.ItemCheck) = True Then
        ReturnVal = CDollar(GetFloat(IA2210AnSp.Q3ItmDed) * 1.5)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q3Balance_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA2210AnSp.Q3TotTax) - GetCurrency(IA2210AnSp.Q3ExemCr) - GetCurrency(IA2210AnSp.Q3NonRefCr) - GetCurrency(IA2210AnSp.Q3RefCr))
End Sub

Private Sub Q3BalDue_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA2210AnSp.Q3PerTax) - GetCurrency(IA2210AnSp.Q3PQInst))
End Sub

Private Sub Q3Deduct_Calculation()
    ReturnVal = MaxValue(GetCurrency(IA2210AnSp.Q3AnItmDed), GetCurrency(IA2210AnSp.Q3StndDed))
End Sub

Private Sub Q3ExemCr_Calculation()
    ReturnVal = GetCurrency(IA2210AnSp.Q1ExemCr)
End Sub

Private Sub Q3PerTax_Calculation()
    ReturnVal = CDollar(GetFloat(IA2210AnSp.Q3Balance) * 0.675)
End Sub

Private Sub Q3PQInst_Calculation()
    ReturnVal = GetCurrency(IA2210AnSp.Q1AIInstall) + GetCurrency(IA2210AnSp.Q2AIInstall)
End Sub

Private Sub Q3PQUnpay_Calculation()
    ReturnVal = GetCurrency(IA2210AnSp.Q2Unpay)
End Sub

Private Sub Q3ReqPay_Calculation()
    ReturnVal = GetCurrency(IA2210Sp.Q3Install)
End Sub

Private Sub Q3StndDed_Calculation()
    ReturnVal = GetCurrency(IA2210AnSp.Q1StndDed)
End Sub

Private Sub Q3Tax_Calculation()
' updated for 2018

    Dim Mid As Currency
    Dim MidInt As Long
    Dim TotTaxInc As Currency
    
    TotTaxInc = GetCurrency(IA2210AnSp.Q3TaxInc)
    
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
    ReturnVal = MaxValue(0, GetCurrency(IA2210AnSp.Q3AnInc) - GetCurrency(IA2210AnSp.Q3AnFedPay) - GetCurrency(IA2210AnSp.Q3Deduct))
End Sub

Private Sub Q3TotPay_Calculation()
    ReturnVal = GetCurrency(IA2210AnSp.Q3ReqPay) + GetCurrency(IA2210AnSp.Q3PQUnpay)
End Sub

Private Sub Q3TotTax_Calculation()
    ReturnVal = GetCurrency(IA2210AnSp.Q3Tax) + GetCurrency(IA2210AnSp.Q3OthTax)
End Sub

Private Sub Q3Unpay_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA2210AnSp.Q3TotPay) - GetCurrency(IA2210AnSp.Q3BalDue))
End Sub

Private Sub Q4AIInstall_Calculation()
    ReturnVal = MinValue(GetCurrency(IA2210AnSp.Q4BalDue), GetCurrency(IA2210AnSp.Q4TotPay))
End Sub

Private Sub Q4AnFedPay_Calculation()
    ReturnVal = GetCurrency(IA2210AnSp.Q4FedPay)
End Sub

Private Sub Q4AnInc_Calculation()
    ReturnVal = GetCurrency(IA2210AnSp.Q4NetInc)
End Sub

Private Sub Q4AnItmDed_Calculation()
    ReturnVal = GetCurrency(IA2210AnSp.Q4ItmDed)
End Sub

Private Sub Q4Balance_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA2210AnSp.Q4TotTax) - GetCurrency(IA2210AnSp.Q4ExemCr) - GetCurrency(IA2210AnSp.Q4NonRefCr) - GetCurrency(IA2210AnSp.Q4RefCr))
End Sub

Private Sub Q4BalDue_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA2210AnSp.Q4PerTax) - GetCurrency(IA2210AnSp.Q4PQInst))
End Sub

Private Sub Q4Deduct_Calculation()
    ReturnVal = MaxValue(GetCurrency(IA2210AnSp.Q4AnItmDed), GetCurrency(IA2210AnSp.Q4StndDed))
End Sub

Private Sub Q4ExemCr_Calculation()
    ReturnVal = GetCurrency(IA2210AnSp.Q1ExemCr)
End Sub

Private Sub Q4FedPay_Calculation()
    ReturnVal = GetCurrency(IAF1040.BFedDed) - GetCurrency(IAF1040.BFedTax)
End Sub

Private Sub Q4ItmDed_Calculation()
    If GetBool(IAF1040.ItemCheck) = True Then
        ReturnVal = GetCurrency(IAF1040.BDedBox)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q4NetInc_Calculation()
    ReturnVal = GetCurrency(IAF1040.BNet)
End Sub

Private Sub Q4NonRefCr_Calculation()
    ReturnVal = GetCurrency(IAF1040.BTuit) + GetCurrency(IAF1040.BVolFireCr) + GetCurrency(IAF1040.BCrNon) + GetCurrency(IAF1040.BOutState) + GetCurrency(IAF1040.BOthIACr)
End Sub

Private Sub Q4OthTax_Calculation()
    ReturnVal = GetCurrency(IAF1040.BLump) + GetCurrency(IAF1040.BIAMin)
End Sub

Private Sub Q4PerTax_Calculation()
    ReturnVal = CDollar(GetFloat(IA2210AnSp.Q4Balance) * 0.9)
End Sub

Private Sub Q4PQInst_Calculation()
    ReturnVal = GetCurrency(IA2210AnSp.Q1AIInstall) + GetCurrency(IA2210AnSp.Q2AIInstall) + GetCurrency(IA2210AnSp.Q3AIInstall)
End Sub

Private Sub Q4PQUnpay_Calculation()
    ReturnVal = GetCurrency(IA2210AnSp.Q3Unpay)
End Sub

Private Sub Q4RefCr_Calculation()
    ReturnVal = GetCurrency(IAF1040.BFuel) + GetCurrency(IAF1040.BChild) + GetCurrency(IAF1040.BIEIC) + GetCurrency(IAF1040.BOthRefCr)
End Sub

Private Sub Q4ReqPay_Calculation()
    ReturnVal = GetCurrency(IA2210Sp.Q4Install)
End Sub

Private Sub Q4StndDed_Calculation()
    ReturnVal = GetCurrency(IA2210AnSp.Q1StndDed)
End Sub

Private Sub Q4Tax_Calculation()
' updated for 2018

    Dim Mid As Currency
    Dim MidInt As Long
    Dim TotTaxInc As Currency
    
    TotTaxInc = GetCurrency(IA2210AnSp.Q4TaxInc)
    
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
    ReturnVal = MaxValue(0, GetCurrency(IA2210AnSp.Q4AnInc) - GetCurrency(IA2210AnSp.Q4AnFedPay) - GetCurrency(IA2210AnSp.Q4Deduct))
End Sub

Private Sub Q4TotPay_Calculation()
    ReturnVal = GetCurrency(IA2210AnSp.Q4ReqPay) + GetCurrency(IA2210AnSp.Q4PQUnpay)
End Sub

Private Sub Q4TotTax_Calculation()
    ReturnVal = GetCurrency(IA2210AnSp.Q4Tax) + GetCurrency(IA2210AnSp.Q4OthTax)
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SpouseSSN)
End Sub

