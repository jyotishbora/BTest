Private Sub AnotherVN_Calculation(Index As Integer)
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetBool(USF2106.AnotherVN(Index), ParentCopy())
    End If
End Sub

Private Sub AnotherVY_Calculation(Index As Integer)
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetBool(USF2106.AnotherVY(Index), ParentCopy())
    End If
End Sub

Private Sub Common_Calculation()
    ReturnVal = GetString(USWBasicInfo.TPCommon)
End Sub

Private Sub Description_Calculation()
    ReturnVal = GetString(IA2106.FirstName)
End Sub

Private Sub DOT_Calculation()
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetBool(USF2106.DOT, ParentCopy())
    End If
End Sub

Private Sub DOTMeals_Calculation()
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        If GetBool(IA2106.DOT) = True Then
            ReturnVal = GetCurrency(USF2106.DOTMeals, ParentCopy())
        Else
            ReturnVal = 0
        End If
    End If
End Sub

Private Sub EmpExp_Calculation()
'should clergy be factored in, see 2017 Fed 2106 line 10 calc, would need checkbox and ClergyExp added to 2018 fed 2106 state section and interviewed (looks like these fields were added to fed in 2014)
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(IA2106.LimMEColA) + GetCurrency(IA2106.LimMEColB)
    End If
End Sub

Private Sub EvidenceN_Calculation(Index As Integer)
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetBool(USF2106.EvidenceN(Index), ParentCopy())
    End If
End Sub

Private Sub EvidenceY_Calculation(Index As Integer)
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetBool(USF2106.EvidenceY(Index), ParentCopy())
    End If
End Sub

Private Sub Exist_Calculation()
    ReturnVal = 1
End Sub

Private Sub Fed2106_Calculation()
    ReturnVal = "BEGIN HERE: Open federal Form 2106       Click on the folder to open the supporting document."
End Sub

Private Sub FedLn4_Calculation()
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(USF2106.TotBusExp, ParentCopy())
    End If
End Sub

Private Sub FirstName_Calculation()
    If GetBool(IA2106.Spouse) = True Then
        ReturnVal = GetString(IAF1040.SpouseFirst)
    Else
        ReturnVal = GetString(IAF1040.FirstName)
    End If
End Sub

Private Sub IAExcessReim_Calculation()
    If GetCurrency(IA2106.TotColA) - GetCurrency(IA2106.UnreimColA) < 0 Then
        ReturnVal = Abs(GetCurrency(IA2106.TotColA) - GetCurrency(IA2106.UnreimColA))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub IAStateDeprAdj_Calculation()
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(USF2106.IAStateDeprAdj, ParentCopy()) *  -1
    End If
End Sub

Private Sub IAWages_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA2106.IAExcessReim) - GetCurrency(IA2106.Wages))
End Sub

Private Sub LastName_Calculation()
    If GetBool(IA2106.Spouse) = True Then
        ReturnVal = GetString(IAF1040.SpouseLast)
    Else
        ReturnVal = GetString(IAF1040.LastName)
    End If
End Sub

Private Sub LimMEColA_Calculation()
    If GetCurrency(IA2106.NetColA) > 0 Then
        ReturnVal = GetCurrency(IA2106.NetColA)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub LimMEColB_Calculation()
    Dim DOTMeals As Currency
    Dim OthMeals As Currency
    
    DOTMeals = MaxValue(0, GetCurrency(IA2106.DOTMeals) - GetCurrency(IA2106.ReimbDOT))
    OthMeals = MaxValue(0, GetCurrency(IA2106.OthMeals) - GetCurrency(IA2106.ReimbOth))
    
    If DOTMeals + OthMeals > 0 Then
        If GetBool(IA2106.DOT) = True Then
            ReturnVal = CDollar(CDbl(DOTMeals) * 0.8) + CDollar(CDbl(OthMeals) * 0.5)
        Else
            ReturnVal = CDollar(CDbl(OthMeals) * 0.5)
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Meals_Calculation()
    If GetBool(IA2106.DOT) = True Then
        ReturnVal = GetCurrency(IA2106.DOTMeals) + GetCurrency(IA2106.OthMeals)
    Else
        ReturnVal = GetCurrency(IA2106.OthMeals)
    End If
End Sub

Private Sub NetColA_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA2106.TotColA) - GetCurrency(IA2106.UnreimColA))
End Sub

Private Sub NetColB_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA2106.TotColB) - GetCurrency(IA2106.UnReimColB))
End Sub

Private Sub Occupation_Calculation()
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = ""
    Else
        ReturnVal = GetString(USF2106.Occupation, ParentCopy())
    End If
End Sub

Private Sub OffN_Calculation(Index As Integer)
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetBool(USF2106.OffN(Index), ParentCopy())
    End If
End Sub

Private Sub OffY_Calculation(Index As Integer)
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetBool(USF2106.OffY(Index), ParentCopy())
    End If
End Sub

Private Sub OthMeals_Calculation()
    Dim TotMeals As Currency
    
    TotMeals = GetCurrency(USF2106.Meals, ParentCopy())
    
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = MaxValue(0, (TotMeals - GetCurrency(IA2106.DOTMeals)))
    End If
End Sub

Private Sub Parking_Calculation()
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(USF2106.Parking, ParentCopy())
    End If
End Sub

Private Sub PAvgComm_Calculation(Index As Integer)
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetNumber(USF2106.PAvgComm(Index), ParentCopy())
    End If
End Sub

Private Sub PBasis_Calculation(Index As Integer)
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(USF2106.PBasis(Index), ParentCopy())
    End If
End Sub

Private Sub PBusMiles_Calculation(Index As Integer)
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetNumber(USF2106.PBusMiles(Index), ParentCopy())
    End If
End Sub

Private Sub PBusPer_Calculation(Index As Integer)
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetFloat(USF2106.PBusPer(Index), ParentCopy())
    End If
End Sub

Private Sub PCommute_Calculation(Index As Integer)
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetNumber(USF2106.PCommute(Index), ParentCopy())
    End If
End Sub

Private Sub PDate_Calculation(Index As Integer)
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = ""
    Else
        ReturnVal = GetString(USF2106.PDate(Index), ParentCopy())
    End If
End Sub

Private Sub PDepr_Calculation(Index As Integer)
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(IA2106.PTotDepr(Index))
    End If
End Sub

Private Sub PDeprBasis_Calculation(Index As Integer)
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = MaxValue(0, CDollar(GetFloat(IA2106.PBasis(Index)) * GetFloat(IA2106.PBusPer(Index))) - GetCurrency(USF2106.PStateSec179(Index), ParentCopy()))
    End If
End Sub

Private Sub PDeprVeh_Calculation(Index As Integer)
'need to make sure sec179 is included, IA 2106 does not have a line for State sec179 and does not address in the instructions, seems this filed will have to show the depr basis x rate plus 179.
'Verified below is calling USW2106Veh.DeprNoBonus which includes depr x bus per. plus state 179
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(USF2106.PDeprVehState(Index), ParentCopy())
    End If
End Sub

Private Sub PExp_Calculation(Index As Integer)
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(USF2106.PExp(Index), ParentCopy())
    End If
End Sub

Private Sub PGas_Calculation(Index As Integer)
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(USF2106.PGas(Index), ParentCopy())
    End If
End Sub

Private Sub PInclusion_Calculation(Index As Integer)
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(USF2106.PInclusion(Index), ParentCopy())
    End If
End Sub

Private Sub PLuxLim_Calculation(Index As Integer)
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(USF2106.LuxLimState2(Index), ParentCopy())
    End If
End Sub

Private Sub PMethod_Calculation(Index As Integer)
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = ""
    Else
        ReturnVal = GetString(USF2106.PMethod(Index), ParentCopy())
    End If
End Sub

Private Sub PNetRent_Calculation(Index As Integer)
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(USF2106.PNetRent(Index), ParentCopy())
    End If
End Sub

Private Sub POthMiles_Calculation(Index As Integer)
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetNumber(USF2106.POthMiles(Index), ParentCopy())
    End If
End Sub

Private Sub PPerExp_Calculation(Index As Integer)
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(USF2106.PPerExp(Index), ParentCopy())
    End If
End Sub

Private Sub PPerLim_Calculation(Index As Integer)
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(USF2106.PerLimState2(Index), ParentCopy())
    End If
End Sub

Private Sub PRate_Calculation(Index As Integer)
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = ""
    Else
        ReturnVal = GetString(USF2106.PRate(Index), ParentCopy())
    End If
End Sub

Private Sub PRent_Calculation(Index As Integer)
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(USF2106.PRent(Index), ParentCopy())
    End If
End Sub

Private Sub PrintMe_Calculation()
    If GetCurrency(IA2106.EmpExp) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PrintPg21_Calculation()
    If GetCurrency(IA2106.PStandard(0)) > 0@ Or GetCurrency(IA2106.PTotAct(0)) > 0@ Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PrintPg22_Calculation()
    If GetCurrency(IA2106.PStandard(1)) > 0@ Or GetCurrency(IA2106.PTotAct(1)) > 0@ Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PrintPg23_Calculation()
    If GetCurrency(IA2106.PStandard(2)) > 0@ Or GetCurrency(IA2106.PTotAct(2)) > 0@ Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PrintPg24_Calculation()
    If GetCurrency(IA2106.PStandard(3)) > 0@ Or GetCurrency(IA2106.PTotAct(3)) > 0@ Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PStandard_Calculation(Index As Integer)
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(USF2106.PStandard(Index), ParentCopy())
    End If
End Sub

Private Sub PTotAct_Calculation(Index As Integer)
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    ElseIf GetCurrency(IA2106.PStandard(Index)) = 0 Then
        ReturnVal = GetCurrency(IA2106.PPerExp(Index)) + GetCurrency(IA2106.PDepr(Index))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PTotDepr_Calculation(Index As Integer)
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    ElseIf GetCurrency(IA2106.PLuxLim(Index)) = 0 And GetCurrency(IA2106.PPerLim(Index)) = 0 Then
        ReturnVal = GetCurrency(IA2106.PDeprVeh(Index))
    Else
        ReturnVal = MinValue(GetCurrency(IA2106.PDeprVeh(Index)), GetCurrency(IA2106.PPerLim(Index)))
    End If
End Sub

Private Sub PTotMiles_Calculation(Index As Integer)
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetNumber(USF2106.PTotMiles(Index), ParentCopy())
    End If
End Sub

Private Sub PValue_Calculation(Index As Integer)
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(USF2106.PValue(Index), ParentCopy())
    End If
End Sub

Private Sub FedQualifies_Calculation()
    ReturnVal = GetBool(USF2106.Qualifies, ParentCopy())
End Sub

Private Sub ReimbDOT_Calculation()
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        If GetBool(IA2106.DOT) = True Then
            ReturnVal = GetCurrency(USF2106.ReimbDOT, ParentCopy())
        Else
            ReturnVal = 0
        End If
    End If
End Sub

Private Sub ReimbOth_Calculation()
    Dim TotReimb As Currency
    
    TotReimb = GetCurrency(USF2106.UnReimColB, ParentCopy())
    
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = MaxValue(0, (TotReimb - GetCurrency(IA2106.ReimbDOT)))
    End If
End Sub

Private Sub SchAAMt_Calculation()
    ReturnVal = GetCurrency(IA2106.EmpExp)
End Sub

Private Sub Spouse_Calculation()
    ReturnVal = GetBool(USF2106.Spouse, ParentCopy())
End Sub

Private Sub SpouseCommon_Calculation()
    ReturnVal = GetString(USWBasicInfo.SPCommon)
End Sub

Private Sub SSN_Calculation()
    If GetBool(IA2106.Spouse) = True Then
        ReturnVal = GetString(IAF1040.SpouseSSN)
    Else
        ReturnVal = GetString(IAF1040.SSN)
    End If
End Sub

Private Sub Taxpayer_Calculation()
    ReturnVal = GetBool(USF2106.Taxpayer, ParentCopy())
End Sub

Private Sub TotBusExp_Calculation()
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(IA2106.FedLn4) + GetCurrency(IA2106.IAStateDeprAdj)
    End If
End Sub

Private Sub TotColA_Calculation()
    ReturnVal = GetCurrency(IA2106.VehExp) + GetCurrency(IA2106.Parking) + GetCurrency(IA2106.Travel) + GetCurrency(IA2106.TotBusExp)
End Sub

Private Sub TotColB_Calculation()
    ReturnVal = GetCurrency(IA2106.Meals)
End Sub

Private Sub Travel_Calculation()
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(USF2106.Travel, ParentCopy())
    End If
End Sub

Private Sub UnreimColA_Calculation()
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(USF2106.UnreimColA, ParentCopy())
    End If
End Sub

Private Sub UnReimColB_Calculation()
    If GetBool(IA2106.DOT) = True Then
        ReturnVal = GetCurrency(IA2106.ReimbDOT) + GetCurrency(IA2106.ReimbOth)
    Else
        ReturnVal = GetCurrency(IA2106.ReimbOth)
    End If
End Sub

Private Sub VehExp_Calculation()
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(IA2106.PStandard(0)) + GetCurrency(IA2106.PStandard(1)) + GetCurrency(IA2106.PStandard(2)) + GetCurrency(IA2106.PStandard(3)) + GetCurrency(IA2106.PTotAct(0)) + GetCurrency(IA2106.PTotAct(1)) + GetCurrency(IA2106.PTotAct(2)) + GetCurrency(IA2106.PTotAct(3))
    End If
End Sub

Private Sub Wages_Calculation()
    ReturnVal = GetCurrency(USF2106.Wages, ParentCopy())
End Sub

Private Sub WrittenN_Calculation(Index As Integer)
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetBool(USF2106.WrittenN(Index), ParentCopy())
    End If
End Sub

Private Sub WrittenY_Calculation(Index As Integer)
    If GetBool(IA2106.FedQualifies) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetBool(USF2106.WrittenY(Index), ParentCopy())
    End If
End Sub

Private Sub YrMakeModel_Calculation(Index As Integer)
    ReturnVal = GetString(IA2106.Year(Index)) + " " + GetString(IA2106.Make(Index)) + " " + GetString(IA2106.Model(Index))
End Sub

