Private Sub Code_Calculation(Index As Integer)
    Dim count As Integer
    Dim Hold As String
    count = 0
    Hold = ""
    
    If GetCurrency(IANROthAdj.TOth1) <> 0 Or GetCurrency(IANROthAdj.SOth1) <> 0 Then
        If Index = count Then
           Hold = "dd"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPActiveMil) <> 0 Or GetCurrency(IANROthAdj.SPActiveMil) <> 0 Then
        If Index = count Then
           Hold = "b"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPAltMV) <> 0 Or GetCurrency(IANROthAdj.SPAltMV) <> 0 Then
        If Index = count Then
           Hold = "c"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPInvolConv) <> 0 Or GetCurrency(IANROthAdj.SPInvolConv) <> 0 Then
        If Index = count Then
           Hold = "e"
           count = 99
        Else
            count = count + 1
        End If
    End If

    If GetCurrency(IANROthAdj.TPClaimOfRight) <> 0 Or GetCurrency(IANROthAdj.SPClaimOfRight) <> 0 Then
        If Index = count Then
           Hold = "f"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPIAEd) <> 0 Or GetCurrency(IANROthAdj.SPIAEd) <> 0 Then
        If Index = count Then
           Hold = "g"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPIADis) <> 0 Or GetCurrency(IANROthAdj.SPIADis) <> 0 Then
        If Index = count Then
           Hold = "h"
           count = 99
        Else
            count = count + 1
        End If
    End If

    If GetCurrency(IANROthAdj.TPDomProd) <> 0 Or GetCurrency(IANROthAdj.SPDomProd) <> 0 Then
        If Index = count Then
           Hold = "i"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPFirstHmBuy) <> 0 Or GetCurrency(IANROthAdj.SPFirstHmBuy) <> 0 Then
        If Index = count Then
           Hold = "j"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPEmployerSS) <> 0 Or GetCurrency(IANROthAdj.SPEmployerSS) <> 0 Then
        If Index = count Then
           Hold = "k"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPFedFuels) <> 0 Or GetCurrency(IANROthAdj.SPFedFuels) <> 0 Then
        If Index = count Then
           Hold = "l"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPForeign) <> 0 Or GetCurrency(IANROthAdj.SPForeign) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TP2555) <> 0 Or GetCurrency(IANROthAdj.SP2555) <> 0 Then
        If Index = count Then
           Hold = "m"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPDistressed) <> 0 Or GetCurrency(IANROthAdj.SPDistressed) <> 0 Then
        If Index = count Then
           Hold = "n"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPHealthSav) <> 0 Or GetCurrency(IANROthAdj.SPHealthSav) <> 0 Then
        If Index = count Then
           Hold = "o"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPVet) <> 0 Or GetCurrency(IANROthAdj.SPVet) <> 0 Then
        If Index = count Then
           Hold = "p"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
     If GetCurrency(IANROthAdj.TPVetGrant) <> 0 Or GetCurrency(IANROthAdj.SPVetGrant) <> 0 Then
        If Index = count Then
           Hold = "q"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPHomeHealth) <> 0 Or GetCurrency(IANROthAdj.SPHomeHealth) <> 0 Then
        If Index = count Then
           Hold = "r"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPIAVetTrust) <> 0 Or GetCurrency(IANROthAdj.SPIAVetTrust) <> 0 Then
        If Index = count Then
           Hold = "s"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPMilitaryExem) <> 0 Or GetCurrency(IANROthAdj.SPMilitaryExem) <> 0 Then
        If Index = count Then
           Hold = "t"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TIANOL) <> 0 Or GetCurrency(IANROthAdj.SIANOL) <> 0 Then
        If Index = count Then
           Hold = "u"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPOrgan) <> 0 Or GetCurrency(IANROthAdj.SPOrgan) <> 0 Then
        If Index = count Then
           Hold = "v"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPK1) <> 0 Or GetCurrency(IANROthAdj.SPK1) <> 0 Then
        If Index = count Then
           Hold = "w"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPSegal) <> 0 Or GetCurrency(IANROthAdj.SPSegal) <> 0 Then
        If Index = count Then
           Hold = "x"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPShell) <> 0 Or GetCurrency(IANROthAdj.SPShell) <> 0 Then
        If Index = count Then
           Hold = "y"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TStud) <> 0 Or GetCurrency(IANROthAdj.SStud) <> 0 Then
        If Index = count Then
           Hold = "z"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPVictim) <> 0 Or GetCurrency(IANROthAdj.SPVictim) <> 0 Then
        If Index = count Then
           Hold = "aa"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPWages) <> 0 Or GetCurrency(IANROthAdj.SPWages) <> 0 Then
        If Index = count Then
           Hold = "bb"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPWorkCr) <> 0 Or GetCurrency(IANROthAdj.SPWorkCr) <> 0 Then
        If Index = count Then
           Hold = "cc"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TP2106) <> 0 Or GetCurrency(IANROthAdj.SP2106) <> 0 Then
        If Index = count Then
           Hold = "dd"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TMSA) <> 0 Or GetCurrency(IANROthAdj.SMSA) <> 0 Then
        If Index = count Then
           Hold = "dd"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPJury) <> 0 Or GetCurrency(IANROthAdj.SPJury) <> 0 Then
        If Index = count Then
           Hold = "dd"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPRFST) <> 0 Or GetCurrency(IANROthAdj.SPRFST) <> 0 Then
        If Index = count Then
           Hold = "dd"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPSub) <> 0 Or GetCurrency(IANROthAdj.SPSub) <> 0 Then
        If Index = count Then
           Hold = "dd"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TP501c) <> 0 Or GetCurrency(IANROthAdj.SP501c) <> 0 Then
        If Index = count Then
           Hold = "dd"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPPerRent) <> 0 Or GetCurrency(IANROthAdj.SPPerRent) <> 0 Then
        If Index = count Then
           Hold = "dd"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TP403b) <> 0 Or GetCurrency(IANROthAdj.SP403b) <> 0 Then
        If Index = count Then
           Hold = "dd"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPUDC) <> 0 Or GetCurrency(IANROthAdj.SPUDC) <> 0 Then
        If Index = count Then
           Hold = "dd"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPWBF) <> 0 Or GetCurrency(IANROthAdj.SPWBF) <> 0 Then
        If Index = count Then
           Hold = "dd"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TP8873) <> 0 Or GetCurrency(IANROthAdj.SP8873) <> 0 Then
        If Index = count Then
           Hold = "dd"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPOlympic) <> 0 Or GetCurrency(IANROthAdj.SPOlympic) <> 0 Then
        If Index = count Then
           Hold = "dd"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPEducator) <> 0 Or GetCurrency(IANROthAdj.SPEducator) <> 0 Then
        If Index = count Then
           Hold = "ee"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPTuition) <> 0 Or GetCurrency(IANROthAdj.SPTuition) <> 0 Then
        If Index = count Then
           Hold = "ff"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPElectric) <> 0 Or GetCurrency(IANROthAdj.SPElectric) <> 0 Then
        If Index = count Then
           Hold = "gg"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPRapid) <> 0 Or GetCurrency(IANROthAdj.SPRapid) <> 0 Then
        If Index = count Then
           Hold = "hh"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPIAABLE) <> 0 Or GetCurrency(IANROthAdj.SPIAABLE) <> 0 Then
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
    
    Total = GetCurrency(IANROthAdj.TPTot) + GetCurrency(IANROthAdj.SPTot)
    
    ReturnVal = CStr(Total)
End Sub

Private Sub Description_Calculation(Index As Integer)
    Dim count As Integer
    Dim Hold As String
    count = 0
    Hold = ""
    
    If GetCurrency(IANROthAdj.TOth1) <> 0 Or GetCurrency(IANROthAdj.SOth1) <> 0 Then
        If Index = count Then
           Hold = GetString(IANROthAdj.TxtOth1)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPActiveMil) <> 0 Or GetCurrency(IANROthAdj.SPActiveMil) <> 0 Then
        If Index = count Then
           Hold = "Active duty military pay"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPAltMV) <> 0 Or GetCurrency(IANROthAdj.SPAltMV) <> 0 Then
        If Index = count Then
           Hold = "Alternative motor vehicle deduction"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPInvolConv) <> 0 Or GetCurrency(IANROthAdj.SPInvolConv) <> 0 Then
        If Index = count Then
           Hold = "Capital or ordinary gain from involuntary conversion"
           count = 99
        Else
            count = count + 1
        End If
    End If

    If GetCurrency(IANROthAdj.TPClaimOfRight) <> 0 Or GetCurrency(IANROthAdj.SPClaimOfRight) <> 0 Then
        If Index = count Then
           Hold = "Claim of Right deduction"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPIAEd) <> 0 Or GetCurrency(IANROthAdj.SPIAEd) <> 0 Then
        If Index = count Then
           Hold = "College Savings Iowa or Iowa Advisor 529 Plan"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPIADis) <> 0 Or GetCurrency(IANROthAdj.SPIADis) <> 0 Then
        If Index = count Then
           Hold = "Disability income exclusion"
           count = 99
        Else
            count = count + 1
        End If
    End If

    If GetCurrency(IANROthAdj.TPDomProd) <> 0 Or GetCurrency(IANROthAdj.SPDomProd) <> 0 Then
        If Index = count Then
           Hold = "Domestic production activities deduction"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPFirstHmBuy) <> 0 Or GetCurrency(IANROthAdj.SPFirstHmBuy) <> 0 Then
        If Index = count Then
           Hold = "First-Time Homebuyer Savings Account qualifying contributions"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPEmployerSS) <> 0 Or GetCurrency(IANROthAdj.SPEmployerSS) <> 0 Then
        If Index = count Then
           Hold = "Employer social security credit, federal Form 8846"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPFedFuels) <> 0 Or GetCurrency(IANROthAdj.SPFedFuels) <> 0 Then
        If Index = count Then
           Hold = "Alcohol and cellulosic biofuel credit, federal Form 6478"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPForeign) <> 0 Or GetCurrency(IANROthAdj.SPForeign) <> 0 Then
        If Index = count Then
           Hold = "Foreign earned income exclusion, federal Form 2555"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TP2555) <> 0 Or GetCurrency(IANROthAdj.SP2555) <> 0 Then
        If Index = count Then
           Hold = "Foreign housing deduction, federal Form 2555"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPDistressed) <> 0 Or GetCurrency(IANROthAdj.SPDistressed) <> 0 Then
        If Index = count Then
           Hold = "Gains or losses from distressed sale transactions"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPHealthSav) <> 0 Or GetCurrency(IANROthAdj.SPHealthSav) <> 0 Then
        If Index = count Then
           Hold = "Health savings account deduction, federal Form 8889"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPVet) <> 0 Or GetCurrency(IANROthAdj.SPVet) <> 0 Then
        If Index = count Then
           Hold = "Injured veterans programs - contributions"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
     If GetCurrency(IANROthAdj.TPVetGrant) <> 0 Or GetCurrency(IANROthAdj.SPVetGrant) <> 0 Then
        If Index = count Then
           Hold = "Injured veterans programs - grants"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPHomeHealth) <> 0 Or GetCurrency(IANROthAdj.SPHomeHealth) <> 0 Then
        If Index = count Then
           Hold = "In-home health care"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPIAVetTrust) <> 0 Or GetCurrency(IANROthAdj.SPIAVetTrust) <> 0 Then
        If Index = count Then
           Hold = "Iowa Veterans Trust Fund"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPMilitaryExem) <> 0 Or GetCurrency(IANROthAdj.SPMilitaryExem) <> 0 Then
        If Index = count Then
           Hold = "Military exemptions"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TIANOL) <> 0 Or GetCurrency(IANROthAdj.SIANOL) <> 0 Then
        If Index = count Then
           Hold = "Iowa Net Operating Loss"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPOrgan) <> 0 Or GetCurrency(IANROthAdj.SPOrgan) <> 0 Then
        If Index = count Then
           Hold = "Organ transplant expenses"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPK1) <> 0 Or GetCurrency(IANROthAdj.SPK1) <> 0 Then
        If Index = count Then
           Hold = "Partnership income and/or S Corporation income"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPSegal) <> 0 Or GetCurrency(IANROthAdj.SPSegal) <> 0 Then
        If Index = count Then
           Hold = "Segal Americorps Education Award payments"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPShell) <> 0 Or GetCurrency(IANROthAdj.SPShell) <> 0 Then
        If Index = count Then
           Hold = "Speculative shell buildings"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TStud) <> 0 Or GetCurrency(IANROthAdj.SStud) <> 0 Then
        If Index = count Then
           Hold = "Student loan interest deduction"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPVictim) <> 0 Or GetCurrency(IANROthAdj.SPVictim) <> 0 Then
        If Index = count Then
           Hold = "Victim compensation awards"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPWages) <> 0 Or GetCurrency(IANROthAdj.SPWages) <> 0 Then
        If Index = count Then
           Hold = "Wages paid to certain individuals"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPWorkCr) <> 0 Or GetCurrency(IANROthAdj.SPWorkCr) <> 0 Then
        If Index = count Then
           Hold = "Work opportunity credit, federal Form 5884"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TP2106) <> 0 Or GetCurrency(IANROthAdj.SP2106) <> 0 Then
        If Index = count Then
           Hold = "Business expenses of reservists, QPA, FBO, federal Form 2106"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TMSA) <> 0 Or GetCurrency(IANROthAdj.SMSA) <> 0 Then
        If Index = count Then
           Hold = "Archer MSA deduction, federal Form 8853"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPJury) <> 0 Or GetCurrency(IANROthAdj.SPJury) <> 0 Then
        If Index = count Then
           Hold = "Jury pay repayment to employer"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPRFST) <> 0 Or GetCurrency(IANROthAdj.SPRFST) <> 0 Then
        If Index = count Then
           Hold = "Reforestation amortization and expenses"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPSub) <> 0 Or GetCurrency(IANROthAdj.SPSub) <> 0 Then
        If Index = count Then
           Hold = "Repayment of supplemental unemployment benefits"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TP501c) <> 0 Or GetCurrency(IANROthAdj.SP501c) <> 0 Then
        If Index = count Then
           Hold = "Contributions to a 501(c)(18) pension plan"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPPerRent) <> 0 Or GetCurrency(IANROthAdj.SPPerRent) <> 0 Then
        If Index = count Then
           Hold = "Expenses for personal property rental"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TP403b) <> 0 Or GetCurrency(IANROthAdj.SP403b) <> 0 Then
        If Index = count Then
           Hold = "Contributions by certain chaplains to a 403(b) plan"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPUDC) <> 0 Or GetCurrency(IANROthAdj.SPUDC) <> 0 Then
        If Index = count Then
           Hold = "Qualified attorney/court fees paid after 10/22/2004"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPWBF) <> 0 Or GetCurrency(IANROthAdj.SPWBF) <> 0 Then
        If Index = count Then
           Hold = "Qualified whistleblower fees"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TP8873) <> 0 Or GetCurrency(IANROthAdj.SP8873) <> 0 Then
        If Index = count Then
           Hold = "Extraterritorial Income Exclusion, federal Form 8873"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPOlympic) <> 0 Or GetCurrency(IANROthAdj.SPOlympic) <> 0 Then
        If Index = count Then
           Hold = "Nontaxable amount of Olympic and Paralympic medals and USOC prize money"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPEducator) <> 0 Or GetCurrency(IANROthAdj.SPEducator) <> 0 Then
        If Index = count Then
           Hold = "Educator expenses"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPTuition) <> 0 Or GetCurrency(IANROthAdj.SPTuition) <> 0 Then
        If Index = count Then
           Hold = "Tuition and fees deduction"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPElectric) <> 0 Or GetCurrency(IANROthAdj.SPElectric) <> 0 Then
        If Index = count Then
           Hold = "Nonresident Electric Utility Reciprocity"
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPRapid) <> 0 Or GetCurrency(IANROthAdj.SPRapid) <> 0 Then
        If Index = count Then
           Hold = "Rapid Response to State Disasters"
           count = 99
        Else
            count = count + 1
        End If
    End If
       
    If GetCurrency(IANROthAdj.TPIAABLE) <> 0 Or GetCurrency(IANROthAdj.SPIAABLE) <> 0 Then
        If Index = count Then
           Hold = "Iowa ABLE savings plan trust"
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

Private Sub PrintMe_Calculation()
    If GetCurrency(IANROthAdj.TPTot) <> 0 Or GetCurrency(IANROthAdj.SPTot) <> 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPAmount_Calculation(Index As Integer)
    Dim count As Integer
    Dim Hold As Currency
    count = 0
    Hold = 0
    
    If GetCurrency(IANROthAdj.TOth1) <> 0 Or GetCurrency(IANROthAdj.SOth1) <> 0 Then
        If Index = count Then
        Hold = GetCurrency(IANROthAdj.SOth1)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPActiveMil) <> 0 Or GetCurrency(IANROthAdj.SPActiveMil) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPActiveMil)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPAltMV) <> 0 Or GetCurrency(IANROthAdj.SPAltMV) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPAltMV)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPInvolConv) <> 0 Or GetCurrency(IANROthAdj.SPInvolConv) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPInvolConv)
           count = 99
        Else
            count = count + 1
        End If
    End If

    If GetCurrency(IANROthAdj.TPClaimOfRight) <> 0 Or GetCurrency(IANROthAdj.SPClaimOfRight) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPClaimOfRight)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPIAEd) <> 0 Or GetCurrency(IANROthAdj.SPIAEd) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPIAEd)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPIADis) <> 0 Or GetCurrency(IANROthAdj.SPIADis) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPIADis)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPDomProd) <> 0 Or GetCurrency(IANROthAdj.SPDomProd) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPDomProd)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPFirstHmBuy) <> 0 Or GetCurrency(IANROthAdj.SPFirstHmBuy) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPFirstHmBuy)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPEmployerSS) <> 0 Or GetCurrency(IANROthAdj.SPEmployerSS) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPEmployerSS)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPFedFuels) <> 0 Or GetCurrency(IANROthAdj.SPFedFuels) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPFedFuels)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPForeign) <> 0 Or GetCurrency(IANROthAdj.SPForeign) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPForeign)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TP2555) <> 0 Or GetCurrency(IANROthAdj.SP2555) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SP2555)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPDistressed) <> 0 Or GetCurrency(IANROthAdj.SPDistressed) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPDistressed)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPHealthSav) <> 0 Or GetCurrency(IANROthAdj.SPHealthSav) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPHealthSav)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPVet) <> 0 Or GetCurrency(IANROthAdj.SPVet) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPVet)
           count = 99
        Else
            count = count + 1
        End If
    End If

    If GetCurrency(IANROthAdj.TPVetGrant) <> 0 Or GetCurrency(IANROthAdj.SPVetGrant) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPVetGrant)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPHomeHealth) <> 0 Or GetCurrency(IANROthAdj.SPHomeHealth) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPHomeHealth)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPIAVetTrust) <> 0 Or GetCurrency(IANROthAdj.SPIAVetTrust) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPIAVetTrust)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPMilitaryExem) <> 0 Or GetCurrency(IANROthAdj.SPMilitaryExem) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPMilitaryExem)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TIANOL) <> 0 Or GetCurrency(IANROthAdj.SIANOL) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SIANOL)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPOrgan) <> 0 Or GetCurrency(IANROthAdj.SPOrgan) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPOrgan)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPK1) <> 0 Or GetCurrency(IANROthAdj.SPK1) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPK1)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPSegal) <> 0 Or GetCurrency(IANROthAdj.SPSegal) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPSegal)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPShell) <> 0 Or GetCurrency(IANROthAdj.SPShell) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPShell)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TStud) <> 0 Or GetCurrency(IANROthAdj.SStud) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SStud)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPVictim) <> 0 Or GetCurrency(IANROthAdj.SPVictim) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPVictim)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPWages) <> 0 Or GetCurrency(IANROthAdj.SPWages) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPWages)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPWorkCr) <> 0 Or GetCurrency(IANROthAdj.SPWorkCr) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPWorkCr)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TP2106) <> 0 Or GetCurrency(IANROthAdj.SP2106) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SP2106)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TMSA) <> 0 Or GetCurrency(IANROthAdj.SMSA) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SMSA)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPJury) <> 0 Or GetCurrency(IANROthAdj.SPJury) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPJury)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPRFST) <> 0 Or GetCurrency(IANROthAdj.SPRFST) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPRFST)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPSub) <> 0 Or GetCurrency(IANROthAdj.SPSub) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPSub)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TP501c) <> 0 Or GetCurrency(IANROthAdj.SP501c) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SP501c)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPPerRent) <> 0 Or GetCurrency(IANROthAdj.SPPerRent) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPPerRent)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TP403b) <> 0 Or GetCurrency(IANROthAdj.SP403b) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SP403b)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPUDC) <> 0 Or GetCurrency(IANROthAdj.SPUDC) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPUDC)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPWBF) <> 0 Or GetCurrency(IANROthAdj.SPWBF) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPWBF)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TP8873) <> 0 Or GetCurrency(IANROthAdj.SP8873) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SP8873)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPOlympic) <> 0 Or GetCurrency(IANROthAdj.SPOlympic) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPOlympic)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPEducator) <> 0 Or GetCurrency(IANROthAdj.SPEducator) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPEducator)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPTuition) <> 0 Or GetCurrency(IANROthAdj.SPTuition) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPTuition)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPElectric) <> 0 Or GetCurrency(IANROthAdj.SPElectric) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPElectric)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPRapid) <> 0 Or GetCurrency(IANROthAdj.SPRapid) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPRapid)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPIAABLE) <> 0 Or GetCurrency(IANROthAdj.SPIAABLE) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.SPIAABLE)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    ReturnVal = Hold
End Sub

Private Sub SPName_Calculation()
    ReturnVal = GetString(USWBasicInfo.SPCommon)
End Sub

Private Sub SPTot_Calculation()
    If GetBool(IARequired.AskSpouse) = True And GetBool(IAF126.SpRes) = False Then
        ReturnVal = GetCurrency(IANROthAdj.SOth1) + GetCurrency(IANROthAdj.SPActiveMil) + GetCurrency(IANROthAdj.SPAltMV) + GetCurrency(IANROthAdj.SPInvolConv) + GetCurrency(IANROthAdj.SPClaimOfRight) + GetCurrency(IANROthAdj.SPIAEd) + GetCurrency(IANROthAdj.SPIADis) + GetCurrency(IANROthAdj.SPDomProd) + GetCurrency(IANROthAdj.SPFirstHmBuy) + GetCurrency(IANROthAdj.SPEmployerSS) + GetCurrency(IANROthAdj.SPFedFuels) + GetCurrency(IANROthAdj.SPForeign) + GetCurrency(IANROthAdj.SP2555) + GetCurrency(IANROthAdj.SPDistressed) + GetCurrency(IANROthAdj.SPHealthSav) + GetCurrency(IANROthAdj.SPVet) + GetCurrency(IANROthAdj.SPVetGrant) + GetCurrency(IANROthAdj.SPHomeHealth) + GetCurrency(IANROthAdj.SPIAVetTrust) + GetCurrency(IANROthAdj.SPMilitaryExem) + GetCurrency(IANROthAdj.SIANOL) + GetCurrency(IANROthAdj.SPOrgan) + GetCurrency(IANROthAdj.SPK1) + GetCurrency(IANROthAdj.SPSegal) + GetCurrency(IANROthAdj.SPShell) + GetCurrency(IANROthAdj.SStud) + GetCurrency(IANROthAdj.SPVictim) + GetCurrency(IANROthAdj.SPWages) + GetCurrency(IANROthAdj.SPWorkCr) + GetCurrency(IANROthAdj.SP2106) + GetCurrency(IANROthAdj.SMSA) + GetCurrency(IANROthAdj.SPJury) + GetCurrency(IANROthAdj.SPRFST) + GetCurrency(IANROthAdj.SPSub) + GetCurrency(IANROthAdj.SP501c) + GetCurrency(IANROthAdj.SPPerRent) + GetCurrency(IANROthAdj.SP403b) + GetCurrency(IANROthAdj.SPUDC) + GetCurrency(IANROthAdj.SPWBF) + GetCurrency(IANROthAdj.SP8873) + GetCurrency(IANROthAdj.SPOlympic) + GetCurrency(IANROthAdj.SPEducator) + GetCurrency(IANROthAdj.SPTuition) + GetCurrency(IANROthAdj.SPElectric) + GetCurrency(IANROthAdj.SPRapid) + GetCurrency(IANROthAdj.SPIAABLE)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

Private Sub TPAmount_Calculation(Index As Integer)
    Dim count As Integer
    Dim Hold As Currency
    count = 0
    Hold = 0
    
    If GetCurrency(IANROthAdj.TOth1) <> 0 Or GetCurrency(IANROthAdj.SOth1) <> 0 Then
        If Index = count Then
        Hold = GetCurrency(IANROthAdj.TOth1)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPActiveMil) <> 0 Or GetCurrency(IANROthAdj.SPActiveMil) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPActiveMil)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPAltMV) <> 0 Or GetCurrency(IANROthAdj.SPAltMV) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPAltMV)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPInvolConv) <> 0 Or GetCurrency(IANROthAdj.SPInvolConv) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPInvolConv)
           count = 99
        Else
            count = count + 1
        End If
    End If

    If GetCurrency(IANROthAdj.TPClaimOfRight) <> 0 Or GetCurrency(IANROthAdj.SPClaimOfRight) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPClaimOfRight)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPIAEd) <> 0 Or GetCurrency(IANROthAdj.SPIAEd) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPIAEd)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPIADis) <> 0 Or GetCurrency(IANROthAdj.SPIADis) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPIADis)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPDomProd) <> 0 Or GetCurrency(IANROthAdj.SPDomProd) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPDomProd)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPFirstHmBuy) <> 0 Or GetCurrency(IANROthAdj.SPFirstHmBuy) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPFirstHmBuy)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPEmployerSS) <> 0 Or GetCurrency(IANROthAdj.SPEmployerSS) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPEmployerSS)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPFedFuels) <> 0 Or GetCurrency(IANROthAdj.SPFedFuels) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPFedFuels)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPForeign) <> 0 Or GetCurrency(IANROthAdj.SPForeign) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPForeign)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TP2555) <> 0 Or GetCurrency(IANROthAdj.SP2555) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TP2555)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPDistressed) <> 0 Or GetCurrency(IANROthAdj.SPDistressed) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPDistressed)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPHealthSav) <> 0 Or GetCurrency(IANROthAdj.SPHealthSav) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPHealthSav)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPVet) <> 0 Or GetCurrency(IANROthAdj.SPVet) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPVet)
           count = 99
        Else
            count = count + 1
        End If
    End If

    If GetCurrency(IANROthAdj.TPVetGrant) <> 0 Or GetCurrency(IANROthAdj.SPVetGrant) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPVetGrant)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPHomeHealth) <> 0 Or GetCurrency(IANROthAdj.SPHomeHealth) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPHomeHealth)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPIAVetTrust) <> 0 Or GetCurrency(IANROthAdj.SPIAVetTrust) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPIAVetTrust)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPMilitaryExem) <> 0 Or GetCurrency(IANROthAdj.SPMilitaryExem) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPMilitaryExem)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TIANOL) <> 0 Or GetCurrency(IANROthAdj.SIANOL) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TIANOL)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPOrgan) <> 0 Or GetCurrency(IANROthAdj.SPOrgan) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPOrgan)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPK1) <> 0 Or GetCurrency(IANROthAdj.SPK1) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPK1)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPSegal) <> 0 Or GetCurrency(IANROthAdj.SPSegal) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPSegal)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPShell) <> 0 Or GetCurrency(IANROthAdj.SPShell) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPShell)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TStud) <> 0 Or GetCurrency(IANROthAdj.SStud) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TStud)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPVictim) <> 0 Or GetCurrency(IANROthAdj.SPVictim) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPVictim)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPWages) <> 0 Or GetCurrency(IANROthAdj.SPWages) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPWages)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPWorkCr) <> 0 Or GetCurrency(IANROthAdj.SPWorkCr) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPWorkCr)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TP2106) <> 0 Or GetCurrency(IANROthAdj.SP2106) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TP2106)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TMSA) <> 0 Or GetCurrency(IANROthAdj.SMSA) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TMSA)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPJury) <> 0 Or GetCurrency(IANROthAdj.SPJury) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPJury)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPRFST) <> 0 Or GetCurrency(IANROthAdj.SPRFST) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPRFST)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPSub) <> 0 Or GetCurrency(IANROthAdj.SPSub) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPSub)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TP501c) <> 0 Or GetCurrency(IANROthAdj.SP501c) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TP501c)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPPerRent) <> 0 Or GetCurrency(IANROthAdj.SPPerRent) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPPerRent)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TP403b) <> 0 Or GetCurrency(IANROthAdj.SP403b) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TP403b)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPUDC) <> 0 Or GetCurrency(IANROthAdj.SPUDC) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPUDC)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPWBF) <> 0 Or GetCurrency(IANROthAdj.SPWBF) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPWBF)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TP8873) <> 0 Or GetCurrency(IANROthAdj.SP8873) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TP8873)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPOlympic) <> 0 Or GetCurrency(IANROthAdj.SPOlympic) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPOlympic)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPEducator) <> 0 Or GetCurrency(IANROthAdj.SPEducator) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPEducator)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPTuition) <> 0 Or GetCurrency(IANROthAdj.SPTuition) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPTuition)
           count = 99
        Else
            count = count + 1
        End If
     End If
     
    If GetCurrency(IANROthAdj.TPElectric) <> 0 Or GetCurrency(IANROthAdj.SPElectric) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPElectric)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPRapid) <> 0 Or GetCurrency(IANROthAdj.SPRapid) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPRapid)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    If GetCurrency(IANROthAdj.TPIAABLE) <> 0 Or GetCurrency(IANROthAdj.SPIAABLE) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IANROthAdj.TPIAABLE)
           count = 99
        Else
            count = count + 1
        End If
    End If
    
    ReturnVal = Hold
End Sub

Private Sub TPJointAmount_Calculation(Index As Integer)
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetCurrency(IANROthAdj.TPAmount(Index))
    Else
        ReturnVal = GetCurrency(IANROthAdj.TPAmount(Index)) + GetCurrency(IANROthAdj.SPAmount(Index))
    End If
End Sub

Private Sub TPName_Calculation()
    ReturnVal = GetString(USWBasicInfo.TPCommon)
End Sub

Private Sub TPTot_Calculation()
    If GetBool(IAF126.TpPYRes) = True Or GetBool(IAF126.TpNonRes) = True Then
        ReturnVal = GetCurrency(IANROthAdj.TOth1) + GetCurrency(IANROthAdj.TPActiveMil) + GetCurrency(IANROthAdj.TPAltMV) + GetCurrency(IANROthAdj.TPInvolConv) + GetCurrency(IANROthAdj.TPClaimOfRight) + GetCurrency(IANROthAdj.TPIAEd) + GetCurrency(IANROthAdj.TPIADis) + GetCurrency(IANROthAdj.TPDomProd) + GetCurrency(IANROthAdj.TPFirstHmBuy) + GetCurrency(IANROthAdj.TPEmployerSS) + GetCurrency(IANROthAdj.TPFedFuels) + GetCurrency(IANROthAdj.TPForeign) + GetCurrency(IANROthAdj.TP2555) + GetCurrency(IANROthAdj.TPDistressed) + GetCurrency(IANROthAdj.TPHealthSav) + GetCurrency(IANROthAdj.TPVet) + GetCurrency(IANROthAdj.TPVetGrant) + GetCurrency(IANROthAdj.TPHomeHealth) + GetCurrency(IANROthAdj.TPIAVetTrust) + GetCurrency(IANROthAdj.TPMilitaryExem) + GetCurrency(IANROthAdj.TIANOL) + GetCurrency(IANROthAdj.TPOrgan) + GetCurrency(IANROthAdj.TPK1) + GetCurrency(IANROthAdj.TPSegal) + GetCurrency(IANROthAdj.TPShell) + GetCurrency(IANROthAdj.TStud) + GetCurrency(IANROthAdj.TPVictim) + GetCurrency(IANROthAdj.TPWages) + GetCurrency(IANROthAdj.TPWorkCr) + GetCurrency(IANROthAdj.TP2106) + GetCurrency(IANROthAdj.TMSA) + GetCurrency(IANROthAdj.TPJury) + GetCurrency(IANROthAdj.TPRFST) + GetCurrency(IANROthAdj.TPSub) + GetCurrency(IANROthAdj.TP501c) + GetCurrency(IANROthAdj.TPPerRent) + GetCurrency(IANROthAdj.TP403b) + GetCurrency(IANROthAdj.TPUDC) + GetCurrency(IANROthAdj.TPWBF) + GetCurrency(IANROthAdj.TP8873) + GetCurrency(IANROthAdj.TPOlympic) + GetCurrency(IANROthAdj.TPEducator) + GetCurrency(IANROthAdj.TPTuition) + GetCurrency(IANROthAdj.TPElectric) + GetCurrency(IANROthAdj.TPRapid) + GetCurrency(IANROthAdj.TPIAABLE)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TxtOth1_Calculation()
    ReturnVal = GetString(IAOthAdj.TxtOth1)
End Sub

