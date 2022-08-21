from forms.out import IA2106
from forms.out import IA4562A
from forms.out import IA4562PIV
from forms.out import IA4562SP
from forms.out import IAF1040
from forms.out import IAREQUIRED
from forms.out import IAWNONCONFORMADJ
from forms.out import IAWOTHINC
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Code_Calculation(Index):
    count = Integer()

    Hold = String()
    count = 0
    Hold = ''
    if get_currency(IAWOTHINC.TPOth1) != 0 or get_currency(IAWOTHINC.SPOth1) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPOth2) != 0 or get_currency(IAWOTHINC.SPOth2) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPBabySit) != 0 or get_currency(IAWOTHINC.SPBabySit) != 0:
        if Index == count:
            Hold = 'a'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPBonus) != 0 or get_currency(IAWOTHINC.SPBonus) != 0:
        if Index == count:
            Hold = 'b'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPIAEd) != 0 or get_currency(IAWOTHINC.SPIAEd) != 0:
        if Index == count:
            Hold = 'd'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPDirector) != 0 or get_currency(IAWOTHINC.SPDirector) != 0:
        if Index == count:
            Hold = 'e'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPIntangDrill) != 0 or get_currency(IAWOTHINC.SPIntangDrill) != 0:
        if Index == count:
            Hold = 'f'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPExecutor) != 0 or get_currency(IAWOTHINC.SPExecutor) != 0:
        if Index == count:
            Hold = 'g'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPFirstHmBuy) != 0 or get_currency(IAWOTHINC.SPFirstHmBuy) != 0:
        if Index == count:
            Hold = 'h'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPK1) != 0 or get_currency(IAWOTHINC.SPK1) != 0:
        if Index == count:
            Hold = 'i'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPRefundCr) != 0 or get_currency(IAWOTHINC.SPRefundCr) != 0:
        if Index == count:
            Hold = 'j'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPStRefund) != 0 or get_currency(IAWOTHINC.SPStRefund) != 0:
        if Index == count:
            Hold = 'k'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPDepl) != 0 or get_currency(IAWOTHINC.SPDepl) != 0:
        if Index == count:
            Hold = 'l'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPJury) != 0 or get_currency(IAWOTHINC.SPJury) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPPerRent) != 0 or get_currency(IAWOTHINC.SPPerRent) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TP8814) != 0 or get_currency(IAWOTHINC.SP8814) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPMSA) != 0 or get_currency(IAWOTHINC.SPMSA) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPMedMSA) != 0 or get_currency(IAWOTHINC.SPMedMSA) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPLTC) != 0 or get_currency(IAWOTHINC.SPLTC) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPMisc) != 0 or get_currency(IAWOTHINC.SPMisc) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPAlaska) != 0 or get_currency(IAWOTHINC.SPAlaska) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPCoverdell) != 0 or get_currency(IAWOTHINC.SPCoverdell) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPCanceled) != 0 or get_currency(IAWOTHINC.SPCanceled) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPPshipCan) != 0 or get_currency(IAWOTHINC.SPPshipCan) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPHSA) != 0 or get_currency(IAWOTHINC.SPHSA) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPAltTrade) != 0 or get_currency(IAWOTHINC.SPAltTrade) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPRecapTuit) != 0 or get_currency(IAWOTHINC.SPRecapTuit) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPRecapChar) != 0 or get_currency(IAWOTHINC.SPRecapChar) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TP5471) != 0 or get_currency(IAWOTHINC.SP5471) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPHobby) != 0 or get_currency(IAWOTHINC.SPHobby) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TP8621) != 0 or get_currency(IAWOTHINC.SP8621) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPDefDist) != 0 or get_currency(IAWOTHINC.SPDefDist) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPDisaster) != 0 or get_currency(IAWOTHINC.SPDisaster) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPFoster) != 0 or get_currency(IAWOTHINC.SPFoster) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPCredAdj) != 0 or get_currency(IAWOTHINC.SPCredAdj) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPPYNPTC) != 0 or get_currency(IAWOTHINC.SPPYNPTC) != 0:
        if Index == count:
            Hold = 'n'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TP1099QA) != 0 or get_currency(IAWOTHINC.SP1099QA) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPAirline) != 0 or get_currency(IAWOTHINC.SPAirline) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TP1099B) != 0 or get_currency(IAWOTHINC.SP1099B) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPIAABLE) != 0 or get_currency(IAWOTHINC.SPIAABLE) != 0:
        if Index == count:
            Hold = 'o'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPBusPass) != 0 or get_currency(IAWOTHINC.SPBusPass) != 0:
        if Index == count:
            Hold = 'p'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPFarmLoss) != 0 or get_currency(IAWOTHINC.SPFarmLoss) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TP8824) != 0 or get_currency(IAWOTHINC.SP8824) != 0:
        if Index == count:
            Hold = 'q'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPStudLoanDis) != 0 or get_currency(IAWOTHINC.SPStudLoanDis) != 0:
        if Index == count:
            Hold = 'r'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TP4684) != 0 or get_currency(IAWOTHINC.SP4684) != 0:
        if Index == count:
            Hold = 's'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TP3903) != 0 or get_currency(IAWOTHINC.SP3903) != 0:
        if Index == count:
            Hold = 't'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPBusInt) != 0 or get_currency(IAWOTHINC.SPBusInt) != 0:
        if Index == count:
            Hold = 'u'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPEntExp) != 0 or get_currency(IAWOTHINC.SPEntExp) != 0:
        if Index == count:
            Hold = 'v'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TP2106) != 0 or get_currency(IAWOTHINC.SP2106) != 0:
        if Index == count:
            Hold = 'w'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPOthNC) != 0 or get_currency(IAWOTHINC.SPOthNC) != 0:
        if Index == count:
            Hold = 'x'
            count = 99
        else:
            count = count + 1
    return Hold

def Desc_Calculation():
    Total = Currency()
    Total = get_currency(IAWOTHINC.TPTot) + get_currency(IAWOTHINC.SPTot)
    return CStr(Total)

def Description_Calculation(Index):
    count = Integer()

    Hold = String()
    count = 0
    Hold = ''
    if get_currency(IAWOTHINC.TPOth1) != 0 or get_currency(IAWOTHINC.SPOth1) != 0:
        if Index == count:
            Hold = get_string(IAWOTHINC.Txt1)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPOth2) != 0 or get_currency(IAWOTHINC.SPOth2) != 0:
        if Index == count:
            Hold = get_string(IAWOTHINC.Txt2)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPBabySit) != 0 or get_currency(IAWOTHINC.SPBabySit) != 0:
        if Index == count:
            Hold = 'Baby-sitting income not reported on federal Schedule C'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPBonus) != 0 or get_currency(IAWOTHINC.SPBonus) != 0:
        if Index == count:
            Hold = 'Bonus depreciation/section 179 adjustment'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPIAEd) != 0 or get_currency(IAWOTHINC.SPIAEd) != 0:
        if Index == count:
            Hold = 'College Savings Iowa or Iowa Advisor 529 Plan'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPDirector) != 0 or get_currency(IAWOTHINC.SPDirector) != 0:
        if Index == count:
            Hold = 'Director\'s fees'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPIntangDrill) != 0 or get_currency(IAWOTHINC.SPIntangDrill) != 0:
        if Index == count:
            Hold = 'Drilling'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPExecutor) != 0 or get_currency(IAWOTHINC.SPExecutor) != 0:
        if Index == count:
            Hold = 'Executor\'s fees'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPFirstHmBuy) != 0 or get_currency(IAWOTHINC.SPFirstHmBuy) != 0:
        if Index == count:
            Hold = 'First-time homebuyers account non-qualifying withdrawals'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPK1) != 0 or get_currency(IAWOTHINC.SPK1) != 0:
        if Index == count:
            Hold = 'Partnership income and/or S Corporation income'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPRefundCr) != 0 or get_currency(IAWOTHINC.SPRefundCr) != 0:
        if Index == count:
            Hold = 'Refundable Iowa credits'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPStRefund) != 0 or get_currency(IAWOTHINC.SPStRefund) != 0:
        if Index == count:
            Hold = 'State income tax refunds'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPDepl) != 0 or get_currency(IAWOTHINC.SPDepl) != 0:
        if Index == count:
            Hold = 'Wells'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPJury) != 0 or get_currency(IAWOTHINC.SPJury) != 0:
        if Index == count:
            Hold = 'Jury pay'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPPerRent) != 0 or get_currency(IAWOTHINC.SPPerRent) != 0:
        if Index == count:
            Hold = 'Income from personal property'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TP8814) != 0 or get_currency(IAWOTHINC.SP8814) != 0:
        if Index == count:
            Hold = 'Child\'s income amount, federal Form 8814'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPMSA) != 0 or get_currency(IAWOTHINC.SPMSA) != 0:
        if Index == count:
            Hold = 'MSA distributions, federal Form 8853'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPMedMSA) != 0 or get_currency(IAWOTHINC.SPMedMSA) != 0:
        if Index == count:
            Hold = 'Medicare Advantage distributions, federal Form 8853'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPLTC) != 0 or get_currency(IAWOTHINC.SPLTC) != 0:
        if Index == count:
            Hold = 'Long-term care distribution, federal Form 8853'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPMisc) != 0 or get_currency(IAWOTHINC.SPMisc) != 0:
        if Index == count:
            Hold = 'Form 1099-MISC, boxes 3 or 8'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPAlaska) != 0 or get_currency(IAWOTHINC.SPAlaska) != 0:
        if Index == count:
            Hold = 'Alaska Permanent Fund dividends'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPCoverdell) != 0 or get_currency(IAWOTHINC.SPCoverdell) != 0:
        if Index == count:
            Hold = 'Coverdell ESA Or Qualified Tuition Program'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPCanceled) != 0 or get_currency(IAWOTHINC.SPCanceled) != 0:
        if Index == count:
            Hold = 'Cancellation of nonbusiness debt, federal Form 1099-C'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPPshipCan) != 0 or get_currency(IAWOTHINC.SPPshipCan) != 0:
        if Index == count:
            Hold = 'Cancellation of business debt, Partnership Schedule K-1'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPHSA) != 0 or get_currency(IAWOTHINC.SPHSA) != 0:
        if Index == count:
            Hold = 'HSA distributions, federal Form 8889'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPAltTrade) != 0 or get_currency(IAWOTHINC.SPAltTrade) != 0:
        if Index == count:
            Hold = 'Alternative trade adjustment assistance payments'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPRecapTuit) != 0 or get_currency(IAWOTHINC.SPRecapTuit) != 0:
        if Index == count:
            Hold = 'Recapture of prior year tuition and fees deduction'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPRecapChar) != 0 or get_currency(IAWOTHINC.SPRecapChar) != 0:
        if Index == count:
            Hold = 'Recapture of charitable contribution deduction'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TP5471) != 0 or get_currency(IAWOTHINC.SP5471) != 0:
        if Index == count:
            Hold = 'Income from a foreign corporation, federal Form 5471'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPHobby) != 0 or get_currency(IAWOTHINC.SPHobby) != 0:
        if Index == count:
            Hold = 'Hobby income'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TP8621) != 0 or get_currency(IAWOTHINC.SP8621) != 0:
        if Index == count:
            Hold = 'Income or loss from Section 1291, federal Form 8621'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPDefDist) != 0 or get_currency(IAWOTHINC.SPDefDist) != 0:
        if Index == count:
            Hold = 'Loss on excess deferral distribution'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPDisaster) != 0 or get_currency(IAWOTHINC.SPDisaster) != 0:
        if Index == count:
            Hold = 'Disaster relief payments'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPFoster) != 0 or get_currency(IAWOTHINC.SPFoster) != 0:
        if Index == count:
            Hold = 'Medicaid waiver payments to care provider'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPCredAdj) != 0 or get_currency(IAWOTHINC.SPCredAdj) != 0:
        if Index == count:
            Hold = 'Credit adjustment income, federal Forms 6478 and 8864'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPPYNPTC) != 0 or get_currency(IAWOTHINC.SPPYNPTC) != 0:
        if Index == count:
            Hold = 'Net Premium Tax Credit'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TP1099QA) != 0 or get_currency(IAWOTHINC.SP1099QA) != 0:
        if Index == count:
            Hold = 'Distributions from ABLE account'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPAirline) != 0 or get_currency(IAWOTHINC.SPAirline) != 0:
        if Index == count:
            Hold = 'Qualified airline payments'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TP1099B) != 0 or get_currency(IAWOTHINC.SP1099B) != 0:
        if Index == count:
            Hold = 'Foreign currency transaction'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPIAABLE) != 0 or get_currency(IAWOTHINC.SPIAABLE) != 0:
        if Index == count:
            Hold = 'Distributions from an Iowa ABLE account'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPBusPass) != 0 or get_currency(IAWOTHINC.SPBusPass) != 0:
        if Index == count:
            Hold = 'Employer provided bus pass or transportation expenses'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPFarmLoss) != 0 or get_currency(IAWOTHINC.SPFarmLoss) != 0:
        if Index == count:
            Hold = 'Section 461(j) excess farm loss limitation adjustments'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TP8824) != 0 or get_currency(IAWOTHINC.SP8824) != 0:
        if Index == count:
            Hold = 'IA 8824 worksheet, due to nonconformity'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPStudLoanDis) != 0 or get_currency(IAWOTHINC.SPStudLoanDis) != 0:
        if Index == count:
            Hold = 'Discharge of student loan debt - death or disability'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TP4684) != 0 or get_currency(IAWOTHINC.SP4684) != 0:
        if Index == count:
            Hold = 'IA 4684 worksheet, due to nonconformity'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TP3903) != 0 or get_currency(IAWOTHINC.SP3903) != 0:
        if Index == count:
            Hold = 'IA 3903 worksheet line 8a, due to nonconformity'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPBusInt) != 0 or get_currency(IAWOTHINC.SPBusInt) != 0:
        if Index == count:
            Hold = 'Business interest expense limitation, due to nonconformity'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPEntExp) != 0 or get_currency(IAWOTHINC.SPEntExp) != 0:
        if Index == count:
            Hold = 'Entertainment expenses, due to nonconformity'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TP2106) != 0 or get_currency(IAWOTHINC.SP2106) != 0:
        if Index == count:
            Hold = 'IA 2106 worksheet line 8, due to nonconformity'
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPOthNC) != 0 or get_currency(IAWOTHINC.SPOthNC) != 0:
        if Index == count:
            Hold = 'Other nonconformity adjustments'
            count = 99
        else:
            count = count + 1
    return Hold

def Exist_Calculation():
    return 1

def Names_Calculation():
    return get_string(IAREQUIRED.CombNames)

def Print_Calculation():
    if get_currency(IAWOTHINC.TPTot) != 0 or get_currency(IAWOTHINC.SPTot) != 0:
        return 1
    else:
        return 0

def SP1099B_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.SP1099B)
    else:
        return 0

def SP1099QA_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.SP1099QA)
    else:
        return 0

def SP2106_Calculation():
    return get_currency(IA2106.IAWages, FieldCopies(IA2106.Spouse))

def SP3903_Calculation():
    return get_currency(IAREQUIRED.SIAExReimb)

def SP5471_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.SP5471)
    else:
        return 0

def SP8621_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.SP8621)
    else:
        return 0

def SP8814_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.SP8814)
    else:
        return 0

def SP8824_Calculation():
    return get_currency(IAREQUIRED.SP8824)

def SPAirline_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.SPAirline)
    else:
        return 0

def SPAlaska_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.SPAlaska)
    else:
        return 0

def SPAltTrade_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.SPAltTrade)
    else:
        return 0

def SPAmount_Calculation(Index):
    count = Integer()

    Hold = Currency()
    count = 0
    Hold = 0
    if get_currency(IAWOTHINC.TPOth1) != 0 or get_currency(IAWOTHINC.SPOth1) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPOth1)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPOth2) != 0 or get_currency(IAWOTHINC.SPOth2) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPOth2)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPBabySit) != 0 or get_currency(IAWOTHINC.SPBabySit) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPBabySit)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPBonus) != 0 or get_currency(IAWOTHINC.SPBonus) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPBonus)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPIAEd) != 0 or get_currency(IAWOTHINC.SPIAEd) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPIAEd)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPDirector) != 0 or get_currency(IAWOTHINC.SPDirector) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPDirector)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPIntangDrill) != 0 or get_currency(IAWOTHINC.SPIntangDrill) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPIntangDrill)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPExecutor) != 0 or get_currency(IAWOTHINC.SPExecutor) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPExecutor)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPFirstHmBuy) != 0 or get_currency(IAWOTHINC.SPFirstHmBuy) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPFirstHmBuy)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPK1) != 0 or get_currency(IAWOTHINC.SPK1) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPK1)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPRefundCr) != 0 or get_currency(IAWOTHINC.SPRefundCr) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPRefundCr)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPStRefund) != 0 or get_currency(IAWOTHINC.SPStRefund) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPStRefund)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPDepl) != 0 or get_currency(IAWOTHINC.SPDepl) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPDepl)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPJury) != 0 or get_currency(IAWOTHINC.SPJury) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPJury)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPPerRent) != 0 or get_currency(IAWOTHINC.SPPerRent) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPPerRent)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TP8814) != 0 or get_currency(IAWOTHINC.SP8814) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SP8814)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPMSA) != 0 or get_currency(IAWOTHINC.SPMSA) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPMSA)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPMedMSA) != 0 or get_currency(IAWOTHINC.SPMedMSA) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPMedMSA)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPLTC) != 0 or get_currency(IAWOTHINC.SPLTC) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPLTC)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPMisc) != 0 or get_currency(IAWOTHINC.SPMisc) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPMisc)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPAlaska) != 0 or get_currency(IAWOTHINC.SPAlaska) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPAlaska)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPCoverdell) != 0 or get_currency(IAWOTHINC.SPCoverdell) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPCoverdell)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPCanceled) != 0 or get_currency(IAWOTHINC.SPCanceled) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPCanceled)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPPshipCan) != 0 or get_currency(IAWOTHINC.SPPshipCan) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPPshipCan)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPHSA) != 0 or get_currency(IAWOTHINC.SPHSA) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPHSA)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPAltTrade) != 0 or get_currency(IAWOTHINC.SPAltTrade) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPAltTrade)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPRecapTuit) != 0 or get_currency(IAWOTHINC.SPRecapTuit) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPRecapTuit)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPRecapChar) != 0 or get_currency(IAWOTHINC.SPRecapChar) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPRecapChar)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TP5471) != 0 or get_currency(IAWOTHINC.SP5471) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SP5471)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPHobby) != 0 or get_currency(IAWOTHINC.SPHobby) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPHobby)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TP8621) != 0 or get_currency(IAWOTHINC.SP8621) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SP8621)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPDefDist) != 0 or get_currency(IAWOTHINC.SPDefDist) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPDefDist)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPDisaster) != 0 or get_currency(IAWOTHINC.SPDisaster) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPDisaster)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPFoster) != 0 or get_currency(IAWOTHINC.SPFoster) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPFoster)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPCredAdj) != 0 or get_currency(IAWOTHINC.SPCredAdj) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPCredAdj)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPPYNPTC) != 0 or get_currency(IAWOTHINC.SPPYNPTC) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPPYNPTC)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TP1099QA) != 0 or get_currency(IAWOTHINC.SP1099QA) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SP1099QA)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPAirline) != 0 or get_currency(IAWOTHINC.SPAirline) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPAirline)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TP1099B) != 0 or get_currency(IAWOTHINC.SP1099B) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SP1099B)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPIAABLE) != 0 or get_currency(IAWOTHINC.SPIAABLE) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPIAABLE)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPBusPass) != 0 or get_currency(IAWOTHINC.SPBusPass) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPBusPass)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPFarmLoss) != 0 or get_currency(IAWOTHINC.SPFarmLoss) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPFarmLoss)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TP8824) != 0 or get_currency(IAWOTHINC.SP8824) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SP8824)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPStudLoanDis) != 0 or get_currency(IAWOTHINC.SPStudLoanDis) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPStudLoanDis)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TP4684) != 0 or get_currency(IAWOTHINC.SP4684) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SP4684)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TP3903) != 0 or get_currency(IAWOTHINC.SP3903) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SP3903)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPBusInt) != 0 or get_currency(IAWOTHINC.SPBusInt) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPBusInt)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPEntExp) != 0 or get_currency(IAWOTHINC.SPEntExp) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPEntExp)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TP2106) != 0 or get_currency(IAWOTHINC.SP2106) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SP2106)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPOthNC) != 0 or get_currency(IAWOTHINC.SPOthNC) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.SPOthNC)
            count = 99
        else:
            count = count + 1
    return Hold

def SPBonus_Calculation():
    return get_currency(IAWOTHINC.TotBonus) - get_currency(IAWOTHINC.TPBonus)

def SPCanceled_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.SPCanceled)
    else:
        return 0

def SPCoverdell_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.SPCoverdell)
    else:
        return 0

def SPCredAdj_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.SPCredAdj)
    else:
        return 0

def SPDefDist_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.SPDefDist)
    else:
        return 0

def SPDisaster_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.SPDisaster)
    else:
        return 0

def SPFoster_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.SPFoster)
    else:
        return 0

def SPHobby_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.SPHobby)
    else:
        return 0

def SPHSA_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.SPHSA)
    else:
        return 0

def SPJury_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.SPJury)
    else:
        return 0

def SPK1_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return max_value(0, get_currency(USWOthInc.SPK1))
    else:
        return 0

def SPLTC_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.SPLTC)
    else:
        return 0

def SPMedMSA_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.SPMedMSA)
    else:
        return 0

def SPMisc_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.SPMisc) + get_currency(USWOthInc.SPIndianGaming) + get_currency(USWOthInc.SPTribDist) + get_currency(USWOthInc.SPNativeDist)
    else:
        return 0

def SPMSA_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.SP8853)
    else:
        return 0

def SPName_Calculation():
    return get_string(USWBasicInfo.SPCommon)

def SPOth1_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.SPOth1)
    else:
        return 0

def SPOth2_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.SPOth2)
    else:
        return 0

def SPOthNC_Calculation():
    return get_currency(IAWNONCONFORMADJ.SPTotNonConformAdj)

def SPPerRent_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.SPPerRent)
    else:
        return 0

def SPPshipCan_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.SPPshipCan)
    else:
        return 0

def SPRecapChar_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.SPRecapChContTax) + get_currency(USWOthInc.SPRecapChar)
    else:
        return 0

def SPRecapTuit_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.SPRecapTuit)
    else:
        return 0

def SPTot_Calculation():
    return get_currency(IAWOTHINC.SPOth1) + get_currency(IAWOTHINC.SPOth2) + get_currency(IAWOTHINC.SPBabySit) + get_currency(IAWOTHINC.SPBonus) + get_currency(IAWOTHINC.SPIAEd) + get_currency(IAWOTHINC.SPDirector) + get_currency(IAWOTHINC.SPIntangDrill) + get_currency(IAWOTHINC.SPExecutor) + get_currency(IAWOTHINC.SPFirstHmBuy) + get_currency(IAWOTHINC.SPK1) + get_currency(IAWOTHINC.SPRefundCr) + get_currency(IAWOTHINC.SPStRefund) + get_currency(IAWOTHINC.SPDepl) + get_currency(IAWOTHINC.SPJury) + get_currency(IAWOTHINC.SPPerRent) + get_currency(IAWOTHINC.SP8814) + get_currency(IAWOTHINC.SPMSA) + get_currency(IAWOTHINC.SPMedMSA) + get_currency(IAWOTHINC.SPLTC) + get_currency(IAWOTHINC.SPMisc) + get_currency(IAWOTHINC.SPAlaska) + get_currency(IAWOTHINC.SPCoverdell) + get_currency(IAWOTHINC.SPCanceled) + get_currency(IAWOTHINC.SPPshipCan) + get_currency(IAWOTHINC.SPHSA) + get_currency(IAWOTHINC.SPAltTrade) + get_currency(IAWOTHINC.SPRecapTuit) + get_currency(IAWOTHINC.SPRecapChar) + get_currency(IAWOTHINC.SP5471) + get_currency(IAWOTHINC.SPHobby) + get_currency(IAWOTHINC.SP8621) + get_currency(IAWOTHINC.SPDefDist) + get_currency(IAWOTHINC.SPDisaster) + get_currency(IAWOTHINC.SPFoster) + get_currency(IAWOTHINC.SPCredAdj) + get_currency(IAWOTHINC.SPPYNPTC) + get_currency(IAWOTHINC.SP1099QA) + get_currency(IAWOTHINC.SPIAABLE) + get_currency(IAWOTHINC.SPBusPass) + get_currency(IAWOTHINC.SPAirline) + get_currency(IAWOTHINC.SP1099B) + get_currency(IAWOTHINC.SPFarmLoss) + get_currency(IAWOTHINC.SP8824) + get_currency(IAWOTHINC.SPStudLoanDis) + get_currency(IAWOTHINC.SP4684) + get_currency(IAWOTHINC.SP3903) + get_currency(IAWOTHINC.SPBusInt) + get_currency(IAWOTHINC.SPEntExp) + get_currency(IAWOTHINC.SP2106) + get_currency(IAWOTHINC.SPOthNC)

def SPTotNonConform_Calculation():
    return get_currency(IAWOTHINC.SPFarmLoss) + get_currency(IAWOTHINC.SP8824) + get_currency(IAWOTHINC.SPStudLoanDis) + get_currency(IAWOTHINC.SP4684) + get_currency(IAWOTHINC.SP3903) + get_currency(IAWOTHINC.SPBusInt) + get_currency(IAWOTHINC.SPEntExp) + get_currency(IAWOTHINC.SP2106) + get_currency(IAWOTHINC.SPOthNC)

def SSN_Calculation():
    return get_string(IAF1040.SSN)

def TotBonus_Calculation():
    return get_currency(IA4562.TotDepAdj) + get_currency(IA4562SP.TotDepAdj) + get_currency(IA4562A.TotDepAdj)

def TotNonConform_Calculation():
    return get_currency(IAWOTHINC.SPTotNonConform) + get_currency(IAWOTHINC.TPTotNonConform)

def TP1099B_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.TP1099B)
    else:
        return get_currency(USWOthIncNR.TP1099B)

def TP1099QA_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.TP1099QA)
    else:
        return get_currency(USWOthIncNR.TP1099QA)

def TP2106_Calculation():
    return get_currency(IA2106.IAWages, FieldCopies(IA2106.Taxpayer))

def TP3903_Calculation():
    return get_currency(IAREQUIRED.TIAExReimb)

def TP4684_Calculation():
    return get_currency(IA4684.IANonConformAdj) - get_currency(IAWOTHINC.SP4684)

def TP5471_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.TP5471)
    else:
        return get_currency(USWOthIncNR.TP5471)

def TP8621_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.TP8621)
    else:
        return 0

def TP8814_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.TP8814)
    else:
        return get_currency(USWOthIncNR.TP8814)

def TP8824_Calculation():
    return get_currency(IAREQUIRED.TP8824)

def TPAirline_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.TPAirline)
    else:
        return 0

def TPAlaska_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.TPAlaska)
    else:
        return 0

def TPAltTrade_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.TPAltTrade)
    else:
        return get_currency(USWOthIncNR.TPAltTrade)

def TPAmount_Calculation(Index):
    count = Integer()

    Hold = Currency()
    count = 0
    Hold = 0
    if get_currency(IAWOTHINC.TPOth1) != 0 or get_currency(IAWOTHINC.SPOth1) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPOth1)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPOth2) != 0 or get_currency(IAWOTHINC.SPOth2) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPOth2)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPBabySit) != 0 or get_currency(IAWOTHINC.SPBabySit) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPBabySit)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPBonus) != 0 or get_currency(IAWOTHINC.SPBonus) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPBonus)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPIAEd) != 0 or get_currency(IAWOTHINC.SPIAEd) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPIAEd)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPDirector) != 0 or get_currency(IAWOTHINC.SPDirector) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPDirector)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPIntangDrill) != 0 or get_currency(IAWOTHINC.SPIntangDrill) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPIntangDrill)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPExecutor) != 0 or get_currency(IAWOTHINC.SPExecutor) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPExecutor)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPFirstHmBuy) != 0 or get_currency(IAWOTHINC.SPFirstHmBuy) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPFirstHmBuy)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPK1) != 0 or get_currency(IAWOTHINC.SPK1) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPK1)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPRefundCr) != 0 or get_currency(IAWOTHINC.SPRefundCr) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPRefundCr)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPStRefund) != 0 or get_currency(IAWOTHINC.SPStRefund) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPStRefund)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPDepl) != 0 or get_currency(IAWOTHINC.SPDepl) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPDepl)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPJury) != 0 or get_currency(IAWOTHINC.SPJury) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPJury)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPPerRent) != 0 or get_currency(IAWOTHINC.SPPerRent) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPPerRent)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TP8814) != 0 or get_currency(IAWOTHINC.SP8814) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TP8814)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPMSA) != 0 or get_currency(IAWOTHINC.SPMSA) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPMSA)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPMedMSA) != 0 or get_currency(IAWOTHINC.SPMedMSA) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPMedMSA)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPLTC) != 0 or get_currency(IAWOTHINC.SPLTC) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPLTC)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPMisc) != 0 or get_currency(IAWOTHINC.SPMisc) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPMisc)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPAlaska) != 0 or get_currency(IAWOTHINC.SPAlaska) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPAlaska)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPCoverdell) != 0 or get_currency(IAWOTHINC.SPCoverdell) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPCoverdell)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPCanceled) != 0 or get_currency(IAWOTHINC.SPCanceled) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPCanceled)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPPshipCan) != 0 or get_currency(IAWOTHINC.SPPshipCan) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPPshipCan)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPHSA) != 0 or get_currency(IAWOTHINC.SPHSA) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPHSA)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPAltTrade) != 0 or get_currency(IAWOTHINC.SPAltTrade) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPAltTrade)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPRecapTuit) != 0 or get_currency(IAWOTHINC.SPRecapTuit) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPRecapTuit)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPRecapChar) != 0 or get_currency(IAWOTHINC.SPRecapChar) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPRecapChar)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TP5471) != 0 or get_currency(IAWOTHINC.SP5471) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TP5471)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPHobby) != 0 or get_currency(IAWOTHINC.SPHobby) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPHobby)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TP8621) != 0 or get_currency(IAWOTHINC.SP8621) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TP8621)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPDefDist) != 0 or get_currency(IAWOTHINC.SPDefDist) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPDefDist)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPDisaster) != 0 or get_currency(IAWOTHINC.SPDisaster) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPDisaster)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPFoster) != 0 or get_currency(IAWOTHINC.SPFoster) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPFoster)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPCredAdj) != 0 or get_currency(IAWOTHINC.SPCredAdj) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPCredAdj)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPPYNPTC) != 0 or get_currency(IAWOTHINC.SPPYNPTC) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPPYNPTC)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TP1099QA) != 0 or get_currency(IAWOTHINC.SP1099QA) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TP1099QA)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPAirline) != 0 or get_currency(IAWOTHINC.SPAirline) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPAirline)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TP1099B) != 0 or get_currency(IAWOTHINC.SP1099B) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TP1099B)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPIAABLE) != 0 or get_currency(IAWOTHINC.SPIAABLE) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPIAABLE)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPBusPass) != 0 or get_currency(IAWOTHINC.SPBusPass) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPBusPass)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPFarmLoss) != 0 or get_currency(IAWOTHINC.SPFarmLoss) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPFarmLoss)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TP8824) != 0 or get_currency(IAWOTHINC.SP8824) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TP8824)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPStudLoanDis) != 0 or get_currency(IAWOTHINC.SPStudLoanDis) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPStudLoanDis)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TP4684) != 0 or get_currency(IAWOTHINC.SP4684) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TP4684)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TP3903) != 0 or get_currency(IAWOTHINC.SP3903) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TP3903)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPBusInt) != 0 or get_currency(IAWOTHINC.SPBusInt) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPBusInt)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPEntExp) != 0 or get_currency(IAWOTHINC.SPEntExp) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPEntExp)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TP2106) != 0 or get_currency(IAWOTHINC.SP2106) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TP2106)
            count = 99
        else:
            count = count + 1
    if get_currency(IAWOTHINC.TPOthNC) != 0 or get_currency(IAWOTHINC.SPOthNC) != 0:
        if Index == count:
            Hold = get_currency(IAWOTHINC.TPOthNC)
            count = 99
        else:
            count = count + 1
    return Hold

def TPBonus_Calculation():
    JT = Currency()
    JT = c_dollar(CDbl(Round(get_currency(IAWDepr.TotAdj, FieldCopies(IAWDepr.Joint)))) * 0.5)
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return JT + get_currency(IAWDepr.TotAdj, FieldCopies(IAWDepr.Taxpayer)) + get_currency(IA4562A.TotDepAdj, FieldCopies(IA4562A.Taxpayer)) + get_currency(IA4562PIV.TPTotAdj)
    else:
        return get_currency(IAWOTHINC.TotBonus)

def TPBonusTrigger_Calculation():
    if IAFS() == 3:
        return get_currency(IAWOTHINC.TPBonus)
    else:
        return get_currency(IAWOTHINC.TPBonus) + get_currency(IAWOTHINC.SPBonus)

def TPCanceled_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.TPCanceled)
    else:
        return get_currency(USWOthIncNR.TPCanceled)

def TPCoverdell_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.TPCoverdell)
    else:
        return get_currency(USWOthIncNR.TPCoverdell)

def TPCredAdj_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.TPCredAdj)
    else:
        return get_currency(USWOthIncNR.TPCredAdj)

def TPDefDist_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.TPDefDist)
    else:
        return get_currency(USWOthIncNR.TPDefDist)

def TPDepl_Calculation():
    return max_value(0, get_currency(USF6251.Depl) - get_currency(IAWOTHINC.SPDepl))

def TPDisaster_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.TPDisaster)
    else:
        return get_currency(USWOthIncNR.TPDisaster)

def TPFarmLoss_Calculation():
    return max_value(0, Abs(get_currency(IAWSchFLoss.ExcessLoss)) - get_currency(IAWOTHINC.SPFarmLoss))

def TPFoster_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.TPFoster)
    else:
        return get_currency(USWOthIncNR.TPFoster)

def TPHobby_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.TPHobby)
    else:
        return 0

def TPHSA_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.TPHSA)
    else:
        return get_currency(USWOthIncNR.TPHSA)

def TPIntangDrill_Calculation():
    return max_value(0, get_currency(USF6251.IntangDrill) - get_currency(IAWOTHINC.SPIntangDrill))

def TPJointAmount_Calculation(Index):
    if get_bool(IAF1040.CombMFS) == True:
        return get_currency(IAWOTHINC.TPAmount(Index))
    else:
        return get_currency(IAWOTHINC.TPAmount(Index)) + get_currency(IAWOTHINC.SPAmount(Index))

def TPJury_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.TPJury)
    else:
        return 0

def TPK1_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return max_value(0, get_currency(USWOthInc.TPK1))
    else:
        return max_value(0, get_currency(USWOthIncNR.TPK1))

def TPLTC_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.TPLTC)
    else:
        return get_currency(USWOthIncNR.TPLTC)

def TPMedMSA_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.TPMedMSA)
    else:
        return get_currency(USWOthIncNR.TPMedMSA)

def TPMisc_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.TPMisc) + get_currency(USWOthInc.TPIndianGaming) + get_currency(USWOthInc.TPTribDist) + get_currency(USWOthInc.TPNativeDist)
    else:
        return get_currency(USWOthIncNR.TPMisc)

def TPMSA_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.TP8853)
    else:
        return get_currency(USWOthIncNR.TP8853)

def TPName_Calculation():
    return get_string(USWBasicInfo.TPCommon)

def TPOth1_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.TPOth1)
    else:
        return get_currency(USWOthIncNR.TPOth1)

def TPOth2_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.TPOth2)
    else:
        return get_currency(USWOthIncNR.TPOth2)

def TPOthNC_Calculation():
    return get_currency(IAWNONCONFORMADJ.TPTotNonConformAdj)

def TPPerRent_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.TPPerRent)
    else:
        return 0

def TPPshipCan_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.TPPshipCan)
    else:
        return get_currency(USWOthIncNR.TPPshipCan)

def TPPYNPTC_Calculation():
    if get_bool(USWSpouse.NonRes) == True:
        return max_value(0, get_currency(USWRec.PYNPTCNR) - get_currency(IAWOTHINC.SPPYNPTC))
    else:
        return max_value(0, get_currency(USWRec.PYNPTC) - get_currency(IAWOTHINC.SPPYNPTC))

def TPRecapChar_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.TPRecapChContTax) + get_currency(USWOthInc.TPRecapChar)
    else:
        return get_currency(USWOthIncNR.TPRecapChContTax) + get_currency(USWOthIncNR.TPRecapChar)

def TPRecapTuit_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthInc.TPRecapTuit)
    else:
        return 0

def TPTot_Calculation():
    return get_currency(IAWOTHINC.TPOth1) + get_currency(IAWOTHINC.TPOth2) + get_currency(IAWOTHINC.TPBabySit) + get_currency(IAWOTHINC.TPBonus) + get_currency(IAWOTHINC.TPIAEd) + get_currency(IAWOTHINC.TPDirector) + get_currency(IAWOTHINC.TPIntangDrill) + get_currency(IAWOTHINC.TPExecutor) + get_currency(IAWOTHINC.TPFirstHmBuy) + get_currency(IAWOTHINC.TPK1) + get_currency(IAWOTHINC.TPRefundCr) + get_currency(IAWOTHINC.TPStRefund) + get_currency(IAWOTHINC.TPDepl) + get_currency(IAWOTHINC.TPJury) + get_currency(IAWOTHINC.TPPerRent) + get_currency(IAWOTHINC.TP8814) + get_currency(IAWOTHINC.TPMSA) + get_currency(IAWOTHINC.TPMedMSA) + get_currency(IAWOTHINC.TPLTC) + get_currency(IAWOTHINC.TPMisc) + get_currency(IAWOTHINC.TPAlaska) + get_currency(IAWOTHINC.TPCoverdell) + get_currency(IAWOTHINC.TPCanceled) + get_currency(IAWOTHINC.TPPshipCan) + get_currency(IAWOTHINC.TPHSA) + get_currency(IAWOTHINC.TPAltTrade) + get_currency(IAWOTHINC.TPRecapTuit) + get_currency(IAWOTHINC.TPRecapChar) + get_currency(IAWOTHINC.TP5471) + get_currency(IAWOTHINC.TPHobby) + get_currency(IAWOTHINC.TP8621) + get_currency(IAWOTHINC.TPDefDist) + get_currency(IAWOTHINC.TPDisaster) + get_currency(IAWOTHINC.TPFoster) + get_currency(IAWOTHINC.TPCredAdj) + get_currency(IAWOTHINC.TPPYNPTC) + get_currency(IAWOTHINC.TP1099QA) + get_currency(IAWOTHINC.TPIAABLE) + get_currency(IAWOTHINC.TPBusPass) + get_currency(IAWOTHINC.TPAirline) + get_currency(IAWOTHINC.TP1099B) + get_currency(IAWOTHINC.TPFarmLoss) + get_currency(IAWOTHINC.TP8824) + get_currency(IAWOTHINC.TPStudLoanDis) + get_currency(IAWOTHINC.TP4684) + get_currency(IAWOTHINC.TP3903) + get_currency(IAWOTHINC.TPBusInt) + get_currency(IAWOTHINC.TPEntExp) + get_currency(IAWOTHINC.TP2106) + get_currency(IAWOTHINC.TPOthNC)

def TPTotNonConform_Calculation():
    return get_currency(IAWOTHINC.TPFarmLoss) + get_currency(IAWOTHINC.TP8824) + get_currency(IAWOTHINC.TPStudLoanDis) + get_currency(IAWOTHINC.TP4684) + get_currency(IAWOTHINC.TP3903) + get_currency(IAWOTHINC.TPBusInt) + get_currency(IAWOTHINC.TPEntExp) + get_currency(IAWOTHINC.TP2106) + get_currency(IAWOTHINC.TPOthNC)

def Txt1_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_string(USWOthInc.Txt1)
    else:
        return get_string(USWOthIncNR.Txt1)

def Txt2_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_string(USWOthInc.Txt2)
    else:
        return get_string(USWOthIncNR.Txt2)


