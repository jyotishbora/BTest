Private Sub ArrayNonRefCr_Calculation(Index As Integer)
    If Index = 0 Then
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr1)
    ElseIf Index = 1 Then
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr2)
    ElseIf Index = 2 Then
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr3)
    ElseIf Index = 3 Then
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr4)
    ElseIf Index = 4 Then
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr5)
    ElseIf Index = 5 Then
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr6)
    ElseIf Index = 6 Then
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr7)
    ElseIf Index = 7 Then
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr8)
    ElseIf Index = 8 Then
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr9)
    ElseIf Index = 9 Then
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr10)
    ElseIf Index = 10 Then
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr11)
    ElseIf Index = 11 Then
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr12)
    ElseIf Index = 12 Then
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr13)
    ElseIf Index = 13 Then
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr14)
    ElseIf Index = 14 Then
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr15)
    ElseIf Index = 15 Then
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr16)
    ElseIf Index = 16 Then
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr17)
    ElseIf Index = 17 Then
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr18)
    ElseIf Index = 18 Then
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr19)
    ElseIf Index = 19 Then
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr20)
    ElseIf Index = 20 Then
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr21)
    ElseIf Index = 21 Then
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr22)
    ElseIf Index = 22 Then
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr23)
    ElseIf Index = 23 Then
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr24)
    ElseIf Index = 24 Then
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr25)
    ElseIf Index = 25 Then
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr26)
    ElseIf Index = 26 Then
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr27)
    ElseIf Index = 27 Then
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr28)
    Else
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr29)
    End If
End Sub

Private Sub AvailCr_Calculation(Index As Integer)
    If GetString(IAWBP148Sp.NonRefCode(Index)) = "09" Then
        ReturnVal = GetCurrency(IA8801Sp.AMTCR)
    Else
        ReturnVal = GetCurrency(IAWBP148Sp.PYCarry(Index)) + GetCurrency(IAWBP148Sp.CYCredit(Index))
    End If
End Sub

Private Sub CYCarry_Calculation(Index As Integer)
    If GetString(IAWBP148Sp.NonRefCode(Index)) = "09" Then
        ReturnVal = GetCurrency(IA8801Sp.CYCarryforward)
    Else
        ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.AvailCr(Index)) - GetCurrency(IAWBP148Sp.ArrayNonRefCr(Index)) - GetCurrency(IAWBP148Sp.ExpCr(Index)))
    End If
End Sub

Private Sub CYCredit_Calculation(Index As Integer)
  Dim strindex As Long
  Dim copystr As String
  Dim Copy As Long
  
  strindex = ((((GetCopy() - 1) * 29) + 9 + Index) * 4) + 1
  copystr = Trim(Mid(GetString(IA148Sp.NonRefCopiesStr), strindex, 4))
  
  If GetNumber(IA148Sp.NonRefNbr) = 10 Then
    ReturnVal = 0
  ElseIf copystr <> "" Then
    Copy = CLng(copystr)
    If (Copy > 100) And (Copy <= 200) Then
      ReturnVal = GetCurrency(IA147.FranchiseCr, (Copy) - 100)
    ElseIf (Copy > 200) And (Copy <= 300) Then
      ReturnVal = GetCurrency(IA134.Credit, (Copy) - 200)
    ElseIf (Copy > 300) And (Copy <= 400) Then
      ReturnVal = GetCurrency(IACred.CYCredit, (Copy) - 300)
    ElseIf (Copy > 400) And (Copy <= 500) Then
      ReturnVal = GetCurrency(IACred.CYCredit, (Copy) - 400)
    ElseIf (Copy > 500) And (Copy <= 600) Then
      ReturnVal = GetCurrency(IACred.CYCredit, (Copy) - 500)
    ElseIf (Copy > 600) And (Copy <= 700) Then
      ReturnVal = GetCurrency(IACred.CYCredit, (Copy) - 600)
    ElseIf (Copy > 700) And (Copy <= 800) Then
      ReturnVal = GetCurrency(IACred.CYCredit, (Copy) - 700)
    ElseIf (Copy > 800) And (Copy <= 900) Then
      ReturnVal = GetCurrency(IACred.CYCredit, (Copy) - 800)
    ElseIf (Copy > 900) And (Copy <= 1000) Then
      ReturnVal = GetCurrency(IACred.CYCredit, (Copy) - 900)
    ElseIf (Copy > 1000) And (Copy <= 1100) Then
      ReturnVal = GetCurrency(IACred.CYCredit, (Copy) - 1000)
    ElseIf (Copy > 1100) And (Copy <= 1200) Then
      ReturnVal = GetCurrency(IACred.CYCredit, (Copy) - 1100)
    ElseIf (Copy > 1200) And (Copy <= 1300) Then
      ReturnVal = GetCurrency(IACred.CYCredit, (Copy) - 1200)
    ElseIf (Copy > 1300) And (Copy <= 1400) Then
      ReturnVal = GetCurrency(IACred.CYCredit, (Copy) - 1300)
    ElseIf (Copy > 1400) And (Copy <= 1500) Then
      ReturnVal = GetCurrency(IACred.CYCredit, (Copy) - 1400)
    ElseIf (Copy > 1500) And (Copy <= 1600) Then
      ReturnVal = GetCurrency(IACred.CYCredit, (Copy) - 1500)
    ElseIf (Copy > 1600) And (Copy <= 1700) Then
      ReturnVal = GetCurrency(IACred.CYCredit, (Copy) - 1600)
    ElseIf (Copy > 1700) And (Copy <= 1800) Then
      ReturnVal = GetCurrency(IACred.CYCredit, (Copy) - 1700)
    ElseIf (Copy > 1800) And (Copy <= 1900) Then
      ReturnVal = GetCurrency(IACred.CYCredit, (Copy) - 1800)
    ElseIf (Copy > 1900) And (Copy <= 2000) Then
      ReturnVal = GetCurrency(IACred.CYCredit, (Copy) - 1900)
    ElseIf (Copy > 2000) And (Copy <= 2100) Then
      ReturnVal = GetCurrency(IACred.CYCredit, (Copy) - 2000)
    ElseIf (Copy > 2100) And (Copy <= 2200) Then
      ReturnVal = GetCurrency(IACred.CYCredit, (Copy) - 2100)
    ElseIf (Copy > 2200) And (Copy <= 2300) Then
      ReturnVal = GetCurrency(IACred.CYCredit, (Copy) - 2200)
    ElseIf (Copy > 2300) And (Copy <= 2400) Then
      ReturnVal = GetCurrency(IACred.CYCredit, (Copy) - 2300)
    ElseIf (Copy > 2400) And (Copy <= 2500) Then
      ReturnVal = GetCurrency(IA8801Sp.PYAMT)
    End If
  End If
  ReturnVal = 0
End Sub

Private Sub Desc_Calculation()
    Dim Total1 As Currency
    
    Total1 = GetCurrency(IAWBP148Sp.TotNonRefCr)
    
    ReturnVal = CStr(Total1) & " Nonrefundable Credits"
End Sub

Private Sub ExpCr_Calculation(Index As Integer)
  Dim strindex As Long
  Dim copystr As String
  Dim Copy As Long
  
  strindex = ((((GetCopy() - 1) * 29) + 9 + Index) * 4) + 1
  copystr = Trim(Mid(GetString(IA148Sp.NonRefCopiesStr), strindex, 4))
  
  If GetNumber(IA148Sp.NonRefNbr) = 10 Then
    ReturnVal = 0
  ElseIf copystr <> "" Then
    Copy = CLng(copystr)
    If (Copy > 100) And (Copy <= 200) Then
      ReturnVal = MaxValue(0, GetCurrency(IA148Sp.AvailCr(Index)) - GetCurrency(IA148Sp.ArrayNonRefCr(Index)))
    ElseIf (Copy > 200) And (Copy <= 300) Then
      ReturnVal = MaxValue(0, GetCurrency(IA148Sp.AvailCr(Index)) - GetCurrency(IA148Sp.ArrayNonRefCr(Index)))
    ElseIf (Copy > 300) And (Copy <= 400) Then
      ReturnVal = GetCurrency(IACred.ExpCr, (Copy) - 300)
    ElseIf (Copy > 400) And (Copy <= 500) Then
      ReturnVal = GetCurrency(IACred.ExpCr, (Copy) - 400)
    ElseIf (Copy > 500) And (Copy <= 600) Then
      ReturnVal = GetCurrency(IACred.ExpCr, (Copy) - 500)
    ElseIf (Copy > 600) And (Copy <= 700) Then
      ReturnVal = GetCurrency(IACred.ExpCr, (Copy) - 600)
    ElseIf (Copy > 700) And (Copy <= 800) Then
      ReturnVal = GetCurrency(IACred.ExpCr, (Copy) - 700)
    ElseIf (Copy > 800) And (Copy <= 900) Then
      ReturnVal = GetCurrency(IACred.ExpCr, (Copy) - 800)
    ElseIf (Copy > 900) And (Copy <= 1000) Then
      ReturnVal = GetCurrency(IACred.ExpCr, (Copy) - 900)
    ElseIf (Copy > 1000) And (Copy <= 1100) Then
      ReturnVal = GetCurrency(IACred.ExpCr, (Copy) - 1000)
    ElseIf (Copy > 1100) And (Copy <= 1200) Then
      ReturnVal = GetCurrency(IACred.ExpCr, (Copy) - 1100)
    ElseIf (Copy > 1200) And (Copy <= 1300) Then
      ReturnVal = GetCurrency(IACred.ExpCr, (Copy) - 1200)
    ElseIf (Copy > 1300) And (Copy <= 1400) Then
      ReturnVal = GetCurrency(IACred.ExpCr, (Copy) - 1300)
    ElseIf (Copy > 1400) And (Copy <= 1500) Then
      ReturnVal = GetCurrency(IACred.ExpCr, (Copy) - 1400)
    ElseIf (Copy > 1500) And (Copy <= 1600) Then
      ReturnVal = GetCurrency(IACred.ExpCr, (Copy) - 1500)
    ElseIf (Copy > 1600) And (Copy <= 1700) Then
      ReturnVal = GetCurrency(IACred.ExpCr, (Copy) - 1600)
    ElseIf (Copy > 1700) And (Copy <= 1800) Then
      ReturnVal = GetCurrency(IACred.ExpCr, (Copy) - 1700)
    ElseIf (Copy > 1800) And (Copy <= 1900) Then
      ReturnVal = GetCurrency(IACred.ExpCr, (Copy) - 1800)
    ElseIf (Copy > 1900) And (Copy <= 2000) Then
      ReturnVal = GetCurrency(IACred.ExpCr, (Copy) - 1900)
    ElseIf (Copy > 2000) And (Copy <= 2100) Then
      ReturnVal = GetCurrency(IACred.ExpCr, (Copy) - 2000)
    ElseIf (Copy > 2100) And (Copy <= 2200) Then
      ReturnVal = GetCurrency(IACred.ExpCr, (Copy) - 2100)
    ElseIf (Copy > 2200) And (Copy <= 2300) Then
      ReturnVal = GetCurrency(IACred.ExpCr, (Copy) - 2200)
    ElseIf (Copy > 2300) And (Copy <= 2400) Then
      ReturnVal = GetCurrency(IACred.ExpCr, (Copy) - 2300)
    ElseIf (Copy > 2400) And (Copy <= 2500) Then
      ReturnVal = 0
    End If
  End If
  ReturnVal = 0
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IA148Sp.Names)
End Sub

Private Sub NonRefCert_Calculation(Index As Integer)
  Dim strindex As Long
  Dim copystr As String
  Dim Copy As Long
  
  strindex = ((((GetCopy() - 1) * 29) + 9 + Index) * 4) + 1
  copystr = Trim(Mid(GetString(IA148Sp.NonRefCopiesStr), strindex, 4))
  
  If GetNumber(IA148Sp.NonRefNbr) = 10 Then
    ReturnVal = ""
  ElseIf copystr <> "" Then
    Copy = CLng(copystr)
    If (Copy > 100) And (Copy <= 200) Then
      ReturnVal = ""
    ElseIf (Copy > 200) And (Copy <= 300) Then
      ReturnVal = ""
    ElseIf (Copy > 300) And (Copy <= 400) Then
      ReturnVal = GetString(IACred.CertNumber, (Copy) - 300)
    ElseIf (Copy > 400) And (Copy <= 500) Then
      ReturnVal = GetString(IACred.CertNumber, (Copy) - 400)
    ElseIf (Copy > 500) And (Copy <= 600) Then
      ReturnVal = GetString(IACred.CertNumber, (Copy) - 500)
    ElseIf (Copy > 600) And (Copy <= 700) Then
      ReturnVal = GetString(IACred.CertNumber, (Copy) - 600)
    ElseIf (Copy > 700) And (Copy <= 800) Then
      ReturnVal = GetString(IACred.CertNumber, (Copy) - 700)
    ElseIf (Copy > 800) And (Copy <= 900) Then
      ReturnVal = GetString(IACred.CertNumber, (Copy) - 800)
    ElseIf (Copy > 900) And (Copy <= 1000) Then
      ReturnVal = GetString(IACred.CertNumber, (Copy) - 900)
    ElseIf (Copy > 1000) And (Copy <= 1100) Then
      ReturnVal = GetString(IACred.CertNumber, (Copy) - 1000)
    ElseIf (Copy > 1100) And (Copy <= 1200) Then
      ReturnVal = GetString(IACred.CertNumber, (Copy) - 1100)
    ElseIf (Copy > 1200) And (Copy <= 1300) Then
      ReturnVal = GetString(IACred.CertNumber, (Copy) - 1200)
    ElseIf (Copy > 1300) And (Copy <= 1400) Then
      ReturnVal = GetString(IACred.CertNumber, (Copy) - 1300)
    ElseIf (Copy > 1400) And (Copy <= 1500) Then
      ReturnVal = GetString(IACred.CertNumber, (Copy) - 1400)
    ElseIf (Copy > 1500) And (Copy <= 1600) Then
      ReturnVal = GetString(IACred.CertNumber, (Copy) - 1500)
    ElseIf (Copy > 1600) And (Copy <= 1700) Then
      ReturnVal = GetString(IACred.CertNumber, (Copy) - 1600)
    ElseIf (Copy > 1700) And (Copy <= 1800) Then
      ReturnVal = GetString(IACred.CertNumber, (Copy) - 1700)
    ElseIf (Copy > 1800) And (Copy <= 1900) Then
      ReturnVal = GetString(IACred.CertNumber, (Copy) - 1800)
    ElseIf (Copy > 1900) And (Copy <= 2000) Then
      ReturnVal = GetString(IACred.CertNumber, (Copy) - 1900)
    ElseIf (Copy > 2000) And (Copy <= 2100) Then
      ReturnVal = GetString(IACred.CertNumber, (Copy) - 2000)
    ElseIf (Copy > 2100) And (Copy <= 2200) Then
      ReturnVal = GetString(IACred.CertNumber, (Copy) - 2100)
    ElseIf (Copy > 2200) And (Copy <= 2300) Then
      ReturnVal = GetString(IACred.CertNumber, (Copy) - 2200)
    ElseIf (Copy > 2300) And (Copy <= 2400) Then
      ReturnVal = GetString(IACred.CertNumber, (Copy) - 2300)
    ElseIf (Copy > 2400) And (Copy <= 2500) Then
      ReturnVal = ""
    End If
  End If
  ReturnVal = ""
End Sub

Private Sub NonRefCode_Calculation(Index As Integer)
  Dim strindex As Long
  Dim copystr As String
  Dim Copy As Long
  
  strindex = ((((GetCopy() - 1) * 29) + 9 + Index) * 4) + 1
  copystr = Trim(Mid(GetString(IA148Sp.NonRefCopiesStr), strindex, 4))
  
  If GetNumber(IA148Sp.NonRefNbr) = 10 Then
    ReturnVal = ""
  ElseIf copystr <> "" Then
    Copy = CLng(copystr)
    If (Copy > 100) And (Copy <= 200) Then
      ReturnVal = "04"
    ElseIf (Copy > 200) And (Copy <= 300) Then
      ReturnVal = "11"
    ElseIf (Copy > 300) And (Copy <= 400) Then
      ReturnVal = GetString(IACred.Code, (Copy) - 300)
    ElseIf (Copy > 400) And (Copy <= 500) Then
      ReturnVal = GetString(IACred.Code, (Copy) - 400)
    ElseIf (Copy > 500) And (Copy <= 600) Then
      ReturnVal = GetString(IACred.Code, (Copy) - 500)
    ElseIf (Copy > 600) And (Copy <= 700) Then
      ReturnVal = GetString(IACred.Code, (Copy) - 600)
    ElseIf (Copy > 700) And (Copy <= 800) Then
      ReturnVal = GetString(IACred.Code, (Copy) - 700)
    ElseIf (Copy > 800) And (Copy <= 900) Then
      ReturnVal = GetString(IACred.Code, (Copy) - 800)
    ElseIf (Copy > 900) And (Copy <= 1000) Then
      ReturnVal = GetString(IACred.Code, (Copy) - 900)
    ElseIf (Copy > 1000) And (Copy <= 1100) Then
      ReturnVal = GetString(IACred.Code, (Copy) - 1000)
    ElseIf (Copy > 1100) And (Copy <= 1200) Then
      ReturnVal = GetString(IACred.Code, (Copy) - 1100)
    ElseIf (Copy > 1200) And (Copy <= 1300) Then
      ReturnVal = GetString(IACred.Code, (Copy) - 1200)
    ElseIf (Copy > 1300) And (Copy <= 1400) Then
      ReturnVal = GetString(IACred.Code, (Copy) - 1300)
    ElseIf (Copy > 1400) And (Copy <= 1500) Then
      ReturnVal = GetString(IACred.Code, (Copy) - 1400)
    ElseIf (Copy > 1500) And (Copy <= 1600) Then
      ReturnVal = GetString(IACred.Code, (Copy) - 1500)
    ElseIf (Copy > 1600) And (Copy <= 1700) Then
      ReturnVal = GetString(IACred.Code, (Copy) - 1600)
    ElseIf (Copy > 1700) And (Copy <= 1800) Then
      ReturnVal = GetString(IACred.Code, (Copy) - 1700)
    ElseIf (Copy > 1800) And (Copy <= 1900) Then
      ReturnVal = GetString(IACred.Code, (Copy) - 1800)
    ElseIf (Copy > 1900) And (Copy <= 2000) Then
      ReturnVal = GetString(IACred.Code, (Copy) - 1900)
    ElseIf (Copy > 2000) And (Copy <= 2100) Then
      ReturnVal = GetString(IACred.Code, (Copy) - 2000)
    ElseIf (Copy > 2100) And (Copy <= 2200) Then
      ReturnVal = GetString(IACred.Code, (Copy) - 2100)
    ElseIf (Copy > 2200) And (Copy <= 2300) Then
      ReturnVal = GetString(IACred.Code, (Copy) - 2200)
    ElseIf (Copy > 2300) And (Copy <= 2400) Then
      ReturnVal = GetString(IACred.Code, (Copy) - 2300)
    ElseIf (Copy > 2400) And (Copy <= 2500) Then
      ReturnVal = "09"
    End If
  End If
  ReturnVal = ""
End Sub

Private Sub NonRefCr1_Calculation()
    Dim PriorCopy As Long
    Dim PriorCopyTax As Currency
    
    PriorCopy = GetCopy()
    
    PriorCopyTax = GetCurrency(IAWBP148Sp.NonRefTax30, PriorCopy - 1)
    
    If GetCopy() = 1 Then
        ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(0)), GetCurrency(IA148Sp.NonRefTax10))
    Else
        ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(0)), PriorCopyTax)
    End If
End Sub

Private Sub NonRefCr10_Calculation()
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(9)), GetCurrency(IAWBP148Sp.NonRefTax10))
End Sub

Private Sub NonRefCr11_Calculation()
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(10)), GetCurrency(IAWBP148Sp.NonRefTax11))
End Sub

Private Sub NonRefCr12_Calculation()
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(11)), GetCurrency(IAWBP148Sp.NonRefTax12))
End Sub

Private Sub NonRefCr13_Calculation()
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(12)), GetCurrency(IAWBP148Sp.NonRefTax13))
End Sub

Private Sub NonRefCr14_Calculation()
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(13)), GetCurrency(IAWBP148Sp.NonRefTax14))
End Sub

Private Sub NonRefCr15_Calculation()
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(14)), GetCurrency(IAWBP148Sp.NonRefTax15))
End Sub

Private Sub NonRefCr16_Calculation()
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(15)), GetCurrency(IAWBP148Sp.NonRefTax16))
End Sub

Private Sub NonRefCr17_Calculation()
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(16)), GetCurrency(IAWBP148Sp.NonRefTax17))
End Sub

Private Sub NonRefCr18_Calculation()
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(17)), GetCurrency(IAWBP148Sp.NonRefTax18))
End Sub

Private Sub NonRefCr19_Calculation()
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(18)), GetCurrency(IAWBP148Sp.NonRefTax19))
End Sub

Private Sub NonRefCr2_Calculation()
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(1)), GetCurrency(IAWBP148Sp.NonRefTax2))
End Sub

Private Sub NonRefCr20_Calculation()
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(19)), GetCurrency(IAWBP148Sp.NonRefTax20))
End Sub

Private Sub NonRefCr21_Calculation()
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(20)), GetCurrency(IAWBP148Sp.NonRefTax21))
End Sub

Private Sub NonRefCr22_Calculation()
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(21)), GetCurrency(IAWBP148Sp.NonRefTax22))
End Sub

Private Sub NonRefCr23_Calculation()
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(22)), GetCurrency(IAWBP148Sp.NonRefTax23))
End Sub

Private Sub NonRefCr24_Calculation()
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(23)), GetCurrency(IAWBP148Sp.NonRefTax24))
End Sub

Private Sub NonRefCr25_Calculation()
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(24)), GetCurrency(IAWBP148Sp.NonRefTax25))
End Sub

Private Sub NonRefCr26_Calculation()
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(25)), GetCurrency(IAWBP148Sp.NonRefTax26))
End Sub

Private Sub NonRefCr27_Calculation()
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(26)), GetCurrency(IAWBP148Sp.NonRefTax27))
End Sub

Private Sub NonRefCr28_Calculation()
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(27)), GetCurrency(IAWBP148Sp.NonRefTax28))
End Sub

Private Sub NonRefCr29_Calculation()
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(28)), GetCurrency(IAWBP148Sp.NonRefTax29))
End Sub

Private Sub NonRefCr3_Calculation()
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(2)), GetCurrency(IAWBP148Sp.NonRefTax3))
End Sub

Private Sub NonRefCr4_Calculation()
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(3)), GetCurrency(IAWBP148Sp.NonRefTax4))
End Sub

Private Sub NonRefCr5_Calculation()
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(4)), GetCurrency(IAWBP148Sp.NonRefTax5))
End Sub

Private Sub NonRefCr6_Calculation()
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(5)), GetCurrency(IAWBP148Sp.NonRefTax6))
End Sub

Private Sub NonRefCr7_Calculation()
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(6)), GetCurrency(IAWBP148Sp.NonRefTax7))
End Sub

Private Sub NonRefCr8_Calculation()
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(7)), GetCurrency(IAWBP148Sp.NonRefTax8))
End Sub

Private Sub NonRefCr9_Calculation()
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(8)), GetCurrency(IAWBP148Sp.NonRefTax9))
End Sub

Private Sub NonRefTax10_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax9) - GetCurrency(IAWBP148Sp.NonRefCr9))
End Sub

Private Sub NonRefTax11_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax10) - GetCurrency(IAWBP148Sp.NonRefCr10))
End Sub

Private Sub NonRefTax12_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax11) - GetCurrency(IAWBP148Sp.NonRefCr11))
End Sub

Private Sub NonRefTax13_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax12) - GetCurrency(IAWBP148Sp.NonRefCr12))
End Sub

Private Sub NonRefTax14_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax13) - GetCurrency(IAWBP148Sp.NonRefCr13))
End Sub

Private Sub NonRefTax15_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax14) - GetCurrency(IAWBP148Sp.NonRefCr14))
End Sub

Private Sub NonRefTax16_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax15) - GetCurrency(IAWBP148Sp.NonRefCr15))
End Sub

Private Sub NonRefTax17_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax16) - GetCurrency(IAWBP148Sp.NonRefCr16))
End Sub

Private Sub NonRefTax18_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax17) - GetCurrency(IAWBP148Sp.NonRefCr17))
End Sub

Private Sub NonRefTax19_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax18) - GetCurrency(IAWBP148Sp.NonRefCr18))
End Sub

Private Sub NonRefTax2_Calculation()
    Dim PriorCopy As Long
    
    PriorCopy = GetCopy()
        
    If GetCopy() = 1 Then
        ReturnVal = MaxValue(0, GetCurrency(IA148Sp.NonRefTax10) - GetCurrency(IAWBP148Sp.NonRefCr1))
    Else
        ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax30, PriorCopy - 1) - GetCurrency(IAWBP148Sp.NonRefCr1))
    End If
End Sub

Private Sub NonRefTax20_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax19) - GetCurrency(IAWBP148Sp.NonRefCr19))
End Sub

Private Sub NonRefTax21_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax20) - GetCurrency(IAWBP148Sp.NonRefCr20))
End Sub

Private Sub NonRefTax22_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax21) - GetCurrency(IAWBP148Sp.NonRefCr21))
End Sub

Private Sub NonRefTax23_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax22) - GetCurrency(IAWBP148Sp.NonRefCr22))
End Sub

Private Sub NonRefTax24_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax23) - GetCurrency(IAWBP148Sp.NonRefCr23))
End Sub

Private Sub NonRefTax25_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax24) - GetCurrency(IAWBP148Sp.NonRefCr24))
End Sub

Private Sub NonRefTax26_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax25) - GetCurrency(IAWBP148Sp.NonRefCr25))
End Sub

Private Sub NonRefTax27_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax26) - GetCurrency(IAWBP148Sp.NonRefCr26))
End Sub

Private Sub NonRefTax28_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax27) - GetCurrency(IAWBP148Sp.NonRefCr27))
End Sub

Private Sub NonRefTax29_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax28) - GetCurrency(IAWBP148Sp.NonRefCr28))
End Sub

Private Sub NonRefTax3_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax2) - GetCurrency(IAWBP148Sp.NonRefCr2))
End Sub

Private Sub NonRefTax30_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax29) - GetCurrency(IAWBP148Sp.NonRefCr29))
End Sub

Private Sub NonRefTax4_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax3) - GetCurrency(IAWBP148Sp.NonRefCr3))
End Sub

Private Sub NonRefTax5_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax4) - GetCurrency(IAWBP148Sp.NonRefCr4))
End Sub

Private Sub NonRefTax6_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax5) - GetCurrency(IAWBP148Sp.NonRefCr5))
End Sub

Private Sub NonRefTax7_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax6) - GetCurrency(IAWBP148Sp.NonRefCr6))
End Sub

Private Sub NonRefTax8_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax7) - GetCurrency(IAWBP148Sp.NonRefCr7))
End Sub

Private Sub NonRefTax9_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax8) - GetCurrency(IAWBP148Sp.NonRefCr8))
End Sub

Private Sub NonRefTrig_Calculation(Index As Integer)
    If GetString(IAWBP148Sp.NonRefCode(Index)) = "04" Or GetString(IAWBP148Sp.NonRefCode(Index)) = "11" Or GetString(IAWBP148Sp.NonRefCode(Index)) = "09" Then
        ReturnVal = 0
    ElseIf GetCurrency(IAWBP148Sp.AvailCr(Index)) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Offset_Calculation()
    If GetCopy() = 1 Then
        ReturnVal = 9
    ElseIf GetCopy() = 2 Then
        ReturnVal = 38
    Else
        ReturnVal = 67
    End If
End Sub

Private Sub Print_Calculation()
    If GetCurrency(IAWBP148Sp.TotNonRefCr) > 0 Then
        ReturnVal = 1
    ElseIf Trim(GetString(IAWBP148sp.NonRefCode(0))) <> "" Or GetCurrency(IAWBP148sp.CYCredit(0)) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PTECode_Calculation(Index As Integer)
    Dim Stuff As Integer
    
    Stuff = Index + GetNumber(IAWBP148Sp.Offset) + 1

    ReturnVal = GetString(IA148BumpSp.PTECode(Stuff))
End Sub

Private Sub PTEEIN_Calculation(Index As Integer)
    Dim Stuff As Integer
    
    Stuff = Index + GetNumber(IAWBP148Sp.Offset) + 1

    ReturnVal = GetString(IA148BumpSp.PTEEIN(Stuff))
End Sub

Private Sub PTEName_Calculation(Index As Integer)
    Dim Stuff As Integer
    
    Stuff = Index + GetNumber(IAWBP148Sp.Offset) + 1

    ReturnVal = GetString(IA148BumpSp.PTEName(Stuff))
End Sub

Private Sub PTENRTrig_Calculation(Index As Integer)
    If GetString(IAWBP148Sp.NonRefCode(Index)) = "04" Or GetString(IAWBP148Sp.PTECode(Index)) = "11" Or GetString(IAWBP148Sp.PTECode(Index)) = "09" Then
        ReturnVal = 0
    ElseIf Trim(GetString(IAWBP148Sp.PTEName(Index))) <> "" Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PYCarry_Calculation(Index As Integer)
  Dim strindex As Long
  Dim copystr As String
  Dim Copy As Long
  
  strindex = ((((GetCopy() - 1) * 29) + 9 + Index) * 4) + 1
  copystr = Trim(Mid(GetString(IA148Sp.NonRefCopiesStr), strindex, 4))
  
  If GetNumber(IA148Sp.NonRefNbr) = 10 Then
    ReturnVal = 0
  ElseIf copystr <> "" Then
    Copy = CLng(copystr)
    If (Copy > 100) And (Copy <= 200) Then
      ReturnVal = 0
    ElseIf (Copy > 200) And (Copy <= 300) Then
      ReturnVal = 0
    ElseIf (Copy > 300) And (Copy <= 400) Then
      ReturnVal = GetCurrency(IACred.PYCarry, (Copy) - 300)
    ElseIf (Copy > 400) And (Copy <= 500) Then
      ReturnVal = GetCurrency(IACred.PYCarry, (Copy) - 400)
    ElseIf (Copy > 500) And (Copy <= 600) Then
      ReturnVal = GetCurrency(IACred.PYCarry, (Copy) - 500)
    ElseIf (Copy > 600) And (Copy <= 700) Then
      ReturnVal = GetCurrency(IACred.PYCarry, (Copy) - 600)
    ElseIf (Copy > 700) And (Copy <= 800) Then
      ReturnVal = GetCurrency(IACred.PYCarry, (Copy) - 700)
    ElseIf (Copy > 800) And (Copy <= 900) Then
      ReturnVal = GetCurrency(IACred.PYCarry, (Copy) - 800)
    ElseIf (Copy > 900) And (Copy <= 1000) Then
      ReturnVal = GetCurrency(IACred.PYCarry, (Copy) - 900)
    ElseIf (Copy > 1000) And (Copy <= 1100) Then
      ReturnVal = GetCurrency(IACred.PYCarry, (Copy) - 1000)
    ElseIf (Copy > 1100) And (Copy <= 1200) Then
      ReturnVal = GetCurrency(IACred.PYCarry, (Copy) - 1100)
    ElseIf (Copy > 1200) And (Copy <= 1300) Then
      ReturnVal = GetCurrency(IACred.PYCarry, (Copy) - 1200)
    ElseIf (Copy > 1300) And (Copy <= 1400) Then
      ReturnVal = GetCurrency(IACred.PYCarry, (Copy) - 1300)
    ElseIf (Copy > 1400) And (Copy <= 1500) Then
      ReturnVal = GetCurrency(IACred.PYCarry, (Copy) - 1400)
    ElseIf (Copy > 1500) And (Copy <= 1600) Then
      ReturnVal = GetCurrency(IACred.PYCarry, (Copy) - 1500)
    ElseIf (Copy > 1600) And (Copy <= 1700) Then
      ReturnVal = GetCurrency(IACred.PYCarry, (Copy) - 1600)
    ElseIf (Copy > 1700) And (Copy <= 1800) Then
      ReturnVal = GetCurrency(IACred.PYCarry, (Copy) - 1700)
    ElseIf (Copy > 1800) And (Copy <= 1900) Then
      ReturnVal = GetCurrency(IACred.PYCarry, (Copy) - 1800)
    ElseIf (Copy > 1900) And (Copy <= 2000) Then
      ReturnVal = GetCurrency(IACred.PYCarry, (Copy) - 1900)
    ElseIf (Copy > 2000) And (Copy <= 2100) Then
      ReturnVal = GetCurrency(IACred.PYCarry, (Copy) - 2000)
    ElseIf (Copy > 2100) And (Copy <= 2200) Then
      ReturnVal = GetCurrency(IACred.PYCarry, (Copy) - 2100)
    ElseIf (Copy > 2200) And (Copy <= 2300) Then
      ReturnVal = GetCurrency(IACred.PYCarry, (Copy) - 2200)
    ElseIf (Copy > 2300) And (Copy <= 2400) Then
      ReturnVal = GetCurrency(IACred.PYCarry, (Copy) - 2300)
    ElseIf (Copy > 2400) And (Copy <= 2500) Then
      ReturnVal = GetCurrency(IA8801Sp.PYCarryforward)
    End If
  End If
  ReturnVal = 0
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IA148Sp.SSN)
End Sub

Private Sub TotNonRefCr_Calculation()
    Dim NonRefCr1 As Currency
    Dim NonRefCr2 As Currency
    Dim NonRefCr3 As Currency
    
    NonRefCr1 = GetCurrency(IAWBP148Sp.NonRefCr1) + GetCurrency(IAWBP148Sp.NonRefCr2) + GetCurrency(IAWBP148Sp.NonRefCr3) + GetCurrency(IAWBP148Sp.NonRefCr4) + GetCurrency(IAWBP148Sp.NonRefCr5) + GetCurrency(IAWBP148Sp.NonRefCr6) + GetCurrency(IAWBP148Sp.NonRefCr7) + GetCurrency(IAWBP148Sp.NonRefCr8) + GetCurrency(IAWBP148Sp.NonRefCr9) + GetCurrency(IAWBP148Sp.NonRefCr10)
    NonRefCr2 = GetCurrency(IAWBP148Sp.NonRefCr11) + GetCurrency(IAWBP148Sp.NonRefCr12) + GetCurrency(IAWBP148Sp.NonRefCr13) + GetCurrency(IAWBP148Sp.NonRefCr14) + GetCurrency(IAWBP148Sp.NonRefCr15) + GetCurrency(IAWBP148Sp.NonRefCr16) + GetCurrency(IAWBP148Sp.NonRefCr17) + GetCurrency(IAWBP148Sp.NonRefCr18) + GetCurrency(IAWBP148Sp.NonRefCr19) + GetCurrency(IAWBP148Sp.NonRefCr20)
    NonRefCr3 = GetCurrency(IAWBP148Sp.NonRefCr21) + GetCurrency(IAWBP148Sp.NonRefCr22) + GetCurrency(IAWBP148Sp.NonRefCr23) + GetCurrency(IAWBP148Sp.NonRefCr24) + GetCurrency(IAWBP148Sp.NonRefCr25) + GetCurrency(IAWBP148Sp.NonRefCr26) + GetCurrency(IAWBP148Sp.NonRefCr27) + GetCurrency(IAWBP148Sp.NonRefCr28) + GetCurrency(IAWBP148Sp.NonRefCr29)
    
    ReturnVal = NonRefCr1 + NonRefCr2 + NonRefCr3
End Sub

Private Sub TPPerc_Calculation(Index As Integer)
    Dim Stuff As Integer
    
    Stuff = Index + GetNumber(IAWBP148Sp.Offset) + 1

    ReturnVal = GetFloat(IA148BumpSp.TPPerc(Stuff))
End Sub

