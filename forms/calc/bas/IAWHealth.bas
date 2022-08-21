Private Sub Exist_Calculation()
    ReturnVal = 1
End Sub

Private Sub Description_Calculation()
    Dim Total As Currency
    
    Total = GetCurrency(IAWHealth.TPTotal) + GetCurrency(IAWHealth.SPTotal)
    
    ReturnVal = CStr(Total)
End Sub

Private Sub MobDisQual_Calculation()
    If GetCurrency(IAWHealth.TPTotal) + GetCurrency(IAWHealth.SPTotal) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.CombNames)
End Sub

Private Sub SERatio_Calculation()
    Dim TotSE As Currency
    
    TotSE = GetCurrency(IAWHealth.SPTotSE) + GetCurrency(IAWHealth.TPTotSE)
    
    If TotSE > 0 Then
        ReturnVal = MinValue(1#, MaxValue(0, GetFloat(IAWHealth.SPTotSE) / (GetFloat(IAWHealth.SPTotSE) + GetFloat(IAWHealth.TPTotSE))))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPMedicare_Calculation()
    Dim MedBReduce As Currency
    
    If GetCurrency(IAWHealth.TPSEHealth) > 0 And GetCurrency(IAWHealth.SPSEHealth) > 0 Then
        MedBReduce = CDollar(GetFloat(USWMedicalWS.MedBPremOff) * 0.5)
    ElseIf GetCurrency(IAWHealth.TPSEHealth) = 0 And GetCurrency(IAWHealth.SPSEHealth) > 0 Then
        MedBReduce = GetCurrency(USWMedicalWS.MedBPremOff)
    Else
        MedBReduce = 0
    End If

    ReturnVal = MaxValue(0, (GetCurrency(USWSSBDetail.SPMedB) + Round(GetCurrency(USDRRB1099R.MedB, FieldCopies(USDRRB1099R.Spouse)))) - MedBReduce)
End Sub

Private Sub SPName_Calculation()
    ReturnVal = GetString(USWBasicInfo.SPCommon)
End Sub

Private Sub SPSE_Calculation()
    ReturnVal = GetCurrency(USDSCorpK1.SeHealthInc, FieldCopies(USDSCorpK1.Spouse)) + CDollar(GetFloat(USDSCorpK1.SeHealthInc, FieldCopies(USDSCorpK1.Joint)) * 0.5)
End Sub

Private Sub SPSEHealth_Calculation()
    ReturnVal = CDollar(GetFloat(IAWHealth.TotHealth) * GetFloat(IAWHealth.SERatio))
End Sub

Private Sub SPTotal_Calculation()
    ReturnVal = GetCurrency(IAWHealth.SPSEHealth) + GetCurrency(IAWHealth.SPInsPrem) + GetCurrency(IAWHealth.SPMedicare) + GetCurrency(IAWHealth.SPLTC) + GetCurrency(IAWHealth.SPPYRepayPTC)
End Sub

Private Sub SPTotSE_Calculation()
    ReturnVal = GetCurrency(USSchSESpouse.ANetEarn) + GetCurrency(USSchSESpouse.BNetEarn) + GetCurrency(IAWHealth.SPSE)
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

Private Sub TotHealth_Calculation()
    ReturnVal = GetCurrency(USWSEHealth.InsPrem)
End Sub

Private Sub TotLTC_Calculation()
    ReturnVal = GetCurrency(USWMedicalWS.LTCPrem) + GetCurrency(USWMedicalWS.LTCPrem2) + GetCurrency(USWMedicalWS.LTCPrem3) + GetCurrency(USWMedicalWS.LTCPrem4)
End Sub

Private Sub TotSE_Calculation()
    ReturnVal = GetCurrency(USDSCorpK1.SeHealthInc)
End Sub

Private Sub TPInsPrem_Calculation()
'removed adjustment for USWMedicalWS.PTCAdj in order to only report what was actually paid out of pocket in the current year. The PTC adjustment (either credit or excess repayment) is handled by including repayment on IA 1040 line 28(current year)/line 18(import from prior year) and IA 1040 line 14 for any current year PTC credit to be imported as income the following year.
'change was made based on US 433238 see also CSS ticket 8605571
    Dim AdjInsPrem As Currency
    
    AdjInsPrem = MaxValue(0, GetCurrency(USWMedicalWS.MarketplaceIns)) + GetCurrency(USWMedicalWS.TPSPDepIns)
    
    ReturnVal = MaxValue(0, AdjInsPrem - GetCurrency(IAWHealth.SPInsPrem))
End Sub

Private Sub TPLTC_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWHealth.TotLTC) - GetCurrency(IAWHealth.SPLTC))
End Sub

Private Sub TPMedicare_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(USWMedicalWS.MedBPremTot) - GetCurrency(IAWHealth.SPMedicare))
End Sub

Private Sub TPName_Calculation()
    ReturnVal = GetString(USWBasicInfo.TPCommon)
End Sub

Private Sub TPPYRepayPTC_Calculation()
    If GetBool(USWSpouse.NonRes) = True Then
        ReturnVal = MaxValue(0, GetCurrency(USWRec.PYRepayPTCNR) - GetCurrency(IAWHealth.SPPYRepayPTC))
    Else
        ReturnVal = MaxValue(0, GetCurrency(USWRec.PYRepayPTC) - GetCurrency(IAWHealth.SPPYRepayPTC))
    End If
End Sub

Private Sub TPSE_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWHealth.TotSE) - GetCurrency(IAWHealth.SPSE))
End Sub

Private Sub TPSEHealth_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWHealth.TotHealth) - GetCurrency(IAWHealth.SPSEHealth))
End Sub

Private Sub TPTotal_Calculation()
    ReturnVal = GetCurrency(IAWHealth.TPSEHealth) + GetCurrency(IAWHealth.TPInsPrem) + GetCurrency(IAWHealth.TPMedicare) + GetCurrency(IAWHealth.TPLTC) + GetCurrency(IAWHealth.TPPYRepayPTC)
End Sub

Private Sub TPTotSE_Calculation()
    ReturnVal = GetCurrency(USSchSE.ANetEarn) + GetCurrency(USSchSE.BNetEarn) + GetCurrency(IAWHealth.TPSE)
End Sub

