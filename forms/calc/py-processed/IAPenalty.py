from forms.out import IA2210
from forms.out import IAF1040
from forms.out import IAPENALTY
from forms.out import IAREQUIRED
from forms.out import IASTATEEST
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *
import datetime



def DatePaid_Calculation():
    return GetDate(IAF1040.DateDuePaid)

def Desc_Calculation():
    return CStr(get_currency(IAPENALTY.TotPen))

def Exist_Calculation():
    return 1

def Names_Calculation():
    if get_bool(IAF1040.CombMFS) == True:
        return get_string(IAREQUIRED.TPCombName)
    else:
        return get_string(IAREQUIRED.CombNames)

def Q1Days1_Calculation():
    if GetDate(IASTATEEST.TPStQ2Date) < datetime.datetime(7, 2, 2018):
        return max_value(0, DaysDiff(GetDate(IASTATEEST.TPStQ2Date), datetime.datetime(4, 30, 2018)))
    else:
        return 63

def Q1Days2_Calculation():
    if GetDate(IASTATEEST.TPStQ2Date) < datetime.datetime(7, 2, 2018) and get_currency(IAPENALTY.Q1UnPay2) > 0:
        return max_value(0, DaysDiff(datetime.datetime(7, 2, 2018), GetDate(IASTATEEST.TPStQ2Date)))
    else:
        return 0

def Q1Pen1_Calculation():
    return CCur(Round(( get_float(IAPENALTY.Q1Days1) / 365 )  * 0.06 * get_float(IAPENALTY.Q1UnPay1)))

def Q1Pen2_Calculation():
    return CCur(Round(( get_float(IAPENALTY.Q1Days2) / 365 )  * 0.06 * get_float(IAPENALTY.Q1UnPay2)))

def Q1UnPay1_Calculation():
    return get_currency(IA2210.Q1Undpay)

def Q1UnPay2_Calculation():
    if GetDate(IASTATEEST.TPStQ2Date) < datetime.datetime(7, 2, 2018):
        return max_value(0, get_currency(IAPENALTY.Q1UnPay1) - get_currency(IASTATEEST.TPStQ2))
    else:
        return 0

def Q2Days1_Calculation():
    if GetDate(IASTATEEST.TPStQ3Date) < datetime.datetime(10, 1, 2018):
        return max_value(0, DaysDiff(GetDate(IASTATEEST.TPStQ3Date), datetime.datetime(7, 2, 2018)))
    else:
        return 91

def Q2Days2_Calculation():
    if GetDate(IASTATEEST.TPStQ3Date) < datetime.datetime(10, 1, 2018) and get_currency(IAPENALTY.Q2UnPay2) > 0:
        return max_value(0, DaysDiff(datetime.datetime(10, 1, 2018), GetDate(IASTATEEST.TPStQ3Date)))
    else:
        return 0

def Q2Pen1_Calculation():
    return CCur(Round(( get_float(IAPENALTY.Q2Days1) / 365 )  * 0.06 * get_float(IAPENALTY.Q2UnPay1)))

def Q2Pen2_Calculation():
    return CCur(Round(( get_float(IAPENALTY.Q2Days2) / 365 )  * 0.06 * get_float(IAPENALTY.Q2UnPay2)))

def Q2UnPay1_Calculation():
    return max_value(0, get_currency(IA2210.Q1Ln11) + get_currency(IA2210.Q2Ln11) - get_currency(IA2210.Q1Est) - get_currency(IA2210.Q2est))

def Q2UnPay2_Calculation():
    if GetDate(IASTATEEST.TPStQ3Date) < datetime.datetime(10, 1, 2018):
        return max_value(0, get_currency(IAPENALTY.Q2UnPay1) - get_currency(IASTATEEST.TPStQ3))
    else:
        return 0

def Q3Days1_Calculation():
    if GetDate(IASTATEEST.TPStQ4Date) < datetime.datetime(12, 31, 2018):
        return max_value(0, DaysDiff(GetDate(IASTATEEST.TPStQ4Date), datetime.datetime(10, 1, 2018)))
    else:
        return 91

def Q3Days2_Calculation():
    if GetDate(IASTATEEST.TPStQ4Date) < datetime.datetime(12, 31, 2018) and get_currency(IAPENALTY.Q3UnPay2) > 0:
        return max_value(0, DaysDiff(datetime.datetime(12, 31, 2018), GetDate(IASTATEEST.TPStQ4Date)))
    else:
        return 0

def Q3Days3_Calculation():
    if GetDate(IASTATEEST.TPStQ4Date) < datetime.datetime(1, 31, 2019) and GetDate(IASTATEEST.TPStQ4Date) > datetime.datetime(12, 31, 2018):
        return max_value(0, DaysDiff(GetDate(IASTATEEST.TPStQ4Date), datetime.datetime(12, 31, 2018)))
    elif get_currency(IAPENALTY.Q3Unpay3) >= 0:
        return 31
    else:
        return 0

def Q3Days4_Calculation():
    if GetDate(IASTATEEST.TPStQ4Date) > datetime.datetime(12, 31, 2018) and GetDate(IASTATEEST.TPStQ4Date) < datetime.datetime(1, 31, 2019) and get_currency(IAPENALTY.Q3Unpay4) > 0:
        return max_value(0, DaysDiff(datetime.datetime(1, 31, 2019), GetDate(IASTATEEST.TPStQ4Date)))
    else:
        return 0

def Q3Pen1_Calculation():
    return CCur(Round(( get_float(IAPENALTY.Q3Days1) / 365 )  * 0.06 * get_float(IAPENALTY.Q3Unpay1)))

def Q3Pen2_Calculation():
    return CCur(Round(( get_float(IAPENALTY.Q3Days2) / 365 )  * 0.06 * get_float(IAPENALTY.Q3UnPay2)))

def Q3Pen3_Calculation():
    return CCur(Round(( get_float(IAPENALTY.Q3Days3) / 365 )  * 0.07 * get_float(IAPENALTY.Q3Unpay3)))

def Q3Pen4_Calculation():
    return CCur(Round(( get_float(IAPENALTY.Q3Days4) / 365 )  * 0.07 * get_float(IAPENALTY.Q3Unpay4)))

def Q3Unpay1_Calculation():
    return max_value(0, get_currency(IA2210.Q1Ln11) + get_currency(IA2210.Q2Ln11) + get_currency(IA2210.Q3Ln11) - get_currency(IA2210.Q1Est) - get_currency(IA2210.Q2est) - get_currency(IA2210.Q3Est))

def Q3UnPay2_Calculation():
    if GetDate(IASTATEEST.TPStQ4Date) < datetime.datetime(12, 31, 2018):
        return max_value(0, get_currency(IAPENALTY.Q3Unpay1) - get_currency(IASTATEEST.TPStQ4))
    else:
        return 0

def Q3Unpay3_Calculation():
    if get_currency(IAPENALTY.Q3UnPay2) > 0:
        return get_currency(IAPENALTY.Q3UnPay2)
    elif GetDate(IASTATEEST.TPStQ4Date) < datetime.datetime(1, 1, 2019):
        return max_value(0, get_currency(IAPENALTY.Q3Unpay1) - get_currency(IASTATEEST.TPStQ4))
    else:
        return get_currency(IAPENALTY.Q3Unpay1)

def Q3Unpay4_Calculation():
    if GetDate(IASTATEEST.TPStQ4Date) > datetime.datetime(12, 31, 2018) and GetDate(IASTATEEST.TPStQ4Date) < datetime.datetime(1, 31, 2019):
        return max_value(0, get_currency(IAPENALTY.Q3Unpay1) - get_currency(IASTATEEST.TPStQ4))
    else:
        return 0

def Q4Days1_Calculation():
    # 89 days max in 2018
    if GetDate(IASTATEEST.TPStLateDate) < GetDate(IAF1040.DateDuePaid) and get_currency(IASTATEEST.TPStLate) > 0:
        return max_value(0, DaysDiff(GetDate(IASTATEEST.TPStLateDate), datetime.datetime(1, 31, 2019)))
    else:
        return max_value(0, DaysDiff(GetDate(IAF1040.DateDuePaid), datetime.datetime(1, 31, 2019)))

def Q4Days2_Calculation():
    if GetDate(IASTATEEST.TPStLateDate) < datetime.datetime(4, 30, 2019) and get_currency(IAPENALTY.Q4Unpay2) > 0:
        return max_value(0, DaysDiff(GetDate(IAF1040.DateDuePaid), GetDate(IASTATEEST.TPStLateDate)))
    else:
        return 0

def Q4Pen1_Calculation():
    return CCur(Round(( get_float(IAPENALTY.Q4Days1) / 365 )  * 0.07 * get_float(IAPENALTY.Q4UnPay1)))

def Q4Pen2_Calculation():
    return CCur(Round(( get_float(IAPENALTY.Q4Days2) / 365 )  * 0.07 * get_float(IAPENALTY.Q4Unpay2)))

def Q4UnPay1_Calculation():
    return max_value(0, get_currency(IA2210.Q1Ln11) + get_currency(IA2210.Q2Ln11) + get_currency(IA2210.Q3Ln11) + get_currency(IA2210.Q4Ln11) - get_currency(IA2210.Q1Est) - get_currency(IA2210.Q2est) - get_currency(IA2210.Q3Est) - get_currency(IA2210.Q4Est))

def Q4Unpay2_Calculation():
    if GetDate(IASTATEEST.TPStLateDate) < datetime.datetime(4, 30, 2019) and get_currency(IASTATEEST.TPStLate) > 0:
        return max_value(0, get_currency(IAPENALTY.Q4UnPay1) - get_currency(IASTATEEST.TPStLate))
    else:
        return 0

def SSN_Calculation():
    return get_string(IAF1040.SSN)

def TotPen_Calculation():
    return Round(get_currency(IAPENALTY.Q1Pen1) + get_currency(IAPENALTY.Q1Pen2) + get_currency(IAPENALTY.Q2Pen1) + get_currency(IAPENALTY.Q2Pen2) + get_currency(IAPENALTY.Q3Pen1) + get_currency(IAPENALTY.Q3Pen2) + get_currency(IAPENALTY.Q3Pen3) + get_currency(IAPENALTY.Q3Pen4) + get_currency(IAPENALTY.Q4Pen1) + get_currency(IAPENALTY.Q4Pen2))


