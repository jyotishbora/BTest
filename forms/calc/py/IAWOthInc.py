from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Code_Calculation(Index):
    count = Integer()

    Hold = String()
    count = 0
    Hold = ''
    if GetCurrency(IAWOthInc.TPOth1) != 0 or GetCurrency(IAWOthInc.SPOth1) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPOth2) != 0 or GetCurrency(IAWOthInc.SPOth2) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPBabySit) != 0 or GetCurrency(IAWOthInc.SPBabySit) != 0:
        if Index == count:
            Hold = 'a'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPBonus) != 0 or GetCurrency(IAWOthInc.SPBonus) != 0:
        if Index == count:
            Hold = 'b'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPIAEd) != 0 or GetCurrency(IAWOthInc.SPIAEd) != 0:
        if Index == count:
            Hold = 'd'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPDirector) != 0 or GetCurrency(IAWOthInc.SPDirector) != 0:
        if Index == count:
            Hold = 'e'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPIntangDrill) != 0 or GetCurrency(IAWOthInc.SPIntangDrill) != 0:
        if Index == count:
            Hold = 'f'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPExecutor) != 0 or GetCurrency(IAWOthInc.SPExecutor) != 0:
        if Index == count:
            Hold = 'g'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPFirstHmBuy) != 0 or GetCurrency(IAWOthInc.SPFirstHmBuy) != 0:
        if Index == count:
            Hold = 'h'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPK1) != 0 or GetCurrency(IAWOthInc.SPK1) != 0:
        if Index == count:
            Hold = 'i'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPRefundCr) != 0 or GetCurrency(IAWOthInc.SPRefundCr) != 0:
        if Index == count:
            Hold = 'j'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPStRefund) != 0 or GetCurrency(IAWOthInc.SPStRefund) != 0:
        if Index == count:
            Hold = 'k'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPDepl) != 0 or GetCurrency(IAWOthInc.SPDepl) != 0:
        if Index == count:
            Hold = 'l'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPJury) != 0 or GetCurrency(IAWOthInc.SPJury) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPPerRent) != 0 or GetCurrency(IAWOthInc.SPPerRent) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TP8814) != 0 or GetCurrency(IAWOthInc.SP8814) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPMSA) != 0 or GetCurrency(IAWOthInc.SPMSA) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPMedMSA) != 0 or GetCurrency(IAWOthInc.SPMedMSA) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPLTC) != 0 or GetCurrency(IAWOthInc.SPLTC) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPMisc) != 0 or GetCurrency(IAWOthInc.SPMisc) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPAlaska) != 0 or GetCurrency(IAWOthInc.SPAlaska) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPCoverdell) != 0 or GetCurrency(IAWOthInc.SPCoverdell) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPCanceled) != 0 or GetCurrency(IAWOthInc.SPCanceled) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPPshipCan) != 0 or GetCurrency(IAWOthInc.SPPshipCan) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPHSA) != 0 or GetCurrency(IAWOthInc.SPHSA) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPAltTrade) != 0 or GetCurrency(IAWOthInc.SPAltTrade) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPRecapTuit) != 0 or GetCurrency(IAWOthInc.SPRecapTuit) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPRecapChar) != 0 or GetCurrency(IAWOthInc.SPRecapChar) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TP5471) != 0 or GetCurrency(IAWOthInc.SP5471) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPHobby) != 0 or GetCurrency(IAWOthInc.SPHobby) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TP8621) != 0 or GetCurrency(IAWOthInc.SP8621) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPDefDist) != 0 or GetCurrency(IAWOthInc.SPDefDist) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPDisaster) != 0 or GetCurrency(IAWOthInc.SPDisaster) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPFoster) != 0 or GetCurrency(IAWOthInc.SPFoster) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPCredAdj) != 0 or GetCurrency(IAWOthInc.SPCredAdj) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPPYNPTC) != 0 or GetCurrency(IAWOthInc.SPPYNPTC) != 0:
        if Index == count:
            Hold = 'n'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TP1099QA) != 0 or GetCurrency(IAWOthInc.SP1099QA) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPAirline) != 0 or GetCurrency(IAWOthInc.SPAirline) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TP1099B) != 0 or GetCurrency(IAWOthInc.SP1099B) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPIAABLE) != 0 or GetCurrency(IAWOthInc.SPIAABLE) != 0:
        if Index == count:
            Hold = 'o'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPBusPass) != 0 or GetCurrency(IAWOthInc.SPBusPass) != 0:
        if Index == count:
            Hold = 'p'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPFarmLoss) != 0 or GetCurrency(IAWOthInc.SPFarmLoss) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TP8824) != 0 or GetCurrency(IAWOthInc.SP8824) != 0:
        if Index == count:
            Hold = 'q'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPStudLoanDis) != 0 or GetCurrency(IAWOthInc.SPStudLoanDis) != 0:
        if Index == count:
            Hold = 'r'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TP4684) != 0 or GetCurrency(IAWOthInc.SP4684) != 0:
        if Index == count:
            Hold = 's'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TP3903) != 0 or GetCurrency(IAWOthInc.SP3903) != 0:
        if Index == count:
            Hold = 't'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPBusInt) != 0 or GetCurrency(IAWOthInc.SPBusInt) != 0:
        if Index == count:
            Hold = 'u'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPEntExp) != 0 or GetCurrency(IAWOthInc.SPEntExp) != 0:
        if Index == count:
            Hold = 'v'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TP2106) != 0 or GetCurrency(IAWOthInc.SP2106) != 0:
        if Index == count:
            Hold = 'w'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPOthNC) != 0 or GetCurrency(IAWOthInc.SPOthNC) != 0:
        if Index == count:
            Hold = 'x'
            count = 99
        else:
            count = count + 1
    ReturnVal = Hold

def Desc_Calculation():
    Total = Currency()
    Total = GetCurrency(IAWOthInc.TPTot) + GetCurrency(IAWOthInc.SPTot)
    ReturnVal = CStr(Total)

def Description_Calculation(Index):
    count = Integer()

    Hold = String()
    count = 0
    Hold = ''
    if GetCurrency(IAWOthInc.TPOth1) != 0 or GetCurrency(IAWOthInc.SPOth1) != 0:
        if Index == count:
            Hold = GetString(IAWOthInc.Txt1)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPOth2) != 0 or GetCurrency(IAWOthInc.SPOth2) != 0:
        if Index == count:
            Hold = GetString(IAWOthInc.Txt2)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPBabySit) != 0 or GetCurrency(IAWOthInc.SPBabySit) != 0:
        if Index == count:
            Hold = 'Baby-sitting income not reported on federal Schedule C'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPBonus) != 0 or GetCurrency(IAWOthInc.SPBonus) != 0:
        if Index == count:
            Hold = 'Bonus depreciation/section 179 adjustment'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPIAEd) != 0 or GetCurrency(IAWOthInc.SPIAEd) != 0:
        if Index == count:
            Hold = 'College Savings Iowa or Iowa Advisor 529 Plan'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPDirector) != 0 or GetCurrency(IAWOthInc.SPDirector) != 0:
        if Index == count:
            Hold = 'Director\'s fees'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPIntangDrill) != 0 or GetCurrency(IAWOthInc.SPIntangDrill) != 0:
        if Index == count:
            Hold = 'Drilling'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPExecutor) != 0 or GetCurrency(IAWOthInc.SPExecutor) != 0:
        if Index == count:
            Hold = 'Executor\'s fees'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPFirstHmBuy) != 0 or GetCurrency(IAWOthInc.SPFirstHmBuy) != 0:
        if Index == count:
            Hold = 'First-time homebuyers account non-qualifying withdrawals'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPK1) != 0 or GetCurrency(IAWOthInc.SPK1) != 0:
        if Index == count:
            Hold = 'Partnership income and/or S Corporation income'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPRefundCr) != 0 or GetCurrency(IAWOthInc.SPRefundCr) != 0:
        if Index == count:
            Hold = 'Refundable Iowa credits'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPStRefund) != 0 or GetCurrency(IAWOthInc.SPStRefund) != 0:
        if Index == count:
            Hold = 'State income tax refunds'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPDepl) != 0 or GetCurrency(IAWOthInc.SPDepl) != 0:
        if Index == count:
            Hold = 'Wells'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPJury) != 0 or GetCurrency(IAWOthInc.SPJury) != 0:
        if Index == count:
            Hold = 'Jury pay'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPPerRent) != 0 or GetCurrency(IAWOthInc.SPPerRent) != 0:
        if Index == count:
            Hold = 'Income from personal property'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TP8814) != 0 or GetCurrency(IAWOthInc.SP8814) != 0:
        if Index == count:
            Hold = 'Child\'s income amount, federal Form 8814'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPMSA) != 0 or GetCurrency(IAWOthInc.SPMSA) != 0:
        if Index == count:
            Hold = 'MSA distributions, federal Form 8853'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPMedMSA) != 0 or GetCurrency(IAWOthInc.SPMedMSA) != 0:
        if Index == count:
            Hold = 'Medicare Advantage distributions, federal Form 8853'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPLTC) != 0 or GetCurrency(IAWOthInc.SPLTC) != 0:
        if Index == count:
            Hold = 'Long-term care distribution, federal Form 8853'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPMisc) != 0 or GetCurrency(IAWOthInc.SPMisc) != 0:
        if Index == count:
            Hold = 'Form 1099-MISC, boxes 3 or 8'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPAlaska) != 0 or GetCurrency(IAWOthInc.SPAlaska) != 0:
        if Index == count:
            Hold = 'Alaska Permanent Fund dividends'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPCoverdell) != 0 or GetCurrency(IAWOthInc.SPCoverdell) != 0:
        if Index == count:
            Hold = 'Coverdell ESA Or Qualified Tuition Program'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPCanceled) != 0 or GetCurrency(IAWOthInc.SPCanceled) != 0:
        if Index == count:
            Hold = 'Cancellation of nonbusiness debt, federal Form 1099-C'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPPshipCan) != 0 or GetCurrency(IAWOthInc.SPPshipCan) != 0:
        if Index == count:
            Hold = 'Cancellation of business debt, Partnership Schedule K-1'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPHSA) != 0 or GetCurrency(IAWOthInc.SPHSA) != 0:
        if Index == count:
            Hold = 'HSA distributions, federal Form 8889'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPAltTrade) != 0 or GetCurrency(IAWOthInc.SPAltTrade) != 0:
        if Index == count:
            Hold = 'Alternative trade adjustment assistance payments'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPRecapTuit) != 0 or GetCurrency(IAWOthInc.SPRecapTuit) != 0:
        if Index == count:
            Hold = 'Recapture of prior year tuition and fees deduction'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPRecapChar) != 0 or GetCurrency(IAWOthInc.SPRecapChar) != 0:
        if Index == count:
            Hold = 'Recapture of charitable contribution deduction'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TP5471) != 0 or GetCurrency(IAWOthInc.SP5471) != 0:
        if Index == count:
            Hold = 'Income from a foreign corporation, federal Form 5471'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPHobby) != 0 or GetCurrency(IAWOthInc.SPHobby) != 0:
        if Index == count:
            Hold = 'Hobby income'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TP8621) != 0 or GetCurrency(IAWOthInc.SP8621) != 0:
        if Index == count:
            Hold = 'Income or loss from Section 1291, federal Form 8621'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPDefDist) != 0 or GetCurrency(IAWOthInc.SPDefDist) != 0:
        if Index == count:
            Hold = 'Loss on excess deferral distribution'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPDisaster) != 0 or GetCurrency(IAWOthInc.SPDisaster) != 0:
        if Index == count:
            Hold = 'Disaster relief payments'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPFoster) != 0 or GetCurrency(IAWOthInc.SPFoster) != 0:
        if Index == count:
            Hold = 'Medicaid waiver payments to care provider'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPCredAdj) != 0 or GetCurrency(IAWOthInc.SPCredAdj) != 0:
        if Index == count:
            Hold = 'Credit adjustment income, federal Forms 6478 and 8864'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPPYNPTC) != 0 or GetCurrency(IAWOthInc.SPPYNPTC) != 0:
        if Index == count:
            Hold = 'Net Premium Tax Credit'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TP1099QA) != 0 or GetCurrency(IAWOthInc.SP1099QA) != 0:
        if Index == count:
            Hold = 'Distributions from ABLE account'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPAirline) != 0 or GetCurrency(IAWOthInc.SPAirline) != 0:
        if Index == count:
            Hold = 'Qualified airline payments'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TP1099B) != 0 or GetCurrency(IAWOthInc.SP1099B) != 0:
        if Index == count:
            Hold = 'Foreign currency transaction'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPIAABLE) != 0 or GetCurrency(IAWOthInc.SPIAABLE) != 0:
        if Index == count:
            Hold = 'Distributions from an Iowa ABLE account'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPBusPass) != 0 or GetCurrency(IAWOthInc.SPBusPass) != 0:
        if Index == count:
            Hold = 'Employer provided bus pass or transportation expenses'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPFarmLoss) != 0 or GetCurrency(IAWOthInc.SPFarmLoss) != 0:
        if Index == count:
            Hold = 'Section 461(j) excess farm loss limitation adjustments'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TP8824) != 0 or GetCurrency(IAWOthInc.SP8824) != 0:
        if Index == count:
            Hold = 'IA 8824 worksheet, due to nonconformity'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPStudLoanDis) != 0 or GetCurrency(IAWOthInc.SPStudLoanDis) != 0:
        if Index == count:
            Hold = 'Discharge of student loan debt - death or disability'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TP4684) != 0 or GetCurrency(IAWOthInc.SP4684) != 0:
        if Index == count:
            Hold = 'IA 4684 worksheet, due to nonconformity'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TP3903) != 0 or GetCurrency(IAWOthInc.SP3903) != 0:
        if Index == count:
            Hold = 'IA 3903 worksheet line 8a, due to nonconformity'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPBusInt) != 0 or GetCurrency(IAWOthInc.SPBusInt) != 0:
        if Index == count:
            Hold = 'Business interest expense limitation, due to nonconformity'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPEntExp) != 0 or GetCurrency(IAWOthInc.SPEntExp) != 0:
        if Index == count:
            Hold = 'Entertainment expenses, due to nonconformity'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TP2106) != 0 or GetCurrency(IAWOthInc.SP2106) != 0:
        if Index == count:
            Hold = 'IA 2106 worksheet line 8, due to nonconformity'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPOthNC) != 0 or GetCurrency(IAWOthInc.SPOthNC) != 0:
        if Index == count:
            Hold = 'Other nonconformity adjustments'
            count = 99
        else:
            count = count + 1
    ReturnVal = Hold

def Exist_Calculation():
    ReturnVal = 1

def Names_Calculation():
    ReturnVal = GetString(IARequired.CombNames)

def Print_Calculation():
    if GetCurrency(IAWOthInc.TPTot) != 0 or GetCurrency(IAWOthInc.SPTot) != 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def SP1099B_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.SP1099B)
    else:
        ReturnVal = 0

def SP1099QA_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.SP1099QA)
    else:
        ReturnVal = 0

def SP2106_Calculation():
    ReturnVal = GetCurrency(IA2106.IAWages, FieldCopies(IA2106.Spouse))

def SP3903_Calculation():
    ReturnVal = GetCurrency(IARequired.SIAExReimb)

def SP5471_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.SP5471)
    else:
        ReturnVal = 0

def SP8621_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.SP8621)
    else:
        ReturnVal = 0

def SP8814_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.SP8814)
    else:
        ReturnVal = 0

def SP8824_Calculation():
    ReturnVal = GetCurrency(IARequired.SP8824)

def SPAirline_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.SPAirline)
    else:
        ReturnVal = 0

def SPAlaska_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.SPAlaska)
    else:
        ReturnVal = 0

def SPAltTrade_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.SPAltTrade)
    else:
        ReturnVal = 0

def SPAmount_Calculation(Index):
    count = Integer()

    Hold = Currency()
    count = 0
    Hold = 0
    if GetCurrency(IAWOthInc.TPOth1) != 0 or GetCurrency(IAWOthInc.SPOth1) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPOth1)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPOth2) != 0 or GetCurrency(IAWOthInc.SPOth2) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPOth2)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPBabySit) != 0 or GetCurrency(IAWOthInc.SPBabySit) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPBabySit)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPBonus) != 0 or GetCurrency(IAWOthInc.SPBonus) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPBonus)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPIAEd) != 0 or GetCurrency(IAWOthInc.SPIAEd) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPIAEd)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPDirector) != 0 or GetCurrency(IAWOthInc.SPDirector) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPDirector)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPIntangDrill) != 0 or GetCurrency(IAWOthInc.SPIntangDrill) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPIntangDrill)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPExecutor) != 0 or GetCurrency(IAWOthInc.SPExecutor) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPExecutor)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPFirstHmBuy) != 0 or GetCurrency(IAWOthInc.SPFirstHmBuy) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPFirstHmBuy)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPK1) != 0 or GetCurrency(IAWOthInc.SPK1) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPK1)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPRefundCr) != 0 or GetCurrency(IAWOthInc.SPRefundCr) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPRefundCr)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPStRefund) != 0 or GetCurrency(IAWOthInc.SPStRefund) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPStRefund)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPDepl) != 0 or GetCurrency(IAWOthInc.SPDepl) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPDepl)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPJury) != 0 or GetCurrency(IAWOthInc.SPJury) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPJury)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPPerRent) != 0 or GetCurrency(IAWOthInc.SPPerRent) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPPerRent)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TP8814) != 0 or GetCurrency(IAWOthInc.SP8814) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SP8814)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPMSA) != 0 or GetCurrency(IAWOthInc.SPMSA) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPMSA)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPMedMSA) != 0 or GetCurrency(IAWOthInc.SPMedMSA) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPMedMSA)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPLTC) != 0 or GetCurrency(IAWOthInc.SPLTC) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPLTC)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPMisc) != 0 or GetCurrency(IAWOthInc.SPMisc) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPMisc)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPAlaska) != 0 or GetCurrency(IAWOthInc.SPAlaska) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPAlaska)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPCoverdell) != 0 or GetCurrency(IAWOthInc.SPCoverdell) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPCoverdell)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPCanceled) != 0 or GetCurrency(IAWOthInc.SPCanceled) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPCanceled)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPPshipCan) != 0 or GetCurrency(IAWOthInc.SPPshipCan) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPPshipCan)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPHSA) != 0 or GetCurrency(IAWOthInc.SPHSA) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPHSA)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPAltTrade) != 0 or GetCurrency(IAWOthInc.SPAltTrade) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPAltTrade)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPRecapTuit) != 0 or GetCurrency(IAWOthInc.SPRecapTuit) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPRecapTuit)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPRecapChar) != 0 or GetCurrency(IAWOthInc.SPRecapChar) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPRecapChar)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TP5471) != 0 or GetCurrency(IAWOthInc.SP5471) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SP5471)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPHobby) != 0 or GetCurrency(IAWOthInc.SPHobby) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPHobby)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TP8621) != 0 or GetCurrency(IAWOthInc.SP8621) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SP8621)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPDefDist) != 0 or GetCurrency(IAWOthInc.SPDefDist) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPDefDist)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPDisaster) != 0 or GetCurrency(IAWOthInc.SPDisaster) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPDisaster)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPFoster) != 0 or GetCurrency(IAWOthInc.SPFoster) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPFoster)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPCredAdj) != 0 or GetCurrency(IAWOthInc.SPCredAdj) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPCredAdj)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPPYNPTC) != 0 or GetCurrency(IAWOthInc.SPPYNPTC) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPPYNPTC)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TP1099QA) != 0 or GetCurrency(IAWOthInc.SP1099QA) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SP1099QA)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPAirline) != 0 or GetCurrency(IAWOthInc.SPAirline) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPAirline)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TP1099B) != 0 or GetCurrency(IAWOthInc.SP1099B) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SP1099B)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPIAABLE) != 0 or GetCurrency(IAWOthInc.SPIAABLE) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPIAABLE)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPBusPass) != 0 or GetCurrency(IAWOthInc.SPBusPass) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPBusPass)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPFarmLoss) != 0 or GetCurrency(IAWOthInc.SPFarmLoss) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPFarmLoss)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TP8824) != 0 or GetCurrency(IAWOthInc.SP8824) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SP8824)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPStudLoanDis) != 0 or GetCurrency(IAWOthInc.SPStudLoanDis) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPStudLoanDis)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TP4684) != 0 or GetCurrency(IAWOthInc.SP4684) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SP4684)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TP3903) != 0 or GetCurrency(IAWOthInc.SP3903) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SP3903)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPBusInt) != 0 or GetCurrency(IAWOthInc.SPBusInt) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPBusInt)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPEntExp) != 0 or GetCurrency(IAWOthInc.SPEntExp) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPEntExp)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TP2106) != 0 or GetCurrency(IAWOthInc.SP2106) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SP2106)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPOthNC) != 0 or GetCurrency(IAWOthInc.SPOthNC) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.SPOthNC)
            count = 99
        else:
            count = count + 1
    ReturnVal = Hold

def SPBonus_Calculation():
    ReturnVal = GetCurrency(IAWOthInc.TotBonus) - GetCurrency(IAWOthInc.TPBonus)

def SPCanceled_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.SPCanceled)
    else:
        ReturnVal = 0

def SPCoverdell_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.SPCoverdell)
    else:
        ReturnVal = 0

def SPCredAdj_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.SPCredAdj)
    else:
        ReturnVal = 0

def SPDefDist_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.SPDefDist)
    else:
        ReturnVal = 0

def SPDisaster_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.SPDisaster)
    else:
        ReturnVal = 0

def SPFoster_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.SPFoster)
    else:
        ReturnVal = 0

def SPHobby_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.SPHobby)
    else:
        ReturnVal = 0

def SPHSA_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.SPHSA)
    else:
        ReturnVal = 0

def SPJury_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.SPJury)
    else:
        ReturnVal = 0

def SPK1_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = MaxValue(0, GetCurrency(USWOthInc.SPK1))
    else:
        ReturnVal = 0

def SPLTC_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.SPLTC)
    else:
        ReturnVal = 0

def SPMedMSA_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.SPMedMSA)
    else:
        ReturnVal = 0

def SPMisc_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.SPMisc) + GetCurrency(USWOthInc.SPIndianGaming) + GetCurrency(USWOthInc.SPTribDist) + GetCurrency(USWOthInc.SPNativeDist)
    else:
        ReturnVal = 0

def SPMSA_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.SP8853)
    else:
        ReturnVal = 0

def SPName_Calculation():
    ReturnVal = GetString(USWBasicInfo.SPCommon)

def SPOth1_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.SPOth1)
    else:
        ReturnVal = 0

def SPOth2_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.SPOth2)
    else:
        ReturnVal = 0

def SPOthNC_Calculation():
    ReturnVal = GetCurrency(IAWNonConformAdj.SPTotNonConformAdj)

def SPPerRent_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.SPPerRent)
    else:
        ReturnVal = 0

def SPPshipCan_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.SPPshipCan)
    else:
        ReturnVal = 0

def SPRecapChar_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.SPRecapChContTax) + GetCurrency(USWOthInc.SPRecapChar)
    else:
        ReturnVal = 0

def SPRecapTuit_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.SPRecapTuit)
    else:
        ReturnVal = 0

def SPTot_Calculation():
    ReturnVal = GetCurrency(IAWOthInc.SPOth1) + GetCurrency(IAWOthInc.SPOth2) + GetCurrency(IAWOthInc.SPBabySit) + GetCurrency(IAWOthInc.SPBonus) + GetCurrency(IAWOthInc.SPIAEd) + GetCurrency(IAWOthInc.SPDirector) + GetCurrency(IAWOthInc.SPIntangDrill) + GetCurrency(IAWOthInc.SPExecutor) + GetCurrency(IAWOthInc.SPFirstHmBuy) + GetCurrency(IAWOthInc.SPK1) + GetCurrency(IAWOthInc.SPRefundCr) + GetCurrency(IAWOthInc.SPStRefund) + GetCurrency(IAWOthInc.SPDepl) + GetCurrency(IAWOthInc.SPJury) + GetCurrency(IAWOthInc.SPPerRent) + GetCurrency(IAWOthInc.SP8814) + GetCurrency(IAWOthInc.SPMSA) + GetCurrency(IAWOthInc.SPMedMSA) + GetCurrency(IAWOthInc.SPLTC) + GetCurrency(IAWOthInc.SPMisc) + GetCurrency(IAWOthInc.SPAlaska) + GetCurrency(IAWOthInc.SPCoverdell) + GetCurrency(IAWOthInc.SPCanceled) + GetCurrency(IAWOthInc.SPPshipCan) + GetCurrency(IAWOthInc.SPHSA) + GetCurrency(IAWOthInc.SPAltTrade) + GetCurrency(IAWOthInc.SPRecapTuit) + GetCurrency(IAWOthInc.SPRecapChar) + GetCurrency(IAWOthInc.SP5471) + GetCurrency(IAWOthInc.SPHobby) + GetCurrency(IAWOthInc.SP8621) + GetCurrency(IAWOthInc.SPDefDist) + GetCurrency(IAWOthInc.SPDisaster) + GetCurrency(IAWOthInc.SPFoster) + GetCurrency(IAWOthInc.SPCredAdj) + GetCurrency(IAWOthInc.SPPYNPTC) + GetCurrency(IAWOthInc.SP1099QA) + GetCurrency(IAWOthInc.SPIAABLE) + GetCurrency(IAWOthInc.SPBusPass) + GetCurrency(IAWOthInc.SPAirline) + GetCurrency(IAWOthInc.SP1099B) + GetCurrency(IAWOthInc.SPFarmLoss) + GetCurrency(IAWOthInc.SP8824) + GetCurrency(IAWOthInc.SPStudLoanDis) + GetCurrency(IAWOthInc.SP4684) + GetCurrency(IAWOthInc.SP3903) + GetCurrency(IAWOthInc.SPBusInt) + GetCurrency(IAWOthInc.SPEntExp) + GetCurrency(IAWOthInc.SP2106) + GetCurrency(IAWOthInc.SPOthNC)

def SPTotNonConform_Calculation():
    ReturnVal = GetCurrency(IAWOthInc.SPFarmLoss) + GetCurrency(IAWOthInc.SP8824) + GetCurrency(IAWOthInc.SPStudLoanDis) + GetCurrency(IAWOthInc.SP4684) + GetCurrency(IAWOthInc.SP3903) + GetCurrency(IAWOthInc.SPBusInt) + GetCurrency(IAWOthInc.SPEntExp) + GetCurrency(IAWOthInc.SP2106) + GetCurrency(IAWOthInc.SPOthNC)

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

def TotBonus_Calculation():
    ReturnVal = GetCurrency(IA4562.TotDepAdj) + GetCurrency(IA4562Sp.TotDepAdj) + GetCurrency(IA4562A.TotDepAdj)

def TotNonConform_Calculation():
    ReturnVal = GetCurrency(IAWOthInc.SPTotNonConform) + GetCurrency(IAWOthInc.TPTotNonConform)

def TP1099B_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.TP1099B)
    else:
        ReturnVal = GetCurrency(USWOthIncNR.TP1099B)

def TP1099QA_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.TP1099QA)
    else:
        ReturnVal = GetCurrency(USWOthIncNR.TP1099QA)

def TP2106_Calculation():
    ReturnVal = GetCurrency(IA2106.IAWages, FieldCopies(IA2106.Taxpayer))

def TP3903_Calculation():
    ReturnVal = GetCurrency(IARequired.TIAExReimb)

def TP4684_Calculation():
    ReturnVal = GetCurrency(IA4684.IANonConformAdj) - GetCurrency(IAWOthInc.SP4684)

def TP5471_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.TP5471)
    else:
        ReturnVal = GetCurrency(USWOthIncNR.TP5471)

def TP8621_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.TP8621)
    else:
        ReturnVal = 0

def TP8814_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.TP8814)
    else:
        ReturnVal = GetCurrency(USWOthIncNR.TP8814)

def TP8824_Calculation():
    ReturnVal = GetCurrency(IARequired.TP8824)

def TPAirline_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.TPAirline)
    else:
        ReturnVal = 0

def TPAlaska_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.TPAlaska)
    else:
        ReturnVal = 0

def TPAltTrade_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.TPAltTrade)
    else:
        ReturnVal = GetCurrency(USWOthIncNR.TPAltTrade)

def TPAmount_Calculation(Index):
    count = Integer()

    Hold = Currency()
    count = 0
    Hold = 0
    if GetCurrency(IAWOthInc.TPOth1) != 0 or GetCurrency(IAWOthInc.SPOth1) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPOth1)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPOth2) != 0 or GetCurrency(IAWOthInc.SPOth2) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPOth2)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPBabySit) != 0 or GetCurrency(IAWOthInc.SPBabySit) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPBabySit)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPBonus) != 0 or GetCurrency(IAWOthInc.SPBonus) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPBonus)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPIAEd) != 0 or GetCurrency(IAWOthInc.SPIAEd) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPIAEd)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPDirector) != 0 or GetCurrency(IAWOthInc.SPDirector) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPDirector)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPIntangDrill) != 0 or GetCurrency(IAWOthInc.SPIntangDrill) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPIntangDrill)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPExecutor) != 0 or GetCurrency(IAWOthInc.SPExecutor) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPExecutor)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPFirstHmBuy) != 0 or GetCurrency(IAWOthInc.SPFirstHmBuy) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPFirstHmBuy)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPK1) != 0 or GetCurrency(IAWOthInc.SPK1) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPK1)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPRefundCr) != 0 or GetCurrency(IAWOthInc.SPRefundCr) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPRefundCr)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPStRefund) != 0 or GetCurrency(IAWOthInc.SPStRefund) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPStRefund)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPDepl) != 0 or GetCurrency(IAWOthInc.SPDepl) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPDepl)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPJury) != 0 or GetCurrency(IAWOthInc.SPJury) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPJury)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPPerRent) != 0 or GetCurrency(IAWOthInc.SPPerRent) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPPerRent)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TP8814) != 0 or GetCurrency(IAWOthInc.SP8814) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TP8814)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPMSA) != 0 or GetCurrency(IAWOthInc.SPMSA) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPMSA)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPMedMSA) != 0 or GetCurrency(IAWOthInc.SPMedMSA) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPMedMSA)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPLTC) != 0 or GetCurrency(IAWOthInc.SPLTC) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPLTC)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPMisc) != 0 or GetCurrency(IAWOthInc.SPMisc) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPMisc)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPAlaska) != 0 or GetCurrency(IAWOthInc.SPAlaska) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPAlaska)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPCoverdell) != 0 or GetCurrency(IAWOthInc.SPCoverdell) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPCoverdell)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPCanceled) != 0 or GetCurrency(IAWOthInc.SPCanceled) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPCanceled)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPPshipCan) != 0 or GetCurrency(IAWOthInc.SPPshipCan) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPPshipCan)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPHSA) != 0 or GetCurrency(IAWOthInc.SPHSA) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPHSA)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPAltTrade) != 0 or GetCurrency(IAWOthInc.SPAltTrade) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPAltTrade)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPRecapTuit) != 0 or GetCurrency(IAWOthInc.SPRecapTuit) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPRecapTuit)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPRecapChar) != 0 or GetCurrency(IAWOthInc.SPRecapChar) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPRecapChar)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TP5471) != 0 or GetCurrency(IAWOthInc.SP5471) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TP5471)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPHobby) != 0 or GetCurrency(IAWOthInc.SPHobby) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPHobby)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TP8621) != 0 or GetCurrency(IAWOthInc.SP8621) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TP8621)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPDefDist) != 0 or GetCurrency(IAWOthInc.SPDefDist) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPDefDist)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPDisaster) != 0 or GetCurrency(IAWOthInc.SPDisaster) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPDisaster)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPFoster) != 0 or GetCurrency(IAWOthInc.SPFoster) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPFoster)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPCredAdj) != 0 or GetCurrency(IAWOthInc.SPCredAdj) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPCredAdj)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPPYNPTC) != 0 or GetCurrency(IAWOthInc.SPPYNPTC) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPPYNPTC)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TP1099QA) != 0 or GetCurrency(IAWOthInc.SP1099QA) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TP1099QA)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPAirline) != 0 or GetCurrency(IAWOthInc.SPAirline) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPAirline)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TP1099B) != 0 or GetCurrency(IAWOthInc.SP1099B) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TP1099B)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPIAABLE) != 0 or GetCurrency(IAWOthInc.SPIAABLE) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPIAABLE)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPBusPass) != 0 or GetCurrency(IAWOthInc.SPBusPass) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPBusPass)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPFarmLoss) != 0 or GetCurrency(IAWOthInc.SPFarmLoss) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPFarmLoss)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TP8824) != 0 or GetCurrency(IAWOthInc.SP8824) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TP8824)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPStudLoanDis) != 0 or GetCurrency(IAWOthInc.SPStudLoanDis) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPStudLoanDis)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TP4684) != 0 or GetCurrency(IAWOthInc.SP4684) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TP4684)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TP3903) != 0 or GetCurrency(IAWOthInc.SP3903) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TP3903)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPBusInt) != 0 or GetCurrency(IAWOthInc.SPBusInt) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPBusInt)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPEntExp) != 0 or GetCurrency(IAWOthInc.SPEntExp) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPEntExp)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TP2106) != 0 or GetCurrency(IAWOthInc.SP2106) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TP2106)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAWOthInc.TPOthNC) != 0 or GetCurrency(IAWOthInc.SPOthNC) != 0:
        if Index == count:
            Hold = GetCurrency(IAWOthInc.TPOthNC)
            count = 99
        else:
            count = count + 1
    ReturnVal = Hold

def TPBonus_Calculation():
    JT = Currency()
    JT = CDollar(CDbl(Round(GetCurrency(IAWDepr.TotAdj, FieldCopies(IAWDepr.Joint)))) * 0.5)
    if GetBool(IARequired.AskSpouse) == True:
        ReturnVal = JT + GetCurrency(IAWDepr.TotAdj, FieldCopies(IAWDepr.Taxpayer)) + GetCurrency(IA4562A.TotDepAdj, FieldCopies(IA4562A.Taxpayer)) + GetCurrency(IA4562PIV.TPTotAdj)
    else:
        ReturnVal = GetCurrency(IAWOthInc.TotBonus)

def TPBonusTrigger_Calculation():
    if IAFS() == 3:
        ReturnVal = GetCurrency(IAWOthInc.TPBonus)
    else:
        ReturnVal = GetCurrency(IAWOthInc.TPBonus) + GetCurrency(IAWOthInc.SPBonus)

def TPCanceled_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.TPCanceled)
    else:
        ReturnVal = GetCurrency(USWOthIncNR.TPCanceled)

def TPCoverdell_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.TPCoverdell)
    else:
        ReturnVal = GetCurrency(USWOthIncNR.TPCoverdell)

def TPCredAdj_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.TPCredAdj)
    else:
        ReturnVal = GetCurrency(USWOthIncNR.TPCredAdj)

def TPDefDist_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.TPDefDist)
    else:
        ReturnVal = GetCurrency(USWOthIncNR.TPDefDist)

def TPDepl_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(USF6251.Depl) - GetCurrency(IAWOthInc.SPDepl))

def TPDisaster_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.TPDisaster)
    else:
        ReturnVal = GetCurrency(USWOthIncNR.TPDisaster)

def TPFarmLoss_Calculation():
    ReturnVal = MaxValue(0, Abs(GetCurrency(IAWSchFLoss.ExcessLoss)) - GetCurrency(IAWOthInc.SPFarmLoss))

def TPFoster_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.TPFoster)
    else:
        ReturnVal = GetCurrency(USWOthIncNR.TPFoster)

def TPHobby_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.TPHobby)
    else:
        ReturnVal = 0

def TPHSA_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.TPHSA)
    else:
        ReturnVal = GetCurrency(USWOthIncNR.TPHSA)

def TPIntangDrill_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(USF6251.IntangDrill) - GetCurrency(IAWOthInc.SPIntangDrill))

def TPJointAmount_Calculation(Index):
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetCurrency(IAWOthInc.TPAmount(Index))
    else:
        ReturnVal = GetCurrency(IAWOthInc.TPAmount(Index)) + GetCurrency(IAWOthInc.SPAmount(Index))

def TPJury_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.TPJury)
    else:
        ReturnVal = 0

def TPK1_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = MaxValue(0, GetCurrency(USWOthInc.TPK1))
    else:
        ReturnVal = MaxValue(0, GetCurrency(USWOthIncNR.TPK1))

def TPLTC_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.TPLTC)
    else:
        ReturnVal = GetCurrency(USWOthIncNR.TPLTC)

def TPMedMSA_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.TPMedMSA)
    else:
        ReturnVal = GetCurrency(USWOthIncNR.TPMedMSA)

def TPMisc_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.TPMisc) + GetCurrency(USWOthInc.TPIndianGaming) + GetCurrency(USWOthInc.TPTribDist) + GetCurrency(USWOthInc.TPNativeDist)
    else:
        ReturnVal = GetCurrency(USWOthIncNR.TPMisc)

def TPMSA_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.TP8853)
    else:
        ReturnVal = GetCurrency(USWOthIncNR.TP8853)

def TPName_Calculation():
    ReturnVal = GetString(USWBasicInfo.TPCommon)

def TPOth1_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.TPOth1)
    else:
        ReturnVal = GetCurrency(USWOthIncNR.TPOth1)

def TPOth2_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.TPOth2)
    else:
        ReturnVal = GetCurrency(USWOthIncNR.TPOth2)

def TPOthNC_Calculation():
    ReturnVal = GetCurrency(IAWNonConformAdj.TPTotNonConformAdj)

def TPPerRent_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.TPPerRent)
    else:
        ReturnVal = 0

def TPPshipCan_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.TPPshipCan)
    else:
        ReturnVal = GetCurrency(USWOthIncNR.TPPshipCan)

def TPPYNPTC_Calculation():
    if GetBool(USWSpouse.NonRes) == True:
        ReturnVal = MaxValue(0, GetCurrency(USWRec.PYNPTCNR) - GetCurrency(IAWOthInc.SPPYNPTC))
    else:
        ReturnVal = MaxValue(0, GetCurrency(USWRec.PYNPTC) - GetCurrency(IAWOthInc.SPPYNPTC))

def TPRecapChar_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.TPRecapChContTax) + GetCurrency(USWOthInc.TPRecapChar)
    else:
        ReturnVal = GetCurrency(USWOthIncNR.TPRecapChContTax) + GetCurrency(USWOthIncNR.TPRecapChar)

def TPRecapTuit_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthInc.TPRecapTuit)
    else:
        ReturnVal = 0

def TPTot_Calculation():
    ReturnVal = GetCurrency(IAWOthInc.TPOth1) + GetCurrency(IAWOthInc.TPOth2) + GetCurrency(IAWOthInc.TPBabySit) + GetCurrency(IAWOthInc.TPBonus) + GetCurrency(IAWOthInc.TPIAEd) + GetCurrency(IAWOthInc.TPDirector) + GetCurrency(IAWOthInc.TPIntangDrill) + GetCurrency(IAWOthInc.TPExecutor) + GetCurrency(IAWOthInc.TPFirstHmBuy) + GetCurrency(IAWOthInc.TPK1) + GetCurrency(IAWOthInc.TPRefundCr) + GetCurrency(IAWOthInc.TPStRefund) + GetCurrency(IAWOthInc.TPDepl) + GetCurrency(IAWOthInc.TPJury) + GetCurrency(IAWOthInc.TPPerRent) + GetCurrency(IAWOthInc.TP8814) + GetCurrency(IAWOthInc.TPMSA) + GetCurrency(IAWOthInc.TPMedMSA) + GetCurrency(IAWOthInc.TPLTC) + GetCurrency(IAWOthInc.TPMisc) + GetCurrency(IAWOthInc.TPAlaska) + GetCurrency(IAWOthInc.TPCoverdell) + GetCurrency(IAWOthInc.TPCanceled) + GetCurrency(IAWOthInc.TPPshipCan) + GetCurrency(IAWOthInc.TPHSA) + GetCurrency(IAWOthInc.TPAltTrade) + GetCurrency(IAWOthInc.TPRecapTuit) + GetCurrency(IAWOthInc.TPRecapChar) + GetCurrency(IAWOthInc.TP5471) + GetCurrency(IAWOthInc.TPHobby) + GetCurrency(IAWOthInc.TP8621) + GetCurrency(IAWOthInc.TPDefDist) + GetCurrency(IAWOthInc.TPDisaster) + GetCurrency(IAWOthInc.TPFoster) + GetCurrency(IAWOthInc.TPCredAdj) + GetCurrency(IAWOthInc.TPPYNPTC) + GetCurrency(IAWOthInc.TP1099QA) + GetCurrency(IAWOthInc.TPIAABLE) + GetCurrency(IAWOthInc.TPBusPass) + GetCurrency(IAWOthInc.TPAirline) + GetCurrency(IAWOthInc.TP1099B) + GetCurrency(IAWOthInc.TPFarmLoss) + GetCurrency(IAWOthInc.TP8824) + GetCurrency(IAWOthInc.TPStudLoanDis) + GetCurrency(IAWOthInc.TP4684) + GetCurrency(IAWOthInc.TP3903) + GetCurrency(IAWOthInc.TPBusInt) + GetCurrency(IAWOthInc.TPEntExp) + GetCurrency(IAWOthInc.TP2106) + GetCurrency(IAWOthInc.TPOthNC)

def TPTotNonConform_Calculation():
    ReturnVal = GetCurrency(IAWOthInc.TPFarmLoss) + GetCurrency(IAWOthInc.TP8824) + GetCurrency(IAWOthInc.TPStudLoanDis) + GetCurrency(IAWOthInc.TP4684) + GetCurrency(IAWOthInc.TP3903) + GetCurrency(IAWOthInc.TPBusInt) + GetCurrency(IAWOthInc.TPEntExp) + GetCurrency(IAWOthInc.TP2106) + GetCurrency(IAWOthInc.TPOthNC)

def Txt1_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetString(USWOthInc.Txt1)
    else:
        ReturnVal = GetString(USWOthIncNR.Txt1)

def Txt2_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetString(USWOthInc.Txt2)
    else:
        ReturnVal = GetString(USWOthIncNR.Txt2)

