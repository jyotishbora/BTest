Private Sub AddComm1_Calculation()
    If Trim(GetString(IAWPrepCLtr.Comm1)) <> "" Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AddComm2_Calculation()
    If Trim(GetString(IAWPrepCLtr.Comm2)) <> "" Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AddComm3_Calculation()
    If Trim(GetString(IAWPrepCLtr.Comm3)) <> "" Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AddComm4_Calculation()
    If Trim(GetString(IAWPrepCLtr.Comm4)) <> "" Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AddComm5_Calculation()
    If Trim(GetString(IAWPrepCLtr.Comm5)) <> "" Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AddComm6_Calculation()
    If Trim(GetString(IAWPrepCLtr.Comm6)) <> "" Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub C1EstInfo_Calculation()
    If GetBool(IAWPrepCLtr.NEst) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetBool(IAFilingInst.C1EstInfo)
    End If
End Sub

Private Sub C2EstInfo_Calculation()
    If GetBool(IAWPrepCLtr.NEst) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetBool(IAFilingInst.C2EstInfo)
    End If
End Sub

Private Sub Comm1_Calculation()
    ReturnVal = GetString(USWPrepMasterLet.StComm1)
End Sub

Private Sub Comm2_Calculation()
    ReturnVal = GetString(USWPrepMasterLet.StComm2)
End Sub

Private Sub Comm3_Calculation()
    ReturnVal = GetString(USWPrepMasterLet.StComm3)
End Sub

Private Sub Comm4_Calculation()
    ReturnVal = GetString(USWPrepMasterLet.StComm4)
End Sub

Private Sub Comm5_Calculation()
    ReturnVal = GetString(USWPrepMasterLet.StComm5)
End Sub

Private Sub Comm6_Calculation()
    ReturnVal = GetString(USWPrepMasterLet.StComm6)
End Sub

Private Sub Date_Calculation()
    ReturnVal = GetString(USWPrepCLtr.Date)
End Sub

Private Sub EFAccept_Calculation()
    If GetBool(IAWPrepCLtr.EFRet) = True Then
        If GetBool(USWPrepCLtr.Transmit) = True Then
            ReturnVal = 0
        ElseIf GetBool(USWPrepCLtr.WasTran) = True Then
            ReturnVal = 0
        ElseIf GetBool(USWPrepCLtr.F8879) = True Then
            ReturnVal = 0
        Else
            ReturnVal = 1
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub EFDate_Calculation()
    ReturnVal = GetString(IAWPrepCLtr.StSubmitDate)
End Sub

Private Sub EFRet_Calculation()
    If GetBool(IAWPrepCLtr.PaperRet) = True Then
        ReturnVal = 0
    Else
        ReturnVal = 1
    End If
End Sub

Private Sub EFTrans_Calculation()
    If GetBool(IAWPrepCLtr.EFRet) = True Then
        If GetBool(USWPrepCLtr.Transmit) = True Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub EFWasTran_Calculation()
    If GetBool(IAWPrepCLtr.EFRet) = True Then
        If GetBool(USWPrepCLtr.WasTran) = True Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub EstInfo_Calculation()
    If GetBool(IAWPrepCLtr.NEst) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetBool(IAFilingInst.EstInfo)
    End If
End Sub

Private Sub Exist_Calculation()
    ReturnVal = 1
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(USWPrepCLtr.Names)
End Sub

Private Sub NEst_Calculation()
    If GetBool(IAEstimates.Print, 1) = False And GetBool(IAEstimates.Print, 2) = False Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PaperAdd1_Calculation()
    If GetBool(IAWPrepCLtr.PaperRet) = True Then
        ReturnVal = GetString(IAFilingInst.IRSAdd1) + "<br>" + GetString(IAFilingInst.IRSAdd2) + "<br>" + GetString(IAFilingInst.IRSAdd3)
    ElseIf GetBool(IAWPrepCLtr.EFRet) = True And GetNumber(IA1040V.PrVou) = 1 Then
        ReturnVal = GetString(IAFilingInst.IRSAdd1) + "<br>" + GetString(IAFilingInst.IRSAdd2) + "<br>" + GetString(IAFilingInst.IRSAdd3)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub PaperRet_Calculation()
    If GetBool(USWEFQual.QualifiesForEF) = False Then
        ReturnVal = 1
    ElseIf GetBool(IAWEFQual.NotQualifyEF) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PrepPaymentDate_Calculation()
    ReturnVal = GetVerboseDate(GetDate(IAEFWksht.EFEFWDate))
End Sub

Private Sub Refund_Calculation()
    ReturnVal = GetBool(USWPrepCLtr.Refund)
End Sub

Private Sub Ret1_Calculation()
    If GetBool(IAWPrepCLtr.EFRet) = True Then
        ReturnVal = "Please find enclosed a copy of your " + YearString + " Iowa income tax return for your records."
    Else
        ReturnVal = "Please find enclosed your " + YearString + " Iowa income tax return as well as a copy for your records."
    End If
End Sub

Private Sub Ret2_Calculation()
    If GetBool(IAWPrepCLtr.EFRet) = True And GetBool(USWPrepCLtr.NA) = True Then
        ReturnVal = "Your Iowa return was electronically transmitted to the Iowa Department of Revenue;"
    ElseIf GetBool(IAWPrepCLtr.EFWasTran) = True Then
        ReturnVal = "Your Iowa return was electronically transmitted to the Iowa Department of Revenue on " + GetString(IAWPrepCLtr.VerbEFDate) + ";"
    ElseIf GetBool(IAWPrepCLtr.EFAccept) = True Then
        ReturnVal = "Your Iowa return was electronically filed and accepted by the Iowa Department of Revenue on " + GetString(IAWPrepCLtr.VerbEFDate) + ";"
    ElseIf GetBool(IAWPrepCLtr.EFTrans) = True Then
        ReturnVal = "Your Iowa return will be electronically transmitted to the Iowa Department of Revenue on " + GetString(IAWPrepCLtr.VerbEFDate) + ";"
    ElseIf GetBool(IAWPrepCLtr.EFRet) = True Then
        ReturnVal = "Your Iowa return will be electronically transmitted to the Iowa Department of Revenue;"
    Else
        ReturnVal = "Your Iowa return is due " + GetString(IAWPrepCLtr.VerbStDate) + "."
    End If
End Sub

Private Sub Ret3_Calculation()
    If GetBool(IAWPrepCLtr.EFRet) = True Then
        ReturnVal = "therefore, do not mail your Iowa Form 1040 to the Iowa Department of Revenue."
    Else
        ReturnVal = "Please sign and date your Iowa Form 1040."
    End If
End Sub

Private Sub Ret3a_Calculation()
    If GetBool(IAWPrepCLtr.PaperRet) = True And GetNumber(IA1040V.PrVou) = 1 Then
        ReturnVal = "Mail your Iowa Form 1040, Iowa payment voucher, payment and required attachments to:"
    ElseIf GetBool(IAWPrepCLtr.PaperRet) = True Then
        ReturnVal = "Mail your Iowa Form 1040 and required attachments to:"
    ElseIf GetBool(IAWPrepCLtr.EFRet) = True And GetNumber(IA1040V.PrVou) = 1 And GetDate(IAWPrepCLtr.Date) > GetDate(IAWPrepCLtr.StDueDate) Then
        ReturnVal = "Mail your payment and Iowa payment voucher (Form IA 1040-V) to:"
    ElseIf GetBool(IAWPrepCLtr.EFRet) = True And GetNumber(IA1040V.PrVou) = 1 Then
        ReturnVal = "Mail your payment and Iowa payment voucher (Form IA 1040-V) by " + GetString(IAWPrepCLtr.VerbStDate) + " to:"
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub Ret4_Calculation()
    ReturnVal = GetString(IAWPrepCLtr.PaperAdd1)
End Sub

Private Sub Ret7_Calculation()
    If GetCurrency(IAF1040.RefBalDue) < 0 Then
        ReturnVal = "The amount you owe on your Iowa return is "
    Else
        ReturnVal = "The amount you overpaid on your Iowa return is "
    End If
End Sub

Private Sub Ret7Amount_Calculation()
    If GetCurrency(IAF1040.RefBalDue) < 0 Then
        ReturnVal = GetCurrency(IAF1040.TotDue)
    Else
        ReturnVal = GetCurrency(IAF1040.OVerPaid)
    End If
End Sub

Private Sub Ret8_Calculation()
    If GetBool(IAWPrepCLtr.EFRet) = True And GetCurrency(IAF1040.RefBalDue) < 0 And GetString(IAEFWksht.EFDDCode) = "2" Then
        ReturnVal = "Your payment is scheduled to be withdrawn from your bank account on " + GetString(IAWPrepCLtr.PrepPaymentDate) + "."
    ElseIf GetCurrency(IAF1040.RefBalDue) < 0 Then
        ReturnVal = "Make your check or money order payable to ' Treasurer - State of Iowa '."
    Else
        ReturnVal = "The amount of overpayment applied to your " + NextYearString + " estimates is "
    End If
End Sub

Private Sub Ret8Amount_Calculation()
    ReturnVal = GetCurrency(IARequired.TotApplied)
End Sub

Private Sub Ret8Trig_Calculation()
    If GetCurrency(IAF1040.RefBalDue) < 0 Then
        ReturnVal = 0
    Else
        ReturnVal = 1
    End If
End Sub

Private Sub Ret9_Calculation()
' balance due
    If GetBool(IAWPrepCLtr.EFRet) = True And GetString(IAEFWksht.EFDDCode) = "2" Then
        ReturnVal = ""
    ElseIf GetCurrency(IAF1040.RefBalDue) < 0 Then
        ReturnVal = "Write '" + YearString + " Form 1040' on your check."
' refund
    ElseIf GetBool(IAWPrepCLtr.EFRet) = True And GetBool(IAWPrepCLtr.Refund) = True And GetBool(IAEFWksht.PrepBPTrans) = True Then
        ReturnVal = "The amount to be refunded to you is "
    ElseIf GetBool(IAWPrepCLtr.EFRet) = True And GetBool(IAWPrepCLtr.Refund) = True And GetString(IAEFWksht.EFDDCode) = "1" Then
        ReturnVal = "The amount to be refunded to you by direct deposit is "
    ElseIf GetBool(IAWPrepCLtr.Refund) = True And GetCurrency(IAF1040.Refund) > 0 And Trim(GetString(IAF1040.ActNum)) <> "" Then
        ReturnVal = "The amount to be refunded to you by direct deposit is "
    ElseIf GetBool(IAWPrepCLtr.Refund) = True And GetCurrency(IAF1040.Refund) > 0 Then
        ReturnVal = "The amount to be refunded to you by paper check is "
    Else
        ReturnVal = "The amount to be refunded to you is "
    End If
End Sub

Private Sub Ret9Amount_Calculation()
    ReturnVal = GetCurrency(IAF1040.Refund)
End Sub

Private Sub StateEF_Calculation()
    Dim TempStr As String
    Dim TempCount As Long
    Dim TempHold As Long
    Dim Submission As String
    
    TempStr = GetString(USWEFOptions.EFSubmissionHistory)
    TempCount = 1
    TempHold = 0
    
    Submission = GetParam(TempStr, TempCount, "|")
    
    Do While Submission <> ""
        If GetParam(Submission, 1, ";") = "IA" And GetParam(Submission, 2, ";") = "0" Then
            ReturnVal = 1
        End If
        
        TempCount = TempCount + 1
        Submission = GetParam(TempStr, TempCount, "|")
    Loop

    ReturnVal = 0
End Sub

Private Sub StDueDate_Calculation()
    ReturnVal = #4/30/2019#
End Sub

Private Sub StSubmitDate_Calculation()
    Dim TempStr As String
    Dim TempCount As Long
    Dim TempHold As Long
    Dim Submission As String
    
    TempStr = GetString(USWEFOptions.EFSubmissionHistory)
    TempCount = 1
    TempHold = 0
    
    Submission = GetParam(TempStr, TempCount, "|")
    
    Do While Submission <> ""
        If GetParam(Submission, 1, ";") = "IA" And GetParam(Submission, 2, ";") = "0" Then
            ReturnVal = GetParam(Submission, 4, ";")
        End If
        
        TempCount = TempCount + 1
        Submission = GetParam(TempStr, TempCount, "|")
    Loop

    ReturnVal = ""
End Sub

Private Sub VerbDate_Calculation()
    ReturnVal = GetVerboseDate(GetDate(IAWPrepCLtr.Date))
End Sub

Private Sub VerbEFDate_Calculation()
    ReturnVal = GetVerboseDate(GetDate(IAWPrepCLtr.EFDate))
End Sub

Private Sub VerbStDate_Calculation()
    ReturnVal = GetVerboseDate(GetDate(IAWPrepCLtr.StDueDate))
End Sub

Private Sub YEst_Calculation()
    If GetBool(IAEstimates.Print, 1) = True Or GetBool(IAEstimates.Print, 2) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

