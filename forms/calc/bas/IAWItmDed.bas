Private Sub AGI_Calculation()
    ReturnVal = GetCurrency(IASchA.IAAGI)
End Sub

Private Sub AllowableDed2_Calculation()
    ReturnVal = GetCurrency(IAWItmDed.AllowableDed)
End Sub

Private Sub AllowableDed_Calculation()
    ReturnVal = MaxValue(0, (GetCurrency(IAWItmDed.IATotDed) - GetCurrency(IAWItmDed.Limit)))
End Sub

Private Sub Description_Calculation()
    ReturnVal = CStr(GetCurrency(IAWItmDed.LimitDed)) & " Itemized Deductions"
End Sub

Private Sub Divide_Calculation()
    If GetCurrency(IAWItmDed.Subtract2) = 0 Then
        ReturnVal = 0
    Else
        ReturnVal = Round(GetFloat(IAWItmDed.Subtract1) / GetFloat(IAWItmDed.Subtract2), 3)
    End If
End Sub

Private Sub ExcInc_Calculation()
    ReturnVal = MaxValue(0, (GetCurrency(IAWItmDed.AGI) - GetCurrency(IAWItmDed.IncLimit)))
End Sub

Private Sub IADedTax2_Calculation()
    ReturnVal = GetCurrency(IAWItmDed.IADedTax)
End Sub

Private Sub IADedTax_Calculation()
    If GetBool(USWRec.ItmDdn) = True Then
        If GetBool(USSchA.Income) = True Or GetBool(USWResidency.F1040NR) = True Then
            ReturnVal = MaxValue(0, GetCurrency(IASchA.IATax))
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub IATotDed2_Calculation()
    ReturnVal = GetCurrency(IAWItmDed.IATotDed)
End Sub

Private Sub IATotDed_Calculation()
    ReturnVal = GetCurrency(IAWItmDed.TotDed) + GetCurrency(IAWItmDed.IADedTax)
End Sub

Private Sub IncLimit_Calculation()
' updated for 2018 - RJ

    If FedFS() = 1 Then
        ReturnVal = 266700@
    ElseIf FedFS() = 3 Then
        ReturnVal = 160000@
    ElseIf FedFS() = 4 Then
        ReturnVal = 293350@
    Else
        ReturnVal = 320000@
    End If
End Sub

Private Sub Limit3_Calculation()
    ReturnVal = CDollar(GetFloat(IAWItmDed.ExcInc) * 0.03)
End Sub

Private Sub Limit80_Calculation()
    ReturnVal = CDollar(GetFloat(IAWItmDed.PODed) * 0.8)
End Sub

Private Sub Limit_Calculation()
    ReturnVal = MinValue(GetCurrency(IAWItmDed.Limit80), GetCurrency(IAWItmDed.Limit3))
End Sub

Private Sub LimitDed_Calculation()
    ReturnVal = MaxValue(0, (GetCurrency(IAWItmDed.AllowableDed2) - GetCurrency(IAWItmDed.Multiply)))
End Sub

Private Sub Multiply_Calculation()
    ReturnVal = CDollar(GetFloat(IAWItmDed.IADedTax2) * GetFloat(IAWItmDed.Divide))
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.CombNames)
End Sub

Private Sub No1_Calculation()
    If GetCurrency(IAWItmDed.NonPODed) < GetCurrency(IAWItmDed.IATotDed) Then
        ReturnVal = 0
    Else
        ReturnVal = 1
    End If
End Sub

Private Sub No2_Calculation()
    If GetCurrency(IAWItmDed.IncLimit) < GetCurrency(IAWItmDed.AGI) Then
        ReturnVal = 0
    Else
        ReturnVal = 1
    End If
End Sub

Private Sub NonPODed2_Calculation()
    ReturnVal = GetCurrency(IAWItmDed.NonPODed)
End Sub

Private Sub NonPODed_Calculation()
    Dim GamblingLoss As Currency
    
    If GetBool(USWResidency.F1040NR) = True Then
        GamblingLoss = 0
    Else
        GamblingLoss = GetCurrency(IAWSchAPrint.GamblingLoss)
    End If
        
    ReturnVal = GetCurrency(IASchA.MedDed) + GetCurrency(IASchA.Invest) + GetCurrency(IASchA.Theft) + GetCurrency(IAWSchAPrint.Form4684) + GamblingLoss
End Sub

Private Sub PODed_Calculation()
    ReturnVal = MaxValue(0, (GetCurrency(IAWItmDed.IATotDed) - GetCurrency(IAWItmDed.NonPODed)))
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

Private Sub Subtract1_Calculation()
    ReturnVal = MaxValue(0, (GetCurrency(IAWItmDed.AllowableDed2) - GetCurrency(IAWItmDed.NonPODed2)))
End Sub

Private Sub Subtract2_Calculation()
    ReturnVal = MaxValue(0, (GetCurrency(IAWItmDed.IATotDed2) - GetCurrency(IAWItmDed.NonPODed2)))
End Sub

Private Sub TotDed_Calculation()
    ReturnVal = GetCurrency(IASchA.MedDed) + GetCurrency(IASchA.TaxPd) + GetCurrency(IASchA.TotInt) + GetCurrency(IASchA.TotGifts) + GetCurrency(IASchA.Theft) + GetCurrency(IASchA.AllowExp) + GetCurrency(IASchA.OthMisc)
End Sub

Private Sub Yes1_Calculation()
    If GetBool(IAWItmDed.No1) = True Then
        ReturnVal = 0
    Else
        ReturnVal = 1
    End If
End Sub

Private Sub Yes2_Calculation()
    If GetBool(IAWItmDed.No2) = True Then
        ReturnVal = 0
    Else
        ReturnVal = 1
    End If
End Sub

