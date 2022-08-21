Private Sub AAlimony_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpPYRes) = True) Or GetBool(IAF126.TpPYRes) = True Then
        ReturnVal = GetCurrency(IAF1040.AAlimony)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AAllSource_Calculation()
    If GetBool(IAF126.TpPYNR) = True Then
        ReturnVal = GetCurrency(IAF1040.ANet)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub ABusInc_Calculation()
'made change based on user story 445128 to calculate when a nonresident, for past 10 years lines 1-14 only calced when a part-year res. Based on Iowa 126 instructions decided to calc lines 5, 7, 10, 11, 12, 13, and 14 when a NR/PY to be conservative.
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAF1040.ABusInc)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub ACapGain_Calculation()
'decided to change this to be same as line 5, 7, 10, 11, 12, 13. Leaving lines 1-4 and 8 and 9 as they have specific instructions.
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAF1040.ACapGain)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub ACredit_Calculation()
    ReturnVal = CDollar(GetFloat(IAF126.ANetTax) * GetFloat(IAF126.ACrPer))
End Sub

Private Sub ACrPer_Calculation()
    If GetBool(IAF126.TpPYNR) = True Then
        ReturnVal = MaxValue(0, 1# - GetFloat(IAF126.AIAPer))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub ADividend_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpPYRes) = True) Or GetBool(IAF126.TpPYRes) = True Then
        ReturnVal = GetCurrency(IAF1040.ADividend)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AFarm_Calculation()
'made change based on user story 445128 to calculate when a nonresident, for past 10 years lines 1-14 only calced when a part-year res. Based on Iowa 126 instructions decided to calc lines 5, 7, 10, 11, 12, 13, and 14 when a NR/PY to be conservative.
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAF1040.AFarm)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AGamble_Calculation()
'made change based on user story 445128 to calculate when a nonresident, for past 10 years lines 1-14 only calced when a part-year res. Based on Iowa 126 instructions decided to calc lines 5, 7, 10, 11, 12, 13, and 14 when a NR/PY to be conservative.
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAF1040.AGamble)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AIATax_Calculation()
    If GetBool(IAF126.TpPYNR) = True Then
        ReturnVal = GetCurrency(IAF1040.AAltTax)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AInterest_Calculation()
    If (IAFS() = 2 And GetBool(IAF126.SpPYRes) = True) Or GetBool(IAF126.TpPYRes) = True Then
        ReturnVal = GetCurrency(IAF1040.AInterest)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AIRA_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IAWPenExc.NRTPIRA)
    Else
        ReturnVal = GetCurrency(IAWPenExc.NRTPIRA) + GetCurrency(IAWPenExc.NRSPIRA)
    End If
End Sub

Private Sub AMove_Calculation()
    If GetBool(IAF126.TpPYRes) = True Then
        If GetDate(IAF126.TpDateIn) > #12/31/2017# And GetDate(IAF126.TpDateOut) = 0 Then
            ReturnVal = GetCurrency(IAF1040.AMove)
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub ANet_Calculation()
    ReturnVal = GetCurrency(IAF126.GrossInc) - GetCurrency(IAF126.ATotAdj)
End Sub

Private Sub ANetTax_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAF126.AIATax) - GetCurrency(IAF126.ATotCr))
End Sub

Private Sub AOthAdj_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IANROthAdj.TPTot)
    Else
        ReturnVal = GetCurrency(IANROthAdj.TPTot) + GetCurrency(IANROthAdj.SPTot)
    End If
End Sub

Private Sub AOtherInc_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IANROthInc.TPTot)
    Else
        ReturnVal = GetCurrency(IANROthInc.TPTot) + GetCurrency(IANROthInc.SPTot)
    End If
End Sub

Private Sub AOthGain_Calculation()
'made change based on user story 445128 to calculate when a nonresident, for past 10 years lines 1-14 only calced when a part-year res. Based on Iowa 126 instructions decided to calc lines 5, 7, 10, 11, 12, 13, and 14 when a NR/PY to be conservative.
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAF1040.AOthGain)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub APenExcl_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IAWPenExc.NRTPPenExc)
    Else
        ReturnVal = GetCurrency(IAWPenExc.NRTPPenExc) + GetCurrency(IAWPenExc.NRSPPenExc)
    End If
End Sub

Private Sub APensions_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IAWPenExc.NRTPPensions)
    Else
        ReturnVal = GetCurrency(IAWPenExc.NRTPPensions) + GetCurrency(IAWPenExc.NRSPPensions)
    End If
End Sub

Private Sub ARents_Calculation()
'made change based on user story 445128 to calculate when a nonresident, for past 10 years lines 1-14 only calced when a part-year res. Based on Iowa 126 instructions decided to calc lines 5, 7, 10, 11, 12, 13, and 14 when a NR/PY to be conservative.
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAF1040.ARents)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AIAPer_Calculation()
    Dim TopLim As Double
    
    If GetBool(IAF126.IANotReqFIle) = True Then
        ReturnVal = 0
    ElseIf GetBool(IAF126.TpPYNR) = True Then
        If GetFloat(IAF126.AAllSource) <= 0 Then
            ReturnVal = 1#
        Else
            TopLim = MinValue(1#, Round(GetFloat(IAF126.ANet) / GetFloat(IAF126.AAllSource), 3))
            ReturnVal = MaxValue(0, TopLim)
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub ATotAdj_Calculation()
    If GetBool(IAF126.TpPYNR) = True Then
        ReturnVal = GetCurrency(IAF126.AKeogh) + GetCurrency(IAF126.ABusIncL) + GetCurrency(IAF126.AHealth) + GetCurrency(IAF126.APenalty) + GetCurrency(IAF126.AAlimonyP) + GetCurrency(IAF126.APenExcl) + GetCurrency(IAF126.AMove) + GetCurrency(IAF126.AGainDed) + GetCurrency(IAF126.AOthAdj)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub ATotCr_Calculation()
    If GetBool(IAF126.TpPYNR) = True Then
        ReturnVal = GetCurrency(IAF1040.ACredits)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AUnemp_Calculation()
'made change based on user story 445128 to calculate when a nonresident, for past 10 years lines 1-14 only calced when a part-year res. Based on Iowa 126 instructions decided to calc lines 5, 7, 10, 11, 12, 13, and 14 when a NR/PY to be conservative.
    If (IAFS() = 2 And GetBool(IAF126.SpRes) = False) Or GetBool(IAF126.TpRes) = False Then
        ReturnVal = GetCurrency(IAF1040.AUnemp)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub AWages_Calculation()
    If IAFS() = 2 And (GetBool(IAF126.SpRes) = False Or GetBool(IAF126.TpRes) = False) Then
        ReturnVal = MaxValue(GetCurrency(IAF126.TpWages), GetCurrency(IAF126.TpIAWages)) + MaxValue(GetCurrency(IAF126.SpWages), GetCurrency(IAF126.SpIAWages))
    ElseIf GetBool(IAF126.TpRes) = False Then
        ReturnVal = MaxValue(GetCurrency(IAF126.TpWages), GetCurrency(IAF126.TpIAWages))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BAlimony_Calculation()
    If GetBool(IAF1040.CombMFS) = True And GetBool(IAF126.SpPYRes) = True Then
        ReturnVal = GetCurrency(IAF1040.BAlimony)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BAllSource_Calculation()
    If GetBool(IAF126.SpPYNR) = True Then
        ReturnVal = GetCurrency(IAF1040.BNet)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BBusInc_Calculation()
'made change based on user story 445128 to calculate when a nonresident, for past 10 years lines 1-14 only calced when a part-year res. Based on Iowa 126 instructions decided to calc lines 5, 7, 10, 11, 12, 13, and 14 when a NR/PY to be conservative.
    If GetBool(IAF1040.CombMFS) = True And GetBool(IAF126.SpRes) = False Then
        ReturnVal = GetCurrency(IAF1040.BBusInc)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BCapGain_Calculation()
'decided to change this to be same as line 5, 7, 10, 11, 12, 13. Leaving lines 1-4 and 8 and 9 as they have specific instructions.
    If GetBool(IAF1040.CombMFS) = True And GetBool(IAF126.SpRes) = False Then
        ReturnVal = GetCurrency(IAF1040.BCapGain)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BCredit_Calculation()
    ReturnVal = CDollar(GetFloat(IAF126.BNetTax) * GetFloat(IAF126.BCrPer))
End Sub

Private Sub BCrPer_Calculation()
    If GetBool(IAF126.SpPYNR) = True Then
        ReturnVal = MaxValue(0, 1# - GetFloat(IAF126.BIAPer))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BDividend_Calculation()
    If GetBool(IAF1040.CombMFS) = True And GetBool(IAF126.SpPYRes) = True Then
        ReturnVal = GetCurrency(IAF1040.BDividend)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BFarm_Calculation()
'made change based on user story 445128 to calculate when a nonresident, for past 10 years lines 1-14 only calced when a part-year res. Based on Iowa 126 instructions decided to calc lines 5, 7, 10, 11, 12, 13, and 14 when a NR/PY to be conservative.
    If GetBool(IAF1040.CombMFS) = True And GetBool(IAF126.SpRes) = False Then
        ReturnVal = GetCurrency(IAF1040.BFarm)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BGamble_Calculation()
'made change based on user story 445128 to calculate when a nonresident, for past 10 years lines 1-14 only calced when a part-year res. Based on Iowa 126 instructions decided to calc lines 5, 7, 10, 11, 12, 13, and 14 when a NR/PY to be conservative.
    If GetBool(IAF1040.CombMFS) = True And GetBool(IAF126.SpRes) = False Then
        ReturnVal = GetCurrency(IAF1040.BGamble)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BGross_Calculation()
    If GetBool(IAF126.SpPYNR) = True Then
        ReturnVal = GetCurrency(IAF126.BWages) + GetCurrency(IAF126.BInterest) + GetCurrency(IAF126.BDividend) + GetCurrency(IAF126.BAlimony) + GetCurrency(IAF126.BBusInc) + GetCurrency(IAF126.BCapGain) + GetCurrency(IAF126.BOthGain) + GetCurrency(IAF126.BIRA) + GetCurrency(IAF126.BPensions) + GetCurrency(IAF126.BRents) + GetCurrency(IAF126.BFarm) + GetCurrency(IAF126.BUnemp) + GetCurrency(IAF126.BGamble) + GetCurrency(IAF126.BOtherInc)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BIATax_Calculation()
    If GetBool(IAF126.SpPYNR) = True Then
        ReturnVal = GetCurrency(IAF1040.BAltTax)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BInterest_Calculation()
    If GetBool(IAF1040.CombMFS) = True And GetBool(IAF126.SpPYRes) = True Then
        ReturnVal = GetCurrency(IAF1040.BInterest)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BIRA_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IAWPenExc.NRSPIRA)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BMove_Calculation()
    If IAFS() = 3 And GetBool(IAF126.SpPYRes) = True Then
        If GetDate(IAF126.SpDateIn) > #12/31/2017# And GetDate(IAF126.SpDateOut) = 0 Then
            ReturnVal = GetCurrency(IAF1040.BMove)
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BNet_Calculation()
    ReturnVal = GetCurrency(IAF126.BGross) - GetCurrency(IAF126.BTotAdj)
End Sub

Private Sub BNetTax_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAF126.BIATax) - GetCurrency(IAF126.BTotCr))
End Sub

Private Sub BOthAdj_Calculation()
    If GetBool(IAF126.SpPYNR) = True Then
        ReturnVal = GetCurrency(IANROthAdj.SPTot)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BOtherInc_Calculation()
    If GetBool(IAF126.SpPYNR) = True Then
        ReturnVal = GetCurrency(IANROthInc.SPTot)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BOthGain_Calculation()
'made change based on user story 445128 to calculate when a nonresident, for past 10 years lines 1-14 only calced when a part-year res. Based on Iowa 126 instructions decided to calc lines 5, 7, 10, 11, 12, 13, and 14 when a NR/PY to be conservative.
    If GetBool(IAF1040.CombMFS) = True And GetBool(IAF126.SpRes) = False Then
        ReturnVal = GetCurrency(IAF1040.BOthGain)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BPenExcl_Calculation()
    If GetBool(IAF126.SpPYNR) = True Then
        ReturnVal = GetCurrency(IAWPenExc.NRSPPenExc)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BPensions_Calculation()
    If IAFS() = 3 Then
        ReturnVal = GetCurrency(IAWPenExc.NRSPPensions)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BRents_Calculation()
'made change based on user story 445128 to calculate when a nonresident, for past 10 years lines 1-14 only calced when a part-year res. Based on Iowa 126 instructions decided to calc lines 5, 7, 10, 11, 12, 13, and 14 when a NR/PY to be conservative.
    If GetBool(IAF1040.CombMFS) = True And GetBool(IAF126.SpRes) = False Then
        ReturnVal = GetCurrency(IAF1040.BRents)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BIAPer_Calculation()
    Dim TopLim As Double
    
    If GetBool(IAF126.IANotReqFIle) = True Then
        ReturnVal = 0
    ElseIf GetBool(IAF126.SpPYNR) = True Then
        If GetFloat(IAF126.BAllSource) <= 0 Then
            ReturnVal = 1#
        Else
            TopLim = MinValue(1#, Round(GetFloat(IAF126.BNet) / GetFloat(IAF126.BAllSource), 3))
            ReturnVal = MaxValue(0, TopLim)
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BTotAdj_Calculation()
    If GetBool(IAF126.SpPYNR) = True Then
        ReturnVal = GetCurrency(IAF126.BKeogh) + GetCurrency(IAF126.BBusIncL) + GetCurrency(IAF126.BHealth) + GetCurrency(IAF126.BPenalty) + GetCurrency(IAF126.BAlimonyP) + GetCurrency(IAF126.BPenExcl) + GetCurrency(IAF126.BMove) + GetCurrency(IAF126.BGainDed) + GetCurrency(IAF126.BOthAdj)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BTotCr_Calculation()
    If GetBool(IAF126.SpPYNR) = True Then
        ReturnVal = GetCurrency(IAF1040.BCredits)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BUnemp_Calculation()
'made change based on user story 445128 to calculate when a nonresident, for past 10 years lines 1-14 only calced when a part-year res. Based on Iowa 126 instructions decided to calc lines 5, 7, 10, 11, 12, 13, and 14 when a NR/PY to be conservative.
    If GetBool(IAF1040.CombMFS) = True And GetBool(IAF126.SpRes) = False Then
        ReturnVal = GetCurrency(IAF1040.BUnemp)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BWages_Calculation()
    If GetBool(IAF126.SpPYNR) = True Then
        ReturnVal = MaxValue(GetCurrency(IAF126.SpWages), GetCurrency(IAF126.SpIAWages))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Desc_Calculation()
    Dim Total As Currency
    
    Total = GetCurrency(IAF126.BCredit) + GetCurrency(IAF126.ACredit)
    
    ReturnVal = CStr(Total) & " Credit"
End Sub

Private Sub Exist_Calculation()
    ReturnVal = 1
End Sub

Private Sub GrossInc_Calculation()
    If GetBool(IAF126.TpPYNR) = True Then
        ReturnVal = GetCurrency(IAF126.AWages) + GetCurrency(IAF126.AInterest) + GetCurrency(IAF126.ADividend) + GetCurrency(IAF126.AAlimony) + GetCurrency(IAF126.ABusInc) + GetCurrency(IAF126.ACapGain) + GetCurrency(IAF126.AOthGain) + GetCurrency(IAF126.AIRA) + GetCurrency(IAF126.APensions) + GetCurrency(IAF126.ARents) + GetCurrency(IAF126.AFarm) + GetCurrency(IAF126.AUnemp) + GetCurrency(IAF126.AGamble) + GetCurrency(IAF126.AOtherInc)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub IANotReqFIle_Calculation()
    If GetBool(IAF1040.MFS) = True Then
        ReturnVal = 0    
    ElseIf GetCurrency(IAF126.BNet) + GetCurrency(IAF126.ANet) >= 1000@ Then
        ReturnVal = 0
    ElseIf GetCurrency(IA6251.AMT) > 0 Or GetCurrency(IA6251Sp.AMT) > 0 Then
        ReturnVal = 0
    ElseIf GetCurrency(IAF1040.BLump) > 0 Or GetCurrency(IAF1040.ALump) > 0 Then
        ReturnVal = 0        
    Else
        ReturnVal = 1
    End If        
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.CombNames)
End Sub

Private Sub Print_Calculation()
    If GetBool(IAF126.TpPYNR) = True Or GetBool(IAF126.SpPYNR) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SpIAWages_Calculation()
    Dim count1 As Long
    Dim HowManyW2 As Long
    Dim Total1 As Currency
    Dim W2Index As Long
    Dim StEpWage As Currency
    Dim AllW2Wage As Currency    
    Dim OthWages As Currency  
   
    count1 = 1
    HowManyW2 = GetAllCopies(USDW2)
    Total1 = 0
    StEpWage = 0
       
    Do While count1 <= HowManyW2
        W2Index = 0
        Do While W2Index < 8
            If GetString(USDW2.St(W2Index), count1) = "IA" And GetBool(USDW2.Stat, count1) = False And GetBool(USDW2.Spouse, count1) = True Then
            Total1 = Total1 + Round(GetCurrency(USDW2.StWages(W2Index), count1))
        End If
        W2Index = W2Index + 1
        Loop
        count1 = count1 + 1
    Loop
    
    Do While count1 <= HowManyW2
        If GetBool(USDW2.Stat, count1) = True And GetBool(USDW2.Spouse, count1) = True Then
            StEpWage = StEpWage + Round(GetCurrency(USDW2.Wages, count1))
        End If
        count1 = count1 + 1
    Loop    
    
    AllW2Wage = GetCurrency(USDW2.Wages, FieldCopies(USDW2.Spouse))
    OthWages = GetCurrency(USWRec.SWages) - Round(AllW2Wage - StEpWage)
       
    ReturnVal = Total1 + OthWages
End Sub

Private Sub SpNonRes_Calculation()
    If GetBool(IAF1040.MFJ) = True Or GetBool(IAF1040.CombMFS) = True Then
        If GetBool(USWResidency.F1040NR) = False Then
            ReturnVal = 0
        Else
            ReturnVal = 1
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SpPYNR_Calculation()
    If GetBool(IAF1040.CombMFS) = True And GetBool(IAF126.SpRes) = False Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SpRes_Calculation()
    If GetBool(IAF1040.MFJ) = True Or GetBool(IAF1040.CombMFS) = True Then
        If GetBool(USWResidency.F1040NR) = False Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SpWages_Calculation()
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
            If GetString(USDW2.St(W2Index), count1) <> "IA" And GetBool(USDW2.Spouse, count1) = True Then
                Total1 = Total1 + GetCurrency(USDW2.StWages(W2Index), count1)
            End If
            W2Index = W2Index + 1
        Loop
        count1 = count1 + 1
    Loop
    
    ReturnVal = MaxValue(0, GetCurrency(USWRec.SWages) - Total1)

End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

Private Sub TpIAWages_Calculation()
    Dim count1 As Long
    Dim HowManyW2 As Long
    Dim Total1 As Currency
    Dim W2Index As Long
    Dim StEpWage As Currency
    Dim AllW2Wage As Currency    
    Dim OthWages As Currency  
   
    count1 = 1
    HowManyW2 = GetAllCopies(USDW2)
    Total1 = 0
    StEpWage = 0
       
    Do While count1 <= HowManyW2
        W2Index = 0
        Do While W2Index < 8
            If GetString(USDW2.St(W2Index), count1) = "IA" And GetBool(USDW2.Stat, count1) = False And GetBool(USDW2.Taxpayer, count1) = True Then
            Total1 = Total1 + Round(GetCurrency(USDW2.StWages(W2Index), count1))
        End If
        W2Index = W2Index + 1
        Loop
        count1 = count1 + 1
    Loop
    
    Do While count1 <= HowManyW2
        If GetBool(USDW2.Stat, count1) = True And GetBool(USDW2.Taxpayer, count1) = True Then
            StEpWage = StEpWage + Round(GetCurrency(USDW2.Wages, count1))
        End If
        count1 = count1 + 1
    Loop    
    
    AllW2Wage = GetCurrency(USDW2.Wages, FieldCopies(USDW2.Taxpayer))
    OthWages = GetCurrency(USWRec.TWages) - Round(AllW2Wage - StEpWage)
       
    ReturnVal = Total1 + OthWages

End Sub

Private Sub TpJtDateIn_Calculation()
    If GetBool(IAF126.TpPYRes) = True Then
        ReturnVal = GetString(IAF126.TpDateIn)
    ElseIf GetBool(IAF126.TpNonRes) = True Then
        ReturnVal = ""
    ElseIf GetBool(IAF1040.MFJ) = True And GetBool(IAF126.SpPYRes) = True Then
        ReturnVal = GetString(IAF126.SpDateIn)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub TpJtDateOut_Calculation()
    If GetBool(IAF126.TpPYRes) = True Then
        ReturnVal = GetString(IAF126.TpDateOut)
    ElseIf GetBool(IAF126.TpNonRes) = True Then
        ReturnVal = ""
    ElseIf GetBool(IAF1040.MFJ) = True And GetBool(IAF126.SpPYRes) = True Then
        ReturnVal = GetString(IAF126.SpDateOut)
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub TPJtNonRes_Calculation()
    If GetBool(IAF126.TpNonRes) = True Then
        ReturnVal = 1
    ElseIf GetBool(IAF126.TpPYRes) = True Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.MFJ) = True And GetBool(IAF126.SpNonRes) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPJtPYRes_Calculation()
    If GetBool(IAF126.TpPYRes) = True Then
        ReturnVal = 1
    ElseIf GetBool(IAF126.TpNonRes) = True Then
        ReturnVal = 0
    ElseIf GetBool(IAF1040.MFJ) = True And GetBool(IAF126.SpPYRes) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TpNonRes_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = 0
    Else
        ReturnVal = 1
    End If
End Sub

Private Sub TpPYNR_Calculation()
    If GetBool(IAF1040.MFJ) = True Then
        If GetBool(IAF126.TpRes) = False Or GetBool(IAF126.SpRes) = False Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    ElseIf GetBool(IAF126.TpRes) = False Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TpRes_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TpWages_Calculation()
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
            If GetString(USDW2.St(W2Index), count1) <> "IA" And GetBool(USDW2.Taxpayer, count1) = True Then
                Total1 = Total1 + GetCurrency(USDW2.StWages(W2Index), count1)
            End If
            W2Index = W2Index + 1
        Loop
        count1 = count1 + 1
    Loop
    
    ReturnVal = MaxValue(0, GetCurrency(USWRec.TWages) - Total1)
End Sub

