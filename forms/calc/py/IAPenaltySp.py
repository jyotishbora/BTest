from vb2py.vbfunctions import *
from vb2py.vbdebug import *
import datetime



def DatePaid_Calculation():
    ReturnVal = GetDate(IAF1040.DateDuePaid)

def Desc_Calculation():
    ReturnVal = CStr(GetCurrency(IAPenaltySp.TotPen))

def Exist_Calculation():
    ReturnVal = 1

def Names_Calculation():
    ReturnVal = GetString(IARequired.SPCombName)

def Q1Days1_Calculation():
    if GetDate(IAStateEst.SPStQ2Date) < datetime.datetime(7, 2, 2018):
        ReturnVal = MaxValue(0, DaysDiff(GetDate(IAStateEst.SPStQ2Date), datetime.datetime(4, 30, 2018)))
    else:
        ReturnVal = 63

def Q1Days2_Calculation():
    if GetDate(IAStateEst.SPStQ2Date) < datetime.datetime(7, 2, 2018) and GetCurrency(IAPenaltySp.Q1UnPay2) > 0:
        ReturnVal = MaxValue(0, DaysDiff(datetime.datetime(7, 2, 2018), GetDate(IAStateEst.SPStQ2Date)))
    else:
        ReturnVal = 0

def Q1Pen1_Calculation():
    ReturnVal = CCur(Round(( GetFloat(IAPenaltySp.Q1Days1) / 365 )  * 0.06 * GetFloat(IAPenaltySp.Q1UnPay1)))

def Q1Pen2_Calculation():
    ReturnVal = CCur(Round(( GetFloat(IAPenaltySp.Q1Days2) / 365 )  * 0.06 * GetFloat(IAPenaltySp.Q1UnPay2)))

def Q1UnPay1_Calculation():
    ReturnVal = GetCurrency(IA2210Sp.Q1Undpay)

def Q1UnPay2_Calculation():
    if GetDate(IAStateEst.SPStQ2Date) < datetime.datetime(7, 2, 2018):
        ReturnVal = MaxValue(0, GetCurrency(IAPenaltySp.Q1UnPay1) - GetCurrency(IAStateEst.SPStQ2))
    else:
        ReturnVal = 0

def Q2Days1_Calculation():
    if GetDate(IAStateEst.SPStQ3Date) < datetime.datetime(10, 1, 2018):
        ReturnVal = MaxValue(0, DaysDiff(GetDate(IAStateEst.SPStQ3Date), datetime.datetime(7, 2, 2018)))
    else:
        ReturnVal = 91

def Q2Days2_Calculation():
    if GetDate(IAStateEst.SPStQ3Date) < datetime.datetime(10, 1, 2018) and GetCurrency(IAPenaltySp.Q2UnPay2) > 0:
        ReturnVal = MaxValue(0, DaysDiff(datetime.datetime(10, 1, 2018), GetDate(IAStateEst.SPStQ3Date)))
    else:
        ReturnVal = 0

def Q2Pen1_Calculation():
    ReturnVal = CCur(Round(( GetFloat(IAPenaltySp.Q2Days1) / 365 )  * 0.06 * GetFloat(IAPenaltySp.Q2UnPay1)))

def Q2Pen2_Calculation():
    ReturnVal = CCur(Round(( GetFloat(IAPenaltySp.Q2Days2) / 365 )  * 0.06 * GetFloat(IAPenaltySp.Q2UnPay2)))

def Q2UnPay1_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2210Sp.Q1Ln11) + GetCurrency(IA2210Sp.Q2Ln11) - GetCurrency(IA2210Sp.Q1Est) - GetCurrency(IA2210Sp.Q2est))

def Q2UnPay2_Calculation():
    if GetDate(IAStateEst.SPStQ3Date) < datetime.datetime(10, 1, 2018):
        ReturnVal = MaxValue(0, GetCurrency(IAPenaltySp.Q2UnPay1) - GetCurrency(IAStateEst.SPStQ3))
    else:
        ReturnVal = 0

def Q3Days1_Calculation():
    if GetDate(IAStateEst.SPStQ4Date) < datetime.datetime(12, 31, 2018):
        ReturnVal = MaxValue(0, DaysDiff(GetDate(IAStateEst.SPStQ4Date), datetime.datetime(10, 1, 2018)))
    else:
        ReturnVal = 91

def Q3Days2_Calculation():
    if GetDate(IAStateEst.SPStQ4Date) < datetime.datetime(12, 31, 2018) and GetCurrency(IAPenaltySp.Q3UnPay2) > 0:
        ReturnVal = MaxValue(0, DaysDiff(datetime.datetime(12, 31, 2018), GetDate(IAStateEst.SPStQ4Date)))
    else:
        ReturnVal = 0

def Q3Days3_Calculation():
    if GetDate(IAStateEst.SPStQ4Date) < datetime.datetime(1, 31, 2019) and GetDate(IAStateEst.SPStQ4Date) > datetime.datetime(12, 31, 2018):
        ReturnVal = MaxValue(0, DaysDiff(GetDate(IAStateEst.SPStQ4Date), datetime.datetime(12, 31, 2018)))
    elif GetCurrency(IAPenaltySp.Q3Unpay3) >= 0:
        ReturnVal = 31
    else:
        ReturnVal = 0

def Q3Days4_Calculation():
    if GetDate(IAStateEst.SPStQ4Date) > datetime.datetime(12, 31, 2018) and GetDate(IAStateEst.SPStQ4Date) < datetime.datetime(1, 31, 2019) and GetCurrency(IAPenaltySp.Q3Unpay4) > 0:
        ReturnVal = MaxValue(0, DaysDiff(datetime.datetime(1, 31, 2019), GetDate(IAStateEst.SPStQ4Date)))
    else:
        ReturnVal = 0

def Q3Pen1_Calculation():
    ReturnVal = CCur(Round(( GetFloat(IAPenaltySp.Q3Days1) / 365 )  * 0.06 * GetFloat(IAPenaltySp.Q3Unpay1)))

def Q3Pen2_Calculation():
    ReturnVal = CCur(Round(( GetFloat(IAPenaltySp.Q3Days2) / 365 )  * 0.06 * GetFloat(IAPenaltySp.Q3UnPay2)))

def Q3Pen3_Calculation():
    ReturnVal = CCur(Round(( GetFloat(IAPenaltySp.Q3Days3) / 365 )  * 0.07 * GetFloat(IAPenaltySp.Q3Unpay3)))

def Q3Pen4_Calculation():
    ReturnVal = CCur(Round(( GetFloat(IAPenaltySp.Q3Days4) / 365 )  * 0.07 * GetFloat(IAPenaltySp.Q3Unpay4)))

def Q3Unpay1_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2210Sp.Q1Ln11) + GetCurrency(IA2210Sp.Q2Ln11) + GetCurrency(IA2210Sp.Q3Ln11) - GetCurrency(IA2210Sp.Q1Est) - GetCurrency(IA2210Sp.Q2est) - GetCurrency(IA2210Sp.Q3Est))

def Q3UnPay2_Calculation():
    if GetDate(IAStateEst.SPStQ4Date) < datetime.datetime(12, 31, 2018):
        ReturnVal = MaxValue(0, GetCurrency(IAPenaltySp.Q3Unpay1) - GetCurrency(IAStateEst.SPStQ4))
    else:
        ReturnVal = 0

def Q3Unpay3_Calculation():
    if GetCurrency(IAPenaltySp.Q3UnPay2) > 0:
        ReturnVal = GetCurrency(IAPenaltySp.Q3UnPay2)
    elif GetDate(IAStateEst.SPStQ4Date) < datetime.datetime(1, 1, 2019):
        ReturnVal = MaxValue(0, GetCurrency(IAPenaltySp.Q3Unpay1) - GetCurrency(IAStateEst.SPStQ4))
    else:
        ReturnVal = GetCurrency(IAPenaltySp.Q3Unpay1)

def Q3Unpay4_Calculation():
    if GetDate(IAStateEst.SPStQ4Date) > datetime.datetime(12, 31, 2018) and GetDate(IAStateEst.SPStQ4Date) < datetime.datetime(1, 31, 2019):
        ReturnVal = MaxValue(0, GetCurrency(IAPenaltySp.Q3Unpay1) - GetCurrency(IAStateEst.SPStQ4))
    else:
        ReturnVal = 0

def Q4Days1_Calculation():
    # 89 days max in 2018
    if GetDate(IAStateEst.SPStLateDate) < GetDate(IAF1040.DateDuePaid) and GetCurrency(IAStateEst.SPStLate) > 0:
        ReturnVal = MaxValue(0, DaysDiff(GetDate(IAStateEst.SPStLateDate), datetime.datetime(1, 31, 2019)))
    else:
        ReturnVal = MaxValue(0, DaysDiff(GetDate(IAF1040.DateDuePaid), datetime.datetime(1, 31, 2019)))

def Q4Days2_Calculation():
    if GetDate(IAStateEst.SPStLateDate) < datetime.datetime(4, 30, 2019) and GetCurrency(IAPenaltySp.Q4Unpay2) > 0:
        ReturnVal = MaxValue(0, DaysDiff(GetDate(IAF1040.DateDuePaid), GetDate(IAStateEst.SPStLateDate)))
    else:
        ReturnVal = 0

def Q4Pen1_Calculation():
    ReturnVal = CCur(Round(( GetFloat(IAPenaltySp.Q4Days1) / 365 )  * 0.07 * GetFloat(IAPenaltySp.Q4UnPay1)))

def Q4Pen2_Calculation():
    ReturnVal = CCur(Round(( GetFloat(IAPenaltySp.Q4Days2) / 365 )  * 0.07 * GetFloat(IAPenaltySp.Q4Unpay2)))

def Q4UnPay1_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2210Sp.Q1Ln11) + GetCurrency(IA2210Sp.Q2Ln11) + GetCurrency(IA2210Sp.Q3Ln11) + GetCurrency(IA2210Sp.Q4Ln11) - GetCurrency(IA2210Sp.Q1Est) - GetCurrency(IA2210Sp.Q2est) - GetCurrency(IA2210Sp.Q3Est) - GetCurrency(IA2210Sp.Q4Est))

def Q4Unpay2_Calculation():
    if GetDate(IAStateEst.SPStLateDate) < datetime.datetime(4, 30, 2019) and GetCurrency(IAStateEst.SPStLate) > 0:
        ReturnVal = MaxValue(0, GetCurrency(IAPenaltySp.Q4UnPay1) - GetCurrency(IAStateEst.SPStLate))
    else:
        ReturnVal = 0

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SpouseSSN)

def TotPen_Calculation():
    if GetBool(IAF1040.CombMFS) == False:
        ReturnVal = 0
    else:
        ReturnVal = Round(GetCurrency(IAPenaltySp.Q1Pen1) + GetCurrency(IAPenaltySp.Q1Pen2) + GetCurrency(IAPenaltySp.Q2Pen1) + GetCurrency(IAPenaltySp.Q2Pen2) + GetCurrency(IAPenaltySp.Q3Pen1) + GetCurrency(IAPenaltySp.Q3Pen2) + GetCurrency(IAPenaltySp.Q3Pen3) + GetCurrency(IAPenaltySp.Q3Pen4) + GetCurrency(IAPenaltySp.Q4Pen1) + GetCurrency(IAPenaltySp.Q4Pen2))

