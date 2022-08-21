from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Description_Calculation():
    ReturnVal = 'Nonconformity Adjustment ' + CStr(GetCurrency(IAWNonConformAdj.PrTotNonConformAdj))

def EOYDate_Calculation():
    ReturnVal = MakeDate(12, 31, YearNumber)

def PrAlaskaNativeCorp_Calculation():
    ReturnVal = GetCurrency(IAWNonConformAdj.SPAlaskaNativeCorp) + GetCurrency(IAWNonConformAdj.TPAlaskaNativeCorp)

def PrBasisLifeIns_Calculation():
    ReturnVal = GetCurrency(IAWNonConformAdj.SPBasisLifeIns) + GetCurrency(IAWNonConformAdj.TPBasisLifeIns)

def PrBasisLimitPartLoss_Calculation():
    ReturnVal = GetCurrency(IAWNonConformAdj.SPBasisLimitPartLoss) + GetCurrency(IAWNonConformAdj.TPBasisLimitPartLoss)

def PrBuiltInLosses_Calculation():
    ReturnVal = GetCurrency(IAWNonConformAdj.SPBuiltInLosses) + GetCurrency(IAWNonConformAdj.TPBuiltInLosses)

def PrBusInterestLimit_Calculation():
    ReturnVal = GetCurrency(IAWNonConformAdj.SPBusInterestLimit) + GetCurrency(IAWNonConformAdj.TPBusInterestLimit)

def PrCapContr_Calculation():
    ReturnVal = GetCurrency(IAWNonConformAdj.SPCapContr) + GetCurrency(IAWNonConformAdj.TPCapContr)

def PrCapRules_Calculation():
    ReturnVal = GetCurrency(IAWNonConformAdj.SPCapRules) + GetCurrency(IAWNonConformAdj.TPCapRules)

def PrCertCapAssets_Calculation():
    ReturnVal = GetCurrency(IAWNonConformAdj.SPCertCapAssets) + GetCurrency(IAWNonConformAdj.TPCertCapAssets)

def PrCertSettlement_Calculation():
    ReturnVal = GetCurrency(IAWNonConformAdj.SPCertSettlement) + GetCurrency(IAWNonConformAdj.TPCertSettlement)

def PrCharContLimit_Calculation():
    ReturnVal = GetCurrency(IAWNonConformAdj.SPCharContLimit) + GetCurrency(IAWNonConformAdj.TPCharContLimit)

def PrDomProd_Calculation():
    ReturnVal = GetCurrency(IAWNonConformAdj.SPDomProd) + GetCurrency(IAWNonConformAdj.TPDomProd)

def PrExcessBusLossLimit_Calculation():
    ReturnVal = GetCurrency(IAWNonConformAdj.SPExcessBusLossLimit) + GetCurrency(IAWNonConformAdj.TPExcessBusLossLimit)

def PrExcessiveRemun_Calculation():
    ReturnVal = GetCurrency(IAWNonConformAdj.SPExcessiveRemun) + GetCurrency(IAWNonConformAdj.TPExcessiveRemun)

def PrFDICPrem_Calculation():
    ReturnVal = GetCurrency(IAWNonConformAdj.SPFDICPrem) + GetCurrency(IAWNonConformAdj.TPFDICPrem)

def PrForSourceDiv_Calculation():
    ReturnVal = GetCurrency(IAWNonConformAdj.SPForSourceDiv) + GetCurrency(IAWNonConformAdj.TPForSourceDiv)

def PrGlobalLowTI_Calculation():
    ReturnVal = GetCurrency(IAWNonConformAdj.SPGlobalLowTI) + GetCurrency(IAWNonConformAdj.TPGlobalLowTI)

def PrInventorySales_Calculation():
    ReturnVal = GetCurrency(IAWNonConformAdj.SPInventorySales) + GetCurrency(IAWNonConformAdj.TPInventorySales)

def PrIRC965Repat_Calculation():
    ReturnVal = GetCurrency(IAWNonConformAdj.SPIRC965Repat) + GetCurrency(IAWNonConformAdj.TPIRC965Repat)

def PrLikeKind_Calculation():
    ReturnVal = GetCurrency(IAWNonConformAdj.SPLikeKind) + GetCurrency(IAWNonConformAdj.TPLikeKind)

def PrOthBusDed_Calculation():
    ReturnVal = GetCurrency(IAWNonConformAdj.SPOthBusDed) + GetCurrency(IAWNonConformAdj.TPOthBusDed)

def PrOtherAdj_Calculation():
    ReturnVal = GetCurrency(IAWNonConformAdj.SPOtherAdj) + GetCurrency(IAWNonConformAdj.TPOtherAdj)

def PrOwnedForCorp_Calculation():
    ReturnVal = GetCurrency(IAWNonConformAdj.SPOwnedForCorp) + GetCurrency(IAWNonConformAdj.TPOwnedForCorp)

def PrQualEquityGrants_Calculation():
    ReturnVal = GetCurrency(IAWNonConformAdj.SPQualEquityGrants) + GetCurrency(IAWNonConformAdj.TPQualEquityGrants)

def PrQualOppZone_Calculation():
    ReturnVal = GetCurrency(IAWNonConformAdj.SPQualOppZone) + GetCurrency(IAWNonConformAdj.TPQualOppZone)

def PrRelParHybridTrans_Calculation():
    ReturnVal = GetCurrency(IAWNonConformAdj.SPRelParHybridTrans) + GetCurrency(IAWNonConformAdj.TPRelParHybridTrans)

def PrSCorpCharCont_Calculation():
    ReturnVal = GetCurrency(IAWNonConformAdj.SPSCorpCharCont) + GetCurrency(IAWNonConformAdj.TPSCorpCharCont)

def PrSec199CoopDed_Calculation():
    ReturnVal = GetCurrency(IAWNonConformAdj.SPSec199CoopDed) + GetCurrency(IAWNonConformAdj.TPSec199CoopDed)

def PrSec199QBIDed_Calculation():
    ReturnVal = GetCurrency(IAWNonConformAdj.SPSec199QBIDed) + GetCurrency(IAWNonConformAdj.TPSec199QBIDed)

def PrSubPartF_Calculation():
    ReturnVal = GetCurrency(IAWNonConformAdj.SPSubPartF) + GetCurrency(IAWNonConformAdj.TPSubPartF)

def PrTotNonConformAdj_Calculation():
    ReturnVal = GetCurrency(IAWNonConformAdj.SPTotNonConformAdj) + GetCurrency(IAWNonConformAdj.TPTotNonConformAdj)

def PrTransferValueLifeIns_Calculation():
    ReturnVal = GetCurrency(IAWNonConformAdj.SPTransferValueLifeIns) + GetCurrency(IAWNonConformAdj.TPTransferValueLifeIns)

def SPExcessBusLossLimit_Calculation():
    ReturnVal = 0

def SPLikeKind_Calculation():
    ReturnVal = 0

def SPName_Calculation():
    ReturnVal = GetString(USWBasicInfo.SPCommon)

def SPQualEquityGrants_Calculation():
    ReturnVal = Round(GetCurrency(USDW2.CodeHH, FieldCopies(USDW2.Spouse)))

def SPTotNonConformAdj_Calculation():
    Tot1to10 = Currency()

    Tot11to20 = Currency()

    Tot21to30 = Currency()
    Tot1to10 = GetCurrency(IAWNonConformAdj.SPCapContr) + GetCurrency(IAWNonConformAdj.SPLikeKind) + GetCurrency(IAWNonConformAdj.SPBusInterestLimit) + GetCurrency(IAWNonConformAdj.SPExcessiveRemun) + GetCurrency(IAWNonConformAdj.SPCertSettlement) + GetCurrency(IAWNonConformAdj.SPFDICPrem) + GetCurrency(IAWNonConformAdj.SPDomProd) + GetCurrency(IAWNonConformAdj.SPSec199QBIDed) + GetCurrency(IAWNonConformAdj.SPSec199CoopDed) + GetCurrency(IAWNonConformAdj.SPOthBusDed)
    Tot11to20 = GetCurrency(IAWNonConformAdj.SPCharContLimit) + GetCurrency(IAWNonConformAdj.SPSCorpCharCont) + GetCurrency(IAWNonConformAdj.SPExcessBusLossLimit) + GetCurrency(IAWNonConformAdj.SPQualEquityGrants) + GetCurrency(IAWNonConformAdj.SPCapRules) + GetCurrency(IAWNonConformAdj.SPCertCapAssets) + GetCurrency(IAWNonConformAdj.SPQualOppZone) + GetCurrency(IAWNonConformAdj.SPBuiltInLosses) + GetCurrency(IAWNonConformAdj.SPBasisLimitPartLoss) + GetCurrency(IAWNonConformAdj.SPBasisLifeIns)
    Tot21to30 = GetCurrency(IAWNonConformAdj.SPTransferValueLifeIns) + GetCurrency(IAWNonConformAdj.SPAlaskaNativeCorp) + GetCurrency(IAWNonConformAdj.SPGlobalLowTI) + GetCurrency(IAWNonConformAdj.SPRelParHybridTrans) + GetCurrency(IAWNonConformAdj.SPInventorySales) + GetCurrency(IAWNonConformAdj.SPOwnedForCorp) + GetCurrency(IAWNonConformAdj.SPSubPartF) + GetCurrency(IAWNonConformAdj.SPForSourceDiv) + GetCurrency(IAWNonConformAdj.SPIRC965Repat) + GetCurrency(IAWNonConformAdj.SPOtherAdj)
    ReturnVal = Tot1to10 + Tot11to20 + Tot21to30

def TPExcessBusLossLimit_Calculation():
    ReturnVal = 0

def Exist_Calculation():
    ReturnVal = 1

def TPLikeKind_Calculation():
    ReturnVal = 0

def Names_Calculation():
    ReturnVal = GetString(USWBasicInfo.CombNames)

def PrintMe_Calculation():
    if GetCurrency(IAWNonConformAdj.SPTotNonConformAdj) != 0 or GetCurrency(IAWNonConformAdj.TPTotNonConformAdj) != 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def TPName_Calculation():
    ReturnVal = GetString(USWBasicInfo.TPCommon)

def TPQualEquityGrants_Calculation():
    ReturnVal = Round(GetCurrency(USDW2.CodeHH, FieldCopies(USDW2.Taxpayer)))

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

def TPTotNonConformAdj_Calculation():
    Tot1to10 = Currency()

    Tot11to20 = Currency()

    Tot21to30 = Currency()
    Tot1to10 = GetCurrency(IAWNonConformAdj.TPCapContr) + GetCurrency(IAWNonConformAdj.TPLikeKind) + GetCurrency(IAWNonConformAdj.TPBusInterestLimit) + GetCurrency(IAWNonConformAdj.TPExcessiveRemun) + GetCurrency(IAWNonConformAdj.TPCertSettlement) + GetCurrency(IAWNonConformAdj.TPFDICPrem) + GetCurrency(IAWNonConformAdj.TPDomProd) + GetCurrency(IAWNonConformAdj.TPSec199QBIDed) + GetCurrency(IAWNonConformAdj.TPSec199CoopDed) + GetCurrency(IAWNonConformAdj.TPOthBusDed)
    Tot11to20 = GetCurrency(IAWNonConformAdj.TPCharContLimit) + GetCurrency(IAWNonConformAdj.TPSCorpCharCont) + GetCurrency(IAWNonConformAdj.TPExcessBusLossLimit) + GetCurrency(IAWNonConformAdj.TPQualEquityGrants) + GetCurrency(IAWNonConformAdj.TPCapRules) + GetCurrency(IAWNonConformAdj.TPCertCapAssets) + GetCurrency(IAWNonConformAdj.TPQualOppZone) + GetCurrency(IAWNonConformAdj.TPBuiltInLosses) + GetCurrency(IAWNonConformAdj.TPBasisLimitPartLoss) + GetCurrency(IAWNonConformAdj.TPBasisLifeIns)
    Tot21to30 = GetCurrency(IAWNonConformAdj.TPTransferValueLifeIns) + GetCurrency(IAWNonConformAdj.TPAlaskaNativeCorp) + GetCurrency(IAWNonConformAdj.TPGlobalLowTI) + GetCurrency(IAWNonConformAdj.TPRelParHybridTrans) + GetCurrency(IAWNonConformAdj.TPInventorySales) + GetCurrency(IAWNonConformAdj.TPOwnedForCorp) + GetCurrency(IAWNonConformAdj.TPSubPartF) + GetCurrency(IAWNonConformAdj.TPForSourceDiv) + GetCurrency(IAWNonConformAdj.TPIRC965Repat) + GetCurrency(IAWNonConformAdj.TPOtherAdj)
    ReturnVal = Tot1to10 + Tot11to20 + Tot21to30

