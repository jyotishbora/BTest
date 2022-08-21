Private Sub ExpressCantFile_Calculation()
If GetBool(IAF1040.HOH) = True Then
        ReturnVal = 1
    ElseIf GetBool(IAF1040.QualWidow) = True Then
        ReturnVal = 1
    ElseIf GetBool(IAF126.SpPYNR) = True Then
        ReturnVal = 1
    ElseIf GetBool(IAF126.TpPYNR) = True Then
        ReturnVal = 1
    ElseIf GetBool(IAF1040.ItemCheck) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub NotQualifyEF_Calculation()
    If GetBool(IAWEFQual.QualifiesForEF) = True Then
        ReturnVal = 0
    Else
        ReturnVal = 1
    End If
End Sub

Private Sub Qual10_Calculation()
    'State now allows
    'If GetBool(USWResidency.F1040NR) = True Then
    '    ReturnVal = 1
    'Else
        ReturnVal = 0
    'End If
End Sub

Private Sub Qual20_Calculation()
    If GetCurrency(IAF1040.AGainDed) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IAF1040.BGainDed) <> 0 And GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Qual30_Calculation()
    Dim count As Integer
    Dim Lim As Integer
    Dim Total As Integer
    
    Lim = GetAllCopies(IACred)
    count = 1
    Total = 0
    
    Do While count <= Lim
        If GetBool(IACred.NonRefCr, count) = True And GetBool(IACred.Taxpayer, count) = True And GetString(IACred.Code, count) = "08" Then
            Total = Total + 1
        Else
            Total = Total
        End If
        
        count = count + 1
    Loop
    
    Dim count2 As Integer
    Dim Lim2 As Integer
    Dim Total2 As Integer
    
    Lim2 = GetAllCopies(IACred)
    count2 = 1
    Total2 = 0
    
    Do While count2 <= Lim2
        If GetBool(IACred.NonRefCr, count2) = True And GetBool(IACred.Spouse, count2) = True And GetString(IACred.Code, count2) = "08" Then
            Total2 = Total2 + 1
        Else
            Total2 = Total2
        End If
        
        count2 = count2 + 1
    Loop
    

    If Total <> 0 Then
        ReturnVal = 1
    ElseIf GetBool(IAF1040.CombMFS) = False Then
        ReturnVal = 0
    ElseIf Total2 <> 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Qual40_Calculation()
    ReturnVal = 0
End Sub

Private Sub Qual45_Calculation()
    Dim count As Integer
    Dim Lim As Integer
    Dim Total As Integer
    
    Lim = GetAllCopies(IACred)
    count = 1
    Total = 0
    
    Do While count <= Lim
        If GetBool(IACred.NonRefCr, count) = True And GetBool(IACred.Taxpayer, count) = True And GetString(IACred.Code, count) = "28" Then
            Total = Total + 1
        Else
            Total = Total
        End If
        
        count = count + 1
    Loop
    
    Dim count2 As Integer
    Dim Lim2 As Integer
    Dim Total2 As Integer
    
    Lim2 = GetAllCopies(IACred)
    count2 = 1
    Total2 = 0
    
    Do While count2 <= Lim2
        If GetBool(IACred.NonRefCr, count2) = True And GetBool(IACred.Spouse, count2) = True And GetString(IACred.Code, count2) = "28" Then
            Total2 = Total2 + 1
        Else
            Total2 = Total2
        End If
        
        count2 = count2 + 1
    Loop
    

    If Total <> 0 Then
        ReturnVal = 1
    ElseIf GetBool(IAF1040.CombMFS) = False Then
        ReturnVal = 0
    ElseIf Total2 <> 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Qual50_Calculation()
    If (GetCurrency(IA2210.Penalty) > 0) Or (GetCurrency(IA2210Sp.Penalty) > 0) Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub QualifiesForEF_Calculation()
    If IsPhone() = True Then
        If GetBool(IAWEFQual.Qual10) = True Or GetBool(IAWEFQual.Qual20) = True Or GetBool(IAWEFQual.Qual30) = True Or GetBool(IAWEFQual.Qual40) = True Or GetBool(IAWEFQual.Qual45) = True Or GetBool(IAWEFQual.Qual50) = True Then
            ReturnVal = 0
        Else
            ReturnVal = 1
        End If
    ElseIf GetBool(IAWEFQual.Qual10) = True Or GetBool(IAWEFQual.Qual20) = True Or GetBool(IAWEFQual.Qual30) = True Or GetBool(IAWEFQual.Qual40) = True Or GetBool(IAWEFQual.Qual45) = True Then
        ReturnVal = 0
    Else
        ReturnVal = 1
    End If
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.CombNames)
End Sub

Private Sub Reject10_Calculation()
    Dim SameRTN As Integer
    Dim SameDAN As Integer
    Dim SameType As Integer
    
    If GetString(USWRALApp.StateRTRTN) = GetString(IAEFWksht.DirDepRTN) Then
        SameRTN = 1
    Else
        SameRTN = 0
    End If
    
    If GetString(USWRALApp.StateRTDAN) = GetString(IAEFWksht.DirDepDan) Then
        SameDAN = 1
    Else
        SameDAN = 0
    End If
    
    If GetBool(USWRALApp.StRTCheck) = True And GetBool(IAEFWksht.DirDepChecking) = True Then
        SameType = 1
    ElseIf GetBool(USWRALApp.StRTSave) = True And GetBool(IAEFWksht.DirDepSavings) = True Then
        SameType = 1
    Else
        SameType = 0
    End If
    
    If GetBool(USWBankProd.IsStateRPT) = True And GetBool(IAEFWksht.IsStateRPT) = True And GetBool(USWRALApp.StateRTDD) = True Then
        If SameRTN + SameDAN + SameType <> 3 Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If

End Sub

Private Sub Reject20_Calculation()
    If GetBool(IAEFWksht.IsStateRPT) = True Then
        If GetBool(USWRALApp.StateRTDD) = True And GetBool(IAEFWksht.DirDeposit) = False Then
            ReturnVal = 1
        ElseIf GetBool(USWRALApp.StateRTDC) = True And GetBool(IAEFWksht.DebitCard) = False And GetBool(IAEFWksht.AskDebitCard) = True Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Reject50_Calculation()
    If GetBool(IAEFWksht.PrepBPTrans) = True Then    
        ReturnVal = 0
    ElseIf GetBool(IAEFWksht.DebitCard) = True And GetCurrency(IAEFWksht.Refund) > 0 Then
        ReturnVal = 0
    ElseIf GetNumber(IAEFWksht.EFDDCode) <> 0 Then
        If Trim(GetString(IAEFWksht.Acct)) = "" Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Reject60_Calculation()
    If GetNumber(IAEFWksht.EFDDCode) = 2 Then
        If GetYear(GetDate(IAEFWksht.EFWDate)) = YearNumber + 1 Then
            ReturnVal = 0
        Else
            ReturnVal = 1
        End If
    Else
        ReturnVal = 0
    End If
End Sub

