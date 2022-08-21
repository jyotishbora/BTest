Private Sub Alert10_Calculation()
    If GetCurrency(IA2210.Penalty) > 0 And GetCurrency(IA2210.PYTax) = 0 And GetBool(IA2210.PYZero) = False Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert20_Calculation()
    If GetCurrency(IA2210Sp.Penalty) > 0 And GetCurrency(IA2210Sp.PYTax) = 0 And GetBool(IA2210Sp.PYZero) = False Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Amt8_Calculation()
    ReturnVal = CDollar(GetFloat(IA2210.Bal) * 0.9)
End Sub

Private Sub Bal_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA2210.CYTax) - GetCurrency(IA2210.TotCr))
End Sub

Private Sub ChildC_Calculation()
    ReturnVal = GetCurrency(IAF1040.AChild)
End Sub

Private Sub CYTax_Calculation()
    ReturnVal = GetCurrency(IAF1040.ABal4)
End Sub

Private Sub Description_Calculation()
    ReturnVal = CStr(GetCurrency(IA2210.Penalty)) & " Penalty"
End Sub

Private Sub EFile_Calculation()
    If GetBool(IA1040X.EFAmend) = True Then
        ReturnVal = 0
    ElseIf GetBool(IA2210.Print) = True Then
        ReturnVal = 1
    ElseIf GetCurrency(IA2210.Amt8) >= 200@ Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub EFStQ1_Calculation()
    ReturnVal = GetCurrency(IAStateEst.TPStApply) + GetCurrency(IAStateEst.TPStQ1)
End Sub

Private Sub ExpPenalty_Calculation()
    If GetCurrency(IA2210.Penalty) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Fuel_Calculation()
    ReturnVal = GetCurrency(IAF1040.AFuel)
End Sub

Private Sub IAEIC_Calculation()
    ReturnVal = GetCurrency(IAF1040.AIEIC)
End Sub

Private Sub Names_Calculation()
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetString(IARequired.TPCombName)
    Else
        ReturnVal = GetString(IARequired.CombNames)
    End If
End Sub

Private Sub NoPen_Calculation()
    ReturnVal = GetBool(USWPrepMnNm.AlwaysState2210)
End Sub

Private Sub Penalty_Calculation()
    If GetBool(IA2210.NoPen) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(IAPenalty.TotPen)
    End If
End Sub

Private Sub Print_Calculation()
    If GetBool(IA2210.AnInc) = True Then
        ReturnVal = 1
    ElseIf GetCurrency(IA2210.Penalty) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PYTax_Calculation()
    Dim PYAGILimit As Currency
    Dim AGI As Currency
    Dim AGIBonus As Currency
    
    If GetBool(USWSpouse.MFS) = True And GetBool(USWSpouse.NonRes) = False Then
        PYAGILimit = 75000@
    Else
        PYAGILimit = 150000@
    End If
    
    If GetBool(USWSpouse.NonRes) = True Then
        AGI = GetCurrency(USWRec.PYAGINR)
    ElseIf IAFS() <> 3 Then
        AGI = GetCurrency(USWRec.PYTAGI)
    Else
        AGI = GetCurrency(USWRec.PYAGI)
    End If    

    If IAFS() <> 3 Then
        AGIBonus = AGI + GetCurrency(USZIA1040.IATotBonus) + GetCurrency(USZIA1040.IATotBonusSp)
    Else
        AGIBonus = AGI + GetCurrency(USZIA1040.IATotBonus)
    End If

    If AGIBonus > PYAGILimit Then
        ReturnVal = CDollar(GetFloat(USZIA1040.IA2210PYTax) * 1.1)
    Else
        ReturnVal = GetCurrency(USZIA1040.IA2210PYTax)
    End If
End Sub

Private Sub Q1AnInc_Calculation()
    If GetBool(IA2210.AnInc) = True Then
        ReturnVal = GetCurrency(IA2210An.Q1AIInstall)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q1DaysB_Calculation()
    If GetCurrency(IA2210.Penalty) > 0 Then
        ReturnVal = "See"
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub Q1Est_Calculation()
    ReturnVal = GetCurrency(IA2210.Q1WH) + GetCurrency(IAStateEst.TPStApply) + GetCurrency(IAStateEst.TPStQ1)
End Sub

Private Sub Q1Install_Calculation()
    ReturnVal = CDollar(GetFloat(IA2210.Small) * 0.25)
End Sub

Private Sub Q1Ln11_Calculation()
    If GetBool(IA2210.AnInc) = True Then
        ReturnVal = GetCurrency(IA2210.Q1AnInc)
    Else
        ReturnVal = GetCurrency(IA2210.Q1Install)
    End If
End Sub

Private Sub Q1Ln19a_Calculation()
    If GetCurrency(IA2210.Penalty) > 0 Then
        ReturnVal = "Worksheet"
    Else
        ReturnVal = ""
    End If

End Sub

Private Sub Q1Ln19B_Calculation()
    If GetCurrency(IA2210.Penalty) > 0 Then
        ReturnVal = "Attached"
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub Q1Undpay_Calculation()
    If GetCurrency(IA2210.Q1Est) < GetCurrency(IA2210.Q1Ln11) Then
        ReturnVal = GetCurrency(IA2210.Q1Ln11) - GetCurrency(IA2210.Q1Est)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q1WH_Calculation()
    ReturnVal = CDollar(CDbl(GetCurrency(IAF1040.AIATaxWith)) * 0.25)
End Sub

Private Sub Q2AnInc_Calculation()
    If GetBool(IA2210.AnInc) = True Then
        ReturnVal = GetCurrency(IA2210An.Q2AIInstall)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q2est_Calculation()
    ReturnVal = GetCurrency(IA2210.Q2WH) + GetCurrency(IAStateEst.TPStQ2)
End Sub

Private Sub Q2Install_Calculation()
    ReturnVal = CDollar(CDbl(GetCurrency(IA2210.Small) - GetCurrency(IA2210.Q1Install)) * 0.3333)
End Sub

Private Sub Q2Ln11_Calculation()
    If GetBool(IA2210.AnInc) = True Then
        ReturnVal = GetCurrency(IA2210.Q2AnInc)
    Else
        ReturnVal = GetCurrency(IA2210.Q2Install)
    End If
End Sub

Private Sub Q2WH_Calculation()
    ReturnVal = CDollar(CDbl(GetCurrency(IAF1040.AIATaxWith) - GetCurrency(IA2210.Q1WH)) * 0.3333)
End Sub

Private Sub Q3AnInc_Calculation()
    If GetBool(IA2210.AnInc) = True Then
        ReturnVal = GetCurrency(IA2210An.Q3AIInstall)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q3Est_Calculation()
    ReturnVal = GetCurrency(IA2210.Q3WH) + GetCurrency(IAStateEst.TPStQ3)
End Sub

Private Sub Q3Install_Calculation()
    ReturnVal = CDollar(CDbl(GetCurrency(IA2210.Small) - GetCurrency(IA2210.Q1Install) - GetCurrency(IA2210.Q2Install)) * 0.5)
End Sub

Private Sub Q3Ln11_Calculation()
    If GetBool(IA2210.AnInc) = True Then
        ReturnVal = GetCurrency(IA2210.Q3AnInc)
    Else
        ReturnVal = GetCurrency(IA2210.Q3Install)
    End If
End Sub

Private Sub Q3WH_Calculation()
    ReturnVal = CDollar(CDbl(GetCurrency(IAF1040.AIATaxWith) - GetCurrency(IA2210.Q1WH) - GetCurrency(IA2210.Q2WH)) * 0.5)
End Sub

Private Sub Q4AnInc_Calculation()
    If GetBool(IA2210.AnInc) = True Then
        ReturnVal = GetCurrency(IA2210An.Q4AIInstall)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q4Est_Calculation()
    ReturnVal = GetCurrency(IA2210.Q4WH) + GetCurrency(IAStateEst.TPStQ4)
End Sub

Private Sub Q4Install_Calculation()
    ReturnVal = GetCurrency(IA2210.Small) - GetCurrency(IA2210.Q1Install) - GetCurrency(IA2210.Q2Install) - GetCurrency(IA2210.Q3Install)
End Sub

Private Sub Q4Ln11_Calculation()
    If GetBool(IA2210.AnInc) = True Then
        ReturnVal = GetCurrency(IA2210.Q4AnInc)
    Else
        ReturnVal = GetCurrency(IA2210.Q4Install)
    End If
End Sub

Private Sub Q4WH_Calculation()
    ReturnVal = GetCurrency(IAF1040.AIATaxWith) - GetCurrency(IA2210.Q1WH) - GetCurrency(IA2210.Q2WH) - GetCurrency(IA2210.Q3WH)
End Sub

Private Sub RefundCr_Calculation()
    ReturnVal = GetCurrency(IAF1040.AOthRefCr)
End Sub

Private Sub Small_Calculation()
    If GetBool(IA2210.NoPen) = True Then
        ReturnVal = 0
    ElseIf GetCurrency(IA2210.Amt8) < 200@ Then
        ReturnVal = 0
    ElseIf GetBool(IA2210.PYZero) = True Then
        ReturnVal = 0
    ElseIf GetCurrency(IA2210.PYTax) = 0 Then
        ReturnVal = GetCurrency(IA2210.Amt8)
    Else
        ReturnVal = MinValue(GetCurrency(IA2210.Amt8), GetCurrency(IA2210.PYTax))
    End If
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

Private Sub TotCr_Calculation()
    ReturnVal = GetCurrency(IA2210.Fuel) + GetCurrency(IA2210.ChildC) + GetCurrency(IA2210.IAEIC) + GetCurrency(IA2210.RefundCr)
End Sub

