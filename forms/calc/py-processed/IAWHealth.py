from forms.out import IAF1040
from forms.out import IAREQUIRED
from forms.out import IAWHEALTH
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Exist_Calculation():
    return 1

def Description_Calculation():
    Total = Currency()
    Total = get_currency(IAWHEALTH.TPTotal) + get_currency(IAWHEALTH.SPTotal)
    return CStr(Total)

def MobDisQual_Calculation():
    if get_currency(IAWHEALTH.TPTotal) + get_currency(IAWHEALTH.SPTotal) > 0:
        return 1
    else:
        return 0

def Names_Calculation():
    return get_string(IAREQUIRED.CombNames)

def SERatio_Calculation():
    TotSE = Currency()
    TotSE = get_currency(IAWHEALTH.SPTotSE) + get_currency(IAWHEALTH.TPTotSE)
    if TotSE > 0:
        return min_value(1, max_value(0, get_float(IAWHEALTH.SPTotSE) /  ( get_float(IAWHEALTH.SPTotSE) + get_float(IAWHEALTH.TPTotSE) )))
    else:
        return 0

def SPMedicare_Calculation():
    MedBReduce = Currency()
    if get_currency(IAWHEALTH.TPSEHealth) > 0 and get_currency(IAWHEALTH.SPSEHealth) > 0:
        MedBReduce = c_dollar(get_float(USWMedicalWS.MedBPremOff) * 0.5)
    elif get_currency(IAWHEALTH.TPSEHealth) == 0 and get_currency(IAWHEALTH.SPSEHealth) > 0:
        MedBReduce = get_currency(USWMedicalWS.MedBPremOff)
    else:
        MedBReduce = 0
    return max_value(0, ( get_currency(USWSSBDetail.SPMedB) + Round(get_currency(USDRRB1099R.MedB, FieldCopies(USDRRB1099R.Spouse))) )  - MedBReduce)

def SPName_Calculation():
    return get_string(USWBasicInfo.SPCommon)

def SPSE_Calculation():
    return get_currency(USDSCorpK1.SeHealthInc, FieldCopies(USDSCorpK1.Spouse)) + c_dollar(get_float(USDSCorpK1.SeHealthInc, FieldCopies(USDSCorpK1.Joint)) * 0.5)

def SPSEHealth_Calculation():
    return c_dollar(get_float(IAWHEALTH.TotHealth) * get_float(IAWHEALTH.SERatio))

def SPTotal_Calculation():
    return get_currency(IAWHEALTH.SPSEHealth) + get_currency(IAWHEALTH.SPInsPrem) + get_currency(IAWHEALTH.SPMedicare) + get_currency(IAWHEALTH.SPLTC) + get_currency(IAWHEALTH.SPPYRepayPTC)

def SPTotSE_Calculation():
    return get_currency(USSchSESpouse.ANetEarn) + get_currency(USSchSESpouse.BNetEarn) + get_currency(IAWHEALTH.SPSE)

def SSN_Calculation():
    return get_string(IAF1040.SSN)

def TotHealth_Calculation():
    return get_currency(USWSEHealth.InsPrem)

def TotLTC_Calculation():
    return get_currency(USWMedicalWS.LTCPrem) + get_currency(USWMedicalWS.LTCPrem2) + get_currency(USWMedicalWS.LTCPrem3) + get_currency(USWMedicalWS.LTCPrem4)

def TotSE_Calculation():
    return get_currency(USDSCorpK1.SeHealthInc)

def TPInsPrem_Calculation():
    AdjInsPrem = Currency()
    #removed adjustment for USWMedicalWS.PTCAdj in order to only report what was actually paid out of pocket in the current year. The PTC adjustment (either credit or excess repayment) is handled by including repayment on IA 1040 line 28(current year)/line 18(import from prior year) and IA 1040 line 14 for any current year PTC credit to be imported as income the following year.
    #change was made based on US 433238 see also CSS ticket 8605571
    AdjInsPrem = max_value(0, get_currency(USWMedicalWS.MarketplaceIns)) + get_currency(USWMedicalWS.TPSPDepIns)
    return max_value(0, AdjInsPrem - get_currency(IAWHEALTH.SPInsPrem))

def TPLTC_Calculation():
    return max_value(0, get_currency(IAWHEALTH.TotLTC) - get_currency(IAWHEALTH.SPLTC))

def TPMedicare_Calculation():
    return max_value(0, get_currency(USWMedicalWS.MedBPremTot) - get_currency(IAWHEALTH.SPMedicare))

def TPName_Calculation():
    return get_string(USWBasicInfo.TPCommon)

def TPPYRepayPTC_Calculation():
    if get_bool(USWSpouse.NonRes) == True:
        return max_value(0, get_currency(USWRec.PYRepayPTCNR) - get_currency(IAWHEALTH.SPPYRepayPTC))
    else:
        return max_value(0, get_currency(USWRec.PYRepayPTC) - get_currency(IAWHEALTH.SPPYRepayPTC))

def TPSE_Calculation():
    return max_value(0, get_currency(IAWHEALTH.TotSE) - get_currency(IAWHEALTH.SPSE))

def TPSEHealth_Calculation():
    return max_value(0, get_currency(IAWHEALTH.TotHealth) - get_currency(IAWHEALTH.SPSEHealth))

def TPTotal_Calculation():
    return get_currency(IAWHEALTH.TPSEHealth) + get_currency(IAWHEALTH.TPInsPrem) + get_currency(IAWHEALTH.TPMedicare) + get_currency(IAWHEALTH.TPLTC) + get_currency(IAWHEALTH.TPPYRepayPTC)

def TPTotSE_Calculation():
    return get_currency(USSchSE.ANetEarn) + get_currency(USSchSE.BNetEarn) + get_currency(IAWHEALTH.TPSE)


