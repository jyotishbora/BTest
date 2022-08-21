Private Sub AccMktDiscIntCopies_Calculation()
    Dim TPAccMktDiscInt As Integer
    Dim SPAccMktDiscInt As Integer
    Dim JTAccMktDiscInt As Integer
    
    If GetCurrency(IASchB.TPAccMktDiscInt) > 0 Then
        TPAccMktDiscInt = 1
    Else
        TPAccMktDiscInt = 0
    End If
    
    If GetCurrency(IASchB.SPAccMktDiscInt) > 0 Then
        SPAccMktDiscInt = 1
    Else
        SPAccMktDiscInt = 0
    End If
    
    If GetCurrency(IASchB.JtAccMktDiscInt) > 0 Then
        JTAccMktDiscInt = 1
    Else
        JTAccMktDiscInt = 0
    End If
    
    ReturnVal = TPAccMktDiscInt + SPAccMktDiscInt + JTAccMktDiscInt
End Sub

Private Sub ContigentPayCopies_Calculation()
    Dim TPContigentPay As Integer
    Dim SPContigentPay As Integer
    Dim JTContigentPay As Integer
    
    If GetCurrency(IASchB.TPContigentPay) > 0 Then
        TPContigentPay = 1
    Else
        TPContigentPay = 0
    End If
    
    If GetCurrency(IASchB.SPContigentPay) > 0 Then
        SPContigentPay = 1
    Else
        SPContigentPay = 0
    End If
    
    If GetCurrency(IASchB.JtContigentPay) > 0 Then
        JTContigentPay = 1
    Else
        JTContigentPay = 0
    End If
    
    ReturnVal = TPContigentPay + SPContigentPay + JTContigentPay
End Sub

Private Sub CrBP11_Calculation()
    If GetNumber(IASchB.TotINTCopies) > 226 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBP12_Calculation()
    If GetNumber(IASchB.TotINTCopies) > 248 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBP1_Calculation()
    If GetNumber(IASchB.TotINTCopies) > 7 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBP10_Calculation()
    If GetNumber(IASchB.TotINTCopies) > 204 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBP2_Calculation()
    If GetNumber(IASchB.TotINTCopies) > 28 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBP3_Calculation()
    If GetNumber(IASchB.TotINTCopies) > 50 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBP4_Calculation()
    If GetNumber(IASchB.TotINTCopies) > 72 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBP5_Calculation()
    If GetNumber(IASchB.TotINTCopies) > 94 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBP6_Calculation()
    If GetNumber(IASchB.TotINTCopies) > 116 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBP7_Calculation()
    If GetNumber(IASchB.TotINTCopies) > 138 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBP8_Calculation()
    If GetNumber(IASchB.TotINTCopies) > 160 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBP9_Calculation()
    If GetNumber(IASchB.TotINTCopies) > 182 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDiv10_Calculation()
    If GetNumber(IASchB.TotDIVCopies) > 204 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDiv11_Calculation()
    If GetNumber(IASchB.TotDIVCopies) > 226 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDiv1_Calculation()
    If GetNumber(IASchB.TotDIVCopies) > 7 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDiv2_Calculation()
    If GetNumber(IASchB.TotDIVCopies) > 28 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDiv3_Calculation()
    If GetNumber(IASchB.TotDIVCopies) > 50 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDiv4_Calculation()
    If GetNumber(IASchB.TotDIVCopies) > 72 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDiv5_Calculation()
    If GetNumber(IASchB.TotDIVCopies) > 94 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDiv6_Calculation()
    If GetNumber(IASchB.TotDIVCopies) > 116 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDiv7_Calculation()
    If GetNumber(IASchB.TotDIVCopies) > 138 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDiv8_Calculation()
    If GetNumber(IASchB.TotDIVCopies) > 160 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CrBPDiv9_Calculation()
    If GetNumber(IASchB.TotDIVCopies) > 182 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Desc_Calculation()
    ReturnVal = GetString(IARequired.CombNames)
End Sub

Private Sub DivAcctOwner_Calculation(Index As Integer)
    If GetBool(IASchB.DTp1(Index)) = True Then
        ReturnVal = "Taxpayer"
    ElseIf GetBool(IASchB.DSp1(Index)) = True Then
        ReturnVal = "Spouse"
    ElseIf GetBool(IASchB.DJ1(Index)) = True Then
        ReturnVal = "Joint"
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub Dividend_Calculation(Index As Integer)
    Dim Stuff As Integer
    Dim DIV As Integer
    Dim PartK1 As Integer
    Dim SCorpK1 As Integer
    Dim EstK1 As Integer
    Dim F5471 As Integer
    Dim F8621 As Integer
    Dim F8814 As Integer

    DIV = GetNumber(IAWBBump.DIVNbr)
    PartK1 = GetNumber(IAWBBump.PartK1DivNbr)
    SCorpK1 = GetNumber(IAWBBump.SCorpK1DivNbr)
    EstK1 = GetNumber(IAWBBump.EstK1DivNbr)
    F5471 = GetNumber(IAWBBump.F5471Nbr)
    F8621 = GetNumber(IAWBBump.F8621Nbr)
    F8814 = GetNumber(IAWBBump.F8814Nbr)
    
    If Index = 6 And GetNumber(IASchB.TotDIVCopies) > 7 Then
        ReturnVal = GetCurrency(IAWBPDiv.TotalDividend)
    ElseIf DIV > Index Then
        ReturnVal = Round(GetCurrency(USD1099DIV.ORDDIV, GetNumber(IAWBBump.DIV(Index)))) + Round(GetCurrency(USD1099DIV.FedExmpt, GetNumber(IAWBBump.DIV(Index))))
    ElseIf DIV + PartK1 > Index Then
        Stuff = (Index) - DIV
        ReturnVal = GetCurrency(USDPartK1.Dividends, (GetNumber(IAWBBump.PartK1Div(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 > Index Then
        Stuff = (Index) - DIV - PartK1
        ReturnVal = GetCurrency(USDSCorpK1.Dividends, (GetNumber(IAWBBump.SCorpK1Div(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 > Index Then
        Stuff = (Index) - DIV - PartK1 - SCorpK1
        ReturnVal = GetCurrency(USDEstK1.Dividends, (GetNumber(IAWBBump.EstK1Div(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 + F5471 > Index Then
        Stuff = (Index) - DIV - PartK1 - SCorpK1 - EstK1
        ReturnVal = GetCurrency(USW5471SchI.DivOrd, (GetNumber(IAWBBump.F5471(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 > Index Then
        Stuff = (Index) - DIV - PartK1 - SCorpK1 - EstK1 - F5471
        ReturnVal = GetCurrency(USF8621.DivTo1040, (GetNumber(IAWBBump.F8621(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 + F8814 > Index Then
        Stuff = (Index) - DIV - PartK1 - SCorpK1 - EstK1 - F5471 - F8621
        ReturnVal = GetCurrency(USF8814.L6XL7, (GetNumber(IAWBBump.F8814(Stuff))))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub DivPayer_Calculation(Index As Integer)
    Dim Stuff As Integer
    Dim DIV As Integer
    Dim PartK1 As Integer
    Dim SCorpK1 As Integer
    Dim EstK1 As Integer
    Dim F5471 As Integer
    Dim F8621 As Integer
    Dim F8814 As Integer

    DIV = GetNumber(IAWBBump.DIVNbr)
    PartK1 = GetNumber(IAWBBump.PartK1DivNbr)
    SCorpK1 = GetNumber(IAWBBump.SCorpK1DivNbr)
    EstK1 = GetNumber(IAWBBump.EstK1DivNbr)
    F5471 = GetNumber(IAWBBump.F5471Nbr)
    F8621 = GetNumber(IAWBBump.F8621Nbr)
    F8814 = GetNumber(IAWBBump.F8814Nbr)
    
    If Index = 6 And GetNumber(IASchB.TotDIVCopies) > 7 Then
        ReturnVal = "See Statement Attached"
    ElseIf DIV > Index Then
        ReturnVal = GetString(USD1099DIV.PayerName, GetNumber(IAWBBump.DIV(Index)))
    ElseIf DIV + PartK1 > Index Then
        Stuff = (Index) - DIV
        ReturnVal = GetString(USDPartK1.CoName, (GetNumber(IAWBBump.PartK1Div(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 > Index Then
        Stuff = (Index) - DIV - PartK1
        ReturnVal = GetString(USDSCorpK1.CoName, (GetNumber(IAWBBump.SCorpK1Div(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 > Index Then
        Stuff = (Index) - DIV - PartK1 - SCorpK1
        ReturnVal = GetString(USDEstK1.TrustName, (GetNumber(IAWBBump.EstK1Div(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 + F5471 > Index Then
        Stuff = (Index) - DIV - PartK1 - SCorpK1 - EstK1
        ReturnVal = "Form 5471"
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 > Index Then
        Stuff = (Index) - DIV - PartK1 - SCorpK1 - EstK1 - F5471
        ReturnVal = "Form 8621 - " & GetString(USF8621.CoName, (GetNumber(IAWBBump.F8621(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 + F8814 > Index Then
        Stuff = (Index) - DIV - PartK1 - SCorpK1 - EstK1 - F5471 - F8621
        ReturnVal = "Form 8814 - " & GetString(USF8814.ChName, (GetNumber(IAWBBump.F8814(Stuff))))
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub DJ1_Calculation(Index As Integer)
    Dim Stuff As Integer
    Dim DIV As Integer
    Dim PartK1 As Integer
    Dim SCorpK1 As Integer
    Dim EstK1 As Integer
    Dim F5471 As Integer
    Dim F8621 As Integer
    Dim F8814 As Integer

    DIV = GetNumber(IAWBBump.DIVNbr)
    PartK1 = GetNumber(IAWBBump.PartK1DivNbr)
    SCorpK1 = GetNumber(IAWBBump.SCorpK1DivNbr)
    EstK1 = GetNumber(IAWBBump.EstK1DivNbr)
    F5471 = GetNumber(IAWBBump.F5471Nbr)
    F8621 = GetNumber(IAWBBump.F8621Nbr)
    F8814 = GetNumber(IAWBBump.F8814Nbr)
    
    If Index = 6 And GetNumber(IASchB.TotDIVCopies) > 7 Then
        ReturnVal = 0
    ElseIf DIV > Index Then
        ReturnVal = GetBool(USD1099DIV.Joint, GetNumber(IAWBBump.DIV(Index)))
    ElseIf DIV + PartK1 > Index Then
        Stuff = (Index) - DIV
        ReturnVal = GetBool(USDPartK1.Joint, (GetNumber(IAWBBump.PartK1Div(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 > Index Then
        Stuff = (Index) - DIV - PartK1
        ReturnVal = GetBool(USDSCorpK1.Joint, (GetNumber(IAWBBump.SCorpK1Div(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 > Index Then
        Stuff = (Index) - DIV - PartK1 - SCorpK1
        ReturnVal = GetBool(USDEstK1.Joint, (GetNumber(IAWBBump.EstK1Div(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 + F5471 > Index Then
        Stuff = (Index) - DIV - PartK1 - SCorpK1 - EstK1
        ReturnVal = 0
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 > Index Then
        Stuff = (Index) - DIV - PartK1 - SCorpK1 - EstK1 - F5471
        ReturnVal = GetBool(USF8621.Joint, (GetNumber(IAWBBump.F8621(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 + F8814 > Index Then
        Stuff = (Index) - DIV - PartK1 - SCorpK1 - EstK1 - F5471 - F8621
        If GetBool(USWBasicInfo.JointCalc) = True Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub DSp1_Calculation(Index As Integer)
    Dim Stuff As Integer
    Dim DIV As Integer
    Dim PartK1 As Integer
    Dim SCorpK1 As Integer
    Dim EstK1 As Integer
    Dim F5471 As Integer
    Dim F8621 As Integer
    Dim F8814 As Integer

    DIV = GetNumber(IAWBBump.DIVNbr)
    PartK1 = GetNumber(IAWBBump.PartK1DivNbr)
    SCorpK1 = GetNumber(IAWBBump.SCorpK1DivNbr)
    EstK1 = GetNumber(IAWBBump.EstK1DivNbr)
    F5471 = GetNumber(IAWBBump.F5471Nbr)
    F8621 = GetNumber(IAWBBump.F8621Nbr)
    F8814 = GetNumber(IAWBBump.F8814Nbr)
    
    If Index = 6 And GetNumber(IASchB.TotDIVCopies) > 7 Then
        ReturnVal = 0
    ElseIf DIV > Index Then
        ReturnVal = GetBool(USD1099DIV.Spouse, GetNumber(IAWBBump.DIV(Index)))
    ElseIf DIV + PartK1 > Index Then
        Stuff = (Index) - DIV
        ReturnVal = GetBool(USDPartK1.Spouse, (GetNumber(IAWBBump.PartK1Div(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 > Index Then
        Stuff = (Index) - DIV - PartK1
        ReturnVal = GetBool(USDSCorpK1.Spouse, (GetNumber(IAWBBump.SCorpK1Div(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 > Index Then
        Stuff = (Index) - DIV - PartK1 - SCorpK1
        ReturnVal = GetBool(USDEstK1.Spouse, (GetNumber(IAWBBump.EstK1Div(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 + F5471 > Index Then
        Stuff = (Index) - DIV - PartK1 - SCorpK1 - EstK1
        If GetString(USW5471SchI.SchISSN, (GetNumber(IAWBBump.F5471(Stuff)))) = GetString(USWBasicInfo.SpouseSSN) Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 > Index Then
        Stuff = (Index) - DIV - PartK1 - SCorpK1 - EstK1 - F5471
        ReturnVal = GetBool(USF8621.Spouse, (GetNumber(IAWBBump.F8621(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 + F8814 > Index Then
        Stuff = (Index) - DIV - PartK1 - SCorpK1 - EstK1 - F5471 - F8621
        ReturnVal = 0
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub DTp1_Calculation(Index As Integer)
    Dim Stuff As Integer
    Dim DIV As Integer
    Dim PartK1 As Integer
    Dim SCorpK1 As Integer
    Dim EstK1 As Integer
    Dim F5471 As Integer
    Dim F8621 As Integer
    Dim F8814 As Integer

    DIV = GetNumber(IAWBBump.DIVNbr)
    PartK1 = GetNumber(IAWBBump.PartK1DivNbr)
    SCorpK1 = GetNumber(IAWBBump.SCorpK1DivNbr)
    EstK1 = GetNumber(IAWBBump.EstK1DivNbr)
    F5471 = GetNumber(IAWBBump.F5471Nbr)
    F8621 = GetNumber(IAWBBump.F8621Nbr)
    F8814 = GetNumber(IAWBBump.F8814Nbr)
    
    If Index = 6 And GetNumber(IASchB.TotDIVCopies) > 7 Then
        ReturnVal = 0
    ElseIf DIV > Index Then
        ReturnVal = GetBool(USD1099DIV.Taxpayer, GetNumber(IAWBBump.DIV(Index)))
    ElseIf DIV + PartK1 > Index Then
        Stuff = (Index) - DIV
        ReturnVal = GetBool(USDPartK1.Taxpayer, (GetNumber(IAWBBump.PartK1Div(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 > Index Then
        Stuff = (Index) - DIV - PartK1
        ReturnVal = GetBool(USDSCorpK1.Taxpayer, (GetNumber(IAWBBump.SCorpK1Div(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 > Index Then
        Stuff = (Index) - DIV - PartK1 - SCorpK1
        ReturnVal = GetBool(USDEstK1.Taxpayer, (GetNumber(IAWBBump.EstK1Div(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 + F5471 > Index Then
        Stuff = (Index) - DIV - PartK1 - SCorpK1 - EstK1
        If GetString(USW5471SchI.SchISSN, (GetNumber(IAWBBump.F5471(Stuff)))) = GetString(USWBasicInfo.SSN) Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 > Index Then
        Stuff = (Index) - DIV - PartK1 - SCorpK1 - EstK1 - F5471
        ReturnVal = GetBool(USF8621.Taxpayer, (GetNumber(IAWBBump.F8621(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 + F8814 > Index Then
        Stuff = (Index) - DIV - PartK1 - SCorpK1 - EstK1 - F5471 - F8621
        If GetBool(USWBasicInfo.JointCalc) = True Then
            ReturnVal = 0
        Else
            ReturnVal = 1
        End If
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub ExemptDiv_Calculation(Index As Integer)
    Dim Stuff As Integer
    Dim DIV As Integer
    Dim PartK1 As Integer
    Dim SCorpK1 As Integer
    Dim EstK1 As Integer
    Dim F5471 As Integer
    Dim F8621 As Integer
    Dim F8814 As Integer

    DIV = GetNumber(IAWBBump.DIVNbr)
    PartK1 = GetNumber(IAWBBump.PartK1DivNbr)
    SCorpK1 = GetNumber(IAWBBump.SCorpK1DivNbr)
    EstK1 = GetNumber(IAWBBump.EstK1DivNbr)
    F5471 = GetNumber(IAWBBump.F5471Nbr)
    F8621 = GetNumber(IAWBBump.F8621Nbr)
    F8814 = GetNumber(IAWBBump.F8814Nbr)
    
    If Index = 6 And GetNumber(IASchB.TotDIVCopies) > 7 Then
        ReturnVal = GetCurrency(IAWBPDiv.TotalExemptDiv)
    ElseIf DIV > Index Then
        ReturnVal = Round(GetCurrency(USD1099DIV.Nominee, GetNumber(IAWBBump.DIV(Index)))) + Round(GetCurrency(USD1099DIV.StExmpt, GetNumber(IAWBBump.DIV(Index)))) + Round(GetCurrency(USD1099DIV.FedStExmpt, GetNumber(IAWBBump.DIV(Index)))) + Round(GetCurrency(USD1099DIV.Restricted, GetNumber(IAWBBump.DIV(Index))))
    ElseIf DIV + PartK1 > Index Then
        Stuff = (Index) - DIV
        ReturnVal = GetCurrency(USDPartK1.NetStTED, (GetNumber(IAWBBump.PartK1Div(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 > Index Then
        Stuff = (Index) - DIV - PartK1
        ReturnVal = GetCurrency(USDSCorpK1.NetStTED, (GetNumber(IAWBBump.SCorpK1Div(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 > Index Then
        Stuff = (Index) - DIV - PartK1 - SCorpK1
        ReturnVal = GetCurrency(USDEstK1.NetStTED, (GetNumber(IAWBBump.EstK1Div(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 + F5471 > Index Then
        Stuff = (Index) - DIV - PartK1 - SCorpK1 - EstK1
        ReturnVal = 0
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 > Index Then
        Stuff = (Index) - DIV - PartK1 - SCorpK1 - EstK1 - F5471
        ReturnVal = 0
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 + F8814 > Index Then
        Stuff = (Index) - DIV - PartK1 - SCorpK1 - EstK1 - F5471 - F8621
        ReturnVal = 0
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub ExemptInt_Calculation(Index As Integer)
    Dim Stuff As Integer
    Dim ResSFM As Integer
    Dim OthSFM As Integer
    Dim OID As Integer
    Dim INT1099 As Integer
    Dim PartK1 As Integer
    Dim SCorpK1 As Integer
    Dim EstK1 As Integer
    Dim TPAccMktDisc As Boolean
    
    ResSFM = GetNumber(IAWBBump.ResSFMNbr)
    OthSFM = GetNumber(IAWBBump.OthSFMNbr)
    OID = GetNumber(IAWBBump.OIDNbr)
    INT1099 = GetNumber(IAWBBump.INTNbr)
    PartK1 = GetNumber(IAWBBump.PartK1Nbr)
    SCorpK1 = GetNumber(IAWBBump.SCorpK1Nbr)
    EstK1 = GetNumber(IAWBBump.EstK1Nbr)
    TPAccMktDisc = GetBool(IASchB.TPAccMktDiscInt)
    
    If Index = 6 And GetNumber(IASchB.TotINTCopies) > 7 Then
        ReturnVal = GetCurrency(IAWBPInt.TotalExemptInt)
    ElseIf ResSFM > Index Then
        ReturnVal = 0
    ElseIf ResSFM + OthSFM > Index Then
        Stuff = (Index) - ResSFM
        ReturnVal = 0
    ElseIf ResSFM + OthSFM + OID > Index Then
        Stuff = (Index) - ResSFM - OthSFM
        ReturnVal = Round(GetCurrency(USD1099OID.USInt, (GetNumber(IAWBBump.OID(Stuff))))) + Round(GetCurrency(USD1099OID.StExempt, (GetNumber(IAWBBump.OID(Stuff))))) + Round(GetCurrency(USD1099OID.Nominee, (GetNumber(IAWBBump.OID(Stuff))))) + MaxValue(0, Round(GetCurrency(USD1099OID.BOIDAdjAmt, (GetNumber(IAWBBump.OID(Stuff))))))
    ElseIf ResSFM + OthSFM + OID + INT1099 > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID
        ReturnVal = Round(GetCurrency(USD1099INT.USInt, (GetNumber(IAWBBump.INT(Stuff))))) + Round(GetCurrency(USD1099INT.Nominee, (GetNumber(IAWBBump.INT(Stuff))))) + Round(GetCurrency(USD1099INT.AccruedInt, (GetNumber(IAWBBump.INT(Stuff))))) + Round(GetCurrency(USD1099INT.ABP, (GetNumber(IAWBBump.INT(Stuff))))) + Round(GetCurrency(USD1099INT.StateExmpt, (GetNumber(IAWBBump.INT(Stuff)))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099
        ReturnVal = GetCurrency(USDPartK1.NetStTEI, (GetNumber(IAWBBump.PartK1(Stuff)))) + GetCurrency(USDPartK1.FedStTEI, (GetNumber(IAWBBump.PartK1(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1
        ReturnVal = GetCurrency(USDSCorpK1.NetStTEI, (GetNumber(IAWBBump.SCorpK1(Stuff)))) + GetCurrency(USDSCorpK1.FedStTEI, (GetNumber(IAWBBump.SCorpK1(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1
        ReturnVal = GetCurrency(USDEstK1.NetStTEI, (GetNumber(IAWBBump.EstK1(Stuff)))) + GetCurrency(USDEstK1.FedStTEI, (GetNumber(IAWBBump.EstK1(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + GetBool(IASchB.TPAccMktDiscInt) > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1
        ReturnVal = 0
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - GetBool(IASchB.TPAccMktDiscInt)
        ReturnVal = 0
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt)
        ReturnVal = 0
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt)
        ReturnVal = 0
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay)
        ReturnVal = 0
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) + GetBool(IASchB.JtContigentPay) > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay) - GetBool(IASchB.SPContigentPay)
        ReturnVal = 0
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub IJ1_Calculation(Index As Integer)
    Dim Stuff As Integer
    Dim ResSFM As Integer
    Dim OthSFM As Integer
    Dim OID As Integer
    Dim INT1099 As Integer
    Dim PartK1 As Integer
    Dim SCorpK1 As Integer
    Dim EstK1 As Integer
    Dim TPAccMktDisc As Boolean
    
    ResSFM = GetNumber(IAWBBump.ResSFMNbr)
    OthSFM = GetNumber(IAWBBump.OthSFMNbr)
    OID = GetNumber(IAWBBump.OIDNbr)
    INT1099 = GetNumber(IAWBBump.INTNbr)
    PartK1 = GetNumber(IAWBBump.PartK1Nbr)
    SCorpK1 = GetNumber(IAWBBump.SCorpK1Nbr)
    EstK1 = GetNumber(IAWBBump.EstK1Nbr)
    TPAccMktDisc = GetBool(IASchB.TPAccMktDiscInt)
    
    If Index = 6 And GetNumber(IASchB.TotINTCopies) > 7 Then
        ReturnVal = 0
    ElseIf ResSFM > Index Then
        ReturnVal = GetBool(USDSFM.Joint, GetNumber(IAWBBump.ResSFM(Index)))
    ElseIf ResSFM + OthSFM > Index Then
        Stuff = (Index) - ResSFM
        ReturnVal = GetBool(USDSFM.Joint, (GetNumber(IAWBBump.OthSFM(Stuff))))
    ElseIf ResSFM + OthSFM + OID > Index Then
        Stuff = (Index) - ResSFM - OthSFM
        ReturnVal = GetBool(USD1099OID.Joint, (GetNumber(IAWBBump.OID(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID
        ReturnVal = GetBool(USD1099INT.Joint, (GetNumber(IAWBBump.Int(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099
        ReturnVal = GetBool(USDPartK1.Joint, (GetNumber(IAWBBump.PartK1(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1
        ReturnVal = GetBool(USDSCorpK1.Joint, (GetNumber(IAWBBump.SCorpK1(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1
        ReturnVal = GetBool(USDEstK1.Joint, (GetNumber(IAWBBump.EstK1(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1
        ReturnVal = 0
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc
        ReturnVal = 0
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt)
        ReturnVal = 1
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt)
        ReturnVal = 0
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay)
        ReturnVal = 0
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) + GetBool(IASchB.JtContigentPay) > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay) - GetBool(IASchB.SPContigentPay)
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub IntAcctOwner_Calculation(Index As Integer)
    If GetBool(IASchB.ITp1(Index)) = True Then
        ReturnVal = "Taxpayer"
    ElseIf GetBool(IASchB.ISp1(Index)) = True Then
        ReturnVal = "Spouse"
    ElseIf GetBool(IASchB.IJ1(Index)) = True Then
        ReturnVal = "Joint"
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub Interest_Calculation(Index As Integer)
    Dim Stuff As Integer
    Dim ResSFM As Integer
    Dim OthSFM As Integer
    Dim OID As Integer
    Dim INT1099 As Integer
    Dim PartK1 As Integer
    Dim SCorpK1 As Integer
    Dim EstK1 As Integer
    Dim TPAccMktDisc As Boolean
    
    ResSFM = GetNumber(IAWBBump.ResSFMNbr)
    OthSFM = GetNumber(IAWBBump.OthSFMNbr)
    OID = GetNumber(IAWBBump.OIDNbr)
    INT1099 = GetNumber(IAWBBump.INTNbr)
    PartK1 = GetNumber(IAWBBump.PartK1Nbr)
    SCorpK1 = GetNumber(IAWBBump.SCorpK1Nbr)
    EstK1 = GetNumber(IAWBBump.EstK1Nbr)
    TPAccMktDisc = GetBool(IASchB.TPAccMktDiscInt)
    
    If Index = 6 And GetNumber(IASchB.TotINTCopies) > 7 Then
        ReturnVal = GetCurrency(IAWBPInt.TotalInterest)
    ElseIf ResSFM > Index Then
        ReturnVal = Round(GetCurrency(USDSFM.Interest, GetNumber(IAWBBump.ResSFM(Index))))
    ElseIf ResSFM + OthSFM > Index Then
        Stuff = (Index) - ResSFM
        ReturnVal = Round(GetCurrency(USDSFM.Interest, (GetNumber(IAWBBump.OthSFM(Stuff)))))
    ElseIf ResSFM + OthSFM + OID > Index Then
        Stuff = (Index) - ResSFM - OthSFM
        ReturnVal = GetCurrency(USD1099OID.BAmt, (GetNumber(IAWBBump.OID(Stuff)))) + Round(GetCurrency(USD1099OID.TaxExempt, (GetNumber(IAWBBump.OID(Stuff))))) - MinValue(0, Round(GetCurrency(USD1099OID.BOIDAdjAmt, (GetNumber(IAWBBump.OID(Stuff))))))
    ElseIf ResSFM + OthSFM + OID + INT1099 > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID
        ReturnVal = GetCurrency(USD1099INT.BAmtEF, (GetNumber(IAWBBump.INT(Stuff)))) + GetCurrency(USD1099INT.FedExmpt, (GetNumber(IAWBBump.INT(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099
        ReturnVal = GetCurrency(USDPartK1.HaveInt, (GetNumber(IAWBBump.PartK1(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1
        ReturnVal = GetCurrency(USDSCorpK1.HaveInt, (GetNumber(IAWBBump.SCorpK1(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1
        ReturnVal = GetCurrency(USDEstK1.HaveInt, (GetNumber(IAWBBump.EstK1(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1
        ReturnVal = GetCurrency(IASchB.TPAccMktDiscInt)
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc
        ReturnVal = GetCurrency(IASchB.SPAccMktDiscInt)
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt)
        ReturnVal = GetCurrency(IASchB.JtAccMktDiscInt)
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt)
        ReturnVal = GetCurrency(IASchB.TPContigentPay)
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay)
        ReturnVal = GetCurrency(IASchB.SPContigentPay)
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) + GetBool(IASchB.JtContigentPay) > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay) - GetBool(IASchB.SPContigentPay)
        ReturnVal = GetCurrency(IASchB.JtContigentPay)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub ISp1_Calculation(Index As Integer)
    Dim Stuff As Integer
    Dim ResSFM As Integer
    Dim OthSFM As Integer
    Dim OID As Integer
    Dim INT1099 As Integer
    Dim PartK1 As Integer
    Dim SCorpK1 As Integer
    Dim EstK1 As Integer
    Dim TPAccMktDisc As Boolean
    
    ResSFM = GetNumber(IAWBBump.ResSFMNbr)
    OthSFM = GetNumber(IAWBBump.OthSFMNbr)
    OID = GetNumber(IAWBBump.OIDNbr)
    INT1099 = GetNumber(IAWBBump.INTNbr)
    PartK1 = GetNumber(IAWBBump.PartK1Nbr)
    SCorpK1 = GetNumber(IAWBBump.SCorpK1Nbr)
    EstK1 = GetNumber(IAWBBump.EstK1Nbr)
    TPAccMktDisc = GetBool(IASchB.TPAccMktDiscInt)
    
    If Index = 6 And GetNumber(IASchB.TotINTCopies) > 7 Then
        ReturnVal = 0
    ElseIf ResSFM > Index Then
        ReturnVal = GetBool(USDSFM.Spouse, GetNumber(IAWBBump.ResSFM(Index)))
    ElseIf ResSFM + OthSFM > Index Then
        Stuff = (Index) - ResSFM
        ReturnVal = GetBool(USDSFM.Spouse, (GetNumber(IAWBBump.OthSFM(Stuff))))
    ElseIf ResSFM + OthSFM + OID > Index Then
        Stuff = (Index) - ResSFM - OthSFM
        ReturnVal = GetBool(USD1099OID.Spouse, (GetNumber(IAWBBump.OID(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID
        ReturnVal = GetBool(USD1099INT.Spouse, (GetNumber(IAWBBump.Int(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099
        ReturnVal = GetBool(USDPartK1.Spouse, (GetNumber(IAWBBump.PartK1(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1
        ReturnVal = GetBool(USDSCorpK1.Spouse, (GetNumber(IAWBBump.SCorpK1(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1
        ReturnVal = GetBool(USDEstK1.Spouse, (GetNumber(IAWBBump.EstK1(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1
        ReturnVal = 0
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc
        ReturnVal = 1
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt)
        ReturnVal = 0
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt)
        ReturnVal = 0
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay)
        ReturnVal = 1
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) + GetBool(IASchB.JtContigentPay) > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay) - GetBool(IASchB.SPContigentPay)
        ReturnVal = 0
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub ITp1_Calculation(Index As Integer)
    Dim Stuff As Integer
    Dim ResSFM As Integer
    Dim OthSFM As Integer
    Dim OID As Integer
    Dim INT1099 As Integer
    Dim PartK1 As Integer
    Dim SCorpK1 As Integer
    Dim EstK1 As Integer
    Dim TPAccMktDisc As Boolean
    
    ResSFM = GetNumber(IAWBBump.ResSFMNbr)
    OthSFM = GetNumber(IAWBBump.OthSFMNbr)
    OID = GetNumber(IAWBBump.OIDNbr)
    INT1099 = GetNumber(IAWBBump.INTNbr)
    PartK1 = GetNumber(IAWBBump.PartK1Nbr)
    SCorpK1 = GetNumber(IAWBBump.SCorpK1Nbr)
    EstK1 = GetNumber(IAWBBump.EstK1Nbr)
    TPAccMktDisc = GetBool(IASchB.TPAccMktDiscInt)
    
    If Index = 6 And GetNumber(IASchB.TotINTCopies) > 7 Then
        ReturnVal = 0
    ElseIf ResSFM > Index Then
        ReturnVal = GetBool(USDSFM.Taxpayer, GetNumber(IAWBBump.ResSFM(Index)))
    ElseIf ResSFM + OthSFM > Index Then
        Stuff = (Index) - ResSFM
        ReturnVal = GetBool(USDSFM.Taxpayer, (GetNumber(IAWBBump.OthSFM(Stuff))))
    ElseIf ResSFM + OthSFM + OID > Index Then
        Stuff = (Index) - ResSFM - OthSFM
        ReturnVal = GetBool(USD1099OID.Taxpayer, (GetNumber(IAWBBump.OID(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID
        ReturnVal = GetBool(USD1099INT.Taxpayer, (GetNumber(IAWBBump.Int(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099
        ReturnVal = GetBool(USDPartK1.Taxpayer, (GetNumber(IAWBBump.PartK1(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1
        ReturnVal = GetBool(USDSCorpK1.Taxpayer, (GetNumber(IAWBBump.SCorpK1(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1
        ReturnVal = GetBool(USDEstK1.Taxpayer, (GetNumber(IAWBBump.EstK1(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1
        ReturnVal = 1
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc
        ReturnVal = 0
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt)
        ReturnVal = 0
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt)
        ReturnVal = 1
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay)
        ReturnVal = 0
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) + GetBool(IASchB.JtContigentPay) > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay) - GetBool(IASchB.SPContigentPay)
        ReturnVal = 0
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub JtAccMktDiscInt_Calculation()
    Dim count As Integer
    Dim Lim As Integer
    Dim Total As Currency
    
    Lim = GetAllCopies(USDCapGain)
    count = 1
    Total = 0
    
    Do While count <= Lim
        If GetBool(USDCapGain.Joint, count) = True And GetCurrency(USDCapGain.IntIncome, count) > 0 Then
            Total = Total + GetCurrency(USDCapGain.IntIncome, count)
        Else
            Total = Total
        End If
        
        count = count + 1
    Loop
    
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = Total
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub JtContigentPay_Calculation()
    Dim count As Integer
    Dim Lim As Integer
    Dim Total As Currency
    
    Lim = GetAllCopies(USDCapGain)
    count = 1
    Total = 0
    
    Do While count <= Lim
        If GetBool(USDCapGain.Joint, count) = True And GetBool(USDCapGain.Ordinary, count) = True Then
            Total = Total + GetCurrency(USDCapGain.OrdGain, count) - GetCurrency(USDCapGain.OrdLoss, count)
        Else
            Total = Total
        End If
        
        count = count + 1
    Loop
    
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = Total
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.CombNames)
End Sub

Private Sub Payer_Calculation(Index As Integer)
    Dim Stuff As Integer
    Dim ResSFM As Integer
    Dim OthSFM As Integer
    Dim OID As Integer
    Dim INT1099 As Integer
    Dim PartK1 As Integer
    Dim SCorpK1 As Integer
    Dim EstK1 As Integer
    Dim TPAccMktDisc As Boolean
    
    ResSFM = GetNumber(IAWBBump.ResSFMNbr)
    OthSFM = GetNumber(IAWBBump.OthSFMNbr)
    OID = GetNumber(IAWBBump.OIDNbr)
    INT1099 = GetNumber(IAWBBump.INTNbr)
    PartK1 = GetNumber(IAWBBump.PartK1Nbr)
    SCorpK1 = GetNumber(IAWBBump.SCorpK1Nbr)
    EstK1 = GetNumber(IAWBBump.EstK1Nbr)
    TPAccMktDisc = GetBool(IASchB.TPAccMktDiscInt)
    
    If Index = 6 And GetNumber(IASchB.TotINTCopies) > 7 Then
        ReturnVal = "See Statement Attached"
    ElseIf ResSFM > Index Then
        ReturnVal = GetString(USDSFM.NameAdd, GetNumber(IAWBBump.ResSFM(Index)))
    ElseIf ResSFM + OthSFM > Index Then
        Stuff = (Index) - ResSFM
        ReturnVal = GetString(USDSFM.PayerName, (GetNumber(IAWBBump.OthSFM(Stuff))))
    ElseIf ResSFM + OthSFM + OID > Index Then
        Stuff = (Index) - ResSFM - OthSFM
        ReturnVal = GetString(USD1099OID.PayerName, (GetNumber(IAWBBump.OID(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID
        ReturnVal = GetString(USD1099INT.PayerName, (GetNumber(IAWBBump.Int(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099
        ReturnVal = GetString(USDPartK1.CoName, (GetNumber(IAWBBump.PartK1(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1
        ReturnVal = GetString(USDSCorpK1.CoName, (GetNumber(IAWBBump.SCorpK1(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1
        ReturnVal = GetString(USDEstK1.TrustName, (GetNumber(IAWBBump.EstK1(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1
        ReturnVal = "Accrued Market Discount"
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc
        ReturnVal = "Accrued Market Discount"
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt)
        ReturnVal = "Accrued Market Discount"
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt)
        ReturnVal = "Contingent Payment Debt Instrument"
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay)
        ReturnVal = "Contingent Payment Debt Instrument"
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) + GetBool(IASchB.JtContigentPay) > Index Then
        Stuff = (Index) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay) - GetBool(IASchB.SPContigentPay)
        ReturnVal = "Contingent Payment Debt Instrument"
    Else
        ReturnVal = ""
    End If

End Sub

Private Sub PrintIAB_Calculation()
    If GetCurrency(IASchB.TotalInterest) > 1500@ Or GetCurrency(IASchB.TotalDividend) > 1500@ Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPAccMktDiscInt_Calculation()
    Dim count As Integer
    Dim Lim As Integer
    Dim Total As Currency
    
    Lim = GetAllCopies(USDCapGain)
    count = 1
    Total = 0
    
    Do While count <= Lim
        If GetBool(USDCapGain.Spouse, count) = True And GetCurrency(USDCapGain.IntIncome, count) > 0 Then
            Total = Total + GetCurrency(USDCapGain.IntIncome, count)
        Else
            Total = Total
        End If
        
        count = count + 1
    Loop
    
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = Total
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SPContigentPay_Calculation()
    Dim count As Integer
    Dim Lim As Integer
    Dim Total As Currency
    
    Lim = GetAllCopies(USDCapGain)
    count = 1
    Total = 0
    
    Do While count <= Lim
        If GetBool(USDCapGain.Spouse, count) = True And GetBool(USDCapGain.Ordinary, count) = True Then
            Total = Total + GetCurrency(USDCapGain.OrdGain, count) - GetCurrency(USDCapGain.OrdLoss, count)
        Else
            Total = Total
        End If
        
        count = count + 1
    Loop
    
    If GetBool(IARequired.AskSpouse) = True Then
        ReturnVal = Total
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

Private Sub TaxDiv_Calculation(Index As Integer)
    ReturnVal = MaxValue(0, GetCurrency(IASchB.Dividend(Index)) - GetCurrency(IASchB.ExemptDiv(Index)))
End Sub

Private Sub TaxInt_Calculation(Index As Integer)
    ReturnVal = MaxValue(0, GetCurrency(IASchB.Interest(Index)) - GetCurrency(IASchB.ExemptInt(Index)))
End Sub

Private Sub TotAccMktDiscInt_Calculation()
    Dim count As Integer
    Dim Lim As Integer
    Dim Total As Currency
    
    Lim = GetAllCopies(USDCapGain)
    count = 1
    Total = 0
    
    Do While count <= Lim
        If GetCurrency(USDCapGain.IntIncome, count) > 0 Then
            Total = Total + GetCurrency(USDCapGain.IntIncome, count)
        Else
            Total = Total
        End If
        
        count = count + 1
    Loop
    
    ReturnVal = Round(Total)
End Sub

Private Sub TotalDividend_Calculation()
    Dim count As Integer
    Dim SubTot As Currency

    count = 0
    SubTot = 0

    Do While count < 7
        SubTot = SubTot + GetCurrency(IASchB.Dividend(count))
        count = count + 1
    Loop
    
    ReturnVal = SubTot
End Sub

Private Sub TotalExemptDiv_Calculation()
    Dim count As Integer
    Dim SubTot As Currency

    count = 0
    SubTot = 0

    Do While count < 7
        SubTot = SubTot + GetCurrency(IASchB.ExemptDiv(count))
        count = count + 1
    Loop
    
    ReturnVal = SubTot
End Sub

Private Sub TotalExemptInt_Calculation()
    Dim count As Integer
    Dim SubTot As Currency

    count = 0
    SubTot = 0

    Do While count < 7
        SubTot = SubTot + GetCurrency(IASchB.ExemptInt(count))
        count = count + 1
    Loop
    
    ReturnVal = SubTot
End Sub

Private Sub TotalInterest_Calculation()
    Dim count As Integer
    Dim SubTot As Currency

    count = 0
    SubTot = 0

    Do While count < 7
        SubTot = SubTot + GetCurrency(IASchB.Interest(count))
        count = count + 1
    Loop
    
    ReturnVal = SubTot
End Sub

Private Sub TotalTaxDiv_Calculation()
    Dim count As Integer
    Dim SubTot As Currency

    count = 0
    SubTot = 0

    Do While count < 7
        SubTot = SubTot + GetCurrency(IASchB.TaxDiv(count))
        count = count + 1
    Loop
    
    ReturnVal = SubTot
End Sub

Private Sub TotalTaxInt_Calculation()
    Dim count As Integer
    Dim SubTot As Currency

    count = 0
    SubTot = 0

    Do While count < 7
        SubTot = SubTot + GetCurrency(IASchB.TaxInt(count))
        count = count + 1
    Loop
    
    ReturnVal = SubTot
End Sub

Private Sub TotContigentPay_Calculation()
    Dim count As Integer
    Dim Lim As Integer
    Dim Total As Currency
    
    Lim = GetAllCopies(USDCapGain)
    count = 1
    Total = 0
    
    Do While count <= Lim
        If GetBool(USDCapGain.Ordinary, count) = True Then
            Total = Total + GetCurrency(USDCapGain.OrdGain, count) - GetCurrency(USDCapGain.OrdLoss, count)
        Else
            Total = Total
        End If
        
        count = count + 1
    Loop
    
    ReturnVal = Round(Total)
End Sub

Private Sub TotDIVCopies_Calculation()
    ReturnVal = GetNumber(IAWBBump.DIVNbr) + GetNumber(IAWBBump.PartK1DivNbr) + GetNumber(IAWBBump.SCorpK1DivNbr) + GetNumber(IAWBBump.EstK1DivNbr) + GetNumber(IAWBBump.F5471Nbr) + GetNumber(IAWBBump.F8621Nbr) + GetNumber(IAWBBump.F8814Nbr)
End Sub

Private Sub TotINTCopies_Calculation()
    ReturnVal = GetNumber(IAWBBump.ResSFMNbr) + GetNumber(IAWBBump.OthSFMNbr) + GetNumber(IAWBBump.OIDNbr) + GetNumber(IAWBBump.INTNbr) + GetNumber(IAWBBump.PartK1Nbr) + GetNumber(IAWBBump.SCorpK1Nbr) + GetNumber(IAWBBump.EstK1Nbr) + GetNumber(IASchB.AccMktDiscIntCopies) + GetNumber(IASchB.ContigentPayCopies)
End Sub

Private Sub TPAccMktDiscInt_Calculation()
    ReturnVal = GetCurrency(IASchB.TotAccMktDiscInt) - GetCurrency(IASchB.SPAccMktDiscInt) - GetCurrency(IASchB.JtAccMktDiscInt)
End Sub

Private Sub TPContigentPay_Calculation()
    ReturnVal = GetCurrency(IASchB.TotContigentPay) - GetCurrency(IASchB.SPContigentPay) - GetCurrency(IASchB.JtContigentPay)
End Sub

