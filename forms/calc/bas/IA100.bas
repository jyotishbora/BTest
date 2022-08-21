Private Sub Common_Calculation()
    If GetBool(IAF1040.MFJ) = True Then
        ReturnVal = GetString(USWBasicInfo.CombFirst)
    Else
        ReturnVal = GetString(USWBasicInfo.TPCommon)
    End If
End Sub

Private Sub MEF100SP_Calculation()
    If GetBool(IA100.Spouse) = True And GetBool(IA100.Print) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub MEF100TP_Calculation()
    If GetBool(IA100.Taxpayer) = True And GetBool(IA100.Print) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Names_Calculation()
    If GetBool(IA100.Spouse) = True Then
        ReturnVal = GetString(IARequired.SPCombName)
    Else
        ReturnVal = GetString(IARequired.TPCombName)
    End If
End Sub

Private Sub P2Gain_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA100.P2SalesPx) - GetCurrency(IA100.P2Cost))
End Sub

Private Sub P2TPSharePerc_Calculation()
    ReturnVal = GetFloat(IA100.P2TPShare) * 100
End Sub

Private Sub Print_Calculation()
    If GetCurrency(IA100.P6CGD) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SpouseCommon_Calculation()
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetString(USWBasicInfo.SPCommon)
    Else
        ReturnVal = "Not Applicable"
    End If
End Sub

Private Sub SSN_Calculation()
    If GetBool(IA100.Spouse) = True Then
        ReturnVal = GetString(IAF1040.SpouseSSN)
    Else
        ReturnVal = GetString(IAF1040.SSN)
    End If
End Sub

