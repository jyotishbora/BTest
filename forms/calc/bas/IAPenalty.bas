Private Sub DatePaid_Calculation()
    ReturnVal = GetDate(IAF1040.DateDuePaid)
End Sub

Private Sub Desc_Calculation()
    ReturnVal = CStr(GetCurrency(IAPenalty.TotPen))
End Sub

Private Sub Exist_Calculation()
    ReturnVal = 1
End Sub

Private Sub Names_Calculation()
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetString(IARequired.TPCombName)
    Else
        ReturnVal = GetString(IARequired.CombNames)
    End If
End Sub

Private Sub Q1Days1_Calculation()
    If GetDate(IAStateEst.TPStQ2Date) < #7/2/2018# Then
        ReturnVal = MaxValue(0, DaysDiff(GetDate(IAStateEst.TPStQ2Date), #4/30/2018#))
    Else
        ReturnVal = 63
    End If
End Sub

Private Sub Q1Days2_Calculation()
    If GetDate(IAStateEst.TPStQ2Date) < #7/2/2018# And GetCurrency(IAPenalty.Q1UnPay2) > 0 Then
        ReturnVal = MaxValue(0, DaysDiff(#7/2/2018#, GetDate(IAStateEst.TPStQ2Date)))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q1Pen1_Calculation()
    ReturnVal = CCur(Round((GetFloat(IAPenalty.Q1Days1) / 365#) * 0.06 * GetFloat(IAPenalty.Q1UnPay1)))
End Sub

Private Sub Q1Pen2_Calculation()
    ReturnVal = CCur(Round((GetFloat(IAPenalty.Q1Days2) / 365#) * 0.06 * GetFloat(IAPenalty.Q1UnPay2)))
End Sub

Private Sub Q1UnPay1_Calculation()
    ReturnVal = GetCurrency(IA2210.Q1Undpay)
End Sub

Private Sub Q1UnPay2_Calculation()
    If GetDate(IAStateEst.TPStQ2Date) < #7/2/2018# Then
        ReturnVal = MaxValue(0, GetCurrency(IAPenalty.Q1UnPay1) - GetCurrency(IAStateEst.TPStQ2))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q2Days1_Calculation()
    If GetDate(IAStateEst.TPStQ3Date) < #10/1/2018# Then
        ReturnVal = MaxValue(0, DaysDiff(GetDate(IAStateEst.TPStQ3Date), #7/2/2018#))
    Else
        ReturnVal = 91
    End If
End Sub

Private Sub Q2Days2_Calculation()
    If GetDate(IAStateEst.TPStQ3Date) < #10/1/2018# And GetCurrency(IAPenalty.Q2UnPay2) > 0 Then
        ReturnVal = MaxValue(0, DaysDiff(#10/1/2018#, GetDate(IAStateEst.TPStQ3Date)))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q2Pen1_Calculation()
    ReturnVal = CCur(Round((GetFloat(IAPenalty.Q2Days1) / 365#) * 0.06 * GetFloat(IAPenalty.Q2UnPay1)))
End Sub

Private Sub Q2Pen2_Calculation()
    ReturnVal = CCur(Round((GetFloat(IAPenalty.Q2Days2) / 365#) * 0.06 * GetFloat(IAPenalty.Q2UnPay2)))
End Sub

Private Sub Q2UnPay1_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA2210.Q1Ln11) + GetCurrency(IA2210.Q2Ln11) - GetCurrency(IA2210.Q1Est) - GetCurrency(IA2210.Q2est))
End Sub

Private Sub Q2UnPay2_Calculation()
    If GetDate(IAStateEst.TPStQ3Date) < #10/1/2018# Then
        ReturnVal = MaxValue(0, GetCurrency(IAPenalty.Q2UnPay1) - GetCurrency(IAStateEst.TPStQ3))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q3Days1_Calculation()
    If GetDate(IAStateEst.TPStQ4Date) < #12/31/2018# Then
        ReturnVal = MaxValue(0, DaysDiff(GetDate(IAStateEst.TPStQ4Date), #10/1/2018#))
    Else
        ReturnVal = 91
    End If
End Sub

Private Sub Q3Days2_Calculation()
    If GetDate(IAStateEst.TPStQ4Date) < #12/31/2018# And GetCurrency(IAPenalty.Q3UnPay2) > 0 Then
        ReturnVal = MaxValue(0, DaysDiff(#12/31/2018#, GetDate(IAStateEst.TPStQ4Date)))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q3Days3_Calculation()
    If GetDate(IAStateEst.TPStQ4Date) < #1/31/2019# And GetDate(IAStateEst.TPStQ4Date) > #12/31/2018# Then
        ReturnVal = MaxValue(0, DaysDiff(GetDate(IAStateEst.TPStQ4Date), #12/31/2018#))
    ElseIf GetCurrency(IAPenalty.Q3Unpay3) >= 0 Then
        ReturnVal = 31
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q3Days4_Calculation()
    If GetDate(IAStateEst.TPStQ4Date) > #12/31/2018# And GetDate(IAStateEst.TPStQ4Date) < #1/31/2019# And GetCurrency(IAPenalty.Q3Unpay4) > 0 Then
        ReturnVal = MaxValue(0, DaysDiff(#1/31/2019#, GetDate(IAStateEst.TPStQ4Date)))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q3Pen1_Calculation()
    ReturnVal = CCur(Round((GetFloat(IAPenalty.Q3Days1) / 365#) * 0.06 * GetFloat(IAPenalty.Q3Unpay1)))
End Sub

Private Sub Q3Pen2_Calculation()
    ReturnVal = CCur(Round((GetFloat(IAPenalty.Q3Days2) / 365#) * 0.06 * GetFloat(IAPenalty.Q3UnPay2)))
End Sub

Private Sub Q3Pen3_Calculation()
    ReturnVal = CCur(Round((GetFloat(IAPenalty.Q3Days3) / 365#) * 0.07 * GetFloat(IAPenalty.Q3Unpay3)))
End Sub

Private Sub Q3Pen4_Calculation()
    ReturnVal = CCur(Round((GetFloat(IAPenalty.Q3Days4) / 365#) * 0.07 * GetFloat(IAPenalty.Q3Unpay4)))
End Sub

Private Sub Q3Unpay1_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA2210.Q1Ln11) + GetCurrency(IA2210.Q2Ln11) + GetCurrency(IA2210.Q3Ln11) - GetCurrency(IA2210.Q1Est) - GetCurrency(IA2210.Q2est) - GetCurrency(IA2210.Q3Est))
End Sub

Private Sub Q3UnPay2_Calculation()
    If GetDate(IAStateEst.TPStQ4Date) < #12/31/2018# Then
        ReturnVal = MaxValue(0, GetCurrency(IAPenalty.Q3Unpay1) - GetCurrency(IAStateEst.TPStQ4))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q3Unpay3_Calculation()
    If GetCurrency(IAPenalty.Q3UnPay2) > 0 Then
        ReturnVal = GetCurrency(IAPenalty.Q3UnPay2)
    ElseIf GetDate(IAStateEst.TPStQ4Date) < #1/1/2019# Then
        ReturnVal = MaxValue(0, GetCurrency(IAPenalty.Q3Unpay1) - GetCurrency(IAStateEst.TPStQ4))
    Else
        ReturnVal = GetCurrency(IAPenalty.Q3Unpay1)
    End If
End Sub

Private Sub Q3Unpay4_Calculation()
    If GetDate(IAStateEst.TPStQ4Date) > #12/31/2018# And GetDate(IAStateEst.TPStQ4Date) < #1/31/2019# Then
        ReturnVal = MaxValue(0, GetCurrency(IAPenalty.Q3Unpay1) - GetCurrency(IAStateEst.TPStQ4))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q4Days1_Calculation()
    ' 89 days max in 2018
    If GetDate(IAStateEst.TPStLateDate) < GetDate(IAF1040.DateDuePaid) And GetCurrency(IAStateEst.TPStLate) > 0 Then
        ReturnVal = MaxValue(0, DaysDiff(GetDate(IAStateEst.TPStLateDate), #1/31/2019#))
    Else
        ReturnVal = MaxValue(0, DaysDiff(GetDate(IAF1040.DateDuePaid), #1/31/2019#))
    End If
End Sub

Private Sub Q4Days2_Calculation()
    If GetDate(IAStateEst.TPStLateDate) < #4/30/2019# And GetCurrency(IAPenalty.Q4Unpay2) > 0 Then
        ReturnVal = MaxValue(0, DaysDiff(GetDate(IAF1040.DateDuePaid), GetDate(IAStateEst.TPStLateDate)))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q4Pen1_Calculation()
    ReturnVal = CCur(Round((GetFloat(IAPenalty.Q4Days1) / 365#) * 0.07 * GetFloat(IAPenalty.Q4UnPay1)))
End Sub

Private Sub Q4Pen2_Calculation()
    ReturnVal = CCur(Round((GetFloat(IAPenalty.Q4Days2) / 365#) * 0.07 * GetFloat(IAPenalty.Q4Unpay2)))
End Sub

Private Sub Q4UnPay1_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA2210.Q1Ln11) + GetCurrency(IA2210.Q2Ln11) + GetCurrency(IA2210.Q3Ln11) + GetCurrency(IA2210.Q4Ln11) - GetCurrency(IA2210.Q1Est) - GetCurrency(IA2210.Q2est) - GetCurrency(IA2210.Q3Est) - GetCurrency(IA2210.Q4Est))
End Sub

Private Sub Q4Unpay2_Calculation()
    If GetDate(IAStateEst.TPStLateDate) < #4/30/2019# And GetCurrency(IAStateEst.TPStLate) > 0 Then
        ReturnVal = MaxValue(0, GetCurrency(IAPenalty.Q4UnPay1) - GetCurrency(IAStateEst.TPStLate))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

Private Sub TotPen_Calculation()
    ReturnVal = Round(GetCurrency(IAPenalty.Q1Pen1) + GetCurrency(IAPenalty.Q1Pen2) + GetCurrency(IAPenalty.Q2Pen1) + GetCurrency(IAPenalty.Q2Pen2) + GetCurrency(IAPenalty.Q3Pen1) + GetCurrency(IAPenalty.Q3Pen2) + GetCurrency(IAPenalty.Q3Pen3) + GetCurrency(IAPenalty.Q3Pen4) + GetCurrency(IAPenalty.Q4Pen1) + GetCurrency(IAPenalty.Q4Pen2))
End Sub

