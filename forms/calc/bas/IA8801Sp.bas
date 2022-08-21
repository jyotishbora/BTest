Private Sub AMTCR_Calculation()
    ReturnVal = MinValue(GetCurrency(IA8801Sp.MaxAMT), GetCurrency(IA8801Sp.CYRegTax))
End Sub

Private Sub ApporRegTx_Calculation()
    ReturnVal = GetCurrency(IA8801Sp.CYTax) - GetCurrency(IA8801Sp.PYNRCr)
End Sub

Private Sub CYAMT_Calculation()
    If GetBool(IAF1040.CombMFS) = False Then
        ReturnVal = 0
    ElseIf GetBool(IAF126.SpPYNR) = True Then
        ReturnVal = MaxValue(0, CDollar(GetFloat(IA6251Sp.TentAMT) * GetFloat(IA6251Sp.PYNRRatio)))
    Else
        ReturnVal = GetCurrency(IA6251Sp.TentAMT)
    End If
End Sub

Private Sub CYCarryforward_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA8801Sp.TotalPYAMT) - GetCurrency(IA8801Sp.AMTCR))
End Sub

Private Sub CYRegTax_Calculation()
    If GetCurrency(IA8801Sp.ExcRegTax) = 0 Then
        ReturnVal = 0
    Else
        ReturnVal = MaxValue(0, GetCurrency(IA8801Sp.CYTax) - GetCurrency(IA8801Sp.TotCr))
    End If
End Sub

Private Sub CYTax_Calculation()
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetCurrency(IAF1040.BAltTax)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Description_Calculation()
    Dim Total As Currency
    
    Total = GetCurrency(IA8801Sp.AMTCR)
    
    ReturnVal = CStr(Total) & " Credit"
End Sub

Private Sub EFile_Calculation()
    If GetCurrency(IA8801Sp.AMTCR) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub ExcRegTax_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA8801Sp.ApporRegTx) - GetCurrency(IA8801Sp.CYAMT))
End Sub

Private Sub MaxAMT_Calculation()
    ReturnVal = MinValue(GetCurrency(IA8801Sp.TotalPYAMT), GetCurrency(IA8801Sp.ExcRegTax))
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.SPCombName)
End Sub

Private Sub Print_Calculation()
    If GetCurrency(IA8801Sp.AMTCR) > 0 Or GetCurrency(IA8801Sp.CYCarryforward) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PYAMT_Calculation()
    If GetBool(IAF1040.CombMFS) = False Then
        ReturnVal = 0
    ElseIf GetString(USZIA1040.IAPYFS) = GetString(IARequired.FilingStatus) Then
        ReturnVal = GetCurrency(USZIA1040.IAPYMinTaxB)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PYCarryforward_Calculation()
    ReturnVal = GetCurrency(USZIA1040.IAPY8801CFSp)
End Sub

Private Sub PYNRCr_Calculation()
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetCurrency(IAF1040.BCrNon)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SpouseSSN)
End Sub

Private Sub Sum148Cr_Calculation()
    If GetCurrency(IA8801Sp.ExcRegTax) = 0 Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetCurrency(IA148Sp.TotNonRefNo8801)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SumCr_Calculation()
    If GetCurrency(IA8801Sp.ExcRegTax) = 0 Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetCurrency(IAF1040.BCredits) + GetCurrency(IAF1040.BCrNon) + GetCurrency(IAF1040.BOutState)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TotalPYAMT_Calculation()
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetCurrency(IA8801Sp.PYAMT) + GetCurrency(IA8801Sp.PYCarryforward)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TotCr_Calculation()
    ReturnVal = GetCurrency(IA8801Sp.SumCr) + GetCurrency(IA8801Sp.Sum148Cr)
End Sub

