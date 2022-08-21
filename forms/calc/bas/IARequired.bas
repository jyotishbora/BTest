Private Sub Alert10_Calculation()
    If GetString(IAF1040.CountyNo) = "" Or GetString(IAF1040.SchNo) = "" Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert11_Calculation()
    If GetString(IAF1040.CountyNo) = "" Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert12_Calculation()
    If GetString(IAF1040.SchNo) = "" Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert15_Calculation()
    If GetBool(IAF1040.MFJ) = True Or GetBool(IAF1040.CombMFS) = True Then
        If (GetBool(IAF126.TpNonRes) = True Or (GetBool(IAF126.TpPYRes) = True And (GetDate(IAF126.TpDateOut) > 0 And GetDate(IAF126.TpDateOut) < MakeDate(12, 31, YearNumber)))) And (GetBool(IAF126.SpNonRes) = True Or (GetBool(IAF126.SpPYRes) = True And (GetDate(IAF126.SpDateOut) > 0 And GetDate(IAF126.SpDateOut) < MakeDate(12, 31, YearNumber)))) Then
            If GetString(IAF1040.CountyNo) = "00" Then
                ReturnVal = 0
            Else
                ReturnVal = 1
            End If
        Else
            ReturnVal = 0
        End If
    ElseIf GetBool(IAF126.TpNonRes) = True Or (GetBool(IAF126.TpPYRes) = True And (GetDate(IAF126.TpDateOut) > 0 And GetDate(IAF126.TpDateOut) < MakeDate(12, 31, YearNumber))) Then
            If GetString(IAF1040.CountyNo) = "00" Then
                ReturnVal = 0
            Else
                ReturnVal = 1
            End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert100_Calculation()
    If IAFS() = 3 And GetCurrency(IAF1040.BGainDed) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IAF1040.AGainDed) <> 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert110_Calculation()
    If GetNumber(USD1099R.UnderAge) > 0 Then
        If GetCurrency(IAOthAdj.TPIADis) + GetCurrency(IAOthAdj.SPIADis) = 0 Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert120_Calculation()
    If GetBool(USWResidency.F1040NR) = False And GetCurrency(IAOthAdj.SIANOL) > 0 And GetCurrency(IAOthAdj.SIANOL) = Abs(GetCurrency(USWOthInc.SPNOL)) Then
        ReturnVal = 1
    ElseIf GetBool(USWResidency.F1040NR) = False And GetCurrency(IAOthAdj.TIANOL) > 0 And GetCurrency(IAOthAdj.TIANOL) = Abs(GetCurrency(USWOthInc.TPNOL)) Then
        ReturnVal = 1
    ElseIf GetBool(USWResidency.F1040NR) = True And GetCurrency(IAOthAdj.TIANOL) > 0 And GetCurrency(IAOthAdj.TIANOL) = Abs(GetCurrency(USWOthIncNR.TPNOL)) Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert130_Calculation()
    If GetCurrency(IAAddFedTax.TPBalDue) <> 0 Or GetCurrency(IAAddFedTax.SPBalDue) <> 0 Then
        ReturnVal = 0
    ElseIf GetCurrency(IAF1040.BRefund) = 0 And GetCurrency(IAF1040.ARefund) = 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert150_Calculation()
    If GetBool(USWRec.ItmDdn) = False And GetBool(IAF1040.ItemCheck) = False Then
        If GetCurrency(IARequired.SchADeprAmt) <> 0 Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert180_Calculation()
    If (GetCurrency(USF1040.Foreign) > 0 Or GetCurrency(USF1040NR.Foreign) > 0) And GetBool(IA130.Exist) = False Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert190_Calculation()
    Dim count As Integer
    Dim Lim As Integer
    Dim Total As Integer
    Dim Total2 As Integer

    Lim = GetAllCopies(IA137)
    count = 1
    Total = 0
    Total2 = 0
    
    Do While count <= Lim
        If GetBool(IA137.Taxpayer, count) = True And GetBool(IA137.Company, count) = True And GetBool(IA137.Print, count) = True Then
            Total = Total + 1
        Else
            Total = Total
        End If
        
        If GetBool(IA137.Taxpayer, count) = True And GetBool(IA137.Site, count) = True And GetBool(IA137.Print, count) = True Then
            Total2 = Total2 + 1
        Else
            Total2 = Total2
        End If
        
        count = count + 1
    Loop
    
    If Total > 1 Then
        ReturnVal = 1
    ElseIf Total > 0 And Total2 > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
    
End Sub

Private Sub Alert20_Calculation()
    If FedFS() = 1 And IAFS() <> 1 Then
        ReturnVal = 1
    ElseIf FedFS() = 2 And IAFS() <> 2 And IAFS() <> 3 Then
        ReturnVal = 1
    ElseIf FedFS() = 3 And IAFS() <> 4 Then
        ReturnVal = 1
    ElseIf FedFS() = 4 And IAFS() <> 5 Then
        ReturnVal = 1
    ElseIf FedFS() = 5 And IAFS() <> 6 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert200_Calculation()
    Dim count As Integer
    Dim Lim As Integer
    Dim Total As Integer
    Dim Total2 As Integer
    
    Lim = GetAllCopies(IA137)
    count = 1
    Total = 0
    Total2 = 0
    
    Do While count <= Lim
        If GetBool(IA137.Spouse, count) = True And GetBool(IA137.Company, count) = True And GetBool(IA137.Print, count) = True Then
            Total = Total + 1
        Else
            Total = Total
        End If
        
        If GetBool(IA137.Spouse, count) = True And GetBool(IA137.Site, count) = True And GetBool(IA137.Print, count) = True Then
            Total2 = Total2 + 1
        Else
            Total2 = Total2
        End If
        
        count = count + 1
    Loop
    
    If Total > 1 Then
        ReturnVal = 1
    ElseIf Total > 0 And Total2 > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert210_Calculation()
    If GetNumber(IASch4136.MEF4136TP) > 1 Or GetNumber(IASch4136.MEF4136SP) > 1 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert220_Calculation()
    If IAFS() <> 3 Then
        If GetCurrency(IASch4136.TotCr, 1) > 0 And GetCurrency(IASch4136.TotCr, 2) > 0 Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert225_Calculation()
    ReturnVal = 0
End Sub

Private Sub Alert250_Calculation()
    If GetCurrency(IAF1040.Penalty) > 0 And GetDate(IAF1040.DateDuePaid) = #4/30/2019# Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert260_Calculation()
    Dim Est1 As Long
    Dim Est2 As Long

    If GetBool(IAEstimates.ApplySpecific, 1) = True Then
        If GetCurrency(IAEstimates.SpecAmt, 1) > GetCurrency(IAEstimates.TotNetTax2, 1) Then
            Est1 = 1
        Else
            Est1 = 0
        End If
    Else
        Est1 = 0
    End If
    
    If GetBool(IAEstimates.ApplySpecific, 2) = True Then
        If GetCurrency(IAEstimates.SpecAmt, 2) > GetCurrency(IAEstimates.TotNetTax2, 2) Then
            Est2 = 1
        Else
            Est2 = 0
        End If
    Else
        Est2 = 0
    End If
    
    If Est1 + Est2 > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert280_Calculation()
    Dim count As Integer
    Dim Lim As Integer
    Dim Total As Integer
    
    Lim = GetAllCopies(IA177)
    count = 1
    Total = 0
    
    Do While count <= Lim
        If GetCurrency(IA177.CYAdoptionTaxCr, count) > 0 Then
            Total = Total + 1
        Else
            Total = Total
        End If
        
        count = count + 1
    Loop

    If GetNumber(USWAdoption.Create) > 0 And GetCurrency(IASchA.TotAdoptAmt) = 0 And Total = 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert30_Calculation()
    If GetCurrency(USWRec.TAGI) > 0 And GetCurrency(USWRec.SAGI) > 0 And GetBool(IAF1040.MFJ) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert282_Calculation()
    If GetBool(IAF1040.CombMFS) = True And GetBool(IA177.Spouse) = 0 And GetCurrency(IA177.CYAdoptionTaxCr) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert285_Calculation()
    If GetBool(IARequired.VerifiedIA177) = True Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.CombMFS) = True And GetCurrency(IA177.CYAdoptionTaxCr) > 5000@ Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert295A_Calculation()
    If GetCurrency(IAF1040.AEst) = 0 Then
        ReturnVal = 0
    ElseIf GetCurrency(IAF1040.AEst) = GetCurrency(IAF1040.AIATaxWith) Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert295B_Calculation()
    If GetCurrency(IAF1040.BEst) = 0 Then
        ReturnVal = 0
    ElseIf GetCurrency(IAF1040.BEst) = GetCurrency(IAF1040.BIATaxWith) Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert300_Calculation()
    If GetNumber(IARequired.SchBIntNoPayer) > 0 Then
        ReturnVal = 1
    ElseIf GetNumber(IAWBPInt.IntNoPayer) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert310_Calculation()
    If GetNumber(IARequired.SchBDivNoPayer) > 0 Then
        ReturnVal = 1
    ElseIf GetNumber(IAWBPDiv.DivNoPayer) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert320_Calculation()
    If GetBool(IAF126.TpPYRes) = True Then
        If GetString(IAF126.TpDateIn) = "" And GetString(IAF126.TpDateOut) = "" Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert330_Calculation()
    If GetBool(IAF126.SpPYRes) = True And GetBool(IARequired.AskSpouse) = True Then
        If GetString(IAF126.SpDateIn) = "" And GetString(IAF126.SpDateOut) = "" Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert40_Calculation()
    If GetBool(IAF1040.NoMFSInc) = True Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.MFS) = True And GetCurrency(IAF1040.SpIncome) = 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert50_Calculation()
    If GetBool(IAF1040.MFS) = True And (GetCurrency(IAWkAltTax.Lesser) > 0 And (GetCurrency(IAWkAltTax.Lesser) = GetCurrency(IAWkAltTax.Mult))) Then
        If GetCurrency(IAF1040.SpSSB) = 0 And GetBool(IAF1040.NoSpSSB) = False Then
            ReturnVal = 1
        ElseIf GetCurrency(IAF1040.SpPenExcl) = 0 And GetBool(IAF1040.NoSpPenExcl) = False Then
            ReturnVal = 1
        ElseIf GetCurrency(IAF1040.SpTaxInc) = 0 And GetBool(IAF1040.NoSpTaxInc) = False Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert60_Calculation()
    If GetCurrency(IARequired.IAEic) > 0 Then
        If GetBool(IAF1040.NoMFSEI) = True Then
            ReturnVal = 0
        ElseIf GetBool(IAF1040.MFS) = True And GetCurrency(IAF1040.MFSEI) = 0 Then
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

Private Sub Alert80_Calculation()
'Re-did to factor in prior year 179 assets and use IAStatePrior. Does trigger for any year with bonus.  Next year 2019 need to alert non conformity assets that are disposed? Not this year since should only be current year assets.
    ReturnVal = GetNumber(IAWDepr.StatePriorDisposal)
End Sub

Private Sub Alert90_Calculation()
'for 2018 make no change since need to ask or alert if had depr adjustment in prior year and need to make an entry for catch-up depr. May need to see next year if should exclude 2018 veh that were not reported on IA4562A since was just on IA 2106
    If GetBool(IARequired.Ask4562A) = True Then
        If GetCurrency(IA4562A.TotP2ColF) = 0 Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert340_Calculation()
'set this to zero if Iowa passes conformity
    'ReturnVal = GetNumber(USWSpouse.StateSec179Tent) fed math for this is below, do similar but with IA fields
    'If GetCurrency(USW4562State.TotElect179) <> GetCurrency(USW4562State.Tent179) Then
    '    ReturnVal = 1
    'Else
    '    ReturnVal = 0
    'End If
    
    If GetCurrency(IARequired.TotElect179) <> GetCurrency(IARequired.Tent179) Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert345_Calculation()
    If GetCurrency(IARequired.Diss179) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert350_Calculation()
    If GetCurrency(IA1040X.TotPrevTax) > 0@ And (GetCurrency(IA1040X.TotPrevTax) = GetCurrency(IA1040X.PrevOP)) Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert360_Calculation()
    If GetBool(IARequired.VerifiedIA126) = True Then
        ReturnVal = 0
    ElseIf GetNumber(IAF126.Print) = 1 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Ask130Copy_Calculation()
    If GetBool(IARequired.F130Y) = True And GetNumber(IA130.Exist) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Ask134_Calculation()
    If GetNumber(IA134.Exist) > 0 Then
        ReturnVal = 1
    ElseIf GetBool(IAF1040.CombMFS) = True And GetNumber(IA134Sp.Exist) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Ask4136_Calculation()
    If GetBool(USF4136.Exist) = True Or GetNumber(USSchF.Exist) > 0 Or GetNumber(USSchC.Exist) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Ask4562A_Calculation()
    If GetNumber(IA4562A.StateDispNbr) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Ask4562PIV_Calculation()
    If GetNumber(USDPartK1.Exist) > 0 Or GetNumber(USDSCorpK1.Exist) > 0 Then
        ReturnVal = 1
    ElseIf GetNumber(IA4562PIV.Exist) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AskCharCont_Calculation()
    Dim FedContributions As Currency
    
    If GetBool(USWResidency.F1040NR) = False Then
        FedContributions = GetCurrency(USSchA.Cash) + GetCurrency(USSchA.NonCash)
    Else
        FedContributions = GetCurrency(USSchANR.Cash) + GetCurrency(USSchANR.NonCash)
    End If

    If FedContributions > 0 Then
        If GetCurrency(IAF1040.BOthIACr) > 0 Or GetCurrency(IAF1040.AOthIACr) > 0 Then
            ReturnVal = 1
        ElseIf GetCurrency(IAOthAdj.TPVet) > 0 Or GetCurrency(IAOthAdj.SPVet) > 0 Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AskEarlyChCr_Calculation()
    If Trim(GetString(IAChildCredit.DepName(0))) <> "" And GetCurrency(IAChildCredit.TotNI) < 45000@ Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AskEstCopy_Calculation()
    If GetBool(IARequired.EstY) = True And GetNumber(IAEstimates.Exist) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AskFedFuel_Calculation()
    If GetBool(IARequired.AskSpouse) = True Then
        If GetCurrency(USF4136.TotalCredit) > 0 Or GetCurrency(IAAddFedTax.SPFuel) > 0 Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AskFilStat_Calculation()
    If IAFS() = 2 Or IAFS() = 3 Or IAFS() = 4 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AskIAEst_Calculation()
    If GetBool(IAF1040.CombMFS) = True And GetCurrency(IAStateEst.TotIAEst) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AskMedExp_Calculation()
    If GetCurrency(USSchA.MedExp) > 0 Then
        If GetCurrency(IAF1040.BHealth) > 0 Or GetCurrency(IAF1040.AHealth) > 0 Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AskPenExc_Calculation()
    If GetCurrency(IAF1040.AIRA) + GetCurrency(IAF1040.APensions) + GetCurrency(IAF1040.BIRA) + GetCurrency(IAF1040.BPensions) + GetCurrency(IAF126.AIRA) + GetCurrency(IAF126.APensions) + GetCurrency(IAF126.BIRA) + GetCurrency(IAF126.BPensions) <> 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AskPensions_Calculation()
    If GetCurrency(USWRec.TotPension) > 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IAWPenExc.TPPensions) + GetCurrency(IAWPenExc.SPPensions) <> 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AskReviewOthAdj_Calculation()
    If GetStatusCopies(IAWHealth, ModifiedStatus) > 0 Then
        ReturnVal = 1
    ElseIf GetStatusCopies(IAWPenExc, ModifiedStatus) > 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IAF1040.AGainDed) > 0 Or GetCurrency(IAF1040.BGainDed) > 0 Then
        ReturnVal = 1
    ElseIf GetStatusCopies(IAOthAdj, ModifiedStatus) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BalDueAmt_Calculation()
    ReturnVal = Abs(GetCurrency(IAF1040.RefBalDue))
End Sub

Private Sub BaseAmt_Calculation()
    If GetBool(IAF1040.Over65) = True Then
        ReturnVal = 24000@
    Else
        ReturnVal = 9000@
    End If
End Sub

Private Sub BProRate_Calculation()
    If IAFS() = 3 Then
        If GetCurrency(IAF1040.BNet) < 0 And GetCurrency(IAF1040.ANet) < 0 Then
            If GetCurrency(IAF1040.BNet) < GetCurrency(IAF1040.ANet) Then
                ReturnVal = 0
            Else
                ReturnVal = 1
            End If
        ElseIf GetCurrency(IAF1040.BNet) < 0 Then
            ReturnVal = 0
        ElseIf GetCurrency(IAF1040.BNet) > 0 And GetCurrency(IARequired.TotNI) <= 0 Then
            ReturnVal = 1
        ElseIf GetCurrency(IARequired.TotNI) = 0 Then
            ReturnVal = 0
        Else
            ReturnVal = MaxValue(0, (MinValue(1#, GetFloat(IAF1040.BNet) / GetFloat(IARequired.TotNI))))
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BusInc179_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IARequired.FedLn11) + GetCurrency(IARequired.IABusinessNC))
End Sub

Private Sub CombNames_Calculation()
    If GetBool(IAF1040.MFJ) = True Or GetBool(IAF1040.CombMFS) = True Then
        If GetString(IAF1040.LastName) = GetString(IAF1040.SpouseLast) Then
            ReturnVal = GetString(IAF1040.FirstName) & " and " & GetString(IAF1040.SpouseFirst) & " " & GetString(IAF1040.LastName)
        Else
            ReturnVal = GetString(IAF1040.FirstName) & " " & GetString(IAF1040.LastName) & " and " & GetString(IAF1040.SpouseFirst) & " " & GetString(IAF1040.SpouseLast)
        End If
    Else
        ReturnVal = GetString(IAF1040.FirstName) & " " & GetString(IAF1040.LastName)
    End If
End Sub

Private Sub CrAddFedTax_Calculation()
    If GetNumber(USWFICA.Exist) > 0 Then
        ReturnVal = 1
    ElseIf GetNumber(USF4136.Exist) > 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(USWRec.PYOwe) > 0 Then
        ReturnVal = 1        
    ElseIf GetCurrency(USWRec.PYOweNR) > 0 Then
        ReturnVal = 1        
    ElseIf GetCurrency(USWRec.PYExt) > 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(USWRec.PYExtNR) > 0 Then
        ReturnVal = 1        
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrOthAdj_Calculation()
    If GetNumber(USWOthAdj.Exist) > 0 Then
        ReturnVal = 1
    ElseIf GetNumber(USWOthAdjNR.Exist) > 0 Then
        ReturnVal = 1
    ElseIf GetNumber(USWOthInc.Exist) > 0 Then
        ReturnVal = 1
    ElseIf GetNumber(USWOthIncNR.Exist) > 0 Then
        ReturnVal = 1
    ElseIf GetBool(USF8910.Print) = True Then
        ReturnVal = 1
    ElseIf GetCurrency(USWRec.TotEdExp) > 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(USWRec.TotBusExp2106) > 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(USWRec.TotStudAdj) > 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(USWRec.TotTuitAdj) > 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(USWRec.TotHealthSav) > 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(USWRec.TotDomProd) > 0 Then
        ReturnVal = 1
' Need to create if PYNR so interview displays correctly for IA 126 worksheets
    ElseIf GetBool(IAF126.TpPYNR) = True Or GetBool(IAF126.SpPYNR) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrOthInc_Calculation()
    If GetNumber(USWOthInc.Exist) > 0 Then
        ReturnVal = 1
    ElseIf GetNumber(USWOthIncNR.Exist) > 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA4562.TotDepAdj) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA4562Sp.TotDepAdj) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA4562A.TotDepAdj) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(USF6251.Depl) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(USF6251.IntangDrill) <> 0 Then
        ReturnVal = 1
' Need to create if PYNR so interview displays correctly for IA 126 worksheets
    ElseIf GetBool(IAF126.TpPYNR) = True Or GetBool(IAF126.SpPYNR) = True Then
        ReturnVal = 1
    ElseIf GetCurrency(IARequired.Tot8824) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IARequired.TotIAExReimb) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IAWNonConformAdj.SPTotNonConformAdj) <> 0 Or GetCurrency(IAWNonConformAdj.TPTotNonConformAdj) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA4684.IANonConformAdj) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IA2106.IAWages) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IAWSchFLoss.ExcessLoss) <> 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrPenExc_Calculation()
    If GetCurrency(USWRec.TotIRAInc) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(USWRetirement.TPAddQCD) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(USWRetirement.SPAddQCD) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(USWRec.TotPension) <> 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrSETax_Calculation()
    If GetCurrency(USF8962.PTCRepay) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(USF1040.SETax) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(USF1040NR.SETax) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(USF1040.TipTax) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(USF1040NR.TipTax) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(USWRetirement.RetTax) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(USF1040.SchHTax) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(USF1040NR.SchHTax) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(USF1040.HomeBuyRepay) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(USF1040NR.HomeBuyRepay) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(USWHealthPen.Penalty) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(USF8959.TotAddMedTax) <> 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(USWOthTax.TotOthTax) <> 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CurrentDate_Calculation()
    ReturnVal = CDate("Current")
End Sub

Private Sub Ded179_Calculation()
    ReturnVal = MinValue(GetCurrency(IARequired.BusInc179), GetCurrency(IARequired.Tent179) + GetCurrency(IARequired.TotCo179))
End Sub

Private Sub DepLength_Calculation()
    ReturnVal = Len(GetString(IARequired.DepNames))
End Sub

Private Sub DepNames_Calculation()
    Dim DepName As String
  
    If GetString(USWAddDep.DepFName(0)) <> "" Then
        DepName = GetString(USWAddDep.DepFName(0)) & " "
    End If
    If GetString(USWAddDep.DepFName(1)) <> "" Then
        DepName = DepName + GetString(USWAddDep.DepFName(1)) + " "
    End If
    If GetString(USWAddDep.DepFName(2)) <> "" Then
        DepName = DepName + GetString(USWAddDep.DepFName(2)) + " "
    End If
    If GetString(USWAddDep.DepFName(3)) <> "" Then
        DepName = DepName + GetString(USWAddDep.DepFName(3)) + " "
    End If
    If GetString(USWAddDep.DepFName(4)) <> "" Then
        DepName = DepName + GetString(USWAddDep.DepFName(4)) + " "
    End If
    If GetString(USWAddDep.DepFName(5)) <> "" Then
        DepName = DepName + GetString(USWAddDep.DepFName(5)) + " "
    End If

    ReturnVal = DepName
End Sub

Private Sub DeprAdj_Calculation()
    ReturnVal = GetCurrency(IAWOthInc.TotBonus)
End Sub

Private Sub Diss179_Calculation()
    ReturnVal = GetCurrency(IARequired.TotCo179) + GetCurrency(IARequired.Tent179) - GetCurrency(IARequired.Ded179)
End Sub

Private Sub EICRatio_Calculation()
    If GetCurrency(IARequired.TotEICEarnInc) = 0 Then
        ReturnVal = 0
    ElseIf GetCurrency(IARequired.SEICEarnInc) < 0 Then
        ReturnVal = 0
    Else
        ReturnVal = MinValue(1#, MaxValue(0, GetFloat(IARequired.SEICEarnInc) / GetFloat(IARequired.TotEICEarnInc)))
    End If
End Sub

Private Sub FedAGI_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USF1040.AGI)
    Else
        ReturnVal = GetCurrency(USF1040NR.AGI) 
    End If
End Sub

Private Sub FedFilingStatus_Calculation()
    If FedFS() = 1 Then
        ReturnVal = "single"
    ElseIf FedFS() = 2 Then
        ReturnVal = "married filing jointly"
    ElseIf FedFS() = 3 Then
        ReturnVal = "married filing separately"
    ElseIf FedFS() = 4 Then
        ReturnVal = "head of household"
    Else
        ReturnVal = "qualifying widow(er)"
    End If
End Sub

Private Sub FedLn11_Calculation()
    ReturnVal = GetCurrency(USF4562.BusInc179, 1)
End Sub

Private Sub FilingStatus_Calculation()
    ReturnVal = IAFS()
End Sub

Private Sub FYEIC_Calculation()
    ReturnVal = CDollar(GetFloat(USF1040.Eic) * 0.15)
End Sub

Private Sub FYRes_Calculation()
    Dim Only1NR As Long
    Dim TPRes As Long
    Dim SPRes As Long
    
    If GetBool(IAF126.TpNonRes) = True And GetBool(IAF126.SpRes) = True Then
        Only1NR = 1
    ElseIf GetBool(IAF126.TpRes) = True And GetBool(IAF126.SpNonRes) = True Then
        Only1NR = 1
    Else
        Only1NR = 0
    End If

    If GetBool(IAF126.Exist) = False Then
        TPRes = 1
    ElseIf GetBool(IAF1040.MFJ) = True And Only1NR = 1 Then
        TPRes = 1
    ElseIf GetBool(IAF1040.MFJ) = True And GetBool(IAF126.TpRes) = True And GetBool(IAF126.SpRes) = True Then
        TPRes = 1
    ElseIf GetBool(IAF1040.MFJ) <> True And GetBool(IAF126.TpRes) = True Then
        TPRes = 1
    Else
        TPRes = 0
    End If
    
    If GetBool(IAF1040.CombMFS) = True Then
        If GetBool(IAF126.Exist) = False Then
            SPRes = 1
        ElseIf GetBool(IAF126.SpRes) = True Then
            SPRes = 1
        Else
            SPRes = 0
        End If
    Else
        SPRes = 0
    End If
    
    If GetBool(IAF1040.CombMFS) = True Then
        If TPRes + SPRes = 2 Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    ElseIf TPRes = 1 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
            
End Sub

Private Sub IAAGI_Calculation()
    ReturnVal = GetCurrency(IARequired.FedAGI) + GetCurrency(IARequired.DeprAdj) + GetCurrency(IARequired.NonConfLn14) - GetCurrency(IARequired.NCMove) - GetCurrency(IARequired.NCDomProd)
End Sub

Private Sub IABusinessNC_Calculation()
    ReturnVal = GetCurrency(IAWOthInc.TotNonConform)
End Sub

Private Sub IAEic_Calculation()
    If GetBool(IAF126.TpPYNR) = True Or GetBool(IAF126.SpPYNR) Then
        ReturnVal = GetCurrency(IARequired.PYNREIC)
    Else
        ReturnVal = GetCurrency(IARequired.FYEIC)
    End If
End Sub

Private Sub JointDiv_Calculation()
    Dim count As Integer
    Dim SchBTotal As Currency

    count = 0
    SchBTotal = 0

    Do While count < 7
        If GetBool(IASchB.DJ1(count)) = True Then
            SchBTotal = SchBTotal + GetCurrency(IASchB.TaxDiv(count))
        Else
            SchBTotal = SchBTotal
        End If
        count = count + 1
    Loop

    Dim count1 As Integer
    Dim HowManyWBPDiv As Long
    Dim WSTotal As Currency
    Dim DivIndex As Long
    
    count1 = 1
    HowManyWBPDiv = GetAllCopies(IAWBPDiv)
    WSTotal = 0
    
    Do While count1 <= HowManyWBPDiv
        DivIndex = 0
        Do While DivIndex < 22
            If GetBool(IAWBPDiv.DJ1(DivIndex), count1) = True Then
                WSTotal = WSTotal + GetCurrency(IAWBPDiv.TaxDiv(DivIndex), count1)
            End If
            DivIndex = DivIndex + 1
        Loop
        count1 = count1 + 1
    Loop
    
    ReturnVal = SchBTotal + WSTotal
End Sub

Private Sub JointInt_Calculation()
    Dim count As Integer
    Dim SchBTotal As Currency

    count = 0
    SchBTotal = 0

    Do While count < 7
        If GetBool(IASchB.IJ1(count)) = True Then
            SchBTotal = SchBTotal + GetCurrency(IASchB.TaxInt(count))
        Else
            SchBTotal = SchBTotal
        End If
        count = count + 1
    Loop

    Dim count1 As Integer
    Dim HowManyWBPInt As Long
    Dim WSTotal As Currency
    Dim IntIndex As Long
    
    count1 = 1
    HowManyWBPInt = GetAllCopies(IAWBPInt)
    WSTotal = 0
    
    Do While count1 <= HowManyWBPInt
        IntIndex = 0
        Do While IntIndex < 22
            If GetBool(IAWBPInt.IJ1(IntIndex), count1) = True Then
                WSTotal = WSTotal + GetCurrency(IAWBPInt.TaxInt(IntIndex), count1)
            End If
            IntIndex = IntIndex + 1
        Loop
        count1 = count1 + 1
    Loop
    
    ReturnVal = SchBTotal + WSTotal
End Sub

Private Sub JointSPDiv_Calculation()
    ReturnVal = Round(CDollar(CDbl(GetCurrency(IARequired.JointDiv)) * 0.5))
End Sub

Private Sub JointSPInt_Calculation()
    ReturnVal = Round(CDollar(CDbl(GetCurrency(IARequired.JointInt)) * 0.5))
End Sub

Private Sub JointTPDiv_Calculation()
    ReturnVal = GetCurrency(IARequired.JointDiv) - GetCurrency(IARequired.JointSPDiv)
End Sub

Private Sub JointTPInt_Calculation()
    ReturnVal = GetCurrency(IARequired.JointInt) - GetCurrency(IARequired.JointSPInt)
End Sub

Private Sub JTComb_Calculation()
    If GetString(IAF1040.LastName) = GetString(IAF1040.SpouseLast) Then
        ReturnVal = GetString(IAF1040.LastName) & ", " & GetString(IAF1040.FirstName) & " and " & GetString(IAF1040.SpouseFirst)
    Else
        ReturnVal = GetString(IAF1040.LastName) & ", " & GetString(IAF1040.FirstName) & " and " & GetString(IAF1040.SpouseLast) & ", " & GetString(IAF1040.SpouseFirst)
    End If
End Sub

Private Sub LILimit_Calculation()
    If IAFS() = 1 And GetBool(IAF1040.DepY) = True Then
        ReturnVal = 5000@
    ElseIf IAFS() = 1 And GetBool(IAF1040.DepY) = False And GetBool(IAF1040.Over65) = True Then
        ReturnVal = 24001@
    ElseIf IAFS() = 1 And GetBool(IAF1040.DepY) = False Then
        ReturnVal = 9001@
    ElseIf IAFS() = 1 Or GetBool(IAF1040.DepY) = True Then
        ReturnVal = 0@
    ElseIf GetBool(IAF1040.Over65) = True Then
        ReturnVal = 32001@
    Else
        ReturnVal = 13501@
    End If
End Sub

Private Sub Limit179_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IARequired.Max179) - GetCurrency(IARequired.Reduction179))
End Sub

Private Sub LITotIncome_Calculation()
    ReturnVal = GetCurrency(IAWkAltTax.Ln26)
End Sub

Private Sub LowInc_Calculation()
    If GetCurrency(USF4972.Tax) + GetCurrency(USF4972Spouse.Tax) > 0 Then
        ReturnVal = 0
    ElseIf GetCurrency(IAF1040.AIAMin) > 0 Or GetCurrency(IAF1040.BIAMin) > 0 Then
        ReturnVal = 0
    ElseIf GetBool(IAF126.TpPYNR) = True Or GetBool(IAF126.SpPYNR) = True Then
        ReturnVal = 0
    ElseIf GetBool(IARequired.AskFilStat) = True And GetBool(IAWkAltTax.NOL) = True Then
        ReturnVal = 0
    ElseIf GetCurrency(IARequired.LITotIncome) < GetCurrency(IARequired.LILimit) Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Max179_Calculation()
    ReturnVal = 70000@
End Sub

Private Sub MobDisQual_Calculation()
    ReturnVal = 0
End Sub

Private Sub ModAmt_Calculation()
    Dim TP As Currency
    Dim SP As Currency
    
    TP = GetCurrency(IAF1040.ATotAdj) - GetCurrency(IAF1040.AFedTax) + GetCurrency(IAF1040.AFedDed) + GetCurrency(IAF1040.ADedBox)
    SP = GetCurrency(IAF1040.BTotAdj) - GetCurrency(IAF1040.BFedTax) + GetCurrency(IAF1040.BFedDed) + GetCurrency(IAF1040.BDedBox)
    
    ReturnVal = TP + SP
End Sub

Private Sub ModChg_Calculation()
    ReturnVal = Abs(GetCurrency(IARequired.TotIncChg) - GetCurrency(IAF1040.AAltTax))
End Sub

Private Sub ModCk_Calculation()
    Dim Tax As Currency
    Dim Modifications As Currency
    
    Tax = GetCurrency(IAF1040.AAltTax)
    
    Modifications = GetCurrency(IARequired.TotIncChg) - Tax
    
    If Modifications > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.CombNames)
End Sub

Private Sub NCDomProd_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAOthAdj.TPDomProd) + GetCurrency(IAOthAdj.SPDomProd) - GetCurrency(USF8903.DPADeduction))
End Sub

Private Sub NCMove_Calculation()
    ReturnVal = GetCurrency(IA3903.MovExpDdn)
End Sub

Private Sub NonConfLn14_Calculation()
    ReturnVal = GetCurrency(IAWOthInc.TotNonConform)
End Sub

Private Sub NonCredAmt_Calculation()
    Dim TP As Currency
    Dim SP As Currency
    
    TP = GetCurrency(IAF1040.ACredits) + GetCurrency(IAF1040.ACrNon) + GetCurrency(IAF1040.AOutState) + GetCurrency(IAF1040.AOthIACr)
    SP = GetCurrency(IAF1040.BCredits) + GetCurrency(IAF1040.BCrNon) + GetCurrency(IAF1040.BOutState) + GetCurrency(IAF1040.BOthIACr)
    
    ReturnVal = TP + SP
End Sub

Private Sub NonCredChg_Calculation()
    ReturnVal = GetCurrency(IARequired.NonCredAmt)
End Sub

Private Sub NonCredCk_Calculation()
    If GetCurrency(IARequired.NonCredChg) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub OthTaxAmt_Calculation()
    Dim TP As Currency
    Dim SP As Currency
    
    TP = GetCurrency(IAF1040.ALump) + GetCurrency(IAF1040.AIAMin) + GetCurrency(IAF1040.ASch)
    TP = GetCurrency(IAF1040.BLump) + GetCurrency(IAF1040.BIAMin) + GetCurrency(IAF1040.BSch)
    
    ReturnVal = TP + SP + GetCurrency(IAF1040.TotContrib)
End Sub

Private Sub OthTaxChg_Calculation()
    ReturnVal = GetCurrency(IARequired.OthTaxAmt)
End Sub

Private Sub OthTaxCk_Calculation()
    If GetCurrency(IARequired.OthTaxChg) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PayAmt_Calculation()
    ReturnVal = GetCurrency(IAF1040.TotCredit)
End Sub

Private Sub PayChg_Calculation()
    ReturnVal = GetCurrency(IARequired.PayAmt)
End Sub

Private Sub PayCk_Calculation()
    If GetCurrency(IARequired.PayChg) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PenDonAmt_Calculation()
    ReturnVal = GetCurrency(IAF1040.BApply99) + GetCurrency(IAF1040.AApply99) + GetCurrency(IAF1040.Penalty) + GetCurrency(IAF1040.PenInt)
End Sub

Private Sub PenDonChg_Calculation()
    ReturnVal = GetCurrency(IARequired.PenDonAmt)
End Sub

Private Sub PenDonCk_Calculation()
    If GetCurrency(IARequired.PenDonChg) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PrnSchCode_Calculation()
    If GetString(IAF1040.SchNo) = "00811" Then
        ReturnVal = "0081"
    ElseIf GetString(IAF1040.SchNo) = "44911" Then
        ReturnVal = "4491"
    ElseIf GetString(IAF1040.SchNo) = "45181" Then
        ReturnVal = "4518"
    ElseIf GetString(IAF1040.SchNo) = "58951" Then
        ReturnVal = "5895"
    Else
        ReturnVal = GetString(IAF1040.SchNo)
    End If
End Sub

Private Sub PrnSurvivorSP_Calculation()
    If GetString(USWTaxpayer.PrnSurvivorSP) = "File as Surviving Sp." Then
        ReturnVal = GetString(USWTaxpayer.PrnSurvivorSP) + " " + GetString(USWBasicInfo.YouDeath)
    Else
        ReturnVal = GetString(USWTaxpayer.PrnSurvivorSP)
    End If
End Sub

Private Sub PrnSurvivorTP_Calculation()
    If GetString(USWTaxpayer.PrnSurvivorTP) = "File as Surviving Sp." Then
        ReturnVal = GetString(USWTaxpayer.PrnSurvivorTP)
    Else
        ReturnVal = GetString(USWTaxpayer.PrnSurvivorTP)
    End If
End Sub

Private Sub PYNetInc_Calculation()
    ReturnVal = GetCurrency(IARequired.PYNetIncA) + GetCurrency(IARequired.PYNetIncB)
End Sub

Private Sub PYNetIncA_Calculation()
    ReturnVal = GetCurrency(USZIA1040.IAPYNetIncA)
End Sub

Private Sub PYNetIncB_Calculation()
    ReturnVal = GetCurrency(USZIA1040.IAPYNetIncB)
End Sub

Private Sub PYNREIC_Calculation()
    ReturnVal = MinValue(GetCurrency(IARequired.FYEIC), (CDollar(GetFloat(IARequired.FYEIC) * GetFloat(IAChildCredit.PYNRPercent))))
End Sub

Private Sub PYRatio_Calculation()
    If GetBool(IARequired.AskSpouse) = False Then
        ReturnVal = 0
    ElseIf GetCurrency(IARequired.PYNetIncB) < 0 And GetCurrency(IARequired.PYNetIncA) < 0 Then
        If GetCurrency(IARequired.PYNetIncB) < GetCurrency(IARequired.PYNetIncA) Then
            ReturnVal = 0
        Else
            ReturnVal = 1
        End If
    ElseIf GetCurrency(IARequired.PYNetIncB) < 0 Then
        ReturnVal = 0
    ElseIf GetCurrency(IARequired.PYNetIncB) > 0 And GetCurrency(IARequired.PYNetInc) <= 0 Then
        ReturnVal = 1
    ElseIf GetCurrency(IARequired.PYNetInc) = 0 Then
        ReturnVal = 0
    Else
        ReturnVal = MaxValue(0, (MinValue(1#, GetFloat(IARequired.PYNetIncB) / GetFloat(IARequired.PYNetInc))))
    End If
End Sub

Private Sub QnACompMob_Calculation()
    If GetBool(IARequired.QnAComp) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub QSAmtOwe_Calculation()
    If GetCurrency(IAF1040.RefBalDue) < 0 Then
        ReturnVal = Abs(GetCurrency(IAF1040.RefBalDue))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub QSRefund_Calculation()
    If GetCurrency(IAF1040.RefBalDue) > 0 Then
        ReturnVal = GetCurrency(IAF1040.RefBalDue)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Reduction179_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IARequired.TotCost179) - GetCurrency(IARequired.Threshold179))
End Sub

Private Sub RefundAmt_Calculation()
    ReturnVal = GetCurrency(IAF1040.RefBalDue)
End Sub

Private Sub RefundCk_Calculation()
    If GetCurrency(IARequired.RefundAmt) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub S1099RWH_Calculation()
    Dim count1 As Integer
    Dim HowMany1099R As Long
    Dim Total1 As Currency
    
    count1 = 1
    HowMany1099R = GetAllCopies(USD1099R)
    Total1 = 0
    
    Do While count1 <= HowMany1099R
        If GetString(USD1099R.St1, count1) = "IA" And GetBool(USD1099R.Spouse, count1) = True Then
            Total1 = Total1 + GetCurrency(USD1099R.StWh1, count1)
        End If
        
        If GetString(USD1099R.St2, count1) = "IA" And GetBool(USD1099R.Spouse, count1) = True Then
            Total1 = Total1 + GetCurrency(USD1099R.STWh2, count1)
        End If
        
        count1 = count1 + 1
    Loop
    
    ReturnVal = Round(Total1)

End Sub

Private Sub SchADeprAmt_Calculation()
'believe situation now is that parent A is gone, should only have this situation now when fed 2106 is for a "Disabled" (which goes to Sch A for fed and IA) and have either 4562 or 2106veh depr. All other 2106 depr is either only claimed on IA subject to 2% (no adjustment needed since nothing on fed) or claimed on fed (fed .Quaifies) as an adjustment to AGI and then we will properly account for this on IA4562A
    Dim count As Long
    Dim count3 As Long
    Dim Total1 As Currency
    Dim Total3 As Currency
    Dim HowManyIAWDepr As Long
    Dim HowManyIA4562A As Long
    
    count = 1
    count3 = 1
    Total1 = 0
    Total3 = 0
    HowManyIAWDepr = GetAllCopies(IAWDepr)
    HowManyIA4562A = GetAllCopies(IA4562A)
    
    Do While count <= HowManyIAWDepr
        If GetString(IAWDepr.ParentType, count) = "2106" And GetBool(IAWDepr.Qualifies, count) = True Then
            Total1 = Total1 + GetCurrency(IAWDepr.TotAdj, count)
        End If
        
        count = count + 1
    Loop
    
    Do While count3 <= HowManyIA4562A
        If GetString(IA4562A.EmpBusType, count3) = "27" Then
            Total3 = Total3 + GetCurrency(IA4562A.DepAdj, count3)
        End If
        
        count3 = count3 + 1
    Loop
    
    ReturnVal = Total1 + Total3
    
End Sub

Private Sub SchBDivNoPayer_Calculation()
    Dim count, Iter As Integer
    
    count = 0
    Iter = 0
    Do While Iter < 7
        If GetCurrency(IASchB.Dividend(Iter)) > 0 And Trim(GetString(IASchB.DivPayer(Iter))) = "" Then
            count = count + 1
        End If
        Iter = Iter + 1
    Loop
    
    If GetBool(IASchB.PrintIAB) = True And count > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SchBIntNoPayer_Calculation()
    Dim count, Iter As Integer
    
    count = 0
    Iter = 0
    Do While Iter < 7
        If GetCurrency(IASchB.Interest(Iter)) > 0 And Trim(GetString(IASchB.Payer(Iter))) = "" Then
            count = count + 1
        End If
        Iter = Iter + 1
    Loop
    
    If GetBool(IASchB.PrintIAB) = True And count > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SEarnInc_Calculation()
    Dim Part As Currency
    Dim SE As Currency
    Dim Wages As Currency
    Dim NonTaxCombat As Currency
    Dim SP409AInc As Currency
    Dim JtSP409AInc As Currency
         
    Part = GetCurrency(USDPartK1.SEInc, FieldCopies(USDPartK1.Spouse)) + CDollar(GetFloat(USDPartK1.SEInc, FieldCopies(USDPartK1.Joint)) * 0.5)
    SE = GetCurrency(IAF1040.BBusInc) + GetCurrency(IAF1040.BFarm) - GetCurrency(IAF1040.BBusIncL) - GetCurrency(USWRec.SKeough)
    Wages = MaxValue(0, GetCurrency(IAF1040.BWages) - GetCurrency(USDStudent.TaxScholar, FieldCopies(USDStudent.Spouse)) - Round(GetCurrency(USDW2.NonQual, FieldCopies(USDW2.Spouse))) - Round(GetCurrency(USDW2AS.NonQual, FieldCopies(USDW2AS.Spouse))) - Round(GetCurrency(USDW2CM.NonQual, FieldCopies(USDW2CM.Spouse))) - Round(GetCurrency(USDW2GU.NonQual, FieldCopies(USDW2GU.Spouse))) - Round(GetCurrency(USDW2VI.NonQual, FieldCopies(USDW2VI.Spouse))))
    NonTaxCombat = Round(GetCurrency(USDW2.CodeQ, FieldCopies(USDW2.Spouse))) + Round(GetCurrency(USDW2AS.CodeQ, FieldCopies(USDW2AS.Spouse))) + Round(GetCurrency(USDW2CM.CodeQ, FieldCopies(USDW2CM.Spouse))) + Round(GetCurrency(USDW2GU.CodeQ, FieldCopies(USDW2GU.Spouse))) + Round(GetCurrency(USDW2VI.CodeQ, FieldCopies(USDW2VI.Spouse)))
    SP409AInc = Round(GetCurrency(USDW2.CodeZ, FieldCopies(USDW2.Spouse))) + Round(GetCurrency(USDW2AS.CodeZ, FieldCopies(USDW2AS.Spouse))) + Round(GetCurrency(USDW2CM.CodeZ, FieldCopies(USDW2CM.Spouse))) + Round(GetCurrency(USDW2GU.CodeZ, FieldCopies(USDW2GU.Spouse))) + Round(GetCurrency(USDW2VI.CodeZ, FieldCopies(USDW2VI.Spouse))) + Round(GetCurrency(USD1099MISC.Income, FieldCopies(USD1099MISC.Spouse)))
    JtSP409AInc = Round(CDollar(GetFloat(USD1099MISC.Income, FieldCopies(USD1099MISC.Joint)) * 0.5))
     
    ReturnVal = MaxValue(0, Wages + GetCurrency(IAF1040.BAlimony) + MaxValue(0, SE + Part) + GetCurrency(USWOthInc.SP2555) + NonTaxCombat - SP409AInc - JtSP409AInc)
End Sub

Private Sub SEICEarnInc_Calculation()
    If GetBool(IAF1040.MFS) = True Then
        ReturnVal = GetCurrency(IAF1040.MFSEI)
    Else
        ReturnVal = GetCurrency(IAF1040.BWages) + GetCurrency(IAF1040.BBusInc) + GetCurrency(IAF1040.BFarm)
    End If
End Sub

Private Sub ShowRef_Calculation()
    If GetCurrency(IARequired.QSAmtOwe) > 0 Then
        ReturnVal = 0
    Else
        ReturnVal = 1
    End If
End Sub

Private Sub SIaEIC_Calculation()
    ReturnVal = CDollar(GetFloat(IARequired.IAEic) * GetFloat(IARequired.EICRatio))
End Sub

Private Sub SIAExReimb_Calculation()
    ReturnVal = GetCurrency(IARequired.TotIAExReimb) - GetCurrency(IARequired.TIAExReimb)
End Sub

Private Sub SIAW2WH_Calculation()
    Dim count1 As Integer
    Dim HowManyW2 As Long
    Dim Total1 As Currency
    Dim W2Index As Long
    
    count1 = 1
    HowManyW2 = GetAllCopies(USDW2)
    Total1 = 0
    
    Do While count1 <= HowManyW2
        W2Index = 0
        Do While W2Index < 8
            If GetString(USDW2.St(W2Index), count1) = "IA" And GetBool(USDW2.Spouse, count1) = True Then
                Total1 = Total1 + GetCurrency(USDW2.STWh(W2Index), count1)
            End If
            W2Index = W2Index + 1
        Loop
        count1 = count1 + 1
    Loop
    
    ReturnVal = Round(Total1)
    
End Sub

Private Sub SIRA_Calculation()
    If IAFS() = 3 Then
        If GetCurrency(IARequired.TEarnInc) < GetCurrency(USWIRA.TPDedIRA) Then
            ReturnVal = GetCurrency(USWIRA.TPDedIRA) + GetCurrency(USWIRA.SPDedIRA) - GetCurrency(IARequired.TEarnInc)
        Else
            ReturnVal = MinValue(GetCurrency(IARequired.SEarnInc), GetCurrency(USWIRA.SPDedIRA))
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AskSpouse_Calculation()
    If IAFS() = 2 Or IAFS() = 3 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SLimLoss_Calculation()
    ReturnVal = GetCurrency(USWDRec.LimLoss) - GetCurrency(IARequired.TLimLoss)
End Sub

Private Sub SMove_Calculation()
    ReturnVal = GetCurrency(IARequired.TotMove) - GetCurrency(IARequired.TMove)
End Sub

Private Sub SP8824_Calculation()
    ReturnVal = GetCurrency(IARequired.Tot8824) - GetCurrency(IARequired.TP8824)
End Sub

Private Sub SPCapGainWH_Calculation()
    Dim count1 As Integer
    Dim HowManyCapGain As Long
    Dim Total1 As Currency
    Dim CGIndex As Long
    
    count1 = 1
    HowManyCapGain = GetAllCopies(USDCapGain)
    Total1 = 0
    
    Do While count1 <= HowManyCapGain
        CGIndex = 0
        Do While CGIndex < 2
            If GetString(USDCapGain.St2(CGIndex), count1) = "IA" And GetBool(USDCapGain.Spouse, count1) = True Then
                Total1 = Total1 + GetCurrency(USDCapGain.STWh2(CGIndex), count1)
            ElseIf GetString(USDCapGain.St2(CGIndex), count1) = "IA" And GetBool(USDCapGain.Joint, count1) = True Then
                Total1 = Total1 + CDollar(GetFloat(USDCapGain.STWh2(CGIndex), count1) * 0.5)
            End If
            CGIndex = CGIndex + 1
        Loop
        count1 = count1 + 1
    Loop
    
    ReturnVal = Round(Total1)  
End Sub

Private Sub SPComb_Calculation()
    If GetBool(IAF1040.MFJ) = True Or GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetString(IAF1040.SpouseLast) & ", " & GetString(IAF1040.SpouseFirst)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub SPCombName_Calculation()
    If GetBool(IAF1040.MFJ) = True Or GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetString(IAF1040.SpouseFirst) & " " & GetString(IAF1040.SpouseLast)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub SPDivWH_Calculation()
    Dim count1 As Integer
    Dim HowMany1099Div As Long
    Dim Total1 As Currency
    Dim DivIndex As Long
    
    count1 = 1
    HowMany1099Div = GetAllCopies(USD1099DIV)
    Total1 = 0
    
    Do While count1 <= HowMany1099Div
        DivIndex = 0
        Do While DivIndex < 2
            If GetString(USD1099DIV.St(DivIndex), count1) = "IA" And GetBool(USD1099DIV.Spouse, count1) = True Then
                Total1 = Total1 + GetCurrency(USD1099DIV.STWh(DivIndex), count1)
            ElseIf GetString(USD1099DIV.St(DivIndex), count1) = "IA" And GetBool(USD1099DIV.Joint, count1) = True Then
                Total1 = Total1 + CDollar(GetFloat(USD1099DIV.STWh(DivIndex), count1) * 0.5)
            End If
            DivIndex = DivIndex + 1
        Loop
        count1 = count1 + 1
    Loop
    
    ReturnVal = Round(Total1)
End Sub

Private Sub SPIntWH_Calculation()
    Dim count1 As Integer
    Dim HowMany1099Int As Long
    Dim Total1 As Currency
    Dim IntIndex As Long
    
    count1 = 1
    HowMany1099Int = GetAllCopies(USD1099INT)
    Total1 = 0
    
    Do While count1 <= HowMany1099Int
        IntIndex = 0
        Do While IntIndex < 2
            If GetString(USD1099INT.St(IntIndex), count1) = "IA" And GetBool(USD1099INT.Spouse, count1) = True Then
                Total1 = Total1 + GetCurrency(USD1099INT.STWh(IntIndex), count1)
            ElseIf GetString(USD1099INT.St(IntIndex), count1) = "IA" And GetBool(USD1099INT.Joint, count1) = True Then
                Total1 = Total1 + CDollar(GetFloat(USD1099INT.STWh(IntIndex), count1) * 0.5)
            End If
            IntIndex = IntIndex + 1
        Loop
        count1 = count1 + 1
    Loop
    
    ReturnVal = Round(Total1)
End Sub

Private Sub SPKWH_Calculation()
    Dim count1 As Integer
    Dim HowMany1099K As Long
    Dim Total1 As Currency
    Dim KIndex As Long
    
    count1 = 1
    HowMany1099K = GetAllCopies(USD1099K)
    Total1 = 0
    
    Do While count1 <= HowMany1099K
        KIndex = 0
        Do While KIndex < 2
            If GetString(USD1099K.State(KIndex), count1) = "IA" And GetBool(USD1099K.Spouse, count1) = True Then
                Total1 = Total1 + GetCurrency(USD1099K.StateInc(KIndex), count1)
            ElseIf GetString(USD1099K.State(KIndex), count1) = "IA" And GetBool(USD1099K.Joint, count1) = True Then
                Total1 = Total1 + CDollar(GetFloat(USD1099K.StateInc(KIndex), count1) * 0.5)
            End If
            KIndex = KIndex + 1
        Loop
        count1 = count1 + 1
    Loop
    
    ReturnVal = Round(Total1)
End Sub

Private Sub SPMiscWH_Calculation()
    Dim count1 As Integer
    Dim HowMany1099MISC As Long
    Dim Total1 As Currency
    
    count1 = 1
    HowMany1099MISC = GetAllCopies(USD1099MISC)
    Total1 = 0
    
    Do While count1 <= HowMany1099MISC
        If GetString(USD1099MISC.State, count1) = "IA" Then
            If GetBool(USD1099MISC.Spouse, count1) = True Then
                Total1 = Total1 + GetCurrency(USD1099MISC.StateWH, count1)
            ElseIf GetBool(USD1099MISC.Joint, count1) = True Then
                Total1 = Total1 + CDollar(GetFloat(USD1099MISC.StateWH, count1) * 0.5)
            Else
                Total1 = Total1
            End If
        Else
            Total1 = Total1
        End If
        
        If GetString(USD1099MISC.State2, count1) = "IA" Then
            If GetBool(USD1099MISC.Spouse, count1) = True Then
                Total1 = Total1 + GetCurrency(USD1099MISC.StateWH2, count1)
            ElseIf GetBool(USD1099MISC.Joint, count1) = True Then
                Total1 = Total1 + CDollar(GetFloat(USD1099MISC.StateWH2, count1) * 0.5)
            Else
                Total1 = Total1
            End If
        Else
            Total1 = Total1
        End If
        
        count1 = count1 + 1
    Loop
    
    ReturnVal = Round(Total1)

End Sub

Private Sub SPOIDWH_Calculation()
    Dim count1 As Integer
    Dim HowMany1099OID As Long
    Dim Total1 As Currency
    Dim OIDIndex As Long
    
    count1 = 1
    HowMany1099OID = GetAllCopies(USD1099OID)
    Total1 = 0
    
    Do While count1 <= HowMany1099OID
        OIDIndex = 0
        Do While OIDIndex < 2
            If GetString(USD1099OID.St(OIDIndex), count1) = "IA" And GetBool(USD1099OID.Spouse, count1) = True Then
                Total1 = Total1 + GetCurrency(USD1099OID.STWh(OIDIndex), count1)
            ElseIf GetString(USD1099OID.St(OIDIndex), count1) = "IA" And GetBool(USD1099OID.Joint, count1) = True Then
                Total1 = Total1 + CDollar(GetFloat(USD1099OID.STWh(OIDIndex), count1) * 0.5)
            End If
            OIDIndex = OIDIndex + 1
        Loop
        count1 = count1 + 1
    Loop
    
    ReturnVal = Round(Total1)
End Sub

Private Sub SPOthIncWH_Calculation()

    ReturnVal = 0
    
End Sub

Private Sub SPTotIncChg_Calculation()
' updated for 2018

    Dim Mid As Currency
    Dim MidInt As Long
    Dim TotTaxInc As Currency
    
    TotTaxInc = GetCurrency(IAF1040.BGross)
    
    If TotTaxInc > 95650@ Then
        Mid = TotTaxInc
    ElseIf TotTaxInc > 150@ Then
        MidInt = CLng((TotTaxInc - 1@) / 50@)
        Mid = (CCur(MidInt) * 50@) + 25@
    Else
        Mid = 0@
    End If
    
    ReturnVal = Tax(Mid)
End Sub

Private Sub SPUnemWH_Calculation()
    Dim count1 As Integer
    Dim HowManyUnempl As Long
    Dim Total1 As Currency
    Dim UnIndex As Long
    
    count1 = 1
    HowManyUnempl = GetAllCopies(USWUnempl)
    Total1 = 0
    
    Do While count1 <= HowManyUnempl
        UnIndex = 0
        Do While UnIndex < 2
            If GetString(USWUnempl.TPState(UnIndex), count1) = "IA" And GetBool(USWUnempl.Spouse, count1) = True Then
                Total1 = Total1 + GetCurrency(USWUnempl.TPStWH(UnIndex), count1)
            End If
            UnIndex = UnIndex + 1
        Loop
        count1 = count1 + 1
    Loop
    
    ReturnVal = Round(Total1)    

End Sub

Private Sub SPW2GWH_Calculation()
    Dim count1 As Integer
    Dim HowManyW2G As Long
    Dim Total1 As Currency
    
    count1 = 1
    HowManyW2G = GetAllCopies(USDW2G)
    Total1 = 0
    
    Do While count1 <= HowManyW2G
        If GetString(USDW2G.StateWon, count1) = "IA" And GetBool(USDW2G.Spouse, count1) = True Then
            Total1 = Total1 + GetCurrency(USDW2G.StateWH, count1)
        End If
        
        count1 = count1 + 1
    Loop
    
    ReturnVal = Round(Total1)

End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

Private Sub SummaryScript_Calculation()
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub T1099rWH_Calculation()
    ReturnVal = GetCurrency(IARequired.Tot1099rWH) - GetCurrency(IARequired.S1099RWH)
End Sub

Private Sub TaxReduction_Calculation()
    ReturnVal = MinValue(GetCurrency(IARequired.TentTaxRed), GetCurrency(IARequired.TentTax))
End Sub

Private Sub TEarnInc_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(USWIRATrad.EarnInc) - GetCurrency(IARequired.SEarnInc))
End Sub

Private Sub Tent179_Calculation()
    ReturnVal = MinValue(GetCurrency(IARequired.TotElect179), GetCurrency(IARequired.Limit179))
End Sub

Private Sub TentTax_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAF1040.ATotIATax) - GetCurrency(IAF1040.ACredits))
End Sub

Private Sub TentTaxRed_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IARequired.TotNIPenExc) - GetCurrency(IARequired.BaseAmt))
End Sub

Private Sub Threshold179_Calculation()
    ReturnVal = 280000@
End Sub

Private Sub TIAEic_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IARequired.IAEic) - GetCurrency(IARequired.SIaEIC))
End Sub

Private Sub TIAExReimb_Calculation()
    ReturnVal = GetCurrency(IA3903.IAExReimb, FieldCopies(IA3903.Taxpayer)) + CDollar(GetFloat(IA3903.IAExReimb, FieldCopies(IA3903.Joint)) * 0.5)
End Sub

Private Sub TIAW2WH_Calculation()
    ReturnVal = GetCurrency(IARequired.TotIAW2WH) - GetCurrency(IARequired.SIAW2WH)
End Sub

Private Sub TIRA_Calculation()
    ReturnVal = GetCurrency(IARequired.TotIRA) - GetCurrency(IARequired.SIRA)
End Sub

Private Sub TLimLoss_Calculation()
    If GetCurrency(USWDRec.CapGain) < 0 Then
        If GetCurrency(USWDRec.TCapGain) < 0 And GetCurrency(USWDRec.SCapGain) < 0 And IAFS() = 3 Then
            If GetCurrency(USWDRec.SCapGain) < -1500@ Then
                ReturnVal = MaxValue(GetCurrency(USWDRec.TCapGain), -1500@)
            Else
                ReturnVal = GetCurrency(USWDRec.LimLoss) - GetCurrency(USWDRec.SCapGain)
            End If
        ElseIf GetCurrency(USWDRec.TCapGain) < 0 Then
            ReturnVal = GetCurrency(USWDRec.LimLoss)
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TMove_Calculation()
    Dim FedMove As Currency
    Dim StateMove As Currency
    
    FedMove = GetCurrency(USWRec.TMove)
    StateMove = Round(GetCurrency(IA3903.MovExpDdn, FieldCopies(IA3903.Taxpayer)) + CDollar(GetFloat(IA3903.MovExpDdn, FieldCopies(IA3903.Joint)) * 0.5))

    ReturnVal = FedMove + StateMove
End Sub

Private Sub Tot1042S_Calculation()
    Dim count1 As Integer
    Dim HowMany1042S As Long
    Dim Total1 As Currency
    Dim F1042SIndex As Long
    
    count1 = 1
    HowMany1042S = GetAllCopies(USD1042S)
    Total1 = 0
    
    Do While count1 <= HowMany1042S
        F1042SIndex = 0
        Do While F1042SIndex < 4
            If GetString(USD1042S.St(F1042SIndex), count1) = "IA" Then
                Total1 = Total1 + GetCurrency(USD1042S.StWh(F1042SIndex), count1)
            End If
            F1042SIndex = F1042SIndex + 1
        Loop
        count1 = count1 + 1
    Loop
    
    ReturnVal = Round(Total1)
End Sub

Private Sub Tot1099rWH_Calculation()
    Dim count1 As Integer
    Dim HowMany1099R As Long
    Dim Total1 As Currency
    
    count1 = 1
    HowMany1099R = GetAllCopies(USD1099R)
    Total1 = 0
    
    Do While count1 <= HowMany1099R
        If GetString(USD1099R.St1, count1) = "IA" Then
            Total1 = Total1 + GetCurrency(USD1099R.StWh1, count1)
        End If
        
        If GetString(USD1099R.St2, count1) = "IA" Then
            Total1 = Total1 + GetCurrency(USD1099R.STWh2, count1)
        End If
        
        count1 = count1 + 1
    Loop
    
    ReturnVal = Round(Total1)

End Sub

Private Sub Tot8824_Calculation()
    ReturnVal = GetCurrency(IA8824.IANonConformAdj)
End Sub

Private Sub TotApplied_Calculation()
    ReturnVal = GetCurrency(IAF1040.AApply99) + GetCurrency(IAF1040.BApply99)
End Sub

Private Sub TotCapGainWH_Calculation()
    Dim count1 As Integer
    Dim HowManyCapGain As Long
    Dim Total1 As Currency
    Dim CGIndex As Long
    
    count1 = 1
    HowManyCapGain = GetAllCopies(USDCapGain)
    Total1 = 0
    
    Do While count1 <= HowManyCapGain
        CGIndex = 0
        Do While CGIndex < 2
            If GetString(USDCapGain.St2(CGIndex), count1) = "IA" Then
                Total1 = Total1 + GetCurrency(USDCapGain.STWh2(CGIndex), count1)
            End If
            CGIndex = CGIndex + 1
        Loop
        count1 = count1 + 1
    Loop
    
    ReturnVal = Round(Total1)
End Sub

Private Sub TotCo179_Calculation()
    ReturnVal = 0
End Sub

Private Sub TotCost179_Calculation()
'per 2016 Section 179 Expensing FAQs under section III for pass through entities #4 example shows that the cost of section 179 property passed through for federal should not pass through to the partner for purposes of the Iowa section 179 phase-out limits, remove + GetCurrency(USDPartK1.Sec179) + GetCurrency(USDSCorpK1.Sec179) from reproduced fed calc below.
    ReturnVal = GetCurrency(USWDepr.Sec179Basis) + GetCurrency(USWDepr.List179basis) + GetCurrency(USF4562.Sec179Basis2106, 1)
End Sub

Private Sub TotCYIAEst_Calculation()
    Dim TP As Currency
    Dim SP As Currency
                
    If GetDate(IAStateEst.TPStQ4Date) < MakeDate(1, 1, YearNumber + 1) Then
        TP = GetCurrency(IAStateEst.TPStApply) + GetCurrency(IAStateEst.TPStQ1) + GetCurrency(IAStateEst.TPStQ2) + GetCurrency(IAStateEst.TPStQ3) + GetCurrency(IAStateEst.TPStQ4)
    Else
        TP = GetCurrency(IAStateEst.TPStApply) + GetCurrency(IAStateEst.TPStQ1) + GetCurrency(IAStateEst.TPStQ2) + GetCurrency(IAStateEst.TPStQ3)
    End If
    
    If GetDate(IAStateEst.SPStQ4Date) < MakeDate(1, 1, YearNumber + 1) Then
        SP = GetCurrency(IAStateEst.SPStApply) + GetCurrency(IAStateEst.SPStQ1) + GetCurrency(IAStateEst.SPStQ2) + GetCurrency(IAStateEst.SPStQ3) + GetCurrency(IAStateEst.SPStQ4)
    Else
        SP = GetCurrency(IAStateEst.SPStApply) + GetCurrency(IAStateEst.SPStQ1) + GetCurrency(IAStateEst.SPStQ2) + GetCurrency(IAStateEst.SPStQ3)
    End If
    
    If IAFS() = 3 Then
        ReturnVal = TP + SP
    Else
        ReturnVal = TP
    End If
End Sub

Private Sub TotCyLocEst_Calculation()
    Dim Local1 As Currency
    Dim Local2 As Currency
    Dim Local3 As Currency
    
    If GetString(USWEstPay.LocName1) = "OTHER" Then
        Local1 = GetCurrency(USWLocalEst.CYLocal, 1)
    Else
        Local1 = 0
    End If
    
    If GetString(USWEstPay.LocName2) = "OTHER" Then
        Local2 = GetCurrency(USWLocalEst.CYLocal, 2)
    Else
        Local2 = 0
    End If
    
    If GetString(USWEstPay.LocName3) = "OTHER" Then
        Local3 = GetCurrency(USWLocalEst.CYLocal, 3)
    Else
        Local3 = 0
    End If
    
    ReturnVal = Local1 + Local2 + Local3
End Sub

Private Sub TotDiv_Calculation()
    ReturnVal = GetCurrency(IASchB.TotalTaxDiv)
End Sub

Private Sub TotDivWH_Calculation()
    Dim count1 As Integer
    Dim HowMany1099Div As Long
    Dim Total1 As Currency
    Dim DivIndex As Long
    
    count1 = 1
    HowMany1099Div = GetAllCopies(USD1099DIV)
    Total1 = 0
    
    Do While count1 <= HowMany1099Div
        DivIndex = 0
        Do While DivIndex < 2
            If GetString(USD1099DIV.St(DivIndex), count1) = "IA" Then
                Total1 = Total1 + GetCurrency(USD1099DIV.STWh(DivIndex), count1)
            End If
            DivIndex = DivIndex + 1
        Loop
        count1 = count1 + 1
    Loop
    
    ReturnVal = Round(Total1)
End Sub

Private Sub TotEICEarnInc_Calculation()
    If GetBool(IAF1040.MFS) = True Then
        ReturnVal = GetCurrency(IAF1040.MFSEI) + GetCurrency(IAF1040.AWages) + GetCurrency(IAF1040.ABusInc) + GetCurrency(IAF1040.AFarm)
    Else
        ReturnVal = GetCurrency(IAF1040.BWages) + GetCurrency(IAF1040.BBusInc) + GetCurrency(IAF1040.BFarm) + GetCurrency(IAF1040.AWages) + GetCurrency(IAF1040.ABusInc) + GetCurrency(IAF1040.AFarm)
    End If
End Sub

Private Sub TotElect179_Calculation()
    ReturnVal = GetCurrency(USWDepr.IACYSec179Rep) + GetCurrency(USF4562.StateTotCySec1792106, 1) + GetCurrency(USWSummary179.StateK1)
End Sub

Private Sub TotIAExReimb_Calculation()
    ReturnVal = GetCurrency(IA3903.IAExReimb)
End Sub

Private Sub TotIAW2WH_Calculation()
    Dim count1 As Integer
    Dim HowManyW2 As Long
    Dim Total1 As Currency
    Dim W2Index As Long
    
    count1 = 1
    HowManyW2 = GetAllCopies(USDW2)
    Total1 = 0
    
    Do While count1 <= HowManyW2
        W2Index = 0
        Do While W2Index < 8
            If GetString(USDW2.St(W2Index), count1) = "IA" Then
                Total1 = Total1 + GetCurrency(USDW2.STWh(W2Index), count1)
            End If
            W2Index = W2Index + 1
        Loop
        count1 = count1 + 1
    Loop
    
    ReturnVal = Round(Total1)
    
End Sub

Private Sub TotIncAmt_Calculation()
    ReturnVal = GetCurrency(IAF1040.AGross) + GetCurrency(IAF1040.BGross)
End Sub

Private Sub TotIncChg_Calculation()
    ReturnVal = GetCurrency(IARequired.TPTotIncChg) + GetCurrency(IARequired.SPTotIncChg)
End Sub

Private Sub TotIncCk_Calculation()
    If GetCurrency(IARequired.TotIncChg) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TotInt_Calculation()
    ReturnVal = GetCurrency(IASchB.TotalTaxInt)
End Sub

Private Sub TotIntWH_Calculation()
    Dim count1 As Integer
    Dim HowMany1099Int As Long
    Dim Total1 As Currency
    Dim IntIndex As Long
    
    count1 = 1
    HowMany1099Int = GetAllCopies(USD1099INT)
    Total1 = 0
    
    Do While count1 <= HowMany1099Int
        IntIndex = 0
        Do While IntIndex < 2
            If GetString(USD1099INT.St(IntIndex), count1) = "IA" Then
                Total1 = Total1 + GetCurrency(USD1099INT.STWh(IntIndex), count1)
            End If
            IntIndex = IntIndex + 1
        Loop
        count1 = count1 + 1
    Loop
    
    ReturnVal = Round(Total1)
End Sub

Private Sub TotIRA_Calculation()
    ReturnVal = GetCurrency(USWRec.TotIRAAdj)
End Sub

Private Sub TotKWH_Calculation()
    Dim count1 As Integer
    Dim HowMany1099K As Long
    Dim Total1 As Currency
    Dim KIndex As Long
    
    count1 = 1
    HowMany1099K = GetAllCopies(USD1099K)
    Total1 = 0
    
    Do While count1 <= HowMany1099K
        KIndex = 0
        Do While KIndex < 2
            If GetString(USD1099K.State(KIndex), count1) = "IA" Then
                Total1 = Total1 + GetCurrency(USD1099K.StateInc(KIndex), count1)
            End If
            KIndex = KIndex + 1
        Loop
        count1 = count1 + 1
    Loop
    
    ReturnVal = Round(Total1)
End Sub

Private Sub TotMiscWH_Calculation()
    Dim count1 As Integer
    Dim HowMany1099MISC As Long
    Dim Total1 As Currency
    
    count1 = 1
    HowMany1099MISC = GetAllCopies(USD1099MISC)
    Total1 = 0
    
    Do While count1 <= HowMany1099MISC
        If GetString(USD1099MISC.State, count1) = "IA" Then
            Total1 = Total1 + GetCurrency(USD1099MISC.StateWH, count1)
        End If
        
        If GetString(USD1099MISC.State2, count1) = "IA" Then
            Total1 = Total1 + GetCurrency(USD1099MISC.StateWH2, count1)
        End If
        
        count1 = count1 + 1
    Loop
    
    ReturnVal = Round(Total1)   

End Sub

Private Sub TotMove_Calculation()
    ReturnVal = GetCurrency(USWRec.TotMove) + GetCurrency(IA3903.MovExpDdn)
End Sub

Private Sub TotNI_Calculation()
    ReturnVal = GetCurrency(IAF1040.ANet) + GetCurrency(IAF1040.BNet)
End Sub

Private Sub TotNIPenExc_Calculation()
    ReturnVal = GetCurrency(IAWkAltTax.Ln26)
End Sub

Private Sub TotOIDWH_Calculation()
    Dim count1 As Integer
    Dim HowMany1099OID As Long
    Dim Total1 As Currency
    Dim OIDIndex As Long
    
    count1 = 1
    HowMany1099OID = GetAllCopies(USD1099OID)
    Total1 = 0
    
    Do While count1 <= HowMany1099OID
        OIDIndex = 0
        Do While OIDIndex < 2
            If GetString(USD1099OID.St(OIDIndex), count1) = "IA" Then
                Total1 = Total1 + GetCurrency(USD1099OID.STWh(OIDIndex), count1)
            End If
            OIDIndex = OIDIndex + 1
        Loop
        count1 = count1 + 1
    Loop
    
    ReturnVal = Round(Total1)

End Sub

Private Sub TotOthIncWH_Calculation()
    
    ReturnVal = 0

End Sub

Private Sub TotSPDiv_Calculation()
    Dim count As Integer
    Dim SchBTotal As Currency

    count = 0
    SchBTotal = 0

    Do While count < 7
        If GetBool(IASchB.DSp1(count)) = True Then
            SchBTotal = SchBTotal + GetCurrency(IASchB.TaxDiv(count))
        Else
            SchBTotal = SchBTotal
        End If
        count = count + 1
    Loop

    Dim count1 As Integer
    Dim HowManyWBPDiv As Long
    Dim WSTotal As Currency
    Dim DivIndex As Long
    
    count1 = 1
    HowManyWBPDiv = GetAllCopies(IAWBPDiv)
    WSTotal = 0
    
    Do While count1 <= HowManyWBPDiv
        DivIndex = 0
        Do While DivIndex < 22
            If GetBool(IAWBPDiv.DSp1(DivIndex), count1) = True Then
                WSTotal = WSTotal + GetCurrency(IAWBPDiv.TaxDiv(DivIndex), count1)
            End If
            DivIndex = DivIndex + 1
        Loop
        count1 = count1 + 1
    Loop
    
    ReturnVal = SchBTotal + WSTotal + GetCurrency(IARequired.JointSPDiv)
End Sub

Private Sub TotSPInt_Calculation()
    Dim count As Integer
    Dim SchBTotal As Currency

    count = 0
    SchBTotal = 0

    Do While count < 7
        If GetBool(IASchB.ISp1(count)) = True Then
            SchBTotal = SchBTotal + GetCurrency(IASchB.TaxInt(count))
        Else
            SchBTotal = SchBTotal
        End If
        count = count + 1
    Loop

    Dim count1 As Integer
    Dim HowManyWBPInt As Long
    Dim WSTotal As Currency
    Dim IntIndex As Long
    
    count1 = 1
    HowManyWBPInt = GetAllCopies(IAWBPInt)
    WSTotal = 0
    
    Do While count1 <= HowManyWBPInt
        IntIndex = 0
        Do While IntIndex < 22
            If GetBool(IAWBPInt.ISp1(IntIndex), count1) = True Then
                WSTotal = WSTotal + GetCurrency(IAWBPInt.TaxInt(IntIndex), count1)
            End If
            IntIndex = IntIndex + 1
        Loop
        count1 = count1 + 1
    Loop
    
    ReturnVal = SchBTotal + WSTotal + GetCurrency(IARequired.JointSPInt)
End Sub

Private Sub TotTPDiv_Calculation()
    ReturnVal = GetCurrency(IARequired.TotDiv) - GetCurrency(IARequired.TotSPDiv)
End Sub

Private Sub TotTPInt_Calculation()
    ReturnVal = GetCurrency(IARequired.TotInt) - GetCurrency(IARequired.TotSPInt)
End Sub

Private Sub TotUnemWH_Calculation()
    Dim count1 As Integer
    Dim HowManyUnempl As Long
    Dim Total1 As Currency
    Dim UnIndex As Long
    
    count1 = 1
    HowManyUnempl = GetAllCopies(USWUnempl)
    Total1 = 0
    
    Do While count1 <= HowManyUnempl
        UnIndex = 0
        Do While UnIndex < 2
            If GetString(USWUnempl.TPState(UnIndex), count1) = "IA" Then
                Total1 = Total1 + GetCurrency(USWUnempl.TPStWH(UnIndex), count1)
            End If
            UnIndex = UnIndex + 1
        Loop
        count1 = count1 + 1
    Loop
    
    ReturnVal = Round(Total1)    

End Sub

Private Sub TotW2GWH_Calculation()
    Dim count1 As Integer
    Dim HowManyW2G As Long
    Dim Total1 As Currency
    
    count1 = 1
    HowManyW2G = GetAllCopies(USDW2G)
    Total1 = 0
    
    Do While count1 <= HowManyW2G
        If GetString(USDW2G.StateWon, count1) = "IA" Then
            Total1 = Total1 + GetCurrency(USDW2G.StateWH, count1)
        End If
        
        count1 = count1 + 1
    Loop
    
    ReturnVal = Round(Total1)

End Sub

Private Sub TP8824_Calculation()
    ReturnVal = GetCurrency(IA8824.IANonConformAdj, FieldCopies(IA8824.Taxpayer)) + CDollar(GetFloat(IA8824.IANonConformAdj, FieldCopies(IA8824.Joint)) * 0.5)
End Sub

Private Sub TPCapGainWH_Calculation()
    ReturnVal = GetCurrency(IARequired.TotCapGainWH) - GetCurrency(IARequired.SPCapGainWH)
End Sub

Private Sub TPComb_Calculation()
    ReturnVal = GetString(IAF1040.LastName) & ", " & GetString(IAF1040.FirstName)
End Sub

Private Sub TPCombName_Calculation()
    ReturnVal = GetString(IAF1040.FirstName) & " " & GetString(IAF1040.LastName)
End Sub

Private Sub TPDivWH_Calculation()
    ReturnVal = GetCurrency(IARequired.TotDivWH) - GetCurrency(IARequired.SPDivWH)
End Sub

Private Sub TPIntWH_Calculation()
    ReturnVal = GetCurrency(IARequired.TotIntWH) - GetCurrency(IARequired.SPIntWH)
End Sub

Private Sub TPKWH_Calculation()
    ReturnVal = GetCurrency(USZIA1040.TotKWH) - GetCurrency(USZIA1040.SPKWH)
End Sub

Private Sub TPMiscWH_Calculation()
    ReturnVal = GetCurrency(IARequired.TotMiscWH) - GetCurrency(IARequired.SPMiscWH)
End Sub

Private Sub TPOIDWH_Calculation()
    ReturnVal = GetCurrency(IARequired.TotOIDWH) - GetCurrency(IARequired.SPOIDWH)
End Sub

Private Sub TpOthIncWH_Calculation()
    ReturnVal = GetCurrency(IARequired.TotOthIncWH) - GetCurrency(IARequired.SPOthIncWH)
End Sub

Private Sub TPTotIncChg_Calculation()
' updated for 2018

    Dim Mid As Currency
    Dim MidInt As Long
    Dim TotTaxInc As Currency
    
    TotTaxInc = GetCurrency(IAF1040.AGross)
    
    If TotTaxInc > 95650@ Then
        Mid = TotTaxInc
    ElseIf TotTaxInc > 150@ Then
        MidInt = CLng((TotTaxInc - 1@) / 50@)
        Mid = (CCur(MidInt) * 50@) + 25@
    Else
        Mid = 0@
    End If
    
    ReturnVal = Tax(Mid)
End Sub

Private Sub TPUnemWH_Calculation()
    ReturnVal = GetCurrency(IARequired.TotUnemWH) - GetCurrency(IARequired.SPUnemWH)
End Sub

Private Sub TPW2GWH_Calculation()
    ReturnVal = GetCurrency(IARequired.TotW2GWH) - GetCurrency(IARequired.SPW2GWH)
End Sub

