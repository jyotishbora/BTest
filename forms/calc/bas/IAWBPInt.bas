Private Sub Desc_Calculation()
    ReturnVal = CStr(GetCurrency(IAWBPInt.TotalInterest)) & " Additional Interest"
End Sub

Private Sub ExemptInt_Calculation(Index As Integer)
    Dim Stuff As Integer
    Dim MoStuff As Integer
    Dim ResSFM As Integer
    Dim OthSFM As Integer
    Dim OID As Integer
    Dim INT1099 As Integer
    Dim PartK1 As Integer
    Dim SCorpK1 As Integer
    Dim EstK1 As Integer
    Dim TPAccMktDisc As Boolean
    
    ResSFM = GetNumber(IAWBBump.ResSFMNbr)
    OthSFM = GetNumber(IAWBBump.OthSFMNbr)
    OID = GetNumber(IAWBBump.OIDNbr)
    INT1099 = GetNumber(IAWBBump.INTNbr)
    PartK1 = GetNumber(IAWBBump.PartK1Nbr)
    SCorpK1 = GetNumber(IAWBBump.SCorpK1Nbr)
    EstK1 = GetNumber(IAWBBump.EstK1Nbr)
    TPAccMktDisc = GetBool(IASchB.TPAccMktDiscInt)
    
    MoStuff = Index + GetNumber(IAWBPInt.Offset)
    
    If GetNumber(IASchB.TotINTCopies) = 7 Then
        ReturnVal = 0
    ElseIf ResSFM > MoStuff Then
        ReturnVal = 0
    ElseIf ResSFM + OthSFM > MoStuff Then
        Stuff = (MoStuff) - ResSFM
        ReturnVal = 0
    ElseIf ResSFM + OthSFM + OID > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM
        ReturnVal = Round(GetCurrency(USD1099OID.USInt, (GetNumber(IAWBBump.OID(Stuff))))) + Round(GetCurrency(USD1099OID.StExempt, (GetNumber(IAWBBump.OID(Stuff))))) + Round(GetCurrency(USD1099OID.Nominee, (GetNumber(IAWBBump.OID(Stuff))))) + MaxValue(0, Round(GetCurrency(USD1099OID.BOIDAdjAmt, (GetNumber(IAWBBump.OID(Stuff))))))
    ElseIf ResSFM + OthSFM + OID + INT1099 > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID
        ReturnVal = Round(GetCurrency(USD1099INT.USInt, (GetNumber(IAWBBump.INT(Stuff))))) + Round(GetCurrency(USD1099INT.Nominee, (GetNumber(IAWBBump.INT(Stuff))))) + Round(GetCurrency(USD1099INT.AccruedInt, (GetNumber(IAWBBump.INT(Stuff))))) + Round(GetCurrency(USD1099INT.ABP, (GetNumber(IAWBBump.INT(Stuff))))) + Round(GetCurrency(USD1099INT.StateExmpt, (GetNumber(IAWBBump.INT(Stuff)))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099
        ReturnVal = GetCurrency(USDPartK1.NetStTEI, (GetNumber(IAWBBump.PartK1(Stuff)))) + GetCurrency(USDPartK1.FedStTEI, (GetNumber(IAWBBump.PartK1(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1
        ReturnVal = GetCurrency(USDSCorpK1.NetStTEI, (GetNumber(IAWBBump.SCorpK1(Stuff)))) + GetCurrency(USDSCorpK1.FedStTEI, (GetNumber(IAWBBump.SCorpK1(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1
        ReturnVal = GetCurrency(USDEstK1.NetStTEI, (GetNumber(IAWBBump.EstK1(Stuff)))) + GetCurrency(USDEstK1.FedStTEI, (GetNumber(IAWBBump.EstK1(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1
        ReturnVal = 0
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc
        ReturnVal = 0
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt)
        ReturnVal = 0
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt)
        ReturnVal = 0
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay)
        ReturnVal = 0
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) + GetBool(IASchB.JtContigentPay) > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay) - GetBool(IASchB.SPContigentPay)
        ReturnVal = 0
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Exist_Calculation()
    ReturnVal = 1
End Sub

Private Sub IJ1_Calculation(Index As Integer)
    Dim Stuff As Integer
    Dim MoStuff As Integer
    Dim ResSFM As Integer
    Dim OthSFM As Integer
    Dim OID As Integer
    Dim INT1099 As Integer
    Dim PartK1 As Integer
    Dim SCorpK1 As Integer
    Dim EstK1 As Integer
    Dim TPAccMktDisc As Boolean
    
    ResSFM = GetNumber(IAWBBump.ResSFMNbr)
    OthSFM = GetNumber(IAWBBump.OthSFMNbr)
    OID = GetNumber(IAWBBump.OIDNbr)
    INT1099 = GetNumber(IAWBBump.INTNbr)
    PartK1 = GetNumber(IAWBBump.PartK1Nbr)
    SCorpK1 = GetNumber(IAWBBump.SCorpK1Nbr)
    EstK1 = GetNumber(IAWBBump.EstK1Nbr)
    TPAccMktDisc = GetBool(IASchB.TPAccMktDiscInt)
    
    MoStuff = Index + GetNumber(IAWBPInt.Offset)
    
    If GetNumber(IASchB.TotINTCopies) = 7 Then
        ReturnVal = 0
    ElseIf ResSFM > MoStuff Then
        ReturnVal = GetBool(USDSFM.Joint, GetNumber(IAWBBump.ResSFM(MoStuff)))
    ElseIf ResSFM + OthSFM > MoStuff Then
        Stuff = (MoStuff) - ResSFM
        ReturnVal = GetBool(USDSFM.Joint, (GetNumber(IAWBBump.OthSFM(Stuff))))
    ElseIf ResSFM + OthSFM + OID > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM
        ReturnVal = GetBool(USD1099OID.Joint, (GetNumber(IAWBBump.OID(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID
        ReturnVal = GetBool(USD1099INT.Joint, (GetNumber(IAWBBump.Int(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099
        ReturnVal = GetBool(USDPartK1.Joint, (GetNumber(IAWBBump.PartK1(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1
        ReturnVal = GetBool(USDSCorpK1.Joint, (GetNumber(IAWBBump.SCorpK1(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1
        ReturnVal = GetBool(USDEstK1.Joint, (GetNumber(IAWBBump.EstK1(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1
        ReturnVal = 0
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc
        ReturnVal = 0
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt)
        ReturnVal = 1
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt)
        ReturnVal = 0
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay)
        ReturnVal = 0
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) + GetBool(IASchB.JtContigentPay) > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay) - GetBool(IASchB.SPContigentPay)
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub IntAcctOwner_Calculation(Index As Integer)
    If GetBool(IAWBPInt.ITp1(Index)) = True Then
        ReturnVal = "Taxpayer"
    ElseIf GetBool(IAWBPInt.ISp1(Index)) = True Then
        ReturnVal = "Spouse"
    ElseIf GetBool(IAWBPInt.IJ1(Index)) = True Then
        ReturnVal = "Joint"
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub Interest_Calculation(Index As Integer)
    Dim Stuff As Integer
    Dim MoStuff As Integer
    Dim ResSFM As Integer
    Dim OthSFM As Integer
    Dim OID As Integer
    Dim INT1099 As Integer
    Dim PartK1 As Integer
    Dim SCorpK1 As Integer
    Dim EstK1 As Integer
    Dim TPAccMktDisc As Boolean
    
    ResSFM = GetNumber(IAWBBump.ResSFMNbr)
    OthSFM = GetNumber(IAWBBump.OthSFMNbr)
    OID = GetNumber(IAWBBump.OIDNbr)
    INT1099 = GetNumber(IAWBBump.INTNbr)
    PartK1 = GetNumber(IAWBBump.PartK1Nbr)
    SCorpK1 = GetNumber(IAWBBump.SCorpK1Nbr)
    EstK1 = GetNumber(IAWBBump.EstK1Nbr)
    TPAccMktDisc = GetBool(IASchB.TPAccMktDiscInt)
    
    MoStuff = Index + GetNumber(IAWBPInt.Offset)
    
    If GetNumber(IASchB.TotINTCopies) = 7 Then
        ReturnVal = 0
    ElseIf ResSFM > MoStuff Then
        ReturnVal = Round(GetCurrency(USDSFM.Interest, GetNumber(IAWBBump.ResSFM(MoStuff))))
    ElseIf ResSFM + OthSFM > MoStuff Then
        Stuff = (MoStuff) - ResSFM
        ReturnVal = Round(GetCurrency(USDSFM.Interest, (GetNumber(IAWBBump.OthSFM(Stuff)))))
    ElseIf ResSFM + OthSFM + OID > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM
        ReturnVal = GetCurrency(USD1099OID.BAmt, (GetNumber(IAWBBump.OID(Stuff)))) + Round(GetCurrency(USD1099OID.TaxExempt, (GetNumber(IAWBBump.OID(Stuff))))) - MinValue(0, Round(GetCurrency(USD1099OID.BOIDAdjAmt, (GetNumber(IAWBBump.OID(Stuff))))))
    ElseIf ResSFM + OthSFM + OID + INT1099 > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID
        ReturnVal = GetCurrency(USD1099INT.BAmtEF, (GetNumber(IAWBBump.INT(Stuff)))) + GetCurrency(USD1099INT.FedExmpt, (GetNumber(IAWBBump.INT(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099
        ReturnVal = GetCurrency(USDPartK1.HaveInt, (GetNumber(IAWBBump.PartK1(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1
        ReturnVal = GetCurrency(USDSCorpK1.HaveInt, (GetNumber(IAWBBump.SCorpK1(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1
        ReturnVal = GetCurrency(USDEstK1.HaveInt, (GetNumber(IAWBBump.EstK1(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1
        ReturnVal = GetCurrency(IASchB.TPAccMktDiscInt)
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc
        ReturnVal = GetCurrency(IASchB.SPAccMktDiscInt)
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt)
        ReturnVal = GetCurrency(IASchB.JtAccMktDiscInt)
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt)
        ReturnVal = GetCurrency(IASchB.TPContigentPay)
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay)
        ReturnVal = GetCurrency(IASchB.SPContigentPay)
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) + GetBool(IASchB.JtContigentPay) > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay) - GetBool(IASchB.SPContigentPay)
        ReturnVal = GetCurrency(IASchB.JtContigentPay)
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub IntNoPayer_Calculation()
    Dim count, Iter As Integer
    
    count = 0
    Iter = 0
    Do While Iter < 22
        If GetCurrency(IAWBPInt.Interest(Iter)) > 0 And Trim(GetString(IAWBPInt.Payer(Iter))) = "" Then
            count = count + 1
        End If
        Iter = Iter + 1
    Loop
    
    If GetBool(IAWBPInt.Print) = True And count > 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub ISp1_Calculation(Index As Integer)
    Dim Stuff As Integer
    Dim MoStuff As Integer
    Dim ResSFM As Integer
    Dim OthSFM As Integer
    Dim OID As Integer
    Dim INT1099 As Integer
    Dim PartK1 As Integer
    Dim SCorpK1 As Integer
    Dim EstK1 As Integer
    Dim TPAccMktDisc As Boolean
    
    ResSFM = GetNumber(IAWBBump.ResSFMNbr)
    OthSFM = GetNumber(IAWBBump.OthSFMNbr)
    OID = GetNumber(IAWBBump.OIDNbr)
    INT1099 = GetNumber(IAWBBump.INTNbr)
    PartK1 = GetNumber(IAWBBump.PartK1Nbr)
    SCorpK1 = GetNumber(IAWBBump.SCorpK1Nbr)
    EstK1 = GetNumber(IAWBBump.EstK1Nbr)
    TPAccMktDisc = GetBool(IASchB.TPAccMktDiscInt)
    
    MoStuff = Index + GetNumber(IAWBPInt.Offset)
    
    If GetNumber(IASchB.TotINTCopies) = 7 Then
        ReturnVal = 0
    ElseIf ResSFM > MoStuff Then
        ReturnVal = GetBool(USDSFM.Spouse, GetNumber(IAWBBump.ResSFM(MoStuff)))
    ElseIf ResSFM + OthSFM > MoStuff Then
        Stuff = (MoStuff) - ResSFM
        ReturnVal = GetBool(USDSFM.Spouse, (GetNumber(IAWBBump.OthSFM(Stuff))))
    ElseIf ResSFM + OthSFM + OID > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM
        ReturnVal = GetBool(USD1099OID.Spouse, (GetNumber(IAWBBump.OID(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID
        ReturnVal = GetBool(USD1099INT.Spouse, (GetNumber(IAWBBump.Int(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099
        ReturnVal = GetBool(USDPartK1.Spouse, (GetNumber(IAWBBump.PartK1(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1
        ReturnVal = GetBool(USDSCorpK1.Spouse, (GetNumber(IAWBBump.SCorpK1(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1
        ReturnVal = GetBool(USDEstK1.Spouse, (GetNumber(IAWBBump.EstK1(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1
        ReturnVal = 0
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc
        ReturnVal = 1
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt)
        ReturnVal = 0
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt)
        ReturnVal = 0
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay)
        ReturnVal = 1
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) + GetBool(IASchB.JtContigentPay) > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay) - GetBool(IASchB.SPContigentPay)
        ReturnVal = 0
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub ITp1_Calculation(Index As Integer)
    Dim Stuff As Integer
    Dim MoStuff As Integer
    Dim ResSFM As Integer
    Dim OthSFM As Integer
    Dim OID As Integer
    Dim INT1099 As Integer
    Dim PartK1 As Integer
    Dim SCorpK1 As Integer
    Dim EstK1 As Integer
    Dim TPAccMktDisc As Boolean
    
    ResSFM = GetNumber(IAWBBump.ResSFMNbr)
    OthSFM = GetNumber(IAWBBump.OthSFMNbr)
    OID = GetNumber(IAWBBump.OIDNbr)
    INT1099 = GetNumber(IAWBBump.INTNbr)
    PartK1 = GetNumber(IAWBBump.PartK1Nbr)
    SCorpK1 = GetNumber(IAWBBump.SCorpK1Nbr)
    EstK1 = GetNumber(IAWBBump.EstK1Nbr)
    TPAccMktDisc = GetBool(IASchB.TPAccMktDiscInt)
    
    MoStuff = Index + GetNumber(IAWBPInt.Offset)
    
    If GetNumber(IASchB.TotINTCopies) = 7 Then
        ReturnVal = 0
    ElseIf ResSFM > MoStuff Then
        ReturnVal = GetBool(USDSFM.Taxpayer, GetNumber(IAWBBump.ResSFM(MoStuff)))
    ElseIf ResSFM + OthSFM > MoStuff Then
        Stuff = (MoStuff) - ResSFM
        ReturnVal = GetBool(USDSFM.Taxpayer, (GetNumber(IAWBBump.OthSFM(Stuff))))
    ElseIf ResSFM + OthSFM + OID > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM
        ReturnVal = GetBool(USD1099OID.Taxpayer, (GetNumber(IAWBBump.OID(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID
        ReturnVal = GetBool(USD1099INT.Taxpayer, (GetNumber(IAWBBump.Int(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099
        ReturnVal = GetBool(USDPartK1.Taxpayer, (GetNumber(IAWBBump.PartK1(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1
        ReturnVal = GetBool(USDSCorpK1.Taxpayer, (GetNumber(IAWBBump.SCorpK1(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1
        ReturnVal = GetBool(USDEstK1.Taxpayer, (GetNumber(IAWBBump.EstK1(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1
        ReturnVal = 1
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc
        ReturnVal = 0
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt)
        ReturnVal = 0
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt)
        ReturnVal = 1
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay)
        ReturnVal = 0
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) + GetBool(IASchB.JtContigentPay) > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay) - GetBool(IASchB.SPContigentPay)
        ReturnVal = 0
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.CombNames)
End Sub

Private Sub Offset_Calculation()
    If GetCopy() = 1 Then
        ReturnVal = 6
    ElseIf GetCopy() = 2 Then
        ReturnVal = 28
    ElseIf GetCopy() = 3 Then
        ReturnVal = 50
    ElseIf GetCopy() = 4 Then
        ReturnVal = 72
    ElseIf GetCopy() = 5 Then
        ReturnVal = 94
    ElseIf GetCopy() = 6 Then
        ReturnVal = 116
    ElseIf GetCopy() = 7 Then
        ReturnVal = 138
    ElseIf GetCopy() = 8 Then
        ReturnVal = 160
    ElseIf GetCopy() = 9 Then
        ReturnVal = 182
    ElseIf GetCopy() = 10 Then
        ReturnVal = 204
    ElseIf GetCopy() = 11 Then
        ReturnVal = 226
    Else
        ReturnVal = 248
    End If
End Sub

Private Sub Payer_Calculation(Index As Integer)
    Dim Stuff As Integer
    Dim MoStuff As Integer
    Dim ResSFM As Integer
    Dim OthSFM As Integer
    Dim OID As Integer
    Dim INT1099 As Integer
    Dim PartK1 As Integer
    Dim SCorpK1 As Integer
    Dim EstK1 As Integer
    Dim TPAccMktDisc As Boolean
    
    ResSFM = GetNumber(IAWBBump.ResSFMNbr)
    OthSFM = GetNumber(IAWBBump.OthSFMNbr)
    OID = GetNumber(IAWBBump.OIDNbr)
    INT1099 = GetNumber(IAWBBump.INTNbr)
    PartK1 = GetNumber(IAWBBump.PartK1Nbr)
    SCorpK1 = GetNumber(IAWBBump.SCorpK1Nbr)
    EstK1 = GetNumber(IAWBBump.EstK1Nbr)
    TPAccMktDisc = GetBool(IASchB.TPAccMktDiscInt)
    
    MoStuff = Index + GetNumber(IAWBPInt.Offset)
    
    If GetNumber(IASchB.TotINTCopies) = 7 Then
        ReturnVal = ""
    ElseIf ResSFM > MoStuff Then
        ReturnVal = GetString(USDSFM.NameAdd, GetNumber(IAWBBump.ResSFM(MoStuff)))
    ElseIf ResSFM + OthSFM > MoStuff Then
        Stuff = (MoStuff) - ResSFM
        ReturnVal = GetString(USDSFM.PayerName, (GetNumber(IAWBBump.OthSFM(Stuff))))
    ElseIf ResSFM + OthSFM + OID > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM
        ReturnVal = GetString(USD1099OID.PayerName, (GetNumber(IAWBBump.OID(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID
        ReturnVal = GetString(USD1099INT.PayerName, (GetNumber(IAWBBump.INT(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099
        ReturnVal = GetString(USDPartK1.CoName, (GetNumber(IAWBBump.PartK1(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1
        ReturnVal = GetString(USDSCorpK1.CoName, (GetNumber(IAWBBump.SCorpK1(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1
        ReturnVal = GetString(USDEstK1.TrustName, (GetNumber(IAWBBump.EstK1(Stuff))))
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1
        ReturnVal = "Accrued Market Discount"
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc
        ReturnVal = "Accrued Market Discount"
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt)
        ReturnVal = "Accrued Market Discount"
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt)
        ReturnVal = "Contingent Payment Debt Instrument"
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay)
        ReturnVal = "Contingent Payment Debt Instrument"
    ElseIf ResSFM + OthSFM + OID + INT1099 + PartK1 + SCorpK1 + EstK1 + TPAccMktDisc + GetBool(IASchB.SPAccMktDiscInt) + GetBool(IASchB.JtAccMktDiscInt) + GetBool(IASchB.TPContigentPay) + GetBool(IASchB.SPContigentPay) + GetBool(IASchB.JtContigentPay) > MoStuff Then
        Stuff = (MoStuff) - ResSFM - OthSFM - OID - INT1099 - PartK1 - SCorpK1 - EstK1 - TPAccMktDisc - GetBool(IASchB.SPAccMktDiscInt) - GetBool(IASchB.JtAccMktDiscInt) - GetBool(IASchB.TPContigentPay) - GetBool(IASchB.SPContigentPay)
        ReturnVal = "Contingent Payment Debt Instrument"
    Else
        ReturnVal = ""
    End If
End Sub

Private Sub Print_Calculation()
    If GetNumber(IASchB.PrintIAB) = 1 And GetCurrency(IAWBPInt.TotalInterest) <> 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

Private Sub TaxInt_Calculation(Index As Integer)
    ReturnVal = MaxValue(0, GetCurrency(IAWBPInt.Interest(Index)) - GetCurrency(IAWBPInt.ExemptInt(Index)))
End Sub

Private Sub TotalExemptInt_Calculation()
    Dim count As Integer
    Dim SubTot As Currency

    count = 0
    SubTot = 0

    Do While count < 22
        SubTot = SubTot + GetCurrency(IAWBPInt.ExemptInt(count))
        count = count + 1
    Loop
    
    ReturnVal = SubTot
End Sub

Private Sub TotalInterest_Calculation()
    Dim count As Integer
    Dim SubTot As Currency

    count = 0
    SubTot = 0

    Do While count < 22
        SubTot = SubTot + GetCurrency(IAWBPInt.Interest(count))
        count = count + 1
    Loop
    
    ReturnVal = SubTot
End Sub

Private Sub TotalTaxInt_Calculation()
    Dim count As Integer
    Dim SubTot As Currency

    count = 0
    SubTot = 0

    Do While count < 22
        SubTot = SubTot + GetCurrency(IAWBPInt.TaxInt(count))
        count = count + 1
    Loop
    
    ReturnVal = SubTot
End Sub

