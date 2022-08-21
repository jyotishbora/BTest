from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def CBF_Calculation():
    ReturnVal = GetBool(USWPrepBInv.StY)

def CBF1040_Calculation():
    ReturnVal = GetCurrency(USZIAMasterCBF.CBF1040)

def CBF1040ES_Calculation():
    ReturnVal = GetCurrency(USZIAMasterCBF.CBF1040ES)

def CBF1040V_Calculation():
    ReturnVal = GetCurrency(USZIAMasterCBF.CBF1040V)

def CBF1040X_Calculation():
    ReturnVal = GetCurrency(USZIAMasterCBF.CBF1040X)

def CBF1040XV_Calculation():
    ReturnVal = GetCurrency(USZIAMasterCBF.CBF1040XV)

def CBF2210_Calculation():
    ReturnVal = GetCurrency(USZIAMasterCBF.CBF2210)

def CBF2210SchAI_Calculation():
    ReturnVal = GetCurrency(USZIAMasterCBF.CBF2210SchAI)

def CBF4136_Calculation():
    ReturnVal = GetCurrency(USZIAMasterCBF.CBF4136)

def CBF4562A_Calculation():
    ReturnVal = GetCurrency(USZIAMasterCBF.CBF4562A)

def CBF4562B_Calculation():
    ReturnVal = GetCurrency(USZIAMasterCBF.CBF4562B)

def CBF6251_Calculation():
    ReturnVal = GetCurrency(USZIAMasterCBF.CBF6251)

def CBF8453_Calculation():
    ReturnVal = GetCurrency(USZIAMasterCBF.CBF8453)

def CBF8801_Calculation():
    ReturnVal = GetCurrency(USZIAMasterCBF.CBF8801)

def CBF8864_Calculation():
    ReturnVal = GetCurrency(USZIAMasterCBF.CBF8864)

def CBFName_Calculation():
    ReturnVal = GetString(IARequired.CombNames)

def CBFOthAmt_Calculation(Index):
    ReturnVal = GetCurrency(USZIAMasterCBF.CBFOthAmt(Index))

def CBFSch126_Calculation():
    ReturnVal = GetCurrency(USZIAMasterCBF.CBFSch126)

def CBFSch128_Calculation():
    ReturnVal = GetCurrency(USZIAMasterCBF.CBFSch128)

def CBFSch128S_Calculation():
    ReturnVal = GetCurrency(USZIAMasterCBF.CBFSch128S)

def CBFSch130_Calculation():
    ReturnVal = GetCurrency(USZIAMasterCBF.CBFSch130)

def CBFSch134_Calculation():
    ReturnVal = GetCurrency(USZIAMasterCBF.CBFSch134)

def CBFSch135_Calculation():
    ReturnVal = GetCurrency(USZIAMasterCBF.CBFSch135)

def CBFSch137_Calculation():
    ReturnVal = GetCurrency(USZIAMasterCBF.CBFSch137)

def CBFSch138_Calculation():
    ReturnVal = GetCurrency(USZIAMasterCBF.CBFSch138)

def CBFSch147_Calculation():
    ReturnVal = GetCurrency(USZIAMasterCBF.CBFSch147)

def CBFSch148_Calculation():
    ReturnVal = GetCurrency(USZIAMasterCBF.CBFSch148)

def CBFSch177_Calculation():
    ReturnVal = GetCurrency(USZIAMasterCBF.CBFSch177)

def CBFSchA_Calculation():
    ReturnVal = GetCurrency(USZIAMasterCBF.CBFSchA)

def CBFSchB_Calculation():
    ReturnVal = GetCurrency(USZIAMasterCBF.CBFSchB)

def CF147_Calculation():
    ReturnVal = GetNumber(IA147.Print)

def CF177_Calculation():
    ReturnVal = GetNumber(IA177.Print)

def CF1040_Calculation():
    ReturnVal = 1

def CF126_Calculation():
    ReturnVal = GetNumber(IAF126.Print)

def CF128_Calculation():
    ReturnVal = GetNumber(IA128.Print)

def CF128S_Calculation():
    ReturnVal = GetNumber(IA128S.Print)

def CF130_Calculation():
    ReturnVal = GetNumber(IA130.PrintMe)

def CF134_Calculation():
    ReturnVal = GetNumber(IA134.Print) + GetNumber(IA134Sp.Print)

def CF135_Calculation():
    ReturnVal = GetNumber(IA135.Print)

def CF137_Calculation():
    ReturnVal = GetNumber(IA137.Print)

def CF138_Calculation():
    ReturnVal = GetNumber(IA138.Print)

def CF148_Calculation():
    ReturnVal = GetNumber(IA148.Print) + GetNumber(IA148Sp.Print)

def CF1040V_Calculation():
    ReturnVal = GetNumber(IA1040V.PrVou)

def CF1040XV_Calculation():
    ReturnVal = GetNumber(IA1040XV.PrVou)

def CF2210_Calculation():
    ReturnVal = GetNumber(IA2210.Print) + GetNumber(IA2210Sp.Print)

def CF2210SchAI_Calculation():
    ReturnVal = GetNumber(IA2210An.Print) + GetNumber(IA2210AnSp.Print)

def CF4136_Calculation():
    ReturnVal = GetBool(IASch4136.TotCr, 1) + GetBool(IASch4136.TotCr, 2)

def CF4562A_Calculation():
    ReturnVal = GetNumber(IA4562.PrIA4562) + GetNumber(IA4562Sp.PrIA4562) + GetNumber(IA4562A.PrIA4562A)

def CF4562B_Calculation():
    ReturnVal = GetNumber(IA4562B.Print) + GetNumber(IA4562BSp.Print)

def CF6251_Calculation():
    ReturnVal = GetNumber(IA6251.Print) + GetNumber(IA6251Sp.Print)

def CF8801_Calculation():
    ReturnVal = GetNumber(IA8801.Print) + GetNumber(IA8801Sp.Print)

def CF8864_Calculation():
    ReturnVal = GetNumber(IA8864.Print)

def CFA_Calculation():
    ReturnVal = GetNumber(IASchA.PrintSchA)

def CFB_Calculation():
    ReturnVal = GetNumber(IASchB.PrintIAB)

def CFES_Calculation():
    ReturnVal = GetNumber(IAEstimates.Print)

def CFX_Calculation():
    ReturnVal = GetNumber(IA1040X.Exist)

def CopFOthName_Calculation(Index):
    ReturnVal = GetString(USZIAMasterCBF.CBFOth1Name(Index))

def FOthAmt_Calculation(Index):
    ReturnVal = GetCurrency(IAWPrepCBF.CopFOth(Index)) * GetCurrency(IAWPrepCBF.CBFOthAmt(Index))

def FTotal1040_Calculation():
    ReturnVal = GetCurrency(IAWPrepCBF.CF1040) * GetCurrency(IAWPrepCBF.CBF1040)

def FTotal1040ES_Calculation():
    ReturnVal = GetCurrency(IAWPrepCBF.CFES) * GetCurrency(IAWPrepCBF.CBF1040ES)

def FTotal1040V_Calculation():
    ReturnVal = GetCurrency(IAWPrepCBF.CF1040V) * GetCurrency(IAWPrepCBF.CBF1040V)

def FTotal1040X_Calculation():
    ReturnVal = GetCurrency(IAWPrepCBF.CFX) * GetCurrency(IAWPrepCBF.CBF1040X)

def FTotal1040XV_Calculation():
    ReturnVal = GetCurrency(IAWPrepCBF.CF1040XV) * GetCurrency(IAWPrepCBF.CBF1040XV)

def FTotal2210_Calculation():
    ReturnVal = GetCurrency(IAWPrepCBF.CF2210) * GetCurrency(IAWPrepCBF.CBF2210)

def FTotal2210SchAI_Calculation():
    ReturnVal = GetCurrency(IAWPrepCBF.CF2210SchAI) * GetCurrency(IAWPrepCBF.CBF2210SchAI)

def FTotal4136_Calculation():
    ReturnVal = GetCurrency(IAWPrepCBF.CF4136) * GetCurrency(IAWPrepCBF.CBF4136)

def FTotal4562A_Calculation():
    ReturnVal = GetCurrency(IAWPrepCBF.CF4562A) * GetCurrency(IAWPrepCBF.CBF4562A)

def FTotal4562B_Calculation():
    ReturnVal = GetCurrency(IAWPrepCBF.CF4562B) * GetCurrency(IAWPrepCBF.CBF4562B)

def FTotal6251_Calculation():
    ReturnVal = GetCurrency(IAWPrepCBF.CF6251) * GetCurrency(IAWPrepCBF.CBF6251)

def FTotal8453_Calculation():
    ReturnVal = GetCurrency(IAWPrepCBF.CF8453) * GetCurrency(IAWPrepCBF.CBF8453)

def FTotal8801_Calculation():
    ReturnVal = GetCurrency(IAWPrepCBF.CF8801) * GetCurrency(IAWPrepCBF.CBF8801)

def FTotal8864_Calculation():
    ReturnVal = GetCurrency(IAWPrepCBF.CF8864) * GetCurrency(IAWPrepCBF.CBF8864)

def FTotalSch126_Calculation():
    ReturnVal = GetCurrency(IAWPrepCBF.CF126) * GetCurrency(IAWPrepCBF.CBFSch126)

def FTotalSch128_Calculation():
    ReturnVal = GetCurrency(IAWPrepCBF.CF128) * GetCurrency(IAWPrepCBF.CBFSch128)

def FTotalSch128S_Calculation():
    ReturnVal = GetCurrency(IAWPrepCBF.CF128S) * GetCurrency(IAWPrepCBF.CBFSch128S)

def FTotalSch130_Calculation():
    ReturnVal = GetCurrency(IAWPrepCBF.CF130) * GetCurrency(IAWPrepCBF.CBFSch130)

def FTotalSch134_Calculation():
    ReturnVal = GetCurrency(IAWPrepCBF.CF134) * GetCurrency(IAWPrepCBF.CBFSch134)

def FTotalSch135_Calculation():
    ReturnVal = GetCurrency(IAWPrepCBF.CF135) * GetCurrency(IAWPrepCBF.CBFSch135)

def FTotalSch137_Calculation():
    ReturnVal = GetCurrency(IAWPrepCBF.CF137) * GetCurrency(IAWPrepCBF.CBFSch137)

def FTotalSch138_Calculation():
    ReturnVal = GetCurrency(IAWPrepCBF.CF138) * GetCurrency(IAWPrepCBF.CBFSch138)

def FTotalSch147_Calculation():
    ReturnVal = GetCurrency(IAWPrepCBF.CF147) * GetCurrency(IAWPrepCBF.CBFSch147)

def FTotalSch148_Calculation():
    ReturnVal = GetCurrency(IAWPrepCBF.CF148) * GetCurrency(IAWPrepCBF.CBFSch148)

def FTotalSch177_Calculation():
    ReturnVal = GetCurrency(IAWPrepCBF.CF177) * GetCurrency(IAWPrepCBF.CBFSch177)

def FTotalSchA_Calculation():
    ReturnVal = GetCurrency(IAWPrepCBF.CFA) * GetCurrency(IAWPrepCBF.CBFSchA)

def FTotalSchB_Calculation():
    ReturnVal = GetCurrency(IAWPrepCBF.CFB) * GetCurrency(IAWPrepCBF.CBFSchB)

def TotCharge_Calculation():
    TotCharge1 = Currency()

    TotCharge2 = Currency()
    TotCharge1 = GetCurrency(IAWPrepCBF.FTotal1040) + GetCurrency(IAWPrepCBF.FTotal1040ES) + GetCurrency(IAWPrepCBF.FTotal1040V) + GetCurrency(IAWPrepCBF.FTotal1040X) + GetCurrency(IAWPrepCBF.FTotal1040XV) + GetCurrency(IAWPrepCBF.FTotalSchA) + GetCurrency(IAWPrepCBF.FTotalSchB) + GetCurrency(IAWPrepCBF.FTotalSch126) + GetCurrency(IAWPrepCBF.FTotalSch128) + GetCurrency(IAWPrepCBF.FTotalSch128S) + GetCurrency(IAWPrepCBF.FTotalSch130) + GetCurrency(IAWPrepCBF.FTotalSch134) + GetCurrency(IAWPrepCBF.FTotalSch135) + GetCurrency(IAWPrepCBF.FTotalSch137) + GetCurrency(IAWPrepCBF.FTotalSch138) + GetCurrency(IAWPrepCBF.FTotalSch147) + GetCurrency(IAWPrepCBF.FTotalSch148)
    TotCharge2 = GetCurrency(IAWPrepCBF.FTotalSch177) + GetCurrency(IAWPrepCBF.FTotal2210) + GetCurrency(IAWPrepCBF.FTotal2210SchAI) + GetCurrency(IAWPrepCBF.FTotal4136) + GetCurrency(IAWPrepCBF.FTotal4562A) + GetCurrency(IAWPrepCBF.FTotal4562B) + GetCurrency(IAWPrepCBF.FTotal6251) + GetCurrency(IAWPrepCBF.FTotal8453) + GetCurrency(IAWPrepCBF.FTotal8801) + GetCurrency(IAWPrepCBF.FTotal8864) + GetCurrency(IAWPrepCBF.FOthAmt(0)) + GetCurrency(IAWPrepCBF.FOthAmt(1)) + GetCurrency(IAWPrepCBF.FOthAmt(2)) + GetCurrency(IAWPrepCBF.FOthAmt(3)) + GetCurrency(IAWPrepCBF.FOthAmt(4))
    ReturnVal = TotCharge1 + TotCharge2

