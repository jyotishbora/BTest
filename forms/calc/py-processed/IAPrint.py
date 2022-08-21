from forms.out import IAF1040
from forms.out import IAPRINT
from forms.out import IAREQUIRED
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def AAltTax_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.AAltTax)
    else:
        return 0

def ABal1_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.ABal1)
    else:
        return 0

def ABal2_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.ABal2)
    else:
        return 0

def ABal4_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.ABal4)
    else:
        return 0

def ABal36_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.ABal36)
    else:
        return 0

def ABal3_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.ABal3)
    else:
        return 0

def ABalance_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.ABalance)
    else:
        return 0

def ACredits_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.ACredits)
    else:
        return 0

def ACrNon_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.ACrNon)
    else:
        return 0

def ADedBox_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.ADedBox)
    else:
        return 0

def AEstTax_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.AEstTax)
    else:
        return 0

def AExemCr_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.AExemCr)
    else:
        return 0

def AFedDed_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.AFedDed)
    else:
        return 0

def AFedTax_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.AFedTax)
    else:
        return 0

def AIAMin_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.AIAMin)
    else:
        return 0

def ALump_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.ALump)
    else:
        return 0

def AOthIACr_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.AOthIACr)
    else:
        return 0

def AOutState_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.AOutState)
    else:
        return 0

def APrior_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.APrior)
    else:
        return 0

def ARefund_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.ARefund)
    else:
        return 0

def ASch_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.ASch)
    else:
        return 0

def ASelf_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.ASelf)
    else:
        return 0

def ATaxB4Cont_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.ATaxB4Cont)
    else:
        return 0

def ATaxInc_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.ATaxInc)
    else:
        return 0

def ATaxWith_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.ATaxWith)
    else:
        return 0

def ATotIATax_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.ATotIATax)
    else:
        return 0

def ATotTax_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.ATotTax)
    else:
        return 0

def ATuit_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.ATuit)
    else:
        return 0

def AVolFireCr_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.AVolFireCr)
    else:
        return 0

def BAltTax_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.BAltTax)
    else:
        return 0

def BBal1_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.BBal1)
    else:
        return 0

def BBal2_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.BBal2)
    else:
        return 0

def BBal4_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.BBal4)
    else:
        return 0

def BBal36_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.BBal36)
    else:
        return 0

def BBal3_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.BBal3)
    else:
        return 0

def BBalance_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.BBalance)
    else:
        return 0

def BCredits_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.BCredits)
    else:
        return 0

def BCrNon_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.BCrNon)
    else:
        return 0

def BDedBox_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.BDedBox)
    else:
        return 0

def BEstTax_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.BEstTax)
    else:
        return 0

def BExemCr_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.BExemCr)
    else:
        return 0

def BFedDed_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.BFedDed)
    else:
        return 0

def BFedTax_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.BFedTax)
    else:
        return 0

def BIAMin_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.BIAMin)
    else:
        return 0

def BLump_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.BLump)
    else:
        return 0

def BOthIACr_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.BOthIACr)
    else:
        return 0

def BOutState_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.BOutState)
    else:
        return 0

def BPrior_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.BPrior)
    else:
        return 0

def BRefund_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.BRefund)
    else:
        return 0

def BSch_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.BSch)
    else:
        return 0

def BSelf_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.BSelf)
    else:
        return 0

def BTaxB4Cont_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.BTaxB4Cont)
    else:
        return 0

def BTaxInc_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.BTaxInc)
    else:
        return 0

def BTaxWith_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.BTaxWith)
    else:
        return 0

def BTotIATax_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.BTotIATax)
    else:
        return 0

def BTotTax_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.BTotTax)
    else:
        return 0

def BTuit_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.BTuit)
    else:
        return 0

def BVolFireCr_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.BVolFireCr)
    else:
        return 0

def FirstName_Calculation():
    return get_string(IAF1040.FirstName)

def ItemCheck_Calculation():
    if get_bool(IAREQUIRED.LowInc) == True:
        return 0
    else:
        return get_bool(IAF1040.ItemCheck)

def LastName_Calculation():
    return get_string(IAF1040.LastName)

def LowInc_Calculation():
    if get_bool(IAREQUIRED.LowInc) == True:
        return 0
    else:
        return 1

def SSN_Calculation():
    return get_string(IAF1040.SSN)

def StadCheck_Calculation():
    if get_bool(IAREQUIRED.LowInc) == True:
        return 0
    else:
        return get_bool(IAF1040.StadCheck)

def TotalTax_Calculation():
    if get_number(IAPRINT.LowInc) == 1:
        return get_currency(IAF1040.TotalTax)
    else:
        return 0


