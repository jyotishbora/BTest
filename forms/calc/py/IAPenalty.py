from vb2py.vbfunctions import *
from vb2py.vbdebug import *
import datetime



def DatePaid_Calculation():
    ReturnVal = GetDate(IAF1040.DateDuePaid)

def Desc_Calculation():
    ReturnVal = CStr(GetCurrency(IAPenalty.TotPen))

def Exist_Calculation():
    ReturnVal = 1

def Names_Calculation():
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetString(IARequired.TPCombName)
    else:
        ReturnVal = GetString(IARequired.CombNames)

def Q1Days1_Calculation():
    if GetDate(IAStateEst.TPStQ2Date) < datetime.datetime(7, 2, 2018):
        ReturnVal = MaxValue(0, DaysDiff(GetDate(IAStateEst.TPStQ2Date), datetime.datetime(4, 30, 2018)))
    else:
        ReturnVal = 63

def Q1Days2_Calculation():
    if GetDate(IAStateEst.TPStQ2Date) < datetime.datetime(7, 2, 2018) and GetCurrency(IAPenalty.Q1UnPay2) > 0:
        ReturnVal = MaxValue(0, DaysDiff(datetime.datetime(7, 2, 2018), GetDate(IAStateEst.TPStQ2Date)))
    else:
        ReturnVal = 0

def Q1Pen1_Calculation():
    ReturnVal = CCur(Round(( GetFloat(IAPenalty.Q1Days1) / 365 )  * 0.06 * GetFloat(IAPenalty.Q1UnPay1)))

def Q1Pen2_Calculation():
    ReturnVal = CCur(Round(( GetFloat(IAPenalty.Q1Days2) / 365 )  * 0.06 * GetFloat(IAPenalty.Q1UnPay2)))

def Q1UnPay1_Calculation():
    ReturnVal = GetCurrency(IA2210.Q1Undpay)

def Q1UnPay2_Calculation():
    if GetDate(IAStateEst.TPStQ2Date) < datetime.datetime(7, 2, 2018):
        ReturnVal = MaxValue(0, GetCurrency(IAPenalty.Q1UnPay1) - GetCurrency(IAStateEst.TPStQ2))
    else:
        ReturnVal = 0

def Q2Days1_Calculation():
    if GetDate(IAStateEst.TPStQ3Date) < datetime.datetime(10, 1, 2018):
        ReturnVal = MaxValue(0, DaysDiff(GetDate(IAStateEst.TPStQ3Date), datetime.datetime(7, 2, 2018)))
    else:
        ReturnVal = 91

def Q2Days2_Calculation():
    if GetDate(IAStateEst.TPStQ3Date) < datetime.datetime(10, 1, 2018) and GetCurrency(IAPenalty.Q2UnPay2) > 0:
        ReturnVal = MaxValue(0, DaysDiff(datetime.datetime(10, 1, 2018), GetDate(IAStateEst.TPStQ3Date)))
    else:
        ReturnVal = 0

def Q2Pen1_Calculation():
    ReturnVal = CCur(Round(( GetFloat(IAPenalty.Q2Days1) / 365 )  * 0.06 * GetFloat(IAPenalty.Q2UnPay1)))

def Q2Pen2_Calculation():
    ReturnVal = CCur(Round(( GetFloat(IAPenalty.Q2Days2) / 365 )  * 0.06 * GetFloat(IAPenalty.Q2UnPay2)))

def Q2UnPay1_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2210.Q1Ln11) + GetCurrency(IA2210.Q2Ln11) - GetCurrency(IA2210.Q1Est) - GetCurrency(IA2210.Q2est))

def Q2UnPay2_Calculation():
    if GetDate(IAStateEst.TPStQ3Date) < datetime.datetime(10, 1, 2018):
        ReturnVal = MaxValue(0, GetCurrency(IAPenalty.Q2UnPay1) - GetCurrency(IAStateEst.TPStQ3))
    else:
        ReturnVal = 0

def Q3Days1_Calculation():
    if GetDate(IAStateEst.TPStQ4Date) < datetime.datetime(12, 31, 2018):
        ReturnVal = MaxValue(0, DaysDiff(GetDate(IAStateEst.TPStQ4Date), datetime.datetime(10, 1, 2018)))
    else:
        ReturnVal = 91

def Q3Days2_Calculation():
    if GetDate(IAStateEst.TPStQ4Date) < datetime.datetime(12, 31, 2018) and GetCurrency(IAPenalty.Q3UnPay2) > 0:
        ReturnVal = MaxValue(0, DaysDiff(datetime.datetime(12, 31, 2018), GetDate(IAStateEst.TPStQ4Date)))
    else:
        ReturnVal = 0

def Q3Days3_Calculation():
    if GetDate(IAStateEst.TPStQ4Date) < datetime.datetime(1, 31, 2019) and GetDate(IAStateEst.TPStQ4Date) > datetime.datetime(12, 31, 2018):
        ReturnVal = MaxValue(0, DaysDiff(GetDate(IAStateEst.TPStQ4Date), datetime.datetime(12, 31, 2018)))
    elif GetCurrency(IAPenalty.Q3Unpay3) >= 0:
        ReturnVal = 31
    else:
        ReturnVal = 0

def Q3Days4_Calculation():
    if GetDate(IAStateEst.TPStQ4Date) > datetime.datetime(12, 31, 2018) and GetDate(IAStateEst.TPStQ4Date) < datetime.datetime(1, 31, 2019) and GetCurrency(IAPenalty.Q3Unpay4) > 0:
        ReturnVal = MaxValue(0, DaysDiff(datetime.datetime(1, 31, 2019), GetDate(IAStateEst.TPStQ4Date)))
    else:
        ReturnVal = 0

def Q3Pen1_Calculation():
    ReturnVal = CCur(Round(( GetFloat(IAPenalty.Q3Days1) / 365 )  * 0.06 * GetFloat(IAPenalty.Q3Unpay1)))

def Q3Pen2_Calculation():
    ReturnVal = CCur(Round(( GetFloat(IAPenalty.Q3Days2) / 365 )  * 0.06 * GetFloat(IAPenalty.Q3UnPay2)))

def Q3Pen3_Calculation():
    ReturnVal = CCur(Round(( GetFloat(IAPenalty.Q3Days3) / 365 )  * 0.07 * GetFloat(IAPenalty.Q3Unpay3)))

def Q3Pen4_Calculation():
    ReturnVal = CCur(Round(( GetFloat(IAPenalty.Q3Days4) / 365 )  * 0.07 * GetFloat(IAPenalty.Q3Unpay4)))

def Q3Unpay1_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2210.Q1Ln11) + GetCurrency(IA2210.Q2Ln11) + GetCurrency(IA2210.Q3Ln11) - GetCurrency(IA2210.Q1Est) - GetCurrency(IA2210.Q2est) - GetCurrency(IA2210.Q3Est))

def Q3UnPay2_Calculation():
    if GetDate(IAStateEst.TPStQ4Date) < datetime.datetime(12, 31, 2018):
        ReturnVal = MaxValue(0, GetCurrency(IAPenalty.Q3Unpay1) - GetCurrency(IAStateEst.TPStQ4))
    else:
        ReturnVal = 0

def Q3Unpay3_Calculation():
    if GetCurrency(IAPenalty.Q3UnPay2) > 0:
        ReturnVal = GetCurrency(IAPenalty.Q3UnPay2)
    elif GetDate(IAStateEst.TPStQ4Date) < datetime.datetime(1, 1, 2019):
        ReturnVal = MaxValue(0, GetCurrency(IAPenalty.Q3Unpay1) - GetCurrency(IAStateEst.TPStQ4))
    else:
        ReturnVal = GetCurrency(IAPenalty.Q3Unpay1)

def Q3Unpay4_Calculation():
    if GetDate(IAStateEst.TPStQ4Date) > datetime.datetime(12, 31, 2018) and GetDate(IAStateEst.TPStQ4Date) < datetime.datetime(1, 31, 2019):
        ReturnVal = MaxValue(0, GetCurrency(IAPenalty.Q3Unpay1) - GetCurrency(IAStateEst.TPStQ4))
    else:
        ReturnVal = 0

def Q4Days1_Calculation():
    # 89 days max in 2018
    if GetDate(IAStateEst.TPStLateDate) < GetDate(IAF1040.DateDuePaid) and GetCurrency(IAStateEst.TPStLate) > 0:
        ReturnVal = MaxValue(0, DaysDiff(GetDate(IAStateEst.TPStLateDate), datetime.datetime(1, 31, 2019)))
    else:
        ReturnVal = MaxValue(0, DaysDiff(GetDate(IAF1040.DateDuePaid), datetime.datetime(1, 31, 2019)))

def Q4Days2_Calculation():
    if GetDate(IAStateEst.TPStLateDate) < datetime.datetime(4, 30, 2019) and GetCurrency(IAPenalty.Q4Unpay2) > 0:
        ReturnVal = MaxValue(0, DaysDiff(GetDate(IAF1040.DateDuePaid), GetDate(IAStateEst.TPStLateDate)))
    else:
        ReturnVal = 0

def Q4Pen1_Calculation():
    ReturnVal = CCur(Round(( GetFloat(IAPenalty.Q4Days1) / 365 )  * 0.07 * GetFloat(IAPenalty.Q4UnPay1)))

def Q4Pen2_Calculation():
    ReturnVal = CCur(Round(( GetFloat(IAPenalty.Q4Days2) / 365 )  * 0.07 * GetFloat(IAPenalty.Q4Unpay2)))

def Q4UnPay1_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2210.Q1Ln11) + GetCurrency(IA2210.Q2Ln11) + GetCurrency(IA2210.Q3Ln11) + GetCurrency(IA2210.Q4Ln11) - GetCurrency(IA2210.Q1Est) - GetCurrency(IA2210.Q2est) - GetCurrency(IA2210.Q3Est) - GetCurrency(IA2210.Q4Est))

def Q4Unpay2_Calculation():
    if GetDate(IAStateEst.TPStLateDate) < datetime.datetime(4, 30, 2019) and GetCurrency(IAStateEst.TPStLate) > 0:
        ReturnVal = MaxValue(0, GetCurrency(IAPenalty.Q4UnPay1) - GetCurrency(IAStateEst.TPStLate))
    else:
        ReturnVal = 0

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

def TotPen_Calculation():
    ReturnVal = Round(GetCurrency(IAPenalty.Q1Pen1) + GetCurrency(IAPenalty.Q1Pen2) + GetCurrency(IAPenalty.Q2Pen1) + GetCurrency(IAPenalty.Q2Pen2) + GetCurrency(IAPenalty.Q3Pen1) + GetCurrency(IAPenalty.Q3Pen2) + GetCurrency(IAPenalty.Q3Pen3) + GetCurrency(IAPenalty.Q3Pen4) + GetCurrency(IAPenalty.Q4Pen1) + GetCurrency(IAPenalty.Q4Pen2))

