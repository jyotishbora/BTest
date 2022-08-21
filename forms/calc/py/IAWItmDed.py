from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def AGI_Calculation():
    ReturnVal = GetCurrency(IASchA.IAAGI)

def AllowableDed2_Calculation():
    ReturnVal = GetCurrency(IAWItmDed.AllowableDed)

def AllowableDed_Calculation():
    ReturnVal = MaxValue(0, ( GetCurrency(IAWItmDed.IATotDed) - GetCurrency(IAWItmDed.Limit) ))

def Description_Calculation():
    ReturnVal = CStr(GetCurrency(IAWItmDed.LimitDed)) + ' Itemized Deductions'

def Divide_Calculation():
    if GetCurrency(IAWItmDed.Subtract2) == 0:
        ReturnVal = 0
    else:
        ReturnVal = Round(GetFloat(IAWItmDed.Subtract1) / GetFloat(IAWItmDed.Subtract2), 3)

def ExcInc_Calculation():
    ReturnVal = MaxValue(0, ( GetCurrency(IAWItmDed.AGI) - GetCurrency(IAWItmDed.IncLimit) ))

def IADedTax2_Calculation():
    ReturnVal = GetCurrency(IAWItmDed.IADedTax)

def IADedTax_Calculation():
    if GetBool(USWRec.ItmDdn) == True:
        if GetBool(USSchA.Income) == True or GetBool(USWResidency.F1040NR) == True:
            ReturnVal = MaxValue(0, GetCurrency(IASchA.IATax))
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def IATotDed2_Calculation():
    ReturnVal = GetCurrency(IAWItmDed.IATotDed)

def IATotDed_Calculation():
    ReturnVal = GetCurrency(IAWItmDed.TotDed) + GetCurrency(IAWItmDed.IADedTax)

def IncLimit_Calculation():
    # updated for 2018 - RJ
    if FedFS() == 1:
        ReturnVal = Decimal("266700")
    elif FedFS() == 3:
        ReturnVal = Decimal("160000")
    elif FedFS() == 4:
        ReturnVal = Decimal("293350")
    else:
        ReturnVal = Decimal("320000")

def Limit3_Calculation():
    ReturnVal = CDollar(GetFloat(IAWItmDed.ExcInc) * 0.03)

def Limit80_Calculation():
    ReturnVal = CDollar(GetFloat(IAWItmDed.PODed) * 0.8)

def Limit_Calculation():
    ReturnVal = MinValue(GetCurrency(IAWItmDed.Limit80), GetCurrency(IAWItmDed.Limit3))

def LimitDed_Calculation():
    ReturnVal = MaxValue(0, ( GetCurrency(IAWItmDed.AllowableDed2) - GetCurrency(IAWItmDed.Multiply) ))

def Multiply_Calculation():
    ReturnVal = CDollar(GetFloat(IAWItmDed.IADedTax2) * GetFloat(IAWItmDed.Divide))

def Names_Calculation():
    ReturnVal = GetString(IARequired.CombNames)

def No1_Calculation():
    if GetCurrency(IAWItmDed.NonPODed) < GetCurrency(IAWItmDed.IATotDed):
        ReturnVal = 0
    else:
        ReturnVal = 1

def No2_Calculation():
    if GetCurrency(IAWItmDed.IncLimit) < GetCurrency(IAWItmDed.AGI):
        ReturnVal = 0
    else:
        ReturnVal = 1

def NonPODed2_Calculation():
    ReturnVal = GetCurrency(IAWItmDed.NonPODed)

def NonPODed_Calculation():
    GamblingLoss = Currency()
    if GetBool(USWResidency.F1040NR) == True:
        GamblingLoss = 0
    else:
        GamblingLoss = GetCurrency(IAWSchAPrint.GamblingLoss)
    ReturnVal = GetCurrency(IASchA.MedDed) + GetCurrency(IASchA.Invest) + GetCurrency(IASchA.Theft) + GetCurrency(IAWSchAPrint.Form4684) + GamblingLoss

def PODed_Calculation():
    ReturnVal = MaxValue(0, ( GetCurrency(IAWItmDed.IATotDed) - GetCurrency(IAWItmDed.NonPODed) ))

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

def Subtract1_Calculation():
    ReturnVal = MaxValue(0, ( GetCurrency(IAWItmDed.AllowableDed2) - GetCurrency(IAWItmDed.NonPODed2) ))

def Subtract2_Calculation():
    ReturnVal = MaxValue(0, ( GetCurrency(IAWItmDed.IATotDed2) - GetCurrency(IAWItmDed.NonPODed2) ))

def TotDed_Calculation():
    ReturnVal = GetCurrency(IASchA.MedDed) + GetCurrency(IASchA.TaxPd) + GetCurrency(IASchA.TotInt) + GetCurrency(IASchA.TotGifts) + GetCurrency(IASchA.Theft) + GetCurrency(IASchA.AllowExp) + GetCurrency(IASchA.OthMisc)

def Yes1_Calculation():
    if GetBool(IAWItmDed.No1) == True:
        ReturnVal = 0
    else:
        ReturnVal = 1

def Yes2_Calculation():
    if GetBool(IAWItmDed.No2) == True:
        ReturnVal = 0
    else:
        ReturnVal = 1

