Private Sub Common_Calculation()
    If GetBool(IAF1040.MFJ) = True Then
        ReturnVal = GetString(USWBasicInfo.CombFirst)
    Else
        ReturnVal = GetString(USWBasicInfo.TPCommon)
    End If
End Sub

Private Sub IA133Applied_Calculation()
    ReturnVal = GetCurrency(IA133.NewJobCr)
End Sub

Private Sub IncreaseEmpPerc_Calculation()
    Dim TopLim As Double
    
    If GetFloat(IA133.Base) <= 0 Then
        ReturnVal = 0.10
    Else
        TopLim = Round(GetFloat(IA133.TotEligNewJobs) / GetFloat(IA133.Base), 3)
        ReturnVal = MaxValue(0, TopLim)
    End If
End Sub

Private Sub MEF133SP_Calculation()
    If GetBool(IA133.Spouse) = True And GetBool(IA133.Print) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub MEF133TP_Calculation()
    If GetBool(IA133.Taxpayer) = True And GetBool(IA133.Print) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Names_Calculation()
    If GetBool(IA100.Spouse) = True Then
        ReturnVal = GetString(IARequired.SPCombName)
    Else
        ReturnVal = GetString(IARequired.TPCombName)
    End If
End Sub

Private Sub ProjectJobs_Calculation()
    ReturnVal = GetNumber(IA133.SchATotHours)
End Sub

Private Sub SchATotHours_Calculation()
    Dim count As Integer
    Dim SubTot As Integer

    count = 0
    SubTot = 0

    Do While count < 14
        SubTot = SubTot + GetNumber(IA133.SchAHours(count))
        count = count + 1
    Loop
    
    ReturnVal = SubTot
End Sub

Private Sub SchATotTaxWages_Calculation()
    Dim count As Integer
    Dim SubTot As Currency

    count = 0
    SubTot = 0

    Do While count < 14
        SubTot = SubTot + GetCurrency(IA133.SchATaxWages(count))
        count = count + 1
    Loop
    
    ReturnVal = SubTot
End Sub

Private Sub SpouseCommon_Calculation()
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetString(USWBasicInfo.SPCommon)
    Else
        ReturnVal = "Not Applicable"
    End If
End Sub

Private Sub SSN_Calculation()
    If GetBool(IA100.Spouse) = True Then
        ReturnVal = GetString(IAF1040.SpouseSSN)
    Else
        ReturnVal = GetString(IAF1040.SSN)
    End If
End Sub

Private Sub TotEligNewJobs_Calculation()
    ReturnVal = MinValue(GetNumber(IA133.TotSchBHoursShare), GetNumber(IA133.TotEmplGain))
End Sub

Private Sub TotEmplGain_Calculation()
    ReturnVal = GetNumber(IA133.TotNewJobs) - GetNumber(IA133.Base)
End Sub

Private Sub TotSchBHoursShare_Calculation()
    ReturnVal = GetNumber(IA133.ProjectJobs) + GetNumber(IA133.TotSchAHoursShare)
End Sub

