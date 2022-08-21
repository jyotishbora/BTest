Private Sub Credit_Calculation(Index As Integer)
    If Trim(GetString(IATuition.DepName(Index))) <> "" Then
        ReturnVal = CDollar(CDbl(MinValue(GetCurrency(IATuition.Expenses(Index)), 1000@)) * 0.25)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub DepName_Calculation(Index As Integer)
    Dim count As Integer
    Dim Hold As String
    count = 0
    Hold = ""
    
  
    If GetNumber(IAAddDep.FDepAge(0)) > 0 And GetNumber(IAAddDep.FDepAge(0)) < 20 Then
        If Index = count Then
            Hold = GetString(IAAddDep.FDepName(0)) + " " + GetString(IAAddDep.FDepLast(0))
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetNumber(IAAddDep.FDepAge(1)) > 0 And GetNumber(IAAddDep.FDepAge(1)) < 20 Then
        If Index = count Then
            Hold = GetString(IAAddDep.FDepName(1)) + " " + GetString(IAAddDep.FDepLast(1))
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetNumber(IAAddDep.FDepAge(2)) > 0 And GetNumber(IAAddDep.FDepAge(2)) < 20 Then
        If Index = count Then
            Hold = GetString(IAAddDep.FDepName(2)) + " " + GetString(IAAddDep.FDepLast(2))
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetNumber(IAAddDep.FDepAge(3)) > 0 And GetNumber(IAAddDep.FDepAge(3)) < 20 Then
        If Index = count Then
            Hold = GetString(IAAddDep.FDepName(3)) + " " + GetString(IAAddDep.FDepLast(3))
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetNumber(IAAddDep.FDepAge(4)) > 0 And GetNumber(IAAddDep.FDepAge(4)) < 20 Then
        If Index = count Then
            Hold = GetString(IAAddDep.FDepName(4)) + " " + GetString(IAAddDep.FDepLast(4))
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetNumber(IAAddDep.FDepAge(5)) > 0 And GetNumber(IAAddDep.FDepAge(5)) < 20 Then
        If Index = count Then
            Hold = GetString(IAAddDep.FDepName(5)) + " " + GetString(IAAddDep.FDepLast(5))
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetNumber(IAAddDep.FDepAge(6)) > 0 And GetNumber(IAAddDep.FDepAge(6)) < 20 Then
        If Index = count Then
            Hold = GetString(IAAddDep.FDepName(6)) + " " + GetString(IAAddDep.FDepLast(6))
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetNumber(IAAddDep.FDepAge(7)) > 0 And GetNumber(IAAddDep.FDepAge(7)) < 20 Then
        If Index = count Then
            Hold = GetString(IAAddDep.FDepName(7)) + " " + GetString(IAAddDep.FDepLast(7))
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetNumber(IAAddDep.FDepAge(8)) > 0 And GetNumber(IAAddDep.FDepAge(8)) < 20 Then
        If Index = count Then
            Hold = GetString(IAAddDep.FDepName(8)) + " " + GetString(IAAddDep.FDepLast(8))
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetNumber(IAAddDep.FDepAge(9)) > 0 And GetNumber(IAAddDep.FDepAge(9)) < 20 Then
        If Index = count Then
            Hold = GetString(IAAddDep.FDepName(9)) + " " + GetString(IAAddDep.FDepLast(9))
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetNumber(IAAddDep.FDepAge(10)) > 0 And GetNumber(IAAddDep.FDepAge(10)) < 20 Then
        If Index = count Then
            Hold = GetString(IAAddDep.FDepName(10)) + " " + GetString(IAAddDep.FDepLast(10))
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetNumber(IAAddDep.FDepAge(11)) > 0 And GetNumber(IAAddDep.FDepAge(11)) < 20 Then
        If Index = count Then
            Hold = GetString(IAAddDep.FDepName(11)) + " " + GetString(IAAddDep.FDepLast(11))
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetNumber(IAAddDep.FDepAge(12)) > 0 And GetNumber(IAAddDep.FDepAge(12)) < 20 Then
        If Index = count Then
            Hold = GetString(IAAddDep.FDepName(12)) + " " + GetString(IAAddDep.FDepLast(12))
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetNumber(IAAddDep.FDepAge(13)) > 0 And GetNumber(IAAddDep.FDepAge(13)) < 20 Then
        If Index = count Then
            Hold = GetString(IAAddDep.FDepName(13)) + " " + GetString(IAAddDep.FDepLast(13))
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetNumber(IAAddDep.FDepAge(14)) > 0 And GetNumber(IAAddDep.FDepAge(14)) < 20 Then
        If Index = count Then
            Hold = GetString(IAAddDep.FDepName(14)) + " " + GetString(IAAddDep.FDepLast(14))
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    ReturnVal = Hold
End Sub

Private Sub Description_Calculation()
    ReturnVal = CStr(GetCurrency(IATuition.TotCR))
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.CombNames)
End Sub

Private Sub Spouse_Calculation(Index As Integer)
    If Trim(GetString(IATuition.DepName(Index))) <> "" Then
        If GetBool(IAF1040.CombMFS) = False Then
            ReturnVal = 0
        ElseIf GetNumber(IAF1040.DC2) = 0 Then
            ReturnVal = 0
        ElseIf GetNumber(IAF1040.DC2) > Index Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

Private Sub STuit_Calculation()
    Dim count As Integer
    Dim SubTot As Currency

    count = 0
    SubTot = 0

    Do While count < 15
        If GetBool(IATuition.Spouse(count)) = True Then
            SubTot = SubTot + GetCurrency(IATuition.Credit(count))
        Else
            SubTot = SubTot
        End If
        count = count + 1
    Loop
    
    If GetBool(IAF1040.CombMFS) = True And GetNumber(IAF1040.DC2) > 0 Then
        ReturnVal = SubTot
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Taxpayer_Calculation(Index As Integer)
    If Trim(GetString(IATuition.DepName(Index))) <> "" And GetBool(IATuition.Spouse(Index)) = False Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TotCR_Calculation()
    Dim count As Integer
    Dim SubTot As Currency

    count = 0
    SubTot = 0

    Do While count < 15
        SubTot = SubTot + GetCurrency(IATuition.Credit(count))
        count = count + 1
    Loop
    
    ReturnVal = SubTot
    
End Sub

Private Sub TotExp_Calculation()
    Dim count As Integer
    Dim SubTot As Currency

    count = 0
    SubTot = 0

    Do While count < 15
        SubTot = SubTot + GetCurrency(IATuition.Expenses(count))
        count = count + 1
    Loop
    
    ReturnVal = SubTot
    
End Sub

Private Sub TTuit_Calculation()
    ReturnVal = GetCurrency(IATuition.TotCR) - GetCurrency(IATuition.STuit)
End Sub

