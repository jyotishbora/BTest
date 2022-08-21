Private Sub Desc_Calculation()
    ReturnVal = CStr(GetCurrency(IAStateEst.TotIAEst))
End Sub

Private Sub Exist_Calculation()
    ReturnVal = 1
End Sub

Private Sub MobDisQual_Calculation()
    If GetCurrency(IAStateEst.TotIAEst) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.CombNames)
End Sub

Private Sub SPIAEst_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IAStateEst.SPStApply) + GetCurrency(IAStateEst.SPStQ1) + GetCurrency(IAStateEst.SPStQ2) + GetCurrency(IAStateEst.SPStQ3) + GetCurrency(IAStateEst.SPStQ4) + GetCurrency(IAStateEst.SPStLate)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPName_Calculation()
    ReturnVal = GetString(USWBasicInfo.SPCommon)
End Sub

Private Sub SPStLateDate_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetDate(IAStateEst.TPStLateDate)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub SPStQ1Date_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetDate(IAStateEst.TPStQ1Date)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub SPStQ2Date_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetDate(IAStateEst.TPStQ2Date)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub SPStQ3Date_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetDate(IAStateEst.TPStQ3Date)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub SPStQ4Date_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetDate(IAStateEst.TPStQ4Date)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

Private Sub StApply_Calculation()
    If GetString(USWEstPay.StName1) = "Iowa" Then
        ReturnVal = GetCurrency(USWEstPay.StApply)
    ElseIf GetString(USWEstPay.StName2) = "Iowa" Then
        ReturnVal = GetCurrency(USWEstPay.St2Apply)
    ElseIf GetString(USWEstPay.StName3) = "Iowa" Then
        ReturnVal = GetCurrency(USWEstPay.St3Apply)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub StLate_Calculation()
    If GetString(USWEstPay.StName1) = "Iowa" Then
        ReturnVal = GetCurrency(USWEstPay.StLate)
    ElseIf GetString(USWEstPay.StName2) = "Iowa" Then
        ReturnVal = GetCurrency(USWEstPay.St2Late)
    ElseIf GetString(USWEstPay.StName3) = "Iowa" Then
        ReturnVal = GetCurrency(USWEstPay.St3Late)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub StQ1_Calculation()
    If GetString(USWEstPay.StName1) = "Iowa" Then
        ReturnVal = GetCurrency(USWEstPay.StQ1)
    ElseIf GetString(USWEstPay.StName2) = "Iowa" Then
        ReturnVal = GetCurrency(USWEstPay.St2Q1)
    ElseIf GetString(USWEstPay.StName3) = "Iowa" Then
        ReturnVal = GetCurrency(USWEstPay.St3Q1)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub StQ2_Calculation()
    If GetString(USWEstPay.StName1) = "Iowa" Then
        ReturnVal = GetCurrency(USWEstPay.StQ2)
    ElseIf GetString(USWEstPay.StName2) = "Iowa" Then
        ReturnVal = GetCurrency(USWEstPay.St2Q2)
    ElseIf GetString(USWEstPay.StName3) = "Iowa" Then
        ReturnVal = GetCurrency(USWEstPay.St3Q2)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub StQ3_Calculation()
    If GetString(USWEstPay.StName1) = "Iowa" Then
        ReturnVal = GetCurrency(USWEstPay.StQ3)
    ElseIf GetString(USWEstPay.StName2) = "Iowa" Then
        ReturnVal = GetCurrency(USWEstPay.St2Q3)
    ElseIf GetString(USWEstPay.StName3) = "Iowa" Then
        ReturnVal = GetCurrency(USWEstPay.St3Q3)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub StQ4_Calculation()
    If GetString(USWEstPay.StName1) = "Iowa" Then
        ReturnVal = GetCurrency(USWEstPay.StQ4)
    ElseIf GetString(USWEstPay.StName2) = "Iowa" Then
        ReturnVal = GetCurrency(USWEstPay.St2Q4)
    ElseIf GetString(USWEstPay.StName3) = "Iowa" Then
        ReturnVal = GetCurrency(USWEstPay.St3Q4)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TotIAEst_Calculation()
    ReturnVal = GetCurrency(IAStateEst.StApply) + GetCurrency(IAStateEst.StQ1) + GetCurrency(IAStateEst.StQ2) + GetCurrency(IAStateEst.StQ3) + GetCurrency(IAStateEst.StQ4) + GetCurrency(IAStateEst.StLate)
End Sub

Private Sub TPName_Calculation()
    ReturnVal = GetString(USWBasicInfo.TPCommon)
End Sub

Private Sub TPStApply_Calculation()
    If IAFS() = 3 Then
        ReturnVal = MaxValue(0, GetCurrency(IAStateEst.StApply) - GetCurrency(IAStateEst.SPStApply))
    Else
        ReturnVal = GetCurrency(IAStateEst.StApply)
    End If
End Sub

Private Sub TPStLate_Calculation()
    If IAFS() = 3 Then
        ReturnVal = MaxValue(0, GetCurrency(IAStateEst.StLate) - GetCurrency(IAStateEst.SPStLate))
    Else
        ReturnVal = GetCurrency(IAStateEst.StLate)
    End If
End Sub

Private Sub TPStLateDate_Calculation()
    If GetString(USWEstPay.StName1) = "Iowa" Then
        ReturnVal = GetDate(USWEstPay.StLateDate)
    ElseIf GetString(USWEstPay.StName2) = "Iowa" Then
        ReturnVal = GetDate(USWEstPay.St2LateDate)
    ElseIf GetString(USWEstPay.StName3) = "Iowa" Then
        ReturnVal = GetDate(USWEstPay.St3LateDate)
    Else
        ReturnVal = #4/30/2019#
    End If
End Sub

Private Sub TPStQ1_Calculation()
    If IAFS() = 3 Then
        ReturnVal = MaxValue(0, GetCurrency(IAStateEst.StQ1) - GetCurrency(IAStateEst.SPStQ1))
    Else
        ReturnVal = GetCurrency(IAStateEst.StQ1)
    End If
End Sub

Private Sub TPStQ1Date_Calculation()
    If GetString(USWEstPay.StName1) = "Iowa" Then
        ReturnVal = GetDate(USWEstPay.StQ1Date)
    ElseIf GetString(USWEstPay.StName2) = "Iowa" Then
        ReturnVal = GetDate(USWEstPay.St2Q1Date)
    ElseIf GetString(USWEstPay.StName3) = "Iowa" Then
        ReturnVal = GetDate(USWEstPay.St3Q1Date)
    Else
        ReturnVal = #4/30/2018#
    End If
End Sub

Private Sub TPStQ2_Calculation()
    If IAFS() = 3 Then
        ReturnVal = MaxValue(0, GetCurrency(IAStateEst.StQ2) - GetCurrency(IAStateEst.SPStQ2))
    Else
        ReturnVal = GetCurrency(IAStateEst.StQ2)
    End If
End Sub

Private Sub TPStQ2Date_Calculation()
    If GetString(USWEstPay.StName1) = "Iowa" Then
        ReturnVal = GetDate(USWEstPay.StQ2Date)
    ElseIf GetString(USWEstPay.StName2) = "Iowa" Then
        ReturnVal = GetDate(USWEstPay.St2Q2Date)
    ElseIf GetString(USWEstPay.StName3) = "Iowa" Then
        ReturnVal = GetDate(USWEstPay.St3Q2Date)
    Else
        ReturnVal = #7/2/2018#
    End If
End Sub

Private Sub TPStQ3_Calculation()
    If IAFS() = 3 Then
        ReturnVal = MaxValue(0, GetCurrency(IAStateEst.StQ3) - GetCurrency(IAStateEst.SPStQ3))
    Else
        ReturnVal = GetCurrency(IAStateEst.StQ3)
    End If
End Sub

Private Sub TPStQ3Date_Calculation()
    If GetString(USWEstPay.StName1) = "Iowa" Then
        ReturnVal = GetDate(USWEstPay.StQ3Date)
    ElseIf GetString(USWEstPay.StName2) = "Iowa" Then
        ReturnVal = GetDate(USWEstPay.St2Q3Date)
    ElseIf GetString(USWEstPay.StName3) = "Iowa" Then
        ReturnVal = GetDate(USWEstPay.St3Q3Date)
    Else
        ReturnVal = #10/1/2018#
    End If
End Sub

Private Sub TPStQ4_Calculation()
    If IAFS() = 3 Then
        ReturnVal = MaxValue(0, GetCurrency(IAStateEst.StQ4) - GetCurrency(IAStateEst.SPStQ4))
    Else
        ReturnVal = GetCurrency(IAStateEst.StQ4)
    End If
End Sub

Private Sub TPStQ4Date_Calculation()
    If GetString(USWEstPay.StName1) = "Iowa" Then
        ReturnVal = GetDate(USWEstPay.StQ4Date)
    ElseIf GetString(USWEstPay.StName2) = "Iowa" Then
        ReturnVal = GetDate(USWEstPay.St2Q4Date)
    ElseIf GetString(USWEstPay.StName3) = "Iowa" Then
        ReturnVal = GetDate(USWEstPay.St3Q4Date)
    Else
        ReturnVal = #1/31/2019#
    End If
End Sub

