Private Sub CBF_Calculation()
    ReturnVal = GetBool(USWPrepBInv.StY)
End Sub

Private Sub CBF1040_Calculation()
    ReturnVal = GetCurrency(USZIAMasterCBF.CBF1040)
End Sub

Private Sub CBF1040ES_Calculation()
    ReturnVal = GetCurrency(USZIAMasterCBF.CBF1040ES)
End Sub

Private Sub CBF1040V_Calculation()
    ReturnVal = GetCurrency(USZIAMasterCBF.CBF1040V)
End Sub

Private Sub CBF1040X_Calculation()
    ReturnVal = GetCurrency(USZIAMasterCBF.CBF1040X)
End Sub

Private Sub CBF1040XV_Calculation()
    ReturnVal = GetCurrency(USZIAMasterCBF.CBF1040XV)
End Sub

Private Sub CBF2210_Calculation()
    ReturnVal = GetCurrency(USZIAMasterCBF.CBF2210)
End Sub

Private Sub CBF2210SchAI_Calculation()
    ReturnVal = GetCurrency(USZIAMasterCBF.CBF2210SchAI)
End Sub

Private Sub CBF4136_Calculation()
    ReturnVal = GetCurrency(USZIAMasterCBF.CBF4136)
End Sub

Private Sub CBF4562A_Calculation()
    ReturnVal = GetCurrency(USZIAMasterCBF.CBF4562A)
End Sub

Private Sub CBF4562B_Calculation()
    ReturnVal = GetCurrency(USZIAMasterCBF.CBF4562B)
End Sub

Private Sub CBF6251_Calculation()
    ReturnVal = GetCurrency(USZIAMasterCBF.CBF6251)
End Sub

Private Sub CBF8453_Calculation()
        ReturnVal = GetCurrency(USZIAMasterCBF.CBF8453)
End Sub

Private Sub CBF8801_Calculation()
    ReturnVal = GetCurrency(USZIAMasterCBF.CBF8801)
End Sub

Private Sub CBF8864_Calculation()
    ReturnVal = GetCurrency(USZIAMasterCBF.CBF8864)
End Sub

Private Sub CBFName_Calculation()
    ReturnVal = GetString(IARequired.CombNames)
End Sub

Private Sub CBFOthAmt_Calculation(Index As Integer)
    ReturnVal = GetCurrency(USZIAMasterCBF.CBFOthAmt(Index))
End Sub

Private Sub CBFSch126_Calculation()
    ReturnVal = GetCurrency(USZIAMasterCBF.CBFSch126)
End Sub

Private Sub CBFSch128_Calculation()
    ReturnVal = GetCurrency(USZIAMasterCBF.CBFSch128)
End Sub

Private Sub CBFSch128S_Calculation()
    ReturnVal = GetCurrency(USZIAMasterCBF.CBFSch128S)
End Sub

Private Sub CBFSch130_Calculation()
    ReturnVal = GetCurrency(USZIAMasterCBF.CBFSch130)
End Sub

Private Sub CBFSch134_Calculation()
    ReturnVal = GetCurrency(USZIAMasterCBF.CBFSch134)
End Sub

Private Sub CBFSch135_Calculation()
    ReturnVal = GetCurrency(USZIAMasterCBF.CBFSch135)
End Sub

Private Sub CBFSch137_Calculation()
    ReturnVal = GetCurrency(USZIAMasterCBF.CBFSch137)
End Sub

Private Sub CBFSch138_Calculation()
    ReturnVal = GetCurrency(USZIAMasterCBF.CBFSch138)
End Sub

Private Sub CBFSch147_Calculation()
    ReturnVal = GetCurrency(USZIAMasterCBF.CBFSch147)
End Sub

Private Sub CBFSch148_Calculation()
    ReturnVal = GetCurrency(USZIAMasterCBF.CBFSch148)
End Sub

Private Sub CBFSch177_Calculation()
    ReturnVal = GetCurrency(USZIAMasterCBF.CBFSch177)
End Sub

Private Sub CBFSchA_Calculation()
    ReturnVal = GetCurrency(USZIAMasterCBF.CBFSchA)
End Sub

Private Sub CBFSchB_Calculation()
    ReturnVal = GetCurrency(USZIAMasterCBF.CBFSchB)
End Sub

Private Sub CF147_Calculation()
    ReturnVal = GetNumber(IA147.Print)
End Sub

Private Sub CF177_Calculation()
    ReturnVal = GetNumber(IA177.Print)
End Sub

Private Sub CF1040_Calculation()
    ReturnVal = 1
End Sub

Private Sub CF126_Calculation()
    ReturnVal = GetNumber(IAF126.Print)
End Sub

Private Sub CF128_Calculation()
    ReturnVal = GetNumber(IA128.Print)
End Sub

Private Sub CF128S_Calculation()
    ReturnVal = GetNumber(IA128S.Print)
End Sub

Private Sub CF130_Calculation()
    ReturnVal = GetNumber(IA130.PrintMe)
End Sub

Private Sub CF134_Calculation()
    ReturnVal = GetNumber(IA134.Print) + GetNumber(IA134Sp.Print)
End Sub

Private Sub CF135_Calculation()
    ReturnVal = GetNumber(IA135.Print)
End Sub

Private Sub CF137_Calculation()
    ReturnVal = GetNumber(IA137.Print)
End Sub

Private Sub CF138_Calculation()
    ReturnVal = GetNumber(IA138.Print)
End Sub

Private Sub CF148_Calculation()
    ReturnVal = GetNumber(IA148.Print) + GetNumber(IA148Sp.Print)
End Sub

Private Sub CF1040V_Calculation()
    ReturnVal = GetNumber(IA1040V.PrVou)
End Sub

Private Sub CF1040XV_Calculation()
    ReturnVal = GetNumber(IA1040XV.PrVou)
End Sub

Private Sub CF2210_Calculation()
    ReturnVal = GetNumber(IA2210.Print) + GetNumber(IA2210Sp.Print)
End Sub

Private Sub CF2210SchAI_Calculation()
    ReturnVal = GetNumber(IA2210An.Print) + GetNumber(IA2210AnSp.Print)
End Sub

Private Sub CF4136_Calculation()
    ReturnVal = GetBool(IASch4136.TotCr, 1) + GetBool(IASch4136.TotCr, 2)
End Sub

Private Sub CF4562A_Calculation()
    ReturnVal = GetNumber(IA4562.PrIA4562) + GetNumber(IA4562Sp.PrIA4562) + GetNumber(IA4562A.PrIA4562A)
End Sub

Private Sub CF4562B_Calculation()
    ReturnVal = GetNumber(IA4562B.Print) + GetNumber(IA4562BSp.Print)
End Sub

Private Sub CF6251_Calculation()
    ReturnVal = GetNumber(IA6251.Print) + GetNumber(IA6251Sp.Print)
End Sub

Private Sub CF8801_Calculation()
    ReturnVal = GetNumber(IA8801.Print) + GetNumber(IA8801Sp.Print)
End Sub

Private Sub CF8864_Calculation()
    ReturnVal = GetNumber(IA8864.Print)
End Sub

Private Sub CFA_Calculation()
    ReturnVal = GetNumber(IASchA.PrintSchA)
End Sub

Private Sub CFB_Calculation()
    ReturnVal = GetNumber(IASchB.PrintIAB)
End Sub

Private Sub CFES_Calculation()
    ReturnVal = GetNumber(IAEstimates.Print)
End Sub

Private Sub CFX_Calculation()
    ReturnVal = GetNumber(IA1040X.Exist)
End Sub

Private Sub CopFOthName_Calculation(Index As Integer)
    ReturnVal = GetString(USZIAMasterCBF.CBFOth1Name(Index))
End Sub

Private Sub FOthAmt_Calculation(Index As Integer)
    ReturnVal = GetCurrency(IAWPrepCBF.CopFOth(Index)) * GetCurrency(IAWPrepCBF.CBFOthAmt(Index))
End Sub

Private Sub FTotal1040_Calculation()
    ReturnVal = GetCurrency(IAWPrepCBF.CF1040) * GetCurrency(IAWPrepCBF.CBF1040)
End Sub

Private Sub FTotal1040ES_Calculation()
    ReturnVal = GetCurrency(IAWPrepCBF.CFES) * GetCurrency(IAWPrepCBF.CBF1040ES)
End Sub

Private Sub FTotal1040V_Calculation()
    ReturnVal = GetCurrency(IAWPrepCBF.CF1040V) * GetCurrency(IAWPrepCBF.CBF1040V)
End Sub

Private Sub FTotal1040X_Calculation()
    ReturnVal = GetCurrency(IAWPrepCBF.CFX) * GetCurrency(IAWPrepCBF.CBF1040X)
End Sub

Private Sub FTotal1040XV_Calculation()
    ReturnVal = GetCurrency(IAWPrepCBF.CF1040XV) * GetCurrency(IAWPrepCBF.CBF1040XV)
End Sub

Private Sub FTotal2210_Calculation()
    ReturnVal = GetCurrency(IAWPrepCBF.CF2210) * GetCurrency(IAWPrepCBF.CBF2210)
End Sub

Private Sub FTotal2210SchAI_Calculation()
    ReturnVal = GetCurrency(IAWPrepCBF.CF2210SchAI) * GetCurrency(IAWPrepCBF.CBF2210SchAI)
End Sub

Private Sub FTotal4136_Calculation()
    ReturnVal = GetCurrency(IAWPrepCBF.CF4136) * GetCurrency(IAWPrepCBF.CBF4136)
End Sub

Private Sub FTotal4562A_Calculation()
    ReturnVal = GetCurrency(IAWPrepCBF.CF4562A) * GetCurrency(IAWPrepCBF.CBF4562A)
End Sub

Private Sub FTotal4562B_Calculation()
    ReturnVal = GetCurrency(IAWPrepCBF.CF4562B) * GetCurrency(IAWPrepCBF.CBF4562B)
End Sub

Private Sub FTotal6251_Calculation()
    ReturnVal = GetCurrency(IAWPrepCBF.CF6251) * GetCurrency(IAWPrepCBF.CBF6251)
End Sub

Private Sub FTotal8453_Calculation()
    ReturnVal = GetCurrency(IAWPrepCBF.CF8453) * GetCurrency(IAWPrepCBF.CBF8453)
End Sub

Private Sub FTotal8801_Calculation()
    ReturnVal = GetCurrency(IAWPrepCBF.CF8801) * GetCurrency(IAWPrepCBF.CBF8801)
End Sub

Private Sub FTotal8864_Calculation()
    ReturnVal = GetCurrency(IAWPrepCBF.CF8864) * GetCurrency(IAWPrepCBF.CBF8864)
End Sub

Private Sub FTotalSch126_Calculation()
    ReturnVal = GetCurrency(IAWPrepCBF.CF126) * GetCurrency(IAWPrepCBF.CBFSch126)
End Sub

Private Sub FTotalSch128_Calculation()
    ReturnVal = GetCurrency(IAWPrepCBF.CF128) * GetCurrency(IAWPrepCBF.CBFSch128)
End Sub

Private Sub FTotalSch128S_Calculation()
    ReturnVal = GetCurrency(IAWPrepCBF.CF128S) * GetCurrency(IAWPrepCBF.CBFSch128S)
End Sub

Private Sub FTotalSch130_Calculation()
    ReturnVal = GetCurrency(IAWPrepCBF.CF130) * GetCurrency(IAWPrepCBF.CBFSch130)
End Sub

Private Sub FTotalSch134_Calculation()
    ReturnVal = GetCurrency(IAWPrepCBF.CF134) * GetCurrency(IAWPrepCBF.CBFSch134)
End Sub

Private Sub FTotalSch135_Calculation()
    ReturnVal = GetCurrency(IAWPrepCBF.CF135) * GetCurrency(IAWPrepCBF.CBFSch135)
End Sub

Private Sub FTotalSch137_Calculation()
    ReturnVal = GetCurrency(IAWPrepCBF.CF137) * GetCurrency(IAWPrepCBF.CBFSch137)
End Sub

Private Sub FTotalSch138_Calculation()
    ReturnVal = GetCurrency(IAWPrepCBF.CF138) * GetCurrency(IAWPrepCBF.CBFSch138)
End Sub

Private Sub FTotalSch147_Calculation()
    ReturnVal = GetCurrency(IAWPrepCBF.CF147) * GetCurrency(IAWPrepCBF.CBFSch147)
End Sub

Private Sub FTotalSch148_Calculation()
    ReturnVal = GetCurrency(IAWPrepCBF.CF148) * GetCurrency(IAWPrepCBF.CBFSch148)
End Sub

Private Sub FTotalSch177_Calculation()
    ReturnVal = GetCurrency(IAWPrepCBF.CF177) * GetCurrency(IAWPrepCBF.CBFSch177)
End Sub

Private Sub FTotalSchA_Calculation()
    ReturnVal = GetCurrency(IAWPrepCBF.CFA) * GetCurrency(IAWPrepCBF.CBFSchA)
End Sub

Private Sub FTotalSchB_Calculation()
    ReturnVal = GetCurrency(IAWPrepCBF.CFB) * GetCurrency(IAWPrepCBF.CBFSchB)
End Sub

Private Sub TotCharge_Calculation()
    Dim TotCharge1 As Currency
    Dim TotCharge2 As Currency

    TotCharge1 = GetCurrency(IAWPrepCBF.FTotal1040) + GetCurrency(IAWPrepCBF.FTotal1040ES) + GetCurrency(IAWPrepCBF.FTotal1040V) + GetCurrency(IAWPrepCBF.FTotal1040X) + GetCurrency(IAWPrepCBF.FTotal1040XV) + GetCurrency(IAWPrepCBF.FTotalSchA) + GetCurrency(IAWPrepCBF.FTotalSchB) + GetCurrency(IAWPrepCBF.FTotalSch126) + GetCurrency(IAWPrepCBF.FTotalSch128) + GetCurrency(IAWPrepCBF.FTotalSch128S) + GetCurrency(IAWPrepCBF.FTotalSch130) + GetCurrency(IAWPrepCBF.FTotalSch134) + GetCurrency(IAWPrepCBF.FTotalSch135) + GetCurrency(IAWPrepCBF.FTotalSch137) + GetCurrency(IAWPrepCBF.FTotalSch138) + GetCurrency(IAWPrepCBF.FTotalSch147) + GetCurrency(IAWPrepCBF.FTotalSch148)
    TotCharge2 = GetCurrency(IAWPrepCBF.FTotalSch177) + GetCurrency(IAWPrepCBF.FTotal2210) + GetCurrency(IAWPrepCBF.FTotal2210SchAI) + GetCurrency(IAWPrepCBF.FTotal4136) + GetCurrency(IAWPrepCBF.FTotal4562A) + GetCurrency(IAWPrepCBF.FTotal4562B) + GetCurrency(IAWPrepCBF.FTotal6251) + GetCurrency(IAWPrepCBF.FTotal8453) + GetCurrency(IAWPrepCBF.FTotal8801) + GetCurrency(IAWPrepCBF.FTotal8864) + GetCurrency(IAWPrepCBF.FOthAmt(0)) + GetCurrency(IAWPrepCBF.FOthAmt(1)) + GetCurrency(IAWPrepCBF.FOthAmt(2)) + GetCurrency(IAWPrepCBF.FOthAmt(3)) + GetCurrency(IAWPrepCBF.FOthAmt(4))
    
    ReturnVal = TotCharge1 + TotCharge2
End Sub

