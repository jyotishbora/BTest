from vb2py.vbfunctions import *
from vb2py.vbdebug import *
import datetime



def Description_Calculation():
    Total = Currency()
    Total = GetCurrency(IAFedEst.TPTotEst) + GetCurrency(IAFedEst.SPTotEst)
    ReturnVal = CStr(Total)

def Exist_Calculation():
    ReturnVal = 1

def MobDisQual_Calculation():
    if GetCurrency(IAFedEst.TPTotEst) + GetCurrency(IAFedEst.SPTotEst) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Names_Calculation():
    ReturnVal = GetString(IARequired.CombNames)

def SPCYEst_Calculation():
    if IAFS() == 3:
        ReturnVal = CDollar(GetFloat(IARequired.BProRate) * GetFloat(IAFedEst.TotCYEst))
    else:
        ReturnVal = 0

def SPName_Calculation():
    ReturnVal = GetString(USWBasicInfo.SPCommon)

def SPPYEst_Calculation():
    if IAFS() == 3:
        ReturnVal = CDollar(GetFloat(IARequired.BProRate) * GetFloat(IAFedEst.TotPYEst))
    else:
        ReturnVal = 0

def SPTotEst_Calculation():
    ReturnVal = GetCurrency(IAFedEst.SPCYEst) + GetCurrency(IAFedEst.SPPYEst)

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

def TotCYEst_Calculation():
    if GetDate(USWEstPay.Q4Date) < datetime.datetime(1, 1, 2019):
        ReturnVal = GetCurrency(USWEstPay.Applied) + GetCurrency(USWEstPay.Q1) + GetCurrency(USWEstPay.Q2) + GetCurrency(USWEstPay.Q3) + GetCurrency(USWEstPay.Q4)
    else:
        ReturnVal = GetCurrency(USWEstPay.Applied) + GetCurrency(USWEstPay.Q1) + GetCurrency(USWEstPay.Q2) + GetCurrency(USWEstPay.Q3)

def TotPYEst_Calculation():
    if GetDate(USWSpouse.PY4EstDate) > datetime.datetime(12, 31, 2017):
        ReturnVal = GetCurrency(USWSpouse.PY4Est) + GetCurrency(USWSpouse.PYLateEst)
    else:
        ReturnVal = GetCurrency(USWSpouse.PYLateEst)

def TPCYEst_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAFedEst.TotCYEst) - GetCurrency(IAFedEst.SPCYEst))

def TPName_Calculation():
    ReturnVal = GetString(USWBasicInfo.TPCommon)

def TPPYEst_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAFedEst.TotPYEst) - GetCurrency(IAFedEst.SPPYEst))

def TPTotEst_Calculation():
    ReturnVal = GetCurrency(IAFedEst.TPCYEst) + GetCurrency(IAFedEst.TPPYEst)

