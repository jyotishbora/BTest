Private Sub AccFedDep_Calculation(Index As Integer)
    Dim Stuff As Integer
    
    Stuff = Index - GetNumber(IA4562PIV.SpCopy)
    
    If GetNumber(IA4562PIV.SpCopy) = 1 And Index = 0 Then
        ReturnVal = 0
    ElseIf GetNumber(IA4562Sp.DepSeeAttBool) = 1 And Index = 3 Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(IAWDepr.SPAccFedDep, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))
    End If
End Sub

Private Sub AccIADep_Calculation(Index As Integer)
    Dim Stuff As Integer
    
    Stuff = Index - GetNumber(IA4562PIV.SpCopy)
    
    If GetNumber(IA4562PIV.SpCopy) = 1 And Index = 0 Then
        ReturnVal = 0
    ElseIf GetNumber(IA4562Sp.DepSeeAttBool) = 1 And Index = 3 Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(IAWDepr.SPAccIADep, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))
    End If
End Sub

Private Sub Basis_Calculation(Index As Integer)
    Dim Stuff As Integer
    
    Stuff = Index - GetNumber(IA4562PIV.SpCopy)
    
    If GetNumber(IA4562PIV.SpCopy) = 1 And Index = 0 Then
        ReturnVal = 0
    ElseIf GetNumber(IA4562Sp.DepSeeAttBool) = 1 And Index = 3 Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(IAWDepr.SPBasis, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))
    End If
End Sub

Private Sub CrBPDep1_Calculation()
    If (GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy)) > 4 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDep10_Calculation()
    If (GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy)) > 264 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDep11_Calculation()
    If (GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy)) > 293 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDep12_Calculation()
    If (GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy)) > 322 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDep13_Calculation()
    If (GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy)) > 351 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDep14_Calculation()
    If (GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy)) > 380 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDep15_Calculation()
    If (GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy)) > 409 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDep16_Calculation()
    If (GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy)) > 438 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDep17_Calculation()
    If (GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy)) > 467 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDep18_Calculation()
    If (GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy)) > 496 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDep19_Calculation()
    If (GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy)) > 525 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDep2_Calculation()
    If (GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy)) > 32 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDep20_Calculation()
    If (GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy)) > 554 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDep3_Calculation()
    If (GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy)) > 61 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDep4_Calculation()
    If (GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy)) > 90 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDep5_Calculation()
    If (GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy)) > 119 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDep6_Calculation()
    If (GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy)) > 148 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDep7_Calculation()
    If (GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy)) > 177 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDep8_Calculation()
    If (GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy)) > 206 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDep9_Calculation()
    If (GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy)) > 235 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDisp1_Calculation()
    If GetNumber(IA4562Sp.StateDispNbr) > 4 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDisp10_Calculation()
    If GetNumber(IA4562Sp.StateDispNbr) > 264 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDisp11_Calculation()
    If GetNumber(IA4562Sp.StateDispNbr) > 293 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDisp12_Calculation()
    If GetNumber(IA4562Sp.StateDispNbr) > 322 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDisp13_Calculation()
    If GetNumber(IA4562Sp.StateDispNbr) > 351 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDisp14_Calculation()
    If GetNumber(IA4562Sp.StateDispNbr) > 380 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDisp15_Calculation()
    If GetNumber(IA4562Sp.StateDispNbr) > 409 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDisp16_Calculation()
    If GetNumber(IA4562Sp.StateDispNbr) > 438 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDisp17_Calculation()
    If GetNumber(IA4562Sp.StateDispNbr) > 467 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDisp18_Calculation()
    If GetNumber(IA4562Sp.StateDispNbr) > 496 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDisp19_Calculation()
    If GetNumber(IA4562Sp.StateDispNbr) > 525 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDisp2_Calculation()
    If GetNumber(IA4562Sp.StateDispNbr) > 32 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDisp20_Calculation()
    If GetNumber(IA4562Sp.StateDispNbr) > 554 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDisp3_Calculation()
    If GetNumber(IA4562Sp.StateDispNbr) > 61 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDisp4_Calculation()
    If GetNumber(IA4562Sp.StateDispNbr) > 90 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDisp5_Calculation()
    If GetNumber(IA4562Sp.StateDispNbr) > 119 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDisp6_Calculation()
    If GetNumber(IA4562Sp.StateDispNbr) > 148 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDisp7_Calculation()
    If GetNumber(IA4562Sp.StateDispNbr) > 177 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDisp8_Calculation()
    If GetNumber(IA4562Sp.StateDispNbr) > 206 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDisp9_Calculation()
    If GetNumber(IA4562Sp.StateDispNbr) > 235 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub DateServ_Calculation(Index As Integer)
    Dim Stuff As Integer
    
    Stuff = Index - GetNumber(IA4562PIV.SpCopy)
    
    If GetNumber(IA4562PIV.SpCopy) = 1 And Index = 0 Then
        ReturnVal = ""
    ElseIf GetNumber(IA4562Sp.DepSeeAttBool) = 1 And Index = 3 Then
        ReturnVal = ""
    Else
        ReturnVal = GetString(IAWDepr.DateServ, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))
    End If
End Sub

Private Sub DepAdj_Calculation()
    ReturnVal = GetCurrency(IA4562Sp.TotColF) - GetCurrency(IA4562Sp.TotColI)
End Sub

Private Sub DepSeeAttBool_Calculation()
    If (GetNumber(IA4562Sp.StateDeprNbr) + GetNumber(IA4562PIV.SpCopy)) > 4 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Desc_Calculation()
    Dim Total As Currency
    
    Total = GetCurrency(IA4562Sp.TotDepAdj)
    
    ReturnVal = CStr(Total) & " Adjustment"

End Sub

Private Sub DisAdj_Calculation(Index As Integer)
    If GetNumber(IA4562Sp.DisSeeAttBool) = 1 And Index = 3 Then
        ReturnVal = GetCurrency(IAWBPDispSp.TotDisAdj)
    Else
        ReturnVal = GetCurrency(IA4562Sp.DisIADep(Index)) - GetCurrency(IA4562Sp.DisFedDep(Index))
    End If
End Sub

Private Sub DisDTServ_Calculation(Index As Integer)
    If GetNumber(IA4562Sp.DisSeeAttBool) = 1 And Index = 3 Then
        ReturnVal = ""
    Else
        ReturnVal = GetString(IAWDepr.DateServ, GetNumber(IA4562Sp.StateDispCopyNbr(Index)))
    End If
End Sub

Private Sub DisDTSld_Calculation(Index As Integer)
    If GetNumber(IA4562Sp.DisSeeAttBool) = 1 And Index = 3 Then
        ReturnVal = ""
    Else
        ReturnVal = GetString(IAWDepr.DisDTSld, GetNumber(IA4562Sp.StateDispCopyNbr(Index)))
    End If
End Sub

Private Sub DisFedDep_Calculation(Index As Integer)
    If GetNumber(IA4562Sp.DisSeeAttBool) = 1 And Index = 3 Then
        ReturnVal = GetCurrency(IAWBPDispSp.TotDisFedDep)
    Else
        ReturnVal = GetCurrency(IAWDepr.SPDisFedDep, GetNumber(IA4562Sp.StateDispCopyNbr(Index)))
    End If
End Sub

Private Sub DisIADep_Calculation(Index As Integer)
    If GetNumber(IA4562Sp.DisSeeAttBool) = 1 And Index = 3 Then
        ReturnVal = GetCurrency(IAWBPDispSp.TotDisIADep)
    Else
        ReturnVal = GetCurrency(IAWDepr.SPDisIADep, GetNumber(IA4562Sp.StateDispCopyNbr(Index)))
    End If
End Sub

Private Sub DisPropDesc_Calculation(Index As Integer)
    If GetNumber(IA4562Sp.DisSeeAttBool) = 1 And Index = 3 Then
        ReturnVal = "See Stmt Att."
    Else
        ReturnVal = GetString(IAWDepr.PropDesc, GetNumber(IA4562Sp.StateDispCopyNbr(Index)))
    End If
End Sub

Private Sub DisSeeAttBool_Calculation()
    If GetNumber(IA4562Sp.StateDispNbr) > 4 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Fed179_Calculation(Index As Integer)
    Dim Stuff As Integer
    
    Stuff = Index - GetNumber(IA4562PIV.SpCopy)
    
    If GetNumber(IA4562PIV.SpCopy) = 1 And Index = 0 Then
        ReturnVal = GetCurrency(IA4562PIV.SPLine1)
    ElseIf GetNumber(IA4562Sp.DepSeeAttBool) = 1 And Index = 3 Then
        ReturnVal = GetCurrency(IAWBPDepSp.TotFed179)
    Else
        ReturnVal = GetCurrency(IAWDepr.SPFed179, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))
    End If
End Sub

Private Sub FedDepDed_Calculation(Index As Integer)
    Dim Stuff As Integer
    
    Stuff = Index - GetNumber(IA4562PIV.SpCopy)
    
    If GetNumber(IA4562PIV.SpCopy) = 1 And Index = 0 Then
        ReturnVal = 0
    ElseIf GetNumber(IA4562Sp.DepSeeAttBool) = 1 And Index = 3 Then
        ReturnVal = GetCurrency(IAWBPDepSp.TotFDD)
    Else
        ReturnVal = GetCurrency(IAWDepr.SPFedDepDed, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))
    End If
End Sub

Private Sub IA179_Calculation(Index As Integer)
    Dim Stuff As Integer
    
    Stuff = Index - GetNumber(IA4562PIV.SpCopy)
    
    If GetNumber(IA4562PIV.SpCopy) = 1 And Index = 0 Then
        ReturnVal = GetCurrency(IA4562PIV.SPPartIV179)
    ElseIf GetNumber(IA4562Sp.DepSeeAttBool) = 1 And Index = 3 Then
        ReturnVal = GetCurrency(IAWBPDepSp.TotIA179)
    Else
        ReturnVal = GetCurrency(IAWDepr.SPIA179, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))
    End If
End Sub

Private Sub Life_Calculation(Index As Integer)
    Dim Stuff As Integer
    
    Stuff = Index - GetNumber(IA4562PIV.SpCopy)
    
    If GetNumber(IA4562PIV.SpCopy) = 1 And Index = 0 Then
        ReturnVal = ""
    ElseIf GetNumber(IA4562Sp.DepSeeAttBool) = 1 And Index = 3 Then
        ReturnVal = ""
    Else
        ReturnVal = GetString(IAWDepr.Life, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))
    End If
End Sub

Private Sub MACRSIA_Calculation(Index As Integer)
    Dim Stuff As Integer
    
    Stuff = Index - GetNumber(IA4562PIV.SpCopy)
    
    If GetNumber(IA4562PIV.SpCopy) = 1 And Index = 0 Then
        ReturnVal = 0
    ElseIf GetNumber(IA4562Sp.DepSeeAttBool) = 1 And Index = 3 Then
        ReturnVal = GetCurrency(IAWBPDepSp.TotMACRS)
    Else
        ReturnVal = GetCurrency(IAWDepr.SPMACRSIA, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))
    End If
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.SPCombName)
End Sub

Private Sub PrIA4562_Calculation()
    If GetCurrency(IA4562Sp.TotFed179) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA4562Sp.TotFDD) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA4562Sp.TotIA179) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA4562Sp.TotMACRS) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA4562Sp.TotDisAdj) <> 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PropDesc_Calculation(Index As Integer)
    Dim Stuff As Integer
    
    Stuff = Index - GetNumber(IA4562PIV.SpCopy)
    
    If GetNumber(IA4562PIV.SpCopy) = 1 And Index = 0 Then
        ReturnVal = GetString(IA4562PIV.SPPropDescr)
    ElseIf GetNumber(IA4562Sp.DepSeeAttBool) = 1 And Index = 3 Then
        ReturnVal = "See Stmt Att."
    Else
        ReturnVal = GetString(IAWDepr.PropDesc, GetNumber(IA4562Sp.StateDeprCopyNbr(Stuff)))
    End If
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SpouseSSN)
End Sub

Private Sub StateDeprCopyNbr_Calculation(Index As Integer)
    Dim count As Long
    Dim max As Long
    Dim listedcount As Long
    
    listedcount = 0
    max = GetAllCopies(IAWDepr)
    count = 0
    
    Do While count < max
        count = count + 1
        If GetBool(IAWDepr.SpCopy, count) = True Then
            If listedcount = Index Then
                ReturnVal = count
            Else
                listedcount = listedcount + 1
            End If
        End If
    Loop
    
    ReturnVal = 0
    
End Sub

Private Sub StateDeprNbr_Calculation()
    Dim count As Integer
    Dim Lim As Integer
    Dim Total As Integer
    
    Lim = GetAllCopies(IAWDepr)
    count = 1
    Total = 0
    
    Do While count <= Lim
        If GetBool(IAWDepr.SpCopy, count) = True Then
            Total = Total + 1
        Else
            Total = Total
        End If
        
        count = count + 1
    Loop
    
    ReturnVal = Total
End Sub

Private Sub StateDispCopyNbr_Calculation(Index As Integer)
    Dim count As Long
    Dim max As Long
    Dim listedcount As Long
    
    listedcount = 0
    max = GetAllCopies(IAWDepr)
    count = 0
    
    Do While count < max
        count = count + 1
        If GetBool(IAWDepr.SpCopyDisp, count) = True Then
            If listedcount = Index Then
                ReturnVal = count
            Else
                listedcount = listedcount + 1
            End If
        End If
    Loop
    
    ReturnVal = 0

End Sub

Private Sub StateDispNbr_Calculation()
    Dim count As Integer
    Dim Lim As Integer
    Dim Total As Integer
    
    Lim = GetAllCopies(IAWDepr)
    count = 1
    Total = 0
    
    Do While count <= Lim
        If GetBool(IAWDepr.SpCopyDisp, count) = True Then
            Total = Total + 1
        Else
            Total = Total
        End If
        
        count = count + 1
    Loop
    
    ReturnVal = Total
    
End Sub

Private Sub TotColF_Calculation()
    ReturnVal = GetCurrency(IA4562Sp.TotFed179) + GetCurrency(IA4562Sp.TotFDD)
End Sub

Private Sub TotFed179_Calculation()
    Dim count As Integer
    Dim SubTot As Currency

    count = 0
    SubTot = 0

    Do While count < 4
        SubTot = SubTot + GetCurrency(IA4562Sp.Fed179(count))
        count = count + 1
    Loop
    
    ReturnVal = SubTot

End Sub

Private Sub TotIA179_Calculation()
    Dim count As Integer
    Dim SubTot As Currency

    count = 0
    SubTot = 0

    Do While count < 4
        SubTot = SubTot + GetCurrency(IA4562Sp.IA179(count))
        count = count + 1
    Loop
    
    ReturnVal = SubTot

End Sub

Private Sub TotP2ColF_Calculation()
    ReturnVal = GetCurrency(IA4562Sp.TotDisAdj)
End Sub

Private Sub TotColI_Calculation()
    ReturnVal = GetCurrency(IA4562Sp.TotIA179) + GetCurrency(IA4562Sp.TotMACRS)
End Sub

Private Sub TotDepAdj_Calculation()
    ReturnVal = GetCurrency(IA4562Sp.DepAdj) + GetCurrency(IA4562Sp.TotP2ColF)
End Sub

Private Sub TotDisAdj_Calculation()
    Dim count As Integer
    Dim SubTot As Currency

    count = 0
    SubTot = 0

    Do While count < 4
        SubTot = SubTot + GetCurrency(IA4562Sp.DisAdj(count))
        count = count + 1
    Loop
    
    ReturnVal = SubTot

End Sub

Private Sub TotDisFedDep_Calculation()
    Dim count As Integer
    Dim SubTot As Currency

    count = 0
    SubTot = 0

    Do While count < 4
        SubTot = SubTot + GetCurrency(IA4562Sp.DisFedDep(count))
        count = count + 1
    Loop
    
    ReturnVal = SubTot
    
End Sub

Private Sub TotDisIADep_Calculation()
    Dim count As Integer
    Dim SubTot As Currency

    count = 0
    SubTot = 0

    Do While count < 4
        SubTot = SubTot + GetCurrency(IA4562Sp.DisIADep(count))
        count = count + 1
    Loop
    
    ReturnVal = SubTot
    
End Sub

Private Sub TotFDD_Calculation()
    Dim count As Integer
    Dim SubTot As Currency

    count = 0
    SubTot = 0

    Do While count < 4
        SubTot = SubTot + GetCurrency(IA4562Sp.FedDepDed(count))
        count = count + 1
    Loop
    
    ReturnVal = SubTot

End Sub

Private Sub TotMACRS_Calculation()
    Dim count As Integer
    Dim SubTot As Currency

    count = 0
    SubTot = 0

    Do While count < 4
        SubTot = SubTot + GetCurrency(IA4562Sp.MACRSIA(count))
        count = count + 1
    Loop
    
    ReturnVal = SubTot

End Sub

