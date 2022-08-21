from forms.out import IAF1040
from forms.out import IAREQUIRED
from forms.out import IASTATEEST
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *
import datetime



def Desc_Calculation():
    return CStr(get_currency(IASTATEEST.TotIAEst))

def Exist_Calculation():
    return 1

def MobDisQual_Calculation():
    if get_currency(IASTATEEST.TotIAEst) > 0:
        return 1
    else:
        return 0

def Names_Calculation():
    return get_string(IAREQUIRED.CombNames)

def SPIAEst_Calculation():
    if IAFS() == 3:
        return get_currency(IASTATEEST.SPStApply) + get_currency(IASTATEEST.SPStQ1) + get_currency(IASTATEEST.SPStQ2) + get_currency(IASTATEEST.SPStQ3) + get_currency(IASTATEEST.SPStQ4) + get_currency(IASTATEEST.SPStLate)
    else:
        return 0

def SPName_Calculation():
    return get_string(USWBasicInfo.SPCommon)

def SPStLateDate_Calculation():
    if IAFS() == 3:
        return GetDate(IASTATEEST.TPStLateDate)
    else:
        return ''

def SPStQ1Date_Calculation():
    if IAFS() == 3:
        return GetDate(IASTATEEST.TPStQ1Date)
    else:
        return ''

def SPStQ2Date_Calculation():
    if IAFS() == 3:
        return GetDate(IASTATEEST.TPStQ2Date)
    else:
        return ''

def SPStQ3Date_Calculation():
    if IAFS() == 3:
        return GetDate(IASTATEEST.TPStQ3Date)
    else:
        return ''

def SPStQ4Date_Calculation():
    if IAFS() == 3:
        return GetDate(IASTATEEST.TPStQ4Date)
    else:
        return ''

def SSN_Calculation():
    return get_string(IAF1040.SSN)

def StApply_Calculation():
    if get_string(USWEstPay.StName1) == 'Iowa':
        return get_currency(USWEstPay.StApply)
    elif get_string(USWEstPay.StName2) == 'Iowa':
        return get_currency(USWEstPay.St2Apply)
    elif get_string(USWEstPay.StName3) == 'Iowa':
        return get_currency(USWEstPay.St3Apply)
    else:
        return 0

def StLate_Calculation():
    if get_string(USWEstPay.StName1) == 'Iowa':
        return get_currency(USWEstPay.StLate)
    elif get_string(USWEstPay.StName2) == 'Iowa':
        return get_currency(USWEstPay.St2Late)
    elif get_string(USWEstPay.StName3) == 'Iowa':
        return get_currency(USWEstPay.St3Late)
    else:
        return 0

def StQ1_Calculation():
    if get_string(USWEstPay.StName1) == 'Iowa':
        return get_currency(USWEstPay.StQ1)
    elif get_string(USWEstPay.StName2) == 'Iowa':
        return get_currency(USWEstPay.St2Q1)
    elif get_string(USWEstPay.StName3) == 'Iowa':
        return get_currency(USWEstPay.St3Q1)
    else:
        return 0

def StQ2_Calculation():
    if get_string(USWEstPay.StName1) == 'Iowa':
        return get_currency(USWEstPay.StQ2)
    elif get_string(USWEstPay.StName2) == 'Iowa':
        return get_currency(USWEstPay.St2Q2)
    elif get_string(USWEstPay.StName3) == 'Iowa':
        return get_currency(USWEstPay.St3Q2)
    else:
        return 0

def StQ3_Calculation():
    if get_string(USWEstPay.StName1) == 'Iowa':
        return get_currency(USWEstPay.StQ3)
    elif get_string(USWEstPay.StName2) == 'Iowa':
        return get_currency(USWEstPay.St2Q3)
    elif get_string(USWEstPay.StName3) == 'Iowa':
        return get_currency(USWEstPay.St3Q3)
    else:
        return 0

def StQ4_Calculation():
    if get_string(USWEstPay.StName1) == 'Iowa':
        return get_currency(USWEstPay.StQ4)
    elif get_string(USWEstPay.StName2) == 'Iowa':
        return get_currency(USWEstPay.St2Q4)
    elif get_string(USWEstPay.StName3) == 'Iowa':
        return get_currency(USWEstPay.St3Q4)
    else:
        return 0

def TotIAEst_Calculation():
    return get_currency(IASTATEEST.StApply) + get_currency(IASTATEEST.StQ1) + get_currency(IASTATEEST.StQ2) + get_currency(IASTATEEST.StQ3) + get_currency(IASTATEEST.StQ4) + get_currency(IASTATEEST.StLate)

def TPName_Calculation():
    return get_string(USWBasicInfo.TPCommon)

def TPStApply_Calculation():
    if IAFS() == 3:
        return max_value(0, get_currency(IASTATEEST.StApply) - get_currency(IASTATEEST.SPStApply))
    else:
        return get_currency(IASTATEEST.StApply)

def TPStLate_Calculation():
    if IAFS() == 3:
        return max_value(0, get_currency(IASTATEEST.StLate) - get_currency(IASTATEEST.SPStLate))
    else:
        return get_currency(IASTATEEST.StLate)

def TPStLateDate_Calculation():
    if get_string(USWEstPay.StName1) == 'Iowa':
        return GetDate(USWEstPay.StLateDate)
    elif get_string(USWEstPay.StName2) == 'Iowa':
        return GetDate(USWEstPay.St2LateDate)
    elif get_string(USWEstPay.StName3) == 'Iowa':
        return GetDate(USWEstPay.St3LateDate)
    else:
        return datetime.datetime(4, 30, 2019)

def TPStQ1_Calculation():
    if IAFS() == 3:
        return max_value(0, get_currency(IASTATEEST.StQ1) - get_currency(IASTATEEST.SPStQ1))
    else:
        return get_currency(IASTATEEST.StQ1)

def TPStQ1Date_Calculation():
    if get_string(USWEstPay.StName1) == 'Iowa':
        return GetDate(USWEstPay.StQ1Date)
    elif get_string(USWEstPay.StName2) == 'Iowa':
        return GetDate(USWEstPay.St2Q1Date)
    elif get_string(USWEstPay.StName3) == 'Iowa':
        return GetDate(USWEstPay.St3Q1Date)
    else:
        return datetime.datetime(4, 30, 2018)

def TPStQ2_Calculation():
    if IAFS() == 3:
        return max_value(0, get_currency(IASTATEEST.StQ2) - get_currency(IASTATEEST.SPStQ2))
    else:
        return get_currency(IASTATEEST.StQ2)

def TPStQ2Date_Calculation():
    if get_string(USWEstPay.StName1) == 'Iowa':
        return GetDate(USWEstPay.StQ2Date)
    elif get_string(USWEstPay.StName2) == 'Iowa':
        return GetDate(USWEstPay.St2Q2Date)
    elif get_string(USWEstPay.StName3) == 'Iowa':
        return GetDate(USWEstPay.St3Q2Date)
    else:
        return datetime.datetime(7, 2, 2018)

def TPStQ3_Calculation():
    if IAFS() == 3:
        return max_value(0, get_currency(IASTATEEST.StQ3) - get_currency(IASTATEEST.SPStQ3))
    else:
        return get_currency(IASTATEEST.StQ3)

def TPStQ3Date_Calculation():
    if get_string(USWEstPay.StName1) == 'Iowa':
        return GetDate(USWEstPay.StQ3Date)
    elif get_string(USWEstPay.StName2) == 'Iowa':
        return GetDate(USWEstPay.St2Q3Date)
    elif get_string(USWEstPay.StName3) == 'Iowa':
        return GetDate(USWEstPay.St3Q3Date)
    else:
        return datetime.datetime(10, 1, 2018)

def TPStQ4_Calculation():
    if IAFS() == 3:
        return max_value(0, get_currency(IASTATEEST.StQ4) - get_currency(IASTATEEST.SPStQ4))
    else:
        return get_currency(IASTATEEST.StQ4)

def TPStQ4Date_Calculation():
    if get_string(USWEstPay.StName1) == 'Iowa':
        return GetDate(USWEstPay.StQ4Date)
    elif get_string(USWEstPay.StName2) == 'Iowa':
        return GetDate(USWEstPay.St2Q4Date)
    elif get_string(USWEstPay.StName3) == 'Iowa':
        return GetDate(USWEstPay.St3Q4Date)
    else:
        return datetime.datetime(1, 31, 2019)


