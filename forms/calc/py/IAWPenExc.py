from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Description_Calculation():
    Total = Currency()
    Total = GetCurrency(IAWPenExc.TPPenExc) + GetCurrency(IAWPenExc.SPPenExc)
    ReturnVal = CStr(Total)

def Eligible_Calculation():
    if IAFS() == 2 or IAFS() == 3:
        if GetBool(IAWPenExc.ExTP) == True or GetBool(IAWPenExc.ExSp) == True:
            ReturnVal = 1
        else:
            ReturnVal = 0
    elif GetBool(IAWPenExc.ExTP) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

def ExSp_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        if GetNumber(USWBasicInfo.SPAgeRec) > 54:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def ExTP_Calculation():
    if GetNumber(USWBasicInfo.TPAgeRec) > 54:
        ReturnVal = 1
    else:
        ReturnVal = 0

def MaxExc_Calculation():
    if GetBool(IAWPenExc.Eligible) == True:
        if IAFS() == 4:
            if GetCurrency(IAF1040.SpPenExcl) == 0 and GetBool(IAF1040.NoSpPenExcl) == True:
                ReturnVal = Decimal("12000")
            elif GetCurrency(IAF1040.SpPenExcl) > 0:
                ReturnVal = MaxValue(0, Decimal("12000") - GetCurrency(IAF1040.SpPenExcl))
            else:
                ReturnVal = Decimal("6000")
        elif IAFS() == 2 or IAFS() == 3:
            ReturnVal = Decimal("12000")
        else:
            ReturnVal = Decimal("6000")
    else:
        ReturnVal = 0

def MinExc_Calculation():
    ReturnVal = MinValue(GetCurrency(IAWPenExc.TotRetire), GetCurrency(IAWPenExc.MaxExc))

def MobDisQual_Calculation():
    if GetCurrency(IAWPenExc.TPPenExc) + GetCurrency(IAWPenExc.SPPenExc) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Names_Calculation():
    ReturnVal = GetString(IARequired.CombNames)

def NREligible_Calculation():
    if IAFS() == 2 or IAFS() == 3:
        if GetBool(IAWPenExc.NRExTP) == True or GetBool(IAWPenExc.NRExSp) == True:
            ReturnVal = 1
        else:
            ReturnVal = 0
    elif GetBool(IAWPenExc.NRExTP) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

def NRExSp_Calculation():
    if GetBool(IAF126.SpPYRes) == True and GetBool(IAWPenExc.ExSp) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

def NRExTP_Calculation():
    if GetBool(IAF126.TpPYRes) == True and GetBool(IAWPenExc.ExTP) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

def NRMaxExc_Calculation():
    if GetBool(IAWPenExc.NREligible) == True:
        ReturnVal = GetCurrency(IAWPenExc.MaxExc)
    else:
        ReturnVal = 0

def NRMinExc_Calculation():
    ReturnVal = MinValue(GetCurrency(IAWPenExc.NRTotRetire), GetCurrency(IAWPenExc.NRMaxExc))

def NRSPIRA_Calculation():
    if GetBool(IAF126.SpPYRes) == True:
        ReturnVal = GetCurrency(IAWPenExc.SPIRA)
    else:
        ReturnVal = 0

def NRSPPenExc_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWPenExc.NRMinExc) - GetCurrency(IAWPenExc.NRTPPenExc))

def NRSPPensions_Calculation():
    if GetBool(IAF126.SpPYRes) == True:
        ReturnVal = GetCurrency(IAWPenExc.SPPensions)
    else:
        ReturnVal = 0

def NRSPRatio_Calculation():
    if GetCurrency(IAWPenExc.NRTotRetire) == 0:
        ReturnVal = 0
    elif GetBool(IAF126.SpPYRes) == True:
        ReturnVal = MaxValue(0, 1 - GetFloat(IAWPenExc.NRTPRatio))
    else:
        ReturnVal = 0

def NRSPRetire_Calculation():
    if GetBool(IARequired.AskSpouse) == True and GetBool(IAWPenExc.NRExSp) == True:
        ReturnVal = GetCurrency(IAWPenExc.NRSPIRA) + GetCurrency(IAWPenExc.NRSPPensions)
    else:
        ReturnVal = 0

def NRTotRetire_Calculation():
    ReturnVal = GetCurrency(IAWPenExc.NRTPRetire) + GetCurrency(IAWPenExc.NRSPRetire)

def NRTPIRA_Calculation():
    if GetBool(IAF126.TpPYRes) == True:
        ReturnVal = GetCurrency(IAWPenExc.TPIRA)
    else:
        ReturnVal = 0

def NRTPPenExc_Calculation():
    ReturnVal = CDollar(GetFloat(IAWPenExc.NRMinExc) * GetFloat(IAWPenExc.NRTPRatio))

def NRTPPensions_Calculation():
    if GetBool(IAF126.TpPYRes) == True:
        ReturnVal = GetCurrency(IAWPenExc.TPPensions)
    else:
        ReturnVal = 0

def NRTPRatio_Calculation():
    if GetCurrency(IAWPenExc.NRTotRetire) == 0:
        ReturnVal = 0
    else:
        ReturnVal = MinValue(1, GetFloat(IAWPenExc.NRTPRetire) / GetFloat(IAWPenExc.NRTotRetire))

def NRTPRetire_Calculation():
    if GetBool(IAWPenExc.NRExTP) == True:
        ReturnVal = GetCurrency(IAWPenExc.NRTPIRA) + GetCurrency(IAWPenExc.NRTPPensions)
    else:
        ReturnVal = 0

def SPIRA_Calculation():
    #See Expanded instructions on Iowa website for 'Taxable IRA Distributions Step 5 Gross Income'. In 2016 QCD was to be added back to IA income and then were allowed a deduction on line 21
    #For 2018 the expanded instructions say Iowa has conformed, no addback needed
    #Extender: + GetCurrency(USWRetirement.SPAddQCD)
    ReturnVal = GetCurrency(USWRec.SIRAInc)

def SPMilPen_Calculation():
    Count1 = Long()

    MilPen = Currency()
    Count1 = 1
    MilPen = 0
    while Count1 <= GetAllCopies(USD1099R):
        if GetBool(USD1099R.MilPen, Count1) == True and GetBool(USD1099R.Spouse, Count1) == True:
            MilPen = MilPen + Round(GetCurrency(USD1099R.PenTax, Count1))
        else:
            MilPen = MilPen
        Count1 = Count1 + 1
    ReturnVal = Round(MilPen)

def SPName_Calculation():
    ReturnVal = GetString(USWBasicInfo.SPCommon)

def SPName2_Calculation():
    ReturnVal = GetString(USWBasicInfo.SPCommon)

def SPPenExc_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWPenExc.MinExc) - GetCurrency(IAWPenExc.TPPenExc))

def SPPensions_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(USWRec.SPension) - GetCurrency(IAWPenExc.SPMilPen) - Round(GetCurrency(USDRRB1099R.PenTax, FieldCopies(USDRRB1099R.Spouse))))

def SPRatio_Calculation():
    if GetCurrency(IAWPenExc.TotRetire) == 0:
        ReturnVal = 0
    else:
        ReturnVal = MaxValue(0, 1 - GetFloat(IAWPenExc.TPRatio))

def SPRetire_Calculation():
    if GetBool(IARequired.AskSpouse) == True and GetBool(IAWPenExc.ExSp) == True:
        ReturnVal = GetCurrency(IAWPenExc.SPIRA) + GetCurrency(IAWPenExc.SPPensions)
    else:
        ReturnVal = 0

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

def TotRetire_Calculation():
    ReturnVal = GetCurrency(IAWPenExc.TPRetire) + GetCurrency(IAWPenExc.SPRetire)

def TPIRA_Calculation():
    #See Expanded instructions on Iowa website for 'Taxable IRA Distributions Step 5 Gross Income'. In 2016 QCD was to be added back to IA income and then were allowed a deduction on line 21
    #For 2018 the expanded instructions say Iowa has conformed, no addback needed
    #Extender: + GetCurrency(USWRetirement.TPAddQCD)
    ReturnVal = GetCurrency(USWRec.TIRAInc)

def TPMilPen_Calculation():
    Count1 = Long()

    MilPen = Currency()
    Count1 = 1
    MilPen = 0
    while Count1 <= GetAllCopies(USD1099R):
        if GetBool(USD1099R.MilPen, Count1) == True and GetBool(USD1099R.Taxpayer, Count1) == True:
            MilPen = MilPen + Round(GetCurrency(USD1099R.PenTax, Count1))
        else:
            MilPen = MilPen
        Count1 = Count1 + 1
    ReturnVal = Round(MilPen)

def TPName_Calculation():
    ReturnVal = GetString(USWBasicInfo.TPCommon)

def TPName2_Calculation():
    ReturnVal = GetString(USWBasicInfo.TPCommon)

def TPPenExc_Calculation():
    ReturnVal = CDollar(GetFloat(IAWPenExc.MinExc) * GetFloat(IAWPenExc.TPRatio))

def TPPensions_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(USWRec.TPension) - GetCurrency(IAWPenExc.TPMilPen) - Round(GetCurrency(USDRRB1099R.PenTax, FieldCopies(USDRRB1099R.Taxpayer))))

def TPRatio_Calculation():
    if GetCurrency(IAWPenExc.TotRetire) == 0:
        ReturnVal = 0
    else:
        ReturnVal = MinValue(1, GetFloat(IAWPenExc.TPRetire) / GetFloat(IAWPenExc.TotRetire))

def TPRetire_Calculation():
    if GetBool(IAWPenExc.ExTP) == True:
        ReturnVal = GetCurrency(IAWPenExc.TPIRA) + GetCurrency(IAWPenExc.TPPensions)
    else:
        ReturnVal = 0

