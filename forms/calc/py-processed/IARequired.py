from forms.out import IA1040X
from forms.out import IA130
from forms.out import IA134SP
from forms.out import IA137
from forms.out import IA2106
from forms.out import IA3903
from forms.out import IA4562A
from forms.out import IA4562PIV
from forms.out import IA4562SP
from forms.out import IAADDFEDTAX
from forms.out import IACHILDCREDIT
from forms.out import IAESTIMATES
from forms.out import IAF1040
from forms.out import IAF126
from forms.out import IAOTHADJ
from forms.out import IAREQUIRED
from forms.out import IASCHA
from forms.out import IASCHB
from forms.out import IASTATEEST
from forms.out import IAWBPDIV
from forms.out import IAWBPINT
from forms.out import IAWHEALTH
from forms.out import IAWKALTTAX
from forms.out import IAWNONCONFORMADJ
from forms.out import IAWOTHINC
from forms.out import IAWPENEXC
from forms.out import USF4972SPOUSE
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *
import datetime



def Alert10_Calculation():
    if get_string(IAF1040.CountyNo) == '' or get_string(IAF1040.SchNo) == '':
        return 1
    else:
        return 0

def Alert11_Calculation():
    if get_string(IAF1040.CountyNo) == '':
        return 1
    else:
        return 0

def Alert12_Calculation():
    if get_string(IAF1040.SchNo) == '':
        return 1
    else:
        return 0

def Alert15_Calculation():
    if get_bool(IAF1040.MFJ) == True or get_bool(IAF1040.CombMFS) == True:
        if ( get_bool(IAF126.TpNonRes) == True or  ( get_bool(IAF126.TpPYRes) == True and  ( GetDate(IAF126.TpDateOut) > 0 and GetDate(IAF126.TpDateOut) < MakeDate(12, 31, YearNumber) ) ) )  and  ( get_bool(IAF126.SpNonRes) == True or  ( get_bool(IAF126.SpPYRes) == True and  ( GetDate(IAF126.SpDateOut) > 0 and GetDate(IAF126.SpDateOut) < MakeDate(12, 31, YearNumber) ) ) ) :
            if get_string(IAF1040.CountyNo) == '00':
                return 0
            else:
                return 1
        else:
            return 0
    elif get_bool(IAF126.TpNonRes) == True or  ( get_bool(IAF126.TpPYRes) == True and  ( GetDate(IAF126.TpDateOut) > 0 and GetDate(IAF126.TpDateOut) < MakeDate(12, 31, YearNumber) ) ) :
        if get_string(IAF1040.CountyNo) == '00':
            return 0
        else:
            return 1
    else:
        return 0

def Alert100_Calculation():
    if IAFS() == 3 and get_currency(IAF1040.BGainDed) != 0:
        return 1
    elif get_currency(IAF1040.AGainDed) != 0:
        return 1
    else:
        return 0

def Alert110_Calculation():
    if get_number(USD1099R.UnderAge) > 0:
        if get_currency(IAOTHADJ.TPIADis) + get_currency(IAOTHADJ.SPIADis) == 0:
            return 1
        else:
            return 0
    else:
        return 0

def Alert120_Calculation():
    if get_bool(USWResidency.F1040NR) == False and get_currency(IAOTHADJ.SIANOL) > 0 and get_currency(IAOTHADJ.SIANOL) == Abs(get_currency(USWOthInc.SPNOL)):
        return 1
    elif get_bool(USWResidency.F1040NR) == False and get_currency(IAOTHADJ.TIANOL) > 0 and get_currency(IAOTHADJ.TIANOL) == Abs(get_currency(USWOthInc.TPNOL)):
        return 1
    elif get_bool(USWResidency.F1040NR) == True and get_currency(IAOTHADJ.TIANOL) > 0 and get_currency(IAOTHADJ.TIANOL) == Abs(get_currency(USWOthIncNR.TPNOL)):
        return 1
    else:
        return 0

def Alert130_Calculation():
    if get_currency(IAADDFEDTAX.TPBalDue) != 0 or get_currency(IAADDFEDTAX.SPBalDue) != 0:
        return 0
    elif get_currency(IAF1040.BRefund) == 0 and get_currency(IAF1040.ARefund) == 0:
        return 1
    else:
        return 0

def Alert150_Calculation():
    if get_bool(USWRec.ItmDdn) == False and get_bool(IAF1040.ItemCheck) == False:
        if get_currency(IAREQUIRED.SchADeprAmt) != 0:
            return 1
        else:
            return 0
    else:
        return 0

def Alert180_Calculation():
    if ( get_currency(USF1040.Foreign) > 0 or get_currency(USF1040NR.Foreign) > 0 )  and get_bool(IA130.Exist) == False:
        return 1
    else:
        return 0

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
        if get_bool(IA137.Taxpayer, count) == True and get_bool(IA137.Company, count) == True and get_bool(IA137.Print, count) == True:
            Total = Total + 1
        else:
            Total = Total
        if get_bool(IA137.Taxpayer, count) == True and get_bool(IA137.Site, count) == True and get_bool(IA137.Print, count) == True:
            Total2 = Total2 + 1
        else:
            Total2 = Total2
        count = count + 1
    if Total > 1:
        return 1
    elif Total > 0 and Total2 > 0:
        return 1
    else:
        return 0

def Alert20_Calculation():
    if FedFS() == 1 and IAFS() != 1:
        return 1
    elif FedFS() == 2 and IAFS() != 2 and IAFS() != 3:
        return 1
    elif FedFS() == 3 and IAFS() != 4:
        return 1
    elif FedFS() == 4 and IAFS() != 5:
        return 1
    elif FedFS() == 5 and IAFS() != 6:
        return 1
    else:
        return 0

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
        if get_bool(IA137.Spouse, count) == True and get_bool(IA137.Company, count) == True and get_bool(IA137.Print, count) == True:
            Total = Total + 1
        else:
            Total = Total
        if get_bool(IA137.Spouse, count) == True and get_bool(IA137.Site, count) == True and get_bool(IA137.Print, count) == True:
            Total2 = Total2 + 1
        else:
            Total2 = Total2
        count = count + 1
    if Total > 1:
        return 1
    elif Total > 0 and Total2 > 0:
        return 1
    else:
        return 0

def Alert210_Calculation():
    if get_number(IASch4136.MEF4136TP) > 1 or get_number(IASch4136.MEF4136SP) > 1:
        return 1
    else:
        return 0

def Alert220_Calculation():
    if IAFS() != 3:
        if get_currency(IASch4136.TotCr, 1) > 0 and get_currency(IASch4136.TotCr, 2) > 0:
            return 1
        else:
            return 0
    else:
        return 0

def Alert225_Calculation():
    return 0

def Alert250_Calculation():
    if get_currency(IAF1040.Penalty) > 0 and GetDate(IAF1040.DateDuePaid) == datetime.datetime(4, 30, 2019):
        return 1
    else:
        return 0

def Alert260_Calculation():
    Est1 = Long()

    Est2 = Long()
    if get_bool(IAESTIMATES.ApplySpecific, 1) == True:
        if get_currency(IAESTIMATES.SpecAmt, 1) > get_currency(IAESTIMATES.TotNetTax2, 1):
            Est1 = 1
        else:
            Est1 = 0
    else:
        Est1 = 0
    if get_bool(IAESTIMATES.ApplySpecific, 2) == True:
        if get_currency(IAESTIMATES.SpecAmt, 2) > get_currency(IAESTIMATES.TotNetTax2, 2):
            Est2 = 1
        else:
            Est2 = 0
    else:
        Est2 = 0
    if Est1 + Est2 > 0:
        return 1
    else:
        return 0

def Alert280_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Integer()
    Lim = GetAllCopies(IA177)
    count = 1
    Total = 0
    while count <= Lim:
        if get_currency(IA177.CYAdoptionTaxCr, count) > 0:
            Total = Total + 1
        else:
            Total = Total
        count = count + 1
    if get_number(USWAdoption.Create) > 0 and get_currency(IASCHA.TotAdoptAmt) == 0 and Total == 0:
        return 1
    else:
        return 0

def Alert30_Calculation():
    if get_currency(USWRec.TAGI) > 0 and get_currency(USWRec.SAGI) > 0 and get_bool(IAF1040.MFJ) == True:
        return 1
    else:
        return 0

def Alert282_Calculation():
    if get_bool(IAF1040.CombMFS) == True and get_bool(IA177.Spouse) == 0 and get_currency(IA177.CYAdoptionTaxCr) > 0:
        return 1
    else:
        return 0

def Alert285_Calculation():
    if get_bool(IAREQUIRED.VerifiedIA177) == True:
        return 0
    elif get_bool(IAF1040.CombMFS) == True and get_currency(IA177.CYAdoptionTaxCr) > Decimal("5000"):
        return 1
    else:
        return 0

def Alert295A_Calculation():
    if get_currency(IAF1040.AEst) == 0:
        return 0
    elif get_currency(IAF1040.AEst) == get_currency(IAF1040.AIATaxWith):
        return 1
    else:
        return 0

def Alert295B_Calculation():
    if get_currency(IAF1040.BEst) == 0:
        return 0
    elif get_currency(IAF1040.BEst) == get_currency(IAF1040.BIATaxWith):
        return 1
    else:
        return 0

def Alert300_Calculation():
    if get_number(IAREQUIRED.SchBIntNoPayer) > 0:
        return 1
    elif get_number(IAWBPINT.IntNoPayer) > 0:
        return 1
    else:
        return 0

def Alert310_Calculation():
    if get_number(IAREQUIRED.SchBDivNoPayer) > 0:
        return 1
    elif get_number(IAWBPDIV.DivNoPayer) > 0:
        return 1
    else:
        return 0

def Alert320_Calculation():
    if get_bool(IAF126.TpPYRes) == True:
        if get_string(IAF126.TpDateIn) == '' and get_string(IAF126.TpDateOut) == '':
            return 1
        else:
            return 0
    else:
        return 0

def Alert330_Calculation():
    if get_bool(IAF126.SpPYRes) == True and get_bool(IAREQUIRED.AskSpouse) == True:
        if get_string(IAF126.SpDateIn) == '' and get_string(IAF126.SpDateOut) == '':
            return 1
        else:
            return 0
    else:
        return 0

def Alert40_Calculation():
    if get_bool(IAF1040.NoMFSInc) == True:
        return 0
    elif get_bool(IAF1040.MFS) == True and get_currency(IAF1040.SpIncome) == 0:
        return 1
    else:
        return 0

def Alert50_Calculation():
    if get_bool(IAF1040.MFS) == True and  ( get_currency(IAWKALTTAX.Lesser) > 0 and  ( get_currency(IAWKALTTAX.Lesser) == get_currency(IAWKALTTAX.Mult) ) ) :
        if get_currency(IAF1040.SpSSB) == 0 and get_bool(IAF1040.NoSpSSB) == False:
            return 1
        elif get_currency(IAF1040.SpPenExcl) == 0 and get_bool(IAF1040.NoSpPenExcl) == False:
            return 1
        elif get_currency(IAF1040.SpTaxInc) == 0 and get_bool(IAF1040.NoSpTaxInc) == False:
            return 1
        else:
            return 0
    else:
        return 0

def Alert60_Calculation():
    if get_currency(IAREQUIRED.IAEic) > 0:
        if get_bool(IAF1040.NoMFSEI) == True:
            return 0
        elif get_bool(IAF1040.MFS) == True and get_currency(IAF1040.MFSEI) == 0:
            return 1
        else:
            return 0
    else:
        return 0

def Alert70_Calculation():
    return 0

def Alert80_Calculation():
    #Re-did to factor in prior year 179 assets and use IAStatePrior. Does trigger for any year with bonus.  Next year 2019 need to alert non conformity assets that are disposed? Not this year since should only be current year assets.
    return get_number(IAWDepr.StatePriorDisposal)

def Alert90_Calculation():
    #for 2018 make no change since need to ask or alert if had depr adjustment in prior year and need to make an entry for catch-up depr. May need to see next year if should exclude 2018 veh that were not reported on IA4562A since was just on IA 2106
    if get_bool(IAREQUIRED.Ask4562A) == True:
        if get_currency(IA4562A.TotP2ColF) == 0:
            return 1
        else:
            return 0
    else:
        return 0

def Alert340_Calculation():
    #set this to zero if Iowa passes conformity
    #return get_number(USWSpouse.StateSec179Tent) fed calc for this is below, do similar but with IA fields
    #If get_currency(USW4562State.TotElect179) <> get_currency(USW4562State.Tent179) Then
    #    return 1
    #Else
    #    return 0
    #End If
    if get_currency(IAREQUIRED.TotElect179) != get_currency(IAREQUIRED.Tent179):
        return 1
    else:
        return 0

def Alert345_Calculation():
    if get_currency(IAREQUIRED.Diss179) > 0:
        return 1
    else:
        return 0

def Alert350_Calculation():
    if get_currency(IA1040X.TotPrevTax) > Decimal("0") and  ( get_currency(IA1040X.TotPrevTax) == get_currency(IA1040X.PrevOP) ) :
        return 1
    else:
        return 0

def Alert360_Calculation():
    if get_bool(IAREQUIRED.VerifiedIA126) == True:
        return 0
    elif get_number(IAF126.Print) == 1:
        return 1
    else:
        return 0

def Ask130Copy_Calculation():
    if get_bool(IAREQUIRED.F130Y) == True and get_number(IA130.Exist) > 0:
        return 1
    else:
        return 0

def Ask134_Calculation():
    if get_number(IA134.Exist) > 0:
        return 1
    elif get_bool(IAF1040.CombMFS) == True and get_number(IA134SP.Exist) > 0:
        return 1
    else:
        return 0

def Ask4136_Calculation():
    if get_bool(USF4136.Exist) == True or get_number(USSchF.Exist) > 0 or get_number(USSchC.Exist) > 0:
        return 1
    else:
        return 0

def Ask4562A_Calculation():
    if get_number(IA4562A.StateDispNbr) > 0:
        return 1
    else:
        return 0

def Ask4562PIV_Calculation():
    if get_number(USDPartK1.Exist) > 0 or get_number(USDSCorpK1.Exist) > 0:
        return 1
    elif get_number(IA4562PIV.Exist) > 0:
        return 1
    else:
        return 0

def AskCharCont_Calculation():
    FedContributions = Currency()
    if get_bool(USWResidency.F1040NR) == False:
        FedContributions = get_currency(USSchA.Cash) + get_currency(USSchA.NonCash)
    else:
        FedContributions = get_currency(USSchANR.Cash) + get_currency(USSchANR.NonCash)
    if FedContributions > 0:
        if get_currency(IAF1040.BOthIACr) > 0 or get_currency(IAF1040.AOthIACr) > 0:
            return 1
        elif get_currency(IAOTHADJ.TPVet) > 0 or get_currency(IAOTHADJ.SPVet) > 0:
            return 1
        else:
            return 0
    else:
        return 0

def AskEarlyChCr_Calculation():
    if trim(get_string(IACHILDCREDIT.DepName(0))) != '' and get_currency(IACHILDCREDIT.TotNI) < Decimal("45000"):
        return 1
    else:
        return 0

def AskEstCopy_Calculation():
    if get_bool(IAREQUIRED.EstY) == True and get_number(IAESTIMATES.Exist) > 0:
        return 1
    else:
        return 0

def AskFedFuel_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        if get_currency(USF4136.TotalCredit) > 0 or get_currency(IAADDFEDTAX.SPFuel) > 0:
            return 1
        else:
            return 0
    else:
        return 0

def AskFilStat_Calculation():
    if IAFS() == 2 or IAFS() == 3 or IAFS() == 4:
        return 1
    else:
        return 0

def AskIAEst_Calculation():
    if get_bool(IAF1040.CombMFS) == True and get_currency(IASTATEEST.TotIAEst) > 0:
        return 1
    else:
        return 0

def AskMedExp_Calculation():
    if get_currency(USSchA.MedExp) > 0:
        if get_currency(IAF1040.BHealth) > 0 or get_currency(IAF1040.AHealth) > 0:
            return 1
        else:
            return 0
    else:
        return 0

def AskPenExc_Calculation():
    if get_currency(IAF1040.AIRA) + get_currency(IAF1040.APensions) + get_currency(IAF1040.BIRA) + get_currency(IAF1040.BPensions) + get_currency(IAF126.AIRA) + get_currency(IAF126.APensions) + get_currency(IAF126.BIRA) + get_currency(IAF126.BPensions) != 0:
        return 1
    else:
        return 0

def AskPensions_Calculation():
    if get_currency(USWRec.TotPension) > 0:
        return 1
    elif get_currency(IAWPENEXC.TPPensions) + get_currency(IAWPENEXC.SPPensions) != 0:
        return 1
    else:
        return 0

def AskReviewOthAdj_Calculation():
    if GetStatusCopies(IAWHEALTH, ModifiedStatus) > 0:
        return 1
    elif GetStatusCopies(IAWPENEXC, ModifiedStatus) > 0:
        return 1
    elif get_currency(IAF1040.AGainDed) > 0 or get_currency(IAF1040.BGainDed) > 0:
        return 1
    elif GetStatusCopies(IAOTHADJ, ModifiedStatus) > 0:
        return 1
    else:
        return 0

def BalDueAmt_Calculation():
    return Abs(get_currency(IAF1040.RefBalDue))

def BaseAmt_Calculation():
    if get_bool(IAF1040.Over65) == True:
        return Decimal("24000")
    else:
        return Decimal("9000")

def BProRate_Calculation():
    if IAFS() == 3:
        if get_currency(IAF1040.BNet) < 0 and get_currency(IAF1040.ANet) < 0:
            if get_currency(IAF1040.BNet) < get_currency(IAF1040.ANet):
                return 0
            else:
                return 1
        elif get_currency(IAF1040.BNet) < 0:
            return 0
        elif get_currency(IAF1040.BNet) > 0 and get_currency(IAREQUIRED.TotNI) <= 0:
            return 1
        elif get_currency(IAREQUIRED.TotNI) == 0:
            return 0
        else:
            return max_value(0, ( min_value(1, get_float(IAF1040.BNet) / get_float(IAREQUIRED.TotNI)) ))
    else:
        return 0

def BusInc179_Calculation():
    return max_value(0, get_currency(IAREQUIRED.FedLn11) + get_currency(IAREQUIRED.IABusinessNC))

def CombNames_Calculation():
    if get_bool(IAF1040.MFJ) == True or get_bool(IAF1040.CombMFS) == True:
        if get_string(IAF1040.LastName) == get_string(IAF1040.SpouseLast):
            return get_string(IAF1040.FirstName) + ' and ' + get_string(IAF1040.SpouseFirst) + ' ' + get_string(IAF1040.LastName)
        else:
            return get_string(IAF1040.FirstName) + ' ' + get_string(IAF1040.LastName) + ' and ' + get_string(IAF1040.SpouseFirst) + ' ' + get_string(IAF1040.SpouseLast)
    else:
        return get_string(IAF1040.FirstName) + ' ' + get_string(IAF1040.LastName)

def CrAddFedTax_Calculation():
    if get_number(USWFICA.Exist) > 0:
        return 1
    elif get_number(USF4136.Exist) > 0:
        return 1
    elif get_currency(USWRec.PYOwe) > 0:
        return 1
    elif get_currency(USWRec.PYOweNR) > 0:
        return 1
    elif get_currency(USWRec.PYExt) > 0:
        return 1
    elif get_currency(USWRec.PYExtNR) > 0:
        return 1
    else:
        return 0

def CrOthAdj_Calculation():
    if get_number(USWOthAdj.Exist) > 0:
        return 1
    elif get_number(USWOthAdjNR.Exist) > 0:
        return 1
    elif get_number(USWOthInc.Exist) > 0:
        return 1
    elif get_number(USWOthIncNR.Exist) > 0:
        return 1
    elif get_bool(USF8910.Print) == True:
        return 1
    elif get_currency(USWRec.TotEdExp) > 0:
        return 1
    elif get_currency(USWRec.TotBusExp2106) > 0:
        return 1
    elif get_currency(USWRec.TotStudAdj) > 0:
        return 1
    elif get_currency(USWRec.TotTuitAdj) > 0:
        return 1
    elif get_currency(USWRec.TotHealthSav) > 0:
        return 1
    elif get_currency(USWRec.TotDomProd) > 0:
        return 1
        # Need to create if PYNR so interview displays correctly for IA 126 worksheets
    elif get_bool(IAF126.TpPYNR) == True or get_bool(IAF126.SpPYNR) == True:
        return 1
    else:
        return 0

def CrOthInc_Calculation():
    if get_number(USWOthInc.Exist) > 0:
        return 1
    elif get_number(USWOthIncNR.Exist) > 0:
        return 1
    elif get_currency(IA4562.TotDepAdj) != 0:
        return 1
    elif get_currency(IA4562SP.TotDepAdj) != 0:
        return 1
    elif get_currency(IA4562A.TotDepAdj) != 0:
        return 1
    elif get_currency(USF6251.Depl) != 0:
        return 1
    elif get_currency(USF6251.IntangDrill) != 0:
        return 1
        # Need to create if PYNR so interview displays correctly for IA 126 worksheets
    elif get_bool(IAF126.TpPYNR) == True or get_bool(IAF126.SpPYNR) == True:
        return 1
    elif get_currency(IAREQUIRED.Tot8824) != 0:
        return 1
    elif get_currency(IAREQUIRED.TotIAExReimb) != 0:
        return 1
    elif get_currency(IAWNONCONFORMADJ.SPTotNonConformAdj) != 0 or get_currency(IAWNONCONFORMADJ.TPTotNonConformAdj) != 0:
        return 1
    elif get_currency(IA4684.IANonConformAdj) != 0:
        return 1
    elif get_currency(IA2106.IAWages) != 0:
        return 1
    elif get_currency(IAWSchFLoss.ExcessLoss) != 0:
        return 1
    else:
        return 0

def CrPenExc_Calculation():
    if get_currency(USWRec.TotIRAInc) != 0:
        return 1
    elif get_currency(USWRetirement.TPAddQCD) != 0:
        return 1
    elif get_currency(USWRetirement.SPAddQCD) != 0:
        return 1
    elif get_currency(USWRec.TotPension) != 0:
        return 1
    else:
        return 0

def CrSETax_Calculation():
    if get_currency(USF8962.PTCRepay) != 0:
        return 1
    elif get_currency(USF1040.SETax) != 0:
        return 1
    elif get_currency(USF1040NR.SETax) != 0:
        return 1
    elif get_currency(USF1040.TipTax) != 0:
        return 1
    elif get_currency(USF1040NR.TipTax) != 0:
        return 1
    elif get_currency(USWRetirement.RetTax) != 0:
        return 1
    elif get_currency(USF1040.SchHTax) != 0:
        return 1
    elif get_currency(USF1040NR.SchHTax) != 0:
        return 1
    elif get_currency(USF1040.HomeBuyRepay) != 0:
        return 1
    elif get_currency(USF1040NR.HomeBuyRepay) != 0:
        return 1
    elif get_currency(USWHealthPen.Penalty) != 0:
        return 1
    elif get_currency(USF8959.TotAddMedTax) != 0:
        return 1
    elif get_currency(USWOthTax.TotOthTax) != 0:
        return 1
    else:
        return 0

def CurrentDate_Calculation():
    return CDate('Current')

def Ded179_Calculation():
    return min_value(get_currency(IAREQUIRED.BusInc179), get_currency(IAREQUIRED.Tent179) + get_currency(IAREQUIRED.TotCo179))

def DepLength_Calculation():
    return Len(get_string(IAREQUIRED.DepNames))

def DepNames_Calculation():
    DepName = String()
    if get_string(USWAddDep.DepFName(0)) != '':
        DepName = get_string(USWAddDep.DepFName(0)) + ' '
    if get_string(USWAddDep.DepFName(1)) != '':
        DepName = DepName + get_string(USWAddDep.DepFName(1)) + ' '
    if get_string(USWAddDep.DepFName(2)) != '':
        DepName = DepName + get_string(USWAddDep.DepFName(2)) + ' '
    if get_string(USWAddDep.DepFName(3)) != '':
        DepName = DepName + get_string(USWAddDep.DepFName(3)) + ' '
    if get_string(USWAddDep.DepFName(4)) != '':
        DepName = DepName + get_string(USWAddDep.DepFName(4)) + ' '
    if get_string(USWAddDep.DepFName(5)) != '':
        DepName = DepName + get_string(USWAddDep.DepFName(5)) + ' '
    return DepName

def DeprAdj_Calculation():
    return get_currency(IAWOTHINC.TotBonus)

def Diss179_Calculation():
    return get_currency(IAREQUIRED.TotCo179) + get_currency(IAREQUIRED.Tent179) - get_currency(IAREQUIRED.Ded179)

def EICRatio_Calculation():
    if get_currency(IAREQUIRED.TotEICEarnInc) == 0:
        return 0
    elif get_currency(IAREQUIRED.SEICEarnInc) < 0:
        return 0
    else:
        return min_value(1, max_value(0, get_float(IAREQUIRED.SEICEarnInc) / get_float(IAREQUIRED.TotEICEarnInc)))

def FedAGI_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USF1040.AGI)
    else:
        return get_currency(USF1040NR.AGI)

def FedFilingStatus_Calculation():
    if FedFS() == 1:
        return 'single'
    elif FedFS() == 2:
        return 'married filing jointly'
    elif FedFS() == 3:
        return 'married filing separately'
    elif FedFS() == 4:
        return 'head of household'
    else:
        return 'qualifying widow(er)'

def FedLn11_Calculation():
    return get_currency(USF4562.BusInc179, 1)

def FilingStatus_Calculation():
    return IAFS()

def FYEIC_Calculation():
    return c_dollar(get_float(USF1040.Eic) * 0.15)

def FYRes_Calculation():
    Only1NR = Long()

    TPRes = Long()

    SPRes = Long()
    if get_bool(IAF126.TpNonRes) == True and get_bool(IAF126.SpRes) == True:
        Only1NR = 1
    elif get_bool(IAF126.TpRes) == True and get_bool(IAF126.SpNonRes) == True:
        Only1NR = 1
    else:
        Only1NR = 0
    if get_bool(IAF126.Exist) == False:
        TPRes = 1
    elif get_bool(IAF1040.MFJ) == True and Only1NR == 1:
        TPRes = 1
    elif get_bool(IAF1040.MFJ) == True and get_bool(IAF126.TpRes) == True and get_bool(IAF126.SpRes) == True:
        TPRes = 1
    elif get_bool(IAF1040.MFJ) != True and get_bool(IAF126.TpRes) == True:
        TPRes = 1
    else:
        TPRes = 0
    if get_bool(IAF1040.CombMFS) == True:
        if get_bool(IAF126.Exist) == False:
            SPRes = 1
        elif get_bool(IAF126.SpRes) == True:
            SPRes = 1
        else:
            SPRes = 0
    else:
        SPRes = 0
    if get_bool(IAF1040.CombMFS) == True:
        if TPRes + SPRes == 2:
            return 1
        else:
            return 0
    elif TPRes == 1:
        return 1
    else:
        return 0

def IAAGI_Calculation():
    return get_currency(IAREQUIRED.FedAGI) + get_currency(IAREQUIRED.DeprAdj) + get_currency(IAREQUIRED.NonConfLn14) - get_currency(IAREQUIRED.NCMove) - get_currency(IAREQUIRED.NCDomProd)

def IABusinessNC_Calculation():
    return get_currency(IAWOTHINC.TotNonConform)

def IAEic_Calculation():
    if get_bool(IAF126.TpPYNR) == True or get_bool(IAF126.SpPYNR):
        return get_currency(IAREQUIRED.PYNREIC)
    else:
        return get_currency(IAREQUIRED.FYEIC)

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
        if get_bool(IASCHB.DJ1(count)) == True:
            SchBTotal = SchBTotal + get_currency(IASCHB.TaxDiv(count))
        else:
            SchBTotal = SchBTotal
        count = count + 1
    count1 = 1
    HowManyWBPDiv = GetAllCopies(IAWBPDIV)
    WSTotal = 0
    while count1 <= HowManyWBPDiv:
        DivIndex = 0
        while DivIndex < 22:
            if get_bool(IAWBPDIV.DJ1(DivIndex), count1) == True:
                WSTotal = WSTotal + get_currency(IAWBPDIV.TaxDiv(DivIndex), count1)
            DivIndex = DivIndex + 1
        count1 = count1 + 1
    return SchBTotal + WSTotal

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
        if get_bool(IASCHB.IJ1(count)) == True:
            SchBTotal = SchBTotal + get_currency(IASCHB.TaxInt(count))
        else:
            SchBTotal = SchBTotal
        count = count + 1
    count1 = 1
    HowManyWBPInt = GetAllCopies(IAWBPINT)
    WSTotal = 0
    while count1 <= HowManyWBPInt:
        IntIndex = 0
        while IntIndex < 22:
            if get_bool(IAWBPINT.IJ1(IntIndex), count1) == True:
                WSTotal = WSTotal + get_currency(IAWBPINT.TaxInt(IntIndex), count1)
            IntIndex = IntIndex + 1
        count1 = count1 + 1
    return SchBTotal + WSTotal

def JointSPDiv_Calculation():
    return Round(c_dollar(CDbl(get_currency(IAREQUIRED.JointDiv)) * 0.5))

def JointSPInt_Calculation():
    return Round(c_dollar(CDbl(get_currency(IAREQUIRED.JointInt)) * 0.5))

def JointTPDiv_Calculation():
    return get_currency(IAREQUIRED.JointDiv) - get_currency(IAREQUIRED.JointSPDiv)

def JointTPInt_Calculation():
    return get_currency(IAREQUIRED.JointInt) - get_currency(IAREQUIRED.JointSPInt)

def JTComb_Calculation():
    if get_string(IAF1040.LastName) == get_string(IAF1040.SpouseLast):
        return get_string(IAF1040.LastName) + ', ' + get_string(IAF1040.FirstName) + ' and ' + get_string(IAF1040.SpouseFirst)
    else:
        return get_string(IAF1040.LastName) + ', ' + get_string(IAF1040.FirstName) + ' and ' + get_string(IAF1040.SpouseLast) + ', ' + get_string(IAF1040.SpouseFirst)

def LILimit_Calculation():
    if IAFS() == 1 and get_bool(IAF1040.DepY) == True:
        return Decimal("5000")
    elif IAFS() == 1 and get_bool(IAF1040.DepY) == False and get_bool(IAF1040.Over65) == True:
        return Decimal("24001")
    elif IAFS() == 1 and get_bool(IAF1040.DepY) == False:
        return Decimal("9001")
    elif IAFS() == 1 or get_bool(IAF1040.DepY) == True:
        return Decimal("0")
    elif get_bool(IAF1040.Over65) == True:
        return Decimal("32001")
    else:
        return Decimal("13501")

def Limit179_Calculation():
    return max_value(0, get_currency(IAREQUIRED.Max179) - get_currency(IAREQUIRED.Reduction179))

def LITotIncome_Calculation():
    return get_currency(IAWKALTTAX.Ln26)

def LowInc_Calculation():
    if get_currency(USF4972.Tax) + get_currency(USF4972SPOUSE.Tax) > 0:
        return 0
    elif get_currency(IAF1040.AIAMin) > 0 or get_currency(IAF1040.BIAMin) > 0:
        return 0
    elif get_bool(IAF126.TpPYNR) == True or get_bool(IAF126.SpPYNR) == True:
        return 0
    elif get_bool(IAREQUIRED.AskFilStat) == True and get_bool(IAWKALTTAX.NOL) == True:
        return 0
    elif get_currency(IAREQUIRED.LITotIncome) < get_currency(IAREQUIRED.LILimit):
        return 1
    else:
        return 0

def Max179_Calculation():
    return Decimal("70000")

def MobDisQual_Calculation():
    return 0

def ModAmt_Calculation():
    TP = Currency()

    SP = Currency()
    TP = get_currency(IAF1040.ATotAdj) - get_currency(IAF1040.AFedTax) + get_currency(IAF1040.AFedDed) + get_currency(IAF1040.ADedBox)
    SP = get_currency(IAF1040.BTotAdj) - get_currency(IAF1040.BFedTax) + get_currency(IAF1040.BFedDed) + get_currency(IAF1040.BDedBox)
    return TP + SP

def ModChg_Calculation():
    return Abs(get_currency(IAREQUIRED.TotIncChg) - get_currency(IAF1040.AAltTax))

def ModCk_Calculation():
    Tax = Currency()

    Modifications = Currency()
    Tax = get_currency(IAF1040.AAltTax)
    Modifications = get_currency(IAREQUIRED.TotIncChg) - Tax
    if Modifications > 0:
        return 1
    else:
        return 0

def Names_Calculation():
    return get_string(IAREQUIRED.CombNames)

def NCDomProd_Calculation():
    return max_value(0, get_currency(IAOTHADJ.TPDomProd) + get_currency(IAOTHADJ.SPDomProd) - get_currency(USF8903.DPADeduction))

def NCMove_Calculation():
    return get_currency(IA3903.MovExpDdn)

def NonConfLn14_Calculation():
    return get_currency(IAWOTHINC.TotNonConform)

def NonCredAmt_Calculation():
    TP = Currency()

    SP = Currency()
    TP = get_currency(IAF1040.ACredits) + get_currency(IAF1040.ACrNon) + get_currency(IAF1040.AOutState) + get_currency(IAF1040.AOthIACr)
    SP = get_currency(IAF1040.BCredits) + get_currency(IAF1040.BCrNon) + get_currency(IAF1040.BOutState) + get_currency(IAF1040.BOthIACr)
    return TP + SP

def NonCredChg_Calculation():
    return get_currency(IAREQUIRED.NonCredAmt)

def NonCredCk_Calculation():
    if get_currency(IAREQUIRED.NonCredChg) > 0:
        return 1
    else:
        return 0

def OthTaxAmt_Calculation():
    TP = Currency()

    SP = Currency()
    TP = get_currency(IAF1040.ALump) + get_currency(IAF1040.AIAMin) + get_currency(IAF1040.ASch)
    TP = get_currency(IAF1040.BLump) + get_currency(IAF1040.BIAMin) + get_currency(IAF1040.BSch)
    return TP + SP + get_currency(IAF1040.TotContrib)

def OthTaxChg_Calculation():
    return get_currency(IAREQUIRED.OthTaxAmt)

def OthTaxCk_Calculation():
    if get_currency(IAREQUIRED.OthTaxChg) > 0:
        return 1
    else:
        return 0

def PayAmt_Calculation():
    return get_currency(IAF1040.TotCredit)

def PayChg_Calculation():
    return get_currency(IAREQUIRED.PayAmt)

def PayCk_Calculation():
    if get_currency(IAREQUIRED.PayChg) > 0:
        return 1
    else:
        return 0

def PenDonAmt_Calculation():
    return get_currency(IAF1040.BApply99) + get_currency(IAF1040.AApply99) + get_currency(IAF1040.Penalty) + get_currency(IAF1040.PenInt)

def PenDonChg_Calculation():
    return get_currency(IAREQUIRED.PenDonAmt)

def PenDonCk_Calculation():
    if get_currency(IAREQUIRED.PenDonChg) > 0:
        return 1
    else:
        return 0

def PrnSchCode_Calculation():
    if get_string(IAF1040.SchNo) == '00811':
        return '0081'
    elif get_string(IAF1040.SchNo) == '44911':
        return '4491'
    elif get_string(IAF1040.SchNo) == '45181':
        return '4518'
    elif get_string(IAF1040.SchNo) == '58951':
        return '5895'
    else:
        return get_string(IAF1040.SchNo)

def PrnSurvivorSP_Calculation():
    if get_string(USWTaxpayer.PrnSurvivorSP) == 'File as Surviving Sp.':
        return get_string(USWTaxpayer.PrnSurvivorSP) + ' ' + get_string(USWBasicInfo.YouDeath)
    else:
        return get_string(USWTaxpayer.PrnSurvivorSP)

def PrnSurvivorTP_Calculation():
    if get_string(USWTaxpayer.PrnSurvivorTP) == 'File as Surviving Sp.':
        return get_string(USWTaxpayer.PrnSurvivorTP)
    else:
        return get_string(USWTaxpayer.PrnSurvivorTP)

def PYNetInc_Calculation():
    return get_currency(IAREQUIRED.PYNetIncA) + get_currency(IAREQUIRED.PYNetIncB)

def PYNetIncA_Calculation():
    return get_currency(USZIA1040.IAPYNetIncA)

def PYNetIncB_Calculation():
    return get_currency(USZIA1040.IAPYNetIncB)

def PYNREIC_Calculation():
    return min_value(get_currency(IAREQUIRED.FYEIC), ( c_dollar(get_float(IAREQUIRED.FYEIC) * get_float(IACHILDCREDIT.PYNRPercent)) ))

def PYRatio_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == False:
        return 0
    elif get_currency(IAREQUIRED.PYNetIncB) < 0 and get_currency(IAREQUIRED.PYNetIncA) < 0:
        if get_currency(IAREQUIRED.PYNetIncB) < get_currency(IAREQUIRED.PYNetIncA):
            return 0
        else:
            return 1
    elif get_currency(IAREQUIRED.PYNetIncB) < 0:
        return 0
    elif get_currency(IAREQUIRED.PYNetIncB) > 0 and get_currency(IAREQUIRED.PYNetInc) <= 0:
        return 1
    elif get_currency(IAREQUIRED.PYNetInc) == 0:
        return 0
    else:
        return max_value(0, ( min_value(1, get_float(IAREQUIRED.PYNetIncB) / get_float(IAREQUIRED.PYNetInc)) ))

def QnACompMob_Calculation():
    if get_bool(IAREQUIRED.QnAComp) == True:
        return 1
    else:
        return 0

def QSAmtOwe_Calculation():
    if get_currency(IAF1040.RefBalDue) < 0:
        return Abs(get_currency(IAF1040.RefBalDue))
    else:
        return 0

def QSRefund_Calculation():
    if get_currency(IAF1040.RefBalDue) > 0:
        return get_currency(IAF1040.RefBalDue)
    else:
        return 0

def Reduction179_Calculation():
    return max_value(0, get_currency(IAREQUIRED.TotCost179) - get_currency(IAREQUIRED.Threshold179))

def RefundAmt_Calculation():
    return get_currency(IAF1040.RefBalDue)

def RefundCk_Calculation():
    if get_currency(IAREQUIRED.RefundAmt) > 0:
        return 1
    else:
        return 0

def S1099RWH_Calculation():
    count1 = Integer()

    HowMany1099R = Long()

    Total1 = Currency()
    count1 = 1
    HowMany1099R = GetAllCopies(USD1099R)
    Total1 = 0
    while count1 <= HowMany1099R:
        if get_string(USD1099R.St1, count1) == 'IA' and get_bool(USD1099R.Spouse, count1) == True:
            Total1 = Total1 + get_currency(USD1099R.StWh1, count1)
        if get_string(USD1099R.St2, count1) == 'IA' and get_bool(USD1099R.Spouse, count1) == True:
            Total1 = Total1 + get_currency(USD1099R.STWh2, count1)
        count1 = count1 + 1
    return Round(Total1)

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
        if get_string(IAWDepr.ParentType, count) == '2106' and get_bool(IAWDepr.Qualifies, count) == True:
            Total1 = Total1 + get_currency(IAWDepr.TotAdj, count)
        count = count + 1
    while count3 <= HowManyIA4562A:
        if get_string(IA4562A.EmpBusType, count3) == '27':
            Total3 = Total3 + get_currency(IA4562A.DepAdj, count3)
        count3 = count3 + 1
    return Total1 + Total3

def SchBDivNoPayer_Calculation():
    count = Variant()

    Iter = Integer()
    count = 0
    Iter = 0
    while Iter < 7:
        if get_currency(IASCHB.Dividend(Iter)) > 0 and trim(get_string(IASCHB.DivPayer(Iter))) == '':
            count = count + 1
        Iter = Iter + 1
    if get_bool(IASCHB.PrintIAB) == True and count > 0:
        return 1
    else:
        return 0

def SchBIntNoPayer_Calculation():
    count = Variant()

    Iter = Integer()
    count = 0
    Iter = 0
    while Iter < 7:
        if get_currency(IASCHB.Interest(Iter)) > 0 and trim(get_string(IASCHB.Payer(Iter))) == '':
            count = count + 1
        Iter = Iter + 1
    if get_bool(IASCHB.PrintIAB) == True and count > 0:
        return 1
    else:
        return 0

def SEarnInc_Calculation():
    Part = Currency()

    SE = Currency()

    Wages = Currency()

    NonTaxCombat = Currency()

    SP409AInc = Currency()

    JtSP409AInc = Currency()
    Part = get_currency(USDPartK1.SEInc, FieldCopies(USDPartK1.Spouse)) + c_dollar(get_float(USDPartK1.SEInc, FieldCopies(USDPartK1.Joint)) * 0.5)
    SE = get_currency(IAF1040.BBusInc) + get_currency(IAF1040.BFarm) - get_currency(IAF1040.BBusIncL) - get_currency(USWRec.SKeough)
    Wages = max_value(0, get_currency(IAF1040.BWages) - get_currency(USDStudent.TaxScholar, FieldCopies(USDStudent.Spouse)) - Round(get_currency(USDW2.NonQual, FieldCopies(USDW2.Spouse))) - Round(get_currency(USDW2AS.NonQual, FieldCopies(USDW2AS.Spouse))) - Round(get_currency(USDW2CM.NonQual, FieldCopies(USDW2CM.Spouse))) - Round(get_currency(USDW2GU.NonQual, FieldCopies(USDW2GU.Spouse))) - Round(get_currency(USDW2VI.NonQual, FieldCopies(USDW2VI.Spouse))))
    NonTaxCombat = Round(get_currency(USDW2.CodeQ, FieldCopies(USDW2.Spouse))) + Round(get_currency(USDW2AS.CodeQ, FieldCopies(USDW2AS.Spouse))) + Round(get_currency(USDW2CM.CodeQ, FieldCopies(USDW2CM.Spouse))) + Round(get_currency(USDW2GU.CodeQ, FieldCopies(USDW2GU.Spouse))) + Round(get_currency(USDW2VI.CodeQ, FieldCopies(USDW2VI.Spouse)))
    SP409AInc = Round(get_currency(USDW2.CodeZ, FieldCopies(USDW2.Spouse))) + Round(get_currency(USDW2AS.CodeZ, FieldCopies(USDW2AS.Spouse))) + Round(get_currency(USDW2CM.CodeZ, FieldCopies(USDW2CM.Spouse))) + Round(get_currency(USDW2GU.CodeZ, FieldCopies(USDW2GU.Spouse))) + Round(get_currency(USDW2VI.CodeZ, FieldCopies(USDW2VI.Spouse))) + Round(get_currency(USD1099MISC.Income, FieldCopies(USD1099MISC.Spouse)))
    JtSP409AInc = Round(c_dollar(get_float(USD1099MISC.Income, FieldCopies(USD1099MISC.Joint)) * 0.5))
    return max_value(0, Wages + get_currency(IAF1040.BAlimony) + max_value(0, SE + Part) + get_currency(USWOthInc.SP2555) + NonTaxCombat - SP409AInc - JtSP409AInc)

def SEICEarnInc_Calculation():
    if get_bool(IAF1040.MFS) == True:
        return get_currency(IAF1040.MFSEI)
    else:
        return get_currency(IAF1040.BWages) + get_currency(IAF1040.BBusInc) + get_currency(IAF1040.BFarm)

def ShowRef_Calculation():
    if get_currency(IAREQUIRED.QSAmtOwe) > 0:
        return 0
    else:
        return 1

def SIaEIC_Calculation():
    return c_dollar(get_float(IAREQUIRED.IAEic) * get_float(IAREQUIRED.EICRatio))

def SIAExReimb_Calculation():
    return get_currency(IAREQUIRED.TotIAExReimb) - get_currency(IAREQUIRED.TIAExReimb)

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
            if get_string(USDW2.St(W2Index), count1) == 'IA' and get_bool(USDW2.Spouse, count1) == True:
                Total1 = Total1 + get_currency(USDW2.STWh(W2Index), count1)
            W2Index = W2Index + 1
        count1 = count1 + 1
    return Round(Total1)

def SIRA_Calculation():
    if IAFS() == 3:
        if get_currency(IAREQUIRED.TEarnInc) < get_currency(USWIRA.TPDedIRA):
            return get_currency(USWIRA.TPDedIRA) + get_currency(USWIRA.SPDedIRA) - get_currency(IAREQUIRED.TEarnInc)
        else:
            return min_value(get_currency(IAREQUIRED.SEarnInc), get_currency(USWIRA.SPDedIRA))
    else:
        return 0

def AskSpouse_Calculation():
    if IAFS() == 2 or IAFS() == 3:
        return 1
    else:
        return 0

def SLimLoss_Calculation():
    return get_currency(USWDRec.LimLoss) - get_currency(IAREQUIRED.TLimLoss)

def SMove_Calculation():
    return get_currency(IAREQUIRED.TotMove) - get_currency(IAREQUIRED.TMove)

def SP8824_Calculation():
    return get_currency(IAREQUIRED.Tot8824) - get_currency(IAREQUIRED.TP8824)

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
            if get_string(USDCapGain.St2(CGIndex), count1) == 'IA' and get_bool(USDCapGain.Spouse, count1) == True:
                Total1 = Total1 + get_currency(USDCapGain.STWh2(CGIndex), count1)
            elif get_string(USDCapGain.St2(CGIndex), count1) == 'IA' and get_bool(USDCapGain.Joint, count1) == True:
                Total1 = Total1 + c_dollar(get_float(USDCapGain.STWh2(CGIndex), count1) * 0.5)
            CGIndex = CGIndex + 1
        count1 = count1 + 1
    return Round(Total1)

def SPComb_Calculation():
    if get_bool(IAF1040.MFJ) == True or get_bool(IAF1040.CombMFS) == True:
        return get_string(IAF1040.SpouseLast) + ', ' + get_string(IAF1040.SpouseFirst)
    else:
        return ''

def SPCombName_Calculation():
    if get_bool(IAF1040.MFJ) == True or get_bool(IAF1040.CombMFS) == True:
        return get_string(IAF1040.SpouseFirst) + ' ' + get_string(IAF1040.SpouseLast)
    else:
        return ''

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
            if get_string(USD1099DIV.St(DivIndex), count1) == 'IA' and get_bool(USD1099DIV.Spouse, count1) == True:
                Total1 = Total1 + get_currency(USD1099DIV.STWh(DivIndex), count1)
            elif get_string(USD1099DIV.St(DivIndex), count1) == 'IA' and get_bool(USD1099DIV.Joint, count1) == True:
                Total1 = Total1 + c_dollar(get_float(USD1099DIV.STWh(DivIndex), count1) * 0.5)
            DivIndex = DivIndex + 1
        count1 = count1 + 1
    return Round(Total1)

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
            if get_string(USD1099INT.St(IntIndex), count1) == 'IA' and get_bool(USD1099INT.Spouse, count1) == True:
                Total1 = Total1 + get_currency(USD1099INT.STWh(IntIndex), count1)
            elif get_string(USD1099INT.St(IntIndex), count1) == 'IA' and get_bool(USD1099INT.Joint, count1) == True:
                Total1 = Total1 + c_dollar(get_float(USD1099INT.STWh(IntIndex), count1) * 0.5)
            IntIndex = IntIndex + 1
        count1 = count1 + 1
    return Round(Total1)

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
            if get_string(USD1099K.State(KIndex), count1) == 'IA' and get_bool(USD1099K.Spouse, count1) == True:
                Total1 = Total1 + get_currency(USD1099K.StateInc(KIndex), count1)
            elif get_string(USD1099K.State(KIndex), count1) == 'IA' and get_bool(USD1099K.Joint, count1) == True:
                Total1 = Total1 + c_dollar(get_float(USD1099K.StateInc(KIndex), count1) * 0.5)
            KIndex = KIndex + 1
        count1 = count1 + 1
    return Round(Total1)

def SPMiscWH_Calculation():
    count1 = Integer()

    HowMany1099MISC = Long()

    Total1 = Currency()
    count1 = 1
    HowMany1099MISC = GetAllCopies(USD1099MISC)
    Total1 = 0
    while count1 <= HowMany1099MISC:
        if get_string(USD1099MISC.State, count1) == 'IA':
            if get_bool(USD1099MISC.Spouse, count1) == True:
                Total1 = Total1 + get_currency(USD1099MISC.StateWH, count1)
            elif get_bool(USD1099MISC.Joint, count1) == True:
                Total1 = Total1 + c_dollar(get_float(USD1099MISC.StateWH, count1) * 0.5)
            else:
                Total1 = Total1
        else:
            Total1 = Total1
        if get_string(USD1099MISC.State2, count1) == 'IA':
            if get_bool(USD1099MISC.Spouse, count1) == True:
                Total1 = Total1 + get_currency(USD1099MISC.StateWH2, count1)
            elif get_bool(USD1099MISC.Joint, count1) == True:
                Total1 = Total1 + c_dollar(get_float(USD1099MISC.StateWH2, count1) * 0.5)
            else:
                Total1 = Total1
        else:
            Total1 = Total1
        count1 = count1 + 1
    return Round(Total1)

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
            if get_string(USD1099OID.St(OIDIndex), count1) == 'IA' and get_bool(USD1099OID.Spouse, count1) == True:
                Total1 = Total1 + get_currency(USD1099OID.STWh(OIDIndex), count1)
            elif get_string(USD1099OID.St(OIDIndex), count1) == 'IA' and get_bool(USD1099OID.Joint, count1) == True:
                Total1 = Total1 + c_dollar(get_float(USD1099OID.STWh(OIDIndex), count1) * 0.5)
            OIDIndex = OIDIndex + 1
        count1 = count1 + 1
    return Round(Total1)

def SPOthIncWH_Calculation():
    return 0

def SPTotIncChg_Calculation():
    Mid = Currency()

    MidInt = Long()

    TotTaxInc = Currency()
    # updated for 2018
    TotTaxInc = get_currency(IAF1040.BGross)
    if TotTaxInc > Decimal("95650"):
        Mid = TotTaxInc
    elif TotTaxInc > Decimal("150"):
        MidInt = CLng(( TotTaxInc - Decimal("1") )  / Decimal("50"))
        Mid = ( CCur(MidInt) * Decimal("50") )  + Decimal("25")
    else:
        Mid = Decimal("0")
    return Tax(Mid)

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
            if get_string(USWUnempl.TPState(UnIndex), count1) == 'IA' and get_bool(USWUnempl.Spouse, count1) == True:
                Total1 = Total1 + get_currency(USWUnempl.TPStWH(UnIndex), count1)
            UnIndex = UnIndex + 1
        count1 = count1 + 1
    return Round(Total1)

def SPW2GWH_Calculation():
    count1 = Integer()

    HowManyW2G = Long()

    Total1 = Currency()
    count1 = 1
    HowManyW2G = GetAllCopies(USDW2G)
    Total1 = 0
    while count1 <= HowManyW2G:
        if get_string(USDW2G.StateWon, count1) == 'IA' and get_bool(USDW2G.Spouse, count1) == True:
            Total1 = Total1 + get_currency(USDW2G.StateWH, count1)
        count1 = count1 + 1
    return Round(Total1)

def SSN_Calculation():
    return get_string(IAF1040.SSN)

def SummaryScript_Calculation():
    if get_bool(IAF1040.CombMFS) == True:
        return 1
    else:
        return 0

def T1099rWH_Calculation():
    return get_currency(IAREQUIRED.Tot1099rWH) - get_currency(IAREQUIRED.S1099RWH)

def TaxReduction_Calculation():
    return min_value(get_currency(IAREQUIRED.TentTaxRed), get_currency(IAREQUIRED.TentTax))

def TEarnInc_Calculation():
    return max_value(0, get_currency(USWIRATrad.EarnInc) - get_currency(IAREQUIRED.SEarnInc))

def Tent179_Calculation():
    return min_value(get_currency(IAREQUIRED.TotElect179), get_currency(IAREQUIRED.Limit179))

def TentTax_Calculation():
    return max_value(0, get_currency(IAF1040.ATotIATax) - get_currency(IAF1040.ACredits))

def TentTaxRed_Calculation():
    return max_value(0, get_currency(IAREQUIRED.TotNIPenExc) - get_currency(IAREQUIRED.BaseAmt))

def Threshold179_Calculation():
    return Decimal("280000")

def TIAEic_Calculation():
    return max_value(0, get_currency(IAREQUIRED.IAEic) - get_currency(IAREQUIRED.SIaEIC))

def TIAExReimb_Calculation():
    return get_currency(IA3903.IAExReimb, FieldCopies(IA3903.Taxpayer)) + c_dollar(get_float(IA3903.IAExReimb, FieldCopies(IA3903.Joint)) * 0.5)

def TIAW2WH_Calculation():
    return get_currency(IAREQUIRED.TotIAW2WH) - get_currency(IAREQUIRED.SIAW2WH)

def TIRA_Calculation():
    return get_currency(IAREQUIRED.TotIRA) - get_currency(IAREQUIRED.SIRA)

def TLimLoss_Calculation():
    if get_currency(USWDRec.CapGain) < 0:
        if get_currency(USWDRec.TCapGain) < 0 and get_currency(USWDRec.SCapGain) < 0 and IAFS() == 3:
            if get_currency(USWDRec.SCapGain) < - Decimal("1500"):
                return max_value(get_currency(USWDRec.TCapGain), - Decimal("1500"))
            else:
                return get_currency(USWDRec.LimLoss) - get_currency(USWDRec.SCapGain)
        elif get_currency(USWDRec.TCapGain) < 0:
            return get_currency(USWDRec.LimLoss)
        else:
            return 0
    else:
        return 0

def TMove_Calculation():
    FedMove = Currency()

    StateMove = Currency()
    FedMove = get_currency(USWRec.TMove)
    StateMove = Round(get_currency(IA3903.MovExpDdn, FieldCopies(IA3903.Taxpayer)) + c_dollar(get_float(IA3903.MovExpDdn, FieldCopies(IA3903.Joint)) * 0.5))
    return FedMove + StateMove

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
            if get_string(USD1042S.St(F1042SIndex), count1) == 'IA':
                Total1 = Total1 + get_currency(USD1042S.StWh(F1042SIndex), count1)
            F1042SIndex = F1042SIndex + 1
        count1 = count1 + 1
    return Round(Total1)

def Tot1099rWH_Calculation():
    count1 = Integer()

    HowMany1099R = Long()

    Total1 = Currency()
    count1 = 1
    HowMany1099R = GetAllCopies(USD1099R)
    Total1 = 0
    while count1 <= HowMany1099R:
        if get_string(USD1099R.St1, count1) == 'IA':
            Total1 = Total1 + get_currency(USD1099R.StWh1, count1)
        if get_string(USD1099R.St2, count1) == 'IA':
            Total1 = Total1 + get_currency(USD1099R.STWh2, count1)
        count1 = count1 + 1
    return Round(Total1)

def Tot8824_Calculation():
    return get_currency(IA8824.IANonConformAdj)

def TotApplied_Calculation():
    return get_currency(IAF1040.AApply99) + get_currency(IAF1040.BApply99)

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
            if get_string(USDCapGain.St2(CGIndex), count1) == 'IA':
                Total1 = Total1 + get_currency(USDCapGain.STWh2(CGIndex), count1)
            CGIndex = CGIndex + 1
        count1 = count1 + 1
    return Round(Total1)

def TotCo179_Calculation():
    return 0

def TotCost179_Calculation():
    #per 2016 Section 179 Expensing FAQs under section III for pass through entities #4 example shows that the cost of section 179 property passed through for federal should not pass through to the partner for purposes of the Iowa section 179 phase-out limits, remove + get_currency(USDPartK1.Sec179) + get_currency(USDSCorpK1.Sec179) from reproduced fed calc below.
    return get_currency(USWDepr.Sec179Basis) + get_currency(USWDepr.List179basis) + get_currency(USF4562.Sec179Basis2106, 1)

def TotCYIAEst_Calculation():
    TP = Currency()

    SP = Currency()
    if GetDate(IASTATEEST.TPStQ4Date) < MakeDate(1, 1, YearNumber + 1):
        TP = get_currency(IASTATEEST.TPStApply) + get_currency(IASTATEEST.TPStQ1) + get_currency(IASTATEEST.TPStQ2) + get_currency(IASTATEEST.TPStQ3) + get_currency(IASTATEEST.TPStQ4)
    else:
        TP = get_currency(IASTATEEST.TPStApply) + get_currency(IASTATEEST.TPStQ1) + get_currency(IASTATEEST.TPStQ2) + get_currency(IASTATEEST.TPStQ3)
    if GetDate(IASTATEEST.SPStQ4Date) < MakeDate(1, 1, YearNumber + 1):
        SP = get_currency(IASTATEEST.SPStApply) + get_currency(IASTATEEST.SPStQ1) + get_currency(IASTATEEST.SPStQ2) + get_currency(IASTATEEST.SPStQ3) + get_currency(IASTATEEST.SPStQ4)
    else:
        SP = get_currency(IASTATEEST.SPStApply) + get_currency(IASTATEEST.SPStQ1) + get_currency(IASTATEEST.SPStQ2) + get_currency(IASTATEEST.SPStQ3)
    if IAFS() == 3:
        return TP + SP
    else:
        return TP

def TotCyLocEst_Calculation():
    Local1 = Currency()

    Local2 = Currency()

    Local3 = Currency()
    if get_string(USWEstPay.LocName1) == 'OTHER':
        Local1 = get_currency(USWLocalEst.CYLocal, 1)
    else:
        Local1 = 0
    if get_string(USWEstPay.LocName2) == 'OTHER':
        Local2 = get_currency(USWLocalEst.CYLocal, 2)
    else:
        Local2 = 0
    if get_string(USWEstPay.LocName3) == 'OTHER':
        Local3 = get_currency(USWLocalEst.CYLocal, 3)
    else:
        Local3 = 0
    return Local1 + Local2 + Local3

def TotDiv_Calculation():
    return get_currency(IASCHB.TotalTaxDiv)

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
            if get_string(USD1099DIV.St(DivIndex), count1) == 'IA':
                Total1 = Total1 + get_currency(USD1099DIV.STWh(DivIndex), count1)
            DivIndex = DivIndex + 1
        count1 = count1 + 1
    return Round(Total1)

def TotEICEarnInc_Calculation():
    if get_bool(IAF1040.MFS) == True:
        return get_currency(IAF1040.MFSEI) + get_currency(IAF1040.AWages) + get_currency(IAF1040.ABusInc) + get_currency(IAF1040.AFarm)
    else:
        return get_currency(IAF1040.BWages) + get_currency(IAF1040.BBusInc) + get_currency(IAF1040.BFarm) + get_currency(IAF1040.AWages) + get_currency(IAF1040.ABusInc) + get_currency(IAF1040.AFarm)

def TotElect179_Calculation():
    return get_currency(USWDepr.IACYSec179Rep) + get_currency(USF4562.StateTotCySec1792106, 1) + get_currency(USWSummary179.StateK1)

def TotIAExReimb_Calculation():
    return get_currency(IA3903.IAExReimb)

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
            if get_string(USDW2.St(W2Index), count1) == 'IA':
                Total1 = Total1 + get_currency(USDW2.STWh(W2Index), count1)
            W2Index = W2Index + 1
        count1 = count1 + 1
    return Round(Total1)

def TotIncAmt_Calculation():
    return get_currency(IAF1040.AGross) + get_currency(IAF1040.BGross)

def TotIncChg_Calculation():
    return get_currency(IAREQUIRED.TPTotIncChg) + get_currency(IAREQUIRED.SPTotIncChg)

def TotIncCk_Calculation():
    if get_currency(IAREQUIRED.TotIncChg) > 0:
        return 1
    else:
        return 0

def TotInt_Calculation():
    return get_currency(IASCHB.TotalTaxInt)

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
            if get_string(USD1099INT.St(IntIndex), count1) == 'IA':
                Total1 = Total1 + get_currency(USD1099INT.STWh(IntIndex), count1)
            IntIndex = IntIndex + 1
        count1 = count1 + 1
    return Round(Total1)

def TotIRA_Calculation():
    return get_currency(USWRec.TotIRAAdj)

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
            if get_string(USD1099K.State(KIndex), count1) == 'IA':
                Total1 = Total1 + get_currency(USD1099K.StateInc(KIndex), count1)
            KIndex = KIndex + 1
        count1 = count1 + 1
    return Round(Total1)

def TotMiscWH_Calculation():
    count1 = Integer()

    HowMany1099MISC = Long()

    Total1 = Currency()
    count1 = 1
    HowMany1099MISC = GetAllCopies(USD1099MISC)
    Total1 = 0
    while count1 <= HowMany1099MISC:
        if get_string(USD1099MISC.State, count1) == 'IA':
            Total1 = Total1 + get_currency(USD1099MISC.StateWH, count1)
        if get_string(USD1099MISC.State2, count1) == 'IA':
            Total1 = Total1 + get_currency(USD1099MISC.StateWH2, count1)
        count1 = count1 + 1
    return Round(Total1)

def TotMove_Calculation():
    return get_currency(USWRec.TotMove) + get_currency(IA3903.MovExpDdn)

def TotNI_Calculation():
    return get_currency(IAF1040.ANet) + get_currency(IAF1040.BNet)

def TotNIPenExc_Calculation():
    return get_currency(IAWKALTTAX.Ln26)

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
            if get_string(USD1099OID.St(OIDIndex), count1) == 'IA':
                Total1 = Total1 + get_currency(USD1099OID.STWh(OIDIndex), count1)
            OIDIndex = OIDIndex + 1
        count1 = count1 + 1
    return Round(Total1)

def TotOthIncWH_Calculation():
    return 0

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
        if get_bool(IASCHB.DSp1(count)) == True:
            SchBTotal = SchBTotal + get_currency(IASCHB.TaxDiv(count))
        else:
            SchBTotal = SchBTotal
        count = count + 1
    count1 = 1
    HowManyWBPDiv = GetAllCopies(IAWBPDIV)
    WSTotal = 0
    while count1 <= HowManyWBPDiv:
        DivIndex = 0
        while DivIndex < 22:
            if get_bool(IAWBPDIV.DSp1(DivIndex), count1) == True:
                WSTotal = WSTotal + get_currency(IAWBPDIV.TaxDiv(DivIndex), count1)
            DivIndex = DivIndex + 1
        count1 = count1 + 1
    return SchBTotal + WSTotal + get_currency(IAREQUIRED.JointSPDiv)

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
        if get_bool(IASCHB.ISp1(count)) == True:
            SchBTotal = SchBTotal + get_currency(IASCHB.TaxInt(count))
        else:
            SchBTotal = SchBTotal
        count = count + 1
    count1 = 1
    HowManyWBPInt = GetAllCopies(IAWBPINT)
    WSTotal = 0
    while count1 <= HowManyWBPInt:
        IntIndex = 0
        while IntIndex < 22:
            if get_bool(IAWBPINT.ISp1(IntIndex), count1) == True:
                WSTotal = WSTotal + get_currency(IAWBPINT.TaxInt(IntIndex), count1)
            IntIndex = IntIndex + 1
        count1 = count1 + 1
    return SchBTotal + WSTotal + get_currency(IAREQUIRED.JointSPInt)

def TotTPDiv_Calculation():
    return get_currency(IAREQUIRED.TotDiv) - get_currency(IAREQUIRED.TotSPDiv)

def TotTPInt_Calculation():
    return get_currency(IAREQUIRED.TotInt) - get_currency(IAREQUIRED.TotSPInt)

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
            if get_string(USWUnempl.TPState(UnIndex), count1) == 'IA':
                Total1 = Total1 + get_currency(USWUnempl.TPStWH(UnIndex), count1)
            UnIndex = UnIndex + 1
        count1 = count1 + 1
    return Round(Total1)

def TotW2GWH_Calculation():
    count1 = Integer()

    HowManyW2G = Long()

    Total1 = Currency()
    count1 = 1
    HowManyW2G = GetAllCopies(USDW2G)
    Total1 = 0
    while count1 <= HowManyW2G:
        if get_string(USDW2G.StateWon, count1) == 'IA':
            Total1 = Total1 + get_currency(USDW2G.StateWH, count1)
        count1 = count1 + 1
    return Round(Total1)

def TP8824_Calculation():
    return get_currency(IA8824.IANonConformAdj, FieldCopies(IA8824.Taxpayer)) + c_dollar(get_float(IA8824.IANonConformAdj, FieldCopies(IA8824.Joint)) * 0.5)

def TPCapGainWH_Calculation():
    return get_currency(IAREQUIRED.TotCapGainWH) - get_currency(IAREQUIRED.SPCapGainWH)

def TPComb_Calculation():
    return get_string(IAF1040.LastName) + ', ' + get_string(IAF1040.FirstName)

def TPCombName_Calculation():
    return get_string(IAF1040.FirstName) + ' ' + get_string(IAF1040.LastName)

def TPDivWH_Calculation():
    return get_currency(IAREQUIRED.TotDivWH) - get_currency(IAREQUIRED.SPDivWH)

def TPIntWH_Calculation():
    return get_currency(IAREQUIRED.TotIntWH) - get_currency(IAREQUIRED.SPIntWH)

def TPKWH_Calculation():
    return get_currency(USZIA1040.TotKWH) - get_currency(USZIA1040.SPKWH)

def TPMiscWH_Calculation():
    return get_currency(IAREQUIRED.TotMiscWH) - get_currency(IAREQUIRED.SPMiscWH)

def TPOIDWH_Calculation():
    return get_currency(IAREQUIRED.TotOIDWH) - get_currency(IAREQUIRED.SPOIDWH)

def TpOthIncWH_Calculation():
    return get_currency(IAREQUIRED.TotOthIncWH) - get_currency(IAREQUIRED.SPOthIncWH)

def TPTotIncChg_Calculation():
    Mid = Currency()

    MidInt = Long()

    TotTaxInc = Currency()
    # updated for 2018
    TotTaxInc = get_currency(IAF1040.AGross)
    if TotTaxInc > Decimal("95650"):
        Mid = TotTaxInc
    elif TotTaxInc > Decimal("150"):
        MidInt = CLng(( TotTaxInc - Decimal("1") )  / Decimal("50"))
        Mid = ( CCur(MidInt) * Decimal("50") )  + Decimal("25")
    else:
        Mid = Decimal("0")
    return Tax(Mid)

def TPUnemWH_Calculation():
    return get_currency(IAREQUIRED.TotUnemWH) - get_currency(IAREQUIRED.SPUnemWH)

def TPW2GWH_Calculation():
    return get_currency(IAREQUIRED.TotW2GWH) - get_currency(IAREQUIRED.SPW2GWH)


