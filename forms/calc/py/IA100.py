from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Common_Calculation():
    if GetBool(IAF1040.MFJ) == True:
        ReturnVal = GetString(USWBasicInfo.CombFirst)
    else:
        ReturnVal = GetString(USWBasicInfo.TPCommon)

def MEF100SP_Calculation():
    if GetBool(IA100.Spouse) == True and GetBool(IA100.Print) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

def MEF100TP_Calculation():
    if GetBool(IA100.Taxpayer) == True and GetBool(IA100.Print) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Names_Calculation():
    if GetBool(IA100.Spouse) == True:
        ReturnVal = GetString(IARequired.SPCombName)
    else:
        ReturnVal = GetString(IARequired.TPCombName)

def P2Gain_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA100.P2SalesPx) - GetCurrency(IA100.P2Cost))

def P2TPSharePerc_Calculation():
    ReturnVal = GetFloat(IA100.P2TPShare) * 100

def Print_Calculation():
    if GetCurrency(IA100.P6CGD) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def SpouseCommon_Calculation():
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetString(USWBasicInfo.SPCommon)
    else:
        ReturnVal = 'Not Applicable'

def SSN_Calculation():
    if GetBool(IA100.Spouse) == True:
        ReturnVal = GetString(IAF1040.SpouseSSN)
    else:
        ReturnVal = GetString(IAF1040.SSN)

