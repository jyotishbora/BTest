Private Sub Description_Calculation()
    Dim Total As Currency
    
    Total = GetCurrency(IAFedRef.TPST) + GetCurrency(IAFedRef.SPST)
    
    ReturnVal = CStr(Total)
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.CombNames)
End Sub

Private Sub NetRef_Calculation()
    If GetBool(IAFedRef.PYNR) = True Then
        ReturnVal = 0
    Else
        ReturnVal = MaxValue(0, GetCurrency(IAFedRef.PyRef) - GetCurrency(IAFedRef.PYEIC) - GetCurrency(IAFedRef.PYAddCTC) - GetCurrency(IAFedRef.PYRefHopeCr) - GetCurrency(IAFedRef.PYPTC))
    End If
End Sub

Private Sub PYAddCTC_Calculation()
    If GetBool(USWSpouse.NonRes) = True Then
        ReturnVal = GetCurrency(USWRec.PYAddCTCNR)
    Else
        ReturnVal = GetCurrency(USWRec.PYAddCTC)
    End If        
End Sub

Private Sub PYEIC_Calculation()
    ReturnVal = GetCurrency(USWRec.PYEIC)
End Sub

Private Sub PYNR_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        If (GetBool(IAF126.TpPYRes) = True And GetDate(IAF126.TpDateIn) > #12/31/2017#) And (GetBool(IAF126.SpPYRes) = True And GetDate(IAF126.SpDateIn) > #12/31/2017#) Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    ElseIf (GetBool(IAF126.TpPYRes) = True And GetDate(IAF126.TpDateIn) > #12/31/2017#) Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PYPTC_Calculation()
    If GetBool(USWSpouse.NonRes) = True Then
        ReturnVal = GetCurrency(USWRec.PYNPTCNR)
    Else
        ReturnVal = GetCurrency(USWRec.PYNPTC)
    End If
End Sub

Private Sub PyRef_Calculation()
    If GetBool(USWSpouse.NonRes) = True Then    
        ReturnVal = GetCurrency(USWRec.PYRefNR)
    Else
        ReturnVal = GetCurrency(USWRec.PYRef)
    End If
End Sub

Private Sub PYRefHopeCr_Calculation()
    ReturnVal = GetCurrency(USWRec.PYRefHopeCr)
End Sub

Private Sub SPName_Calculation()
    ReturnVal = GetString(USWBasicInfo.SPCommon)
End Sub

Private Sub SPST_Calculation()
    ReturnVal = CDollar(GetFloat(IARequired.PYRatio) * GetFloat(IAFedRef.NetRef))
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

Private Sub TPName_Calculation()
    ReturnVal = GetString(USWBasicInfo.TPCommon)
End Sub

Private Sub TPST_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAFedRef.NetRef) - GetCurrency(IAFedRef.SPST))
End Sub

