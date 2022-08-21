from vb2py.vbfunctions import *
from vb2py.vbdebug import *
import datetime



def AAlimony_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpPYRes) == True )  or GetBool(IAF126.TpPYRes) == True:
        ReturnVal = GetCurrency(IAF1040.AAlimony)
    else:
        ReturnVal = 0

def AAllSource_Calculation():
    if GetBool(IAF126.TpPYNR) == True:
        ReturnVal = GetCurrency(IAF1040.ANet)
    else:
        ReturnVal = 0

def ABusInc_Calculation():
    #made change based on user story 445128 to calculate when a nonresident, for past 10 years lines 1-14 only calced when a part-year res. Based on Iowa 126 instructions decided to calc lines 5, 7, 10, 11, 12, 13, and 14 when a NR/PY to be conservative.
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAF1040.ABusInc)
    else:
        ReturnVal = 0

def ACapGain_Calculation():
    #decided to change this to be same as line 5, 7, 10, 11, 12, 13. Leaving lines 1-4 and 8 and 9 as they have specific instructions.
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAF1040.ACapGain)
    else:
        ReturnVal = 0

def ACredit_Calculation():
    ReturnVal = CDollar(GetFloat(IAF126.ANetTax) * GetFloat(IAF126.ACrPer))

def ACrPer_Calculation():
    if GetBool(IAF126.TpPYNR) == True:
        ReturnVal = MaxValue(0, 1 - GetFloat(IAF126.AIAPer))
    else:
        ReturnVal = 0

def ADividend_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpPYRes) == True )  or GetBool(IAF126.TpPYRes) == True:
        ReturnVal = GetCurrency(IAF1040.ADividend)
    else:
        ReturnVal = 0

def AFarm_Calculation():
    #made change based on user story 445128 to calculate when a nonresident, for past 10 years lines 1-14 only calced when a part-year res. Based on Iowa 126 instructions decided to calc lines 5, 7, 10, 11, 12, 13, and 14 when a NR/PY to be conservative.
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAF1040.AFarm)
    else:
        ReturnVal = 0

def AGamble_Calculation():
    #made change based on user story 445128 to calculate when a nonresident, for past 10 years lines 1-14 only calced when a part-year res. Based on Iowa 126 instructions decided to calc lines 5, 7, 10, 11, 12, 13, and 14 when a NR/PY to be conservative.
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAF1040.AGamble)
    else:
        ReturnVal = 0

def AIATax_Calculation():
    if GetBool(IAF126.TpPYNR) == True:
        ReturnVal = GetCurrency(IAF1040.AAltTax)
    else:
        ReturnVal = 0

def AInterest_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpPYRes) == True )  or GetBool(IAF126.TpPYRes) == True:
        ReturnVal = GetCurrency(IAF1040.AInterest)
    else:
        ReturnVal = 0

def AIRA_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IAWPenExc.NRTPIRA)
    else:
        ReturnVal = GetCurrency(IAWPenExc.NRTPIRA) + GetCurrency(IAWPenExc.NRSPIRA)

def AMove_Calculation():
    if GetBool(IAF126.TpPYRes) == True:
        if GetDate(IAF126.TpDateIn) > datetime.datetime(12, 31, 2017) and GetDate(IAF126.TpDateOut) == 0:
            ReturnVal = GetCurrency(IAF1040.AMove)
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def ANet_Calculation():
    ReturnVal = GetCurrency(IAF126.GrossInc) - GetCurrency(IAF126.ATotAdj)

def ANetTax_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAF126.AIATax) - GetCurrency(IAF126.ATotCr))

def AOthAdj_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IANROthAdj.TPTot)
    else:
        ReturnVal = GetCurrency(IANROthAdj.TPTot) + GetCurrency(IANROthAdj.SPTot)

def AOtherInc_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IANROthInc.TPTot)
    else:
        ReturnVal = GetCurrency(IANROthInc.TPTot) + GetCurrency(IANROthInc.SPTot)

def AOthGain_Calculation():
    #made change based on user story 445128 to calculate when a nonresident, for past 10 years lines 1-14 only calced when a part-year res. Based on Iowa 126 instructions decided to calc lines 5, 7, 10, 11, 12, 13, and 14 when a NR/PY to be conservative.
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAF1040.AOthGain)
    else:
        ReturnVal = 0

def APenExcl_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IAWPenExc.NRTPPenExc)
    else:
        ReturnVal = GetCurrency(IAWPenExc.NRTPPenExc) + GetCurrency(IAWPenExc.NRSPPenExc)

def APensions_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IAWPenExc.NRTPPensions)
    else:
        ReturnVal = GetCurrency(IAWPenExc.NRTPPensions) + GetCurrency(IAWPenExc.NRSPPensions)

def ARents_Calculation():
    #made change based on user story 445128 to calculate when a nonresident, for past 10 years lines 1-14 only calced when a part-year res. Based on Iowa 126 instructions decided to calc lines 5, 7, 10, 11, 12, 13, and 14 when a NR/PY to be conservative.
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAF1040.ARents)
    else:
        ReturnVal = 0

def AIAPer_Calculation():
    TopLim = Double()
    if GetBool(IAF126.IANotReqFIle) == True:
        ReturnVal = 0
    elif GetBool(IAF126.TpPYNR) == True:
        if GetFloat(IAF126.AAllSource) <= 0:
            ReturnVal = 1
        else:
            TopLim = MinValue(1, Round(GetFloat(IAF126.ANet) / GetFloat(IAF126.AAllSource), 3))
            ReturnVal = MaxValue(0, TopLim)
    else:
        ReturnVal = 0

def ATotAdj_Calculation():
    if GetBool(IAF126.TpPYNR) == True:
        ReturnVal = GetCurrency(IAF126.AKeogh) + GetCurrency(IAF126.ABusIncL) + GetCurrency(IAF126.AHealth) + GetCurrency(IAF126.APenalty) + GetCurrency(IAF126.AAlimonyP) + GetCurrency(IAF126.APenExcl) + GetCurrency(IAF126.AMove) + GetCurrency(IAF126.AGainDed) + GetCurrency(IAF126.AOthAdj)
    else:
        ReturnVal = 0

def ATotCr_Calculation():
    if GetBool(IAF126.TpPYNR) == True:
        ReturnVal = GetCurrency(IAF1040.ACredits)
    else:
        ReturnVal = 0

def AUnemp_Calculation():
    #made change based on user story 445128 to calculate when a nonresident, for past 10 years lines 1-14 only calced when a part-year res. Based on Iowa 126 instructions decided to calc lines 5, 7, 10, 11, 12, 13, and 14 when a NR/PY to be conservative.
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAF1040.AUnemp)
    else:
        ReturnVal = 0

def AWages_Calculation():
    if IAFS() == 2 and  ( GetBool(IAF126.SpRes) == False or GetBool(IAF126.TpRes) == False ) :
        ReturnVal = MaxValue(GetCurrency(IAF126.TpWages), GetCurrency(IAF126.TpIAWages)) + MaxValue(GetCurrency(IAF126.SpWages), GetCurrency(IAF126.SpIAWages))
    elif GetBool(IAF126.TpRes) == False:
        ReturnVal = MaxValue(GetCurrency(IAF126.TpWages), GetCurrency(IAF126.TpIAWages))
    else:
        ReturnVal = 0

def BAlimony_Calculation():
    if GetBool(IAF1040.CombMFS) == True and GetBool(IAF126.SpPYRes) == True:
        ReturnVal = GetCurrency(IAF1040.BAlimony)
    else:
        ReturnVal = 0

def BAllSource_Calculation():
    if GetBool(IAF126.SpPYNR) == True:
        ReturnVal = GetCurrency(IAF1040.BNet)
    else:
        ReturnVal = 0

def BBusInc_Calculation():
    #made change based on user story 445128 to calculate when a nonresident, for past 10 years lines 1-14 only calced when a part-year res. Based on Iowa 126 instructions decided to calc lines 5, 7, 10, 11, 12, 13, and 14 when a NR/PY to be conservative.
    if GetBool(IAF1040.CombMFS) == True and GetBool(IAF126.SpRes) == False:
        ReturnVal = GetCurrency(IAF1040.BBusInc)
    else:
        ReturnVal = 0

def BCapGain_Calculation():
    #decided to change this to be same as line 5, 7, 10, 11, 12, 13. Leaving lines 1-4 and 8 and 9 as they have specific instructions.
    if GetBool(IAF1040.CombMFS) == True and GetBool(IAF126.SpRes) == False:
        ReturnVal = GetCurrency(IAF1040.BCapGain)
    else:
        ReturnVal = 0

def BCredit_Calculation():
    ReturnVal = CDollar(GetFloat(IAF126.BNetTax) * GetFloat(IAF126.BCrPer))

def BCrPer_Calculation():
    if GetBool(IAF126.SpPYNR) == True:
        ReturnVal = MaxValue(0, 1 - GetFloat(IAF126.BIAPer))
    else:
        ReturnVal = 0

def BDividend_Calculation():
    if GetBool(IAF1040.CombMFS) == True and GetBool(IAF126.SpPYRes) == True:
        ReturnVal = GetCurrency(IAF1040.BDividend)
    else:
        ReturnVal = 0

def BFarm_Calculation():
    #made change based on user story 445128 to calculate when a nonresident, for past 10 years lines 1-14 only calced when a part-year res. Based on Iowa 126 instructions decided to calc lines 5, 7, 10, 11, 12, 13, and 14 when a NR/PY to be conservative.
    if GetBool(IAF1040.CombMFS) == True and GetBool(IAF126.SpRes) == False:
        ReturnVal = GetCurrency(IAF1040.BFarm)
    else:
        ReturnVal = 0

def BGamble_Calculation():
    #made change based on user story 445128 to calculate when a nonresident, for past 10 years lines 1-14 only calced when a part-year res. Based on Iowa 126 instructions decided to calc lines 5, 7, 10, 11, 12, 13, and 14 when a NR/PY to be conservative.
    if GetBool(IAF1040.CombMFS) == True and GetBool(IAF126.SpRes) == False:
        ReturnVal = GetCurrency(IAF1040.BGamble)
    else:
        ReturnVal = 0

def BGross_Calculation():
    if GetBool(IAF126.SpPYNR) == True:
        ReturnVal = GetCurrency(IAF126.BWages) + GetCurrency(IAF126.BInterest) + GetCurrency(IAF126.BDividend) + GetCurrency(IAF126.BAlimony) + GetCurrency(IAF126.BBusInc) + GetCurrency(IAF126.BCapGain) + GetCurrency(IAF126.BOthGain) + GetCurrency(IAF126.BIRA) + GetCurrency(IAF126.BPensions) + GetCurrency(IAF126.BRents) + GetCurrency(IAF126.BFarm) + GetCurrency(IAF126.BUnemp) + GetCurrency(IAF126.BGamble) + GetCurrency(IAF126.BOtherInc)
    else:
        ReturnVal = 0

def BIATax_Calculation():
    if GetBool(IAF126.SpPYNR) == True:
        ReturnVal = GetCurrency(IAF1040.BAltTax)
    else:
        ReturnVal = 0

def BInterest_Calculation():
    if GetBool(IAF1040.CombMFS) == True and GetBool(IAF126.SpPYRes) == True:
        ReturnVal = GetCurrency(IAF1040.BInterest)
    else:
        ReturnVal = 0

def BIRA_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IAWPenExc.NRSPIRA)
    else:
        ReturnVal = 0

def BMove_Calculation():
    if IAFS() == 3 and GetBool(IAF126.SpPYRes) == True:
        if GetDate(IAF126.SpDateIn) > datetime.datetime(12, 31, 2017) and GetDate(IAF126.SpDateOut) == 0:
            ReturnVal = GetCurrency(IAF1040.BMove)
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def BNet_Calculation():
    ReturnVal = GetCurrency(IAF126.BGross) - GetCurrency(IAF126.BTotAdj)

def BNetTax_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAF126.BIATax) - GetCurrency(IAF126.BTotCr))

def BOthAdj_Calculation():
    if GetBool(IAF126.SpPYNR) == True:
        ReturnVal = GetCurrency(IANROthAdj.SPTot)
    else:
        ReturnVal = 0

def BOtherInc_Calculation():
    if GetBool(IAF126.SpPYNR) == True:
        ReturnVal = GetCurrency(IANROthInc.SPTot)
    else:
        ReturnVal = 0

def BOthGain_Calculation():
    #made change based on user story 445128 to calculate when a nonresident, for past 10 years lines 1-14 only calced when a part-year res. Based on Iowa 126 instructions decided to calc lines 5, 7, 10, 11, 12, 13, and 14 when a NR/PY to be conservative.
    if GetBool(IAF1040.CombMFS) == True and GetBool(IAF126.SpRes) == False:
        ReturnVal = GetCurrency(IAF1040.BOthGain)
    else:
        ReturnVal = 0

def BPenExcl_Calculation():
    if GetBool(IAF126.SpPYNR) == True:
        ReturnVal = GetCurrency(IAWPenExc.NRSPPenExc)
    else:
        ReturnVal = 0

def BPensions_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IAWPenExc.NRSPPensions)
    else:
        ReturnVal = 0

def BRents_Calculation():
    #made change based on user story 445128 to calculate when a nonresident, for past 10 years lines 1-14 only calced when a part-year res. Based on Iowa 126 instructions decided to calc lines 5, 7, 10, 11, 12, 13, and 14 when a NR/PY to be conservative.
    if GetBool(IAF1040.CombMFS) == True and GetBool(IAF126.SpRes) == False:
        ReturnVal = GetCurrency(IAF1040.BRents)
    else:
        ReturnVal = 0

def BIAPer_Calculation():
    TopLim = Double()
    if GetBool(IAF126.IANotReqFIle) == True:
        ReturnVal = 0
    elif GetBool(IAF126.SpPYNR) == True:
        if GetFloat(IAF126.BAllSource) <= 0:
            ReturnVal = 1
        else:
            TopLim = MinValue(1, Round(GetFloat(IAF126.BNet) / GetFloat(IAF126.BAllSource), 3))
            ReturnVal = MaxValue(0, TopLim)
    else:
        ReturnVal = 0

def BTotAdj_Calculation():
    if GetBool(IAF126.SpPYNR) == True:
        ReturnVal = GetCurrency(IAF126.BKeogh) + GetCurrency(IAF126.BBusIncL) + GetCurrency(IAF126.BHealth) + GetCurrency(IAF126.BPenalty) + GetCurrency(IAF126.BAlimonyP) + GetCurrency(IAF126.BPenExcl) + GetCurrency(IAF126.BMove) + GetCurrency(IAF126.BGainDed) + GetCurrency(IAF126.BOthAdj)
    else:
        ReturnVal = 0

def BTotCr_Calculation():
    if GetBool(IAF126.SpPYNR) == True:
        ReturnVal = GetCurrency(IAF1040.BCredits)
    else:
        ReturnVal = 0

def BUnemp_Calculation():
    #made change based on user story 445128 to calculate when a nonresident, for past 10 years lines 1-14 only calced when a part-year res. Based on Iowa 126 instructions decided to calc lines 5, 7, 10, 11, 12, 13, and 14 when a NR/PY to be conservative.
    if GetBool(IAF1040.CombMFS) == True and GetBool(IAF126.SpRes) == False:
        ReturnVal = GetCurrency(IAF1040.BUnemp)
    else:
        ReturnVal = 0

def BWages_Calculation():
    if GetBool(IAF126.SpPYNR) == True:
        ReturnVal = MaxValue(GetCurrency(IAF126.SpWages), GetCurrency(IAF126.SpIAWages))
    else:
        ReturnVal = 0

def Desc_Calculation():
    Total = Currency()
    Total = GetCurrency(IAF126.BCredit) + GetCurrency(IAF126.ACredit)
    ReturnVal = CStr(Total) + ' Credit'

def Exist_Calculation():
    ReturnVal = 1

def GrossInc_Calculation():
    if GetBool(IAF126.TpPYNR) == True:
        ReturnVal = GetCurrency(IAF126.AWages) + GetCurrency(IAF126.AInterest) + GetCurrency(IAF126.ADividend) + GetCurrency(IAF126.AAlimony) + GetCurrency(IAF126.ABusInc) + GetCurrency(IAF126.ACapGain) + GetCurrency(IAF126.AOthGain) + GetCurrency(IAF126.AIRA) + GetCurrency(IAF126.APensions) + GetCurrency(IAF126.ARents) + GetCurrency(IAF126.AFarm) + GetCurrency(IAF126.AUnemp) + GetCurrency(IAF126.AGamble) + GetCurrency(IAF126.AOtherInc)
    else:
        ReturnVal = 0

def IANotReqFIle_Calculation():
    if GetBool(IAF1040.MFS) == True:
        ReturnVal = 0
    elif GetCurrency(IAF126.BNet) + GetCurrency(IAF126.ANet) >= Decimal("1000"):
        ReturnVal = 0
    elif GetCurrency(IA6251.AMT) > 0 or GetCurrency(IA6251Sp.AMT) > 0:
        ReturnVal = 0
    elif GetCurrency(IAF1040.BLump) > 0 or GetCurrency(IAF1040.ALump) > 0:
        ReturnVal = 0
    else:
        ReturnVal = 1

def Names_Calculation():
    ReturnVal = GetString(IARequired.CombNames)

def Print_Calculation():
    if GetBool(IAF126.TpPYNR) == True or GetBool(IAF126.SpPYNR) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

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
            if GetString(USDW2.St(W2Index), count1) == 'IA' and GetBool(USDW2.Stat, count1) == False and GetBool(USDW2.Spouse, count1) == True:
                Total1 = Total1 + Round(GetCurrency(USDW2.StWages(W2Index), count1))
            W2Index = W2Index + 1
        count1 = count1 + 1
    while count1 <= HowManyW2:
        if GetBool(USDW2.Stat, count1) == True and GetBool(USDW2.Spouse, count1) == True:
            StEpWage = StEpWage + Round(GetCurrency(USDW2.Wages, count1))
        count1 = count1 + 1
    AllW2Wage = GetCurrency(USDW2.Wages, FieldCopies(USDW2.Spouse))
    OthWages = GetCurrency(USWRec.SWages) - Round(AllW2Wage - StEpWage)
    ReturnVal = Total1 + OthWages

def SpNonRes_Calculation():
    if GetBool(IAF1040.MFJ) == True or GetBool(IAF1040.CombMFS) == True:
        if GetBool(USWResidency.F1040NR) == False:
            ReturnVal = 0
        else:
            ReturnVal = 1
    else:
        ReturnVal = 0

def SpPYNR_Calculation():
    if GetBool(IAF1040.CombMFS) == True and GetBool(IAF126.SpRes) == False:
        ReturnVal = 1
    else:
        ReturnVal = 0

def SpRes_Calculation():
    if GetBool(IAF1040.MFJ) == True or GetBool(IAF1040.CombMFS) == True:
        if GetBool(USWResidency.F1040NR) == False:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

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
            if GetString(USDW2.St(W2Index), count1) != 'IA' and GetBool(USDW2.Spouse, count1) == True:
                Total1 = Total1 + GetCurrency(USDW2.StWages(W2Index), count1)
            W2Index = W2Index + 1
        count1 = count1 + 1
    ReturnVal = MaxValue(0, GetCurrency(USWRec.SWages) - Total1)

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

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
            if GetString(USDW2.St(W2Index), count1) == 'IA' and GetBool(USDW2.Stat, count1) == False and GetBool(USDW2.Taxpayer, count1) == True:
                Total1 = Total1 + Round(GetCurrency(USDW2.StWages(W2Index), count1))
            W2Index = W2Index + 1
        count1 = count1 + 1
    while count1 <= HowManyW2:
        if GetBool(USDW2.Stat, count1) == True and GetBool(USDW2.Taxpayer, count1) == True:
            StEpWage = StEpWage + Round(GetCurrency(USDW2.Wages, count1))
        count1 = count1 + 1
    AllW2Wage = GetCurrency(USDW2.Wages, FieldCopies(USDW2.Taxpayer))
    OthWages = GetCurrency(USWRec.TWages) - Round(AllW2Wage - StEpWage)
    ReturnVal = Total1 + OthWages

def TpJtDateIn_Calculation():
    if GetBool(IAF126.TpPYRes) == True:
        ReturnVal = GetString(IAF126.TpDateIn)
    elif GetBool(IAF126.TpNonRes) == True:
        ReturnVal = ''
    elif GetBool(IAF1040.MFJ) == True and GetBool(IAF126.SpPYRes) == True:
        ReturnVal = GetString(IAF126.SpDateIn)
    else:
        ReturnVal = ''

def TpJtDateOut_Calculation():
    if GetBool(IAF126.TpPYRes) == True:
        ReturnVal = GetString(IAF126.TpDateOut)
    elif GetBool(IAF126.TpNonRes) == True:
        ReturnVal = ''
    elif GetBool(IAF1040.MFJ) == True and GetBool(IAF126.SpPYRes) == True:
        ReturnVal = GetString(IAF126.SpDateOut)
    else:
        ReturnVal = ''

def TPJtNonRes_Calculation():
    if GetBool(IAF126.TpNonRes) == True:
        ReturnVal = 1
    elif GetBool(IAF126.TpPYRes) == True:
        ReturnVal = 0
    elif GetBool(IAF1040.MFJ) == True and GetBool(IAF126.SpNonRes) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

def TPJtPYRes_Calculation():
    if GetBool(IAF126.TpPYRes) == True:
        ReturnVal = 1
    elif GetBool(IAF126.TpNonRes) == True:
        ReturnVal = 0
    elif GetBool(IAF1040.MFJ) == True and GetBool(IAF126.SpPYRes) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

def TpNonRes_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = 0
    else:
        ReturnVal = 1

def TpPYNR_Calculation():
    if GetBool(IAF1040.MFJ) == True:
        if GetBool(IAF126.TpRes) == False or GetBool(IAF126.SpRes) == False:
            ReturnVal = 1
        else:
            ReturnVal = 0
    elif GetBool(IAF126.TpRes) == False:
        ReturnVal = 1
    else:
        ReturnVal = 0

def TpRes_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = 1
    else:
        ReturnVal = 0

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
            if GetString(USDW2.St(W2Index), count1) != 'IA' and GetBool(USDW2.Taxpayer, count1) == True:
                Total1 = Total1 + GetCurrency(USDW2.StWages(W2Index), count1)
            W2Index = W2Index + 1
        count1 = count1 + 1
    ReturnVal = MaxValue(0, GetCurrency(USWRec.TWages) - Total1)

