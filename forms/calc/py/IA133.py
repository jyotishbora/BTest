from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Common_Calculation():
    if GetBool(IAF1040.MFJ) == True:
        ReturnVal = GetString(USWBasicInfo.CombFirst)
    else:
        ReturnVal = GetString(USWBasicInfo.TPCommon)

def IA133Applied_Calculation():
    ReturnVal = GetCurrency(IA133.NewJobCr)

def IncreaseEmpPerc_Calculation():
    TopLim = Double()
    if GetFloat(IA133.Base) <= 0:
        ReturnVal = 0.10
    else:
        TopLim = Round(GetFloat(IA133.TotEligNewJobs) / GetFloat(IA133.Base), 3)
        ReturnVal = MaxValue(0, TopLim)

def MEF133SP_Calculation():
    if GetBool(IA133.Spouse) == True and GetBool(IA133.Print) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

def MEF133TP_Calculation():
    if GetBool(IA133.Taxpayer) == True and GetBool(IA133.Print) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Names_Calculation():
    if GetBool(IA100.Spouse) == True:
        ReturnVal = GetString(IARequired.SPCombName)
    else:
        ReturnVal = GetString(IARequired.TPCombName)

def ProjectJobs_Calculation():
    ReturnVal = GetNumber(IA133.SchATotHours)

def SchATotHours_Calculation():
    count = Integer()

    SubTot = Integer()
    count = 0
    SubTot = 0
    while count < 14:
        SubTot = SubTot + GetNumber(IA133.SchAHours(count))
        count = count + 1
    ReturnVal = SubTot

def SchATotTaxWages_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 14:
        SubTot = SubTot + GetCurrency(IA133.SchATaxWages(count))
        count = count + 1
    ReturnVal = SubTot

def SpouseCommon_Calculation():
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetString(USWBasicInfo.SPCommon)
    else:
        ReturnVal = 'Not Applicable'

def SSN_Calculation():
    if GetBool(IA100.Spouse) == True:
        ReturnVal = GetString(IAF1040.SpouseSSN)
    else:
        ReturnVal = GetString(IAF1040.SSN)

def TotEligNewJobs_Calculation():
    ReturnVal = MinValue(GetNumber(IA133.TotSchBHoursShare), GetNumber(IA133.TotEmplGain))

def TotEmplGain_Calculation():
    ReturnVal = GetNumber(IA133.TotNewJobs) - GetNumber(IA133.Base)

def TotSchBHoursShare_Calculation():
    ReturnVal = GetNumber(IA133.ProjectJobs) + GetNumber(IA133.TotSchAHoursShare)

