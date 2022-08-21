from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Code_Calculation(Index):
    count = Integer()

    Hold = String()
    count = 0
    Hold = ''
    if GetCurrency(IANROthInc.TPOth1) != 0 or GetCurrency(IANROthInc.SPOth1) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPOth2) != 0 or GetCurrency(IANROthInc.SPOth2) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPBabySit) != 0 or GetCurrency(IANROthInc.SPBabySit) != 0:
        if Index == count:
            Hold = 'a'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPBonus) != 0 or GetCurrency(IANROthInc.SPBonus) != 0:
        if Index == count:
            Hold = 'b'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPIAEd) != 0 or GetCurrency(IANROthInc.SPIAEd) != 0:
        if Index == count:
            Hold = 'd'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPDirector) != 0 or GetCurrency(IANROthInc.SPDirector) != 0:
        if Index == count:
            Hold = 'e'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPIntangDrill) != 0 or GetCurrency(IANROthInc.SPIntangDrill) != 0:
        if Index == count:
            Hold = 'f'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPExecutor) != 0 or GetCurrency(IANROthInc.SPExecutor) != 0:
        if Index == count:
            Hold = 'g'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPFirstHmBuy) != 0 or GetCurrency(IANROthInc.SPFirstHmBuy) != 0:
        if Index == count:
            Hold = 'h'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPK1) != 0 or GetCurrency(IANROthInc.SPK1) != 0:
        if Index == count:
            Hold = 'i'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPRefundCr) != 0 or GetCurrency(IANROthInc.SPRefundCr) != 0:
        if Index == count:
            Hold = 'j'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPStRefund) != 0 or GetCurrency(IANROthInc.SPStRefund) != 0:
        if Index == count:
            Hold = 'k'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPDepl) != 0 or GetCurrency(IANROthInc.SPDepl) != 0:
        if Index == count:
            Hold = 'l'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPJury) != 0 or GetCurrency(IANROthInc.SPJury) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPPerRent) != 0 or GetCurrency(IANROthInc.SPPerRent) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TP8814) != 0 or GetCurrency(IANROthInc.SP8814) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPMSA) != 0 or GetCurrency(IANROthInc.SPMSA) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPMedMSA) != 0 or GetCurrency(IANROthInc.SPMedMSA) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPLTC) != 0 or GetCurrency(IANROthInc.SPLTC) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPMisc) != 0 or GetCurrency(IANROthInc.SPMisc) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPAlaska) != 0 or GetCurrency(IANROthInc.SPAlaska) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPCoverdell) != 0 or GetCurrency(IANROthInc.SPCoverdell) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPCanceled) != 0 or GetCurrency(IANROthInc.SPCanceled) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPPshipCan) != 0 or GetCurrency(IANROthInc.SPPshipCan) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPHSA) != 0 or GetCurrency(IANROthInc.SPHSA) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPAltTrade) != 0 or GetCurrency(IANROthInc.SPAltTrade) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPRecapTuit) != 0 or GetCurrency(IANROthInc.SPRecapTuit) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPRecapChar) != 0 or GetCurrency(IANROthInc.SPRecapChar) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TP5471) != 0 or GetCurrency(IANROthInc.SP5471) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPHobby) != 0 or GetCurrency(IANROthInc.SPHobby) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TP8621) != 0 or GetCurrency(IANROthInc.SP8621) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPDefDist) != 0 or GetCurrency(IANROthInc.SPDefDist) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPDisaster) != 0 or GetCurrency(IANROthInc.SPDisaster) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPFoster) != 0 or GetCurrency(IANROthInc.SPFoster) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPCredAdj) != 0 or GetCurrency(IANROthInc.SPCredAdj) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPPYNPTC) != 0 or GetCurrency(IANROthInc.SPPYNPTC) != 0:
        if Index == count:
            Hold = 'n'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TP1099QA) != 0 or GetCurrency(IANROthInc.SP1099QA) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPAirline) != 0 or GetCurrency(IANROthInc.SPAirline) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TP1099B) != 0 or GetCurrency(IANROthInc.SP1099B) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPIAABLE) != 0 or GetCurrency(IANROthInc.SPIAABLE) != 0:
        if Index == count:
            Hold = 'o'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPBusPass) != 0 or GetCurrency(IANROthInc.SPBusPass) != 0:
        if Index == count:
            Hold = 'p'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPFarmLoss) != 0 or GetCurrency(IANROthInc.SPFarmLoss) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TP8824) != 0 or GetCurrency(IANROthInc.SP8824) != 0:
        if Index == count:
            Hold = 'q'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPStudLoanDis) != 0 or GetCurrency(IANROthInc.SPStudLoanDis) != 0:
        if Index == count:
            Hold = 'r'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TP4684) != 0 or GetCurrency(IANROthInc.SP4684) != 0:
        if Index == count:
            Hold = 's'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TP3903) != 0 or GetCurrency(IANROthInc.SP3903) != 0:
        if Index == count:
            Hold = 't'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPBusInt) != 0 or GetCurrency(IANROthInc.SPBusInt) != 0:
        if Index == count:
            Hold = 'u'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPEntExp) != 0 or GetCurrency(IANROthInc.SPEntExp) != 0:
        if Index == count:
            Hold = 'v'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TP2106) != 0 or GetCurrency(IANROthInc.SP2106) != 0:
        if Index == count:
            Hold = 'w'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPOthNC) != 0 or GetCurrency(IANROthInc.SPOthNC) != 0:
        if Index == count:
            Hold = 'x'
            count = 99
        else:
            count = count + 1
    ReturnVal = Hold

def Desc_Calculation():
    Total = Currency()
    Total = GetCurrency(IANROthInc.TPTot) + GetCurrency(IANROthInc.SPTot)
    ReturnVal = CStr(Total)

def Description_Calculation(Index):
    count = Integer()

    Hold = String()
    count = 0
    Hold = ''
    if GetCurrency(IANROthInc.TPOth1) != 0 or GetCurrency(IANROthInc.SPOth1) != 0:
        if Index == count:
            Hold = GetString(IANROthInc.Txt1)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPOth2) != 0 or GetCurrency(IANROthInc.SPOth2) != 0:
        if Index == count:
            Hold = GetString(IANROthInc.Txt2)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPBabySit) != 0 or GetCurrency(IANROthInc.SPBabySit) != 0:
        if Index == count:
            Hold = 'Baby-sitting income not reported on federal Schedule C'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPBonus) != 0 or GetCurrency(IANROthInc.SPBonus) != 0:
        if Index == count:
            Hold = 'Bonus depreciation/section 179 adjustment'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPIAEd) != 0 or GetCurrency(IANROthInc.SPIAEd) != 0:
        if Index == count:
            Hold = 'College Savings Iowa or Iowa Advisor 529 Plan'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPDirector) != 0 or GetCurrency(IANROthInc.SPDirector) != 0:
        if Index == count:
            Hold = 'Director\'s fees'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPIntangDrill) != 0 or GetCurrency(IANROthInc.SPIntangDrill) != 0:
        if Index == count:
            Hold = 'Drilling'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPExecutor) != 0 or GetCurrency(IANROthInc.SPExecutor) != 0:
        if Index == count:
            Hold = 'Executor\'s fees'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPFirstHmBuy) != 0 or GetCurrency(IANROthInc.SPFirstHmBuy) != 0:
        if Index == count:
            Hold = 'First-time homebuyers account non-qualifying withdrawals'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPK1) != 0 or GetCurrency(IANROthInc.SPK1) != 0:
        if Index == count:
            Hold = 'Partnership income and/or S Corporation income'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPRefundCr) != 0 or GetCurrency(IANROthInc.SPRefundCr) != 0:
        if Index == count:
            Hold = 'Refundable Iowa credits'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPStRefund) != 0 or GetCurrency(IANROthInc.SPStRefund) != 0:
        if Index == count:
            Hold = 'State income tax refunds'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPDepl) != 0 or GetCurrency(IANROthInc.SPDepl) != 0:
        if Index == count:
            Hold = 'Wells'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPJury) != 0 or GetCurrency(IANROthInc.SPJury) != 0:
        if Index == count:
            Hold = 'Jury pay'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPPerRent) != 0 or GetCurrency(IANROthInc.SPPerRent) != 0:
        if Index == count:
            Hold = 'Income from personal property'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TP8814) != 0 or GetCurrency(IANROthInc.SP8814) != 0:
        if Index == count:
            Hold = 'Child\'s income amount, federal Form 8814'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPMSA) != 0 or GetCurrency(IANROthInc.SPMSA) != 0:
        if Index == count:
            Hold = 'MSA distributions, federal Form 8853'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPMedMSA) != 0 or GetCurrency(IANROthInc.SPMedMSA) != 0:
        if Index == count:
            Hold = 'Medicare Advantage distributions, federal Form 8853'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPLTC) != 0 or GetCurrency(IANROthInc.SPLTC) != 0:
        if Index == count:
            Hold = 'Long-term care distribution, federal Form 8853'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPMisc) != 0 or GetCurrency(IANROthInc.SPMisc) != 0:
        if Index == count:
            Hold = 'Form 1099-MISC, boxes 3 or 8'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPAlaska) != 0 or GetCurrency(IANROthInc.SPAlaska) != 0:
        if Index == count:
            Hold = 'Alaska Permanent Fund dividends'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPCoverdell) != 0 or GetCurrency(IANROthInc.SPCoverdell) != 0:
        if Index == count:
            Hold = 'Coverdell ESA Or Qualified Tuition Program'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPCanceled) != 0 or GetCurrency(IANROthInc.SPCanceled) != 0:
        if Index == count:
            Hold = 'Cancellation of nonbusiness debt, federal Form 1099-C'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPPshipCan) != 0 or GetCurrency(IANROthInc.SPPshipCan) != 0:
        if Index == count:
            Hold = 'Cancellation of business debt, Partnership Schedule K-1'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPHSA) != 0 or GetCurrency(IANROthInc.SPHSA) != 0:
        if Index == count:
            Hold = 'HSA distributions, federal Form 8889'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPAltTrade) != 0 or GetCurrency(IANROthInc.SPAltTrade) != 0:
        if Index == count:
            Hold = 'Alternative trade adjustment assistance payments'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPRecapTuit) != 0 or GetCurrency(IANROthInc.SPRecapTuit) != 0:
        if Index == count:
            Hold = 'Recapture of prior year tuition and fees deduction'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPRecapChar) != 0 or GetCurrency(IANROthInc.SPRecapChar) != 0:
        if Index == count:
            Hold = 'Recapture of charitable contribution deduction'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TP5471) != 0 or GetCurrency(IANROthInc.SP5471) != 0:
        if Index == count:
            Hold = 'Income from a foreign corporation, federal Form 5471'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPHobby) != 0 or GetCurrency(IANROthInc.SPHobby) != 0:
        if Index == count:
            Hold = 'Hobby income'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TP8621) != 0 or GetCurrency(IANROthInc.SP8621) != 0:
        if Index == count:
            Hold = 'Income or loss from Section 1291, federal Form 8621'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPDefDist) != 0 or GetCurrency(IANROthInc.SPDefDist) != 0:
        if Index == count:
            Hold = 'Loss on excess deferral distribution'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPDisaster) != 0 or GetCurrency(IANROthInc.SPDisaster) != 0:
        if Index == count:
            Hold = 'Disaster relief payments'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPFoster) != 0 or GetCurrency(IANROthInc.SPFoster) != 0:
        if Index == count:
            Hold = 'Medicaid waiver payments to care provider'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPCredAdj) != 0 or GetCurrency(IANROthInc.SPCredAdj) != 0:
        if Index == count:
            Hold = 'Credit adjustment income, federal Forms 6478 and 8864'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPPYNPTC) != 0 or GetCurrency(IANROthInc.SPPYNPTC) != 0:
        if Index == count:
            Hold = 'Net Premium Tax Credit'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TP1099QA) != 0 or GetCurrency(IANROthInc.SP1099QA) != 0:
        if Index == count:
            Hold = 'Distributions from ABLE account'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPAirline) != 0 or GetCurrency(IANROthInc.SPAirline) != 0:
        if Index == count:
            Hold = 'Qualified airline payments'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TP1099B) != 0 or GetCurrency(IANROthInc.SP1099B) != 0:
        if Index == count:
            Hold = 'Foreign currency transaction'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPIAABLE) != 0 or GetCurrency(IANROthInc.SPIAABLE) != 0:
        if Index == count:
            Hold = 'Distributions from an Iowa ABLE account'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPBusPass) != 0 or GetCurrency(IANROthInc.SPBusPass) != 0:
        if Index == count:
            Hold = 'Employer provided bus pass or transportation expenses'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPFarmLoss) != 0 or GetCurrency(IANROthInc.SPFarmLoss) != 0:
        if Index == count:
            Hold = 'Section 461(j) excess farm loss limitation adjustments'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TP8824) != 0 or GetCurrency(IANROthInc.SP8824) != 0:
        if Index == count:
            Hold = 'IA 8824 worksheet, due to nonconformity'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPStudLoanDis) != 0 or GetCurrency(IANROthInc.SPStudLoanDis) != 0:
        if Index == count:
            Hold = 'Discharge of student loan debt - death or disability'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TP4684) != 0 or GetCurrency(IANROthInc.SP4684) != 0:
        if Index == count:
            Hold = 'IA 4684 worksheet, due to nonconformity'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TP3903) != 0 or GetCurrency(IANROthInc.SP3903) != 0:
        if Index == count:
            Hold = 'IA 3903 worksheet line 8a, due to nonconformity'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPBusInt) != 0 or GetCurrency(IANROthInc.SPBusInt) != 0:
        if Index == count:
            Hold = 'Business interest expense limitation, due to nonconformity'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPEntExp) != 0 or GetCurrency(IANROthInc.SPEntExp) != 0:
        if Index == count:
            Hold = 'Entertainment expenses, due to nonconformity'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TP2106) != 0 or GetCurrency(IANROthInc.SP2106) != 0:
        if Index == count:
            Hold = 'IA 2106 worksheet line 8, due to nonconformity'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPOthNC) != 0 or GetCurrency(IANROthInc.SPOthNC) != 0:
        if Index == count:
            Hold = 'Other nonconformity adjustments'
            count = 99
        else:
            count = count + 1
    ReturnVal = Hold

def Names_Calculation():
    ReturnVal = GetString(IARequired.CombNames)

def Print_Calculation():
    if GetCurrency(IANROthInc.TPTot) != 0 or GetCurrency(IANROthInc.SPTot) != 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def SP1099B_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SP1099B)
    else:
        ReturnVal = 0

def SP1099QA_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SP1099QA)
    else:
        ReturnVal = 0

def SP2106_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SP2106)
    else:
        ReturnVal = 0

def SP3903_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SP3903)
    else:
        ReturnVal = 0

def SP4684_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SP4684)
    else:
        ReturnVal = 0

def SP5471_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SP5471)
    else:
        ReturnVal = 0

def SP8621_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SP8621)
    else:
        ReturnVal = 0

def SP8814_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SP8814)
    else:
        ReturnVal = 0

def SP8824_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SP8824)
    else:
        ReturnVal = 0

def SPAirline_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPAirline)
    else:
        ReturnVal = 0

def SPAlaska_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPAlaska)
    else:
        ReturnVal = 0

def SPAltTrade_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPAltTrade)
    else:
        ReturnVal = 0

def SPAmount_Calculation(Index):
    count = Integer()

    Hold = Currency()
    count = 0
    Hold = 0
    if GetCurrency(IANROthInc.TPOth1) != 0 or GetCurrency(IANROthInc.SPOth1) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPOth1)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPOth2) != 0 or GetCurrency(IANROthInc.SPOth2) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPOth2)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPBabySit) != 0 or GetCurrency(IANROthInc.SPBabySit) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPBabySit)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPBonus) != 0 or GetCurrency(IANROthInc.SPBonus) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPBonus)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPIAEd) != 0 or GetCurrency(IANROthInc.SPIAEd) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPIAEd)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPDirector) != 0 or GetCurrency(IANROthInc.SPDirector) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPDirector)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPIntangDrill) != 0 or GetCurrency(IANROthInc.SPIntangDrill) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPIntangDrill)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPExecutor) != 0 or GetCurrency(IANROthInc.SPExecutor) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPExecutor)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPFirstHmBuy) != 0 or GetCurrency(IANROthInc.SPFirstHmBuy) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPFirstHmBuy)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPK1) != 0 or GetCurrency(IANROthInc.SPK1) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPK1)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPRefundCr) != 0 or GetCurrency(IANROthInc.SPRefundCr) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPRefundCr)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPStRefund) != 0 or GetCurrency(IANROthInc.SPStRefund) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPStRefund)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPDepl) != 0 or GetCurrency(IANROthInc.SPDepl) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPDepl)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPJury) != 0 or GetCurrency(IANROthInc.SPJury) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPJury)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPPerRent) != 0 or GetCurrency(IANROthInc.SPPerRent) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPPerRent)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TP8814) != 0 or GetCurrency(IANROthInc.SP8814) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SP8814)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPMSA) != 0 or GetCurrency(IANROthInc.SPMSA) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPMSA)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPMedMSA) != 0 or GetCurrency(IANROthInc.SPMedMSA) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPMedMSA)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPLTC) != 0 or GetCurrency(IANROthInc.SPLTC) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPLTC)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPMisc) != 0 or GetCurrency(IANROthInc.SPMisc) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPMisc)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPAlaska) != 0 or GetCurrency(IANROthInc.SPAlaska) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPAlaska)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPCoverdell) != 0 or GetCurrency(IANROthInc.SPCoverdell) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPCoverdell)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPCanceled) != 0 or GetCurrency(IANROthInc.SPCanceled) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPCanceled)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPPshipCan) != 0 or GetCurrency(IANROthInc.SPPshipCan) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPPshipCan)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPHSA) != 0 or GetCurrency(IANROthInc.SPHSA) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPHSA)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPAltTrade) != 0 or GetCurrency(IANROthInc.SPAltTrade) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPAltTrade)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPRecapTuit) != 0 or GetCurrency(IANROthInc.SPRecapTuit) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPRecapTuit)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPRecapChar) != 0 or GetCurrency(IANROthInc.SPRecapChar) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPRecapChar)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TP5471) != 0 or GetCurrency(IANROthInc.SP5471) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SP5471)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPHobby) != 0 or GetCurrency(IANROthInc.SPHobby) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPHobby)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TP8621) != 0 or GetCurrency(IANROthInc.SP8621) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SP8621)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPDefDist) != 0 or GetCurrency(IANROthInc.SPDefDist) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPDefDist)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPDisaster) != 0 or GetCurrency(IANROthInc.SPDisaster) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPDisaster)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPFoster) != 0 or GetCurrency(IANROthInc.SPFoster) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPFoster)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPCredAdj) != 0 or GetCurrency(IANROthInc.SPCredAdj) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPCredAdj)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPPYNPTC) != 0 or GetCurrency(IANROthInc.SPPYNPTC) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPPYNPTC)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TP1099QA) != 0 or GetCurrency(IANROthInc.SP1099QA) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SP1099QA)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPAirline) != 0 or GetCurrency(IANROthInc.SPAirline) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPAirline)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TP1099B) != 0 or GetCurrency(IANROthInc.SP1099B) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SP1099B)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPIAABLE) != 0 or GetCurrency(IANROthInc.SPIAABLE) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPIAABLE)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPBusPass) != 0 or GetCurrency(IANROthInc.SPBusPass) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPBusPass)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPFarmLoss) != 0 or GetCurrency(IANROthInc.SPFarmLoss) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPFarmLoss)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TP8824) != 0 or GetCurrency(IANROthInc.SP8824) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SP8824)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPStudLoanDis) != 0 or GetCurrency(IANROthInc.SPStudLoanDis) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPStudLoanDis)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TP4684) != 0 or GetCurrency(IANROthInc.SP4684) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SP4684)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TP3903) != 0 or GetCurrency(IANROthInc.SP3903) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SP3903)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPBusInt) != 0 or GetCurrency(IANROthInc.SPBusInt) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPBusInt)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPEntExp) != 0 or GetCurrency(IANROthInc.SPEntExp) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPEntExp)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TP2106) != 0 or GetCurrency(IANROthInc.SP2106) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SP2106)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPOthNC) != 0 or GetCurrency(IANROthInc.SPOthNC) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.SPOthNC)
            count = 99
        else:
            count = count + 1
    ReturnVal = Hold

def SPBabySit_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPBabySit)
    else:
        ReturnVal = 0

def SPBonus_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPBonus)
    else:
        ReturnVal = 0

def SPBusInt_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPBusInt)
    else:
        ReturnVal = 0

def SPBusPass_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPBusPass)
    else:
        ReturnVal = 0

def SPCanceled_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPCanceled)
    else:
        ReturnVal = 0

def SPCoverdell_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPCoverdell)
    else:
        ReturnVal = 0

def SPCredAdj_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPCredAdj)
    else:
        ReturnVal = 0

def SPDefDist_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPDefDist)
    else:
        ReturnVal = 0

def SPDepl_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPDepl)
    else:
        ReturnVal = 0

def SPDirector_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPDirector)
    else:
        ReturnVal = 0

def SPDisaster_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPDisaster)
    else:
        ReturnVal = 0

def SPEntExp_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPEntExp)
    else:
        ReturnVal = 0

def SPExecutor_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPExecutor)
    else:
        ReturnVal = 0

def SPFarmLoss_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPFarmLoss)
    else:
        ReturnVal = 0

def SPFirstHmBuy_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPFirstHmBuy)
    else:
        ReturnVal = 0

def SPFoster_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPFoster)
    else:
        ReturnVal = 0

def SPHobby_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPHobby)
    else:
        ReturnVal = 0

def SPHSA_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPHSA)
    else:
        ReturnVal = 0

def SPIAABLE_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPIAABLE)
    else:
        ReturnVal = 0

def SPIAEd_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPIAEd)
    else:
        ReturnVal = 0

def SPIntangDrill_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPIntangDrill)
    else:
        ReturnVal = 0

def SPJury_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPJury)
    else:
        ReturnVal = 0

def SPK1_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPK1)
    else:
        ReturnVal = 0

def SPLTC_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPLTC)
    else:
        ReturnVal = 0

def SPMedMSA_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPMedMSA)
    else:
        ReturnVal = 0

def SPMisc_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPMisc)
    else:
        ReturnVal = 0

def SPMSA_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPMSA)
    else:
        ReturnVal = 0

def SPName_Calculation():
    ReturnVal = GetString(USWBasicInfo.SPCommon)

def SPOth1_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPOth1)
    else:
        ReturnVal = 0

def SPOth2_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPOth2)
    else:
        ReturnVal = 0

def SPOthNC_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPOthNC)
    else:
        ReturnVal = 0

def SPPerRent_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPPerRent)
    else:
        ReturnVal = 0

def SPPshipCan_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPPshipCan)
    else:
        ReturnVal = 0

def SPPYNPTC_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPPYNPTC)
    else:
        ReturnVal = 0

def SPRecapChar_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPRecapChar)
    else:
        ReturnVal = 0

def SPRecapTuit_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPRecapTuit)
    else:
        ReturnVal = 0

def SPRefundCr_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPRefundCr)
    else:
        ReturnVal = 0

def SPStRefund_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPStRefund)
    else:
        ReturnVal = 0

def SPStudLoanDis_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPStudLoanDis)
    else:
        ReturnVal = 0

def SPTot_Calculation():
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = GetCurrency(IANROthInc.SPOth1) + GetCurrency(IANROthInc.SPOth2) + GetCurrency(IANROthInc.SPBabySit) + GetCurrency(IANROthInc.SPBonus) + GetCurrency(IANROthInc.SPIAEd) + GetCurrency(IANROthInc.SPDirector) + GetCurrency(IANROthInc.SPIntangDrill) + GetCurrency(IANROthInc.SPExecutor) + GetCurrency(IANROthInc.SPFirstHmBuy) + GetCurrency(IANROthInc.SPK1) + GetCurrency(IANROthInc.SPRefundCr) + GetCurrency(IANROthInc.SPStRefund) + GetCurrency(IANROthInc.SPDepl) + GetCurrency(IANROthInc.SPJury) + GetCurrency(IANROthInc.SPPerRent) + GetCurrency(IANROthInc.SP8814) + GetCurrency(IANROthInc.SPMSA) + GetCurrency(IANROthInc.SPMedMSA) + GetCurrency(IANROthInc.SPLTC) + GetCurrency(IANROthInc.SPMisc) + GetCurrency(IANROthInc.SPAlaska) + GetCurrency(IANROthInc.SPCoverdell) + GetCurrency(IANROthInc.SPCanceled) + GetCurrency(IANROthInc.SPPshipCan) + GetCurrency(IANROthInc.SPHSA) + GetCurrency(IANROthInc.SPAltTrade) + GetCurrency(IANROthInc.SPRecapTuit) + GetCurrency(IANROthInc.SPRecapChar) + GetCurrency(IANROthInc.SP5471) + GetCurrency(IANROthInc.SPHobby) + GetCurrency(IANROthInc.SP8621) + GetCurrency(IANROthInc.SPDefDist) + GetCurrency(IANROthInc.SPDisaster) + GetCurrency(IANROthInc.SPFoster) + GetCurrency(IANROthInc.SPCredAdj) + GetCurrency(IANROthInc.SPPYNPTC) + GetCurrency(IANROthInc.SP1099QA) + GetCurrency(IANROthInc.SPIAABLE) + GetCurrency(IANROthInc.SPBusPass) + GetCurrency(IANROthInc.SPAirline) + GetCurrency(IANROthInc.SP1099B) + GetCurrency(IANROthInc.SPFarmLoss) + GetCurrency(IANROthInc.SP8824) + GetCurrency(IANROthInc.SPStudLoanDis) + GetCurrency(IANROthInc.SP4684) + GetCurrency(IANROthInc.SP3903) + GetCurrency(IANROthInc.SPBusInt) + GetCurrency(IANROthInc.SPEntExp) + GetCurrency(IANROthInc.SP2106) + GetCurrency(IANROthInc.SPOthNC)
    else:
        ReturnVal = 0

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

def TP1099B_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TP1099B)
    else:
        ReturnVal = 0

def TP1099QA_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TP1099QA)
    else:
        ReturnVal = 0

def TP2106_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TP2106)
    else:
        ReturnVal = 0

def TP3903_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TP3903)
    else:
        ReturnVal = 0

def TP4684_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TP4684)
    else:
        ReturnVal = 0

def TP5471_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TP5471)
    else:
        ReturnVal = 0

def TP8621_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TP8621)
    else:
        ReturnVal = 0

def TP8814_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TP8814)
    else:
        ReturnVal = 0

def TP8824_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TP8824)
    else:
        ReturnVal = 0

def TPAirline_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPAirline)
    else:
        ReturnVal = 0

def TPAlaska_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPAlaska)
    else:
        ReturnVal = 0

def TPAltTrade_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPAltTrade)
    else:
        ReturnVal = 0

def TPAmount_Calculation(Index):
    count = Integer()

    Hold = Currency()
    count = 0
    Hold = 0
    if GetCurrency(IANROthInc.TPOth1) != 0 or GetCurrency(IANROthInc.SPOth1) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPOth1)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPOth2) != 0 or GetCurrency(IANROthInc.SPOth2) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPOth2)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPBabySit) != 0 or GetCurrency(IANROthInc.SPBabySit) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPBabySit)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPBonus) != 0 or GetCurrency(IANROthInc.SPBonus) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPBonus)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPIAEd) != 0 or GetCurrency(IANROthInc.SPIAEd) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPIAEd)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPDirector) != 0 or GetCurrency(IANROthInc.SPDirector) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPDirector)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPIntangDrill) != 0 or GetCurrency(IANROthInc.SPIntangDrill) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPIntangDrill)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPExecutor) != 0 or GetCurrency(IANROthInc.SPExecutor) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPExecutor)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPFirstHmBuy) != 0 or GetCurrency(IANROthInc.SPFirstHmBuy) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPFirstHmBuy)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPK1) != 0 or GetCurrency(IANROthInc.SPK1) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPK1)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPRefundCr) != 0 or GetCurrency(IANROthInc.SPRefundCr) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPRefundCr)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPStRefund) != 0 or GetCurrency(IANROthInc.SPStRefund) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPStRefund)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPDepl) != 0 or GetCurrency(IANROthInc.SPDepl) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPDepl)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPJury) != 0 or GetCurrency(IANROthInc.SPJury) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPJury)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPPerRent) != 0 or GetCurrency(IANROthInc.SPPerRent) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPPerRent)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TP8814) != 0 or GetCurrency(IANROthInc.SP8814) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TP8814)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPMSA) != 0 or GetCurrency(IANROthInc.SPMSA) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPMSA)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPMedMSA) != 0 or GetCurrency(IANROthInc.SPMedMSA) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPMedMSA)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPLTC) != 0 or GetCurrency(IANROthInc.SPLTC) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPLTC)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPMisc) != 0 or GetCurrency(IANROthInc.SPMisc) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPMisc)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPAlaska) != 0 or GetCurrency(IANROthInc.SPAlaska) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPAlaska)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPCoverdell) != 0 or GetCurrency(IANROthInc.SPCoverdell) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPCoverdell)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPCanceled) != 0 or GetCurrency(IANROthInc.SPCanceled) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPCanceled)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPPshipCan) != 0 or GetCurrency(IANROthInc.SPPshipCan) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPPshipCan)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPHSA) != 0 or GetCurrency(IANROthInc.SPHSA) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPHSA)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPAltTrade) != 0 or GetCurrency(IANROthInc.SPAltTrade) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPAltTrade)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPRecapTuit) != 0 or GetCurrency(IANROthInc.SPRecapTuit) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPRecapTuit)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPRecapChar) != 0 or GetCurrency(IANROthInc.SPRecapChar) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPRecapChar)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TP5471) != 0 or GetCurrency(IANROthInc.SP5471) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TP5471)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPHobby) != 0 or GetCurrency(IANROthInc.SPHobby) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPHobby)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TP8621) != 0 or GetCurrency(IANROthInc.SP8621) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TP8621)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPDefDist) != 0 or GetCurrency(IANROthInc.SPDefDist) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPDefDist)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPDisaster) != 0 or GetCurrency(IANROthInc.SPDisaster) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPDisaster)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPFoster) != 0 or GetCurrency(IANROthInc.SPFoster) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPFoster)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPCredAdj) != 0 or GetCurrency(IANROthInc.SPCredAdj) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPCredAdj)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPPYNPTC) != 0 or GetCurrency(IANROthInc.SPPYNPTC) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPPYNPTC)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TP1099QA) != 0 or GetCurrency(IANROthInc.SP1099QA) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TP1099QA)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPAirline) != 0 or GetCurrency(IANROthInc.SPAirline) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPAirline)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TP1099B) != 0 or GetCurrency(IANROthInc.SP1099B) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TP1099B)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPIAABLE) != 0 or GetCurrency(IANROthInc.SPIAABLE) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPIAABLE)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPBusPass) != 0 or GetCurrency(IANROthInc.SPBusPass) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPBusPass)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPFarmLoss) != 0 or GetCurrency(IANROthInc.SPFarmLoss) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPFarmLoss)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TP8824) != 0 or GetCurrency(IANROthInc.SP8824) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TP8824)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPStudLoanDis) != 0 or GetCurrency(IANROthInc.SPStudLoanDis) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPStudLoanDis)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TP4684) != 0 or GetCurrency(IANROthInc.SP4684) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TP4684)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TP3903) != 0 or GetCurrency(IANROthInc.SP3903) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TP3903)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPBusInt) != 0 or GetCurrency(IANROthInc.SPBusInt) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPBusInt)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPEntExp) != 0 or GetCurrency(IANROthInc.SPEntExp) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPEntExp)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TP2106) != 0 or GetCurrency(IANROthInc.SP2106) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TP2106)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthInc.TPOthNC) != 0 or GetCurrency(IANROthInc.SPOthNC) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthInc.TPOthNC)
            count = 99
        else:
            count = count + 1
    ReturnVal = Hold

def TPBabySit_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPBabySit)
    else:
        ReturnVal = 0

def TPBonus_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPBonus)
    else:
        ReturnVal = 0

def TPBusInt_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPBusInt)
    else:
        ReturnVal = 0

def TPBusPass_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPBusPass)
    else:
        ReturnVal = 0

def TPCanceled_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPCanceled)
    else:
        ReturnVal = 0

def TPCoverdell_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPCoverdell)
    else:
        ReturnVal = 0

def TPCredAdj_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPCredAdj)
    else:
        ReturnVal = 0

def TPDefDist_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPDefDist)
    else:
        ReturnVal = 0

def TPDepl_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPDepl)
    else:
        ReturnVal = 0

def TPDirector_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPDirector)
    else:
        ReturnVal = 0

def TPDisaster_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPDisaster)
    else:
        ReturnVal = 0

def TPEntExp_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPEntExp)
    else:
        ReturnVal = 0

def TPExecutor_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPExecutor)
    else:
        ReturnVal = 0

def TPFarmLoss_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPFarmLoss)
    else:
        ReturnVal = 0

def TPFirstHmBuy_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPFirstHmBuy)
    else:
        ReturnVal = 0

def TPFoster_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPFoster)
    else:
        ReturnVal = 0

def TPHobby_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPHobby)
    else:
        ReturnVal = 0

def TPHSA_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPHSA)
    else:
        ReturnVal = 0

def TPIAABLE_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPIAABLE)
    else:
        ReturnVal = 0

def TPIAEd_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPIAEd)
    else:
        ReturnVal = 0

def TPIntangDrill_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPIntangDrill)
    else:
        ReturnVal = 0

def TPJointAmount_Calculation(Index):
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetCurrency(IANROthInc.TPAmount(Index))
    else:
        ReturnVal = GetCurrency(IANROthInc.TPAmount(Index)) + GetCurrency(IANROthInc.SPAmount(Index))

def TPJury_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPJury)
    else:
        ReturnVal = 0

def TPK1_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPK1)
    else:
        ReturnVal = 0

def TPLTC_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPLTC)
    else:
        ReturnVal = 0

def TPMedMSA_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPMedMSA)
    else:
        ReturnVal = 0

def TPMisc_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPMisc)
    else:
        ReturnVal = 0

def TPMSA_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPMSA)
    else:
        ReturnVal = 0

def TPName_Calculation():
    ReturnVal = GetString(USWBasicInfo.TPCommon)

def TPOth1_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPOth1)
    else:
        ReturnVal = 0

def TPOth2_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPOth2)
    else:
        ReturnVal = 0

def TPOthNC_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPOthNC)
    else:
        ReturnVal = 0

def TPPerRent_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPPerRent)
    else:
        ReturnVal = 0

def TPPshipCan_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPPshipCan)
    else:
        ReturnVal = 0

def TPPYNPTC_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPPYNPTC)
    else:
        ReturnVal = 0

def TPRecapChar_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPRecapChar)
    else:
        ReturnVal = 0

def TPRecapTuit_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPRecapTuit)
    else:
        ReturnVal = 0

def TPRefundCr_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPRefundCr)
    else:
        ReturnVal = 0

def TPStRefund_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPStRefund)
    else:
        ReturnVal = 0

def TPStudLoanDis_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IAWOthInc.TPStudLoanDis)
    else:
        ReturnVal = 0

def TPTot_Calculation():
    if ( IAFS() == 2 and GetBool(IAF126.SpRes) == False )  or GetBool(IAF126.TpRes) == False:
        ReturnVal = GetCurrency(IANROthInc.TPOth1) + GetCurrency(IANROthInc.TPOth2) + GetCurrency(IANROthInc.TPBabySit) + GetCurrency(IANROthInc.TPBonus) + GetCurrency(IANROthInc.TPIAEd) + GetCurrency(IANROthInc.TPDirector) + GetCurrency(IANROthInc.TPIntangDrill) + GetCurrency(IANROthInc.TPExecutor) + GetCurrency(IANROthInc.TPFirstHmBuy) + GetCurrency(IANROthInc.TPK1) + GetCurrency(IANROthInc.TPRefundCr) + GetCurrency(IANROthInc.TPStRefund) + GetCurrency(IANROthInc.TPDepl) + GetCurrency(IANROthInc.TPJury) + GetCurrency(IANROthInc.TPPerRent) + GetCurrency(IANROthInc.TP8814) + GetCurrency(IANROthInc.TPMSA) + GetCurrency(IANROthInc.TPMedMSA) + GetCurrency(IANROthInc.TPLTC) + GetCurrency(IANROthInc.TPMisc) + GetCurrency(IANROthInc.TPAlaska) + GetCurrency(IANROthInc.TPCoverdell) + GetCurrency(IANROthInc.TPCanceled) + GetCurrency(IANROthInc.TPPshipCan) + GetCurrency(IANROthInc.TPHSA) + GetCurrency(IANROthInc.TPAltTrade) + GetCurrency(IANROthInc.TPRecapTuit) + GetCurrency(IANROthInc.TPRecapChar) + GetCurrency(IANROthInc.TP5471) + GetCurrency(IANROthInc.TPHobby) + GetCurrency(IANROthInc.TP8621) + GetCurrency(IANROthInc.TPDefDist) + GetCurrency(IANROthInc.TPDisaster) + GetCurrency(IANROthInc.TPFoster) + GetCurrency(IANROthInc.TPCredAdj) + GetCurrency(IANROthInc.TPPYNPTC) + GetCurrency(IANROthInc.TP1099QA) + GetCurrency(IANROthInc.TPIAABLE) + GetCurrency(IANROthInc.TPBusPass) + GetCurrency(IANROthInc.TPAirline) + GetCurrency(IANROthInc.TP1099B) + GetCurrency(IANROthInc.TPFarmLoss) + GetCurrency(IANROthInc.TP8824) + GetCurrency(IANROthInc.TPStudLoanDis) + GetCurrency(IANROthInc.TP4684) + GetCurrency(IANROthInc.TP3903) + GetCurrency(IANROthInc.TPBusInt) + GetCurrency(IANROthInc.TPEntExp) + GetCurrency(IANROthInc.TP2106) + GetCurrency(IANROthInc.TPOthNC)
    else:
        ReturnVal = 0

def Txt1_Calculation():
    ReturnVal = GetString(IAWOthInc.Txt1)

def Txt2_Calculation():
    ReturnVal = GetString(IAWOthInc.Txt2)

