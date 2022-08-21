Private Sub Description_Calculation()
    ReturnVal = "Nonconformity Adjustment " + CStr(GetCurrency(IAWNonConformAdj.PrTotNonConformAdj))
End Sub

Private Sub EOYDate_Calculation()
    ReturnVal = MakeDate(12, 31, YearNumber)
End Sub

Private Sub PrAlaskaNativeCorp_Calculation()
    ReturnVal = GetCurrency(IAWNonConformAdj.SPAlaskaNativeCorp) + GetCurrency(IAWNonConformAdj.TPAlaskaNativeCorp)
End Sub

Private Sub PrBasisLifeIns_Calculation()
    ReturnVal = GetCurrency(IAWNonConformAdj.SPBasisLifeIns) + GetCurrency(IAWNonConformAdj.TPBasisLifeIns)
End Sub

Private Sub PrBasisLimitPartLoss_Calculation()
    ReturnVal = GetCurrency(IAWNonConformAdj.SPBasisLimitPartLoss) + GetCurrency(IAWNonConformAdj.TPBasisLimitPartLoss)
End Sub

Private Sub PrBuiltInLosses_Calculation()
    ReturnVal = GetCurrency(IAWNonConformAdj.SPBuiltInLosses) + GetCurrency(IAWNonConformAdj.TPBuiltInLosses)
End Sub

Private Sub PrBusInterestLimit_Calculation()
    ReturnVal = GetCurrency(IAWNonConformAdj.SPBusInterestLimit) + GetCurrency(IAWNonConformAdj.TPBusInterestLimit)
End Sub

Private Sub PrCapContr_Calculation()
    ReturnVal = GetCurrency(IAWNonConformAdj.SPCapContr) + GetCurrency(IAWNonConformAdj.TPCapContr)
End Sub

Private Sub PrCapRules_Calculation()
    ReturnVal = GetCurrency(IAWNonConformAdj.SPCapRules) + GetCurrency(IAWNonConformAdj.TPCapRules)
End Sub

Private Sub PrCertCapAssets_Calculation()
    ReturnVal = GetCurrency(IAWNonConformAdj.SPCertCapAssets) + GetCurrency(IAWNonConformAdj.TPCertCapAssets)
End Sub

Private Sub PrCertSettlement_Calculation()
    ReturnVal = GetCurrency(IAWNonConformAdj.SPCertSettlement) + GetCurrency(IAWNonConformAdj.TPCertSettlement)
End Sub

Private Sub PrCharContLimit_Calculation()
    ReturnVal = GetCurrency(IAWNonConformAdj.SPCharContLimit) + GetCurrency(IAWNonConformAdj.TPCharContLimit)
End Sub

Private Sub PrDomProd_Calculation()
    ReturnVal = GetCurrency(IAWNonConformAdj.SPDomProd) + GetCurrency(IAWNonConformAdj.TPDomProd)
End Sub

Private Sub PrExcessBusLossLimit_Calculation()
    ReturnVal = GetCurrency(IAWNonConformAdj.SPExcessBusLossLimit) + GetCurrency(IAWNonConformAdj.TPExcessBusLossLimit)
End Sub

Private Sub PrExcessiveRemun_Calculation()
    ReturnVal = GetCurrency(IAWNonConformAdj.SPExcessiveRemun) + GetCurrency(IAWNonConformAdj.TPExcessiveRemun)
End Sub

Private Sub PrFDICPrem_Calculation()
    ReturnVal = GetCurrency(IAWNonConformAdj.SPFDICPrem) + GetCurrency(IAWNonConformAdj.TPFDICPrem)
End Sub

Private Sub PrForSourceDiv_Calculation()
    ReturnVal = GetCurrency(IAWNonConformAdj.SPForSourceDiv) + GetCurrency(IAWNonConformAdj.TPForSourceDiv)
End Sub

Private Sub PrGlobalLowTI_Calculation()
    ReturnVal = GetCurrency(IAWNonConformAdj.SPGlobalLowTI) + GetCurrency(IAWNonConformAdj.TPGlobalLowTI)
End Sub

Private Sub PrInventorySales_Calculation()
    ReturnVal = GetCurrency(IAWNonConformAdj.SPInventorySales) + GetCurrency(IAWNonConformAdj.TPInventorySales)
End Sub

Private Sub PrIRC965Repat_Calculation()
    ReturnVal = GetCurrency(IAWNonConformAdj.SPIRC965Repat) + GetCurrency(IAWNonConformAdj.TPIRC965Repat)
End Sub

Private Sub PrLikeKind_Calculation()
    ReturnVal = GetCurrency(IAWNonConformAdj.SPLikeKind) + GetCurrency(IAWNonConformAdj.TPLikeKind)
End Sub

Private Sub PrOthBusDed_Calculation()
    ReturnVal = GetCurrency(IAWNonConformAdj.SPOthBusDed) + GetCurrency(IAWNonConformAdj.TPOthBusDed)
End Sub

Private Sub PrOtherAdj_Calculation()
    ReturnVal = GetCurrency(IAWNonConformAdj.SPOtherAdj) + GetCurrency(IAWNonConformAdj.TPOtherAdj)
End Sub

Private Sub PrOwnedForCorp_Calculation()
    ReturnVal = GetCurrency(IAWNonConformAdj.SPOwnedForCorp) + GetCurrency(IAWNonConformAdj.TPOwnedForCorp)
End Sub

Private Sub PrQualEquityGrants_Calculation()
    ReturnVal = GetCurrency(IAWNonConformAdj.SPQualEquityGrants) + GetCurrency(IAWNonConformAdj.TPQualEquityGrants)
End Sub

Private Sub PrQualOppZone_Calculation()
    ReturnVal = GetCurrency(IAWNonConformAdj.SPQualOppZone) + GetCurrency(IAWNonConformAdj.TPQualOppZone)
End Sub

Private Sub PrRelParHybridTrans_Calculation()
    ReturnVal = GetCurrency(IAWNonConformAdj.SPRelParHybridTrans) + GetCurrency(IAWNonConformAdj.TPRelParHybridTrans)
End Sub

Private Sub PrSCorpCharCont_Calculation()
    ReturnVal = GetCurrency(IAWNonConformAdj.SPSCorpCharCont) + GetCurrency(IAWNonConformAdj.TPSCorpCharCont)
End Sub

Private Sub PrSec199CoopDed_Calculation()
    ReturnVal = GetCurrency(IAWNonConformAdj.SPSec199CoopDed) + GetCurrency(IAWNonConformAdj.TPSec199CoopDed)
End Sub

Private Sub PrSec199QBIDed_Calculation()
    ReturnVal = GetCurrency(IAWNonConformAdj.SPSec199QBIDed) + GetCurrency(IAWNonConformAdj.TPSec199QBIDed)
End Sub

Private Sub PrSubPartF_Calculation()
    ReturnVal = GetCurrency(IAWNonConformAdj.SPSubPartF) + GetCurrency(IAWNonConformAdj.TPSubPartF)
End Sub

Private Sub PrTotNonConformAdj_Calculation()
    ReturnVal = GetCurrency(IAWNonConformAdj.SPTotNonConformAdj) + GetCurrency(IAWNonConformAdj.TPTotNonConformAdj)
End Sub

Private Sub PrTransferValueLifeIns_Calculation()
    ReturnVal = GetCurrency(IAWNonConformAdj.SPTransferValueLifeIns) + GetCurrency(IAWNonConformAdj.TPTransferValueLifeIns)
End Sub

Private Sub SPExcessBusLossLimit_Calculation()
    ReturnVal = 0
End Sub

Private Sub SPLikeKind_Calculation()
    ReturnVal = 0
End Sub

Private Sub SPName_Calculation()
    ReturnVal = GetString(USWBasicInfo.SPCommon)
End Sub

Private Sub SPQualEquityGrants_Calculation()
    ReturnVal = Round(GetCurrency(USDW2.CodeHH, FieldCopies(USDW2.Spouse)))
End Sub

Private Sub SPTotNonConformAdj_Calculation()
    Dim Tot1to10 As Currency
    Dim Tot11to20 As Currency
    Dim Tot21to30 As Currency
    
    Tot1to10 = GetCurrency(IAWNonConformAdj.SPCapContr) + GetCurrency(IAWNonConformAdj.SPLikeKind) + GetCurrency(IAWNonConformAdj.SPBusInterestLimit) + GetCurrency(IAWNonConformAdj.SPExcessiveRemun) + GetCurrency(IAWNonConformAdj.SPCertSettlement) + GetCurrency(IAWNonConformAdj.SPFDICPrem) + GetCurrency(IAWNonConformAdj.SPDomProd) + GetCurrency(IAWNonConformAdj.SPSec199QBIDed) + GetCurrency(IAWNonConformAdj.SPSec199CoopDed) + GetCurrency(IAWNonConformAdj.SPOthBusDed)
    Tot11to20 = GetCurrency(IAWNonConformAdj.SPCharContLimit) + GetCurrency(IAWNonConformAdj.SPSCorpCharCont) + GetCurrency(IAWNonConformAdj.SPExcessBusLossLimit) + GetCurrency(IAWNonConformAdj.SPQualEquityGrants) + GetCurrency(IAWNonConformAdj.SPCapRules) + GetCurrency(IAWNonConformAdj.SPCertCapAssets) + GetCurrency(IAWNonConformAdj.SPQualOppZone) + GetCurrency(IAWNonConformAdj.SPBuiltInLosses) + GetCurrency(IAWNonConformAdj.SPBasisLimitPartLoss) + GetCurrency(IAWNonConformAdj.SPBasisLifeIns)
    Tot21to30 = GetCurrency(IAWNonConformAdj.SPTransferValueLifeIns) + GetCurrency(IAWNonConformAdj.SPAlaskaNativeCorp) + GetCurrency(IAWNonConformAdj.SPGlobalLowTI) + GetCurrency(IAWNonConformAdj.SPRelParHybridTrans) + GetCurrency(IAWNonConformAdj.SPInventorySales) + GetCurrency(IAWNonConformAdj.SPOwnedForCorp) + GetCurrency(IAWNonConformAdj.SPSubPartF) + GetCurrency(IAWNonConformAdj.SPForSourceDiv) + GetCurrency(IAWNonConformAdj.SPIRC965Repat) + GetCurrency(IAWNonConformAdj.SPOtherAdj)
    
    ReturnVal = Tot1to10 + Tot11to20 + Tot21to30
End Sub

Private Sub TPExcessBusLossLimit_Calculation()
    ReturnVal = 0
End Sub

Private Sub Exist_Calculation()
    ReturnVal = 1
End Sub

Private Sub TPLikeKind_Calculation()
    ReturnVal = 0
End Sub

Private Sub Names_Calculation()
    ReturnVal = GetString(USWBasicInfo.CombNames)
End Sub

Private Sub PrintMe_Calculation()
    If GetCurrency(IAWNonConformAdj.SPTotNonConformAdj) <> 0 Or GetCurrency(IAWNonConformAdj.TPTotNonConformAdj) <> 0 Then
        ReturnVal = 1
    Else
        ReturnVal = 0
    End If
End Sub

Private Sub TPName_Calculation()
    ReturnVal = GetString(USWBasicInfo.TPCommon)
End Sub

Private Sub TPQualEquityGrants_Calculation()
    ReturnVal = Round(GetCurrency(USDW2.CodeHH, FieldCopies(USDW2.Taxpayer)))
End Sub

Private Sub SSN_Calculation()
    ReturnVal = GetString(IAF1040.SSN)
End Sub

Private Sub TPTotNonConformAdj_Calculation()
    Dim Tot1to10 As Currency
    Dim Tot11to20 As Currency
    Dim Tot21to30 As Currency
    
    Tot1to10 = GetCurrency(IAWNonConformAdj.TPCapContr) + GetCurrency(IAWNonConformAdj.TPLikeKind) + GetCurrency(IAWNonConformAdj.TPBusInterestLimit) + GetCurrency(IAWNonConformAdj.TPExcessiveRemun) + GetCurrency(IAWNonConformAdj.TPCertSettlement) + GetCurrency(IAWNonConformAdj.TPFDICPrem) + GetCurrency(IAWNonConformAdj.TPDomProd) + GetCurrency(IAWNonConformAdj.TPSec199QBIDed) + GetCurrency(IAWNonConformAdj.TPSec199CoopDed) + GetCurrency(IAWNonConformAdj.TPOthBusDed)
    Tot11to20 = GetCurrency(IAWNonConformAdj.TPCharContLimit) + GetCurrency(IAWNonConformAdj.TPSCorpCharCont) + GetCurrency(IAWNonConformAdj.TPExcessBusLossLimit) + GetCurrency(IAWNonConformAdj.TPQualEquityGrants) + GetCurrency(IAWNonConformAdj.TPCapRules) + GetCurrency(IAWNonConformAdj.TPCertCapAssets) + GetCurrency(IAWNonConformAdj.TPQualOppZone) + GetCurrency(IAWNonConformAdj.TPBuiltInLosses) + GetCurrency(IAWNonConformAdj.TPBasisLimitPartLoss) + GetCurrency(IAWNonConformAdj.TPBasisLifeIns)
    Tot21to30 = GetCurrency(IAWNonConformAdj.TPTransferValueLifeIns) + GetCurrency(IAWNonConformAdj.TPAlaskaNativeCorp) + GetCurrency(IAWNonConformAdj.TPGlobalLowTI) + GetCurrency(IAWNonConformAdj.TPRelParHybridTrans) + GetCurrency(IAWNonConformAdj.TPInventorySales) + GetCurrency(IAWNonConformAdj.TPOwnedForCorp) + GetCurrency(IAWNonConformAdj.TPSubPartF) + GetCurrency(IAWNonConformAdj.TPForSourceDiv) + GetCurrency(IAWNonConformAdj.TPIRC965Repat) + GetCurrency(IAWNonConformAdj.TPOtherAdj)
    
    ReturnVal = Tot1to10 + Tot11to20 + Tot21to30
End Sub

