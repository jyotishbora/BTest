Private Sub Add_Calculation()
    ReturnVal = GetString(IAF1040.Add)
End Sub

Private Sub CityComb_Calculation()
    ReturnVal = GetString(IAF1040.CityComb)
End Sub

Private Sub CombNames_Calculation()
    ReturnVal = GetString(IARequired.CombNames)
End Sub

Private Sub Desc_Calculation()
    ReturnVal = "Payment Voucher - " + GetString(IA1040V.TotDue)
End Sub

Private Sub PeriodEnd_Calculation()
    ReturnVal = "123118"
End Sub

Private Sub Phone_Calculation()
    ReturnVal = GetString(IAF1040.Phone)
End Sub

Private Sub PrVou_Calculation()
    If GetCurrency(IA1040V.TotDue) > 0 And GetBool(IAEFWksht.Yes) = True Then
        ReturnVal = 1
    ElseIf GetCurrency(IA1040V.TotDue) > 0 And GetBool(IAEFWksht.EFW) = False Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

Private Sub TotDue_Calculation()
    ReturnVal = GetCurrency(IAF1040.TotDue)
End Sub

