Private Sub DatePaid_Calculation()
    ReturnVal = GetDate(IAF1040.DateDuePaid)
End Sub

Private Sub Desc_Calculation()
    ReturnVal = CStr(GetCurrency(IAPenaltySp.TotPen))
End Sub

Private Sub Exist_Calculation()
    ReturnVal = 1
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.SPCombName)
End Sub

Private Sub Q1Days1_Calculation()
    If GetDate(IAStateEst.SPStQ2Date) < #7/2/2018# Then
        ReturnVal = MaxValue(0, DaysDiff(GetDate(IAStateEst.SPStQ2Date), #4/30/2018#))
    Else
        ReturnVal = 63
    End If
End Sub

Private Sub Q1Days2_Calculation()
    If GetDate(IAStateEst.SPStQ2Date) < #7/2/2018# And GetCurrency(IAPenaltySp.Q1UnPay2) > 0 Then
        ReturnVal = MaxValue(0, DaysDiff(#7/2/2018#, GetDate(IAStateEst.SPStQ2Date)))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q1Pen1_Calculation()
    ReturnVal = CCur(Round((GetFloat(IAPenaltySp.Q1Days1) / 365#) * 0.06 * GetFloat(IAPenaltySp.Q1UnPay1)))
End Sub

Private Sub Q1Pen2_Calculation()
    ReturnVal = CCur(Round((GetFloat(IAPenaltySp.Q1Days2) / 365#) * 0.06 * GetFloat(IAPenaltySp.Q1UnPay2)))
End Sub

Private Sub Q1UnPay1_Calculation()
    ReturnVal = GetCurrency(IA2210Sp.Q1Undpay)
End Sub

Private Sub Q1UnPay2_Calculation()
    If GetDate(IAStateEst.SPStQ2Date) < #7/2/2018# Then
        ReturnVal = MaxValue(0, GetCurrency(IAPenaltySp.Q1UnPay1) - GetCurrency(IAStateEst.SPStQ2))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q2Days1_Calculation()
    If GetDate(IAStateEst.SPStQ3Date) < #10/1/2018# Then
        ReturnVal = MaxValue(0, DaysDiff(GetDate(IAStateEst.SPStQ3Date), #7/2/2018#))
    Else
        ReturnVal = 91
    End If
End Sub

Private Sub Q2Days2_Calculation()
    If GetDate(IAStateEst.SPStQ3Date) < #10/1/2018# And GetCurrency(IAPenaltySp.Q2UnPay2) > 0 Then
        ReturnVal = MaxValue(0, DaysDiff(#10/1/2018#, GetDate(IAStateEst.SPStQ3Date)))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q2Pen1_Calculation()
    ReturnVal = CCur(Round((GetFloat(IAPenaltySp.Q2Days1) / 365#) * 0.06 * GetFloat(IAPenaltySp.Q2UnPay1)))
End Sub

Private Sub Q2Pen2_Calculation()
    ReturnVal = CCur(Round((GetFloat(IAPenaltySp.Q2Days2) / 365#) * 0.06 * GetFloat(IAPenaltySp.Q2UnPay2)))
End Sub

Private Sub Q2UnPay1_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA2210Sp.Q1Ln11) + GetCurrency(IA2210Sp.Q2Ln11) - GetCurrency(IA2210Sp.Q1Est) - GetCurrency(IA2210Sp.Q2est))
End Sub

Private Sub Q2UnPay2_Calculation()
    If GetDate(IAStateEst.SPStQ3Date) < #10/1/2018# Then
        ReturnVal = MaxValue(0, GetCurrency(IAPenaltySp.Q2UnPay1) - GetCurrency(IAStateEst.SPStQ3))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q3Days1_Calculation()
    If GetDate(IAStateEst.SPStQ4Date) < #12/31/2018# Then
        ReturnVal = MaxValue(0, DaysDiff(GetDate(IAStateEst.SPStQ4Date), #10/1/2018#))
    Else
        ReturnVal = 91
    End If
End Sub

Private Sub Q3Days2_Calculation()
    If GetDate(IAStateEst.SPStQ4Date) < #12/31/2018# And GetCurrency(IAPenaltySp.Q3UnPay2) > 0 Then
        ReturnVal = MaxValue(0, DaysDiff(#12/31/2018#, GetDate(IAStateEst.SPStQ4Date)))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q3Days3_Calculation()
    If GetDate(IAStateEst.SPStQ4Date) < #1/31/2019# And GetDate(IAStateEst.SPStQ4Date) > #12/31/2018# Then
        ReturnVal = MaxValue(0, DaysDiff(GetDate(IAStateEst.SPStQ4Date), #12/31/2018#))
    ElseIf GetCurrency(IAPenaltySp.Q3Unpay3) >= 0 Then
        ReturnVal = 31
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q3Days4_Calculation()
    If GetDate(IAStateEst.SPStQ4Date) > #12/31/2018# And GetDate(IAStateEst.SPStQ4Date) < #1/31/2019# And GetCurrency(IAPenaltySp.Q3Unpay4) > 0 Then
        ReturnVal = MaxValue(0, DaysDiff(#1/31/2019#, GetDate(IAStateEst.SPStQ4Date)))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q3Pen1_Calculation()
    ReturnVal = CCur(Round((GetFloat(IAPenaltySp.Q3Days1) / 365#) * 0.06 * GetFloat(IAPenaltySp.Q3Unpay1)))
End Sub

Private Sub Q3Pen2_Calculation()
    ReturnVal = CCur(Round((GetFloat(IAPenaltySp.Q3Days2) / 365#) * 0.06 * GetFloat(IAPenaltySp.Q3UnPay2)))
End Sub

Private Sub Q3Pen3_Calculation()
    ReturnVal = CCur(Round((GetFloat(IAPenaltySp.Q3Days3) / 365#) * 0.07 * GetFloat(IAPenaltySp.Q3Unpay3)))
End Sub

Private Sub Q3Pen4_Calculation()
    ReturnVal = CCur(Round((GetFloat(IAPenaltySp.Q3Days4) / 365#) * 0.07 * GetFloat(IAPenaltySp.Q3Unpay4)))
End Sub

Private Sub Q3Unpay1_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA2210Sp.Q1Ln11) + GetCurrency(IA2210Sp.Q2Ln11) + GetCurrency(IA2210Sp.Q3Ln11) - GetCurrency(IA2210Sp.Q1Est) - GetCurrency(IA2210Sp.Q2est) - GetCurrency(IA2210Sp.Q3Est))
End Sub

Private Sub Q3UnPay2_Calculation()
    If GetDate(IAStateEst.SPStQ4Date) < #12/31/2018# Then
        ReturnVal = MaxValue(0, GetCurrency(IAPenaltySp.Q3Unpay1) - GetCurrency(IAStateEst.SPStQ4))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q3Unpay3_Calculation()
    If GetCurrency(IAPenaltySp.Q3UnPay2) > 0 Then
        ReturnVal = GetCurrency(IAPenaltySp.Q3UnPay2)
    ElseIf GetDate(IAStateEst.SPStQ4Date) < #1/1/2019# Then
        ReturnVal = MaxValue(0, GetCurrency(IAPenaltySp.Q3Unpay1) - GetCurrency(IAStateEst.SPStQ4))
    Else
        ReturnVal = GetCurrency(IAPenaltySp.Q3Unpay1)
    End If
End Sub

Private Sub Q3Unpay4_Calculation()
    If GetDate(IAStateEst.SPStQ4Date) > #12/31/2018# And GetDate(IAStateEst.SPStQ4Date) < #1/31/2019# Then
        ReturnVal = MaxValue(0, GetCurrency(IAPenaltySp.Q3Unpay1) - GetCurrency(IAStateEst.SPStQ4))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q4Days1_Calculation()
    ' 89 days max in 2018
    If GetDate(IAStateEst.SPStLateDate) < GetDate(IAF1040.DateDuePaid) And GetCurrency(IAStateEst.SPStLate) > 0 Then
        ReturnVal = MaxValue(0, DaysDiff(GetDate(IAStateEst.SPStLateDate), #1/31/2019#))
    Else
        ReturnVal = MaxValue(0, DaysDiff(GetDate(IAF1040.DateDuePaid), #1/31/2019#))
    End If
End Sub

Private Sub Q4Days2_Calculation()
    If GetDate(IAStateEst.SPStLateDate) < #4/30/2019# And GetCurrency(IAPenaltySp.Q4Unpay2) > 0 Then
        ReturnVal = MaxValue(0, DaysDiff(GetDate(IAF1040.DateDuePaid), GetDate(IAStateEst.SPStLateDate)))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Q4Pen1_Calculation()
    ReturnVal = CCur(Round((GetFloat(IAPenaltySp.Q4Days1) / 365#) * 0.07 * GetFloat(IAPenaltySp.Q4UnPay1)))
End Sub

Private Sub Q4Pen2_Calculation()
    ReturnVal = CCur(Round((GetFloat(IAPenaltySp.Q4Days2) / 365#) * 0.07 * GetFloat(IAPenaltySp.Q4Unpay2)))
End Sub

Private Sub Q4UnPay1_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA2210Sp.Q1Ln11) + GetCurrency(IA2210Sp.Q2Ln11) + GetCurrency(IA2210Sp.Q3Ln11) + GetCurrency(IA2210Sp.Q4Ln11) - GetCurrency(IA2210Sp.Q1Est) - GetCurrency(IA2210Sp.Q2est) - GetCurrency(IA2210Sp.Q3Est) - GetCurrency(IA2210Sp.Q4Est))
End Sub

Private Sub Q4Unpay2_Calculation()
    If GetDate(IAStateEst.SPStLateDate) < #4/30/2019# And GetCurrency(IAStateEst.SPStLate) > 0 Then
        ReturnVal = MaxValue(0, GetCurrency(IAPenaltySp.Q4UnPay1) - GetCurrency(IAStateEst.SPStLate))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SpouseSSN)
End Sub

Private Sub TotPen_Calculation()
    If GetBool(IAF1040.CombMFS) = False Then
        ReturnVal = 0
    Else
        ReturnVal = Round(GetCurrency(IAPenaltySp.Q1Pen1) + GetCurrency(IAPenaltySp.Q1Pen2) + GetCurrency(IAPenaltySp.Q2Pen1) + GetCurrency(IAPenaltySp.Q2Pen2) + GetCurrency(IAPenaltySp.Q3Pen1) + GetCurrency(IAPenaltySp.Q3Pen2) + GetCurrency(IAPenaltySp.Q3Pen3) + GetCurrency(IAPenaltySp.Q3Pen4) + GetCurrency(IAPenaltySp.Q4Pen1) + GetCurrency(IAPenaltySp.Q4Pen2))
    End If
End Sub

