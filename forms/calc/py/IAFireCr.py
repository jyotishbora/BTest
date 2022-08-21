from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Description_Calculation():
    Total = Currency()
    Total = GetCurrency(IAFireCr.SPTotCr) + GetCurrency(IAFireCr.TPTotCr)
    ReturnVal = CStr(Total)

def MobDisQual_Calculation():
    if GetCurrency(IAFireCr.SPTotCr) + GetCurrency(IAFireCr.TPTotCr) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Names_Calculation():
    ReturnVal = GetString(IARequired.CombNames)

def SPName_Calculation():
    ReturnVal = GetString(USWBasicInfo.SPCommon)

def SPTotCr_Calculation():
    # updated for 2018
    if GetBool(IAFireCr.SPQual) == True and GetBool(IARequired.AskSpouse) == True:
        ReturnVal = MinValue(Decimal("100"), CDollar(GetFloat(IAFireCr.SPMonths) * 834))
    else:
        ReturnVal = 0

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

def TPName_Calculation():
    ReturnVal = GetString(USWBasicInfo.TPCommon)

def TPTotCr_Calculation():
    # updated for 2018
    if GetBool(IAFireCr.TPQual) == True:
        ReturnVal = MinValue(Decimal("100"), CDollar(GetFloat(IAFireCr.TPMonths) * 834))
    else:
        ReturnVal = 0

