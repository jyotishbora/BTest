Private Sub Alert10_Calculation()
    If GetNumber(IASchA.PrintSchA) = 1 Then
        If GetCurrency(IAWSchAPrint.OtherExp) <> 0 And Not IsValidEFileString(GetString(IAWSchAPrint.OtherMiscText)) Then
            ReturnVal = 1
        ElseIf GetCurrency(IAWSchAPrint.OtherExp2) <> 0 And Not IsValidEFileString(GetString(IAWSchAPrint.OtherMiscText2)) Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert20_Calculation()
    If GetNumber(IASchA.PrintSchA) = 1 Then
        If GetCurrency(IAWSchAPrint.OthExp) <> 0 And Not IsValidEFileString(GetString(IAWSchAPrint.OtherText)) Then
            ReturnVal = 1
        ElseIf GetCurrency(IAWSchAPrint.OthExp2) <> 0 And Not IsValidEFileString(GetString(IAWSchAPrint.OtherText2)) Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert30_Calculation()
    If GetNumber(IASchA.PrintSchA) = 1 Then
        If GetCurrency(IAWSchAPrint.Hobby) > (GetCurrency(IAWOthInc.TPHobby) + GetCurrency(IAWOthInc.SPHobby)) Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Bond_Calculation()
    ReturnVal = GetCurrency(USWSchAPrint.Bond)
End Sub

Private Sub CasualtyLoss_Calculation()
'believe current conditions being used to pull from 4684B ST and LT are not correct, the fed 4684 will not have amounts of an employee, just remove condition or use a different condition?
'verify .Ln22Employee will still be calced on Fed Sch A
    Dim TOne As Currency
    Dim TTwo As Currency
    
    'If GetCurrency(USF4684.STIncPro) > 0 Then
        TOne = GetCurrency(USF4684B.TotEmplST)
    'Else
    '    TOne = 0
    'End If
    
    'If GetCurrency(USF4684.L35bii) > 0 Then
        TTwo = GetCurrency(USF4684B.TotEmplLT)
    'Else
    '    TTwo = 0
    'End If
    
    ReturnVal = TOne + TTwo + GetCurrency(USSchA.Ln22Employee)
End Sub

Private Sub Debt_Calculation()
    ReturnVal = GetCurrency(USWSchAPrint.Debt)
End Sub

Private Sub Description_Calculation()
    If GetString(USWBasicInfo.FECombo) = "" Then
        ReturnVal = "Iowa Itemized Deductions"
    Else
        ReturnVal = GetString(USWBasicInfo.FECombo)
    End If
End Sub

Private Sub ExcessDed_Calculation()
    ReturnVal = GetCurrency(USDEstK1.ExcDed)
End Sub

Private Sub Exist_Calculation()
    ReturnVal = 1
End Sub

Private Sub F2106_Calculation()
    ReturnVal = GetCurrency(IA2106.SchAAMt)
End Sub

Private Sub Form4684_Calculation()
    ReturnVal = GetCurrency(USWSchAPrint.Form4684)
End Sub

Private Sub GamblingLoss_Calculation()
    ReturnVal = GetCurrency(USWSchAPrint.GamblingLoss)
End Sub

Private Sub ImpWrkExp_Calculation()
    ReturnVal = GetCurrency(USWSchAPrint.ImpWrkExp)
End Sub

Private Sub Indirect_Calculation()
'how will these expenses now be reported by the entity? Seems they still need to be passed through. Will we have an entry point on fed at all?
    'ReturnVal = GetCurrency(USWPartK1Detail.PortfolioDed2) + GetCurrency(USWPartK1Detail.MiscItmDed) + GetCurrency(USWSCorpK1Detail.PortfolioDed2) + GetCurrency(USWSCorpK1Detail.MiscItmDed)
    ReturnVal = 0
End Sub

Private Sub Invest_Calculation()
    ReturnVal = Round(GetCurrency(USD1099DIV.InvExp) + GetCurrency(USD1099INT.InvExp) + GetCurrency(USD1099OID.InvExp))
End Sub

Private Sub K1DedPort_Calculation()
    ReturnVal = GetCurrency(USWSchAPrint.K1DedPort)
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.CombNames)
End Sub

Private Sub Pension_Calculation()
    ReturnVal = GetCurrency(USWSchAPrint.Pension)
End Sub

Private Sub REMIC_Calculation()
    ReturnVal = GetCurrency(USSchEP2.RemicOtherInc)
End Sub

Private Sub Repay_Calculation()
    ReturnVal = GetCurrency(USWSchAPrint.Repay)
End Sub

Private Sub RepayInc_Calculation()
    If GetCurrency(USWUnempl.TPPrevUnemRepay) > 3000@ Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(USWUnempl.TPPrevUnemRepay)
    End If
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

Private Sub TotEstK1_Calculation()
    ReturnVal = GetCurrency(USWSchAPrint.TotEstK1)
End Sub

Private Sub TotExp_Calculation()
    If GetBool(USWResidency.F1040NR) = True Then
        ReturnVal = GetCurrency(IAWSchAPrint.Legal) + GetCurrency(IAWSchAPrint.OthLegal) + GetCurrency(IAWSchAPrint.Clerical) + GetCurrency(IAWSchAPrint.Custodial) + GetCurrency(IAWSchAPrint.Invest) + GetCurrency(IAWSchAPrint.InsolventLoss) + GetCurrency(IAWSchAPrint.CasualtyLoss) + GetCurrency(IAWSchAPrint.Appraisal) + GetCurrency(IAWSchAPrint.DeprTot) + GetCurrency(IAWSchAPrint.Amort) + GetCurrency(IAWSchAPrint.ExcessDed) + GetCurrency(IAWSchAPrint.Fees) + GetCurrency(IAWSchAPrint.Indirect) + GetCurrency(IAWSchAPrint.REMIC) + GetCurrency(IAWSchAPrint.IRALoss) + GetCurrency(IAWSchAPrint.RepayInc) + GetCurrency(IAWSchAPrint.SafeBox) + GetCurrency(IAWSchAPrint.ServiceCharge) + GetCurrency(IAWSchAPrint.TaxAdvice) + GetCurrency(IAWSchAPrint.Trustee) + GetCurrency(IAWSchAPrint.CreditFees) + GetCurrency(IAWSchAPrint.OthExp) + GetCurrency(IAWSchAPrint.OthExp2)
    Else
        ReturnVal = GetCurrency(IAWSchAPrint.Legal) + GetCurrency(IAWSchAPrint.OthLegal) + GetCurrency(IAWSchAPrint.Clerical) + GetCurrency(IAWSchAPrint.Custodial) + GetCurrency(IAWSchAPrint.Invest) + GetCurrency(IAWSchAPrint.InsolventLoss) + GetCurrency(IAWSchAPrint.CasualtyLoss) + GetCurrency(IAWSchAPrint.Appraisal) + GetCurrency(IAWSchAPrint.DeprTot) + GetCurrency(IAWSchAPrint.Amort) + GetCurrency(IAWSchAPrint.ExcessDed) + GetCurrency(IAWSchAPrint.Fees) + GetCurrency(IAWSchAPrint.Hobby) + GetCurrency(IAWSchAPrint.Indirect) + GetCurrency(IAWSchAPrint.REMIC) + GetCurrency(IAWSchAPrint.IRALoss) + GetCurrency(IAWSchAPrint.RepayInc) + GetCurrency(IAWSchAPrint.RepaySSB) + GetCurrency(IAWSchAPrint.SafeBox) + GetCurrency(IAWSchAPrint.ServiceCharge) + GetCurrency(IAWSchAPrint.TaxAdvice) + GetCurrency(IAWSchAPrint.Trustee) + GetCurrency(IAWSchAPrint.CreditFees) + GetCurrency(IAWSchAPrint.OthExp) + GetCurrency(IAWSchAPrint.OthExp2)
    End If
End Sub

Private Sub TotOthDed_Calculation()
    If GetBool(USWResidency.F1040NR) = True Then
        ReturnVal = GetCurrency(IAWSchAPrint.Form4684) + GetCurrency(IAWSchAPrint.K1DedPort) + GetCurrency(IAWSchAPrint.ImpWrkExp) + GetCurrency(IAWSchAPrint.Repay) + GetCurrency(IAWSchAPrint.Pension)
    Else
        ReturnVal = GetCurrency(IAWSchAPrint.Form4684) + GetCurrency(IAWSchAPrint.GamblingLoss) + GetCurrency(IAWSchAPrint.K1DedPort) + GetCurrency(IAWSchAPrint.ImpWrkExp) + GetCurrency(IAWSchAPrint.TotEstK1) + GetCurrency(IAWSchAPrint.Repay) + GetCurrency(IAWSchAPrint.Bond) + GetCurrency(IAWSchAPrint.Pension) + GetCurrency(IAWSchAPrint.Debt)
    End If
End Sub

Private Sub TotOtherExp_Calculation()
    ReturnVal = GetCurrency(IAWSchAPrint.F2106) + GetCurrency(IAWSchAPrint.BadDebt) + GetCurrency(IAWSchAPrint.LiabilityPrem) + GetCurrency(IAWSchAPrint.Breach) + GetCurrency(IAWSchAPrint.ChamberDues) + GetCurrency(IAWSchAPrint.ProffDues) + GetCurrency(IAWSchAPrint.JobSearch) + GetCurrency(IAWSchAPrint.LabFees) + GetCurrency(IAWSchAPrint.LegalFees) + GetCurrency(IAWSchAPrint.LicenseFees) + GetCurrency(IAWSchAPrint.Malpractice) + GetCurrency(IAWSchAPrint.MedExam) + GetCurrency(IAWSchAPrint.Occupational) + GetCurrency(IAWSchAPrint.Passport) + GetCurrency(IAWSchAPrint.RepayEmpInc) + GetCurrency(IAWSchAPrint.Research) + GetCurrency(IAWSchAPrint.Subscriptions) + GetCurrency(IAWSchAPrint.Tools) + GetCurrency(IAWSchAPrint.Union) + GetCurrency(IAWSchAPrint.Uniforms) + GetCurrency(IAWSchAPrint.WorkEdu) + GetCurrency(IAWSchAPrint.OtherExp) + GetCurrency(IAWSchAPrint.OtherExp2)
End Sub

Private Sub Union_Calculation()
    ReturnVal = Round(GetCurrency(USDW2.UnionDues))
End Sub

