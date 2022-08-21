Private Sub AAltTax_Calculation()
' 1st condition added for situation when MFS return and reporting spouse income causes an alternate tax calculation yet taxpayer has zero income
' See saved return IA MFS Alternate Tax Issue.ta2
    If GetBool(IA1040X.MFS) = True And GetCurrency(IA1040X.ATaxInc) = 0 Then
        ReturnVal = 0
    ElseIf (GetCurrency(IAWkAltTax.Mult) < GetCurrency(IA1040X.TotTaxSch)) And GetBool(IAWkAltTax.Qualify) = True Then
        ReturnVal = GetCurrency(IAF1040.ATax)
    Else
        ReturnVal = GetCurrency(IA1040X.ARegTax)
    End If
End Sub

Private Sub ABalance14_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA1040X.ATotTax) - GetCurrency(IA1040X.ATotCr50))
End Sub

Private Sub ABalance16_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA1040X.ABalance14) - GetCurrency(IA1040X.ACrNon))
End Sub

Private Sub ABalance18_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA1040X.ABalance16) - GetCurrency(IA1040X.AOthIACr))
End Sub

Private Sub ABalance7_Calculation()
    ReturnVal = GetCurrency(IA1040X.ATotInc) - GetCurrency(IA1040X.AFedDed)
End Sub

Private Sub AContrib_Calculation()
    If GetBool(IA1040X.CombMFS) = True Then
        ReturnVal = GetCurrency(IAF1040.TotContrib) - GetCurrency(IA1040X.BContrib)
    Else
        ReturnVal = GetCurrency(IAF1040.TotContrib)
    End If
End Sub

Private Sub ACrNon_Calculation()
    ReturnVal = GetCurrency(IAF1040.ACrNon)
End Sub

Private Sub Add_Calculation()
    ReturnVal = GetString(IAF1040.Add)
End Sub

Private Sub ADedBox_Calculation()
    ReturnVal = GetCurrency(IAF1040.ADedBox)
End Sub

Private Sub AdjRef_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA1040X.CalcOP) - GetCurrency(IA1040X.TotCF))
End Sub

Private Sub AFedDed_Calculation()
    ReturnVal = GetCurrency(IAF1040.AFedDed)
End Sub

Private Sub AFedTax_Calculation()
    ReturnVal = GetCurrency(IAF1040.AFedTax)
End Sub

Private Sub AGross_Calculation()
    ReturnVal = GetCurrency(IAF1040.AGross)
End Sub

Private Sub ALumpMin_Calculation()
    ReturnVal = GetCurrency(IAF1040.ALump) + GetCurrency(IAF1040.AIAMin)
End Sub

Private Sub ANet_Calculation()
    ReturnVal = GetCurrency(IAF1040.ANet)
End Sub

Private Sub AOthIACr_Calculation()
    ReturnVal = GetCurrency(IAF1040.AOutState) + GetCurrency(IAF1040.AOthIACr)
End Sub

Private Sub APenExcl_Calculation()
    ReturnVal = GetCurrency(IAF1040.APenExcl)
End Sub

Private Sub ARegTax_Calculation()
    Dim TotTaxInc As Currency
    
    TotTaxInc = GetCurrency(IA1040X.ATaxInc)
    
    ReturnVal = Tax(TotTaxInc)
    
End Sub

Private Sub ARepSSB_Calculation()
    ReturnVal = GetCurrency(IAF1040.ARepSSB)
End Sub

Private Sub ASch_Calculation()
    ReturnVal = GetCurrency(IAF1040.ASch)
End Sub

Private Sub ATaxInc_Calculation()
    ReturnVal = GetCurrency(IAF1040.ATaxInc)
End Sub

Private Sub ATotAdj_Calculation()
    ReturnVal = GetCurrency(IAF1040.ATotAdj)
End Sub

Private Sub ATotCr50_Calculation()
    ReturnVal = GetCurrency(IAF1040.ACredits)
End Sub

Private Sub ATotInc_Calculation()
    ReturnVal = GetCurrency(IA1040X.ANet) + GetCurrency(IA1040X.AFedTax)
End Sub

Private Sub ATotTax_Calculation()
    ReturnVal = GetCurrency(IA1040X.AAltTax) + GetCurrency(IA1040X.ALumpMin)
End Sub

Private Sub ATotTax2_Calculation()
    ReturnVal = GetCurrency(IA1040X.ABalance18) + GetCurrency(IA1040X.ASch) + GetCurrency(IA1040X.AContrib)
End Sub

Private Sub Balance27_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA1040X.TotPay) - GetCurrency(IA1040X.PrevOP))
End Sub

Private Sub BAltTax_Calculation()
    If IAFS() = 3 Then
        If (GetCurrency(IAWkAltTax.Mult) < GetCurrency(IA1040X.TotTaxSch)) And GetBool(IAWkAltTax.Qualify) = True Then
            ReturnVal = GetCurrency(IAF1040.BTax)
        Else
            ReturnVal = GetCurrency(IA1040X.BRegTax)
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BBalance14_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA1040X.BTotTax) - GetCurrency(IA1040X.BTotCr50))
End Sub

Private Sub BBalance16_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA1040X.BBalance14) - GetCurrency(IA1040X.BCrNon))
End Sub

Private Sub BBalance18_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA1040X.BBalance16) - GetCurrency(IA1040X.BOthIACr))
End Sub

Private Sub BBalance7_Calculation()
    ReturnVal = GetCurrency(IA1040X.BTotInc) - GetCurrency(IA1040X.BFedDed)
End Sub

Private Sub BContrib_Calculation()
    If GetBool(IA1040X.CombMFS) = True Then
        ReturnVal = CDollar(GetFloat(IAF1040.TotContrib) * 0.5)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BCrNon_Calculation()
    ReturnVal = GetCurrency(IAF1040.BCrNon)
End Sub

Private Sub BDedBox_Calculation()
    ReturnVal = GetCurrency(IAF1040.BDedBox)
End Sub

Private Sub BFedDed_Calculation()
    ReturnVal = GetCurrency(IAF1040.BFedDed)
End Sub

Private Sub BFedTax_Calculation()
    ReturnVal = GetCurrency(IAF1040.BFedTax)
End Sub

Private Sub BGross_Calculation()
    ReturnVal = GetCurrency(IAF1040.BGross)
End Sub

Private Sub BLumpMin_Calculation()
    ReturnVal = GetCurrency(IAF1040.BLump) + GetCurrency(IAF1040.BIAMin)
End Sub

Private Sub BNet_Calculation()
    ReturnVal = GetCurrency(IAF1040.BNet)
End Sub

Private Sub BOthIACr_Calculation()
    ReturnVal = GetCurrency(IAF1040.BOutState) + GetCurrency(IAF1040.BOthIACr)
End Sub

Private Sub BPenExcl_Calculation()
    ReturnVal = GetCurrency(IAF1040.BPenExcl)
End Sub

Private Sub BRegTax_Calculation()
    Dim TotTaxInc As Currency
    
    If GetBool(IAF1040.MFS) = True Then
        TotTaxInc = GetCurrency(IAF1040.SpTaxInc)
    Else
        TotTaxInc = GetCurrency(IA1040X.BTaxInc)
    End If
    
    ReturnVal = Tax(TotTaxInc)
    
End Sub

Private Sub BRepSSB_Calculation()
    ReturnVal = GetCurrency(IAF1040.BRepSSB)
End Sub

Private Sub BSch_Calculation()
    ReturnVal = GetCurrency(IAF1040.BSch)
End Sub

Private Sub BTaxInc_Calculation()
    ReturnVal = GetCurrency(IAF1040.BTaxInc)
End Sub

Private Sub BTotAdj_Calculation()
    ReturnVal = GetCurrency(IAF1040.BTotAdj)
End Sub

Private Sub BTotCr50_Calculation()
    ReturnVal = GetCurrency(IAF1040.BCredits)
End Sub

Private Sub BTotInc_Calculation()
    ReturnVal = GetCurrency(IA1040X.BNet) + GetCurrency(IA1040X.BFedTax)
End Sub

Private Sub BTotTax_Calculation()
    ReturnVal = GetCurrency(IA1040X.BAltTax) + GetCurrency(IA1040X.BLumpMin)
End Sub

Private Sub BTotTax2_Calculation()
    ReturnVal = GetCurrency(IA1040X.BBalance18) + GetCurrency(IA1040X.BSch) + GetCurrency(IA1040X.BContrib)
End Sub

Private Sub CalcOP_Calculation()
    Dim PrevOP As Currency
    
    PrevOP = MaxValue(0, GetCurrency(IA1040X.PrevOP) - GetCurrency(IA1040X.TotPay))

    ReturnVal = MaxValue(0, GetCurrency(IA1040X.Balance27) - GetCurrency(IA1040X.Total) - PrevOP)
End Sub

Private Sub City_Calculation()
    ReturnVal = GetString(IAF1040.CityComb)
End Sub

Private Sub CombMFS_Calculation()
    ReturnVal = GetBool(IAF1040.CombMFS)
End Sub

Private Sub CountyNo_Calculation()
    ReturnVal = GetString(IAF1040.CountyNo)
End Sub

Private Sub DC1_Calculation()
    ReturnVal = GetNumber(IAF1040.DC1)
End Sub

Private Sub DC2_Calculation()
    ReturnVal = GetNumber(IAF1040.DC2)
End Sub

Private Sub DepN_Calculation()
    ReturnVal = GetBool(IAF1040.DepN)
End Sub

Private Sub DepNames_Calculation()
    ReturnVal = GetString(IAF1040.DepNames)
End Sub

Private Sub DepY_Calculation()
    ReturnVal = GetBool(IAF1040.DepY)
End Sub

Private Sub Desc_Calculation()
    ReturnVal = GetString(IARequired.CombNames)
End Sub

Private Sub EFExplanation_Calculation()
    Dim t As String
    Dim a As Integer
    
    t = ""
    a = 0
    
    Do While a < 18
        t = t + " " + GetString(IA1040X.Explanation(a))
        a = a + 1
    Loop

    If GetBool(IA1040X.EFAmend) = True Then
        ReturnVal = Trim(t)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub ExempA_Calculation()
    ReturnVal = GetCurrency(IAF1040.ExempA)
End Sub

Private Sub ExempB_Calculation()
    ReturnVal = GetCurrency(IAF1040.ExempB)
End Sub

Private Sub Exist_Calculation()
    ReturnVal = 1
End Sub

Private Sub FirstName_Calculation()
    ReturnVal = GetString(IAF1040.FirstName)
End Sub

Private Sub HOH_Calculation()
    ReturnVal = GetBool(IAF1040.HOH)
End Sub

Private Sub HOHDep_Calculation()
    ReturnVal = GetString(IAF1040.HOHDep)
End Sub

Private Sub HOHSSN_Calculation()
    ReturnVal = GetString(IAF1040.HOHSSN)
End Sub

Private Sub Int_Calculation()
    ReturnVal = GetCurrency(IAF1040.Int74)
End Sub

Private Sub ItemCheck_Calculation()
    ReturnVal = GetBool(IAF1040.ItemCheck)
End Sub

Private Sub LastName_Calculation()
    ReturnVal = GetString(IAF1040.LastName)
End Sub

Private Sub Lesser_Calculation()
    If IAFS() = 1 Then
        ReturnVal = GetCurrency(IA1040X.TotTaxSch)
    Else
        If GetBool(IAWkAltTax.Qualify) = True Then
            ReturnVal = MinValue(GetCurrency(IAWkAltTax.Mult), GetCurrency(IA1040X.TotTaxSch))
        Else
            ReturnVal = GetCurrency(IA1040X.TotTaxSch)
        End If
    End If
End Sub

Private Sub MFJ_Calculation()
    ReturnVal = GetBool(IAF1040.MFJ)
End Sub

Private Sub MFS_Calculation()
    ReturnVal = GetBool(IAF1040.MFS)
End Sub

Private Sub MFSName_Calculation()
    ReturnVal = GetString(IAF1040.MFSName)
End Sub

Private Sub MFSSSN_Calculation()
    ReturnVal = GetString(IAF1040.MFSSSN)
End Sub

Private Sub Over65_Calculation()
    ReturnVal = GetBool(IAF1040.Over65)
End Sub

Private Sub Owe_Calculation()
    Dim PrevOP As Currency
    
    PrevOP = MaxValue(0, GetCurrency(IA1040X.PrevOP) - GetCurrency(IA1040X.TotPay))

    ReturnVal = MaxValue(0, GetCurrency(IA1040X.Total) + PrevOP - GetCurrency(IA1040X.Balance27))
End Sub

Private Sub PC1a_Calculation()
    ReturnVal = GetNumber(IAF1040.PC1a)
End Sub

Private Sub PC1b_Calculation()
    ReturnVal = GetNumber(IAF1040.PC1b)
End Sub

Private Sub PC2a_Calculation()
    ReturnVal = GetNumber(IAF1040.PC2a)
End Sub

Private Sub PC2b_Calculation()
    ReturnVal = GetNumber(IAF1040.PC2b)
End Sub

Private Sub Pen_Calculation()
    ReturnVal = GetCurrency(IAF1040.Pen74)
End Sub

Private Sub PenInt_Calculation()
    If GetCurrency(IA1040X.Refund) > 0 Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(IA1040X.Pen) + GetCurrency(IA1040X.Int)
    End If
End Sub

Private Sub Phone_Calculation()
    ReturnVal = GetString(IAF1040.Phone)
End Sub

Private Sub PrepAdd_Calculation()
    ReturnVal = GetString(USWBasicInfo.PrepAdd)
End Sub

Private Sub PrepCitySt_Calculation()
    ReturnVal = GetString(USWBasicInfo.CombPrepCityStZipFor)
End Sub

Private Sub PrepFirm_Calculation()
    ReturnVal = GetString(USWBasicInfo.PrepName)
End Sub

Private Sub PrepID_Calculation()
    ReturnVal = GetString(IAF1040.PrepID)
End Sub

Private Sub PrepPhone_Calculation()
    ReturnVal = GetString(IAF1040.PrepPhone)
End Sub

Private Sub QualWidow_Calculation()
    ReturnVal = GetBool(IAF1040.QualWidow)
End Sub

Private Sub Refund_Calculation()
    Dim PrevOP As Currency
    
    PrevOP = MaxValue(0, GetCurrency(IA1040X.PrevOP) - GetCurrency(IA1040X.TotPay))

    If GetCurrency(IA1040X.TotCF) > 0 Then
        ReturnVal = GetCurrency(IA1040X.AdjRef)
    Else
        ReturnVal = MaxValue(0, GetCurrency(IA1040X.Balance27) - GetCurrency(IA1040X.Total) - PrevOP)
    End If
End Sub

Private Sub SchNo_Calculation()
    ReturnVal = GetString(IAF1040.SchNo)
End Sub

Private Sub Single_Calculation()
    ReturnVal = GetBool(IAF1040.Single)
End Sub

Private Sub SpIncome_Calculation()
    ReturnVal = GetCurrency(IAF1040.SpIncome)
End Sub

Private Sub SpouseFirst_Calculation()
    ReturnVal = GetString(IAF1040.SpouseFirst)
End Sub

Private Sub SpouseLast_Calculation()
    ReturnVal = GetString(IAF1040.SpouseLast)
End Sub

Private Sub SpouseSSN_Calculation()
    ReturnVal = GetString(IAF1040.SpouseSSN)
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

Private Sub StadCheck_Calculation()
    ReturnVal = GetBool(IAF1040.StadCheck)
End Sub

Private Sub TaxYear_Calculation()
    Dim TaxYear As Integer
    
    TaxYear = YearNumber
    
    ReturnVal = CStr(TaxYear)
End Sub

Private Sub Tot67_Calculation()
    If GetBool(IA1040X.EFAmend) = True Then
        ReturnVal = GetCurrency(IAF1040.BTot67) + GetCurrency(IAF1040.ATot67) - GetCurrency(IA1040X.TotPrevTax)
    Else
        ReturnVal = GetCurrency(IAF1040.BTot67) + GetCurrency(IAF1040.ATot67)
    End If
End Sub

Private Sub Total_Calculation()
    ReturnVal = GetCurrency(IA1040X.BTotTax2) + GetCurrency(IA1040X.ATotTax2)
End Sub

Private Sub TotCF_Calculation()
    ReturnVal = GetCurrency(IA1040X.TPElectCF) + GetCurrency(IA1040X.SPElectCF)
End Sub

Private Sub TotDC1_Calculation()
    ReturnVal = GetCurrency(IAF1040.TotDC1)
End Sub

Private Sub TotDC2_Calculation()
    ReturnVal = GetCurrency(IAF1040.TotDC2)
End Sub

Private Sub TotDue_Calculation()
    ReturnVal = GetCurrency(IA1040X.Owe) + GetCurrency(IA1040X.PenInt)
End Sub

Private Sub TotPay_Calculation()
    ReturnVal = GetCurrency(IA1040X.Tot67) + GetCurrency(IA1040X.TotPrevTax)
End Sub

Private Sub TotPC2a_Calculation()
    ReturnVal = GetCurrency(IAF1040.TotPC2a)
End Sub

Private Sub TotPC2b_Calculation()
    ReturnVal = GetCurrency(IAF1040.TotPC2b)
End Sub

Private Sub TotPCa_Calculation()
    ReturnVal = GetCurrency(IAF1040.TotPCa)
End Sub

Private Sub TotPCb_Calculation()
    ReturnVal = GetCurrency(IAF1040.TotPCb)
End Sub

Private Sub TotTaxSch_Calculation()
    ReturnVal = GetCurrency(IA1040X.ARegTax) + GetCurrency(IA1040X.BRegTax)
End Sub

