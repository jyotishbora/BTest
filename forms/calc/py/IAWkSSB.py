from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Box5_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = MaxValue(0, GetCurrency(USWSSBDetail.TotSS))
    else:
        ReturnVal = MaxValue(0, GetCurrency(USWSSBDetailNR.TPSS))

def Description_Calculation():
    ReturnVal = CStr(GetCurrency(IAWkSSB.ReportSSB)) + ' Reportable Benefits'

def FilStat_Calculation():
    if FedFS() == 2:
        ReturnVal = Decimal("32000")
    elif FedFS() == 3 and GetBool(USWBasicInfo.MFSAllYr) == False:
        ReturnVal = 0
    else:
        ReturnVal = Decimal("25000")

def Half10_Calculation():
    ReturnVal = CDollar(GetFloat(IAWkSSB.Sub9) * 0.5)

def Half2_Calculation():
    ReturnVal = CDollar(GetFloat(IAWkSSB.Box5) * 0.5)

def Line31_Calculation():
    ReturnVal = GetCurrency(USWRec.TotEdExp) + GetCurrency(USWRec.TotBusExp2106) + GetCurrency(USWRec.TotHealthSav) + GetCurrency(USWRec.TotMove) + GetCurrency(USWRec.TotHalfSE) + GetCurrency(USWRec.TotKeough) + GetCurrency(USWRec.TotSEHealth) + GetCurrency(USWRec.TotEarlyPen) + GetCurrency(USWRec.TotAlimonyAdj) + GetCurrency(USWRec.TotScholEx) + GetCurrency(USWRec.TotIRAAdj) + GetCurrency(USWRec.TotOthAdj)

def Line8b_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USF1040.TEI)
    else:
        ReturnVal = GetCurrency(USF1040NR.TEI)

def Names_Calculation():
    ReturnVal = GetString(IARequired.CombNames)

def ReportSSB_Calculation():
    ReturnVal = MinValue(GetCurrency(IAWkSSB.Half2), GetCurrency(IAWkSSB.Half10))

def SPRepSSB_Calculation():
    TotSSB = Currency()

    SpSSB = Currency()
    TotSSB = GetCurrency(IAWkSSB.Box5)
    SpSSB = GetCurrency(USWSSBDetail.SPSS)
    if GetBool(USWResidency.F1040NR) == False:
        if TotSSB > 0:
            ReturnVal = CDollar(( CDbl(SpSSB) / CDbl(TotSSB) )  * GetFloat(IAWkSSB.ReportSSB))
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

def Sub_Calculation():
    ReturnVal = GetCurrency(IAWkSSB.Sum5) - GetCurrency(IAWkSSB.Line31)

def Sub9_Calculation():
    ReturnVal = MaxValue(0, ( GetCurrency(IAWkSSB.Sub) - GetCurrency(IAWkSSB.FilStat) ))

def Sum3_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWSSB.SSBInc) + GetCurrency(USWSSB.TotExempt) + GetCurrency(IAWOthInc.TotBonus) + GetCurrency(IAWOthInc.TotNonConform) - GetCurrency(IARequired.NCMove) - GetCurrency(IARequired.NCDomProd) + CDollar(GetFloat(USWSSBDetail.TotRR) / 2)
    else:
        ReturnVal = GetCurrency(USF1040NR.TECI) + GetCurrency(USF8839.SumL22) + GetCurrency(IAWOthInc.TotBonus) + GetCurrency(IAWOthInc.TotNonConform) - GetCurrency(IARequired.NCMove) - GetCurrency(IARequired.NCDomProd) + CDollar(GetFloat(USWSSBDetailNR.TPRR) / 2)

def Sum5_Calculation():
    ReturnVal = GetCurrency(IAWkSSB.Half2) + GetCurrency(IAWkSSB.Sum3) + GetCurrency(IAWkSSB.Line8b)

def TPRepSSB_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWkSSB.ReportSSB) - GetCurrency(IAWkSSB.SPRepSSB))

