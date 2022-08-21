Private Sub Add_Calculation()
    ReturnVal = GetString(IA1040X.Add)
End Sub

Private Sub CityComb_Calculation()
    ReturnVal = GetString(IA1040X.City)
End Sub

Private Sub CombNames_Calculation()
    ReturnVal = GetString(IARequired.CombNames)
End Sub

Private Sub Desc_Calculation()
    ReturnVal = "Payment Voucher - " + GetString(IA1040XV.TotDue)
End Sub

Private Sub PeriodEnd_Calculation()
    ReturnVal = "123118"
End Sub

Private Sub Phone_Calculation()
    ReturnVal = GetString(IA1040X.Phone)
End Sub

Private Sub PrVou_Calculation()
    If GetCurrency(IA1040XV.TotDue) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IA1040X.SSN)
End Sub

Private Sub TotDue_Calculation()
    ReturnVal = GetCurrency(IA1040X.TotDue)
End Sub

