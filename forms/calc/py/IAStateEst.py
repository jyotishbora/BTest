from vb2py.vbfunctions import *
from vb2py.vbdebug import *
import datetime



def Desc_Calculation():
    ReturnVal = CStr(GetCurrency(IAStateEst.TotIAEst))

def Exist_Calculation():
    ReturnVal = 1

def MobDisQual_Calculation():
    if GetCurrency(IAStateEst.TotIAEst) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Names_Calculation():
    ReturnVal = GetString(IARequired.CombNames)

def SPIAEst_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IAStateEst.SPStApply) + GetCurrency(IAStateEst.SPStQ1) + GetCurrency(IAStateEst.SPStQ2) + GetCurrency(IAStateEst.SPStQ3) + GetCurrency(IAStateEst.SPStQ4) + GetCurrency(IAStateEst.SPStLate)
    else:
        ReturnVal = 0

def SPName_Calculation():
    ReturnVal = GetString(USWBasicInfo.SPCommon)

def SPStLateDate_Calculation():
    if IAFS() == 3:
        ReturnVal = GetDate(IAStateEst.TPStLateDate)
    else:
        ReturnVal = ''

def SPStQ1Date_Calculation():
    if IAFS() == 3:
        ReturnVal = GetDate(IAStateEst.TPStQ1Date)
    else:
        ReturnVal = ''

def SPStQ2Date_Calculation():
    if IAFS() == 3:
        ReturnVal = GetDate(IAStateEst.TPStQ2Date)
    else:
        ReturnVal = ''

def SPStQ3Date_Calculation():
    if IAFS() == 3:
        ReturnVal = GetDate(IAStateEst.TPStQ3Date)
    else:
        ReturnVal = ''

def SPStQ4Date_Calculation():
    if IAFS() == 3:
        ReturnVal = GetDate(IAStateEst.TPStQ4Date)
    else:
        ReturnVal = ''

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

def StApply_Calculation():
    if GetString(USWEstPay.StName1) == 'Iowa':
        ReturnVal = GetCurrency(USWEstPay.StApply)
    elif GetString(USWEstPay.StName2) == 'Iowa':
        ReturnVal = GetCurrency(USWEstPay.St2Apply)
    elif GetString(USWEstPay.StName3) == 'Iowa':
        ReturnVal = GetCurrency(USWEstPay.St3Apply)
    else:
        ReturnVal = 0

def StLate_Calculation():
    if GetString(USWEstPay.StName1) == 'Iowa':
        ReturnVal = GetCurrency(USWEstPay.StLate)
    elif GetString(USWEstPay.StName2) == 'Iowa':
        ReturnVal = GetCurrency(USWEstPay.St2Late)
    elif GetString(USWEstPay.StName3) == 'Iowa':
        ReturnVal = GetCurrency(USWEstPay.St3Late)
    else:
        ReturnVal = 0

def StQ1_Calculation():
    if GetString(USWEstPay.StName1) == 'Iowa':
        ReturnVal = GetCurrency(USWEstPay.StQ1)
    elif GetString(USWEstPay.StName2) == 'Iowa':
        ReturnVal = GetCurrency(USWEstPay.St2Q1)
    elif GetString(USWEstPay.StName3) == 'Iowa':
        ReturnVal = GetCurrency(USWEstPay.St3Q1)
    else:
        ReturnVal = 0

def StQ2_Calculation():
    if GetString(USWEstPay.StName1) == 'Iowa':
        ReturnVal = GetCurrency(USWEstPay.StQ2)
    elif GetString(USWEstPay.StName2) == 'Iowa':
        ReturnVal = GetCurrency(USWEstPay.St2Q2)
    elif GetString(USWEstPay.StName3) == 'Iowa':
        ReturnVal = GetCurrency(USWEstPay.St3Q2)
    else:
        ReturnVal = 0

def StQ3_Calculation():
    if GetString(USWEstPay.StName1) == 'Iowa':
        ReturnVal = GetCurrency(USWEstPay.StQ3)
    elif GetString(USWEstPay.StName2) == 'Iowa':
        ReturnVal = GetCurrency(USWEstPay.St2Q3)
    elif GetString(USWEstPay.StName3) == 'Iowa':
        ReturnVal = GetCurrency(USWEstPay.St3Q3)
    else:
        ReturnVal = 0

def StQ4_Calculation():
    if GetString(USWEstPay.StName1) == 'Iowa':
        ReturnVal = GetCurrency(USWEstPay.StQ4)
    elif GetString(USWEstPay.StName2) == 'Iowa':
        ReturnVal = GetCurrency(USWEstPay.St2Q4)
    elif GetString(USWEstPay.StName3) == 'Iowa':
        ReturnVal = GetCurrency(USWEstPay.St3Q4)
    else:
        ReturnVal = 0

def TotIAEst_Calculation():
    ReturnVal = GetCurrency(IAStateEst.StApply) + GetCurrency(IAStateEst.StQ1) + GetCurrency(IAStateEst.StQ2) + GetCurrency(IAStateEst.StQ3) + GetCurrency(IAStateEst.StQ4) + GetCurrency(IAStateEst.StLate)

def TPName_Calculation():
    ReturnVal = GetString(USWBasicInfo.TPCommon)

def TPStApply_Calculation():
    if IAFS() == 3:
        ReturnVal = MaxValue(0, GetCurrency(IAStateEst.StApply) - GetCurrency(IAStateEst.SPStApply))
    else:
        ReturnVal = GetCurrency(IAStateEst.StApply)

def TPStLate_Calculation():
    if IAFS() == 3:
        ReturnVal = MaxValue(0, GetCurrency(IAStateEst.StLate) - GetCurrency(IAStateEst.SPStLate))
    else:
        ReturnVal = GetCurrency(IAStateEst.StLate)

def TPStLateDate_Calculation():
    if GetString(USWEstPay.StName1) == 'Iowa':
        ReturnVal = GetDate(USWEstPay.StLateDate)
    elif GetString(USWEstPay.StName2) == 'Iowa':
        ReturnVal = GetDate(USWEstPay.St2LateDate)
    elif GetString(USWEstPay.StName3) == 'Iowa':
        ReturnVal = GetDate(USWEstPay.St3LateDate)
    else:
        ReturnVal = datetime.datetime(4, 30, 2019)

def TPStQ1_Calculation():
    if IAFS() == 3:
        ReturnVal = MaxValue(0, GetCurrency(IAStateEst.StQ1) - GetCurrency(IAStateEst.SPStQ1))
    else:
        ReturnVal = GetCurrency(IAStateEst.StQ1)

def TPStQ1Date_Calculation():
    if GetString(USWEstPay.StName1) == 'Iowa':
        ReturnVal = GetDate(USWEstPay.StQ1Date)
    elif GetString(USWEstPay.StName2) == 'Iowa':
        ReturnVal = GetDate(USWEstPay.St2Q1Date)
    elif GetString(USWEstPay.StName3) == 'Iowa':
        ReturnVal = GetDate(USWEstPay.St3Q1Date)
    else:
        ReturnVal = datetime.datetime(4, 30, 2018)

def TPStQ2_Calculation():
    if IAFS() == 3:
        ReturnVal = MaxValue(0, GetCurrency(IAStateEst.StQ2) - GetCurrency(IAStateEst.SPStQ2))
    else:
        ReturnVal = GetCurrency(IAStateEst.StQ2)

def TPStQ2Date_Calculation():
    if GetString(USWEstPay.StName1) == 'Iowa':
        ReturnVal = GetDate(USWEstPay.StQ2Date)
    elif GetString(USWEstPay.StName2) == 'Iowa':
        ReturnVal = GetDate(USWEstPay.St2Q2Date)
    elif GetString(USWEstPay.StName3) == 'Iowa':
        ReturnVal = GetDate(USWEstPay.St3Q2Date)
    else:
        ReturnVal = datetime.datetime(7, 2, 2018)

def TPStQ3_Calculation():
    if IAFS() == 3:
        ReturnVal = MaxValue(0, GetCurrency(IAStateEst.StQ3) - GetCurrency(IAStateEst.SPStQ3))
    else:
        ReturnVal = GetCurrency(IAStateEst.StQ3)

def TPStQ3Date_Calculation():
    if GetString(USWEstPay.StName1) == 'Iowa':
        ReturnVal = GetDate(USWEstPay.StQ3Date)
    elif GetString(USWEstPay.StName2) == 'Iowa':
        ReturnVal = GetDate(USWEstPay.St2Q3Date)
    elif GetString(USWEstPay.StName3) == 'Iowa':
        ReturnVal = GetDate(USWEstPay.St3Q3Date)
    else:
        ReturnVal = datetime.datetime(10, 1, 2018)

def TPStQ4_Calculation():
    if IAFS() == 3:
        ReturnVal = MaxValue(0, GetCurrency(IAStateEst.StQ4) - GetCurrency(IAStateEst.SPStQ4))
    else:
        ReturnVal = GetCurrency(IAStateEst.StQ4)

def TPStQ4Date_Calculation():
    if GetString(USWEstPay.StName1) == 'Iowa':
        ReturnVal = GetDate(USWEstPay.StQ4Date)
    elif GetString(USWEstPay.StName2) == 'Iowa':
        ReturnVal = GetDate(USWEstPay.St2Q4Date)
    elif GetString(USWEstPay.StName3) == 'Iowa':
        ReturnVal = GetDate(USWEstPay.St3Q4Date)
    else:
        ReturnVal = datetime.datetime(1, 31, 2019)

