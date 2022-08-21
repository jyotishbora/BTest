from forms.out import IA100
from forms.out import IA133
from forms.out import IAF1040
from forms.out import IAREQUIRED
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Common_Calculation():
    if get_bool(IAF1040.MFJ) == True:
        return get_string(USWBasicInfo.CombFirst)
    else:
        return get_string(USWBasicInfo.TPCommon)

def IA133Applied_Calculation():
    return get_currency(IA133.NewJobCr)

def IncreaseEmpPerc_Calculation():
    TopLim = Double()
    if get_float(IA133.Base) <= 0:
        return 0.10
    else:
        TopLim = Round(get_float(IA133.TotEligNewJobs) / get_float(IA133.Base), 3)
        return max_value(0, TopLim)

def MEF133SP_Calculation():
    if get_bool(IA133.Spouse) == True and get_bool(IA133.Print) == True:
        return 1
    else:
        return 0

def MEF133TP_Calculation():
    if get_bool(IA133.Taxpayer) == True and get_bool(IA133.Print) == True:
        return 1
    else:
        return 0

def Names_Calculation():
    if get_bool(IA100.Spouse) == True:
        return get_string(IAREQUIRED.SPCombName)
    else:
        return get_string(IAREQUIRED.TPCombName)

def ProjectJobs_Calculation():
    return get_number(IA133.SchATotHours)

def SchATotHours_Calculation():
    count = Integer()

    SubTot = Integer()
    count = 0
    SubTot = 0
    while count < 14:
        SubTot = SubTot + get_number(IA133.SchAHours(count))
        count = count + 1
    return SubTot

def SchATotTaxWages_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 14:
        SubTot = SubTot + get_currency(IA133.SchATaxWages(count))
        count = count + 1
    return SubTot

def SpouseCommon_Calculation():
    if get_bool(IAF1040.CombMFS) == True:
        return get_string(USWBasicInfo.SPCommon)
    else:
        return 'Not Applicable'

def SSN_Calculation():
    if get_bool(IA100.Spouse) == True:
        return get_string(IAF1040.SpouseSSN)
    else:
        return get_string(IAF1040.SSN)

def TotEligNewJobs_Calculation():
    return min_value(get_number(IA133.TotSchBHoursShare), get_number(IA133.TotEmplGain))

def TotEmplGain_Calculation():
    return get_number(IA133.TotNewJobs) - get_number(IA133.Base)

def TotSchBHoursShare_Calculation():
    return get_number(IA133.ProjectJobs) + get_number(IA133.TotSchAHoursShare)


