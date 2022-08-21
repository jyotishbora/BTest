Private Sub AccFedDep_Calculation(Index As Integer)
    Dim Stuff As Long
    
    Stuff = GetNumber(IA4562A.StateDeprCopyNbr(Index))
    
    If GetNumber(IA4562A.StateDeprNbr) > Index Then
        ReturnVal = GetCurrency(USW2106Veh.AccumFed, Stuff)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AccIADep_Calculation(Index As Integer)
'will need to review next year to make sure prior depr brings forward the limitied IA lux limits
    Dim Stuff As Long
    
    Stuff = GetNumber(IA4562A.StateDeprCopyNbr(Index))
    
    If GetNumber(IA4562A.StateDeprNbr) > Index Then
        If GetBool(USW2106Veh.New, Stuff) = True Then
            If GetCurrency(USW2106Veh.LuxLimState2, Stuff) = 0 And GetCurrency(USW2106Veh.PerLimState2, Stuff) = 0 Then
                ReturnVal = GetCurrency(USW2106Veh.AccumState, Stuff)
            Else
                ReturnVal = GetCurrency(USW2106Veh.PriorState) + MinValue(GetCurrency(USW2106Veh.DeprNoBonus), GetCurrency(USW2106Veh.PerLimState2, Stuff))
            End If
        Else
            ReturnVal = GetCurrency(USW2106Veh.AccumState, Stuff)
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Basis_Calculation(Index As Integer)
    Dim Stuff As Long
    
    Stuff = GetNumber(IA4562A.StateDeprCopyNbr(Index))
    
    If GetNumber(IA4562A.StateDeprNbr) > Index Then
        ReturnVal = GetCurrency(USW2106Veh.Basis, Stuff)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub DateServ_Calculation(Index As Integer)
    Dim Stuff As Long
    
    Stuff = GetNumber(IA4562A.StateDeprCopyNbr(Index))
    
    If GetNumber(IA4562A.StateDeprNbr) > Index Then
        ReturnVal = GetString(USW2106Veh.Date, Stuff)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub DepAdj_Calculation()
    ReturnVal = GetCurrency(IA4562A.TotColF) - GetCurrency(IA4562A.TotColI)
End Sub

Private Sub Desc_Calculation()
    ReturnVal = GetString(USF2106.Desc, ParentCopy())
End Sub

Private Sub DisAdj_Calculation(Index As Integer)
    ReturnVal = GetCurrency(IA4562A.DisIADep(Index)) - GetCurrency(IA4562A.DisFedDep(Index))
End Sub

Private Sub EFSP_Calculation()
    If GetBool(IA4562A.PrIA4562A) = True Then
        If GetBool(IAF1040.CombMFS) = False Then
            ReturnVal = 0
        ElseIf GetBool(IA4562A.Spouse) = True Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub EFSPDisp_Calculation()
    If GetBool(IA4562A.PrIA4562A) = True And GetCurrency(IA4562A.TotDisAdj) <> 0 Then
        If GetBool(IAF1040.CombMFS) = False Then
            ReturnVal = 0
        ElseIf GetBool(IA4562A.Spouse) = True Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub EFTPJoint_Calculation()
    If GetBool(IA4562A.PrIA4562A) = True Then
        If GetBool(IAF1040.CombMFS) = False Then
            ReturnVal = 1
        ElseIf GetBool(IA4562A.Taxpayer) = True Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub EFTPJointDisp_Calculation()
    If GetBool(IA4562A.PrIA4562A) = True And GetCurrency(IA4562A.TotDisAdj) <> 0 Then
        If GetBool(IAF1040.CombMFS) = False Then
            ReturnVal = 1
        ElseIf GetBool(IA4562A.Taxpayer) = True Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub EmpBusType_Calculation()
    If GetBool(USF2106.QPA, ParentCopy()) = True Or GetBool(USF2106.FBO, ParentCopy()) = True Or GetBool(USF2106.NatG, ParentCopy()) = True Then
        ReturnVal = "1040"
    ElseIf GetBool(USF2106.Disable, ParentCopy()) = True Then
        ReturnVal = "27"
    Else
        ReturnVal = "20"
    End If
End Sub

Private Sub Exist_Calculation()
    ReturnVal = 1
End Sub

Private Sub Fed179_Calculation(Index As Integer)
    Dim Stuff As Long
    
    Stuff = GetNumber(IA4562A.StateDeprCopyNbr(Index))
    
    If GetNumber(IA4562A.StateDeprNbr) > Index Then
        If GetBool(USW2106Veh.New, Stuff) = True Then
            ReturnVal = GetCurrency(USW2106Veh.Sec179Calc, Stuff)
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub FedDepDed_Calculation(Index As Integer)
    Dim Stuff As Long
    
    Stuff = GetNumber(IA4562A.StateDeprCopyNbr(Index))
    
    If GetNumber(IA4562A.StateDeprNbr) > Index Then
        If GetBool(USW2106Veh.New, Stuff) = True Then
            ReturnVal = GetCurrency(USW2106Veh.Bonus, Stuff) + MaxValue(0, GetCurrency(USW2106Veh.TotDepr, Stuff) - GetCurrency(USW2106Veh.Sec179, Stuff) - GetCurrency(USW2106Veh.Bonus, Stuff))
        Else
            ReturnVal = GetCurrency(USW2106Veh.TotDepr, Stuff)
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub IA179_Calculation(Index As Integer)
' Iowa not yet coupled with increased Section 179 expensing for 2017
    
    Dim Stuff As Long
    
    Stuff = GetNumber(IA4562A.StateDeprCopyNbr(Index))
    
    If GetNumber(IA4562A.StateDeprNbr) > Index Then
        If GetBool(USW2106Veh.New, Stuff) = True Then
            If GetCurrency(USW2106Veh.LuxLimState2, Stuff) = 0 And GetCurrency(USW2106Veh.PerLimState2, Stuff) = 0 Then
                ReturnVal = GetCurrency(USW2106Veh.StateSec179Calc, Stuff)
            Else
                ReturnVal = MinValue(GetCurrency(USW2106Veh.StateSec179Calc, Stuff), GetCurrency(USW2106Veh.PerLimState2, Stuff))
            End If
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Life_Calculation(Index As Integer)
    If GetString(IA4562A.DateServ(Index)) <> "" Then
        ReturnVal = "5"
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub MACRSIA_Calculation(Index As Integer)
'will need to review this next year for the state basis brought forward when hit the lower IA lux limits, will .DeprNoBonus still be valid
    Dim Stuff As Long
    
    Stuff = GetNumber(IA4562A.StateDeprCopyNbr(Index))
    
    If GetNumber(IA4562A.StateDeprNbr) > Index Then
        If GetBool(USW2106Veh.New, Stuff) = True Then
            If GetCurrency(USW2106Veh.LuxLimState2, Stuff) = 0 And GetCurrency(USW2106Veh.PerLimState2, Stuff) = 0 Then
                ReturnVal = MaxValue(0, GetCurrency(USW2106Veh.DeprNoBonus, Stuff) - GetCurrency(USW2106Veh.StateSec179, Stuff))
            Else
                ReturnVal = MaxValue(0, MinValue(GetCurrency(USW2106Veh.DeprNoBonus, Stuff), GetCurrency(USW2106Veh.PerLimState2, Stuff)) - GetCurrency(IA4562A.IA179(Index)))
            End If
        Else
            ReturnVal = GetCurrency(USW2106Veh.DeprNoBonus, Stuff)
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(USF2106.FirstName, ParentCopy())
End Sub

Private Sub Owner_Calculation()
    If GetBool(IA4562A.Taxpayer) = True And Trim(GetString(USWBasicInfo.FirstName)) = "" Then
        ReturnVal = "the taxpayer"
    ElseIf GetBool(IA4562A.Taxpayer) = True Then
        ReturnVal = GetString(USWBasicInfo.FirstName)
    ElseIf GetBool(IA4562A.Spouse) = True And Trim(GetString(USWBasicInfo.SpouseFirst)) = "" Then
        ReturnVal = "the spouse"
    Else
        ReturnVal = GetString(USWBasicInfo.SpouseFirst)
    End If
End Sub

Private Sub PrIA4562A_Calculation()
    If GetCurrency(IA4562A.TotFed179) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA4562A.TotFDD) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA4562A.TotIA179) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA4562A.TotMACRS) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA4562A.TotDisAdj) <> 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PropDesc_Calculation(Index As Integer)
    Dim Stuff As Long
    
    Stuff = GetNumber(IA4562A.StateDeprCopyNbr(Index))
    
    If GetNumber(IA4562A.StateDeprNbr) > Index Then
        ReturnVal = GetString(USW2106Veh.Occupation, Stuff) & " Vehicle"
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub Spouse_Calculation()
    If GetBool(USF2106.Spouse, ParentCopy()) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(USF2106.SSN, ParentCopy())
End Sub

Private Sub StateDeprCopyNbr_Calculation(Index As Integer)
    Dim F2106 As Long
    Dim DeprCount As Long
    Dim MaxDepr As Long
    Dim listedcount As Long
    
    F2106 = GetParentCopy(USF2106)
    listedcount = 0
    MaxDepr = GetAllCopies(USW2106Veh)
    DeprCount = 0
    
    Do While DeprCount < MaxDepr
        DeprCount = DeprCount + 1
        If GetParentCopy(USF2106, USW2106Veh, DeprCount) = F2106 Then
            If (GetBool(USW2106Veh.BonusYes, DeprCount) = True Or GetBool(USW2106Veh.IAFedStSec179, DeprCount) = True Or GetBool(USW2106Veh.IAUsingLuxLim, DeprCount) = True) And GetBool(USW2106Veh.Qualifies, DeprCount) = True Then
                If (GetDate(USW2106Veh.Date, DeprCount) > #9/10/2001# And GetDate(USW2106Veh.Date, DeprCount) < #5/6/2003#) Or (GetDate(USW2106Veh.Date, DeprCount) > #12/31/2007# And GetDate(USW2106Veh.Date, DeprCount) < MakeDate(1, 1, YearNumber + 1)) Then
                    If listedcount = Index Then
                        ReturnVal = DeprCount
                    Else
                        listedcount = listedcount + 1
                    End If
                End If
            End If
        End If
    Loop
    
    ReturnVal = 0
    
End Sub

Private Sub StateDeprNbr_Calculation()
    Dim DeprCount As Long
    Dim F2106 As Long
    Dim MaxDepr As Long
    Dim Total As Integer
    
    DeprCount = 1
    F2106 = GetParentCopy(USF2106)
    MaxDepr = GetAllCopies(USW2106Veh)
    Total = 0
    
    Do While DeprCount <= MaxDepr
        If GetParentCopy(USF2106, USW2106Veh, DeprCount) = F2106 Then
            If (GetBool(USW2106Veh.BonusYes, DeprCount) = True Or GetBool(USW2106Veh.IAFedStSec179, DeprCount) = True Or GetBool(USW2106Veh.IAUsingLuxLim, DeprCount) = True) And GetBool(USW2106Veh.Qualifies, DeprCount) = True Then
                If (GetDate(USW2106Veh.Date, DeprCount) > #9/10/2001# And GetDate(USW2106Veh.Date, DeprCount) < #5/6/2003#) Or (GetDate(USW2106Veh.Date, DeprCount) > #12/31/2007# And GetDate(USW2106Veh.Date, DeprCount) < MakeDate(1, 1, YearNumber + 1)) Then
                    Total = Total + 1
                Else
                    Total = Total
                End If
            End If
        End If
    
    DeprCount = DeprCount + 1
    Loop
        
    ReturnVal = Total

End Sub

Private Sub StateDispNbr_Calculation()
'for 2018 make no change since need to ask or alert if had depr adjustment in prior year and need to make and entry for catch-up depr. May need to see next year if should exclude 2018 veh that were not reported on IA4562A since was just on IA 2106
    Dim DeprCount As Long
    Dim F2106 As Long
    Dim MaxDepr As Long
    Dim Total As Integer
    
    DeprCount = 1
    F2106 = GetParentCopy(USF2106)
    MaxDepr = GetAllCopies(USW2106Veh)
    Total = 0
    
    Do While DeprCount <= MaxDepr
        If GetParentCopy(USF2106, USW2106Veh, DeprCount) = F2106 Then
            If GetBool(USW2106Veh.BonusYes, DeprCount) = True And GetString(USW2106Veh.DisposeDate, DeprCount) <> "" And ((GetDate(USW2106Veh.Date, DeprCount) > #9/10/2001# And GetDate(USW2106Veh.Date, DeprCount) < #5/6/2003#) Or (GetDate(USW2106Veh.Date, DeprCount) > #12/31/2007# And GetDate(USW2106Veh.Date, DeprCount) < MakeDate(1, 1, YearNumber + 1))) Then
                Total = Total + 1
            Else
                Total = Total
            End If
        End If
    
    DeprCount = DeprCount + 1
    Loop
    
    ReturnVal = Total
    
End Sub

Private Sub Taxpayer_Calculation()
    If GetBool(USF2106.Taxpayer, ParentCopy()) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TotColF_Calculation()
    ReturnVal = GetCurrency(IA4562A.TotFed179) + GetCurrency(IA4562A.TotFDD)
End Sub

Private Sub TotFed179_Calculation()
    ReturnVal = GetCurrency(IA4562A.Fed179(0)) + GetCurrency(IA4562A.Fed179(1)) + GetCurrency(IA4562A.Fed179(2)) + GetCurrency(IA4562A.Fed179(3))
End Sub

Private Sub TotIA179_Calculation()
    ReturnVal = GetCurrency(IA4562A.IA179(0)) + GetCurrency(IA4562A.IA179(1)) + GetCurrency(IA4562A.IA179(2)) + GetCurrency(IA4562A.IA179(3))
End Sub

Private Sub TotP2ColF_Calculation()
    ReturnVal = GetCurrency(IA4562A.TotDisAdj)
End Sub

Private Sub TotColI_Calculation()
    ReturnVal = GetCurrency(IA4562A.TotIA179) + GetCurrency(IA4562A.TotMACRS)
End Sub

Private Sub TotDepAdj_Calculation()
    ReturnVal = GetCurrency(IA4562A.DepAdj) + GetCurrency(IA4562A.TotP2ColF)
End Sub

Private Sub TotDisAdj_Calculation()
    ReturnVal = GetCurrency(IA4562A.DisAdj(0)) + GetCurrency(IA4562A.DisAdj(1)) + GetCurrency(IA4562A.DisAdj(2)) + GetCurrency(IA4562A.DisAdj(3))
End Sub

Private Sub TotDisFedDep_Calculation()
    ReturnVal = GetCurrency(IA4562A.DisFedDep(0)) + GetCurrency(IA4562A.DisFedDep(1)) + GetCurrency(IA4562A.DisFedDep(2)) + GetCurrency(IA4562A.DisFedDep(3))
End Sub

Private Sub TotDisIADep_Calculation()
    ReturnVal = GetCurrency(IA4562A.DisIADep(0)) + GetCurrency(IA4562A.DisIADep(1)) + GetCurrency(IA4562A.DisIADep(2)) + GetCurrency(IA4562A.DisIADep(3))
End Sub

Private Sub TotFDD_Calculation()
    ReturnVal = GetCurrency(IA4562A.FedDepDed(0)) + GetCurrency(IA4562A.FedDepDed(1)) + GetCurrency(IA4562A.FedDepDed(2)) + GetCurrency(IA4562A.FedDepDed(3))
End Sub

Private Sub TotMACRS_Calculation()
    ReturnVal = GetCurrency(IA4562A.MACRSIA(0)) + GetCurrency(IA4562A.MACRSIA(1)) + GetCurrency(IA4562A.MACRSIA(2)) + GetCurrency(IA4562A.MACRSIA(3))
End Sub

