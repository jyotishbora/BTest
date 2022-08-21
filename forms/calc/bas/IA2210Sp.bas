Private Sub Amt8_Calculation()
    ReturnVal = CDollar(GetFloat(IA2210Sp.Bal) * 0.9)
End Sub

Private Sub Bal_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA2210Sp.CYTax) - GetCurrency(IA2210Sp.TotCr))
End Sub

Private Sub ChildC_Calculation()
    ReturnVal = GetCurrency(IAF1040.BChild)
End Sub

Private Sub CYTax_Calculation()
    ReturnVal = GetCurrency(IAF1040.BBal4)
End Sub

Private Sub Description_Calculation()
    ReturnVal = CStr(GetCurrency(IA2210Sp.Penalty)) & " Penalty"
End Sub

Private Sub EFile_Calculation()
    If GetBool(IA1040X.EFAmend) = True Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.CombMFS) = False Then
        ReturnVal = 0
    ElseIf GetBool(IA2210Sp.Print) = True Then
        ReturnVal = 1
    ElseIf GetCurrency(IA2210Sp.Amt8) >= 200@ Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub EFStQ1_Calculation()
    ReturnVal = GetCurrency(IAStateEst.SPStApply) + GetCurrency(IAStateEst.SPStQ1)
End Sub

Private Sub ExpPenalty_Calculation()
    If GetCurrency(IA2210SP.Penalty) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Fuel_Calculation()
    ReturnVal = GetCurrency(IAF1040.BFuel)
End Sub

Private Sub IAEIC_Calculation()
    ReturnVal = GetCurrency(IAF1040.BIEIC)
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.SPCombName)
End Sub

Private Sub NoPen_Calculation()
    ReturnVal = GetBool(USWPrepMnNm.AlwaysState2210)
End Sub

Private Sub Penalty_Calculation()
    If GetBool(IAF1040.CombMFS) = False Then
        ReturnVal = 0
    ElseIf GetBool(IA2210Sp.NoPen) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(IAPenaltySp.TotPen)
    End If
End Sub

Private Sub Print_Calculation()
    If GetBool(IAF1040.CombMFS) = False Then
        ReturnVal = 0
    ElseIf GetBool(IA2210Sp.AnInc) = True Then
        ReturnVal = 1
    ElseIf GetCurrency(IA2210Sp.Penalty) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PYTax_Calculation()
    Dim AGIBonus As Currency
    
    AGIBonus = GetCurrency(USWRec.PYSAGI) + GetCurrency(USZIA1040.IATotBonusSp)

    If GetBool(IAF1040.CombMFS) = False Then
        ReturnVal = 0
    ElseIf GetString(USZIA1040.IAPYFS) = GetString(IARequired.FilingStatus) Then
        If AGIBonus > 150000@ Then
            ReturnVal = CDollar(GetFloat(USZIA1040.IA2210PYTaxSp) * 1.1)
        Else
            ReturnVal = GetCurrency(USZIA1040.IA2210PYTaxSp)
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q1AnInc_Calculation()
    If GetBool(IA2210Sp.AnInc) = True Then
        ReturnVal = GetCurrency(IA2210AnSp.Q1AIInstall)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q1DaysB_Calculation()
    If GetCurrency(IA2210Sp.Penalty) > 0 Then
        ReturnVal = "See"
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub Q1Est_Calculation()
    ReturnVal = GetCurrency(IA2210Sp.Q1WH) + GetCurrency(IAStateEst.SPStApply) + GetCurrency(IAStateEst.SPStQ1)
End Sub

Private Sub Q1Install_Calculation()
    ReturnVal = CDollar(GetFloat(IA2210Sp.Small) * 0.25)
End Sub

Private Sub Q1Ln11_Calculation()
    If GetBool(IA2210Sp.AnInc) = True Then
        ReturnVal = GetCurrency(IA2210Sp.Q1AnInc)
    Else
        ReturnVal = GetCurrency(IA2210Sp.Q1Install)
    End If
End Sub

Private Sub Q1Ln19a_Calculation()
    If GetCurrency(IA2210Sp.Penalty) > 0 Then
        ReturnVal = "Worksheet"
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub Q1Ln19B_Calculation()
    If GetCurrency(IA2210Sp.Penalty) > 0 Then
        ReturnVal = "Attached"
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub Q1Undpay_Calculation()
    If GetCurrency(IA2210Sp.Q1Est) < GetCurrency(IA2210Sp.Q1Ln11) Then
        ReturnVal = GetCurrency(IA2210Sp.Q1Ln11) - GetCurrency(IA2210Sp.Q1Est)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q1WH_Calculation()
    ReturnVal = CDollar(CDbl(GetCurrency(IAF1040.BIATaxWith)) * 0.25)
End Sub

Private Sub Q2AnInc_Calculation()
    If GetBool(IA2210Sp.AnInc) = True Then
        ReturnVal = GetCurrency(IA2210AnSp.Q2AIInstall)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q2est_Calculation()
    ReturnVal = GetCurrency(IA2210Sp.Q2WH) + GetCurrency(IAStateEst.SPStQ2)
End Sub

Private Sub Q2Install_Calculation()
    ReturnVal = CDollar(CDbl(GetCurrency(IA2210Sp.Small) - GetCurrency(IA2210Sp.Q1Install)) * 0.3333)
End Sub

Private Sub Q2Ln11_Calculation()
    If GetBool(IA2210Sp.AnInc) = True Then
        ReturnVal = GetCurrency(IA2210Sp.Q2AnInc)
    Else
        ReturnVal = GetCurrency(IA2210Sp.Q2Install)
    End If
End Sub

Private Sub Q2WH_Calculation()
    ReturnVal = CDollar(CDbl(GetCurrency(IAF1040.BIATaxWith) - GetCurrency(IA2210Sp.Q1WH)) * 0.3333)
End Sub

Private Sub Q3AnInc_Calculation()
    If GetBool(IA2210Sp.AnInc) = True Then
        ReturnVal = GetCurrency(IA2210AnSp.Q3AIInstall)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q3Est_Calculation()
    ReturnVal = GetCurrency(IA2210Sp.Q3WH) + GetCurrency(IAStateEst.SPStQ3)
End Sub

Private Sub Q3Install_Calculation()
    ReturnVal = CDollar(CDbl(GetCurrency(IA2210Sp.Small) - GetCurrency(IA2210Sp.Q1Install) - GetCurrency(IA2210Sp.Q2Install)) * 0.5)
End Sub

Private Sub Q3Ln11_Calculation()
    If GetBool(IA2210Sp.AnInc) = True Then
        ReturnVal = GetCurrency(IA2210Sp.Q3AnInc)
    Else
        ReturnVal = GetCurrency(IA2210Sp.Q3Install)
    End If

End Sub

Private Sub Q3WH_Calculation()
    ReturnVal = CDollar(CDbl(GetCurrency(IAF1040.BIATaxWith) - GetCurrency(IA2210Sp.Q1WH) - GetCurrency(IA2210Sp.Q2WH)) * 0.5)
End Sub

Private Sub Q4AnInc_Calculation()
    If GetBool(IA2210Sp.AnInc) = True Then
        ReturnVal = GetCurrency(IA2210AnSp.Q4AIInstall)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q4Est_Calculation()
    ReturnVal = GetCurrency(IA2210Sp.Q4WH) + GetCurrency(IAStateEst.SPStQ4)
End Sub

Private Sub Q4Install_Calculation()
    ReturnVal = GetCurrency(IA2210Sp.Small) - GetCurrency(IA2210Sp.Q1Install) - GetCurrency(IA2210Sp.Q2Install) - GetCurrency(IA2210Sp.Q3Install)
End Sub

Private Sub Q4Ln11_Calculation()
    If GetBool(IA2210Sp.AnInc) = True Then
        ReturnVal = GetCurrency(IA2210Sp.Q4AnInc)
    Else
        ReturnVal = GetCurrency(IA2210Sp.Q4Install)
    End If
End Sub

Private Sub Q4WH_Calculation()
    ReturnVal = GetCurrency(IAF1040.BIATaxWith) - GetCurrency(IA2210Sp.Q1WH) - GetCurrency(IA2210Sp.Q2WH) - GetCurrency(IA2210Sp.Q3WH)
End Sub

Private Sub RefundCr_Calculation()
    ReturnVal = GetCurrency(IAF1040.BOthRefCr)
End Sub

Private Sub Small_Calculation()
    If GetBool(IAF1040.CombMFS) = False Then
        ReturnVal = 0
    ElseIf GetBool(IA2210Sp.NoPen) = True Then
        ReturnVal = 0
    ElseIf GetCurrency(IA2210Sp.Amt8) < 200@ Then
        ReturnVal = 0
    ElseIf GetBool(IA2210Sp.PYZero) = True Then
        ReturnVal = 0
    ElseIf GetCurrency(IA2210Sp.PYTax) = 0 Then
        ReturnVal = GetCurrency(IA2210Sp.Amt8)
    Else
        ReturnVal = MinValue(GetCurrency(IA2210Sp.Amt8), GetCurrency(IA2210Sp.PYTax))
    End If
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SpouseSSN)
End Sub

Private Sub TotCr_Calculation()
    ReturnVal = GetCurrency(IA2210Sp.Fuel) + GetCurrency(IA2210Sp.ChildC) + GetCurrency(IA2210Sp.IAEIC) + GetCurrency(IA2210Sp.RefundCr)
End Sub

