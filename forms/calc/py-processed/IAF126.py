from forms.out import IA6251
from forms.out import IA6251SP
from forms.out import IAF1040
from forms.out import IAF126
from forms.out import IANROTHADJ
from forms.out import IANROTHINC
from forms.out import IAREQUIRED
from forms.out import IAWPENEXC
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *
import datetime



def AAlimony_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpPYRes) == True )  or get_bool(IAF126.TpPYRes) == True:
        return get_currency(IAF1040.AAlimony)
    else:
        return 0

def AAllSource_Calculation():
    if get_bool(IAF126.TpPYNR) == True:
        return get_currency(IAF1040.ANet)
    else:
        return 0

def ABusInc_Calculation():
    #made change based on user story 445128 to calculate when a nonresident, for past 10 years lines 1-14 only calced when a part-year res. Based on Iowa 126 instructions decided to calc lines 5, 7, 10, 11, 12, 13, and 14 when a NR/PY to be conservative.
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAF1040.ABusInc)
    else:
        return 0

def ACapGain_Calculation():
    #decided to change this to be same as line 5, 7, 10, 11, 12, 13. Leaving lines 1-4 and 8 and 9 as they have specific instructions.
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAF1040.ACapGain)
    else:
        return 0

def ACredit_Calculation():
    return c_dollar(get_float(IAF126.ANetTax) * get_float(IAF126.ACrPer))

def ACrPer_Calculation():
    if get_bool(IAF126.TpPYNR) == True:
        return max_value(0, 1 - get_float(IAF126.AIAPer))
    else:
        return 0

def ADividend_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpPYRes) == True )  or get_bool(IAF126.TpPYRes) == True:
        return get_currency(IAF1040.ADividend)
    else:
        return 0

def AFarm_Calculation():
    #made change based on user story 445128 to calculate when a nonresident, for past 10 years lines 1-14 only calced when a part-year res. Based on Iowa 126 instructions decided to calc lines 5, 7, 10, 11, 12, 13, and 14 when a NR/PY to be conservative.
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAF1040.AFarm)
    else:
        return 0

def AGamble_Calculation():
    #made change based on user story 445128 to calculate when a nonresident, for past 10 years lines 1-14 only calced when a part-year res. Based on Iowa 126 instructions decided to calc lines 5, 7, 10, 11, 12, 13, and 14 when a NR/PY to be conservative.
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAF1040.AGamble)
    else:
        return 0

def AIATax_Calculation():
    if get_bool(IAF126.TpPYNR) == True:
        return get_currency(IAF1040.AAltTax)
    else:
        return 0

def AInterest_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpPYRes) == True )  or get_bool(IAF126.TpPYRes) == True:
        return get_currency(IAF1040.AInterest)
    else:
        return 0

def AIRA_Calculation():
    if IAFS() == 3:
        return get_currency(IAWPENEXC.NRTPIRA)
    else:
        return get_currency(IAWPENEXC.NRTPIRA) + get_currency(IAWPENEXC.NRSPIRA)

def AMove_Calculation():
    if get_bool(IAF126.TpPYRes) == True:
        if GetDate(IAF126.TpDateIn) > datetime.datetime(12, 31, 2017) and GetDate(IAF126.TpDateOut) == 0:
            return get_currency(IAF1040.AMove)
        else:
            return 0
    else:
        return 0

def ANet_Calculation():
    return get_currency(IAF126.GrossInc) - get_currency(IAF126.ATotAdj)

def ANetTax_Calculation():
    return max_value(0, get_currency(IAF126.AIATax) - get_currency(IAF126.ATotCr))

def AOthAdj_Calculation():
    if IAFS() == 3:
        return get_currency(IANROTHADJ.TPTot)
    else:
        return get_currency(IANROTHADJ.TPTot) + get_currency(IANROTHADJ.SPTot)

def AOtherInc_Calculation():
    if IAFS() == 3:
        return get_currency(IANROTHINC.TPTot)
    else:
        return get_currency(IANROTHINC.TPTot) + get_currency(IANROTHINC.SPTot)

def AOthGain_Calculation():
    #made change based on user story 445128 to calculate when a nonresident, for past 10 years lines 1-14 only calced when a part-year res. Based on Iowa 126 instructions decided to calc lines 5, 7, 10, 11, 12, 13, and 14 when a NR/PY to be conservative.
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAF1040.AOthGain)
    else:
        return 0

def APenExcl_Calculation():
    if IAFS() == 3:
        return get_currency(IAWPENEXC.NRTPPenExc)
    else:
        return get_currency(IAWPENEXC.NRTPPenExc) + get_currency(IAWPENEXC.NRSPPenExc)

def APensions_Calculation():
    if IAFS() == 3:
        return get_currency(IAWPENEXC.NRTPPensions)
    else:
        return get_currency(IAWPENEXC.NRTPPensions) + get_currency(IAWPENEXC.NRSPPensions)

def ARents_Calculation():
    #made change based on user story 445128 to calculate when a nonresident, for past 10 years lines 1-14 only calced when a part-year res. Based on Iowa 126 instructions decided to calc lines 5, 7, 10, 11, 12, 13, and 14 when a NR/PY to be conservative.
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAF1040.ARents)
    else:
        return 0

def AIAPer_Calculation():
    TopLim = Double()
    if get_bool(IAF126.IANotReqFIle) == True:
        return 0
    elif get_bool(IAF126.TpPYNR) == True:
        if get_float(IAF126.AAllSource) <= 0:
            return 1
        else:
            TopLim = min_value(1, Round(get_float(IAF126.ANet) / get_float(IAF126.AAllSource), 3))
            return max_value(0, TopLim)
    else:
        return 0

def ATotAdj_Calculation():
    if get_bool(IAF126.TpPYNR) == True:
        return get_currency(IAF126.AKeogh) + get_currency(IAF126.ABusIncL) + get_currency(IAF126.AHealth) + get_currency(IAF126.APenalty) + get_currency(IAF126.AAlimonyP) + get_currency(IAF126.APenExcl) + get_currency(IAF126.AMove) + get_currency(IAF126.AGainDed) + get_currency(IAF126.AOthAdj)
    else:
        return 0

def ATotCr_Calculation():
    if get_bool(IAF126.TpPYNR) == True:
        return get_currency(IAF1040.ACredits)
    else:
        return 0

def AUnemp_Calculation():
    #made change based on user story 445128 to calculate when a nonresident, for past 10 years lines 1-14 only calced when a part-year res. Based on Iowa 126 instructions decided to calc lines 5, 7, 10, 11, 12, 13, and 14 when a NR/PY to be conservative.
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAF1040.AUnemp)
    else:
        return 0

def AWages_Calculation():
    if IAFS() == 2 and  ( get_bool(IAF126.SpRes) == False or get_bool(IAF126.TpRes) == False ) :
        return max_value(get_currency(IAF126.TpWages), get_currency(IAF126.TpIAWages)) + max_value(get_currency(IAF126.SpWages), get_currency(IAF126.SpIAWages))
    elif get_bool(IAF126.TpRes) == False:
        return max_value(get_currency(IAF126.TpWages), get_currency(IAF126.TpIAWages))
    else:
        return 0

def BAlimony_Calculation():
    if get_bool(IAF1040.CombMFS) == True and get_bool(IAF126.SpPYRes) == True:
        return get_currency(IAF1040.BAlimony)
    else:
        return 0

def BAllSource_Calculation():
    if get_bool(IAF126.SpPYNR) == True:
        return get_currency(IAF1040.BNet)
    else:
        return 0

def BBusInc_Calculation():
    #made change based on user story 445128 to calculate when a nonresident, for past 10 years lines 1-14 only calced when a part-year res. Based on Iowa 126 instructions decided to calc lines 5, 7, 10, 11, 12, 13, and 14 when a NR/PY to be conservative.
    if get_bool(IAF1040.CombMFS) == True and get_bool(IAF126.SpRes) == False:
        return get_currency(IAF1040.BBusInc)
    else:
        return 0

def BCapGain_Calculation():
    #decided to change this to be same as line 5, 7, 10, 11, 12, 13. Leaving lines 1-4 and 8 and 9 as they have specific instructions.
    if get_bool(IAF1040.CombMFS) == True and get_bool(IAF126.SpRes) == False:
        return get_currency(IAF1040.BCapGain)
    else:
        return 0

def BCredit_Calculation():
    return c_dollar(get_float(IAF126.BNetTax) * get_float(IAF126.BCrPer))

def BCrPer_Calculation():
    if get_bool(IAF126.SpPYNR) == True:
        return max_value(0, 1 - get_float(IAF126.BIAPer))
    else:
        return 0

def BDividend_Calculation():
    if get_bool(IAF1040.CombMFS) == True and get_bool(IAF126.SpPYRes) == True:
        return get_currency(IAF1040.BDividend)
    else:
        return 0

def BFarm_Calculation():
    #made change based on user story 445128 to calculate when a nonresident, for past 10 years lines 1-14 only calced when a part-year res. Based on Iowa 126 instructions decided to calc lines 5, 7, 10, 11, 12, 13, and 14 when a NR/PY to be conservative.
    if get_bool(IAF1040.CombMFS) == True and get_bool(IAF126.SpRes) == False:
        return get_currency(IAF1040.BFarm)
    else:
        return 0

def BGamble_Calculation():
    #made change based on user story 445128 to calculate when a nonresident, for past 10 years lines 1-14 only calced when a part-year res. Based on Iowa 126 instructions decided to calc lines 5, 7, 10, 11, 12, 13, and 14 when a NR/PY to be conservative.
    if get_bool(IAF1040.CombMFS) == True and get_bool(IAF126.SpRes) == False:
        return get_currency(IAF1040.BGamble)
    else:
        return 0

def BGross_Calculation():
    if get_bool(IAF126.SpPYNR) == True:
        return get_currency(IAF126.BWages) + get_currency(IAF126.BInterest) + get_currency(IAF126.BDividend) + get_currency(IAF126.BAlimony) + get_currency(IAF126.BBusInc) + get_currency(IAF126.BCapGain) + get_currency(IAF126.BOthGain) + get_currency(IAF126.BIRA) + get_currency(IAF126.BPensions) + get_currency(IAF126.BRents) + get_currency(IAF126.BFarm) + get_currency(IAF126.BUnemp) + get_currency(IAF126.BGamble) + get_currency(IAF126.BOtherInc)
    else:
        return 0

def BIATax_Calculation():
    if get_bool(IAF126.SpPYNR) == True:
        return get_currency(IAF1040.BAltTax)
    else:
        return 0

def BInterest_Calculation():
    if get_bool(IAF1040.CombMFS) == True and get_bool(IAF126.SpPYRes) == True:
        return get_currency(IAF1040.BInterest)
    else:
        return 0

def BIRA_Calculation():
    if IAFS() == 3:
        return get_currency(IAWPENEXC.NRSPIRA)
    else:
        return 0

def BMove_Calculation():
    if IAFS() == 3 and get_bool(IAF126.SpPYRes) == True:
        if GetDate(IAF126.SpDateIn) > datetime.datetime(12, 31, 2017) and GetDate(IAF126.SpDateOut) == 0:
            return get_currency(IAF1040.BMove)
        else:
            return 0
    else:
        return 0

def BNet_Calculation():
    return get_currency(IAF126.BGross) - get_currency(IAF126.BTotAdj)

def BNetTax_Calculation():
    return max_value(0, get_currency(IAF126.BIATax) - get_currency(IAF126.BTotCr))

def BOthAdj_Calculation():
    if get_bool(IAF126.SpPYNR) == True:
        return get_currency(IANROTHADJ.SPTot)
    else:
        return 0

def BOtherInc_Calculation():
    if get_bool(IAF126.SpPYNR) == True:
        return get_currency(IANROTHINC.SPTot)
    else:
        return 0

def BOthGain_Calculation():
    #made change based on user story 445128 to calculate when a nonresident, for past 10 years lines 1-14 only calced when a part-year res. Based on Iowa 126 instructions decided to calc lines 5, 7, 10, 11, 12, 13, and 14 when a NR/PY to be conservative.
    if get_bool(IAF1040.CombMFS) == True and get_bool(IAF126.SpRes) == False:
        return get_currency(IAF1040.BOthGain)
    else:
        return 0

def BPenExcl_Calculation():
    if get_bool(IAF126.SpPYNR) == True:
        return get_currency(IAWPENEXC.NRSPPenExc)
    else:
        return 0

def BPensions_Calculation():
    if IAFS() == 3:
        return get_currency(IAWPENEXC.NRSPPensions)
    else:
        return 0

def BRents_Calculation():
    #made change based on user story 445128 to calculate when a nonresident, for past 10 years lines 1-14 only calced when a part-year res. Based on Iowa 126 instructions decided to calc lines 5, 7, 10, 11, 12, 13, and 14 when a NR/PY to be conservative.
    if get_bool(IAF1040.CombMFS) == True and get_bool(IAF126.SpRes) == False:
        return get_currency(IAF1040.BRents)
    else:
        return 0

def BIAPer_Calculation():
    TopLim = Double()
    if get_bool(IAF126.IANotReqFIle) == True:
        return 0
    elif get_bool(IAF126.SpPYNR) == True:
        if get_float(IAF126.BAllSource) <= 0:
            return 1
        else:
            TopLim = min_value(1, Round(get_float(IAF126.BNet) / get_float(IAF126.BAllSource), 3))
            return max_value(0, TopLim)
    else:
        return 0

def BTotAdj_Calculation():
    if get_bool(IAF126.SpPYNR) == True:
        return get_currency(IAF126.BKeogh) + get_currency(IAF126.BBusIncL) + get_currency(IAF126.BHealth) + get_currency(IAF126.BPenalty) + get_currency(IAF126.BAlimonyP) + get_currency(IAF126.BPenExcl) + get_currency(IAF126.BMove) + get_currency(IAF126.BGainDed) + get_currency(IAF126.BOthAdj)
    else:
        return 0

def BTotCr_Calculation():
    if get_bool(IAF126.SpPYNR) == True:
        return get_currency(IAF1040.BCredits)
    else:
        return 0

def BUnemp_Calculation():
    #made change based on user story 445128 to calculate when a nonresident, for past 10 years lines 1-14 only calced when a part-year res. Based on Iowa 126 instructions decided to calc lines 5, 7, 10, 11, 12, 13, and 14 when a NR/PY to be conservative.
    if get_bool(IAF1040.CombMFS) == True and get_bool(IAF126.SpRes) == False:
        return get_currency(IAF1040.BUnemp)
    else:
        return 0

def BWages_Calculation():
    if get_bool(IAF126.SpPYNR) == True:
        return max_value(get_currency(IAF126.SpWages), get_currency(IAF126.SpIAWages))
    else:
        return 0

def Desc_Calculation():
    Total = Currency()
    Total = get_currency(IAF126.BCredit) + get_currency(IAF126.ACredit)
    return CStr(Total) + ' Credit'

def Exist_Calculation():
    return 1

def GrossInc_Calculation():
    if get_bool(IAF126.TpPYNR) == True:
        return get_currency(IAF126.AWages) + get_currency(IAF126.AInterest) + get_currency(IAF126.ADividend) + get_currency(IAF126.AAlimony) + get_currency(IAF126.ABusInc) + get_currency(IAF126.ACapGain) + get_currency(IAF126.AOthGain) + get_currency(IAF126.AIRA) + get_currency(IAF126.APensions) + get_currency(IAF126.ARents) + get_currency(IAF126.AFarm) + get_currency(IAF126.AUnemp) + get_currency(IAF126.AGamble) + get_currency(IAF126.AOtherInc)
    else:
        return 0

def IANotReqFIle_Calculation():
    if get_bool(IAF1040.MFS) == True:
        return 0
    elif get_currency(IAF126.BNet) + get_currency(IAF126.ANet) >= Decimal("1000"):
        return 0
    elif get_currency(IA6251.AMT) > 0 or get_currency(IA6251SP.AMT) > 0:
        return 0
    elif get_currency(IAF1040.BLump) > 0 or get_currency(IAF1040.ALump) > 0:
        return 0
    else:
        return 1

def Names_Calculation():
    return get_string(IAREQUIRED.CombNames)

def Print_Calculation():
    if get_bool(IAF126.TpPYNR) == True or get_bool(IAF126.SpPYNR) == True:
        return 1
    else:
        return 0

def SpIAWages_Calculation():
    count1 = Long()

    HowManyW2 = Long()

    Total1 = Currency()

    W2Index = Long()

    StEpWage = Currency()

    AllW2Wage = Currency()

    OthWages = Currency()
    count1 = 1
    HowManyW2 = GetAllCopies(USDW2)
    Total1 = 0
    StEpWage = 0
    while count1 <= HowManyW2:
        W2Index = 0
        while W2Index < 8:
            if get_string(USDW2.St(W2Index), count1) == 'IA' and get_bool(USDW2.Stat, count1) == False and get_bool(USDW2.Spouse, count1) == True:
                Total1 = Total1 + Round(get_currency(USDW2.StWages(W2Index), count1))
            W2Index = W2Index + 1
        count1 = count1 + 1
    while count1 <= HowManyW2:
        if get_bool(USDW2.Stat, count1) == True and get_bool(USDW2.Spouse, count1) == True:
            StEpWage = StEpWage + Round(get_currency(USDW2.Wages, count1))
        count1 = count1 + 1
    AllW2Wage = get_currency(USDW2.Wages, FieldCopies(USDW2.Spouse))
    OthWages = get_currency(USWRec.SWages) - Round(AllW2Wage - StEpWage)
    return Total1 + OthWages

def SpNonRes_Calculation():
    if get_bool(IAF1040.MFJ) == True or get_bool(IAF1040.CombMFS) == True:
        if get_bool(USWResidency.F1040NR) == False:
            return 0
        else:
            return 1
    else:
        return 0

def SpPYNR_Calculation():
    if get_bool(IAF1040.CombMFS) == True and get_bool(IAF126.SpRes) == False:
        return 1
    else:
        return 0

def SpRes_Calculation():
    if get_bool(IAF1040.MFJ) == True or get_bool(IAF1040.CombMFS) == True:
        if get_bool(USWResidency.F1040NR) == False:
            return 1
        else:
            return 0
    else:
        return 0

def SpWages_Calculation():
    count1 = Integer()

    HowManyW2 = Long()

    Total1 = Currency()

    W2Index = Long()
    count1 = 1
    HowManyW2 = GetAllCopies(USDW2)
    Total1 = 0
    while count1 <= HowManyW2:
        W2Index = 0
        while W2Index < 8:
            if get_string(USDW2.St(W2Index), count1) != 'IA' and get_bool(USDW2.Spouse, count1) == True:
                Total1 = Total1 + get_currency(USDW2.StWages(W2Index), count1)
            W2Index = W2Index + 1
        count1 = count1 + 1
    return max_value(0, get_currency(USWRec.SWages) - Total1)

def SSN_Calculation():
    return get_string(IAF1040.SSN)

def TpIAWages_Calculation():
    count1 = Long()

    HowManyW2 = Long()

    Total1 = Currency()

    W2Index = Long()

    StEpWage = Currency()

    AllW2Wage = Currency()

    OthWages = Currency()
    count1 = 1
    HowManyW2 = GetAllCopies(USDW2)
    Total1 = 0
    StEpWage = 0
    while count1 <= HowManyW2:
        W2Index = 0
        while W2Index < 8:
            if get_string(USDW2.St(W2Index), count1) == 'IA' and get_bool(USDW2.Stat, count1) == False and get_bool(USDW2.Taxpayer, count1) == True:
                Total1 = Total1 + Round(get_currency(USDW2.StWages(W2Index), count1))
            W2Index = W2Index + 1
        count1 = count1 + 1
    while count1 <= HowManyW2:
        if get_bool(USDW2.Stat, count1) == True and get_bool(USDW2.Taxpayer, count1) == True:
            StEpWage = StEpWage + Round(get_currency(USDW2.Wages, count1))
        count1 = count1 + 1
    AllW2Wage = get_currency(USDW2.Wages, FieldCopies(USDW2.Taxpayer))
    OthWages = get_currency(USWRec.TWages) - Round(AllW2Wage - StEpWage)
    return Total1 + OthWages

def TpJtDateIn_Calculation():
    if get_bool(IAF126.TpPYRes) == True:
        return get_string(IAF126.TpDateIn)
    elif get_bool(IAF126.TpNonRes) == True:
        return ''
    elif get_bool(IAF1040.MFJ) == True and get_bool(IAF126.SpPYRes) == True:
        return get_string(IAF126.SpDateIn)
    else:
        return ''

def TpJtDateOut_Calculation():
    if get_bool(IAF126.TpPYRes) == True:
        return get_string(IAF126.TpDateOut)
    elif get_bool(IAF126.TpNonRes) == True:
        return ''
    elif get_bool(IAF1040.MFJ) == True and get_bool(IAF126.SpPYRes) == True:
        return get_string(IAF126.SpDateOut)
    else:
        return ''

def TPJtNonRes_Calculation():
    if get_bool(IAF126.TpNonRes) == True:
        return 1
    elif get_bool(IAF126.TpPYRes) == True:
        return 0
    elif get_bool(IAF1040.MFJ) == True and get_bool(IAF126.SpNonRes) == True:
        return 1
    else:
        return 0

def TPJtPYRes_Calculation():
    if get_bool(IAF126.TpPYRes) == True:
        return 1
    elif get_bool(IAF126.TpNonRes) == True:
        return 0
    elif get_bool(IAF1040.MFJ) == True and get_bool(IAF126.SpPYRes) == True:
        return 1
    else:
        return 0

def TpNonRes_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return 0
    else:
        return 1

def TpPYNR_Calculation():
    if get_bool(IAF1040.MFJ) == True:
        if get_bool(IAF126.TpRes) == False or get_bool(IAF126.SpRes) == False:
            return 1
        else:
            return 0
    elif get_bool(IAF126.TpRes) == False:
        return 1
    else:
        return 0

def TpRes_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return 1
    else:
        return 0

def TpWages_Calculation():
    count1 = Integer()

    HowManyW2 = Long()

    Total1 = Currency()

    W2Index = Long()
    count1 = 1
    HowManyW2 = GetAllCopies(USDW2)
    Total1 = 0
    while count1 <= HowManyW2:
        W2Index = 0
        while W2Index < 8:
            if get_string(USDW2.St(W2Index), count1) != 'IA' and get_bool(USDW2.Taxpayer, count1) == True:
                Total1 = Total1 + get_currency(USDW2.StWages(W2Index), count1)
            W2Index = W2Index + 1
        count1 = count1 + 1
    return max_value(0, get_currency(USWRec.TWages) - Total1)


