from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Amt8_Calculation():
    ReturnVal = CDollar(GetFloat(IA2210Sp.Bal) * 0.9)

def Bal_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2210Sp.CYTax) - GetCurrency(IA2210Sp.TotCr))

def ChildC_Calculation():
    ReturnVal = GetCurrency(IAF1040.BChild)

def CYTax_Calculation():
    ReturnVal = GetCurrency(IAF1040.BBal4)

def Description_Calculation():
    ReturnVal = CStr(GetCurrency(IA2210Sp.Penalty)) + ' Penalty'

def EFile_Calculation():
    if GetBool(IA1040X.EFAmend) == True:
        ReturnVal = 0
    elif GetBool(IAF1040.CombMFS) == False:
        ReturnVal = 0
    elif GetBool(IA2210Sp.Print) == True:
        ReturnVal = 1
    elif GetCurrency(IA2210Sp.Amt8) >= Decimal("200"):
        ReturnVal = 1
    else:
        ReturnVal = 0

def EFStQ1_Calculation():
    ReturnVal = GetCurrency(IAStateEst.SPStApply) + GetCurrency(IAStateEst.SPStQ1)

def ExpPenalty_Calculation():
    if GetCurrency(IA2210SP.Penalty) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Fuel_Calculation():
    ReturnVal = GetCurrency(IAF1040.BFuel)

def IAEIC_Calculation():
    ReturnVal = GetCurrency(IAF1040.BIEIC)

def Names_Calculation():
    ReturnVal = GetString(IARequired.SPCombName)

def NoPen_Calculation():
    ReturnVal = GetBool(USWPrepMnNm.AlwaysState2210)

def Penalty_Calculation():
    if GetBool(IAF1040.CombMFS) == False:
        ReturnVal = 0
    elif GetBool(IA2210Sp.NoPen) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(IAPenaltySp.TotPen)

def Print_Calculation():
    if GetBool(IAF1040.CombMFS) == False:
        ReturnVal = 0
    elif GetBool(IA2210Sp.AnInc) == True:
        ReturnVal = 1
    elif GetCurrency(IA2210Sp.Penalty) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def PYTax_Calculation():
    AGIBonus = Currency()
    AGIBonus = GetCurrency(USWRec.PYSAGI) + GetCurrency(USZIA1040.IATotBonusSp)
    if GetBool(IAF1040.CombMFS) == False:
        ReturnVal = 0
    elif GetString(USZIA1040.IAPYFS) == GetString(IARequired.FilingStatus):
        if AGIBonus > Decimal("150000"):
            ReturnVal = CDollar(GetFloat(USZIA1040.IA2210PYTaxSp) * 1.1)
        else:
            ReturnVal = GetCurrency(USZIA1040.IA2210PYTaxSp)
    else:
        ReturnVal = 0

def Q1AnInc_Calculation():
    if GetBool(IA2210Sp.AnInc) == True:
        ReturnVal = GetCurrency(IA2210AnSp.Q1AIInstall)
    else:
        ReturnVal = 0

def Q1DaysB_Calculation():
    if GetCurrency(IA2210Sp.Penalty) > 0:
        ReturnVal = 'See'
    else:
        ReturnVal = ''

def Q1Est_Calculation():
    ReturnVal = GetCurrency(IA2210Sp.Q1WH) + GetCurrency(IAStateEst.SPStApply) + GetCurrency(IAStateEst.SPStQ1)

def Q1Install_Calculation():
    ReturnVal = CDollar(GetFloat(IA2210Sp.Small) * 0.25)

def Q1Ln11_Calculation():
    if GetBool(IA2210Sp.AnInc) == True:
        ReturnVal = GetCurrency(IA2210Sp.Q1AnInc)
    else:
        ReturnVal = GetCurrency(IA2210Sp.Q1Install)

def Q1Ln19a_Calculation():
    if GetCurrency(IA2210Sp.Penalty) > 0:
        ReturnVal = 'Worksheet'
    else:
        ReturnVal = ''

def Q1Ln19B_Calculation():
    if GetCurrency(IA2210Sp.Penalty) > 0:
        ReturnVal = 'Attached'
    else:
        ReturnVal = ''

def Q1Undpay_Calculation():
    if GetCurrency(IA2210Sp.Q1Est) < GetCurrency(IA2210Sp.Q1Ln11):
        ReturnVal = GetCurrency(IA2210Sp.Q1Ln11) - GetCurrency(IA2210Sp.Q1Est)
    else:
        ReturnVal = 0

def Q1WH_Calculation():
    ReturnVal = CDollar(CDbl(GetCurrency(IAF1040.BIATaxWith)) * 0.25)

def Q2AnInc_Calculation():
    if GetBool(IA2210Sp.AnInc) == True:
        ReturnVal = GetCurrency(IA2210AnSp.Q2AIInstall)
    else:
        ReturnVal = 0

def Q2est_Calculation():
    ReturnVal = GetCurrency(IA2210Sp.Q2WH) + GetCurrency(IAStateEst.SPStQ2)

def Q2Install_Calculation():
    ReturnVal = CDollar(CDbl(GetCurrency(IA2210Sp.Small) - GetCurrency(IA2210Sp.Q1Install)) * 0.3333)

def Q2Ln11_Calculation():
    if GetBool(IA2210Sp.AnInc) == True:
        ReturnVal = GetCurrency(IA2210Sp.Q2AnInc)
    else:
        ReturnVal = GetCurrency(IA2210Sp.Q2Install)

def Q2WH_Calculation():
    ReturnVal = CDollar(CDbl(GetCurrency(IAF1040.BIATaxWith) - GetCurrency(IA2210Sp.Q1WH)) * 0.3333)

def Q3AnInc_Calculation():
    if GetBool(IA2210Sp.AnInc) == True:
        ReturnVal = GetCurrency(IA2210AnSp.Q3AIInstall)
    else:
        ReturnVal = 0

def Q3Est_Calculation():
    ReturnVal = GetCurrency(IA2210Sp.Q3WH) + GetCurrency(IAStateEst.SPStQ3)

def Q3Install_Calculation():
    ReturnVal = CDollar(CDbl(GetCurrency(IA2210Sp.Small) - GetCurrency(IA2210Sp.Q1Install) - GetCurrency(IA2210Sp.Q2Install)) * 0.5)

def Q3Ln11_Calculation():
    if GetBool(IA2210Sp.AnInc) == True:
        ReturnVal = GetCurrency(IA2210Sp.Q3AnInc)
    else:
        ReturnVal = GetCurrency(IA2210Sp.Q3Install)

def Q3WH_Calculation():
    ReturnVal = CDollar(CDbl(GetCurrency(IAF1040.BIATaxWith) - GetCurrency(IA2210Sp.Q1WH) - GetCurrency(IA2210Sp.Q2WH)) * 0.5)

def Q4AnInc_Calculation():
    if GetBool(IA2210Sp.AnInc) == True:
        ReturnVal = GetCurrency(IA2210AnSp.Q4AIInstall)
    else:
        ReturnVal = 0

def Q4Est_Calculation():
    ReturnVal = GetCurrency(IA2210Sp.Q4WH) + GetCurrency(IAStateEst.SPStQ4)

def Q4Install_Calculation():
    ReturnVal = GetCurrency(IA2210Sp.Small) - GetCurrency(IA2210Sp.Q1Install) - GetCurrency(IA2210Sp.Q2Install) - GetCurrency(IA2210Sp.Q3Install)

def Q4Ln11_Calculation():
    if GetBool(IA2210Sp.AnInc) == True:
        ReturnVal = GetCurrency(IA2210Sp.Q4AnInc)
    else:
        ReturnVal = GetCurrency(IA2210Sp.Q4Install)

def Q4WH_Calculation():
    ReturnVal = GetCurrency(IAF1040.BIATaxWith) - GetCurrency(IA2210Sp.Q1WH) - GetCurrency(IA2210Sp.Q2WH) - GetCurrency(IA2210Sp.Q3WH)

def RefundCr_Calculation():
    ReturnVal = GetCurrency(IAF1040.BOthRefCr)

def Small_Calculation():
    if GetBool(IAF1040.CombMFS) == False:
        ReturnVal = 0
    elif GetBool(IA2210Sp.NoPen) == True:
        ReturnVal = 0
    elif GetCurrency(IA2210Sp.Amt8) < Decimal("200"):
        ReturnVal = 0
    elif GetBool(IA2210Sp.PYZero) == True:
        ReturnVal = 0
    elif GetCurrency(IA2210Sp.PYTax) == 0:
        ReturnVal = GetCurrency(IA2210Sp.Amt8)
    else:
        ReturnVal = MinValue(GetCurrency(IA2210Sp.Amt8), GetCurrency(IA2210Sp.PYTax))

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SpouseSSN)

def TotCr_Calculation():
    ReturnVal = GetCurrency(IA2210Sp.Fuel) + GetCurrency(IA2210Sp.ChildC) + GetCurrency(IA2210Sp.IAEIC) + GetCurrency(IA2210Sp.RefundCr)

