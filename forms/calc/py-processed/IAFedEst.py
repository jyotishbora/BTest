from forms.out import IAF1040
from forms.out import IAFEDEST
from forms.out import IAREQUIRED
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *
import datetime



def Description_Calculation():
    Total = Currency()
    Total = get_currency(IAFEDEST.TPTotEst) + get_currency(IAFEDEST.SPTotEst)
    return CStr(Total)

def Exist_Calculation():
    return 1

def MobDisQual_Calculation():
    if get_currency(IAFEDEST.TPTotEst) + get_currency(IAFEDEST.SPTotEst) > 0:
        return 1
    else:
        return 0

def Names_Calculation():
    return get_string(IAREQUIRED.CombNames)

def SPCYEst_Calculation():
    if IAFS() == 3:
        return c_dollar(get_float(IAREQUIRED.BProRate) * get_float(IAFEDEST.TotCYEst))
    else:
        return 0

def SPName_Calculation():
    return get_string(USWBasicInfo.SPCommon)

def SPPYEst_Calculation():
    if IAFS() == 3:
        return c_dollar(get_float(IAREQUIRED.BProRate) * get_float(IAFEDEST.TotPYEst))
    else:
        return 0

def SPTotEst_Calculation():
    return get_currency(IAFEDEST.SPCYEst) + get_currency(IAFEDEST.SPPYEst)

def SSN_Calculation():
    return get_string(IAF1040.SSN)

def TotCYEst_Calculation():
    if GetDate(USWEstPay.Q4Date) < datetime.datetime(1, 1, 2019):
        return get_currency(USWEstPay.Applied) + get_currency(USWEstPay.Q1) + get_currency(USWEstPay.Q2) + get_currency(USWEstPay.Q3) + get_currency(USWEstPay.Q4)
    else:
        return get_currency(USWEstPay.Applied) + get_currency(USWEstPay.Q1) + get_currency(USWEstPay.Q2) + get_currency(USWEstPay.Q3)

def TotPYEst_Calculation():
    if GetDate(USWSpouse.PY4EstDate) > datetime.datetime(12, 31, 2017):
        return get_currency(USWSpouse.PY4Est) + get_currency(USWSpouse.PYLateEst)
    else:
        return get_currency(USWSpouse.PYLateEst)

def TPCYEst_Calculation():
    return max_value(0, get_currency(IAFEDEST.TotCYEst) - get_currency(IAFEDEST.SPCYEst))

def TPName_Calculation():
    return get_string(USWBasicInfo.TPCommon)

def TPPYEst_Calculation():
    return max_value(0, get_currency(IAFEDEST.TotPYEst) - get_currency(IAFEDEST.SPPYEst))

def TPTotEst_Calculation():
    return get_currency(IAFEDEST.TPCYEst) + get_currency(IAFEDEST.TPPYEst)


