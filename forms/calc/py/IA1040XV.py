from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Add_Calculation():
    ReturnVal = GetString(IA1040X.Add)

def CityComb_Calculation():
    ReturnVal = GetString(IA1040X.City)

def CombNames_Calculation():
    ReturnVal = GetString(IARequired.CombNames)

def Desc_Calculation():
    ReturnVal = 'Payment Voucher - ' + GetString(IA1040XV.TotDue)

def PeriodEnd_Calculation():
    ReturnVal = '123118'

def Phone_Calculation():
    ReturnVal = GetString(IA1040X.Phone)

def PrVou_Calculation():
    if GetCurrency(IA1040XV.TotDue) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def SSN_Calculation():
    ReturnVal = GetString(IA1040X.SSN)

def TotDue_Calculation():
    ReturnVal = GetCurrency(IA1040X.TotDue)

