Private Sub Alert10_Calculation()
    If GetNumber(IA134Sp.Print) > 0 Then
        If Trim(GetString(IA134Sp.SCorpName)) = "" Then
            ReturnVal = 1
        ElseIf GetString(IA134Sp.SCorpEIN) = "" Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert20_Calculation()
    If GetNumber(IA134Sp.Print) > 0 Then
        If GetCurrency(IA134Sp.StateAdj) <> 0 And Trim(GetString(IA134Sp.StateAdjExpl)) = "" Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Alert30_Calculation()
    If GetNumber(IA134Sp.Print) > 0 Then
        If GetCurrency(IA134Sp.FedRegTax) = 0 Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub BiggerInc_Calculation()
    ReturnVal = MaxValue(GetCurrency(IA134Sp.IASourceInc), GetCurrency(IA134Sp.NetDist))
End Sub

Private Sub Credit_Calculation()
    ReturnVal = CDollar((((Round(GetFloat(IA134Sp.CreditPercent) * 100#)) / 100#) * GetFloat(IA134Sp.NetTax)) / 100#)
End Sub

Private Sub CreditPercent_Calculation()
    If GetFloat(IA134Sp.BusRatio) > 0 Then
        ReturnVal = MaxValue(0, 100# - GetFloat(IA134Sp.TaxPercent))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Description_Calculation()
    Dim Total As Currency
    
    Total = GetCurrency(IA134Sp.Credit)
    
    ReturnVal = CStr(Total) & " Credit"
End Sub

Private Sub Dividends_Calculation()
    ReturnVal = GetCurrency(USDSCorpK1.Dividends, ParentCopy()) - (CDollar(GetFloat(USDSCorpK1.Dividends, ParentCopy()) * GetFloat(IA134Sp.TPRatio)))
End Sub

Private Sub Exist_Calculation()
    ReturnVal = 1
End Sub

Private Sub FedAGI_Calculation()
    If GetFloat(IA134Sp.BusRatio) > 0 Then
        If GetBool(IAF1040.CombMFS) = True Then
            ReturnVal = GetCurrency(USWRec.SAGI)
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub FedTax_Calculation()
    ReturnVal = GetCurrency(IA134Sp.K1FedTax)
End Sub

Private Sub IAApportion_Calculation()
    ReturnVal = CDollar((((Round(GetFloat(IA134Sp.IABusRatio) * 100#)) / 100#) * GetFloat(IA134Sp.NetIAInc)) / 100#)
End Sub

Private Sub IABusRatio_Calculation()
    ReturnVal = GetFloat(IA134Sp.BusRatio) * 100
End Sub

Private Sub IAInc_Calculation()
    If GetFloat(IA134Sp.BusRatio) > 0 Then
        If GetBool(IAF1040.CombMFS) = True Then
            ReturnVal = GetCurrency(IAF1040.BNet) + GetCurrency(IAOthAdj.SIANOL)
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub IASCorpInc_Calculation()
    If GetFloat(IA134Sp.BusRatio) > 0 Then
        ReturnVal = GetCurrency(IA134Sp.K1Inc) + GetCurrency(IA134Sp.StateAdj)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub IASourceInc_Calculation()
    If GetFloat(IA134Sp.BusRatio) > 0 Then
        ReturnVal = GetCurrency(IA134Sp.IAApportion) + GetCurrency(IA134Sp.IANonBusInc)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Interest_Calculation()
    ReturnVal = GetCurrency(USDSCorpK1.Interest, ParentCopy()) - (CDollar(GetFloat(USDSCorpK1.Interest, ParentCopy()) * GetFloat(IA134Sp.TPRatio)))
End Sub

Private Sub IntSCorp_Calculation()
    If Trim(GetString(IA134Sp.SCorpName)) <> "" Then
        ReturnVal = GetString(IA134Sp.SCorpName)
    Else
        ReturnVal = "this S corporation"
    End If
End Sub

Private Sub K1FedTax_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA134Sp.K1Tax) - GetCurrency(IA134Sp.K1FedCredits))
End Sub

Private Sub K1Inc_Calculation()
    ReturnVal = GetCurrency(IA134Sp.TotInc) - GetCurrency(IA134Sp.TotDed)
End Sub

Private Sub K1Inc2_Calculation()
    ReturnVal = GetCurrency(IA134Sp.K1Inc)
End Sub

Private Sub K1IncPercent_Calculation()
    ReturnVal = GetFloat(IA134Sp.K1IncRatio) * 100
End Sub

Private Sub K1IncRatio_Calculation()
    Dim TopLim As Double
    
    If GetFloat(IA134Sp.BusRatio) = 0 Then
        ReturnVal = 0
    ElseIf GetFloat(IA134Sp.FedAGI) <= 0 Then
        ReturnVal = 1#
    Else
        TopLim = MinValue(1#, Round(GetFloat(IA134Sp.K1Inc2) / GetFloat(IA134Sp.FedAGI), 6))
        ReturnVal = MaxValue(0, TopLim)
    End If
End Sub

Private Sub K1Tax_Calculation()
    ReturnVal = Round(CDollar(GetFloat(IA134Sp.NetFedTax) * (GetFloat(IA134Sp.K1IncPercent) / 100#)))    
End Sub

Private Sub LtGain_Calculation()
    ReturnVal = GetCurrency(USDSCorpK1.LtGain, ParentCopy()) - (CDollar(GetFloat(USDSCorpK1.LtGain, ParentCopy()) * GetFloat(IA134Sp.TPRatio)))
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.SPCombName)
End Sub

Private Sub NetDist_Calculation()
    If GetFloat(IA134Sp.BusRatio) > 0 Then
        ReturnVal = MaxValue(0, GetCurrency(IA134Sp.Distributions) - GetCurrency(IA134Sp.FedTax))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub NetFedTax_Calculation()
    ReturnVal = GetCurrency(IA134Sp.FedRegTax) + GetCurrency(IA134Sp.FedAMT)
End Sub

Private Sub NetIAInc_Calculation()
    If GetFloat(IA134Sp.BusRatio) > 0 Then
        ReturnVal = GetCurrency(IA134Sp.IASCorpInc) - GetCurrency(IA134Sp.NonBusInc)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub NetTax_Calculation()
    If GetFloat(IA134Sp.BusRatio) > 0 Then
        ReturnVal = GetCurrency(IAF1040.BTotIATax)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Numerator_Calculation()
    ReturnVal = GetCurrency(IA134Sp.BiggerInc) + GetCurrency(IA134Sp.Remainder)
End Sub

Private Sub Ordinary_Calculation()
    ReturnVal = GetCurrency(USDSCorpK1.OrdAmt, ParentCopy()) - (CDollar(GetFloat(USDSCorpK1.OrdAmt, ParentCopy()) * GetFloat(IA134Sp.TPRatio)))
End Sub

Private Sub OthDed_Calculation()
    ReturnVal = GetCurrency(USDSCorpK1.SCOthDed, ParentCopy()) - (CDollar(GetFloat(USDSCorpK1.SCOthDed, ParentCopy()) * GetFloat(IA134Sp.TPRatio)))
End Sub

Private Sub OtherInc_Calculation()
    Dim PortInc As Currency
    Dim Sec1256 As Currency
    Dim MineCost As Currency
    Dim OthInc As Currency
    
    PortInc = GetCurrency(USDSCorpK1.PortInc, ParentCopy()) - (CDollar(GetFloat(USDSCorpK1.PortInc, ParentCopy()) * GetFloat(IA134Sp.TPRatio)))
    Sec1256 = GetCurrency(USDSCorpK1.Sec1256, ParentCopy()) - (CDollar(GetFloat(USDSCorpK1.Sec1256, ParentCopy()) * GetFloat(IA134Sp.TPRatio)))
    MineCost = GetCurrency(USDSCorpK1.MineCost, ParentCopy()) - (CDollar(GetFloat(USDSCorpK1.MineCost, ParentCopy()) * GetFloat(IA134Sp.TPRatio)))
    OthInc = GetCurrency(USDSCorpK1.OthInc, ParentCopy()) - (CDollar(GetFloat(USDSCorpK1.OthInc, ParentCopy()) * GetFloat(IA134Sp.TPRatio)))
    
    ReturnVal = PortInc + Sec1256 + MineCost + OthInc
    
End Sub

Private Sub Print_Calculation()
    If GetBool(IAF1040.CombMFS) = False Then
        ReturnVal = 0
    ElseIf GetCurrency(IA134Sp.Credit) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub RealEstate_Calculation()
    ReturnVal = GetCurrency(USDSCorpK1.RentAmt, ParentCopy()) - (CDollar(GetFloat(USDSCorpK1.RentAmt, ParentCopy()) * GetFloat(IA134Sp.TPRatio)))
End Sub

Private Sub Remainder_Calculation()
    ReturnVal = GetCurrency(IA134Sp.IAInc) - GetCurrency(IA134Sp.IASCorpInc)
End Sub

Private Sub Rental_Calculation()
    ReturnVal = GetCurrency(USDSCorpK1.Rental, ParentCopy()) - (CDollar(GetFloat(USDSCorpK1.Rental, ParentCopy()) * GetFloat(IA134Sp.TPRatio)))
End Sub

Private Sub Royalties_Calculation()
    ReturnVal = GetCurrency(USDSCorpK1.Royalties, ParentCopy()) - (CDollar(GetFloat(USDSCorpK1.Royalties, ParentCopy()) * GetFloat(IA134Sp.TPRatio)))
End Sub

Private Sub SCorpEIN_Calculation()
    ReturnVal = GetString(USDSCorpK1.EIN, ParentCopy())
End Sub

Private Sub SCorpName_Calculation()
    ReturnVal = GetString(USDSCorpK1.CoName, ParentCopy())
End Sub

Private Sub Sec1231_Calculation()
    ReturnVal = GetCurrency(USDSCorpK1.Sec1231, ParentCopy()) - (CDollar(GetFloat(USDSCorpK1.Sec1231, ParentCopy()) * GetFloat(IA134Sp.TPRatio)))
End Sub

Private Sub Sec179_Calculation()
    ReturnVal = GetCurrency(USDSCorpK1.Sec179, ParentCopy()) - (CDollar(GetFloat(USDSCorpK1.Sec179, ParentCopy()) * GetFloat(IA134Sp.TPRatio)))
End Sub

Private Sub SPApplied_Calculation()
    Dim count As Integer
    
    count = 0
    
    Do While count <= 9
        If GetString(IA148Sp.NonRefCode(count)) = "11" And GetCurrency(IA148Sp.CYCredit(count)) = GetCurrency(IA134Sp.Credit) Then
            ReturnVal = GetCurrency(IA148Sp.ArrayNonRefCr(count))
        End If
        count = count + 1
    Loop
    
    Dim count2 As Integer
    
    count2 = 0
        
    Do While count <= 28
        If GetString(IAWBP148Sp.NonRefCode(count2)) = "11" And GetCurrency(IAWBP148Sp.CYCredit(count2)) = GetCurrency(IA134Sp.Credit) Then
            ReturnVal = GetCurrency(IAWBP148Sp.ArrayNonRefCr(count2))
        End If
        count = count + 1
    Loop
    
    ReturnVal = 0
End Sub

Private Sub SPExpired_Calculation()
    Dim count As Integer
    
    count = 0
    
    Do While count <= 9
        If GetString(IA148Sp.NonRefCode(count)) = "11" And GetCurrency(IA148Sp.CYCredit(count)) = GetCurrency(IA134Sp.Credit) Then
            ReturnVal = GetCurrency(IA148Sp.ExpCr(count))
        End If
        count = count + 1
    Loop
    
    Dim count2 As Integer
    
    count2 = 0
        
    Do While count <= 28
        If GetString(IAWBP148Sp.NonRefCode(count2)) = "11" And GetCurrency(IAWBP148Sp.CYCredit(count2)) = GetCurrency(IA134Sp.Credit) Then
            ReturnVal = GetCurrency(IAWBP148Sp.ExpCr(count2))
        End If
        count = count + 1
    Loop
    
    ReturnVal = 0
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SpouseSSN)
End Sub

Private Sub StGain_Calculation()
    ReturnVal = GetCurrency(USDSCorpK1.StGain, ParentCopy()) - (CDollar(GetFloat(USDSCorpK1.StGain, ParentCopy()) * GetFloat(IA134Sp.TPRatio)))
End Sub

Private Sub TaxPercent_Calculation()
    ReturnVal = GetFloat(IA134Sp.TaxRatio) * 100
End Sub

Private Sub TaxRatio_Calculation()
    Dim TopLim As Double
    
    If GetFloat(IA134Sp.BusRatio) = 0 Then
        ReturnVal = 0
    ElseIf GetFloat(IA134Sp.IAInc) = 0 Then
        ReturnVal = 1#
    Else
        TopLim = MinValue(1#, Round(GetFloat(IA134Sp.Numerator) / GetFloat(IA134Sp.IAInc), 6))
        ReturnVal = MaxValue(0, TopLim)
    End If
End Sub

Private Sub TotDed_Calculation()
    If GetFloat(IA134Sp.BusRatio) > 0 Then
        ReturnVal = GetCurrency(IA134Sp.Sec179) + GetCurrency(IA134Sp.OthDed)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TotInc_Calculation()
    If GetFloat(IA134Sp.BusRatio) > 0 Then
        ReturnVal = GetCurrency(IA134Sp.Ordinary) + GetCurrency(IA134Sp.RealEstate) + GetCurrency(IA134Sp.Rental) + GetCurrency(IA134Sp.Interest) + GetCurrency(IA134Sp.Dividends) + GetCurrency(IA134Sp.Royalties) + GetCurrency(IA134Sp.StGain) + GetCurrency(IA134Sp.LtGain) + GetCurrency(IA134Sp.Sec1231) + GetCurrency(IA134Sp.OtherInc)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPRatio_Calculation()
    If GetBool(IAF1040.CombMFS) = True And GetBool(USDSCorpK1.Joint, ParentCopy()) = True Then
        ReturnVal = 0.5
    ElseIf GetBool(IAF1040.CombMFS) = True And GetBool(USDSCorpK1.Spouse, ParentCopy()) = True Then
        ReturnVal = 0
    Else
        ReturnVal = 1#
    End If
End Sub

