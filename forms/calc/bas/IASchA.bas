Private Sub AddMilesDed_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IASchA.TotMilesDed) - GetCurrency(IASchA.SchAMilesDed))
End Sub

Private Sub AdoptSub_Calculation()
    ReturnVal = MaxValue(0, CDollar(GetFloat(IAChildCredit.TotNI) * 0.03))
End Sub

Private Sub AGI_Calculation()
    If GetCurrency(IASchA.MedExp) = 0 Then
        ReturnVal = 0
    Else
        ReturnVal = MaxValue(0, CDollar(GetFloat(IASchA.IAAGI) * 0.1))
    End If
End Sub

Private Sub Alert10_Calculation()
    Dim FedMedical As Currency
    
    If GetBool(USWResidency.F1040NR) = False Then
        FedMedical = GetCurrency(USSchA.MedExp)
    Else
        FedMedical = 0
    End If

    If GetCurrency(IASchA.MedExp) >= FedMedical And GetCurrency(IASchA.MedExp) > 0 Then
        If GetCurrency(IAF1040.BHealth) > 0 Or GetCurrency(IAF1040.AHealth) > 0 Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert15_Calculation()
    If GetBool(IAF1040.ItemCheck) = True And GetCurrency(IASchA.Mort) > 0 Then
        If GetCurrency(USD1098.MortPrem) > 1000000@ Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert20_Calculation()
'add net nonconformity items? Next year could them factor in. If user imports we should import correct Iowa amounts, if we continue to also pull the federal carryover amounts should still bring up this alert
'alert is saying to adjust carryover if had any nonconforming items last year, leave as only depr since othinc ws is only current year items, possibly factor in next year (either imported NC items/bonus and/or current year NC items)
    If GetCurrency(IASchA.Over) <> 0 And GetCurrency(IAWOthInc.TotBonus) <> 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert22_Calculation()
    Dim TotCont As Currency
    
    TotCont = GetCurrency(IAWContLimit.CY50Lim) + GetCurrency(IAWContLimit.CY30Lim) + GetCurrency(IAWContLimit.CY30LimCG) + GetCurrency(IAWContLimit.CY20Lim) + GetCurrency(IAWContLimit.CYNoLim)
       
    If TotCont > GetCurrency(IAWContLimit.CYTot) Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert24_Calculation()
    If GetCurrency(IAWContLimit.PY50Lim) < 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IAWContLimit.PY30Lim) < 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IAWContLimit.PY30LimCG) < 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IAWContLimit.PY20Lim) < 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IAWContLimit.PYNoLim) < 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert26_Calculation()
    If GetCurrency(IAWContLimit.NYTot) <> 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert27_Calculation()
    If GetCurrency(IAWContLimit.CYQualLim) <> 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert28_Calculation()
    If GetCurrency(IAWContLimit.CYQualLim) > GetCurrency(IASchA.Contrib) Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert30_Calculation()
    ReturnVal = 0
End Sub

Private Sub Alert40_Calculation()
    If GetBool(IAF1040.ItemCheck) = True And GetCurrency(IASchA.OthMisc) > 0 Then
        If GetCurrency(IASchA.IAAdjOthMisc) <> 0 And Trim(GetString(IASchA.IAAdjOthMiscDesc)) = "" Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert50_Calculation()
    Dim count, Iter As Integer
    
    count = 0
    Iter = 0
    Do While Iter < 5
        If GetCurrency(IASchA.DisableAmt(Iter)) > 0 And Trim(GetString(IASchA.DisableExp(Iter))) = "" Then
            count = count + 1
        End If
        Iter = Iter + 1
    Loop

    If GetBool(IAF1040.ItemCheck) = True And count > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert60_Calculation()
    Dim count As Integer
    Dim Lim As Integer
    Dim Total As Integer
    
    Lim = GetAllCopies(IA177)
    count = 1
    Total = 0
    
    Do While count <= Lim
        If GetCurrency(IA177.CYAdoptionTaxCr, count) > 0 And GetBool(IA177.Taxpayer, count) = True Then
            Total = Total + 1
        Else
            Total = Total
        End If
        
        count = count + 1
    Loop
    
    Dim count2 As Integer
    Dim Lim2 As Integer
    Dim Total2 As Integer
    
    Lim2 = GetAllCopies(IA177)
    count2 = 1
    Total2 = 0
    
    Do While count2 <= Lim2
        If GetCurrency(IA177.CYAdoptionTaxCr, count) > 0 And GetBool(IA177.Spouse, count2) = True Then
            Total2 = Total2 + 1
        Else
            Total2 = Total2
        End If
        
        count2 = count2 + 1
    Loop

    If GetCurrency(IASchA.TotAdoptAmt) > 0 Then
        If Total > 0 Then
            ReturnVal = 1
        ElseIf Total2 > 0 And GetBool(IAF1040.CombMFS) = True Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert70_Calculation()
    Dim count, Iter As Integer
    
    count = 0
    Iter = 0
    Do While Iter < 5
        If GetCurrency(IASchA.AdoptAmt(Iter)) > 0 And Trim(GetString(IASchA.AdoptExp(Iter))) = "" Then
            count = count + 1
        End If
        Iter = Iter + 1
    Loop

    If GetBool(IAF1040.ItemCheck) = True And GetCurrency(IASchA.AllowAdopt) > 0 And count > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert80_Calculation()
    If GetCurrency(IAWSchAPrint.GamblingLoss) > (GetCurrency(IAF1040.BGamble) + GetCurrency(IAF1040.AGamble)) Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert85_Calculation()
    If GetBool(IAF1040.ItemCheck) = True Then
        If GetCurrency(IASchA.OthTax) <> 0 And Trim(GetString(IASchA.OthList)) = "" Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AllowAdopt_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IASchA.TotAdoptAmt) - GetCurrency(IASchA.AdoptSub))
End Sub

Private Sub AllowExp_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IASchA.Expense) - GetCurrency(IASchA.Mult))
End Sub

Private Sub CombOthExpDesc_Calculation()
    ReturnVal = GetString(IASchA.OthExpDesc(0)) + " " + GetString(IASchA.OthExpDesc(1)) + " " + GetString(IASchA.OthExpDesc(2)) + " " + GetString(IASchA.OthExpDesc(3)) + " " + GetString(IASchA.OthExpDesc(4)) + " " + GetString(IASchA.OthExpDesc(5)) + " " + GetString(IASchA.OthExpDesc(6)) + " " + GetString(IASchA.OthExpDesc(7)) + " " + GetString(IASchA.OthExpDesc(8)) + " " + GetString(IASchA.OthExpDesc(9)) + " " + GetString(IASchA.OthExpDesc(10)) + " " + GetString(IASchA.OthExpDesc(11)) + " " + GetString(IASchA.OthExpDesc(12)) + " " + GetString(IASchA.OthExpDesc(13)) + " " + GetString(IASchA.OthExpDesc(14)) + " " + GetString(IASchA.OthExpDesc(15)) + " " + GetString(IASchA.OthExpDesc(16)) + " " + GetString(IASchA.OthExpDesc(17)) + " " + GetString(IASchA.OthExpDesc(18)) + " " + GetString(IASchA.OthExpDesc(19)) + " " + GetString(IASchA.OthExpDesc(20)) + " " + GetString(IASchA.OthExpDesc(21)) + " " + GetString(IASchA.OthExpDesc(22)) + " " + GetString(IASchA.OthExpDesc(23)) + " " + GetString(IASchA.OthExpDesc(24))
End Sub

Private Sub CombOthMiscDesc_Calculation()
    ReturnVal = GetString(IASchA.OthMiscDesc(0)) + " " + GetString(IASchA.OthMiscDesc(1)) + " " + GetString(IASchA.OthMiscDesc(2)) + " " + GetString(IASchA.OthMiscDesc(3)) + " " + GetString(IASchA.OthMiscDesc(4)) + " " + GetString(IASchA.OthMiscDesc(5)) + " " + GetString(IASchA.OthMiscDesc(6)) + " " + GetString(IASchA.OthMiscDesc(7)) + " " + GetString(IASchA.OthMiscDesc(8)) + " " + GetString(IASchA.OthMiscDesc(9))
End Sub

Private Sub Contrib_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IASchA.TotContrib) - GetCurrency(IASchA.IAAdjContrib))
End Sub

Private Sub Description_Calculation()
    ReturnVal = CStr(GetCurrency(IASchA.Item)) & " Itemized Deductions"
End Sub

Private Sub Exist_Calculation()
    ReturnVal = 1
End Sub

Private Sub Expense_Calculation()
    ReturnVal = GetCurrency(IASchA.Unreimb) + GetCurrency(IASchA.TaxFee) + GetCurrency(IASchA.OthExp)
End Sub

Private Sub GenSales_Calculation()
'Iowa expanded instructions can only claim gen sales tax if itemize federally and elect to claim gen sales on fed. Leave calced.
    If GetBool(USWRec.ItmDdn) = True And GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetBool(USSchA.GenSales)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Gifts_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IASchA.TotNonCash) - GetCurrency(IASchA.IAAdjNonCash))
End Sub

Private Sub Header1_Calculation()
    ReturnVal = "IA 1040 Schedule A - Itemized Deductions - Line 21 Attachment"
End Sub

Private Sub IAAGI_Calculation()
    ReturnVal = GetCurrency(IARequired.IAAGI)
End Sub

Private Sub IATax_Calculation()
    Dim IAWHEst As Currency
    Dim OthIAWH As Currency
    
    IAWHEst = GetCurrency(IARequired.TotIAW2WH) + GetCurrency(IARequired.TotW2GWH) + GetCurrency(IARequired.Tot1042S) + GetCurrency(IARequired.TotCapGainWH) + GetCurrency(IARequired.TotDivWH) + GetCurrency(IARequired.TotUnemWH) + GetCurrency(IARequired.TotIntWH) + GetCurrency(IARequired.TotKWH) + GetCurrency(IARequired.TotMiscWH) + GetCurrency(IARequired.TotOIDWH) + GetCurrency(IARequired.Tot1099rWH) + GetCurrency(IARequired.TotOthIncWH) + GetCurrency(IARequired.TotCyLocEst) + GetCurrency(IARequired.TotCYIAEst)
    
    If GetBool(USWResidency.F1040NR) = False Then
        OthIAWH = GetCurrency(USSchA.StateWH3) + GetCurrency(USSchA.StateWH4) + GetCurrency(USSchA.StateWH5)
    Else
        OthIAWH = GetCurrency(USSchANR.StateWH3) + GetCurrency(USSchANR.StateWH4) + GetCurrency(USSchANR.StateWH5)
    End If
    
    If GetBool(IAF126.TpPYNR) = True Or GetBool(IAF126.SpPYNR) = True Then
        ReturnVal = IAWHEst
    Else
        ReturnVal = MinValue(GetCurrency(IASchA.TotStTax), IAWHEst + OthIAWH)
    End If
End Sub

Private Sub Income_Calculation()
    If GetBool(IASchA.GenSales) = True Then
        ReturnVal = 0
    Else
        ReturnVal = 1
    End If
End Sub

Private Sub Invest_Calculation()
    ReturnVal = GetCurrency(USSchA.InvInt)
End Sub

Private Sub Item_Calculation()
    ReturnVal = GetCurrency(IASchA.TotDeductions) + GetCurrency(IASchA.TotOthDed)
End Sub

Private Sub ListExp_Calculation()
    If GetCurrency(IASchA.OthExp) <> 0 Then
        ReturnVal = GetString(IASchA.Ln21SeeAtt)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub ListMisc_Calculation()
    If GetCurrency(IASchA.OthMisc) <> 0 Then
        ReturnVal = GetString(IASchA.OthMiscDesc(0)) + " " + GetString(IASchA.OthMiscDesc(1)) + " " + GetString(IASchA.OthMiscDesc(2)) + " " + GetString(IASchA.OthMiscDesc(3)) + " " + GetString(IASchA.OthMiscDesc(4))
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub Ln21SeeAtt_Calculation()
    If GetCurrency(IASchA.OthLn21Amt(1)) <> 0 Then
        ReturnVal = "See Attached"
    Else
        ReturnVal = GetString(IASchA.OthExpDesc(0))
    End If
End Sub

Private Sub MedDed_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = MaxValue(0, GetCurrency(IASchA.MedExp) - GetCurrency(IASchA.AGI))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub MedExp_Calculation()
'removed the prior year excess advanced PTC from the HealthInsDed since should not offset current year medical expenses
'adjusted medical expense calc for PTC adjustment if claiming on IA 1040 line 18 (if not claiming on line 18 should follow federal treatment of PTC, if on 18 PTC handled on IA 1040)
'change was made based on US 433238 see also CSS ticket 8605571
    Dim HealthInsDed As Currency
    
    HealthInsDed = GetCurrency(IAWHealth.TPInsPrem) + GetCurrency(IAWHealth.TPMedicare) + GetCurrency(IAWHealth.TPLTC) + GetCurrency(IAWHealth.SPInsPrem) + GetCurrency(IAWHealth.SPMedicare) + GetCurrency(IAWHealth.SPLTC)

    If GetBool(USWResidency.F1040NR) = False Then
        If (GetCurrency(IAWHealth.TPInsPrem) + GetCurrency(IAWHealth.SPInsPrem)) = 0 Then
            ReturnVal = MaxValue(0, GetCurrency(USSchA.MedExp) - HealthInsDed)
        Else
            ReturnVal = MaxValue(0, MaxValue(0, GetCurrency(USSchA.MedExp) + GetCurrency(USWMedicalWS.PTCAdj)) - HealthInsDed)
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Mort_Calculation()
    ReturnVal = GetCurrency(IASchA.MortFed) + GetCurrency(IASchA.MortAdj)
End Sub

Private Sub MortAdj_Calculation()
    If GetBool(USWResidency.F1040NR) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(USD1098.StateAdj)
    End If
End Sub

Private Sub MortFed_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USSchA.MortInt) + GetCurrency(USF8396.CrInt)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub MortNot_Calculation()
    ReturnVal = GetCurrency(USSchA.Sfm)
End Sub

Private Sub MtgePrem_Calculation()
    ReturnVal = GetCurrency(USSchA.MtgePrem)
End Sub

Private Sub Mult_Calculation()
    If GetCurrency(IASchA.Expense) > 0 Then
        ReturnVal = MaxValue(0, CDollar(GetFloat(IASchA.IAAGI) * 0.02))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.CombNames)
End Sub

Private Sub OthExp_Calculation()
    ReturnVal = GetCurrency(IAWSchAPrint.TotExp)
End Sub

Private Sub OthExpDesc_Calculation(Index As Integer)
    Dim count As Integer
    Dim Hold As String
    count = 0
    Hold = ""
    
    If GetCurrency(IAWSchAPrint.Legal) <> 0 Then
        If Index = count Then
            Hold = "Legal Fees - Taxable Income"
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.OthLegal) <> 0 Then
        If Index = count Then
            Hold = "Other Legal Fees"
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.Clerical) <> 0 Then
        If Index = count Then
            Hold = "Clerical Help"
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.Custodial) <> 0 Then
        If Index = count Then
            Hold = "Custodial/Investment Fees"
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.Invest) <> 0 Then
        If Index = count Then
            Hold = "Investment Expenses Form 1099s"
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.InsolventLoss) <> 0 Then
        If Index = count Then
            Hold = "Insolvent Losses"
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.CasualtyLoss) <> 0 Then
        If Index = count Then
            Hold = "Form 4684"
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.Appraisal) <> 0 Then
        If Index = count Then
            Hold = "Appraisal Fees"
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.DeprTot) <> 0 Then
        If Index = count Then
            Hold = "Depreciation Computer"
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.Amort) <> 0 Then
        If Index = count Then
            Hold = "Amortization"
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.ExcessDed) <> 0 Then
        If Index = count Then
            Hold = "Excess K-1 Ded"
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.Fees) <> 0 Then
        If Index = count Then
            Hold = "Fees to Collect"
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.Hobby) <> 0 And GetBool(USWResidency.F1040NR) = False Then
        If Index = count Then
            Hold = "Hobby Expenses"
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.Indirect) <> 0 Then
        If Index = count Then
            Hold = "Indirect Pass-through"
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.REMIC) <> 0 Then
        If Index = count Then
            Hold = "REMIC"
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.IRALoss) <> 0 Then
        If Index = count Then
            Hold = "IRA Loss"
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.RepayInc) <> 0 Then
        If Index = count Then
            Hold = "Income Repay"
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.RepaySSB) <> 0 And GetBool(USWResidency.F1040NR) = False Then
        If Index = count Then
            Hold = "SSB Repay"
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.SafeBox) <> 0 Then
        If Index = count Then
            Hold = "Safe Deposit"
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.ServiceCharge) <> 0 Then
        If Index = count Then
            Hold = "Service Charges Div"
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.TaxAdvice) <> 0 Then
        If Index = count Then
            Hold = "Tax Advice"
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.Trustee) <> 0 Then
        If Index = count Then
            Hold = "Trustee's Fees IRA"
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.CreditFees) <> 0 Then
        If Index = count Then
            Hold = "Convenience Fee"
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.OthExp) <> 0 Then
        If Index = count Then
            Hold = GetString(IAWSchAPrint.OtherText)
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.OthExp2) <> 0 Then
        If Index = count Then
            Hold = GetString(IAWSchAPrint.OtherText2)
            count = 99
        Else
            count = count + 1
        End If
    End If
       
    ReturnVal = Hold

End Sub

Private Sub OthList_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetString(USSchA.OtherTaxType)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub OthLn21Amt_Calculation(Index As Integer)
    Dim count As Integer
    Dim Hold As Currency
    count = 0
    Hold = 0
    
    If GetCurrency(IAWSchAPrint.Legal) <> 0 Then
        If Index = count Then
            Hold = GetCurrency(IAWSchAPrint.Legal)
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.OthLegal) <> 0 Then
        If Index = count Then
            Hold = GetCurrency(IAWSchAPrint.OthLegal)
            count = 99
        Else
            count = count + 1
        End If
    End If
       
    If GetCurrency(IAWSchAPrint.Clerical) <> 0 Then
        If Index = count Then
            Hold = GetCurrency(IAWSchAPrint.Clerical)
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.Custodial) <> 0 Then
        If Index = count Then
            Hold = GetCurrency(IAWSchAPrint.Custodial)
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.Invest) <> 0 Then
        If Index = count Then
            Hold = GetCurrency(IAWSchAPrint.Invest)
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.InsolventLoss) <> 0 Then
        If Index = count Then
            Hold = GetCurrency(IAWSchAPrint.InsolventLoss)
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    
    If GetCurrency(IAWSchAPrint.CasualtyLoss) <> 0 Then
        If Index = count Then
            Hold = GetCurrency(IAWSchAPrint.CasualtyLoss)
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.Appraisal) <> 0 Then
        If Index = count Then
            Hold = GetCurrency(IAWSchAPrint.Appraisal)
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.DeprTot) <> 0 Then
        If Index = count Then
            Hold = GetCurrency(IAWSchAPrint.DeprTot)
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.Amort) <> 0 Then
        If Index = count Then
            Hold = GetCurrency(IAWSchAPrint.Amort)
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.ExcessDed) <> 0 Then
        If Index = count Then
            Hold = GetCurrency(IAWSchAPrint.ExcessDed)
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.Fees) <> 0 Then
        If Index = count Then
            Hold = GetCurrency(IAWSchAPrint.Fees)
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.Hobby) <> 0 And GetBool(USWResidency.F1040NR) = False Then
        If Index = count Then
            Hold = GetCurrency(IAWSchAPrint.Hobby)
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.Indirect) <> 0 Then
        If Index = count Then
            Hold = GetCurrency(IAWSchAPrint.Indirect)
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.REMIC) <> 0 Then
        If Index = count Then
            Hold = GetCurrency(IAWSchAPrint.REMIC)
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.IRALoss) <> 0 Then
        If Index = count Then
            Hold = GetCurrency(IAWSchAPrint.IRALoss)
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.RepayInc) <> 0 Then
        If Index = count Then
            Hold = GetCurrency(IAWSchAPrint.RepayInc)
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.RepaySSB) <> 0 And GetBool(USWResidency.F1040NR) = False Then
        If Index = count Then
            Hold = GetCurrency(IAWSchAPrint.RepaySSB)
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.SafeBox) <> 0 Then
        If Index = count Then
            Hold = GetCurrency(IAWSchAPrint.SafeBox)
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.ServiceCharge) <> 0 Then
        If Index = count Then
            Hold = GetCurrency(IAWSchAPrint.ServiceCharge)
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.TaxAdvice) <> 0 Then
        If Index = count Then
            Hold = GetCurrency(IAWSchAPrint.TaxAdvice)
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.Trustee) <> 0 Then
        If Index = count Then
            Hold = GetCurrency(IAWSchAPrint.Trustee)
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.CreditFees) <> 0 Then
        If Index = count Then
            Hold = GetCurrency(IAWSchAPrint.CreditFees)
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.OthExp) <> 0 Then
        If Index = count Then
            Hold = GetCurrency(IAWSchAPrint.OthExp)
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.OthExp2) <> 0 Then
        If Index = count Then
            Hold = GetCurrency(IAWSchAPrint.OthExp2)
            count = 99
        Else
            count = count + 1
        End If
    End If
       
    ReturnVal = Hold
End Sub

Private Sub OthMisc_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IASchA.TotOthMisc) + GetCurrency(IASchA.IAAdjOthMisc))
End Sub

Private Sub OthMiscDesc_Calculation(Index As Integer)
    Dim count As Integer
    Dim Hold As String
    count = 0
    Hold = ""
    
    If GetCurrency(IAWSchAPrint.Form4684) <> 0 Then
        If Index = count Then
            Hold = "Casualty and theft loss"
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.GamblingLoss) <> 0 And GetBool(USWResidency.F1040NR) = False Then
        If Index = count Then
            Hold = "Gambling losses"
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.K1DedPort) <> 0 Then
        If Index = count Then
            Hold = "Schedule K-1"
            count = 99
        Else
            count = count + 1
        End If
    End If
    
     If GetCurrency(IAWSchAPrint.ImpWrkExp) <> 0 Then
        If Index = count Then
            Hold = "Impairment-related work expenses"
            count = 99
        Else
            count = count + 1
        End If
    End If
    
     If GetCurrency(IAWSchAPrint.TotEstK1) <> 0 And GetBool(USWResidency.F1040NR) = False Then
        If Index = count Then
            Hold = "Federal estate tax"
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.Repay) <> 0 Then
        If Index = count Then
            Hold = "Claim repayments"
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.Bond) <> 0 And GetBool(USWResidency.F1040NR) = False Then
        If Index = count Then
            Hold = "Amortizable bond premiums"
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.Pension) <> 0 Then
        If Index = count Then
            Hold = "Unrecovered pension investments"
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWSchAPrint.Debt) <> 0 Then
        If Index = count Then
            Hold = "Ordinary loss"
            count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IASchA.IAAdjOthMisc) <> 0 Then
        If Index = count Then
            Hold = GetString(IASchA.IAAdjOthMiscDesc)
            count = 99
        Else
            count = count + 1
        End If
    End If        
    
    ReturnVal = Hold

End Sub

Private Sub OthTax_Calculation()
'review to default calc - fed not allowing foreign taxes paid.
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USSchA.OtherTax)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Over_Calculation()
    ReturnVal = GetCurrency(IAWContLimit.PYTot)
    'If GetBool(USWResidency.F1040NR) = False Then
    '    ReturnVal = GetCurrency(USSchA.Carry)
    'Else
    '    ReturnVal = GetCurrency(USSchANR.Carry)
    'End If
End Sub

Private Sub Perc_Calculation()
    Dim TopLim As Double
        
    If GetCurrency(IASchA.YouNet) < 0 And GetCurrency(IASchA.SpNet) < 0 Then
        If GetCurrency(IASchA.YouNet) < GetCurrency(IASchA.SpNet) Then
            ReturnVal = 0
        Else
            ReturnVal = 1
        End If
    ElseIf GetCurrency(IASchA.YouNet) < 0 Then
        ReturnVal = 0
    ElseIf GetCurrency(IASchA.YouNet) > 0 And GetCurrency(IASchA.TotNet) <= 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IASchA.TotNet) = 0 Then
        ReturnVal = 0
    Else
        TopLim = MinValue(1#, Round(GetFloat(IASchA.YouNet) / GetFloat(IASchA.TotNet), 3))
        ReturnVal = MaxValue(0, TopLim)      
    End If
End Sub

Private Sub PrintSchA_Calculation()
    If GetBool(IARequired.LowInc) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetNumber(IAF1040.ItemCheck)
    End If
End Sub

Private Sub PrLn21SeeAtt_Calculation()
    If GetCurrency(IASchA.OthLn21Amt(1)) <> 0 And GetNumber(IASchA.PrintSchA) = 1 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Prop_Calculation()
    ReturnVal = GetCurrency(USSchA.PerPropTax)
End Sub

Private Sub PtsNot_Calculation()
    ReturnVal = GetCurrency(USSchA.Points)
End Sub

Private Sub RealEst_Calculation()
    ReturnVal = GetCurrency(USSchA.RealTax)
End Sub

Private Sub SalesTax_Calculation()
    ReturnVal = GetCurrency(USSchA.SalesTax)
End Sub

Private Sub SchAMilesDed_Calculation()
'per fed, no change for 2018 remains at 14 cents
    Dim Con1 As Currency
    
    If GetBool(USWResidency.F1040NR) = False Then
        Con1 = CDollar(GetFloat(USSchA.ConMiles) * 14#)
    Else
        Con1 = CDollar(GetFloat(USSchANR.ConMiles) * 14#)
    End If
    
    ReturnVal = Con1
End Sub

Private Sub SchoolTax_Calculation()
    If GetBool(IAF1040.MFJ) = True Or GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetCurrency(USZIA1040.IAPYSurtaxA) + GetCurrency(USZIA1040.IAPYSurtaxB)
    Else
        ReturnVal = GetCurrency(USZIA1040.IAPYSurtaxA)
    End If
End Sub

Private Sub SpNet_Calculation()
    If GetBool(IAF1040.CombMFS) = True Or GetBool(IAF1040.MFS) = True Then
        ReturnVal = GetCurrency(IAF1040.BNet)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SpPro_Calculation()
    If GetBool(IAF1040.CombMFS) = True Or GetBool(IAF1040.MFS) = True Then
        ReturnVal = MaxValue(0, GetCurrency(IASchA.Item) - GetCurrency(IASchA.YouPC))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

Private Sub StTax_Calculation()
    If GetBool(IASchA.GenSales) = True Then
        ReturnVal = GetCurrency(IASchA.SalesTax)
    Else
        ReturnVal = GetCurrency(IASchA.TotIncTax)
    End If
End Sub

Private Sub TaxFee_Calculation()
    ReturnVal = 0
    'If GetBool(USWResidency.F1040NR) = False Then
    '    ReturnVal = GetCurrency(USSchA.TaxPrep)
    'Else
    '    ReturnVal = GetCurrency(USSchANR.TaxPrep)
    'End If
End Sub

Private Sub TaxPd_Calculation()
    ReturnVal = GetCurrency(IASchA.StTax) + GetCurrency(IASchA.RealEst) + GetCurrency(IASchA.Prop) + GetCurrency(IASchA.OthTax)
End Sub

Private Sub Theft_Calculation()
    ReturnVal = GetCurrency(IA4684.SctATot)
End Sub

Private Sub TotAdoptAmt_Calculation()
    ReturnVal = GetCurrency(IASchA.AdoptAmt(0)) + GetCurrency(IASchA.AdoptAmt(1)) + GetCurrency(IASchA.AdoptAmt(2)) + GetCurrency(IASchA.AdoptAmt(3)) + GetCurrency(IASchA.AdoptAmt(4))
End Sub

Private Sub TotContrib_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USSchA.Cash)
    Else
        ReturnVal = GetCurrency(USSchANR.Cash)
    End If
End Sub

Private Sub TotDeductions_Calculation()
' updated for 2018 - RJ
    Dim Limit As Currency
    
    If FedFS() = 1 Then
        Limit = 266700@
    ElseIf FedFS() = 3 Then
        Limit = 160000@
    ElseIf FedFS() = 4 Then
        Limit = 293350@
    Else
        Limit = 320000@
    End If
    
    If GetCurrency(IASchA.IAAGI) > Limit Then
        ReturnVal = GetCurrency(IAWItmDed.LimitDed)
    Else
        ReturnVal = GetCurrency(IASchA.OthMisc) + GetCurrency(IASchA.AllowExp) + GetCurrency(IASchA.Theft) + GetCurrency(IASchA.TotGifts) + GetCurrency(IASchA.TotInt) + GetCurrency(IASchA.TaxPd) + GetCurrency(IASchA.MedDed)
    End If
End Sub

Private Sub TotDisableAmt_Calculation()
    Dim TotDisable As Currency
    
    TotDisable = GetCurrency(IASchA.DisableAmt(0)) + GetCurrency(IASchA.DisableAmt(1)) + GetCurrency(IASchA.DisableAmt(2)) + GetCurrency(IASchA.DisableAmt(3)) + GetCurrency(IASchA.DisableAmt(4))

    ReturnVal = MinValue(5000@, TotDisable)
End Sub

Private Sub TotGifts_Calculation()
    ReturnVal = GetCurrency(IAWContLimit.CYTotAfter)
End Sub

Private Sub TotIncTax_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IASchA.TotStTax) + GetCurrency(IASchA.SchoolTax) - GetCurrency(IASchA.IATax))
End Sub

Private Sub TotInt_Calculation()
    ReturnVal = GetCurrency(IASchA.Mort) + GetCurrency(IASchA.MortNot) + GetCurrency(IASchA.PtsNot) + GetCurrency(IASchA.Invest)
End Sub

Private Sub TotMilesDed_Calculation()
    Dim Con1 As Currency
    
    If GetBool(USWResidency.F1040NR) = False Then
        Con1 = CDollar(GetFloat(USSchA.ConMiles) * 39#)
    Else
        Con1 = CDollar(GetFloat(USSchANR.ConMiles) * 39#)
    End If
    
    ReturnVal = Con1
End Sub

Private Sub TotNet_Calculation()
    ReturnVal = GetCurrency(IASchA.SpNet) + GetCurrency(IASchA.YouNet)
End Sub

Private Sub TotNonCash_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USSchA.NonCash)
    Else
        ReturnVal = GetCurrency(USSchANR.NonCash)
    End If
End Sub

Private Sub TotOthDed_Calculation()
    ReturnVal = GetCurrency(IASchA.TotDisableAmt) + GetCurrency(IASchA.AllowAdopt) + GetCurrency(IASchA.AddMilesDed)
End Sub

Private Sub TotOthMisc_Calculation()
    ReturnVal = GetCurrency(IAWSchAPrint.TotOthDed)
End Sub

Private Sub TotStTax_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = MaxValue(0, GetCurrency(USSchA.StateWH1) + GetCurrency(USSchA.StateWH2) + GetCurrency(USSchA.LocalWH) + GetCurrency(USSchA.StateWH3) + GetCurrency(USSchA.StateWH4) + GetCurrency(USSchA.StateWH5) - GetCurrency(USSchA.WHOff))
    Else
        ReturnVal = MaxValue(0, GetCurrency(USSchANR.StateWH1) + GetCurrency(USSchANR.StateWH2) + GetCurrency(USSchANR.LocalWH) + GetCurrency(USSchANR.StateWH3) + GetCurrency(USSchANR.StateWH4) + GetCurrency(USSchANR.StateWH5) - GetCurrency(USSchANR.WHOff))
    End If
End Sub

Private Sub Unreimb_Calculation()
    ReturnVal = GetCurrency(IAWSchAPrint.TotOtherExp)
End Sub

Private Sub YouNet_Calculation()
    If GetBool(IAF1040.CombMFS) = True Or GetBool(IAF1040.MFS) = True Then
        ReturnVal = GetCurrency(IAF1040.ANet)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub YouPC_Calculation()
    ReturnVal = CDollar(GetFloat(IASchA.Perc) * GetFloat(IASchA.Item))
End Sub

