from forms.out import IA1040V
from forms.out import IA1040X
from forms.out import IA1040XV
from forms.out import IA130
from forms.out import IA134SP
from forms.out import IA137
from forms.out import IA148SP
from forms.out import IA2210
from forms.out import IA2210AN
from forms.out import IA2210ANSP
from forms.out import IA2210SP
from forms.out import IA4562A
from forms.out import IA4562BSP
from forms.out import IA4562SP
from forms.out import IA6251
from forms.out import IA6251SP
from forms.out import IA8801SP
from forms.out import IAESTIMATES
from forms.out import IAF126
from forms.out import IAREQUIRED
from forms.out import IASCHA
from forms.out import IASCHB
from forms.out import IAWPREPCBF
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def CBF_Calculation():
    return get_bool(USWPrepBInv.StY)

def CBF1040_Calculation():
    return get_currency(USZIAMasterCBF.CBF1040)

def CBF1040ES_Calculation():
    return get_currency(USZIAMasterCBF.CBF1040ES)

def CBF1040V_Calculation():
    return get_currency(USZIAMasterCBF.CBF1040V)

def CBF1040X_Calculation():
    return get_currency(USZIAMasterCBF.CBF1040X)

def CBF1040XV_Calculation():
    return get_currency(USZIAMasterCBF.CBF1040XV)

def CBF2210_Calculation():
    return get_currency(USZIAMasterCBF.CBF2210)

def CBF2210SchAI_Calculation():
    return get_currency(USZIAMasterCBF.CBF2210SchAI)

def CBF4136_Calculation():
    return get_currency(USZIAMasterCBF.CBF4136)

def CBF4562A_Calculation():
    return get_currency(USZIAMasterCBF.CBF4562A)

def CBF4562B_Calculation():
    return get_currency(USZIAMasterCBF.CBF4562B)

def CBF6251_Calculation():
    return get_currency(USZIAMasterCBF.CBF6251)

def CBF8453_Calculation():
    return get_currency(USZIAMasterCBF.CBF8453)

def CBF8801_Calculation():
    return get_currency(USZIAMasterCBF.CBF8801)

def CBF8864_Calculation():
    return get_currency(USZIAMasterCBF.CBF8864)

def CBFName_Calculation():
    return get_string(IAREQUIRED.CombNames)

def CBFOthAmt_Calculation(Index):
    return get_currency(USZIAMasterCBF.CBFOthAmt(Index))

def CBFSch126_Calculation():
    return get_currency(USZIAMasterCBF.CBFSch126)

def CBFSch128_Calculation():
    return get_currency(USZIAMasterCBF.CBFSch128)

def CBFSch128S_Calculation():
    return get_currency(USZIAMasterCBF.CBFSch128S)

def CBFSch130_Calculation():
    return get_currency(USZIAMasterCBF.CBFSch130)

def CBFSch134_Calculation():
    return get_currency(USZIAMasterCBF.CBFSch134)

def CBFSch135_Calculation():
    return get_currency(USZIAMasterCBF.CBFSch135)

def CBFSch137_Calculation():
    return get_currency(USZIAMasterCBF.CBFSch137)

def CBFSch138_Calculation():
    return get_currency(USZIAMasterCBF.CBFSch138)

def CBFSch147_Calculation():
    return get_currency(USZIAMasterCBF.CBFSch147)

def CBFSch148_Calculation():
    return get_currency(USZIAMasterCBF.CBFSch148)

def CBFSch177_Calculation():
    return get_currency(USZIAMasterCBF.CBFSch177)

def CBFSchA_Calculation():
    return get_currency(USZIAMasterCBF.CBFSchA)

def CBFSchB_Calculation():
    return get_currency(USZIAMasterCBF.CBFSchB)

def CF147_Calculation():
    return get_number(IA147.Print)

def CF177_Calculation():
    return get_number(IA177.Print)

def CF1040_Calculation():
    return 1

def CF126_Calculation():
    return get_number(IAF126.Print)

def CF128_Calculation():
    return get_number(IA128.Print)

def CF128S_Calculation():
    return get_number(IA128S.Print)

def CF130_Calculation():
    return get_number(IA130.PrintMe)

def CF134_Calculation():
    return get_number(IA134.Print) + get_number(IA134SP.Print)

def CF135_Calculation():
    return get_number(IA135.Print)

def CF137_Calculation():
    return get_number(IA137.Print)

def CF138_Calculation():
    return get_number(IA138.Print)

def CF148_Calculation():
    return get_number(IA148.Print) + get_number(IA148SP.Print)

def CF1040V_Calculation():
    return get_number(IA1040V.PrVou)

def CF1040XV_Calculation():
    return get_number(IA1040XV.PrVou)

def CF2210_Calculation():
    return get_number(IA2210.Print) + get_number(IA2210SP.Print)

def CF2210SchAI_Calculation():
    return get_number(IA2210AN.Print) + get_number(IA2210ANSP.Print)

def CF4136_Calculation():
    return get_bool(IASch4136.TotCr, 1) + get_bool(IASch4136.TotCr, 2)

def CF4562A_Calculation():
    return get_number(IA4562.PrIA4562) + get_number(IA4562SP.PrIA4562) + get_number(IA4562A.PrIA4562A)

def CF4562B_Calculation():
    return get_number(IA4562B.Print) + get_number(IA4562BSP.Print)

def CF6251_Calculation():
    return get_number(IA6251.Print) + get_number(IA6251SP.Print)

def CF8801_Calculation():
    return get_number(IA8801.Print) + get_number(IA8801SP.Print)

def CF8864_Calculation():
    return get_number(IA8864.Print)

def CFA_Calculation():
    return get_number(IASCHA.PrintSchA)

def CFB_Calculation():
    return get_number(IASCHB.PrintIAB)

def CFES_Calculation():
    return get_number(IAESTIMATES.Print)

def CFX_Calculation():
    return get_number(IA1040X.Exist)

def CopFOthName_Calculation(Index):
    return get_string(USZIAMasterCBF.CBFOth1Name(Index))

def FOthAmt_Calculation(Index):
    return get_currency(IAWPREPCBF.CopFOth(Index)) * get_currency(IAWPREPCBF.CBFOthAmt(Index))

def FTotal1040_Calculation():
    return get_currency(IAWPREPCBF.CF1040) * get_currency(IAWPREPCBF.CBF1040)

def FTotal1040ES_Calculation():
    return get_currency(IAWPREPCBF.CFES) * get_currency(IAWPREPCBF.CBF1040ES)

def FTotal1040V_Calculation():
    return get_currency(IAWPREPCBF.CF1040V) * get_currency(IAWPREPCBF.CBF1040V)

def FTotal1040X_Calculation():
    return get_currency(IAWPREPCBF.CFX) * get_currency(IAWPREPCBF.CBF1040X)

def FTotal1040XV_Calculation():
    return get_currency(IAWPREPCBF.CF1040XV) * get_currency(IAWPREPCBF.CBF1040XV)

def FTotal2210_Calculation():
    return get_currency(IAWPREPCBF.CF2210) * get_currency(IAWPREPCBF.CBF2210)

def FTotal2210SchAI_Calculation():
    return get_currency(IAWPREPCBF.CF2210SchAI) * get_currency(IAWPREPCBF.CBF2210SchAI)

def FTotal4136_Calculation():
    return get_currency(IAWPREPCBF.CF4136) * get_currency(IAWPREPCBF.CBF4136)

def FTotal4562A_Calculation():
    return get_currency(IAWPREPCBF.CF4562A) * get_currency(IAWPREPCBF.CBF4562A)

def FTotal4562B_Calculation():
    return get_currency(IAWPREPCBF.CF4562B) * get_currency(IAWPREPCBF.CBF4562B)

def FTotal6251_Calculation():
    return get_currency(IAWPREPCBF.CF6251) * get_currency(IAWPREPCBF.CBF6251)

def FTotal8453_Calculation():
    return get_currency(IAWPREPCBF.CF8453) * get_currency(IAWPREPCBF.CBF8453)

def FTotal8801_Calculation():
    return get_currency(IAWPREPCBF.CF8801) * get_currency(IAWPREPCBF.CBF8801)

def FTotal8864_Calculation():
    return get_currency(IAWPREPCBF.CF8864) * get_currency(IAWPREPCBF.CBF8864)

def FTotalSch126_Calculation():
    return get_currency(IAWPREPCBF.CF126) * get_currency(IAWPREPCBF.CBFSch126)

def FTotalSch128_Calculation():
    return get_currency(IAWPREPCBF.CF128) * get_currency(IAWPREPCBF.CBFSch128)

def FTotalSch128S_Calculation():
    return get_currency(IAWPREPCBF.CF128S) * get_currency(IAWPREPCBF.CBFSch128S)

def FTotalSch130_Calculation():
    return get_currency(IAWPREPCBF.CF130) * get_currency(IAWPREPCBF.CBFSch130)

def FTotalSch134_Calculation():
    return get_currency(IAWPREPCBF.CF134) * get_currency(IAWPREPCBF.CBFSch134)

def FTotalSch135_Calculation():
    return get_currency(IAWPREPCBF.CF135) * get_currency(IAWPREPCBF.CBFSch135)

def FTotalSch137_Calculation():
    return get_currency(IAWPREPCBF.CF137) * get_currency(IAWPREPCBF.CBFSch137)

def FTotalSch138_Calculation():
    return get_currency(IAWPREPCBF.CF138) * get_currency(IAWPREPCBF.CBFSch138)

def FTotalSch147_Calculation():
    return get_currency(IAWPREPCBF.CF147) * get_currency(IAWPREPCBF.CBFSch147)

def FTotalSch148_Calculation():
    return get_currency(IAWPREPCBF.CF148) * get_currency(IAWPREPCBF.CBFSch148)

def FTotalSch177_Calculation():
    return get_currency(IAWPREPCBF.CF177) * get_currency(IAWPREPCBF.CBFSch177)

def FTotalSchA_Calculation():
    return get_currency(IAWPREPCBF.CFA) * get_currency(IAWPREPCBF.CBFSchA)

def FTotalSchB_Calculation():
    return get_currency(IAWPREPCBF.CFB) * get_currency(IAWPREPCBF.CBFSchB)

def TotCharge_Calculation():
    TotCharge1 = Currency()

    TotCharge2 = Currency()
    TotCharge1 = get_currency(IAWPREPCBF.FTotal1040) + get_currency(IAWPREPCBF.FTotal1040ES) + get_currency(IAWPREPCBF.FTotal1040V) + get_currency(IAWPREPCBF.FTotal1040X) + get_currency(IAWPREPCBF.FTotal1040XV) + get_currency(IAWPREPCBF.FTotalSchA) + get_currency(IAWPREPCBF.FTotalSchB) + get_currency(IAWPREPCBF.FTotalSch126) + get_currency(IAWPREPCBF.FTotalSch128) + get_currency(IAWPREPCBF.FTotalSch128S) + get_currency(IAWPREPCBF.FTotalSch130) + get_currency(IAWPREPCBF.FTotalSch134) + get_currency(IAWPREPCBF.FTotalSch135) + get_currency(IAWPREPCBF.FTotalSch137) + get_currency(IAWPREPCBF.FTotalSch138) + get_currency(IAWPREPCBF.FTotalSch147) + get_currency(IAWPREPCBF.FTotalSch148)
    TotCharge2 = get_currency(IAWPREPCBF.FTotalSch177) + get_currency(IAWPREPCBF.FTotal2210) + get_currency(IAWPREPCBF.FTotal2210SchAI) + get_currency(IAWPREPCBF.FTotal4136) + get_currency(IAWPREPCBF.FTotal4562A) + get_currency(IAWPREPCBF.FTotal4562B) + get_currency(IAWPREPCBF.FTotal6251) + get_currency(IAWPREPCBF.FTotal8453) + get_currency(IAWPREPCBF.FTotal8801) + get_currency(IAWPREPCBF.FTotal8864) + get_currency(IAWPREPCBF.FOthAmt(0)) + get_currency(IAWPREPCBF.FOthAmt(1)) + get_currency(IAWPREPCBF.FOthAmt(2)) + get_currency(IAWPREPCBF.FOthAmt(3)) + get_currency(IAWPREPCBF.FOthAmt(4))
    return TotCharge1 + TotCharge2


