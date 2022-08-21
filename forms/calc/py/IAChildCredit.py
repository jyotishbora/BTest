from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def ChDepCr_Calculation():
    ReturnVal = CDollar(GetFloat(IAChildCredit.FedCredit) * GetFloat(IAChildCredit.Percent))

def Credit_Calculation(Index):
    if GetCurrency(IAChildCredit.TotNI) < Decimal("45000") and Trim(GetString(IAChildCredit.DepName(Index))) != '':
        ReturnVal = CDollar(CDbl(MinValue(GetCurrency(IAChildCredit.Expenses(Index)), Decimal("1000"))) * 0.25)
    else:
        ReturnVal = 0

def DepName_Calculation(Index):
    count = Integer()

    Hold = String()
    count = 0
    Hold = ''
    if GetNumber(IAAddDep.FDepAge(0)) > 2 and GetNumber(IAAddDep.FDepAge(0)) < 7:
        if Index == count:
            Hold = GetString(IAAddDep.FDepName(0)) + ' ' + GetString(IAAddDep.FDepLast(0))
            count = 99
        else:
            count = count + 1
    if GetNumber(IAAddDep.FDepAge(1)) > 2 and GetNumber(IAAddDep.FDepAge(1)) < 7:
        if Index == count:
            Hold = GetString(IAAddDep.FDepName(1)) + ' ' + GetString(IAAddDep.FDepLast(1))
            count = 99
        else:
            count = count + 1
    if GetNumber(IAAddDep.FDepAge(2)) > 2 and GetNumber(IAAddDep.FDepAge(2)) < 7:
        if Index == count:
            Hold = GetString(IAAddDep.FDepName(2)) + ' ' + GetString(IAAddDep.FDepLast(2))
            count = 99
        else:
            count = count + 1
    if GetNumber(IAAddDep.FDepAge(3)) > 2 and GetNumber(IAAddDep.FDepAge(3)) < 7:
        if Index == count:
            Hold = GetString(IAAddDep.FDepName(3)) + ' ' + GetString(IAAddDep.FDepLast(3))
            count = 99
        else:
            count = count + 1
    if GetNumber(IAAddDep.FDepAge(4)) > 2 and GetNumber(IAAddDep.FDepAge(4)) < 7:
        if Index == count:
            Hold = GetString(IAAddDep.FDepName(4)) + ' ' + GetString(IAAddDep.FDepLast(4))
            count = 99
        else:
            count = count + 1
    if GetNumber(IAAddDep.FDepAge(5)) > 2 and GetNumber(IAAddDep.FDepAge(5)) < 7:
        if Index == count:
            Hold = GetString(IAAddDep.FDepName(5)) + ' ' + GetString(IAAddDep.FDepLast(5))
            count = 99
        else:
            count = count + 1
    if GetNumber(IAAddDep.FDepAge(6)) > 2 and GetNumber(IAAddDep.FDepAge(6)) < 7:
        if Index == count:
            Hold = GetString(IAAddDep.FDepName(6)) + ' ' + GetString(IAAddDep.FDepLast(6))
            count = 99
        else:
            count = count + 1
    if GetNumber(IAAddDep.FDepAge(7)) > 2 and GetNumber(IAAddDep.FDepAge(7)) < 7:
        if Index == count:
            Hold = GetString(IAAddDep.FDepName(7)) + ' ' + GetString(IAAddDep.FDepLast(7))
            count = 99
        else:
            count = count + 1
    if GetNumber(IAAddDep.FDepAge(8)) > 2 and GetNumber(IAAddDep.FDepAge(8)) < 7:
        if Index == count:
            Hold = GetString(IAAddDep.FDepName(8)) + ' ' + GetString(IAAddDep.FDepLast(8))
            count = 99
        else:
            count = count + 1
    if GetNumber(IAAddDep.FDepAge(9)) > 2 and GetNumber(IAAddDep.FDepAge(9)) < 7:
        if Index == count:
            Hold = GetString(IAAddDep.FDepName(9)) + ' ' + GetString(IAAddDep.FDepLast(9))
            count = 99
        else:
            count = count + 1
    if GetNumber(IAAddDep.FDepAge(10)) > 2 and GetNumber(IAAddDep.FDepAge(10)) < 7:
        if Index == count:
            Hold = GetString(IAAddDep.FDepName(10)) + ' ' + GetString(IAAddDep.FDepLast(10))
            count = 99
        else:
            count = count + 1
    if GetNumber(IAAddDep.FDepAge(11)) > 2 and GetNumber(IAAddDep.FDepAge(11)) < 7:
        if Index == count:
            Hold = GetString(IAAddDep.FDepName(11)) + ' ' + GetString(IAAddDep.FDepLast(11))
            count = 99
        else:
            count = count + 1
    if GetNumber(IAAddDep.FDepAge(12)) > 2 and GetNumber(IAAddDep.FDepAge(12)) < 7:
        if Index == count:
            Hold = GetString(IAAddDep.FDepName(12)) + ' ' + GetString(IAAddDep.FDepLast(12))
            count = 99
        else:
            count = count + 1
    if GetNumber(IAAddDep.FDepAge(13)) > 2 and GetNumber(IAAddDep.FDepAge(13)) < 7:
        if Index == count:
            Hold = GetString(IAAddDep.FDepName(13)) + ' ' + GetString(IAAddDep.FDepLast(13))
            count = 99
        else:
            count = count + 1
    if GetNumber(IAAddDep.FDepAge(14)) > 2 and GetNumber(IAAddDep.FDepAge(14)) < 7:
        if Index == count:
            Hold = GetString(IAAddDep.FDepName(14)) + ' ' + GetString(IAAddDep.FDepLast(14))
            count = 99
        else:
            count = count + 1
    ReturnVal = Hold

def Description_Calculation():
    TotCR = Currency()
    if GetBool(IAF1040.ChildCareCk) == True:
        TotCR = GetCurrency(IAChildCredit.TotChDepCr)
    elif GetBool(IAF1040.EarlyChildCk) == True:
        TotCR = GetCurrency(IAChildCredit.TotCR)
    else:
        TotCR = 0
    ReturnVal = CStr(TotCR)

def FedCredit_Calculation():
    ReturnVal = GetCurrency(USF2441.TentCred)

def MFSProRate_Calculation():
    if IAFS() == 4:
        if GetCurrency(IAF1040.SpIncome) < 0 and GetCurrency(IAF1040.ANet) < 0:
            if GetCurrency(IAF1040.SpIncome) < GetCurrency(IAF1040.ANet):
                ReturnVal = 0
            else:
                ReturnVal = 1
        elif GetCurrency(IAF1040.SpIncome) < 0:
            ReturnVal = 0
        elif GetCurrency(IAF1040.SpIncome) > 0 and GetCurrency(IAChildCredit.MFSTotNet) <= 0:
            ReturnVal = 1
        elif GetCurrency(IAChildCredit.MFSTotNet) == 0:
            ReturnVal = 0
        else:
            ReturnVal = MaxValue(0, ( MinValue(1, GetFloat(IAF1040.SpIncome) / GetFloat(IAChildCredit.MFSTotNet)) ))
    else:
        ReturnVal = 0

def MFSTotNet_Calculation():
    if GetBool(IAF1040.MFS) == True:
        ReturnVal = GetCurrency(IAF1040.ANet) + GetCurrency(IAOthAdj.TIANOL) + GetCurrency(IAF1040.SpIncome)
    else:
        ReturnVal = 0

def Names_Calculation():
    ReturnVal = GetString(IARequired.CombNames)

def Percent_Calculation():
    if GetCurrency(IAChildCredit.TotNI) > Decimal("44999"):
        ReturnVal = 0
    elif GetCurrency(IAChildCredit.TotNI) > Decimal("39999"):
        ReturnVal = 0.3
    elif GetCurrency(IAChildCredit.TotNI) > Decimal("34999"):
        ReturnVal = 0.4
    elif GetCurrency(IAChildCredit.TotNI) > Decimal("24999"):
        ReturnVal = 0.5
    elif GetCurrency(IAChildCredit.TotNI) > Decimal("19999"):
        ReturnVal = 0.55
    elif GetCurrency(IAChildCredit.TotNI) > Decimal("9999"):
        ReturnVal = 0.65
    else:
        ReturnVal = 0.75

def PYNRChDepCr_Calculation():
    ReturnVal = MinValue(GetCurrency(IAChildCredit.ChDepCr), ( CDollar(GetFloat(IAChildCredit.ChDepCr) * GetFloat(IAChildCredit.PYNRPercent)) ))

def PYNRPercent_Calculation():
    if GetCurrency(IAChildCredit.TotNI) > 0:
        ReturnVal = MinValue(1, MaxValue(0, CDbl(GetCurrency(IAChildCredit.PYNRTotNI)) / CDbl(GetCurrency(IAChildCredit.TotNI))))
    else:
        ReturnVal = 0

def PYNRTotNI_Calculation():
    if GetBool(IAF126.TpPYNR) == True or GetBool(IAF126.SpPYNR):
        ReturnVal = GetCurrency(IAChildCredit.TPNRIncome) + GetCurrency(IAChildCredit.SPNRIncome)
    else:
        ReturnVal = 0

def SChild_Calculation():
    if GetBool(IAF1040.MFS) == True:
        ReturnVal = CDollar(GetFloat(IAChildCredit.TotChDepCr) * GetFloat(IAChildCredit.MFSProRate))
    else:
        ReturnVal = CDollar(GetFloat(IAChildCredit.TotChDepCr) * GetFloat(IARequired.BProRate))

def SEarly_Calculation():
    if GetBool(IAF1040.MFS) == True:
        ReturnVal = CDollar(GetFloat(IAChildCredit.TotCR) * GetFloat(IAChildCredit.MFSProRate))
    else:
        ReturnVal = CDollar(GetFloat(IAChildCredit.TotCR) * GetFloat(IARequired.BProRate))

def SPNRIncome_Calculation():
    if GetBool(IAF1040.MFS) == True:
        ReturnVal = GetCurrency(IAF1040.SpIncome)
    elif GetBool(IAF126.SpPYNR) == True:
        ReturnVal = GetCurrency(IAF126.BNet) + GetCurrency(IANROthAdj.SIANOL)
    else:
        ReturnVal = GetCurrency(IAF1040.BNet) + GetCurrency(IAOthAdj.SIANOL)

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

def TChild_Calculation():
    ReturnVal = GetCurrency(IAChildCredit.TotChDepCr) - GetCurrency(IAChildCredit.SChild)

def TEarly_Calculation():
    ReturnVal = GetCurrency(IAChildCredit.TotCR) - GetCurrency(IAChildCredit.SEarly)

def TotChDepCr_Calculation():
    if GetBool(IAF126.TpPYNR) == True or GetBool(IAF126.SpPYNR):
        ReturnVal = GetCurrency(IAChildCredit.PYNRChDepCr)
    else:
        ReturnVal = GetCurrency(IAChildCredit.ChDepCr)

def TotCR_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 15:
        SubTot = SubTot + GetCurrency(IAChildCredit.Credit(count))
        count = count + 1
    ReturnVal = SubTot

def TotNI_Calculation():
    if GetBool(IAF1040.MFS) == True:
        ReturnVal = GetCurrency(IAChildCredit.MFSTotNet)
    else:
        ReturnVal = GetCurrency(IARequired.TotNI) + GetCurrency(IAOthAdj.TIANOL) + GetCurrency(IAOthAdj.SIANOL)

def TPNRIncome_Calculation():
    if GetBool(IAF126.TpPYNR) == True:
        ReturnVal = GetCurrency(IAF126.ANet) + GetCurrency(IANROthAdj.TIANOL)
    else:
        ReturnVal = GetCurrency(IAF1040.ANet) + GetCurrency(IAOthAdj.TIANOL)

