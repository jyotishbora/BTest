Private Sub Desc_Calculation()
    Dim Total1 As Currency
    
    Total1 = GetCurrency(IAWBP148RefSp.TotRefCr1) + GetCurrency(IAWBP148RefSp.TotRefCr2)
    
    ReturnVal = CStr(Total1) & " Refundable Credits"
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IA148Sp.Names)
End Sub

Private Sub Offset_Calculation()
    If GetCopy() = 1 Then
        ReturnVal = 6
    Else
        ReturnVal = 56
    End If
End Sub

Private Sub Print_Calculation()
    If GetCurrency(IAWBP148RefSp.TotRefCr1) > 0 Or GetCurrency(IAWBP148RefSp.TotRefCr2) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PTERefTrig_Calculation(Index As Integer)
    If GetString(IAWBP148RefSp.RefPTECode(Index)) = "64" Or GetString(IAWBP148RefSp.RefPTECode(Index)) = "58" Or GetString(IAWBP148RefSp.RefPTECode(Index)) = "55" Or GetString(IAWBP148RefSp.RefPTECode(Index)) = "52" Or GetString(IAWBP148RefSp.RefPTECode(Index)) = "59" Or GetString(IAWBP148RefSp.RefPTECode(Index)) = "65" Or GetString(IAWBP148RefSp.RefPTECode(Index)) = "66" Then
        ReturnVal = 0
    ElseIf Trim(GetString(IAWBP148RefSp.RefPTEName(Index))) <> "" Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub RefCert_Calculation(Index As Integer)
  Dim strindex As Long
  Dim copystr As String
  Dim Copy As Long
  
  strindex = ((((GetCopy() - 1) * 50) + 6 + Index) * 4) + 1
  copystr = Trim(Mid(GetString(IA148Sp.RefCopiesStr), strindex, 4))
  
  If GetNumber(IA148Sp.RefNbr) = 7 Then
    ReturnVal = ""
  ElseIf copystr <> "" Then
    Copy = CLng(copystr)
    If (Copy > 100) And (Copy <= 200) Then
      ReturnVal = ""
    ElseIf (Copy > 200) And (Copy <= 300) Then
      ReturnVal = GetString(IACred.CertNumber, (Copy) - 200)
    ElseIf (Copy > 300) And (Copy <= 400) Then
      ReturnVal = ""
    ElseIf (Copy > 400) And (Copy <= 500) Then
      ReturnVal = GetString(IACred.CertNumber, (Copy) - 400)
    ElseIf (Copy > 500) And (Copy <= 600) Then
      ReturnVal = ""
    ElseIf (Copy > 600) And (Copy <= 700) Then
      ReturnVal = ""
    ElseIf (Copy > 700) And (Copy <= 800) Then
      ReturnVal = GetString(IA128.SuppCertNbr, (Copy) - 700)
    ElseIf (Copy > 800) And (Copy <= 900) Then
      ReturnVal = GetString(IA128S.SuppCertNbr, (Copy) - 800)
    ElseIf (Copy > 900) And (Copy <= 1000) Then
      ReturnVal = ""
    ElseIf (Copy > 1000) And (Copy <= 1100) Then
      ReturnVal = ""
    ElseIf (Copy > 1100) And (Copy <= 1200) Then
      ReturnVal = ""
    ElseIf (Copy > 1200) And (Copy <= 1300) Then
      ReturnVal = GetString(IACred.CertNumber, (Copy) - 1200)
    ElseIf (Copy > 1300) And (Copy <= 1400) Then
      ReturnVal = GetString(IACred.CertNumber, (Copy) - 1300)
    ElseIf (Copy > 1400) And (Copy <= 1500) Then
      ReturnVal = GetString(IACred.CertNumber, (Copy) - 1400)
    End If
  End If
 ReturnVal = ""
End Sub

Private Sub RefCode_Calculation(Index As Integer)
  Dim strindex As Long
  Dim copystr As String
  Dim Copy As Long
  
  strindex = ((((GetCopy() - 1) * 50) + 6 + Index) * 4) + 1
  copystr = Trim(Mid(GetString(IA148Sp.RefCopiesStr), strindex, 4))
  
  If GetNumber(IA148Sp.RefNbr) = 7 Then
    ReturnVal = ""
  ElseIf copystr <> "" Then
    Copy = CLng(copystr)
    If (Copy > 100) And (Copy <= 200) Then
      ReturnVal = "52"
    ElseIf (Copy > 200) And (Copy <= 300) Then
      ReturnVal = GetString(IACred.Code, (Copy) - 200)
    ElseIf (Copy > 300) And (Copy <= 400) Then
      ReturnVal = "55"
    ElseIf (Copy > 400) And (Copy <= 500) Then
      ReturnVal = GetString(IACred.Code, (Copy) - 400)
    ElseIf (Copy > 500) And (Copy <= 600) Then
      ReturnVal = "58"
    ElseIf (Copy > 600) And (Copy <= 700) Then
      ReturnVal = "58"
    ElseIf (Copy > 700) And (Copy <= 800) Then
      ReturnVal = "59"
    ElseIf (Copy > 800) And (Copy <= 900) Then
      ReturnVal = "59"
    ElseIf (Copy > 900) And (Copy <= 1000) Then
      ReturnVal = "64"
    ElseIf (Copy > 1000) And (Copy <= 1100) Then
      ReturnVal = "65"
    ElseIf (Copy > 1100) And (Copy <= 1200) Then
      ReturnVal = "66"
    ElseIf (Copy > 1200) And (Copy <= 1300) Then
      ReturnVal = GetString(IACred.Code, (Copy) - 1200)
    ElseIf (Copy > 1300) And (Copy <= 1400) Then
      ReturnVal = GetString(IACred.Code, (Copy) - 1300)
    ElseIf (Copy > 1400) And (Copy <= 1500) Then
      ReturnVal = GetString(IACred.Code, (Copy) - 1400)
    End If
  End If
  ReturnVal = ""
End Sub

Private Sub RefCr_Calculation(Index As Integer)
  Dim strindex As Long
  Dim copystr As String
  Dim Copy As Long
  
  strindex = ((((GetCopy() - 1) * 50) + 6 + Index) * 4) + 1
  copystr = Trim(Mid(GetString(IA148Sp.RefCopiesStr), strindex, 4))
  
  If GetNumber(IA148Sp.RefNbr) = 7 Then
    ReturnVal = 0
  ElseIf copystr <> "" Then
    Copy = CLng(copystr)
    If (Copy > 100) And (Copy <= 200) Then
      ReturnVal = GetCurrency(IA8864.BiodieselCr, (Copy) - 100)
    ElseIf (Copy > 200) And (Copy <= 300) Then
      ReturnVal = GetCurrency(IACred.CYCredit, (Copy) - 200)
    ElseIf (Copy > 300) And (Copy <= 400) Then
      ReturnVal = GetCurrency(IA135.E85Credit, (Copy) - 300)
    ElseIf (Copy > 400) And (Copy <= 500) Then
      ReturnVal = GetCurrency(IACred.CYCredit, (Copy) - 400)
    ElseIf (Copy > 500) And (Copy <= 600) Then
      ReturnVal = GetCurrency(IA128.TotResearchCr, (Copy) - 500)
    ElseIf (Copy > 600) And (Copy <= 700) Then
      ReturnVal = GetCurrency(IA128S.TotResearchCr, (Copy) - 600)
    ElseIf (Copy > 700) And (Copy <= 800) Then
      ReturnVal = GetCurrency(IA128.TotSuppResearchCr, (Copy) - 700)
    ElseIf (Copy > 800) And (Copy <= 900) Then
      ReturnVal = GetCurrency(IA128S.TotSuppResearchCr, (Copy) - 800)
    ElseIf (Copy > 900) And (Copy <= 1000) Then
      ReturnVal = GetCurrency(IA137.EthPromoteCr, (Copy) - 900)
    ElseIf (Copy > 1000) And (Copy <= 1100) Then
      ReturnVal = GetCurrency(IA138.E15Credit, (Copy) - 1000)
    ElseIf (Copy > 1100) And (Copy <= 1200) Then
      ReturnVal = GetCurrency(IA177.CYAdoptionTaxCr, (Copy) - 1100)
    ElseIf (Copy > 1200) And (Copy <= 1300) Then
      ReturnVal = GetCurrency(IACred.CYCredit, (Copy) - 1200)
    ElseIf (Copy > 1300) And (Copy <= 1400) Then
      ReturnVal = GetCurrency(IACred.CYCredit, (Copy) - 1300)
    ElseIf (Copy > 1400) And (Copy <= 1500) Then
      ReturnVal = GetCurrency(IACred.CYCredit, (Copy) - 1400)
    End If
  End If
  ReturnVal = 0
End Sub

Private Sub RefPTECode_Calculation(Index As Integer)
    Dim Stuff As Integer
    
    Stuff = Index + GetNumber(IAWBP148RefSp.Offset) + 1

    ReturnVal = GetString(IA148BumpSp.RefPTECode(Stuff))
End Sub

Private Sub RefPTEEIN_Calculation(Index As Integer)
    Dim Stuff As Integer
    
    Stuff = Index + GetNumber(IAWBP148RefSp.Offset) + 1

    ReturnVal = GetString(IA148BumpSp.RefPTEEIN(Stuff))
End Sub

Private Sub RefPTEName_Calculation(Index As Integer)
    Dim Stuff As Integer
    
    Stuff = Index + GetNumber(IAWBP148RefSp.Offset) + 1

    ReturnVal = GetString(IA148BumpSp.RefPTEName(Stuff))
End Sub

Private Sub RefTPPerc_Calculation(Index As Integer)
    Dim Stuff As Integer
    
    Stuff = Index + GetNumber(IAWBP148RefSp.Offset) + 1

    ReturnVal = GetFloat(IA148BumpSp.RefTPPerc(Stuff))
End Sub

Private Sub RefTrig_Calculation(Index As Integer)
    If GetString(IAWBP148RefSp.RefCode(Index)) = "64" Or GetString(IAWBP148RefSp.RefCode(Index)) = "58" Or GetString(IAWBP148RefSp.RefCode(Index)) = "55" Or GetString(IAWBP148RefSp.RefCode(Index)) = "52" Or GetString(IAWBP148RefSp.RefCode(Index)) = "59" Or GetString(IAWBP148RefSp.RefCode(Index)) = "65" Or GetString(IAWBP148RefSp.RefCode(Index)) = "66" Then
        ReturnVal = 0
    ElseIf GetCurrency(IAWBP148RefSp.RefCr(Index)) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IA148Sp.SSN)
End Sub

Private Sub TotRefCr1_Calculation()
    Dim count As Integer
    Dim SubTot As Currency

    count = 0
    SubTot = 0

    Do While count < 25
        SubTot = SubTot + GetCurrency(IAWBP148RefSp.RefCr(count))
        count = count + 1
    Loop
    
    ReturnVal = SubTot
End Sub

Private Sub TotRefCr2_Calculation()
    Dim count As Integer
    Dim SubTot As Currency

    count = 25
    SubTot = 0

    Do While count < 50
        SubTot = SubTot + GetCurrency(IAWBP148RefSp.RefCr(count))
        count = count + 1
    Loop
    
    ReturnVal = SubTot
End Sub

