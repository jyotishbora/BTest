Private Sub Desc_Calculation()
    ReturnVal = CStr(GetCurrency(IAWBPDiv.TotalDividend)) & " Additional Dividends"
End Sub

Private Sub DivAcctOwner_Calculation(Index As Integer)
    If GetBool(IAWBPDiv.DTp1(Index)) = True Then
        ReturnVal = "Taxpayer"
    ElseIf GetBool(IAWBPDiv.DSp1(Index)) = True Then
        ReturnVal = "Spouse"
    ElseIf GetBool(IAWBPDiv.DJ1(Index)) = True Then
        ReturnVal = "Joint"
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub Dividend_Calculation(Index As Integer)
    Dim Stuff As Integer
    Dim MoStuff As Integer
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
    
    MoStuff = Index + GetNumber(IAWBPDiv.Offset)
    
    If GetNumber(IASchB.TotDIVCopies) = 7 Then
        ReturnVal = 0
    ElseIf DIV > MoStuff Then
        ReturnVal = Round(GetCurrency(USD1099DIV.ORDDIV, GetNumber(IAWBBump.DIV(MoStuff)))) + Round(GetCurrency(USD1099DIV.FedExmpt, GetNumber(IAWBBump.DIV(MoStuff))))
    ElseIf DIV + PartK1 > MoStuff Then
        Stuff = (MoStuff) - DIV
        ReturnVal = GetCurrency(USDPartK1.Dividends, (GetNumber(IAWBBump.PartK1Div(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 > MoStuff Then
        Stuff = (MoStuff) - DIV - PartK1
        ReturnVal = GetCurrency(USDSCorpK1.Dividends, (GetNumber(IAWBBump.SCorpK1Div(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 > MoStuff Then
        Stuff = (MoStuff) - DIV - PartK1 - SCorpK1
        ReturnVal = GetCurrency(USDEstK1.Dividends, (GetNumber(IAWBBump.EstK1Div(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 + F5471 > MoStuff Then
        Stuff = (MoStuff) - DIV - PartK1 - SCorpK1 - EstK1
        ReturnVal = GetCurrency(USW5471SchI.DivOrd, (GetNumber(IAWBBump.F5471(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 > MoStuff Then
        Stuff = (MoStuff) - DIV - PartK1 - SCorpK1 - EstK1 - F5471
        ReturnVal = GetCurrency(USF8621.DivTo1040, (GetNumber(IAWBBump.F8621(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 + F8814 > MoStuff Then
        Stuff = (MoStuff) - DIV - PartK1 - SCorpK1 - EstK1 - F5471 - F8621
        ReturnVal = GetCurrency(USF8814.L6XL7, (GetNumber(IAWBBump.F8814(Stuff))))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub DivNoPayer_Calculation()
    Dim count, Iter As Integer
    
    count = 0
    Iter = 0
    Do While Iter < 22
        If GetCurrency(IAWBPDiv.Dividend(Iter)) > 0 And Trim(GetString(IAWBPDiv.DivPayer(Iter))) = "" Then
            count = count + 1
        End If
        Iter = Iter + 1
    Loop
    
    If GetBool(IAWBPDiv.Print) = True And count > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub DivPayer_Calculation(Index As Integer)
    Dim Stuff As Integer
    Dim MoStuff As Integer
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
    
    MoStuff = Index + GetNumber(IAWBPDiv.Offset)
    
    If GetNumber(IASchB.TotDIVCopies) = 7 Then
        ReturnVal = ""
    ElseIf DIV > MoStuff Then
        ReturnVal = GetString(USD1099DIV.PayerName, GetNumber(IAWBBump.DIV(MoStuff)))
    ElseIf DIV + PartK1 > MoStuff Then
        Stuff = (MoStuff) - DIV
        ReturnVal = GetString(USDPartK1.CoName, (GetNumber(IAWBBump.PartK1Div(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 > MoStuff Then
        Stuff = (MoStuff) - DIV - PartK1
        ReturnVal = GetString(USDSCorpK1.CoName, (GetNumber(IAWBBump.SCorpK1Div(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 > MoStuff Then
        Stuff = (MoStuff) - DIV - PartK1 - SCorpK1
        ReturnVal = GetString(USDEstK1.TrustName, (GetNumber(IAWBBump.EstK1Div(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 + F5471 > MoStuff Then
        Stuff = (MoStuff) - DIV - PartK1 - SCorpK1 - EstK1
        ReturnVal = "Form 5471"
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 > MoStuff Then
        Stuff = (MoStuff) - DIV - PartK1 - SCorpK1 - EstK1 - F5471
        ReturnVal = "Form 8621 - " & GetString(USF8621.CoName, (GetNumber(IAWBBump.F8621(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 + F8814 > MoStuff Then
        Stuff = (MoStuff) - DIV - PartK1 - SCorpK1 - EstK1 - F5471 - F8621
        ReturnVal = "Form 8814 - " & GetString(USF8814.ChName, (GetNumber(IAWBBump.F8814(Stuff))))
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub DJ1_Calculation(Index As Integer)
    Dim Stuff As Integer
    Dim MoStuff As Integer
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
    
    MoStuff = Index + GetNumber(IAWBPDiv.Offset)
    
    If GetNumber(IASchB.TotDIVCopies) = 7 Then
        ReturnVal = 0
    ElseIf DIV > MoStuff Then
        ReturnVal = GetBool(USD1099DIV.Joint, GetNumber(IAWBBump.DIV(MoStuff)))
    ElseIf DIV + PartK1 > MoStuff Then
        Stuff = (MoStuff) - DIV
        ReturnVal = GetBool(USDPartK1.Joint, (GetNumber(IAWBBump.PartK1Div(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 > MoStuff Then
        Stuff = (MoStuff) - DIV - PartK1
        ReturnVal = GetBool(USDSCorpK1.Joint, (GetNumber(IAWBBump.SCorpK1Div(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 > MoStuff Then
        Stuff = (MoStuff) - DIV - PartK1 - SCorpK1
        ReturnVal = GetBool(USDEstK1.Joint, (GetNumber(IAWBBump.EstK1Div(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 + F5471 > MoStuff Then
        Stuff = (MoStuff) - DIV - PartK1 - SCorpK1 - EstK1
        ReturnVal = 0
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 > MoStuff Then
        Stuff = (MoStuff) - DIV - PartK1 - SCorpK1 - EstK1 - F5471
        ReturnVal = GetBool(USF8621.Joint, (GetNumber(IAWBBump.F8621(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 + F8814 > MoStuff Then
        Stuff = (MoStuff) - DIV - PartK1 - SCorpK1 - EstK1 - F5471 - F8621
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
    Dim MoStuff As Integer
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
    
    MoStuff = Index + GetNumber(IAWBPDiv.Offset)
    
    If GetNumber(IASchB.TotDIVCopies) = 7 Then
        ReturnVal = 0
    ElseIf DIV > MoStuff Then
        ReturnVal = GetBool(USD1099DIV.Spouse, GetNumber(IAWBBump.DIV(MoStuff)))
    ElseIf DIV + PartK1 > MoStuff Then
        Stuff = (MoStuff) - DIV
        ReturnVal = GetBool(USDPartK1.Spouse, (GetNumber(IAWBBump.PartK1Div(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 > MoStuff Then
        Stuff = (MoStuff) - DIV - PartK1
        ReturnVal = GetBool(USDSCorpK1.Spouse, (GetNumber(IAWBBump.SCorpK1Div(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 > MoStuff Then
        Stuff = (MoStuff) - DIV - PartK1 - SCorpK1
        ReturnVal = GetBool(USDEstK1.Spouse, (GetNumber(IAWBBump.EstK1Div(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 + F5471 > MoStuff Then
        Stuff = (MoStuff) - DIV - PartK1 - SCorpK1 - EstK1
        If GetString(USW5471SchI.SchISSN, (GetNumber(IAWBBump.F5471(Stuff)))) = GetString(USWBasicInfo.SpouseSSN) Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 > MoStuff Then
        Stuff = (MoStuff) - DIV - PartK1 - SCorpK1 - EstK1 - F5471
        ReturnVal = GetBool(USF8621.Spouse, (GetNumber(IAWBBump.F8621(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 + F8814 > MoStuff Then
        Stuff = (MoStuff) - DIV - PartK1 - SCorpK1 - EstK1 - F5471 - F8621
        ReturnVal = 0
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub DTp1_Calculation(Index As Integer)
    Dim Stuff As Integer
    Dim MoStuff As Integer
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
    
    MoStuff = Index + GetNumber(IAWBPDiv.Offset)
    
    If GetNumber(IASchB.TotDIVCopies) = 7 Then
        ReturnVal = 0
    ElseIf DIV > MoStuff Then
        ReturnVal = GetBool(USD1099DIV.Taxpayer, GetNumber(IAWBBump.DIV(MoStuff)))
    ElseIf DIV + PartK1 > MoStuff Then
        Stuff = (MoStuff) - DIV
        ReturnVal = GetBool(USDPartK1.Taxpayer, (GetNumber(IAWBBump.PartK1Div(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 > MoStuff Then
        Stuff = (MoStuff) - DIV - PartK1
        ReturnVal = GetBool(USDSCorpK1.Taxpayer, (GetNumber(IAWBBump.SCorpK1Div(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 > MoStuff Then
        Stuff = (MoStuff) - DIV - PartK1 - SCorpK1
        ReturnVal = GetBool(USDEstK1.Taxpayer, (GetNumber(IAWBBump.EstK1Div(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 + F5471 > MoStuff Then
        Stuff = (MoStuff) - DIV - PartK1 - SCorpK1 - EstK1
        If GetString(USW5471SchI.SchISSN, (GetNumber(IAWBBump.F5471(Stuff)))) = GetString(USWBasicInfo.SSN) Then
            ReturnVal = 1
        Else
            ReturnVal = 0
        End If
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 > MoStuff Then
        Stuff = (MoStuff) - DIV - PartK1 - SCorpK1 - EstK1 - F5471
        ReturnVal = GetBool(USF8621.Taxpayer, (GetNumber(IAWBBump.F8621(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 + F8814 > MoStuff Then
        Stuff = (MoStuff) - DIV - PartK1 - SCorpK1 - EstK1 - F5471 - F8621
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
    Dim MoStuff As Integer
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
    
    MoStuff = Index + GetNumber(IAWBPDiv.Offset)
    
    If GetNumber(IASchB.TotDIVCopies) = 7 Then
        ReturnVal = 0
    ElseIf DIV > MoStuff Then
        ReturnVal = Round(GetCurrency(USD1099DIV.Nominee, GetNumber(IAWBBump.DIV(MoStuff)))) + Round(GetCurrency(USD1099DIV.StExmpt, GetNumber(IAWBBump.DIV(MoStuff)))) + Round(GetCurrency(USD1099DIV.FedStExmpt, GetNumber(IAWBBump.DIV(MoStuff)))) + Round(GetCurrency(USD1099DIV.Restricted, GetNumber(IAWBBump.DIV(MoStuff))))
    ElseIf DIV + PartK1 > MoStuff Then
        Stuff = (MoStuff) - DIV
        ReturnVal = GetCurrency(USDPartK1.NetStTED, (GetNumber(IAWBBump.PartK1Div(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 > MoStuff Then
        Stuff = (MoStuff) - DIV - PartK1
        ReturnVal = GetCurrency(USDSCorpK1.NetStTED, (GetNumber(IAWBBump.SCorpK1Div(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 > MoStuff Then
        Stuff = (MoStuff) - DIV - PartK1 - SCorpK1
        ReturnVal = GetCurrency(USDEstK1.NetStTED, (GetNumber(IAWBBump.EstK1Div(Stuff))))
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 + F5471 > MoStuff Then
        Stuff = (MoStuff) - DIV - PartK1 - SCorpK1 - EstK1
        ReturnVal = 0
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 > MoStuff Then
        Stuff = (MoStuff) - DIV - PartK1 - SCorpK1 - EstK1 - F5471
        ReturnVal = 0
    ElseIf DIV + PartK1 + SCorpK1 + EstK1 + F5471 + F8621 + F8814 > MoStuff Then
        Stuff = (MoStuff) - DIV - PartK1 - SCorpK1 - EstK1 - F5471 - F8621
        ReturnVal = 0
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Exist_Calculation()
    ReturnVal = 1
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.CombNames)
End Sub

Private Sub Offset_Calculation()
    If GetCopy() = 1 Then
        ReturnVal = 6
    ElseIf GetCopy() = 2 Then
        ReturnVal = 28
    ElseIf GetCopy() = 3 Then
        ReturnVal = 50
    ElseIf GetCopy() = 4 Then
        ReturnVal = 72
    ElseIf GetCopy() = 5 Then
        ReturnVal = 94
    ElseIf GetCopy() = 6 Then
        ReturnVal = 116
    ElseIf GetCopy() = 7 Then
        ReturnVal = 138
    ElseIf GetCopy() = 8 Then
        ReturnVal = 160
    ElseIf GetCopy() = 9 Then
        ReturnVal = 182
    ElseIf GetCopy() = 10 Then
        ReturnVal = 204
    Else
        ReturnVal = 226
    End If
End Sub

Private Sub Print_Calculation()
    If GetNumber(IASchB.PrintIAB) = 1 And GetCurrency(IAWBPDiv.TotalDividend) <> 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

Private Sub TaxDiv_Calculation(Index As Integer)
    ReturnVal = MaxValue(0, GetCurrency(IAWBPDiv.Dividend(Index)) - GetCurrency(IAWBPDiv.ExemptDiv(Index)))
End Sub

Private Sub TotalDividend_Calculation()
    Dim count As Integer
    Dim SubTot As Currency

    count = 0
    SubTot = 0

    Do While count < 22
        SubTot = SubTot + GetCurrency(IAWBPDiv.Dividend(count))
        count = count + 1
    Loop
    
    ReturnVal = SubTot
End Sub

Private Sub TotalExemptDiv_Calculation()
    Dim count As Integer
    Dim SubTot As Currency

    count = 0
    SubTot = 0

    Do While count < 22
        SubTot = SubTot + GetCurrency(IAWBPDiv.ExemptDiv(count))
        count = count + 1
    Loop
    
    ReturnVal = SubTot
End Sub

Private Sub TotalTaxDiv_Calculation()
    Dim count As Integer
    Dim SubTot As Currency

    count = 0
    SubTot = 0

    Do While count < 22
        SubTot = SubTot + GetCurrency(IAWBPDiv.TaxDiv(count))
        count = count + 1
    Loop
    
    ReturnVal = SubTot
End Sub

