Private Sub AMTInt_Calculation()
    If GetBool(USWResidency.F1040NR) = True Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.ItemCheck) = True Then
        ReturnVal = MinValue(GetCurrency(IAW6251MortInt.TotMortInt), GetCurrency(IAW6251MortInt.MortInt98) + GetCurrency(IAW6251MortInt.RefinInt) + GetCurrency(IAW6251MortInt.OthInt))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Desc_Calculation()
    ReturnVal = CStr(GetCurrency(IAW6251MortInt.AMTInt))
End Sub

Private Sub Exist_Calculation()
    ReturnVal = 1
End Sub

Private Sub MortInt_Calculation()
    If GetBool(USWResidency.F1040NR) = True Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.ItemCheck) = True Then
        ReturnVal = GetCurrency(IASchA.Mort)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub MortInt98_Calculation()
    If GetBool(IAF1040.ItemCheck) = True Then
        ReturnVal = GetCurrency(USD1098.StateAdj)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub MtgePrem_Calculation()
    If GetBool(USWResidency.F1040NR) = True Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.ItemCheck) = True Then
        ReturnVal = GetCurrency(IASchA.MtgePrem)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.CombNames)
End Sub

Private Sub Points_Calculation()
    If GetBool(USWResidency.F1040NR) = True Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.ItemCheck) = True Then
        ReturnVal = GetCurrency(IASchA.PtsNot)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Sfm_Calculation()
    If GetBool(USWResidency.F1040NR) = True Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.ItemCheck) = True Then
        ReturnVal = GetCurrency(IASchA.MortNot)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

Private Sub TotMortInt_Calculation()
    If GetBool(USWResidency.F1040NR) = True Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.ItemCheck) = True Then
        ReturnVal = GetCurrency(IAW6251MortInt.MortInt) + GetCurrency(IAW6251MortInt.Sfm) + GetCurrency(IAW6251MortInt.Points) + GetCurrency(IAW6251MortInt.MtgePrem)
    Else
        ReturnVal = 0
    End If
End Sub

