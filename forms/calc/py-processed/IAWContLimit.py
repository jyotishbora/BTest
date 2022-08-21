from forms.out import IAF1040
from forms.out import IAREQUIRED
from forms.out import IASCHA
from forms.out import IAWCONTLIMIT
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def AGI20_Calculation():
    return max_value(0, c_dollar(get_float(IAWCONTLIMIT.CYAGI) * 0.2))

def AGI30_Calculation():
    return max_value(0, c_dollar(get_float(IAWCONTLIMIT.CYAGI) * 0.3))

def AGI50_Calculation():
    return max_value(0, c_dollar(get_float(IAWCONTLIMIT.CYAGI) * 0.5))

def AGI100_Calculation():
    return max_value(0, c_dollar(get_float(IAWCONTLIMIT.CYAGI) * 1))

def CY20After_Calculation():
    return get_currency(IAWCONTLIMIT.DedCY20) + get_currency(IAWCONTLIMIT.DedPY20)

def CY20Lim_Calculation():
    return get_currency(USWContLimit.CY20Lim)

def CY30After_Calculation():
    return get_currency(IAWCONTLIMIT.DedCY30) + get_currency(IAWCONTLIMIT.DedPY30)

def CY30AfterCG_Calculation():
    return get_currency(IAWCONTLIMIT.DedCY30CG) + get_currency(IAWCONTLIMIT.DedPY30CG)

def CY30Lim_Calculation():
    return get_currency(USWContLimit.CY30Lim)

def CY30LimCG_Calculation():
    return get_currency(USWContLimit.CY30LimCG)

def CY50After_Calculation():
    return get_currency(IAWCONTLIMIT.DedCY50) + get_currency(IAWCONTLIMIT.DedPY50)

def CY50Lim_Calculation():
    return max_value(0, get_currency(IAWCONTLIMIT.CYTot) - get_currency(IAWCONTLIMIT.CY30Lim) - get_currency(IAWCONTLIMIT.CY30LimCG) - get_currency(IAWCONTLIMIT.CY20Lim) - get_currency(IAWCONTLIMIT.CYNoLim) - get_currency(IAWCONTLIMIT.CYQualLim))

def CYAGI_Calculation():
    return get_currency(IASCHA.IAAGI)

def CYNoLim_Calculation():
    return get_currency(USWContLimit.CYNoLim)

def CYNoLimit2_Calculation():
    return get_currency(IAWCONTLIMIT.DedCY100) + get_currency(IAWCONTLIMIT.DedPY100)

def CYQualAfter_Calculation():
    Contributions = Currency()
    Contributions = min_value(get_currency(IAWCONTLIMIT.CYQualLim), get_currency(IAWCONTLIMIT.CYAGI) - get_currency(IAWCONTLIMIT.CY50After) - get_currency(IAWCONTLIMIT.CY30After) - get_currency(IAWCONTLIMIT.CY30AfterCG) - get_currency(IAWCONTLIMIT.CY20After) - get_currency(IAWCONTLIMIT.CYNoLimit2))
    return max_value(0, Contributions)

def CYTot_Calculation():
    return get_currency(IASCHA.Contrib) + get_currency(IASCHA.Gifts)

def CYTotAfter_Calculation():
    return get_currency(IAWCONTLIMIT.CY50After) + get_currency(IAWCONTLIMIT.CY30After) + get_currency(IAWCONTLIMIT.CY30AfterCG) + get_currency(IAWCONTLIMIT.CY20After) + get_currency(IAWCONTLIMIT.CYNoLimit2) + get_currency(IAWCONTLIMIT.CYQualAfter)

def DedCY20_Calculation():
    Rem20 = Currency()

    Rem30 = Currency()

    Rem30CG = Currency()

    Rem50 = Currency()

    Min2 = Currency()

    Min3 = Currency()
    #per pub 526 limited to lesser of 20% of AGI, or 30% of AGI minus 30% contributions or 50% of AGI minus 50% contributions
    Rem20 = max_value(0, min_value(get_currency(IAWCONTLIMIT.AGI20), get_currency(IAWCONTLIMIT.CY20Lim)))
    Rem30 = max_value(0, get_currency(IAWCONTLIMIT.AGI30) - get_currency(IAWCONTLIMIT.Tot30Cont))
    Rem30CG = max_value(0, get_currency(IAWCONTLIMIT.AGI30) - get_currency(IAWCONTLIMIT.Tot30ContCG))
    Rem50 = max_value(0, get_currency(IAWCONTLIMIT.AGI50) - get_currency(IAWCONTLIMIT.Tot50Cont) - get_currency(IAWCONTLIMIT.Tot30ContCG) - get_currency(IAWCONTLIMIT.Tot30Cont))
    Min2 = min_value(Rem20, Rem30)
    Min3 = min_value(Min2, Rem30CG)
    return max_value(0, min_value(Min3, Rem50))

def DedCY30_Calculation():
    Rem30 = Currency()

    Rem50 = Currency()

    Thirty = Currency()
    Rem30 = max_value(0, min_value(get_currency(IAWCONTLIMIT.AGI30), get_currency(IAWCONTLIMIT.CY30Lim)))
    Rem50 = max_value(0, get_currency(IAWCONTLIMIT.AGI50) - get_currency(IAWCONTLIMIT.Tot50Cont) - get_currency(IAWCONTLIMIT.Tot30ContCG))
    return max_value(0, min_value(Rem30, Rem50))

def DedCY30CG_Calculation():
    Rem30 = Currency()
    Rem30 = max_value(0, min_value(get_currency(IAWCONTLIMIT.AGI30), get_currency(IAWCONTLIMIT.CY30LimCG)))
    return max_value(0, min_value(Rem30, get_currency(IAWCONTLIMIT.AGI50) - get_currency(IAWCONTLIMIT.Tot50Cont)))

def DedCY50_Calculation():
    return min_value(get_currency(IAWCONTLIMIT.CY50Lim), get_currency(IAWCONTLIMIT.AGI50))

def DedCY100_Calculation():
    Rem100 = Currency()

    Hundred = Currency()
    Rem100 = max_value(0, min_value(get_currency(IAWCONTLIMIT.AGI100), get_currency(IAWCONTLIMIT.CYNoLim)))
    Hundred = max_value(0, min_value(Rem100, get_currency(IAWCONTLIMIT.AGI100) - get_currency(IAWCONTLIMIT.Tot50Cont) - get_currency(IAWCONTLIMIT.Tot30ContCG) - get_currency(IAWCONTLIMIT.Tot30Cont) - get_currency(IAWCONTLIMIT.Tot20Cont)))
    return max_value(0, min_value(Rem100, Hundred))

def DedPY20_Calculation():
    Rem20 = Currency()

    Rem30CG = Currency()

    Rem30 = Currency()

    Rem50 = Currency()

    Min2 = Currency()

    Min3 = Currency()

    Min4 = Currency()

    Twenty = Currency()
    Rem20 = max_value(0, min_value(get_currency(IAWCONTLIMIT.AGI20), get_currency(IAWCONTLIMIT.PY20Lim)))
    Rem30CG = max_value(0, get_currency(IAWCONTLIMIT.AGI30) - get_currency(IAWCONTLIMIT.Tot30ContCG) - get_currency(IAWCONTLIMIT.DedCY20))
    Rem30 = max_value(0, get_currency(IAWCONTLIMIT.AGI30) - get_currency(IAWCONTLIMIT.Tot30Cont) - get_currency(IAWCONTLIMIT.DedCY20))
    Rem50 = max_value(0, get_currency(IAWCONTLIMIT.AGI50) - get_currency(IAWCONTLIMIT.Tot50Cont) - get_currency(IAWCONTLIMIT.Tot30ContCG) - get_currency(IAWCONTLIMIT.Tot30Cont) - get_currency(IAWCONTLIMIT.DedCY20))
    Twenty = max_value(0, get_currency(IAWCONTLIMIT.AGI20) - get_currency(IAWCONTLIMIT.DedCY20))
    Min2 = min_value(Rem20, Rem30CG)
    Min3 = min_value(Rem30, Rem50)
    Min4 = min_value(Min2, Twenty)
    return max_value(0, min_value(Min3, Min4))

def DedPY30_Calculation():
    Rem30 = Currency()

    Tot30 = Currency()

    Thirty = Currency()
    Rem30 = max_value(0, min_value(get_currency(IAWCONTLIMIT.AGI30), get_currency(IAWCONTLIMIT.PY30Lim)))
    Tot30 = max_value(0, get_currency(IAWCONTLIMIT.AGI30) - get_currency(IAWCONTLIMIT.CY30Lim))
    Thirty = max_value(0, min_value(Rem30, get_currency(IAWCONTLIMIT.AGI50) - get_currency(IAWCONTLIMIT.Tot50Cont) - get_currency(IAWCONTLIMIT.Tot30ContCG) - get_currency(IAWCONTLIMIT.DedCY30)))
    return min_value(Thirty, Tot30)

def DedPY30CG_Calculation():
    Rem30CG = Currency()

    Rem50 = Currency()

    Min2 = Currency()

    ThirtyCG = Currency()
    Rem30CG = max_value(0, min_value(get_currency(IAWCONTLIMIT.AGI30), get_currency(IAWCONTLIMIT.PY30LimCG)))
    Rem50 = max_value(0, get_currency(IAWCONTLIMIT.AGI50) - get_currency(IAWCONTLIMIT.Tot50Cont) - get_currency(IAWCONTLIMIT.DedCY30CG))
    ThirtyCG = max_value(0, get_currency(IAWCONTLIMIT.AGI30) - get_currency(IAWCONTLIMIT.DedCY30CG))
    Min2 = min_value(Rem30CG, Rem50)
    return max_value(0, min_value(Min2, ThirtyCG))

def DedPY50_Calculation():
    Rem50 = Currency()
    Rem50 = max_value(0, min_value(get_currency(IAWCONTLIMIT.AGI50), get_currency(IAWCONTLIMIT.PY50Lim)))
    return max_value(0, min_value(Rem50, get_currency(IAWCONTLIMIT.AGI50) - get_currency(IAWCONTLIMIT.DedCY50)))

def DedPY100_Calculation():
    Hundred = Currency()

    Rem100 = Currency()
    Rem100 = max_value(0, min_value(get_currency(IAWCONTLIMIT.AGI100), get_currency(IAWCONTLIMIT.PYNoLim)))
    Hundred = max_value(0, min_value(Rem100, get_currency(IAWCONTLIMIT.AGI100) - get_currency(IAWCONTLIMIT.Tot50Cont) - get_currency(IAWCONTLIMIT.Tot30ContCG) - get_currency(IAWCONTLIMIT.Tot30Cont) - get_currency(IAWCONTLIMIT.Tot20Cont) - get_currency(IAWCONTLIMIT.DedCY100)))
    return max_value(0, min_value(Rem100, Hundred))

def Desc_Calculation():
    return 'Contribution Limitation Worksheet'

def Exist_Calculation():
    return 1

def Names_Calculation():
    return get_string(IAREQUIRED.CombNames)

def NY20Lim_Calculation():
    return max_value(0, get_currency(IAWCONTLIMIT.Tot20Cont) - get_currency(IAWCONTLIMIT.CY20After))

def NY30Lim_Calculation():
    return max_value(0, get_currency(IAWCONTLIMIT.Tot30Cont) - get_currency(IAWCONTLIMIT.CY30After))

def NY30LimCG_Calculation():
    return max_value(0, get_currency(IAWCONTLIMIT.Tot30ContCG) - get_currency(IAWCONTLIMIT.CY30AfterCG))

def NY50Lim_Calculation():
    return max_value(0, get_currency(IAWCONTLIMIT.Tot50Cont) - get_currency(IAWCONTLIMIT.CY50After))

def NYNoLim_Calculation():
    return max_value(0, get_currency(IAWCONTLIMIT.Tot100Cont) - get_currency(IAWCONTLIMIT.CYNoLimit2))

def NYQualLim_Calculation():
    return max_value(0, get_currency(IAWCONTLIMIT.TotQualCont) - get_currency(IAWCONTLIMIT.CYQualAfter))

def NYTot_Calculation():
    return get_currency(IAWCONTLIMIT.NY50Lim) + get_currency(IAWCONTLIMIT.NY30Lim) + get_currency(IAWCONTLIMIT.NY30LimCG) + get_currency(IAWCONTLIMIT.NY20Lim) + get_currency(IAWCONTLIMIT.NYNoLim) + get_currency(IAWCONTLIMIT.NYQualLim)

def PY20Lim_Calculation():
    return get_currency(USWContLimit.PY20Lim)

def PY30Lim_Calculation():
    return get_currency(USWContLimit.PY30Lim)

def PY30LimCG_Calculation():
    return get_currency(USWContLimit.PY30LimCG)

def PY50Lim_Calculation():
    return get_currency(USWContLimit.PY50Lim)

def PYNoLim_Calculation():
    return get_currency(USWContLimit.PYNoLim)

def PYTot_Calculation():
    return get_currency(IAWCONTLIMIT.PY50Lim) + get_currency(IAWCONTLIMIT.PY30Lim) + get_currency(IAWCONTLIMIT.PY30LimCG) + get_currency(IAWCONTLIMIT.PY20Lim) + get_currency(IAWCONTLIMIT.PYNoLim)

def SSN_Calculation():
    return get_string(IAF1040.SSN)

def Tot20Cont_Calculation():
    return get_currency(IAWCONTLIMIT.PY20Lim) + get_currency(IAWCONTLIMIT.CY20Lim)

def Tot30Cont_Calculation():
    return get_currency(IAWCONTLIMIT.PY30Lim) + get_currency(IAWCONTLIMIT.CY30Lim)

def Tot30ContCG_Calculation():
    return get_currency(IAWCONTLIMIT.PY30LimCG) + get_currency(IAWCONTLIMIT.CY30LimCG)

def Tot50Cont_Calculation():
    return get_currency(IAWCONTLIMIT.PY50Lim) + get_currency(IAWCONTLIMIT.CY50Lim)

def Tot100Cont_Calculation():
    return get_currency(IAWCONTLIMIT.PYNoLim) + get_currency(IAWCONTLIMIT.CYNoLim)

def TotCont_Calculation():
    return get_currency(IAWCONTLIMIT.PYTot) + get_currency(IAWCONTLIMIT.CYTot)

def TotQualCont_Calculation():
    return get_currency(IAWCONTLIMIT.CYQualLim)


