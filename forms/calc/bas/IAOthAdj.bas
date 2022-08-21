Private Sub ANet_Calculation()
    Dim ATotAdj As Currency
    
    ATotAdj = GetCurrency(IAF1040.AKeogh) + GetCurrency(IAF1040.ABusIncL) + GetCurrency(IAF1040.AHealth) + GetCurrency(IAF1040.APenalty) + GetCurrency(IAF1040.AAlimonyP) + GetCurrency(IAF1040.APenExcl) + GetCurrency(IAF1040.AMove) + GetCurrency(IAF1040.AGainDed) + GetCurrency(IAOthAdj.ModTPTot)
    
    ReturnVal = GetCurrency(IAF1040.AGross) - ATotAdj
End Sub

Private Sub BNet_Calculation()
    Dim BTotAdj As Currency
    
    BTotAdj = GetCurrency(IAF1040.BKeogh) + GetCurrency(IAF1040.BBusIncL) + GetCurrency(IAF1040.BHealth) + GetCurrency(IAF1040.BPenalty) + GetCurrency(IAF1040.BAlimonyP) + GetCurrency(IAF1040.BPenExcl) + GetCurrency(IAF1040.BMove) + GetCurrency(IAF1040.BGainDed) + GetCurrency(IAOthAdj.ModSPTot)
    
    ReturnVal = GetCurrency(IAF1040.BGross) - BTotAdj
End Sub

Private Sub BProRate_Calculation()
    If IAFS() = 3 Then
        If GetCurrency(IAOthAdj.BNet) < 0 And GetCurrency(IAOthAdj.ANet) < 0 Then
            If GetCurrency(IAOthAdj.BNet) < GetCurrency(IAOthAdj.ANet) Then
                ReturnVal = 0
            Else
                ReturnVal = 1
            End If
        ElseIf GetCurrency(IAOthAdj.BNet) < 0 Then
            ReturnVal = 0
        ElseIf GetCurrency(IAOthAdj.BNet) > 0 And GetCurrency(IAOthAdj.TotNI) <= 0 Then
            ReturnVal = 1
        ElseIf GetCurrency(IAOthAdj.TotNI) = 0 Then
            ReturnVal = 0
        Else
            ReturnVal = MaxValue(0, (MinValue(1#, GetFloat(IAOthAdj.BNet) / GetFloat(IAOthAdj.TotNI))))
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Code_Calculation(Index As Integer)
    Dim count As Integer
    Dim Hold As String
    count = 0
    Hold = ""
    
    If GetCurrency(IAOthAdj.TOth1) <> 0 Or GetCurrency(IAOthAdj.SOth1) <> 0 Then
        If Index = count Then
           Hold = "dd"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPActiveMil) <> 0 Or GetCurrency(IAOthAdj.SPActiveMil) <> 0 Then
        If Index = count Then
           Hold = "b"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPAltMV) <> 0 Or GetCurrency(IAOthAdj.SPAltMV) <> 0 Then
        If Index = count Then
           Hold = "c"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPInvolConv) <> 0 Or GetCurrency(IAOthAdj.SPInvolConv) <> 0 Then
        If Index = count Then
           Hold = "e"
           count = 99
        Else
            count = count + 1
        End If
    End If

    If GetCurrency(IAOthAdj.TPClaimOfRight) <> 0 Or GetCurrency(IAOthAdj.SPClaimOfRight) <> 0 Then
        If Index = count Then
           Hold = "f"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPIAEd) <> 0 Or GetCurrency(IAOthAdj.SPIAEd) <> 0 Then
        If Index = count Then
           Hold = "g"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPIADis) <> 0 Or GetCurrency(IAOthAdj.SPIADis) <> 0 Then
        If Index = count Then
           Hold = "h"
           count = 99
        Else
            count = count + 1
        End If
    End If

    If GetCurrency(IAOthAdj.TPDomProd) <> 0 Or GetCurrency(IAOthAdj.SPDomProd) <> 0 Then
        If Index = count Then
           Hold = "i"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPFirstHmBuy) <> 0 Or GetCurrency(IAOthAdj.SPFirstHmBuy) <> 0 Then
        If Index = count Then
           Hold = "j"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPEmployerSS) <> 0 Or GetCurrency(IAOthAdj.SPEmployerSS) <> 0 Then
        If Index = count Then
           Hold = "k"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPFedFuels) <> 0 Or GetCurrency(IAOthAdj.SPFedFuels) <> 0 Then
        If Index = count Then
           Hold = "l"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPForeign) <> 0 Or GetCurrency(IAOthAdj.SPForeign) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TP2555) <> 0 Or GetCurrency(IAOthAdj.SP2555) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPDistressed) <> 0 Or GetCurrency(IAOthAdj.SPDistressed) <> 0 Then
        If Index = count Then
           Hold = "n"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPHealthSav) <> 0 Or GetCurrency(IAOthAdj.SPHealthSav) <> 0 Then
        If Index = count Then
           Hold = "o"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPVet) <> 0 Or GetCurrency(IAOthAdj.SPVet) <> 0 Then
        If Index = count Then
           Hold = "p"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
     If GetCurrency(IAOthAdj.TPVetGrant) <> 0 Or GetCurrency(IAOthAdj.SPVetGrant) <> 0 Then
        If Index = count Then
           Hold = "q"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPHomeHealth) <> 0 Or GetCurrency(IAOthAdj.SPHomeHealth) <> 0 Then
        If Index = count Then
           Hold = "r"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPIAVetTrust) <> 0 Or GetCurrency(IAOthAdj.SPIAVetTrust) <> 0 Then
        If Index = count Then
           Hold = "s"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPMilitaryExem) <> 0 Or GetCurrency(IAOthAdj.SPMilitaryExem) <> 0 Then
        If Index = count Then
           Hold = "t"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TIANOL) <> 0 Or GetCurrency(IAOthAdj.SIANOL) <> 0 Then
        If Index = count Then
           Hold = "u"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPOrgan) <> 0 Or GetCurrency(IAOthAdj.SPOrgan) <> 0 Then
        If Index = count Then
           Hold = "v"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPK1) <> 0 Or GetCurrency(IAOthAdj.SPK1) <> 0 Then
        If Index = count Then
           Hold = "w"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPSegal) <> 0 Or GetCurrency(IAOthAdj.SPSegal) <> 0 Then
        If Index = count Then
           Hold = "x"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPShell) <> 0 Or GetCurrency(IAOthAdj.SPShell) <> 0 Then
        If Index = count Then
           Hold = "y"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TStud) <> 0 Or GetCurrency(IAOthAdj.SStud) <> 0 Then
        If Index = count Then
           Hold = "z"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPVictim) <> 0 Or GetCurrency(IAOthAdj.SPVictim) <> 0 Then
        If Index = count Then
           Hold = "aa"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPWages) <> 0 Or GetCurrency(IAOthAdj.SPWages) <> 0 Then
        If Index = count Then
           Hold = "bb"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPWorkCr) <> 0 Or GetCurrency(IAOthAdj.SPWorkCr) <> 0 Then
        If Index = count Then
           Hold = "cc"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TP2106) <> 0 Or GetCurrency(IAOthAdj.SP2106) <> 0 Then
        If Index = count Then
           Hold = "dd"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TMSA) <> 0 Or GetCurrency(IAOthAdj.SMSA) <> 0 Then
        If Index = count Then
           Hold = "dd"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPJury) <> 0 Or GetCurrency(IAOthAdj.SPJury) <> 0 Then
        If Index = count Then
           Hold = "dd"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPRFST) <> 0 Or GetCurrency(IAOthAdj.SPRFST) <> 0 Then
        If Index = count Then
           Hold = "dd"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPSub) <> 0 Or GetCurrency(IAOthAdj.SPSub) <> 0 Then
        If Index = count Then
           Hold = "dd"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TP501c) <> 0 Or GetCurrency(IAOthAdj.SP501c) <> 0 Then
        If Index = count Then
           Hold = "dd"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPPerRent) <> 0 Or GetCurrency(IAOthAdj.SPPerRent) <> 0 Then
        If Index = count Then
           Hold = "dd"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TP403b) <> 0 Or GetCurrency(IAOthAdj.SP403b) <> 0 Then
        If Index = count Then
           Hold = "dd"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPUDC) <> 0 Or GetCurrency(IAOthAdj.SPUDC) <> 0 Then
        If Index = count Then
           Hold = "dd"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPWBF) <> 0 Or GetCurrency(IAOthAdj.SPWBF) <> 0 Then
        If Index = count Then
           Hold = "dd"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TP8873) <> 0 Or GetCurrency(IAOthAdj.SP8873) <> 0 Then
        If Index = count Then
           Hold = "dd"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPOlympic) <> 0 Or GetCurrency(IAOthAdj.SPOlympic) <> 0 Then
        If Index = count Then
           Hold = "dd"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPEducator) <> 0 Or GetCurrency(IAOthAdj.SPEducator) <> 0 Then
        If Index = count Then
           Hold = "ee"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPTuition) <> 0 Or GetCurrency(IAOthAdj.SPTuition) <> 0 Then
        If Index = count Then
           Hold = "ff"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPElectric) <> 0 Or GetCurrency(IAOthAdj.SPElectric) <> 0 Then
        If Index = count Then
           Hold = "gg"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPRapid) <> 0 Or GetCurrency(IAOthAdj.SPRapid) <> 0 Then
        If Index = count Then
           Hold = "hh"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPIAABLE) <> 0 Or GetCurrency(IAOthAdj.SPIAABLE) <> 0 Then
        If Index = count Then
           Hold = "ii"
           count = 99
        Else
            count = count + 1
        End If
    End If
       
    ReturnVal = Hold
    
End Sub

Private Sub Desc_Calculation()
    Dim Total As Currency
    
    Total = GetCurrency(IAOthAdj.TPTot) + GetCurrency(IAOthAdj.SPTot)
    
    ReturnVal = CStr(Total)
End Sub

Private Sub Description_Calculation(Index As Integer)
    Dim count As Integer
    Dim Hold As String
    count = 0
    Hold = ""
    
    If GetCurrency(IAOthAdj.TOth1) <> 0 Or GetCurrency(IAOthAdj.SOth1) <> 0 Then
        If Index = count Then
           Hold = GetString(IAOthAdj.TxtOth1)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPActiveMil) <> 0 Or GetCurrency(IAOthAdj.SPActiveMil) <> 0 Then
        If Index = count Then
           Hold = "Active duty military pay"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPAltMV) <> 0 Or GetCurrency(IAOthAdj.SPAltMV) <> 0 Then
        If Index = count Then
           Hold = "Alternative motor vehicle deduction"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPInvolConv) <> 0 Or GetCurrency(IAOthAdj.SPInvolConv) <> 0 Then
        If Index = count Then
           Hold = "Capital or ordinary gain from involuntary conversion"
           count = 99
        Else
            count = count + 1
        End If
    End If

    If GetCurrency(IAOthAdj.TPClaimOfRight) <> 0 Or GetCurrency(IAOthAdj.SPClaimOfRight) <> 0 Then
        If Index = count Then
           Hold = "Claim of Right deduction"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPIAEd) <> 0 Or GetCurrency(IAOthAdj.SPIAEd) <> 0 Then
        If Index = count Then
           Hold = "College Savings Iowa or Iowa Advisor 529 Plan"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPIADis) <> 0 Or GetCurrency(IAOthAdj.SPIADis) <> 0 Then
        If Index = count Then
           Hold = "Disability income exclusion"
           count = 99
        Else
            count = count + 1
        End If
    End If

    If GetCurrency(IAOthAdj.TPDomProd) <> 0 Or GetCurrency(IAOthAdj.SPDomProd) <> 0 Then
        If Index = count Then
           Hold = "Domestic production activities deduction"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPFirstHmBuy) <> 0 Or GetCurrency(IAOthAdj.SPFirstHmBuy) <> 0 Then
        If Index = count Then
           Hold = "First-Time Homebuyer Savings Account qualifying contributions"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPEmployerSS) <> 0 Or GetCurrency(IAOthAdj.SPEmployerSS) <> 0 Then
        If Index = count Then
           Hold = "Employer social security credit, federal Form 8846"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPFedFuels) <> 0 Or GetCurrency(IAOthAdj.SPFedFuels) <> 0 Then
        If Index = count Then
           Hold = "Alcohol and cellulosic biofuel credit, federal Form 6478"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPForeign) <> 0 Or GetCurrency(IAOthAdj.SPForeign) <> 0 Then
        If Index = count Then
           Hold = "Foreign earned income exclusion, federal Form 2555"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TP2555) <> 0 Or GetCurrency(IAOthAdj.SP2555) <> 0 Then
        If Index = count Then
           Hold = "Foreign housing deduction, federal Form 2555"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPDistressed) <> 0 Or GetCurrency(IAOthAdj.SPDistressed) <> 0 Then
        If Index = count Then
           Hold = "Gains or losses from distressed sale transactions"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPHealthSav) <> 0 Or GetCurrency(IAOthAdj.SPHealthSav) <> 0 Then
        If Index = count Then
           Hold = "Health savings account deduction, federal Form 8889"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPVet) <> 0 Or GetCurrency(IAOthAdj.SPVet) <> 0 Then
        If Index = count Then
           Hold = "Injured veterans programs - contributions"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
     If GetCurrency(IAOthAdj.TPVetGrant) <> 0 Or GetCurrency(IAOthAdj.SPVetGrant) <> 0 Then
        If Index = count Then
           Hold = "Injured veterans programs - grants"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPHomeHealth) <> 0 Or GetCurrency(IAOthAdj.SPHomeHealth) <> 0 Then
        If Index = count Then
           Hold = "In-home health care"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPIAVetTrust) <> 0 Or GetCurrency(IAOthAdj.SPIAVetTrust) <> 0 Then
        If Index = count Then
           Hold = "Iowa Veterans Trust Fund"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPMilitaryExem) <> 0 Or GetCurrency(IAOthAdj.SPMilitaryExem) <> 0 Then
        If Index = count Then
           Hold = "Military exemptions"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TIANOL) <> 0 Or GetCurrency(IAOthAdj.SIANOL) <> 0 Then
        If Index = count Then
           Hold = "Iowa Net Operating Loss"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPOrgan) <> 0 Or GetCurrency(IAOthAdj.SPOrgan) <> 0 Then
        If Index = count Then
           Hold = "Organ transplant expenses"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPK1) <> 0 Or GetCurrency(IAOthAdj.SPK1) <> 0 Then
        If Index = count Then
           Hold = "Partnership income and/or S Corporation income"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPSegal) <> 0 Or GetCurrency(IAOthAdj.SPSegal) <> 0 Then
        If Index = count Then
           Hold = "Segal Americorps Education Award payments"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPShell) <> 0 Or GetCurrency(IAOthAdj.SPShell) <> 0 Then
        If Index = count Then
           Hold = "Speculative shell buildings"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TStud) <> 0 Or GetCurrency(IAOthAdj.SStud) <> 0 Then
        If Index = count Then
           Hold = "Student loan interest deduction"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPVictim) <> 0 Or GetCurrency(IAOthAdj.SPVictim) <> 0 Then
        If Index = count Then
           Hold = "Victim compensation awards"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPWages) <> 0 Or GetCurrency(IAOthAdj.SPWages) <> 0 Then
        If Index = count Then
           Hold = "Wages paid to certain individuals"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPWorkCr) <> 0 Or GetCurrency(IAOthAdj.SPWorkCr) <> 0 Then
        If Index = count Then
           Hold = "Work opportunity credit, federal Form 5884"
           count = 99
        Else
            count = count + 1
        End If
    End If    
    
    If GetCurrency(IAOthAdj.TP2106) <> 0 Or GetCurrency(IAOthAdj.SP2106) <> 0 Then
        If Index = count Then
           Hold = "Business expenses of reservists, QPA, FBO, federal Form 2106"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TMSA) <> 0 Or GetCurrency(IAOthAdj.SMSA) <> 0 Then
        If Index = count Then
           Hold = "Archer MSA deduction, federal Form 8853"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPJury) <> 0 Or GetCurrency(IAOthAdj.SPJury) <> 0 Then
        If Index = count Then
           Hold = "Jury pay repayment to employer"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPRFST) <> 0 Or GetCurrency(IAOthAdj.SPRFST) <> 0 Then
        If Index = count Then
           Hold = "Reforestation amortization and expenses"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPSub) <> 0 Or GetCurrency(IAOthAdj.SPSub) <> 0 Then
        If Index = count Then
           Hold = "Repayment of supplemental unemployment benefits"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TP501c) <> 0 Or GetCurrency(IAOthAdj.SP501c) <> 0 Then
        If Index = count Then
           Hold = "Contributions to a 501(c)(18) pension plan"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPPerRent) <> 0 Or GetCurrency(IAOthAdj.SPPerRent) <> 0 Then
        If Index = count Then
           Hold = "Expenses for personal property rental"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TP403b) <> 0 Or GetCurrency(IAOthAdj.SP403b) <> 0 Then
        If Index = count Then
           Hold = "Contributions by certain chaplains to a 403(b) plan"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPUDC) <> 0 Or GetCurrency(IAOthAdj.SPUDC) <> 0 Then
        If Index = count Then
           Hold = "Qualified attorney/court fees paid after 10/22/2004"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPWBF) <> 0 Or GetCurrency(IAOthAdj.SPWBF) <> 0 Then
        If Index = count Then
           Hold = "Qualified whistleblower fees"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TP8873) <> 0 Or GetCurrency(IAOthAdj.SP8873) <> 0 Then
        If Index = count Then
           Hold = "Extraterritorial Income Exclusion, federal Form 8873"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPOlympic) <> 0 Or GetCurrency(IAOthAdj.SPOlympic) <> 0 Then
        If Index = count Then
           Hold = "Nontaxable amount of Olympic and Paralympic medals and USOC prize money"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPEducator) <> 0 Or GetCurrency(IAOthAdj.SPEducator) <> 0 Then
        If Index = count Then
           Hold = "Educator expenses"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPTuition) <> 0 Or GetCurrency(IAOthAdj.SPTuition) <> 0 Then
        If Index = count Then
           Hold = "Tuition and fees deduction"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPElectric) <> 0 Or GetCurrency(IAOthAdj.SPElectric) <> 0 Then
        If Index = count Then
           Hold = "Nonresident Electric Utility Reciprocity"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPRapid) <> 0 Or GetCurrency(IAOthAdj.SPRapid) <> 0 Then
        If Index = count Then
           Hold = "Rapid Response to State Disasters"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPIAABLE) <> 0 Or GetCurrency(IAOthAdj.SPIAABLE) <> 0 Then
        If Index = count Then
           Hold = "Iowa ABLE savings plan trust"
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

Private Sub ModSPTot_Calculation()
    ReturnVal = GetCurrency(IAOthAdj.SOth1) + GetCurrency(IAOthAdj.SPActiveMil) + GetCurrency(IAOthAdj.SPInvolConv) + GetCurrency(IAOthAdj.SPClaimOfRight) + GetCurrency(IAOthAdj.SPIAEd) + GetCurrency(IAOthAdj.SPIADis) + GetCurrency(IAOthAdj.SPDomProd) + GetCurrency(IAOthAdj.SPFirstHmBuy) + GetCurrency(IAOthAdj.SPEmployerSS) + GetCurrency(IAOthAdj.SPFedFuels) + GetCurrency(IAOthAdj.SPForeign) + GetCurrency(IAOthAdj.SP2555) + GetCurrency(IAOthAdj.SPDistressed) + GetCurrency(IAOthAdj.SPHealthSav) + GetCurrency(IAOthAdj.SPVet) + GetCurrency(IAOthAdj.SPVetGrant) + GetCurrency(IAOthAdj.SPHomeHealth) + GetCurrency(IAOthAdj.SPIAVetTrust) + GetCurrency(IAOthAdj.SPMilitaryExem) + GetCurrency(IAOthAdj.SIANOL) + GetCurrency(IAOthAdj.SPOrgan) + GetCurrency(IAOthAdj.SPK1) + GetCurrency(IAOthAdj.SPSegal) + GetCurrency(IAOthAdj.SPShell) + GetCurrency(IAOthAdj.SStud) + GetCurrency(IAOthAdj.SPVictim) + GetCurrency(IAOthAdj.SPWages) + GetCurrency(IAOthAdj.SPWorkCr) + GetCurrency(IAOthAdj.SP2106) + GetCurrency(IAOthAdj.SMSA) + GetCurrency(IAOthAdj.SPJury) + GetCurrency(IAOthAdj.SPRFST) + GetCurrency(IAOthAdj.SPSub) + GetCurrency(IAOthAdj.SP501c) + GetCurrency(IAOthAdj.SPPerRent) + GetCurrency(IAOthAdj.SP403b) + GetCurrency(IAOthAdj.SPUDC) + GetCurrency(IAOthAdj.SPWBF) + GetCurrency(IAOthAdj.SP8873) + GetCurrency(IAOthAdj.SPOlympic) + GetCurrency(IAOthAdj.SPEducator) + GetCurrency(IAOthAdj.SPTuition) + GetCurrency(IAOthAdj.SPElectric) + GetCurrency(IAOthAdj.SPRapid) + GetCurrency(IAOthAdj.SPIAABLE)
End Sub

Private Sub ModTPTot_Calculation()
    ReturnVal = GetCurrency(IAOthAdj.TOth1) + GetCurrency(IAOthAdj.TPActiveMil) + GetCurrency(IAOthAdj.TPInvolConv) + GetCurrency(IAOthAdj.TPClaimOfRight) + GetCurrency(IAOthAdj.TPIAEd) + GetCurrency(IAOthAdj.TPIADis) + GetCurrency(IAOthAdj.TPDomProd) + GetCurrency(IAOthAdj.TPFirstHmBuy) + GetCurrency(IAOthAdj.TPEmployerSS) + GetCurrency(IAOthAdj.TPFedFuels) + GetCurrency(IAOthAdj.TPForeign) + GetCurrency(IAOthAdj.TP2555) + GetCurrency(IAOthAdj.TPDistressed) + GetCurrency(IAOthAdj.TPHealthSav) + GetCurrency(IAOthAdj.TPVet) + GetCurrency(IAOthAdj.TPVetGrant) + GetCurrency(IAOthAdj.TPHomeHealth) + GetCurrency(IAOthAdj.TPIAVetTrust) + GetCurrency(IAOthAdj.TPMilitaryExem) + GetCurrency(IAOthAdj.TIANOL) + GetCurrency(IAOthAdj.TPOrgan) + GetCurrency(IAOthAdj.TPK1) + GetCurrency(IAOthAdj.TPSegal) + GetCurrency(IAOthAdj.TPShell) + GetCurrency(IAOthAdj.TStud) + GetCurrency(IAOthAdj.TPVictim) + GetCurrency(IAOthAdj.TPWages) + GetCurrency(IAOthAdj.TPWorkCr) + GetCurrency(IAOthAdj.TP2106) + GetCurrency(IAOthAdj.TMSA) + GetCurrency(IAOthAdj.TPJury) + GetCurrency(IAOthAdj.TPRFST) + GetCurrency(IAOthAdj.TPSub) + GetCurrency(IAOthAdj.TP501c) + GetCurrency(IAOthAdj.TPPerRent) + GetCurrency(IAOthAdj.TP403b) + GetCurrency(IAOthAdj.TPUDC) + GetCurrency(IAOthAdj.TPWBF) + GetCurrency(IAOthAdj.TP8873) + GetCurrency(IAOthAdj.TPOlympic) + GetCurrency(IAOthAdj.TPEducator) + GetCurrency(IAOthAdj.TPTuition) + GetCurrency(IAOthAdj.TPElectric) + GetCurrency(IAOthAdj.TPRapid) + GetCurrency(IAOthAdj.TPIAABLE)
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.CombNames)
End Sub

Private Sub PrintMe_Calculation()
    If GetCurrency(IAOthAdj.TPTot) <> 0 Or GetCurrency(IAOthAdj.SPTot) <> 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SIANOL_Calculation()
    If GetBool(IAF126.SpNonRes) = True Then
        ReturnVal = 0
    ElseIf GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = Abs(GetCurrency(USWOthInc.SPNOL))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SMSA_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthAdj.SP8853)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SP2106_Calculation()
    ReturnVal = GetCurrency(USWRec.SBusExp2106)
End Sub

Private Sub SP2555_Calculation()
    ReturnVal = GetCurrency(USWOthAdj.SP2555)
End Sub

Private Sub SP403b_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthAdj.SP403b)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SP501c_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthAdj.SPTotal501)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SP8873_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthAdj.SP8873)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPAltMV_Calculation()
'2018 expanded instructions - deduction does not apply to purchases on or after 1/1/2015 due to nonconformity, federal does not ask for a purchase date, believe will be very uncommon for ability to take this credit on Iowa, remove math and make user entered
    'If IAFS() = 3 And GetBool(USF8910.Print) = True Then
    '    ReturnVal = CDollar(GetFloat(IAOthAdj.BProRate) * 2000@)
    'Else
        ReturnVal = 0
    'End If
End Sub

Private Sub SPAmount_Calculation(Index As Integer)
    Dim count As Integer
    Dim Hold As Currency
    count = 0
    Hold = 0
    
    If GetCurrency(IAOthAdj.TOth1) <> 0 Or GetCurrency(IAOthAdj.SOth1) <> 0 Then
        If Index = count Then
        Hold = GetCurrency(IAOthAdj.SOth1)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPActiveMil) <> 0 Or GetCurrency(IAOthAdj.SPActiveMil) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPActiveMil)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPAltMV) <> 0 Or GetCurrency(IAOthAdj.SPAltMV) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPAltMV)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPInvolConv) <> 0 Or GetCurrency(IAOthAdj.SPInvolConv) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPInvolConv)
           count = 99
        Else
            count = count + 1
        End If
    End If

    If GetCurrency(IAOthAdj.TPClaimOfRight) <> 0 Or GetCurrency(IAOthAdj.SPClaimOfRight) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPClaimOfRight)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPIAEd) <> 0 Or GetCurrency(IAOthAdj.SPIAEd) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPIAEd)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPIADis) <> 0 Or GetCurrency(IAOthAdj.SPIADis) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPIADis)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPDomProd) <> 0 Or GetCurrency(IAOthAdj.SPDomProd) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPDomProd)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPFirstHmBuy) <> 0 Or GetCurrency(IAOthAdj.SPFirstHmBuy) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPFirstHmBuy)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPEmployerSS) <> 0 Or GetCurrency(IAOthAdj.SPEmployerSS) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPEmployerSS)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPFedFuels) <> 0 Or GetCurrency(IAOthAdj.SPFedFuels) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPFedFuels)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPForeign) <> 0 Or GetCurrency(IAOthAdj.SPForeign) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPForeign)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TP2555) <> 0 Or GetCurrency(IAOthAdj.SP2555) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SP2555)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPDistressed) <> 0 Or GetCurrency(IAOthAdj.SPDistressed) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPDistressed)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPHealthSav) <> 0 Or GetCurrency(IAOthAdj.SPHealthSav) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPHealthSav)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPVet) <> 0 Or GetCurrency(IAOthAdj.SPVet) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPVet)
           count = 99
        Else
            count = count + 1
        End If
    End If

    If GetCurrency(IAOthAdj.TPVetGrant) <> 0 Or GetCurrency(IAOthAdj.SPVetGrant) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPVetGrant)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPHomeHealth) <> 0 Or GetCurrency(IAOthAdj.SPHomeHealth) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPHomeHealth)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPIAVetTrust) <> 0 Or GetCurrency(IAOthAdj.SPIAVetTrust) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPIAVetTrust)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPMilitaryExem) <> 0 Or GetCurrency(IAOthAdj.SPMilitaryExem) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPMilitaryExem)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TIANOL) <> 0 Or GetCurrency(IAOthAdj.SIANOL) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SIANOL)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPOrgan) <> 0 Or GetCurrency(IAOthAdj.SPOrgan) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPOrgan)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPK1) <> 0 Or GetCurrency(IAOthAdj.SPK1) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPK1)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPSegal) <> 0 Or GetCurrency(IAOthAdj.SPSegal) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPSegal)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPShell) <> 0 Or GetCurrency(IAOthAdj.SPShell) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPShell)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TStud) <> 0 Or GetCurrency(IAOthAdj.SStud) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SStud)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPVictim) <> 0 Or GetCurrency(IAOthAdj.SPVictim) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPVictim)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPWages) <> 0 Or GetCurrency(IAOthAdj.SPWages) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPWages)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPWorkCr) <> 0 Or GetCurrency(IAOthAdj.SPWorkCr) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPWorkCr)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TP2106) <> 0 Or GetCurrency(IAOthAdj.SP2106) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SP2106)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TMSA) <> 0 Or GetCurrency(IAOthAdj.SMSA) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SMSA)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPJury) <> 0 Or GetCurrency(IAOthAdj.SPJury) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPJury)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPRFST) <> 0 Or GetCurrency(IAOthAdj.SPRFST) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPRFST)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPSub) <> 0 Or GetCurrency(IAOthAdj.SPSub) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPSub)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TP501c) <> 0 Or GetCurrency(IAOthAdj.SP501c) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SP501c)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPPerRent) <> 0 Or GetCurrency(IAOthAdj.SPPerRent) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPPerRent)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TP403b) <> 0 Or GetCurrency(IAOthAdj.SP403b) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SP403b)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPUDC) <> 0 Or GetCurrency(IAOthAdj.SPUDC) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPUDC)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPWBF) <> 0 Or GetCurrency(IAOthAdj.SPWBF) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPWBF)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TP8873) <> 0 Or GetCurrency(IAOthAdj.SP8873) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SP8873)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPOlympic) <> 0 Or GetCurrency(IAOthAdj.SPOlympic) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPOlympic)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPEducator) <> 0 Or GetCurrency(IAOthAdj.SPEducator) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPEducator)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPTuition) <> 0 Or GetCurrency(IAOthAdj.SPTuition) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPTuition)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPElectric) <> 0 Or GetCurrency(IAOthAdj.SPElectric) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPElectric)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPRapid) <> 0 Or GetCurrency(IAOthAdj.SPRapid) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPRapid)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPIAABLE) <> 0 Or GetCurrency(IAOthAdj.SPIAABLE) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.SPIAABLE)
           count = 99
        Else
            count = count + 1
        End If
    End If
       
    ReturnVal = Hold
End Sub

Private Sub SPDomProd_Calculation()
'Iowa expanded instructions - Iowa has not conformed to the repeal of the federal domestic production activities deduction. For Iowa will need to complete a federal 8903 and keep with their records and follow IA instructions for adjustments needed when calcing.
    'ReturnVal = GetCurrency(USWRec.SDomProd)
    ReturnVal = 0
End Sub

Private Sub SPEducator_Calculation()
    ReturnVal = GetCurrency(USWRec.SEdExp)
End Sub

Private Sub SPForeign_Calculation()
    ReturnVal = Abs(GetCurrency(USWOthInc.SP2555))
End Sub

Private Sub SPHealthSav_Calculation()
    ReturnVal = GetCurrency(USWRec.SHealthSav)
End Sub

Private Sub SPJury_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthAdj.SPJury)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPK1_Calculation()
    If GetBool(USWResidency.F1040NR) = False And GetCurrency(USWOthInc.SPK1) < 0 Then
        ReturnVal = Abs(GetCurrency(USWOthInc.SPK1))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPName_Calculation()
    ReturnVal = GetString(USWBasicInfo.SPCommon)
End Sub

Private Sub SPOlympic_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthAdj.Text2)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPPerRent_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthAdj.SPPerRent)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPRFST_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthAdj.SPRFST)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPSub_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthAdj.SPSub)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPTot_Calculation()
    ReturnVal = GetCurrency(IAOthAdj.SOth1) + GetCurrency(IAOthAdj.SPActiveMil) + GetCurrency(IAOthAdj.SPAltMV) + GetCurrency(IAOthAdj.SPInvolConv) + GetCurrency(IAOthAdj.SPClaimOfRight) + GetCurrency(IAOthAdj.SPIAEd) + GetCurrency(IAOthAdj.SPIADis) + GetCurrency(IAOthAdj.SPDomProd) + GetCurrency(IAOthAdj.SPFirstHmBuy) + GetCurrency(IAOthAdj.SPEmployerSS) + GetCurrency(IAOthAdj.SPFedFuels) + GetCurrency(IAOthAdj.SPForeign) + GetCurrency(IAOthAdj.SP2555) + GetCurrency(IAOthAdj.SPDistressed) + GetCurrency(IAOthAdj.SPHealthSav) + GetCurrency(IAOthAdj.SPVet) + GetCurrency(IAOthAdj.SPVetGrant) + GetCurrency(IAOthAdj.SPHomeHealth) + GetCurrency(IAOthAdj.SPIAVetTrust) + GetCurrency(IAOthAdj.SPMilitaryExem) + GetCurrency(IAOthAdj.SIANOL) + GetCurrency(IAOthAdj.SPOrgan) + GetCurrency(IAOthAdj.SPK1) + GetCurrency(IAOthAdj.SPSegal) + GetCurrency(IAOthAdj.SPShell) + GetCurrency(IAOthAdj.SStud) + GetCurrency(IAOthAdj.SPVictim) + GetCurrency(IAOthAdj.SPWages) + GetCurrency(IAOthAdj.SPWorkCr) + GetCurrency(IAOthAdj.SP2106) + GetCurrency(IAOthAdj.SMSA) + GetCurrency(IAOthAdj.SPJury) + GetCurrency(IAOthAdj.SPRFST) + GetCurrency(IAOthAdj.SPSub) + GetCurrency(IAOthAdj.SP501c) + GetCurrency(IAOthAdj.SPPerRent) + GetCurrency(IAOthAdj.SP403b) + GetCurrency(IAOthAdj.SPUDC) + GetCurrency(IAOthAdj.SPWBF) + GetCurrency(IAOthAdj.SP8873) + GetCurrency(IAOthAdj.SPEducator) + GetCurrency(IAOthAdj.SPTuition) + GetCurrency(IAOthAdj.SPElectric) + GetCurrency(IAOthAdj.SPRapid) + GetCurrency(IAOthAdj.SPOlympic) + GetCurrency(IAOthAdj.SPIAABLE)
End Sub

Private Sub SPTuition_Calculation()
    ReturnVal = 0
    'ReturnVal = GetCurrency(USWRec.STuitAdj)
End Sub

Private Sub SPUDC_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthAdj.SPUDC)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPWBF_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthAdj.SPWBF)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

Private Sub SStud_Calculation()
    ReturnVal = GetCurrency(USWRec.SStudAdj)
End Sub

Private Sub TIANOL_Calculation()
    If GetBool(IAF126.TpNonRes) = True Then
        ReturnVal = 0
    ElseIf GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = Abs(GetCurrency(USWOthInc.TPNOL))
    Else
        ReturnVal = Abs(GetCurrency(USWOthIncNR.TPNOL))
    End If
End Sub

Private Sub TMSA_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthAdj.TP8853)
    Else
        ReturnVal = GetCurrency(USWOthAdjNR.TP8853)
    End If
End Sub

Private Sub TotNI_Calculation()
    ReturnVal = GetCurrency(IAOthAdj.ANet) + GetCurrency(IAOthAdj.BNet)
End Sub

Private Sub TP2106_Calculation()
    ReturnVal = GetCurrency(USWRec.TBusExp2106)
End Sub

Private Sub TP2555_Calculation()
    ReturnVal = GetCurrency(USWOthAdj.TP2555)
End Sub

Private Sub TP403b_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthAdj.TP403b)
    Else
        ReturnVal = GetCurrency(USWOthAdjNR.TP403b)
    End If
End Sub

Private Sub TP501c_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthAdj.TPTotal501)
    Else
        ReturnVal = GetCurrency(USWOthAdjNR.Total501)
    End If
End Sub

Private Sub TP8873_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthAdj.TP8873)
    Else
        ReturnVal = GetCurrency(USWOthAdjNR.TP8873)
    End If
End Sub

Private Sub TPAltMV_Calculation()
'2018 expanded instructions - deduction does not apply to purchases on or after 1/1/2015 due to nonconformity, federal does not ask for a purchase date, believe will be very uncommon for ability to take this credit on Iowa, remove math and make user entered
    'If GetBool(USF8910.Print) = False Then
        ReturnVal = 0
    'ElseIf IAFS() = 3 Then
    '    ReturnVal = MaxValue(0, 2000@ - GetCurrency(IAOthAdj.SPAltMV))
    'Else
    '    ReturnVal = 2000@
    'End If
End Sub

Private Sub TPAmount_Calculation(Index As Integer)
    Dim count As Integer
    Dim Hold As Currency
    count = 0
    Hold = 0
    
    If GetCurrency(IAOthAdj.TOth1) <> 0 Or GetCurrency(IAOthAdj.SOth1) <> 0 Then
        If Index = count Then
        Hold = GetCurrency(IAOthAdj.TOth1)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPActiveMil) <> 0 Or GetCurrency(IAOthAdj.SPActiveMil) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPActiveMil)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPAltMV) <> 0 Or GetCurrency(IAOthAdj.SPAltMV) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPAltMV)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPInvolConv) <> 0 Or GetCurrency(IAOthAdj.SPInvolConv) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPInvolConv)
           count = 99
        Else
            count = count + 1
        End If
    End If

    If GetCurrency(IAOthAdj.TPClaimOfRight) <> 0 Or GetCurrency(IAOthAdj.SPClaimOfRight) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPClaimOfRight)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPIAEd) <> 0 Or GetCurrency(IAOthAdj.SPIAEd) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPIAEd)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPIADis) <> 0 Or GetCurrency(IAOthAdj.SPIADis) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPIADis)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPDomProd) <> 0 Or GetCurrency(IAOthAdj.SPDomProd) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPDomProd)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPFirstHmBuy) <> 0 Or GetCurrency(IAOthAdj.SPFirstHmBuy) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPFirstHmBuy)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPEmployerSS) <> 0 Or GetCurrency(IAOthAdj.SPEmployerSS) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPEmployerSS)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPFedFuels) <> 0 Or GetCurrency(IAOthAdj.SPFedFuels) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPFedFuels)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPForeign) <> 0 Or GetCurrency(IAOthAdj.SPForeign) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPForeign)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TP2555) <> 0 Or GetCurrency(IAOthAdj.SP2555) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TP2555)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPDistressed) <> 0 Or GetCurrency(IAOthAdj.SPDistressed) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPDistressed)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPHealthSav) <> 0 Or GetCurrency(IAOthAdj.SPHealthSav) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPHealthSav)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPVet) <> 0 Or GetCurrency(IAOthAdj.SPVet) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPVet)
           count = 99
        Else
            count = count + 1
        End If
    End If

    If GetCurrency(IAOthAdj.TPVetGrant) <> 0 Or GetCurrency(IAOthAdj.SPVetGrant) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPVetGrant)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPHomeHealth) <> 0 Or GetCurrency(IAOthAdj.SPHomeHealth) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPHomeHealth)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPIAVetTrust) <> 0 Or GetCurrency(IAOthAdj.SPIAVetTrust) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPIAVetTrust)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPMilitaryExem) <> 0 Or GetCurrency(IAOthAdj.SPMilitaryExem) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPMilitaryExem)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TIANOL) <> 0 Or GetCurrency(IAOthAdj.SIANOL) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TIANOL)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPOrgan) <> 0 Or GetCurrency(IAOthAdj.SPOrgan) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPOrgan)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPK1) <> 0 Or GetCurrency(IAOthAdj.SPK1) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPK1)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPSegal) <> 0 Or GetCurrency(IAOthAdj.SPSegal) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPSegal)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPShell) <> 0 Or GetCurrency(IAOthAdj.SPShell) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPShell)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TStud) <> 0 Or GetCurrency(IAOthAdj.SStud) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TStud)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPVictim) <> 0 Or GetCurrency(IAOthAdj.SPVictim) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPVictim)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPWages) <> 0 Or GetCurrency(IAOthAdj.SPWages) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPWages)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPWorkCr) <> 0 Or GetCurrency(IAOthAdj.SPWorkCr) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPWorkCr)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TP2106) <> 0 Or GetCurrency(IAOthAdj.SP2106) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TP2106)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TMSA) <> 0 Or GetCurrency(IAOthAdj.SMSA) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TMSA)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPJury) <> 0 Or GetCurrency(IAOthAdj.SPJury) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPJury)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPRFST) <> 0 Or GetCurrency(IAOthAdj.SPRFST) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPRFST)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPSub) <> 0 Or GetCurrency(IAOthAdj.SPSub) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPSub)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TP501c) <> 0 Or GetCurrency(IAOthAdj.SP501c) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TP501c)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPPerRent) <> 0 Or GetCurrency(IAOthAdj.SPPerRent) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPPerRent)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TP403b) <> 0 Or GetCurrency(IAOthAdj.SP403b) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TP403b)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPUDC) <> 0 Or GetCurrency(IAOthAdj.SPUDC) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPUDC)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPWBF) <> 0 Or GetCurrency(IAOthAdj.SPWBF) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPWBF)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TP8873) <> 0 Or GetCurrency(IAOthAdj.SP8873) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TP8873)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPOlympic) <> 0 Or GetCurrency(IAOthAdj.SPOlympic) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPOlympic)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPEducator) <> 0 Or GetCurrency(IAOthAdj.SPEducator) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPEducator)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPTuition) <> 0 Or GetCurrency(IAOthAdj.SPTuition) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPTuition)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPElectric) <> 0 Or GetCurrency(IAOthAdj.SPElectric) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPElectric)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPRapid) <> 0 Or GetCurrency(IAOthAdj.SPRapid) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPRapid)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IAOthAdj.TPIAABLE) <> 0 Or GetCurrency(IAOthAdj.SPIAABLE) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IAOthAdj.TPIAABLE)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    ReturnVal = Hold
End Sub

Private Sub TPDomProd_Calculation()
'Iowa expanded instructions - Iowa has not conformed to the repeal of the federal domestic production activities deduction. For Iowa will need to complete a federal 8903 and keep with their records and follow IA instructions for adjustments needed when calcing.
    'ReturnVal = GetCurrency(USWRec.TDomProd)
    ReturnVal = 0
End Sub

Private Sub TPEducator_Calculation()
    ReturnVal = GetCurrency(USWRec.TEdExp)
End Sub

Private Sub TPForeign_Calculation()
    ReturnVal = Abs(GetCurrency(USWOthInc.TP2555))
End Sub

Private Sub TPHealthSav_Calculation()
    ReturnVal = GetCurrency(USWRec.THealthSav)
End Sub

Private Sub TPJointAmount_Calculation(Index As Integer)
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetCurrency(IAOthAdj.TPAmount(Index))
    Else
        ReturnVal = GetCurrency(IAOthAdj.TPAmount(Index)) + GetCurrency(IAOthAdj.SPAmount(Index))
    End If
End Sub

Private Sub TPJury_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthAdj.TPJury)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPK1_Calculation()
    If GetBool(USWResidency.F1040NR) = False And GetCurrency(USWOthInc.TPK1) < 0 Then
        ReturnVal = Abs(GetCurrency(USWOthInc.TPK1))
    ElseIf GetBool(USWResidency.F1040NR) = True And GetCurrency(USWOthIncNR.TPK1) < 0 Then
        ReturnVal = Abs(GetCurrency(USWOthIncNR.TPK1))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPName_Calculation()
    ReturnVal = GetString(USWBasicInfo.TPCommon)
End Sub

Private Sub TPOlympic_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthAdj.Text1)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPPerRent_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthAdj.TPPerRent)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPRFST_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthAdj.TPRFST)
    Else
        ReturnVal = GetCurrency(USWOthAdjNR.TPRFST)
    End If
End Sub

Private Sub TPSub_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthAdj.TPSub)
    Else
        ReturnVal = GetCurrency(USWOthAdjNR.TPSub)
    End If
End Sub

Private Sub TPTot_Calculation()
    ReturnVal = GetCurrency(IAOthAdj.TOth1) + GetCurrency(IAOthAdj.TPActiveMil) + GetCurrency(IAOthAdj.TPAltMV) + GetCurrency(IAOthAdj.TPInvolConv) + GetCurrency(IAOthAdj.TPClaimOfRight) + GetCurrency(IAOthAdj.TPIAEd) + GetCurrency(IAOthAdj.TPIADis) + GetCurrency(IAOthAdj.TPDomProd) + GetCurrency(IAOthAdj.TPFirstHmBuy) + GetCurrency(IAOthAdj.TPEmployerSS) + GetCurrency(IAOthAdj.TPFedFuels) + GetCurrency(IAOthAdj.TPForeign) + GetCurrency(IAOthAdj.TP2555) + GetCurrency(IAOthAdj.TPDistressed) + GetCurrency(IAOthAdj.TPHealthSav) + GetCurrency(IAOthAdj.TPVet) + GetCurrency(IAOthAdj.TPVetGrant) + GetCurrency(IAOthAdj.TPHomeHealth) + GetCurrency(IAOthAdj.TPIAVetTrust) + GetCurrency(IAOthAdj.TPMilitaryExem) + GetCurrency(IAOthAdj.TIANOL) + GetCurrency(IAOthAdj.TPOrgan) + GetCurrency(IAOthAdj.TPK1) + GetCurrency(IAOthAdj.TPSegal) + GetCurrency(IAOthAdj.TPShell) + GetCurrency(IAOthAdj.TStud) + GetCurrency(IAOthAdj.TPVictim) + GetCurrency(IAOthAdj.TPWages) + GetCurrency(IAOthAdj.TPWorkCr) + GetCurrency(IAOthAdj.TP2106) + GetCurrency(IAOthAdj.TMSA) + GetCurrency(IAOthAdj.TPJury) + GetCurrency(IAOthAdj.TPRFST) + GetCurrency(IAOthAdj.TPSub) + GetCurrency(IAOthAdj.TP501c) + GetCurrency(IAOthAdj.TPPerRent) + GetCurrency(IAOthAdj.TP403b) + GetCurrency(IAOthAdj.TPUDC) + GetCurrency(IAOthAdj.TPWBF) + GetCurrency(IAOthAdj.TP8873) + GetCurrency(IAOthAdj.TPEducator) + GetCurrency(IAOthAdj.TPTuition) + GetCurrency(IAOthAdj.TPElectric) + GetCurrency(IAOthAdj.TPRapid) + GetCurrency(IAOthAdj.TPOlympic) + GetCurrency(IAOthAdj.TPIAABLE)
End Sub

Private Sub TPTuition_Calculation()
    ReturnVal = 0
    'ReturnVal = GetCurrency(USWRec.TTuitAdj)
End Sub

Private Sub TPUDC_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthAdj.TPUDC)
    Else
        ReturnVal = GetCurrency(USWOthAdjNR.TPUDC)
    End If
End Sub

Private Sub TPWBF_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWOthAdj.TPWBF)
    Else
        ReturnVal = GetCurrency(USWOthAdjNR.TPWBF)
    End If
End Sub

Private Sub TStud_Calculation()
    ReturnVal = GetCurrency(USWRec.TStudAdj)
End Sub

