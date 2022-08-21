Private Sub Attach1_Calculation()
    ReturnVal = "Please include a complete copy of your federal return. "
End Sub

Private Sub Attach2_Calculation()
    If GetBool(IAFilingInst.AttWHStmt) = True Then
        ReturnVal = "Please attach state copies of W-2(s), W-2G(s) and/or 1099(s) showing Iowa tax withheld."
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub Attach3_Calculation()
    If GetNumber(IAFilingInst.OtherState) > 0 Then
        ReturnVal = "Please attach a copy of the other state return for Schedule IA 130."
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub Attach4_Calculation()
    If GetBool(IA148.Print) = True Or GetBool(IA148Sp.Print) = True Then
        ReturnVal = "Please attach all supporting forms for the credits claimed on Schedule IA 148."
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub AttWHStmt_Calculation()
    If GetCurrency(IAF1040.AIATaxWith) > 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IAF1040.BIATaxWith) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub C1Est1_Calculation()
    ReturnVal = GetBool(IAEstimates.EstPay1, 1)
End Sub

Private Sub C1Est2_Calculation()
    ReturnVal = GetBool(IAEstimates.EstPay2, 1)
End Sub

Private Sub C1Est3_Calculation()
    ReturnVal = GetBool(IAEstimates.EstPay3, 1)
End Sub

Private Sub C1Est4_Calculation()
    ReturnVal = GetBool(IAEstimates.EstPay4, 1)
End Sub

Private Sub C1EstInfo_Calculation()
    If GetBool(IAEstimates.Print, 1) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub C1EstInfoDirDeb_Calculation()
    If GetBool(IAEstimates.Print, 1) = True And GetBool(IAEstimates.EstEFW, 1) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub C1Owner_Calculation()
    If GetBool(IAEstimates.Print, 1) = True And GetBool(IAEstimates.Print, 2) = True Then
        ReturnVal = " for " & GetString(IAEstimates.Owner, 1)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub C1Q1_Calculation()
    ReturnVal = GetCurrency(IAEstimates.V1PayAmt1, 1)
End Sub

Private Sub C1Q1WithDate_Calculation()
    ReturnVal = GetVerboseDate(GetDate(IAEstimates.Est1Date, 1))
End Sub

Private Sub C1Q2_Calculation()
    ReturnVal = GetCurrency(IAEstimates.V2PayAmt1, 1)
End Sub

Private Sub C1Q2WithDate_Calculation()
    ReturnVal = GetVerboseDate(GetDate(IAEstimates.Est2Date, 1))
End Sub

Private Sub C1Q3_Calculation()
    ReturnVal = GetCurrency(IAEstimates.V3PayAmt1, 1)
End Sub

Private Sub C1Q3WithDate_Calculation()
    ReturnVal = GetVerboseDate(GetDate(IAEstimates.Est3Date, 1))
End Sub

Private Sub C1Q4_Calculation()
    ReturnVal = GetCurrency(IAEstimates.V4PayAmt1, 1)
End Sub

Private Sub C1Q4WithDate_Calculation()
    ReturnVal = GetVerboseDate(GetDate(IAEstimates.Est4Date, 1))
End Sub

Private Sub C2Est1_Calculation()
    ReturnVal = GetBool(IAEstimates.EstPay1, 2)
End Sub

Private Sub C2Est2_Calculation()
    ReturnVal = GetBool(IAEstimates.EstPay2, 2)
End Sub

Private Sub C2Est3_Calculation()
    ReturnVal = GetBool(IAEstimates.EstPay3, 2)
End Sub

Private Sub C2Est4_Calculation()
    ReturnVal = GetBool(IAEstimates.EstPay4, 2)
End Sub

Private Sub C2EstInfo_Calculation()
    If GetBool(IAEstimates.Print, 2) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub C2EstInfoDirDeb_Calculation()
    If GetBool(IAEstimates.Print, 2) = True And GetBool(IAEstimates.EstEFW, 2) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub C2Owner_Calculation()
    If GetBool(IAEstimates.Print, 1) = True And GetBool(IAEstimates.Print, 2) = True Then
        ReturnVal = " for " & GetString(IAEstimates.Owner, 2)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub C2Q1_Calculation()
    ReturnVal = GetCurrency(IAEstimates.V1PayAmt1, 2)
End Sub

Private Sub C2Q1WithDate_Calculation()
    ReturnVal = GetVerboseDate(GetDate(IAEstimates.Est1Date, 2))
End Sub

Private Sub C2Q2_Calculation()
    ReturnVal = GetCurrency(IAEstimates.V2PayAmt1, 2)
End Sub

Private Sub C2Q2WithDate_Calculation()
    ReturnVal = GetVerboseDate(GetDate(IAEstimates.Est2Date, 2))
End Sub

Private Sub C2Q3_Calculation()
    ReturnVal = GetCurrency(IAEstimates.V3PayAmt1, 2)
End Sub

Private Sub C2Q3WithDate_Calculation()
    ReturnVal = GetVerboseDate(GetDate(IAEstimates.Est3Date, 2))
End Sub

Private Sub C2Q4_Calculation()
    ReturnVal = GetCurrency(IAEstimates.V4PayAmt1, 2)
End Sub

Private Sub C2Q4WithDate_Calculation()
    ReturnVal = GetVerboseDate(GetDate(IAEstimates.Est4Date, 2))
End Sub

Private Sub DueDate_Calculation()
    ReturnVal = "April 30, 2019"
End Sub

Private Sub EitherDirDeb_Calculation()
    If GetNumber(IAFilingInst.C1EstInfoDirDeb) = 1 Or GetNumber(IAFilingInst.C2EstInfoDirDeb) = 1 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub EstAdd1_Calculation()
    ReturnVal = "Iowa Department of Revenue<br>PO Box 10466 <br>Des Moines, IA 50306-0466"
End Sub

Private Sub EstInfo_Calculation()
    If GetBool(IAFilingInst.C1EstInfo) = True Then
        ReturnVal = 1
    ElseIf GetBool(IAFilingInst.C2EstInfo) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub IRSAdd1_Calculation()
    ReturnVal = "Iowa Income Tax Document Processing"
End Sub

Private Sub IRSAdd2_Calculation()
    ReturnVal = "PO Box 9187"
End Sub

Private Sub IRSAdd3_Calculation()
    ReturnVal = "Des Moines, IA  50306-9187"
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.CombNames)
End Sub

Private Sub OtherState_Calculation()
    If GetCurrency(IAF1040.AOutState) > 0 Or GetCurrency(IAF1040.BOutState) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Pay1_Calculation()
    If GetCurrency(IAF1040.RefBalDue) < 0 Then
        ReturnVal = "The balance due on your Iowa return is " & GetString(IAF1040.TotDue)
    Else
        ReturnVal = "The overpayment on your return is " & GetString(IAF1040.OVerPaid)
    End If
End Sub

Private Sub Pay2_Calculation()
    If GetCurrency(IAF1040.RefBalDue) < 0 Then
        ReturnVal = "Make your check payable to: Treasurer, State of Iowa"
    Else
        ReturnVal = "The amount of overpayment applied to your 2019 estimates is " & GetString(IARequired.TotApplied)
    End If
End Sub

Private Sub Pay3_Calculation()
    If GetCurrency(IAF1040.RefBalDue) < 0 Then
        ReturnVal = "Write '2018 Form 1040' on your check."
    Else
        ReturnVal = "The amount to be refunded to you is " & GetString(IAF1040.Refund) & "."
    End If
End Sub

Private Sub Pay4_Calculation()
    If GetCurrency(IAF1040.RefBalDue) <= 0 Then
        ReturnVal = ""
    ElseIf Trim(GetString(IAF1040.ActNum)) <> "" Then
        ReturnVal = "You have elected to receive your refund via direct deposit."
    Else
        ReturnVal = "You have elected to receive your refund on a paper check."
    End If
End Sub

Private Sub Q1Date_Calculation()
    ReturnVal = "April 30, 2019"
End Sub

Private Sub Q2Date_Calculation()
    ReturnVal = "July 1, 2019"
End Sub

Private Sub Q3Date_Calculation()
    ReturnVal = "September 30, 2019"
End Sub

Private Sub Q4Date_Calculation()
    ReturnVal = "January 31, 2020"
End Sub

