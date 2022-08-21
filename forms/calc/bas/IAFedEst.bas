Private Sub Description_Calculation()
    Dim Total As Currency
    
    Total = GetCurrency(IAFedEst.TPTotEst) + GetCurrency(IAFedEst.SPTotEst)
    
    ReturnVal = CStr(Total)
End Sub

Private Sub Exist_Calculation()
    ReturnVal = 1
End Sub

Private Sub MobDisQual_Calculation()
    If GetCurrency(IAFedEst.TPTotEst) + GetCurrency(IAFedEst.SPTotEst) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.CombNames)
End Sub

Private Sub SPCYEst_Calculation()
    If IAFS() = 3 Then
        ReturnVal = CDollar(GetFloat(IARequired.BProRate) * GetFloat(IAFedEst.TotCYEst))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPName_Calculation()
    ReturnVal = GetString(USWBasicInfo.SPCommon)
End Sub

Private Sub SPPYEst_Calculation()
    If IAFS() = 3 Then
        ReturnVal = CDollar(GetFloat(IARequired.BProRate) * GetFloat(IAFedEst.TotPYEst))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPTotEst_Calculation()
    ReturnVal = GetCurrency(IAFedEst.SPCYEst) + GetCurrency(IAFedEst.SPPYEst)
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

Private Sub TotCYEst_Calculation()
    If GetDate(USWEstPay.Q4Date) < #1/1/2019# Then
        ReturnVal = GetCurrency(USWEstPay.Applied) + GetCurrency(USWEstPay.Q1) + GetCurrency(USWEstPay.Q2) + GetCurrency(USWEstPay.Q3) + GetCurrency(USWEstPay.Q4)
    Else
        ReturnVal = GetCurrency(USWEstPay.Applied) + GetCurrency(USWEstPay.Q1) + GetCurrency(USWEstPay.Q2) + GetCurrency(USWEstPay.Q3)
    End If
End Sub

Private Sub TotPYEst_Calculation()
    If GetDate(USWSpouse.PY4EstDate) > #12/31/2017# Then
        ReturnVal = GetCurrency(USWSpouse.PY4Est) + GetCurrency(USWSpouse.PYLateEst)
    Else
        ReturnVal = GetCurrency(USWSpouse.PYLateEst)
    End If
End Sub

Private Sub TPCYEst_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAFedEst.TotCYEst) - GetCurrency(IAFedEst.SPCYEst))
End Sub

Private Sub TPName_Calculation()
    ReturnVal = GetString(USWBasicInfo.TPCommon)
End Sub

Private Sub TPPYEst_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAFedEst.TotPYEst) - GetCurrency(IAFedEst.SPPYEst))
End Sub

Private Sub TPTotEst_Calculation()
    ReturnVal = GetCurrency(IAFedEst.TPCYEst) + GetCurrency(IAFedEst.TPPYEst)
End Sub

