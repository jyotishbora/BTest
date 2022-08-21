from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def AMTInt_Calculation():
    if GetBool(USWResidency.F1040NR) == True:
        ReturnVal = 0
    elif GetBool(IAF1040.ItemCheck) == True:
        ReturnVal = MinValue(GetCurrency(IAW6251MortInt.TotMortInt), GetCurrency(IAW6251MortInt.MortInt98) + GetCurrency(IAW6251MortInt.RefinInt) + GetCurrency(IAW6251MortInt.OthInt))
    else:
        ReturnVal = 0

def Desc_Calculation():
    ReturnVal = CStr(GetCurrency(IAW6251MortInt.AMTInt))

def Exist_Calculation():
    ReturnVal = 1

def MortInt_Calculation():
    if GetBool(USWResidency.F1040NR) == True:
        ReturnVal = 0
    elif GetBool(IAF1040.ItemCheck) == True:
        ReturnVal = GetCurrency(IASchA.Mort)
    else:
        ReturnVal = 0

def MortInt98_Calculation():
    if GetBool(IAF1040.ItemCheck) == True:
        ReturnVal = GetCurrency(USD1098.StateAdj)
    else:
        ReturnVal = 0

def MtgePrem_Calculation():
    if GetBool(USWResidency.F1040NR) == True:
        ReturnVal = 0
    elif GetBool(IAF1040.ItemCheck) == True:
        ReturnVal = GetCurrency(IASchA.MtgePrem)
    else:
        ReturnVal = 0

def Names_Calculation():
    ReturnVal = GetString(IARequired.CombNames)

def Points_Calculation():
    if GetBool(USWResidency.F1040NR) == True:
        ReturnVal = 0
    elif GetBool(IAF1040.ItemCheck) == True:
        ReturnVal = GetCurrency(IASchA.PtsNot)
    else:
        ReturnVal = 0

def Sfm_Calculation():
    if GetBool(USWResidency.F1040NR) == True:
        ReturnVal = 0
    elif GetBool(IAF1040.ItemCheck) == True:
        ReturnVal = GetCurrency(IASchA.MortNot)
    else:
        ReturnVal = 0

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

def TotMortInt_Calculation():
    if GetBool(USWResidency.F1040NR) == True:
        ReturnVal = 0
    elif GetBool(IAF1040.ItemCheck) == True:
        ReturnVal = GetCurrency(IAW6251MortInt.MortInt) + GetCurrency(IAW6251MortInt.Sfm) + GetCurrency(IAW6251MortInt.Points) + GetCurrency(IAW6251MortInt.MtgePrem)
    else:
        ReturnVal = 0

