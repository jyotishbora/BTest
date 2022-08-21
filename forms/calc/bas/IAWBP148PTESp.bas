Private Sub Desc_Calculation()
    ReturnVal = "Additonal Entities"
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IA148Sp.Names)
End Sub

Private Sub Offset_Calculation()
    If GetCopy() = 1 Then
        ReturnVal = 5
    ElseIf GetCopy() = 2 Then
        ReturnVal = 35
    ElseIf GetCopy() = 3 Then
        ReturnVal = 65
    ElseIf GetCopy() = 4 Then
        ReturnVal = 95
    Else
        ReturnVal = 125
    End If
End Sub

Private Sub Print_Calculation()
    If GetBool(IA148Sp.Print) = False Then
        ReturnVal = 0
    ElseIf Trim(GetString(IAWBP148PTESp.PTEName(0))) <> "" Or Trim(GetString(IAWBP148PTESp.PTEEIN(0))) <> "" Then
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
    Dim MoStuff As Integer
   
    PTE = GetNumber(IA148BumpSp.TotPTE)
    RefPTE = GetNumber(IA148BumpSp.TotRefPTE)
    
    MoStuff = Index + GetNumber(IAWBP148PTESp.Offset)
    
    If GetNumber(IA148Sp.TotPTE) = 6 Then
        ReturnVal = ""
    ElseIf PTE > MoStuff Then
        Stuff2 = GetNumber(IA148BumpSp.PTEIndexNbr(MoStuff))
        ReturnVal = GetString(IA148BumpSp.PTEEIN(Stuff2))
    ElseIf PTE + RefPTE > MoStuff Then
        Stuff = (MoStuff) - PTE
        Stuff2 = GetNumber(IA148BumpSp.RefPTEIndexNbr(Stuff))
        ReturnVal = GetString(IA148BumpSp.RefPTEEIN(Stuff2))
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub PTEName_Calculation(Index As Integer)
    Dim PTE As Integer
    Dim RefPTE As Integer
    Dim Stuff As Integer
    Dim Stuff2 As Integer
    Dim MoStuff As Integer
   
    PTE = GetNumber(IA148BumpSp.TotPTE)
    RefPTE = GetNumber(IA148BumpSp.TotRefPTE)
    
    MoStuff = Index + GetNumber(IAWBP148PTESp.Offset)
    
    If GetNumber(IA148Sp.TotPTE) = 6 Then
        ReturnVal = ""
    ElseIf PTE > MoStuff Then
        Stuff2 = GetNumber(IA148BumpSp.PTEIndexNbr(MoStuff))
        ReturnVal = GetString(IA148BumpSp.PTEName(Stuff2))
    ElseIf PTE + RefPTE > MoStuff Then
        Stuff = (MoStuff) - PTE
        Stuff2 = GetNumber(IA148BumpSp.RefPTEIndexNbr(Stuff))
        ReturnVal = GetString(IA148BumpSp.RefPTEName(Stuff2))
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IA148Sp.SSN)
End Sub

Private Sub TPPerc_Calculation(Index As Integer)
    Dim PTE As Integer
    Dim RefPTE As Integer
    Dim Stuff As Integer
    Dim Stuff2 As Integer
    Dim MoStuff As Integer
   
    PTE = GetNumber(IA148BumpSp.TotPTE)
    RefPTE = GetNumber(IA148BumpSp.TotRefPTE)
    
    MoStuff = Index + GetNumber(IAWBP148PTESp.Offset)
    
    If GetNumber(IA148Sp.TotPTE) = 6 Then
        ReturnVal = 0
    ElseIf PTE > MoStuff Then
        Stuff2 = GetNumber(IA148BumpSp.PTEIndexNbr(MoStuff))
        ReturnVal = GetFloat(IA148BumpSp.TPPerc(Stuff2))
    ElseIf PTE + RefPTE > MoStuff Then
        Stuff = (MoStuff) - PTE
        Stuff2 = GetNumber(IA148BumpSp.RefPTEIndexNbr(Stuff))
        ReturnVal = GetFloat(IA148BumpSp.RefTPPerc(Stuff2))
    Else
        ReturnVal = 0
    End If
End Sub

