from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Exist_Calculation():
    ReturnVal = 1

def Description_Calculation():
    Total = Currency()
    Total = GetCurrency(IAWHealth.TPTotal) + GetCurrency(IAWHealth.SPTotal)
    ReturnVal = CStr(Total)

def MobDisQual_Calculation():
    if GetCurrency(IAWHealth.TPTotal) + GetCurrency(IAWHealth.SPTotal) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Names_Calculation():
    ReturnVal = GetString(IARequired.CombNames)

def SERatio_Calculation():
    TotSE = Currency()
    TotSE = GetCurrency(IAWHealth.SPTotSE) + GetCurrency(IAWHealth.TPTotSE)
    if TotSE > 0:
        ReturnVal = MinValue(1, MaxValue(0, GetFloat(IAWHealth.SPTotSE) /  ( GetFloat(IAWHealth.SPTotSE) + GetFloat(IAWHealth.TPTotSE) )))
    else:
        ReturnVal = 0

def SPMedicare_Calculation():
    MedBReduce = Currency()
    if GetCurrency(IAWHealth.TPSEHealth) > 0 and GetCurrency(IAWHealth.SPSEHealth) > 0:
        MedBReduce = CDollar(GetFloat(USWMedicalWS.MedBPremOff) * 0.5)
    elif GetCurrency(IAWHealth.TPSEHealth) == 0 and GetCurrency(IAWHealth.SPSEHealth) > 0:
        MedBReduce = GetCurrency(USWMedicalWS.MedBPremOff)
    else:
        MedBReduce = 0
    ReturnVal = MaxValue(0, ( GetCurrency(USWSSBDetail.SPMedB) + Round(GetCurrency(USDRRB1099R.MedB, FieldCopies(USDRRB1099R.Spouse))) )  - MedBReduce)

def SPName_Calculation():
    ReturnVal = GetString(USWBasicInfo.SPCommon)

def SPSE_Calculation():
    ReturnVal = GetCurrency(USDSCorpK1.SeHealthInc, FieldCopies(USDSCorpK1.Spouse)) + CDollar(GetFloat(USDSCorpK1.SeHealthInc, FieldCopies(USDSCorpK1.Joint)) * 0.5)

def SPSEHealth_Calculation():
    ReturnVal = CDollar(GetFloat(IAWHealth.TotHealth) * GetFloat(IAWHealth.SERatio))

def SPTotal_Calculation():
    ReturnVal = GetCurrency(IAWHealth.SPSEHealth) + GetCurrency(IAWHealth.SPInsPrem) + GetCurrency(IAWHealth.SPMedicare) + GetCurrency(IAWHealth.SPLTC) + GetCurrency(IAWHealth.SPPYRepayPTC)

def SPTotSE_Calculation():
    ReturnVal = GetCurrency(USSchSESpouse.ANetEarn) + GetCurrency(USSchSESpouse.BNetEarn) + GetCurrency(IAWHealth.SPSE)

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

def TotHealth_Calculation():
    ReturnVal = GetCurrency(USWSEHealth.InsPrem)

def TotLTC_Calculation():
    ReturnVal = GetCurrency(USWMedicalWS.LTCPrem) + GetCurrency(USWMedicalWS.LTCPrem2) + GetCurrency(USWMedicalWS.LTCPrem3) + GetCurrency(USWMedicalWS.LTCPrem4)

def TotSE_Calculation():
    ReturnVal = GetCurrency(USDSCorpK1.SeHealthInc)

def TPInsPrem_Calculation():
    AdjInsPrem = Currency()
    #removed adjustment for USWMedicalWS.PTCAdj in order to only report what was actually paid out of pocket in the current year. The PTC adjustment (either credit or excess repayment) is handled by including repayment on IA 1040 line 28(current year)/line 18(import from prior year) and IA 1040 line 14 for any current year PTC credit to be imported as income the following year.
    #change was made based on US 433238 see also CSS ticket 8605571
    AdjInsPrem = MaxValue(0, GetCurrency(USWMedicalWS.MarketplaceIns)) + GetCurrency(USWMedicalWS.TPSPDepIns)
    ReturnVal = MaxValue(0, AdjInsPrem - GetCurrency(IAWHealth.SPInsPrem))

def TPLTC_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWHealth.TotLTC) - GetCurrency(IAWHealth.SPLTC))

def TPMedicare_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(USWMedicalWS.MedBPremTot) - GetCurrency(IAWHealth.SPMedicare))

def TPName_Calculation():
    ReturnVal = GetString(USWBasicInfo.TPCommon)

def TPPYRepayPTC_Calculation():
    if GetBool(USWSpouse.NonRes) == True:
        ReturnVal = MaxValue(0, GetCurrency(USWRec.PYRepayPTCNR) - GetCurrency(IAWHealth.SPPYRepayPTC))
    else:
        ReturnVal = MaxValue(0, GetCurrency(USWRec.PYRepayPTC) - GetCurrency(IAWHealth.SPPYRepayPTC))

def TPSE_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWHealth.TotSE) - GetCurrency(IAWHealth.SPSE))

def TPSEHealth_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWHealth.TotHealth) - GetCurrency(IAWHealth.SPSEHealth))

def TPTotal_Calculation():
    ReturnVal = GetCurrency(IAWHealth.TPSEHealth) + GetCurrency(IAWHealth.TPInsPrem) + GetCurrency(IAWHealth.TPMedicare) + GetCurrency(IAWHealth.TPLTC) + GetCurrency(IAWHealth.TPPYRepayPTC)

def TPTotSE_Calculation():
    ReturnVal = GetCurrency(USSchSE.ANetEarn) + GetCurrency(USSchSE.BNetEarn) + GetCurrency(IAWHealth.TPSE)

