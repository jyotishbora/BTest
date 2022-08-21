from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Add_Calculation():
    ReturnVal = GetString(IAF1040.Add)

def CityComb_Calculation():
    ReturnVal = GetString(IAF1040.CityComb)

def CombNames_Calculation():
    ReturnVal = GetString(IARequired.CombNames)

def Desc_Calculation():
    ReturnVal = 'Payment Voucher - ' + GetString(IA1040V.TotDue)

def PeriodEnd_Calculation():
    ReturnVal = '123118'

def Phone_Calculation():
    ReturnVal = GetString(IAF1040.Phone)

def PrVou_Calculation():
    if GetCurrency(IA1040V.TotDue) > 0 and GetBool(IAEFWksht.Yes) == True:
        ReturnVal = 1
    elif GetCurrency(IA1040V.TotDue) > 0 and GetBool(IAEFWksht.EFW) == False:
        ReturnVal = 1
    else:
        ReturnVal = 0

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

def TotDue_Calculation():
    ReturnVal = GetCurrency(IAF1040.TotDue)

