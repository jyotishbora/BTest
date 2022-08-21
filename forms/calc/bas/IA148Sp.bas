Private Sub ArrayNonRefCr_Calculation(Index As Integer)
    If Index = 0 Then
        ReturnVal = GetCurrency(IA148Sp.NonRefCr1)
    ElseIf Index = 1 Then
        ReturnVal = GetCurrency(IA148Sp.NonRefCr2)
    ElseIf Index = 2 Then
        ReturnVal = GetCurrency(IA148Sp.NonRefCr3)
    ElseIf Index = 3 Then
        ReturnVal = GetCurrency(IA148Sp.NonRefCr4)
    ElseIf Index = 4 Then
        ReturnVal = GetCurrency(IA148Sp.NonRefCr5)
    ElseIf Index = 5 Then
        ReturnVal = GetCurrency(IA148Sp.NonRefCr6)
    ElseIf Index = 6 Then
        ReturnVal = GetCurrency(IA148Sp.NonRefCr7)
    ElseIf Index = 7 Then
        ReturnVal = GetCurrency(IA148Sp.NonRefCr8)
    ElseIf Index = 8 Then
        ReturnVal = GetCurrency(IA148Sp.NonRefCr9)
    Else
        ReturnVal = GetCurrency(IA148Sp.NonRefCr10)
    End If
End Sub

Private Sub AvailCr_Calculation(Index As Integer)
    If GetString(IA148Sp.NonRefCode(Index)) = "09" Then
        ReturnVal = GetCurrency(IA8801Sp.AMTCR)
    Else
        ReturnVal = GetCurrency(IA148Sp.PYCarry(Index)) + GetCurrency(IA148Sp.CYCredit(Index))
    End If
End Sub

Private Sub CreateBPNonRef1_Calculation()
    If GetNumber(IA148Sp.NonRefNbr) > 10 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CreateBPNonRef2_Calculation()
    If GetNumber(IA148Sp.NonRefNbr) > 38 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CreateBPNonRef3_Calculation()
    If GetNumber(IA148Sp.NonRefNbr) > 67 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CreateBPNonRef4_Calculation()
    If GetNumber(IA148Sp.NonRefNbr) > 96 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CreateBPPTE1_Calculation()
    If GetNumber(IA148Sp.TotPTE) > 6 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CreateBPPTE2_Calculation()
    If GetNumber(IA148Sp.TotPTE) > 35 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CreateBPPTE3_Calculation()
    If GetNumber(IA148Sp.TotPTE) > 65 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CreateBPPTE4_Calculation()
    If GetNumber(IA148Sp.TotPTE) > 95 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CreateBPPTE5_Calculation()
    If GetNumber(IA148Sp.TotPTE) > 125 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CreateBPRef1_Calculation()
    If GetNumber(IA148Sp.RefNbr) > 7 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CreateBPRef2_Calculation()
    If GetNumber(IA148Sp.RefNbr) > 56 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CYCarry_Calculation(Index As Integer)
    If GetString(IA148Sp.NonRefCode(Index)) = "09" Then
        ReturnVal = GetCurrency(IA8801Sp.CYCarryforward)
    Else
        ReturnVal = MaxValue(0, GetCurrency(IA148Sp.AvailCr(Index)) - GetCurrency(IA148Sp.ArrayNonRefCr(Index)) - GetCurrency(IA148Sp.ExpCr(Index)))
    End If
End Sub

Private Sub CYCredit_Calculation(Index As Integer)
  Dim strindex As Long
  Dim copystr As String
  Dim Copy As Long
  
  strindex = ((Index) * 4) + 1
  copystr = Trim(Mid(GetString(IA148Sp.NonRefCopiesStr), strindex, 4))
  
  If Index = 9 And GetNumber(IA148Sp.NonRefNbr) > 10 Then
    ReturnVal = 0
  ElseIf copystr <> "" Then
    Copy = CLng(copystr)
    If (Copy > 100) And (Copy <= 200) Then
      ReturnVal = GetCurrency(IA147.FranchiseCr, (Copy) - 100)
    ElseIf (Copy > 200) And (Copy <= 300) Then
      ReturnVal = GetCurrency(IA134Sp.Credit, (Copy) - 200)
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
    Dim Total2 As Currency
    
    Total1 = GetCurrency(IA148Sp.TotNonRefCr)
    Total2 = GetCurrency(IA148Sp.TotRefCr)
    
    If Total1 > 0 And Total2 = 0 Then
        ReturnVal = CStr(Total1) & " Nonrefundable Credits"
    ElseIf Total1 = 0 And Total2 > 0 Then
        ReturnVal = CStr(Total2) & " Refundable Credits"
    ElseIf Total1 > 0 And Total2 > 0 Then
        ReturnVal = CStr(Total1) & " Nonrefundable Credits " & CStr(Total2) & " Refundable Credits"
    Else
        ReturnVal = CStr(Total1) & " Credits"
    End If
End Sub

Private Sub ExpCr_Calculation(Index As Integer)
  Dim strindex As Long
  Dim copystr As String
  Dim Copy As Long
  
  strindex = ((Index) * 4) + 1
  copystr = Trim(Mid(GetString(IA148Sp.NonRefCopiesStr), strindex, 4))
  
  If Index = 9 And GetNumber(IA148Sp.NonRefNbr) > 10 Then
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

Private Sub FirstCopy137Site_Calculation()
    Dim count As Long
    Dim max As Long

    max = GetAllCopies(IA137)
    count = 0
    
    Do While count < max
        count = count + 1
        If GetBool(IA137.Spouse, count) = True And GetBool(IA137.Site, count) = True And GetCurrency(IA137.TotEthSoldCr, count) > 0 Then
            ReturnVal = count
        Else
            count = count
        End If
    Loop
        
    ReturnVal = 0
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.SPCombName)
End Sub

Private Sub NonRefCert_Calculation(Index As Integer)
  Dim strindex As Long
  Dim copystr As String
  Dim Copy As Long
  
  strindex = ((Index) * 4) + 1
  copystr = Trim(Mid(GetString(IA148Sp.NonRefCopiesStr), strindex, 4))
  
  If Index = 9 And GetNumber(IA148Sp.NonRefNbr) > 10 Then
    ReturnVal = "Stmt Att."
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
  
  strindex = ((Index) * 4) + 1
  copystr = Trim(Mid(GetString(IA148Sp.NonRefCopiesStr), strindex, 4))
  
  If Index = 9 And GetNumber(IA148Sp.NonRefNbr) > 10 Then
    ReturnVal = "See"
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

Private Sub NonRefCopiesStr_Calculation()
'2017 removed credit codes 18 and 19 which were in credit order #10 and #11, re-used Copy10, Copystr10 and copiesstr10 for new credit code #28 and put it last in the order since no new IA Admin Rule is out, left copy11, copystr11 and copiesstr11 for future use
    Dim Copy As Long
    Dim Copy2 As Long
    Dim Copy3 As Long
    Dim Copy4 As Long
    Dim Copy5 As Long
    Dim Copy6 As Long
    Dim Copy7 As Long
    Dim Copy8 As Long
    Dim Copy9 As Long
    Dim Copy10 As Long
    Dim Copy11 As Long
    Dim Copy12 As Long
    Dim Copy13 As Long
    Dim Copy14 As Long
    Dim Copy15 As Long
    Dim Copy16 As Long
    Dim Copy17 As Long
    Dim Copy18 As Long
    Dim Copy19 As Long
    Dim Copy20 As Long
    Dim Copy21 As Long
    Dim Copy22 As Long
    Dim Copy23 As Long
    Dim Copy24 As Long
    
    Dim max As Long
    Dim max2 As Long
    Dim max3 As Long
    Dim max4 As Long
    
    Dim copystr As String
    Dim copystr2 As String
    Dim copystr3 As String
    Dim copystr4 As String
    Dim copystr5 As String
    Dim copystr6 As String
    Dim copystr7 As String
    Dim copystr8 As String
    Dim copystr9 As String
    Dim copystr10 As String
    Dim copystr11 As String
    Dim copystr12 As String
    Dim copystr13 As String
    Dim copystr14 As String
    Dim copystr15 As String
    Dim copystr16 As String
    Dim copystr17 As String
    Dim copystr18 As String
    Dim copystr19 As String
    Dim copystr20 As String
    Dim copystr21 As String
    Dim copystr22 As String
    Dim copystr23 As String
    Dim copystr24 As String
    
    Dim copiesstr As String
    Dim copiesstr2 As String
    Dim copiesstr3 As String
    Dim copiesstr4 As String
    Dim copiesstr5 As String
    Dim copiesstr6 As String
    Dim copiesstr7 As String
    Dim copiesstr8 As String
    Dim copiesstr9 As String
    Dim copiesstr10 As String
    Dim copiesstr11 As String
    Dim copiesstr12 As String
    Dim copiesstr13 As String
    Dim copiesstr14 As String
    Dim copiesstr15 As String
    Dim copiesstr16 As String
    Dim copiesstr17 As String
    Dim copiesstr18 As String
    Dim copiesstr19 As String
    Dim copiesstr20 As String
    Dim copiesstr21 As String
    Dim copiesstr22 As String
    Dim copiesstr23 As String
    Dim copiesstr24 As String
    
    copiesstr = ""
    Copy = 1
    max = GetAllCopies(IA147)
    
    Do While Copy <= max
        If GetCurrency(IA147.FranchiseCr, Copy) > 0 Then
            If GetCurrency(IA147.FranchiseCr, Copy) > 0 And GetBool(IA147.Spouse, Copy) = True Then
                copystr = CStr(Copy + 100)
                Do While Len(copystr) < 4
                    copystr = copystr + " "
                Loop
                copiesstr = copiesstr + copystr
            End If
        End If
     Copy = Copy + 1
    Loop
    
    copiesstr2 = ""
    Copy2 = 1
    max2 = GetAllCopies(IA134Sp)
    
    Do While Copy2 <= max2
        If GetCurrency(IA134Sp.Credit, Copy2) > 0 Then
            If GetCurrency(IA134Sp.Credit, Copy2) > 0 Then
                copystr2 = CStr(Copy2 + 200) + " "
                copiesstr2 = copiesstr2 + copystr2
            End If
        End If
        Copy2 = Copy2 + 1
    Loop
    
    max3 = GetAllCopies(IACred)
    copiesstr3 = ""
    copiesstr4 = ""
    copiesstr5 = ""
    copiesstr6 = ""
    copiesstr7 = ""
    copiesstr8 = ""
    copiesstr9 = ""
    copiesstr10 = ""
    copiesstr11 = ""
    copiesstr12 = ""
    copiesstr13 = ""
    copiesstr14 = ""
    copiesstr15 = ""
    copiesstr16 = ""
    copiesstr17 = ""
    copiesstr18 = ""
    copiesstr19 = ""
    copiesstr20 = ""
    copiesstr21 = ""
    copiesstr22 = ""
    copiesstr23 = ""
    copiesstr24 = ""
    
    
    Copy3 = 1
    Copy4 = 1
    Copy5 = 1
    Copy6 = 1
    Copy7 = 1
    Copy8 = 1
    Copy9 = 1
    Copy10 = 1
    Copy11 = 1
    Copy12 = 1
    Copy13 = 1
    Copy14 = 1
    Copy15 = 1
    Copy16 = 1
    Copy17 = 1
    Copy18 = 1
    Copy19 = 1
    Copy20 = 1
    Copy21 = 1
    Copy22 = 1
    Copy23 = 1
    
    
    Do While Copy3 <= max3
        If GetString(IACred.Code, Copy3) = "12" Then
    
            If GetBool(IACred.NonRefCr, Copy3) = True And GetBool(IACred.Spouse, Copy3) = True And GetString(IACred.Code, Copy3) = "12" Then
                copystr3 = CStr(Copy3 + 300) + " "
                copiesstr3 = copiesstr3 + copystr3
            End If
            
        End If
        Copy3 = Copy3 + 1
    Loop
    
    Do While Copy4 <= max3
        If GetString(IACred.Code, Copy4) = "14" Then
    
            If GetBool(IACred.NonRefCr, Copy4) = True And GetBool(IACred.Spouse, Copy4) = True And GetString(IACred.Code, Copy4) = "14" Then
                copystr4 = CStr(Copy4 + 400) + " "
                copiesstr4 = copiesstr4 + copystr4
            End If
            
        End If
        Copy4 = Copy4 + 1
    Loop
    
    Do While Copy5 <= max3
        If GetString(IACred.Code, Copy5) = "15" Then
    
            If GetBool(IACred.NonRefCr, Copy5) = True And GetBool(IACred.Spouse, Copy5) = True And GetString(IACred.Code, Copy5) = "15" Then
                copystr5 = CStr(Copy5 + 500) + " "
                copiesstr5 = copiesstr5 + copystr5
            End If
            
        End If
        Copy5 = Copy5 + 1
    Loop
    
    Do While Copy6 <= max3
        If GetString(IACred.Code, Copy6) = "25" Then
            
            If GetBool(IACred.NonRefCr, Copy6) = True And GetBool(IACred.Spouse, Copy6) = True And GetString(IACred.Code, Copy6) = "25" Then
                copystr6 = CStr(Copy6 + 600) + " "
                copiesstr6 = copiesstr6 + copystr6
            End If
            
        End If
        Copy6 = Copy6 + 1
    Loop
            
    Do While Copy7 <= max3
        If GetString(IACred.Code, Copy7) = "03" Then
            
            If GetBool(IACred.NonRefCr, Copy7) = True And GetBool(IACred.Spouse, Copy7) = True And GetString(IACred.Code, Copy7) = "03" Then
                copystr7 = CStr(Copy7 + 700) + " "
                copiesstr7 = copiesstr7 + copystr7
            End If
            
        End If
        Copy7 = Copy7 + 1
    Loop
            
    Do While Copy8 <= max3
        If GetString(IACred.Code, Copy8) = "17" Then
            
            If GetBool(IACred.NonRefCr, Copy8) = True And GetBool(IACred.Spouse, Copy8) = True And GetString(IACred.Code, Copy8) = "17" Then
                copystr8 = CStr(Copy8 + 800) + " "
                copiesstr8 = copiesstr8 + copystr8
            End If
            
        End If
        Copy8 = Copy8 + 1
    Loop

    Do While Copy9 <= max3
        If GetString(IACred.Code, Copy9) = "24" Then
            
            If GetBool(IACred.NonRefCr, Copy9) = True And GetBool(IACred.Spouse, Copy9) = True And GetString(IACred.Code, Copy9) = "24" Then
                copystr9 = CStr(Copy9 + 900) + " "
                copiesstr9 = copiesstr9 + copystr9
            End If
            
        End If
        Copy9 = Copy9 + 1
    Loop
            
    Do While Copy10 <= max3
        If GetString(IACred.Code, Copy10) = "28" Then
            
            If GetBool(IACred.NonRefCr, Copy10) = True And GetBool(IACred.Spouse, Copy10) = True And GetString(IACred.Code, Copy10) = "28" Then
                copystr10 = CStr(Copy10 + 1000)
                copiesstr10 = copiesstr10 + copystr10
            End If
            
        End If
        Copy10 = Copy10 + 1
    Loop

            
    Do While Copy12 <= max3
        If GetString(IACred.Code, Copy12) = "21" Then
            
            If GetBool(IACred.NonRefCr, Copy12) = True And GetBool(IACred.Spouse, Copy12) = True And GetString(IACred.Code, Copy12) = "21" Then
                copystr12 = CStr(Copy12 + 1200)
                copiesstr12 = copiesstr12 + copystr12
            End If
            
        End If
        Copy12 = Copy12 + 1
    Loop
            

    Do While Copy13 <= max3
        If GetString(IACred.Code, Copy13) = "26" Then
            
            If GetBool(IACred.NonRefCr, Copy13) = True And GetBool(IACred.Spouse, Copy13) = True And GetString(IACred.Code, Copy13) = "26" Then
                copystr13 = CStr(Copy13 + 1300)
                copiesstr13 = copiesstr13 + copystr13
            End If
            
        End If
        Copy13 = Copy13 + 1
    Loop

    Do While Copy14 <= max3
        If GetString(IACred.Code, Copy14) = "06" Then
            
            If GetBool(IACred.NonRefCr, Copy14) = True And GetBool(IACred.Spouse, Copy14) = True And GetString(IACred.Code, Copy14) = "06" Then
                copystr14 = CStr(Copy14 + 1400)
                copiesstr14 = copiesstr14 + copystr14
            End If
            
        End If
        Copy14 = Copy14 + 1
    Loop

    Do While Copy15 <= max3
        If GetString(IACred.Code, Copy15) = "07" Then
            
            If GetBool(IACred.NonRefCr, Copy15) = True And GetBool(IACred.Spouse, Copy15) = True And GetString(IACred.Code, Copy15) = "07" Then
                copystr15 = CStr(Copy15 + 1500)
                copiesstr15 = copiesstr15 + copystr15
            End If
            
        End If
        Copy15 = Copy15 + 1
    Loop

    Do While Copy16 <= max3
        If GetString(IACred.Code, Copy16) = "27" Then
            
            If GetBool(IACred.NonRefCr, Copy16) = True And GetBool(IACred.Spouse, Copy16) = True And GetString(IACred.Code, Copy16) = "27" Then
                copystr16 = CStr(Copy16 + 1600)
                copiesstr16 = copiesstr16 + copystr16
            End If
            
        End If
        Copy16 = Copy16 + 1
    Loop

    Do While Copy17 <= max3
        If GetString(IACred.Code, Copy17) = "16" Then
            
            If GetBool(IACred.NonRefCr, Copy17) = True And GetBool(IACred.Spouse, Copy17) = True And GetString(IACred.Code, Copy17) = "16" Then
                copystr17 = CStr(Copy17 + 1700)
                copiesstr17 = copiesstr17 + copystr17
            End If
            
        End If
        Copy17 = Copy17 + 1
    Loop

    Do While Copy18 <= max3
        If GetString(IACred.Code, Copy18) = "10" Then
            
           If GetBool(IACred.NonRefCr, Copy18) = True And GetBool(IACred.Spouse, Copy18) = True And GetString(IACred.Code, Copy18) = "10" Then
                copystr18 = CStr(Copy18 + 1800)
                copiesstr18 = copiesstr18 + copystr18
            End If
            
        End If
        Copy18 = Copy18 + 1
    Loop

    Do While Copy19 <= max3
        If GetString(IACred.Code, Copy19) = "13" Then
            
            If GetBool(IACred.NonRefCr, Copy19) = True And GetBool(IACred.Spouse, Copy19) = True And GetString(IACred.Code, Copy19) = "13" Then
                copystr19 = CStr(Copy19 + 1900)
                copiesstr19 = copiesstr19 + copystr19
            End If
            
        End If
        Copy19 = Copy19 + 1
    Loop
            
    Do While Copy20 <= max3
        If GetString(IACred.Code, Copy20) = "08" Then
            
            If GetBool(IACred.NonRefCr, Copy20) = True And GetBool(IACred.Spouse, Copy20) = True And GetString(IACred.Code, Copy20) = "08" Then
                copystr20 = CStr(Copy20 + 2000)
                copiesstr20 = copiesstr20 + copystr20
            End If
            
        End If
        Copy20 = Copy20 + 1
    Loop
            
    Do While Copy21 <= max3
        If GetString(IACred.Code, Copy21) = "23" Then
            
            If GetBool(IACred.NonRefCr, Copy21) = True And GetBool(IACred.Spouse, Copy21) = True And GetString(IACred.Code, Copy21) = "23" Then
                copystr21 = CStr(Copy21 + 2100)
                copiesstr21 = copiesstr21 + copystr21
            End If
            
        End If
        Copy21 = Copy21 + 1
    Loop
            
    Do While Copy22 <= max3
        If GetString(IACred.Code, Copy22) = "22" Then
            
            If GetBool(IACred.NonRefCr, Copy22) = True And GetBool(IACred.Spouse, Copy22) = True And GetString(IACred.Code, Copy22) = "22" Then
                copystr22 = CStr(Copy22 + 2200)
                copiesstr22 = copiesstr22 + copystr22
            End If
            
        End If
        Copy22 = Copy22 + 1
    Loop
            
    Do While Copy23 <= max3
        If GetString(IACred.Code, Copy23) = "20" Then
            
            If GetBool(IACred.NonRefCr, Copy23) = True And GetBool(IACred.Spouse, Copy23) = True And GetString(IACred.Code, Copy23) = "20" Then
                copystr23 = CStr(Copy23 + 2300)
                copiesstr23 = copiesstr23 + copystr23
            End If
            
        End If
        Copy23 = Copy23 + 1
    Loop
              
    copiesstr24 = ""
    Copy24 = 1
    max4 = GetAllCopies(IA8801Sp)
    
    Do While Copy24 <= max4
        If GetCurrency(IA8801Sp.Print, Copy24) > 0 Then
            If GetCurrency(IA8801Sp.Print, Copy24) > 0 Then
                copystr24 = CStr(Copy24 + 2400)
                copiesstr24 = copiesstr24 + copystr24
            End If
        End If
        Copy24 = Copy24 + 1
    Loop
    
    ReturnVal = copiesstr + copiesstr2 + copiesstr3 + copiesstr4 + copiesstr5 + copiesstr7 + copiesstr12 + copiesstr13 + copiesstr16 + copiesstr14 + copiesstr15 + copiesstr17 + copiesstr18 + copiesstr19 + copiesstr20 + copiesstr6 + copiesstr8 + copiesstr9 + copiesstr21 + copiesstr22 + copiesstr23 + copiesstr24 + copiesstr10
End Sub

Private Sub NonRefCr1_Calculation()
    ReturnVal = MinValue(GetCurrency(IA148Sp.AvailCr(0)), GetCurrency(IAF1040.BBal3))
End Sub

Private Sub NonRefCr10_Calculation()
    If GetNumber(IA148Sp.NonRefNbr) > 10 Then
        ReturnVal = GetCurrency(IAWBP148Sp.TotNonRefCr)
    Else
        ReturnVal = MinValue(GetCurrency(IA148Sp.AvailCr(9)), GetCurrency(IA148Sp.NonRefTax10))
    End If
End Sub

Private Sub NonRefCr2_Calculation()
    ReturnVal = MinValue(GetCurrency(IA148Sp.AvailCr(1)), GetCurrency(IA148Sp.NonRefTax2))
End Sub

Private Sub NonRefCr3_Calculation()
    ReturnVal = MinValue(GetCurrency(IA148Sp.AvailCr(2)), GetCurrency(IA148Sp.NonRefTax3))
End Sub

Private Sub NonRefCr4_Calculation()
    ReturnVal = MinValue(GetCurrency(IA148Sp.AvailCr(3)), GetCurrency(IA148Sp.NonRefTax4))
End Sub

Private Sub NonRefCr5_Calculation()
    ReturnVal = MinValue(GetCurrency(IA148Sp.AvailCr(4)), GetCurrency(IA148Sp.NonRefTax5))
End Sub

Private Sub NonRefCr6_Calculation()
    ReturnVal = MinValue(GetCurrency(IA148Sp.AvailCr(5)), GetCurrency(IA148Sp.NonRefTax6))
End Sub

Private Sub NonRefCr7_Calculation()
    ReturnVal = MinValue(GetCurrency(IA148Sp.AvailCr(6)), GetCurrency(IA148Sp.NonRefTax7))
End Sub

Private Sub NonRefCr8_Calculation()
    ReturnVal = MinValue(GetCurrency(IA148Sp.AvailCr(7)), GetCurrency(IA148Sp.NonRefTax8))
End Sub

Private Sub NonRefCr9_Calculation()
    ReturnVal = MinValue(GetCurrency(IA148Sp.AvailCr(8)), GetCurrency(IA148Sp.NonRefTax9))
End Sub

Private Sub NonRefNbr_Calculation()
    Dim count2 As Integer
    Dim Lim2 As Integer
    Dim Total As Integer
    
    Lim2 = GetAllCopies(IA147)
    count2 = 1
    Total = 0
    
    Do While count2 <= Lim2
        If GetBool(IA147.Spouse, count2) = True And GetCurrency(IA147.FranchiseCr, count2) > 0 Then
            Total = Total + 1
        Else
            Total = Total
        End If
        
        count2 = count2 + 1
    Loop
    
    Dim count3 As Integer
    Dim Lim3 As Integer
    
    Lim3 = GetAllCopies(IA134Sp)
    count3 = 1
    
    Do While count3 <= Lim3
        If GetCurrency(IA134Sp.Credit, count3) > 0 Then
            Total = Total + 1
        Else
            Total = Total
        End If
        
        count3 = count3 + 1
    Loop
    
    Dim count As Integer
    Dim Lim As Integer
    Dim IACredit As String
    
    Lim = GetAllCopies(IACred)
    count = 1
    
    
    Do While count <= Lim
        IACredit = GetString(IACred.Code, count)
        If GetBool(IACred.NonRefCr, count) = True And GetBool(IACred.Spouse, count) = True And (IACredit = "12" Or IACredit = "14" Or IACredit = "15" Or IACredit = "25" Or IACredit = "03" Or IACredit = "17" Or IACredit = "24" Or IACredit = "21" Or IACredit = "26" Or IACredit = "06" Or IACredit = "07" Or IACredit = "27" Or IACredit = "16" Or IACredit = "10" Or IACredit = "13" Or IACredit = "08" Or IACredit = "23" Or IACredit = "22" Or IACredit = "20" Or IACredit = "28") Then
            Total = Total + 1
        Else
            Total = Total
        End If
        
        count = count + 1
    Loop
    
    ReturnVal = Total + GetBool(IA8801Sp.Print)
End Sub

Private Sub NonRefTax10_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA148Sp.NonRefTax9) - GetCurrency(IA148Sp.NonRefCr9))
End Sub

Private Sub NonRefTax2_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAF1040.BBal3) - GetCurrency(IA148Sp.NonRefCr1))
End Sub

Private Sub NonRefTax3_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA148Sp.NonRefTax2) - GetCurrency(IA148Sp.NonRefCr2))
End Sub

Private Sub NonRefTax4_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA148Sp.NonRefTax3) - GetCurrency(IA148Sp.NonRefCr3))
End Sub

Private Sub NonRefTax5_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA148Sp.NonRefTax4) - GetCurrency(IA148Sp.NonRefCr4))
End Sub

Private Sub NonRefTax6_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA148Sp.NonRefTax5) - GetCurrency(IA148Sp.NonRefCr5))
End Sub

Private Sub NonRefTax7_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA148Sp.NonRefTax6) - GetCurrency(IA148Sp.NonRefCr6))
End Sub

Private Sub NonRefTax8_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA148Sp.NonRefTax7) - GetCurrency(IA148Sp.NonRefCr7))
End Sub

Private Sub NonRefTax9_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IA148Sp.NonRefTax8) - GetCurrency(IA148Sp.NonRefCr8))
End Sub

Private Sub NonRefTrig_Calculation(Index As Integer)
    If GetString(IA148Sp.NonRefCode(Index)) = "04" Or GetString(IA148Sp.NonRefCode(Index)) = "11" Or GetString(IA148Sp.NonRefCode(Index)) = "09" Then
        ReturnVal = 0
    ElseIf GetCurrency(IA148Sp.AvailCr(Index)) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Print_Calculation()
    Dim count As Integer
    Dim SubTot As Currency

    count = 0
    SubTot = 0

    Do While count < 10
        SubTot = SubTot + GetCurrency(IA148Sp.CYCarry(count))
        count = count + 1
    Loop
    
    If GetBool(IAF1040.CombMFS) = False Then
        ReturnVal = 0
    ElseIf GetCurrency(IA148Sp.TotNonRefCr) > 0 Or GetCurrency(IA148Sp.TotRefCr) > 0 Then
        ReturnVal = 1
    ElseIf SubTot > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PTEEIN_Calculation(Index As Integer)
    Dim PTE As Integer
    Dim RefPTE As Integer
    Dim Stuff As Integer
    Dim Stuff2 As Integer
   
    PTE = GetNumber(IA148BumpSp.TotPTE)
    RefPTE = GetNumber(IA148BumpSp.TotRefPTE)
    
    If Index = 5 And GetNumber(IA148Sp.TotPTE) > 6 Then
        ReturnVal = ""
    ElseIf PTE > Index Then
        Stuff2 = GetNumber(IA148BumpSp.PTEIndexNbr(Index))
        ReturnVal = GetString(IA148BumpSp.PTEEIN(Stuff2))
    ElseIf PTE + RefPTE > Index Then
        Stuff = (Index) - PTE
       Stuff2 = GetNumber(IA148BumpSp.RefPTEIndexNbr(Stuff))
        ReturnVal = GetString(IA148BumpSp.RefPTEEIN(Stuff2))
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub PTELine_Calculation(Index As Integer)
    Dim PTE As Integer
    Dim RefPTE As Integer
    Dim Stuff As Integer
    Dim Stuff2 As Integer
   
    PTE = GetNumber(IA148BumpSp.TotPTE)
    RefPTE = GetNumber(IA148BumpSp.TotRefPTE)
    
    If Index = 5 And GetNumber(IA148Sp.TotPTE) > 6 Then
        ReturnVal = ""
    ElseIf PTE > Index Then
        Stuff2 = GetNumber(IA148BumpSp.PTEIndexNbr(Index))
        ReturnVal = GetString(IA148BumpSp.PTELine(Stuff2))
    ElseIf PTE + RefPTE > Index Then
        Stuff = (Index) - PTE
        Stuff2 = GetNumber(IA148BumpSp.RefPTEIndexNbr(Stuff))
        ReturnVal = GetString(IA148BumpSp.RefPTELine(Stuff2))
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub PTEName_Calculation(Index As Integer)
    Dim PTE As Integer
    Dim RefPTE As Integer
    Dim Stuff As Integer
    Dim Stuff2 As Integer
   
    PTE = GetNumber(IA148BumpSp.TotPTE)
    RefPTE = GetNumber(IA148BumpSp.TotRefPTE)
    
    If Index = 5 And GetNumber(IA148Sp.TotPTE) > 6 Then
        ReturnVal = "See Statement Attached"
    ElseIf PTE > Index Then
        Stuff2 = GetNumber(IA148BumpSp.PTEIndexNbr(Index))
        ReturnVal = GetString(IA148BumpSp.PTEName(Stuff2))
    ElseIf PTE + RefPTE > Index Then
        Stuff = (Index) - PTE
        Stuff2 = GetNumber(IA148BumpSp.RefPTEIndexNbr(Stuff))
        ReturnVal = GetString(IA148BumpSp.RefPTEName(Stuff2))
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub PYCarry_Calculation(Index As Integer)
  Dim strindex As Long
  Dim copystr As String
  Dim Copy As Long
  
  strindex = ((Index) * 4) + 1
  copystr = Trim(Mid(GetString(IA148Sp.NonRefCopiesStr), strindex, 4))
  
  If Index = 9 And GetNumber(IA148Sp.NonRefNbr) > 10 Then
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

Private Sub RefCert_Calculation(Index As Integer)
  Dim strindex As Long
  Dim copystr As String
  Dim Copy As Long
  
  strindex = ((Index) * 4) + 1
  copystr = Trim(Mid(GetString(IA148Sp.RefCopiesStr), strindex, 4))
  
  If Index = 6 And GetNumber(IA148Sp.RefNbr) > 7 Then
    ReturnVal = "See Statement Attached"
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
  
  strindex = ((Index) * 4) + 1
  copystr = Trim(Mid(GetString(IA148Sp.RefCopiesStr), strindex, 4))
  
  If Index = 6 And GetNumber(IA148Sp.RefNbr) > 7 Then
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

Private Sub RefCopiesStr_Calculation()
    Dim Copy As Long
    Dim Copy2 As Long
    Dim Copy3 As Long
    Dim Copy4 As Long
    Dim Copy5 As Long
    Dim Copy6 As Long
    Dim Copy7 As Long
    Dim Copy8 As Long
    Dim Copy9 As Long
    Dim Copy10 As Long
    Dim Copy11 As Long
    Dim Copy12 As Long
    Dim Copy13 As Long
    Dim Copy14 As Long
    Dim max As Long
    Dim max2 As Long
    Dim max3 As Long
    Dim max5 As Long
    Dim max6 As Long
    Dim max9 As Long
    Dim max10 As Long
    Dim max11 As Long
    Dim max12 As Long
    Dim max13 As Long
    Dim max14 As Long
    Dim copystr As String
    Dim copystr2 As String
    Dim copystr3 As String
    Dim copystr4 As String
    Dim copystr5 As String
    Dim copystr6 As String
    Dim copystr7 As String
    Dim copystr8 As String
    Dim copystr9 As String
    Dim copystr10 As String
    Dim copystr11 As String
    Dim copystr12 As String
    Dim copystr13 As String
    Dim copystr14 As String
    Dim copiesstr As String
    Dim copiesstr2 As String
    Dim copiesstr3 As String
    Dim copiesstr4 As String
    Dim copiesstr5 As String
    Dim copiesstr6 As String
    Dim copiesstr7 As String
    Dim copiesstr8 As String
    Dim copiesstr9 As String
    Dim copiesstr10 As String
    Dim copiesstr11 As String
    Dim copiesstr12 As String
    Dim copiesstr13 As String
    Dim copiesstr14 As String
    
    copiesstr = ""
    Copy = 1
    max = GetAllCopies(IA8864)
    
    Do While Copy <= max
        If GetCurrency(IA8864.BiodieselCr, Copy) > 0 Then
            If GetCurrency(IA8864.BiodieselCr, Copy) > 0 And GetBool(IA8864.Spouse, Copy) = True Then
                copystr = CStr(Copy + 100)
                Do While Len(copystr) < 4
                    copystr = copystr + " "
                Loop
                copiesstr = copiesstr + copystr
            End If
        End If
     Copy = Copy + 1
    Loop
    
    copiesstr2 = ""
    Copy2 = 1
    max2 = GetAllCopies(IACred)
    
    Do While Copy2 <= max2
        If GetString(IACred.Code, Copy2) = "53" Then
            If GetBool(IACred.RefCr, Copy2) = True And GetBool(IACred.Spouse, Copy2) = True And GetString(IACred.Code, Copy2) = "53" Then
                copystr2 = CStr(Copy2 + 200) + " "
                copiesstr2 = copiesstr2 + copystr2
            End If
        End If
        Copy2 = Copy2 + 1
    Loop
    
    copiesstr3 = ""
    Copy3 = 1
    max3 = GetAllCopies(IA135)
    
    Do While Copy3 <= max3
        If GetCurrency(IA135.E85Credit, Copy3) > 0 Then
            If GetBool(IA135.Spouse, Copy3) = True And GetCurrency(IA135.E85Credit, Copy3) > 0 Then
                copystr3 = CStr(Copy3 + 300) + " "
                copiesstr3 = copiesstr3 + copystr3
            End If
            
        End If
        Copy3 = Copy3 + 1
    Loop
    
    copiesstr4 = ""
    Copy4 = 1
    
    Do While Copy4 <= max2
        If GetString(IACred.Code, Copy4) = "56" Then
            If GetBool(IACred.RefCr, Copy4) = True And GetBool(IACred.Spouse, Copy4) = True And GetString(IACred.Code, Copy4) = "56" Then
                copystr4 = CStr(Copy4 + 400) + " "
                copiesstr4 = copiesstr4 + copystr4
            End If
            
        End If
        Copy4 = Copy4 + 1
    Loop
    
    copiesstr5 = ""
    Copy5 = 1
    max5 = GetAllCopies(IA128)
    
    Do While Copy5 <= max5
        If GetCurrency(IA128.TotResearchCr, Copy5) > 0 Then
            If GetBool(IA128.Spouse, Copy5) = True And GetCurrency(IA128.TotResearchCr, Copy5) > 0 Then
                copystr5 = CStr(Copy5 + 500) + " "
                copiesstr5 = copiesstr5 + copystr5
            End If
            
        End If
        Copy5 = Copy5 + 1
    Loop
    
    copiesstr6 = ""
    Copy6 = 1
    max6 = GetAllCopies(IA128S)
    
    Do While Copy6 <= max6
        If GetCurrency(IA128S.TotResearchCr, Copy6) > 0 Then
            If GetBool(IA128S.Spouse, Copy6) = True And GetCurrency(IA128S.TotResearchCr, Copy6) > 0 Then
                copystr6 = CStr(Copy6 + 600) + " "
                copiesstr6 = copiesstr6 + copystr6
            End If
            
        End If
        Copy6 = Copy6 + 1
    Loop
    
    copiesstr7 = ""
    Copy7 = 1
            
    Do While Copy7 <= max5
        If GetCurrency(IA128.TotSuppResearchCr, Copy7) > 0 Then
            If GetBool(IA128.Spouse, Copy7) = True And GetCurrency(IA128.TotSuppResearchCr, Copy7) > 0 Then
                copystr7 = CStr(Copy7 + 700) + " "
                copiesstr7 = copiesstr7 + copystr7
            End If
            
        End If
        Copy7 = Copy7 + 1
    Loop
            
    copiesstr8 = ""
    Copy8 = 1
                    
    Do While Copy8 <= max6
        If GetCurrency(IA128S.TotSuppResearchCr, Copy8) > 0 Then
            If GetBool(IA128S.Spouse, Copy8) = True And GetCurrency(IA128S.TotSuppResearchCr, Copy8) > 0 Then
                copystr8 = CStr(Copy8 + 800) + " "
                copiesstr8 = copiesstr8 + copystr8
            End If
            
        End If
        Copy8 = Copy8 + 1
    Loop
    
    copiesstr9 = ""
    Copy9 = 1
    max9 = GetAllCopies(IA137)

    #If INDCALC Then
        Do While Copy9 <= max9
            If GetCurrency(IA137.EthPromoteCr, Copy9) > 0 Then
                If GetBool(IA137.Spouse, Copy9) = True And GetCurrency(IA137.EthPromoteCr, Copy9) > 0 Then
                    copystr9 = CStr(Copy9 + 900) + " "
                    copiesstr9 = copiesstr9 + copystr9
                End If
                
            End If
            Copy9 = Copy9 + 1
        Loop
    #Else
        Do While Copy9 <= max9
            If GetCurrency(IA137.EthPromoteCr, Copy9) > 0 Then
                If GetCurrency(IA137.EthPromoteCr, Copy9) > 0 Then
                    copystr9 = CStr(Copy9 + 900) + " "
                    copiesstr9 = copiesstr9 + copystr9
                End If
                
            End If
            Copy9 = Copy9 + 1
        Loop
    #End If
    
    copiesstr10 = ""
    Copy10 = 1
    max10 = GetAllCopies(IA138)
            
    Do While Copy10 <= max10
        If GetCurrency(IA138.E15Credit, Copy10) > 0 Then
            If GetBool(IA138.Spouse, Copy10) = True And GetCurrency(IA138.E15Credit, Copy10) > 0 Then
                copystr10 = CStr(Copy10 + 1000)
                copiesstr10 = copiesstr10 + copystr10
            End If
            
        End If
        Copy10 = Copy10 + 1
    Loop
            
    copiesstr11 = ""
    Copy11 = 1
    max11 = GetAllCopies(IA177)
    
    Do While Copy11 <= max11
        If GetCurrency(IA177.CYAdoptionTaxCr, Copy11) > 0 Then
            If GetBool(IA177.Spouse, Copy11) = True And GetCurrency(IA177.CYAdoptionTaxCr, Copy11) > 0 Then
                copystr11 = CStr(Copy11 + 1100)
                copiesstr11 = copiesstr11 + copystr11
            End If
            
        End If
        Copy11 = Copy11 + 1
    Loop
    
    copiesstr12 = ""
    Copy12 = 1
    max12 = GetAllCopies(IACred)
    
    Do While Copy12 <= max12
        If GetString(IACred.Code, Copy12) = "67" Then
            If GetBool(IACred.RefCr, Copy12) = True And GetBool(IACred.Spouse, Copy12) = True And GetString(IACred.Code, Copy12) = "67" Then
                copystr12 = CStr(Copy12 + 1200)
                copiesstr12 = copiesstr12 + copystr12
            End If
        End If
        Copy12 = Copy12 + 1
    Loop
            
    copiesstr13 = ""
    Copy13 = 1
    max13 = GetAllCopies(IACred)
    
    Do While Copy13 <= max13
        If GetString(IACred.Code, Copy13) = "68" Then
            If GetBool(IACred.RefCr, Copy13) = True And GetBool(IACred.Spouse, Copy13) = True And GetString(IACred.Code, Copy13) = "68" Then
                copystr13 = CStr(Copy13 + 1300)
                copiesstr13 = copiesstr13 + copystr13
            End If
        End If
        Copy13 = Copy13 + 1
    Loop
    
    copiesstr14 = ""
    Copy14 = 1
    max14 = GetAllCopies(IACred)
    
    Do While Copy14 <= max14
        If GetString(IACred.Code, Copy14) = "69" Then
            If GetBool(IACred.RefCr, Copy14) = True And GetBool(IACred.Spouse, Copy14) = True And GetString(IACred.Code, Copy14) = "69" Then
                copystr14 = CStr(Copy14 + 1400)
                copiesstr14 = copiesstr14 + copystr14
            End If
        End If
        Copy14 = Copy14 + 1
    Loop
                
            
    ReturnVal = copiesstr + copiesstr2 + copiesstr3 + copiesstr4 + copiesstr5 + copiesstr6 + copiesstr7 + copiesstr8 + copiesstr9 + copiesstr10 + copiesstr11 + copiesstr12 + copiesstr13 + copiesstr14

End Sub

Private Sub RefCr_Calculation(Index As Integer)
  Dim strindex As Long
  Dim copystr As String
  Dim Copy As Long
  
  strindex = ((Index) * 4) + 1
  copystr = Trim(Mid(GetString(IA148Sp.RefCopiesStr), strindex, 4))
  
  If Index = 6 And GetNumber(IA148Sp.RefNbr) > 7 Then
    ReturnVal = GetCurrency(IAWBP148RefSp.TotRefCr1) + GetCurrency(IAWBP148RefSp.TotRefCr2)
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

Private Sub RefNbr_Calculation()
    Dim count As Integer
    Dim Lim As Integer
    Dim Total As Integer
    
    Lim = GetAllCopies(IA8864)
    count = 1
    Total = 0
    
    Do While count <= Lim
        If GetBool(IA8864.Spouse, count) = True And GetCurrency(IA8864.BiodieselCr, count) > 0 Then
            Total = Total + 1
        Else
            Total = Total
        End If
        
        count = count + 1
    Loop
    
    Dim count2 As Integer
    Dim Lim2 As Integer
    Dim IACredit As String
    
    Lim2 = GetAllCopies(IACred)
    count2 = 1
    
    Do While count2 <= Lim2
    IACredit = GetString(IACred.Code, count2)
        If GetBool(IACred.RefCr, count2) = True And GetBool(IACred.Spouse, count2) = True And (IACredit = "53" Or IACredit = "56" Or IACredit = "67" Or IACredit = "68" Or IACredit = "69") Then
            Total = Total + 1
        Else
            Total = Total
        End If
        
        count2 = count2 + 1
    Loop
    
    Dim count3 As Integer
    Dim Lim3 As Integer
    
    Lim3 = GetAllCopies(IA135)
    count3 = 1
    
    Do While count3 <= Lim3
        If GetBool(IA135.Spouse, count3) = True And GetCurrency(IA135.E85Credit, count3) > 0 Then
            Total = Total + 1
        Else
            Total = Total
        End If
        
        count3 = count3 + 1
    Loop
    
    Dim count4 As Integer
    Dim Lim4 As Integer
    
    Lim4 = GetAllCopies(IA128)
    count4 = 1
    
    Do While count4 <= Lim4
        If GetBool(IA128.Spouse, count4) = True And GetCurrency(IA128.TotResearchCr, count4) > 0 Then
            Total = Total + 1
        Else
            Total = Total
        End If
        
        count4 = count4 + 1
    Loop
    
    Dim count5 As Integer
    Dim Lim5 As Integer
    
    Lim5 = GetAllCopies(IA128)
    count5 = 1
    
    Do While count5 <= Lim5
        If GetBool(IA128.Spouse, count5) = True And GetCurrency(IA128.TotSuppResearchCr, count5) > 0 Then
            Total = Total + 1
        Else
            Total = Total
        End If
        
        count5 = count5 + 1
    Loop
    
    Dim count6 As Integer
    Dim Lim6 As Integer
    
    Lim6 = GetAllCopies(IA128S)
    count6 = 1
    
    Do While count6 <= Lim6
        If GetBool(IA128S.Spouse, count6) = True And GetCurrency(IA128S.TotResearchCr, count6) > 0 Then
            Total = Total + 1
        Else
            Total = Total
        End If
        
        count6 = count6 + 1
    Loop
    
    Dim count7 As Integer
    Dim Lim7 As Integer
    
    Lim7 = GetAllCopies(IA128S)
    count7 = 1
    
    Do While count7 <= Lim7
        If GetBool(IA128S.Spouse, count7) = True And GetCurrency(IA128S.TotSuppResearchCr, count7) > 0 Then
            Total = Total + 1
        Else
            Total = Total
        End If
        
        count7 = count7 + 1
    Loop
    
    Dim count8 As Integer
    Dim Lim8 As Integer
    
    Lim8 = GetAllCopies(IA137)
    count8 = 1
    
    Do While count8 <= Lim8
        #If INDCALC Then
            If GetBool(IA137.Spouse, count8) = True And GetCurrency(IA137.EthPromoteCr, count8) > 0 Then
                Total = Total + 1
            Else
                Total = Total
            End If
        #Else
            If GetCurrency(IA137.EthPromoteCr, count8) > 0 Then
                Total = Total + 1
            Else
                Total = Total
            End If
        #End If
        
        count8 = count8 + 1
    Loop
    
    Dim count9 As Integer
    Dim Lim9 As Integer
    
    Lim9 = GetAllCopies(IA138)
    count9 = 1
    
    Do While count9 <= Lim9
        If GetBool(IA138.Spouse, count9) = True And GetCurrency(IA138.E15Credit, count9) > 0 Then
            Total = Total + 1
        Else
            Total = Total
        End If
        
        count9 = count9 + 1
    Loop
    
    Dim count10 As Integer
    Dim Lim10 As Integer
    
    Lim10 = GetAllCopies(IA177)
    count10 = 1
    
    Do While count10 <= Lim10
        If GetBool(IA177.Spouse, count10) = True And GetCurrency(IA177.CYAdoptionTaxCr, count10) > 0 Then
            Total = Total + 1
        Else
            Total = Total
        End If
        
        count10 = count10 + 1
    Loop
    
    ReturnVal = Total
End Sub

Private Sub RefTrig_Calculation(Index As Integer)
    If GetString(IA148Sp.RefCode(Index)) = "64" Or GetString(IA148Sp.RefCode(Index)) = "58" Or GetString(IA148Sp.RefCode(Index)) = "55" Or GetString(IA148Sp.RefCode(Index)) = "52" Or GetString(IA148Sp.RefCode(Index)) = "59" Or GetString(IA148Sp.RefCode(Index)) = "65" Or GetString(IA148Sp.RefCode(Index)) = "66" Then
        ReturnVal = 0
    ElseIf GetCurrency(IA148Sp.RefCr(Index)) > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SpouseSSN)
End Sub

Private Sub TotCode64_Calculation()
    Dim count As Integer
    Dim Lim As Integer
    Dim Total As Currency
    
    Lim = GetAllCopies(IA137)
    count = 1
    Total = 0
    
    Do While count <= Lim
        If GetBool(IA137.Spouse, count) = True Then
            Total = Total + GetCurrency(IA137.TotEthSoldCr, count)
        Else
            Total = Total
        End If
        
        count = count + 1
    Loop
        
    ReturnVal = Total
End Sub

Private Sub TotNonRefCr_Calculation()
    If GetBool(IAF1040.CombMFS) = False Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(IA148Sp.NonRefCr1) + GetCurrency(IA148Sp.NonRefCr2) + GetCurrency(IA148Sp.NonRefCr3) + GetCurrency(IA148Sp.NonRefCr4) + GetCurrency(IA148Sp.NonRefCr5) + GetCurrency(IA148Sp.NonRefCr6) + GetCurrency(IA148Sp.NonRefCr7) + GetCurrency(IA148Sp.NonRefCr8) + GetCurrency(IA148Sp.NonRefCr9) + GetCurrency(IA148Sp.NonRefCr10)
    End If
End Sub

Private Sub TotNonRefNo8801_Calculation()
    Dim count As Integer
    Dim Lim As Integer
    Dim WSTotal As Currency
    Dim Total As Currency
    
    Lim = GetAllCopies(IACred)
    count = 1
    WSTotal = 0
    
    Do While count <= Lim
        If GetBool(IACred.NonrefCr, count) = True And GetBool(IACred.Spouse, count) = True Then
            WSTotal = WSTotal + GetCurrency(IACred.CYCredit, count) + GetCurrency(IACred.PYCarry, count)
        Else
            WSTotal = WSTotal
        End If
        
        count = count + 1
    Loop
    
    Total = WSTotal + GetCurrency(IA134Sp.Credit) + GetCurrency(IA147.FranchiseCr, FieldCopies(IA147.Spouse))
        
    ReturnVal = Total
End Sub

Private Sub TotPTE_Calculation()
    ReturnVal = GetNumber(IA148BumpSp.TotPTE) + GetNumber(IA148BumpSp.TotRefPTE)
End Sub

Private Sub TotRefCr_Calculation()
    Dim count As Integer
    Dim SubTot As Currency

    count = 0
    SubTot = 0

    Do While count < 7
        SubTot = SubTot + GetCurrency(IA148Sp.RefCr(count))
        count = count + 1
    Loop
    
    If GetBool(IAF1040.CombMFS) = False Then
        ReturnVal = 0
    Else
        ReturnVal = SubTot
    End If
End Sub

Private Sub TPPerc_Calculation(Index As Integer)
    Dim PTE As Integer
    Dim RefPTE As Integer
    Dim Stuff As Integer
    Dim Stuff2 As Integer
   
    PTE = GetNumber(IA148BumpSp.TotPTE)
    RefPTE = GetNumber(IA148BumpSp.TotRefPTE)
    
    If Index = 5 And GetNumber(IA148Sp.TotPTE) > 6 Then
        ReturnVal = 0
    ElseIf PTE > Index Then
        Stuff2 = GetNumber(IA148BumpSp.PTEIndexNbr(Index))
        ReturnVal = GetFloat(IA148BumpSp.TPPerc(Stuff2))
    ElseIf PTE + RefPTE > Index Then
        Stuff = (Index) - PTE
        Stuff2 = GetNumber(IA148BumpSp.RefPTEIndexNbr(Stuff))
        ReturnVal = GetFloat(IA148BumpSp.RefTPPerc(Stuff2))
    Else
        ReturnVal = 0
    End If
End Sub

