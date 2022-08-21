Private Sub Alert10_Calculation()
    If GetBool(IA4562PIV.SpecElectYes) = False And GetCurrency(IA4562PIV.Total179) > 70000@ Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert20_Calculation()
    If GetBool(IA4562PIV.UsingSpecElec) = True Then
        If (GetCurrency(IA4562PIV.TPFed1065) + GetCurrency(IA4562PIV.SPFed1065) + GetCurrency(IA4562PIV.TPFed1120S) + GetCurrency(IA4562PIV.SPFed1120S)) > 0@ Then
            If (GetCurrency(IA4562PIV.TPIA1065) + GetCurrency(IA4562PIV.SPIA1065) + GetCurrency(IA4562PIV.TPIA1120S) + GetCurrency(IA4562PIV.SPIA1120S)) = 0@ Then
                ReturnVal = 1
            Else
                ReturnVal = 0
            End If
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert30_Calculation()
    If GetBool(IA4562PIV.UsingSpecElec) = True Then
        If (GetCurrency(USWDepr.IACYSec179Rep) + GetCurrency(USF4562.StateTotCySec1792106, 1)) > 0 Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CarryOver179Yr1_Calculation()
    ReturnVal = MaxValue(0, (GetCurrency(IA4562PIV.Excess179) - GetCurrency(IA4562PIV.CarryOver179Yr2) - GetCurrency(IA4562PIV.CarryOver179Yr3) - GetCurrency(IA4562PIV.CarryOver179Yr4) - GetCurrency(IA4562PIV.CarryOver179Yr5)))
End Sub

Private Sub CarryOver179Yr2_Calculation()
    ReturnVal = CDollar(GetFloat(IA4562PIV.Excess179) * 0.2)
End Sub

Private Sub CarryOver179Yr3_Calculation()
    ReturnVal = CDollar(GetFloat(IA4562PIV.Excess179) * 0.2)
End Sub

Private Sub CarryOver179Yr4_Calculation()
    ReturnVal = CDollar(GetFloat(IA4562PIV.Excess179) * 0.2)
End Sub

Private Sub CarryOver179Yr5_Calculation()
    ReturnVal = CDollar(GetFloat(IA4562PIV.Excess179) * 0.2)
End Sub

Private Sub Desc_Calculation()
    Dim Total As Currency
    
    Total = GetCurrency(IA4562PIV.Excess179)
    
    ReturnVal = CStr(Total) & " Special Election Deduction"

End Sub

Private Sub Excess179_Calculation()
    If GetBool(IA4562PIV.SpecElectYes) = True Then
        ReturnVal = MaxValue(0, (GetCurrency(IA4562PIV.Total179) - GetCurrency(IA4562PIV.Limit)))
    Else
        ReturnVal = 0@
    End If
End Sub

Private Sub Exist_Calculation()
    ReturnVal = 1
End Sub

Private Sub IASec179NoK1s_Calculation()
    ReturnVal = GetCurrency(USWDepr.IACYSec179Rep) + GetCurrency(USF4562.StateTotCySec1792106, 1)
End Sub

Private Sub Limit_Calculation()
    If GetBool(IA4562PIV.SpecElectYes) = True Then
        ReturnVal = 70000@
    Else
        ReturnVal = 0@
    End If
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.CombNames)
End Sub

Private Sub PrIA4562PIV_Calculation()
    If GetCurrency(IA4562PIV.TPPartIV179) <> 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PrIA4562PIVSP_Calculation()
    If GetCurrency(IA4562PIV.SPPartIV179) <> 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Print_Calculation()
    If GetCurrency(IA4562PIV.Excess179) <> 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPAccFedDep_Calculation()
    ReturnVal = 0
End Sub

Private Sub SPAccIADep_Calculation()
    ReturnVal = 0
End Sub

Private Sub SPBasis_Calculation()
    ReturnVal = 0
End Sub

Private Sub SPCarryOver179Yr1_Calculation()
    If GetBool(IA4562PIV.UsingSpecElec) = False Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = CDollar(GetFloat(IA4562PIV.CarryOver179Yr1) * GetFloat(IA4562PIV.SPRatio))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPCarryOver179Yr2_Calculation()
    If GetBool(IA4562PIV.UsingSpecElec) = False Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = CDollar(GetFloat(IA4562PIV.CarryOver179Yr2) * GetFloat(IA4562PIV.SPRatio))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPCarryOver179Yr3_Calculation()
    If GetBool(IA4562PIV.UsingSpecElec) = False Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = CDollar(GetFloat(IA4562PIV.CarryOver179Yr3) * GetFloat(IA4562PIV.SPRatio))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPCarryOver179Yr4_Calculation()
    If GetBool(IA4562PIV.UsingSpecElec) = False Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = CDollar(GetFloat(IA4562PIV.CarryOver179Yr4) * GetFloat(IA4562PIV.SPRatio))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPCarryOver179Yr5_Calculation()
    If GetBool(IA4562PIV.UsingSpecElec) = False Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = CDollar(GetFloat(IA4562PIV.CarryOver179Yr5) * GetFloat(IA4562PIV.SPRatio))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SpCopy_Calculation()
    If GetCurrency(IA4562PIV.SPPartIV179) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPDateServ_Calculation()
    ReturnVal = MakeDate(12, 31, YearNumber)
End Sub

Private Sub SPExcess179_Calculation()
    If GetBool(IA4562PIV.UsingSpecElec) = False Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = CDollar(GetFloat(IA4562PIV.Excess179) * GetFloat(IA4562PIV.SPRatio))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPFed1065_Calculation()
    ReturnVal = GetCurrency(USDPartK1.Sec179, FieldCopies(USDPartK1.Spouse)) + MaxValue(0, GetCurrency(USDPartK1.Sec179, FieldCopies(USDPartK1.Joint)) - CDollar(GetFloat(USDPartK1.Sec179, FieldCopies(USDPartK1.Joint)) * 0.5))
End Sub

Private Sub SPFed1120S_Calculation()
    ReturnVal = GetCurrency(USDSCorpK1.Sec179, FieldCopies(USDSCorpK1.Spouse)) + MaxValue(0, GetCurrency(USDSCorpK1.Sec179, FieldCopies(USDSCorpK1.Joint)) - CDollar(GetFloat(USDSCorpK1.Sec179, FieldCopies(USDSCorpK1.Joint)) * 0.5))
End Sub

Private Sub SPFedDepDed_Calculation()
    ReturnVal = 0
End Sub

Private Sub SPLife_Calculation()
    ReturnVal = "0"
End Sub

Private Sub SPLine1_Calculation()
    If GetBool(IA4562PIV.UsingSpecElec) = False Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = CDollar(GetFloat(IA4562PIV.Total179) * GetFloat(IA4562PIV.SPRatio))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPLine1a_Calculation()
    If GetBool(IA4562PIV.UsingSpecElec) = False Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetCurrency(IA4562PIV.SPIA1065)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPLine1b_Calculation()
    If GetBool(IA4562PIV.UsingSpecElec) = False Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetCurrency(IA4562PIV.SPFed1065)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPLine1c_Calculation()
    If GetBool(IA4562PIV.UsingSpecElec) = False Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetCurrency(IA4562PIV.SPIA1120S)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPLine1d_Calculation()
    If GetBool(IA4562PIV.UsingSpecElec) = False Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetCurrency(IA4562PIV.SPFed1120S)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPMACRSIA_Calculation()
    ReturnVal = 0
End Sub

Private Sub SPName_Calculation()
    ReturnVal = GetString(IARequired.SPCombName)
End Sub

Private Sub SPPartIV179_Calculation()
    If GetBool(IA4562PIV.UsingSpecElec) = False Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = CDollar(GetFloat(IA4562PIV.Limit) * GetFloat(IA4562PIV.SPRatio))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPPropDescr_Calculation()
    If GetCurrency(IA4562PIV.SPPartIV179) > 0 Then
        ReturnVal = "Part IV"
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub SPRatio_Calculation()
    If GetCurrency(IA4562PIV.Tot179Nolimit) = 0 Then
        ReturnVal = 0
    Else
        ReturnVal = MaxValue(0, (MinValue(1#, GetFloat(IA4562PIV.SPTot179) / GetFloat(IA4562PIV.Tot179Nolimit))))
    End If
End Sub

Private Sub SPSSN_Calculation()
    ReturnVal = GetString(IAF1040.SpouseSSN)
End Sub

Private Sub SPTot179_Calculation()
    ReturnVal = GetCurrency(IA4562PIV.SPIA1065) + GetCurrency(IA4562PIV.SPFed1065) + GetCurrency(IA4562PIV.SPIA1120S) + GetCurrency(IA4562PIV.SPFed1120S)
End Sub

Private Sub SPTotAdj_Calculation()
    ReturnVal = GetCurrency(IA4562PIV.SPLine1) - GetCurrency(IA4562PIV.SPPartIV179)
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

Private Sub Tot179Nolimit_Calculation()
    ReturnVal = GetCurrency(IA4562PIV.TPTot179) + GetCurrency(IA4562PIV.SPTot179)
End Sub

Private Sub Total179_Calculation()
    Dim Tot As Currency
    
    Tot = GetCurrency(IA4562PIV.TotIA1065) + GetCurrency(IA4562PIV.TotFed1065) + GetCurrency(IA4562PIV.TotIA1120S) + GetCurrency(IA4562PIV.TotFed1120S)
    
    ReturnVal = MinValue(Tot, 1000000@)
End Sub

Private Sub TotFed1065_Calculation()
    ReturnVal = GetCurrency(IA4562PIV.TPFed1065) + GetCurrency(IA4562PIV.SPFed1065)
End Sub

Private Sub TotFed1120S_Calculation()
    ReturnVal = GetCurrency(IA4562PIV.TPFed1120S) + GetCurrency(IA4562PIV.SPFed1120S)
End Sub

Private Sub TotIA1065_Calculation()
    ReturnVal = GetCurrency(IA4562PIV.TPIA1065) + GetCurrency(IA4562PIV.SPIA1065)
End Sub

Private Sub TotIA1120S_Calculation()
    ReturnVal = GetCurrency(IA4562PIV.TPIA1120S) + GetCurrency(IA4562PIV.SPIA1120S)
End Sub

Private Sub TPAccFedDep_Calculation()
    ReturnVal = 0
End Sub

Private Sub TPAccIADep_Calculation()
    ReturnVal = 0
End Sub

Private Sub TPBasis_Calculation()
    ReturnVal = 0
End Sub

Private Sub TPCarryOver179Yr1_Calculation()
    If GetBool(IA4562PIV.UsingSpecElec) = False Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetCurrency(IA4562PIV.CarryOver179Yr1) - GetCurrency(IA4562PIV.SPCarryOver179Yr1)
    Else
        ReturnVal = GetCurrency(IA4562PIV.CarryOver179Yr1)
    End If
End Sub

Private Sub TPCarryOver179Yr2_Calculation()
    If GetBool(IA4562PIV.UsingSpecElec) = False Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetCurrency(IA4562PIV.CarryOver179Yr2) - GetCurrency(IA4562PIV.SPCarryOver179Yr2)
    Else
        ReturnVal = GetCurrency(IA4562PIV.CarryOver179Yr2)
    End If
End Sub

Private Sub TPCarryOver179Yr3_Calculation()
    If GetBool(IA4562PIV.UsingSpecElec) = False Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetCurrency(IA4562PIV.CarryOver179Yr3) - GetCurrency(IA4562PIV.SPCarryOver179Yr3)
    Else
        ReturnVal = GetCurrency(IA4562PIV.CarryOver179Yr3)
    End If
End Sub

Private Sub TPCarryOver179Yr4_Calculation()
    If GetBool(IA4562PIV.UsingSpecElec) = False Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetCurrency(IA4562PIV.CarryOver179Yr4) - GetCurrency(IA4562PIV.SPCarryOver179Yr4)
    Else
        ReturnVal = GetCurrency(IA4562PIV.CarryOver179Yr4)
    End If
End Sub

Private Sub TPCarryOver179Yr5_Calculation()
    If GetBool(IA4562PIV.UsingSpecElec) = False Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetCurrency(IA4562PIV.CarryOver179Yr5) - GetCurrency(IA4562PIV.SPCarryOver179Yr5)
    Else
        ReturnVal = GetCurrency(IA4562PIV.CarryOver179Yr5)
    End If
End Sub

Private Sub TpCopy_Calculation()
    If GetCurrency(IA4562PIV.TPPartIV179) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPDateServ_Calculation()
    ReturnVal = MakeDate(12, 31, YearNumber)
End Sub

Private Sub TPExcess179_Calculation()
    If GetBool(IA4562PIV.UsingSpecElec) = False Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetCurrency(IA4562PIV.Excess179) - GetCurrency(IA4562PIV.SPExcess179)
    Else
        ReturnVal = GetCurrency(IA4562PIV.Excess179)
    End If
End Sub

Private Sub TPFed1065_Calculation()
    ReturnVal = GetCurrency(USDPartK1.Sec179, FieldCopies(USDPartK1.Taxpayer)) + CDollar(GetFloat(USDPartK1.Sec179, FieldCopies(USDPartK1.Joint)) * 0.5)
End Sub

Private Sub TPFed1120S_Calculation()
    ReturnVal = GetCurrency(USDSCorpK1.Sec179, FieldCopies(USDSCorpK1.Taxpayer)) + CDollar(GetFloat(USDSCorpK1.Sec179, FieldCopies(USDSCorpK1.Joint)) * 0.5)
End Sub

Private Sub TPFedDepDed_Calculation()
    ReturnVal = 0
End Sub

Private Sub TPLife_Calculation()
    ReturnVal = "0"
End Sub

Private Sub TPLine1_Calculation()
    If GetBool(IA4562PIV.UsingSpecElec) = False Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetCurrency(IA4562PIV.Total179) - GetCurrency(IA4562PIV.SPLine1)
    Else
        ReturnVal = GetCurrency(IA4562PIV.Total179)
    End If
End Sub

Private Sub TPLine1a_Calculation()
    If GetBool(IA4562PIV.UsingSpecElec) = False Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetCurrency(IA4562PIV.TPIA1065)
    Else
        ReturnVal = GetCurrency(IA4562PIV.TotIA1065)
    End If
End Sub

Private Sub TPLine1b_Calculation()
    If GetBool(IA4562PIV.UsingSpecElec) = False Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetCurrency(IA4562PIV.TPFed1065)
    Else
        ReturnVal = GetCurrency(IA4562PIV.TotFed1065)
    End If
End Sub

Private Sub TPLine1c_Calculation()
    If GetBool(IA4562PIV.UsingSpecElec) = False Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetCurrency(IA4562PIV.TPIA1120S)
    Else
        ReturnVal = GetCurrency(IA4562PIV.TotIA1120S)
    End If
End Sub

Private Sub TPLine1d_Calculation()
    If GetBool(IA4562PIV.UsingSpecElec) = False Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetCurrency(IA4562PIV.TPFed1120S)
    Else
        ReturnVal = GetCurrency(IA4562PIV.TotFed1120S)
    End If
End Sub

Private Sub TPMACRSIA_Calculation()
    ReturnVal = 0
End Sub

Private Sub TPorJTName_Calculation()
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetString(IARequired.TPCombName)
    Else
        ReturnVal = GetString(IARequired.CombNames)
    End If
End Sub

Private Sub TPorJTSSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

Private Sub TPPartIV179_Calculation()
    If GetBool(IA4562PIV.UsingSpecElec) = False Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetCurrency(IA4562PIV.Limit) - GetCurrency(IA4562PIV.SPPartIV179)
    Else
        ReturnVal = GetCurrency(IA4562PIV.Limit)
    End If
End Sub

Private Sub TPPropDescr_Calculation()
    If GetCurrency(IA4562PIV.TPPartIV179) > 0 Then
        ReturnVal = "Part IV"
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub TPTot179_Calculation()
    ReturnVal = GetCurrency(IA4562PIV.TPIA1065) + GetCurrency(IA4562PIV.TPFed1065) + GetCurrency(IA4562PIV.TPIA1120S) + GetCurrency(IA4562PIV.TPFed1120S)
End Sub

Private Sub TPTotAdj_Calculation()
    ReturnVal = GetCurrency(IA4562PIV.TPLine1) - GetCurrency(IA4562PIV.TPPartIV179)
End Sub

Private Sub UsingSpecElec_Calculation()
    If GetBool(IA4562PIV.SpecElectYes) = True And GetCurrency(IA4562PIV.Excess179) > 0@ Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

