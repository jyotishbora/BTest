Private Sub AccFedDep_Calculation(Index As Integer)
    Dim Stuff As Integer
    
    Stuff = Index + GetNumber(IAWBPDepSp.Offset)
    
    If GetNumber(IA4562Sp.DepSeeAttBool) = 0 Then
        ReturnVal = 0
    ElseIf GetNumber(IA4562Sp.StateDeprNbr) > Stuff Then
        ReturnVal = GetCurrency(IAWDepr.SPAccFedDep, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AccIADep_Calculation(Index As Integer)
    Dim Stuff As Integer
    
    Stuff = Index + GetNumber(IAWBPDepSp.Offset)
    
    If GetNumber(IA4562Sp.DepSeeAttBool) = 0 Then
        ReturnVal = 0
    ElseIf GetNumber(IA4562Sp.StateDeprNbr) > Stuff Then
        ReturnVal = GetCurrency(IAWDepr.SPAccIADep, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Basis_Calculation(Index As Integer)
    Dim Stuff As Integer
    
    Stuff = Index + GetNumber(IAWBPDepSp.Offset)
    
    If GetNumber(IA4562Sp.DepSeeAttBool) = 0 Then
        ReturnVal = 0
    ElseIf GetNumber(IA4562Sp.StateDeprNbr) > Stuff Then
        ReturnVal = GetCurrency(IAWDepr.SPBasis, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub DateServ_Calculation(Index As Integer)
    Dim Stuff As Integer
    
    Stuff = Index + GetNumber(IAWBPDepSp.Offset)
    
    If GetNumber(IA4562Sp.DepSeeAttBool) = 0 Then
        ReturnVal = ""
    ElseIf GetNumber(IA4562Sp.StateDeprNbr) > Stuff Then
        ReturnVal = GetString(IAWDepr.DateServ, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub Desc_Calculation()
    ReturnVal = GetString(IAWBPDepSp.Names)
End Sub

Private Sub Fed179_Calculation(Index As Integer)
    Dim Stuff As Integer
    
    Stuff = Index + GetNumber(IAWBPDepSp.Offset)
    
    If GetNumber(IA4562Sp.DepSeeAttBool) = 0 Then
        ReturnVal = 0
    ElseIf GetNumber(IA4562Sp.StateDeprNbr) > Stuff Then
        ReturnVal = GetCurrency(IAWDepr.SPFed179, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub FedDepDed_Calculation(Index As Integer)
    Dim Stuff As Integer
    
    Stuff = Index + GetNumber(IAWBPDepSp.Offset)
    
    If GetNumber(IA4562Sp.DepSeeAttBool) = 0 Then
        ReturnVal = 0
    ElseIf GetNumber(IA4562Sp.StateDeprNbr) > Stuff Then
        ReturnVal = GetCurrency(IAWDepr.SPFedDepDed, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub IA179_Calculation(Index As Integer)
    Dim Stuff As Integer
    
    Stuff = Index + GetNumber(IAWBPDepSp.Offset)
    
    If GetNumber(IA4562Sp.DepSeeAttBool) = 0 Then
        ReturnVal = 0
    ElseIf GetNumber(IA4562Sp.StateDeprNbr) > Stuff Then
        ReturnVal = GetCurrency(IAWDepr.SPIA179, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Life_Calculation(Index As Integer)
    Dim Stuff As Integer
    
    Stuff = Index + GetNumber(IAWBPDepSp.Offset)
    
    If GetNumber(IA4562Sp.DepSeeAttBool) = 0 Then
        ReturnVal = ""
    ElseIf GetNumber(IA4562Sp.StateDeprNbr) > Stuff Then
        ReturnVal = GetString(IAWDepr.Life, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub MACRSIA_Calculation(Index As Integer)
    Dim Stuff As Integer
    
    Stuff = Index + GetNumber(IAWBPDepSp.Offset)
    
    If GetNumber(IA4562Sp.DepSeeAttBool) = 0 Then
        ReturnVal = 0
    ElseIf GetNumber(IA4562Sp.StateDeprNbr) > Stuff Then
        ReturnVal = GetCurrency(IAWDepr.SPMACRSIA, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IA4562Sp.Names)
End Sub

Private Sub Offset_Calculation()
    If GetCopy() = 1 Then
        ReturnVal = 3 - GetNumber(IA4562PIV.SpCopy)
    ElseIf GetCopy() = 2 Then
        ReturnVal = 32 - GetNumber(IA4562PIV.SpCopy)
    ElseIf GetCopy() = 3 Then
        ReturnVal = 61 - GetNumber(IA4562PIV.SpCopy)
    ElseIf GetCopy() = 4 Then
        ReturnVal = 90 - GetNumber(IA4562PIV.SpCopy)
    ElseIf GetCopy() = 5 Then
        ReturnVal = 119 - GetNumber(IA4562PIV.SpCopy)
    ElseIf GetCopy() = 6 Then
        ReturnVal = 148 - GetNumber(IA4562PIV.SpCopy)
    ElseIf GetCopy() = 7 Then
        ReturnVal = 177 - GetNumber(IA4562PIV.SpCopy)
    ElseIf GetCopy() = 8 Then
        ReturnVal = 206 - GetNumber(IA4562PIV.SpCopy)
    ElseIf GetCopy() = 9 Then
        ReturnVal = 235 - GetNumber(IA4562PIV.SpCopy)
    ElseIf GetCopy() = 10 Then
        ReturnVal = 264 - GetNumber(IA4562PIV.SpCopy)
    ElseIf GetCopy() = 11 Then
        ReturnVal = 293 - GetNumber(IA4562PIV.SpCopy)
    ElseIf GetCopy() = 12 Then
        ReturnVal = 322 - GetNumber(IA4562PIV.SpCopy)
    ElseIf GetCopy() = 13 Then
        ReturnVal = 351 - GetNumber(IA4562PIV.SpCopy)
    ElseIf GetCopy() = 14 Then
        ReturnVal = 380 - GetNumber(IA4562PIV.SpCopy)
    ElseIf GetCopy() = 15 Then
        ReturnVal = 409 - GetNumber(IA4562PIV.SpCopy)
    ElseIf GetCopy() = 16 Then
        ReturnVal = 438 - GetNumber(IA4562PIV.SpCopy)
    ElseIf GetCopy() = 17 Then
        ReturnVal = 467 - GetNumber(IA4562PIV.SpCopy)
    ElseIf GetCopy() = 18 Then
        ReturnVal = 496 - GetNumber(IA4562PIV.SpCopy)
    ElseIf GetCopy() = 19 Then
        ReturnVal = 525 - GetNumber(IA4562PIV.SpCopy)
    Else
        ReturnVal = 554 - GetNumber(IA4562PIV.SpCopy)
    End If
End Sub

Private Sub PropDesc_Calculation(Index As Integer)
    Dim Stuff As Integer
    
    Stuff = Index + GetNumber(IAWBPDepSp.Offset)
    
    If GetNumber(IA4562Sp.DepSeeAttBool) = 0 Then
        ReturnVal = ""
    ElseIf GetNumber(IA4562Sp.StateDeprNbr) > Stuff Then
        ReturnVal = GetString(IAWDepr.PropDesc, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub PrWBPDep_Calculation()
    If GetCurrency(IAWBPDepSp.TotFed179) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IAWBPDepSp.TotFDD) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IAWBPDepSp.TotIA179) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IAWBPDepSp.TotMACRS) <> 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IA4562Sp.SSN)
End Sub

Private Sub TotFDD_Calculation()
    Dim count As Integer
    Dim SubTot As Currency
    
    count = 0
    SubTot = 0
    
    Do While count < 29
        SubTot = SubTot + GetCurrency(IAWBPDepSp.FedDepDed(count))
        count = count + 1
    Loop
    
    ReturnVal = SubTot
End Sub

Private Sub TotFed179_Calculation()
    Dim count As Integer
    Dim SubTot As Currency
    
    count = 0
    SubTot = 0
    
    Do While count < 29
        SubTot = SubTot + GetCurrency(IAWBPDepSp.Fed179(count))
        count = count + 1
    Loop
    
    ReturnVal = SubTot
End Sub

Private Sub TotIA179_Calculation()
    Dim count As Integer
    Dim SubTot As Currency
    
    count = 0
    SubTot = 0
    
    Do While count < 29
        SubTot = SubTot + GetCurrency(IAWBPDepSp.IA179(count))
        count = count + 1
    Loop
    
    ReturnVal = SubTot
End Sub

Private Sub TotMACRS_Calculation()
    Dim count As Integer
    Dim SubTot As Currency
    
    count = 0
    SubTot = 0
    
    Do While count < 29
        SubTot = SubTot + GetCurrency(IAWBPDepSp.MACRSIA(count))
        count = count + 1
    Loop
    
    ReturnVal = SubTot
End Sub

