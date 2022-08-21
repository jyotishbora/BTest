Private Sub Box5_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = MaxValue(0, GetCurrency(USWSSBDetail.TotSS))
    Else
        ReturnVal = MaxValue(0, GetCurrency(USWSSBDetailNR.TPSS))
    End If
End Sub

Private Sub Description_Calculation()
    ReturnVal = CStr(GetCurrency(IAWkSSB.ReportSSB)) & " Reportable Benefits"
End Sub

Private Sub FilStat_Calculation()
    If FedFS() = 2 Then
        ReturnVal = 32000@
    ElseIf FedFS() = 3 And GetBool(USWBasicInfo.MFSAllYr) = False Then
        ReturnVal = 0
    Else
        ReturnVal = 25000@
    End If
End Sub

Private Sub Half10_Calculation()
    ReturnVal = CDollar(GetFloat(IAWkSSB.Sub9) * 0.5)
End Sub

Private Sub Half2_Calculation()
    ReturnVal = CDollar(GetFloat(IAWkSSB.Box5) * 0.5)
End Sub

Private Sub Line31_Calculation()
    ReturnVal = GetCurrency(USWRec.TotEdExp) + GetCurrency(USWRec.TotBusExp2106) + GetCurrency(USWRec.TotHealthSav) + GetCurrency(USWRec.TotMove) + GetCurrency(USWRec.TotHalfSE) + GetCurrency(USWRec.TotKeough) + GetCurrency(USWRec.TotSEHealth) + GetCurrency(USWRec.TotEarlyPen) + GetCurrency(USWRec.TotAlimonyAdj) + GetCurrency(USWRec.TotScholEx) + GetCurrency(USWRec.TotIRAAdj) + GetCurrency(USWRec.TotOthAdj)
End Sub

Private Sub Line8b_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USF1040.TEI)
    Else
        ReturnVal = GetCurrency(USF1040NR.TEI)
    End If
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.CombNames)
End Sub

Private Sub ReportSSB_Calculation()
    ReturnVal = MinValue(GetCurrency(IAWkSSB.Half2), GetCurrency(IAWkSSB.Half10))
End Sub

Private Sub SPRepSSB_Calculation()
    Dim TotSSB As Currency
    Dim SpSSB As Currency
    
    TotSSB = GetCurrency(IAWkSSB.Box5)
    SpSSB = GetCurrency(USWSSBDetail.SPSS)
    
    If GetBool(USWResidency.F1040NR) = False Then
        If TotSSB > 0 Then
            ReturnVal = CDollar((CDbl(SpSSB) / CDbl(TotSSB)) * GetFloat(IAWkSSB.ReportSSB))
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

Private Sub Sub_Calculation()
    ReturnVal = GetCurrency(IAWkSSB.Sum5) - GetCurrency(IAWkSSB.Line31)
End Sub

Private Sub Sub9_Calculation()
    ReturnVal = MaxValue(0, (GetCurrency(IAWkSSB.Sub) - GetCurrency(IAWkSSB.FilStat)))
End Sub

Private Sub Sum3_Calculation()
    If GetBool(USWResidency.F1040NR) = False Then
        ReturnVal = GetCurrency(USWSSB.SSBInc) + GetCurrency(USWSSB.TotExempt) + GetCurrency(IAWOthInc.TotBonus) + GetCurrency(IAWOthInc.TotNonConform) - GetCurrency(IARequired.NCMove) - GetCurrency(IARequired.NCDomProd) + CDollar(GetFloat(USWSSBDetail.TotRR) / 2)
    Else
        ReturnVal = GetCurrency(USF1040NR.TECI) + GetCurrency(USF8839.SumL22) + GetCurrency(IAWOthInc.TotBonus) + GetCurrency(IAWOthInc.TotNonConform) - GetCurrency(IARequired.NCMove) - GetCurrency(IARequired.NCDomProd) + CDollar(GetFloat(USWSSBDetailNR.TPRR) / 2)
    End If
End Sub

Private Sub Sum5_Calculation()
    ReturnVal = GetCurrency(IAWkSSB.Half2) + GetCurrency(IAWkSSB.Sum3) + GetCurrency(IAWkSSB.Line8b)
End Sub

Private Sub TPRepSSB_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWkSSB.ReportSSB) - GetCurrency(IAWkSSB.SPRepSSB))
End Sub

