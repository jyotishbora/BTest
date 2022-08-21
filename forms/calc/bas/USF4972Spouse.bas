Private Sub ActValue_Calculation()
    Dim ActValue As Currency
    Dim count As Integer
    
    count = 1
    ActValue = 0
    
    Do While count <= GetAllCopies(USD1099R)
        If GetBool(USD1099R.Qual4972, count) = True And GetBool(USD1099R.Spouse, count) = True Then
            ActValue = ActValue + Round(GetCurrency(USD1099R.Other, count))
        Else
            ActValue = ActValue
        End If
        count = count + 1
    Loop
    
    If GetBool(USF4972Spouse.UseForm) = True And GetBool(USF4972Spouse.Choose10Year) = True Then
        If GetBool(USF4972Spouse.MRD) = True And GetBool(USF4972Spouse.Box8Perc) <> 0 Then
            ReturnVal = CCur(ActValue / (GetFloat(USF4972Spouse.Box8Perc) / 100#))
        Else
            ReturnVal = ActValue
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AdjTotTaxable_Calculation()
    If GetBool(USF4972Spouse.UseForm) = True And GetBool(USF4972Spouse.Choose10Year) = True Then
        ReturnVal = GetCurrency(USF4972Spouse.TotTaxable) + GetCurrency(USF4972Spouse.ActValue)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert10_Calculation()
    Dim count As Integer
    Dim Hit As Long
    
    count = 1
    Hit = 0
    
    Do While count <= GetAllCopies(USD1099R)
        If GetBool(USD1099R.Spouse, count) = True And GetBool(USD1099R.Qual4972, count) = True Then
            Hit = Hit + 1
        Else
            Hit = Hit
        End If
        count = count + 1
    Loop
    
    If GetBool(USF4972Spouse.UseForm) = True And GetBool(USF4972Spouse.ChooseCapGain) = False And GetBool(USF4972Spouse.Choose10Year) = False And Hit <> 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert20_Calculation()
    Dim count As Integer
    Dim Hit As Long
    
    count = 1
    Hit = 0
    
    Do While count <= GetAllCopies(USD1099R)
        If GetBool(USD1099R.Spouse, count) = True And GetBool(USD1099R.Qual4972, count) = True Then
            Hit = Hit + 1
        Else
            Hit = Hit
        End If
        count = count + 1
    Loop
    
    If GetNumber(USF4972Spouse.Print) = 1 And Hit > 1 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert30_Calculation()
    ReturnVal = 0
End Sub

Private Sub Alert40_Calculation()
    ReturnVal = 0
End Sub

Private Sub Alert5_Calculation()
    If GetNumber(USWRetirement.SP4972) = 1 And GetStatus(UserModifiedStatus) = False Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert50_Calculation()
    If GetBool(USF4972Spouse.MRD) = True And GetBool(USF4972Spouse.Choose10Year) = True And GetBool(USF4972Spouse.UseForm) = True And GetFloat(USF4972Spouse.Box9aPerc) = 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert60_Calculation()
    Dim count As Integer
    Dim Hit As Long
    
    count = 1
    Hit = 0
    
    Do While count <= GetAllCopies(USD1099R)
        If GetCurrency(USD1099R.Other, count) > 0 And GetBool(USD1099R.Spouse, count) = True And GetBool(USD1099R.Qual4972, count) = True Then
            Hit = Hit + 1
        Else
            Hit = Hit
        End If
        count = count + 1
    Loop
    
    If GetBool(USF4972Spouse.MRD) = True And GetBool(USF4972Spouse.Choose10Year) = True And GetBool(USF4972Spouse.UseForm) = True Then
        If Hit <> 0 And GetFloat(USF4972Spouse.Box8Perc) = 0 Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert70_Calculation()
    ReturnVal = 0
End Sub

Private Sub CapGain_Calculation()
    Dim Estate As Currency

    Estate = CDollar(GetCurrency(USF4972Spouse.EstateTax) * GetFloat(USF4972Spouse.DBWC))
    
    If GetBool(USF4972Spouse.UseForm) = True And GetBool(USF4972Spouse.ChooseCapGain) = True Then
        ReturnVal = MaxValue(0, GetCurrency(USF4972Spouse.DBWF) - Estate)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CapGainTax_Calculation()
    ReturnVal = CDollar(GetCurrency(USF4972Spouse.CapGain) * 0.2)
End Sub

Private Sub Common_Calculation()
    ReturnVal = GetString(USWBasicInfo.SPCommon)
End Sub

Private Sub DBWA_Calculation()
    ReturnVal = GetCurrency(USF4972Spouse.NUAG)
End Sub

Private Sub DBWB_Calculation()
    If GetBool(USF4972Spouse.NUA) = True Then
        ReturnVal = GetCurrency(USF4972Spouse.NUAB) + GetCurrency(USF4972Spouse.NUAD)
    Else
        ReturnVal = GetCurrency(USF4972Spouse.NUAB)
    End If
End Sub

Private Sub DBWC_Calculation()
    If GetCurrency(USF4972Spouse.DBWB) = 0 Then
        ReturnVal = 0
    Else
        ReturnVal = GetFloat(USF4972Spouse.DBWA) / GetFloat(USF4972Spouse.DBWB)
    End If
End Sub

Private Sub DBWD_Calculation()
    ReturnVal = GetCurrency(USF4972Spouse.DeathExcl)
End Sub

Private Sub DBWE_Calculation()
    ReturnVal = CDollar(GetCurrency(USF4972Spouse.DBWD) * GetFloat(USF4972Spouse.DBWC))
End Sub

Private Sub DBWF_Calculation()
    ReturnVal = GetCurrency(USF4972Spouse.DBWA) - GetCurrency(USF4972Spouse.DBWE)
End Sub

Private Sub Death_Calculation()
    Dim TPShare As Currency
    
    If GetBool(USF4972Spouse.CapGain) = True Then
        TPShare = GetCurrency(USF4972Spouse.DBWD) - GetCurrency(USF4972Spouse.DBWE)
    Else
        TPShare = GetCurrency(USF4972Spouse.DeathExcl)
    End If
    
    If GetBool(USF4972Spouse.UseForm) = True And GetBool(USF4972Spouse.Choose10Year) = True Then
        If GetBool(USF4972Spouse.MRD) = True And GetFloat(USF4972Spouse.Box9aPerc) <> 0 Then
            ReturnVal = CCur(TPShare / (GetFloat(USF4972Spouse.Box9aPerc) / 100#))
        Else
            ReturnVal = TPShare
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Desc_Calculation()
    ReturnVal = GetString(USF4972Spouse.Common)
End Sub

Private Sub Estate_Calculation()
    Dim CapGainEstate As Currency
    
    If GetBool(USF4972Spouse.ChooseCapGain) = True Then
        CapGainEstate = CDollar(GetCurrency(USF4972Spouse.EstateTax) * GetFloat(USF4972Spouse.DBWC))
    Else
        CapGainEstate = 0
    End If
    
    If GetBool(USF4972Spouse.UseForm) = True And GetBool(USF4972Spouse.Choose10Year) = True Then
        If GetBool(USF4972Spouse.MRD) = True And GetFloat(USF4972Spouse.Box9aPerc) <> 0 Then
            ReturnVal = CCur((GetCurrency(USF4972Spouse.EstateTax) - CapGainEstate) / (GetFloat(USF4972Spouse.Box9aPerc) / 100#))
        Else
            ReturnVal = GetCurrency(USF4972Spouse.EstateTax) - CapGainEstate
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Exist_Calculation()
    ReturnVal = 1
End Sub

Private Sub Ln13_Calculation()
    If GetCurrency(USF4972Spouse.AdjTotTaxable) > 69999@ Then
        ReturnVal = 0
    Else
        ReturnVal = MinValue(10000@, CDollar(GetCurrency(USF4972Spouse.AdjTotTaxable) * 0.5))
    End If
End Sub

Private Sub Ln14_Calculation()
    If GetCurrency(USF4972Spouse.AdjTotTaxable) > 69999@ Then
        ReturnVal = 0
    Else
        ReturnVal = MaxValue(0, GetCurrency(USF4972Spouse.AdjTotTaxable) - 20000@)
    End If
End Sub

Private Sub Ln15_Calculation()
    ReturnVal = CDollar(GetCurrency(USF4972Spouse.Ln14) * 0.2)
End Sub

Private Sub Ln17_Calculation()
    ReturnVal = GetCurrency(USF4972Spouse.AdjTotTaxable) - GetCurrency(USF4972Spouse.MinDisAllow)
End Sub

Private Sub Ln19_Calculation()
    If GetBool(USF4972Spouse.UseForm) = True And GetBool(USF4972Spouse.Choose10Year) = True Then
        ReturnVal = MaxValue(0, GetCurrency(USF4972Spouse.Ln17) - GetCurrency(USF4972Spouse.Estate))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Ln20_Calculation()
    If GetBool(USF4972Spouse.UseForm) = True And GetBool(USF4972Spouse.Choose10Year) = True Then
        If GetCurrency(USF4972Spouse.ActValue) > 0 Then
            If GetCurrency(USF4972Spouse.AdjTotTaxable) = 0 Then
                ReturnVal = 0
            Else
                ReturnVal = GetFloat(USF4972Spouse.ActValue) / GetFloat(USF4972Spouse.AdjTotTaxable)
            End If
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Ln21_Calculation()
    ReturnVal = CDollar(GetCurrency(USF4972Spouse.MinDisAllow) * GetFloat(USF4972Spouse.Ln20))
End Sub

Private Sub Ln22_Calculation()
    If GetBool(USF4972Spouse.UseForm) = True And GetBool(USF4972Spouse.Choose10Year) = True Then
        ReturnVal = MaxValue(0, GetCurrency(USF4972Spouse.ActValue) - GetCurrency(USF4972Spouse.Ln21))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Ln23_Calculation()
    ReturnVal = CDollar(GetCurrency(USF4972Spouse.Ln19) * 0.1)
End Sub

Private Sub Ln26_Calculation()
    ReturnVal = CDollar(GetCurrency(USF4972Spouse.Ln22) * 0.1)
End Sub

Private Sub MinDisAllow_Calculation()
    ReturnVal = GetCurrency(USF4972Spouse.Ln13) - GetCurrency(USF4972Spouse.Ln15)
End Sub

Private Sub MobDisQual_Calculation()
    If GetBool(USF4972Spouse.Print) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub MRDText_Calculation()
    If GetNumber(USF4972Spouse.Print) = 1 And GetBool(USF4972Spouse.Choose10Year) = True And GetBool(USF4972Spouse.MRD) = True Then
        ReturnVal = "MRD"
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(USWBasicInfo.SPCombName)
End Sub

Private Sub NUAA_Calculation()
    Dim CapGain As Currency
    Dim count As Integer
    
    count = 1
    CapGain = 0
    
    Do While count <= GetAllCopies(USD1099R)
        If GetBool(USD1099R.Qual4972, count) = True And GetBool(USD1099R.Spouse, count) = True Then
            CapGain = CapGain + Round(GetCurrency(USD1099R.CapGain, count))
        Else
            CapGain = CapGain
        End If
        count = count + 1
    Loop
    
    ReturnVal = CapGain
End Sub

Private Sub NUAAmt_Calculation()
    If GetNumber(USF4972Spouse.Print) = 1 And GetBool(USF4972Spouse.NUA) = True And GetBool(USF4972Spouse.ChooseCapGain) = True And GetCurrency(USF4972Spouse.NUAD) > 0 Then
        ReturnVal = GetCurrency(USF4972Spouse.NUAE)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub NUAAmt2_Calculation()
    If GetNumber(USF4972Spouse.Print) = 1 And GetBool(USF4972Spouse.NUA) = True And GetBool(USF4972Spouse.ChooseCapGain) = False And GetCurrency(USF4972Spouse.NUAD) > 0 Then
        ReturnVal = GetCurrency(USF4972Spouse.NUAD)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub NUAB_Calculation()
    Dim Taxable As Currency
    Dim count As Integer
    
    count = 1
    Taxable = 0
    
    Do While count <= GetAllCopies(USD1099R)
        If GetBool(USD1099R.Qual4972, count) = True And GetBool(USD1099R.Spouse, count) = True Then
            Taxable = Taxable + Round(GetCurrency(USD1099R.LumpSum, count))
        Else
            Taxable = Taxable
        End If
        count = count + 1
    Loop
    
    ReturnVal = Taxable
End Sub

Private Sub NUAC_Calculation()
    If GetCurrency(USF4972Spouse.NUAB) = 0 Then
        ReturnVal = 0
    Else
        ReturnVal = GetFloat(USF4972Spouse.NUAA) / GetFloat(USF4972Spouse.NUAB)
    End If
End Sub

Private Sub NUAD_Calculation()
    Dim NUA As Currency
    Dim count As Integer
    
    count = 1
    NUA = 0
    
    Do While count <= GetAllCopies(USD1099R)
        If GetBool(USD1099R.Qual4972, count) = True And GetBool(USD1099R.Spouse, count) = True Then
            NUA = NUA + Round(GetCurrency(USD1099R.UnRealApp, count))
        Else
            NUA = NUA
        End If
        count = count + 1
    Loop
    
    ReturnVal = NUA
End Sub

Private Sub NUAE_Calculation()
'pulls from each R instead of computing the amount in total
    Dim NUA As Currency
    Dim count As Integer
    
    count = 1
    NUA = 0
    
    Do While count <= GetAllCopies(USD1099R)
        If GetBool(USD1099R.Qual4972, count) = True And GetBool(USD1099R.Spouse, count) = True Then
            NUA = NUA + Round(GetCurrency(USD1099R.F4972NUA, count))
        Else
            NUA = NUA
        End If
        count = count + 1
    Loop
    
    ReturnVal = NUA
End Sub

Private Sub NUAF_Calculation()
    ReturnVal = GetCurrency(USF4972Spouse.NUAD) - GetCurrency(USF4972Spouse.NUAE)
End Sub

Private Sub NUAG_Calculation()
    If GetBool(USF4972Spouse.NUA) = True Then
        ReturnVal = GetCurrency(USF4972Spouse.NUAA) + GetCurrency(USF4972Spouse.NUAE)
    Else
        ReturnVal = GetCurrency(USF4972Spouse.NUAA)
    End If
End Sub

Private Sub NUALn6_Calculation()
    If GetString(USF4972Spouse.NUAText) <> "" Then
        ReturnVal = GetString(USF4972Spouse.NUAText) & " " & GetString(USF4972Spouse.NUAAmt)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub NUALn8_Calculation()
    If GetString(USF4972Spouse.NUAText2) <> "" Then
        ReturnVal = GetString(USF4972Spouse.NUAText2) & " " & GetString(USF4972Spouse.NUAAmt2)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub NUAText_Calculation()
    If GetNumber(USF4972Spouse.Print) = 1 And GetBool(USF4972Spouse.NUA) = True And GetBool(USF4972Spouse.ChooseCapGain) = True And GetCurrency(USF4972Spouse.NUAD) > 0 Then
        ReturnVal = "NUA"
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub NUAText2_Calculation()
    If GetNumber(USF4972Spouse.Print) = 1 And GetBool(USF4972Spouse.NUA) = True And GetBool(USF4972Spouse.ChooseCapGain) = False And GetCurrency(USF4972Spouse.NUAD) > 0 Then
        ReturnVal = "NUA"
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub OrdInc_Calculation()
    Dim OrdInc As Currency
    Dim Taxable As Currency
    Dim CapGain As Currency
    
    Taxable = GetCurrency(USF4972Spouse.NUAB)
    CapGain = GetCurrency(USF4972Spouse.NUAA)
    
    If GetBool(USF4972Spouse.NUA) = True And GetBool(USF4972Spouse.CapGain) = True Then
        OrdInc = MaxValue(0, Taxable - CapGain) + GetCurrency(USF4972Spouse.NUAF)
    ElseIf GetBool(USF4972Spouse.NUA) = True And GetBool(USF4972Spouse.CapGain) = False Then
        OrdInc = Taxable + GetCurrency(USF4972Spouse.NUAD)
    ElseIf GetBool(USF4972Spouse.NUA) = False And GetBool(USF4972Spouse.CapGain) = True Then
        OrdInc = MaxValue(0, Taxable - CapGain)
    Else
        OrdInc = Taxable
    End If
    
    If GetBool(USF4972Spouse.UseForm) = True And GetBool(USF4972Spouse.Choose10Year) = True Then
        If GetBool(USF4972Spouse.MRD) = True Then
            If GetFloat(USF4972Spouse.Box9aPerc) <> 0 Then
                ReturnVal = CCur(OrdInc / (GetFloat(USF4972Spouse.Box9aPerc) / 100#))
            Else
                ReturnVal = OrdInc
            End If
        Else
            ReturnVal = OrdInc
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Print_Calculation()
    If GetCurrency(USF4972Spouse.Tax) > 0 And FS() = 2 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(USWBasicInfo.SpouseSSN)
End Sub

Private Sub StopR_Calculation()
'to stop the calculation of pensions on 1099-R
    If GetBool(USF4972Spouse.UseForm) = True And GetBool(USF4972Spouse.Choose10Year) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Tax_Calculation()
    ReturnVal = GetCurrency(USF4972Spouse.CapGainTax) + GetCurrency(USF4972Spouse.Tax1MTax2)
End Sub

Private Sub Tax1_Calculation()
    ReturnVal = LumpSumTax(GetCurrency(USF4972Spouse.Ln23))
End Sub

Private Sub Tax1By10_Calculation()
    ReturnVal = CDollar(GetCurrency(USF4972Spouse.Tax1) * 10#)
End Sub

Private Sub Tax1MTax2_Calculation()
    Dim Line29 As Currency
    
    Line29 = MaxValue(0, GetCurrency(USF4972Spouse.Tax1By10) - GetCurrency(USF4972Spouse.Tax2By10))
    
    If GetBool(USF4972Spouse.MRD) = True And GetFloat(USF4972Spouse.Box9aPerc) <> 0 Then
        ReturnVal = CDollar(Line29 * (GetFloat(USF4972Spouse.Box9aPerc) / 100#))
    Else
        ReturnVal = Line29
    End If
End Sub

Private Sub Tax2_Calculation()
    ReturnVal = LumpSumTax(GetCurrency(USF4972Spouse.Ln26))
End Sub

Private Sub Tax2By10_Calculation()
    ReturnVal = CDollar(GetCurrency(USF4972Spouse.Tax2) * 10#)
End Sub

Private Sub TotTaxable_Calculation()
    If GetBool(USF4972Spouse.UseForm) = True Then
        ReturnVal = MaxValue(0, GetCurrency(USF4972Spouse.OrdInc) - GetCurrency(USF4972Spouse.Death))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPAddback_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(USF4972Spouse.TPCapGain) + GetCurrency(USF4972Spouse.TPTaxAmt) - GetCurrency(USF4972Spouse.TPEstate))
End Sub

Private Sub TPAddbackNoEx_Calculation()
    ReturnVal = GetCurrency(USF4972Spouse.TPCapGainNoEx) + GetCurrency(USF4972Spouse.TPOrdInc)
End Sub

Private Sub TPCapGain_Calculation()
    ReturnVal = GetCurrency(USF4972Spouse.CapGain)
End Sub

Private Sub TPCapGainNoEx_Calculation()
    Dim Estate As Currency

    Estate = CDollar(GetCurrency(USF4972Spouse.EstateTax) * GetFloat(USF4972Spouse.DBWC))
    
    If GetBool(USF4972Spouse.ChooseCapGain) = True And GetBool(USF4972Spouse.UseForm) = True Then
        ReturnVal = GetCurrency(USF4972Spouse.CapGain) + GetCurrency(USF4972Spouse.DBWE) + Estate
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPDBE_Calculation()
    Dim CapGainDBE As Currency
    
    If GetBool(USF4972Spouse.ChooseCapGain) = True Then
        CapGainDBE = GetCurrency(USF4972Spouse.DBWE)
    Else
        CapGainDBE = 0
    End If
    
    If GetBool(USF4972Spouse.UseForm) = True And GetBool(USF4972Spouse.Choose10Year) = True Then
        ReturnVal = GetCurrency(USF4972Spouse.DeathExcl) - CapGainDBE
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPEstate_Calculation()
'to reduce line 10
    Dim CapGainEstate As Currency
    
    If GetBool(USF4972Spouse.ChooseCapGain) = True Then
        CapGainEstate = CDollar(GetCurrency(USF4972Spouse.EstateTax) * GetFloat(USF4972Spouse.DBWC))
    Else
        CapGainEstate = 0
    End If
    
    If GetBool(USF4972Spouse.UseForm) = True And GetBool(USF4972Spouse.Choose10Year) = True Then
        ReturnVal = GetCurrency(USF4972Spouse.EstateTax) - CapGainEstate
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPOrdInc_Calculation()
    Dim Taxable As Currency
    Dim CapGain As Currency
    
    Taxable = GetCurrency(USF4972Spouse.NUAB)
    CapGain = GetCurrency(USF4972Spouse.NUAA)
    
    If GetBool(USF4972Spouse.UseForm) = True And GetBool(USF4972Spouse.Choose10Year) = True Then
        If GetBool(USF4972Spouse.NUA) = True And GetBool(USF4972Spouse.CapGain) = True Then
            ReturnVal = MaxValue(0, Taxable - CapGain) + GetCurrency(USF4972Spouse.NUAF)
        ElseIf GetBool(USF4972Spouse.NUA) = True And GetBool(USF4972Spouse.CapGain) = False Then
            ReturnVal = Taxable + GetCurrency(USF4972Spouse.NUAD)
        ElseIf GetBool(USF4972Spouse.NUA) = False And GetBool(USF4972Spouse.CapGain) = True Then
            ReturnVal = MaxValue(0, Taxable - CapGain)
        Else
            ReturnVal = Taxable
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPTaxAmt_Calculation()
    If GetBool(USF4972Spouse.UseForm) = True And GetBool(USF4972Spouse.Choose10Year) = True Then
        If GetBool(USF4972Spouse.MRD) = True And GetFloat(USF4972Spouse.Box9aPerc) <> 0 Then
            ReturnVal = CCur(GetCurrency(USF4972Spouse.TotTaxable) * (GetFloat(USF4972Spouse.Box9aPerc) / 100#))
        Else
            ReturnVal = GetCurrency(USF4972Spouse.TotTaxable)
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub UseForm_Calculation()
    Dim Ln1 As Long
    Dim Ln2 As Long
    Dim Ln3and4 As Long
    Dim Ln5a As Long
    Dim Ln5b As Long
    
    If GetBool(USF4972Spouse.Ln1Yes) = True Then
        Ln1 = 0
    Else
        Ln1 = 1
    End If
    
    If GetBool(USF4972Spouse.Ln2No) = True Then
        Ln2 = 0
    Else
        Ln2 = 1
    End If
    
    If GetBool(USF4972Spouse.Ln3Yes) = True And GetBool(USF4972Spouse.Ln4Yes) = True Then
        Ln3and4 = 0
    ElseIf GetBool(USF4972Spouse.Ln3Yes) = True And GetBool(USF4972Spouse.Ln4No) = True Then
        Ln3and4 = 0
    ElseIf GetBool(USF4972Spouse.Ln3No) = True And GetBool(USF4972Spouse.Ln4Yes) = True Then
        Ln3and4 = 0
    Else
        Ln3and4 = 1
    End If
    
    If GetBool(USF4972Spouse.Ln5aNo) = True Then
        Ln5a = 0
    Else
        Ln5a = 1
    End If
    
    If GetBool(USF4972Spouse.Ln5bYes) = True Then
        Ln5b = 1
    Else
        Ln5b = 0
    End If
'condition above reversed since it applies only if rec'd as beneficiary
    
    If Ln1 + Ln2 + Ln3and4 + Ln5a + Ln5b = 0 And FS() = 2 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

