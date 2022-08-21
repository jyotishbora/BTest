Private Sub Description_Calculation()
    Dim Total As Currency
    
    Total = GetCurrency(IAWPenExc.TPPenExc) + GetCurrency(IAWPenExc.SPPenExc)
    
    ReturnVal = CStr(Total)

End Sub

Private Sub Eligible_Calculation()
    If IAFS() = 2 Or IAFS() = 3 Then
        If GetBool(IAWPenExc.ExTP) = True Or GetBool(IAWPenExc.ExSp) = True Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    ElseIf GetBool(IAWPenExc.ExTP) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub ExSp_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        If GetNumber(USWBasicInfo.SPAgeRec) > 54 Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub ExTP_Calculation()
    If GetNumber(USWBasicInfo.TPAgeRec) > 54 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub MaxExc_Calculation()
    If GetBool(IAWPenExc.Eligible) = True Then
        If IAFS() = 4 Then
            If GetCurrency(IAF1040.SpPenExcl) = 0 And GetBool(IAF1040.NoSpPenExcl) = True Then
                ReturnVal = 12000@
            ElseIf GetCurrency(IAF1040.SpPenExcl) > 0 Then
                ReturnVal = MaxValue(0, 12000@ - GetCurrency(IAF1040.SpPenExcl))
            Else
                ReturnVal = 6000@
            End If
        ElseIf IAFS() = 2 Or IAFS() = 3 Then
            ReturnVal = 12000@
        Else
            ReturnVal = 6000@
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub MinExc_Calculation()
    ReturnVal = MinValue(GetCurrency(IAWPenExc.TotRetire), GetCurrency(IAWPenExc.MaxExc))
End Sub

Private Sub MobDisQual_Calculation()
    If GetCurrency(IAWPenExc.TPPenExc) + GetCurrency(IAWPenExc.SPPenExc) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.CombNames)
End Sub

Private Sub NREligible_Calculation()
    If IAFS() = 2 Or IAFS() = 3 Then
        If GetBool(IAWPenExc.NRExTP) = True Or GetBool(IAWPenExc.NRExSp) = True Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    ElseIf GetBool(IAWPenExc.NRExTP) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub NRExSp_Calculation()
    If GetBool(IAF126.SpPYRes) = True And GetBool(IAWPenExc.ExSp) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub NRExTP_Calculation()
    If GetBool(IAF126.TpPYRes) = True And GetBool(IAWPenExc.ExTP) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub NRMaxExc_Calculation()
    If GetBool(IAWPenExc.NREligible) = True Then
        ReturnVal = GetCurrency(IAWPenExc.MaxExc)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub NRMinExc_Calculation()
    ReturnVal = MinValue(GetCurrency(IAWPenExc.NRTotRetire), GetCurrency(IAWPenExc.NRMaxExc))
End Sub

Private Sub NRSPIRA_Calculation()
    If GetBool(IAF126.SpPYRes) = True Then
        ReturnVal = GetCurrency(IAWPenExc.SPIRA)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub NRSPPenExc_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWPenExc.NRMinExc) - GetCurrency(IAWPenExc.NRTPPenExc))
End Sub

Private Sub NRSPPensions_Calculation()
    If GetBool(IAF126.SpPYRes) = True Then
        ReturnVal = GetCurrency(IAWPenExc.SPPensions)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub NRSPRatio_Calculation()
    If GetCurrency(IAWPenExc.NRTotRetire) = 0 Then
        ReturnVal = 0
    ElseIf GetBool(IAF126.SpPYRes) = True Then
        ReturnVal = MaxValue(0, 1# - GetFloat(IAWPenExc.NRTPRatio))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub NRSPRetire_Calculation()
    If GetBool(IARequired.AskSpouse) = True And GetBool(IAWPenExc.NRExSp) = True Then
        ReturnVal = GetCurrency(IAWPenExc.NRSPIRA) + GetCurrency(IAWPenExc.NRSPPensions)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub NRTotRetire_Calculation()
    ReturnVal = GetCurrency(IAWPenExc.NRTPRetire) + GetCurrency(IAWPenExc.NRSPRetire)
End Sub

Private Sub NRTPIRA_Calculation()
    If GetBool(IAF126.TpPYRes) = True Then
        ReturnVal = GetCurrency(IAWPenExc.TPIRA)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub NRTPPenExc_Calculation()
    ReturnVal = CDollar(GetFloat(IAWPenExc.NRMinExc) * GetFloat(IAWPenExc.NRTPRatio))
End Sub

Private Sub NRTPPensions_Calculation()
    If GetBool(IAF126.TpPYRes) = True Then
        ReturnVal = GetCurrency(IAWPenExc.TPPensions)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub NRTPRatio_Calculation()
    If GetCurrency(IAWPenExc.NRTotRetire) = 0 Then
        ReturnVal = 0
    Else
        ReturnVal = MinValue(1#, GetFloat(IAWPenExc.NRTPRetire) / GetFloat(IAWPenExc.NRTotRetire))
    End If
End Sub

Private Sub NRTPRetire_Calculation()
    If GetBool(IAWPenExc.NRExTP) = True Then
        ReturnVal = GetCurrency(IAWPenExc.NRTPIRA) + GetCurrency(IAWPenExc.NRTPPensions)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPIRA_Calculation()
'See Expanded instructions on Iowa website for 'Taxable IRA Distributions Step 5 Gross Income'. In 2016 QCD was to be added back to IA income and then were allowed a deduction on line 21
'For 2018 the expanded instructions say Iowa has conformed, no addback needed
'Extender: + GetCurrency(USWRetirement.SPAddQCD)
    ReturnVal = GetCurrency(USWRec.SIRAInc)
End Sub

Private Sub SPMilPen_Calculation()
    Dim Count1 As Long
    Dim MilPen As Currency
    
    Count1 = 1
    MilPen = 0
    
    Do While Count1 <= GetAllCopies(USD1099R)
        If GetBool(USD1099R.MilPen, Count1) = True And GetBool(USD1099R.Spouse, Count1) = True Then
            MilPen = MilPen + Round(GetCurrency(USD1099R.PenTax, Count1))
        Else
            MilPen = MilPen
        End If
        Count1 = Count1 + 1
    Loop
    
    ReturnVal = Round(MilPen)

End Sub

Private Sub SPName_Calculation()
    ReturnVal = GetString(USWBasicInfo.SPCommon)
End Sub

Private Sub SPName2_Calculation()
    ReturnVal = GetString(USWBasicInfo.SPCommon)
End Sub

Private Sub SPPenExc_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWPenExc.MinExc) - GetCurrency(IAWPenExc.TPPenExc))
End Sub

Private Sub SPPensions_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(USWRec.SPension) - GetCurrency(IAWPenExc.SPMilPen) - Round(GetCurrency(USDRRB1099R.PenTax, FieldCopies(USDRRB1099R.Spouse))))
End Sub

Private Sub SPRatio_Calculation()
    If GetCurrency(IAWPenExc.TotRetire) = 0 Then
        ReturnVal = 0
    Else
        ReturnVal = MaxValue(0, 1# - GetFloat(IAWPenExc.TPRatio))
    End If
End Sub

Private Sub SPRetire_Calculation()
    If GetBool(IARequired.AskSpouse) = True And GetBool(IAWPenExc.ExSp) = True Then
        ReturnVal = GetCurrency(IAWPenExc.SPIRA) + GetCurrency(IAWPenExc.SPPensions)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

Private Sub TotRetire_Calculation()
    ReturnVal = GetCurrency(IAWPenExc.TPRetire) + GetCurrency(IAWPenExc.SPRetire)
End Sub

Private Sub TPIRA_Calculation()
'See Expanded instructions on Iowa website for 'Taxable IRA Distributions Step 5 Gross Income'. In 2016 QCD was to be added back to IA income and then were allowed a deduction on line 21
'For 2018 the expanded instructions say Iowa has conformed, no addback needed
'Extender: + GetCurrency(USWRetirement.TPAddQCD)
    ReturnVal = GetCurrency(USWRec.TIRAInc)
End Sub

Private Sub TPMilPen_Calculation()
    Dim Count1 As Long
    Dim MilPen As Currency
    
    Count1 = 1
    MilPen = 0
    
    Do While Count1 <= GetAllCopies(USD1099R)
        If GetBool(USD1099R.MilPen, Count1) = True And GetBool(USD1099R.Taxpayer, Count1) = True Then
            MilPen = MilPen + Round(GetCurrency(USD1099R.PenTax, Count1))
        Else
            MilPen = MilPen
        End If
        Count1 = Count1 + 1
    Loop
    
    ReturnVal = Round(MilPen)
End Sub

Private Sub TPName_Calculation()
    ReturnVal = GetString(USWBasicInfo.TPCommon)
End Sub

Private Sub TPName2_Calculation()
    ReturnVal = GetString(USWBasicInfo.TPCommon)
End Sub

Private Sub TPPenExc_Calculation()
    ReturnVal = CDollar(GetFloat(IAWPenExc.MinExc) * GetFloat(IAWPenExc.TPRatio))
End Sub

Private Sub TPPensions_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(USWRec.TPension) - GetCurrency(IAWPenExc.TPMilPen) - Round(GetCurrency(USDRRB1099R.PenTax, FieldCopies(USDRRB1099R.Taxpayer))))
End Sub

Private Sub TPRatio_Calculation()
    If GetCurrency(IAWPenExc.TotRetire) = 0 Then
        ReturnVal = 0
    Else
        ReturnVal = MinValue(1#, GetFloat(IAWPenExc.TPRetire) / GetFloat(IAWPenExc.TotRetire))
    End If
End Sub

Private Sub TPRetire_Calculation()
    If GetBool(IAWPenExc.ExTP) = True Then
        ReturnVal = GetCurrency(IAWPenExc.TPIRA) + GetCurrency(IAWPenExc.TPPensions)
    Else
        ReturnVal = 0
    End If
End Sub

