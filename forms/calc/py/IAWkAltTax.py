from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def ATax_Calculation():
    if GetNumber(IAWkAltTax.ProRate) == 1:
        ReturnVal = CDollar(GetFloat(IAWkAltTax.Lesser) * GetFloat(IAWkAltTax.BProRate))
    else:
        ReturnVal = 0

def BProRate_Calculation():
    if GetNumber(IAWkAltTax.ProRate) == 1:
        if GetCurrency(IAWkAltTax.SPModNI) < 0 and GetCurrency(IAWkAltTax.TPModNI) < 0:
            if GetCurrency(IAWkAltTax.TPModNI) < GetCurrency(IAWkAltTax.SPModNI):
                ReturnVal = 0
            else:
                ReturnVal = 1
        elif GetCurrency(IAWkAltTax.TPModNI) < 0:
            ReturnVal = 0
        elif GetCurrency(IAWkAltTax.TPModNI) > 0 and GetCurrency(IAWkAltTax.TotAdjIANetInc) <= 0:
            ReturnVal = 1
        elif GetCurrency(IAWkAltTax.TotAdjIANetInc) == 0:
            ReturnVal = 0
        else:
            ReturnVal = MaxValue(0, ( MinValue(1, Round(GetFloat(IAWkAltTax.TPModNI) / GetFloat(IAWkAltTax.TotAdjIANetInc), 3)) ))
    else:
        ReturnVal = 0

def BTax_Calculation():
    if GetNumber(IAWkAltTax.ProRate) == 1:
        ReturnVal = GetCurrency(IAWkAltTax.Lesser) - GetCurrency(IAWkAltTax.ATax)
    else:
        ReturnVal = 0

def Description_Calculation():
    ReturnVal = CStr(GetCurrency(IAWkAltTax.Lesser))

def IncLimit_Calculation():
    if GetBool(IAF1040.Over65) == True:
        ReturnVal = Decimal("32000")
    else:
        ReturnVal = Decimal("13500")

def Lesser_Calculation():
    if GetBool(IAWkAltTax.Qualify) == True:
        ReturnVal = MinValue(GetCurrency(IAWkAltTax.Mult), GetCurrency(IAWkAltTax.Tables))
    else:
        ReturnVal = GetCurrency(IAWkAltTax.Tables)

def Ln26_Calculation():
    ReturnVal = GetCurrency(IAWkAltTax.TotSPLine1) + GetCurrency(IAWkAltTax.TotLine1)

def LumpSum_Calculation():
    ReturnVal = GetCurrency(USF4972.TPCapGain) + GetCurrency(USF4972.TPTaxAmt)

def Mult_Calculation():
    ReturnVal = CDollar(GetFloat(IAWkAltTax.Sub1) * 0.0898)

def Names_Calculation():
    ReturnVal = GetString(IARequired.CombNames)

def NetInc_Calculation():
    ReturnVal = GetCurrency(IAF1040.ANet)

def PenExcl_Calculation():
    ReturnVal = GetCurrency(IAF1040.APenExcl)

def ProRate_Calculation():
    if IAFS() == 3 or IAFS() == 4:
        if ( GetCurrency(IAWkAltTax.Mult) < GetCurrency(IAWkAltTax.Tables) )  and GetBool(IAWkAltTax.Qualify) == True:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def Qualify_Calculation():
    NoMFSQual = Long()
    if GetCurrency(IAF1040.SpIncome) == 0 and GetBool(IAF1040.NoMFSInc) == False:
        NoMFSQual = 1
    else:
        NoMFSQual = 0
    if IAFS() == 1:
        ReturnVal = 0
    elif GetBool(IARequired.AskFilStat) == True and GetBool(IAWkAltTax.NOL) == True:
        ReturnVal = 0
    elif IAFS() == 4 and NoMFSQual == 1:
        ReturnVal = 0
    else:
        ReturnVal = 1

def SPLumpSum_Calculation():
    #probably should ask for the form 4972 amounts on the IA 1040 under the filing status 4 section, however for the number of users that will fall in this situation not going to add this year.
    if IAFS() == 4:
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(USF4972Spouse.TPCapGain) + GetCurrency(USF4972Spouse.TPTaxAmt)

def SPModNI_Calculation():
    if GetNumber(IAWkAltTax.ProRate) == 1:
        ReturnVal = GetCurrency(IAWkAltTax.TotSPLine1)
    else:
        ReturnVal = 0

def SPNetInc_Calculation():
    if IAFS() == 4:
        ReturnVal = GetCurrency(IAF1040.SpIncome)
    else:
        ReturnVal = GetCurrency(IAF1040.BNet)

def SPPenExcl_Calculation():
    if IAFS() == 4:
        ReturnVal = GetCurrency(IAF1040.SpPenExcl)
    else:
        ReturnVal = GetCurrency(IAF1040.BPenExcl)

def SPSSB_Calculation():
    if IAFS() == 4:
        ReturnVal = GetCurrency(IAF1040.SpSSB)
    else:
        ReturnVal = GetCurrency(IAF1040.BRepSSB)

def SSB_Calculation():
    ReturnVal = GetCurrency(IAF1040.ARepSSB)

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

def Sub1_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWkAltTax.Ln26) - GetCurrency(IAWkAltTax.IncLimit))

def Tables_Calculation():
    ReturnVal = GetCurrency(IAF1040.ARegTax) + GetCurrency(IAF1040.BRegTax)

def TotAdjIANetInc_Calculation():
    ReturnVal = GetCurrency(IAWkAltTax.SPModNI) + GetCurrency(IAWkAltTax.TPModNI)

def TotLine1_Calculation():
    ReturnVal = GetCurrency(IAWkAltTax.NetInc) + GetCurrency(IAWkAltTax.PenExcl) + GetCurrency(IAWkAltTax.SSB) + GetCurrency(IAWkAltTax.LumpSum)

def TotSPLine1_Calculation():
    ReturnVal = GetCurrency(IAWkAltTax.SPNetInc) + GetCurrency(IAWkAltTax.SPPenExcl) + GetCurrency(IAWkAltTax.SPSSB) + GetCurrency(IAWkAltTax.SPLumpSum)

def TPModNI_Calculation():
    if GetNumber(IAWkAltTax.ProRate) == 1:
        ReturnVal = GetCurrency(IAWkAltTax.TotLine1)
    else:
        ReturnVal = 0

