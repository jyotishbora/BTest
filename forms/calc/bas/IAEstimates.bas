Private Sub AdjBal_Calculation()
    ReturnVal = GetCurrency(IAEstimates.Balance) + GetCurrency(IAEstimates.OthTax)
End Sub

Private Sub AskSp_Calculation()
    If GetBool(IAF1040.CombMFS) = True Or GetBool(IAF1040.MFJ) = True Then
        If GetCurrency(IAEstimates.Overpayment) > 0 And GetBool(IAEstimates.Taxpayer) = True Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AskStillPay_Calculation()
    If GetBool(IAEstimates.StillPay) = True Then
        ReturnVal = 1
    ElseIf GetBool(IAEstimates.Print) = False Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Balance_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAEstimates.IATax) - GetCurrency(IAEstimates.NonrefCr))
End Sub

Private Sub Common_Calculation()
    ReturnVal = GetString(USWBasicInfo.TPCommon)
End Sub

Private Sub DDAcct_Calculation()
    If GetBool(IAEstimates.DirectDebEst) = True And (GetCurrency(IAEstimates.Est1Amt) = 0 And GetCurrency(IAEstimates.Est2Amt) = 0 And GetCurrency(IAEstimates.Est3Amt) = 0 And GetCurrency(IAEstimates.Est4Amt) = 0) Then
        ReturnVal = ""
    ElseIf (GetBool(IAEstimates.DirectDebEst) = True And (GetCurrency(IAEstimates.Est1Amt) > 0 Or GetCurrency(IAEstimates.Est2Amt) > 0 Or GetCurrency(IAEstimates.Est3Amt) > 0 Or GetCurrency(IAEstimates.Est4Amt) > 0)) Then
        Dim count As Integer
        Dim MaxAcct As Integer
        Dim Acct As String
        
        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)
        Acct = ""

        Do While count <= MaxAcct
            If GetString(USWBankAcct.BankAcct, count) <> "" Then
                If GetBool(USWBankAcct.Default, count) = True Then
                    ReturnVal = GetString(USWBankAcct.BankAcct, count)
                    count = 99
                End If
            End If
            count = count + 1
        Loop
        ReturnVal = ""
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub Description_Calculation()
    If GetBool(IAEstimates.Taxpayer) = True Then
        ReturnVal = GetString(IAEstimates.Common)
    ElseIf GetBool(IAEstimates.Spouse) = True Then
        ReturnVal = GetString(IAEstimates.SpouseCommon)
    Else
        ReturnVal = GetString(IAEstimates.JtCommon)
    End If
End Sub

Private Sub Est1Amt_Calculation()
    If GetBool(IAEstimates.Est1) = True Then
        ReturnVal = GetCurrency(IAEstimates.V1PayAmt1)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Est1Date_Calculation()
    If GetBool(IAEstimates.Est1) = True Then
        ReturnVal = MakeDate(4, 30, YearNumber + 1)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub Est2Amt_Calculation()
    If GetBool(IAEstimates.Est2) = True Then
        ReturnVal = GetCurrency(IAEstimates.V2PayAmt1)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Est2Date_Calculation()
    If GetBool(IAEstimates.Est2) = True Then
        ReturnVal = MakeDate(7, 1, YearNumber + 1)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub Est3Amt_Calculation()
    If GetBool(IAEstimates.Est3) = True Then
        ReturnVal = GetCurrency(IAEstimates.V3PayAmt1)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Est3Date_Calculation()
    If GetBool(IAEstimates.Est3) = True Then
        ReturnVal = MakeDate(9, 30, YearNumber + 1)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub Est4Amt_Calculation()
    If GetBool(IAEstimates.Est4) = True Then
        ReturnVal = GetCurrency(IAEstimates.V4PayAmt1)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Est4Date_Calculation()
    If GetBool(IAEstimates.Est4) = True Then
        ReturnVal = MakeDate(1, 31, YearNumber + 2)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub EstAcctNum_Calculation()
    If GetBool(IAEstimates.DirectDebEst) = True And (GetCurrency(IAEstimates.Est1Amt) = 0 And GetCurrency(IAEstimates.Est2Amt) = 0 And GetCurrency(IAEstimates.Est3Amt) = 0 And GetCurrency(IAEstimates.Est4Amt) = 0) Then
        ReturnVal = ""
    ElseIf (GetBool(IAEstimates.DirectDebEst) = True And (GetCurrency(IAEstimates.Est1Amt) > 0 Or GetCurrency(IAEstimates.Est2Amt) > 0 Or GetCurrency(IAEstimates.Est3Amt) > 0 Or GetCurrency(IAEstimates.Est4Amt) > 0)) Then
        Dim count As Integer
        Dim MaxAcct As Integer
        
        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)

        Do While count <= MaxAcct
            If GetString(USWBankAcct.BankAcct, count) <> "" Then
                If IsStrEqual(GetString(IAEstimates.DDAcct), GetString(USWBankAcct.BankAcct, count)) Then
                    ReturnVal = GetString(USWBankAcct.AcctNum, count)
                    count = 99
                End If
            End If
            count = count + 1
        Loop
        ReturnVal = ""
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub EstAcctNum2_Calculation(Index As Integer)
    ReturnVal = GetString(IAEstimates.EstAcctNum)
End Sub

Private Sub EstChecking_Calculation()
    If GetBool(IAEstimates.DirectDebEst) = True And (GetCurrency(IAEstimates.Est1Amt) = 0 And GetCurrency(IAEstimates.Est2Amt) = 0 And GetCurrency(IAEstimates.Est3Amt) = 0 And GetCurrency(IAEstimates.Est4Amt) = 0) Then
        ReturnVal = 0
    ElseIf (GetBool(IAEstimates.DirectDebEst) = True And (GetCurrency(IAEstimates.Est1Amt) > 0 Or GetCurrency(IAEstimates.Est2Amt) > 0 Or GetCurrency(IAEstimates.Est3Amt) > 0 Or GetCurrency(IAEstimates.Est4Amt) > 0)) Then
        Dim count As Integer
        Dim MaxAcct As Integer
        
        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)

        Do While count <= MaxAcct
            If GetString(USWBankAcct.BankAcct, count) <> "" Then
                If IsStrEqual(GetString(IAEstimates.DDAcct), GetString(USWBankAcct.BankAcct, count)) Then
                    ReturnVal = GetBool(USWBankAcct.Checking, count)
                    count = 99
                End If
            End If
            count = count + 1
        Loop
        ReturnVal = 0
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub EstChecking2_Calculation(Index As Integer)
    ReturnVal = GetBool(IAEstimates.EstChecking)
End Sub

Private Sub EstDed_Calculation()
' updated for 2018

    If GetBool(IAEstimates.Joint) = True Then
        ReturnVal = 5120@
    Else
        ReturnVal = 2080@
    End If
End Sub

Private Sub EstEFW_Calculation()
    If GetBool(IAEstimates.EstIAT) = True Then
        ReturnVal = 0
    ElseIf GetBool(IAEstimates.DirectDebEst) = True Then
        If GetBool(IAEstimates.EstPay1) = True Or GetBool(IAEstimates.EstPay2) = True Or GetBool(IAEstimates.EstPay3) = True Or GetBool(IAEstimates.EstPay4) = True Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub EstIAT_Calculation()
    If GetBool(IAEstimates.DirectDebEst) = True And (GetCurrency(IAEstimates.Est1Amt) = 0 And GetCurrency(IAEstimates.Est2Amt) = 0 And GetCurrency(IAEstimates.Est3Amt) = 0 And GetCurrency(IAEstimates.Est4Amt) = 0) Then
        ReturnVal = 0
    ElseIf (GetBool(IAEstimates.DirectDebEst) = True And (GetCurrency(IAEstimates.Est1Amt) > 0 Or GetCurrency(IAEstimates.Est2Amt) > 0 Or GetCurrency(IAEstimates.Est3Amt) > 0 Or GetCurrency(IAEstimates.Est4Amt) > 0)) Then
        Dim count As Integer
        Dim MaxAcct As Integer
        
        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)

        Do While count <= MaxAcct
            If GetString(USWBankAcct.BankAcct, count) <> "" Then
                If IsStrEqual(GetString(IAEstimates.DDAcct), GetString(USWBankAcct.BankAcct, count)) Then
                    ReturnVal = GetBool(USWBankAcct.IAT, count)
                    count = 99
                End If
            End If
            count = count + 1
        Loop
        ReturnVal = 0
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub EstIATNo_Calculation()
    ReturnVal = GetBool(IAEstimates.EstEFW)
End Sub

Private Sub EstPay1_Calculation()
    If GetBool(IAEstimates.Est1) = True And GetCurrency(IAEstimates.Est1Amt) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub EstPay2_Calculation()
    If GetBool(IAEstimates.Est2) = True And GetCurrency(IAEstimates.Est2Amt) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub EstPay3_Calculation()
    If GetBool(IAEstimates.Est3) = True And GetCurrency(IAEstimates.Est3Amt) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub EstPay4_Calculation()
    If GetBool(IAEstimates.Est4) = True And GetCurrency(IAEstimates.Est4Amt) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub EstRTN_Calculation()
    If GetBool(IAEstimates.DirectDebEst) = True And (GetCurrency(IAEstimates.Est1Amt) = 0 And GetCurrency(IAEstimates.Est2Amt) = 0 And GetCurrency(IAEstimates.Est3Amt) = 0 And GetCurrency(IAEstimates.Est4Amt) = 0) Then
        ReturnVal = ""
    ElseIf (GetBool(IAEstimates.DirectDebEst) = True And (GetCurrency(IAEstimates.Est1Amt) > 0 Or GetCurrency(IAEstimates.Est2Amt) > 0 Or GetCurrency(IAEstimates.Est3Amt) > 0 Or GetCurrency(IAEstimates.Est4Amt) > 0)) Then
        Dim count As Integer
        Dim MaxAcct As Integer
        
        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)

        Do While count <= MaxAcct
            If GetString(USWBankAcct.BankAcct, count) <> "" Then
                If IsStrEqual(GetString(IAEstimates.DDAcct), GetString(USWBankAcct.BankAcct, count)) Then
                    ReturnVal = GetString(USWBankAcct.RTN, count)
                    count = 99
                End If
            End If
            count = count + 1
        Loop
        ReturnVal = ""
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub EstRTN2_Calculation(Index As Integer)
    ReturnVal = GetString(IAEstimates.EstRTN)
End Sub

Private Sub EstSavings_Calculation()
    If GetBool(IAEstimates.DirectDebEst) = True And (GetCurrency(IAEstimates.Est1Amt) = 0 And GetCurrency(IAEstimates.Est2Amt) = 0 And GetCurrency(IAEstimates.Est3Amt) = 0 And GetCurrency(IAEstimates.Est4Amt) = 0) Then
        ReturnVal = 0
    ElseIf (GetBool(IAEstimates.DirectDebEst) = True And (GetCurrency(IAEstimates.Est1Amt) > 0 Or GetCurrency(IAEstimates.Est2Amt) > 0 Or GetCurrency(IAEstimates.Est3Amt) > 0 Or GetCurrency(IAEstimates.Est4Amt) > 0)) Then
        Dim count As Integer
        Dim MaxAcct As Integer
        
        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)

        Do While count <= MaxAcct
            If GetString(USWBankAcct.BankAcct, count) <> "" Then
                If IsStrEqual(GetString(IAEstimates.DDAcct), GetString(USWBankAcct.BankAcct, count)) Then
                    ReturnVal = GetBool(USWBankAcct.Savings, count)
                    count = 99
                End If
            End If
            count = count + 1
        Loop
        ReturnVal = 0
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub EstSavings2_Calculation(Index As Integer)
    ReturnVal = GetBool(IAEstimates.EstSavings)
End Sub

Private Sub Exist_Calculation()
    ReturnVal = 1
End Sub

Private Sub GrossIncOption_Calculation()
    If GetBool(IAEstimates.Gross) = True Then
        ReturnVal = CDollar(GetFloat(IAEstimates.Gross5) * 0.05)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub IANetInc_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAEstimates.NetInc) - GetCurrency(IAEstimates.FedTaxPd))
End Sub

Private Sub IATax_Calculation()
    If GetFloat(IAEstimates.NRIAPer) < 1# Then
        ReturnVal = CDollar(GetFloat(IAEstimates.NetTax) * GetFloat(IAEstimates.NRIAPer))
    Else
        ReturnVal = GetCurrency(IAEstimates.NetTax)
    End If
End Sub

Private Sub JtCommon_Calculation()
    ReturnVal = GetString(USWBasicInfo.CombFirst)
End Sub

Private Sub MainName_Calculation()
    If GetBool(IAEstimates.Taxpayer) = True Then
        ReturnVal = GetString(IARequired.TPComb)
    ElseIf GetBool(IAEstimates.Spouse) = True Then
        ReturnVal = GetString(IARequired.SPComb)
    Else
        ReturnVal = GetString(IARequired.JTComb)
    End If
End Sub

Private Sub Names_Calculation()
    If GetBool(IAEstimates.Spouse) = True Then
        ReturnVal = GetString(IARequired.SPCombName)
    ElseIf GetBool(IAEstimates.Taxpayer) = True Then
        ReturnVal = GetString(IARequired.TPCombName)
    Else
        ReturnVal = GetString(IARequired.CombNames)
    End If
End Sub

Private Sub NetTax_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAEstimates.TotEstLiab) - GetCurrency(IAEstimates.TotCr))
End Sub

Private Sub NoBankSel3_Calculation()
    If GetBool(IAEstimates.DirectDebEst) = True Then
        If Trim(GetString(IAEstimates.DDAcct)) = "" Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub NoBankSelInt3_Calculation()
    If GetBool(IAEstimates.DirectDebEst) = True And (GetCurrency(IAEstimates.Est1Amt) > 0 Or GetCurrency(IAEstimates.Est2Amt) > 0 Or GetCurrency(IAEstimates.Est3Amt) > 0 Or GetCurrency(IAEstimates.Est4Amt) > 0) Then
        If GetBool(USTopicList.HaveBankWSSend) = False Then
            ReturnVal = 0
        ElseIf Trim(GetString(IAEstimates.DDAcct)) = "" Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub NRIAPer_Calculation()
    If GetCurrency(IAEstimates.NetInc) = 0 Then
        ReturnVal = 0#
    ElseIf GetCurrency(IAEstimates.NRIAInc) = 0 Then
        ReturnVal = 1#
    Else
        ReturnVal = MinValue(1#, Round((GetFloat(IAEstimates.NRIAInc) / GetFloat(IAEstimates.NetInc)) * 10000) / 10000)
    End If
End Sub

Private Sub Overpayment_Calculation()
    If GetCurrency(IAF1040.OVerPaid) > 0 Then
        If GetBool(IAEstimates.Spouse) = False Then
            ReturnVal = MaxValue(0, GetCurrency(IAF1040.OVerPaid) - GetCurrency(IAF1040.Penalty))
        ElseIf GetBool(IAEstimates.Spouse) = True And GetBool(IAEstimates.Taxpayer, 1) = False And GetBool(IAEstimates.Taxpayer, 2) = False Then
            ReturnVal = MaxValue(0, GetCurrency(IAF1040.OVerPaid) - GetCurrency(IAF1040.Penalty))
        Else
            ReturnVal = MinValue(MaxValue(0, (GetCurrency(IAF1040.OVerPaid)) - GetCurrency(IAF1040.Penalty)), GetCurrency(IAEstimates.SpOvpd, FieldCopies(IAEstimates.Taxpayer)))
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Owner_Calculation()
    If GetBool(IAEstimates.Taxpayer) = True And Trim(GetString(USWBasicInfo.FirstName)) = "" Then
        ReturnVal = "the taxpayer"
    ElseIf GetBool(IAEstimates.Taxpayer) = True Then
        ReturnVal = GetString(USWBasicInfo.FirstName)
    ElseIf GetBool(IAEstimates.Spouse) = True And Trim(GetString(USWBasicInfo.SpouseFirst)) = "" Then
        ReturnVal = "the spouse"
    ElseIf GetBool(IAEstimates.Spouse) = True Then
        ReturnVal = GetString(USWBasicInfo.SpouseFirst)
    Else
        ReturnVal = "the taxpayer and spouse"
    End If
End Sub

Private Sub Payments_Calculation()
    ReturnVal = GetCurrency(IAEstimates.V1PayAmt1) + GetCurrency(IAEstimates.V2PayAmt1) + GetCurrency(IAEstimates.V3PayAmt1) + GetCurrency(IAEstimates.V4PayAmt1)
End Sub

Private Sub Print_Calculation()
    If GetCurrency(IAEstimates.TaxDue) > 0 Then
        If GetCurrency(IAEstimates.V1PayAmt1) + GetCurrency(IAEstimates.V2PayAmt1) + GetCurrency(IAEstimates.V3PayAmt1) + GetCurrency(IAEstimates.V4PayAmt1) Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PYTaxOption_Calculation()
    Dim TotTax As Currency
    Dim SubTot As Currency

    If GetBool(IAEstimates.Spouse) = True Then
        TotTax = GetCurrency(IAF1040.BBal4)
    ElseIf GetBool(IAEstimates.Taxpayer) = True Then
        TotTax = GetCurrency(IAF1040.ABal4)
    Else
        TotTax = GetCurrency(IAF1040.ABal4) + GetCurrency(IAF1040.BBal4)
    End If
    
    If GetCurrency(IARequired.IAAGI) > 150000@ Then
        SubTot = CDollar((TotTax) * 1.1)
    Else
        SubTot = TotTax
    End If
    
    If GetBool(IAEstimates.PYTax) = True Then
        ReturnVal = MaxValue(0, SubTot - GetCurrency(IAEstimates.PYCredits))
    Else
        ReturnVal = 0
    End If
    
End Sub

Private Sub Quarter_Calculation()
    ReturnVal = CDollar(GetFloat(IAEstimates.TaxDue) * 0.25)
End Sub

Private Sub RndV1_Calculation()
    Dim L16 As Currency
    Dim R25 As Currency
    Dim R50 As Currency
    Dim R100 As Currency
    Dim Drop As Integer
    Dim Drop25 As Integer
    Dim Drop50 As Integer
    Dim Drop100 As Integer
    Dim Payment As Currency
    Dim Payment25 As Currency
    Dim Payment50 As Currency
    Dim Payment100 As Currency
    
    L16 = GetCurrency(IAEstimates.Roundup10)
    R25 = GetCurrency(IAEstimates.Roundup25)
    R50 = GetCurrency(IAEstimates.Roundup50)
    R100 = GetCurrency(IAEstimates.Roundup100)
        
    Drop = CLng(L16 / 40@)
    Drop25 = CLng(R25 / 100@)
    Drop50 = CLng(R50 / 200@)
    Drop100 = CLng(R100 / 400@)
    
    Payment = (CCur(Drop) * 40@) + 40@
    Payment25 = (CCur(Drop25) * 100@) + 100@
    Payment50 = (CCur(Drop50) * 200@) + 200@
    Payment100 = (CCur(Drop100) * 400@) + 400@
  
    If GetBool(IAEstimates.Round10) = True Then
        If (L16 Mod 40@) = 0 Then
            ReturnVal = Round(CDollar(CDbl(L16) * 0.25))
        Else
            ReturnVal = Round(CDollar(CDbl(Payment) * 0.25))
        End If
    ElseIf GetBool(IAEstimates.Round25) = True Then
        If (R25 Mod 100@) = 0 Then
            ReturnVal = Round(CDollar(CDbl(R25) * 0.25))
        Else
            ReturnVal = Round(CDollar(CDbl(Payment25) * 0.25))
        End If
    ElseIf GetBool(IAEstimates.Round50) = True Then
        If (R50 Mod 200@) = 0 Then
            ReturnVal = Round(CDollar(CDbl(R50) * 0.25))
        Else
            ReturnVal = Round(CDollar(CDbl(Payment50) * 0.25))
        End If
    ElseIf GetBool(IAEstimates.Round100) = True Then
        If (R100 Mod 400@) = 0 Then
            ReturnVal = Round(CDollar(CDbl(R100) * 0.25))
        Else
            ReturnVal = Round(CDollar(CDbl(Payment100) * 0.25))
        End If
    Else
        ReturnVal = Round(CDollar(GetFloat(IAEstimates.TaxDue) * 0.25))
    End If

End Sub

Private Sub RndV2_Calculation()
    Dim L16 As Currency
    Dim R25 As Currency
    Dim R50 As Currency
    Dim R100 As Currency
    Dim Drop As Integer
    Dim Drop25 As Integer
    Dim Drop50 As Integer
    Dim Drop100 As Integer
    Dim Payment As Currency
    Dim Payment25 As Currency
    Dim Payment50 As Currency
    Dim Payment100 As Currency
    
    L16 = GetCurrency(IAEstimates.Roundup10) - GetCurrency(IAEstimates.V1Pay)
    R25 = GetCurrency(IAEstimates.Roundup25) - GetCurrency(IAEstimates.V1Pay)
    R50 = GetCurrency(IAEstimates.Roundup50) - GetCurrency(IAEstimates.V1Pay)
    R100 = GetCurrency(IAEstimates.Roundup100) - GetCurrency(IAEstimates.V1Pay)
        
    Drop = CLng(L16 / 30@)
    Drop25 = CLng(R25 / 75@)
    Drop50 = CLng(R50 / 150@)
    Drop100 = CLng(R100 / 300@)
    
    Payment = (CCur(Drop) * 30@) + 30@
    Payment25 = (CCur(Drop25) * 75@) + 75@
    Payment50 = (CCur(Drop50) * 150@) + 150@
    Payment100 = (CCur(Drop100) * 300@) + 300@
  
    If GetBool(IAEstimates.Round10) = True Then
        If (L16 Mod 30@) = 0 Then
            ReturnVal = Round(CDollar(CDbl(L16) * 0.333333))
        Else
            ReturnVal = Round(CDollar(CDbl(Payment) * 0.333333))
        End If
    ElseIf GetBool(IAEstimates.Round25) = True Then
        If (R25 Mod 75@) = 0 Then
            ReturnVal = Round(CDollar(CDbl(R25) * 0.333333))
        Else
            ReturnVal = Round(CDollar(CDbl(Payment25) * 0.333333))
        End If
    ElseIf GetBool(IAEstimates.Round50) = True Then
        If (R50 Mod 150@) = 0 Then
            ReturnVal = Round(CDollar(CDbl(R50) * 0.333333))
        Else
            ReturnVal = Round(CDollar(CDbl(Payment50) * 0.333333))
        End If
    ElseIf GetBool(IAEstimates.Round100) = True Then
        If (R100 Mod 300@) = 0 Then
            ReturnVal = Round(CDollar(CDbl(R100) * 0.333333))
        Else
            ReturnVal = Round(CDollar(CDbl(Payment100) * 0.333333))
        End If
    Else
        ReturnVal = Round(CDollar(CDbl(GetCurrency(IAEstimates.TaxDue) - GetCurrency(IAEstimates.V1Pay)) * 0.333333))
    End If

End Sub

Private Sub RndV3_Calculation()
   Dim L16 As Currency
    Dim R25 As Currency
    Dim R50 As Currency
    Dim R100 As Currency
    Dim Drop As Integer
    Dim Drop25 As Integer
    Dim Drop50 As Integer
    Dim Drop100 As Integer
    Dim Payment As Currency
    Dim Payment25 As Currency
    Dim Payment50 As Currency
    Dim Payment100 As Currency
    
    L16 = GetCurrency(IAEstimates.Roundup10) - GetCurrency(IAEstimates.V1Pay) - GetCurrency(IAEstimates.V2Pay)
    R25 = GetCurrency(IAEstimates.Roundup25) - GetCurrency(IAEstimates.V1Pay) - GetCurrency(IAEstimates.V2Pay)
    R50 = GetCurrency(IAEstimates.Roundup50) - GetCurrency(IAEstimates.V1Pay) - GetCurrency(IAEstimates.V2Pay)
    R100 = GetCurrency(IAEstimates.Roundup100) - GetCurrency(IAEstimates.V1Pay) - GetCurrency(IAEstimates.V2Pay)
        
    Drop = CLng(L16 / 20@)
    Drop25 = CLng(R25 / 50@)
    Drop50 = CLng(R50 / 100@)
    Drop100 = CLng(R100 / 200@)
    
    Payment = (CCur(Drop) * 20@) + 20@
    Payment25 = (CCur(Drop25) * 50@) + 50@
    Payment50 = (CCur(Drop50) * 100@) + 100@
    Payment100 = (CCur(Drop100) * 200@) + 200@
  
    If GetBool(IAEstimates.Round10) = True Then
        If (L16 Mod 20@) = 0 Then
            ReturnVal = Round(CDollar(CDbl(L16) * 0.5))
        Else
            ReturnVal = Round(CDollar(CDbl(Payment) * 0.5))
        End If
    ElseIf GetBool(IAEstimates.Round25) = True Then
        If (R25 Mod 50@) = 0 Then
            ReturnVal = Round(CDollar(CDbl(R25) * 0.5))
        Else
            ReturnVal = Round(CDollar(CDbl(Payment25) * 0.5))
        End If
    ElseIf GetBool(IAEstimates.Round50) = True Then
        If (R50 Mod 100@) = 0 Then
            ReturnVal = Round(CDollar(CDbl(R50) * 0.5))
        Else
            ReturnVal = Round(CDollar(CDbl(Payment50) * 0.5))
        End If
    ElseIf GetBool(IAEstimates.Round100) = True Then
        If (R100 Mod 200@) = 0 Then
            ReturnVal = Round(CDollar(CDbl(R100) * 0.5))
        Else
            ReturnVal = Round(CDollar(CDbl(Payment100) * 0.5))
        End If
    Else
        ReturnVal = Round(CDollar(CDbl(GetCurrency(IAEstimates.TaxDue) - GetCurrency(IAEstimates.V1Pay) - GetCurrency(IAEstimates.V2Pay)) * 0.5))
    End If
End Sub

Private Sub RndV4_Calculation()
    Dim L16 As Currency
    Dim R25 As Currency
    Dim R50 As Currency
    Dim R100 As Currency
    Dim Drop As Integer
    Dim Drop25 As Integer
    Dim Drop50 As Integer
    Dim Drop100 As Integer
    Dim Payment As Currency
    Dim Payment25 As Currency
    Dim Payment50 As Currency
    Dim Payment100 As Currency
    
    L16 = GetCurrency(IAEstimates.Roundup10) - GetCurrency(IAEstimates.V1Pay) - GetCurrency(IAEstimates.V2Pay) - GetCurrency(IAEstimates.V3Pay)
    R25 = GetCurrency(IAEstimates.Roundup25) - GetCurrency(IAEstimates.V1Pay) - GetCurrency(IAEstimates.V2Pay) - GetCurrency(IAEstimates.V3Pay)
    R50 = GetCurrency(IAEstimates.Roundup50) - GetCurrency(IAEstimates.V1Pay) - GetCurrency(IAEstimates.V2Pay) - GetCurrency(IAEstimates.V3Pay)
    R100 = GetCurrency(IAEstimates.Roundup100) - GetCurrency(IAEstimates.V1Pay) - GetCurrency(IAEstimates.V2Pay) - GetCurrency(IAEstimates.V3Pay)
        
    Drop = CLng(L16 / 10@)
    Drop25 = CLng(R25 / 25@)
    Drop50 = CLng(R50 / 50@)
    Drop100 = CLng(R100 / 100@)
    
    Payment = (CCur(Drop) * 10@) + 10@
    Payment25 = (CCur(Drop25) * 10@) + 10@
    Payment50 = (CCur(Drop50) * 10@) + 10@
    Payment100 = (CCur(Drop100) * 100@) + 100@
  
    If GetBool(IAEstimates.Round10) = True Then
        If (L16 Mod 10@) = 0 Then
            ReturnVal = L16
        Else
            ReturnVal = Round(Payment)
        End If
    ElseIf GetBool(IAEstimates.Round25) = True Then
        If (R25 Mod 25@) = 0 Then
            ReturnVal = R25
        Else
            ReturnVal = Round(Payment25)
        End If
    ElseIf GetBool(IAEstimates.Round50) = True Then
        If (R50 Mod 50@) = 0 Then
            ReturnVal = R50
        Else
            ReturnVal = Round(Payment50)
        End If
    ElseIf GetBool(IAEstimates.Round100) = True Then
        If (R100 Mod 100@) = 0 Then
            ReturnVal = R100
       Else
            ReturnVal = Round(Payment100)
        End If
    Else
        ReturnVal = Round(GetCurrency(IAEstimates.TaxDue) - GetCurrency(IAEstimates.V1Pay) - GetCurrency(IAEstimates.V2Pay) - GetCurrency(IAEstimates.V3Pay))
    End If
End Sub

Private Sub Roundup10_Calculation()
    Dim Required As Currency
    Dim Drop As Integer
    Dim Payment As Currency
    
    Required = GetCurrency(IAEstimates.TaxDue)
        
    Drop = CLng(Required / 40@)
    
    Payment = (CCur(Drop) * 40@) + 40@
  
    If GetBool(IAEstimates.Round10) = True Then
        If (Required Mod 40@) = 0 Then
            ReturnVal = Required
        Else
            ReturnVal = Payment
        End If
    Else
        ReturnVal = GetCurrency(IAEstimates.TaxDue)
    End If
End Sub

Private Sub Roundup100_Calculation()
    Dim Required As Currency
    Dim Drop As Integer
    Dim Payment As Currency
    
    Required = GetCurrency(IAEstimates.TaxDue)
        
    Drop = CLng(GetFloat(IAEstimates.TaxDue) / 40000#)
    
    Payment = (CCur(Drop) * 400@) + 400@
  
    If GetBool(IAEstimates.Round100) = True Then
        If (Required Mod 400@) = 0 Then
            ReturnVal = Required
        Else
            ReturnVal = Payment
        End If
    Else
        ReturnVal = GetCurrency(IAEstimates.TaxDue)
    End If
End Sub

Private Sub Roundup25_Calculation()
    Dim Required As Currency
    Dim Drop As Integer
    Dim Payment As Currency
    
    Required = GetCurrency(IAEstimates.TaxDue)
        
    Drop = CLng(GetFloat(IAEstimates.TaxDue) / 10000#)
    
    Payment = (CCur(Drop) * 100@) + 100@
  
    If GetBool(IAEstimates.Round25) = True Then
        If (Required Mod 100@) = 0 Then
            ReturnVal = Required
        Else
            ReturnVal = Payment
        End If
    Else
        ReturnVal = GetCurrency(IAEstimates.TaxDue)
    End If
End Sub

Private Sub Roundup50_Calculation()
    Dim Required As Currency
    Dim Drop As Integer
    Dim Payment As Currency
    
    Required = GetCurrency(IAEstimates.TaxDue)
        
    Drop = CLng(CDbl(Required) / 20000#)
    
    Payment = (CCur(Drop) * 200@) + 200@
  
    If GetBool(IAEstimates.Round50) = True Then
        If (Required Mod 200@) = 0 Then
            ReturnVal = Required
        Else
            ReturnVal = Payment
        End If
    Else
        ReturnVal = GetCurrency(IAEstimates.TaxDue)
    End If
End Sub

Private Sub SpouseCommon_Calculation()
    ReturnVal = GetString(USWBasicInfo.SPCommon)
End Sub

Private Sub SSN_Calculation()
    If GetBool(IAEstimates.Spouse) = True Then
        ReturnVal = GetString(IAF1040.SpouseSSN)
    Else
        ReturnVal = GetString(IAF1040.SSN)
    End If
End Sub

Private Sub Tax_Calculation()
    ReturnVal = NextYearTax(GetCurrency(IAEstimates.TaxInc))
End Sub

Private Sub TaxDue_Calculation()
    If GetBool(IAEstimates.Gross) = True Then
        ReturnVal = GetCurrency(IAEstimates.GrossIncOption)
    ElseIf GetBool(IAEstimates.PYTax) = True Then
        ReturnVal = GetCurrency(IAEstimates.PYTaxOption)
    ElseIf GetCurrency(IAEstimates.TotEstTax) > 200@ Or GetBool(IAEstimates.StillPay) = True Then
        ReturnVal = GetCurrency(IAEstimates.TotEstTax)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TaxInc_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAEstimates.IANetInc) - GetCurrency(IAEstimates.EstDed))
End Sub

Private Sub Taxpayer_Calculation()
    ReturnVal = 1
End Sub

Private Sub TotApplied_Calculation()
    ReturnVal = (GetCurrency(IAEstimates.V1Apply) + GetCurrency(IAEstimates.V2Apply) + GetCurrency(IAEstimates.V3Apply) + GetCurrency(IAEstimates.V4Apply))
End Sub

Private Sub TotCr_Calculation()
    If GetBool(IAEstimates.Joint) = True Then
        ReturnVal = 80@
    Else
        ReturnVal = 40@
    End If
End Sub

Private Sub TotEstimate_Calculation()
    ReturnVal = GetCurrency(IAEstimates.V1Pay) + GetCurrency(IAEstimates.V2Pay) + GetCurrency(IAEstimates.V3Pay) + GetCurrency(IAEstimates.V4Pay)
End Sub

Private Sub TotEstLiab_Calculation()
    ReturnVal = GetCurrency(IAEstimates.Tax) + GetCurrency(IAEstimates.MinTax) + GetCurrency(IAEstimates.LSD)
End Sub

Private Sub TotEstTax_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAEstimates.AdjBal) - GetCurrency(IAEstimates.IACr))
End Sub

Private Sub TotNetTax2_Calculation()
    If GetBool(IAEstimates.Taxpayer) = False Then
        ReturnVal = GetCurrency(IAEstimates.Overpayment)
    Else
        ReturnVal = MaxValue(0, GetCurrency(IAEstimates.Overpayment) - GetCurrency(IAEstimates.SpOvpd))
    End If
End Sub

Private Sub V1Apply_Calculation()
    Dim Smaller As Currency
    
    Smaller = MinValue(GetCurrency(IAEstimates.TotNetTax2), GetCurrency(IAEstimates.SpecAmt))

    If GetBool(IAEstimates.Refund) = True Then
        ReturnVal = 0
    ElseIf GetBool(IAEstimates.ApplySpecific) = True And GetCurrency(IAEstimates.TaxDue) = 0 Then
        ReturnVal = Smaller
    ElseIf GetBool(IAEstimates.ApplySpecific) = True Then
        ReturnVal = MinValue(Smaller, GetCurrency(IAEstimates.V1Pay))
    Else
        ReturnVal = MinValue(GetCurrency(IAEstimates.TotNetTax2), GetCurrency(IAEstimates.V1Pay))
    End If
End Sub

Private Sub V1Pay_Calculation()
    ReturnVal = GetCurrency(IAEstimates.RndV1)
End Sub

Private Sub V1PayAmt1_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAEstimates.V1Pay) - GetCurrency(IAEstimates.V1Apply))
End Sub

Private Sub V2Apply_Calculation()
    Dim Smaller As Currency
    Dim Limited As Currency
    Dim Limited2 As Currency
    
    Smaller = MinValue(GetCurrency(IAEstimates.TotNetTax2), GetCurrency(IAEstimates.SpecAmt))
    Limited = MinValue(GetCurrency(IAEstimates.V2Pay), GetCurrency(IAEstimates.TotNetTax2) - GetCurrency(IAEstimates.V1Pay))
    Limited2 = MinValue(GetCurrency(IAEstimates.V2Pay), Smaller - GetCurrency(IAEstimates.V1Pay))

    If GetBool(IAEstimates.Refund) = True Or GetBool(IAEstimates.FirstQt) = True Then
        ReturnVal = 0
    ElseIf GetBool(IAEstimates.ApplySpecific) = True Then
        ReturnVal = MaxValue(0, Limited2)
    Else
        ReturnVal = MaxValue(0, Limited)
    End If
End Sub

Private Sub V2Pay_Calculation()
    ReturnVal = GetCurrency(IAEstimates.RndV2)
End Sub

Private Sub V2PayAmt1_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAEstimates.V2Pay) - GetCurrency(IAEstimates.V2Apply))
End Sub

Private Sub V3Apply_Calculation()
    Dim Smaller As Currency
    Dim Limited As Currency
    Dim Limited2 As Currency
        
    Smaller = MinValue(GetCurrency(IAEstimates.TotNetTax2), GetCurrency(IAEstimates.SpecAmt))
    Limited = MinValue(GetCurrency(IAEstimates.V3Pay), GetCurrency(IAEstimates.TotNetTax2) - GetCurrency(IAEstimates.V1Pay) - GetCurrency(IAEstimates.V2Pay))
    Limited2 = MinValue(GetCurrency(IAEstimates.V3Pay), Smaller - GetCurrency(IAEstimates.V1Pay) - GetCurrency(IAEstimates.V2Pay))
    
    If GetBool(IAEstimates.Refund) = True Or GetBool(IAEstimates.FirstQt) = True Then
        ReturnVal = 0
    ElseIf GetBool(IAEstimates.ApplySpecific) = True Then
        ReturnVal = MaxValue(0, Limited2)
    Else
        ReturnVal = MaxValue(0, Limited)
    End If
End Sub

Private Sub V3Pay_Calculation()
    ReturnVal = GetCurrency(IAEstimates.RndV3)
End Sub

Private Sub V3PayAmt1_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAEstimates.V3Pay) - GetCurrency(IAEstimates.V3Apply))
End Sub

Private Sub V4Apply_Calculation()
    Dim Smaller As Currency
    Dim Limited As Currency
    
    If GetBool(IAEstimates.Refund) = True Or GetBool(IAEstimates.FirstQt) = True Then
        ReturnVal = 0
    ElseIf GetBool(IAEstimates.ApplyAll) = True Then
        Limited = MaxValue(0, GetCurrency(IAEstimates.TotNetTax2) - GetCurrency(IAEstimates.V1Pay) - GetCurrency(IAEstimates.V2Pay) - GetCurrency(IAEstimates.V3Pay))
        ReturnVal = MinValue(GetCurrency(IAEstimates.V4Pay), Limited)
    ElseIf GetBool(IAEstimates.ApplySpecific) = True Then
        Smaller = MinValue(GetCurrency(IAEstimates.TotNetTax2), GetCurrency(IAEstimates.SpecAmt))
        ReturnVal = MaxValue(0, Smaller - GetCurrency(IAEstimates.V1Apply) - GetCurrency(IAEstimates.V2Apply) - GetCurrency(IAEstimates.V3Apply))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub V4Pay_Calculation()
    ReturnVal = GetCurrency(IAEstimates.RndV4)
End Sub

Private Sub V4PayAmt1_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAEstimates.V4Pay) - GetCurrency(IAEstimates.V4Apply))
End Sub

