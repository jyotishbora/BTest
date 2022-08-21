Private Sub AbsL6ML7_Calculation()
    If GetCurrency(IA3903.L6ML7) < 0 Then
        ReturnVal = Abs(GetCurrency(IA3903.L6ML7))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub CodeP_Calculation()
    If GetBool(USF3903.StateNotFed, ParentCopy()) = True Then
        ReturnVal = GetCurrency(USF3903.CodeP, ParentCopy())
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Common_Calculation()
    ReturnVal = GetString(USWBasicInfo.TPCommon)
End Sub

Private Sub Description_Calculation()
    ReturnVal = "Moving Expenses " + CStr(GetCurrency(IA3903.MovExpDdn))
End Sub

Private Sub DNo_Calculation()
    If GetNumber(IA3903.NewLessOld) < 50 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub DYes_Calculation()
    If GetNumber(IA3903.NewLessOld) >= 50 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Exist_Calculation()
    ReturnVal = 1
End Sub

Private Sub ExReimb_Calculation()
    ReturnVal = GetCurrency(USF3903.ExReimb, ParentCopy())
End Sub

Private Sub Fed3903_Calculation()
    ReturnVal = "BEGIN HERE: Open federal Form 3903       Click on the folder to open the supporting document."
End Sub

Private Sub FedMilNo_Calculation()
    If GetBool(USF3903.EligibleY, ParentCopy()) = True Then
        ReturnVal = 0
    Else
        ReturnVal = 1
    End If
End Sub

Private Sub FedMilYes_Calculation()
    If GetBool(USF3903.EligibleY, ParentCopy()) = True Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub FirstName_Calculation()
    If GetBool(IA3903.Spouse) = True Then
        ReturnVal = GetString(IAF1040.SpouseFirst)
    Else
        ReturnVal = GetString(IAF1040.FirstName)
    End If
End Sub

Private Sub IAExReimb_Calculation()
'after testing not sure code P will have an excess for a non military move, also need to review how federal handles the .ExReimb
'as of 1/2/2019 fed is pulling code P all the time and taking to wages even if a non mil. move, IA instructions appear that could have reimb. from a 2017 move, not sure if should be on fed or if no IA wage adj would be needed, leave codeP def calc an online filable in case user needs to modify
'if determine not needed could also remove IARequired fields, but there is a new code/line on the IA1040 line 14 oth inc worksheet.
    ReturnVal = MaxValue(0, GetCurrency(IA3903.AbsL6ML7) - GetCurrency(IA3903.ExReimb))
End Sub

Private Sub Joint_Calculation()
    ReturnVal = GetBool(USF3903.Joint, ParentCopy())
End Sub

Private Sub JtCommon_Calculation()
    ReturnVal = GetString(USWBasicInfo.CombFirst)
End Sub

Private Sub L6ML7_Calculation()
    ReturnVal = GetCurrency(IA3903.TotalExp) - GetCurrency(IA3903.CodeP)
End Sub

Private Sub LastName_Calculation()
    If GetBool(IA3903.Spouse) = True Then
        ReturnVal = GetString(IAF1040.SpouseLast)
    Else
        ReturnVal = GetString(IAF1040.LastName)
    End If
End Sub

Private Sub MoveExp_Calculation()
    If GetBool(IA3903.FedMilYes) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(USF3903.MoveExp, ParentCopy())
    End If
End Sub

Private Sub MovExpDdn_Calculation()
    If GetBool(USF3903.StateNotFed, ParentCopy()) = True Then
        ReturnVal = MaxValue(0, GetCurrency(IA3903.L6ML7))
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub NewLessOld_Calculation()
    ReturnVal = MaxValue(0, GetNumber(IA3903.ToNewWork) - GetNumber(IA3903.ToOldWork))
End Sub

Private Sub PrintMe_Calculation()
    If GetCurrency(IA3903.MovExpDdn) <> 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Spouse_Calculation()
    ReturnVal = GetBool(USF3903.Spouse, ParentCopy())
End Sub

Private Sub SpouseCommon_Calculation()
    ReturnVal = GetString(USWBasicInfo.SPCommon)
End Sub

Private Sub SSN_Calculation()
    If GetBool(IA3903.Spouse) = True Then
        ReturnVal = GetString(IAF1040.SpouseSSN)
    Else
        ReturnVal = GetString(IAF1040.SSN)
    End If
End Sub

Private Sub Taxpayer_Calculation()
    ReturnVal = GetBool(USF3903.Taxpayer, ParentCopy())
End Sub

Private Sub ToNewWork_Calculation()
    If GetBool(IA3903.FedMilYes) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetNumber(USF3903.PrToNewWork, ParentCopy())
    End If
End Sub

Private Sub ToOldWork_Calculation()
    If GetBool(IA3903.FedMilYes) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetNumber(USF3903.PrToOldWork, ParentCopy())
    End If
End Sub

Private Sub TotalExp_Calculation()
    If GetBool(USF3903.StateNotFed, ParentCopy()) = True Then
        ReturnVal = GetCurrency(IA3903.MoveExp) + GetCurrency(IA3903.TravExp)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TotMoreThanPN_Calculation()
    If GetCurrency(IA3903.TotalExp) <= GetCurrency(IA3903.CodeP) Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TotMoreThanPY_Calculation()
    If GetCurrency(IA3903.TotalExp) > GetCurrency(IA3903.CodeP) Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TravExp_Calculation()
    If GetBool(IA3903.FedMilYes) = True Then
        ReturnVal = 0
    Else
        ReturnVal = GetCurrency(USF3903.TravExp, ParentCopy())
    End If
End Sub

