Private Sub Alert10_Calculation()
    Dim RetailZip As Integer
    
    If Trim(GetString(IA137.StateAbb)) = "" Then
        RetailZip = 0
    ElseIf (IsValidZIP(GetString(IA137.ZipCode), GetString(IA137.StateAbb))) Then
        RetailZip = 0
    Else
        RetailZip = 1
    End If

    If GetBool(IA137.Print) = False Or GetBool(IA137.Site) = False Then
        ReturnVal = 0
    ElseIf Not IsValidEFileString(GetString(IA137.RetailName)) Then
        ReturnVal = 1
    ElseIf Not IsValidEFileString(GetString(IA137.RetailAdd)) Then
        ReturnVal = 1
    ElseIf Not IsValidEFileString(GetString(IA137.City)) Then
        ReturnVal = 1
    ElseIf Trim(GetString(IA137.StateAbb)) = "" Then
        ReturnVal = 1
    ElseIf RetailZip = 1 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If

End Sub

Private Sub AllSitesTotal_Calculation()
    If GetBool(IA137.Site) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetNumber(IA137.TotGas)
    End If
End Sub

Private Sub BioDisparity_Calculation()
    ReturnVal = MaxValue(0, Round(GetFloat(IA137.BioThresPer) - GetFloat(IA137.BioDistPer), 4))
End Sub

Private Sub BioDistPer_Calculation()
    If GetNumber(IA137.TotGas) <= 0 Then
        ReturnVal = 0
    Else
        ReturnVal = Round(GetFloat(IA137.TotGal) / GetFloat(IA137.TotGas), 4)
    End If
End Sub

Private Sub BioThresPer_Calculation()
' updated for 2018
    
    If GetNumber(IA137.AllSitesTotal) <= 0 Then
        ReturnVal = 0
    ElseIf GetNumber(IA137.AllSitesTotal) <= 200000 Then
        ReturnVal = 0.19
    Else
        ReturnVal = 0.23
    End If
End Sub

Private Sub Common_Calculation()
    If GetBool(IAF1040.MFJ) = True Then
        ReturnVal = GetString(USWBasicInfo.CombFirst)
    Else
        ReturnVal = GetString(USWBasicInfo.TPCommon)
    End If
End Sub

Private Sub CreditRate_Calculation()
    If GetFloat(IA137.BioDisparity) = 0 Then
        ReturnVal = "0.080"
    ElseIf GetFloat(IA137.BioDisparity) >= 0.0001 And GetFloat(IA137.BioDisparity) <= 0.02 Then
        ReturnVal = "0.060"
    ElseIf GetFloat(IA137.BioDisparity) >= 0.0201 And GetFloat(IA137.BioDisparity) <= 0.04 Then
        ReturnVal = "0.040"
    Else
        ReturnVal = "0"
    End If
End Sub

Private Sub Description_Calculation()
    Dim Total As Currency
    
    Total = GetCurrency(IA137.TotEthSoldCr) + GetCurrency(IA137.PassThruCr)
    
    ReturnVal = CStr(Total) & " Credit"

End Sub

Private Sub EthPromoteCr_Calculation()
    ReturnVal = GetCurrency(IA137.IndEthPromoteCr) + GetCurrency(IA137.PassThruCr)
End Sub

Private Sub EthSoldCr_Calculation()
    If GetFloat(IA137.BioDisparity) = 0 Then
        ReturnVal = CDollar(GetFloat(IA137.TotEth) * 8)
    ElseIf GetFloat(IA137.BioDisparity) >= 0.0001 And GetFloat(IA137.BioDisparity) <= 0.02 Then
        ReturnVal = CDollar(GetFloat(IA137.TotEth) * 6)
    ElseIf GetFloat(IA137.BioDisparity) >= 0.0201 And GetFloat(IA137.BioDisparity) <= 0.04 Then
        ReturnVal = CDollar(GetFloat(IA137.TotEth) * 4)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub IndEthPromoteCr_Calculation()
    If GetBool(IA137.Company) = True And GetBool(IA137.Taxpayer) = True Then
        ReturnVal = GetCurrency(IA148.TotCode64)
    ElseIf GetBool(IA137.Company) = True And GetBool(IA137.Spouse) = True Then
        ReturnVal = GetCurrency(IA148Sp.TotCode64)
    ElseIf GetCopy() = GetNumber(IA148.FirstCopy137Site) And GetBool(IA137.Taxpayer) = True Then
        ReturnVal = GetCurrency(IA148.TotCode64)
    ElseIf GetCopy() = GetNumber(IA148Sp.FirstCopy137Site) And GetBool(IA137.Spouse) = True Then
        ReturnVal = GetCurrency(IA148Sp.TotCode64)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub MEF137SP_Calculation()
    If GetBool(IA137.Spouse) = True And GetCurrency(IA137.TotEthSoldCr) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub MEF137SPPTE_Calculation()
    If GetBool(IA137.Spouse) = True And GetCurrency(IA137.PassThruCr) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub MEF137TP_Calculation()
    If GetBool(IA137.Taxpayer) = True And GetCurrency(IA137.TotEthSoldCr) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub MEF137TPPTE_Calculation()
    If GetBool(IA137.Taxpayer) = True And GetCurrency(IA137.PassThruCr) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub MeFBioDisparity_Calculation()
    ReturnVal = GetFloat(IA137.BioDisparity) * 100
End Sub

Private Sub Names_Calculation()
    If GetBool(IA137.Spouse) = True Then
        ReturnVal = GetString(IARequired.SPCombName)
    Else
        ReturnVal = GetString(IARequired.TPCombName)
    End If
End Sub

Private Sub Owner_Calculation()
    If GetBool(IA137.Taxpayer) = True Then
        ReturnVal = GetString(USWBasicInfo.TPTheName)
    Else
        ReturnVal = GetString(USWBasicInfo.SPTheName)
    End If
End Sub

Private Sub PassThruCr_Calculation()
    ReturnVal = GetCurrency(IA137.PTECredit(0))
End Sub

Private Sub Print_Calculation()
    If GetBool(IA137.Spouse) = True And GetBool(IAF1040.CombMFS) = False Then
        ReturnVal = 0
    ElseIf GetCurrency(IA137.TotEthSoldCr) > 0 Or GetCurrency(IA137.PassThruCr) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PTEFEIN_Calculation()
    If GetCurrency(IA137.PassThruCr) > 0 Then
        ReturnVal = GetString(IA137.PTEEIN(0))
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub PTEName_Calculation(Index As Integer)
    If GetCurrency(IA137.PassThruCr) > 0 Then
        ReturnVal = GetString(IA137.PTEEntity(0))
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub RetailCityStZip_Calculation()
    ReturnVal = GetString(IA137.City) & ", " & GetString(IA137.StateAbb) & " " & GetString(IA137.ZipCode)
End Sub

Private Sub SpouseCommon_Calculation()
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetString(USWBasicInfo.SPCommon)
    Else
        ReturnVal = "Not Applicable"
    End If
End Sub

Private Sub SSN_Calculation()
    If GetBool(IA137.Spouse) = True Then
        ReturnVal = GetString(IAF1040.SpouseSSN)
    Else
        ReturnVal = GetString(IAF1040.SSN)
    End If
End Sub

Private Sub TotB10Gal_Calculation()
    ReturnVal = CLng(Round(GetNumber(IA137.B10Gal) * 0.11))
End Sub

Private Sub TotB20Gal_Calculation()
    ReturnVal = CLng(Round(GetNumber(IA137.B20Gal) * 0.2))
End Sub

Private Sub TotB2Gal_Calculation()
    ReturnVal = CLng(Round(GetNumber(IA137.B2Gal) * 0.02))
End Sub

Private Sub TotB5Gal_Calculation()
    ReturnVal = CLng(Round(GetNumber(IA137.B5Gal) * 0.05))
End Sub

Private Sub TotBTypeGal_Calculation()
    ReturnVal = CLng(Round(GetFloat(IA137.BTypeGal) * (GetFloat(IA137.BTypeGalPer) / 100#)))
End Sub

Private Sub TotE10Gal_Calculation()
    ReturnVal = CLng(Round(GetNumber(IA137.E10Gal) * 0.1))
End Sub

Private Sub TotE15Gal_Calculation()
    ReturnVal = CLng(Round(GetNumber(IA137.E15Gal) * 0.15))
End Sub

Private Sub TotE85Gal_Calculation()
    ReturnVal = CLng(Round(GetNumber(IA137.E85Gal) * 0.79))
End Sub

Private Sub TotEth_Calculation()
    ReturnVal = GetNumber(IA137.TotEthGal)
End Sub

Private Sub TotEthGal_Calculation()
    ReturnVal = GetNumber(IA137.TotE10Gal) + GetNumber(IA137.TotE15Gal) + GetNumber(IA137.TotE85Gal) + GetNumber(IA137.TotOthGal)
End Sub

Private Sub TotEthGalColA_Calculation()
    ReturnVal = GetNumber(IA137.E10Gal) + GetNumber(IA137.E15Gal) + GetNumber(IA137.E85Gal) + GetNumber(IA137.OthGal)
End Sub

Private Sub TotEthSoldCr_Calculation()
    ReturnVal = GetCurrency(IA137.EthSoldCr)
End Sub

Private Sub TotGas_Calculation()
    ReturnVal = GetNumber(IA137.E10Gal) + GetNumber(IA137.E15Gal) + GetNumber(IA137.E85Gal) + GetNumber(IA137.OthGal) + GetNumber(IA137.NonEthGal)
End Sub

Private Sub TotGal_Calculation()
    ReturnVal = GetNumber(IA137.TotEthGal) + GetNumber(IA137.TotB2Gal) + GetNumber(IA137.TotB5Gal) + GetNumber(IA137.TotB10Gal) + GetNumber(IA137.TotB20Gal) + GetNumber(IA137.TotBTypeGal)
End Sub

Private Sub TotOthGal_Calculation()
    ReturnVal = CLng(Round(GetFloat(IA137.OthGal) * (GetFloat(IA137.OthGalPer) / 100#)))
End Sub

