from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Description_Calculation():
    Total = Currency()
    Total = GetCurrency(IAAddFedTax.TPTotal) + GetCurrency(IAAddFedTax.SPTotal)
    ReturnVal = CStr(Total)

def Exist_Calculation():
    ReturnVal = 1

def Names_Calculation():
    ReturnVal = GetString(IARequired.CombNames)

def NetDue_Calculation():
    if GetCurrency(USZIA1040.IAPYNetIncB) == 0 and GetCurrency(USZIA1040.IAPYNetIncA) == 0:
        ReturnVal = 0
    else:
        ReturnVal = MaxValue(0, GetCurrency(IAAddFedTax.PyDue) - GetCurrency(IAAddFedTax.PYPen))

def PyDue_Calculation():
    if GetBool(USWSpouse.NonRes) == True:
        ReturnVal = GetCurrency(USWRec.PYOweNR)
    else:
        ReturnVal = GetCurrency(USWRec.PYOwe)

def PYExt_Calculation():
    if GetBool(USWSpouse.NonRes) == True:
        ReturnVal = GetCurrency(USWRec.PYExtNR)
    else:
        ReturnVal = GetCurrency(USWRec.PYExt)

def PYPen_Calculation():
    if GetBool(USWSpouse.NonRes) == True:
        ReturnVal = GetCurrency(USWRec.PYPenaltyNR)
    else:
        ReturnVal = GetCurrency(USWRec.PYPenalty)

def SPBalDue_Calculation():
    ReturnVal = CDollar(GetFloat(IARequired.PYRatio) * GetFloat(IAAddFedTax.NetDue))

def SPExcFICA_Calculation():
    ReturnVal = GetCurrency(USWFICA.SCredit)

def SPExt_Calculation():
    ReturnVal = CDollar(GetFloat(IARequired.PYRatio) * GetFloat(IAAddFedTax.PYExt))

def SPName_Calculation():
    ReturnVal = GetString(USWBasicInfo.SPCommon)

def SPTotal_Calculation():
    ReturnVal = GetCurrency(IAAddFedTax.SPBalDue) + GetCurrency(IAAddFedTax.SPExt) + GetCurrency(IAAddFedTax.SPFuel) + GetCurrency(IAAddFedTax.SPExcFICA)

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

def TPBalDue_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAAddFedTax.NetDue) - GetCurrency(IAAddFedTax.SPBalDue))

def TPExcFICA_Calculation():
    ReturnVal = GetCurrency(USWFICA.TCredit)

def TPExt_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAAddFedTax.PYExt) - GetCurrency(IAAddFedTax.SPExt))

def TPFuel_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(USF4136.TotalCredit) - GetCurrency(IAAddFedTax.SPFuel))

def TPName_Calculation():
    ReturnVal = GetString(USWBasicInfo.TPCommon)

def TPTotal_Calculation():
    ReturnVal = GetCurrency(IAAddFedTax.TPBalDue) + GetCurrency(IAAddFedTax.TPExt) + GetCurrency(IAAddFedTax.TPFuel) + GetCurrency(IAAddFedTax.TPExcFICA)

