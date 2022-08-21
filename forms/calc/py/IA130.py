from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Alert10_Calculation():
    if GetBool(IA130.MEF130TP) == True and Trim(GetString(IA130.EFTPState)) == '':
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert20_Calculation():
    if GetBool(IA130.MEF130SP) == True and Trim(GetString(IA130.EFTPState)) == '':
        ReturnVal = 1
    else:
        ReturnVal = 0

def Common_Calculation():
    if GetBool(IAF1040.MFJ) == True:
        ReturnVal = GetString(USWBasicInfo.CombFirst)
    else:
        ReturnVal = GetString(USWBasicInfo.TPCommon)

def Credit_Calculation():
    ReturnVal = GetCurrency(IA130.Small) + GetCurrency(IA130.PY130Cr)

def Description_Calculation():
    Total = Currency()
    Total = GetCurrency(IA130.Small) + GetCurrency(IA130.PY130Cr)
    ReturnVal = CStr(Total) + ' Credit'

def Div_Calculation():
    TopLim = Double()
    if GetCurrency(IA130.Inc15) == 0:
        ReturnVal = 0
    else:
        TopLim = MinValue(1, Round(GetFloat(IA130.GrInc) / GetFloat(IA130.Inc15), 3))
        ReturnVal = MaxValue(0, TopLim)

def EFTPState_Calculation():
    if Trim(GetString(IA130.YouFC)) != '':
        ReturnVal = ForeignCode(Trim(GetString(IA130.YouFC)))
    else:
        ReturnVal = GetString(IA130.YouState)

def Exist_Calculation():
    ReturnVal = 1

def Inc15_Calculation():
    if GetBool(IA130.TPRes) == True:
        ReturnVal = GetCurrency(IAF1040.AGross)
    elif GetBool(IA130.TPPY) == True:
        ReturnVal = GetCurrency(IAF126.GrossInc)
    elif GetBool(IA130.SPRes) == True:
        ReturnVal = GetCurrency(IAF1040.BGross)
    elif GetBool(IA130.SPPY) == True:
        ReturnVal = GetCurrency(IAF126.BGross)
    else:
        ReturnVal = 0

def MEF130SP_Calculation():
    if GetBool(IA130.SPRes) == True and GetCurrency(IA130.Small) != 0:
        ReturnVal = 1
    elif GetBool(IA130.SPPY) == True and GetCurrency(IA130.PY130Cr) != 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def MEF130TP_Calculation():
    if GetBool(IA130.TPRes) == True and GetCurrency(IA130.Small) != 0:
        ReturnVal = 1
    elif GetBool(IA130.TPPY) == True and GetCurrency(IA130.PY130Cr) != 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Mult_Calculation():
    ReturnVal = CDollar(GetFloat(IA130.Div) * GetFloat(IA130.Tax55))

def Names_Calculation():
    if GetBool(IAF1040.CombMFS) == True:
        if GetBool(IA130.Spouse) == True:
            ReturnVal = GetString(IARequired.SPCombName)
        else:
            ReturnVal = GetString(IARequired.TPCombName)
    else:
        ReturnVal = GetString(IARequired.CombNames)

def PartYear_Calculation():
    if GetNumber(IA130.TPPY) > 0 or GetNumber(IA130.SPPY) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def PrintMe_Calculation():
    if GetCurrency(IA130.Small) + GetCurrency(IA130.PY130Cr) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def PY130Cr_Calculation():
    if GetBool(IA130.TPPY) == True or GetBool(IA130.SPPY) == True:
        ReturnVal = MinValue(GetCurrency(IA130.Mult), GetCurrency(IA130.PYTax))
    else:
        ReturnVal = 0

def PYPer_Calculation():
    TopLim = Double()
    if GetBool(IA130.TPPY) == True or GetBool(IA130.SPPY) == True:
        if GetFloat(IA130.PYSmall) == 0:
            ReturnVal = 0
        else:
            TopLim = MinValue(1, Round(GetFloat(IA130.GrInc) / GetFloat(IA130.PYSmall), 3))
            ReturnVal = MaxValue(0, TopLim)
    else:
        ReturnVal = 0

def PYTax_Calculation():
    if GetBool(IA130.TPPY) == True or GetBool(IA130.SPPY) == True:
        ReturnVal = CDollar(GetFloat(IA130.OthTax) * GetFloat(IA130.PYPer))
    else:
        ReturnVal = 0

def Small_Calculation():
    if GetBool(IA130.TPRes) == True or GetBool(IA130.SPRes) == True:
        ReturnVal = MinValue(GetCurrency(IA130.Mult), GetCurrency(IA130.OthTax))
    else:
        ReturnVal = 0

def SPCredit_Calculation():
    if GetNumber(IA130.SPRes) > 0 or GetNumber(IA130.SPPY) > 0:
        ReturnVal = GetCurrency(IA130.Small) + GetCurrency(IA130.PY130Cr)
    else:
        ReturnVal = 0

def SpouseCommon_Calculation():
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetString(USWBasicInfo.SPCommon)
    else:
        ReturnVal = 'Not Applicable'

def SPPY_Calculation():
    if GetBool(IAF1040.CombMFS) == True and GetBool(IAF126.SpPYRes) == True and GetBool(IA130.Spouse) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

def SPRes_Calculation():
    if GetBool(IAF1040.CombMFS) == True and GetBool(IA130.Spouse) == True:
        if GetBool(IAF126.Exist) == False:
            ReturnVal = 1
        elif GetBool(IAF126.SpRes) == True:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def SSN_Calculation():
    if GetBool(IA130.Spouse) == True:
        ReturnVal = GetString(IAF1040.SpouseSSN)
    else:
        ReturnVal = GetString(IAF1040.SSN)

def Tax55_Calculation():
    if GetBool(IA130.TPRes) == True or GetBool(IA130.TPPY) == True:
        ReturnVal = MaxValue(0, GetCurrency(IAF1040.ABal2) -  ( GetCurrency(IAF1040.ALump) + GetCurrency(IAF1040.AIAMin) ))
    elif GetBool(IA130.SPRes) == True or GetBool(IA130.SPPY) == True:
        ReturnVal = MaxValue(0, GetCurrency(IAF1040.BBal2) -  ( GetCurrency(IAF1040.BLump) + GetCurrency(IAF1040.BIAMin) ))
    else:
        ReturnVal = 0

def TPCredit_Calculation():
    if GetNumber(IA130.TPRes) > 0 or GetNumber(IA130.TPPY) > 0:
        ReturnVal = GetCurrency(IA130.Small) + GetCurrency(IA130.PY130Cr)
    else:
        ReturnVal = 0

def TPPY_Calculation():
    if GetBool(IA130.Spouse) == True:
        ReturnVal = 0
    elif GetBool(IAF1040.MFJ) == True:
        if GetBool(IAF126.TpPYRes) == True or GetBool(IAF126.SpPYRes) == True:
            ReturnVal = 1
        else:
            ReturnVal = 0
    elif GetBool(IAF126.TpPYRes) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

def TPRes_Calculation():
    Only1NR = Long()
    if GetBool(IAF126.TpNonRes) == True and GetBool(IAF126.SPRes) == True:
        Only1NR = 1
    elif GetBool(IAF126.TPRes) == True and GetBool(IAF126.SpNonRes) == True:
        Only1NR = 1
    else:
        Only1NR = 0
    if GetBool(IA130.Spouse) == True:
        ReturnVal = 0
    elif GetBool(IAF126.Exist) == False:
        ReturnVal = 1
    elif GetBool(IAF1040.MFJ) == True and Only1NR == 1:
        ReturnVal = 1
    elif GetBool(IAF1040.MFJ) == True and GetBool(IAF126.TPRes) == True and GetBool(IAF126.SPRes) == True:
        ReturnVal = 1
    elif GetBool(IAF1040.MFJ) != True and GetBool(IAF126.TPRes) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

