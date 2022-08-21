from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def AMTCR_Calculation():
    ReturnVal = MinValue(GetCurrency(IA8801Sp.MaxAMT), GetCurrency(IA8801Sp.CYRegTax))

def ApporRegTx_Calculation():
    ReturnVal = GetCurrency(IA8801Sp.CYTax) - GetCurrency(IA8801Sp.PYNRCr)

def CYAMT_Calculation():
    if GetBool(IAF1040.CombMFS) == False:
        ReturnVal = 0
    elif GetBool(IAF126.SpPYNR) == True:
        ReturnVal = MaxValue(0, CDollar(GetFloat(IA6251Sp.TentAMT) * GetFloat(IA6251Sp.PYNRRatio)))
    else:
        ReturnVal = GetCurrency(IA6251Sp.TentAMT)

def CYCarryforward_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA8801Sp.TotalPYAMT) - GetCurrency(IA8801Sp.AMTCR))

def CYRegTax_Calculation():
    if GetCurrency(IA8801Sp.ExcRegTax) == 0:
        ReturnVal = 0
    else:
        ReturnVal = MaxValue(0, GetCurrency(IA8801Sp.CYTax) - GetCurrency(IA8801Sp.TotCr))

def CYTax_Calculation():
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetCurrency(IAF1040.BAltTax)
    else:
        ReturnVal = 0

def Description_Calculation():
    Total = Currency()
    Total = GetCurrency(IA8801Sp.AMTCR)
    ReturnVal = CStr(Total) + ' Credit'

def EFile_Calculation():
    if GetCurrency(IA8801Sp.AMTCR) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def ExcRegTax_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA8801Sp.ApporRegTx) - GetCurrency(IA8801Sp.CYAMT))

def MaxAMT_Calculation():
    ReturnVal = MinValue(GetCurrency(IA8801Sp.TotalPYAMT), GetCurrency(IA8801Sp.ExcRegTax))

def Names_Calculation():
    ReturnVal = GetString(IARequired.SPCombName)

def Print_Calculation():
    if GetCurrency(IA8801Sp.AMTCR) > 0 or GetCurrency(IA8801Sp.CYCarryforward) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def PYAMT_Calculation():
    if GetBool(IAF1040.CombMFS) == False:
        ReturnVal = 0
    elif GetString(USZIA1040.IAPYFS) == GetString(IARequired.FilingStatus):
        ReturnVal = GetCurrency(USZIA1040.IAPYMinTaxB)
    else:
        ReturnVal = 0

def PYCarryforward_Calculation():
    ReturnVal = GetCurrency(USZIA1040.IAPY8801CFSp)

def PYNRCr_Calculation():
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetCurrency(IAF1040.BCrNon)
    else:
        ReturnVal = 0

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SpouseSSN)

def Sum148Cr_Calculation():
    if GetCurrency(IA8801Sp.ExcRegTax) == 0:
        ReturnVal = 0
    elif GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetCurrency(IA148Sp.TotNonRefNo8801)
    else:
        ReturnVal = 0

def SumCr_Calculation():
    if GetCurrency(IA8801Sp.ExcRegTax) == 0:
        ReturnVal = 0
    elif GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetCurrency(IAF1040.BCredits) + GetCurrency(IAF1040.BCrNon) + GetCurrency(IAF1040.BOutState)
    else:
        ReturnVal = 0

def TotalPYAMT_Calculation():
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetCurrency(IA8801Sp.PYAMT) + GetCurrency(IA8801Sp.PYCarryforward)
    else:
        ReturnVal = 0

def TotCr_Calculation():
    ReturnVal = GetCurrency(IA8801Sp.SumCr) + GetCurrency(IA8801Sp.Sum148Cr)

