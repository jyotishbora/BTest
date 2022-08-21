from forms.out import IA2106
from forms.out import IAF1040
from forms.out import IAREQUIRED
from forms.out import IASCHA
from forms.out import IAWOTHINC
from forms.out import IAWSCHAPRINT
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Alert10_Calculation():
    if get_number(IASCHA.PrintSchA) == 1:
        if get_currency(IAWSCHAPRINT.OtherExp) != 0 and not IsValidEFileString(get_string(IAWSCHAPRINT.OtherMiscText)):
            return 1
        elif get_currency(IAWSCHAPRINT.OtherExp2) != 0 and not IsValidEFileString(get_string(IAWSCHAPRINT.OtherMiscText2)):
            return 1
        else:
            return 0
    else:
        return 0

def Alert20_Calculation():
    if get_number(IASCHA.PrintSchA) == 1:
        if get_currency(IAWSCHAPRINT.OthExp) != 0 and not IsValidEFileString(get_string(IAWSCHAPRINT.OtherText)):
            return 1
        elif get_currency(IAWSCHAPRINT.OthExp2) != 0 and not IsValidEFileString(get_string(IAWSCHAPRINT.OtherText2)):
            return 1
        else:
            return 0
    else:
        return 0

def Alert30_Calculation():
    if get_number(IASCHA.PrintSchA) == 1:
        if get_currency(IAWSCHAPRINT.Hobby) >  ( get_currency(IAWOTHINC.TPHobby) + get_currency(IAWOTHINC.SPHobby) ) :
            return 1
        else:
            return 0
    else:
        return 0

def Bond_Calculation():
    return get_currency(USWSchAPrint.Bond)

def CasualtyLoss_Calculation():
    TOne = Currency()

    TTwo = Currency()
    #believe current conditions being used to pull from 4684B ST and LT are not correct, the fed 4684 will not have amounts of an employee, just remove condition or use a different condition?
    #verify .Ln22Employee will still be calced on Fed Sch A
    #If get_currency(USF4684.STIncPro) > 0 Then
    TOne = get_currency(USF4684B.TotEmplST)
    #Else
    #    TOne = 0
    #End If
    #If get_currency(USF4684.L35bii) > 0 Then
    TTwo = get_currency(USF4684B.TotEmplLT)
    #Else
    #    TTwo = 0
    #End If
    return TOne + TTwo + get_currency(USSchA.Ln22Employee)

def Debt_Calculation():
    return get_currency(USWSchAPrint.Debt)

def Description_Calculation():
    if get_string(USWBasicInfo.FECombo) == '':
        return 'Iowa Itemized Deductions'
    else:
        return get_string(USWBasicInfo.FECombo)

def ExcessDed_Calculation():
    return get_currency(USDEstK1.ExcDed)

def Exist_Calculation():
    return 1

def F2106_Calculation():
    return get_currency(IA2106.SchAAMt)

def Form4684_Calculation():
    return get_currency(USWSchAPrint.Form4684)

def GamblingLoss_Calculation():
    return get_currency(USWSchAPrint.GamblingLoss)

def ImpWrkExp_Calculation():
    return get_currency(USWSchAPrint.ImpWrkExp)

def Indirect_Calculation():
    #how will these expenses now be reported by the entity? Seems they still need to be passed through. Will we have an entry point on fed at all?
    #return get_currency(USWPartK1Detail.PortfolioDed2) + get_currency(USWPartK1Detail.MiscItmDed) + get_currency(USWSCorpK1Detail.PortfolioDed2) + get_currency(USWSCorpK1Detail.MiscItmDed)
    return 0

def Invest_Calculation():
    return Round(get_currency(USD1099DIV.InvExp) + get_currency(USD1099INT.InvExp) + get_currency(USD1099OID.InvExp))

def K1DedPort_Calculation():
    return get_currency(USWSchAPrint.K1DedPort)

def Names_Calculation():
    return get_string(IAREQUIRED.CombNames)

def Pension_Calculation():
    return get_currency(USWSchAPrint.Pension)

def REMIC_Calculation():
    return get_currency(USSchEP2.RemicOtherInc)

def Repay_Calculation():
    return get_currency(USWSchAPrint.Repay)

def RepayInc_Calculation():
    if get_currency(USWUnempl.TPPrevUnemRepay) > Decimal("3000"):
        return 0
    else:
        return get_currency(USWUnempl.TPPrevUnemRepay)

def SSN_Calculation():
    return get_string(IAF1040.SSN)

def TotEstK1_Calculation():
    return get_currency(USWSchAPrint.TotEstK1)

def TotExp_Calculation():
    if get_bool(USWResidency.F1040NR) == True:
        return get_currency(IAWSCHAPRINT.Legal) + get_currency(IAWSCHAPRINT.OthLegal) + get_currency(IAWSCHAPRINT.Clerical) + get_currency(IAWSCHAPRINT.Custodial) + get_currency(IAWSCHAPRINT.Invest) + get_currency(IAWSCHAPRINT.InsolventLoss) + get_currency(IAWSCHAPRINT.CasualtyLoss) + get_currency(IAWSCHAPRINT.Appraisal) + get_currency(IAWSCHAPRINT.DeprTot) + get_currency(IAWSCHAPRINT.Amort) + get_currency(IAWSCHAPRINT.ExcessDed) + get_currency(IAWSCHAPRINT.Fees) + get_currency(IAWSCHAPRINT.Indirect) + get_currency(IAWSCHAPRINT.REMIC) + get_currency(IAWSCHAPRINT.IRALoss) + get_currency(IAWSCHAPRINT.RepayInc) + get_currency(IAWSCHAPRINT.SafeBox) + get_currency(IAWSCHAPRINT.ServiceCharge) + get_currency(IAWSCHAPRINT.TaxAdvice) + get_currency(IAWSCHAPRINT.Trustee) + get_currency(IAWSCHAPRINT.CreditFees) + get_currency(IAWSCHAPRINT.OthExp) + get_currency(IAWSCHAPRINT.OthExp2)
    else:
        return get_currency(IAWSCHAPRINT.Legal) + get_currency(IAWSCHAPRINT.OthLegal) + get_currency(IAWSCHAPRINT.Clerical) + get_currency(IAWSCHAPRINT.Custodial) + get_currency(IAWSCHAPRINT.Invest) + get_currency(IAWSCHAPRINT.InsolventLoss) + get_currency(IAWSCHAPRINT.CasualtyLoss) + get_currency(IAWSCHAPRINT.Appraisal) + get_currency(IAWSCHAPRINT.DeprTot) + get_currency(IAWSCHAPRINT.Amort) + get_currency(IAWSCHAPRINT.ExcessDed) + get_currency(IAWSCHAPRINT.Fees) + get_currency(IAWSCHAPRINT.Hobby) + get_currency(IAWSCHAPRINT.Indirect) + get_currency(IAWSCHAPRINT.REMIC) + get_currency(IAWSCHAPRINT.IRALoss) + get_currency(IAWSCHAPRINT.RepayInc) + get_currency(IAWSCHAPRINT.RepaySSB) + get_currency(IAWSCHAPRINT.SafeBox) + get_currency(IAWSCHAPRINT.ServiceCharge) + get_currency(IAWSCHAPRINT.TaxAdvice) + get_currency(IAWSCHAPRINT.Trustee) + get_currency(IAWSCHAPRINT.CreditFees) + get_currency(IAWSCHAPRINT.OthExp) + get_currency(IAWSCHAPRINT.OthExp2)

def TotOthDed_Calculation():
    if get_bool(USWResidency.F1040NR) == True:
        return get_currency(IAWSCHAPRINT.Form4684) + get_currency(IAWSCHAPRINT.K1DedPort) + get_currency(IAWSCHAPRINT.ImpWrkExp) + get_currency(IAWSCHAPRINT.Repay) + get_currency(IAWSCHAPRINT.Pension)
    else:
        return get_currency(IAWSCHAPRINT.Form4684) + get_currency(IAWSCHAPRINT.GamblingLoss) + get_currency(IAWSCHAPRINT.K1DedPort) + get_currency(IAWSCHAPRINT.ImpWrkExp) + get_currency(IAWSCHAPRINT.TotEstK1) + get_currency(IAWSCHAPRINT.Repay) + get_currency(IAWSCHAPRINT.Bond) + get_currency(IAWSCHAPRINT.Pension) + get_currency(IAWSCHAPRINT.Debt)

def TotOtherExp_Calculation():
    return get_currency(IAWSCHAPRINT.F2106) + get_currency(IAWSCHAPRINT.BadDebt) + get_currency(IAWSCHAPRINT.LiabilityPrem) + get_currency(IAWSCHAPRINT.Breach) + get_currency(IAWSCHAPRINT.ChamberDues) + get_currency(IAWSCHAPRINT.ProffDues) + get_currency(IAWSCHAPRINT.JobSearch) + get_currency(IAWSCHAPRINT.LabFees) + get_currency(IAWSCHAPRINT.LegalFees) + get_currency(IAWSCHAPRINT.LicenseFees) + get_currency(IAWSCHAPRINT.Malpractice) + get_currency(IAWSCHAPRINT.MedExam) + get_currency(IAWSCHAPRINT.Occupational) + get_currency(IAWSCHAPRINT.Passport) + get_currency(IAWSCHAPRINT.RepayEmpInc) + get_currency(IAWSCHAPRINT.Research) + get_currency(IAWSCHAPRINT.Subscriptions) + get_currency(IAWSCHAPRINT.Tools) + get_currency(IAWSCHAPRINT.Union) + get_currency(IAWSCHAPRINT.Uniforms) + get_currency(IAWSCHAPRINT.WorkEdu) + get_currency(IAWSCHAPRINT.OtherExp) + get_currency(IAWSCHAPRINT.OtherExp2)

def Union_Calculation():
    return Round(get_currency(USDW2.UnionDues))


