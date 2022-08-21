from vb2py.vbfunctions import *
from vb2py.vbdebug import *
import datetime



def Alert10_Calculation():
    if GetString(IAF1040.CountyNo) == '' or GetString(IAF1040.SchNo) == '':
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert11_Calculation():
    if GetString(IAF1040.CountyNo) == '':
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert12_Calculation():
    if GetString(IAF1040.SchNo) == '':
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert15_Calculation():
    if GetBool(IAF1040.MFJ) == True or GetBool(IAF1040.CombMFS) == True:
        if ( GetBool(IAF126.TpNonRes) == True or  ( GetBool(IAF126.TpPYRes) == True and  ( GetDate(IAF126.TpDateOut) > 0 and GetDate(IAF126.TpDateOut) < MakeDate(12, 31, YearNumber) ) ) )  and  ( GetBool(IAF126.SpNonRes) == True or  ( GetBool(IAF126.SpPYRes) == True and  ( GetDate(IAF126.SpDateOut) > 0 and GetDate(IAF126.SpDateOut) < MakeDate(12, 31, YearNumber) ) ) ) :
            if GetString(IAF1040.CountyNo) == '00':
                ReturnVal = 0
            else:
                ReturnVal = 1
        else:
            ReturnVal = 0
    elif GetBool(IAF126.TpNonRes) == True or  ( GetBool(IAF126.TpPYRes) == True and  ( GetDate(IAF126.TpDateOut) > 0 and GetDate(IAF126.TpDateOut) < MakeDate(12, 31, YearNumber) ) ) :
        if GetString(IAF1040.CountyNo) == '00':
            ReturnVal = 0
        else:
            ReturnVal = 1
    else:
        ReturnVal = 0

def Alert100_Calculation():
    if IAFS() == 3 and GetCurrency(IAF1040.BGainDed) != 0:
        ReturnVal = 1
    elif GetCurrency(IAF1040.AGainDed) != 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert110_Calculation():
    if GetNumber(USD1099R.UnderAge) > 0:
        if GetCurrency(IAOthAdj.TPIADis) + GetCurrency(IAOthAdj.SPIADis) == 0:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def Alert120_Calculation():
    if GetBool(USWResidency.F1040NR) == False and GetCurrency(IAOthAdj.SIANOL) > 0 and GetCurrency(IAOthAdj.SIANOL) == Abs(GetCurrency(USWOthInc.SPNOL)):
        ReturnVal = 1
    elif GetBool(USWResidency.F1040NR) == False and GetCurrency(IAOthAdj.TIANOL) > 0 and GetCurrency(IAOthAdj.TIANOL) == Abs(GetCurrency(USWOthInc.TPNOL)):
        ReturnVal = 1
    elif GetBool(USWResidency.F1040NR) == True and GetCurrency(IAOthAdj.TIANOL) > 0 and GetCurrency(IAOthAdj.TIANOL) == Abs(GetCurrency(USWOthIncNR.TPNOL)):
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert130_Calculation():
    if GetCurrency(IAAddFedTax.TPBalDue) != 0 or GetCurrency(IAAddFedTax.SPBalDue) != 0:
        ReturnVal = 0
    elif GetCurrency(IAF1040.BRefund) == 0 and GetCurrency(IAF1040.ARefund) == 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert150_Calculation():
    if GetBool(USWRec.ItmDdn) == False and GetBool(IAF1040.ItemCheck) == False:
        if GetCurrency(IARequired.SchADeprAmt) != 0:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def Alert180_Calculation():
    if ( GetCurrency(USF1040.Foreign) > 0 or GetCurrency(USF1040NR.Foreign) > 0 )  and GetBool(IA130.Exist) == False:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert190_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Integer()

    Total2 = Integer()
    Lim = GetAllCopies(IA137)
    count = 1
    Total = 0
    Total2 = 0
    while count <= Lim:
        if GetBool(IA137.Taxpayer, count) == True and GetBool(IA137.Company, count) == True and GetBool(IA137.Print, count) == True:
            Total = Total + 1
        else:
            Total = Total
        if GetBool(IA137.Taxpayer, count) == True and GetBool(IA137.Site, count) == True and GetBool(IA137.Print, count) == True:
            Total2 = Total2 + 1
        else:
            Total2 = Total2
        count = count + 1
    if Total > 1:
        ReturnVal = 1
    elif Total > 0 and Total2 > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert20_Calculation():
    if FedFS() == 1 and IAFS() != 1:
        ReturnVal = 1
    elif FedFS() == 2 and IAFS() != 2 and IAFS() != 3:
        ReturnVal = 1
    elif FedFS() == 3 and IAFS() != 4:
        ReturnVal = 1
    elif FedFS() == 4 and IAFS() != 5:
        ReturnVal = 1
    elif FedFS() == 5 and IAFS() != 6:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert200_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Integer()

    Total2 = Integer()
    Lim = GetAllCopies(IA137)
    count = 1
    Total = 0
    Total2 = 0
    while count <= Lim:
        if GetBool(IA137.Spouse, count) == True and GetBool(IA137.Company, count) == True and GetBool(IA137.Print, count) == True:
            Total = Total + 1
        else:
            Total = Total
        if GetBool(IA137.Spouse, count) == True and GetBool(IA137.Site, count) == True and GetBool(IA137.Print, count) == True:
            Total2 = Total2 + 1
        else:
            Total2 = Total2
        count = count + 1
    if Total > 1:
        ReturnVal = 1
    elif Total > 0 and Total2 > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert210_Calculation():
    if GetNumber(IASch4136.MEF4136TP) > 1 or GetNumber(IASch4136.MEF4136SP) > 1:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert220_Calculation():
    if IAFS() != 3:
        if GetCurrency(IASch4136.TotCr, 1) > 0 and GetCurrency(IASch4136.TotCr, 2) > 0:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def Alert225_Calculation():
    ReturnVal = 0

def Alert250_Calculation():
    if GetCurrency(IAF1040.Penalty) > 0 and GetDate(IAF1040.DateDuePaid) == datetime.datetime(4, 30, 2019):
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert260_Calculation():
    Est1 = Long()

    Est2 = Long()
    if GetBool(IAEstimates.ApplySpecific, 1) == True:
        if GetCurrency(IAEstimates.SpecAmt, 1) > GetCurrency(IAEstimates.TotNetTax2, 1):
            Est1 = 1
        else:
            Est1 = 0
    else:
        Est1 = 0
    if GetBool(IAEstimates.ApplySpecific, 2) == True:
        if GetCurrency(IAEstimates.SpecAmt, 2) > GetCurrency(IAEstimates.TotNetTax2, 2):
            Est2 = 1
        else:
            Est2 = 0
    else:
        Est2 = 0
    if Est1 + Est2 > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert280_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Integer()
    Lim = GetAllCopies(IA177)
    count = 1
    Total = 0
    while count <= Lim:
        if GetCurrency(IA177.CYAdoptionTaxCr, count) > 0:
            Total = Total + 1
        else:
            Total = Total
        count = count + 1
    if GetNumber(USWAdoption.Create) > 0 and GetCurrency(IASchA.TotAdoptAmt) == 0 and Total == 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert30_Calculation():
    if GetCurrency(USWRec.TAGI) > 0 and GetCurrency(USWRec.SAGI) > 0 and GetBool(IAF1040.MFJ) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert282_Calculation():
    if GetBool(IAF1040.CombMFS) == True and GetBool(IA177.Spouse) == 0 and GetCurrency(IA177.CYAdoptionTaxCr) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert285_Calculation():
    if GetBool(IARequired.VerifiedIA177) == True:
        ReturnVal = 0
    elif GetBool(IAF1040.CombMFS) == True and GetCurrency(IA177.CYAdoptionTaxCr) > Decimal("5000"):
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert295A_Calculation():
    if GetCurrency(IAF1040.AEst) == 0:
        ReturnVal = 0
    elif GetCurrency(IAF1040.AEst) == GetCurrency(IAF1040.AIATaxWith):
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert295B_Calculation():
    if GetCurrency(IAF1040.BEst) == 0:
        ReturnVal = 0
    elif GetCurrency(IAF1040.BEst) == GetCurrency(IAF1040.BIATaxWith):
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert300_Calculation():
    if GetNumber(IARequired.SchBIntNoPayer) > 0:
        ReturnVal = 1
    elif GetNumber(IAWBPInt.IntNoPayer) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert310_Calculation():
    if GetNumber(IARequired.SchBDivNoPayer) > 0:
        ReturnVal = 1
    elif GetNumber(IAWBPDiv.DivNoPayer) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert320_Calculation():
    if GetBool(IAF126.TpPYRes) == True:
        if GetString(IAF126.TpDateIn) == '' and GetString(IAF126.TpDateOut) == '':
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def Alert330_Calculation():
    if GetBool(IAF126.SpPYRes) == True and GetBool(IARequired.AskSpouse) == True:
        if GetString(IAF126.SpDateIn) == '' and GetString(IAF126.SpDateOut) == '':
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def Alert40_Calculation():
    if GetBool(IAF1040.NoMFSInc) == True:
        ReturnVal = 0
    elif GetBool(IAF1040.MFS) == True and GetCurrency(IAF1040.SpIncome) == 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert50_Calculation():
    if GetBool(IAF1040.MFS) == True and  ( GetCurrency(IAWkAltTax.Lesser) > 0 and  ( GetCurrency(IAWkAltTax.Lesser) == GetCurrency(IAWkAltTax.Mult) ) ) :
        if GetCurrency(IAF1040.SpSSB) == 0 and GetBool(IAF1040.NoSpSSB) == False:
            ReturnVal = 1
        elif GetCurrency(IAF1040.SpPenExcl) == 0 and GetBool(IAF1040.NoSpPenExcl) == False:
            ReturnVal = 1
        elif GetCurrency(IAF1040.SpTaxInc) == 0 and GetBool(IAF1040.NoSpTaxInc) == False:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def Alert60_Calculation():
    if GetCurrency(IARequired.IAEic) > 0:
        if GetBool(IAF1040.NoMFSEI) == True:
            ReturnVal = 0
        elif GetBool(IAF1040.MFS) == True and GetCurrency(IAF1040.MFSEI) == 0:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def Alert70_Calculation():
    ReturnVal = 0

def Alert80_Calculation():
    #Re-did to factor in prior year 179 assets and use IAStatePrior. Does trigger for any year with bonus.  Next year 2019 need to alert non conformity assets that are disposed? Not this year since should only be current year assets.
    ReturnVal = GetNumber(IAWDepr.StatePriorDisposal)

def Alert90_Calculation():
    #for 2018 make no change since need to ask or alert if had depr adjustment in prior year and need to make an entry for catch-up depr. May need to see next year if should exclude 2018 veh that were not reported on IA4562A since was just on IA 2106
    if GetBool(IARequired.Ask4562A) == True:
        if GetCurrency(IA4562A.TotP2ColF) == 0:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def Alert340_Calculation():
    #set this to zero if Iowa passes conformity
    #ReturnVal = GetNumber(USWSpouse.StateSec179Tent) fed calc for this is below, do similar but with IA fields
    #If GetCurrency(USW4562State.TotElect179) <> GetCurrency(USW4562State.Tent179) Then
    #    ReturnVal = 1
    #Else
    #    ReturnVal = 0
    #End If
    if GetCurrency(IARequired.TotElect179) != GetCurrency(IARequired.Tent179):
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert345_Calculation():
    if GetCurrency(IARequired.Diss179) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert350_Calculation():
    if GetCurrency(IA1040X.TotPrevTax) > Decimal("0") and  ( GetCurrency(IA1040X.TotPrevTax) == GetCurrency(IA1040X.PrevOP) ) :
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert360_Calculation():
    if GetBool(IARequired.VerifiedIA126) == True:
        ReturnVal = 0
    elif GetNumber(IAF126.Print) == 1:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Ask130Copy_Calculation():
    if GetBool(IARequired.F130Y) == True and GetNumber(IA130.Exist) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Ask134_Calculation():
    if GetNumber(IA134.Exist) > 0:
        ReturnVal = 1
    elif GetBool(IAF1040.CombMFS) == True and GetNumber(IA134Sp.Exist) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Ask4136_Calculation():
    if GetBool(USF4136.Exist) == True or GetNumber(USSchF.Exist) > 0 or GetNumber(USSchC.Exist) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Ask4562A_Calculation():
    if GetNumber(IA4562A.StateDispNbr) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Ask4562PIV_Calculation():
    if GetNumber(USDPartK1.Exist) > 0 or GetNumber(USDSCorpK1.Exist) > 0:
        ReturnVal = 1
    elif GetNumber(IA4562PIV.Exist) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def AskCharCont_Calculation():
    FedContributions = Currency()
    if GetBool(USWResidency.F1040NR) == False:
        FedContributions = GetCurrency(USSchA.Cash) + GetCurrency(USSchA.NonCash)
    else:
        FedContributions = GetCurrency(USSchANR.Cash) + GetCurrency(USSchANR.NonCash)
    if FedContributions > 0:
        if GetCurrency(IAF1040.BOthIACr) > 0 or GetCurrency(IAF1040.AOthIACr) > 0:
            ReturnVal = 1
        elif GetCurrency(IAOthAdj.TPVet) > 0 or GetCurrency(IAOthAdj.SPVet) > 0:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def AskEarlyChCr_Calculation():
    if Trim(GetString(IAChildCredit.DepName(0))) != '' and GetCurrency(IAChildCredit.TotNI) < Decimal("45000"):
        ReturnVal = 1
    else:
        ReturnVal = 0

def AskEstCopy_Calculation():
    if GetBool(IARequired.EstY) == True and GetNumber(IAEstimates.Exist) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def AskFedFuel_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        if GetCurrency(USF4136.TotalCredit) > 0 or GetCurrency(IAAddFedTax.SPFuel) > 0:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def AskFilStat_Calculation():
    if IAFS() == 2 or IAFS() == 3 or IAFS() == 4:
        ReturnVal = 1
    else:
        ReturnVal = 0

def AskIAEst_Calculation():
    if GetBool(IAF1040.CombMFS) == True and GetCurrency(IAStateEst.TotIAEst) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def AskMedExp_Calculation():
    if GetCurrency(USSchA.MedExp) > 0:
        if GetCurrency(IAF1040.BHealth) > 0 or GetCurrency(IAF1040.AHealth) > 0:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def AskPenExc_Calculation():
    if GetCurrency(IAF1040.AIRA) + GetCurrency(IAF1040.APensions) + GetCurrency(IAF1040.BIRA) + GetCurrency(IAF1040.BPensions) + GetCurrency(IAF126.AIRA) + GetCurrency(IAF126.APensions) + GetCurrency(IAF126.BIRA) + GetCurrency(IAF126.BPensions) != 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def AskPensions_Calculation():
    if GetCurrency(USWRec.TotPension) > 0:
        ReturnVal = 1
    elif GetCurrency(IAWPenExc.TPPensions) + GetCurrency(IAWPenExc.SPPensions) != 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def AskReviewOthAdj_Calculation():
    if GetStatusCopies(IAWHealth, ModifiedStatus) > 0:
        ReturnVal = 1
    elif GetStatusCopies(IAWPenExc, ModifiedStatus) > 0:
        ReturnVal = 1
    elif GetCurrency(IAF1040.AGainDed) > 0 or GetCurrency(IAF1040.BGainDed) > 0:
        ReturnVal = 1
    elif GetStatusCopies(IAOthAdj, ModifiedStatus) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def BalDueAmt_Calculation():
    ReturnVal = Abs(GetCurrency(IAF1040.RefBalDue))

def BaseAmt_Calculation():
    if GetBool(IAF1040.Over65) == True:
        ReturnVal = Decimal("24000")
    else:
        ReturnVal = Decimal("9000")

def BProRate_Calculation():
    if IAFS() == 3:
        if GetCurrency(IAF1040.BNet) < 0 and GetCurrency(IAF1040.ANet) < 0:
            if GetCurrency(IAF1040.BNet) < GetCurrency(IAF1040.ANet):
                ReturnVal = 0
            else:
                ReturnVal = 1
        elif GetCurrency(IAF1040.BNet) < 0:
            ReturnVal = 0
        elif GetCurrency(IAF1040.BNet) > 0 and GetCurrency(IARequired.TotNI) <= 0:
            ReturnVal = 1
        elif GetCurrency(IARequired.TotNI) == 0:
            ReturnVal = 0
        else:
            ReturnVal = MaxValue(0, ( MinValue(1, GetFloat(IAF1040.BNet) / GetFloat(IARequired.TotNI)) ))
    else:
        ReturnVal = 0

def BusInc179_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IARequired.FedLn11) + GetCurrency(IARequired.IABusinessNC))

def CombNames_Calculation():
    if GetBool(IAF1040.MFJ) == True or GetBool(IAF1040.CombMFS) == True:
        if GetString(IAF1040.LastName) == GetString(IAF1040.SpouseLast):
            ReturnVal = GetString(IAF1040.FirstName) + ' and ' + GetString(IAF1040.SpouseFirst) + ' ' + GetString(IAF1040.LastName)
        else:
            ReturnVal = GetString(IAF1040.FirstName) + ' ' + GetString(IAF1040.LastName) + ' and ' + GetString(IAF1040.SpouseFirst) + ' ' + GetString(IAF1040.SpouseLast)
    else:
        ReturnVal = GetString(IAF1040.FirstName) + ' ' + GetString(IAF1040.LastName)

def CrAddFedTax_Calculation():
    if GetNumber(USWFICA.Exist) > 0:
        ReturnVal = 1
    elif GetNumber(USF4136.Exist) > 0:
        ReturnVal = 1
    elif GetCurrency(USWRec.PYOwe) > 0:
        ReturnVal = 1
    elif GetCurrency(USWRec.PYOweNR) > 0:
        ReturnVal = 1
    elif GetCurrency(USWRec.PYExt) > 0:
        ReturnVal = 1
    elif GetCurrency(USWRec.PYExtNR) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrOthAdj_Calculation():
    if GetNumber(USWOthAdj.Exist) > 0:
        ReturnVal = 1
    elif GetNumber(USWOthAdjNR.Exist) > 0:
        ReturnVal = 1
    elif GetNumber(USWOthInc.Exist) > 0:
        ReturnVal = 1
    elif GetNumber(USWOthIncNR.Exist) > 0:
        ReturnVal = 1
    elif GetBool(USF8910.Print) == True:
        ReturnVal = 1
    elif GetCurrency(USWRec.TotEdExp) > 0:
        ReturnVal = 1
    elif GetCurrency(USWRec.TotBusExp2106) > 0:
        ReturnVal = 1
    elif GetCurrency(USWRec.TotStudAdj) > 0:
        ReturnVal = 1
    elif GetCurrency(USWRec.TotTuitAdj) > 0:
        ReturnVal = 1
    elif GetCurrency(USWRec.TotHealthSav) > 0:
        ReturnVal = 1
    elif GetCurrency(USWRec.TotDomProd) > 0:
        ReturnVal = 1
        # Need to create if PYNR so interview displays correctly for IA 126 worksheets
    elif GetBool(IAF126.TpPYNR) == True or GetBool(IAF126.SpPYNR) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrOthInc_Calculation():
    if GetNumber(USWOthInc.Exist) > 0:
        ReturnVal = 1
    elif GetNumber(USWOthIncNR.Exist) > 0:
        ReturnVal = 1
    elif GetCurrency(IA4562.TotDepAdj) != 0:
        ReturnVal = 1
    elif GetCurrency(IA4562Sp.TotDepAdj) != 0:
        ReturnVal = 1
    elif GetCurrency(IA4562A.TotDepAdj) != 0:
        ReturnVal = 1
    elif GetCurrency(USF6251.Depl) != 0:
        ReturnVal = 1
    elif GetCurrency(USF6251.IntangDrill) != 0:
        ReturnVal = 1
        # Need to create if PYNR so interview displays correctly for IA 126 worksheets
    elif GetBool(IAF126.TpPYNR) == True or GetBool(IAF126.SpPYNR) == True:
        ReturnVal = 1
    elif GetCurrency(IARequired.Tot8824) != 0:
        ReturnVal = 1
    elif GetCurrency(IARequired.TotIAExReimb) != 0:
        ReturnVal = 1
    elif GetCurrency(IAWNonConformAdj.SPTotNonConformAdj) != 0 or GetCurrency(IAWNonConformAdj.TPTotNonConformAdj) != 0:
        ReturnVal = 1
    elif GetCurrency(IA4684.IANonConformAdj) != 0:
        ReturnVal = 1
    elif GetCurrency(IA2106.IAWages) != 0:
        ReturnVal = 1
    elif GetCurrency(IAWSchFLoss.ExcessLoss) != 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrPenExc_Calculation():
    if GetCurrency(USWRec.TotIRAInc) != 0:
        ReturnVal = 1
    elif GetCurrency(USWRetirement.TPAddQCD) != 0:
        ReturnVal = 1
    elif GetCurrency(USWRetirement.SPAddQCD) != 0:
        ReturnVal = 1
    elif GetCurrency(USWRec.TotPension) != 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CrSETax_Calculation():
    if GetCurrency(USF8962.PTCRepay) != 0:
        ReturnVal = 1
    elif GetCurrency(USF1040.SETax) != 0:
        ReturnVal = 1
    elif GetCurrency(USF1040NR.SETax) != 0:
        ReturnVal = 1
    elif GetCurrency(USF1040.TipTax) != 0:
        ReturnVal = 1
    elif GetCurrency(USF1040NR.TipTax) != 0:
        ReturnVal = 1
    elif GetCurrency(USWRetirement.RetTax) != 0:
        ReturnVal = 1
    elif GetCurrency(USF1040.SchHTax) != 0:
        ReturnVal = 1
    elif GetCurrency(USF1040NR.SchHTax) != 0:
        ReturnVal = 1
    elif GetCurrency(USF1040.HomeBuyRepay) != 0:
        ReturnVal = 1
    elif GetCurrency(USF1040NR.HomeBuyRepay) != 0:
        ReturnVal = 1
    elif GetCurrency(USWHealthPen.Penalty) != 0:
        ReturnVal = 1
    elif GetCurrency(USF8959.TotAddMedTax) != 0:
        ReturnVal = 1
    elif GetCurrency(USWOthTax.TotOthTax) != 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CurrentDate_Calculation():
    ReturnVal = CDate('Current')

def Ded179_Calculation():
    ReturnVal = MinValue(GetCurrency(IARequired.BusInc179), GetCurrency(IARequired.Tent179) + GetCurrency(IARequired.TotCo179))

def DepLength_Calculation():
    ReturnVal = Len(GetString(IARequired.DepNames))

def DepNames_Calculation():
    DepName = String()
    if GetString(USWAddDep.DepFName(0)) != '':
        DepName = GetString(USWAddDep.DepFName(0)) + ' '
    if GetString(USWAddDep.DepFName(1)) != '':
        DepName = DepName + GetString(USWAddDep.DepFName(1)) + ' '
    if GetString(USWAddDep.DepFName(2)) != '':
        DepName = DepName + GetString(USWAddDep.DepFName(2)) + ' '
    if GetString(USWAddDep.DepFName(3)) != '':
        DepName = DepName + GetString(USWAddDep.DepFName(3)) + ' '
    if GetString(USWAddDep.DepFName(4)) != '':
        DepName = DepName + GetString(USWAddDep.DepFName(4)) + ' '
    if GetString(USWAddDep.DepFName(5)) != '':
        DepName = DepName + GetString(USWAddDep.DepFName(5)) + ' '
    ReturnVal = DepName

def DeprAdj_Calculation():
    ReturnVal = GetCurrency(IAWOthInc.TotBonus)

def Diss179_Calculation():
    ReturnVal = GetCurrency(IARequired.TotCo179) + GetCurrency(IARequired.Tent179) - GetCurrency(IARequired.Ded179)

def EICRatio_Calculation():
    if GetCurrency(IARequired.TotEICEarnInc) == 0:
        ReturnVal = 0
    elif GetCurrency(IARequired.SEICEarnInc) < 0:
        ReturnVal = 0
    else:
        ReturnVal = MinValue(1, MaxValue(0, GetFloat(IARequired.SEICEarnInc) / GetFloat(IARequired.TotEICEarnInc)))

def FedAGI_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USF1040.AGI)
    else:
        ReturnVal = GetCurrency(USF1040NR.AGI)

def FedFilingStatus_Calculation():
    if FedFS() == 1:
        ReturnVal = 'single'
    elif FedFS() == 2:
        ReturnVal = 'married filing jointly'
    elif FedFS() == 3:
        ReturnVal = 'married filing separately'
    elif FedFS() == 4:
        ReturnVal = 'head of household'
    else:
        ReturnVal = 'qualifying widow(er)'

def FedLn11_Calculation():
    ReturnVal = GetCurrency(USF4562.BusInc179, 1)

def FilingStatus_Calculation():
    ReturnVal = IAFS()

def FYEIC_Calculation():
    ReturnVal = CDollar(GetFloat(USF1040.Eic) * 0.15)

def FYRes_Calculation():
    Only1NR = Long()

    TPRes = Long()

    SPRes = Long()
    if GetBool(IAF126.TpNonRes) == True and GetBool(IAF126.SpRes) == True:
        Only1NR = 1
    elif GetBool(IAF126.TpRes) == True and GetBool(IAF126.SpNonRes) == True:
        Only1NR = 1
    else:
        Only1NR = 0
    if GetBool(IAF126.Exist) == False:
        TPRes = 1
    elif GetBool(IAF1040.MFJ) == True and Only1NR == 1:
        TPRes = 1
    elif GetBool(IAF1040.MFJ) == True and GetBool(IAF126.TpRes) == True and GetBool(IAF126.SpRes) == True:
        TPRes = 1
    elif GetBool(IAF1040.MFJ) != True and GetBool(IAF126.TpRes) == True:
        TPRes = 1
    else:
        TPRes = 0
    if GetBool(IAF1040.CombMFS) == True:
        if GetBool(IAF126.Exist) == False:
            SPRes = 1
        elif GetBool(IAF126.SpRes) == True:
            SPRes = 1
        else:
            SPRes = 0
    else:
        SPRes = 0
    if GetBool(IAF1040.CombMFS) == True:
        if TPRes + SPRes == 2:
            ReturnVal = 1
        else:
            ReturnVal = 0
    elif TPRes == 1:
        ReturnVal = 1
    else:
        ReturnVal = 0

def IAAGI_Calculation():
    ReturnVal = GetCurrency(IARequired.FedAGI) + GetCurrency(IARequired.DeprAdj) + GetCurrency(IARequired.NonConfLn14) - GetCurrency(IARequired.NCMove) - GetCurrency(IARequired.NCDomProd)

def IABusinessNC_Calculation():
    ReturnVal = GetCurrency(IAWOthInc.TotNonConform)

def IAEic_Calculation():
    if GetBool(IAF126.TpPYNR) == True or GetBool(IAF126.SpPYNR):
        ReturnVal = GetCurrency(IARequired.PYNREIC)
    else:
        ReturnVal = GetCurrency(IARequired.FYEIC)

def JointDiv_Calculation():
    count = Integer()

    SchBTotal = Currency()

    count1 = Integer()

    HowManyWBPDiv = Long()

    WSTotal = Currency()

    DivIndex = Long()
    count = 0
    SchBTotal = 0
    while count < 7:
        if GetBool(IASchB.DJ1(count)) == True:
            SchBTotal = SchBTotal + GetCurrency(IASchB.TaxDiv(count))
        else:
            SchBTotal = SchBTotal
        count = count + 1
    count1 = 1
    HowManyWBPDiv = GetAllCopies(IAWBPDiv)
    WSTotal = 0
    while count1 <= HowManyWBPDiv:
        DivIndex = 0
        while DivIndex < 22:
            if GetBool(IAWBPDiv.DJ1(DivIndex), count1) == True:
                WSTotal = WSTotal + GetCurrency(IAWBPDiv.TaxDiv(DivIndex), count1)
            DivIndex = DivIndex + 1
        count1 = count1 + 1
    ReturnVal = SchBTotal + WSTotal

def JointInt_Calculation():
    count = Integer()

    SchBTotal = Currency()

    count1 = Integer()

    HowManyWBPInt = Long()

    WSTotal = Currency()

    IntIndex = Long()
    count = 0
    SchBTotal = 0
    while count < 7:
        if GetBool(IASchB.IJ1(count)) == True:
            SchBTotal = SchBTotal + GetCurrency(IASchB.TaxInt(count))
        else:
            SchBTotal = SchBTotal
        count = count + 1
    count1 = 1
    HowManyWBPInt = GetAllCopies(IAWBPInt)
    WSTotal = 0
    while count1 <= HowManyWBPInt:
        IntIndex = 0
        while IntIndex < 22:
            if GetBool(IAWBPInt.IJ1(IntIndex), count1) == True:
                WSTotal = WSTotal + GetCurrency(IAWBPInt.TaxInt(IntIndex), count1)
            IntIndex = IntIndex + 1
        count1 = count1 + 1
    ReturnVal = SchBTotal + WSTotal

def JointSPDiv_Calculation():
    ReturnVal = Round(CDollar(CDbl(GetCurrency(IARequired.JointDiv)) * 0.5))

def JointSPInt_Calculation():
    ReturnVal = Round(CDollar(CDbl(GetCurrency(IARequired.JointInt)) * 0.5))

def JointTPDiv_Calculation():
    ReturnVal = GetCurrency(IARequired.JointDiv) - GetCurrency(IARequired.JointSPDiv)

def JointTPInt_Calculation():
    ReturnVal = GetCurrency(IARequired.JointInt) - GetCurrency(IARequired.JointSPInt)

def JTComb_Calculation():
    if GetString(IAF1040.LastName) == GetString(IAF1040.SpouseLast):
        ReturnVal = GetString(IAF1040.LastName) + ', ' + GetString(IAF1040.FirstName) + ' and ' + GetString(IAF1040.SpouseFirst)
    else:
        ReturnVal = GetString(IAF1040.LastName) + ', ' + GetString(IAF1040.FirstName) + ' and ' + GetString(IAF1040.SpouseLast) + ', ' + GetString(IAF1040.SpouseFirst)

def LILimit_Calculation():
    if IAFS() == 1 and GetBool(IAF1040.DepY) == True:
        ReturnVal = Decimal("5000")
    elif IAFS() == 1 and GetBool(IAF1040.DepY) == False and GetBool(IAF1040.Over65) == True:
        ReturnVal = Decimal("24001")
    elif IAFS() == 1 and GetBool(IAF1040.DepY) == False:
        ReturnVal = Decimal("9001")
    elif IAFS() == 1 or GetBool(IAF1040.DepY) == True:
        ReturnVal = Decimal("0")
    elif GetBool(IAF1040.Over65) == True:
        ReturnVal = Decimal("32001")
    else:
        ReturnVal = Decimal("13501")

def Limit179_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IARequired.Max179) - GetCurrency(IARequired.Reduction179))

def LITotIncome_Calculation():
    ReturnVal = GetCurrency(IAWkAltTax.Ln26)

def LowInc_Calculation():
    if GetCurrency(USF4972.Tax) + GetCurrency(USF4972Spouse.Tax) > 0:
        ReturnVal = 0
    elif GetCurrency(IAF1040.AIAMin) > 0 or GetCurrency(IAF1040.BIAMin) > 0:
        ReturnVal = 0
    elif GetBool(IAF126.TpPYNR) == True or GetBool(IAF126.SpPYNR) == True:
        ReturnVal = 0
    elif GetBool(IARequired.AskFilStat) == True and GetBool(IAWkAltTax.NOL) == True:
        ReturnVal = 0
    elif GetCurrency(IARequired.LITotIncome) < GetCurrency(IARequired.LILimit):
        ReturnVal = 1
    else:
        ReturnVal = 0

def Max179_Calculation():
    ReturnVal = Decimal("70000")

def MobDisQual_Calculation():
    ReturnVal = 0

def ModAmt_Calculation():
    TP = Currency()

    SP = Currency()
    TP = GetCurrency(IAF1040.ATotAdj) - GetCurrency(IAF1040.AFedTax) + GetCurrency(IAF1040.AFedDed) + GetCurrency(IAF1040.ADedBox)
    SP = GetCurrency(IAF1040.BTotAdj) - GetCurrency(IAF1040.BFedTax) + GetCurrency(IAF1040.BFedDed) + GetCurrency(IAF1040.BDedBox)
    ReturnVal = TP + SP

def ModChg_Calculation():
    ReturnVal = Abs(GetCurrency(IARequired.TotIncChg) - GetCurrency(IAF1040.AAltTax))

def ModCk_Calculation():
    Tax = Currency()

    Modifications = Currency()
    Tax = GetCurrency(IAF1040.AAltTax)
    Modifications = GetCurrency(IARequired.TotIncChg) - Tax
    if Modifications > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Names_Calculation():
    ReturnVal = GetString(IARequired.CombNames)

def NCDomProd_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAOthAdj.TPDomProd) + GetCurrency(IAOthAdj.SPDomProd) - GetCurrency(USF8903.DPADeduction))

def NCMove_Calculation():
    ReturnVal = GetCurrency(IA3903.MovExpDdn)

def NonConfLn14_Calculation():
    ReturnVal = GetCurrency(IAWOthInc.TotNonConform)

def NonCredAmt_Calculation():
    TP = Currency()

    SP = Currency()
    TP = GetCurrency(IAF1040.ACredits) + GetCurrency(IAF1040.ACrNon) + GetCurrency(IAF1040.AOutState) + GetCurrency(IAF1040.AOthIACr)
    SP = GetCurrency(IAF1040.BCredits) + GetCurrency(IAF1040.BCrNon) + GetCurrency(IAF1040.BOutState) + GetCurrency(IAF1040.BOthIACr)
    ReturnVal = TP + SP

def NonCredChg_Calculation():
    ReturnVal = GetCurrency(IARequired.NonCredAmt)

def NonCredCk_Calculation():
    if GetCurrency(IARequired.NonCredChg) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def OthTaxAmt_Calculation():
    TP = Currency()

    SP = Currency()
    TP = GetCurrency(IAF1040.ALump) + GetCurrency(IAF1040.AIAMin) + GetCurrency(IAF1040.ASch)
    TP = GetCurrency(IAF1040.BLump) + GetCurrency(IAF1040.BIAMin) + GetCurrency(IAF1040.BSch)
    ReturnVal = TP + SP + GetCurrency(IAF1040.TotContrib)

def OthTaxChg_Calculation():
    ReturnVal = GetCurrency(IARequired.OthTaxAmt)

def OthTaxCk_Calculation():
    if GetCurrency(IARequired.OthTaxChg) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def PayAmt_Calculation():
    ReturnVal = GetCurrency(IAF1040.TotCredit)

def PayChg_Calculation():
    ReturnVal = GetCurrency(IARequired.PayAmt)

def PayCk_Calculation():
    if GetCurrency(IARequired.PayChg) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def PenDonAmt_Calculation():
    ReturnVal = GetCurrency(IAF1040.BApply99) + GetCurrency(IAF1040.AApply99) + GetCurrency(IAF1040.Penalty) + GetCurrency(IAF1040.PenInt)

def PenDonChg_Calculation():
    ReturnVal = GetCurrency(IARequired.PenDonAmt)

def PenDonCk_Calculation():
    if GetCurrency(IARequired.PenDonChg) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def PrnSchCode_Calculation():
    if GetString(IAF1040.SchNo) == '00811':
        ReturnVal = '0081'
    elif GetString(IAF1040.SchNo) == '44911':
        ReturnVal = '4491'
    elif GetString(IAF1040.SchNo) == '45181':
        ReturnVal = '4518'
    elif GetString(IAF1040.SchNo) == '58951':
        ReturnVal = '5895'
    else:
        ReturnVal = GetString(IAF1040.SchNo)

def PrnSurvivorSP_Calculation():
    if GetString(USWTaxpayer.PrnSurvivorSP) == 'File as Surviving Sp.':
        ReturnVal = GetString(USWTaxpayer.PrnSurvivorSP) + ' ' + GetString(USWBasicInfo.YouDeath)
    else:
        ReturnVal = GetString(USWTaxpayer.PrnSurvivorSP)

def PrnSurvivorTP_Calculation():
    if GetString(USWTaxpayer.PrnSurvivorTP) == 'File as Surviving Sp.':
        ReturnVal = GetString(USWTaxpayer.PrnSurvivorTP)
    else:
        ReturnVal = GetString(USWTaxpayer.PrnSurvivorTP)

def PYNetInc_Calculation():
    ReturnVal = GetCurrency(IARequired.PYNetIncA) + GetCurrency(IARequired.PYNetIncB)

def PYNetIncA_Calculation():
    ReturnVal = GetCurrency(USZIA1040.IAPYNetIncA)

def PYNetIncB_Calculation():
    ReturnVal = GetCurrency(USZIA1040.IAPYNetIncB)

def PYNREIC_Calculation():
    ReturnVal = MinValue(GetCurrency(IARequired.FYEIC), ( CDollar(GetFloat(IARequired.FYEIC) * GetFloat(IAChildCredit.PYNRPercent)) ))

def PYRatio_Calculation():
    if GetBool(IARequired.AskSpouse) == False:
        ReturnVal = 0
    elif GetCurrency(IARequired.PYNetIncB) < 0 and GetCurrency(IARequired.PYNetIncA) < 0:
        if GetCurrency(IARequired.PYNetIncB) < GetCurrency(IARequired.PYNetIncA):
            ReturnVal = 0
        else:
            ReturnVal = 1
    elif GetCurrency(IARequired.PYNetIncB) < 0:
        ReturnVal = 0
    elif GetCurrency(IARequired.PYNetIncB) > 0 and GetCurrency(IARequired.PYNetInc) <= 0:
        ReturnVal = 1
    elif GetCurrency(IARequired.PYNetInc) == 0:
        ReturnVal = 0
    else:
        ReturnVal = MaxValue(0, ( MinValue(1, GetFloat(IARequired.PYNetIncB) / GetFloat(IARequired.PYNetInc)) ))

def QnACompMob_Calculation():
    if GetBool(IARequired.QnAComp) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

def QSAmtOwe_Calculation():
    if GetCurrency(IAF1040.RefBalDue) < 0:
        ReturnVal = Abs(GetCurrency(IAF1040.RefBalDue))
    else:
        ReturnVal = 0

def QSRefund_Calculation():
    if GetCurrency(IAF1040.RefBalDue) > 0:
        ReturnVal = GetCurrency(IAF1040.RefBalDue)
    else:
        ReturnVal = 0

def Reduction179_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IARequired.TotCost179) - GetCurrency(IARequired.Threshold179))

def RefundAmt_Calculation():
    ReturnVal = GetCurrency(IAF1040.RefBalDue)

def RefundCk_Calculation():
    if GetCurrency(IARequired.RefundAmt) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def S1099RWH_Calculation():
    count1 = Integer()

    HowMany1099R = Long()

    Total1 = Currency()
    count1 = 1
    HowMany1099R = GetAllCopies(USD1099R)
    Total1 = 0
    while count1 <= HowMany1099R:
        if GetString(USD1099R.St1, count1) == 'IA' and GetBool(USD1099R.Spouse, count1) == True:
            Total1 = Total1 + GetCurrency(USD1099R.StWh1, count1)
        if GetString(USD1099R.St2, count1) == 'IA' and GetBool(USD1099R.Spouse, count1) == True:
            Total1 = Total1 + GetCurrency(USD1099R.STWh2, count1)
        count1 = count1 + 1
    ReturnVal = Round(Total1)

def SchADeprAmt_Calculation():
    count = Long()

    count3 = Long()

    Total1 = Currency()

    Total3 = Currency()

    HowManyIAWDepr = Long()

    HowManyIA4562A = Long()
    #believe situation now is that parent A is gone, should only have this situation now when fed 2106 is for a "Disabled" (which goes to Sch A for fed and IA) and have either 4562 or 2106veh depr. All other 2106 depr is either only claimed on IA subject to 2% (no adjustment needed since nothing on fed) or claimed on fed (fed .Quaifies) as an adjustment to AGI and then we will properly account for this on IA4562A
    count = 1
    count3 = 1
    Total1 = 0
    Total3 = 0
    HowManyIAWDepr = GetAllCopies(IAWDepr)
    HowManyIA4562A = GetAllCopies(IA4562A)
    while count <= HowManyIAWDepr:
        if GetString(IAWDepr.ParentType, count) == '2106' and GetBool(IAWDepr.Qualifies, count) == True:
            Total1 = Total1 + GetCurrency(IAWDepr.TotAdj, count)
        count = count + 1
    while count3 <= HowManyIA4562A:
        if GetString(IA4562A.EmpBusType, count3) == '27':
            Total3 = Total3 + GetCurrency(IA4562A.DepAdj, count3)
        count3 = count3 + 1
    ReturnVal = Total1 + Total3

def SchBDivNoPayer_Calculation():
    count = Variant()

    Iter = Integer()
    count = 0
    Iter = 0
    while Iter < 7:
        if GetCurrency(IASchB.Dividend(Iter)) > 0 and Trim(GetString(IASchB.DivPayer(Iter))) == '':
            count = count + 1
        Iter = Iter + 1
    if GetBool(IASchB.PrintIAB) == True and count > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def SchBIntNoPayer_Calculation():
    count = Variant()

    Iter = Integer()
    count = 0
    Iter = 0
    while Iter < 7:
        if GetCurrency(IASchB.Interest(Iter)) > 0 and Trim(GetString(IASchB.Payer(Iter))) == '':
            count = count + 1
        Iter = Iter + 1
    if GetBool(IASchB.PrintIAB) == True and count > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def SEarnInc_Calculation():
    Part = Currency()

    SE = Currency()

    Wages = Currency()

    NonTaxCombat = Currency()

    SP409AInc = Currency()

    JtSP409AInc = Currency()
    Part = GetCurrency(USDPartK1.SEInc, FieldCopies(USDPartK1.Spouse)) + CDollar(GetFloat(USDPartK1.SEInc, FieldCopies(USDPartK1.Joint)) * 0.5)
    SE = GetCurrency(IAF1040.BBusInc) + GetCurrency(IAF1040.BFarm) - GetCurrency(IAF1040.BBusIncL) - GetCurrency(USWRec.SKeough)
    Wages = MaxValue(0, GetCurrency(IAF1040.BWages) - GetCurrency(USDStudent.TaxScholar, FieldCopies(USDStudent.Spouse)) - Round(GetCurrency(USDW2.NonQual, FieldCopies(USDW2.Spouse))) - Round(GetCurrency(USDW2AS.NonQual, FieldCopies(USDW2AS.Spouse))) - Round(GetCurrency(USDW2CM.NonQual, FieldCopies(USDW2CM.Spouse))) - Round(GetCurrency(USDW2GU.NonQual, FieldCopies(USDW2GU.Spouse))) - Round(GetCurrency(USDW2VI.NonQual, FieldCopies(USDW2VI.Spouse))))
    NonTaxCombat = Round(GetCurrency(USDW2.CodeQ, FieldCopies(USDW2.Spouse))) + Round(GetCurrency(USDW2AS.CodeQ, FieldCopies(USDW2AS.Spouse))) + Round(GetCurrency(USDW2CM.CodeQ, FieldCopies(USDW2CM.Spouse))) + Round(GetCurrency(USDW2GU.CodeQ, FieldCopies(USDW2GU.Spouse))) + Round(GetCurrency(USDW2VI.CodeQ, FieldCopies(USDW2VI.Spouse)))
    SP409AInc = Round(GetCurrency(USDW2.CodeZ, FieldCopies(USDW2.Spouse))) + Round(GetCurrency(USDW2AS.CodeZ, FieldCopies(USDW2AS.Spouse))) + Round(GetCurrency(USDW2CM.CodeZ, FieldCopies(USDW2CM.Spouse))) + Round(GetCurrency(USDW2GU.CodeZ, FieldCopies(USDW2GU.Spouse))) + Round(GetCurrency(USDW2VI.CodeZ, FieldCopies(USDW2VI.Spouse))) + Round(GetCurrency(USD1099MISC.Income, FieldCopies(USD1099MISC.Spouse)))
    JtSP409AInc = Round(CDollar(GetFloat(USD1099MISC.Income, FieldCopies(USD1099MISC.Joint)) * 0.5))
    ReturnVal = MaxValue(0, Wages + GetCurrency(IAF1040.BAlimony) + MaxValue(0, SE + Part) + GetCurrency(USWOthInc.SP2555) + NonTaxCombat - SP409AInc - JtSP409AInc)

def SEICEarnInc_Calculation():
    if GetBool(IAF1040.MFS) == True:
        ReturnVal = GetCurrency(IAF1040.MFSEI)
    else:
        ReturnVal = GetCurrency(IAF1040.BWages) + GetCurrency(IAF1040.BBusInc) + GetCurrency(IAF1040.BFarm)

def ShowRef_Calculation():
    if GetCurrency(IARequired.QSAmtOwe) > 0:
        ReturnVal = 0
    else:
        ReturnVal = 1

def SIaEIC_Calculation():
    ReturnVal = CDollar(GetFloat(IARequired.IAEic) * GetFloat(IARequired.EICRatio))

def SIAExReimb_Calculation():
    ReturnVal = GetCurrency(IARequired.TotIAExReimb) - GetCurrency(IARequired.TIAExReimb)

def SIAW2WH_Calculation():
    count1 = Integer()

    HowManyW2 = Long()

    Total1 = Currency()

    W2Index = Long()
    count1 = 1
    HowManyW2 = GetAllCopies(USDW2)
    Total1 = 0
    while count1 <= HowManyW2:
        W2Index = 0
        while W2Index < 8:
            if GetString(USDW2.St(W2Index), count1) == 'IA' and GetBool(USDW2.Spouse, count1) == True:
                Total1 = Total1 + GetCurrency(USDW2.STWh(W2Index), count1)
            W2Index = W2Index + 1
        count1 = count1 + 1
    ReturnVal = Round(Total1)

def SIRA_Calculation():
    if IAFS() == 3:
        if GetCurrency(IARequired.TEarnInc) < GetCurrency(USWIRA.TPDedIRA):
            ReturnVal = GetCurrency(USWIRA.TPDedIRA) + GetCurrency(USWIRA.SPDedIRA) - GetCurrency(IARequired.TEarnInc)
        else:
            ReturnVal = MinValue(GetCurrency(IARequired.SEarnInc), GetCurrency(USWIRA.SPDedIRA))
    else:
        ReturnVal = 0

def AskSpouse_Calculation():
    if IAFS() == 2 or IAFS() == 3:
        ReturnVal = 1
    else:
        ReturnVal = 0

def SLimLoss_Calculation():
    ReturnVal = GetCurrency(USWDRec.LimLoss) - GetCurrency(IARequired.TLimLoss)

def SMove_Calculation():
    ReturnVal = GetCurrency(IARequired.TotMove) - GetCurrency(IARequired.TMove)

def SP8824_Calculation():
    ReturnVal = GetCurrency(IARequired.Tot8824) - GetCurrency(IARequired.TP8824)

def SPCapGainWH_Calculation():
    count1 = Integer()

    HowManyCapGain = Long()

    Total1 = Currency()

    CGIndex = Long()
    count1 = 1
    HowManyCapGain = GetAllCopies(USDCapGain)
    Total1 = 0
    while count1 <= HowManyCapGain:
        CGIndex = 0
        while CGIndex < 2:
            if GetString(USDCapGain.St2(CGIndex), count1) == 'IA' and GetBool(USDCapGain.Spouse, count1) == True:
                Total1 = Total1 + GetCurrency(USDCapGain.STWh2(CGIndex), count1)
            elif GetString(USDCapGain.St2(CGIndex), count1) == 'IA' and GetBool(USDCapGain.Joint, count1) == True:
                Total1 = Total1 + CDollar(GetFloat(USDCapGain.STWh2(CGIndex), count1) * 0.5)
            CGIndex = CGIndex + 1
        count1 = count1 + 1
    ReturnVal = Round(Total1)

def SPComb_Calculation():
    if GetBool(IAF1040.MFJ) == True or GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetString(IAF1040.SpouseLast) + ', ' + GetString(IAF1040.SpouseFirst)
    else:
        ReturnVal = ''

def SPCombName_Calculation():
    if GetBool(IAF1040.MFJ) == True or GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetString(IAF1040.SpouseFirst) + ' ' + GetString(IAF1040.SpouseLast)
    else:
        ReturnVal = ''

def SPDivWH_Calculation():
    count1 = Integer()

    HowMany1099Div = Long()

    Total1 = Currency()

    DivIndex = Long()
    count1 = 1
    HowMany1099Div = GetAllCopies(USD1099DIV)
    Total1 = 0
    while count1 <= HowMany1099Div:
        DivIndex = 0
        while DivIndex < 2:
            if GetString(USD1099DIV.St(DivIndex), count1) == 'IA' and GetBool(USD1099DIV.Spouse, count1) == True:
                Total1 = Total1 + GetCurrency(USD1099DIV.STWh(DivIndex), count1)
            elif GetString(USD1099DIV.St(DivIndex), count1) == 'IA' and GetBool(USD1099DIV.Joint, count1) == True:
                Total1 = Total1 + CDollar(GetFloat(USD1099DIV.STWh(DivIndex), count1) * 0.5)
            DivIndex = DivIndex + 1
        count1 = count1 + 1
    ReturnVal = Round(Total1)

def SPIntWH_Calculation():
    count1 = Integer()

    HowMany1099Int = Long()

    Total1 = Currency()

    IntIndex = Long()
    count1 = 1
    HowMany1099Int = GetAllCopies(USD1099INT)
    Total1 = 0
    while count1 <= HowMany1099Int:
        IntIndex = 0
        while IntIndex < 2:
            if GetString(USD1099INT.St(IntIndex), count1) == 'IA' and GetBool(USD1099INT.Spouse, count1) == True:
                Total1 = Total1 + GetCurrency(USD1099INT.STWh(IntIndex), count1)
            elif GetString(USD1099INT.St(IntIndex), count1) == 'IA' and GetBool(USD1099INT.Joint, count1) == True:
                Total1 = Total1 + CDollar(GetFloat(USD1099INT.STWh(IntIndex), count1) * 0.5)
            IntIndex = IntIndex + 1
        count1 = count1 + 1
    ReturnVal = Round(Total1)

def SPKWH_Calculation():
    count1 = Integer()

    HowMany1099K = Long()

    Total1 = Currency()

    KIndex = Long()
    count1 = 1
    HowMany1099K = GetAllCopies(USD1099K)
    Total1 = 0
    while count1 <= HowMany1099K:
        KIndex = 0
        while KIndex < 2:
            if GetString(USD1099K.State(KIndex), count1) == 'IA' and GetBool(USD1099K.Spouse, count1) == True:
                Total1 = Total1 + GetCurrency(USD1099K.StateInc(KIndex), count1)
            elif GetString(USD1099K.State(KIndex), count1) == 'IA' and GetBool(USD1099K.Joint, count1) == True:
                Total1 = Total1 + CDollar(GetFloat(USD1099K.StateInc(KIndex), count1) * 0.5)
            KIndex = KIndex + 1
        count1 = count1 + 1
    ReturnVal = Round(Total1)

def SPMiscWH_Calculation():
    count1 = Integer()

    HowMany1099MISC = Long()

    Total1 = Currency()
    count1 = 1
    HowMany1099MISC = GetAllCopies(USD1099MISC)
    Total1 = 0
    while count1 <= HowMany1099MISC:
        if GetString(USD1099MISC.State, count1) == 'IA':
            if GetBool(USD1099MISC.Spouse, count1) == True:
                Total1 = Total1 + GetCurrency(USD1099MISC.StateWH, count1)
            elif GetBool(USD1099MISC.Joint, count1) == True:
                Total1 = Total1 + CDollar(GetFloat(USD1099MISC.StateWH, count1) * 0.5)
            else:
                Total1 = Total1
        else:
            Total1 = Total1
        if GetString(USD1099MISC.State2, count1) == 'IA':
            if GetBool(USD1099MISC.Spouse, count1) == True:
                Total1 = Total1 + GetCurrency(USD1099MISC.StateWH2, count1)
            elif GetBool(USD1099MISC.Joint, count1) == True:
                Total1 = Total1 + CDollar(GetFloat(USD1099MISC.StateWH2, count1) * 0.5)
            else:
                Total1 = Total1
        else:
            Total1 = Total1
        count1 = count1 + 1
    ReturnVal = Round(Total1)

def SPOIDWH_Calculation():
    count1 = Integer()

    HowMany1099OID = Long()

    Total1 = Currency()

    OIDIndex = Long()
    count1 = 1
    HowMany1099OID = GetAllCopies(USD1099OID)
    Total1 = 0
    while count1 <= HowMany1099OID:
        OIDIndex = 0
        while OIDIndex < 2:
            if GetString(USD1099OID.St(OIDIndex), count1) == 'IA' and GetBool(USD1099OID.Spouse, count1) == True:
                Total1 = Total1 + GetCurrency(USD1099OID.STWh(OIDIndex), count1)
            elif GetString(USD1099OID.St(OIDIndex), count1) == 'IA' and GetBool(USD1099OID.Joint, count1) == True:
                Total1 = Total1 + CDollar(GetFloat(USD1099OID.STWh(OIDIndex), count1) * 0.5)
            OIDIndex = OIDIndex + 1
        count1 = count1 + 1
    ReturnVal = Round(Total1)

def SPOthIncWH_Calculation():
    ReturnVal = 0

def SPTotIncChg_Calculation():
    Mid = Currency()

    MidInt = Long()

    TotTaxInc = Currency()
    # updated for 2018
    TotTaxInc = GetCurrency(IAF1040.BGross)
    if TotTaxInc > Decimal("95650"):
        Mid = TotTaxInc
    elif TotTaxInc > Decimal("150"):
        MidInt = CLng(( TotTaxInc - Decimal("1") )  / Decimal("50"))
        Mid = ( CCur(MidInt) * Decimal("50") )  + Decimal("25")
    else:
        Mid = Decimal("0")
    ReturnVal = Tax(Mid)

def SPUnemWH_Calculation():
    count1 = Integer()

    HowManyUnempl = Long()

    Total1 = Currency()

    UnIndex = Long()
    count1 = 1
    HowManyUnempl = GetAllCopies(USWUnempl)
    Total1 = 0
    while count1 <= HowManyUnempl:
        UnIndex = 0
        while UnIndex < 2:
            if GetString(USWUnempl.TPState(UnIndex), count1) == 'IA' and GetBool(USWUnempl.Spouse, count1) == True:
                Total1 = Total1 + GetCurrency(USWUnempl.TPStWH(UnIndex), count1)
            UnIndex = UnIndex + 1
        count1 = count1 + 1
    ReturnVal = Round(Total1)

def SPW2GWH_Calculation():
    count1 = Integer()

    HowManyW2G = Long()

    Total1 = Currency()
    count1 = 1
    HowManyW2G = GetAllCopies(USDW2G)
    Total1 = 0
    while count1 <= HowManyW2G:
        if GetString(USDW2G.StateWon, count1) == 'IA' and GetBool(USDW2G.Spouse, count1) == True:
            Total1 = Total1 + GetCurrency(USDW2G.StateWH, count1)
        count1 = count1 + 1
    ReturnVal = Round(Total1)

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

def SummaryScript_Calculation():
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

def T1099rWH_Calculation():
    ReturnVal = GetCurrency(IARequired.Tot1099rWH) - GetCurrency(IARequired.S1099RWH)

def TaxReduction_Calculation():
    ReturnVal = MinValue(GetCurrency(IARequired.TentTaxRed), GetCurrency(IARequired.TentTax))

def TEarnInc_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(USWIRATrad.EarnInc) - GetCurrency(IARequired.SEarnInc))

def Tent179_Calculation():
    ReturnVal = MinValue(GetCurrency(IARequired.TotElect179), GetCurrency(IARequired.Limit179))

def TentTax_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAF1040.ATotIATax) - GetCurrency(IAF1040.ACredits))

def TentTaxRed_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IARequired.TotNIPenExc) - GetCurrency(IARequired.BaseAmt))

def Threshold179_Calculation():
    ReturnVal = Decimal("280000")

def TIAEic_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IARequired.IAEic) - GetCurrency(IARequired.SIaEIC))

def TIAExReimb_Calculation():
    ReturnVal = GetCurrency(IA3903.IAExReimb, FieldCopies(IA3903.Taxpayer)) + CDollar(GetFloat(IA3903.IAExReimb, FieldCopies(IA3903.Joint)) * 0.5)

def TIAW2WH_Calculation():
    ReturnVal = GetCurrency(IARequired.TotIAW2WH) - GetCurrency(IARequired.SIAW2WH)

def TIRA_Calculation():
    ReturnVal = GetCurrency(IARequired.TotIRA) - GetCurrency(IARequired.SIRA)

def TLimLoss_Calculation():
    if GetCurrency(USWDRec.CapGain) < 0:
        if GetCurrency(USWDRec.TCapGain) < 0 and GetCurrency(USWDRec.SCapGain) < 0 and IAFS() == 3:
            if GetCurrency(USWDRec.SCapGain) < - Decimal("1500"):
                ReturnVal = MaxValue(GetCurrency(USWDRec.TCapGain), - Decimal("1500"))
            else:
                ReturnVal = GetCurrency(USWDRec.LimLoss) - GetCurrency(USWDRec.SCapGain)
        elif GetCurrency(USWDRec.TCapGain) < 0:
            ReturnVal = GetCurrency(USWDRec.LimLoss)
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def TMove_Calculation():
    FedMove = Currency()

    StateMove = Currency()
    FedMove = GetCurrency(USWRec.TMove)
    StateMove = Round(GetCurrency(IA3903.MovExpDdn, FieldCopies(IA3903.Taxpayer)) + CDollar(GetFloat(IA3903.MovExpDdn, FieldCopies(IA3903.Joint)) * 0.5))
    ReturnVal = FedMove + StateMove

def Tot1042S_Calculation():
    count1 = Integer()

    HowMany1042S = Long()

    Total1 = Currency()

    F1042SIndex = Long()
    count1 = 1
    HowMany1042S = GetAllCopies(USD1042S)
    Total1 = 0
    while count1 <= HowMany1042S:
        F1042SIndex = 0
        while F1042SIndex < 4:
            if GetString(USD1042S.St(F1042SIndex), count1) == 'IA':
                Total1 = Total1 + GetCurrency(USD1042S.StWh(F1042SIndex), count1)
            F1042SIndex = F1042SIndex + 1
        count1 = count1 + 1
    ReturnVal = Round(Total1)

def Tot1099rWH_Calculation():
    count1 = Integer()

    HowMany1099R = Long()

    Total1 = Currency()
    count1 = 1
    HowMany1099R = GetAllCopies(USD1099R)
    Total1 = 0
    while count1 <= HowMany1099R:
        if GetString(USD1099R.St1, count1) == 'IA':
            Total1 = Total1 + GetCurrency(USD1099R.StWh1, count1)
        if GetString(USD1099R.St2, count1) == 'IA':
            Total1 = Total1 + GetCurrency(USD1099R.STWh2, count1)
        count1 = count1 + 1
    ReturnVal = Round(Total1)

def Tot8824_Calculation():
    ReturnVal = GetCurrency(IA8824.IANonConformAdj)

def TotApplied_Calculation():
    ReturnVal = GetCurrency(IAF1040.AApply99) + GetCurrency(IAF1040.BApply99)

def TotCapGainWH_Calculation():
    count1 = Integer()

    HowManyCapGain = Long()

    Total1 = Currency()

    CGIndex = Long()
    count1 = 1
    HowManyCapGain = GetAllCopies(USDCapGain)
    Total1 = 0
    while count1 <= HowManyCapGain:
        CGIndex = 0
        while CGIndex < 2:
            if GetString(USDCapGain.St2(CGIndex), count1) == 'IA':
                Total1 = Total1 + GetCurrency(USDCapGain.STWh2(CGIndex), count1)
            CGIndex = CGIndex + 1
        count1 = count1 + 1
    ReturnVal = Round(Total1)

def TotCo179_Calculation():
    ReturnVal = 0

def TotCost179_Calculation():
    #per 2016 Section 179 Expensing FAQs under section III for pass through entities #4 example shows that the cost of section 179 property passed through for federal should not pass through to the partner for purposes of the Iowa section 179 phase-out limits, remove + GetCurrency(USDPartK1.Sec179) + GetCurrency(USDSCorpK1.Sec179) from reproduced fed calc below.
    ReturnVal = GetCurrency(USWDepr.Sec179Basis) + GetCurrency(USWDepr.List179basis) + GetCurrency(USF4562.Sec179Basis2106, 1)

def TotCYIAEst_Calculation():
    TP = Currency()

    SP = Currency()
    if GetDate(IAStateEst.TPStQ4Date) < MakeDate(1, 1, YearNumber + 1):
        TP = GetCurrency(IAStateEst.TPStApply) + GetCurrency(IAStateEst.TPStQ1) + GetCurrency(IAStateEst.TPStQ2) + GetCurrency(IAStateEst.TPStQ3) + GetCurrency(IAStateEst.TPStQ4)
    else:
        TP = GetCurrency(IAStateEst.TPStApply) + GetCurrency(IAStateEst.TPStQ1) + GetCurrency(IAStateEst.TPStQ2) + GetCurrency(IAStateEst.TPStQ3)
    if GetDate(IAStateEst.SPStQ4Date) < MakeDate(1, 1, YearNumber + 1):
        SP = GetCurrency(IAStateEst.SPStApply) + GetCurrency(IAStateEst.SPStQ1) + GetCurrency(IAStateEst.SPStQ2) + GetCurrency(IAStateEst.SPStQ3) + GetCurrency(IAStateEst.SPStQ4)
    else:
        SP = GetCurrency(IAStateEst.SPStApply) + GetCurrency(IAStateEst.SPStQ1) + GetCurrency(IAStateEst.SPStQ2) + GetCurrency(IAStateEst.SPStQ3)
    if IAFS() == 3:
        ReturnVal = TP + SP
    else:
        ReturnVal = TP

def TotCyLocEst_Calculation():
    Local1 = Currency()

    Local2 = Currency()

    Local3 = Currency()
    if GetString(USWEstPay.LocName1) == 'OTHER':
        Local1 = GetCurrency(USWLocalEst.CYLocal, 1)
    else:
        Local1 = 0
    if GetString(USWEstPay.LocName2) == 'OTHER':
        Local2 = GetCurrency(USWLocalEst.CYLocal, 2)
    else:
        Local2 = 0
    if GetString(USWEstPay.LocName3) == 'OTHER':
        Local3 = GetCurrency(USWLocalEst.CYLocal, 3)
    else:
        Local3 = 0
    ReturnVal = Local1 + Local2 + Local3

def TotDiv_Calculation():
    ReturnVal = GetCurrency(IASchB.TotalTaxDiv)

def TotDivWH_Calculation():
    count1 = Integer()

    HowMany1099Div = Long()

    Total1 = Currency()

    DivIndex = Long()
    count1 = 1
    HowMany1099Div = GetAllCopies(USD1099DIV)
    Total1 = 0
    while count1 <= HowMany1099Div:
        DivIndex = 0
        while DivIndex < 2:
            if GetString(USD1099DIV.St(DivIndex), count1) == 'IA':
                Total1 = Total1 + GetCurrency(USD1099DIV.STWh(DivIndex), count1)
            DivIndex = DivIndex + 1
        count1 = count1 + 1
    ReturnVal = Round(Total1)

def TotEICEarnInc_Calculation():
    if GetBool(IAF1040.MFS) == True:
        ReturnVal = GetCurrency(IAF1040.MFSEI) + GetCurrency(IAF1040.AWages) + GetCurrency(IAF1040.ABusInc) + GetCurrency(IAF1040.AFarm)
    else:
        ReturnVal = GetCurrency(IAF1040.BWages) + GetCurrency(IAF1040.BBusInc) + GetCurrency(IAF1040.BFarm) + GetCurrency(IAF1040.AWages) + GetCurrency(IAF1040.ABusInc) + GetCurrency(IAF1040.AFarm)

def TotElect179_Calculation():
    ReturnVal = GetCurrency(USWDepr.IACYSec179Rep) + GetCurrency(USF4562.StateTotCySec1792106, 1) + GetCurrency(USWSummary179.StateK1)

def TotIAExReimb_Calculation():
    ReturnVal = GetCurrency(IA3903.IAExReimb)

def TotIAW2WH_Calculation():
    count1 = Integer()

    HowManyW2 = Long()

    Total1 = Currency()

    W2Index = Long()
    count1 = 1
    HowManyW2 = GetAllCopies(USDW2)
    Total1 = 0
    while count1 <= HowManyW2:
        W2Index = 0
        while W2Index < 8:
            if GetString(USDW2.St(W2Index), count1) == 'IA':
                Total1 = Total1 + GetCurrency(USDW2.STWh(W2Index), count1)
            W2Index = W2Index + 1
        count1 = count1 + 1
    ReturnVal = Round(Total1)

def TotIncAmt_Calculation():
    ReturnVal = GetCurrency(IAF1040.AGross) + GetCurrency(IAF1040.BGross)

def TotIncChg_Calculation():
    ReturnVal = GetCurrency(IARequired.TPTotIncChg) + GetCurrency(IARequired.SPTotIncChg)

def TotIncCk_Calculation():
    if GetCurrency(IARequired.TotIncChg) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def TotInt_Calculation():
    ReturnVal = GetCurrency(IASchB.TotalTaxInt)

def TotIntWH_Calculation():
    count1 = Integer()

    HowMany1099Int = Long()

    Total1 = Currency()

    IntIndex = Long()
    count1 = 1
    HowMany1099Int = GetAllCopies(USD1099INT)
    Total1 = 0
    while count1 <= HowMany1099Int:
        IntIndex = 0
        while IntIndex < 2:
            if GetString(USD1099INT.St(IntIndex), count1) == 'IA':
                Total1 = Total1 + GetCurrency(USD1099INT.STWh(IntIndex), count1)
            IntIndex = IntIndex + 1
        count1 = count1 + 1
    ReturnVal = Round(Total1)

def TotIRA_Calculation():
    ReturnVal = GetCurrency(USWRec.TotIRAAdj)

def TotKWH_Calculation():
    count1 = Integer()

    HowMany1099K = Long()

    Total1 = Currency()

    KIndex = Long()
    count1 = 1
    HowMany1099K = GetAllCopies(USD1099K)
    Total1 = 0
    while count1 <= HowMany1099K:
        KIndex = 0
        while KIndex < 2:
            if GetString(USD1099K.State(KIndex), count1) == 'IA':
                Total1 = Total1 + GetCurrency(USD1099K.StateInc(KIndex), count1)
            KIndex = KIndex + 1
        count1 = count1 + 1
    ReturnVal = Round(Total1)

def TotMiscWH_Calculation():
    count1 = Integer()

    HowMany1099MISC = Long()

    Total1 = Currency()
    count1 = 1
    HowMany1099MISC = GetAllCopies(USD1099MISC)
    Total1 = 0
    while count1 <= HowMany1099MISC:
        if GetString(USD1099MISC.State, count1) == 'IA':
            Total1 = Total1 + GetCurrency(USD1099MISC.StateWH, count1)
        if GetString(USD1099MISC.State2, count1) == 'IA':
            Total1 = Total1 + GetCurrency(USD1099MISC.StateWH2, count1)
        count1 = count1 + 1
    ReturnVal = Round(Total1)

def TotMove_Calculation():
    ReturnVal = GetCurrency(USWRec.TotMove) + GetCurrency(IA3903.MovExpDdn)

def TotNI_Calculation():
    ReturnVal = GetCurrency(IAF1040.ANet) + GetCurrency(IAF1040.BNet)

def TotNIPenExc_Calculation():
    ReturnVal = GetCurrency(IAWkAltTax.Ln26)

def TotOIDWH_Calculation():
    count1 = Integer()

    HowMany1099OID = Long()

    Total1 = Currency()

    OIDIndex = Long()
    count1 = 1
    HowMany1099OID = GetAllCopies(USD1099OID)
    Total1 = 0
    while count1 <= HowMany1099OID:
        OIDIndex = 0
        while OIDIndex < 2:
            if GetString(USD1099OID.St(OIDIndex), count1) == 'IA':
                Total1 = Total1 + GetCurrency(USD1099OID.STWh(OIDIndex), count1)
            OIDIndex = OIDIndex + 1
        count1 = count1 + 1
    ReturnVal = Round(Total1)

def TotOthIncWH_Calculation():
    ReturnVal = 0

def TotSPDiv_Calculation():
    count = Integer()

    SchBTotal = Currency()

    count1 = Integer()

    HowManyWBPDiv = Long()

    WSTotal = Currency()

    DivIndex = Long()
    count = 0
    SchBTotal = 0
    while count < 7:
        if GetBool(IASchB.DSp1(count)) == True:
            SchBTotal = SchBTotal + GetCurrency(IASchB.TaxDiv(count))
        else:
            SchBTotal = SchBTotal
        count = count + 1
    count1 = 1
    HowManyWBPDiv = GetAllCopies(IAWBPDiv)
    WSTotal = 0
    while count1 <= HowManyWBPDiv:
        DivIndex = 0
        while DivIndex < 22:
            if GetBool(IAWBPDiv.DSp1(DivIndex), count1) == True:
                WSTotal = WSTotal + GetCurrency(IAWBPDiv.TaxDiv(DivIndex), count1)
            DivIndex = DivIndex + 1
        count1 = count1 + 1
    ReturnVal = SchBTotal + WSTotal + GetCurrency(IARequired.JointSPDiv)

def TotSPInt_Calculation():
    count = Integer()

    SchBTotal = Currency()

    count1 = Integer()

    HowManyWBPInt = Long()

    WSTotal = Currency()

    IntIndex = Long()
    count = 0
    SchBTotal = 0
    while count < 7:
        if GetBool(IASchB.ISp1(count)) == True:
            SchBTotal = SchBTotal + GetCurrency(IASchB.TaxInt(count))
        else:
            SchBTotal = SchBTotal
        count = count + 1
    count1 = 1
    HowManyWBPInt = GetAllCopies(IAWBPInt)
    WSTotal = 0
    while count1 <= HowManyWBPInt:
        IntIndex = 0
        while IntIndex < 22:
            if GetBool(IAWBPInt.ISp1(IntIndex), count1) == True:
                WSTotal = WSTotal + GetCurrency(IAWBPInt.TaxInt(IntIndex), count1)
            IntIndex = IntIndex + 1
        count1 = count1 + 1
    ReturnVal = SchBTotal + WSTotal + GetCurrency(IARequired.JointSPInt)

def TotTPDiv_Calculation():
    ReturnVal = GetCurrency(IARequired.TotDiv) - GetCurrency(IARequired.TotSPDiv)

def TotTPInt_Calculation():
    ReturnVal = GetCurrency(IARequired.TotInt) - GetCurrency(IARequired.TotSPInt)

def TotUnemWH_Calculation():
    count1 = Integer()

    HowManyUnempl = Long()

    Total1 = Currency()

    UnIndex = Long()
    count1 = 1
    HowManyUnempl = GetAllCopies(USWUnempl)
    Total1 = 0
    while count1 <= HowManyUnempl:
        UnIndex = 0
        while UnIndex < 2:
            if GetString(USWUnempl.TPState(UnIndex), count1) == 'IA':
                Total1 = Total1 + GetCurrency(USWUnempl.TPStWH(UnIndex), count1)
            UnIndex = UnIndex + 1
        count1 = count1 + 1
    ReturnVal = Round(Total1)

def TotW2GWH_Calculation():
    count1 = Integer()

    HowManyW2G = Long()

    Total1 = Currency()
    count1 = 1
    HowManyW2G = GetAllCopies(USDW2G)
    Total1 = 0
    while count1 <= HowManyW2G:
        if GetString(USDW2G.StateWon, count1) == 'IA':
            Total1 = Total1 + GetCurrency(USDW2G.StateWH, count1)
        count1 = count1 + 1
    ReturnVal = Round(Total1)

def TP8824_Calculation():
    ReturnVal = GetCurrency(IA8824.IANonConformAdj, FieldCopies(IA8824.Taxpayer)) + CDollar(GetFloat(IA8824.IANonConformAdj, FieldCopies(IA8824.Joint)) * 0.5)

def TPCapGainWH_Calculation():
    ReturnVal = GetCurrency(IARequired.TotCapGainWH) - GetCurrency(IARequired.SPCapGainWH)

def TPComb_Calculation():
    ReturnVal = GetString(IAF1040.LastName) + ', ' + GetString(IAF1040.FirstName)

def TPCombName_Calculation():
    ReturnVal = GetString(IAF1040.FirstName) + ' ' + GetString(IAF1040.LastName)

def TPDivWH_Calculation():
    ReturnVal = GetCurrency(IARequired.TotDivWH) - GetCurrency(IARequired.SPDivWH)

def TPIntWH_Calculation():
    ReturnVal = GetCurrency(IARequired.TotIntWH) - GetCurrency(IARequired.SPIntWH)

def TPKWH_Calculation():
    ReturnVal = GetCurrency(USZIA1040.TotKWH) - GetCurrency(USZIA1040.SPKWH)

def TPMiscWH_Calculation():
    ReturnVal = GetCurrency(IARequired.TotMiscWH) - GetCurrency(IARequired.SPMiscWH)

def TPOIDWH_Calculation():
    ReturnVal = GetCurrency(IARequired.TotOIDWH) - GetCurrency(IARequired.SPOIDWH)

def TpOthIncWH_Calculation():
    ReturnVal = GetCurrency(IARequired.TotOthIncWH) - GetCurrency(IARequired.SPOthIncWH)

def TPTotIncChg_Calculation():
    Mid = Currency()

    MidInt = Long()

    TotTaxInc = Currency()
    # updated for 2018
    TotTaxInc = GetCurrency(IAF1040.AGross)
    if TotTaxInc > Decimal("95650"):
        Mid = TotTaxInc
    elif TotTaxInc > Decimal("150"):
        MidInt = CLng(( TotTaxInc - Decimal("1") )  / Decimal("50"))
        Mid = ( CCur(MidInt) * Decimal("50") )  + Decimal("25")
    else:
        Mid = Decimal("0")
    ReturnVal = Tax(Mid)

def TPUnemWH_Calculation():
    ReturnVal = GetCurrency(IARequired.TotUnemWH) - GetCurrency(IARequired.SPUnemWH)

def TPW2GWH_Calculation():
    ReturnVal = GetCurrency(IARequired.TotW2GWH) - GetCurrency(IARequired.SPW2GWH)

