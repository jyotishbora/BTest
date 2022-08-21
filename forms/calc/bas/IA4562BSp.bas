Private Sub Balance1_Calculation()
    ReturnVal = GetCurrency(IA4562BSp.AdjAmt(0))
End Sub

Private Sub Balance10_Calculation()
    If GetCurrency(IA4562BSp.Balance9) <> 0 Then
        ReturnVal = GetCurrency(IA4562BSp.Balance9) + GetCurrency(IA4562BSp.AdjAmt(9))
    Else
        ReturnVal = GetCurrency(IA4562BSp.AdjAmt(9))
    End If
End Sub

Private Sub Balance11_Calculation()
    If GetCurrency(IA4562BSp.Balance10) <> 0 Then
        ReturnVal = GetCurrency(IA4562BSp.Balance10) + GetCurrency(IA4562BSp.AdjAmt(10))
    Else
        ReturnVal = GetCurrency(IA4562BSp.AdjAmt(10))
    End If
End Sub

Private Sub Balance12_Calculation()
    If GetCurrency(IA4562BSp.Balance11) <> 0 Then
        ReturnVal = GetCurrency(IA4562BSp.Balance11) + GetCurrency(IA4562BSp.AdjAmt(11))
    Else
        ReturnVal = GetCurrency(IA4562BSp.AdjAmt(11))
    End If
End Sub

Private Sub Balance13_Calculation()
    If GetCurrency(IA4562BSp.Balance12) <> 0 Then
        ReturnVal = GetCurrency(IA4562BSp.Balance12) + GetCurrency(IA4562BSp.AdjAmt(12))
    Else
        ReturnVal = GetCurrency(IA4562BSp.AdjAmt(12))
    End If
End Sub

Private Sub Balance2_Calculation()
    If GetCurrency(IA4562BSp.Balance1) <> 0 Then
        ReturnVal = GetCurrency(IA4562BSp.Balance1) + GetCurrency(IA4562BSp.AdjAmt(1))
    Else
        ReturnVal = GetCurrency(IA4562BSp.AdjAmt(1))
    End If
End Sub

Private Sub Balance3_Calculation()
    If GetCurrency(IA4562BSp.Balance2) <> 0 Then
        ReturnVal = GetCurrency(IA4562BSp.Balance2) + GetCurrency(IA4562BSp.AdjAmt(2))
    Else
        ReturnVal = GetCurrency(IA4562BSp.AdjAmt(2))
    End If
End Sub

Private Sub Balance4_Calculation()
    If GetCurrency(IA4562BSp.Balance3) <> 0 Then
        ReturnVal = GetCurrency(IA4562BSp.Balance3) + GetCurrency(IA4562BSp.AdjAmt(3))
    Else
        ReturnVal = GetCurrency(IA4562BSp.AdjAmt(3))
    End If
End Sub

Private Sub Balance5_Calculation()
    If GetCurrency(IA4562BSp.Balance4) <> 0 Then
        ReturnVal = GetCurrency(IA4562BSp.Balance4) + GetCurrency(IA4562BSp.AdjAmt(4))
    Else
        ReturnVal = GetCurrency(IA4562BSp.AdjAmt(4))
    End If
End Sub

Private Sub Balance6_Calculation()
    If GetCurrency(IA4562BSp.Balance5) <> 0 Then
        ReturnVal = GetCurrency(IA4562BSp.Balance5) + GetCurrency(IA4562BSp.AdjAmt(5))
    Else
        ReturnVal = GetCurrency(IA4562BSp.AdjAmt(5))
    End If
End Sub

Private Sub Balance7_Calculation()
    If GetCurrency(IA4562BSp.Balance6) <> 0 Then
        ReturnVal = GetCurrency(IA4562BSp.Balance6) + GetCurrency(IA4562BSp.AdjAmt(6))
    Else
        ReturnVal = GetCurrency(IA4562BSp.AdjAmt(6))
    End If
End Sub

Private Sub Balance8_Calculation()
    If GetCurrency(IA4562BSp.Balance7) <> 0 Then
        ReturnVal = GetCurrency(IA4562BSp.Balance7) + GetCurrency(IA4562BSp.AdjAmt(7))
    Else
        ReturnVal = GetCurrency(IA4562BSp.AdjAmt(7))
    End If
End Sub

Private Sub Balance9_Calculation()
    If GetCurrency(IA4562BSp.Balance8) <> 0 Then
        ReturnVal = GetCurrency(IA4562BSp.Balance8) + GetCurrency(IA4562BSp.AdjAmt(8))
    Else
        ReturnVal = GetCurrency(IA4562BSp.AdjAmt(8))
    End If
End Sub

Private Sub Balance14_Calculation()
    If GetCurrency(IA4562BSp.Balance13) <> 0 Then
        ReturnVal = GetCurrency(IA4562BSp.Balance13) + GetCurrency(IA4562BSp.AdjAmt(13))
    Else
        ReturnVal = GetCurrency(IA4562BSp.AdjAmt(13))
    End If
End Sub

Private Sub Balance15_Calculation()
    If GetCurrency(IA4562BSp.Balance14) <> 0 Then
        ReturnVal = GetCurrency(IA4562BSp.Balance14) + GetCurrency(IA4562BSp.AdjAmt(14))
    Else
        ReturnVal = GetCurrency(IA4562BSp.AdjAmt(14))
    End If
End Sub

Private Sub Balance16_Calculation()
    If GetCurrency(IA4562BSp.Balance15) <> 0 Then
        ReturnVal = GetCurrency(IA4562BSp.Balance15) + GetCurrency(IA4562BSp.AdjAmt(15))
    Else
        ReturnVal = GetCurrency(IA4562BSp.AdjAmt(15))
    End If
End Sub

Private Sub Balance17_Calculation()
    If GetCurrency(IA4562BSp.Balance16) <> 0 Then
        ReturnVal = GetCurrency(IA4562BSp.Balance16) + GetCurrency(IA4562BSp.CYAdjAmt)
    Else
        ReturnVal = GetCurrency(IA4562BSp.CYAdjAmt)
    End If
End Sub

Private Sub CYAdjAmt_Calculation()
    If GetBool(IAF1040.CombMFS) = True Then
        ReturnVal = GetCurrency(IAWOthInc.SPBonus)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Description_Calculation()
    ReturnVal = CStr(GetCurrency(IA4562BSp.Balance17)) & " Balance"
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IA4562Sp.Names)
End Sub

Private Sub PeriodEnd_Calculation(Index As Integer)
    If Index = 0 Then
        ReturnVal = #12/31/2002#
    ElseIf Index = 1 Then
        ReturnVal = #12/31/2003#
    ElseIf Index = 2 Then
        ReturnVal = #12/31/2004#
    ElseIf Index = 3 Then
        ReturnVal = #12/31/2005#
    ElseIf Index = 4 Then
        ReturnVal = #12/31/2006#
    ElseIf Index = 5 Then
        ReturnVal = #12/31/2007#
    ElseIf Index = 6 Then
        ReturnVal = #12/31/2008#
    ElseIf Index = 7 Then
        ReturnVal = #12/31/2009#
    ElseIf Index = 8 Then
        ReturnVal = #12/31/2010#
    ElseIf Index = 9 Then
        ReturnVal = #12/31/2011#
    ElseIf Index = 10 Then
        ReturnVal = #12/31/2012#
    ElseIf Index = 11 Then
        ReturnVal = #12/31/2013#
    ElseIf Index = 12 Then
        ReturnVal = #12/31/2014#
    ElseIf Index = 13 Then
        ReturnVal = #12/31/2015#
    ElseIf Index = 14 Then
        ReturnVal = #12/31/2016#
    ElseIf Index = 15 Then
        ReturnVal = #12/31/2017#
    Else
        ReturnVal = #12/31/2018#
    End If
End Sub

Private Sub PrAdjAmt_Calculation(Index As Integer)
    Dim count As Integer
    Dim Hold As Currency
    count = 0
    Hold = 0
    
    If GetCurrency(IA4562BSp.AdjAmt(0)) <> 0 Or GetCurrency(IA4562BSp.Balance1) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IA4562BSp.AdjAmt(0))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(1)) <> 0 Or GetCurrency(IA4562BSp.Balance2) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IA4562BSp.AdjAmt(1))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(2)) <> 0 Or GetCurrency(IA4562BSp.Balance3) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IA4562BSp.AdjAmt(2))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(3)) <> 0 Or GetCurrency(IA4562BSp.Balance4) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IA4562BSp.AdjAmt(3))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(4)) <> 0 Or GetCurrency(IA4562BSp.Balance5) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IA4562BSp.AdjAmt(4))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(5)) <> 0 Or GetCurrency(IA4562BSp.Balance6) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IA4562BSp.AdjAmt(5))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(6)) <> 0 Or GetCurrency(IA4562BSp.Balance7) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IA4562BSp.AdjAmt(6))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(7)) <> 0 Or GetCurrency(IA4562BSp.Balance8) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IA4562BSp.AdjAmt(7))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(8)) <> 0 Or GetCurrency(IA4562BSp.Balance9) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IA4562BSp.AdjAmt(8))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(9)) <> 0 Or GetCurrency(IA4562BSp.Balance10) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IA4562BSp.AdjAmt(9))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(10)) <> 0 Or GetCurrency(IA4562BSp.Balance11) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IA4562BSp.AdjAmt(10))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(11)) <> 0 Or GetCurrency(IA4562BSp.Balance12) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IA4562BSp.AdjAmt(11))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(12)) <> 0 Or GetCurrency(IA4562BSp.Balance13) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IA4562BSp.AdjAmt(12))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(13)) <> 0 Or GetCurrency(IA4562BSp.Balance14) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IA4562BSp.AdjAmt(13))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(14)) <> 0 Or GetCurrency(IA4562BSp.Balance15) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IA4562BSp.AdjAmt(14))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(15)) <> 0 Or GetCurrency(IA4562BSp.Balance16) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IA4562BSp.AdjAmt(15))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.CYAdjAmt) <> 0 Or GetCurrency(IA4562BSp.Balance17) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IA4562BSp.CYAdjAmt)
           count = 99
        Else
           count = count + 1
        End If
    End If
    ReturnVal = Hold
End Sub

Private Sub PrAsterik_Calculation(Index As Integer)
    If GetBool(IA4562BSp.PrChangeY(Index)) = True Then
        ReturnVal = "*"
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub PrBalance_Calculation(Index As Integer)
    Dim count As Integer
    Dim Hold As Currency
    count = 0
    Hold = 0
    
    If GetCurrency(IA4562BSp.AdjAmt(0)) <> 0 Or GetCurrency(IA4562BSp.Balance1) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IA4562BSp.Balance1)
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(1)) <> 0 Or GetCurrency(IA4562BSp.Balance2) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IA4562BSp.Balance2)
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(2)) <> 0 Or GetCurrency(IA4562BSp.Balance3) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IA4562BSp.Balance3)
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(3)) <> 0 Or GetCurrency(IA4562BSp.Balance4) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IA4562BSp.Balance4)
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(4)) <> 0 Or GetCurrency(IA4562BSp.Balance5) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IA4562BSp.Balance5)
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(5)) <> 0 Or GetCurrency(IA4562BSp.Balance6) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IA4562BSp.Balance6)
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(6)) <> 0 Or GetCurrency(IA4562BSp.Balance7) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IA4562BSp.Balance7)
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(7)) <> 0 Or GetCurrency(IA4562BSp.Balance8) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IA4562BSp.Balance8)
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(8)) <> 0 Or GetCurrency(IA4562BSp.Balance9) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IA4562BSp.Balance9)
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(9)) <> 0 Or GetCurrency(IA4562BSp.Balance10) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IA4562BSp.Balance10)
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(10)) <> 0 Or GetCurrency(IA4562BSp.Balance11) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IA4562BSp.Balance11)
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(11)) <> 0 Or GetCurrency(IA4562BSp.Balance12) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IA4562BSp.Balance12)
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(12)) <> 0 Or GetCurrency(IA4562BSp.Balance13) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IA4562BSp.Balance13)
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(13)) <> 0 Or GetCurrency(IA4562BSp.Balance14) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IA4562BSp.Balance14)
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(14)) <> 0 Or GetCurrency(IA4562BSp.Balance15) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IA4562BSp.Balance15)
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(15)) <> 0 Or GetCurrency(IA4562BSp.Balance16) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IA4562BSp.Balance16)
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.CYAdjAmt) <> 0 Or GetCurrency(IA4562BSp.Balance17) <> 0 Then
        If Index = count Then
           Hold = GetCurrency(IA4562BSp.Balance17)
           count = 99
        Else
           count = count + 1
        End If
    End If
    ReturnVal = Hold
End Sub

Private Sub PrChangeY_Calculation(Index As Integer)
    Dim count As Integer
    Dim Hold As Boolean
    count = 0
    Hold = 0
    
    If GetCurrency(IA4562BSp.AdjAmt(0)) <> 0 Or GetCurrency(IA4562BSp.Balance1) <> 0 Then
        If Index = count Then
           Hold = GetBool(IA4562BSp.ChangeY(0))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(1)) <> 0 Or GetCurrency(IA4562BSp.Balance2) <> 0 Then
        If Index = count Then
           Hold = GetBool(IA4562BSp.ChangeY(1))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(2)) <> 0 Or GetCurrency(IA4562BSp.Balance3) <> 0 Then
        If Index = count Then
           Hold = GetBool(IA4562BSp.ChangeY(2))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(3)) <> 0 Or GetCurrency(IA4562BSp.Balance4) <> 0 Then
        If Index = count Then
           Hold = GetBool(IA4562BSp.ChangeY(3))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(4)) <> 0 Or GetCurrency(IA4562BSp.Balance5) <> 0 Then
        If Index = count Then
           Hold = GetBool(IA4562BSp.ChangeY(4))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(5)) <> 0 Or GetCurrency(IA4562BSp.Balance6) <> 0 Then
        If Index = count Then
           Hold = GetBool(IA4562BSp.ChangeY(5))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(6)) <> 0 Or GetCurrency(IA4562BSp.Balance7) <> 0 Then
        If Index = count Then
           Hold = GetBool(IA4562BSp.ChangeY(6))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(7)) <> 0 Or GetCurrency(IA4562BSp.Balance8) <> 0 Then
        If Index = count Then
           Hold = GetBool(IA4562BSp.ChangeY(7))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(8)) <> 0 Or GetCurrency(IA4562BSp.Balance9) <> 0 Then
        If Index = count Then
           Hold = GetBool(IA4562BSp.ChangeY(8))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(9)) <> 0 Or GetCurrency(IA4562BSp.Balance10) <> 0 Then
        If Index = count Then
           Hold = GetBool(IA4562BSp.ChangeY(9))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(10)) <> 0 Or GetCurrency(IA4562BSp.Balance11) <> 0 Then
        If Index = count Then
           Hold = GetBool(IA4562BSp.ChangeY(10))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(11)) <> 0 Or GetCurrency(IA4562BSp.Balance12) <> 0 Then
        If Index = count Then
           Hold = GetBool(IA4562BSp.ChangeY(11))
           count = 99
        Else
           count = count + 1
        End If
    End If
      
    If GetCurrency(IA4562BSp.AdjAmt(12)) <> 0 Or GetCurrency(IA4562BSp.Balance13) <> 0 Then
        If Index = count Then
           Hold = GetBool(IA4562BSp.ChangeY(12))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(13)) <> 0 Or GetCurrency(IA4562BSp.Balance14) <> 0 Then
        If Index = count Then
           Hold = GetBool(IA4562BSp.ChangeY(13))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(14)) <> 0 Or GetCurrency(IA4562BSp.Balance15) <> 0 Then
        If Index = count Then
           Hold = GetBool(IA4562BSp.ChangeY(14))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(15)) <> 0 Or GetCurrency(IA4562BSp.Balance16) <> 0 Then
        If Index = count Then
           Hold = GetBool(IA4562BSp.ChangeY(15))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.CYAdjAmt) <> 0 Or GetCurrency(IA4562BSp.Balance17) <> 0 Then
        If Index = count Then
           Hold = GetBool(IA4562BSp.ChangeY(16))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    ReturnVal = Hold
End Sub

Private Sub Print_Calculation()
    If GetCurrency(IA4562BSp.PrBalance(0)) <> 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub PrPeriodEnd_Calculation(Index As Integer)
    Dim count As Integer
    Dim Hold As String
    count = 0
    Hold = ""
    
    If GetCurrency(IA4562BSp.AdjAmt(0)) <> 0 Or GetCurrency(IA4562BSp.Balance1) <> 0 Then
        If Index = count Then
           Hold = GetString(IA4562BSp.PeriodEnd(0))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(1)) <> 0 Or GetCurrency(IA4562BSp.Balance2) <> 0 Then
        If Index = count Then
           Hold = GetString(IA4562BSp.PeriodEnd(1))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(2)) <> 0 Or GetCurrency(IA4562BSp.Balance3) <> 0 Then
        If Index = count Then
           Hold = GetString(IA4562BSp.PeriodEnd(2))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(3)) <> 0 Or GetCurrency(IA4562BSp.Balance4) <> 0 Then
        If Index = count Then
           Hold = GetString(IA4562BSp.PeriodEnd(3))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(4)) <> 0 Or GetCurrency(IA4562BSp.Balance5) <> 0 Then
        If Index = count Then
           Hold = GetString(IA4562BSp.PeriodEnd(4))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(5)) <> 0 Or GetCurrency(IA4562BSp.Balance6) <> 0 Then
        If Index = count Then
           Hold = GetString(IA4562BSp.PeriodEnd(5))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(6)) <> 0 Or GetCurrency(IA4562BSp.Balance7) <> 0 Then
        If Index = count Then
           Hold = GetString(IA4562BSp.PeriodEnd(6))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(7)) <> 0 Or GetCurrency(IA4562BSp.Balance8) <> 0 Then
        If Index = count Then
           Hold = GetString(IA4562BSp.PeriodEnd(7))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(8)) <> 0 Or GetCurrency(IA4562BSp.Balance9) <> 0 Then
        If Index = count Then
           Hold = GetString(IA4562BSp.PeriodEnd(8))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(9)) <> 0 Or GetCurrency(IA4562BSp.Balance10) <> 0 Then
        If Index = count Then
           Hold = GetString(IA4562BSp.PeriodEnd(9))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(10)) <> 0 Or GetCurrency(IA4562BSp.Balance11) <> 0 Then
        If Index = count Then
           Hold = GetString(IA4562BSp.PeriodEnd(10))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(11)) <> 0 Or GetCurrency(IA4562BSp.Balance12) <> 0 Then
        If Index = count Then
           Hold = GetString(IA4562BSp.PeriodEnd(11))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(12)) <> 0 Or GetCurrency(IA4562BSp.Balance13) <> 0 Then
        If Index = count Then
           Hold = GetString(IA4562BSp.PeriodEnd(12))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(13)) <> 0 Or GetCurrency(IA4562BSp.Balance14) <> 0 Then
        If Index = count Then
           Hold = GetString(IA4562BSp.PeriodEnd(13))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(14)) <> 0 Or GetCurrency(IA4562BSp.Balance15) <> 0 Then
        If Index = count Then
           Hold = GetString(IA4562BSp.PeriodEnd(14))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.AdjAmt(15)) <> 0 Or GetCurrency(IA4562BSp.Balance16) <> 0 Then
        If Index = count Then
           Hold = GetString(IA4562BSp.PeriodEnd(15))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    If GetCurrency(IA4562BSp.CYAdjAmt) <> 0 Or GetCurrency(IA4562BSp.Balance17) <> 0 Then
        If Index = count Then
           Hold = GetString(IA4562BSp.PeriodEnd(16))
           count = 99
        Else
           count = count + 1
        End If
    End If
    
    ReturnVal = Hold
    
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IA4562Sp.SSN)
End Sub

