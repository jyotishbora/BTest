from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def AGI20_Calculation():
    ReturnVal = MaxValue(0, CDollar(GetFloat(IAWContLimit.CYAGI) * 0.2))

def AGI30_Calculation():
    ReturnVal = MaxValue(0, CDollar(GetFloat(IAWContLimit.CYAGI) * 0.3))

def AGI50_Calculation():
    ReturnVal = MaxValue(0, CDollar(GetFloat(IAWContLimit.CYAGI) * 0.5))

def AGI100_Calculation():
    ReturnVal = MaxValue(0, CDollar(GetFloat(IAWContLimit.CYAGI) * 1))

def CY20After_Calculation():
    ReturnVal = GetCurrency(IAWContLimit.DedCY20) + GetCurrency(IAWContLimit.DedPY20)

def CY20Lim_Calculation():
    ReturnVal = GetCurrency(USWContLimit.CY20Lim)

def CY30After_Calculation():
    ReturnVal = GetCurrency(IAWContLimit.DedCY30) + GetCurrency(IAWContLimit.DedPY30)

def CY30AfterCG_Calculation():
    ReturnVal = GetCurrency(IAWContLimit.DedCY30CG) + GetCurrency(IAWContLimit.DedPY30CG)

def CY30Lim_Calculation():
    ReturnVal = GetCurrency(USWContLimit.CY30Lim)

def CY30LimCG_Calculation():
    ReturnVal = GetCurrency(USWContLimit.CY30LimCG)

def CY50After_Calculation():
    ReturnVal = GetCurrency(IAWContLimit.DedCY50) + GetCurrency(IAWContLimit.DedPY50)

def CY50Lim_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWContLimit.CYTot) - GetCurrency(IAWContLimit.CY30Lim) - GetCurrency(IAWContLimit.CY30LimCG) - GetCurrency(IAWContLimit.CY20Lim) - GetCurrency(IAWContLimit.CYNoLim) - GetCurrency(IAWContLimit.CYQualLim))

def CYAGI_Calculation():
    ReturnVal = GetCurrency(IASchA.IAAGI)

def CYNoLim_Calculation():
    ReturnVal = GetCurrency(USWContLimit.CYNoLim)

def CYNoLimit2_Calculation():
    ReturnVal = GetCurrency(IAWContLimit.DedCY100) + GetCurrency(IAWContLimit.DedPY100)

def CYQualAfter_Calculation():
    Contributions = Currency()
    Contributions = MinValue(GetCurrency(IAWContLimit.CYQualLim), GetCurrency(IAWContLimit.CYAGI) - GetCurrency(IAWContLimit.CY50After) - GetCurrency(IAWContLimit.CY30After) - GetCurrency(IAWContLimit.CY30AfterCG) - GetCurrency(IAWContLimit.CY20After) - GetCurrency(IAWContLimit.CYNoLimit2))
    ReturnVal = MaxValue(0, Contributions)

def CYTot_Calculation():
    ReturnVal = GetCurrency(IASchA.Contrib) + GetCurrency(IASchA.Gifts)

def CYTotAfter_Calculation():
    ReturnVal = GetCurrency(IAWContLimit.CY50After) + GetCurrency(IAWContLimit.CY30After) + GetCurrency(IAWContLimit.CY30AfterCG) + GetCurrency(IAWContLimit.CY20After) + GetCurrency(IAWContLimit.CYNoLimit2) + GetCurrency(IAWContLimit.CYQualAfter)

def DedCY20_Calculation():
    Rem20 = Currency()

    Rem30 = Currency()

    Rem30CG = Currency()

    Rem50 = Currency()

    Min2 = Currency()

    Min3 = Currency()
    #per pub 526 limited to lesser of 20% of AGI, or 30% of AGI minus 30% contributions or 50% of AGI minus 50% contributions
    Rem20 = MaxValue(0, MinValue(GetCurrency(IAWContLimit.AGI20), GetCurrency(IAWContLimit.CY20Lim)))
    Rem30 = MaxValue(0, GetCurrency(IAWContLimit.AGI30) - GetCurrency(IAWContLimit.Tot30Cont))
    Rem30CG = MaxValue(0, GetCurrency(IAWContLimit.AGI30) - GetCurrency(IAWContLimit.Tot30ContCG))
    Rem50 = MaxValue(0, GetCurrency(IAWContLimit.AGI50) - GetCurrency(IAWContLimit.Tot50Cont) - GetCurrency(IAWContLimit.Tot30ContCG) - GetCurrency(IAWContLimit.Tot30Cont))
    Min2 = MinValue(Rem20, Rem30)
    Min3 = MinValue(Min2, Rem30CG)
    ReturnVal = MaxValue(0, MinValue(Min3, Rem50))

def DedCY30_Calculation():
    Rem30 = Currency()

    Rem50 = Currency()

    Thirty = Currency()
    Rem30 = MaxValue(0, MinValue(GetCurrency(IAWContLimit.AGI30), GetCurrency(IAWContLimit.CY30Lim)))
    Rem50 = MaxValue(0, GetCurrency(IAWContLimit.AGI50) - GetCurrency(IAWContLimit.Tot50Cont) - GetCurrency(IAWContLimit.Tot30ContCG))
    ReturnVal = MaxValue(0, MinValue(Rem30, Rem50))

def DedCY30CG_Calculation():
    Rem30 = Currency()
    Rem30 = MaxValue(0, MinValue(GetCurrency(IAWContLimit.AGI30), GetCurrency(IAWContLimit.CY30LimCG)))
    ReturnVal = MaxValue(0, MinValue(Rem30, GetCurrency(IAWContLimit.AGI50) - GetCurrency(IAWContLimit.Tot50Cont)))

def DedCY50_Calculation():
    ReturnVal = MinValue(GetCurrency(IAWContLimit.CY50Lim), GetCurrency(IAWContLimit.AGI50))

def DedCY100_Calculation():
    Rem100 = Currency()

    Hundred = Currency()
    Rem100 = MaxValue(0, MinValue(GetCurrency(IAWContLimit.AGI100), GetCurrency(IAWContLimit.CYNoLim)))
    Hundred = MaxValue(0, MinValue(Rem100, GetCurrency(IAWContLimit.AGI100) - GetCurrency(IAWContLimit.Tot50Cont) - GetCurrency(IAWContLimit.Tot30ContCG) - GetCurrency(IAWContLimit.Tot30Cont) - GetCurrency(IAWContLimit.Tot20Cont)))
    ReturnVal = MaxValue(0, MinValue(Rem100, Hundred))

def DedPY20_Calculation():
    Rem20 = Currency()

    Rem30CG = Currency()

    Rem30 = Currency()

    Rem50 = Currency()

    Min2 = Currency()

    Min3 = Currency()

    Min4 = Currency()

    Twenty = Currency()
    Rem20 = MaxValue(0, MinValue(GetCurrency(IAWContLimit.AGI20), GetCurrency(IAWContLimit.PY20Lim)))
    Rem30CG = MaxValue(0, GetCurrency(IAWContLimit.AGI30) - GetCurrency(IAWContLimit.Tot30ContCG) - GetCurrency(IAWContLimit.DedCY20))
    Rem30 = MaxValue(0, GetCurrency(IAWContLimit.AGI30) - GetCurrency(IAWContLimit.Tot30Cont) - GetCurrency(IAWContLimit.DedCY20))
    Rem50 = MaxValue(0, GetCurrency(IAWContLimit.AGI50) - GetCurrency(IAWContLimit.Tot50Cont) - GetCurrency(IAWContLimit.Tot30ContCG) - GetCurrency(IAWContLimit.Tot30Cont) - GetCurrency(IAWContLimit.DedCY20))
    Twenty = MaxValue(0, GetCurrency(IAWContLimit.AGI20) - GetCurrency(IAWContLimit.DedCY20))
    Min2 = MinValue(Rem20, Rem30CG)
    Min3 = MinValue(Rem30, Rem50)
    Min4 = MinValue(Min2, Twenty)
    ReturnVal = MaxValue(0, MinValue(Min3, Min4))

def DedPY30_Calculation():
    Rem30 = Currency()

    Tot30 = Currency()

    Thirty = Currency()
    Rem30 = MaxValue(0, MinValue(GetCurrency(IAWContLimit.AGI30), GetCurrency(IAWContLimit.PY30Lim)))
    Tot30 = MaxValue(0, GetCurrency(IAWContLimit.AGI30) - GetCurrency(IAWContLimit.CY30Lim))
    Thirty = MaxValue(0, MinValue(Rem30, GetCurrency(IAWContLimit.AGI50) - GetCurrency(IAWContLimit.Tot50Cont) - GetCurrency(IAWContLimit.Tot30ContCG) - GetCurrency(IAWContLimit.DedCY30)))
    ReturnVal = MinValue(Thirty, Tot30)

def DedPY30CG_Calculation():
    Rem30CG = Currency()

    Rem50 = Currency()

    Min2 = Currency()

    ThirtyCG = Currency()
    Rem30CG = MaxValue(0, MinValue(GetCurrency(IAWContLimit.AGI30), GetCurrency(IAWContLimit.PY30LimCG)))
    Rem50 = MaxValue(0, GetCurrency(IAWContLimit.AGI50) - GetCurrency(IAWContLimit.Tot50Cont) - GetCurrency(IAWContLimit.DedCY30CG))
    ThirtyCG = MaxValue(0, GetCurrency(IAWContLimit.AGI30) - GetCurrency(IAWContLimit.DedCY30CG))
    Min2 = MinValue(Rem30CG, Rem50)
    ReturnVal = MaxValue(0, MinValue(Min2, ThirtyCG))

def DedPY50_Calculation():
    Rem50 = Currency()
    Rem50 = MaxValue(0, MinValue(GetCurrency(IAWContLimit.AGI50), GetCurrency(IAWContLimit.PY50Lim)))
    ReturnVal = MaxValue(0, MinValue(Rem50, GetCurrency(IAWContLimit.AGI50) - GetCurrency(IAWContLimit.DedCY50)))

def DedPY100_Calculation():
    Hundred = Currency()

    Rem100 = Currency()
    Rem100 = MaxValue(0, MinValue(GetCurrency(IAWContLimit.AGI100), GetCurrency(IAWContLimit.PYNoLim)))
    Hundred = MaxValue(0, MinValue(Rem100, GetCurrency(IAWContLimit.AGI100) - GetCurrency(IAWContLimit.Tot50Cont) - GetCurrency(IAWContLimit.Tot30ContCG) - GetCurrency(IAWContLimit.Tot30Cont) - GetCurrency(IAWContLimit.Tot20Cont) - GetCurrency(IAWContLimit.DedCY100)))
    ReturnVal = MaxValue(0, MinValue(Rem100, Hundred))

def Desc_Calculation():
    ReturnVal = 'Contribution Limitation Worksheet'

def Exist_Calculation():
    ReturnVal = 1

def Names_Calculation():
    ReturnVal = GetString(IARequired.CombNames)

def NY20Lim_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWContLimit.Tot20Cont) - GetCurrency(IAWContLimit.CY20After))

def NY30Lim_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWContLimit.Tot30Cont) - GetCurrency(IAWContLimit.CY30After))

def NY30LimCG_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWContLimit.Tot30ContCG) - GetCurrency(IAWContLimit.CY30AfterCG))

def NY50Lim_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWContLimit.Tot50Cont) - GetCurrency(IAWContLimit.CY50After))

def NYNoLim_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWContLimit.Tot100Cont) - GetCurrency(IAWContLimit.CYNoLimit2))

def NYQualLim_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWContLimit.TotQualCont) - GetCurrency(IAWContLimit.CYQualAfter))

def NYTot_Calculation():
    ReturnVal = GetCurrency(IAWContLimit.NY50Lim) + GetCurrency(IAWContLimit.NY30Lim) + GetCurrency(IAWContLimit.NY30LimCG) + GetCurrency(IAWContLimit.NY20Lim) + GetCurrency(IAWContLimit.NYNoLim) + GetCurrency(IAWContLimit.NYQualLim)

def PY20Lim_Calculation():
    ReturnVal = GetCurrency(USWContLimit.PY20Lim)

def PY30Lim_Calculation():
    ReturnVal = GetCurrency(USWContLimit.PY30Lim)

def PY30LimCG_Calculation():
    ReturnVal = GetCurrency(USWContLimit.PY30LimCG)

def PY50Lim_Calculation():
    ReturnVal = GetCurrency(USWContLimit.PY50Lim)

def PYNoLim_Calculation():
    ReturnVal = GetCurrency(USWContLimit.PYNoLim)

def PYTot_Calculation():
    ReturnVal = GetCurrency(IAWContLimit.PY50Lim) + GetCurrency(IAWContLimit.PY30Lim) + GetCurrency(IAWContLimit.PY30LimCG) + GetCurrency(IAWContLimit.PY20Lim) + GetCurrency(IAWContLimit.PYNoLim)

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

def Tot20Cont_Calculation():
    ReturnVal = GetCurrency(IAWContLimit.PY20Lim) + GetCurrency(IAWContLimit.CY20Lim)

def Tot30Cont_Calculation():
    ReturnVal = GetCurrency(IAWContLimit.PY30Lim) + GetCurrency(IAWContLimit.CY30Lim)

def Tot30ContCG_Calculation():
    ReturnVal = GetCurrency(IAWContLimit.PY30LimCG) + GetCurrency(IAWContLimit.CY30LimCG)

def Tot50Cont_Calculation():
    ReturnVal = GetCurrency(IAWContLimit.PY50Lim) + GetCurrency(IAWContLimit.CY50Lim)

def Tot100Cont_Calculation():
    ReturnVal = GetCurrency(IAWContLimit.PYNoLim) + GetCurrency(IAWContLimit.CYNoLim)

def TotCont_Calculation():
    ReturnVal = GetCurrency(IAWContLimit.PYTot) + GetCurrency(IAWContLimit.CYTot)

def TotQualCont_Calculation():
    ReturnVal = GetCurrency(IAWContLimit.CYQualLim)

