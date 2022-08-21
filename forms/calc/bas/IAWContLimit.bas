Private Sub AGI20_Calculation()
    ReturnVal = MaxValue(0, CDollar(GetFloat(IAWContLimit.CYAGI) * 0.2))
End Sub

Private Sub AGI30_Calculation()
    ReturnVal = MaxValue(0, CDollar(GetFloat(IAWContLimit.CYAGI) * 0.3))
End Sub

Private Sub AGI50_Calculation()
    ReturnVal = MaxValue(0, CDollar(GetFloat(IAWContLimit.CYAGI) * 0.5))
End Sub

Private Sub AGI100_Calculation()
    ReturnVal = MaxValue(0, CDollar(GetFloat(IAWContLimit.CYAGI) * 1#))
End Sub

Private Sub CY20After_Calculation()
    ReturnVal = GetCurrency(IAWContLimit.DedCY20) + GetCurrency(IAWContLimit.DedPY20)
End Sub

Private Sub CY20Lim_Calculation()
    ReturnVal = GetCurrency(USWContLimit.CY20Lim)
End Sub

Private Sub CY30After_Calculation()
    ReturnVal = GetCurrency(IAWContLimit.DedCY30) + GetCurrency(IAWContLimit.DedPY30)
End Sub

Private Sub CY30AfterCG_Calculation()
    ReturnVal = GetCurrency(IAWContLimit.DedCY30CG) + GetCurrency(IAWContLimit.DedPY30CG)
End Sub

Private Sub CY30Lim_Calculation()
    ReturnVal = GetCurrency(USWContLimit.CY30Lim)
End Sub

Private Sub CY30LimCG_Calculation()
    ReturnVal = GetCurrency(USWContLimit.CY30LimCG)
End Sub

Private Sub CY50After_Calculation()
    ReturnVal = GetCurrency(IAWContLimit.DedCY50) + GetCurrency(IAWContLimit.DedPY50)
End Sub

Private Sub CY50Lim_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWContLimit.CYTot) - GetCurrency(IAWContLimit.CY30Lim) - GetCurrency(IAWContLimit.CY30LimCG) - GetCurrency(IAWContLimit.CY20Lim) - GetCurrency(IAWContLimit.CYNoLim) - GetCurrency(IAWContLimit.CYQualLim))
End Sub

Private Sub CYAGI_Calculation()
    ReturnVal = GetCurrency(IASchA.IAAGI)
End Sub

Private Sub CYNoLim_Calculation()
    ReturnVal = GetCurrency(USWContLimit.CYNoLim)
End Sub

Private Sub CYNoLimit2_Calculation()
    ReturnVal = GetCurrency(IAWContLimit.DedCY100) + GetCurrency(IAWContLimit.DedPY100)
End Sub

Private Sub CYQualAfter_Calculation()
    Dim Contributions As Currency
    
    Contributions = MinValue(GetCurrency(IAWContLimit.CYQualLim), GetCurrency(IAWContLimit.CYAGI) - GetCurrency(IAWContLimit.CY50After) - GetCurrency(IAWContLimit.CY30After) - GetCurrency(IAWContLimit.CY30AfterCG) - GetCurrency(IAWContLimit.CY20After) - GetCurrency(IAWContLimit.CYNoLimit2))

    ReturnVal = MaxValue(0, Contributions)
End Sub

Private Sub CYTot_Calculation()
    ReturnVal = GetCurrency(IASchA.Contrib) + GetCurrency(IASchA.Gifts)
End Sub

Private Sub CYTotAfter_Calculation()
    ReturnVal = GetCurrency(IAWContLimit.CY50After) + GetCurrency(IAWContLimit.CY30After) + GetCurrency(IAWContLimit.CY30AfterCG) + GetCurrency(IAWContLimit.CY20After) + GetCurrency(IAWContLimit.CYNoLimit2) + GetCurrency(IAWContLimit.CYQualAfter)
End Sub

Private Sub DedCY20_Calculation()
    'per pub 526 limited to lesser of 20% of AGI, or 30% of AGI minus 30% contributions or 50% of AGI minus 50% contributions
    Dim Rem20 As Currency
    Dim Rem30 As Currency
    Dim Rem30CG As Currency
    Dim Rem50 As Currency
    Dim Min2 As Currency
    Dim Min3 As Currency
    
    Rem20 = MaxValue(0, MinValue(GetCurrency(IAWContLimit.AGI20), GetCurrency(IAWContLimit.CY20Lim)))
    Rem30 = MaxValue(0, GetCurrency(IAWContLimit.AGI30) - GetCurrency(IAWContLimit.Tot30Cont))
    Rem30CG = MaxValue(0, GetCurrency(IAWContLimit.AGI30) - GetCurrency(IAWContLimit.Tot30ContCG))
    Rem50 = MaxValue(0, GetCurrency(IAWContLimit.AGI50) - GetCurrency(IAWContLimit.Tot50Cont) - GetCurrency(IAWContLimit.Tot30ContCG) - GetCurrency(IAWContLimit.Tot30Cont))
    
    Min2 = MinValue(Rem20, Rem30)
    Min3 = MinValue(Min2, Rem30CG)
    
    ReturnVal = MaxValue(0, MinValue(Min3, Rem50))
End Sub

Private Sub DedCY30_Calculation()
    Dim Rem30 As Currency
    Dim Rem50 As Currency
    Dim Thirty As Currency
    
    Rem30 = MaxValue(0, MinValue(GetCurrency(IAWContLimit.AGI30), GetCurrency(IAWContLimit.CY30Lim)))
    Rem50 = MaxValue(0, GetCurrency(IAWContLimit.AGI50) - GetCurrency(IAWContLimit.Tot50Cont) - GetCurrency(IAWContLimit.Tot30ContCG))
    
    ReturnVal = MaxValue(0, MinValue(Rem30, Rem50))
End Sub

Private Sub DedCY30CG_Calculation()
    Dim Rem30 As Currency
        
    Rem30 = MaxValue(0, MinValue(GetCurrency(IAWContLimit.AGI30), GetCurrency(IAWContLimit.CY30LimCG)))
    
    ReturnVal = MaxValue(0, MinValue(Rem30, GetCurrency(IAWContLimit.AGI50) - GetCurrency(IAWContLimit.Tot50Cont)))
End Sub

Private Sub DedCY50_Calculation()
    ReturnVal = MinValue(GetCurrency(IAWContLimit.CY50Lim), GetCurrency(IAWContLimit.AGI50))
End Sub

Private Sub DedCY100_Calculation()
    Dim Rem100 As Currency
    Dim Hundred As Currency
    
    Rem100 = MaxValue(0, MinValue(GetCurrency(IAWContLimit.AGI100), GetCurrency(IAWContLimit.CYNoLim)))
    Hundred = MaxValue(0, MinValue(Rem100, GetCurrency(IAWContLimit.AGI100) - GetCurrency(IAWContLimit.Tot50Cont) - GetCurrency(IAWContLimit.Tot30ContCG) - GetCurrency(IAWContLimit.Tot30Cont) - GetCurrency(IAWContLimit.Tot20Cont)))
    
    ReturnVal = MaxValue(0, MinValue(Rem100, Hundred))
End Sub

Private Sub DedPY20_Calculation()
    Dim Rem20 As Currency
    Dim Rem30CG As Currency
    Dim Rem30 As Currency
    Dim Rem50 As Currency
    Dim Min2 As Currency
    Dim Min3 As Currency
    Dim Min4 As Currency
    Dim Twenty As Currency
    
    Rem20 = MaxValue(0, MinValue(GetCurrency(IAWContLimit.AGI20), GetCurrency(IAWContLimit.PY20Lim)))
    Rem30CG = MaxValue(0, GetCurrency(IAWContLimit.AGI30) - GetCurrency(IAWContLimit.Tot30ContCG) - GetCurrency(IAWContLimit.DedCY20))
    Rem30 = MaxValue(0, GetCurrency(IAWContLimit.AGI30) - GetCurrency(IAWContLimit.Tot30Cont) - GetCurrency(IAWContLimit.DedCY20))
    Rem50 = MaxValue(0, GetCurrency(IAWContLimit.AGI50) - GetCurrency(IAWContLimit.Tot50Cont) - GetCurrency(IAWContLimit.Tot30ContCG) - GetCurrency(IAWContLimit.Tot30Cont) - GetCurrency(IAWContLimit.DedCY20))
    Twenty = MaxValue(0, GetCurrency(IAWContLimit.AGI20) - GetCurrency(IAWContLimit.DedCY20))
    
    Min2 = MinValue(Rem20, Rem30CG)
    Min3 = MinValue(Rem30, Rem50)
    Min4 = MinValue(Min2, Twenty)
    
    ReturnVal = MaxValue(0, MinValue(Min3, Min4))
End Sub

Private Sub DedPY30_Calculation()
    Dim Rem30 As Currency
    Dim Tot30 As Currency
    Dim Thirty As Currency
        
    Rem30 = MaxValue(0, MinValue(GetCurrency(IAWContLimit.AGI30), GetCurrency(IAWContLimit.PY30Lim)))
    Tot30 = MaxValue(0, GetCurrency(IAWContLimit.AGI30) - GetCurrency(IAWContLimit.CY30Lim))
    Thirty = MaxValue(0, MinValue(Rem30, GetCurrency(IAWContLimit.AGI50) - GetCurrency(IAWContLimit.Tot50Cont) - GetCurrency(IAWContLimit.Tot30ContCG) - GetCurrency(IAWContLimit.DedCY30)))

    ReturnVal = MinValue(Thirty, Tot30)
End Sub

Private Sub DedPY30CG_Calculation()
    Dim Rem30CG As Currency
    Dim Rem50 As Currency
    Dim Min2 As Currency
    Dim ThirtyCG As Currency
    
    Rem30CG = MaxValue(0, MinValue(GetCurrency(IAWContLimit.AGI30), GetCurrency(IAWContLimit.PY30LimCG)))
    Rem50 = MaxValue(0, GetCurrency(IAWContLimit.AGI50) - GetCurrency(IAWContLimit.Tot50Cont) - GetCurrency(IAWContLimit.DedCY30CG))
    ThirtyCG = MaxValue(0, GetCurrency(IAWContLimit.AGI30) - GetCurrency(IAWContLimit.DedCY30CG))
    Min2 = MinValue(Rem30CG, Rem50)
    
    ReturnVal = MaxValue(0, MinValue(Min2, ThirtyCG))
End Sub

Private Sub DedPY50_Calculation()
    Dim Rem50 As Currency
    
    Rem50 = MaxValue(0, MinValue(GetCurrency(IAWContLimit.AGI50), GetCurrency(IAWContLimit.PY50Lim)))
    
    ReturnVal = MaxValue(0, MinValue(Rem50, GetCurrency(IAWContLimit.AGI50) - GetCurrency(IAWContLimit.DedCY50)))
End Sub

Private Sub DedPY100_Calculation()
    Dim Hundred As Currency
    Dim Rem100 As Currency

    Rem100 = MaxValue(0, MinValue(GetCurrency(IAWContLimit.AGI100), GetCurrency(IAWContLimit.PYNoLim)))
    Hundred = MaxValue(0, MinValue(Rem100, GetCurrency(IAWContLimit.AGI100) - GetCurrency(IAWContLimit.Tot50Cont) - GetCurrency(IAWContLimit.Tot30ContCG) - GetCurrency(IAWContLimit.Tot30Cont) - GetCurrency(IAWContLimit.Tot20Cont) - GetCurrency(IAWContLimit.DedCY100)))
    
    ReturnVal = MaxValue(0, MinValue(Rem100, Hundred))
End Sub

Private Sub Desc_Calculation()
    ReturnVal = "Contribution Limitation Worksheet"
End Sub

Private Sub Exist_Calculation()
    ReturnVal = 1
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(IARequired.CombNames)
End Sub

Private Sub NY20Lim_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWContLimit.Tot20Cont) - GetCurrency(IAWContLimit.CY20After))
End Sub

Private Sub NY30Lim_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWContLimit.Tot30Cont) - GetCurrency(IAWContLimit.CY30After))
End Sub

Private Sub NY30LimCG_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWContLimit.Tot30ContCG) - GetCurrency(IAWContLimit.CY30AfterCG))
End Sub

Private Sub NY50Lim_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWContLimit.Tot50Cont) - GetCurrency(IAWContLimit.CY50After))
End Sub

Private Sub NYNoLim_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWContLimit.Tot100Cont) - GetCurrency(IAWContLimit.CYNoLimit2))
End Sub

Private Sub NYQualLim_Calculation()
    ReturnVal = MaxValue(0, GetCurrency(IAWContLimit.TotQualCont) - GetCurrency(IAWContLimit.CYQualAfter))
End Sub

Private Sub NYTot_Calculation()
    ReturnVal = GetCurrency(IAWContLimit.NY50Lim) + GetCurrency(IAWContLimit.NY30Lim) + GetCurrency(IAWContLimit.NY30LimCG) + GetCurrency(IAWContLimit.NY20Lim) + GetCurrency(IAWContLimit.NYNoLim) + GetCurrency(IAWContLimit.NYQualLim)
End Sub

Private Sub PY20Lim_Calculation()
    ReturnVal = GetCurrency(USWContLimit.PY20Lim)
End Sub

Private Sub PY30Lim_Calculation()
    ReturnVal = GetCurrency(USWContLimit.PY30Lim)
End Sub

Private Sub PY30LimCG_Calculation()
    ReturnVal = GetCurrency(USWContLimit.PY30LimCG)
End Sub

Private Sub PY50Lim_Calculation()
    ReturnVal = GetCurrency(USWContLimit.PY50Lim)
End Sub

Private Sub PYNoLim_Calculation()
    ReturnVal = GetCurrency(USWContLimit.PYNoLim)
End Sub

Private Sub PYTot_Calculation()
    ReturnVal = GetCurrency(IAWContLimit.PY50Lim) + GetCurrency(IAWContLimit.PY30Lim) + GetCurrency(IAWContLimit.PY30LimCG) + GetCurrency(IAWContLimit.PY20Lim) + GetCurrency(IAWContLimit.PYNoLim)
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

Private Sub Tot20Cont_Calculation()
    ReturnVal = GetCurrency(IAWContLimit.PY20Lim) + GetCurrency(IAWContLimit.CY20Lim)
End Sub

Private Sub Tot30Cont_Calculation()
    ReturnVal = GetCurrency(IAWContLimit.PY30Lim) + GetCurrency(IAWContLimit.CY30Lim)
End Sub

Private Sub Tot30ContCG_Calculation()
    ReturnVal = GetCurrency(IAWContLimit.PY30LimCG) + GetCurrency(IAWContLimit.CY30LimCG)
End Sub

Private Sub Tot50Cont_Calculation()
    ReturnVal = GetCurrency(IAWContLimit.PY50Lim) + GetCurrency(IAWContLimit.CY50Lim)
End Sub

Private Sub Tot100Cont_Calculation()
    ReturnVal = GetCurrency(IAWContLimit.PYNoLim) + GetCurrency(IAWContLimit.CYNoLim)
End Sub

Private Sub TotCont_Calculation()
    ReturnVal = GetCurrency(IAWContLimit.PYTot) + GetCurrency(IAWContLimit.CYTot)
End Sub

Private Sub TotQualCont_Calculation()
    ReturnVal = GetCurrency(IAWContLimit.CYQualLim)
End Sub

