from forms.out import IA1040X
from forms.out import IA1040XV
from forms.out import IAREQUIRED
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Add_Calculation():
    return get_string(IA1040X.Add)

def CityComb_Calculation():
    return get_string(IA1040X.City)

def CombNames_Calculation():
    return get_string(IAREQUIRED.CombNames)

def Desc_Calculation():
    return 'Payment Voucher - ' + get_string(IA1040XV.TotDue)

def PeriodEnd_Calculation():
    return '123118'

def Phone_Calculation():
    return get_string(IA1040X.Phone)

def PrVou_Calculation():
    if get_currency(IA1040XV.TotDue) > 0:
        return 1
    else:
        return 0

def SSN_Calculation():
    return get_string(IA1040X.SSN)

def TotDue_Calculation():
    return get_currency(IA1040X.TotDue)


