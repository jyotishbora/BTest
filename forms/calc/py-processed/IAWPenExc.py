from forms.out import IAF1040
from forms.out import IAF126
from forms.out import IAREQUIRED
from forms.out import IAWPENEXC
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Description_Calculation():
    Total = Currency()
    Total = get_currency(IAWPENEXC.TPPenExc) + get_currency(IAWPENEXC.SPPenExc)
    return CStr(Total)

def Eligible_Calculation():
    if IAFS() == 2 or IAFS() == 3:
        if get_bool(IAWPENEXC.ExTP) == True or get_bool(IAWPENEXC.ExSp) == True:
            return 1
        else:
            return 0
    elif get_bool(IAWPENEXC.ExTP) == True:
        return 1
    else:
        return 0

def ExSp_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        if get_number(USWBasicInfo.SPAgeRec) > 54:
            return 1
        else:
            return 0
    else:
        return 0

def ExTP_Calculation():
    if get_number(USWBasicInfo.TPAgeRec) > 54:
        return 1
    else:
        return 0

def MaxExc_Calculation():
    if get_bool(IAWPENEXC.Eligible) == True:
        if IAFS() == 4:
            if get_currency(IAF1040.SpPenExcl) == 0 and get_bool(IAF1040.NoSpPenExcl) == True:
                return Decimal("12000")
            elif get_currency(IAF1040.SpPenExcl) > 0:
                return max_value(0, Decimal("12000") - get_currency(IAF1040.SpPenExcl))
            else:
                return Decimal("6000")
        elif IAFS() == 2 or IAFS() == 3:
            return Decimal("12000")
        else:
            return Decimal("6000")
    else:
        return 0

def MinExc_Calculation():
    return min_value(get_currency(IAWPENEXC.TotRetire), get_currency(IAWPENEXC.MaxExc))

def MobDisQual_Calculation():
    if get_currency(IAWPENEXC.TPPenExc) + get_currency(IAWPENEXC.SPPenExc) > 0:
        return 1
    else:
        return 0

def Names_Calculation():
    return get_string(IAREQUIRED.CombNames)

def NREligible_Calculation():
    if IAFS() == 2 or IAFS() == 3:
        if get_bool(IAWPENEXC.NRExTP) == True or get_bool(IAWPENEXC.NRExSp) == True:
            return 1
        else:
            return 0
    elif get_bool(IAWPENEXC.NRExTP) == True:
        return 1
    else:
        return 0

def NRExSp_Calculation():
    if get_bool(IAF126.SpPYRes) == True and get_bool(IAWPENEXC.ExSp) == True:
        return 1
    else:
        return 0

def NRExTP_Calculation():
    if get_bool(IAF126.TpPYRes) == True and get_bool(IAWPENEXC.ExTP) == True:
        return 1
    else:
        return 0

def NRMaxExc_Calculation():
    if get_bool(IAWPENEXC.NREligible) == True:
        return get_currency(IAWPENEXC.MaxExc)
    else:
        return 0

def NRMinExc_Calculation():
    return min_value(get_currency(IAWPENEXC.NRTotRetire), get_currency(IAWPENEXC.NRMaxExc))

def NRSPIRA_Calculation():
    if get_bool(IAF126.SpPYRes) == True:
        return get_currency(IAWPENEXC.SPIRA)
    else:
        return 0

def NRSPPenExc_Calculation():
    return max_value(0, get_currency(IAWPENEXC.NRMinExc) - get_currency(IAWPENEXC.NRTPPenExc))

def NRSPPensions_Calculation():
    if get_bool(IAF126.SpPYRes) == True:
        return get_currency(IAWPENEXC.SPPensions)
    else:
        return 0

def NRSPRatio_Calculation():
    if get_currency(IAWPENEXC.NRTotRetire) == 0:
        return 0
    elif get_bool(IAF126.SpPYRes) == True:
        return max_value(0, 1 - get_float(IAWPENEXC.NRTPRatio))
    else:
        return 0

def NRSPRetire_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True and get_bool(IAWPENEXC.NRExSp) == True:
        return get_currency(IAWPENEXC.NRSPIRA) + get_currency(IAWPENEXC.NRSPPensions)
    else:
        return 0

def NRTotRetire_Calculation():
    return get_currency(IAWPENEXC.NRTPRetire) + get_currency(IAWPENEXC.NRSPRetire)

def NRTPIRA_Calculation():
    if get_bool(IAF126.TpPYRes) == True:
        return get_currency(IAWPENEXC.TPIRA)
    else:
        return 0

def NRTPPenExc_Calculation():
    return c_dollar(get_float(IAWPENEXC.NRMinExc) * get_float(IAWPENEXC.NRTPRatio))

def NRTPPensions_Calculation():
    if get_bool(IAF126.TpPYRes) == True:
        return get_currency(IAWPENEXC.TPPensions)
    else:
        return 0

def NRTPRatio_Calculation():
    if get_currency(IAWPENEXC.NRTotRetire) == 0:
        return 0
    else:
        return min_value(1, get_float(IAWPENEXC.NRTPRetire) / get_float(IAWPENEXC.NRTotRetire))

def NRTPRetire_Calculation():
    if get_bool(IAWPENEXC.NRExTP) == True:
        return get_currency(IAWPENEXC.NRTPIRA) + get_currency(IAWPENEXC.NRTPPensions)
    else:
        return 0

def SPIRA_Calculation():
    #See Expanded instructions on Iowa website for 'Taxable IRA Distributions Step 5 Gross Income'. In 2016 QCD was to be added back to IA income and then were allowed a deduction on line 21
    #For 2018 the expanded instructions say Iowa has conformed, no addback needed
    #Extender: + get_currency(USWRetirement.SPAddQCD)
    return get_currency(USWRec.SIRAInc)

def SPMilPen_Calculation():
    Count1 = Long()

    MilPen = Currency()
    Count1 = 1
    MilPen = 0
    while Count1 <= GetAllCopies(USD1099R):
        if get_bool(USD1099R.MilPen, Count1) == True and get_bool(USD1099R.Spouse, Count1) == True:
            MilPen = MilPen + Round(get_currency(USD1099R.PenTax, Count1))
        else:
            MilPen = MilPen
        Count1 = Count1 + 1
    return Round(MilPen)

def SPName_Calculation():
    return get_string(USWBasicInfo.SPCommon)

def SPName2_Calculation():
    return get_string(USWBasicInfo.SPCommon)

def SPPenExc_Calculation():
    return max_value(0, get_currency(IAWPENEXC.MinExc) - get_currency(IAWPENEXC.TPPenExc))

def SPPensions_Calculation():
    return max_value(0, get_currency(USWRec.SPension) - get_currency(IAWPENEXC.SPMilPen) - Round(get_currency(USDRRB1099R.PenTax, FieldCopies(USDRRB1099R.Spouse))))

def SPRatio_Calculation():
    if get_currency(IAWPENEXC.TotRetire) == 0:
        return 0
    else:
        return max_value(0, 1 - get_float(IAWPENEXC.TPRatio))

def SPRetire_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True and get_bool(IAWPENEXC.ExSp) == True:
        return get_currency(IAWPENEXC.SPIRA) + get_currency(IAWPENEXC.SPPensions)
    else:
        return 0

def SSN_Calculation():
    return get_string(IAF1040.SSN)

def TotRetire_Calculation():
    return get_currency(IAWPENEXC.TPRetire) + get_currency(IAWPENEXC.SPRetire)

def TPIRA_Calculation():
    #See Expanded instructions on Iowa website for 'Taxable IRA Distributions Step 5 Gross Income'. In 2016 QCD was to be added back to IA income and then were allowed a deduction on line 21
    #For 2018 the expanded instructions say Iowa has conformed, no addback needed
    #Extender: + get_currency(USWRetirement.TPAddQCD)
    return get_currency(USWRec.TIRAInc)

def TPMilPen_Calculation():
    Count1 = Long()

    MilPen = Currency()
    Count1 = 1
    MilPen = 0
    while Count1 <= GetAllCopies(USD1099R):
        if get_bool(USD1099R.MilPen, Count1) == True and get_bool(USD1099R.Taxpayer, Count1) == True:
            MilPen = MilPen + Round(get_currency(USD1099R.PenTax, Count1))
        else:
            MilPen = MilPen
        Count1 = Count1 + 1
    return Round(MilPen)

def TPName_Calculation():
    return get_string(USWBasicInfo.TPCommon)

def TPName2_Calculation():
    return get_string(USWBasicInfo.TPCommon)

def TPPenExc_Calculation():
    return c_dollar(get_float(IAWPENEXC.MinExc) * get_float(IAWPENEXC.TPRatio))

def TPPensions_Calculation():
    return max_value(0, get_currency(USWRec.TPension) - get_currency(IAWPENEXC.TPMilPen) - Round(get_currency(USDRRB1099R.PenTax, FieldCopies(USDRRB1099R.Taxpayer))))

def TPRatio_Calculation():
    if get_currency(IAWPENEXC.TotRetire) == 0:
        return 0
    else:
        return min_value(1, get_float(IAWPENEXC.TPRetire) / get_float(IAWPENEXC.TotRetire))

def TPRetire_Calculation():
    if get_bool(IAWPENEXC.ExTP) == True:
        return get_currency(IAWPENEXC.TPIRA) + get_currency(IAWPENEXC.TPPensions)
    else:
        return 0


