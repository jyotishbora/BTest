Private Sub Description_Calculation()
    Dim Total As Currency
    
    Total = GetCurrency(IAAddFedTax.TPTotal) + GetCurrency(IAAddFedTax.SPTotal)
    
    ReturnVal = CStr(Total)
End Sub

Private Sub Exist_Calculation()
    ReturnVal = 1
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.CombNames)
End Sub

Private Sub NetDue_Calculation()
    If GetCurrency(USZIA1040.IAPYNetIncB) = 0 And GetCurrency(USZIA1040.IAPYNetIncA) = 0 Then
        ReturnVal = 0
    Else
        ReturnVal = MaxValue(0, GetCurrency(IAAddFedTax.PyDue) - GetCurrency(IAAddFedTax.PYPen))
    End If
End Sub

Private Sub PyDue_Calculation()
    If GetBool(USWSpouse.NonRes) = True Then
        ReturnVal = GetCurrency(USWRec.PYOweNR)
    Else
        ReturnVal = GetCurrency(USWRec.PYOwe)
    End If
End Sub

Private Sub PYExt_Calculation()
    If GetBool(USWSpouse.NonRes) = True Then    
        ReturnVal = GetCurrency(USWRec.PYExtNR)
    Else
        ReturnVal = GetCurrency(USWRec.PYExt)
    End If
End Sub

Private Sub PYPen_Calculation()
    If GetBool(USWSpouse.NonRes) = True Then    
        ReturnVal = GetCurrency(USWRec.PYPenaltyNR)
    Else
        ReturnVal = GetCurrency(USWRec.PYPenalty)
    End If        
End Sub

Private Sub SPBalDue_Calculation()
    ReturnVal = CDollar(GetFloat(IARequired.PYRatio) * GetFloat(IAAddFedTax.NetDue))
End Sub

Private Sub SPExcFICA_Calculation()
    ReturnVal = GetCurrency(USWFICA.SCredit)
End Sub

Private Sub SPExt_Calculation()
    ReturnVal = CDollar(GetFloat(IARequired.PYRatio) * GetFloat(IAAddFedTax.PYExt))
End Sub

Private Sub SPName_Calculation()
    ReturnVal = GetString(USWBasicInfo.SPCommon)
End Sub

Private Sub SPTotal_Calculation()
    ReturnVal = GetCurrency(IAAddFedTax.SPBalDue) + GetCurrency(IAAddFedTax.SPExt) + GetCurrency(IAAddFedTax.SPFuel) + GetCurrency(IAAddFedTax.SPExcFICA)
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

Private Sub TPBalDue_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAAddFedTax.NetDue) - GetCurrency(IAAddFedTax.SPBalDue))
End Sub

Private Sub TPExcFICA_Calculation()
    ReturnVal = GetCurrency(USWFICA.TCredit)
End Sub

Private Sub TPExt_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAAddFedTax.PYExt) - GetCurrency(IAAddFedTax.SPExt))
End Sub

Private Sub TPFuel_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(USF4136.TotalCredit) - GetCurrency(IAAddFedTax.SPFuel))
End Sub

Private Sub TPName_Calculation()
    ReturnVal = GetString(USWBasicInfo.TPCommon)
End Sub

Private Sub TPTotal_Calculation()
    ReturnVal = GetCurrency(IAAddFedTax.TPBalDue) + GetCurrency(IAAddFedTax.TPExt) + GetCurrency(IAAddFedTax.TPFuel) + GetCurrency(IAAddFedTax.TPExcFICA)
End Sub

