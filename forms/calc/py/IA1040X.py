from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def AAltTax_Calculation():
    # 1st condition added for situation when MFS return and reporting spouse income causes an alternate tax calculation yet taxpayer has zero income
    # See saved return IA MFS Alternate Tax Issue.ta2
    if GetBool(IA1040X.MFS) == True and GetCurrency(IA1040X.ATaxInc) == 0:
        ReturnVal = 0
    elif  ( GetCurrency(IAWkAltTax.Mult) < GetCurrency(IA1040X.TotTaxSch) )  and GetBool(IAWkAltTax.Qualify) == True:
        ReturnVal = GetCurrency(IAF1040.ATax)
    else:
        ReturnVal = GetCurrency(IA1040X.ARegTax)

def ABalance14_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA1040X.ATotTax) - GetCurrency(IA1040X.ATotCr50))

def ABalance16_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA1040X.ABalance14) - GetCurrency(IA1040X.ACrNon))

def ABalance18_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA1040X.ABalance16) - GetCurrency(IA1040X.AOthIACr))

def ABalance7_Calculation():
    ReturnVal = GetCurrency(IA1040X.ATotInc) - GetCurrency(IA1040X.AFedDed)

def AContrib_Calculation():
    if GetBool(IA1040X.CombMFS) == True:
        ReturnVal = GetCurrency(IAF1040.TotContrib) - GetCurrency(IA1040X.BContrib)
    else:
        ReturnVal = GetCurrency(IAF1040.TotContrib)

def ACrNon_Calculation():
    ReturnVal = GetCurrency(IAF1040.ACrNon)

def Add_Calculation():
    ReturnVal = GetString(IAF1040.Add)

def ADedBox_Calculation():
    ReturnVal = GetCurrency(IAF1040.ADedBox)

def AdjRef_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA1040X.CalcOP) - GetCurrency(IA1040X.TotCF))

def AFedDed_Calculation():
    ReturnVal = GetCurrency(IAF1040.AFedDed)

def AFedTax_Calculation():
    ReturnVal = GetCurrency(IAF1040.AFedTax)

def AGross_Calculation():
    ReturnVal = GetCurrency(IAF1040.AGross)

def ALumpMin_Calculation():
    ReturnVal = GetCurrency(IAF1040.ALump) + GetCurrency(IAF1040.AIAMin)

def ANet_Calculation():
    ReturnVal = GetCurrency(IAF1040.ANet)

def AOthIACr_Calculation():
    ReturnVal = GetCurrency(IAF1040.AOutState) + GetCurrency(IAF1040.AOthIACr)

def APenExcl_Calculation():
    ReturnVal = GetCurrency(IAF1040.APenExcl)

def ARegTax_Calculation():
    TotTaxInc = Currency()
    TotTaxInc = GetCurrency(IA1040X.ATaxInc)
    ReturnVal = Tax(TotTaxInc)

def ARepSSB_Calculation():
    ReturnVal = GetCurrency(IAF1040.ARepSSB)

def ASch_Calculation():
    ReturnVal = GetCurrency(IAF1040.ASch)

def ATaxInc_Calculation():
    ReturnVal = GetCurrency(IAF1040.ATaxInc)

def ATotAdj_Calculation():
    ReturnVal = GetCurrency(IAF1040.ATotAdj)

def ATotCr50_Calculation():
    ReturnVal = GetCurrency(IAF1040.ACredits)

def ATotInc_Calculation():
    ReturnVal = GetCurrency(IA1040X.ANet) + GetCurrency(IA1040X.AFedTax)

def ATotTax_Calculation():
    ReturnVal = GetCurrency(IA1040X.AAltTax) + GetCurrency(IA1040X.ALumpMin)

def ATotTax2_Calculation():
    ReturnVal = GetCurrency(IA1040X.ABalance18) + GetCurrency(IA1040X.ASch) + GetCurrency(IA1040X.AContrib)

def Balance27_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA1040X.TotPay) - GetCurrency(IA1040X.PrevOP))

def BAltTax_Calculation():
    if IAFS() == 3:
        if ( GetCurrency(IAWkAltTax.Mult) < GetCurrency(IA1040X.TotTaxSch) )  and GetBool(IAWkAltTax.Qualify) == True:
            ReturnVal = GetCurrency(IAF1040.BTax)
        else:
            ReturnVal = GetCurrency(IA1040X.BRegTax)
    else:
        ReturnVal = 0

def BBalance14_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA1040X.BTotTax) - GetCurrency(IA1040X.BTotCr50))

def BBalance16_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA1040X.BBalance14) - GetCurrency(IA1040X.BCrNon))

def BBalance18_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA1040X.BBalance16) - GetCurrency(IA1040X.BOthIACr))

def BBalance7_Calculation():
    ReturnVal = GetCurrency(IA1040X.BTotInc) - GetCurrency(IA1040X.BFedDed)

def BContrib_Calculation():
    if GetBool(IA1040X.CombMFS) == True:
        ReturnVal = CDollar(GetFloat(IAF1040.TotContrib) * 0.5)
    else:
        ReturnVal = 0

def BCrNon_Calculation():
    ReturnVal = GetCurrency(IAF1040.BCrNon)

def BDedBox_Calculation():
    ReturnVal = GetCurrency(IAF1040.BDedBox)

def BFedDed_Calculation():
    ReturnVal = GetCurrency(IAF1040.BFedDed)

def BFedTax_Calculation():
    ReturnVal = GetCurrency(IAF1040.BFedTax)

def BGross_Calculation():
    ReturnVal = GetCurrency(IAF1040.BGross)

def BLumpMin_Calculation():
    ReturnVal = GetCurrency(IAF1040.BLump) + GetCurrency(IAF1040.BIAMin)

def BNet_Calculation():
    ReturnVal = GetCurrency(IAF1040.BNet)

def BOthIACr_Calculation():
    ReturnVal = GetCurrency(IAF1040.BOutState) + GetCurrency(IAF1040.BOthIACr)

def BPenExcl_Calculation():
    ReturnVal = GetCurrency(IAF1040.BPenExcl)

def BRegTax_Calculation():
    TotTaxInc = Currency()
    if GetBool(IAF1040.MFS) == True:
        TotTaxInc = GetCurrency(IAF1040.SpTaxInc)
    else:
        TotTaxInc = GetCurrency(IA1040X.BTaxInc)
    ReturnVal = Tax(TotTaxInc)

def BRepSSB_Calculation():
    ReturnVal = GetCurrency(IAF1040.BRepSSB)

def BSch_Calculation():
    ReturnVal = GetCurrency(IAF1040.BSch)

def BTaxInc_Calculation():
    ReturnVal = GetCurrency(IAF1040.BTaxInc)

def BTotAdj_Calculation():
    ReturnVal = GetCurrency(IAF1040.BTotAdj)

def BTotCr50_Calculation():
    ReturnVal = GetCurrency(IAF1040.BCredits)

def BTotInc_Calculation():
    ReturnVal = GetCurrency(IA1040X.BNet) + GetCurrency(IA1040X.BFedTax)

def BTotTax_Calculation():
    ReturnVal = GetCurrency(IA1040X.BAltTax) + GetCurrency(IA1040X.BLumpMin)

def BTotTax2_Calculation():
    ReturnVal = GetCurrency(IA1040X.BBalance18) + GetCurrency(IA1040X.BSch) + GetCurrency(IA1040X.BContrib)

def CalcOP_Calculation():
    PrevOP = Currency()
    PrevOP = MaxValue(0, GetCurrency(IA1040X.PrevOP) - GetCurrency(IA1040X.TotPay))
    ReturnVal = MaxValue(0, GetCurrency(IA1040X.Balance27) - GetCurrency(IA1040X.Total) - PrevOP)

def City_Calculation():
    ReturnVal = GetString(IAF1040.CityComb)

def CombMFS_Calculation():
    ReturnVal = GetBool(IAF1040.CombMFS)

def CountyNo_Calculation():
    ReturnVal = GetString(IAF1040.CountyNo)

def DC1_Calculation():
    ReturnVal = GetNumber(IAF1040.DC1)

def DC2_Calculation():
    ReturnVal = GetNumber(IAF1040.DC2)

def DepN_Calculation():
    ReturnVal = GetBool(IAF1040.DepN)

def DepNames_Calculation():
    ReturnVal = GetString(IAF1040.DepNames)

def DepY_Calculation():
    ReturnVal = GetBool(IAF1040.DepY)

def Desc_Calculation():
    ReturnVal = GetString(IARequired.CombNames)

def EFExplanation_Calculation():
    t = String()

    a = Integer()
    t = ''
    a = 0
    while a < 18:
        t = t + ' ' + GetString(IA1040X.Explanation(a))
        a = a + 1
    if GetBool(IA1040X.EFAmend) == True:
        ReturnVal = Trim(t)
    else:
        ReturnVal = ''

def ExempA_Calculation():
    ReturnVal = GetCurrency(IAF1040.ExempA)

def ExempB_Calculation():
    ReturnVal = GetCurrency(IAF1040.ExempB)

def Exist_Calculation():
    ReturnVal = 1

def FirstName_Calculation():
    ReturnVal = GetString(IAF1040.FirstName)

def HOH_Calculation():
    ReturnVal = GetBool(IAF1040.HOH)

def HOHDep_Calculation():
    ReturnVal = GetString(IAF1040.HOHDep)

def HOHSSN_Calculation():
    ReturnVal = GetString(IAF1040.HOHSSN)

def Int_Calculation():
    ReturnVal = GetCurrency(IAF1040.Int74)

def ItemCheck_Calculation():
    ReturnVal = GetBool(IAF1040.ItemCheck)

def LastName_Calculation():
    ReturnVal = GetString(IAF1040.LastName)

def Lesser_Calculation():
    if IAFS() == 1:
        ReturnVal = GetCurrency(IA1040X.TotTaxSch)
    else:
        if GetBool(IAWkAltTax.Qualify) == True:
            ReturnVal = MinValue(GetCurrency(IAWkAltTax.Mult), GetCurrency(IA1040X.TotTaxSch))
        else:
            ReturnVal = GetCurrency(IA1040X.TotTaxSch)

def MFJ_Calculation():
    ReturnVal = GetBool(IAF1040.MFJ)

def MFS_Calculation():
    ReturnVal = GetBool(IAF1040.MFS)

def MFSName_Calculation():
    ReturnVal = GetString(IAF1040.MFSName)

def MFSSSN_Calculation():
    ReturnVal = GetString(IAF1040.MFSSSN)

def Over65_Calculation():
    ReturnVal = GetBool(IAF1040.Over65)

def Owe_Calculation():
    PrevOP = Currency()
    PrevOP = MaxValue(0, GetCurrency(IA1040X.PrevOP) - GetCurrency(IA1040X.TotPay))
    ReturnVal = MaxValue(0, GetCurrency(IA1040X.Total) + PrevOP - GetCurrency(IA1040X.Balance27))

def PC1a_Calculation():
    ReturnVal = GetNumber(IAF1040.PC1a)

def PC1b_Calculation():
    ReturnVal = GetNumber(IAF1040.PC1b)

def PC2a_Calculation():
    ReturnVal = GetNumber(IAF1040.PC2a)

def PC2b_Calculation():
    ReturnVal = GetNumber(IAF1040.PC2b)

def Pen_Calculation():
    ReturnVal = GetCurrency(IAF1040.Pen74)

def PenInt_Calculation():
    if GetCurrency(IA1040X.Refund) > 0:
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(IA1040X.Pen) + GetCurrency(IA1040X.Int)

def Phone_Calculation():
    ReturnVal = GetString(IAF1040.Phone)

def PrepAdd_Calculation():
    ReturnVal = GetString(USWBasicInfo.PrepAdd)

def PrepCitySt_Calculation():
    ReturnVal = GetString(USWBasicInfo.CombPrepCityStZipFor)

def PrepFirm_Calculation():
    ReturnVal = GetString(USWBasicInfo.PrepName)

def PrepID_Calculation():
    ReturnVal = GetString(IAF1040.PrepID)

def PrepPhone_Calculation():
    ReturnVal = GetString(IAF1040.PrepPhone)

def QualWidow_Calculation():
    ReturnVal = GetBool(IAF1040.QualWidow)

def Refund_Calculation():
    PrevOP = Currency()
    PrevOP = MaxValue(0, GetCurrency(IA1040X.PrevOP) - GetCurrency(IA1040X.TotPay))
    if GetCurrency(IA1040X.TotCF) > 0:
        ReturnVal = GetCurrency(IA1040X.AdjRef)
    else:
        ReturnVal = MaxValue(0, GetCurrency(IA1040X.Balance27) - GetCurrency(IA1040X.Total) - PrevOP)

def SchNo_Calculation():
    ReturnVal = GetString(IAF1040.SchNo)

def Single_Calculation():
    ReturnVal = GetBool(IAF1040.Single)

def SpIncome_Calculation():
    ReturnVal = GetCurrency(IAF1040.SpIncome)

def SpouseFirst_Calculation():
    ReturnVal = GetString(IAF1040.SpouseFirst)

def SpouseLast_Calculation():
    ReturnVal = GetString(IAF1040.SpouseLast)

def SpouseSSN_Calculation():
    ReturnVal = GetString(IAF1040.SpouseSSN)

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

def StadCheck_Calculation():
    ReturnVal = GetBool(IAF1040.StadCheck)

def TaxYear_Calculation():
    TaxYear = Integer()
    TaxYear = YearNumber
    ReturnVal = CStr(TaxYear)

def Tot67_Calculation():
    if GetBool(IA1040X.EFAmend) == True:
        ReturnVal = GetCurrency(IAF1040.BTot67) + GetCurrency(IAF1040.ATot67) - GetCurrency(IA1040X.TotPrevTax)
    else:
        ReturnVal = GetCurrency(IAF1040.BTot67) + GetCurrency(IAF1040.ATot67)

def Total_Calculation():
    ReturnVal = GetCurrency(IA1040X.BTotTax2) + GetCurrency(IA1040X.ATotTax2)

def TotCF_Calculation():
    ReturnVal = GetCurrency(IA1040X.TPElectCF) + GetCurrency(IA1040X.SPElectCF)

def TotDC1_Calculation():
    ReturnVal = GetCurrency(IAF1040.TotDC1)

def TotDC2_Calculation():
    ReturnVal = GetCurrency(IAF1040.TotDC2)

def TotDue_Calculation():
    ReturnVal = GetCurrency(IA1040X.Owe) + GetCurrency(IA1040X.PenInt)

def TotPay_Calculation():
    ReturnVal = GetCurrency(IA1040X.Tot67) + GetCurrency(IA1040X.TotPrevTax)

def TotPC2a_Calculation():
    ReturnVal = GetCurrency(IAF1040.TotPC2a)

def TotPC2b_Calculation():
    ReturnVal = GetCurrency(IAF1040.TotPC2b)

def TotPCa_Calculation():
    ReturnVal = GetCurrency(IAF1040.TotPCa)

def TotPCb_Calculation():
    ReturnVal = GetCurrency(IAF1040.TotPCb)

def TotTaxSch_Calculation():
    ReturnVal = GetCurrency(IA1040X.ARegTax) + GetCurrency(IA1040X.BRegTax)

