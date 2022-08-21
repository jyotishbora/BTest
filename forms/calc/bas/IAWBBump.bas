Private Sub DIV_Calculation(Index As Integer)
    Dim count As Long
    Dim max As Long
    Dim listedcount As Long
    
    listedcount = 0
    max = GetAllCopies(USD1099DIV)
    count = 0
    
    Do While count < max
        count = count + 1
        If GetCurrency(USD1099DIV.OrdDiv, count) + GetCurrency(USD1099DIV.FedExmpt, count) > 0 Then
            If listedcount = Index Then
                ReturnVal = count
            Else
                listedcount = listedcount + 1
            End If
        End If
    Loop
        
    ReturnVal = 0
End Sub

Private Sub DIVNbr_Calculation()
    Dim count As Integer
    Dim Lim As Integer
    Dim Total As Integer
    
    Lim = GetAllCopies(USD1099DIV)
    count = 1
    Total = 0
    
    Do While count <= Lim
        If GetCurrency(USD1099DIV.OrdDiv, count) + GetCurrency(USD1099DIV.FedExmpt, count) > 0 Then
            Total = Total + 1
        Else
            Total = Total
        End If
        
        count = count + 1
    Loop
    
    ReturnVal = Total
End Sub

Private Sub EstK1_Calculation(Index As Integer)
    Dim count As Long
    Dim max As Long
    Dim listedcount As Long
    
    listedcount = 0
    max = GetAllCopies(USDEstK1)
    count = 0
    
    Do While count < max
        count = count + 1
        If GetCurrency(USDEstK1.HaveInt, count) > 0 Then
            If listedcount = Index Then
                ReturnVal = count
            Else
                listedcount = listedcount + 1
            End If
        End If
    Loop
        
    ReturnVal = 0
End Sub

Private Sub EstK1Div_Calculation(Index As Integer)
    Dim count As Long
    Dim max As Long
    Dim listedcount As Long
    
    listedcount = 0
    max = GetAllCopies(USDEstK1)
    count = 0
    
    Do While count < max
        count = count + 1
        If GetCurrency(USDEstK1.Dividends, count) > 0 Then
            If listedcount = Index Then
                ReturnVal = count
            Else
                listedcount = listedcount + 1
            End If
        End If
    Loop
        
    ReturnVal = 0
End Sub

Private Sub EstK1DivNbr_Calculation()
    Dim count As Integer
    Dim Lim As Integer
    Dim Total As Integer
    
    Lim = GetAllCopies(USDEstK1)
    count = 1
    Total = 0
    
    Do While count <= Lim
        If GetCurrency(USDEstK1.Dividends, count) > 0 Then
            Total = Total + 1
        Else
            Total = Total
        End If
        
        count = count + 1
    Loop
    
    ReturnVal = Total
End Sub

Private Sub EstK1Nbr_Calculation()
    Dim count As Integer
    Dim Lim As Integer
    Dim Total As Integer
    
    Lim = GetAllCopies(USDEstK1)
    count = 1
    Total = 0
    
    Do While count <= Lim
        If GetCurrency(USDEstK1.HaveInt, count) > 0 Then
            Total = Total + 1
        Else
            Total = Total
        End If
        
        count = count + 1
    Loop
    
    ReturnVal = Total
End Sub

Private Sub F5471_Calculation(Index As Integer)
    Dim count As Long
    Dim max As Long
    Dim listedcount As Long
    
    listedcount = 0
    max = GetAllCopies(USW5471SchI)
    count = 0
    
    Do While count < max
        count = count + 1
        If GetCurrency(USW5471SchI.DivOrd, count) > 0 And ((GetString(USW5471SchI.SchISSN, count) = GetString(USWBasicInfo.SSN)) Or (GetString(USW5471SchI.SchISSN, count) = GetString(USWBasicInfo.SpouseSSN))) Then
            If listedcount = Index Then
                ReturnVal = count
            Else
                listedcount = listedcount + 1
            End If
        End If
    Loop
        
    ReturnVal = 0
End Sub

Private Sub F5471Nbr_Calculation()
    Dim count As Integer
    Dim Lim As Integer
    Dim Total As Integer
    
    Lim = GetAllCopies(USW5471SchI)
    count = 1
    Total = 0
    
    Do While count <= Lim
        If GetCurrency(USW5471SchI.DivOrd, count) > 0 And ((GetString(USW5471SchI.SchISSN, count) = GetString(USWBasicInfo.SSN)) Or (GetString(USW5471SchI.SchISSN, count) = GetString(USWBasicInfo.SpouseSSN))) Then
            Total = Total + 1
        Else
            Total = Total
        End If
        
        count = count + 1
    Loop
    
    ReturnVal = Total
End Sub

Private Sub F8621_Calculation(Index As Integer)
    Dim count As Long
    Dim max As Long
    Dim listedcount As Long
    
    listedcount = 0
    max = GetAllCopies(USF8621)
    count = 0
    
    Do While count < max
        count = count + 1
        If GetCurrency(USF8621.DivTo1040, count) > 0 Then
            If listedcount = Index Then
                ReturnVal = count
            Else
                listedcount = listedcount + 1
            End If
        End If
    Loop
        
    ReturnVal = 0
End Sub

Private Sub F8621Nbr_Calculation()
    Dim count As Integer
    Dim Lim As Integer
    Dim Total As Integer
    
    Lim = GetAllCopies(USF8621)
    count = 1
    Total = 0
    
    Do While count <= Lim
        If GetCurrency(USF8621.DivTo1040, count) > 0 Then
            Total = Total + 1
        Else
            Total = Total
        End If
        
        count = count + 1
    Loop
    
    ReturnVal = Total
End Sub

Private Sub F8814_Calculation(Index As Integer)
    Dim count As Long
    Dim max As Long
    Dim listedcount As Long
    
    listedcount = 0
    max = GetAllCopies(USF8814)
    count = 0
    
    Do While count < max
        count = count + 1
        If GetCurrency(USF8814.L6XL7, count) > 0 Then
            If listedcount = Index Then
                ReturnVal = count
            Else
                listedcount = listedcount + 1
            End If
        End If
    Loop
        
    ReturnVal = 0
End Sub

Private Sub F8814Nbr_Calculation()
    Dim count As Integer
    Dim Lim As Integer
    Dim Total As Integer
    
    Lim = GetAllCopies(USF8814)
    count = 1
    Total = 0
    
    Do While count <= Lim
        If GetCurrency(USF8814.L6XL7, count) > 0 Then
            Total = Total + 1
        Else
            Total = Total
        End If
        
        count = count + 1
    Loop
    
    ReturnVal = Total
End Sub

Private Sub INT_Calculation(Index As Integer)
    Dim count As Long
    Dim max As Long
    Dim listedcount As Long
    
    listedcount = 0
    max = GetAllCopies(USD1099INT)
    count = 0
    
    Do While count < max
        count = count + 1
        If GetCurrency(USD1099INT.BAmtEF, count) + GetCurrency(USD1099INT.FedExmpt, count) > 0 Then
            If listedcount = Index Then
                ReturnVal = count
            Else
                listedcount = listedcount + 1
            End If
        End If
    Loop
        
    ReturnVal = 0
End Sub

Private Sub INTNbr_Calculation()
    Dim count As Integer
    Dim Lim As Integer
    Dim Total As Integer
    
    Lim = GetAllCopies(USD1099INT)
    count = 1
    Total = 0
    
    Do While count <= Lim
        If GetCurrency(USD1099INT.BAmtEF, count) + GetCurrency(USD1099INT.FedExmpt, count) > 0 Then
            Total = Total + 1
        Else
            Total = Total
        End If
        
        count = count + 1
    Loop
    
    ReturnVal = Total
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IASchB.Names)
End Sub

Private Sub OID_Calculation(Index As Integer)
    Dim count As Long
    Dim max As Long
    Dim listedcount As Long
    
    listedcount = 0
    max = GetAllCopies(USD1099OID)
    count = 0
    
    Do While count < max
        count = count + 1
        If GetCurrency(USD1099OID.BAmt, count) > 0 Or Round(GetCurrency(USD1099OID.BOIDAdjAmt, count)) <> 0 Or Round(GetCurrency(USD1099OID.TaxExempt, count)) <> 0 Then
            If listedcount = Index Then
                ReturnVal = count
            Else
                listedcount = listedcount + 1
            End If
        End If
    Loop
        
    ReturnVal = 0
End Sub

Private Sub OIDNbr_Calculation()
    Dim count As Integer
    Dim Lim As Integer
    Dim Total As Integer
    
    Lim = GetAllCopies(USD1099OID)
    count = 1
    Total = 0
    
    Do While count <= Lim
        If GetCurrency(USD1099OID.BAmt, count) > 0 Or Round(GetCurrency(USD1099OID.BOIDAdjAmt, count)) <> 0 Or Round(GetCurrency(USD1099OID.TaxExempt, count)) <> 0 Then
            Total = Total + 1
        Else
            Total = Total
        End If
        
        count = count + 1
    Loop
    
    ReturnVal = Total
End Sub

Private Sub OthSFM_Calculation(Index As Integer)
    Dim count As Long
    Dim max As Long
    Dim listedcount As Long
    
    listedcount = 0
    max = GetAllCopies(USDSFM)
    count = 0
    
    Do While count < max
        count = count + 1
        If GetBool(USDSFM.Residence, count) = False And GetCurrency(USDSFM.Interest, count) > 0 Then
            If listedcount = Index Then
                ReturnVal = count
            Else
                listedcount = listedcount + 1
            End If
        End If
    Loop
        
    ReturnVal = 0
End Sub

Private Sub OthSFMNbr_Calculation()
    Dim count As Integer
    Dim Lim As Integer
    Dim Total As Integer
    
    Lim = GetAllCopies(USDSFM)
    count = 1
    Total = 0
    
    Do While count <= Lim
        If GetBool(USDSFM.Residence, count) = False And GetCurrency(USDSFM.Interest, count) > 0 Then
            Total = Total + 1
        Else
            Total = Total
        End If
        
        count = count + 1
    Loop
    
    ReturnVal = Total
End Sub

Private Sub PartK1_Calculation(Index As Integer)
    Dim count As Long
    Dim max As Long
    Dim listedcount As Long
    
    listedcount = 0
    max = GetAllCopies(USDPartK1)
    count = 0
    
    Do While count < max
        count = count + 1
        If GetCurrency(USDPartK1.HaveInt, count) > 0 Then
            If listedcount = Index Then
                ReturnVal = count
            Else
                listedcount = listedcount + 1
            End If
        End If
    Loop
        
    ReturnVal = 0
End Sub

Private Sub PartK1Div_Calculation(Index As Integer)
    Dim count As Long
    Dim max As Long
    Dim listedcount As Long
    
    listedcount = 0
    max = GetAllCopies(USDPartK1)
    count = 0
    
    Do While count < max
        count = count + 1
        If GetCurrency(USDPartK1.Dividends, count) > 0 Then
            If listedcount = Index Then
                ReturnVal = count
            Else
                listedcount = listedcount + 1
            End If
        End If
    Loop
        
    ReturnVal = 0
End Sub

Private Sub PartK1DivNbr_Calculation()
    Dim count As Integer
    Dim Lim As Integer
    Dim Total As Integer
    
    Lim = GetAllCopies(USDPartK1)
    count = 1
    Total = 0
    
    Do While count <= Lim
        If GetCurrency(USDPartK1.Dividends, count) > 0 Then
            Total = Total + 1
        Else
            Total = Total
        End If
        
        count = count + 1
    Loop
    
    ReturnVal = Total
End Sub

Private Sub PartK1Nbr_Calculation()
    Dim count As Integer
    Dim Lim As Integer
    Dim Total As Integer
    
    Lim = GetAllCopies(USDPartK1)
    count = 1
    Total = 0
    
    Do While count <= Lim
        If GetCurrency(USDPartK1.HaveInt, count) > 0 Then
            Total = Total + 1
        Else
            Total = Total
        End If
        
        count = count + 1
    Loop
    
    ReturnVal = Total
End Sub

Private Sub ResSFM_Calculation(Index As Integer)
    Dim count As Long
    Dim max As Long
    Dim listedcount As Long
    
    listedcount = 0
    max = GetAllCopies(USDSFM)
    count = 0
    
    Do While count < max
        count = count + 1
        If GetBool(USDSFM.Residence, count) = True And GetCurrency(USDSFM.Interest, count) > 0 Then
            If listedcount = Index Then
                ReturnVal = count
            Else
                listedcount = listedcount + 1
            End If
        End If
    Loop
        
    ReturnVal = 0
End Sub

Private Sub ResSFMNbr_Calculation()
    Dim count As Integer
    Dim Lim As Integer
    Dim Total As Integer
    
    Lim = GetAllCopies(USDSFM)
    count = 1
    Total = 0
    
    Do While count <= Lim
        If GetBool(USDSFM.Residence, count) = True And GetCurrency(USDSFM.Interest, count) > 0 Then
            Total = Total + 1
        Else
            Total = Total
        End If
        
        count = count + 1
    Loop
    
    ReturnVal = Total
End Sub

Private Sub SCorpK1_Calculation(Index As Integer)
    Dim count As Long
    Dim max As Long
    Dim listedcount As Long
    
    listedcount = 0
    max = GetAllCopies(USDSCorpK1)
    count = 0
    
    Do While count < max
        count = count + 1
        If GetCurrency(USDSCorpK1.HaveInt, count) > 0 Then
            If listedcount = Index Then
                ReturnVal = count
            Else
                listedcount = listedcount + 1
            End If
        End If
    Loop
        
    ReturnVal = 0
End Sub

Private Sub SCorpK1Div_Calculation(Index As Integer)
    Dim count As Long
    Dim max As Long
    Dim listedcount As Long
    
    listedcount = 0
    max = GetAllCopies(USDSCorpK1)
    count = 0
    
    Do While count < max
        count = count + 1
        If GetCurrency(USDSCorpK1.Dividends, count) > 0 Then
            If listedcount = Index Then
                ReturnVal = count
            Else
                listedcount = listedcount + 1
            End If
        End If
    Loop
        
    ReturnVal = 0
End Sub

Private Sub SCorpK1DivNbr_Calculation()
    Dim count As Integer
    Dim Lim As Integer
    Dim Total As Integer
    
    Lim = GetAllCopies(USDSCorpK1)
    count = 1
    Total = 0
    
    Do While count <= Lim
        If GetCurrency(USDSCorpK1.Dividends, count) > 0 Then
            Total = Total + 1
        Else
            Total = Total
        End If
        
        count = count + 1
    Loop
    
    ReturnVal = Total
End Sub

Private Sub SCorpK1Nbr_Calculation()
    Dim count As Integer
    Dim Lim As Integer
    Dim Total As Integer
    
    Lim = GetAllCopies(USDSCorpK1)
    count = 1
    Total = 0
    
    Do While count <= Lim
        If GetCurrency(USDSCorpK1.HaveInt, count) > 0 Then
            Total = Total + 1
        Else
            Total = Total
        End If
        
        count = count + 1
    Loop
    
    ReturnVal = Total
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IASchB.SSN)
End Sub

