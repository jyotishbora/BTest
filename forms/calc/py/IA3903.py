from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def AbsL6ML7_Calculation():
    if GetCurrency(IA3903.L6ML7) < 0:
        ReturnVal = Abs(GetCurrency(IA3903.L6ML7))
    else:
        ReturnVal = 0

def CodeP_Calculation():
    if GetBool(USF3903.StateNotFed, ParentCopy()) == True:
        ReturnVal = GetCurrency(USF3903.CodeP, ParentCopy())
    else:
        ReturnVal = 0

def Common_Calculation():
    ReturnVal = GetString(USWBasicInfo.TPCommon)

def Description_Calculation():
    ReturnVal = 'Moving Expenses ' + CStr(GetCurrency(IA3903.MovExpDdn))

def DNo_Calculation():
    if GetNumber(IA3903.NewLessOld) < 50:
        ReturnVal = 1
    else:
        ReturnVal = 0

def DYes_Calculation():
    if GetNumber(IA3903.NewLessOld) >= 50:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Exist_Calculation():
    ReturnVal = 1

def ExReimb_Calculation():
    ReturnVal = GetCurrency(USF3903.ExReimb, ParentCopy())

def Fed3903_Calculation():
    ReturnVal = 'BEGIN HERE: Open federal Form 3903       Click on the folder to open the supporting document.'

def FedMilNo_Calculation():
    if GetBool(USF3903.EligibleY, ParentCopy()) == True:
        ReturnVal = 0
    else:
        ReturnVal = 1

def FedMilYes_Calculation():
    if GetBool(USF3903.EligibleY, ParentCopy()) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

def FirstName_Calculation():
    if GetBool(IA3903.Spouse) == True:
        ReturnVal = GetString(IAF1040.SpouseFirst)
    else:
        ReturnVal = GetString(IAF1040.FirstName)

def IAExReimb_Calculation():
    #after testing not sure code P will have an excess for a non military move, also need to review how federal handles the .ExReimb
    #as of 1/2/2019 fed is pulling code P all the time and taking to wages even if a non mil. move, IA instructions appear that could have reimb. from a 2017 move, not sure if should be on fed or if no IA wage adj would be needed, leave codeP def calc an online filable in case user needs to modify
    #if determine not needed could also remove IARequired fields, but there is a new code/line on the IA1040 line 14 oth inc worksheet.
    ReturnVal = MaxValue(0, GetCurrency(IA3903.AbsL6ML7) - GetCurrency(IA3903.ExReimb))

def Joint_Calculation():
    ReturnVal = GetBool(USF3903.Joint, ParentCopy())

def JtCommon_Calculation():
    ReturnVal = GetString(USWBasicInfo.CombFirst)

def L6ML7_Calculation():
    ReturnVal = GetCurrency(IA3903.TotalExp) - GetCurrency(IA3903.CodeP)

def LastName_Calculation():
    if GetBool(IA3903.Spouse) == True:
        ReturnVal = GetString(IAF1040.SpouseLast)
    else:
        ReturnVal = GetString(IAF1040.LastName)

def MoveExp_Calculation():
    if GetBool(IA3903.FedMilYes) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(USF3903.MoveExp, ParentCopy())

def MovExpDdn_Calculation():
    if GetBool(USF3903.StateNotFed, ParentCopy()) == True:
        ReturnVal = MaxValue(0, GetCurrency(IA3903.L6ML7))
    else:
        ReturnVal = 0

def NewLessOld_Calculation():
    ReturnVal = MaxValue(0, GetNumber(IA3903.ToNewWork) - GetNumber(IA3903.ToOldWork))

def PrintMe_Calculation():
    if GetCurrency(IA3903.MovExpDdn) != 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Spouse_Calculation():
    ReturnVal = GetBool(USF3903.Spouse, ParentCopy())

def SpouseCommon_Calculation():
    ReturnVal = GetString(USWBasicInfo.SPCommon)

def SSN_Calculation():
    if GetBool(IA3903.Spouse) == True:
        ReturnVal = GetString(IAF1040.SpouseSSN)
    else:
        ReturnVal = GetString(IAF1040.SSN)

def Taxpayer_Calculation():
    ReturnVal = GetBool(USF3903.Taxpayer, ParentCopy())

def ToNewWork_Calculation():
    if GetBool(IA3903.FedMilYes) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetNumber(USF3903.PrToNewWork, ParentCopy())

def ToOldWork_Calculation():
    if GetBool(IA3903.FedMilYes) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetNumber(USF3903.PrToOldWork, ParentCopy())

def TotalExp_Calculation():
    if GetBool(USF3903.StateNotFed, ParentCopy()) == True:
        ReturnVal = GetCurrency(IA3903.MoveExp) + GetCurrency(IA3903.TravExp)
    else:
        ReturnVal = 0

def TotMoreThanPN_Calculation():
    if GetCurrency(IA3903.TotalExp) <= GetCurrency(IA3903.CodeP):
        ReturnVal = 1
    else:
        ReturnVal = 0

def TotMoreThanPY_Calculation():
    if GetCurrency(IA3903.TotalExp) > GetCurrency(IA3903.CodeP):
        ReturnVal = 1
    else:
        ReturnVal = 0

def TravExp_Calculation():
    if GetBool(IA3903.FedMilYes) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(USF3903.TravExp, ParentCopy())

