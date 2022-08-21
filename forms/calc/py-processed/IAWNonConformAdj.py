from forms.out import IAF1040
from forms.out import IAWNONCONFORMADJ
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Description_Calculation():
    return 'Nonconformity Adjustment ' + CStr(get_currency(IAWNONCONFORMADJ.PrTotNonConformAdj))

def EOYDate_Calculation():
    return MakeDate(12, 31, YearNumber)

def PrAlaskaNativeCorp_Calculation():
    return get_currency(IAWNONCONFORMADJ.SPAlaskaNativeCorp) + get_currency(IAWNONCONFORMADJ.TPAlaskaNativeCorp)

def PrBasisLifeIns_Calculation():
    return get_currency(IAWNONCONFORMADJ.SPBasisLifeIns) + get_currency(IAWNONCONFORMADJ.TPBasisLifeIns)

def PrBasisLimitPartLoss_Calculation():
    return get_currency(IAWNONCONFORMADJ.SPBasisLimitPartLoss) + get_currency(IAWNONCONFORMADJ.TPBasisLimitPartLoss)

def PrBuiltInLosses_Calculation():
    return get_currency(IAWNONCONFORMADJ.SPBuiltInLosses) + get_currency(IAWNONCONFORMADJ.TPBuiltInLosses)

def PrBusInterestLimit_Calculation():
    return get_currency(IAWNONCONFORMADJ.SPBusInterestLimit) + get_currency(IAWNONCONFORMADJ.TPBusInterestLimit)

def PrCapContr_Calculation():
    return get_currency(IAWNONCONFORMADJ.SPCapContr) + get_currency(IAWNONCONFORMADJ.TPCapContr)

def PrCapRules_Calculation():
    return get_currency(IAWNONCONFORMADJ.SPCapRules) + get_currency(IAWNONCONFORMADJ.TPCapRules)

def PrCertCapAssets_Calculation():
    return get_currency(IAWNONCONFORMADJ.SPCertCapAssets) + get_currency(IAWNONCONFORMADJ.TPCertCapAssets)

def PrCertSettlement_Calculation():
    return get_currency(IAWNONCONFORMADJ.SPCertSettlement) + get_currency(IAWNONCONFORMADJ.TPCertSettlement)

def PrCharContLimit_Calculation():
    return get_currency(IAWNONCONFORMADJ.SPCharContLimit) + get_currency(IAWNONCONFORMADJ.TPCharContLimit)

def PrDomProd_Calculation():
    return get_currency(IAWNONCONFORMADJ.SPDomProd) + get_currency(IAWNONCONFORMADJ.TPDomProd)

def PrExcessBusLossLimit_Calculation():
    return get_currency(IAWNONCONFORMADJ.SPExcessBusLossLimit) + get_currency(IAWNONCONFORMADJ.TPExcessBusLossLimit)

def PrExcessiveRemun_Calculation():
    return get_currency(IAWNONCONFORMADJ.SPExcessiveRemun) + get_currency(IAWNONCONFORMADJ.TPExcessiveRemun)

def PrFDICPrem_Calculation():
    return get_currency(IAWNONCONFORMADJ.SPFDICPrem) + get_currency(IAWNONCONFORMADJ.TPFDICPrem)

def PrForSourceDiv_Calculation():
    return get_currency(IAWNONCONFORMADJ.SPForSourceDiv) + get_currency(IAWNONCONFORMADJ.TPForSourceDiv)

def PrGlobalLowTI_Calculation():
    return get_currency(IAWNONCONFORMADJ.SPGlobalLowTI) + get_currency(IAWNONCONFORMADJ.TPGlobalLowTI)

def PrInventorySales_Calculation():
    return get_currency(IAWNONCONFORMADJ.SPInventorySales) + get_currency(IAWNONCONFORMADJ.TPInventorySales)

def PrIRC965Repat_Calculation():
    return get_currency(IAWNONCONFORMADJ.SPIRC965Repat) + get_currency(IAWNONCONFORMADJ.TPIRC965Repat)

def PrLikeKind_Calculation():
    return get_currency(IAWNONCONFORMADJ.SPLikeKind) + get_currency(IAWNONCONFORMADJ.TPLikeKind)

def PrOthBusDed_Calculation():
    return get_currency(IAWNONCONFORMADJ.SPOthBusDed) + get_currency(IAWNONCONFORMADJ.TPOthBusDed)

def PrOtherAdj_Calculation():
    return get_currency(IAWNONCONFORMADJ.SPOtherAdj) + get_currency(IAWNONCONFORMADJ.TPOtherAdj)

def PrOwnedForCorp_Calculation():
    return get_currency(IAWNONCONFORMADJ.SPOwnedForCorp) + get_currency(IAWNONCONFORMADJ.TPOwnedForCorp)

def PrQualEquityGrants_Calculation():
    return get_currency(IAWNONCONFORMADJ.SPQualEquityGrants) + get_currency(IAWNONCONFORMADJ.TPQualEquityGrants)

def PrQualOppZone_Calculation():
    return get_currency(IAWNONCONFORMADJ.SPQualOppZone) + get_currency(IAWNONCONFORMADJ.TPQualOppZone)

def PrRelParHybridTrans_Calculation():
    return get_currency(IAWNONCONFORMADJ.SPRelParHybridTrans) + get_currency(IAWNONCONFORMADJ.TPRelParHybridTrans)

def PrSCorpCharCont_Calculation():
    return get_currency(IAWNONCONFORMADJ.SPSCorpCharCont) + get_currency(IAWNONCONFORMADJ.TPSCorpCharCont)

def PrSec199CoopDed_Calculation():
    return get_currency(IAWNONCONFORMADJ.SPSec199CoopDed) + get_currency(IAWNONCONFORMADJ.TPSec199CoopDed)

def PrSec199QBIDed_Calculation():
    return get_currency(IAWNONCONFORMADJ.SPSec199QBIDed) + get_currency(IAWNONCONFORMADJ.TPSec199QBIDed)

def PrSubPartF_Calculation():
    return get_currency(IAWNONCONFORMADJ.SPSubPartF) + get_currency(IAWNONCONFORMADJ.TPSubPartF)

def PrTotNonConformAdj_Calculation():
    return get_currency(IAWNONCONFORMADJ.SPTotNonConformAdj) + get_currency(IAWNONCONFORMADJ.TPTotNonConformAdj)

def PrTransferValueLifeIns_Calculation():
    return get_currency(IAWNONCONFORMADJ.SPTransferValueLifeIns) + get_currency(IAWNONCONFORMADJ.TPTransferValueLifeIns)

def SPExcessBusLossLimit_Calculation():
    return 0

def SPLikeKind_Calculation():
    return 0

def SPName_Calculation():
    return get_string(USWBasicInfo.SPCommon)

def SPQualEquityGrants_Calculation():
    return Round(get_currency(USDW2.CodeHH, FieldCopies(USDW2.Spouse)))

def SPTotNonConformAdj_Calculation():
    Tot1to10 = Currency()

    Tot11to20 = Currency()

    Tot21to30 = Currency()
    Tot1to10 = get_currency(IAWNONCONFORMADJ.SPCapContr) + get_currency(IAWNONCONFORMADJ.SPLikeKind) + get_currency(IAWNONCONFORMADJ.SPBusInterestLimit) + get_currency(IAWNONCONFORMADJ.SPExcessiveRemun) + get_currency(IAWNONCONFORMADJ.SPCertSettlement) + get_currency(IAWNONCONFORMADJ.SPFDICPrem) + get_currency(IAWNONCONFORMADJ.SPDomProd) + get_currency(IAWNONCONFORMADJ.SPSec199QBIDed) + get_currency(IAWNONCONFORMADJ.SPSec199CoopDed) + get_currency(IAWNONCONFORMADJ.SPOthBusDed)
    Tot11to20 = get_currency(IAWNONCONFORMADJ.SPCharContLimit) + get_currency(IAWNONCONFORMADJ.SPSCorpCharCont) + get_currency(IAWNONCONFORMADJ.SPExcessBusLossLimit) + get_currency(IAWNONCONFORMADJ.SPQualEquityGrants) + get_currency(IAWNONCONFORMADJ.SPCapRules) + get_currency(IAWNONCONFORMADJ.SPCertCapAssets) + get_currency(IAWNONCONFORMADJ.SPQualOppZone) + get_currency(IAWNONCONFORMADJ.SPBuiltInLosses) + get_currency(IAWNONCONFORMADJ.SPBasisLimitPartLoss) + get_currency(IAWNONCONFORMADJ.SPBasisLifeIns)
    Tot21to30 = get_currency(IAWNONCONFORMADJ.SPTransferValueLifeIns) + get_currency(IAWNONCONFORMADJ.SPAlaskaNativeCorp) + get_currency(IAWNONCONFORMADJ.SPGlobalLowTI) + get_currency(IAWNONCONFORMADJ.SPRelParHybridTrans) + get_currency(IAWNONCONFORMADJ.SPInventorySales) + get_currency(IAWNONCONFORMADJ.SPOwnedForCorp) + get_currency(IAWNONCONFORMADJ.SPSubPartF) + get_currency(IAWNONCONFORMADJ.SPForSourceDiv) + get_currency(IAWNONCONFORMADJ.SPIRC965Repat) + get_currency(IAWNONCONFORMADJ.SPOtherAdj)
    return Tot1to10 + Tot11to20 + Tot21to30

def TPExcessBusLossLimit_Calculation():
    return 0

def Exist_Calculation():
    return 1

def TPLikeKind_Calculation():
    return 0

def Names_Calculation():
    return get_string(USWBasicInfo.CombNames)

def PrintMe_Calculation():
    if get_currency(IAWNONCONFORMADJ.SPTotNonConformAdj) != 0 or get_currency(IAWNONCONFORMADJ.TPTotNonConformAdj) != 0:
        return 1
    else:
        return 0

def TPName_Calculation():
    return get_string(USWBasicInfo.TPCommon)

def TPQualEquityGrants_Calculation():
    return Round(get_currency(USDW2.CodeHH, FieldCopies(USDW2.Taxpayer)))

def SSN_Calculation():
    return get_string(IAF1040.SSN)

def TPTotNonConformAdj_Calculation():
    Tot1to10 = Currency()

    Tot11to20 = Currency()

    Tot21to30 = Currency()
    Tot1to10 = get_currency(IAWNONCONFORMADJ.TPCapContr) + get_currency(IAWNONCONFORMADJ.TPLikeKind) + get_currency(IAWNONCONFORMADJ.TPBusInterestLimit) + get_currency(IAWNONCONFORMADJ.TPExcessiveRemun) + get_currency(IAWNONCONFORMADJ.TPCertSettlement) + get_currency(IAWNONCONFORMADJ.TPFDICPrem) + get_currency(IAWNONCONFORMADJ.TPDomProd) + get_currency(IAWNONCONFORMADJ.TPSec199QBIDed) + get_currency(IAWNONCONFORMADJ.TPSec199CoopDed) + get_currency(IAWNONCONFORMADJ.TPOthBusDed)
    Tot11to20 = get_currency(IAWNONCONFORMADJ.TPCharContLimit) + get_currency(IAWNONCONFORMADJ.TPSCorpCharCont) + get_currency(IAWNONCONFORMADJ.TPExcessBusLossLimit) + get_currency(IAWNONCONFORMADJ.TPQualEquityGrants) + get_currency(IAWNONCONFORMADJ.TPCapRules) + get_currency(IAWNONCONFORMADJ.TPCertCapAssets) + get_currency(IAWNONCONFORMADJ.TPQualOppZone) + get_currency(IAWNONCONFORMADJ.TPBuiltInLosses) + get_currency(IAWNONCONFORMADJ.TPBasisLimitPartLoss) + get_currency(IAWNONCONFORMADJ.TPBasisLifeIns)
    Tot21to30 = get_currency(IAWNONCONFORMADJ.TPTransferValueLifeIns) + get_currency(IAWNONCONFORMADJ.TPAlaskaNativeCorp) + get_currency(IAWNONCONFORMADJ.TPGlobalLowTI) + get_currency(IAWNONCONFORMADJ.TPRelParHybridTrans) + get_currency(IAWNONCONFORMADJ.TPInventorySales) + get_currency(IAWNONCONFORMADJ.TPOwnedForCorp) + get_currency(IAWNONCONFORMADJ.TPSubPartF) + get_currency(IAWNONCONFORMADJ.TPForSourceDiv) + get_currency(IAWNONCONFORMADJ.TPIRC965Repat) + get_currency(IAWNONCONFORMADJ.TPOtherAdj)
    return Tot1to10 + Tot11to20 + Tot21to30


