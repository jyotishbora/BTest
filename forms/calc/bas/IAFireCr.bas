Private Sub Description_Calculation()
    Dim Total As Currency
    
    Total = GetCurrency(IAFireCr.SPTotCr) + GetCurrency(IAFireCr.TPTotCr)
    
    ReturnVal = CStr(Total)
End Sub

Private Sub MobDisQual_Calculation()
    If GetCurrency(IAFireCr.SPTotCr) + GetCurrency(IAFireCr.TPTotCr) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.CombNames)
End Sub

Private Sub SPName_Calculation()
    ReturnVal = GetString(USWBasicInfo.SPCommon)
End Sub

Private Sub SPTotCr_Calculation()
' updated for 2018
    If GetBool(IAFireCr.SPQual) = True And GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = MinValue(100@, CDollar(GetFloat(IAFireCr.SPMonths) * 834#))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

Private Sub TPName_Calculation()
    ReturnVal = GetString(USWBasicInfo.TPCommon)
End Sub

Private Sub TPTotCr_Calculation()
' updated for 2018
    If GetBool(IAFireCr.TPQual) = True Then
        ReturnVal = MinValue(100@, CDollar(GetFloat(IAFireCr.TPMonths) * 834#))
    Else
        ReturnVal = 0
    End If
End Sub

