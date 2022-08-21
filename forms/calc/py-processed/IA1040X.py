from forms.out import IA1040X
from forms.out import IAF1040
from forms.out import IAREQUIRED
from forms.out import IAWKALTTAX
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def AAltTax_Calculation():
    # 1st condition added for situation when MFS return and reporting spouse income causes an alternate tax calculation yet taxpayer has zero income
    # See saved return IA MFS Alternate Tax Issue.ta2
    if get_bool(IA1040X.MFS) == True and get_currency(IA1040X.ATaxInc) == 0:
        return 0
    elif  ( get_currency(IAWKALTTAX.Mult) < get_currency(IA1040X.TotTaxSch) )  and get_bool(IAWKALTTAX.Qualify) == True:
        return get_currency(IAF1040.ATax)
    else:
        return get_currency(IA1040X.ARegTax)

def ABalance14_Calculation():
    return max_value(0, get_currency(IA1040X.ATotTax) - get_currency(IA1040X.ATotCr50))

def ABalance16_Calculation():
    return max_value(0, get_currency(IA1040X.ABalance14) - get_currency(IA1040X.ACrNon))

def ABalance18_Calculation():
    return max_value(0, get_currency(IA1040X.ABalance16) - get_currency(IA1040X.AOthIACr))

def ABalance7_Calculation():
    return get_currency(IA1040X.ATotInc) - get_currency(IA1040X.AFedDed)

def AContrib_Calculation():
    if get_bool(IA1040X.CombMFS) == True:
        return get_currency(IAF1040.TotContrib) - get_currency(IA1040X.BContrib)
    else:
        return get_currency(IAF1040.TotContrib)

def ACrNon_Calculation():
    return get_currency(IAF1040.ACrNon)

def Add_Calculation():
    return get_string(IAF1040.Add)

def ADedBox_Calculation():
    return get_currency(IAF1040.ADedBox)

def AdjRef_Calculation():
    return max_value(0, get_currency(IA1040X.CalcOP) - get_currency(IA1040X.TotCF))

def AFedDed_Calculation():
    return get_currency(IAF1040.AFedDed)

def AFedTax_Calculation():
    return get_currency(IAF1040.AFedTax)

def AGross_Calculation():
    return get_currency(IAF1040.AGross)

def ALumpMin_Calculation():
    return get_currency(IAF1040.ALump) + get_currency(IAF1040.AIAMin)

def ANet_Calculation():
    return get_currency(IAF1040.ANet)

def AOthIACr_Calculation():
    return get_currency(IAF1040.AOutState) + get_currency(IAF1040.AOthIACr)

def APenExcl_Calculation():
    return get_currency(IAF1040.APenExcl)

def ARegTax_Calculation():
    TotTaxInc = Currency()
    TotTaxInc = get_currency(IA1040X.ATaxInc)
    return Tax(TotTaxInc)

def ARepSSB_Calculation():
    return get_currency(IAF1040.ARepSSB)

def ASch_Calculation():
    return get_currency(IAF1040.ASch)

def ATaxInc_Calculation():
    return get_currency(IAF1040.ATaxInc)

def ATotAdj_Calculation():
    return get_currency(IAF1040.ATotAdj)

def ATotCr50_Calculation():
    return get_currency(IAF1040.ACredits)

def ATotInc_Calculation():
    return get_currency(IA1040X.ANet) + get_currency(IA1040X.AFedTax)

def ATotTax_Calculation():
    return get_currency(IA1040X.AAltTax) + get_currency(IA1040X.ALumpMin)

def ATotTax2_Calculation():
    return get_currency(IA1040X.ABalance18) + get_currency(IA1040X.ASch) + get_currency(IA1040X.AContrib)

def Balance27_Calculation():
    return max_value(0, get_currency(IA1040X.TotPay) - get_currency(IA1040X.PrevOP))

def BAltTax_Calculation():
    if IAFS() == 3:
        if ( get_currency(IAWKALTTAX.Mult) < get_currency(IA1040X.TotTaxSch) )  and get_bool(IAWKALTTAX.Qualify) == True:
            return get_currency(IAF1040.BTax)
        else:
            return get_currency(IA1040X.BRegTax)
    else:
        return 0

def BBalance14_Calculation():
    return max_value(0, get_currency(IA1040X.BTotTax) - get_currency(IA1040X.BTotCr50))

def BBalance16_Calculation():
    return max_value(0, get_currency(IA1040X.BBalance14) - get_currency(IA1040X.BCrNon))

def BBalance18_Calculation():
    return max_value(0, get_currency(IA1040X.BBalance16) - get_currency(IA1040X.BOthIACr))

def BBalance7_Calculation():
    return get_currency(IA1040X.BTotInc) - get_currency(IA1040X.BFedDed)

def BContrib_Calculation():
    if get_bool(IA1040X.CombMFS) == True:
        return c_dollar(get_float(IAF1040.TotContrib) * 0.5)
    else:
        return 0

def BCrNon_Calculation():
    return get_currency(IAF1040.BCrNon)

def BDedBox_Calculation():
    return get_currency(IAF1040.BDedBox)

def BFedDed_Calculation():
    return get_currency(IAF1040.BFedDed)

def BFedTax_Calculation():
    return get_currency(IAF1040.BFedTax)

def BGross_Calculation():
    return get_currency(IAF1040.BGross)

def BLumpMin_Calculation():
    return get_currency(IAF1040.BLump) + get_currency(IAF1040.BIAMin)

def BNet_Calculation():
    return get_currency(IAF1040.BNet)

def BOthIACr_Calculation():
    return get_currency(IAF1040.BOutState) + get_currency(IAF1040.BOthIACr)

def BPenExcl_Calculation():
    return get_currency(IAF1040.BPenExcl)

def BRegTax_Calculation():
    TotTaxInc = Currency()
    if get_bool(IAF1040.MFS) == True:
        TotTaxInc = get_currency(IAF1040.SpTaxInc)
    else:
        TotTaxInc = get_currency(IA1040X.BTaxInc)
    return Tax(TotTaxInc)

def BRepSSB_Calculation():
    return get_currency(IAF1040.BRepSSB)

def BSch_Calculation():
    return get_currency(IAF1040.BSch)

def BTaxInc_Calculation():
    return get_currency(IAF1040.BTaxInc)

def BTotAdj_Calculation():
    return get_currency(IAF1040.BTotAdj)

def BTotCr50_Calculation():
    return get_currency(IAF1040.BCredits)

def BTotInc_Calculation():
    return get_currency(IA1040X.BNet) + get_currency(IA1040X.BFedTax)

def BTotTax_Calculation():
    return get_currency(IA1040X.BAltTax) + get_currency(IA1040X.BLumpMin)

def BTotTax2_Calculation():
    return get_currency(IA1040X.BBalance18) + get_currency(IA1040X.BSch) + get_currency(IA1040X.BContrib)

def CalcOP_Calculation():
    PrevOP = Currency()
    PrevOP = max_value(0, get_currency(IA1040X.PrevOP) - get_currency(IA1040X.TotPay))
    return max_value(0, get_currency(IA1040X.Balance27) - get_currency(IA1040X.Total) - PrevOP)

def City_Calculation():
    return get_string(IAF1040.CityComb)

def CombMFS_Calculation():
    return get_bool(IAF1040.CombMFS)

def CountyNo_Calculation():
    return get_string(IAF1040.CountyNo)

def DC1_Calculation():
    return get_number(IAF1040.DC1)

def DC2_Calculation():
    return get_number(IAF1040.DC2)

def DepN_Calculation():
    return get_bool(IAF1040.DepN)

def DepNames_Calculation():
    return get_string(IAF1040.DepNames)

def DepY_Calculation():
    return get_bool(IAF1040.DepY)

def Desc_Calculation():
    return get_string(IAREQUIRED.CombNames)

def EFExplanation_Calculation():
    t = String()

    a = Integer()
    t = ''
    a = 0
    while a < 18:
        t = t + ' ' + get_string(IA1040X.Explanation(a))
        a = a + 1
    if get_bool(IA1040X.EFAmend) == True:
        return trim(t)
    else:
        return ''

def ExempA_Calculation():
    return get_currency(IAF1040.ExempA)

def ExempB_Calculation():
    return get_currency(IAF1040.ExempB)

def Exist_Calculation():
    return 1

def FirstName_Calculation():
    return get_string(IAF1040.FirstName)

def HOH_Calculation():
    return get_bool(IAF1040.HOH)

def HOHDep_Calculation():
    return get_string(IAF1040.HOHDep)

def HOHSSN_Calculation():
    return get_string(IAF1040.HOHSSN)

def Int_Calculation():
    return get_currency(IAF1040.Int74)

def ItemCheck_Calculation():
    return get_bool(IAF1040.ItemCheck)

def LastName_Calculation():
    return get_string(IAF1040.LastName)

def Lesser_Calculation():
    if IAFS() == 1:
        return get_currency(IA1040X.TotTaxSch)
    else:
        if get_bool(IAWKALTTAX.Qualify) == True:
            return min_value(get_currency(IAWKALTTAX.Mult), get_currency(IA1040X.TotTaxSch))
        else:
            return get_currency(IA1040X.TotTaxSch)

def MFJ_Calculation():
    return get_bool(IAF1040.MFJ)

def MFS_Calculation():
    return get_bool(IAF1040.MFS)

def MFSName_Calculation():
    return get_string(IAF1040.MFSName)

def MFSSSN_Calculation():
    return get_string(IAF1040.MFSSSN)

def Over65_Calculation():
    return get_bool(IAF1040.Over65)

def Owe_Calculation():
    PrevOP = Currency()
    PrevOP = max_value(0, get_currency(IA1040X.PrevOP) - get_currency(IA1040X.TotPay))
    return max_value(0, get_currency(IA1040X.Total) + PrevOP - get_currency(IA1040X.Balance27))

def PC1a_Calculation():
    return get_number(IAF1040.PC1a)

def PC1b_Calculation():
    return get_number(IAF1040.PC1b)

def PC2a_Calculation():
    return get_number(IAF1040.PC2a)

def PC2b_Calculation():
    return get_number(IAF1040.PC2b)

def Pen_Calculation():
    return get_currency(IAF1040.Pen74)

def PenInt_Calculation():
    if get_currency(IA1040X.Refund) > 0:
        return 0
    else:
        return get_currency(IA1040X.Pen) + get_currency(IA1040X.Int)

def Phone_Calculation():
    return get_string(IAF1040.Phone)

def PrepAdd_Calculation():
    return get_string(USWBasicInfo.PrepAdd)

def PrepCitySt_Calculation():
    return get_string(USWBasicInfo.CombPrepCityStZipFor)

def PrepFirm_Calculation():
    return get_string(USWBasicInfo.PrepName)

def PrepID_Calculation():
    return get_string(IAF1040.PrepID)

def PrepPhone_Calculation():
    return get_string(IAF1040.PrepPhone)

def QualWidow_Calculation():
    return get_bool(IAF1040.QualWidow)

def Refund_Calculation():
    PrevOP = Currency()
    PrevOP = max_value(0, get_currency(IA1040X.PrevOP) - get_currency(IA1040X.TotPay))
    if get_currency(IA1040X.TotCF) > 0:
        return get_currency(IA1040X.AdjRef)
    else:
        return max_value(0, get_currency(IA1040X.Balance27) - get_currency(IA1040X.Total) - PrevOP)

def SchNo_Calculation():
    return get_string(IAF1040.SchNo)

def Single_Calculation():
    return get_bool(IAF1040.Single)

def SpIncome_Calculation():
    return get_currency(IAF1040.SpIncome)

def SpouseFirst_Calculation():
    return get_string(IAF1040.SpouseFirst)

def SpouseLast_Calculation():
    return get_string(IAF1040.SpouseLast)

def SpouseSSN_Calculation():
    return get_string(IAF1040.SpouseSSN)

def SSN_Calculation():
    return get_string(IAF1040.SSN)

def StadCheck_Calculation():
    return get_bool(IAF1040.StadCheck)

def TaxYear_Calculation():
    TaxYear = Integer()
    TaxYear = YearNumber
    return CStr(TaxYear)

def Tot67_Calculation():
    if get_bool(IA1040X.EFAmend) == True:
        return get_currency(IAF1040.BTot67) + get_currency(IAF1040.ATot67) - get_currency(IA1040X.TotPrevTax)
    else:
        return get_currency(IAF1040.BTot67) + get_currency(IAF1040.ATot67)

def Total_Calculation():
    return get_currency(IA1040X.BTotTax2) + get_currency(IA1040X.ATotTax2)

def TotCF_Calculation():
    return get_currency(IA1040X.TPElectCF) + get_currency(IA1040X.SPElectCF)

def TotDC1_Calculation():
    return get_currency(IAF1040.TotDC1)

def TotDC2_Calculation():
    return get_currency(IAF1040.TotDC2)

def TotDue_Calculation():
    return get_currency(IA1040X.Owe) + get_currency(IA1040X.PenInt)

def TotPay_Calculation():
    return get_currency(IA1040X.Tot67) + get_currency(IA1040X.TotPrevTax)

def TotPC2a_Calculation():
    return get_currency(IAF1040.TotPC2a)

def TotPC2b_Calculation():
    return get_currency(IAF1040.TotPC2b)

def TotPCa_Calculation():
    return get_currency(IAF1040.TotPCa)

def TotPCb_Calculation():
    return get_currency(IAF1040.TotPCb)

def TotTaxSch_Calculation():
    return get_currency(IA1040X.ARegTax) + get_currency(IA1040X.BRegTax)


