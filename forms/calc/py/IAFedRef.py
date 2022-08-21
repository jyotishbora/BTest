from vb2py.vbfunctions import *
from vb2py.vbdebug import *
import datetime



def Description_Calculation():
    Total = Currency()
    Total = GetCurrency(IAFedRef.TPST) + GetCurrency(IAFedRef.SPST)
    ReturnVal = CStr(Total)

def Names_Calculation():
    ReturnVal = GetString(IARequired.CombNames)

def NetRef_Calculation():
    if GetBool(IAFedRef.PYNR) == True:
        ReturnVal = 0
    else:
        ReturnVal = MaxValue(0, GetCurrency(IAFedRef.PyRef) - GetCurrency(IAFedRef.PYEIC) - GetCurrency(IAFedRef.PYAddCTC) - GetCurrency(IAFedRef.PYRefHopeCr) - GetCurrency(IAFedRef.PYPTC))

def PYAddCTC_Calculation():
    if GetBool(USWSpouse.NonRes) == True:
        ReturnVal = GetCurrency(USWRec.PYAddCTCNR)
    else:
        ReturnVal = GetCurrency(USWRec.PYAddCTC)

def PYEIC_Calculation():
    ReturnVal = GetCurrency(USWRec.PYEIC)

def PYNR_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        if ( GetBool(IAF126.TpPYRes) == True and GetDate(IAF126.TpDateIn) > datetime.datetime(12, 31, 2017) )  and  ( GetBool(IAF126.SpPYRes) == True and GetDate(IAF126.SpDateIn) > datetime.datetime(12, 31, 2017) ) :
            ReturnVal = 1
        else:
            ReturnVal = 0
    elif  ( GetBool(IAF126.TpPYRes) == True and GetDate(IAF126.TpDateIn) > datetime.datetime(12, 31, 2017) ) :
        ReturnVal = 1
    else:
        ReturnVal = 0

def PYPTC_Calculation():
    if GetBool(USWSpouse.NonRes) == True:
        ReturnVal = GetCurrency(USWRec.PYNPTCNR)
    else:
        ReturnVal = GetCurrency(USWRec.PYNPTC)

def PyRef_Calculation():
    if GetBool(USWSpouse.NonRes) == True:
        ReturnVal = GetCurrency(USWRec.PYRefNR)
    else:
        ReturnVal = GetCurrency(USWRec.PYRef)

def PYRefHopeCr_Calculation():
    ReturnVal = GetCurrency(USWRec.PYRefHopeCr)

def SPName_Calculation():
    ReturnVal = GetString(USWBasicInfo.SPCommon)

def SPST_Calculation():
    ReturnVal = CDollar(GetFloat(IARequired.PYRatio) * GetFloat(IAFedRef.NetRef))

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

def TPName_Calculation():
    ReturnVal = GetString(USWBasicInfo.TPCommon)

def TPST_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAFedRef.NetRef) - GetCurrency(IAFedRef.SPST))

