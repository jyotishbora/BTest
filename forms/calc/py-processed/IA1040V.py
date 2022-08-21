from forms.out import IA1040V
from forms.out import IAEFWKSHT
from forms.out import IAF1040
from forms.out import IAREQUIRED
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Add_Calculation():
    return get_string(IAF1040.Add)

def CityComb_Calculation():
    return get_string(IAF1040.CityComb)

def CombNames_Calculation():
    return get_string(IAREQUIRED.CombNames)

def Desc_Calculation():
    return 'Payment Voucher - ' + get_string(IA1040V.TotDue)

def PeriodEnd_Calculation():
    return '123118'

def Phone_Calculation():
    return get_string(IAF1040.Phone)

def PrVou_Calculation():
    if get_currency(IA1040V.TotDue) > 0 and get_bool(IAEFWKSHT.Yes) == True:
        return 1
    elif get_currency(IA1040V.TotDue) > 0 and get_bool(IAEFWKSHT.EFW) == False:
        return 1
    else:
        return 0

def SSN_Calculation():
    return get_string(IAF1040.SSN)

def TotDue_Calculation():
    return get_currency(IAF1040.TotDue)


