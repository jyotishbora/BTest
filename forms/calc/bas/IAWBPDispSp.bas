Private Sub Desc_Calculation()
    ReturnVal = GetString(IAWBPDispSp.Names)
End Sub

Private Sub DisAdj_Calculation(Index As Integer)
    ReturnVal = GetCurrency(IAWBPDispSp.DisIADep(Index)) - GetCurrency(IAWBPDispSp.DisFedDep(Index))
End Sub

Private Sub DisDTServ_Calculation(Index As Integer)
    Dim Stuff As Integer
    
    Stuff = Index + GetNumber(IAWBPDispSp.Offset)
    
    If GetNumber(IA4562Sp.StateDispNbr) > Stuff Then
        ReturnVal = GetString(IAWDepr.DateServ, GetNumber(IA4562Sp.StateDispCopyNbr(Stuff)))
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub DisDTSld_Calculation(Index As Integer)
    Dim Stuff As Integer
    
    Stuff = Index + GetNumber(IAWBPDispSp.Offset)
    
    If GetNumber(IA4562Sp.StateDispNbr) > Stuff Then
        ReturnVal = GetString(IAWDepr.DisDTSld, GetNumber(IA4562Sp.StateDispCopyNbr(Stuff)))
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub DisFedDep_Calculation(Index As Integer)
    Dim Stuff As Integer
    
    Stuff = Index + GetNumber(IAWBPDispSp.Offset)
    
    If GetNumber(IA4562Sp.StateDispNbr) > Stuff Then
        ReturnVal = GetCurrency(IAWDepr.SPDisFedDep, GetNumber(IA4562Sp.StateDispCopyNbr(Stuff)))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub DisIADep_Calculation(Index As Integer)
    Dim Stuff As Integer
    
    Stuff = Index + GetNumber(IAWBPDispSp.Offset)
    
    If GetNumber(IA4562Sp.StateDispNbr) > Stuff Then
        ReturnVal = GetCurrency(IAWDepr.SPDisIADep, GetNumber(IA4562Sp.StateDispCopyNbr(Stuff)))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub DisPropDesc_Calculation(Index As Integer)
    Dim Stuff As Integer
    
    Stuff = Index + GetNumber(IAWBPDispSp.Offset)
    
    If GetNumber(IA4562Sp.StateDispNbr) > Stuff Then
        ReturnVal = GetString(IAWDepr.PropDesc, GetNumber(IA4562Sp.StateDispCopyNbr(Stuff)))
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IA4562Sp.Names)
End Sub

Private Sub Offset_Calculation()
    If GetCopy() = 1 Then
        ReturnVal = 3
    ElseIf GetCopy() = 2 Then
        ReturnVal = 32
    ElseIf GetCopy() = 3 Then
        ReturnVal = 61
    ElseIf GetCopy() = 4 Then
        ReturnVal = 90
    ElseIf GetCopy() = 5 Then
        ReturnVal = 119
    ElseIf GetCopy() = 6 Then
        ReturnVal = 148
    ElseIf GetCopy() = 7 Then
        ReturnVal = 177
    ElseIf GetCopy() = 8 Then
        ReturnVal = 206
    ElseIf GetCopy() = 9 Then
        ReturnVal = 235
    ElseIf GetCopy() = 10 Then
        ReturnVal = 264
    ElseIf GetCopy() = 11 Then
        ReturnVal = 293
    ElseIf GetCopy() = 12 Then
        ReturnVal = 322
    ElseIf GetCopy() = 13 Then
        ReturnVal = 351
    ElseIf GetCopy() = 14 Then
        ReturnVal = 380
    ElseIf GetCopy() = 15 Then
        ReturnVal = 409
    ElseIf GetCopy() = 16 Then
        ReturnVal = 438
    ElseIf GetCopy() = 17 Then
        ReturnVal = 467
    ElseIf GetCopy() = 18 Then
        ReturnVal = 496
    ElseIf GetCopy() = 19 Then
        ReturnVal = 525
    Else
        ReturnVal = 554
    End If
End Sub

Private Sub PrWBPDisp_Calculation()
    If GetCurrency(IAWBPDispSp.TotDisAdj) <> 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IA4562Sp.SSN)
End Sub

Private Sub TotDisAdj_Calculation()
    Dim count As Integer
    Dim SubTot As Currency
    
    count = 0
    SubTot = 0
    
    Do While count < 29
        SubTot = SubTot + GetCurrency(IAWBPDispSp.DisAdj(count))
        count = count + 1
    Loop
    
    ReturnVal = SubTot
End Sub

Private Sub TotDisFedDep_Calculation()
    Dim count As Integer
    Dim SubTot As Currency
    
    count = 0
    SubTot = 0
    
    Do While count < 29
        SubTot = SubTot + GetCurrency(IAWBPDispSp.DisFedDep(count))
        count = count + 1
    Loop
    
    ReturnVal = SubTot
End Sub

Private Sub TotDisIADep_Calculation()
    Dim count As Integer
    Dim SubTot As Currency
    
    count = 0
    SubTot = 0
    
    Do While count < 29
        SubTot = SubTot + GetCurrency(IAWBPDispSp.DisIADep(count))
        count = count + 1
    Loop
    
    ReturnVal = SubTot
End Sub

