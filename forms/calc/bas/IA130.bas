Private Sub Alert10_Calculation()
    If GetBool(IA130.MEF130TP) = True And Trim(GetString(IA130.EFTPState)) = "" Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert20_Calculation()
    If GetBool(IA130.MEF130SP) = True And Trim(GetString(IA130.EFTPState)) = "" Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Common_Calculation()
    If GetBool(IAF1040.MFJ) = True Then
        ReturnVal = GetString(USWBasicInfo.CombFirst)
    Else
        ReturnVal = GetString(USWBasicInfo.TPCommon)
    End If
End Sub

Private Sub Credit_Calculation()
    ReturnVal = GetCurrency(IA130.Small) + GetCurrency(IA130.PY130Cr)
End Sub

Private Sub Description_Calculation()
    Dim Total As Currency
    
    Total = GetCurrency(IA130.Small) + GetCurrency(IA130.PY130Cr)
    
    ReturnVal = CStr(Total) & " Credit"
End Sub

Private Sub Div_Calculation()
    Dim TopLim As Double
        
    If GetCurrency(IA130.Inc15) = 0 Then
        ReturnVal = 0
    Else
        TopLim = MinValue(1#, Round(GetFloat(IA130.GrInc) / GetFloat(IA130.Inc15), 3))
        ReturnVal = MaxValue(0, TopLim) 
    End If
End Sub

Private Sub EFTPState_Calculation()
    If Trim(GetString(IA130.YouFC)) <> "" Then
        ReturnVal = ForeignCode(Trim(GetString(IA130.YouFC)))
    Else
        ReturnVal = GetString(IA130.YouState)
    End If
End Sub

Private Sub Exist_Calculation()
    ReturnVal = 1
End Sub

Private Sub Inc15_Calculation()
    If GetBool(IA130.TPRes) = True Then
        ReturnVal = GetCurrency(IAF1040.AGross)
    ElseIf GetBool(IA130.TPPY) = True Then
        ReturnVal = GetCurrency(IAF126.GrossInc)
    ElseIf GetBool(IA130.SPRes) = True Then
        ReturnVal = GetCurrency(IAF1040.BGross)
    ElseIf GetBool(IA130.SPPY) = True Then
        ReturnVal = GetCurrency(IAF126.BGross)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub MEF130SP_Calculation()
    If GetBool(IA130.SPRes) = True And GetCurrency(IA130.Small) <> 0 Then
        ReturnVal = 1
    ElseIf GetBool(IA130.SPPY) = True And GetCurrency(IA130.PY130Cr) <> 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub MEF130TP_Calculation()
    If GetBool(IA130.TPRes) = True And GetCurrency(IA130.Small) <> 0 Then
        ReturnVal = 1
    ElseIf GetBool(IA130.TPPY) = True And GetCurrency(IA130.PY130Cr) <> 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Mult_Calculation()
    ReturnVal = CDollar(GetFloat(IA130.Div) * GetFloat(IA130.Tax55))
End Sub

Private Sub Names_Calculation()
    If GetBool(IAF1040.CombMFS) = True Then
        If GetBool(IA130.Spouse) = True Then
            ReturnVal = GetString(IARequired.SPCombName)
        Else
            ReturnVal = GetString(IARequired.TPCombName)
        End If
    Else
        ReturnVal = GetString(IARequired.CombNames)
    End If
End Sub

Private Sub PartYear_Calculation()
    If GetNumber(IA130.TPPY) > 0 Or GetNumber(IA130.SPPY) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PrintMe_Calculation()
    If GetCurrency(IA130.Small) + GetCurrency(IA130.PY130Cr) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PY130Cr_Calculation()
    If GetBool(IA130.TPPY) = True Or GetBool(IA130.SPPY) = True Then
        ReturnVal = MinValue(GetCurrency(IA130.Mult), GetCurrency(IA130.PYTax))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PYPer_Calculation()
    Dim TopLim As Double
        
    If GetBool(IA130.TPPY) = True Or GetBool(IA130.SPPY) = True Then
        If GetFloat(IA130.PYSmall) = 0 Then
            ReturnVal = 0
        Else
            TopLim = MinValue(1#, Round(GetFloat(IA130.GrInc) / GetFloat(IA130.PYSmall), 3))
            ReturnVal = MaxValue(0, TopLim)                        
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PYTax_Calculation()
    If GetBool(IA130.TPPY) = True Or GetBool(IA130.SPPY) = True Then
        ReturnVal = CDollar(GetFloat(IA130.OthTax) * GetFloat(IA130.PYPer))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Small_Calculation()
    If GetBool(IA130.TPRes) = True Or GetBool(IA130.SPRes) = True Then
        ReturnVal = MinValue(GetCurrency(IA130.Mult), GetCurrency(IA130.OthTax))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPCredit_Calculation()
    If GetNumber(IA130.SPRes) > 0 Or GetNumber(IA130.SPPY) > 0 Then
        ReturnVal = GetCurrency(IA130.Small) + GetCurrency(IA130.PY130Cr)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SpouseCommon_Calculation()
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetString(USWBasicInfo.SPCommon)
    Else
        ReturnVal = "Not Applicable"
    End If
End Sub

Private Sub SPPY_Calculation()
    If GetBool(IAF1040.CombMFS) = True And GetBool(IAF126.SpPYRes) = True And GetBool(IA130.Spouse) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPRes_Calculation()
    If GetBool(IAF1040.CombMFS) = True And GetBool(IA130.Spouse) = True Then
        If GetBool(IAF126.Exist) = False Then
            ReturnVal = 1
        ElseIf GetBool(IAF126.SpRes) = True Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SSN_Calculation()
    If GetBool(IA130.Spouse) = True Then
        ReturnVal = GetString(IAF1040.SpouseSSN)
    Else
        ReturnVal = GetString(IAF1040.SSN)
    End If
End Sub

Private Sub Tax55_Calculation()
    If GetBool(IA130.TPRes) = True Or GetBool(IA130.TPPY) = True Then
        ReturnVal = MaxValue(0, GetCurrency(IAF1040.ABal2) - (GetCurrency(IAF1040.ALump) + GetCurrency(IAF1040.AIAMin)))
    ElseIf GetBool(IA130.SPRes) = True Or GetBool(IA130.SPPY) = True Then
        ReturnVal = MaxValue(0, GetCurrency(IAF1040.BBal2) - (GetCurrency(IAF1040.BLump) + GetCurrency(IAF1040.BIAMin)))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPCredit_Calculation()
    If GetNumber(IA130.TPRes) > 0 Or GetNumber(IA130.TPPY) > 0 Then
        ReturnVal = GetCurrency(IA130.Small) + GetCurrency(IA130.PY130Cr)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPPY_Calculation()
    If GetBool(IA130.Spouse) = True Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.MFJ) = True Then
        If GetBool(IAF126.TpPYRes) = True Or GetBool(IAF126.SpPYRes) = True Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    ElseIf GetBool(IAF126.TpPYRes) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPRes_Calculation()
    Dim Only1NR As Long
    
    If GetBool(IAF126.TpNonRes) = True And GetBool(IAF126.SPRes) = True Then
        Only1NR = 1
    ElseIf GetBool(IAF126.TPRes) = True And GetBool(IAF126.SpNonRes) = True Then
        Only1NR = 1
    Else
        Only1NR = 0
    End If

    If GetBool(IA130.Spouse) = True Then
        ReturnVal = 0
    ElseIf GetBool(IAF126.Exist) = False Then
        ReturnVal = 1
    ElseIf GetBool(IAF1040.MFJ) = True And Only1NR = 1 Then
        ReturnVal = 1
    ElseIf GetBool(IAF1040.MFJ) = True And GetBool(IAF126.TPRes) = True And GetBool(IAF126.SPRes) = True Then
        ReturnVal = 1
    ElseIf GetBool(IAF1040.MFJ) <> True And GetBool(IAF126.TPRes) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

