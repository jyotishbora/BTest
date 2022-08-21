Private Sub Description_Calculation()
    Dim Total As Currency
    
    Total = GetCurrency(IASETax.TPTotal) + GetCurrency(IASETax.SPTotal)
    
    ReturnVal = CStr(Total)
End Sub

Private Sub Exist_Calculation()
    ReturnVal = 1
End Sub

Private Sub MobDisQual_Calculation()
    If GetCurrency(IASETax.TPTotal) + GetCurrency(IASETax.SPTotal) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.CombNames)
End Sub

Private Sub SPHH_Calculation()
    If GetBool(USSchH.Taxpayer) = True Then
        ReturnVal = 0
    ElseIf GetBool(USWResidency.F1040NR) = True Then
        ReturnVal = 0
    ElseIf GetBool(USSchH.Spouse) = True Then
        ReturnVal = GetCurrency(USW1040Supp.HTax)
    Else
        ReturnVal = CDollar(GetFloat(USW1040Supp.HTax) * 0.5)
    End If
End Sub

Private Sub SPName_Calculation()
    ReturnVal = GetString(USWBasicInfo.SPCommon)
End Sub

Private Sub SPRetTax_Calculation()
    ReturnVal = GetCurrency(USF5329Spouse.TotAddTax)
End Sub

Private Sub SPSE_Calculation()
    If GetBool(USSchSESpouse.ShortSE) = True Then
        ReturnVal = GetCurrency(USSchSESpouse.ASETax)
    Else
        ReturnVal = GetCurrency(USSchSESpouse.BSETax)
    End If
End Sub

Private Sub SPTipTax_Calculation()
    ReturnVal = GetCurrency(USF4137Spouse.AddLnTen) + GetCurrency(USF8919Spouse.TotTax)
End Sub

Private Sub SPTotal_Calculation()
    ReturnVal = GetCurrency(IASETax.SPRepayPTC) + GetCurrency(IASETax.SPSE) + GetCurrency(IASETax.SPTipTax) + GetCurrency(IASETax.SPRetTax) + GetCurrency(IASETax.SPHH) + GetCurrency(IASETax.SPHomeBuyRepay) + GetCurrency(IASETax.SpHlthCarePen) + GetCurrency(IASETax.SPTotAddMedTax) + GetCurrency(IASETax.SPOthTax)
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

Private Sub TPHH_Calculation()
    If GetBool(USWResidency.F1040NR) = True Then
        ReturnVal = GetCurrency(USF1040NR.SchHTax)
    ElseIf GetBool(USSchH.Spouse) = True Then
        ReturnVal = 0
    Else
        ReturnVal = MaxValue(0, GetCurrency(USW1040Supp.HTax) - GetCurrency(IASETax.SPHH))
    End If
End Sub

Private Sub TPHlthCarePen_Calculation()
    If GetBool(USWResidency.F1040NR) = True Then
        ReturnVal = 0
    Else
        ReturnVal = MaxValue(0, GetCurrency(USF1040.HlthCarePen) - GetCurrency(IASETax.SpHlthCarePen))
    End If
End Sub

Private Sub TPHomeBuyRepay_Calculation()
    If GetBool(USWResidency.F1040NR) = True Then
        ReturnVal = GetCurrency(USF1040NR.HomeBuyRepay)
    Else
        ReturnVal = MaxValue(0, GetCurrency(USF1040.HomeBuyRepay) - GetCurrency(IASETax.SPHomeBuyRepay))
    End If
End Sub

Private Sub TPName_Calculation()
    ReturnVal = GetString(USWBasicInfo.TPCommon)
End Sub

Private Sub TPOthTax_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(USWOthTax.TotOthTax) - GetCurrency(IASETax.SPOthTax))
End Sub

Private Sub TPRepayPTC_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(USF8962.PTCRepay) - GetCurrency(IASETax.SPRepayPTC))
End Sub

Private Sub TPRetTax_Calculation()
    ReturnVal = GetCurrency(USF5329.TotAddTax)
End Sub

Private Sub TPSE_Calculation()
    If GetBool(USSchSE.ShortSE) = True Then
        ReturnVal = GetCurrency(USSchSE.ASETax)
    Else
        ReturnVal = GetCurrency(USSchSE.BSETax)
    End If
End Sub

Private Sub TPTipTax_Calculation()
    ReturnVal = GetCurrency(USF4137.AddLnTen) + GetCurrency(USF8919.TotTax)
End Sub

Private Sub TPTotAddMedTax_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(USF8959.TotAddMedTax) - GetCurrency(IASETax.SPTotAddMedTax))
End Sub

Private Sub TPTotal_Calculation()
    ReturnVal = GetCurrency(IASETax.TPRepayPTC) + GetCurrency(IASETax.TPSE) + GetCurrency(IASETax.TPTipTax) + GetCurrency(IASETax.TPRetTax) + GetCurrency(IASETax.TPHH) + GetCurrency(IASETax.TPHomeBuyRepay) + GetCurrency(IASETax.TPHlthCarePen) + GetCurrency(IASETax.TPTotAddMedTax) + GetCurrency(IASETax.TPOthTax)
End Sub

