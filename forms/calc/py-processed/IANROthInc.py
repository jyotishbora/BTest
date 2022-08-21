from forms.out import IAF1040
from forms.out import IAF126
from forms.out import IANROTHINC
from forms.out import IAREQUIRED
from forms.out import IAWOTHINC
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Code_Calculation(Index):
    count = Integer()

    Hold = String()
    count = 0
    Hold = ''
    if get_currency(IANROTHINC.TPOth1) != 0 or get_currency(IANROTHINC.SPOth1) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPOth2) != 0 or get_currency(IANROTHINC.SPOth2) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPBabySit) != 0 or get_currency(IANROTHINC.SPBabySit) != 0:
        if Index == count:
            Hold = 'a'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPBonus) != 0 or get_currency(IANROTHINC.SPBonus) != 0:
        if Index == count:
            Hold = 'b'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPIAEd) != 0 or get_currency(IANROTHINC.SPIAEd) != 0:
        if Index == count:
            Hold = 'd'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPDirector) != 0 or get_currency(IANROTHINC.SPDirector) != 0:
        if Index == count:
            Hold = 'e'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPIntangDrill) != 0 or get_currency(IANROTHINC.SPIntangDrill) != 0:
        if Index == count:
            Hold = 'f'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPExecutor) != 0 or get_currency(IANROTHINC.SPExecutor) != 0:
        if Index == count:
            Hold = 'g'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPFirstHmBuy) != 0 or get_currency(IANROTHINC.SPFirstHmBuy) != 0:
        if Index == count:
            Hold = 'h'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPK1) != 0 or get_currency(IANROTHINC.SPK1) != 0:
        if Index == count:
            Hold = 'i'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPRefundCr) != 0 or get_currency(IANROTHINC.SPRefundCr) != 0:
        if Index == count:
            Hold = 'j'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPStRefund) != 0 or get_currency(IANROTHINC.SPStRefund) != 0:
        if Index == count:
            Hold = 'k'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPDepl) != 0 or get_currency(IANROTHINC.SPDepl) != 0:
        if Index == count:
            Hold = 'l'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPJury) != 0 or get_currency(IANROTHINC.SPJury) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPPerRent) != 0 or get_currency(IANROTHINC.SPPerRent) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TP8814) != 0 or get_currency(IANROTHINC.SP8814) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPMSA) != 0 or get_currency(IANROTHINC.SPMSA) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPMedMSA) != 0 or get_currency(IANROTHINC.SPMedMSA) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPLTC) != 0 or get_currency(IANROTHINC.SPLTC) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPMisc) != 0 or get_currency(IANROTHINC.SPMisc) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPAlaska) != 0 or get_currency(IANROTHINC.SPAlaska) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPCoverdell) != 0 or get_currency(IANROTHINC.SPCoverdell) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPCanceled) != 0 or get_currency(IANROTHINC.SPCanceled) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPPshipCan) != 0 or get_currency(IANROTHINC.SPPshipCan) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPHSA) != 0 or get_currency(IANROTHINC.SPHSA) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPAltTrade) != 0 or get_currency(IANROTHINC.SPAltTrade) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPRecapTuit) != 0 or get_currency(IANROTHINC.SPRecapTuit) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPRecapChar) != 0 or get_currency(IANROTHINC.SPRecapChar) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TP5471) != 0 or get_currency(IANROTHINC.SP5471) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPHobby) != 0 or get_currency(IANROTHINC.SPHobby) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TP8621) != 0 or get_currency(IANROTHINC.SP8621) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPDefDist) != 0 or get_currency(IANROTHINC.SPDefDist) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPDisaster) != 0 or get_currency(IANROTHINC.SPDisaster) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPFoster) != 0 or get_currency(IANROTHINC.SPFoster) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPCredAdj) != 0 or get_currency(IANROTHINC.SPCredAdj) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPPYNPTC) != 0 or get_currency(IANROTHINC.SPPYNPTC) != 0:
        if Index == count:
            Hold = 'n'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TP1099QA) != 0 or get_currency(IANROTHINC.SP1099QA) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPAirline) != 0 or get_currency(IANROTHINC.SPAirline) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TP1099B) != 0 or get_currency(IANROTHINC.SP1099B) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPIAABLE) != 0 or get_currency(IANROTHINC.SPIAABLE) != 0:
        if Index == count:
            Hold = 'o'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPBusPass) != 0 or get_currency(IANROTHINC.SPBusPass) != 0:
        if Index == count:
            Hold = 'p'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPFarmLoss) != 0 or get_currency(IANROTHINC.SPFarmLoss) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TP8824) != 0 or get_currency(IANROTHINC.SP8824) != 0:
        if Index == count:
            Hold = 'q'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPStudLoanDis) != 0 or get_currency(IANROTHINC.SPStudLoanDis) != 0:
        if Index == count:
            Hold = 'r'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TP4684) != 0 or get_currency(IANROTHINC.SP4684) != 0:
        if Index == count:
            Hold = 's'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TP3903) != 0 or get_currency(IANROTHINC.SP3903) != 0:
        if Index == count:
            Hold = 't'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPBusInt) != 0 or get_currency(IANROTHINC.SPBusInt) != 0:
        if Index == count:
            Hold = 'u'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPEntExp) != 0 or get_currency(IANROTHINC.SPEntExp) != 0:
        if Index == count:
            Hold = 'v'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TP2106) != 0 or get_currency(IANROTHINC.SP2106) != 0:
        if Index == count:
            Hold = 'w'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPOthNC) != 0 or get_currency(IANROTHINC.SPOthNC) != 0:
        if Index == count:
            Hold = 'x'
            count = 99
        else:
            count = count + 1
    return Hold

def Desc_Calculation():
    Total = Currency()
    Total = get_currency(IANROTHINC.TPTot) + get_currency(IANROTHINC.SPTot)
    return CStr(Total)

def Description_Calculation(Index):
    count = Integer()

    Hold = String()
    count = 0
    Hold = ''
    if get_currency(IANROTHINC.TPOth1) != 0 or get_currency(IANROTHINC.SPOth1) != 0:
        if Index == count:
            Hold = get_string(IANROTHINC.Txt1)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPOth2) != 0 or get_currency(IANROTHINC.SPOth2) != 0:
        if Index == count:
            Hold = get_string(IANROTHINC.Txt2)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPBabySit) != 0 or get_currency(IANROTHINC.SPBabySit) != 0:
        if Index == count:
            Hold = 'Baby-sitting income not reported on federal Schedule C'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPBonus) != 0 or get_currency(IANROTHINC.SPBonus) != 0:
        if Index == count:
            Hold = 'Bonus depreciation/section 179 adjustment'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPIAEd) != 0 or get_currency(IANROTHINC.SPIAEd) != 0:
        if Index == count:
            Hold = 'College Savings Iowa or Iowa Advisor 529 Plan'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPDirector) != 0 or get_currency(IANROTHINC.SPDirector) != 0:
        if Index == count:
            Hold = 'Director\'s fees'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPIntangDrill) != 0 or get_currency(IANROTHINC.SPIntangDrill) != 0:
        if Index == count:
            Hold = 'Drilling'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPExecutor) != 0 or get_currency(IANROTHINC.SPExecutor) != 0:
        if Index == count:
            Hold = 'Executor\'s fees'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPFirstHmBuy) != 0 or get_currency(IANROTHINC.SPFirstHmBuy) != 0:
        if Index == count:
            Hold = 'First-time homebuyers account non-qualifying withdrawals'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPK1) != 0 or get_currency(IANROTHINC.SPK1) != 0:
        if Index == count:
            Hold = 'Partnership income and/or S Corporation income'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPRefundCr) != 0 or get_currency(IANROTHINC.SPRefundCr) != 0:
        if Index == count:
            Hold = 'Refundable Iowa credits'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPStRefund) != 0 or get_currency(IANROTHINC.SPStRefund) != 0:
        if Index == count:
            Hold = 'State income tax refunds'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPDepl) != 0 or get_currency(IANROTHINC.SPDepl) != 0:
        if Index == count:
            Hold = 'Wells'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPJury) != 0 or get_currency(IANROTHINC.SPJury) != 0:
        if Index == count:
            Hold = 'Jury pay'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPPerRent) != 0 or get_currency(IANROTHINC.SPPerRent) != 0:
        if Index == count:
            Hold = 'Income from personal property'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TP8814) != 0 or get_currency(IANROTHINC.SP8814) != 0:
        if Index == count:
            Hold = 'Child\'s income amount, federal Form 8814'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPMSA) != 0 or get_currency(IANROTHINC.SPMSA) != 0:
        if Index == count:
            Hold = 'MSA distributions, federal Form 8853'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPMedMSA) != 0 or get_currency(IANROTHINC.SPMedMSA) != 0:
        if Index == count:
            Hold = 'Medicare Advantage distributions, federal Form 8853'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPLTC) != 0 or get_currency(IANROTHINC.SPLTC) != 0:
        if Index == count:
            Hold = 'Long-term care distribution, federal Form 8853'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPMisc) != 0 or get_currency(IANROTHINC.SPMisc) != 0:
        if Index == count:
            Hold = 'Form 1099-MISC, boxes 3 or 8'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPAlaska) != 0 or get_currency(IANROTHINC.SPAlaska) != 0:
        if Index == count:
            Hold = 'Alaska Permanent Fund dividends'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPCoverdell) != 0 or get_currency(IANROTHINC.SPCoverdell) != 0:
        if Index == count:
            Hold = 'Coverdell ESA Or Qualified Tuition Program'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPCanceled) != 0 or get_currency(IANROTHINC.SPCanceled) != 0:
        if Index == count:
            Hold = 'Cancellation of nonbusiness debt, federal Form 1099-C'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPPshipCan) != 0 or get_currency(IANROTHINC.SPPshipCan) != 0:
        if Index == count:
            Hold = 'Cancellation of business debt, Partnership Schedule K-1'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPHSA) != 0 or get_currency(IANROTHINC.SPHSA) != 0:
        if Index == count:
            Hold = 'HSA distributions, federal Form 8889'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPAltTrade) != 0 or get_currency(IANROTHINC.SPAltTrade) != 0:
        if Index == count:
            Hold = 'Alternative trade adjustment assistance payments'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPRecapTuit) != 0 or get_currency(IANROTHINC.SPRecapTuit) != 0:
        if Index == count:
            Hold = 'Recapture of prior year tuition and fees deduction'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPRecapChar) != 0 or get_currency(IANROTHINC.SPRecapChar) != 0:
        if Index == count:
            Hold = 'Recapture of charitable contribution deduction'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TP5471) != 0 or get_currency(IANROTHINC.SP5471) != 0:
        if Index == count:
            Hold = 'Income from a foreign corporation, federal Form 5471'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPHobby) != 0 or get_currency(IANROTHINC.SPHobby) != 0:
        if Index == count:
            Hold = 'Hobby income'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TP8621) != 0 or get_currency(IANROTHINC.SP8621) != 0:
        if Index == count:
            Hold = 'Income or loss from Section 1291, federal Form 8621'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPDefDist) != 0 or get_currency(IANROTHINC.SPDefDist) != 0:
        if Index == count:
            Hold = 'Loss on excess deferral distribution'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPDisaster) != 0 or get_currency(IANROTHINC.SPDisaster) != 0:
        if Index == count:
            Hold = 'Disaster relief payments'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPFoster) != 0 or get_currency(IANROTHINC.SPFoster) != 0:
        if Index == count:
            Hold = 'Medicaid waiver payments to care provider'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPCredAdj) != 0 or get_currency(IANROTHINC.SPCredAdj) != 0:
        if Index == count:
            Hold = 'Credit adjustment income, federal Forms 6478 and 8864'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPPYNPTC) != 0 or get_currency(IANROTHINC.SPPYNPTC) != 0:
        if Index == count:
            Hold = 'Net Premium Tax Credit'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TP1099QA) != 0 or get_currency(IANROTHINC.SP1099QA) != 0:
        if Index == count:
            Hold = 'Distributions from ABLE account'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPAirline) != 0 or get_currency(IANROTHINC.SPAirline) != 0:
        if Index == count:
            Hold = 'Qualified airline payments'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TP1099B) != 0 or get_currency(IANROTHINC.SP1099B) != 0:
        if Index == count:
            Hold = 'Foreign currency transaction'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPIAABLE) != 0 or get_currency(IANROTHINC.SPIAABLE) != 0:
        if Index == count:
            Hold = 'Distributions from an Iowa ABLE account'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPBusPass) != 0 or get_currency(IANROTHINC.SPBusPass) != 0:
        if Index == count:
            Hold = 'Employer provided bus pass or transportation expenses'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPFarmLoss) != 0 or get_currency(IANROTHINC.SPFarmLoss) != 0:
        if Index == count:
            Hold = 'Section 461(j) excess farm loss limitation adjustments'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TP8824) != 0 or get_currency(IANROTHINC.SP8824) != 0:
        if Index == count:
            Hold = 'IA 8824 worksheet, due to nonconformity'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPStudLoanDis) != 0 or get_currency(IANROTHINC.SPStudLoanDis) != 0:
        if Index == count:
            Hold = 'Discharge of student loan debt - death or disability'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TP4684) != 0 or get_currency(IANROTHINC.SP4684) != 0:
        if Index == count:
            Hold = 'IA 4684 worksheet, due to nonconformity'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TP3903) != 0 or get_currency(IANROTHINC.SP3903) != 0:
        if Index == count:
            Hold = 'IA 3903 worksheet line 8a, due to nonconformity'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPBusInt) != 0 or get_currency(IANROTHINC.SPBusInt) != 0:
        if Index == count:
            Hold = 'Business interest expense limitation, due to nonconformity'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPEntExp) != 0 or get_currency(IANROTHINC.SPEntExp) != 0:
        if Index == count:
            Hold = 'Entertainment expenses, due to nonconformity'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TP2106) != 0 or get_currency(IANROTHINC.SP2106) != 0:
        if Index == count:
            Hold = 'IA 2106 worksheet line 8, due to nonconformity'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPOthNC) != 0 or get_currency(IANROTHINC.SPOthNC) != 0:
        if Index == count:
            Hold = 'Other nonconformity adjustments'
            count = 99
        else:
            count = count + 1
    return Hold

def Names_Calculation():
    return get_string(IAREQUIRED.CombNames)

def Print_Calculation():
    if get_currency(IANROTHINC.TPTot) != 0 or get_currency(IANROTHINC.SPTot) != 0:
        return 1
    else:
        return 0

def SP1099B_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SP1099B)
    else:
        return 0

def SP1099QA_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SP1099QA)
    else:
        return 0

def SP2106_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SP2106)
    else:
        return 0

def SP3903_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SP3903)
    else:
        return 0

def SP4684_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SP4684)
    else:
        return 0

def SP5471_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SP5471)
    else:
        return 0

def SP8621_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SP8621)
    else:
        return 0

def SP8814_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SP8814)
    else:
        return 0

def SP8824_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SP8824)
    else:
        return 0

def SPAirline_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPAirline)
    else:
        return 0

def SPAlaska_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPAlaska)
    else:
        return 0

def SPAltTrade_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPAltTrade)
    else:
        return 0

def SPAmount_Calculation(Index):
    count = Integer()

    Hold = Currency()
    count = 0
    Hold = 0
    if get_currency(IANROTHINC.TPOth1) != 0 or get_currency(IANROTHINC.SPOth1) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPOth1)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPOth2) != 0 or get_currency(IANROTHINC.SPOth2) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPOth2)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPBabySit) != 0 or get_currency(IANROTHINC.SPBabySit) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPBabySit)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPBonus) != 0 or get_currency(IANROTHINC.SPBonus) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPBonus)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPIAEd) != 0 or get_currency(IANROTHINC.SPIAEd) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPIAEd)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPDirector) != 0 or get_currency(IANROTHINC.SPDirector) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPDirector)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPIntangDrill) != 0 or get_currency(IANROTHINC.SPIntangDrill) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPIntangDrill)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPExecutor) != 0 or get_currency(IANROTHINC.SPExecutor) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPExecutor)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPFirstHmBuy) != 0 or get_currency(IANROTHINC.SPFirstHmBuy) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPFirstHmBuy)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPK1) != 0 or get_currency(IANROTHINC.SPK1) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPK1)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPRefundCr) != 0 or get_currency(IANROTHINC.SPRefundCr) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPRefundCr)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPStRefund) != 0 or get_currency(IANROTHINC.SPStRefund) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPStRefund)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPDepl) != 0 or get_currency(IANROTHINC.SPDepl) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPDepl)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPJury) != 0 or get_currency(IANROTHINC.SPJury) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPJury)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPPerRent) != 0 or get_currency(IANROTHINC.SPPerRent) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPPerRent)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TP8814) != 0 or get_currency(IANROTHINC.SP8814) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SP8814)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPMSA) != 0 or get_currency(IANROTHINC.SPMSA) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPMSA)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPMedMSA) != 0 or get_currency(IANROTHINC.SPMedMSA) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPMedMSA)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPLTC) != 0 or get_currency(IANROTHINC.SPLTC) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPLTC)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPMisc) != 0 or get_currency(IANROTHINC.SPMisc) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPMisc)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPAlaska) != 0 or get_currency(IANROTHINC.SPAlaska) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPAlaska)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPCoverdell) != 0 or get_currency(IANROTHINC.SPCoverdell) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPCoverdell)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPCanceled) != 0 or get_currency(IANROTHINC.SPCanceled) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPCanceled)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPPshipCan) != 0 or get_currency(IANROTHINC.SPPshipCan) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPPshipCan)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPHSA) != 0 or get_currency(IANROTHINC.SPHSA) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPHSA)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPAltTrade) != 0 or get_currency(IANROTHINC.SPAltTrade) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPAltTrade)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPRecapTuit) != 0 or get_currency(IANROTHINC.SPRecapTuit) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPRecapTuit)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPRecapChar) != 0 or get_currency(IANROTHINC.SPRecapChar) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPRecapChar)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TP5471) != 0 or get_currency(IANROTHINC.SP5471) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SP5471)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPHobby) != 0 or get_currency(IANROTHINC.SPHobby) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPHobby)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TP8621) != 0 or get_currency(IANROTHINC.SP8621) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SP8621)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPDefDist) != 0 or get_currency(IANROTHINC.SPDefDist) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPDefDist)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPDisaster) != 0 or get_currency(IANROTHINC.SPDisaster) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPDisaster)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPFoster) != 0 or get_currency(IANROTHINC.SPFoster) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPFoster)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPCredAdj) != 0 or get_currency(IANROTHINC.SPCredAdj) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPCredAdj)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPPYNPTC) != 0 or get_currency(IANROTHINC.SPPYNPTC) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPPYNPTC)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TP1099QA) != 0 or get_currency(IANROTHINC.SP1099QA) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SP1099QA)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPAirline) != 0 or get_currency(IANROTHINC.SPAirline) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPAirline)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TP1099B) != 0 or get_currency(IANROTHINC.SP1099B) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SP1099B)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPIAABLE) != 0 or get_currency(IANROTHINC.SPIAABLE) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPIAABLE)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPBusPass) != 0 or get_currency(IANROTHINC.SPBusPass) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPBusPass)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPFarmLoss) != 0 or get_currency(IANROTHINC.SPFarmLoss) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPFarmLoss)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TP8824) != 0 or get_currency(IANROTHINC.SP8824) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SP8824)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPStudLoanDis) != 0 or get_currency(IANROTHINC.SPStudLoanDis) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPStudLoanDis)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TP4684) != 0 or get_currency(IANROTHINC.SP4684) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SP4684)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TP3903) != 0 or get_currency(IANROTHINC.SP3903) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SP3903)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPBusInt) != 0 or get_currency(IANROTHINC.SPBusInt) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPBusInt)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPEntExp) != 0 or get_currency(IANROTHINC.SPEntExp) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPEntExp)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TP2106) != 0 or get_currency(IANROTHINC.SP2106) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SP2106)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPOthNC) != 0 or get_currency(IANROTHINC.SPOthNC) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.SPOthNC)
            count = 99
        else:
            count = count + 1
    return Hold

def SPBabySit_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPBabySit)
    else:
        return 0

def SPBonus_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPBonus)
    else:
        return 0

def SPBusInt_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPBusInt)
    else:
        return 0

def SPBusPass_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPBusPass)
    else:
        return 0

def SPCanceled_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPCanceled)
    else:
        return 0

def SPCoverdell_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPCoverdell)
    else:
        return 0

def SPCredAdj_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPCredAdj)
    else:
        return 0

def SPDefDist_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPDefDist)
    else:
        return 0

def SPDepl_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPDepl)
    else:
        return 0

def SPDirector_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPDirector)
    else:
        return 0

def SPDisaster_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPDisaster)
    else:
        return 0

def SPEntExp_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPEntExp)
    else:
        return 0

def SPExecutor_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPExecutor)
    else:
        return 0

def SPFarmLoss_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPFarmLoss)
    else:
        return 0

def SPFirstHmBuy_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPFirstHmBuy)
    else:
        return 0

def SPFoster_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPFoster)
    else:
        return 0

def SPHobby_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPHobby)
    else:
        return 0

def SPHSA_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPHSA)
    else:
        return 0

def SPIAABLE_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPIAABLE)
    else:
        return 0

def SPIAEd_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPIAEd)
    else:
        return 0

def SPIntangDrill_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPIntangDrill)
    else:
        return 0

def SPJury_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPJury)
    else:
        return 0

def SPK1_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPK1)
    else:
        return 0

def SPLTC_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPLTC)
    else:
        return 0

def SPMedMSA_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPMedMSA)
    else:
        return 0

def SPMisc_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPMisc)
    else:
        return 0

def SPMSA_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPMSA)
    else:
        return 0

def SPName_Calculation():
    return get_string(USWBasicInfo.SPCommon)

def SPOth1_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPOth1)
    else:
        return 0

def SPOth2_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPOth2)
    else:
        return 0

def SPOthNC_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPOthNC)
    else:
        return 0

def SPPerRent_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPPerRent)
    else:
        return 0

def SPPshipCan_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPPshipCan)
    else:
        return 0

def SPPYNPTC_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPPYNPTC)
    else:
        return 0

def SPRecapChar_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPRecapChar)
    else:
        return 0

def SPRecapTuit_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPRecapTuit)
    else:
        return 0

def SPRefundCr_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPRefundCr)
    else:
        return 0

def SPStRefund_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPStRefund)
    else:
        return 0

def SPStudLoanDis_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IAWOTHINC.SPStudLoanDis)
    else:
        return 0

def SPTot_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True:
        return get_currency(IANROTHINC.SPOth1) + get_currency(IANROTHINC.SPOth2) + get_currency(IANROTHINC.SPBabySit) + get_currency(IANROTHINC.SPBonus) + get_currency(IANROTHINC.SPIAEd) + get_currency(IANROTHINC.SPDirector) + get_currency(IANROTHINC.SPIntangDrill) + get_currency(IANROTHINC.SPExecutor) + get_currency(IANROTHINC.SPFirstHmBuy) + get_currency(IANROTHINC.SPK1) + get_currency(IANROTHINC.SPRefundCr) + get_currency(IANROTHINC.SPStRefund) + get_currency(IANROTHINC.SPDepl) + get_currency(IANROTHINC.SPJury) + get_currency(IANROTHINC.SPPerRent) + get_currency(IANROTHINC.SP8814) + get_currency(IANROTHINC.SPMSA) + get_currency(IANROTHINC.SPMedMSA) + get_currency(IANROTHINC.SPLTC) + get_currency(IANROTHINC.SPMisc) + get_currency(IANROTHINC.SPAlaska) + get_currency(IANROTHINC.SPCoverdell) + get_currency(IANROTHINC.SPCanceled) + get_currency(IANROTHINC.SPPshipCan) + get_currency(IANROTHINC.SPHSA) + get_currency(IANROTHINC.SPAltTrade) + get_currency(IANROTHINC.SPRecapTuit) + get_currency(IANROTHINC.SPRecapChar) + get_currency(IANROTHINC.SP5471) + get_currency(IANROTHINC.SPHobby) + get_currency(IANROTHINC.SP8621) + get_currency(IANROTHINC.SPDefDist) + get_currency(IANROTHINC.SPDisaster) + get_currency(IANROTHINC.SPFoster) + get_currency(IANROTHINC.SPCredAdj) + get_currency(IANROTHINC.SPPYNPTC) + get_currency(IANROTHINC.SP1099QA) + get_currency(IANROTHINC.SPIAABLE) + get_currency(IANROTHINC.SPBusPass) + get_currency(IANROTHINC.SPAirline) + get_currency(IANROTHINC.SP1099B) + get_currency(IANROTHINC.SPFarmLoss) + get_currency(IANROTHINC.SP8824) + get_currency(IANROTHINC.SPStudLoanDis) + get_currency(IANROTHINC.SP4684) + get_currency(IANROTHINC.SP3903) + get_currency(IANROTHINC.SPBusInt) + get_currency(IANROTHINC.SPEntExp) + get_currency(IANROTHINC.SP2106) + get_currency(IANROTHINC.SPOthNC)
    else:
        return 0

def SSN_Calculation():
    return get_string(IAF1040.SSN)

def TP1099B_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TP1099B)
    else:
        return 0

def TP1099QA_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TP1099QA)
    else:
        return 0

def TP2106_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TP2106)
    else:
        return 0

def TP3903_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TP3903)
    else:
        return 0

def TP4684_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TP4684)
    else:
        return 0

def TP5471_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TP5471)
    else:
        return 0

def TP8621_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TP8621)
    else:
        return 0

def TP8814_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TP8814)
    else:
        return 0

def TP8824_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TP8824)
    else:
        return 0

def TPAirline_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPAirline)
    else:
        return 0

def TPAlaska_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPAlaska)
    else:
        return 0

def TPAltTrade_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPAltTrade)
    else:
        return 0

def TPAmount_Calculation(Index):
    count = Integer()

    Hold = Currency()
    count = 0
    Hold = 0
    if get_currency(IANROTHINC.TPOth1) != 0 or get_currency(IANROTHINC.SPOth1) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPOth1)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPOth2) != 0 or get_currency(IANROTHINC.SPOth2) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPOth2)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPBabySit) != 0 or get_currency(IANROTHINC.SPBabySit) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPBabySit)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPBonus) != 0 or get_currency(IANROTHINC.SPBonus) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPBonus)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPIAEd) != 0 or get_currency(IANROTHINC.SPIAEd) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPIAEd)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPDirector) != 0 or get_currency(IANROTHINC.SPDirector) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPDirector)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPIntangDrill) != 0 or get_currency(IANROTHINC.SPIntangDrill) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPIntangDrill)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPExecutor) != 0 or get_currency(IANROTHINC.SPExecutor) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPExecutor)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPFirstHmBuy) != 0 or get_currency(IANROTHINC.SPFirstHmBuy) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPFirstHmBuy)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPK1) != 0 or get_currency(IANROTHINC.SPK1) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPK1)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPRefundCr) != 0 or get_currency(IANROTHINC.SPRefundCr) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPRefundCr)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPStRefund) != 0 or get_currency(IANROTHINC.SPStRefund) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPStRefund)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPDepl) != 0 or get_currency(IANROTHINC.SPDepl) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPDepl)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPJury) != 0 or get_currency(IANROTHINC.SPJury) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPJury)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPPerRent) != 0 or get_currency(IANROTHINC.SPPerRent) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPPerRent)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TP8814) != 0 or get_currency(IANROTHINC.SP8814) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TP8814)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPMSA) != 0 or get_currency(IANROTHINC.SPMSA) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPMSA)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPMedMSA) != 0 or get_currency(IANROTHINC.SPMedMSA) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPMedMSA)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPLTC) != 0 or get_currency(IANROTHINC.SPLTC) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPLTC)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPMisc) != 0 or get_currency(IANROTHINC.SPMisc) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPMisc)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPAlaska) != 0 or get_currency(IANROTHINC.SPAlaska) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPAlaska)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPCoverdell) != 0 or get_currency(IANROTHINC.SPCoverdell) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPCoverdell)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPCanceled) != 0 or get_currency(IANROTHINC.SPCanceled) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPCanceled)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPPshipCan) != 0 or get_currency(IANROTHINC.SPPshipCan) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPPshipCan)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPHSA) != 0 or get_currency(IANROTHINC.SPHSA) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPHSA)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPAltTrade) != 0 or get_currency(IANROTHINC.SPAltTrade) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPAltTrade)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPRecapTuit) != 0 or get_currency(IANROTHINC.SPRecapTuit) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPRecapTuit)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPRecapChar) != 0 or get_currency(IANROTHINC.SPRecapChar) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPRecapChar)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TP5471) != 0 or get_currency(IANROTHINC.SP5471) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TP5471)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPHobby) != 0 or get_currency(IANROTHINC.SPHobby) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPHobby)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TP8621) != 0 or get_currency(IANROTHINC.SP8621) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TP8621)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPDefDist) != 0 or get_currency(IANROTHINC.SPDefDist) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPDefDist)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPDisaster) != 0 or get_currency(IANROTHINC.SPDisaster) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPDisaster)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPFoster) != 0 or get_currency(IANROTHINC.SPFoster) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPFoster)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPCredAdj) != 0 or get_currency(IANROTHINC.SPCredAdj) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPCredAdj)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPPYNPTC) != 0 or get_currency(IANROTHINC.SPPYNPTC) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPPYNPTC)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TP1099QA) != 0 or get_currency(IANROTHINC.SP1099QA) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TP1099QA)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPAirline) != 0 or get_currency(IANROTHINC.SPAirline) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPAirline)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TP1099B) != 0 or get_currency(IANROTHINC.SP1099B) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TP1099B)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPIAABLE) != 0 or get_currency(IANROTHINC.SPIAABLE) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPIAABLE)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPBusPass) != 0 or get_currency(IANROTHINC.SPBusPass) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPBusPass)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPFarmLoss) != 0 or get_currency(IANROTHINC.SPFarmLoss) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPFarmLoss)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TP8824) != 0 or get_currency(IANROTHINC.SP8824) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TP8824)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPStudLoanDis) != 0 or get_currency(IANROTHINC.SPStudLoanDis) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPStudLoanDis)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TP4684) != 0 or get_currency(IANROTHINC.SP4684) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TP4684)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TP3903) != 0 or get_currency(IANROTHINC.SP3903) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TP3903)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPBusInt) != 0 or get_currency(IANROTHINC.SPBusInt) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPBusInt)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPEntExp) != 0 or get_currency(IANROTHINC.SPEntExp) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPEntExp)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TP2106) != 0 or get_currency(IANROTHINC.SP2106) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TP2106)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHINC.TPOthNC) != 0 or get_currency(IANROTHINC.SPOthNC) != 0:
        if Index == count:
            Hold = get_currency(IANROTHINC.TPOthNC)
            count = 99
        else:
            count = count + 1
    return Hold

def TPBabySit_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPBabySit)
    else:
        return 0

def TPBonus_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPBonus)
    else:
        return 0

def TPBusInt_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPBusInt)
    else:
        return 0

def TPBusPass_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPBusPass)
    else:
        return 0

def TPCanceled_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPCanceled)
    else:
        return 0

def TPCoverdell_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPCoverdell)
    else:
        return 0

def TPCredAdj_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPCredAdj)
    else:
        return 0

def TPDefDist_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPDefDist)
    else:
        return 0

def TPDepl_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPDepl)
    else:
        return 0

def TPDirector_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPDirector)
    else:
        return 0

def TPDisaster_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPDisaster)
    else:
        return 0

def TPEntExp_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPEntExp)
    else:
        return 0

def TPExecutor_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPExecutor)
    else:
        return 0

def TPFarmLoss_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPFarmLoss)
    else:
        return 0

def TPFirstHmBuy_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPFirstHmBuy)
    else:
        return 0

def TPFoster_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPFoster)
    else:
        return 0

def TPHobby_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPHobby)
    else:
        return 0

def TPHSA_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPHSA)
    else:
        return 0

def TPIAABLE_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPIAABLE)
    else:
        return 0

def TPIAEd_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPIAEd)
    else:
        return 0

def TPIntangDrill_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPIntangDrill)
    else:
        return 0

def TPJointAmount_Calculation(Index):
    if get_bool(IAF1040.CombMFS) == True:
        return get_currency(IANROTHINC.TPAmount(Index))
    else:
        return get_currency(IANROTHINC.TPAmount(Index)) + get_currency(IANROTHINC.SPAmount(Index))

def TPJury_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPJury)
    else:
        return 0

def TPK1_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPK1)
    else:
        return 0

def TPLTC_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPLTC)
    else:
        return 0

def TPMedMSA_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPMedMSA)
    else:
        return 0

def TPMisc_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPMisc)
    else:
        return 0

def TPMSA_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPMSA)
    else:
        return 0

def TPName_Calculation():
    return get_string(USWBasicInfo.TPCommon)

def TPOth1_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPOth1)
    else:
        return 0

def TPOth2_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPOth2)
    else:
        return 0

def TPOthNC_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPOthNC)
    else:
        return 0

def TPPerRent_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPPerRent)
    else:
        return 0

def TPPshipCan_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPPshipCan)
    else:
        return 0

def TPPYNPTC_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPPYNPTC)
    else:
        return 0

def TPRecapChar_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPRecapChar)
    else:
        return 0

def TPRecapTuit_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPRecapTuit)
    else:
        return 0

def TPRefundCr_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPRefundCr)
    else:
        return 0

def TPStRefund_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPStRefund)
    else:
        return 0

def TPStudLoanDis_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IAWOTHINC.TPStudLoanDis)
    else:
        return 0

def TPTot_Calculation():
    if ( IAFS() == 2 and get_bool(IAF126.SpRes) == False )  or get_bool(IAF126.TpRes) == False:
        return get_currency(IANROTHINC.TPOth1) + get_currency(IANROTHINC.TPOth2) + get_currency(IANROTHINC.TPBabySit) + get_currency(IANROTHINC.TPBonus) + get_currency(IANROTHINC.TPIAEd) + get_currency(IANROTHINC.TPDirector) + get_currency(IANROTHINC.TPIntangDrill) + get_currency(IANROTHINC.TPExecutor) + get_currency(IANROTHINC.TPFirstHmBuy) + get_currency(IANROTHINC.TPK1) + get_currency(IANROTHINC.TPRefundCr) + get_currency(IANROTHINC.TPStRefund) + get_currency(IANROTHINC.TPDepl) + get_currency(IANROTHINC.TPJury) + get_currency(IANROTHINC.TPPerRent) + get_currency(IANROTHINC.TP8814) + get_currency(IANROTHINC.TPMSA) + get_currency(IANROTHINC.TPMedMSA) + get_currency(IANROTHINC.TPLTC) + get_currency(IANROTHINC.TPMisc) + get_currency(IANROTHINC.TPAlaska) + get_currency(IANROTHINC.TPCoverdell) + get_currency(IANROTHINC.TPCanceled) + get_currency(IANROTHINC.TPPshipCan) + get_currency(IANROTHINC.TPHSA) + get_currency(IANROTHINC.TPAltTrade) + get_currency(IANROTHINC.TPRecapTuit) + get_currency(IANROTHINC.TPRecapChar) + get_currency(IANROTHINC.TP5471) + get_currency(IANROTHINC.TPHobby) + get_currency(IANROTHINC.TP8621) + get_currency(IANROTHINC.TPDefDist) + get_currency(IANROTHINC.TPDisaster) + get_currency(IANROTHINC.TPFoster) + get_currency(IANROTHINC.TPCredAdj) + get_currency(IANROTHINC.TPPYNPTC) + get_currency(IANROTHINC.TP1099QA) + get_currency(IANROTHINC.TPIAABLE) + get_currency(IANROTHINC.TPBusPass) + get_currency(IANROTHINC.TPAirline) + get_currency(IANROTHINC.TP1099B) + get_currency(IANROTHINC.TPFarmLoss) + get_currency(IANROTHINC.TP8824) + get_currency(IANROTHINC.TPStudLoanDis) + get_currency(IANROTHINC.TP4684) + get_currency(IANROTHINC.TP3903) + get_currency(IANROTHINC.TPBusInt) + get_currency(IANROTHINC.TPEntExp) + get_currency(IANROTHINC.TP2106) + get_currency(IANROTHINC.TPOthNC)
    else:
        return 0

def Txt1_Calculation():
    return get_string(IAWOTHINC.Txt1)

def Txt2_Calculation():
    return get_string(IAWOTHINC.Txt2)


