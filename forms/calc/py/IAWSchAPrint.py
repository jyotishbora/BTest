from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Alert10_Calculation():
    if GetNumber(IASchA.PrintSchA) == 1:
        if GetCurrency(IAWSchAPrint.OtherExp) != 0 and not IsValidEFileString(GetString(IAWSchAPrint.OtherMiscText)):
            ReturnVal = 1
        elif GetCurrency(IAWSchAPrint.OtherExp2) != 0 and not IsValidEFileString(GetString(IAWSchAPrint.OtherMiscText2)):
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def Alert20_Calculation():
    if GetNumber(IASchA.PrintSchA) == 1:
        if GetCurrency(IAWSchAPrint.OthExp) != 0 and not IsValidEFileString(GetString(IAWSchAPrint.OtherText)):
            ReturnVal = 1
        elif GetCurrency(IAWSchAPrint.OthExp2) != 0 and not IsValidEFileString(GetString(IAWSchAPrint.OtherText2)):
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def Alert30_Calculation():
    if GetNumber(IASchA.PrintSchA) == 1:
        if GetCurrency(IAWSchAPrint.Hobby) >  ( GetCurrency(IAWOthInc.TPHobby) + GetCurrency(IAWOthInc.SPHobby) ) :
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def Bond_Calculation():
    ReturnVal = GetCurrency(USWSchAPrint.Bond)

def CasualtyLoss_Calculation():
    TOne = Currency()

    TTwo = Currency()
    #believe current conditions being used to pull from 4684B ST and LT are not correct, the fed 4684 will not have amounts of an employee, just remove condition or use a different condition?
    #verify .Ln22Employee will still be calced on Fed Sch A
    #If GetCurrency(USF4684.STIncPro) > 0 Then
    TOne = GetCurrency(USF4684B.TotEmplST)
    #Else
    #    TOne = 0
    #End If
    #If GetCurrency(USF4684.L35bii) > 0 Then
    TTwo = GetCurrency(USF4684B.TotEmplLT)
    #Else
    #    TTwo = 0
    #End If
    ReturnVal = TOne + TTwo + GetCurrency(USSchA.Ln22Employee)

def Debt_Calculation():
    ReturnVal = GetCurrency(USWSchAPrint.Debt)

def Description_Calculation():
    if GetString(USWBasicInfo.FECombo) == '':
        ReturnVal = 'Iowa Itemized Deductions'
    else:
        ReturnVal = GetString(USWBasicInfo.FECombo)

def ExcessDed_Calculation():
    ReturnVal = GetCurrency(USDEstK1.ExcDed)

def Exist_Calculation():
    ReturnVal = 1

def F2106_Calculation():
    ReturnVal = GetCurrency(IA2106.SchAAMt)

def Form4684_Calculation():
    ReturnVal = GetCurrency(USWSchAPrint.Form4684)

def GamblingLoss_Calculation():
    ReturnVal = GetCurrency(USWSchAPrint.GamblingLoss)

def ImpWrkExp_Calculation():
    ReturnVal = GetCurrency(USWSchAPrint.ImpWrkExp)

def Indirect_Calculation():
    #how will these expenses now be reported by the entity? Seems they still need to be passed through. Will we have an entry point on fed at all?
    #ReturnVal = GetCurrency(USWPartK1Detail.PortfolioDed2) + GetCurrency(USWPartK1Detail.MiscItmDed) + GetCurrency(USWSCorpK1Detail.PortfolioDed2) + GetCurrency(USWSCorpK1Detail.MiscItmDed)
    ReturnVal = 0

def Invest_Calculation():
    ReturnVal = Round(GetCurrency(USD1099DIV.InvExp) + GetCurrency(USD1099INT.InvExp) + GetCurrency(USD1099OID.InvExp))

def K1DedPort_Calculation():
    ReturnVal = GetCurrency(USWSchAPrint.K1DedPort)

def Names_Calculation():
    ReturnVal = GetString(IARequired.CombNames)

def Pension_Calculation():
    ReturnVal = GetCurrency(USWSchAPrint.Pension)

def REMIC_Calculation():
    ReturnVal = GetCurrency(USSchEP2.RemicOtherInc)

def Repay_Calculation():
    ReturnVal = GetCurrency(USWSchAPrint.Repay)

def RepayInc_Calculation():
    if GetCurrency(USWUnempl.TPPrevUnemRepay) > Decimal("3000"):
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(USWUnempl.TPPrevUnemRepay)

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

def TotEstK1_Calculation():
    ReturnVal = GetCurrency(USWSchAPrint.TotEstK1)

def TotExp_Calculation():
    if GetBool(USWResidency.F1040NR) == True:
        ReturnVal = GetCurrency(IAWSchAPrint.Legal) + GetCurrency(IAWSchAPrint.OthLegal) + GetCurrency(IAWSchAPrint.Clerical) + GetCurrency(IAWSchAPrint.Custodial) + GetCurrency(IAWSchAPrint.Invest) + GetCurrency(IAWSchAPrint.InsolventLoss) + GetCurrency(IAWSchAPrint.CasualtyLoss) + GetCurrency(IAWSchAPrint.Appraisal) + GetCurrency(IAWSchAPrint.DeprTot) + GetCurrency(IAWSchAPrint.Amort) + GetCurrency(IAWSchAPrint.ExcessDed) + GetCurrency(IAWSchAPrint.Fees) + GetCurrency(IAWSchAPrint.Indirect) + GetCurrency(IAWSchAPrint.REMIC) + GetCurrency(IAWSchAPrint.IRALoss) + GetCurrency(IAWSchAPrint.RepayInc) + GetCurrency(IAWSchAPrint.SafeBox) + GetCurrency(IAWSchAPrint.ServiceCharge) + GetCurrency(IAWSchAPrint.TaxAdvice) + GetCurrency(IAWSchAPrint.Trustee) + GetCurrency(IAWSchAPrint.CreditFees) + GetCurrency(IAWSchAPrint.OthExp) + GetCurrency(IAWSchAPrint.OthExp2)
    else:
        ReturnVal = GetCurrency(IAWSchAPrint.Legal) + GetCurrency(IAWSchAPrint.OthLegal) + GetCurrency(IAWSchAPrint.Clerical) + GetCurrency(IAWSchAPrint.Custodial) + GetCurrency(IAWSchAPrint.Invest) + GetCurrency(IAWSchAPrint.InsolventLoss) + GetCurrency(IAWSchAPrint.CasualtyLoss) + GetCurrency(IAWSchAPrint.Appraisal) + GetCurrency(IAWSchAPrint.DeprTot) + GetCurrency(IAWSchAPrint.Amort) + GetCurrency(IAWSchAPrint.ExcessDed) + GetCurrency(IAWSchAPrint.Fees) + GetCurrency(IAWSchAPrint.Hobby) + GetCurrency(IAWSchAPrint.Indirect) + GetCurrency(IAWSchAPrint.REMIC) + GetCurrency(IAWSchAPrint.IRALoss) + GetCurrency(IAWSchAPrint.RepayInc) + GetCurrency(IAWSchAPrint.RepaySSB) + GetCurrency(IAWSchAPrint.SafeBox) + GetCurrency(IAWSchAPrint.ServiceCharge) + GetCurrency(IAWSchAPrint.TaxAdvice) + GetCurrency(IAWSchAPrint.Trustee) + GetCurrency(IAWSchAPrint.CreditFees) + GetCurrency(IAWSchAPrint.OthExp) + GetCurrency(IAWSchAPrint.OthExp2)

def TotOthDed_Calculation():
    if GetBool(USWResidency.F1040NR) == True:
        ReturnVal = GetCurrency(IAWSchAPrint.Form4684) + GetCurrency(IAWSchAPrint.K1DedPort) + GetCurrency(IAWSchAPrint.ImpWrkExp) + GetCurrency(IAWSchAPrint.Repay) + GetCurrency(IAWSchAPrint.Pension)
    else:
        ReturnVal = GetCurrency(IAWSchAPrint.Form4684) + GetCurrency(IAWSchAPrint.GamblingLoss) + GetCurrency(IAWSchAPrint.K1DedPort) + GetCurrency(IAWSchAPrint.ImpWrkExp) + GetCurrency(IAWSchAPrint.TotEstK1) + GetCurrency(IAWSchAPrint.Repay) + GetCurrency(IAWSchAPrint.Bond) + GetCurrency(IAWSchAPrint.Pension) + GetCurrency(IAWSchAPrint.Debt)

def TotOtherExp_Calculation():
    ReturnVal = GetCurrency(IAWSchAPrint.F2106) + GetCurrency(IAWSchAPrint.BadDebt) + GetCurrency(IAWSchAPrint.LiabilityPrem) + GetCurrency(IAWSchAPrint.Breach) + GetCurrency(IAWSchAPrint.ChamberDues) + GetCurrency(IAWSchAPrint.ProffDues) + GetCurrency(IAWSchAPrint.JobSearch) + GetCurrency(IAWSchAPrint.LabFees) + GetCurrency(IAWSchAPrint.LegalFees) + GetCurrency(IAWSchAPrint.LicenseFees) + GetCurrency(IAWSchAPrint.Malpractice) + GetCurrency(IAWSchAPrint.MedExam) + GetCurrency(IAWSchAPrint.Occupational) + GetCurrency(IAWSchAPrint.Passport) + GetCurrency(IAWSchAPrint.RepayEmpInc) + GetCurrency(IAWSchAPrint.Research) + GetCurrency(IAWSchAPrint.Subscriptions) + GetCurrency(IAWSchAPrint.Tools) + GetCurrency(IAWSchAPrint.Union) + GetCurrency(IAWSchAPrint.Uniforms) + GetCurrency(IAWSchAPrint.WorkEdu) + GetCurrency(IAWSchAPrint.OtherExp) + GetCurrency(IAWSchAPrint.OtherExp2)

def Union_Calculation():
    ReturnVal = Round(GetCurrency(USDW2.UnionDues))

