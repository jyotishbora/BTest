Private Sub ATax_Calculation()
    If GetNumber(IAWkAltTax.ProRate) = 1 Then
        ReturnVal = CDollar(GetFloat(IAWkAltTax.Lesser) * GetFloat(IAWkAltTax.BProRate))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BProRate_Calculation()
    If GetNumber(IAWkAltTax.ProRate) = 1 Then
        If GetCurrency(IAWkAltTax.SPModNI) < 0 And GetCurrency(IAWkAltTax.TPModNI) < 0 Then
            If GetCurrency(IAWkAltTax.TPModNI) < GetCurrency(IAWkAltTax.SPModNI) Then
                ReturnVal = 0
            Else
                ReturnVal = 1
            End If
        ElseIf GetCurrency(IAWkAltTax.TPModNI) < 0 Then
            ReturnVal = 0
        ElseIf GetCurrency(IAWkAltTax.TPModNI) > 0 And GetCurrency(IAWkAltTax.TotAdjIANetInc) <= 0 Then
            ReturnVal = 1
        ElseIf GetCurrency(IAWkAltTax.TotAdjIANetInc) = 0 Then
            ReturnVal = 0
        Else
            ReturnVal = MaxValue(0, (MinValue(1#, Round(GetFloat(IAWkAltTax.TPModNI) / GetFloat(IAWkAltTax.TotAdjIANetInc), 3))))
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BTax_Calculation()
    If GetNumber(IAWkAltTax.ProRate) = 1 Then
        ReturnVal = GetCurrency(IAWkAltTax.Lesser) - GetCurrency(IAWkAltTax.ATax)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Description_Calculation()
    ReturnVal = CStr(GetCurrency(IAWkAltTax.Lesser))
End Sub

Private Sub IncLimit_Calculation()
    If GetBool(IAF1040.Over65) = True Then
        ReturnVal = 32000@
    Else
        ReturnVal = 13500@
    End If
End Sub

Private Sub Lesser_Calculation()
    If GetBool(IAWkAltTax.Qualify) = True Then
        ReturnVal = MinValue(GetCurrency(IAWkAltTax.Mult), GetCurrency(IAWkAltTax.Tables))
    Else
        ReturnVal = GetCurrency(IAWkAltTax.Tables)
    End If
End Sub

Private Sub Ln26_Calculation()
    ReturnVal = GetCurrency(IAWkAltTax.TotSPLine1) + GetCurrency(IAWkAltTax.TotLine1)
End Sub

Private Sub LumpSum_Calculation()
    ReturnVal = GetCurrency(USF4972.TPCapGain) + GetCurrency(USF4972.TPTaxAmt)
End Sub

Private Sub Mult_Calculation()
    ReturnVal = CDollar(GetFloat(IAWkAltTax.Sub1) * 0.0898)
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.CombNames)
End Sub

Private Sub NetInc_Calculation()
    ReturnVal = GetCurrency(IAF1040.ANet)
End Sub

Private Sub PenExcl_Calculation()
    ReturnVal = GetCurrency(IAF1040.APenExcl)
End Sub

Private Sub ProRate_Calculation()
    If IAFS() = 3 Or IAFS() = 4 Then
        If (GetCurrency(IAWkAltTax.Mult) < GetCurrency(IAWkAltTax.Tables)) And GetBool(IAWkAltTax.Qualify) = True Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Qualify_Calculation()
    Dim NoMFSQual As Long
    
    If GetCurrency(IAF1040.SpIncome) = 0 And GetBool(IAF1040.NoMFSInc) = False Then
        NoMFSQual = 1
    Else
        NoMFSQual = 0
    End If

    If IAFS() = 1 Then
        ReturnVal = 0
    ElseIf GetBool(IARequired.AskFilStat) = True And GetBool(IAWkAltTax.NOL) = True Then
        ReturnVal = 0
    ElseIf IAFS() = 4 And NoMFSQual = 1 Then
        ReturnVal = 0
    Else
        ReturnVal = 1
    End If
End Sub

Private Sub SPLumpSum_Calculation()
'probably should ask for the form 4972 amounts on the IA 1040 under the filing status 4 section, however for the number of users that will fall in this situation not going to add this year.
    If IAFS() = 4 Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(USF4972Spouse.TPCapGain) + GetCurrency(USF4972Spouse.TPTaxAmt)
    End If
End Sub

Private Sub SPModNI_Calculation()
    If GetNumber(IAWkAltTax.ProRate) = 1 Then
        ReturnVal = GetCurrency(IAWkAltTax.TotSPLine1)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPNetInc_Calculation()
    If IAFS() = 4 Then
        ReturnVal = GetCurrency(IAF1040.SpIncome)
    Else
        ReturnVal = GetCurrency(IAF1040.BNet)
    End If
End Sub

Private Sub SPPenExcl_Calculation()
    If IAFS() = 4 Then
        ReturnVal = GetCurrency(IAF1040.SpPenExcl)
    Else
        ReturnVal = GetCurrency(IAF1040.BPenExcl)
    End If
End Sub

Private Sub SPSSB_Calculation()
    If IAFS() = 4 Then
        ReturnVal = GetCurrency(IAF1040.SpSSB)
    Else
        ReturnVal = GetCurrency(IAF1040.BRepSSB)
    End If
End Sub

Private Sub SSB_Calculation()
    ReturnVal = GetCurrency(IAF1040.ARepSSB)
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

Private Sub Sub1_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWkAltTax.Ln26) - GetCurrency(IAWkAltTax.IncLimit))
End Sub

Private Sub Tables_Calculation()
    ReturnVal = GetCurrency(IAF1040.ARegTax) + GetCurrency(IAF1040.BRegTax)
End Sub

Private Sub TotAdjIANetInc_Calculation()
    ReturnVal = GetCurrency(IAWkAltTax.SPModNI) + GetCurrency(IAWkAltTax.TPModNI)
End Sub

Private Sub TotLine1_Calculation()
    ReturnVal = GetCurrency(IAWkAltTax.NetInc) + GetCurrency(IAWkAltTax.PenExcl) + GetCurrency(IAWkAltTax.SSB) + GetCurrency(IAWkAltTax.LumpSum)
End Sub

Private Sub TotSPLine1_Calculation()
    ReturnVal = GetCurrency(IAWkAltTax.SPNetInc) + GetCurrency(IAWkAltTax.SPPenExcl) + GetCurrency(IAWkAltTax.SPSSB) + GetCurrency(IAWkAltTax.SPLumpSum)
End Sub

Private Sub TPModNI_Calculation()
    If GetNumber(IAWkAltTax.ProRate) = 1 Then
        ReturnVal = GetCurrency(IAWkAltTax.TotLine1)
    Else
        ReturnVal = 0
    End If
End Sub

