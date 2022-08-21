Private Sub PTECode_Calculation(Index As Integer)
  Dim strindex As Long
  Dim copystr As String
  Dim Copy As Long
  
  If GetNumber(IA148Sp.NonRefNbr) > 10 And Index > 9 Then
    strindex = ((Index - 1) * 4) + 1
  Else
    strindex = ((Index) * 4) + 1
  End If
  
  copystr = Trim(Mid(GetString(IA148Sp.NonRefCopiesStr), strindex, 4))
  
  If Index = 9 And GetNumber(IA148Sp.NonRefNbr) > 10 Then
    ReturnVal = "Stmt"
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

Private Sub PTEEIN_Calculation(Index As Integer)
  Dim strindex As Long
  Dim copystr As String
  Dim Copy As Long
  
  If GetNumber(IA148Sp.NonRefNbr) > 10 And Index > 9 Then
    strindex = ((Index - 1) * 4) + 1
  Else
    strindex = ((Index) * 4) + 1
  End If
  
  copystr = Trim(Mid(GetString(IA148Sp.NonRefCopiesStr), strindex, 4))
  
  If Index = 9 And GetNumber(IA148Sp.NonRefNbr) > 10 Then
    ReturnVal = ""
  ElseIf copystr <> "" Then
    Copy = CLng(copystr)
    If (Copy > 100) And (Copy <= 200) Then
      ReturnVal = ""
    ElseIf (Copy > 200) And (Copy <= 300) Then
      ReturnVal = GetString(IA134.SCorpEIN, (Copy) - 200)
    ElseIf (Copy > 300) And (Copy <= 400) Then
      ReturnVal = GetString(IACred.PTEEIN, (Copy) - 300)
    ElseIf (Copy > 400) And (Copy <= 500) Then
      ReturnVal = GetString(IACred.PTEEIN, (Copy) - 400)
    ElseIf (Copy > 500) And (Copy <= 600) Then
      ReturnVal = GetString(IACred.PTEEIN, (Copy) - 500)
    ElseIf (Copy > 600) And (Copy <= 700) Then
      ReturnVal = GetString(IACred.PTEEIN, (Copy) - 600)
    ElseIf (Copy > 700) And (Copy <= 800) Then
      ReturnVal = GetString(IACred.PTEEIN, (Copy) - 700)
    ElseIf (Copy > 800) And (Copy <= 900) Then
      ReturnVal = GetString(IACred.PTEEIN, (Copy) - 800)
    ElseIf (Copy > 900) And (Copy <= 1000) Then
      ReturnVal = GetString(IACred.PTEEIN, (Copy) - 900)
    ElseIf (Copy > 1000) And (Copy <= 1100) Then
      ReturnVal = GetString(IACred.PTEEIN, (Copy) - 1000)
    ElseIf (Copy > 1100) And (Copy <= 1200) Then
      ReturnVal = GetString(IACred.PTEEIN, (Copy) - 1100)
    ElseIf (Copy > 1200) And (Copy <= 1300) Then
      ReturnVal = GetString(IACred.PTEEIN, (Copy) - 1200)
    ElseIf (Copy > 1300) And (Copy <= 1400) Then
      ReturnVal = GetString(IACred.PTEEIN, (Copy) - 1300)
    ElseIf (Copy > 1400) And (Copy <= 1500) Then
      ReturnVal = GetString(IACred.PTEEIN, (Copy) - 1400)
    ElseIf (Copy > 1500) And (Copy <= 1600) Then
      ReturnVal = GetString(IACred.PTEEIN, (Copy) - 1500)
    ElseIf (Copy > 1600) And (Copy <= 1700) Then
      ReturnVal = GetString(IACred.PTEEIN, (Copy) - 1600)
    ElseIf (Copy > 1700) And (Copy <= 1800) Then
      ReturnVal = GetString(IACred.PTEEIN, (Copy) - 1700)
    ElseIf (Copy > 1800) And (Copy <= 1900) Then
      ReturnVal = GetString(IACred.PTEEIN, (Copy) - 1800)
    ElseIf (Copy > 1900) And (Copy <= 2000) Then
      ReturnVal = GetString(IACred.PTEEIN, (Copy) - 1900)
    ElseIf (Copy > 2000) And (Copy <= 2100) Then
      ReturnVal = GetString(IACred.PTEEIN, (Copy) - 2000)
    ElseIf (Copy > 2100) And (Copy <= 2200) Then
      ReturnVal = GetString(IACred.PTEEIN, (Copy) - 2100)
    ElseIf (Copy > 2200) And (Copy <= 2300) Then
      ReturnVal = GetString(IACred.PTEEIN, (Copy) - 2200)
    ElseIf (Copy > 2300) And (Copy <= 2400) Then
      ReturnVal = GetString(IACred.PTEEIN, (Copy) - 2300)
    ElseIf (Copy > 2400) And (Copy <= 2500) Then
      ReturnVal = ""
    End If
  End If
  ReturnVal = ""
End Sub

Private Sub PTEIndexNbr_Calculation(Index As Integer)
    Dim count As Long
    Dim max As Long
    Dim listedcount As Long
    
    listedcount = 0
    count = 0
    
    Do While count < 98
        If Trim(GetString(IA148BumpSp.PTEName(count))) <> "" Then
            If listedcount = Index Then
                ReturnVal = count
            Else
                listedcount = listedcount + 1
            End If
        End If
        count = count + 1
    Loop
        
    ReturnVal = 0
End Sub

Private Sub PTELine_Calculation(Index As Integer)
    Dim Hold As Long
    
    Hold = Index + 1
        
    If Index > 9 Then
        ReturnVal = "Attached stmt"
    Else
        ReturnVal = CStr(Hold)
    End If
End Sub

Private Sub PTEName_Calculation(Index As Integer)
  Dim strindex As Long
  Dim copystr As String
  Dim Copy As Long
  
  If GetNumber(IA148Sp.NonRefNbr) > 10 And Index > 9 Then
    strindex = ((Index - 1) * 4) + 1
  Else
    strindex = ((Index) * 4) + 1
  End If
  
  copystr = Trim(Mid(GetString(IA148Sp.NonRefCopiesStr), strindex, 4))
  
  If Index = 9 And GetNumber(IA148Sp.NonRefNbr) > 10 Then
    ReturnVal = ""
  ElseIf copystr <> "" Then
    Copy = CLng(copystr)
    If (Copy > 100) And (Copy <= 200) Then
      ReturnVal = ""
    ElseIf (Copy > 200) And (Copy <= 300) Then
      ReturnVal = GetString(IA134.SCorpName, (Copy) - 200)
    ElseIf (Copy > 300) And (Copy <= 400) Then
      ReturnVal = GetString(IACred.PTEEntity, (Copy) - 300)
    ElseIf (Copy > 400) And (Copy <= 500) Then
      ReturnVal = GetString(IACred.PTEEntity, (Copy) - 400)
    ElseIf (Copy > 500) And (Copy <= 600) Then
      ReturnVal = GetString(IACred.PTEEntity, (Copy) - 500)
    ElseIf (Copy > 600) And (Copy <= 700) Then
      ReturnVal = GetString(IACred.PTEEntity, (Copy) - 600)
    ElseIf (Copy > 700) And (Copy <= 800) Then
      ReturnVal = GetString(IACred.PTEEntity, (Copy) - 700)
    ElseIf (Copy > 800) And (Copy <= 900) Then
      ReturnVal = GetString(IACred.PTEEntity, (Copy) - 800)
    ElseIf (Copy > 900) And (Copy <= 1000) Then
      ReturnVal = GetString(IACred.PTEEntity, (Copy) - 900)
    ElseIf (Copy > 1000) And (Copy <= 1100) Then
      ReturnVal = GetString(IACred.PTEEntity, (Copy) - 1000)
    ElseIf (Copy > 1100) And (Copy <= 1200) Then
      ReturnVal = GetString(IACred.PTEEntity, (Copy) - 1100)
    ElseIf (Copy > 1200) And (Copy <= 1300) Then
      ReturnVal = GetString(IACred.PTEEntity, (Copy) - 1200)
    ElseIf (Copy > 1300) And (Copy <= 1400) Then
      ReturnVal = GetString(IACred.PTEEntity, (Copy) - 1300)
    ElseIf (Copy > 1400) And (Copy <= 1500) Then
      ReturnVal = GetString(IACred.PTEEntity, (Copy) - 1400)
    ElseIf (Copy > 1500) And (Copy <= 1600) Then
      ReturnVal = GetString(IACred.PTEEntity, (Copy) - 1500)
    ElseIf (Copy > 1600) And (Copy <= 1700) Then
      ReturnVal = GetString(IACred.PTEEntity, (Copy) - 1600)
    ElseIf (Copy > 1700) And (Copy <= 1800) Then
      ReturnVal = GetString(IACred.PTEEntity, (Copy) - 1700)
    ElseIf (Copy > 1800) And (Copy <= 1900) Then
      ReturnVal = GetString(IACred.PTEEntity, (Copy) - 1800)
    ElseIf (Copy > 1900) And (Copy <= 2000) Then
      ReturnVal = GetString(IACred.PTEEntity, (Copy) - 1900)
    ElseIf (Copy > 2000) And (Copy <= 2100) Then
      ReturnVal = GetString(IACred.PTEEntity, (Copy) - 2000)
    ElseIf (Copy > 2100) And (Copy <= 2200) Then
      ReturnVal = GetString(IACred.PTEEntity, (Copy) - 2100)
    ElseIf (Copy > 2200) And (Copy <= 2300) Then
      ReturnVal = GetString(IACred.PTEEntity, (Copy) - 2200)
    ElseIf (Copy > 2300) And (Copy <= 2400) Then
      ReturnVal = GetString(IACred.PTEEntity, (Copy) - 2300)
    ElseIf (Copy > 2400) And (Copy <= 2500) Then
      ReturnVal = ""
    End If
  End If
  ReturnVal = ""
End Sub

Private Sub PTENRTrig_Calculation(Index As Integer)
    If GetString(IA148BumpSp.PTECode(Index)) = "04" Or GetString(IA148BumpSp.PTECode(Index)) = "11" Or GetString(IA148BumpSp.PTECode(Index)) = "09" Then
        ReturnVal = 0
    ElseIf Trim(GetString(IA148BumpSp.PTEName(Index))) <> "" Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PTERefTrig_Calculation(Index As Integer)
    If GetString(IA148BumpSp.RefPTECode(Index)) = "64" Or GetString(IA148BumpSp.RefPTECode(Index)) = "58" Or GetString(IA148BumpSp.RefPTECode(Index)) = "55" Or GetString(IA148BumpSp.RefPTECode(Index)) = "52" Or GetString(IA148BumpSp.RefPTECode(Index)) = "59" Or GetString(IA148BumpSp.RefPTECode(Index)) = "65" Or GetString(IA148BumpSp.RefPTECode(Index)) = "66" Then
        ReturnVal = 0
    ElseIf Trim(GetString(IA148BumpSp.RefPTEName(Index))) <> "" Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub RefPTECode_Calculation(Index As Integer)
  Dim strindex As Long
  Dim copystr As String
  Dim Copy As Long
  
  If GetNumber(IA148Sp.NonRefNbr) > 10 And Index > 9 Then
    strindex = ((Index - 1) * 4) + 1
  Else
    strindex = ((Index) * 4) + 1
  End If
  copystr = Trim(Mid(GetString(IA148Sp.RefCopiesStr), strindex, 4))
  
  If Index = 6 And GetNumber(IA148Sp.RefNbr) > 7 Then
    ReturnVal = "See Statement Attached"
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

Private Sub RefPTEEIN_Calculation(Index As Integer)
  Dim strindex As Long
  Dim copystr As String
  Dim Copy As Long
  
  If GetNumber(IA148Sp.NonRefNbr) > 10 And Index > 9 Then
    strindex = ((Index - 1) * 4) + 1
  Else
    strindex = ((Index) * 4) + 1
  End If
  copystr = Trim(Mid(GetString(IA148Sp.RefCopiesStr), strindex, 4))
  
  If Index = 6 And GetNumber(IA148Sp.RefNbr) > 7 Then
    ReturnVal = ""
  ElseIf copystr <> "" Then
    Copy = CLng(copystr)
    If (Copy > 100) And (Copy <= 200) Then
      ReturnVal = GetString(IA8864.PTEEIN(0), (Copy) - 100)
    ElseIf (Copy > 200) And (Copy <= 300) Then
      ReturnVal = GetString(IACred.PTEEIN, (Copy) - 200)
    ElseIf (Copy > 300) And (Copy <= 400) Then
      ReturnVal = GetString(IA135.PTEEIN(0), (Copy) - 300)
    ElseIf (Copy > 400) And (Copy <= 500) Then
      ReturnVal = GetString(IACred.PTEEIN, (Copy) - 400)
    ElseIf (Copy > 500) And (Copy <= 600) Then
      ReturnVal = GetString(IA128.PTEEIN(0), (Copy) - 500)
    ElseIf (Copy > 600) And (Copy <= 700) Then
      ReturnVal = GetString(IA128S.PTEEIN(0), (Copy) - 600)
    ElseIf (Copy > 700) And (Copy <= 800) Then
      ReturnVal = GetString(IA128.PTEEIN(0), (Copy) - 700)
    ElseIf (Copy > 800) And (Copy <= 900) Then
      ReturnVal = GetString(IA128S.PTEEIN(0), (Copy) - 800)
    ElseIf (Copy > 900) And (Copy <= 1000) Then
      ReturnVal = GetString(IA137.PTEEIN(0), (Copy) - 900)
    ElseIf (Copy > 1000) And (Copy <= 1100) Then
      ReturnVal = GetString(IA138.PTEEIN(0), (Copy) - 1000)
    ElseIf (Copy > 1100) And (Copy <= 1200) Then
      ReturnVal = ""
    ElseIf (Copy > 1200) And (Copy <= 1300) Then
      ReturnVal = GetString(IACred.PTEEIN, (Copy) - 1200)
    ElseIf (Copy > 1300) And (Copy <= 1400) Then
      ReturnVal = GetString(IACred.PTEEIN, (Copy) - 1300)
    ElseIf (Copy > 1400) And (Copy <= 1500) Then
      ReturnVal = GetString(IACred.PTEEIN, (Copy) - 1400)
    End If
  End If
  ReturnVal = ""
End Sub

Private Sub RefPTEIndexNbr_Calculation(Index As Integer)
    Dim count As Long
    Dim max As Long
    Dim listedcount As Long
    
    listedcount = 0
    count = 0
    
    Do While count < 69
        If Trim(GetString(IA148BumpSp.RefPTEName(count))) <> "" Then
            If listedcount = Index Then
                ReturnVal = count
            Else
                listedcount = listedcount + 1
            End If
        End If
        count = count + 1
    Loop
        
    ReturnVal = 0
End Sub

Private Sub RefPTELine_Calculation(Index As Integer)
    Dim Hold As Long
    
    Hold = Index + 11
    
    If Index > 9 Then
        ReturnVal = "Attached stmt"
    Else
        ReturnVal = CStr(Hold)
    End If
End Sub

Private Sub RefPTEName_Calculation(Index As Integer)
  Dim strindex As Long
  Dim copystr As String
  Dim Copy As Long
  
  If GetNumber(IA148Sp.NonRefNbr) > 10 And Index > 9 Then
    strindex = ((Index - 1) * 4) + 1
  Else
    strindex = ((Index) * 4) + 1
  End If
  copystr = Trim(Mid(GetString(IA148Sp.RefCopiesStr), strindex, 4))
  
  If Index = 6 And GetNumber(IA148Sp.RefNbr) > 7 Then
    ReturnVal = ""
  ElseIf copystr <> "" Then
    Copy = CLng(copystr)
    If (Copy > 100) And (Copy <= 200) Then
      ReturnVal = GetString(IA8864.PTEEntity(0), (Copy) - 100)
    ElseIf (Copy > 200) And (Copy <= 300) Then
      ReturnVal = GetString(IACred.PTEEntity, (Copy) - 200)
    ElseIf (Copy > 300) And (Copy <= 400) Then
      ReturnVal = GetString(IA135.PTEEntity(0), (Copy) - 300)
    ElseIf (Copy > 400) And (Copy <= 500) Then
      ReturnVal = GetString(IACred.PTEEntity, (Copy) - 400)
    ElseIf (Copy > 500) And (Copy <= 600) Then
      ReturnVal = GetString(IA128.PTEEntity(0), (Copy) - 500)
    ElseIf (Copy > 600) And (Copy <= 700) Then
      ReturnVal = GetString(IA128S.PTEEntity(0), (Copy) - 600)
    ElseIf (Copy > 700) And (Copy <= 800) Then
      ReturnVal = GetString(IA128.PTEEntity(0), (Copy) - 700)
    ElseIf (Copy > 800) And (Copy <= 900) Then
      ReturnVal = GetString(IA128S.PTEEntity(0), (Copy) - 800)
    ElseIf (Copy > 900) And (Copy <= 1000) Then
      ReturnVal = GetString(IA137.PTEEntity(0), (Copy) - 900)
    ElseIf (Copy > 1000) And (Copy <= 1100) Then
      ReturnVal = GetString(IA138.PTEEntity(0), (Copy) - 1000)
    ElseIf (Copy > 1100) And (Copy <= 1200) Then
      ReturnVal = ""
    ElseIf (Copy > 1200) And (Copy <= 1300) Then
      ReturnVal = GetString(IACred.PTEEntity, (Copy) - 1200)
    ElseIf (Copy > 1300) And (Copy <= 1400) Then
      ReturnVal = GetString(IACred.PTEEntity, (Copy) - 1300)
    ElseIf (Copy > 1400) And (Copy <= 1500) Then
      ReturnVal = GetString(IACred.PTEEntity, (Copy) - 1400)
    End If
  End If
  ReturnVal = ""
End Sub

Private Sub RefTPPerc_Calculation(Index As Integer)
  Dim strindex As Long
  Dim copystr As String
  Dim Copy As Long
  
  If GetNumber(IA148Sp.NonRefNbr) > 10 And Index > 9 Then
    strindex = ((Index - 1) * 4) + 1
  Else
    strindex = ((Index) * 4) + 1
  End If
  copystr = Trim(Mid(GetString(IA148Sp.RefCopiesStr), strindex, 4))
  
  If Index = 6 And GetNumber(IA148Sp.RefNbr) > 7 Then
    ReturnVal = 0
  ElseIf copystr <> "" Then
    Copy = CLng(copystr)
    If (Copy > 100) And (Copy <= 200) Then
      ReturnVal = GetFloat(IA8864.TPPerc(0), (Copy) - 100)
    ElseIf (Copy > 200) And (Copy <= 300) Then
      ReturnVal = GetFloat(IACred.TPPerc, (Copy) - 200)
    ElseIf (Copy > 300) And (Copy <= 400) Then
      ReturnVal = GetFloat(IA135.TPPerc(0), (Copy) - 300)
    ElseIf (Copy > 400) And (Copy <= 500) Then
      ReturnVal = GetFloat(IACred.TPPerc, (Copy) - 400)
    ElseIf (Copy > 500) And (Copy <= 600) Then
      ReturnVal = GetFloat(IA128.TPPerc(0), (Copy) - 500)
    ElseIf (Copy > 600) And (Copy <= 700) Then
      ReturnVal = GetFloat(IA128S.TPPerc(0), (Copy) - 600)
    ElseIf (Copy > 700) And (Copy <= 800) Then
      ReturnVal = GetFloat(IA128.TPPerc(0), (Copy) - 700)
    ElseIf (Copy > 800) And (Copy <= 900) Then
      ReturnVal = GetFloat(IA128S.TPPerc(0), (Copy) - 800)
    ElseIf (Copy > 900) And (Copy <= 1000) Then
      ReturnVal = GetFloat(IA137.TPPerc(0), (Copy) - 900)
    ElseIf (Copy > 1000) And (Copy <= 1100) Then
      ReturnVal = GetFloat(IA138.TPPerc(0), (Copy) - 1000)
    ElseIf (Copy > 1100) And (Copy <= 1200) Then
      ReturnVal = 0
    ElseIf (Copy > 1200) And (Copy <= 1300) Then
      ReturnVal = GetFloat(IACred.TPPerc, (Copy) - 1200)
    ElseIf (Copy > 1300) And (Copy <= 1400) Then
      ReturnVal = GetFloat(IACred.TPPerc, (Copy) - 1300)
    ElseIf (Copy > 1400) And (Copy <= 1500) Then
      ReturnVal = GetFloat(IACred.TPPerc, (Copy) - 1400)
    End If
  End If
  ReturnVal = 0
End Sub

Private Sub TotPTE_Calculation()
    Dim count As Integer
    Dim Total As Integer

    count = 0
    Total = 0

    Do While count < 98
        If Trim(GetString(IA148BumpSp.PTEName(count))) <> "" Then
            Total = Total + 1
        Else
            Total = Total
        End If
        count = count + 1
    Loop
    
    ReturnVal = Total
End Sub

Private Sub TotRefPTE_Calculation()
    Dim count As Integer
    Dim Total As Integer

    count = 0
    Total = 0

    Do While count < 69
        If Trim(GetString(IA148BumpSp.RefPTEName(count))) <> "" Then
            Total = Total + 1
        Else
            Total = Total
        End If
        count = count + 1
    Loop
    
    ReturnVal = Total
End Sub

Private Sub TPPerc_Calculation(Index As Integer)
  Dim strindex As Long
  Dim copystr As String
  Dim Copy As Long
  
  If GetNumber(IA148Sp.NonRefNbr) > 10 And Index > 9 Then
    strindex = ((Index - 1) * 4) + 1
  Else
    strindex = ((Index) * 4) + 1
  End If
  
  copystr = Trim(Mid(GetString(IA148Sp.NonRefCopiesStr), strindex, 4))
  
  If Index = 9 And GetNumber(IA148Sp.NonRefNbr) > 10 Then
    ReturnVal = 0
  ElseIf copystr <> "" Then
    Copy = CLng(copystr)
    If (Copy > 100) And (Copy <= 200) Then
      ReturnVal = 0
    ElseIf (Copy > 200) And (Copy <= 300) Then
      ReturnVal = GetFloat(IA134.SCorpPerc, (Copy) - 200)
    ElseIf (Copy > 300) And (Copy <= 400) Then
      ReturnVal = GetFloat(IACred.TPPerc, (Copy) - 300)
    ElseIf (Copy > 400) And (Copy <= 500) Then
      ReturnVal = GetFloat(IACred.TPPerc, (Copy) - 400)
    ElseIf (Copy > 500) And (Copy <= 600) Then
      ReturnVal = GetFloat(IACred.TPPerc, (Copy) - 500)
    ElseIf (Copy > 600) And (Copy <= 700) Then
      ReturnVal = GetFloat(IACred.TPPerc, (Copy) - 600)
    ElseIf (Copy > 700) And (Copy <= 800) Then
      ReturnVal = GetFloat(IACred.TPPerc, (Copy) - 700)
    ElseIf (Copy > 800) And (Copy <= 900) Then
      ReturnVal = GetFloat(IACred.TPPerc, (Copy) - 800)
    ElseIf (Copy > 900) And (Copy <= 1000) Then
      ReturnVal = GetFloat(IACred.TPPerc, (Copy) - 900)
    ElseIf (Copy > 1000) And (Copy <= 1100) Then
      ReturnVal = GetFloat(IACred.TPPerc, (Copy) - 1000)
    ElseIf (Copy > 1100) And (Copy <= 1200) Then
      ReturnVal = GetFloat(IACred.TPPerc, (Copy) - 1100)
    ElseIf (Copy > 1200) And (Copy <= 1300) Then
      ReturnVal = GetFloat(IACred.TPPerc, (Copy) - 1200)
    ElseIf (Copy > 1300) And (Copy <= 1400) Then
      ReturnVal = GetFloat(IACred.TPPerc, (Copy) - 1300)
    ElseIf (Copy > 1400) And (Copy <= 1500) Then
      ReturnVal = GetFloat(IACred.TPPerc, (Copy) - 1400)
    ElseIf (Copy > 1500) And (Copy <= 1600) Then
      ReturnVal = GetFloat(IACred.TPPerc, (Copy) - 1500)
    ElseIf (Copy > 1600) And (Copy <= 1700) Then
      ReturnVal = GetFloat(IACred.TPPerc, (Copy) - 1600)
    ElseIf (Copy > 1700) And (Copy <= 1800) Then
      ReturnVal = GetFloat(IACred.TPPerc, (Copy) - 1700)
    ElseIf (Copy > 1800) And (Copy <= 1900) Then
      ReturnVal = GetFloat(IACred.TPPerc, (Copy) - 1800)
    ElseIf (Copy > 1900) And (Copy <= 2000) Then
      ReturnVal = GetFloat(IACred.TPPerc, (Copy) - 1900)
    ElseIf (Copy > 2000) And (Copy <= 2100) Then
      ReturnVal = GetFloat(IACred.TPPerc, (Copy) - 2000)
    ElseIf (Copy > 2100) And (Copy <= 2200) Then
      ReturnVal = GetFloat(IACred.TPPerc, (Copy) - 2100)
    ElseIf (Copy > 2200) And (Copy <= 2300) Then
      ReturnVal = GetFloat(IACred.TPPerc, (Copy) - 2200)
    ElseIf (Copy > 2300) And (Copy <= 2400) Then
      ReturnVal = GetFloat(IACred.TPPerc, (Copy) - 2300)
    ElseIf (Copy > 2400) And (Copy <= 2500) Then
      ReturnVal = 0
    End If
  End If
  ReturnVal = 0
End Sub

