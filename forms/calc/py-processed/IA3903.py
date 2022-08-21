from forms.out import IA3903
from forms.out import IAF1040
from forms.out import IAREQUIRED
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def AbsL6ML7_Calculation():
    if get_currency(IA3903.L6ML7) < 0:
        return Abs(get_currency(IA3903.L6ML7))
    else:
        return 0

def CodeP_Calculation():
    if get_bool(USF3903.StateNotFed, ParentCopy()) == True:
        return get_currency(USF3903.CodeP, ParentCopy())
    else:
        return 0

def Common_Calculation():
    return get_string(USWBasicInfo.TPCommon)

def Description_Calculation():
    return 'Moving Expenses ' + CStr(get_currency(IA3903.MovExpDdn))

def DNo_Calculation():
    if get_number(IA3903.NewLessOld) < 50:
        return 1
    else:
        return 0

def DYes_Calculation():
    if get_number(IA3903.NewLessOld) >= 50:
        return 1
    else:
        return 0

def Exist_Calculation():
    return 1

def ExReimb_Calculation():
    return get_currency(USF3903.ExReimb, ParentCopy())

def Fed3903_Calculation():
    return 'BEGIN HERE: Open federal Form 3903       Click on the folder to open the supporting document.'

def FedMilNo_Calculation():
    if get_bool(USF3903.EligibleY, ParentCopy()) == True:
        return 0
    else:
        return 1

def FedMilYes_Calculation():
    if get_bool(USF3903.EligibleY, ParentCopy()) == True:
        return 1
    else:
        return 0

def FirstName_Calculation():
    if get_bool(IA3903.Spouse) == True:
        return get_string(IAF1040.SpouseFirst)
    else:
        return get_string(IAF1040.FirstName)

def IAExReimb_Calculation():
    #after testing not sure code P will have an excess for a non military move, also need to review how federal handles the .ExReimb
    #as of 1/2/2019 fed is pulling code P all the time and taking to wages even if a non mil. move, IA instructions appear that could have reimb. from a 2017 move, not sure if should be on fed or if no IA wage adj would be needed, leave codeP def calc an online filable in case user needs to modify
    #if determine not needed could also remove IAREQUIRED fields, but there is a new code/line on the IA1040 line 14 oth inc worksheet.
    return max_value(0, get_currency(IA3903.AbsL6ML7) - get_currency(IA3903.ExReimb))

def Joint_Calculation():
    return get_bool(USF3903.Joint, ParentCopy())

def JtCommon_Calculation():
    return get_string(USWBasicInfo.CombFirst)

def L6ML7_Calculation():
    return get_currency(IA3903.TotalExp) - get_currency(IA3903.CodeP)

def LastName_Calculation():
    if get_bool(IA3903.Spouse) == True:
        return get_string(IAF1040.SpouseLast)
    else:
        return get_string(IAF1040.LastName)

def MoveExp_Calculation():
    if get_bool(IA3903.FedMilYes) == True:
        return 0
    else:
        return get_currency(USF3903.MoveExp, ParentCopy())

def MovExpDdn_Calculation():
    if get_bool(USF3903.StateNotFed, ParentCopy()) == True:
        return max_value(0, get_currency(IA3903.L6ML7))
    else:
        return 0

def NewLessOld_Calculation():
    return max_value(0, get_number(IA3903.ToNewWork) - get_number(IA3903.ToOldWork))

def PrintMe_Calculation():
    if get_currency(IA3903.MovExpDdn) != 0:
        return 1
    else:
        return 0

def Spouse_Calculation():
    return get_bool(USF3903.Spouse, ParentCopy())

def SpouseCommon_Calculation():
    return get_string(USWBasicInfo.SPCommon)

def SSN_Calculation():
    if get_bool(IA3903.Spouse) == True:
        return get_string(IAF1040.SpouseSSN)
    else:
        return get_string(IAF1040.SSN)

def Taxpayer_Calculation():
    return get_bool(USF3903.Taxpayer, ParentCopy())

def ToNewWork_Calculation():
    if get_bool(IA3903.FedMilYes) == True:
        return 0
    else:
        return get_number(USF3903.PrToNewWork, ParentCopy())

def ToOldWork_Calculation():
    if get_bool(IA3903.FedMilYes) == True:
        return 0
    else:
        return get_number(USF3903.PrToOldWork, ParentCopy())

def TotalExp_Calculation():
    if get_bool(USF3903.StateNotFed, ParentCopy()) == True:
        return get_currency(IA3903.MoveExp) + get_currency(IA3903.TravExp)
    else:
        return 0

def TotMoreThanPN_Calculation():
    if get_currency(IA3903.TotalExp) <= get_currency(IA3903.CodeP):
        return 1
    else:
        return 0

def TotMoreThanPY_Calculation():
    if get_currency(IA3903.TotalExp) > get_currency(IA3903.CodeP):
        return 1
    else:
        return 0

def TravExp_Calculation():
    if get_bool(IA3903.FedMilYes) == True:
        return 0
    else:
        return get_currency(USF3903.TravExp, ParentCopy())


