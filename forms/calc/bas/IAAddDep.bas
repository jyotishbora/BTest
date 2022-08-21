Private Sub Description_Calculation()
    If GetNumber(USWAddDep.GrandTotDeps) = 1 Then
        ReturnVal = CStr(GetNumber(USWAddDep.GrandTotDeps)) & " Dependent"
    ElseIf GetNumber(USWAddDep.GrandTotDeps) > 1 Then
        ReturnVal = CStr(GetNumber(USWAddDep.GrandTotDeps)) & " Dependents"
    Else
        ReturnVal = "Dependents"
    End If
End Sub

Private Sub FDepAge_Calculation(Index As Integer)
    Dim max As Long
    Dim count As Long
    Dim Hits As Long
    
    max = GetAllCopies(USWDependents)
    Hits = 0
    count = 0
    
    Do While count < max
        count = count + 1
        If GetNumber(USWDependents.DepQual, count) = 1 Then
            If Hits = Index Then
                ReturnVal = GetNumber(USWDependents.DepAge, count)
            Else
                Hits = Hits + 1
            End If
        End If
    Loop
    
    
    ReturnVal = 0
End Sub

Private Sub FDepLast_Calculation(Index As Integer)
    Dim max As Long
    Dim count As Long
    Dim Hits As Long
    
    max = GetAllCopies(USWDependents)
    Hits = 0
    count = 0
    
    Do While count < max
        count = count + 1
        If GetNumber(USWDependents.DepQual, count) = 1 Then
            If Hits = Index Then
                ReturnVal = GetString(USWDependents.DepLast, count)
            Else
                Hits = Hits + 1
            End If
        End If
    Loop

    
    ReturnVal = ""
End Sub

Private Sub FDepName_Calculation(Index As Integer)
    Dim max As Long
    Dim count As Long
    Dim Hits As Long
    
    max = GetAllCopies(USWDependents)
    Hits = 0
    count = 0
    
    Do While count < max
        count = count + 1
        If GetNumber(USWDependents.DepQual, count) = 1 Then
            If Hits = Index Then
                ReturnVal = GetString(USWDependents.DepName, count)
            Else
                Hits = Hits + 1
            End If
        End If
    Loop

    
    ReturnVal = ""
End Sub

Private Sub FDepRel_Calculation(Index As Integer)
    Dim max As Long
    Dim count As Long
    Dim Hits As Long
    
    max = GetAllCopies(USWDependents)
    Hits = 0
    count = 0
    
    Do While count < max
        count = count + 1
        If GetNumber(USWDependents.DepQual, count) = 1 Then
            If Hits = Index Then
                ReturnVal = GetString(USWDependents.DepRel, count)
            Else
                Hits = Hits + 1
            End If
        End If
    Loop

    
    ReturnVal = ""
End Sub

Private Sub FDEPSSN_Calculation(Index As Integer)
    Dim max As Long
    Dim count As Long
    Dim Hits As Long
    
    max = GetAllCopies(USWDependents)
    Hits = 0
    count = 0
    
    Do While count < max
        count = count + 1
        If GetNumber(USWDependents.DepQual, count) = 1 Then
            If Hits = Index Then
                ReturnVal = GetString(USWDependents.DepSSN, count)
            Else
                Hits = Hits + 1
            End If
        End If
    Loop
    
    
    ReturnVal = ""
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.CombNames)
End Sub

Private Sub PrintMe_Calculation()
    If GetString(IAF1040.DepNames) = "See Attached" Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

