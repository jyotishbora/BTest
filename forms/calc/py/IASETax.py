from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Description_Calculation():
    Total = Currency()
    Total = GetCurrency(IASETax.TPTotal) + GetCurrency(IASETax.SPTotal)
    ReturnVal = CStr(Total)

def Exist_Calculation():
    ReturnVal = 1

def MobDisQual_Calculation():
    if GetCurrency(IASETax.TPTotal) + GetCurrency(IASETax.SPTotal) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Names_Calculation():
    ReturnVal = GetString(IARequired.CombNames)

def SPHH_Calculation():
    if GetBool(USSchH.Taxpayer) == True:
        ReturnVal = 0
    elif GetBool(USWResidency.F1040NR) == True:
        ReturnVal = 0
    elif GetBool(USSchH.Spouse) == True:
        ReturnVal = GetCurrency(USW1040Supp.HTax)
    else:
        ReturnVal = CDollar(GetFloat(USW1040Supp.HTax) * 0.5)

def SPName_Calculation():
    ReturnVal = GetString(USWBasicInfo.SPCommon)

def SPRetTax_Calculation():
    ReturnVal = GetCurrency(USF5329Spouse.TotAddTax)

def SPSE_Calculation():
    if GetBool(USSchSESpouse.ShortSE) == True:
        ReturnVal = GetCurrency(USSchSESpouse.ASETax)
    else:
        ReturnVal = GetCurrency(USSchSESpouse.BSETax)

def SPTipTax_Calculation():
    ReturnVal = GetCurrency(USF4137Spouse.AddLnTen) + GetCurrency(USF8919Spouse.TotTax)

def SPTotal_Calculation():
    ReturnVal = GetCurrency(IASETax.SPRepayPTC) + GetCurrency(IASETax.SPSE) + GetCurrency(IASETax.SPTipTax) + GetCurrency(IASETax.SPRetTax) + GetCurrency(IASETax.SPHH) + GetCurrency(IASETax.SPHomeBuyRepay) + GetCurrency(IASETax.SpHlthCarePen) + GetCurrency(IASETax.SPTotAddMedTax) + GetCurrency(IASETax.SPOthTax)

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

def TPHH_Calculation():
    if GetBool(USWResidency.F1040NR) == True:
        ReturnVal = GetCurrency(USF1040NR.SchHTax)
    elif GetBool(USSchH.Spouse) == True:
        ReturnVal = 0
    else:
        ReturnVal = MaxValue(0, GetCurrency(USW1040Supp.HTax) - GetCurrency(IASETax.SPHH))

def TPHlthCarePen_Calculation():
    if GetBool(USWResidency.F1040NR) == True:
        ReturnVal = 0
    else:
        ReturnVal = MaxValue(0, GetCurrency(USF1040.HlthCarePen) - GetCurrency(IASETax.SpHlthCarePen))

def TPHomeBuyRepay_Calculation():
    if GetBool(USWResidency.F1040NR) == True:
        ReturnVal = GetCurrency(USF1040NR.HomeBuyRepay)
    else:
        ReturnVal = MaxValue(0, GetCurrency(USF1040.HomeBuyRepay) - GetCurrency(IASETax.SPHomeBuyRepay))

def TPName_Calculation():
    ReturnVal = GetString(USWBasicInfo.TPCommon)

def TPOthTax_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(USWOthTax.TotOthTax) - GetCurrency(IASETax.SPOthTax))

def TPRepayPTC_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(USF8962.PTCRepay) - GetCurrency(IASETax.SPRepayPTC))

def TPRetTax_Calculation():
    ReturnVal = GetCurrency(USF5329.TotAddTax)

def TPSE_Calculation():
    if GetBool(USSchSE.ShortSE) == True:
        ReturnVal = GetCurrency(USSchSE.ASETax)
    else:
        ReturnVal = GetCurrency(USSchSE.BSETax)

def TPTipTax_Calculation():
    ReturnVal = GetCurrency(USF4137.AddLnTen) + GetCurrency(USF8919.TotTax)

def TPTotAddMedTax_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(USF8959.TotAddMedTax) - GetCurrency(IASETax.SPTotAddMedTax))

def TPTotal_Calculation():
    ReturnVal = GetCurrency(IASETax.TPRepayPTC) + GetCurrency(IASETax.TPSE) + GetCurrency(IASETax.TPTipTax) + GetCurrency(IASETax.TPRetTax) + GetCurrency(IASETax.TPHH) + GetCurrency(IASETax.TPHomeBuyRepay) + GetCurrency(IASETax.TPHlthCarePen) + GetCurrency(IASETax.TPTotAddMedTax) + GetCurrency(IASETax.TPOthTax)

