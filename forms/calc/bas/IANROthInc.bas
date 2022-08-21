Private Sub Code_Calculation(Index As Integer)
    Dim count As Integer
    Dim Hold As String
    count = 0
    Hold = ""
    
    If GetCurrency(IANROthInc.TPOth1) <> 0 Or GetCurrency(IANROthInc.SPOth1) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPOth2) <> 0 Or GetCurrency(IANROthInc.SPOth2) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPBabySit) <> 0 Or GetCurrency(IANROthInc.SPBabySit) <> 0 Then
        If Index = count Then
           Hold = "a"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPBonus) <> 0 Or GetCurrency(IANROthInc.SPBonus) <> 0 Then
        If Index = count Then
           Hold = "b"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPIAEd) <> 0 Or GetCurrency(IANROthInc.SPIAEd) <> 0 Then
        If Index = count Then
           Hold = "d"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPDirector) <> 0 Or GetCurrency(IANROthInc.SPDirector) <> 0 Then
        If Index = count Then
           Hold = "e"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPIntangDrill) <> 0 Or GetCurrency(IANROthInc.SPIntangDrill) <> 0 Then
        If Index = count Then
           Hold = "f"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPExecutor) <> 0 Or GetCurrency(IANROthInc.SPExecutor) <> 0 Then
        If Index = count Then
           Hold = "g"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPFirstHmBuy) <> 0 Or GetCurrency(IANROthInc.SPFirstHmBuy) <> 0 Then
        If Index = count Then
           Hold = "h"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPK1) <> 0 Or GetCurrency(IANROthInc.SPK1) <> 0 Then
        If Index = count Then
           Hold = "i"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPRefundCr) <> 0 Or GetCurrency(IANROthInc.SPRefundCr) <> 0 Then
        If Index = count Then
           Hold = "j"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPStRefund) <> 0 Or GetCurrency(IANROthInc.SPStRefund) <> 0 Then
        If Index = count Then
           Hold = "k"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPDepl) <> 0 Or GetCurrency(IANROthInc.SPDepl) <> 0 Then
        If Index = count Then
           Hold = "l"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPJury) <> 0 Or GetCurrency(IANROthInc.SPJury) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPPerRent) <> 0 Or GetCurrency(IANROthInc.SPPerRent) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TP8814) <> 0 Or GetCurrency(IANROthInc.SP8814) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPMSA) <> 0 Or GetCurrency(IANROthInc.SPMSA) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPMedMSA) <> 0 Or GetCurrency(IANROthInc.SPMedMSA) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPLTC) <> 0 Or GetCurrency(IANROthInc.SPLTC) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPMisc) <> 0 Or GetCurrency(IANROthInc.SPMisc) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPAlaska) <> 0 Or GetCurrency(IANROthInc.SPAlaska) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPCoverdell) <> 0 Or GetCurrency(IANROthInc.SPCoverdell) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPCanceled) <> 0 Or GetCurrency(IANROthInc.SPCanceled) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPPshipCan) <> 0 Or GetCurrency(IANROthInc.SPPshipCan) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPHSA) <> 0 Or GetCurrency(IANROthInc.SPHSA) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPAltTrade) <> 0 Or GetCurrency(IANROthInc.SPAltTrade) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPRecapTuit) <> 0 Or GetCurrency(IANROthInc.SPRecapTuit) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPRecapChar) <> 0 Or GetCurrency(IANROthInc.SPRecapChar) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If    
    
    If GetCurrency(IANROthInc.TP5471) <> 0 Or GetCurrency(IANROthInc.SP5471) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPHobby) <> 0 Or GetCurrency(IANROthInc.SPHobby) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TP8621) <> 0 Or GetCurrency(IANROthInc.SP8621) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPDefDist) <> 0 Or GetCurrency(IANROthInc.SPDefDist) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPDisaster) <> 0 Or GetCurrency(IANROthInc.SPDisaster) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPFoster) <> 0 Or GetCurrency(IANROthInc.SPFoster) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If    
    
    If GetCurrency(IANROthInc.TPCredAdj) <> 0 Or GetCurrency(IANROthInc.SPCredAdj) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
     End If
     
    If GetCurrency(IANROthInc.TPPYNPTC) <> 0 Or GetCurrency(IANROthInc.SPPYNPTC) <> 0 Then
        If Index = count Then
           Hold = "n"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TP1099QA) <> 0 Or GetCurrency(IANROthInc.SP1099QA) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPAirline) <> 0 Or GetCurrency(IANROthInc.SPAirline) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TP1099B) <> 0 Or GetCurrency(IANROthInc.SP1099B) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPIAABLE) <> 0 Or GetCurrency(IANROthInc.SPIAABLE) <> 0 Then
        If Index = count Then
           Hold = "o"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPBusPass) <> 0 Or GetCurrency(IANROthInc.SPBusPass) <> 0 Then
        If Index = count Then
           Hold = "p"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPFarmLoss) <> 0 Or GetCurrency(IANROthInc.SPFarmLoss) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TP8824) <> 0 Or GetCurrency(IANROthInc.SP8824) <> 0 Then
        If Index = count Then
           Hold = "q"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPStudLoanDis) <> 0 Or GetCurrency(IANROthInc.SPStudLoanDis) <> 0 Then
        If Index = count Then
           Hold = "r"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TP4684) <> 0 Or GetCurrency(IANROthInc.SP4684) <> 0 Then
        If Index = count Then
           Hold = "s"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TP3903) <> 0 Or GetCurrency(IANROthInc.SP3903) <> 0 Then
        If Index = count Then
           Hold = "t"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPBusInt) <> 0 Or GetCurrency(IANROthInc.SPBusInt) <> 0 Then
        If Index = count Then
           Hold = "u"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPEntExp) <> 0 Or GetCurrency(IANROthInc.SPEntExp) <> 0 Then
        If Index = count Then
           Hold = "v"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TP2106) <> 0 Or GetCurrency(IANROthInc.SP2106) <> 0 Then
        If Index = count Then
           Hold = "w"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPOthNC) <> 0 Or GetCurrency(IANROthInc.SPOthNC) <> 0 Then
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
    
    Total = GetCurrency(IANROthInc.TPTot) + GetCurrency(IANROthInc.SPTot)
    
    ReturnVal = CStr(Total)
End Sub

Private Sub Description_Calculation(Index As Integer)
    Dim count As Integer
    Dim Hold As String
    count = 0
    Hold = ""
    
    If GetCurrency(IANROthInc.TPOth1) <> 0 Or GetCurrency(IANROthInc.SPOth1) <> 0 Then
        If Index = count Then
           Hold = GetString(IANROthInc.Txt1)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPOth2) <> 0 Or GetCurrency(IANROthInc.SPOth2) <> 0 Then
        If Index = count Then
           Hold = GetString(IANROthInc.Txt2)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPBabySit) <> 0 Or GetCurrency(IANROthInc.SPBabySit) <> 0 Then
        If Index = count Then
           Hold = "Baby-sitting income not reported on federal Schedule C"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPBonus) <> 0 Or GetCurrency(IANROthInc.SPBonus) <> 0 Then
        If Index = count Then
           Hold = "Bonus depreciation/section 179 adjustment"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPIAEd) <> 0 Or GetCurrency(IANROthInc.SPIAEd) <> 0 Then
        If Index = count Then
           Hold = "College Savings Iowa or Iowa Advisor 529 Plan"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPDirector) <> 0 Or GetCurrency(IANROthInc.SPDirector) <> 0 Then
        If Index = count Then
           Hold = "Director's fees"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPIntangDrill) <> 0 Or GetCurrency(IANROthInc.SPIntangDrill) <> 0 Then
        If Index = count Then
           Hold = "Drilling"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPExecutor) <> 0 Or GetCurrency(IANROthInc.SPExecutor) <> 0 Then
        If Index = count Then
           Hold = "Executor's fees"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPFirstHmBuy) <> 0 Or GetCurrency(IANROthInc.SPFirstHmBuy) <> 0 Then
        If Index = count Then
           Hold = "First-time homebuyers account non-qualifying withdrawals"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPK1) <> 0 Or GetCurrency(IANROthInc.SPK1) <> 0 Then
        If Index = count Then
           Hold = "Partnership income and/or S Corporation income"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    
    If GetCurrency(IANROthInc.TPRefundCr) <> 0 Or GetCurrency(IANROthInc.SPRefundCr) <> 0 Then
        If Index = count Then
           Hold = "Refundable Iowa credits"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPStRefund) <> 0 Or GetCurrency(IANROthInc.SPStRefund) <> 0 Then
        If Index = count Then
           Hold = "State income tax refunds"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPDepl) <> 0 Or GetCurrency(IANROthInc.SPDepl) <> 0 Then
        If Index = count Then
           Hold = "Wells"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPJury) <> 0 Or GetCurrency(IANROthInc.SPJury) <> 0 Then
        If Index = count Then
           Hold = "Jury pay"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPPerRent) <> 0 Or GetCurrency(IANROthInc.SPPerRent) <> 0 Then
        If Index = count Then
           Hold = "Income from personal property"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TP8814) <> 0 Or GetCurrency(IANROthInc.SP8814) <> 0 Then
        If Index = count Then
           Hold = "Child's income amount, federal Form 8814"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPMSA) <> 0 Or GetCurrency(IANROthInc.SPMSA) <> 0 Then
        If Index = count Then
           Hold = "MSA distributions, federal Form 8853"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPMedMSA) <> 0 Or GetCurrency(IANROthInc.SPMedMSA) <> 0 Then
        If Index = count Then
           Hold = "Medicare Advantage distributions, federal Form 8853"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPLTC) <> 0 Or GetCurrency(IANROthInc.SPLTC) <> 0 Then
        If Index = count Then
           Hold = "Long-term care distribution, federal Form 8853"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPMisc) <> 0 Or GetCurrency(IANROthInc.SPMisc) <> 0 Then
        If Index = count Then
           Hold = "Form 1099-MISC, boxes 3 or 8"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPAlaska) <> 0 Or GetCurrency(IANROthInc.SPAlaska) <> 0 Then
        If Index = count Then
           Hold = "Alaska Permanent Fund dividends"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPCoverdell) <> 0 Or GetCurrency(IANROthInc.SPCoverdell) <> 0 Then
        If Index = count Then
           Hold = "Coverdell ESA Or Qualified Tuition Program"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPCanceled) <> 0 Or GetCurrency(IANROthInc.SPCanceled) <> 0 Then
        If Index = count Then
           Hold = "Cancellation of nonbusiness debt, federal Form 1099-C"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPPshipCan) <> 0 Or GetCurrency(IANROthInc.SPPshipCan) <> 0 Then
        If Index = count Then
           Hold = "Cancellation of business debt, Partnership Schedule K-1"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPHSA) <> 0 Or GetCurrency(IANROthInc.SPHSA) <> 0 Then
        If Index = count Then
           Hold = "HSA distributions, federal Form 8889"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPAltTrade) <> 0 Or GetCurrency(IANROthInc.SPAltTrade) <> 0 Then
        If Index = count Then
           Hold = "Alternative trade adjustment assistance payments"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPRecapTuit) <> 0 Or GetCurrency(IANROthInc.SPRecapTuit) <> 0 Then
        If Index = count Then
           Hold = "Recapture of prior year tuition and fees deduction"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPRecapChar) <> 0 Or GetCurrency(IANROthInc.SPRecapChar) <> 0 Then
        If Index = count Then
           Hold = "Recapture of charitable contribution deduction"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TP5471) <> 0 Or GetCurrency(IANROthInc.SP5471) <> 0 Then
        If Index = count Then
           Hold = "Income from a foreign corporation, federal Form 5471"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPHobby) <> 0 Or GetCurrency(IANROthInc.SPHobby) <> 0 Then
        If Index = count Then
           Hold = "Hobby income"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TP8621) <> 0 Or GetCurrency(IANROthInc.SP8621) <> 0 Then
        If Index = count Then
           Hold = "Income or loss from Section 1291, federal Form 8621"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPDefDist) <> 0 Or GetCurrency(IANROthInc.SPDefDist) <> 0 Then
        If Index = count Then
           Hold = "Loss on excess deferral distribution"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPDisaster) <> 0 Or GetCurrency(IANROthInc.SPDisaster) <> 0 Then
        If Index = count Then
           Hold = "Disaster relief payments"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPFoster) <> 0 Or GetCurrency(IANROthInc.SPFoster) <> 0 Then
        If Index = count Then
           Hold = "Medicaid waiver payments to care provider"
           count = 99
        Else
            count = count + 1
        End If
    End If    
    
    If GetCurrency(IANROthInc.TPCredAdj) <> 0 Or GetCurrency(IANROthInc.SPCredAdj) <> 0 Then
        If Index = count Then
           Hold = "Credit adjustment income, federal Forms 6478 and 8864"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPPYNPTC) <> 0 Or GetCurrency(IANROthInc.SPPYNPTC) <> 0 Then
        If Index = count Then
           Hold = "Net Premium Tax Credit"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TP1099QA) <> 0 Or GetCurrency(IANROthInc.SP1099QA) <> 0 Then
        If Index = count Then
           Hold = "Distributions from ABLE account"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPAirline) <> 0 Or GetCurrency(IANROthInc.SPAirline) <> 0 Then
        If Index = count Then
           Hold = "Qualified airline payments"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TP1099B) <> 0 Or GetCurrency(IANROthInc.SP1099B) <> 0 Then
        If Index = count Then
           Hold = "Foreign currency transaction"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPIAABLE) <> 0 Or GetCurrency(IANROthInc.SPIAABLE) <> 0 Then
        If Index = count Then
           Hold = "Distributions from an Iowa ABLE account"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPBusPass) <> 0 Or GetCurrency(IANROthInc.SPBusPass) <> 0 Then
        If Index = count Then
           Hold = "Employer provided bus pass or transportation expenses"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPFarmLoss) <> 0 Or GetCurrency(IANROthInc.SPFarmLoss) <> 0 Then
        If Index = count Then
           Hold = "Section 461(j) excess farm loss limitation adjustments"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TP8824) <> 0 Or GetCurrency(IANROthInc.SP8824) <> 0 Then
        If Index = count Then
           Hold = "IA 8824 worksheet, due to nonconformity"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPStudLoanDis) <> 0 Or GetCurrency(IANROthInc.SPStudLoanDis) <> 0 Then
        If Index = count Then
           Hold = "Discharge of student loan debt - death or disability"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TP4684) <> 0 Or GetCurrency(IANROthInc.SP4684) <> 0 Then
        If Index = count Then
           Hold = "IA 4684 worksheet, due to nonconformity"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TP3903) <> 0 Or GetCurrency(IANROthInc.SP3903) <> 0 Then
        If Index = count Then
           Hold = "IA 3903 worksheet line 8a, due to nonconformity"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPBusInt) <> 0 Or GetCurrency(IANROthInc.SPBusInt) <> 0 Then
        If Index = count Then
           Hold = "Business interest expense limitation, due to nonconformity"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPEntExp) <> 0 Or GetCurrency(IANROthInc.SPEntExp) <> 0 Then
        If Index = count Then
           Hold = "Entertainment expenses, due to nonconformity"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TP2106) <> 0 Or GetCurrency(IANROthInc.SP2106) <> 0 Then
        If Index = count Then
           Hold = "IA 2106 worksheet line 8, due to nonconformity"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPOthNC) <> 0 Or GetCurrency(IANROthInc.SPOthNC) <> 0 Then
        If Index = count Then
           Hold = "Other nonconformity adjustments"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    ReturnVal = Hold
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.CombNames)
End Sub

Private Sub Print_Calculation()
    If GetCurrency(IANROthInc.TPTot) <> 0 Or GetCurrency(IANROthInc.SPTot) <> 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SP1099B_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SP1099B)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SP1099QA_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SP1099QA)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SP2106_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SP2106)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SP3903_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SP3903)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SP4684_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SP4684)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SP5471_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SP5471)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SP8621_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SP8621)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SP8814_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SP8814)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SP8824_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SP8824)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPAirline_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPAirline)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPAlaska_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPAlaska)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPAltTrade_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPAltTrade)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPAmount_Calculation(Index As Integer)
    Dim count As Integer
    Dim Hold As Currency
    count = 0
    Hold = 0
    
    If GetCurrency(IANROthInc.TPOth1) <> 0 Or GetCurrency(IANROthInc.SPOth1) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPOth1)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPOth2) <> 0 Or GetCurrency(IANROthInc.SPOth2) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPOth2)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPBabySit) <> 0 Or GetCurrency(IANROthInc.SPBabySit) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPBabySit)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPBonus) <> 0 Or GetCurrency(IANROthInc.SPBonus) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPBonus)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPIAEd) <> 0 Or GetCurrency(IANROthInc.SPIAEd) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPIAEd)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPDirector) <> 0 Or GetCurrency(IANROthInc.SPDirector) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPDirector)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPIntangDrill) <> 0 Or GetCurrency(IANROthInc.SPIntangDrill) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPIntangDrill)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPExecutor) <> 0 Or GetCurrency(IANROthInc.SPExecutor) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPExecutor)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPFirstHmBuy) <> 0 Or GetCurrency(IANROthInc.SPFirstHmBuy) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPFirstHmBuy)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPK1) <> 0 Or GetCurrency(IANROthInc.SPK1) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPK1)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPRefundCr) <> 0 Or GetCurrency(IANROthInc.SPRefundCr) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPRefundCr)
           count = 99
        Else
            count = count + 1
        End If
    End If

    If GetCurrency(IANROthInc.TPStRefund) <> 0 Or GetCurrency(IANROthInc.SPStRefund) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPStRefund)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPDepl) <> 0 Or GetCurrency(IANROthInc.SPDepl) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPDepl)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPJury) <> 0 Or GetCurrency(IANROthInc.SPJury) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPJury)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPPerRent) <> 0 Or GetCurrency(IANROthInc.SPPerRent) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPPerRent)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TP8814) <> 0 Or GetCurrency(IANROthInc.SP8814) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SP8814)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPMSA) <> 0 Or GetCurrency(IANROthInc.SPMSA) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPMSA)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPMedMSA) <> 0 Or GetCurrency(IANROthInc.SPMedMSA) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPMedMSA)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPLTC) <> 0 Or GetCurrency(IANROthInc.SPLTC) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPLTC)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPMisc) <> 0 Or GetCurrency(IANROthInc.SPMisc) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPMisc)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPAlaska) <> 0 Or GetCurrency(IANROthInc.SPAlaska) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPAlaska)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPCoverdell) <> 0 Or GetCurrency(IANROthInc.SPCoverdell) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPCoverdell)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPCanceled) <> 0 Or GetCurrency(IANROthInc.SPCanceled) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPCanceled)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPPshipCan) <> 0 Or GetCurrency(IANROthInc.SPPshipCan) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPPshipCan)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPHSA) <> 0 Or GetCurrency(IANROthInc.SPHSA) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPHSA)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPAltTrade) <> 0 Or GetCurrency(IANROthInc.SPAltTrade) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPAltTrade)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPRecapTuit) <> 0 Or GetCurrency(IANROthInc.SPRecapTuit) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPRecapTuit)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPRecapChar) <> 0 Or GetCurrency(IANROthInc.SPRecapChar) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPRecapChar)
           count = 99
        Else
            count = count + 1
        End If
    End If

    If GetCurrency(IANROthInc.TP5471) <> 0 Or GetCurrency(IANROthInc.SP5471) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SP5471)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPHobby) <> 0 Or GetCurrency(IANROthInc.SPHobby) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPHobby)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TP8621) <> 0 Or GetCurrency(IANROthInc.SP8621) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SP8621)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPDefDist) <> 0 Or GetCurrency(IANROthInc.SPDefDist) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPDefDist)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPDisaster) <> 0 Or GetCurrency(IANROthInc.SPDisaster) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPDisaster)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPFoster) <> 0 Or GetCurrency(IANROthInc.SPFoster) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPFoster)
           count = 99
        Else
            count = count + 1
        End If
    End If    
    
    If GetCurrency(IANROthInc.TPCredAdj) <> 0 Or GetCurrency(IANROthInc.SPCredAdj) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPCredAdj)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPPYNPTC) <> 0 Or GetCurrency(IANROthInc.SPPYNPTC) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPPYNPTC)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TP1099QA) <> 0 Or GetCurrency(IANROthInc.SP1099QA) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SP1099QA)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPAirline) <> 0 Or GetCurrency(IANROthInc.SPAirline) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPAirline)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TP1099B) <> 0 Or GetCurrency(IANROthInc.SP1099B) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SP1099B)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPIAABLE) <> 0 Or GetCurrency(IANROthInc.SPIAABLE) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPIAABLE)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPBusPass) <> 0 Or GetCurrency(IANROthInc.SPBusPass) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPBusPass)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPFarmLoss) <> 0 Or GetCurrency(IANROthInc.SPFarmLoss) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPFarmLoss)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TP8824) <> 0 Or GetCurrency(IANROthInc.SP8824) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SP8824)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPStudLoanDis) <> 0 Or GetCurrency(IANROthInc.SPStudLoanDis) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPStudLoanDis)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TP4684) <> 0 Or GetCurrency(IANROthInc.SP4684) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SP4684)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TP3903) <> 0 Or GetCurrency(IANROthInc.SP3903) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SP3903)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPBusInt) <> 0 Or GetCurrency(IANROthInc.SPBusInt) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPBusInt)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPEntExp) <> 0 Or GetCurrency(IANROthInc.SPEntExp) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPEntExp)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TP2106) <> 0 Or GetCurrency(IANROthInc.SP2106) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SP2106)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPOthNC) <> 0 Or GetCurrency(IANROthInc.SPOthNC) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.SPOthNC)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    ReturnVal = Hold
End Sub

Private Sub SPBabySit_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPBabySit)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPBonus_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPBonus)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPBusInt_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPBusInt)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPBusPass_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPBusPass)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPCanceled_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPCanceled)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPCoverdell_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPCoverdell)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPCredAdj_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPCredAdj)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPDefDist_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPDefDist)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPDepl_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPDepl)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPDirector_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPDirector)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPDisaster_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPDisaster)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPEntExp_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPEntExp)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPExecutor_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPExecutor)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPFarmLoss_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPFarmLoss)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPFirstHmBuy_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPFirstHmBuy)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPFoster_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPFoster)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPHobby_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPHobby)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPHSA_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPHSA)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPIAABLE_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPIAABLE)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPIAEd_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPIAEd)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPIntangDrill_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPIntangDrill)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPJury_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPJury)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPK1_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPK1)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPLTC_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPLTC)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPMedMSA_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPMedMSA)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPMisc_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPMisc)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPMSA_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPMSA)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPName_Calculation()
    ReturnVal = GetString(USWBasicInfo.SPCommon)
End Sub

Private Sub SPOth1_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPOth1)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPOth2_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPOth2)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPOthNC_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPOthNC)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPPerRent_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPPerRent)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPPshipCan_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPPshipCan)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPPYNPTC_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPPYNPTC)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPRecapChar_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPRecapChar)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPRecapTuit_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPRecapTuit)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPRefundCr_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPRefundCr)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPStRefund_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPStRefund)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPStudLoanDis_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPStudLoanDis)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPTot_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = GetCurrency(IANROthInc.SPOth1) + GetCurrency(IANROthInc.SPOth2) + GetCurrency(IANROthInc.SPBabySit) + GetCurrency(IANROthInc.SPBonus) + GetCurrency(IANROthInc.SPIAEd) + GetCurrency(IANROthInc.SPDirector) + GetCurrency(IANROthInc.SPIntangDrill) + GetCurrency(IANROthInc.SPExecutor) + GetCurrency(IANROthInc.SPFirstHmBuy) + GetCurrency(IANROthInc.SPK1) + GetCurrency(IANROthInc.SPRefundCr) + GetCurrency(IANROthInc.SPStRefund) + GetCurrency(IANROthInc.SPDepl) + GetCurrency(IANROthInc.SPJury) + GetCurrency(IANROthInc.SPPerRent) + GetCurrency(IANROthInc.SP8814) + GetCurrency(IANROthInc.SPMSA) + GetCurrency(IANROthInc.SPMedMSA) + GetCurrency(IANROthInc.SPLTC) + GetCurrency(IANROthInc.SPMisc) + GetCurrency(IANROthInc.SPAlaska) + GetCurrency(IANROthInc.SPCoverdell) + GetCurrency(IANROthInc.SPCanceled) + GetCurrency(IANROthInc.SPPshipCan) + GetCurrency(IANROthInc.SPHSA) + GetCurrency(IANROthInc.SPAltTrade) + GetCurrency(IANROthInc.SPRecapTuit) + GetCurrency(IANROthInc.SPRecapChar) + GetCurrency(IANROthInc.SP5471) + GetCurrency(IANROthInc.SPHobby) + GetCurrency(IANROthInc.SP8621) + GetCurrency(IANROthInc.SPDefDist) + GetCurrency(IANROthInc.SPDisaster) + GetCurrency(IANROthInc.SPFoster) + GetCurrency(IANROthInc.SPCredAdj) + GetCurrency(IANROthInc.SPPYNPTC) + GetCurrency(IANROthInc.SP1099QA) + GetCurrency(IANROthInc.SPIAABLE) + GetCurrency(IANROthInc.SPBusPass) + GetCurrency(IANROthInc.SPAirline) + GetCurrency(IANROthInc.SP1099B) + GetCurrency(IANROthInc.SPFarmLoss) + GetCurrency(IANROthInc.SP8824) + GetCurrency(IANROthInc.SPStudLoanDis) + GetCurrency(IANROthInc.SP4684) + GetCurrency(IANROthInc.SP3903) + GetCurrency(IANROthInc.SPBusInt) + GetCurrency(IANROthInc.SPEntExp) + GetCurrency(IANROthInc.SP2106) + GetCurrency(IANROthInc.SPOthNC)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

Private Sub TP1099B_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TP1099B)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TP1099QA_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TP1099QA)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TP2106_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TP2106)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TP3903_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TP3903)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TP4684_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TP4684)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TP5471_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TP5471)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TP8621_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TP8621)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TP8814_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TP8814)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TP8824_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TP8824)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPAirline_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPAirline)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPAlaska_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPAlaska)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPAltTrade_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPAltTrade)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPAmount_Calculation(Index As Integer)
    Dim count As Integer
    Dim Hold As Currency
    count = 0
    Hold = 0
    
    If GetCurrency(IANROthInc.TPOth1) <> 0 Or GetCurrency(IANROthInc.SPOth1) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPOth1)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPOth2) <> 0 Or GetCurrency(IANROthInc.SPOth2) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPOth2)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPBabySit) <> 0 Or GetCurrency(IANROthInc.SPBabySit) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPBabySit)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPBonus) <> 0 Or GetCurrency(IANROthInc.SPBonus) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPBonus)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPIAEd) <> 0 Or GetCurrency(IANROthInc.SPIAEd) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPIAEd)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPDirector) <> 0 Or GetCurrency(IANROthInc.SPDirector) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPDirector)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPIntangDrill) <> 0 Or GetCurrency(IANROthInc.SPIntangDrill) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPIntangDrill)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPExecutor) <> 0 Or GetCurrency(IANROthInc.SPExecutor) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPExecutor)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPFirstHmBuy) <> 0 Or GetCurrency(IANROthInc.SPFirstHmBuy) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPFirstHmBuy)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPK1) <> 0 Or GetCurrency(IANROthInc.SPK1) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPK1)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPRefundCr) <> 0 Or GetCurrency(IANROthInc.SPRefundCr) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPRefundCr)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPStRefund) <> 0 Or GetCurrency(IANROthInc.SPStRefund) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPStRefund)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPDepl) <> 0 Or GetCurrency(IANROthInc.SPDepl) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPDepl)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPJury) <> 0 Or GetCurrency(IANROthInc.SPJury) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPJury)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPPerRent) <> 0 Or GetCurrency(IANROthInc.SPPerRent) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPPerRent)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TP8814) <> 0 Or GetCurrency(IANROthInc.SP8814) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TP8814)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPMSA) <> 0 Or GetCurrency(IANROthInc.SPMSA) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPMSA)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPMedMSA) <> 0 Or GetCurrency(IANROthInc.SPMedMSA) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPMedMSA)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPLTC) <> 0 Or GetCurrency(IANROthInc.SPLTC) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPLTC)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPMisc) <> 0 Or GetCurrency(IANROthInc.SPMisc) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPMisc)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPAlaska) <> 0 Or GetCurrency(IANROthInc.SPAlaska) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPAlaska)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPCoverdell) <> 0 Or GetCurrency(IANROthInc.SPCoverdell) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPCoverdell)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPCanceled) <> 0 Or GetCurrency(IANROthInc.SPCanceled) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPCanceled)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPPshipCan) <> 0 Or GetCurrency(IANROthInc.SPPshipCan) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPPshipCan)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPHSA) <> 0 Or GetCurrency(IANROthInc.SPHSA) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPHSA)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPAltTrade) <> 0 Or GetCurrency(IANROthInc.SPAltTrade) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPAltTrade)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPRecapTuit) <> 0 Or GetCurrency(IANROthInc.SPRecapTuit) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPRecapTuit)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPRecapChar) <> 0 Or GetCurrency(IANROthInc.SPRecapChar) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPRecapChar)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TP5471) <> 0 Or GetCurrency(IANROthInc.SP5471) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TP5471)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPHobby) <> 0 Or GetCurrency(IANROthInc.SPHobby) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPHobby)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TP8621) <> 0 Or GetCurrency(IANROthInc.SP8621) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TP8621)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPDefDist) <> 0 Or GetCurrency(IANROthInc.SPDefDist) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPDefDist)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPDisaster) <> 0 Or GetCurrency(IANROthInc.SPDisaster) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPDisaster)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPFoster) <> 0 Or GetCurrency(IANROthInc.SPFoster) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPFoster)
           count = 99
        Else
            count = count + 1
        End If
    End If    
    
    If GetCurrency(IANROthInc.TPCredAdj) <> 0 Or GetCurrency(IANROthInc.SPCredAdj) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPCredAdj)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPPYNPTC) <> 0 Or GetCurrency(IANROthInc.SPPYNPTC) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPPYNPTC)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TP1099QA) <> 0 Or GetCurrency(IANROthInc.SP1099QA) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TP1099QA)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPAirline) <> 0 Or GetCurrency(IANROthInc.SPAirline) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPAirline)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TP1099B) <> 0 Or GetCurrency(IANROthInc.SP1099B) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TP1099B)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPIAABLE) <> 0 Or GetCurrency(IANROthInc.SPIAABLE) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPIAABLE)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPBusPass) <> 0 Or GetCurrency(IANROthInc.SPBusPass) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPBusPass)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPFarmLoss) <> 0 Or GetCurrency(IANROthInc.SPFarmLoss) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPFarmLoss)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TP8824) <> 0 Or GetCurrency(IANROthInc.SP8824) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TP8824)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPStudLoanDis) <> 0 Or GetCurrency(IANROthInc.SPStudLoanDis) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPStudLoanDis)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TP4684) <> 0 Or GetCurrency(IANROthInc.SP4684) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TP4684)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TP3903) <> 0 Or GetCurrency(IANROthInc.SP3903) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TP3903)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPBusInt) <> 0 Or GetCurrency(IANROthInc.SPBusInt) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPBusInt)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPEntExp) <> 0 Or GetCurrency(IANROthInc.SPEntExp) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPEntExp)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TP2106) <> 0 Or GetCurrency(IANROthInc.SP2106) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TP2106)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthInc.TPOthNC) <> 0 Or GetCurrency(IANROthInc.SPOthNC) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthInc.TPOthNC)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    ReturnVal = Hold
End Sub

Private Sub TPBabySit_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPBabySit)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPBonus_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPBonus)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPBusInt_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPBusInt)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPBusPass_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPBusPass)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPCanceled_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPCanceled)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPCoverdell_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPCoverdell)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPCredAdj_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPCredAdj)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPDefDist_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPDefDist)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPDepl_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPDepl)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPDirector_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPDirector)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPDisaster_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPDisaster)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPEntExp_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPEntExp)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPExecutor_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPExecutor)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPFarmLoss_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPFarmLoss)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPFirstHmBuy_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPFirstHmBuy)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPFoster_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPFoster)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPHobby_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPHobby)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPHSA_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPHSA)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPIAABLE_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPIAABLE)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPIAEd_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPIAEd)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPIntangDrill_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPIntangDrill)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPJointAmount_Calculation(Index As Integer)
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetCurrency(IANROthInc.TPAmount(Index))
    Else
        ReturnVal = GetCurrency(IANROthInc.TPAmount(Index)) + GetCurrency(IANROthInc.SPAmount(Index))
    End If
End Sub

Private Sub TPJury_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPJury)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPK1_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPK1)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPLTC_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPLTC)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPMedMSA_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPMedMSA)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPMisc_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPMisc)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPMSA_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPMSA)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPName_Calculation()
    ReturnVal = GetString(USWBasicInfo.TPCommon)
End Sub

Private Sub TPOth1_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPOth1)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPOth2_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPOth2)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPOthNC_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPOthNC)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPPerRent_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPPerRent)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPPshipCan_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPPshipCan)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPPYNPTC_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPPYNPTC)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPRecapChar_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPRecapChar)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPRecapTuit_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPRecapTuit)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPRefundCr_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPRefundCr)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPStRefund_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPStRefund)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPStudLoanDis_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAWOthInc.TPStudLoanDis)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPTot_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IANROthInc.TPOth1) + GetCurrency(IANROthInc.TPOth2) + GetCurrency(IANROthInc.TPBabySit) + GetCurrency(IANROthInc.TPBonus) + GetCurrency(IANROthInc.TPIAEd) + GetCurrency(IANROthInc.TPDirector) + GetCurrency(IANROthInc.TPIntangDrill) + GetCurrency(IANROthInc.TPExecutor) + GetCurrency(IANROthInc.TPFirstHmBuy) + GetCurrency(IANROthInc.TPK1) + GetCurrency(IANROthInc.TPRefundCr) + GetCurrency(IANROthInc.TPStRefund) + GetCurrency(IANROthInc.TPDepl) + GetCurrency(IANROthInc.TPJury) + GetCurrency(IANROthInc.TPPerRent) + GetCurrency(IANROthInc.TP8814) + GetCurrency(IANROthInc.TPMSA) + GetCurrency(IANROthInc.TPMedMSA) + GetCurrency(IANROthInc.TPLTC) + GetCurrency(IANROthInc.TPMisc) + GetCurrency(IANROthInc.TPAlaska) + GetCurrency(IANROthInc.TPCoverdell) + GetCurrency(IANROthInc.TPCanceled) + GetCurrency(IANROthInc.TPPshipCan) + GetCurrency(IANROthInc.TPHSA) + GetCurrency(IANROthInc.TPAltTrade) + GetCurrency(IANROthInc.TPRecapTuit) + GetCurrency(IANROthInc.TPRecapChar) + GetCurrency(IANROthInc.TP5471) + GetCurrency(IANROthInc.TPHobby) + GetCurrency(IANROthInc.TP8621) + GetCurrency(IANROthInc.TPDefDist) + GetCurrency(IANROthInc.TPDisaster) + GetCurrency(IANROthInc.TPFoster) + GetCurrency(IANROthInc.TPCredAdj) + GetCurrency(IANROthInc.TPPYNPTC) + GetCurrency(IANROthInc.TP1099QA) + GetCurrency(IANROthInc.TPIAABLE) + GetCurrency(IANROthInc.TPBusPass) + GetCurrency(IANROthInc.TPAirline) + GetCurrency(IANROthInc.TP1099B) + GetCurrency(IANROthInc.TPFarmLoss) + GetCurrency(IANROthInc.TP8824) + GetCurrency(IANROthInc.TPStudLoanDis) + GetCurrency(IANROthInc.TP4684) + GetCurrency(IANROthInc.TP3903) + GetCurrency(IANROthInc.TPBusInt) + GetCurrency(IANROthInc.TPEntExp) + GetCurrency(IANROthInc.TP2106) + GetCurrency(IANROthInc.TPOthNC)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Txt1_Calculation()
    ReturnVal = GetString(IAWOthInc.Txt1)
End Sub

Private Sub Txt2_Calculation()
    ReturnVal = GetString(IAWOthInc.Txt2)
End Sub

