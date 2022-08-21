Private Sub Code_Calculation(Index As Integer)
    Dim count As Integer
    Dim Hold As String
    count = 0
    Hold = ""
    
    If GetCurrency(IAWOthInc.TPOth1) <> 0 Or GetCurrency(IAWOthInc.SPOth1) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPOth2) <> 0 Or GetCurrency(IAWOthInc.SPOth2) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPBabySit) <> 0 Or GetCurrency(IAWOthInc.SPBabySit) <> 0 Then
        If Index = count Then
           Hold = "a"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPBonus) <> 0 Or GetCurrency(IAWOthInc.SPBonus) <> 0 Then
        If Index = count Then
           Hold = "b"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPIAEd) <> 0 Or GetCurrency(IAWOthInc.SPIAEd) <> 0 Then
        If Index = count Then
           Hold = "d"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPDirector) <> 0 Or GetCurrency(IAWOthInc.SPDirector) <> 0 Then
        If Index = count Then
           Hold = "e"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPIntangDrill) <> 0 Or GetCurrency(IAWOthInc.SPIntangDrill) <> 0 Then
        If Index = count Then
           Hold = "f"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPExecutor) <> 0 Or GetCurrency(IAWOthInc.SPExecutor) <> 0 Then
        If Index = count Then
           Hold = "g"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPFirstHmBuy) <> 0 Or GetCurrency(IAWOthInc.SPFirstHmBuy) <> 0 Then
        If Index = count Then
           Hold = "h"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPK1) <> 0 Or GetCurrency(IAWOthInc.SPK1) <> 0 Then
        If Index = count Then
           Hold = "i"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPRefundCr) <> 0 Or GetCurrency(IAWOthInc.SPRefundCr) <> 0 Then
        If Index = count Then
           Hold = "j"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPStRefund) <> 0 Or GetCurrency(IAWOthInc.SPStRefund) <> 0 Then
        If Index = count Then
           Hold = "k"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPDepl) <> 0 Or GetCurrency(IAWOthInc.SPDepl) <> 0 Then
        If Index = count Then
           Hold = "l"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPJury) <> 0 Or GetCurrency(IAWOthInc.SPJury) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPPerRent) <> 0 Or GetCurrency(IAWOthInc.SPPerRent) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TP8814) <> 0 Or GetCurrency(IAWOthInc.SP8814) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPMSA) <> 0 Or GetCurrency(IAWOthInc.SPMSA) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPMedMSA) <> 0 Or GetCurrency(IAWOthInc.SPMedMSA) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPLTC) <> 0 Or GetCurrency(IAWOthInc.SPLTC) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPMisc) <> 0 Or GetCurrency(IAWOthInc.SPMisc) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPAlaska) <> 0 Or GetCurrency(IAWOthInc.SPAlaska) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPCoverdell) <> 0 Or GetCurrency(IAWOthInc.SPCoverdell) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPCanceled) <> 0 Or GetCurrency(IAWOthInc.SPCanceled) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPPshipCan) <> 0 Or GetCurrency(IAWOthInc.SPPshipCan) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPHSA) <> 0 Or GetCurrency(IAWOthInc.SPHSA) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPAltTrade) <> 0 Or GetCurrency(IAWOthInc.SPAltTrade) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPRecapTuit) <> 0 Or GetCurrency(IAWOthInc.SPRecapTuit) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPRecapChar) <> 0 Or GetCurrency(IAWOthInc.SPRecapChar) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TP5471) <> 0 Or GetCurrency(IAWOthInc.SP5471) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPHobby) <> 0 Or GetCurrency(IAWOthInc.SPHobby) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TP8621) <> 0 Or GetCurrency(IAWOthInc.SP8621) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPDefDist) <> 0 Or GetCurrency(IAWOthInc.SPDefDist) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPDisaster) <> 0 Or GetCurrency(IAWOthInc.SPDisaster) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPFoster) <> 0 Or GetCurrency(IAWOthInc.SPFoster) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If    
    
    If GetCurrency(IAWOthInc.TPCredAdj) <> 0 Or GetCurrency(IAWOthInc.SPCredAdj) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPPYNPTC) <> 0 Or GetCurrency(IAWOthInc.SPPYNPTC) <> 0 Then
        If Index = count Then
           Hold = "n"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TP1099QA) <> 0 Or GetCurrency(IAWOthInc.SP1099QA) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPAirline) <> 0 Or GetCurrency(IAWOthInc.SPAirline) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TP1099B) <> 0 Or GetCurrency(IAWOthInc.SP1099B) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPIAABLE) <> 0 Or GetCurrency(IAWOthInc.SPIAABLE) <> 0 Then
        If Index = count Then
           Hold = "o"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPBusPass) <> 0 Or GetCurrency(IAWOthInc.SPBusPass) <> 0 Then
        If Index = count Then
           Hold = "p"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPFarmLoss) <> 0 Or GetCurrency(IAWOthInc.SPFarmLoss) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TP8824) <> 0 Or GetCurrency(IAWOthInc.SP8824) <> 0 Then
        If Index = count Then
           Hold = "q"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPStudLoanDis) <> 0 Or GetCurrency(IAWOthInc.SPStudLoanDis) <> 0 Then
        If Index = count Then
           Hold = "r"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TP4684) <> 0 Or GetCurrency(IAWOthInc.SP4684) <> 0 Then
        If Index = count Then
           Hold = "s"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TP3903) <> 0 Or GetCurrency(IAWOthInc.SP3903) <> 0 Then
        If Index = count Then
           Hold = "t"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPBusInt) <> 0 Or GetCurrency(IAWOthInc.SPBusInt) <> 0 Then
        If Index = count Then
           Hold = "u"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPEntExp) <> 0 Or GetCurrency(IAWOthInc.SPEntExp) <> 0 Then
        If Index = count Then
           Hold = "v"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TP2106) <> 0 Or GetCurrency(IAWOthInc.SP2106) <> 0 Then
        If Index = count Then
           Hold = "w"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPOthNC) <> 0 Or GetCurrency(IAWOthInc.SPOthNC) <> 0 Then
        If Index = count Then
           Hold = "x"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    ReturnVal = Hold
    
End Sub

Private Sub Desc_Calculation()
    Dim Total As Currency
    
    Total = GetCurrency(IAWOthInc.TPTot) + GetCurrency(IAWOthInc.SPTot)
    
    ReturnVal = CStr(Total)
End Sub

Private Sub Description_Calculation(Index As Integer)
    Dim count As Integer
    Dim Hold As String
    count = 0
    Hold = ""
    
    If GetCurrency(IAWOthInc.TPOth1) <> 0 Or GetCurrency(IAWOthInc.SPOth1) <> 0 Then
        If Index = count Then
           Hold = GetString(IAWOthInc.Txt1)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPOth2) <> 0 Or GetCurrency(IAWOthInc.SPOth2) <> 0 Then
        If Index = count Then
           Hold = GetString(IAWOthInc.Txt2)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPBabySit) <> 0 Or GetCurrency(IAWOthInc.SPBabySit) <> 0 Then
        If Index = count Then
           Hold = "Baby-sitting income not reported on federal Schedule C"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPBonus) <> 0 Or GetCurrency(IAWOthInc.SPBonus) <> 0 Then
        If Index = count Then
           Hold = "Bonus depreciation/section 179 adjustment"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPIAEd) <> 0 Or GetCurrency(IAWOthInc.SPIAEd) <> 0 Then
        If Index = count Then
           Hold = "College Savings Iowa or Iowa Advisor 529 Plan"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPDirector) <> 0 Or GetCurrency(IAWOthInc.SPDirector) <> 0 Then
        If Index = count Then
           Hold = "Director's fees"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPIntangDrill) <> 0 Or GetCurrency(IAWOthInc.SPIntangDrill) <> 0 Then
        If Index = count Then
           Hold = "Drilling"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPExecutor) <> 0 Or GetCurrency(IAWOthInc.SPExecutor) <> 0 Then
        If Index = count Then
           Hold = "Executor's fees"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPFirstHmBuy) <> 0 Or GetCurrency(IAWOthInc.SPFirstHmBuy) <> 0 Then
        If Index = count Then
           Hold = "First-time homebuyers account non-qualifying withdrawals"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPK1) <> 0 Or GetCurrency(IAWOthInc.SPK1) <> 0 Then
        If Index = count Then
           Hold = "Partnership income and/or S Corporation income"
           count = 99
        Else
            count = count + 1
        End If
    End If    
    
    If GetCurrency(IAWOthInc.TPRefundCr) <> 0 Or GetCurrency(IAWOthInc.SPRefundCr) <> 0 Then
        If Index = count Then
           Hold = "Refundable Iowa credits"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPStRefund) <> 0 Or GetCurrency(IAWOthInc.SPStRefund) <> 0 Then
        If Index = count Then
           Hold = "State income tax refunds"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPDepl) <> 0 Or GetCurrency(IAWOthInc.SPDepl) <> 0 Then
        If Index = count Then
           Hold = "Wells"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPJury) <> 0 Or GetCurrency(IAWOthInc.SPJury) <> 0 Then
        If Index = count Then
           Hold = "Jury pay"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPPerRent) <> 0 Or GetCurrency(IAWOthInc.SPPerRent) <> 0 Then
        If Index = count Then
           Hold = "Income from personal property"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TP8814) <> 0 Or GetCurrency(IAWOthInc.SP8814) <> 0 Then
        If Index = count Then
           Hold = "Child's income amount, federal Form 8814"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPMSA) <> 0 Or GetCurrency(IAWOthInc.SPMSA) <> 0 Then
        If Index = count Then
           Hold = "MSA distributions, federal Form 8853"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPMedMSA) <> 0 Or GetCurrency(IAWOthInc.SPMedMSA) <> 0 Then
        If Index = count Then
           Hold = "Medicare Advantage distributions, federal Form 8853"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPLTC) <> 0 Or GetCurrency(IAWOthInc.SPLTC) <> 0 Then
        If Index = count Then
           Hold = "Long-term care distribution, federal Form 8853"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPMisc) <> 0 Or GetCurrency(IAWOthInc.SPMisc) <> 0 Then
        If Index = count Then
           Hold = "Form 1099-MISC, boxes 3 or 8"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPAlaska) <> 0 Or GetCurrency(IAWOthInc.SPAlaska) <> 0 Then
        If Index = count Then
           Hold = "Alaska Permanent Fund dividends"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPCoverdell) <> 0 Or GetCurrency(IAWOthInc.SPCoverdell) <> 0 Then
        If Index = count Then
           Hold = "Coverdell ESA Or Qualified Tuition Program"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPCanceled) <> 0 Or GetCurrency(IAWOthInc.SPCanceled) <> 0 Then
        If Index = count Then
           Hold = "Cancellation of nonbusiness debt, federal Form 1099-C"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPPshipCan) <> 0 Or GetCurrency(IAWOthInc.SPPshipCan) <> 0 Then
        If Index = count Then
           Hold = "Cancellation of business debt, Partnership Schedule K-1"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPHSA) <> 0 Or GetCurrency(IAWOthInc.SPHSA) <> 0 Then
        If Index = count Then
           Hold = "HSA distributions, federal Form 8889"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPAltTrade) <> 0 Or GetCurrency(IAWOthInc.SPAltTrade) <> 0 Then
        If Index = count Then
           Hold = "Alternative trade adjustment assistance payments"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPRecapTuit) <> 0 Or GetCurrency(IAWOthInc.SPRecapTuit) <> 0 Then
        If Index = count Then
           Hold = "Recapture of prior year tuition and fees deduction"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPRecapChar) <> 0 Or GetCurrency(IAWOthInc.SPRecapChar) <> 0 Then
        If Index = count Then
           Hold = "Recapture of charitable contribution deduction"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TP5471) <> 0 Or GetCurrency(IAWOthInc.SP5471) <> 0 Then
        If Index = count Then
           Hold = "Income from a foreign corporation, federal Form 5471"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPHobby) <> 0 Or GetCurrency(IAWOthInc.SPHobby) <> 0 Then
        If Index = count Then
           Hold = "Hobby income"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TP8621) <> 0 Or GetCurrency(IAWOthInc.SP8621) <> 0 Then
        If Index = count Then
           Hold = "Income or loss from Section 1291, federal Form 8621"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPDefDist) <> 0 Or GetCurrency(IAWOthInc.SPDefDist) <> 0 Then
        If Index = count Then
           Hold = "Loss on excess deferral distribution"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPDisaster) <> 0 Or GetCurrency(IAWOthInc.SPDisaster) <> 0 Then
        If Index = count Then
           Hold = "Disaster relief payments"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPFoster) <> 0 Or GetCurrency(IAWOthInc.SPFoster) <> 0 Then
        If Index = count Then
           Hold = "Medicaid waiver payments to care provider"
           count = 99
        Else
            count = count + 1
        End If
    End If    
    
    If GetCurrency(IAWOthInc.TPCredAdj) <> 0 Or GetCurrency(IAWOthInc.SPCredAdj) <> 0 Then
        If Index = count Then
           Hold = "Credit adjustment income, federal Forms 6478 and 8864"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPPYNPTC) <> 0 Or GetCurrency(IAWOthInc.SPPYNPTC) <> 0 Then
        If Index = count Then
           Hold = "Net Premium Tax Credit"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TP1099QA) <> 0 Or GetCurrency(IAWOthInc.SP1099QA) <> 0 Then
        If Index = count Then
           Hold = "Distributions from ABLE account"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPAirline) <> 0 Or GetCurrency(IAWOthInc.SPAirline) <> 0 Then
        If Index = count Then
           Hold = "Qualified airline payments"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TP1099B) <> 0 Or GetCurrency(IAWOthInc.SP1099B) <> 0 Then
        If Index = count Then
           Hold = "Foreign currency transaction"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPIAABLE) <> 0 Or GetCurrency(IAWOthInc.SPIAABLE) <> 0 Then
        If Index = count Then
           Hold = "Distributions from an Iowa ABLE account"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPBusPass) <> 0 Or GetCurrency(IAWOthInc.SPBusPass) <> 0 Then
        If Index = count Then
           Hold = "Employer provided bus pass or transportation expenses"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPFarmLoss) <> 0 Or GetCurrency(IAWOthInc.SPFarmLoss) <> 0 Then
        If Index = count Then
           Hold = "Section 461(j) excess farm loss limitation adjustments"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TP8824) <> 0 Or GetCurrency(IAWOthInc.SP8824) <> 0 Then
        If Index = count Then
           Hold = "IA 8824 worksheet, due to nonconformity"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPStudLoanDis) <> 0 Or GetCurrency(IAWOthInc.SPStudLoanDis) <> 0 Then
        If Index = count Then
           Hold = "Discharge of student loan debt - death or disability"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TP4684) <> 0 Or GetCurrency(IAWOthInc.SP4684) <> 0 Then
        If Index = count Then
           Hold = "IA 4684 worksheet, due to nonconformity"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TP3903) <> 0 Or GetCurrency(IAWOthInc.SP3903) <> 0 Then
        If Index = count Then
           Hold = "IA 3903 worksheet line 8a, due to nonconformity"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPBusInt) <> 0 Or GetCurrency(IAWOthInc.SPBusInt) <> 0 Then
        If Index = count Then
           Hold = "Business interest expense limitation, due to nonconformity"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPEntExp) <> 0 Or GetCurrency(IAWOthInc.SPEntExp) <> 0 Then
        If Index = count Then
           Hold = "Entertainment expenses, due to nonconformity"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TP2106) <> 0 Or GetCurrency(IAWOthInc.SP2106) <> 0 Then
        If Index = count Then
           Hold = "IA 2106 worksheet line 8, due to nonconformity"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPOthNC) <> 0 Or GetCurrency(IAWOthInc.SPOthNC) <> 0 Then
        If Index = count Then
           Hold = "Other nonconformity adjustments"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    ReturnVal = Hold
End Sub

Private Sub Exist_Calculation()
    ReturnVal = 1
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.CombNames)
End Sub

Private Sub Print_Calculation()
    If GetCurrency(IAWOthInc.TPTot) <> 0 Or GetCurrency(IAWOthInc.SPTot) <> 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SP1099B_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.SP1099B)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SP1099QA_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.SP1099QA)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SP2106_Calculation()
    ReturnVal = GetCurrency(IA2106.IAWages, FieldCopies(IA2106.Spouse))
End Sub

Private Sub SP3903_Calculation()
    ReturnVal = GetCurrency(IARequired.SIAExReimb)
End Sub

Private Sub SP5471_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.SP5471)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SP8621_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.SP8621)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SP8814_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.SP8814)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SP8824_Calculation()
    ReturnVal = GetCurrency(IARequired.SP8824)
End Sub

Private Sub SPAirline_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.SPAirline)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPAlaska_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.SPAlaska)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPAltTrade_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.SPAltTrade)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPAmount_Calculation(Index As Integer)
    Dim count As Integer
    Dim Hold As Currency
    count = 0
    Hold = 0
    
    If GetCurrency(IAWOthInc.TPOth1) <> 0 Or GetCurrency(IAWOthInc.SPOth1) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPOth1)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPOth2) <> 0 Or GetCurrency(IAWOthInc.SPOth2) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPOth2)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPBabySit) <> 0 Or GetCurrency(IAWOthInc.SPBabySit) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPBabySit)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPBonus) <> 0 Or GetCurrency(IAWOthInc.SPBonus) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPBonus)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPIAEd) <> 0 Or GetCurrency(IAWOthInc.SPIAEd) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPIAEd)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPDirector) <> 0 Or GetCurrency(IAWOthInc.SPDirector) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPDirector)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPIntangDrill) <> 0 Or GetCurrency(IAWOthInc.SPIntangDrill) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPIntangDrill)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPExecutor) <> 0 Or GetCurrency(IAWOthInc.SPExecutor) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPExecutor)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPFirstHmBuy) <> 0 Or GetCurrency(IAWOthInc.SPFirstHmBuy) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPFirstHmBuy)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPK1) <> 0 Or GetCurrency(IAWOthInc.SPK1) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPK1)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPRefundCr) <> 0 Or GetCurrency(IAWOthInc.SPRefundCr) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPRefundCr)
           count = 99
        Else
            count = count + 1
        End If
    End If

    If GetCurrency(IAWOthInc.TPStRefund) <> 0 Or GetCurrency(IAWOthInc.SPStRefund) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPStRefund)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPDepl) <> 0 Or GetCurrency(IAWOthInc.SPDepl) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPDepl)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPJury) <> 0 Or GetCurrency(IAWOthInc.SPJury) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPJury)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPPerRent) <> 0 Or GetCurrency(IAWOthInc.SPPerRent) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPPerRent)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TP8814) <> 0 Or GetCurrency(IAWOthInc.SP8814) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SP8814)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPMSA) <> 0 Or GetCurrency(IAWOthInc.SPMSA) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPMSA)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPMedMSA) <> 0 Or GetCurrency(IAWOthInc.SPMedMSA) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPMedMSA)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPLTC) <> 0 Or GetCurrency(IAWOthInc.SPLTC) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPLTC)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPMisc) <> 0 Or GetCurrency(IAWOthInc.SPMisc) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPMisc)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPAlaska) <> 0 Or GetCurrency(IAWOthInc.SPAlaska) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPAlaska)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPCoverdell) <> 0 Or GetCurrency(IAWOthInc.SPCoverdell) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPCoverdell)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPCanceled) <> 0 Or GetCurrency(IAWOthInc.SPCanceled) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPCanceled)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPPshipCan) <> 0 Or GetCurrency(IAWOthInc.SPPshipCan) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPPshipCan)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPHSA) <> 0 Or GetCurrency(IAWOthInc.SPHSA) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPHSA)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPAltTrade) <> 0 Or GetCurrency(IAWOthInc.SPAltTrade) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPAltTrade)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPRecapTuit) <> 0 Or GetCurrency(IAWOthInc.SPRecapTuit) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPRecapTuit)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPRecapChar) <> 0 Or GetCurrency(IAWOthInc.SPRecapChar) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPRecapChar)
           count = 99
        Else
            count = count + 1
        End If
    End If    
   
    If GetCurrency(IAWOthInc.TP5471) <> 0 Or GetCurrency(IAWOthInc.SP5471) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SP5471)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPHobby) <> 0 Or GetCurrency(IAWOthInc.SPHobby) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPHobby)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TP8621) <> 0 Or GetCurrency(IAWOthInc.SP8621) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SP8621)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPDefDist) <> 0 Or GetCurrency(IAWOthInc.SPDefDist) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPDefDist)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPDisaster) <> 0 Or GetCurrency(IAWOthInc.SPDisaster) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPDisaster)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPFoster) <> 0 Or GetCurrency(IAWOthInc.SPFoster) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPFoster)
           count = 99
        Else
            count = count + 1
        End If
    End If    
    
    If GetCurrency(IAWOthInc.TPCredAdj) <> 0 Or GetCurrency(IAWOthInc.SPCredAdj) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPCredAdj)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPPYNPTC) <> 0 Or GetCurrency(IAWOthInc.SPPYNPTC) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPPYNPTC)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TP1099QA) <> 0 Or GetCurrency(IAWOthInc.SP1099QA) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SP1099QA)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPAirline) <> 0 Or GetCurrency(IAWOthInc.SPAirline) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPAirline)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TP1099B) <> 0 Or GetCurrency(IAWOthInc.SP1099B) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SP1099B)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPIAABLE) <> 0 Or GetCurrency(IAWOthInc.SPIAABLE) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPIAABLE)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPBusPass) <> 0 Or GetCurrency(IAWOthInc.SPBusPass) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPBusPass)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPFarmLoss) <> 0 Or GetCurrency(IAWOthInc.SPFarmLoss) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPFarmLoss)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TP8824) <> 0 Or GetCurrency(IAWOthInc.SP8824) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SP8824)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPStudLoanDis) <> 0 Or GetCurrency(IAWOthInc.SPStudLoanDis) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPStudLoanDis)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TP4684) <> 0 Or GetCurrency(IAWOthInc.SP4684) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SP4684)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TP3903) <> 0 Or GetCurrency(IAWOthInc.SP3903) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SP3903)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPBusInt) <> 0 Or GetCurrency(IAWOthInc.SPBusInt) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPBusInt)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPEntExp) <> 0 Or GetCurrency(IAWOthInc.SPEntExp) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPEntExp)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TP2106) <> 0 Or GetCurrency(IAWOthInc.SP2106) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SP2106)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPOthNC) <> 0 Or GetCurrency(IAWOthInc.SPOthNC) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.SPOthNC)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    ReturnVal = Hold
End Sub

Private Sub SPBonus_Calculation()
    ReturnVal = GetCurrency(IAWOthInc.TotBonus) - GetCurrency(IAWOthInc.TPBonus)
End Sub

Private Sub SPCanceled_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.SPCanceled)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPCoverdell_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.SPCoverdell)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPCredAdj_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.SPCredAdj)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPDefDist_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.SPDefDist)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPDisaster_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.SPDisaster)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPFoster_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.SPFoster)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPHobby_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.SPHobby)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPHSA_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.SPHSA)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPJury_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.SPJury)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPK1_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = MaxValue(0, GetCurrency(USWOthInc.SPK1))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPLTC_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.SPLTC)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPMedMSA_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.SPMedMSA)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPMisc_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.SPMisc) + GetCurrency(USWOthInc.SPIndianGaming) + GetCurrency(USWOthInc.SPTribDist) + GetCurrency(USWOthInc.SPNativeDist)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPMSA_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.SP8853)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPName_Calculation()
    ReturnVal = GetString(USWBasicInfo.SPCommon)
End Sub

Private Sub SPOth1_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.SPOth1)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPOth2_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.SPOth2)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPOthNC_Calculation()
    ReturnVal = GetCurrency(IAWNonConformAdj.SPTotNonConformAdj)
End Sub

Private Sub SPPerRent_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.SPPerRent)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPPshipCan_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.SPPshipCan)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPRecapChar_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.SPRecapChContTax) + GetCurrency(USWOthInc.SPRecapChar)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPRecapTuit_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.SPRecapTuit)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPTot_Calculation()
    ReturnVal = GetCurrency(IAWOthInc.SPOth1) + GetCurrency(IAWOthInc.SPOth2) + GetCurrency(IAWOthInc.SPBabySit) + GetCurrency(IAWOthInc.SPBonus) + GetCurrency(IAWOthInc.SPIAEd) + GetCurrency(IAWOthInc.SPDirector) + GetCurrency(IAWOthInc.SPIntangDrill) + GetCurrency(IAWOthInc.SPExecutor) + GetCurrency(IAWOthInc.SPFirstHmBuy) + GetCurrency(IAWOthInc.SPK1) + GetCurrency(IAWOthInc.SPRefundCr) + GetCurrency(IAWOthInc.SPStRefund) + GetCurrency(IAWOthInc.SPDepl) + GetCurrency(IAWOthInc.SPJury) + GetCurrency(IAWOthInc.SPPerRent) + GetCurrency(IAWOthInc.SP8814) + GetCurrency(IAWOthInc.SPMSA) + GetCurrency(IAWOthInc.SPMedMSA) + GetCurrency(IAWOthInc.SPLTC) + GetCurrency(IAWOthInc.SPMisc) + GetCurrency(IAWOthInc.SPAlaska) + GetCurrency(IAWOthInc.SPCoverdell) + GetCurrency(IAWOthInc.SPCanceled) + GetCurrency(IAWOthInc.SPPshipCan) + GetCurrency(IAWOthInc.SPHSA) + GetCurrency(IAWOthInc.SPAltTrade) + GetCurrency(IAWOthInc.SPRecapTuit) + GetCurrency(IAWOthInc.SPRecapChar) + GetCurrency(IAWOthInc.SP5471) + GetCurrency(IAWOthInc.SPHobby) + GetCurrency(IAWOthInc.SP8621) + GetCurrency(IAWOthInc.SPDefDist) + GetCurrency(IAWOthInc.SPDisaster) + GetCurrency(IAWOthInc.SPFoster) + GetCurrency(IAWOthInc.SPCredAdj) + GetCurrency(IAWOthInc.SPPYNPTC) + GetCurrency(IAWOthInc.SP1099QA) + GetCurrency(IAWOthInc.SPIAABLE) + GetCurrency(IAWOthInc.SPBusPass) + GetCurrency(IAWOthInc.SPAirline) + GetCurrency(IAWOthInc.SP1099B) + GetCurrency(IAWOthInc.SPFarmLoss) + GetCurrency(IAWOthInc.SP8824) + GetCurrency(IAWOthInc.SPStudLoanDis) + GetCurrency(IAWOthInc.SP4684) + GetCurrency(IAWOthInc.SP3903) + GetCurrency(IAWOthInc.SPBusInt) + GetCurrency(IAWOthInc.SPEntExp) + GetCurrency(IAWOthInc.SP2106) + GetCurrency(IAWOthInc.SPOthNC)
End Sub

Private Sub SPTotNonConform_Calculation()
    ReturnVal = GetCurrency(IAWOthInc.SPFarmLoss) + GetCurrency(IAWOthInc.SP8824) + GetCurrency(IAWOthInc.SPStudLoanDis) + GetCurrency(IAWOthInc.SP4684) + GetCurrency(IAWOthInc.SP3903) + GetCurrency(IAWOthInc.SPBusInt) + GetCurrency(IAWOthInc.SPEntExp) + GetCurrency(IAWOthInc.SP2106) + GetCurrency(IAWOthInc.SPOthNC)
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

Private Sub TotBonus_Calculation()
    ReturnVal = GetCurrency(IA4562.TotDepAdj) + GetCurrency(IA4562Sp.TotDepAdj) + GetCurrency(IA4562A.TotDepAdj)
End Sub

Private Sub TotNonConform_Calculation()
    ReturnVal = GetCurrency(IAWOthInc.SPTotNonConform) + GetCurrency(IAWOthInc.TPTotNonConform)
End Sub

Private Sub TP1099B_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.TP1099B)
    Else
        ReturnVal = GetCurrency(USWOthIncNR.TP1099B)
    End If
End Sub

Private Sub TP1099QA_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.TP1099QA)
    Else
        ReturnVal = GetCurrency(USWOthIncNR.TP1099QA)
    End If
End Sub

Private Sub TP2106_Calculation()
    ReturnVal = GetCurrency(IA2106.IAWages, FieldCopies(IA2106.Taxpayer))
End Sub

Private Sub TP3903_Calculation()
    ReturnVal = GetCurrency(IARequired.TIAExReimb)
End Sub

Private Sub TP4684_Calculation()
    ReturnVal = GetCurrency(IA4684.IANonConformAdj) - GetCurrency(IAWOthInc.SP4684)
End Sub

Private Sub TP5471_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.TP5471)
    Else
        ReturnVal = GetCurrency(USWOthIncNR.TP5471)
    End If
End Sub

Private Sub TP8621_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.TP8621)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TP8814_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.TP8814)
    Else
        ReturnVal = GetCurrency(USWOthIncNR.TP8814)
    End If
End Sub

Private Sub TP8824_Calculation()
    ReturnVal = GetCurrency(IARequired.TP8824)
End Sub

Private Sub TPAirline_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.TPAirline)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPAlaska_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.TPAlaska)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPAltTrade_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.TPAltTrade)
    Else
        ReturnVal = GetCurrency(USWOthIncNR.TPAltTrade)
    End If
End Sub

Private Sub TPAmount_Calculation(Index As Integer)
    Dim count As Integer
    Dim Hold As Currency
    count = 0
    Hold = 0
    
    If GetCurrency(IAWOthInc.TPOth1) <> 0 Or GetCurrency(IAWOthInc.SPOth1) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPOth1)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPOth2) <> 0 Or GetCurrency(IAWOthInc.SPOth2) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPOth2)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPBabySit) <> 0 Or GetCurrency(IAWOthInc.SPBabySit) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPBabySit)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPBonus) <> 0 Or GetCurrency(IAWOthInc.SPBonus) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPBonus)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPIAEd) <> 0 Or GetCurrency(IAWOthInc.SPIAEd) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPIAEd)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPDirector) <> 0 Or GetCurrency(IAWOthInc.SPDirector) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPDirector)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPIntangDrill) <> 0 Or GetCurrency(IAWOthInc.SPIntangDrill) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPIntangDrill)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPExecutor) <> 0 Or GetCurrency(IAWOthInc.SPExecutor) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPExecutor)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPFirstHmBuy) <> 0 Or GetCurrency(IAWOthInc.SPFirstHmBuy) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPFirstHmBuy)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPK1) <> 0 Or GetCurrency(IAWOthInc.SPK1) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPK1)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPRefundCr) <> 0 Or GetCurrency(IAWOthInc.SPRefundCr) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPRefundCr)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPStRefund) <> 0 Or GetCurrency(IAWOthInc.SPStRefund) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPStRefund)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPDepl) <> 0 Or GetCurrency(IAWOthInc.SPDepl) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPDepl)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPJury) <> 0 Or GetCurrency(IAWOthInc.SPJury) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPJury)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPPerRent) <> 0 Or GetCurrency(IAWOthInc.SPPerRent) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPPerRent)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TP8814) <> 0 Or GetCurrency(IAWOthInc.SP8814) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TP8814)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPMSA) <> 0 Or GetCurrency(IAWOthInc.SPMSA) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPMSA)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPMedMSA) <> 0 Or GetCurrency(IAWOthInc.SPMedMSA) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPMedMSA)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPLTC) <> 0 Or GetCurrency(IAWOthInc.SPLTC) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPLTC)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPMisc) <> 0 Or GetCurrency(IAWOthInc.SPMisc) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPMisc)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPAlaska) <> 0 Or GetCurrency(IAWOthInc.SPAlaska) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPAlaska)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPCoverdell) <> 0 Or GetCurrency(IAWOthInc.SPCoverdell) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPCoverdell)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPCanceled) <> 0 Or GetCurrency(IAWOthInc.SPCanceled) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPCanceled)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPPshipCan) <> 0 Or GetCurrency(IAWOthInc.SPPshipCan) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPPshipCan)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPHSA) <> 0 Or GetCurrency(IAWOthInc.SPHSA) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPHSA)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPAltTrade) <> 0 Or GetCurrency(IAWOthInc.SPAltTrade) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPAltTrade)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPRecapTuit) <> 0 Or GetCurrency(IAWOthInc.SPRecapTuit) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPRecapTuit)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPRecapChar) <> 0 Or GetCurrency(IAWOthInc.SPRecapChar) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPRecapChar)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TP5471) <> 0 Or GetCurrency(IAWOthInc.SP5471) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TP5471)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPHobby) <> 0 Or GetCurrency(IAWOthInc.SPHobby) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPHobby)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TP8621) <> 0 Or GetCurrency(IAWOthInc.SP8621) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TP8621)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPDefDist) <> 0 Or GetCurrency(IAWOthInc.SPDefDist) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPDefDist)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPDisaster) <> 0 Or GetCurrency(IAWOthInc.SPDisaster) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPDisaster)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPFoster) <> 0 Or GetCurrency(IAWOthInc.SPFoster) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPFoster)
           count = 99
        Else
            count = count + 1
        End If
    End If    
    
    If GetCurrency(IAWOthInc.TPCredAdj) <> 0 Or GetCurrency(IAWOthInc.SPCredAdj) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPCredAdj)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPPYNPTC) <> 0 Or GetCurrency(IAWOthInc.SPPYNPTC) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPPYNPTC)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TP1099QA) <> 0 Or GetCurrency(IAWOthInc.SP1099QA) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TP1099QA)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPAirline) <> 0 Or GetCurrency(IAWOthInc.SPAirline) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPAirline)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TP1099B) <> 0 Or GetCurrency(IAWOthInc.SP1099B) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TP1099B)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPIAABLE) <> 0 Or GetCurrency(IAWOthInc.SPIAABLE) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPIAABLE)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPBusPass) <> 0 Or GetCurrency(IAWOthInc.SPBusPass) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPBusPass)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPFarmLoss) <> 0 Or GetCurrency(IAWOthInc.SPFarmLoss) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPFarmLoss)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TP8824) <> 0 Or GetCurrency(IAWOthInc.SP8824) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TP8824)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPStudLoanDis) <> 0 Or GetCurrency(IAWOthInc.SPStudLoanDis) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPStudLoanDis)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TP4684) <> 0 Or GetCurrency(IAWOthInc.SP4684) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TP4684)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TP3903) <> 0 Or GetCurrency(IAWOthInc.SP3903) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TP3903)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPBusInt) <> 0 Or GetCurrency(IAWOthInc.SPBusInt) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPBusInt)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPEntExp) <> 0 Or GetCurrency(IAWOthInc.SPEntExp) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPEntExp)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TP2106) <> 0 Or GetCurrency(IAWOthInc.SP2106) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TP2106)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAWOthInc.TPOthNC) <> 0 Or GetCurrency(IAWOthInc.SPOthNC) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAWOthInc.TPOthNC)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    ReturnVal = Hold

End Sub

Private Sub TPBonus_Calculation()
    Dim JT As Currency
    
    JT = CDollar(CDbl(Round(GetCurrency(IAWDepr.TotAdj, FieldCopies(IAWDepr.Joint)))) * 0.5)

    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = JT + GetCurrency(IAWDepr.TotAdj, FieldCopies(IAWDepr.Taxpayer)) + GetCurrency(IA4562A.TotDepAdj, FieldCopies(IA4562A.Taxpayer)) + GetCurrency(IA4562PIV.TPTotAdj)
    Else
        ReturnVal = GetCurrency(IAWOthInc.TotBonus)
    End If
End Sub

Private Sub TPBonusTrigger_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IAWOthInc.TPBonus)
    Else
        ReturnVal = GetCurrency(IAWOthInc.TPBonus) + GetCurrency(IAWOthInc.SPBonus)
    End If
End Sub

Private Sub TPCanceled_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.TPCanceled)
    Else
        ReturnVal = GetCurrency(USWOthIncNR.TPCanceled)
    End If
End Sub

Private Sub TPCoverdell_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.TPCoverdell)
    Else
        ReturnVal = GetCurrency(USWOthIncNR.TPCoverdell)
    End If
End Sub

Private Sub TPCredAdj_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.TPCredAdj)
    Else
        ReturnVal = GetCurrency(USWOthIncNR.TPCredAdj)
    End If
End Sub

Private Sub TPDefDist_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.TPDefDist)
    Else
        ReturnVal = GetCurrency(USWOthIncNR.TPDefDist)
    End If
End Sub

Private Sub TPDepl_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(USF6251.Depl) - GetCurrency(IAWOthInc.SPDepl))
End Sub

Private Sub TPDisaster_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.TPDisaster)
    Else
        ReturnVal = GetCurrency(USWOthIncNR.TPDisaster)
    End If
End Sub

Private Sub TPFarmLoss_Calculation()
    ReturnVal = MaxValue(0, Abs(GetCurrency(IAWSchFLoss.ExcessLoss)) - GetCurrency(IAWOthInc.SPFarmLoss))
End Sub

Private Sub TPFoster_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.TPFoster)
    Else
        ReturnVal = GetCurrency(USWOthIncNR.TPFoster)
    End If
End Sub

Private Sub TPHobby_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.TPHobby)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPHSA_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.TPHSA)
    Else
        ReturnVal = GetCurrency(USWOthIncNR.TPHSA)
    End If
End Sub

Private Sub TPIntangDrill_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(USF6251.IntangDrill) - GetCurrency(IAWOthInc.SPIntangDrill))
End Sub

Private Sub TPJointAmount_Calculation(Index As Integer)
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetCurrency(IAWOthInc.TPAmount(Index))
    Else
        ReturnVal = GetCurrency(IAWOthInc.TPAmount(Index)) + GetCurrency(IAWOthInc.SPAmount(Index))
    End If
End Sub

Private Sub TPJury_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.TPJury)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPK1_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = MaxValue(0, GetCurrency(USWOthInc.TPK1))
    Else
        ReturnVal = MaxValue(0, GetCurrency(USWOthIncNR.TPK1))
    End If
End Sub

Private Sub TPLTC_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.TPLTC)
    Else
        ReturnVal = GetCurrency(USWOthIncNR.TPLTC)
    End If
End Sub

Private Sub TPMedMSA_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.TPMedMSA)
    Else
        ReturnVal = GetCurrency(USWOthIncNR.TPMedMSA)
    End If
End Sub

Private Sub TPMisc_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.TPMisc) + GetCurrency(USWOthInc.TPIndianGaming) + GetCurrency(USWOthInc.TPTribDist) + GetCurrency(USWOthInc.TPNativeDist)
    Else
        ReturnVal = GetCurrency(USWOthIncNR.TPMisc)
    End If
End Sub

Private Sub TPMSA_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.TP8853)
    Else
        ReturnVal = GetCurrency(USWOthIncNR.TP8853)
    End If
End Sub

Private Sub TPName_Calculation()
    ReturnVal = GetString(USWBasicInfo.TPCommon)
End Sub

Private Sub TPOth1_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.TPOth1)
    Else
        ReturnVal = GetCurrency(USWOthIncNR.TPOth1)
    End If
End Sub

Private Sub TPOth2_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.TPOth2)
    Else
        ReturnVal = GetCurrency(USWOthIncNR.TPOth2)
    End If
End Sub

Private Sub TPOthNC_Calculation()
    ReturnVal = GetCurrency(IAWNonConformAdj.TPTotNonConformAdj)
End Sub

Private Sub TPPerRent_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.TPPerRent)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPPshipCan_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.TPPshipCan)
    Else
        ReturnVal = GetCurrency(USWOthIncNR.TPPshipCan)
    End If
End Sub

Private Sub TPPYNPTC_Calculation()
    If GetBool(USWSpouse.NonRes) = True Then
        ReturnVal = MaxValue(0, GetCurrency(USWRec.PYNPTCNR) - GetCurrency(IAWOthInc.SPPYNPTC))
    Else
        ReturnVal = MaxValue(0, GetCurrency(USWRec.PYNPTC) - GetCurrency(IAWOthInc.SPPYNPTC))
    End If
End Sub

Private Sub TPRecapChar_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.TPRecapChContTax) + GetCurrency(USWOthInc.TPRecapChar)
    Else
        ReturnVal = GetCurrency(USWOthIncNR.TPRecapChContTax) + GetCurrency(USWOthIncNR.TPRecapChar)
    End If
End Sub

Private Sub TPRecapTuit_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthInc.TPRecapTuit)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPTot_Calculation()
    ReturnVal = GetCurrency(IAWOthInc.TPOth1) + GetCurrency(IAWOthInc.TPOth2) + GetCurrency(IAWOthInc.TPBabySit) + GetCurrency(IAWOthInc.TPBonus) + GetCurrency(IAWOthInc.TPIAEd) + GetCurrency(IAWOthInc.TPDirector) + GetCurrency(IAWOthInc.TPIntangDrill) + GetCurrency(IAWOthInc.TPExecutor) + GetCurrency(IAWOthInc.TPFirstHmBuy) + GetCurrency(IAWOthInc.TPK1) + GetCurrency(IAWOthInc.TPRefundCr) + GetCurrency(IAWOthInc.TPStRefund) + GetCurrency(IAWOthInc.TPDepl) + GetCurrency(IAWOthInc.TPJury) + GetCurrency(IAWOthInc.TPPerRent) + GetCurrency(IAWOthInc.TP8814) + GetCurrency(IAWOthInc.TPMSA) + GetCurrency(IAWOthInc.TPMedMSA) + GetCurrency(IAWOthInc.TPLTC) + GetCurrency(IAWOthInc.TPMisc) + GetCurrency(IAWOthInc.TPAlaska) + GetCurrency(IAWOthInc.TPCoverdell) + GetCurrency(IAWOthInc.TPCanceled) + GetCurrency(IAWOthInc.TPPshipCan) + GetCurrency(IAWOthInc.TPHSA) + GetCurrency(IAWOthInc.TPAltTrade) + GetCurrency(IAWOthInc.TPRecapTuit) + GetCurrency(IAWOthInc.TPRecapChar) + GetCurrency(IAWOthInc.TP5471) + GetCurrency(IAWOthInc.TPHobby) + GetCurrency(IAWOthInc.TP8621) + GetCurrency(IAWOthInc.TPDefDist) + GetCurrency(IAWOthInc.TPDisaster) + GetCurrency(IAWOthInc.TPFoster) + GetCurrency(IAWOthInc.TPCredAdj) + GetCurrency(IAWOthInc.TPPYNPTC) + GetCurrency(IAWOthInc.TP1099QA) + GetCurrency(IAWOthInc.TPIAABLE) + GetCurrency(IAWOthInc.TPBusPass) + GetCurrency(IAWOthInc.TPAirline) + GetCurrency(IAWOthInc.TP1099B) + GetCurrency(IAWOthInc.TPFarmLoss) + GetCurrency(IAWOthInc.TP8824) + GetCurrency(IAWOthInc.TPStudLoanDis) + GetCurrency(IAWOthInc.TP4684) + GetCurrency(IAWOthInc.TP3903) + GetCurrency(IAWOthInc.TPBusInt) + GetCurrency(IAWOthInc.TPEntExp) + GetCurrency(IAWOthInc.TP2106) + GetCurrency(IAWOthInc.TPOthNC)
End Sub

Private Sub TPTotNonConform_Calculation()
    ReturnVal = GetCurrency(IAWOthInc.TPFarmLoss) + GetCurrency(IAWOthInc.TP8824) + GetCurrency(IAWOthInc.TPStudLoanDis) + GetCurrency(IAWOthInc.TP4684) + GetCurrency(IAWOthInc.TP3903) + GetCurrency(IAWOthInc.TPBusInt) + GetCurrency(IAWOthInc.TPEntExp) + GetCurrency(IAWOthInc.TP2106) + GetCurrency(IAWOthInc.TPOthNC)
End Sub

Private Sub Txt1_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetString(USWOthInc.Txt1)
    Else
        ReturnVal = GetString(USWOthIncNR.Txt1)
    End If
End Sub

Private Sub Txt2_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetString(USWOthInc.Txt2)
    Else
        ReturnVal = GetString(USWOthIncNR.Txt2)
    End If
End Sub

