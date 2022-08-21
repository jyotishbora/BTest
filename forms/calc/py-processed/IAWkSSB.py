from forms.out import IAF1040
from forms.out import IAREQUIRED
from forms.out import IAWKSSB
from forms.out import IAWOTHINC
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Box5_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return max_value(0, get_currency(USWSSBDetail.TotSS))
    else:
        return max_value(0, get_currency(USWSSBDetailNR.TPSS))

def Description_Calculation():
    return CStr(get_currency(IAWKSSB.ReportSSB)) + ' Reportable Benefits'

def FilStat_Calculation():
    if FedFS() == 2:
        return Decimal("32000")
    elif FedFS() == 3 and get_bool(USWBasicInfo.MFSAllYr) == False:
        return 0
    else:
        return Decimal("25000")

def Half10_Calculation():
    return c_dollar(get_float(IAWKSSB.Sub9) * 0.5)

def Half2_Calculation():
    return c_dollar(get_float(IAWKSSB.Box5) * 0.5)

def Line31_Calculation():
    return get_currency(USWRec.TotEdExp) + get_currency(USWRec.TotBusExp2106) + get_currency(USWRec.TotHealthSav) + get_currency(USWRec.TotMove) + get_currency(USWRec.TotHalfSE) + get_currency(USWRec.TotKeough) + get_currency(USWRec.TotSEHealth) + get_currency(USWRec.TotEarlyPen) + get_currency(USWRec.TotAlimonyAdj) + get_currency(USWRec.TotScholEx) + get_currency(USWRec.TotIRAAdj) + get_currency(USWRec.TotOthAdj)

def Line8b_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USF1040.TEI)
    else:
        return get_currency(USF1040NR.TEI)

def Names_Calculation():
    return get_string(IAREQUIRED.CombNames)

def ReportSSB_Calculation():
    return min_value(get_currency(IAWKSSB.Half2), get_currency(IAWKSSB.Half10))

def SPRepSSB_Calculation():
    TotSSB = Currency()

    SpSSB = Currency()
    TotSSB = get_currency(IAWKSSB.Box5)
    SpSSB = get_currency(USWSSBDetail.SPSS)
    if get_bool(USWResidency.F1040NR) == False:
        if TotSSB > 0:
            return c_dollar(( CDbl(SpSSB) / CDbl(TotSSB) )  * get_float(IAWKSSB.ReportSSB))
        else:
            return 0
    else:
        return 0

def SSN_Calculation():
    return get_string(IAF1040.SSN)

def Sub_Calculation():
    return get_currency(IAWKSSB.Sum5) - get_currency(IAWKSSB.Line31)

def Sub9_Calculation():
    return max_value(0, ( get_currency(IAWKSSB.Sub) - get_currency(IAWKSSB.FilStat) ))

def Sum3_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWSSB.SSBInc) + get_currency(USWSSB.TotExempt) + get_currency(IAWOTHINC.TotBonus) + get_currency(IAWOTHINC.TotNonConform) - get_currency(IAREQUIRED.NCMove) - get_currency(IAREQUIRED.NCDomProd) + c_dollar(get_float(USWSSBDetail.TotRR) / 2)
    else:
        return get_currency(USF1040NR.TECI) + get_currency(USF8839.SumL22) + get_currency(IAWOTHINC.TotBonus) + get_currency(IAWOTHINC.TotNonConform) - get_currency(IAREQUIRED.NCMove) - get_currency(IAREQUIRED.NCDomProd) + c_dollar(get_float(USWSSBDetailNR.TPRR) / 2)

def Sum5_Calculation():
    return get_currency(IAWKSSB.Half2) + get_currency(IAWKSSB.Sum3) + get_currency(IAWKSSB.Line8b)

def TPRepSSB_Calculation():
    return max_value(0, get_currency(IAWKSSB.ReportSSB) - get_currency(IAWKSSB.SPRepSSB))


