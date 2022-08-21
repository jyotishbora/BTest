from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Alert10_Calculation():
    if GetCurrency(IA2210.Penalty) > 0 and GetCurrency(IA2210.PYTax) == 0 and GetBool(IA2210.PYZero) == False:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert20_Calculation():
    if GetCurrency(IA2210Sp.Penalty) > 0 and GetCurrency(IA2210Sp.PYTax) == 0 and GetBool(IA2210Sp.PYZero) == False:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Amt8_Calculation():
    ReturnVal = CDollar(GetFloat(IA2210.Bal) * 0.9)

def Bal_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA2210.CYTax) - GetCurrency(IA2210.TotCr))

def ChildC_Calculation():
    ReturnVal = GetCurrency(IAF1040.AChild)

def CYTax_Calculation():
    ReturnVal = GetCurrency(IAF1040.ABal4)

def Description_Calculation():
    ReturnVal = CStr(GetCurrency(IA2210.Penalty)) + ' Penalty'

def EFile_Calculation():
    if GetBool(IA1040X.EFAmend) == True:
        ReturnVal = 0
    elif GetBool(IA2210.Print) == True:
        ReturnVal = 1
    elif GetCurrency(IA2210.Amt8) >= Decimal("200"):
        ReturnVal = 1
    else:
        ReturnVal = 0

def EFStQ1_Calculation():
    ReturnVal = GetCurrency(IAStateEst.TPStApply) + GetCurrency(IAStateEst.TPStQ1)

def ExpPenalty_Calculation():
    if GetCurrency(IA2210.Penalty) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Fuel_Calculation():
    ReturnVal = GetCurrency(IAF1040.AFuel)

def IAEIC_Calculation():
    ReturnVal = GetCurrency(IAF1040.AIEIC)

def Names_Calculation():
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetString(IARequired.TPCombName)
    else:
        ReturnVal = GetString(IARequired.CombNames)

def NoPen_Calculation():
    ReturnVal = GetBool(USWPrepMnNm.AlwaysState2210)

def Penalty_Calculation():
    if GetBool(IA2210.NoPen) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(IAPenalty.TotPen)

def Print_Calculation():
    if GetBool(IA2210.AnInc) == True:
        ReturnVal = 1
    elif GetCurrency(IA2210.Penalty) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def PYTax_Calculation():
    PYAGILimit = Currency()

    AGI = Currency()

    AGIBonus = Currency()
    if GetBool(USWSpouse.MFS) == True and GetBool(USWSpouse.NonRes) == False:
        PYAGILimit = Decimal("75000")
    else:
        PYAGILimit = Decimal("150000")
    if GetBool(USWSpouse.NonRes) == True:
        AGI = GetCurrency(USWRec.PYAGINR)
    elif IAFS() != 3:
        AGI = GetCurrency(USWRec.PYTAGI)
    else:
        AGI = GetCurrency(USWRec.PYAGI)
    if IAFS() != 3:
        AGIBonus = AGI + GetCurrency(USZIA1040.IATotBonus) + GetCurrency(USZIA1040.IATotBonusSp)
    else:
        AGIBonus = AGI + GetCurrency(USZIA1040.IATotBonus)
    if AGIBonus > PYAGILimit:
        ReturnVal = CDollar(GetFloat(USZIA1040.IA2210PYTax) * 1.1)
    else:
        ReturnVal = GetCurrency(USZIA1040.IA2210PYTax)

def Q1AnInc_Calculation():
    if GetBool(IA2210.AnInc) == True:
        ReturnVal = GetCurrency(IA2210An.Q1AIInstall)
    else:
        ReturnVal = 0

def Q1DaysB_Calculation():
    if GetCurrency(IA2210.Penalty) > 0:
        ReturnVal = 'See'
    else:
        ReturnVal = ''

def Q1Est_Calculation():
    ReturnVal = GetCurrency(IA2210.Q1WH) + GetCurrency(IAStateEst.TPStApply) + GetCurrency(IAStateEst.TPStQ1)

def Q1Install_Calculation():
    ReturnVal = CDollar(GetFloat(IA2210.Small) * 0.25)

def Q1Ln11_Calculation():
    if GetBool(IA2210.AnInc) == True:
        ReturnVal = GetCurrency(IA2210.Q1AnInc)
    else:
        ReturnVal = GetCurrency(IA2210.Q1Install)

def Q1Ln19a_Calculation():
    if GetCurrency(IA2210.Penalty) > 0:
        ReturnVal = 'Worksheet'
    else:
        ReturnVal = ''

def Q1Ln19B_Calculation():
    if GetCurrency(IA2210.Penalty) > 0:
        ReturnVal = 'Attached'
    else:
        ReturnVal = ''

def Q1Undpay_Calculation():
    if GetCurrency(IA2210.Q1Est) < GetCurrency(IA2210.Q1Ln11):
        ReturnVal = GetCurrency(IA2210.Q1Ln11) - GetCurrency(IA2210.Q1Est)
    else:
        ReturnVal = 0

def Q1WH_Calculation():
    ReturnVal = CDollar(CDbl(GetCurrency(IAF1040.AIATaxWith)) * 0.25)

def Q2AnInc_Calculation():
    if GetBool(IA2210.AnInc) == True:
        ReturnVal = GetCurrency(IA2210An.Q2AIInstall)
    else:
        ReturnVal = 0

def Q2est_Calculation():
    ReturnVal = GetCurrency(IA2210.Q2WH) + GetCurrency(IAStateEst.TPStQ2)

def Q2Install_Calculation():
    ReturnVal = CDollar(CDbl(GetCurrency(IA2210.Small) - GetCurrency(IA2210.Q1Install)) * 0.3333)

def Q2Ln11_Calculation():
    if GetBool(IA2210.AnInc) == True:
        ReturnVal = GetCurrency(IA2210.Q2AnInc)
    else:
        ReturnVal = GetCurrency(IA2210.Q2Install)

def Q2WH_Calculation():
    ReturnVal = CDollar(CDbl(GetCurrency(IAF1040.AIATaxWith) - GetCurrency(IA2210.Q1WH)) * 0.3333)

def Q3AnInc_Calculation():
    if GetBool(IA2210.AnInc) == True:
        ReturnVal = GetCurrency(IA2210An.Q3AIInstall)
    else:
        ReturnVal = 0

def Q3Est_Calculation():
    ReturnVal = GetCurrency(IA2210.Q3WH) + GetCurrency(IAStateEst.TPStQ3)

def Q3Install_Calculation():
    ReturnVal = CDollar(CDbl(GetCurrency(IA2210.Small) - GetCurrency(IA2210.Q1Install) - GetCurrency(IA2210.Q2Install)) * 0.5)

def Q3Ln11_Calculation():
    if GetBool(IA2210.AnInc) == True:
        ReturnVal = GetCurrency(IA2210.Q3AnInc)
    else:
        ReturnVal = GetCurrency(IA2210.Q3Install)

def Q3WH_Calculation():
    ReturnVal = CDollar(CDbl(GetCurrency(IAF1040.AIATaxWith) - GetCurrency(IA2210.Q1WH) - GetCurrency(IA2210.Q2WH)) * 0.5)

def Q4AnInc_Calculation():
    if GetBool(IA2210.AnInc) == True:
        ReturnVal = GetCurrency(IA2210An.Q4AIInstall)
    else:
        ReturnVal = 0

def Q4Est_Calculation():
    ReturnVal = GetCurrency(IA2210.Q4WH) + GetCurrency(IAStateEst.TPStQ4)

def Q4Install_Calculation():
    ReturnVal = GetCurrency(IA2210.Small) - GetCurrency(IA2210.Q1Install) - GetCurrency(IA2210.Q2Install) - GetCurrency(IA2210.Q3Install)

def Q4Ln11_Calculation():
    if GetBool(IA2210.AnInc) == True:
        ReturnVal = GetCurrency(IA2210.Q4AnInc)
    else:
        ReturnVal = GetCurrency(IA2210.Q4Install)

def Q4WH_Calculation():
    ReturnVal = GetCurrency(IAF1040.AIATaxWith) - GetCurrency(IA2210.Q1WH) - GetCurrency(IA2210.Q2WH) - GetCurrency(IA2210.Q3WH)

def RefundCr_Calculation():
    ReturnVal = GetCurrency(IAF1040.AOthRefCr)

def Small_Calculation():
    if GetBool(IA2210.NoPen) == True:
        ReturnVal = 0
    elif GetCurrency(IA2210.Amt8) < Decimal("200"):
        ReturnVal = 0
    elif GetBool(IA2210.PYZero) == True:
        ReturnVal = 0
    elif GetCurrency(IA2210.PYTax) == 0:
        ReturnVal = GetCurrency(IA2210.Amt8)
    else:
        ReturnVal = MinValue(GetCurrency(IA2210.Amt8), GetCurrency(IA2210.PYTax))

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

def TotCr_Calculation():
    ReturnVal = GetCurrency(IA2210.Fuel) + GetCurrency(IA2210.ChildC) + GetCurrency(IA2210.IAEIC) + GetCurrency(IA2210.RefundCr)

