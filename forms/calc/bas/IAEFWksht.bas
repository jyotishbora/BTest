Private Sub Acct_Calculation()
    If GetBool(IAEFWksht.IsStateRPT) = True And GetBool(USWRALApp.StateRTDD) = True And GetBool(IAEFWksht.DirDeposit) = True Then
        ReturnVal = GetString(USWRALApp.StateAccount)
    ElseIf (GetBool(IAEFWksht.DirDeposit) = True And GetCurrency(IAEFWksht.Refund) > 0) Or (GetBool(IAEFWksht.EFW) = True And GetCurrency(IAEFWksht.AmtOwed) > 0) Then
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

Private Sub ACH_Calculation()
    If GetNumber(IAEFWksht.Yes) = 1 Then
        ReturnVal = 0
    ElseIf GetBool(IAEFWksht.EFW) = True And GetCurrency(IAEFWksht.AmtOwed) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Address_Calculation()
    ReturnVal = GetString(IAF1040.Add) + " " + GetString(IAF1040.CityComb)
End Sub

Private Sub AIAWH_Calculation()
    ReturnVal = GetCurrency(IAF1040.AIATaxWith)
End Sub

Private Sub AmtOwed_Calculation()
    ReturnVal = GetCurrency(IAF1040.TotDue)
End Sub

Private Sub ANet_Calculation()
    ReturnVal = GetCurrency(IAF1040.ANet)
End Sub

Private Sub AskBankInfo_Calculation()
    If GetCurrency(IAEFWksht.AmtOwed) > 0 Then
        ReturnVal = 1
    ElseIf GetBool(IAEFWksht.IsStateRPT) = True And GetBool(USWEFQual.FilingSO) = True Then
        ReturnVal = 0
    ElseIf GetCurrency(IAEFWksht.Refund) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AskDebitCard_Calculation()
    If IsPreparer() = True Then
        ReturnVal = 0
    ElseIf GetBool(USWBankProd.HaveBankConsent) = False Then
        ReturnVal = 0
' Do not offer state debit card on linked returns using Republic Direct Deposit RT
    ElseIf GetBool(USWBankProd.DebitCardReturn) = False And GetBool(USWBankProd.RPTReturn) = True Then
        ReturnVal = 0
' Do not offer state debit card on state only returns using Republic Direct Deposit RT
    ElseIf GetBool(USWBankProd.IsStateRPT) = True And GetBool(USWRALApp.StateRTDD) = True Then
        ReturnVal = 0
    ElseIf GetCurrency(IAEFWksht.Refund) < 10000@ Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AskDriverLic_Calculation()
    If GetBool(USWEFOptions.PiggyBackIA) = True Or GetBool(USWEFOptions.SOIA) = True Or GetBool(USWEFOptions.SOIAX) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AskFedStateBank_Calculation()
    If GetBool(IAEFWksht.PrepBPTrans) = True Then
        ReturnVal = 1
    ElseIf IsPreparer() = True And GetBool(USWBasicInfo.BankProd) = True Then
        ReturnVal = 0
    ElseIf GetBool(USWBankProd.IsStateRPT) = True And GetBool(USWEFQual.FilingSO) = True Then
        ReturnVal = 0
    ElseIf GetCurrency(IAEFWksht.Refund) > 0 And GetBool(USWEFWksht.refundbox) = True Then
        If GetBool(USWBasicInfo.DebitCard) = True And GetBool(IAEFWksht.AskDebitCard) = False Then
            ReturnVal = 0
        ElseIf GetBool(IAEFWksht.DebitCard) = True And GetBool(IAEFWksht.AskDebitCard) = False Then
            ReturnVal = 0
        ElseIf GetBool(USWBasicInfo.DebitCard) = True And GetBool(IAEFWksht.DebitCard) = True Then
            ReturnVal = 1
        ElseIf GetBool(USWBasicInfo.DirectDepY) = True And GetBool(IAEFWksht.DirDeposit) = True Then
            If GetString(USF8888.Account1) = GetString(IAEFWksht.Acct) Then
                ReturnVal = 1
            Else
                ReturnVal = 0
            End If
        ElseIf GetBool(USWBasicInfo.DirectDepN) = True And GetBool(IAEFWksht.NoDDEFW) = True Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
        
End Sub

Private Sub AskSORTDC_Calculation()
    If GetBool(USWEFOptions.SOIA) = False Then
        ReturnVal = 0
    ElseIf IsPreparer() = True Then
        ReturnVal = 0
    ElseIf GetBool(USWBankProd.HaveBankConsent) = False Then
        ReturnVal = 0
    ElseIf GetCurrency(IAEFWksht.Refund) < 10000@ Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AskStateRT_Calculation()
    If GetBool(USWEFOptions.SOIAX) = True Then
        ReturnVal = 0
    ElseIf GetCurrency(IAEFWksht.Refund) >= 75@ Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub ATTax_Calculation()
    If GetBool(IARequired.LowInc) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(IAF1040.ATotIATax)
    End If
End Sub

Private Sub BankName_Calculation()
    If (GetBool(IAEFWksht.DirDeposit) = True And GetCurrency(IAEFWksht.Refund) > 0) Or (GetBool(IAEFWksht.EFW) = True And GetCurrency(IAEFWksht.AmtOwed) > 0) Then
        Dim count As Integer
        Dim MaxAcct As Integer
        
        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)

        Do While count <= MaxAcct
            If GetString(USWBankAcct.BankAcct, count) <> "" Then
                If IsStrEqual(GetString(IAEFWksht.Acct), GetString(USWBankAcct.BankAcct, count)) Then
                    ReturnVal = GetString(USWBankAcct.BankName, count)
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

Private Sub BankProDisCd_Calculation()
    'Bank Product Disbursement Declaration
    '0 = Did Not Select bank product Option; 1 = Selected Debit Card Option; 2 = Selected Direct Depoist to the Bank; 3 = Requestd a Check;
    
    'Parameter 6 = Refund Owe Method: 0-No method; 1-AmEx debit card; 2-State issued debit card; 3-Direct deposit no Republic Bank; 4-Direct deposit through Republic Bank; 5-Paper check (refund); 6-AmEx debit card through Republic; 10-Direct debit; 11-Credit card; 12-Paper check (owe); 13-IRS EFTPS

    Dim Submission As String
    Dim TempStr As String
    
    TempStr = GetString(IAEFWksht.EFSubmission)
    Submission = GetParam(TempStr, 1, "|")

    
    If GetParam(Submission, 6, ";") = "0" Then
        ReturnVal = "0"
    ElseIf GetParam(Submission, 6, ";") = "1" Then
        ReturnVal = "1"
    ElseIf GetParam(Submission, 6, ";") = "2" Then
        ReturnVal = "3"
    ElseIf GetParam(Submission, 6, ";") = "3" Then
        ReturnVal = "2"
    ElseIf GetParam(Submission, 6, ";") = "4" Then
        ReturnVal = "2"
    ElseIf GetParam(Submission, 6, ";") = "5" Then
        ReturnVal = "3"
    ElseIf GetParam(Submission, 6, ";") = "6" Then
        ReturnVal = "1"
    Else
        ReturnVal = "0"
    End If

End Sub

Private Sub BIAWH_Calculation()
    ReturnVal = GetCurrency(IAF1040.BIATaxWith)
End Sub

Private Sub BNet_Calculation()
    ReturnVal = GetCurrency(IAF1040.BNet)
End Sub

Private Sub BP_Calculation()
    If GetBool(IAEFWksht.PrepBPTrans) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BTTax_Calculation()
    If GetBool(IARequired.LowInc) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(IAF1040.BTotIATax)
    End If
End Sub

Private Sub CompStateEFQA_Calculation()
' If not filing Iowa return, always return False
    If GetBool(USWEFOptions.PiggyBackIA) = False And GetBool(USWEFOptions.SOIA) = False And GetBool(USWEFOptions.SOIAX) = False Then
        ReturnVal = 0
    ElseIf GetCurrency(IAEFWksht.Refund) > 0 Then
        If GetBool(IAEFWksht.PrepRevQA) = False Then
            ReturnVal = 1
        ElseIf IsPreparer() = True And GetBool(IAEFWksht.PrepBPTrans) = True Then
            ReturnVal = 0
        ElseIf GetBool(USWBankProd.DebitCardReturn) = True And GetBool(IAEFWksht.DebitCard) = False And GetBool(IAEFWksht.DirDeposit) = False And GetBool(IAEFWksht.NoDDEFW) = False Then
            ReturnVal = 1
        ElseIf GetBool(IAEFWksht.DirDeposit) = False And GetBool(IAEFWksht.NoDDEFW) = False Then
            ReturnVal = 1
        ElseIf GetBool(USWBankProd.DebitCardReturn) = False And GetBool(IAEFWksht.DirDeposit) = False And GetBool(IAEFWksht.NoDDEFW) = False Then
            ReturnVal = 1
        ElseIf GetBool(IAEFWksht.DirDeposit) = True And GetNumber(USFInterview.ValidBankAccts) = 0 Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    ElseIf GetCurrency(IAEFWksht.AmtOwed) > 0 Then
        If GetBool(IAEFWksht.PrepRevQA) = False Then
            ReturnVal = 1
        ElseIf GetBool(IAEFWksht.EFW) = False And GetBool(IAEFWksht.NoDDEFW) = False Then
            ReturnVal = 1
        ElseIf GetBool(IAEFWksht.EFW) = True And GetNumber(USFInterview.ValidBankAccts) = 0 Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub DANChange_Calculation()
    ReturnVal = GetString(IAEFWksht.DirDepDan) + "|"
End Sub

Private Sub DC_Calculation()
    If GetBool(IAEFWksht.PrepBPTrans) = True Then
        ReturnVal = 0    
    ElseIf GetBool(IAEFWksht.DebitCard) = True And GetCurrency(IAEFWksht.Refund) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub DD_Calculation()
    If GetNumber(IAEFWksht.Yes) = 1 Then
        ReturnVal = 0
    ElseIf GetBool(IAEFWksht.PrepBPTrans) = True Then
        ReturnVal = 0
    ElseIf GetBool(IAEFWksht.DirDeposit) = True And GetCurrency(IAEFWksht.Refund) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub DebitCard_Calculation()
    If GetBool(IAEFWksht.IsStateRPT) = True Then
        If GetBool(USWRALApp.StateRTDC) = True And GetBool(IAEFWksht.AskDebitCard) = True Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    ElseIf GetBool(USWBasicInfo.DebitCard) = True And GetCurrency(USF1040.RefundOwe) > 0 And GetBool(IAEFWksht.AskDebitCard) = True Then
        If GetCurrency(IAEFWksht.Refund) > 0 Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Desc_Calculation()
    ReturnVal = GetString(IARequired.CombNames)
End Sub

Private Sub DirDepChecking_Calculation()
    
    If (GetBool(IAEFWksht.DirDeposit) = True And GetCurrency(IAEFWksht.Refund) > 0) Or (GetBool(IAEFWksht.EFW) = True And GetCurrency(IAEFWksht.AmtOwed) > 0) Then
        Dim count As Integer
        Dim MaxAcct As Integer
        
        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)

        Do While count <= MaxAcct
            If GetString(USWBankAcct.BankAcct, count) <> "" Then
                If IsStrEqual(GetString(IAEFWksht.Acct), GetString(USWBankAcct.BankAcct, count)) Then
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

Private Sub DirDepDan_Calculation()
    If (GetBool(IAEFWksht.DirDeposit) = True And GetCurrency(IAEFWksht.Refund) > 0) Or (GetBool(IAEFWksht.EFW) = True And GetCurrency(IAEFWksht.AmtOwed) > 0) Then
        Dim count As Integer
        Dim MaxAcct As Integer
        
        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)

        Do While count <= MaxAcct
            If GetString(USWBankAcct.BankAcct, count) <> "" Then
                If IsStrEqual(GetString(IAEFWksht.Acct), GetString(USWBankAcct.BankAcct, count)) Then
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

Private Sub DirDeposit_Calculation()
    If GetBool(IAEFWksht.IsStateRPT) = True Then
        If GetBool(USWRALApp.StateRTDD) = True Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    ElseIf GetBool(USWBasicInfo.DirectDepY) = True And GetCurrency(USF1040.RefundOwe) > 0 Then
        If GetCurrency(IAEFWksht.Refund) > 0 Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub DirDepRTN_Calculation()
    If (GetBool(IAEFWksht.DirDeposit) = True And GetCurrency(IAEFWksht.Refund) > 0) Or (GetBool(IAEFWksht.EFW) = True And GetCurrency(IAEFWksht.AmtOwed) > 0) Then
        Dim count As Integer
        Dim MaxAcct As Integer
        
        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)

        
        Do While count <= MaxAcct
            If GetString(USWBankAcct.BankAcct, count) <> "" Then
                If IsStrEqual(GetString(IAEFWksht.Acct), GetString(USWBankAcct.BankAcct, count)) Then
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

Private Sub DirDepSavings_Calculation()
    If (GetBool(IAEFWksht.DirDeposit) = True And GetCurrency(IAEFWksht.Refund) > 0) Or (GetBool(IAEFWksht.EFW) = True And GetCurrency(IAEFWksht.AmtOwed) > 0) Then
        
        Dim count As Integer
        Dim MaxAcct As Integer
        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)

        Do While count <= MaxAcct
            If GetString(USWBankAcct.BankAcct, count) <> "" Then
                If IsStrEqual(GetString(IAEFWksht.Acct), GetString(USWBankAcct.BankAcct, count)) Then
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

Private Sub DirDepTrigger_Calculation()
    If GetNumber(IAEFWksht.EFDDCode) = 1 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub DirectDepY_Calculation()
    If GetBool(IAEFWksht.DD) = True Then
        If GetBool(USWBankProd.RPTReturn) = True And GetBool(IAEFWksht.SameFedBank) = True Then
            ReturnVal = 1
        ElseIf GetBool(IAEFWksht.IsStateRPT) = True Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    ElseIf GetBool(IAEFWksht.DC) = True Then
        If GetBool(USWBankProd.RPTReturn) = True Then
            ReturnVal = 1
        ElseIf GetBool(IAEFWksht.IsStateRPT) = True Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If

End Sub

Private Sub EFAvailable_Calculation()
    If GetBool(IA1040X.EFAmend) = True Then
        ReturnVal = "IAX,2, Amended|"
    Else
        ReturnVal = "IA,0,|"
    End If
End Sub

Private Sub EFChecking_Calculation()
    If GetBool(IAEFWksht.PrepBPTrans) = True Then
        ReturnVal = GetBool(USWEFWkSht2.DirDepChk)    
    ElseIf GetBool(IAEFWksht.DebitCard) = True And GetCurrency(IAEFWksht.Refund) > 0 Then
        ReturnVal = 1
    ElseIf GetNumber(IAEFWksht.EFDDCode) <> 0 Then
        ReturnVal = GetBool(IAEFWksht.DirDepChecking)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub EFDan_Calculation()
    If GetBool(IAEFWksht.PrepBPTrans) = True Then
        ReturnVal = GetString(USWEFWkSht2.DirDepDan)
    ElseIf GetBool(IAEFWksht.DebitCard) = True And GetCurrency(IAEFWksht.Refund) > 0 Then
        ReturnVal = GetString(USWDebitCard.AcctNum)
    ElseIf GetNumber(IAEFWksht.EFDDCode) <> 0 Then
        ReturnVal = GetString(IAEFWksht.DirDepDan)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub EFDDCode_Calculation()
    If GetBool(IAEFWksht.PrepBPTrans) = True Then
        ReturnVal = 1    
    ElseIf GetBool(IAEFWksht.DebitCard) = True And GetCurrency(IAEFWksht.Refund) > 0 Then
        ReturnVal = 1
    ElseIf GetNumber(IAEFWksht.Yes) = 1 Then
        ReturnVal = 0
    ElseIf GetBool(IAEFWksht.DirDeposit) = True And GetCurrency(IAEFWksht.Refund) > 0 Then
        ReturnVal = 1
    ElseIf GetBool(IAEFWksht.EFW) = True And GetCurrency(IAEFWksht.AmtOwed) > 0 Then
        ReturnVal = 2
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub EFDedCode_Calculation()
    If GetBool(IARequired.LowInc) = True Then
        ReturnVal = ""
    ElseIf GetBool(IAF1040.ItemCheck) = True Then
        ReturnVal = "1"
    Else
        ReturnVal = "3"
    End If
End Sub

Private Sub EFEFWAmt_Calculation()
    If GetNumber(IAEFWksht.EFDDCode) = 2 Then
        ReturnVal = GetCurrency(IAEFWksht.AmtOwed)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub EFEFWDate_Calculation()
    If GetNumber(IAEFWksht.EFDDCode) = 2 Then
        ReturnVal = GetString(IAEFWksht.EFWDate)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub EFRtn_Calculation()
    If GetBool(IAEFWksht.PrepBPTrans) = True Then
        ReturnVal = GetString(USWEFWkSht2.DirDepRTN)
    ElseIf GetBool(IAEFWksht.DebitCard) = True And GetCurrency(IAEFWksht.Refund) > 0 Then
        ReturnVal = GetString(USWDebitCard.RTN)
    ElseIf GetNumber(IAEFWksht.EFDDCode) <> 0 Then
        ReturnVal = GetString(IAEFWksht.DirDepRTN)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub EFSavings_Calculation()
    If GetBool(IAEFWksht.PrepBPTrans) = True Then
        ReturnVal = GetBool(USWEFWkSht2.DirDepSav)       
    ElseIf GetBool(IAEFWksht.DebitCard) = True And GetCurrency(IAEFWksht.Refund) > 0 Then
        ReturnVal = 0
    ElseIf GetNumber(IAEFWksht.EFDDCode) <> 0 Then
        ReturnVal = GetBool(IAEFWksht.DirDepSavings)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub EFSpInit_Calculation()
    If GetBool(IAF1040.MFJ) = True Or GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetString(USWBasicInfo.SpInit)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub EFSpLast_Calculation()
    If GetBool(IAF1040.MFJ) = True Or GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetString(USWBasicInfo.SPLast)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub EFSpouseFirst_Calculation()
    If GetBool(IAF1040.MFJ) = True Or GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetString(USWBasicInfo.SpouseFirst)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub EFSpSuffix_Calculation()
    If GetBool(IAF1040.MFJ) = True Or GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetString(USWBasicInfo.SPSuffix)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub EFStRefund_Calculation()
    If GetBool(USWEFOptions.PiggyBackIA) = True Then
        If GetCurrency(IAEFWksht.Refund) > 0 Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub EFSubmission_Calculation()
' General Guideline to follow (use | bar if more than 1 return can be filed)
' Parameter 1 = Module Name
' Parameter 2 = Return Type: 0-Return; 1-Extension; 2-Amended; 3-Special1; 4-SpecialTaxpayer; 5-SpecialTaxpayerExtension; 6-SpecialSpouse; 7-SpecialSpouseExtension; 8-NewYorkLLC; 9-Special
' Parameter 3 = EF Type: 0-Legacy; 1-Qualifies for MeF (used if state supports legacy); 2-Must Be MeF (always used if state does not support legacy)
' Parameter 4 = Fed XML Version: 0-Send no federal XML; 1-Send accepted federal; 2-Send federal XML used to complete state return
' Parameter 5 = Special Description: description for special returns, if none space 
' Parameter 6 = Refund Owe Method: 0-No method; 1-AmEx debit card; 2-State issued debit card; 3-Direct deposit no Republic Bank; 4-Direct deposit through Republic Bank; 5-Paper check (refund); 6-AmEx debit card through Republic; 10-Direct debit; 11-Credit card; 12-Paper check (owe); 13-IRS EFTPS

    Dim RefOweMethod As String

    If GetBool(USWEFOptions.PiggyBackIA) = True Or GetBool(USWEFOptions.SOIA) = True Then
        If GetCurrency(IAF1040.RefBalDue) = 0 Then
            RefOweMethod = "0"
        ElseIf GetBool(IAEFWksht.PrepBPTrans) = True Then
            RefOweMethod = "4"
        ElseIf GetBool(IAEFWksht.DC) = True Then
            If GetBool(USWBankProd.RPTReturn) = True Then
                RefOweMethod = "6"
            ElseIf GetBool(IAEFWksht.IsStateRPT) = True Then
                RefOweMethod = "6"
            Else
                RefOweMethod = "1"
            End If
        ElseIf GetBool(IAEFWksht.DD) = True Then
            If GetBool(USWBankProd.RPTReturn) = True And GetBool(IAEFWksht.SameFedBank) = True Then
                RefOweMethod = "4"
            ElseIf GetBool(IAEFWksht.IsStateRPT) = True Then
                RefOweMethod = "4"
            Else
                RefOweMethod = "3"
            End If
        ElseIf GetCurrency(IAF1040.RefBalDue) > 0 Then
            RefOweMethod = "5"
        ElseIf GetString(IAEFWksht.EFDDCode) = "2" Then
            RefOweMethod = "10"
        Else
            RefOweMethod = "12"
        End If
    ElseIf GetBool(USWEFOptions.SOIAX) = True Then
        If GetCurrency(IAF1040.RefBalDue) = 0 Then
            RefOweMethod = "0"
        ElseIf GetBool(IAEFWksht.DD) = True Then
            RefOweMethod = "3"
        ElseIf GetCurrency(IAF1040.RefBalDue) > 0 Then
            RefOweMethod = "5"
        ElseIf GetString(IAEFWksht.EFDDCode) = "2" Then
            RefOweMethod = "10"
        Else
            RefOweMethod = "12"
        End If
    Else
        RefOweMethod = "0"
    End If

    If GetBool(USWEFOptions.PiggyBackIA) = True Or GetBool(USWEFOptions.SOIA) = True Then
        ReturnVal = "IA;0;2;2; ;" + RefOweMethod + "|"
    ElseIf GetBool(USWEFOptions.SOIAX) = True Then
        ReturnVal = "IA;2;2;2;Amended;" + RefOweMethod + "|"
    Else
        ReturnVal = ""
    End If

End Sub

Private Sub EROAddress_Calculation()
    If IsPreparer() = True Then
        ReturnVal = GetString(USWBasicInfo.EROAddress)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub EROCityComb_Calculation()
    If IsPreparer() = False Then
        ReturnVal = ""
    ElseIf Trim(GetString(USWBasicInfo.EROForCtry)) <> "" Then
        If Trim(GetString(USWBasicInfo.EROForProvince)) <> "" And Trim(GetString(USWBasicInfo.EROForPC)) <> "" Then
            ReturnVal = GetString(USWBasicInfo.EROCity) & ", " & GetString(USWBasicInfo.EROForProvince) & ", " & GetString(USWBasicInfo.EROForPC) & ", " & GetString(USWBasicInfo.EROForCtry)
        ElseIf Trim(GetString(USWBasicInfo.EROForProvince)) <> "" Then
            ReturnVal = GetString(USWBasicInfo.EROCity) & ", " & GetString(USWBasicInfo.EROForProvince) & ", " & GetString(USWBasicInfo.EROForCtry)
        ElseIf Trim(GetString(USWBasicInfo.EROForPC)) <> "" Then
            ReturnVal = GetString(USWBasicInfo.EROCity) & ", " & GetString(USWBasicInfo.EROForPC) & ", " & GetString(USWBasicInfo.EROForCtry)
        Else
            ReturnVal = GetString(USWBasicInfo.EROCity) & ", " & GetString(USWBasicInfo.EROForCtry)
        End If
    ElseIf Trim(GetString(USWBasicInfo.EROCity)) <> "" Then
        ReturnVal = GetString(USWBasicInfo.EROCity) & ", " & GetString(USWBasicInfo.StateAbbERO) & " " & GetString(USWBasicInfo.EROZip)
    Else
        ReturnVal = GetString(USWBasicInfo.StateAbbERO) & " " & GetString(USWBasicInfo.EROZip)
    End If
End Sub

Private Sub EROEIN_Calculation()
    If IsPreparer() = True Then
        ReturnVal = GetString(USWBasicInfo.EROEIN)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub EROFirmName_Calculation()
    If IsPreparer() = True Then
        ReturnVal = GetString(USWBasicInfo.EROFirmName)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub EROPhone_Calculation()
    If IsPreparer() = False Then
        ReturnVal = ""
    ElseIf Trim(GetString(USWBasicInfo.EROPhone)) <> "" Then
        ReturnVal = GetString(USWBasicInfo.EROPhone)
    Else
        ReturnVal = GetString(USWBasicInfo.EROForPhone)
    End If
End Sub

Private Sub EROPrep_Calculation()
    If IsPreparer() = True Then
        ReturnVal = GetBool(USWBasicInfo.PaidPrepY)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub EROSE_Calculation()
    If IsPreparer() = True Then
        ReturnVal = GetBool(USWBasicInfo.EROSelfEmp)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub EROSSN_Calculation()
    Dim EROPTIN As String
    
    EROPTIN = LetterStr(GetString(USWBasicInfo.EROSSN))
    
    If IsPreparer() = True And IsStrEqual(EROPTIN, "P") Then
        ReturnVal = GetString(USWBasicInfo.EROSSN)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub Exist_Calculation()
    ReturnVal = 1
End Sub

Private Sub FedChecking_Calculation()
    If GetCurrency(USWBasicInfo.WithdrawalAmt) > 0 And GetDate(USWBasicInfo.withdrawldate) <> "" Then
        ReturnVal = GetBool(USWBasicInfo.ACHChecking)
    Else
        ReturnVal = GetBool(USF8888.EFChecking(0))
    End If
End Sub

Private Sub FedDAN_Calculation()
    If GetCurrency(USWBasicInfo.WithdrawalAmt) > 0 And GetDate(USWBasicInfo.withdrawldate) <> "" Then
        ReturnVal = GetString(USWBasicInfo.ACHDAN)
    Else
        ReturnVal = GetString(USF8888.EFAcctNum(0))
    End If
End Sub

Private Sub FedRTN_Calculation()
    If GetCurrency(USWBasicInfo.WithdrawalAmt) > 0 And GetDate(USWBasicInfo.withdrawldate) <> "" Then
        ReturnVal = GetString(USWBasicInfo.ACHRTN)
    Else
        ReturnVal = GetString(USF8888.EFRtn(0))
    End If
End Sub

Private Sub FedSavings_Calculation()
    If GetCurrency(USWBasicInfo.WithdrawalAmt) > 0 And GetDate(USWBasicInfo.withdrawldate) <> "" Then
        ReturnVal = GetBool(USWBasicInfo.ACHSavings)
    Else
        ReturnVal = GetBool(USF8888.EFSaveAcct(0))
    End If
End Sub

Private Sub FedTrans_Calculation()
    'If (GetBool(IAEFWksht.DirDeposit) = True And GetCurrency(IAEFWksht.Refund) > 0) Or (GetBool(IAEFWksht.EFW) = True And GetCurrency(IAEFWksht.AmtOwed) > 0) Then
    '    If GetBool(IAEFWksht.TransInfo) = True Then
    '        ReturnVal = 1
    '    Else
    '        ReturnVal = 0
    '    End If
    'Else
    ReturnVal = 0
    'End If
End Sub

Private Sub FinTransTrigger_Calculation()
    If GetNumber(IAEFWksht.EFDDCode) <> 0 Then
        ReturnVal = 1
    ElseIf GetNumber(IAEstimates.EstEFW, 1) > 0 Or GetNumber(IAEstimates.EstEFW, 2) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub ForCity_Calculation()
    ReturnVal = GetString(USWBasicInfo.ForCity)
End Sub

Private Sub ForCountry_Calculation()
    ReturnVal = GetString(USWBasicInfo.ForCountry)
End Sub

Private Sub ForStreet_Calculation()
    ReturnVal = GetString(USWBasicInfo.ForStreet)
End Sub

Private Sub IsStateRPT_Calculation()
    If GetBool(IAEFWksht.AskStateRT) = False Then
        ReturnVal = 0
    ElseIf GetBool(USWBankProd.ClearedInvoiceFees) = True Then
        ReturnVal = 0
    ElseIf GetBool(USWRALApp.StateRTDC) = True And GetBool(IAEFWksht.AskSORTDC) = False Then
        ReturnVal = 0
    ElseIf GetBool(USWBankProd.StateRPT) = True And GetBool(USWBankProd.StateBankAgree) = True And GetBool(USWBankProd.StateBankAgree2) = True And GetCurrency(IAEFWksht.Refund) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub MeFPrepInfo_Calculation()
    If IsPreparer() = True Then
        If GetBool(USWBasicInfo.NoPrep) = False Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub MeFSP137_Calculation()
    If GetNumber(IA137.MEF137SP, FieldCopies(IA137.Spouse)) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub MeFTP137_Calculation()
    If GetNumber(IA137.MEF137TP, FieldCopies(IA137.Taxpayer)) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Need8453_Calculation()
    ReturnVal = 1
End Sub

Private Sub No_Calculation()
If (GetBool(IAEFWksht.DirDeposit) = True And GetCurrency(IAEFWksht.Refund) > 0) Or (GetBool(IAEFWksht.EFW) = True And GetCurrency(IAEFWksht.AmtOwed) > 0) Then
    If GetBool(IAEFWksht.Yes) = True Then
        ReturnVal = 0
    Else
        ReturnVal = 1
    End If
Else
    ReturnVal = 0
End If
End Sub

Private Sub NoBankSel_Calculation()
    If GetBool(IAEFWksht.DirDeposit) = True Or GetBool(IAEFWksht.EFW) Then
        If Trim(GetString(IAEFWksht.Acct)) = "" Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub NoBankSelInt_Calculation()
    If (GetBool(IAEFWksht.DirDeposit) = True) Or (GetBool(IAEFWksht.EFW) = True) Then
        If GetBool(USTopicList.HaveBankWSSend) = False Then
            ReturnVal = 0
        ElseIf Trim(GetString(IAEFWksht.Acct)) = "" Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub NoDDEFW_Calculation()
    If GetBool(IAEFWksht.IsStateRPT) = True Then
        ReturnVal = 0
    ElseIf GetBool(USWBasicInfo.DirectDepN) = True And GetCurrency(USF1040.RefundOwe) > 0 Then
        If GetCurrency(IAEFWksht.Refund) > 0 Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub NonForCity_Calculation()
    ReturnVal = GetString(USWBasicInfo.NonForCity)
End Sub

Private Sub NonForState_Calculation()
    ReturnVal = GetString(USWBasicInfo.NonForState)
End Sub

Private Sub NonForStreet_Calculation()
    ReturnVal = GetString(USWBasicInfo.NonForStreet)
End Sub

Private Sub NonForZip_Calculation()
    ReturnVal = GetString(USWBasicInfo.NonForZip)
End Sub

Private Sub PC_Calculation()
    If GetCurrency(IAEFWksht.Refund) = 0 Then 
        ReturnVal = 0
    ElseIf GetBool(IAEFWksht.DD) = False And GetBool(IAEFWksht.BP) = False And GetBool(IAEFWksht.DC) = False Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PrBankName_Calculation()
    If GetNumber(IAEFWksht.EFDDCode) <> 0 And GetBool(IAEFWksht.DebitCard) = False And GetBool(IAEFWksht.PrepBPTrans) = False Then
        ReturnVal = GetString(IAEFWksht.BankName)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub PrChecking_Calculation()
    If GetNumber(IAEFWksht.EFDDCode) <> 0 And GetBool(IAEFWksht.DebitCard) = False And GetBool(IAEFWksht.PrepBPTrans) = False Then
        ReturnVal = GetBool(IAEFWksht.DirDepChecking)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PrDAN_Calculation()
    If GetNumber(IAEFWksht.EFDDCode) <> 0 And GetBool(IAEFWksht.DebitCard) = False And GetBool(IAEFWksht.PrepBPTrans) = False Then
        ReturnVal = GetString(IAEFWksht.DirDepDan)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub PrepAddress_Calculation()
    If IsPreparer() = True Then
        If GetBool(IAEFWksht.EROPrep) = False Then
            ReturnVal = GetString(USWBasicInfo.PrepAdd)
        Else
            ReturnVal = ""
        End If
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub PrepBPTrans_Calculation()
    If GetBool(USWRALApp.RepRouteState) = False Then
        ReturnVal = 0
    ElseIf IsPreparer() = False Then
        ReturnVal = 0
    ElseIf GetBool(USWBasicInfo.BankProd) = True And GetCurrency(USF1040.RefundOwe) > 0 Then
        If GetBool(USWBankProd.Republic) = True And GetBool(IAEFWksht.EFStRefund) = True Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PrepCityComb_Calculation()
    If IsPreparer() = True Then
        If GetBool(IAEFWksht.EROPrep) = False Then
            ReturnVal = GetString(USWBasicInfo.CombPrepCityStZipFor)
        Else
            ReturnVal = ""
        End If
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub PrepEIN_Calculation()
    If IsPreparer() = True Then
        If GetBool(IAEFWksht.EROPrep) = False Then
            ReturnVal = GetString(USWBasicInfo.PrepEIN)
        Else
            ReturnVal = ""
        End If
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub PrepFirmName_Calculation()
    If IsPreparer() = True Then
        If GetBool(IAEFWksht.EROPrep) = False Then
            ReturnVal = GetString(USWBasicInfo.PrepName)
        Else
            ReturnVal = ""
        End If
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub PrepPhone_Calculation()
    If IsPreparer() = True Then
        If GetBool(IAEFWksht.EROPrep) = False Then
            ReturnVal = GetString(IAF1040.PrepPhone)
        Else
            ReturnVal = ""
        End If
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub PrepSE_Calculation()
    If IsPreparer() = True Then
        If GetBool(IAEFWksht.EROPrep) = False Then
            ReturnVal = GetBool(USWBasicInfo.SelfEm)
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PrepSSN_Calculation()
    If IsPreparer() = True Then
        If GetBool(IAEFWksht.EROPrep) = False Then
            ReturnVal = GetString(USWBasicInfo.PrepSSN)
        Else
            ReturnVal = ""
        End If
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub PrERODate_Calculation()
    If GetBool(IAEFWksht.EROPrep) = True Then
        ReturnVal = GetString(USWBasicInfo.PrPrepDate)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub PrEROSig_Calculation()
    If GetBool(IAEFWksht.EROPrep) = True Then
        ReturnVal = GetString(USWBasicInfo.PrPrepSig)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub PrintReturn_Calculation()
    PrintList_Clear(PrintList_EF) 
    
    If Trim(GetString(IAEFWksht.EFSubmission)) <> "" Then
        If GetBool(IA1040X.EFAmend) = True Then
            PrintList_AddHTML(PrintList_EF, EFReturnType_AmendedReturn, "E-filing Instructions", "ia instructions/IAWEFFilingInst.htm")
            If GetBool(IAEFWksht.Need8453) = True Then
                PrintList_AddCustom(PrintList_EF, EFReturnType_AmendedReturn, "Form 8453", "PrintEFileForms")
            End If
            PrintList_AddReturn(PrintList_EF, EFReturnType_AmendedReturn, "Amended Return")
        Else
            PrintList_AddHTML(PrintList_EF, EFReturnType_Return, "E-filing Instructions", "ia instructions/IAWEFFilingInst.htm")
            If GetBool(IAEFWksht.Need8453) = True Then
                PrintList_AddCustom(PrintList_EF, EFReturnType_Return, "Form 8453", "PrintEFileForms")
            End If
            PrintList_AddReturn(PrintList_EF, EFReturnType_Return, "Return")
        End If
    End If
    
    ReturnVal = ""
End Sub

Private Sub PrPrepDate_Calculation()
    If IsPreparer() = True Then
        If GetBool(IAEFWksht.EROPrep) = False Then
            ReturnVal = GetString(USWBasicInfo.PrPrepDate)
        Else
            ReturnVal = ""
        End If
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub PrPrepSig_Calculation()
    If IsPreparer() = True Then
        If GetBool(IAEFWksht.EROPrep) = False Then
            ReturnVal = GetString(USWBasicInfo.PrPrepSig)
        Else
            ReturnVal = ""
        End If
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub PrRtn_Calculation()
    If GetNumber(IAEFWksht.EFDDCode) <> 0 And GetBool(IAEFWksht.DebitCard) = False And GetBool(IAEFWksht.PrepBPTrans) = False Then
        ReturnVal = GetString(IAEFWksht.DirDepRTN)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub PrSavings_Calculation()
    If GetNumber(IAEFWksht.EFDDCode) <> 0 And GetBool(IAEFWksht.DebitCard) = False And GetBool(IAEFWksht.PrepBPTrans) = False Then
        ReturnVal = GetBool(IAEFWksht.DirDepSavings)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub QnAFedBank_Calculation()
    'If GetBool(IAEFWksht.AskFedStateBank) = True Then
    '    ReturnVal = 0
    'ElseIf (GetBool(IAEFWksht.DirDeposit) = True And GetCurrency(IAEFWksht.Refund) > 0) Or (GetBool(IAEFWksht.EFW) = True And GetCurrency(IAEFWksht.AmtOwed) > 0) Then
    '    If GetBool(IAEFWksht.TransInfo) = True Then
    '        ReturnVal = 1
    '    ElseIf Trim(GetString(IAEFWksht.FedRTN)) <> "" And Trim(GetString(IAEFWksht.FedDAN)) <> "" Then
    '        ReturnVal = 1
    '    Else
    '        ReturnVal = 0
    '    End If
    'Else
        ReturnVal = 0
    'End If
End Sub

Private Sub RefProdCIPInd_Calculation()
    Dim Submission As String
    Dim TempStr As String
    
    TempStr = GetString(IAEFWksht.EFSubmission)
    Submission = GetParam(TempStr, 1, "|")

    If GetParam(Submission, 6, ";") = "0" Then
        ReturnVal = "0"
    ElseIf GetParam(Submission, 6, ";") = "1" Then
        If Trim(GetString(USWDebitCard.IDNumber)) <> "" Then
            ReturnVal = "1"
        Else
            ReturnVal = "2"
        End If
    ElseIf GetParam(Submission, 6, ";") = "3" Then
        ReturnVal = "0"
    ElseIf GetParam(Submission, 6, ";") = "4" Then
        ReturnVal = "1"
    ElseIf GetParam(Submission, 6, ";") = "5" Then
        ReturnVal = "0"
    ElseIf GetParam(Submission, 6, ";") = "6" Then
        ReturnVal = "1"
    Else
        ReturnVal = "0"
    End If
End Sub

Private Sub RefProdInd_Calculation()
    Dim Submission As String
    Dim TempStr As String
    
    TempStr = GetString(IAEFWksht.EFSubmission)
    Submission = GetParam(TempStr, 1, "|")

    If GetParam(Submission, 6, ";") = "0" Then
        ReturnVal = "0"
    ElseIf GetParam(Submission, 6, ";") = "1" Then
        ReturnVal = "2"
    ElseIf GetParam(Submission, 6, ";") = "2" Then
        ReturnVal = "0"
    ElseIf GetParam(Submission, 6, ";") = "3" Then
        ReturnVal = "0"
    ElseIf GetParam(Submission, 6, ";") = "4" Then
        ReturnVal = "2"
    ElseIf GetParam(Submission, 6, ";") = "5" Then
        ReturnVal = "0"
    ElseIf GetParam(Submission, 6, ";") = "6" Then
        ReturnVal = "2"
    Else
        ReturnVal = "0"
    End If
    
End Sub

Private Sub Refund_Calculation()
    ReturnVal = GetCurrency(IAF1040.Refund)
End Sub

Private Sub RefundDelay_Calculation()
'this was set to 1 in 2017 will need to verify again for 2018 before shipping
    ReturnVal = 0
End Sub

Private Sub RTNChange_Calculation()
    ReturnVal = GetString(IAEFWksht.DirDepRTN) + "|"
End Sub

Private Sub SameFedBank_Calculation()
    Dim SameRTN As Integer
    Dim SameDAN As Integer
    Dim SameType As Integer
    
    If GetString(IAEFWksht.FedRTN) = GetString(IAEFWksht.DirDepRTN) Then
        SameRTN = 1
    Else
        SameRTN = 0
    End If
    
    If GetString(IAEFWksht.FedDAN) = GetString(IAEFWksht.DirDepDan) Then
        SameDAN = 1
    Else
        SameDAN = 0
    End If
    
    If GetBool(IAEFWksht.FedChecking) = True And GetBool(IAEFWksht.DirDepChecking) = True Then
        SameType = 1
    ElseIf GetBool(IAEFWksht.FedSavings) = True And GetBool(IAEFWksht.DirDepSavings) = True Then
        SameType = 1
    Else
        SameType = 0
    End If
    
    If GetBool(USWBasicInfo.DirectDepY) = True And GetCurrency(USF1040.RefundOwe) > 0 Then
        If SameRTN + SameDAN + SameType = 3 Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If

End Sub

Private Sub SPCombName_Calculation()
    ReturnVal = GetString(IARequired.SPCombName)
End Sub

Private Sub SpSSN_Calculation()
    ReturnVal = GetString(IAF1040.SpouseSSN)
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

Private Sub StateDCReturn_Calculation()
    If GetBool(USWEFOptions.PiggyBackIA) = True Or GetBool(USWEFOptions.SOIA) = True Or GetBool(USWEFOptions.SOIAX) = True Then
        If GetBool(IAEFWksht.DebitCard) = True And GetCurrency(IAEFWksht.Refund) > 0 And GetBool(IAEFWksht.AskDebitCard) = True Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPCombName_Calculation()
    ReturnVal = GetString(IARequired.TPCombName)
End Sub

Private Sub UBATrig_Calculation()
    If GetString(IAEFWksht.BankProDisCd) = "1" Then
        ReturnVal = 1
    ElseIf GetString(IAEFWksht.BankProDisCd) = "2" Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub UltDAN_Calculation()
    If GetBool(IAEFWksht.PrepBPTrans) = True Then
        ReturnVal = GetString(USWRALApp.PrepBPDAN)
    Else
        ReturnVal = GetString(IAEFWksht.EFDan)
    End If
End Sub

Private Sub UltRTN_Calculation()
    If GetBool(IAEFWksht.PrepBPTrans) = True Then
        ReturnVal = GetString(USWRALApp.PrepBPRTN)
    Else
        ReturnVal = GetString(IAEFWksht.EFRtn)
    End If
End Sub

Private Sub ViewBankInfo_Calculation()
    Dim RefOweText As String
    Dim DispMethText As String
    Dim Routing As String
    Dim AcctNum As String
    Dim BankType As String
    Dim EffDate As String
    
    RefOweText = ""
    DispMethText = ""
    Routing = ""
    AcctNum = ""
    BankType = ""
    EffDate = ""
    
    If GetCurrency(IAEFWksht.Refund) > 0 Then
        If GetBool(IA1040X.EFAmend) = True Then
            RefOweText = "Iowa Amended Refund"
        Else
            RefOweText = "Iowa Refund"
        End If
        
        If GetBool(IAEFWksht.BP) = True Then
            DispMethText = "Republic Bank Product"
        ElseIf GetBool(IAEFWksht.DD) = True Then
            DispMethText = "Direct Deposit"
            Routing = "RTN: " + GetString(IAEFWksht.EFRtn)
            AcctNum = "Acct #: " + GetString(IAEFWksht.EFDan)
            If GetBool(IAEFWksht.EFChecking) = True Then
                BankType = "Type: Checking"
            Else
                BankType = "Type: Savings"
            End If
        ElseIf GetBool(IAEFWksht.DC) = True Then
            DispMethText = "American Express Serve Card"
        Else
            DispMethText = "Paper Check"
        End If
        
        ReturnVal = RefOweText + "/Refund Method: " + DispMethText + "/" + Routing + "/" + AcctNum + "/" + BankType
    ElseIf GetCurrency(IAEFWksht.AmtOwed) > 0 Then
        If GetBool(IA1040X.EFAmend) = True Then
            RefOweText = "Iowa Amended Balance Due"
        Else
            RefOweText = "Iowa Balance Due"
        End If
        
        If GetBool(IAEFWksht.ACH) = True Then
            DispMethText = "Direct Withdrawal"
            Routing = "RTN: " + GetString(IAEFWksht.EFRtn)
            AcctNum = "Acct #: " + GetString(IAEFWksht.EFDan)
            If GetBool(IAEFWksht.EFChecking) = True Then
                BankType = "Type: Checking"
            Else
                BankType = "Type: Savings"
            End If
            EffDate = "Withdrawal Date: " + GetVerboseDate(GetDate(IAEFWksht.EFEFWDate))
        Else
            DispMethText = "Paper Check"
        End If
        
        ReturnVal = RefOweText + "/Payment Method: " + DispMethText + "/" + Routing + "/" + AcctNum + "/" + BankType + "/" + EffDate
    Else
        If GetBool(IA1040X.EFAmend) = True Then
            ReturnVal = "Iowa:  No Refund or Balance Due on Amended Return"
        Else
            ReturnVal = "Iowa:  No Refund or Balance Due"
        End If
    End If
End Sub

Private Sub Yes_Calculation()
    If (GetBool(IAEFWksht.DirDeposit) = True And GetCurrency(IAEFWksht.Refund) > 0) Or (GetBool(IAEFWksht.EFW) = True And GetCurrency(IAEFWksht.AmtOwed) > 0) Then
        Dim count As Integer
        Dim MaxAcct As Integer
        
        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)

        Do While count <= MaxAcct
            If GetString(USWBankAcct.BankAcct, count) <> "" Then
                If IsStrEqual(GetString(IAEFWksht.Acct), GetString(USWBankAcct.BankAcct, count)) Then
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

