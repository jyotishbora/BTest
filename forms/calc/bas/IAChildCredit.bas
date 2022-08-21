Private Sub ChDepCr_Calculation()
    ReturnVal = CDollar(GetFloat(IAChildCredit.FedCredit) * GetFloat(IAChildCredit.Percent))
End Sub

Private Sub Credit_Calculation(Index As Integer)
    If GetCurrency(IAChildCredit.TotNI) < 45000@ And Trim(GetString(IAChildCredit.DepName(Index))) <> "" Then
        ReturnVal = CDollar(CDbl(MinValue(GetCurrency(IAChildCredit.Expenses(Index)), 1000@)) * 0.25)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub DepName_Calculation(Index As Integer)
    Dim count As Integer
    Dim Hold As String
    count = 0
    Hold = ""
    
  
    If GetNumber(IAAddDep.FDepAge(0)) > 2 And GetNumber(IAAddDep.FDepAge(0)) < 7 Then
        If Index = count Then
            Hold = GetString(IAAddDep.FDepName(0)) + " " + GetString(IAAddDep.FDepLast(0))
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetNumber(IAAddDep.FDepAge(1)) > 2 And GetNumber(IAAddDep.FDepAge(1)) < 7 Then
        If Index = count Then
            Hold = GetString(IAAddDep.FDepName(1)) + " " + GetString(IAAddDep.FDepLast(1))
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetNumber(IAAddDep.FDepAge(2)) > 2 And GetNumber(IAAddDep.FDepAge(2)) < 7 Then
        If Index = count Then
            Hold = GetString(IAAddDep.FDepName(2)) + " " + GetString(IAAddDep.FDepLast(2))
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetNumber(IAAddDep.FDepAge(3)) > 2 And GetNumber(IAAddDep.FDepAge(3)) < 7 Then
        If Index = count Then
            Hold = GetString(IAAddDep.FDepName(3)) + " " + GetString(IAAddDep.FDepLast(3))
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetNumber(IAAddDep.FDepAge(4)) > 2 And GetNumber(IAAddDep.FDepAge(4)) < 7 Then
        If Index = count Then
            Hold = GetString(IAAddDep.FDepName(4)) + " " + GetString(IAAddDep.FDepLast(4))
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetNumber(IAAddDep.FDepAge(5)) > 2 And GetNumber(IAAddDep.FDepAge(5)) < 7 Then
        If Index = count Then
            Hold = GetString(IAAddDep.FDepName(5)) + " " + GetString(IAAddDep.FDepLast(5))
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetNumber(IAAddDep.FDepAge(6)) > 2 And GetNumber(IAAddDep.FDepAge(6)) < 7 Then
        If Index = count Then
            Hold = GetString(IAAddDep.FDepName(6)) + " " + GetString(IAAddDep.FDepLast(6))
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetNumber(IAAddDep.FDepAge(7)) > 2 And GetNumber(IAAddDep.FDepAge(7)) < 7 Then
        If Index = count Then
            Hold = GetString(IAAddDep.FDepName(7)) + " " + GetString(IAAddDep.FDepLast(7))
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetNumber(IAAddDep.FDepAge(8)) > 2 And GetNumber(IAAddDep.FDepAge(8)) < 7 Then
        If Index = count Then
            Hold = GetString(IAAddDep.FDepName(8)) + " " + GetString(IAAddDep.FDepLast(8))
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetNumber(IAAddDep.FDepAge(9)) > 2 And GetNumber(IAAddDep.FDepAge(9)) < 7 Then
        If Index = count Then
            Hold = GetString(IAAddDep.FDepName(9)) + " " + GetString(IAAddDep.FDepLast(9))
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetNumber(IAAddDep.FDepAge(10)) > 2 And GetNumber(IAAddDep.FDepAge(10)) < 7 Then
        If Index = count Then
            Hold = GetString(IAAddDep.FDepName(10)) + " " + GetString(IAAddDep.FDepLast(10))
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetNumber(IAAddDep.FDepAge(11)) > 2 And GetNumber(IAAddDep.FDepAge(11)) < 7 Then
        If Index = count Then
            Hold = GetString(IAAddDep.FDepName(11)) + " " + GetString(IAAddDep.FDepLast(11))
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetNumber(IAAddDep.FDepAge(12)) > 2 And GetNumber(IAAddDep.FDepAge(12)) < 7 Then
        If Index = count Then
            Hold = GetString(IAAddDep.FDepName(12)) + " " + GetString(IAAddDep.FDepLast(12))
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetNumber(IAAddDep.FDepAge(13)) > 2 And GetNumber(IAAddDep.FDepAge(13)) < 7 Then
        If Index = count Then
            Hold = GetString(IAAddDep.FDepName(13)) + " " + GetString(IAAddDep.FDepLast(13))
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetNumber(IAAddDep.FDepAge(14)) > 2 And GetNumber(IAAddDep.FDepAge(14)) < 7 Then
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
    Dim TotCR As Currency
    
    If GetBool(IAF1040.ChildCareCk) = True Then
        TotCR = GetCurrency(IAChildCredit.TotChDepCr)
    ElseIf GetBool(IAF1040.EarlyChildCk) = True Then
        TotCR = GetCurrency(IAChildCredit.TotCR)
    Else
        TotCR = 0
    End If
    
    ReturnVal = CStr(TotCR)
End Sub

Private Sub FedCredit_Calculation()
    ReturnVal = GetCurrency(USF2441.TentCred)
End Sub

Private Sub MFSProRate_Calculation()
    If IAFS() = 4 Then
        If GetCurrency(IAF1040.SpIncome) < 0 And GetCurrency(IAF1040.ANet) < 0 Then
            If GetCurrency(IAF1040.SpIncome) < GetCurrency(IAF1040.ANet) Then
                ReturnVal = 0
            Else
                ReturnVal = 1
            End If
        ElseIf GetCurrency(IAF1040.SpIncome) < 0 Then
            ReturnVal = 0
        ElseIf GetCurrency(IAF1040.SpIncome) > 0 And GetCurrency(IAChildCredit.MFSTotNet) <= 0 Then
            ReturnVal = 1
        ElseIf GetCurrency(IAChildCredit.MFSTotNet) = 0 Then
            ReturnVal = 0
        Else
            ReturnVal = MaxValue(0, (MinValue(1#, GetFloat(IAF1040.SpIncome) / GetFloat(IAChildCredit.MFSTotNet))))
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub MFSTotNet_Calculation()
    If GetBool(IAF1040.MFS) = True Then
        ReturnVal = GetCurrency(IAF1040.ANet) + GetCurrency(IAOthAdj.TIANOL) + GetCurrency(IAF1040.SpIncome)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.CombNames)
End Sub

Private Sub Percent_Calculation()
    If GetCurrency(IAChildCredit.TotNI) > 44999@ Then
        ReturnVal = 0
    ElseIf GetCurrency(IAChildCredit.TotNI) > 39999@ Then
        ReturnVal = 0.3
    ElseIf GetCurrency(IAChildCredit.TotNI) > 34999@ Then
        ReturnVal = 0.4
    ElseIf GetCurrency(IAChildCredit.TotNI) > 24999@ Then
        ReturnVal = 0.5
    ElseIf GetCurrency(IAChildCredit.TotNI) > 19999@ Then
        ReturnVal = 0.55
    ElseIf GetCurrency(IAChildCredit.TotNI) > 9999@ Then
        ReturnVal = 0.65
    Else
        ReturnVal = 0.75
    End If
End Sub

Private Sub PYNRChDepCr_Calculation()
    ReturnVal = MinValue(GetCurrency(IAChildCredit.ChDepCr), (CDollar(GetFloat(IAChildCredit.ChDepCr) * GetFloat(IAChildCredit.PYNRPercent))))
End Sub

Private Sub PYNRPercent_Calculation()
    If GetCurrency(IAChildCredit.TotNI) > 0 Then
        ReturnVal = MinValue(1#, MaxValue(0, CDbl(GetCurrency(IAChildCredit.PYNRTotNI)) / CDbl(GetCurrency(IAChildCredit.TotNI))))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PYNRTotNI_Calculation()
    If GetBool(IAF126.TpPYNR) = True Or GetBool(IAF126.SpPYNR) Then
        ReturnVal = GetCurrency(IAChildCredit.TPNRIncome) + GetCurrency(IAChildCredit.SPNRIncome)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SChild_Calculation()
    If GetBool(IAF1040.MFS) = True Then
        ReturnVal = CDollar(GetFloat(IAChildCredit.TotChDepCr) * GetFloat(IAChildCredit.MFSProRate))
    Else
        ReturnVal = CDollar(GetFloat(IAChildCredit.TotChDepCr) * GetFloat(IARequired.BProRate))
    End If
End Sub

Private Sub SEarly_Calculation()
    If GetBool(IAF1040.MFS) = True Then
        ReturnVal = CDollar(GetFloat(IAChildCredit.TotCR) * GetFloat(IAChildCredit.MFSProRate))
    Else
        ReturnVal = CDollar(GetFloat(IAChildCredit.TotCR) * GetFloat(IARequired.BProRate))
    End If
End Sub

Private Sub SPNRIncome_Calculation()
    If GetBool(IAF1040.MFS) = True Then
        ReturnVal = GetCurrency(IAF1040.SpIncome)
    ElseIf GetBool(IAF126.SpPYNR) = True Then
        ReturnVal = GetCurrency(IAF126.BNet) + GetCurrency(IANROthAdj.SIANOL)
    Else
        ReturnVal = GetCurrency(IAF1040.BNet) + GetCurrency(IAOthAdj.SIANOL)
    End If
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

Private Sub TChild_Calculation()
    ReturnVal = GetCurrency(IAChildCredit.TotChDepCr) - GetCurrency(IAChildCredit.SChild)
End Sub

Private Sub TEarly_Calculation()
    ReturnVal = GetCurrency(IAChildCredit.TotCR) - GetCurrency(IAChildCredit.SEarly)
End Sub

Private Sub TotChDepCr_Calculation()
    If GetBool(IAF126.TpPYNR) = True Or GetBool(IAF126.SpPYNR) Then
        ReturnVal = GetCurrency(IAChildCredit.PYNRChDepCr)
    Else
        ReturnVal = GetCurrency(IAChildCredit.ChDepCr)
    End If
End Sub

Private Sub TotCR_Calculation()
    Dim count As Integer
    Dim SubTot As Currency

    count = 0
    SubTot = 0

    Do While count < 15
        SubTot = SubTot + GetCurrency(IAChildCredit.Credit(count))
        count = count + 1
    Loop
    
    ReturnVal = SubTot
End Sub

Private Sub TotNI_Calculation()
    If GetBool(IAF1040.MFS) = True Then
        ReturnVal = GetCurrency(IAChildCredit.MFSTotNet)
    Else
        ReturnVal = GetCurrency(IARequired.TotNI) + GetCurrency(IAOthAdj.TIANOL) + GetCurrency(IAOthAdj.SIANOL)
    End If
End Sub

Private Sub TPNRIncome_Calculation()
    If GetBool(IAF126.TpPYNR) = True Then
        ReturnVal = GetCurrency(IAF126.ANet) + GetCurrency(IANROthAdj.TIANOL)
    Else
        ReturnVal = GetCurrency(IAF1040.ANet) + GetCurrency(IAOthAdj.TIANOL)
    End If
End Sub

