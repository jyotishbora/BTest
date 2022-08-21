from forms.out import IAF1040
from forms.out import IAF126
from forms.out import IAOTHADJ
from forms.out import IAREQUIRED
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def ANet_Calculation():
    ATotAdj = Currency()
    ATotAdj = get_currency(IAF1040.AKeogh) + get_currency(IAF1040.ABusIncL) + get_currency(IAF1040.AHealth) + get_currency(IAF1040.APenalty) + get_currency(IAF1040.AAlimonyP) + get_currency(IAF1040.APenExcl) + get_currency(IAF1040.AMove) + get_currency(IAF1040.AGainDed) + get_currency(IAOTHADJ.ModTPTot)
    return get_currency(IAF1040.AGross) - ATotAdj

def BNet_Calculation():
    BTotAdj = Currency()
    BTotAdj = get_currency(IAF1040.BKeogh) + get_currency(IAF1040.BBusIncL) + get_currency(IAF1040.BHealth) + get_currency(IAF1040.BPenalty) + get_currency(IAF1040.BAlimonyP) + get_currency(IAF1040.BPenExcl) + get_currency(IAF1040.BMove) + get_currency(IAF1040.BGainDed) + get_currency(IAOTHADJ.ModSPTot)
    return get_currency(IAF1040.BGross) - BTotAdj

def BProRate_Calculation():
    if IAFS() == 3:
        if get_currency(IAOTHADJ.BNet) < 0 and get_currency(IAOTHADJ.ANet) < 0:
            if get_currency(IAOTHADJ.BNet) < get_currency(IAOTHADJ.ANet):
                return 0
            else:
                return 1
        elif get_currency(IAOTHADJ.BNet) < 0:
            return 0
        elif get_currency(IAOTHADJ.BNet) > 0 and get_currency(IAOTHADJ.TotNI) <= 0:
            return 1
        elif get_currency(IAOTHADJ.TotNI) == 0:
            return 0
        else:
            return max_value(0, ( min_value(1, get_float(IAOTHADJ.BNet) / get_float(IAOTHADJ.TotNI)) ))
    else:
        return 0

def Code_Calculation(Index):
    count = Integer()

    Hold = String()
    count = 0
    Hold = ''
    if get_currency(IAOTHADJ.TOth1) != 0 or get_currency(IAOTHADJ.SOth1) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPActiveMil) != 0 or get_currency(IAOTHADJ.SPActiveMil) != 0:
        if Index == count:
            Hold = 'b'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPAltMV) != 0 or get_currency(IAOTHADJ.SPAltMV) != 0:
        if Index == count:
            Hold = 'c'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPInvolConv) != 0 or get_currency(IAOTHADJ.SPInvolConv) != 0:
        if Index == count:
            Hold = 'e'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPClaimOfRight) != 0 or get_currency(IAOTHADJ.SPClaimOfRight) != 0:
        if Index == count:
            Hold = 'f'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPIAEd) != 0 or get_currency(IAOTHADJ.SPIAEd) != 0:
        if Index == count:
            Hold = 'g'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPIADis) != 0 or get_currency(IAOTHADJ.SPIADis) != 0:
        if Index == count:
            Hold = 'h'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPDomProd) != 0 or get_currency(IAOTHADJ.SPDomProd) != 0:
        if Index == count:
            Hold = 'i'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPFirstHmBuy) != 0 or get_currency(IAOTHADJ.SPFirstHmBuy) != 0:
        if Index == count:
            Hold = 'j'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPEmployerSS) != 0 or get_currency(IAOTHADJ.SPEmployerSS) != 0:
        if Index == count:
            Hold = 'k'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPFedFuels) != 0 or get_currency(IAOTHADJ.SPFedFuels) != 0:
        if Index == count:
            Hold = 'l'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPForeign) != 0 or get_currency(IAOTHADJ.SPForeign) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TP2555) != 0 or get_currency(IAOTHADJ.SP2555) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPDistressed) != 0 or get_currency(IAOTHADJ.SPDistressed) != 0:
        if Index == count:
            Hold = 'n'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPHealthSav) != 0 or get_currency(IAOTHADJ.SPHealthSav) != 0:
        if Index == count:
            Hold = 'o'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPVet) != 0 or get_currency(IAOTHADJ.SPVet) != 0:
        if Index == count:
            Hold = 'p'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPVetGrant) != 0 or get_currency(IAOTHADJ.SPVetGrant) != 0:
        if Index == count:
            Hold = 'q'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPHomeHealth) != 0 or get_currency(IAOTHADJ.SPHomeHealth) != 0:
        if Index == count:
            Hold = 'r'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPIAVetTrust) != 0 or get_currency(IAOTHADJ.SPIAVetTrust) != 0:
        if Index == count:
            Hold = 's'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPMilitaryExem) != 0 or get_currency(IAOTHADJ.SPMilitaryExem) != 0:
        if Index == count:
            Hold = 't'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TIANOL) != 0 or get_currency(IAOTHADJ.SIANOL) != 0:
        if Index == count:
            Hold = 'u'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPOrgan) != 0 or get_currency(IAOTHADJ.SPOrgan) != 0:
        if Index == count:
            Hold = 'v'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPK1) != 0 or get_currency(IAOTHADJ.SPK1) != 0:
        if Index == count:
            Hold = 'w'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPSegal) != 0 or get_currency(IAOTHADJ.SPSegal) != 0:
        if Index == count:
            Hold = 'x'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPShell) != 0 or get_currency(IAOTHADJ.SPShell) != 0:
        if Index == count:
            Hold = 'y'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TStud) != 0 or get_currency(IAOTHADJ.SStud) != 0:
        if Index == count:
            Hold = 'z'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPVictim) != 0 or get_currency(IAOTHADJ.SPVictim) != 0:
        if Index == count:
            Hold = 'aa'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPWages) != 0 or get_currency(IAOTHADJ.SPWages) != 0:
        if Index == count:
            Hold = 'bb'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPWorkCr) != 0 or get_currency(IAOTHADJ.SPWorkCr) != 0:
        if Index == count:
            Hold = 'cc'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TP2106) != 0 or get_currency(IAOTHADJ.SP2106) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TMSA) != 0 or get_currency(IAOTHADJ.SMSA) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPJury) != 0 or get_currency(IAOTHADJ.SPJury) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPRFST) != 0 or get_currency(IAOTHADJ.SPRFST) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPSub) != 0 or get_currency(IAOTHADJ.SPSub) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TP501c) != 0 or get_currency(IAOTHADJ.SP501c) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPPerRent) != 0 or get_currency(IAOTHADJ.SPPerRent) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TP403b) != 0 or get_currency(IAOTHADJ.SP403b) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPUDC) != 0 or get_currency(IAOTHADJ.SPUDC) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPWBF) != 0 or get_currency(IAOTHADJ.SPWBF) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TP8873) != 0 or get_currency(IAOTHADJ.SP8873) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPOlympic) != 0 or get_currency(IAOTHADJ.SPOlympic) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPEducator) != 0 or get_currency(IAOTHADJ.SPEducator) != 0:
        if Index == count:
            Hold = 'ee'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPTuition) != 0 or get_currency(IAOTHADJ.SPTuition) != 0:
        if Index == count:
            Hold = 'ff'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPElectric) != 0 or get_currency(IAOTHADJ.SPElectric) != 0:
        if Index == count:
            Hold = 'gg'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPRapid) != 0 or get_currency(IAOTHADJ.SPRapid) != 0:
        if Index == count:
            Hold = 'hh'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPIAABLE) != 0 or get_currency(IAOTHADJ.SPIAABLE) != 0:
        if Index == count:
            Hold = 'ii'
            count = 99
        else:
            count = count + 1
    return Hold

def Desc_Calculation():
    Total = Currency()
    Total = get_currency(IAOTHADJ.TPTot) + get_currency(IAOTHADJ.SPTot)
    return CStr(Total)

def Description_Calculation(Index):
    count = Integer()

    Hold = String()
    count = 0
    Hold = ''
    if get_currency(IAOTHADJ.TOth1) != 0 or get_currency(IAOTHADJ.SOth1) != 0:
        if Index == count:
            Hold = get_string(IAOTHADJ.TxtOth1)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPActiveMil) != 0 or get_currency(IAOTHADJ.SPActiveMil) != 0:
        if Index == count:
            Hold = 'Active duty military pay'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPAltMV) != 0 or get_currency(IAOTHADJ.SPAltMV) != 0:
        if Index == count:
            Hold = 'Alternative motor vehicle deduction'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPInvolConv) != 0 or get_currency(IAOTHADJ.SPInvolConv) != 0:
        if Index == count:
            Hold = 'Capital or ordinary gain from involuntary conversion'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPClaimOfRight) != 0 or get_currency(IAOTHADJ.SPClaimOfRight) != 0:
        if Index == count:
            Hold = 'Claim of Right deduction'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPIAEd) != 0 or get_currency(IAOTHADJ.SPIAEd) != 0:
        if Index == count:
            Hold = 'College Savings Iowa or Iowa Advisor 529 Plan'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPIADis) != 0 or get_currency(IAOTHADJ.SPIADis) != 0:
        if Index == count:
            Hold = 'Disability income exclusion'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPDomProd) != 0 or get_currency(IAOTHADJ.SPDomProd) != 0:
        if Index == count:
            Hold = 'Domestic production activities deduction'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPFirstHmBuy) != 0 or get_currency(IAOTHADJ.SPFirstHmBuy) != 0:
        if Index == count:
            Hold = 'First-Time Homebuyer Savings Account qualifying contributions'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPEmployerSS) != 0 or get_currency(IAOTHADJ.SPEmployerSS) != 0:
        if Index == count:
            Hold = 'Employer social security credit, federal Form 8846'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPFedFuels) != 0 or get_currency(IAOTHADJ.SPFedFuels) != 0:
        if Index == count:
            Hold = 'Alcohol and cellulosic biofuel credit, federal Form 6478'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPForeign) != 0 or get_currency(IAOTHADJ.SPForeign) != 0:
        if Index == count:
            Hold = 'Foreign earned income exclusion, federal Form 2555'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TP2555) != 0 or get_currency(IAOTHADJ.SP2555) != 0:
        if Index == count:
            Hold = 'Foreign housing deduction, federal Form 2555'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPDistressed) != 0 or get_currency(IAOTHADJ.SPDistressed) != 0:
        if Index == count:
            Hold = 'Gains or losses from distressed sale transactions'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPHealthSav) != 0 or get_currency(IAOTHADJ.SPHealthSav) != 0:
        if Index == count:
            Hold = 'Health savings account deduction, federal Form 8889'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPVet) != 0 or get_currency(IAOTHADJ.SPVet) != 0:
        if Index == count:
            Hold = 'Injured veterans programs - contributions'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPVetGrant) != 0 or get_currency(IAOTHADJ.SPVetGrant) != 0:
        if Index == count:
            Hold = 'Injured veterans programs - grants'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPHomeHealth) != 0 or get_currency(IAOTHADJ.SPHomeHealth) != 0:
        if Index == count:
            Hold = 'In-home health care'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPIAVetTrust) != 0 or get_currency(IAOTHADJ.SPIAVetTrust) != 0:
        if Index == count:
            Hold = 'Iowa Veterans Trust Fund'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPMilitaryExem) != 0 or get_currency(IAOTHADJ.SPMilitaryExem) != 0:
        if Index == count:
            Hold = 'Military exemptions'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TIANOL) != 0 or get_currency(IAOTHADJ.SIANOL) != 0:
        if Index == count:
            Hold = 'Iowa Net Operating Loss'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPOrgan) != 0 or get_currency(IAOTHADJ.SPOrgan) != 0:
        if Index == count:
            Hold = 'Organ transplant expenses'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPK1) != 0 or get_currency(IAOTHADJ.SPK1) != 0:
        if Index == count:
            Hold = 'Partnership income and/or S Corporation income'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPSegal) != 0 or get_currency(IAOTHADJ.SPSegal) != 0:
        if Index == count:
            Hold = 'Segal Americorps Education Award payments'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPShell) != 0 or get_currency(IAOTHADJ.SPShell) != 0:
        if Index == count:
            Hold = 'Speculative shell buildings'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TStud) != 0 or get_currency(IAOTHADJ.SStud) != 0:
        if Index == count:
            Hold = 'Student loan interest deduction'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPVictim) != 0 or get_currency(IAOTHADJ.SPVictim) != 0:
        if Index == count:
            Hold = 'Victim compensation awards'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPWages) != 0 or get_currency(IAOTHADJ.SPWages) != 0:
        if Index == count:
            Hold = 'Wages paid to certain individuals'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPWorkCr) != 0 or get_currency(IAOTHADJ.SPWorkCr) != 0:
        if Index == count:
            Hold = 'Work opportunity credit, federal Form 5884'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TP2106) != 0 or get_currency(IAOTHADJ.SP2106) != 0:
        if Index == count:
            Hold = 'Business expenses of reservists, QPA, FBO, federal Form 2106'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TMSA) != 0 or get_currency(IAOTHADJ.SMSA) != 0:
        if Index == count:
            Hold = 'Archer MSA deduction, federal Form 8853'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPJury) != 0 or get_currency(IAOTHADJ.SPJury) != 0:
        if Index == count:
            Hold = 'Jury pay repayment to employer'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPRFST) != 0 or get_currency(IAOTHADJ.SPRFST) != 0:
        if Index == count:
            Hold = 'Reforestation amortization and expenses'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPSub) != 0 or get_currency(IAOTHADJ.SPSub) != 0:
        if Index == count:
            Hold = 'Repayment of supplemental unemployment benefits'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TP501c) != 0 or get_currency(IAOTHADJ.SP501c) != 0:
        if Index == count:
            Hold = 'Contributions to a 501(c)(18) pension plan'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPPerRent) != 0 or get_currency(IAOTHADJ.SPPerRent) != 0:
        if Index == count:
            Hold = 'Expenses for personal property rental'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TP403b) != 0 or get_currency(IAOTHADJ.SP403b) != 0:
        if Index == count:
            Hold = 'Contributions by certain chaplains to a 403(b) plan'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPUDC) != 0 or get_currency(IAOTHADJ.SPUDC) != 0:
        if Index == count:
            Hold = 'Qualified attorney/court fees paid after 10/22/2004'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPWBF) != 0 or get_currency(IAOTHADJ.SPWBF) != 0:
        if Index == count:
            Hold = 'Qualified whistleblower fees'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TP8873) != 0 or get_currency(IAOTHADJ.SP8873) != 0:
        if Index == count:
            Hold = 'Extraterritorial Income Exclusion, federal Form 8873'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPOlympic) != 0 or get_currency(IAOTHADJ.SPOlympic) != 0:
        if Index == count:
            Hold = 'Nontaxable amount of Olympic and Paralympic medals and USOC prize money'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPEducator) != 0 or get_currency(IAOTHADJ.SPEducator) != 0:
        if Index == count:
            Hold = 'Educator expenses'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPTuition) != 0 or get_currency(IAOTHADJ.SPTuition) != 0:
        if Index == count:
            Hold = 'Tuition and fees deduction'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPElectric) != 0 or get_currency(IAOTHADJ.SPElectric) != 0:
        if Index == count:
            Hold = 'Nonresident Electric Utility Reciprocity'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPRapid) != 0 or get_currency(IAOTHADJ.SPRapid) != 0:
        if Index == count:
            Hold = 'Rapid Response to State Disasters'
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPIAABLE) != 0 or get_currency(IAOTHADJ.SPIAABLE) != 0:
        if Index == count:
            Hold = 'Iowa ABLE savings plan trust'
            count = 99
        else:
            count = count + 1
    return Hold

def Exist_Calculation():
    return 1

def ModSPTot_Calculation():
    return get_currency(IAOTHADJ.SOth1) + get_currency(IAOTHADJ.SPActiveMil) + get_currency(IAOTHADJ.SPInvolConv) + get_currency(IAOTHADJ.SPClaimOfRight) + get_currency(IAOTHADJ.SPIAEd) + get_currency(IAOTHADJ.SPIADis) + get_currency(IAOTHADJ.SPDomProd) + get_currency(IAOTHADJ.SPFirstHmBuy) + get_currency(IAOTHADJ.SPEmployerSS) + get_currency(IAOTHADJ.SPFedFuels) + get_currency(IAOTHADJ.SPForeign) + get_currency(IAOTHADJ.SP2555) + get_currency(IAOTHADJ.SPDistressed) + get_currency(IAOTHADJ.SPHealthSav) + get_currency(IAOTHADJ.SPVet) + get_currency(IAOTHADJ.SPVetGrant) + get_currency(IAOTHADJ.SPHomeHealth) + get_currency(IAOTHADJ.SPIAVetTrust) + get_currency(IAOTHADJ.SPMilitaryExem) + get_currency(IAOTHADJ.SIANOL) + get_currency(IAOTHADJ.SPOrgan) + get_currency(IAOTHADJ.SPK1) + get_currency(IAOTHADJ.SPSegal) + get_currency(IAOTHADJ.SPShell) + get_currency(IAOTHADJ.SStud) + get_currency(IAOTHADJ.SPVictim) + get_currency(IAOTHADJ.SPWages) + get_currency(IAOTHADJ.SPWorkCr) + get_currency(IAOTHADJ.SP2106) + get_currency(IAOTHADJ.SMSA) + get_currency(IAOTHADJ.SPJury) + get_currency(IAOTHADJ.SPRFST) + get_currency(IAOTHADJ.SPSub) + get_currency(IAOTHADJ.SP501c) + get_currency(IAOTHADJ.SPPerRent) + get_currency(IAOTHADJ.SP403b) + get_currency(IAOTHADJ.SPUDC) + get_currency(IAOTHADJ.SPWBF) + get_currency(IAOTHADJ.SP8873) + get_currency(IAOTHADJ.SPOlympic) + get_currency(IAOTHADJ.SPEducator) + get_currency(IAOTHADJ.SPTuition) + get_currency(IAOTHADJ.SPElectric) + get_currency(IAOTHADJ.SPRapid) + get_currency(IAOTHADJ.SPIAABLE)

def ModTPTot_Calculation():
    return get_currency(IAOTHADJ.TOth1) + get_currency(IAOTHADJ.TPActiveMil) + get_currency(IAOTHADJ.TPInvolConv) + get_currency(IAOTHADJ.TPClaimOfRight) + get_currency(IAOTHADJ.TPIAEd) + get_currency(IAOTHADJ.TPIADis) + get_currency(IAOTHADJ.TPDomProd) + get_currency(IAOTHADJ.TPFirstHmBuy) + get_currency(IAOTHADJ.TPEmployerSS) + get_currency(IAOTHADJ.TPFedFuels) + get_currency(IAOTHADJ.TPForeign) + get_currency(IAOTHADJ.TP2555) + get_currency(IAOTHADJ.TPDistressed) + get_currency(IAOTHADJ.TPHealthSav) + get_currency(IAOTHADJ.TPVet) + get_currency(IAOTHADJ.TPVetGrant) + get_currency(IAOTHADJ.TPHomeHealth) + get_currency(IAOTHADJ.TPIAVetTrust) + get_currency(IAOTHADJ.TPMilitaryExem) + get_currency(IAOTHADJ.TIANOL) + get_currency(IAOTHADJ.TPOrgan) + get_currency(IAOTHADJ.TPK1) + get_currency(IAOTHADJ.TPSegal) + get_currency(IAOTHADJ.TPShell) + get_currency(IAOTHADJ.TStud) + get_currency(IAOTHADJ.TPVictim) + get_currency(IAOTHADJ.TPWages) + get_currency(IAOTHADJ.TPWorkCr) + get_currency(IAOTHADJ.TP2106) + get_currency(IAOTHADJ.TMSA) + get_currency(IAOTHADJ.TPJury) + get_currency(IAOTHADJ.TPRFST) + get_currency(IAOTHADJ.TPSub) + get_currency(IAOTHADJ.TP501c) + get_currency(IAOTHADJ.TPPerRent) + get_currency(IAOTHADJ.TP403b) + get_currency(IAOTHADJ.TPUDC) + get_currency(IAOTHADJ.TPWBF) + get_currency(IAOTHADJ.TP8873) + get_currency(IAOTHADJ.TPOlympic) + get_currency(IAOTHADJ.TPEducator) + get_currency(IAOTHADJ.TPTuition) + get_currency(IAOTHADJ.TPElectric) + get_currency(IAOTHADJ.TPRapid) + get_currency(IAOTHADJ.TPIAABLE)

def Names_Calculation():
    return get_string(IAREQUIRED.CombNames)

def PrintMe_Calculation():
    if get_currency(IAOTHADJ.TPTot) != 0 or get_currency(IAOTHADJ.SPTot) != 0:
        return 1
    else:
        return 0

def SIANOL_Calculation():
    if get_bool(IAF126.SpNonRes) == True:
        return 0
    elif get_bool(USWResidency.F1040NR) == False:
        return Abs(get_currency(USWOthInc.SPNOL))
    else:
        return 0

def SMSA_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthAdj.SP8853)
    else:
        return 0

def SP2106_Calculation():
    return get_currency(USWRec.SBusExp2106)

def SP2555_Calculation():
    return get_currency(USWOthAdj.SP2555)

def SP403b_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthAdj.SP403b)
    else:
        return 0

def SP501c_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthAdj.SPTotal501)
    else:
        return 0

def SP8873_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthAdj.SP8873)
    else:
        return 0

def SPAltMV_Calculation():
    #2018 expanded instructions - deduction does not apply to purchases on or after 1/1/2015 due to nonconformity, federal does not ask for a purchase date, believe will be very uncommon for ability to take this credit on Iowa, remove calc and make user entered
    #If IAFS() = 3 And get_bool(USF8910.Print) = True Then
    #    return c_dollar(get_float(IAOTHADJ.BProRate) * 2000@)
    #Else
    return 0
    #End If

def SPAmount_Calculation(Index):
    count = Integer()

    Hold = Currency()
    count = 0
    Hold = 0
    if get_currency(IAOTHADJ.TOth1) != 0 or get_currency(IAOTHADJ.SOth1) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SOth1)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPActiveMil) != 0 or get_currency(IAOTHADJ.SPActiveMil) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPActiveMil)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPAltMV) != 0 or get_currency(IAOTHADJ.SPAltMV) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPAltMV)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPInvolConv) != 0 or get_currency(IAOTHADJ.SPInvolConv) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPInvolConv)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPClaimOfRight) != 0 or get_currency(IAOTHADJ.SPClaimOfRight) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPClaimOfRight)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPIAEd) != 0 or get_currency(IAOTHADJ.SPIAEd) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPIAEd)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPIADis) != 0 or get_currency(IAOTHADJ.SPIADis) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPIADis)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPDomProd) != 0 or get_currency(IAOTHADJ.SPDomProd) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPDomProd)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPFirstHmBuy) != 0 or get_currency(IAOTHADJ.SPFirstHmBuy) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPFirstHmBuy)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPEmployerSS) != 0 or get_currency(IAOTHADJ.SPEmployerSS) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPEmployerSS)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPFedFuels) != 0 or get_currency(IAOTHADJ.SPFedFuels) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPFedFuels)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPForeign) != 0 or get_currency(IAOTHADJ.SPForeign) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPForeign)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TP2555) != 0 or get_currency(IAOTHADJ.SP2555) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SP2555)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPDistressed) != 0 or get_currency(IAOTHADJ.SPDistressed) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPDistressed)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPHealthSav) != 0 or get_currency(IAOTHADJ.SPHealthSav) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPHealthSav)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPVet) != 0 or get_currency(IAOTHADJ.SPVet) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPVet)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPVetGrant) != 0 or get_currency(IAOTHADJ.SPVetGrant) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPVetGrant)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPHomeHealth) != 0 or get_currency(IAOTHADJ.SPHomeHealth) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPHomeHealth)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPIAVetTrust) != 0 or get_currency(IAOTHADJ.SPIAVetTrust) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPIAVetTrust)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPMilitaryExem) != 0 or get_currency(IAOTHADJ.SPMilitaryExem) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPMilitaryExem)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TIANOL) != 0 or get_currency(IAOTHADJ.SIANOL) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SIANOL)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPOrgan) != 0 or get_currency(IAOTHADJ.SPOrgan) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPOrgan)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPK1) != 0 or get_currency(IAOTHADJ.SPK1) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPK1)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPSegal) != 0 or get_currency(IAOTHADJ.SPSegal) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPSegal)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPShell) != 0 or get_currency(IAOTHADJ.SPShell) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPShell)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TStud) != 0 or get_currency(IAOTHADJ.SStud) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SStud)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPVictim) != 0 or get_currency(IAOTHADJ.SPVictim) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPVictim)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPWages) != 0 or get_currency(IAOTHADJ.SPWages) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPWages)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPWorkCr) != 0 or get_currency(IAOTHADJ.SPWorkCr) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPWorkCr)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TP2106) != 0 or get_currency(IAOTHADJ.SP2106) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SP2106)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TMSA) != 0 or get_currency(IAOTHADJ.SMSA) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SMSA)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPJury) != 0 or get_currency(IAOTHADJ.SPJury) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPJury)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPRFST) != 0 or get_currency(IAOTHADJ.SPRFST) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPRFST)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPSub) != 0 or get_currency(IAOTHADJ.SPSub) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPSub)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TP501c) != 0 or get_currency(IAOTHADJ.SP501c) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SP501c)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPPerRent) != 0 or get_currency(IAOTHADJ.SPPerRent) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPPerRent)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TP403b) != 0 or get_currency(IAOTHADJ.SP403b) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SP403b)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPUDC) != 0 or get_currency(IAOTHADJ.SPUDC) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPUDC)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPWBF) != 0 or get_currency(IAOTHADJ.SPWBF) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPWBF)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TP8873) != 0 or get_currency(IAOTHADJ.SP8873) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SP8873)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPOlympic) != 0 or get_currency(IAOTHADJ.SPOlympic) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPOlympic)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPEducator) != 0 or get_currency(IAOTHADJ.SPEducator) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPEducator)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPTuition) != 0 or get_currency(IAOTHADJ.SPTuition) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPTuition)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPElectric) != 0 or get_currency(IAOTHADJ.SPElectric) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPElectric)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPRapid) != 0 or get_currency(IAOTHADJ.SPRapid) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPRapid)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPIAABLE) != 0 or get_currency(IAOTHADJ.SPIAABLE) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.SPIAABLE)
            count = 99
        else:
            count = count + 1
    return Hold

def SPDomProd_Calculation():
    #Iowa expanded instructions - Iowa has not conformed to the repeal of the federal domestic production activities deduction. For Iowa will need to complete a federal 8903 and keep with their records and follow IA instructions for adjustments needed when calcing.
    #return get_currency(USWRec.SDomProd)
    return 0

def SPEducator_Calculation():
    return get_currency(USWRec.SEdExp)

def SPForeign_Calculation():
    return Abs(get_currency(USWOthInc.SP2555))

def SPHealthSav_Calculation():
    return get_currency(USWRec.SHealthSav)

def SPJury_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthAdj.SPJury)
    else:
        return 0

def SPK1_Calculation():
    if get_bool(USWResidency.F1040NR) == False and get_currency(USWOthInc.SPK1) < 0:
        return Abs(get_currency(USWOthInc.SPK1))
    else:
        return 0

def SPName_Calculation():
    return get_string(USWBasicInfo.SPCommon)

def SPOlympic_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthAdj.Text2)
    else:
        return 0

def SPPerRent_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthAdj.SPPerRent)
    else:
        return 0

def SPRFST_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthAdj.SPRFST)
    else:
        return 0

def SPSub_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthAdj.SPSub)
    else:
        return 0

def SPTot_Calculation():
    return get_currency(IAOTHADJ.SOth1) + get_currency(IAOTHADJ.SPActiveMil) + get_currency(IAOTHADJ.SPAltMV) + get_currency(IAOTHADJ.SPInvolConv) + get_currency(IAOTHADJ.SPClaimOfRight) + get_currency(IAOTHADJ.SPIAEd) + get_currency(IAOTHADJ.SPIADis) + get_currency(IAOTHADJ.SPDomProd) + get_currency(IAOTHADJ.SPFirstHmBuy) + get_currency(IAOTHADJ.SPEmployerSS) + get_currency(IAOTHADJ.SPFedFuels) + get_currency(IAOTHADJ.SPForeign) + get_currency(IAOTHADJ.SP2555) + get_currency(IAOTHADJ.SPDistressed) + get_currency(IAOTHADJ.SPHealthSav) + get_currency(IAOTHADJ.SPVet) + get_currency(IAOTHADJ.SPVetGrant) + get_currency(IAOTHADJ.SPHomeHealth) + get_currency(IAOTHADJ.SPIAVetTrust) + get_currency(IAOTHADJ.SPMilitaryExem) + get_currency(IAOTHADJ.SIANOL) + get_currency(IAOTHADJ.SPOrgan) + get_currency(IAOTHADJ.SPK1) + get_currency(IAOTHADJ.SPSegal) + get_currency(IAOTHADJ.SPShell) + get_currency(IAOTHADJ.SStud) + get_currency(IAOTHADJ.SPVictim) + get_currency(IAOTHADJ.SPWages) + get_currency(IAOTHADJ.SPWorkCr) + get_currency(IAOTHADJ.SP2106) + get_currency(IAOTHADJ.SMSA) + get_currency(IAOTHADJ.SPJury) + get_currency(IAOTHADJ.SPRFST) + get_currency(IAOTHADJ.SPSub) + get_currency(IAOTHADJ.SP501c) + get_currency(IAOTHADJ.SPPerRent) + get_currency(IAOTHADJ.SP403b) + get_currency(IAOTHADJ.SPUDC) + get_currency(IAOTHADJ.SPWBF) + get_currency(IAOTHADJ.SP8873) + get_currency(IAOTHADJ.SPEducator) + get_currency(IAOTHADJ.SPTuition) + get_currency(IAOTHADJ.SPElectric) + get_currency(IAOTHADJ.SPRapid) + get_currency(IAOTHADJ.SPOlympic) + get_currency(IAOTHADJ.SPIAABLE)

def SPTuition_Calculation():
    return 0
    #return get_currency(USWRec.STuitAdj)

def SPUDC_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthAdj.SPUDC)
    else:
        return 0

def SPWBF_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthAdj.SPWBF)
    else:
        return 0

def SSN_Calculation():
    return get_string(IAF1040.SSN)

def SStud_Calculation():
    return get_currency(USWRec.SStudAdj)

def TIANOL_Calculation():
    if get_bool(IAF126.TpNonRes) == True:
        return 0
    elif get_bool(USWResidency.F1040NR) == False:
        return Abs(get_currency(USWOthInc.TPNOL))
    else:
        return Abs(get_currency(USWOthIncNR.TPNOL))

def TMSA_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthAdj.TP8853)
    else:
        return get_currency(USWOthAdjNR.TP8853)

def TotNI_Calculation():
    return get_currency(IAOTHADJ.ANet) + get_currency(IAOTHADJ.BNet)

def TP2106_Calculation():
    return get_currency(USWRec.TBusExp2106)

def TP2555_Calculation():
    return get_currency(USWOthAdj.TP2555)

def TP403b_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthAdj.TP403b)
    else:
        return get_currency(USWOthAdjNR.TP403b)

def TP501c_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthAdj.TPTotal501)
    else:
        return get_currency(USWOthAdjNR.Total501)

def TP8873_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthAdj.TP8873)
    else:
        return get_currency(USWOthAdjNR.TP8873)

def TPAltMV_Calculation():
    #2018 expanded instructions - deduction does not apply to purchases on or after 1/1/2015 due to nonconformity, federal does not ask for a purchase date, believe will be very uncommon for ability to take this credit on Iowa, remove calc and make user entered
    #If get_bool(USF8910.Print) = False Then
    return 0
    #ElseIf IAFS() = 3 Then
    #    return max_value(0, 2000@ - get_currency(IAOTHADJ.SPAltMV))
    #Else
    #    return 2000@
    #End If

def TPAmount_Calculation(Index):
    count = Integer()

    Hold = Currency()
    count = 0
    Hold = 0
    if get_currency(IAOTHADJ.TOth1) != 0 or get_currency(IAOTHADJ.SOth1) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TOth1)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPActiveMil) != 0 or get_currency(IAOTHADJ.SPActiveMil) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPActiveMil)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPAltMV) != 0 or get_currency(IAOTHADJ.SPAltMV) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPAltMV)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPInvolConv) != 0 or get_currency(IAOTHADJ.SPInvolConv) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPInvolConv)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPClaimOfRight) != 0 or get_currency(IAOTHADJ.SPClaimOfRight) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPClaimOfRight)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPIAEd) != 0 or get_currency(IAOTHADJ.SPIAEd) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPIAEd)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPIADis) != 0 or get_currency(IAOTHADJ.SPIADis) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPIADis)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPDomProd) != 0 or get_currency(IAOTHADJ.SPDomProd) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPDomProd)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPFirstHmBuy) != 0 or get_currency(IAOTHADJ.SPFirstHmBuy) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPFirstHmBuy)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPEmployerSS) != 0 or get_currency(IAOTHADJ.SPEmployerSS) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPEmployerSS)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPFedFuels) != 0 or get_currency(IAOTHADJ.SPFedFuels) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPFedFuels)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPForeign) != 0 or get_currency(IAOTHADJ.SPForeign) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPForeign)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TP2555) != 0 or get_currency(IAOTHADJ.SP2555) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TP2555)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPDistressed) != 0 or get_currency(IAOTHADJ.SPDistressed) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPDistressed)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPHealthSav) != 0 or get_currency(IAOTHADJ.SPHealthSav) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPHealthSav)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPVet) != 0 or get_currency(IAOTHADJ.SPVet) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPVet)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPVetGrant) != 0 or get_currency(IAOTHADJ.SPVetGrant) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPVetGrant)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPHomeHealth) != 0 or get_currency(IAOTHADJ.SPHomeHealth) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPHomeHealth)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPIAVetTrust) != 0 or get_currency(IAOTHADJ.SPIAVetTrust) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPIAVetTrust)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPMilitaryExem) != 0 or get_currency(IAOTHADJ.SPMilitaryExem) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPMilitaryExem)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TIANOL) != 0 or get_currency(IAOTHADJ.SIANOL) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TIANOL)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPOrgan) != 0 or get_currency(IAOTHADJ.SPOrgan) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPOrgan)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPK1) != 0 or get_currency(IAOTHADJ.SPK1) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPK1)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPSegal) != 0 or get_currency(IAOTHADJ.SPSegal) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPSegal)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPShell) != 0 or get_currency(IAOTHADJ.SPShell) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPShell)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TStud) != 0 or get_currency(IAOTHADJ.SStud) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TStud)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPVictim) != 0 or get_currency(IAOTHADJ.SPVictim) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPVictim)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPWages) != 0 or get_currency(IAOTHADJ.SPWages) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPWages)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPWorkCr) != 0 or get_currency(IAOTHADJ.SPWorkCr) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPWorkCr)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TP2106) != 0 or get_currency(IAOTHADJ.SP2106) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TP2106)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TMSA) != 0 or get_currency(IAOTHADJ.SMSA) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TMSA)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPJury) != 0 or get_currency(IAOTHADJ.SPJury) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPJury)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPRFST) != 0 or get_currency(IAOTHADJ.SPRFST) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPRFST)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPSub) != 0 or get_currency(IAOTHADJ.SPSub) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPSub)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TP501c) != 0 or get_currency(IAOTHADJ.SP501c) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TP501c)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPPerRent) != 0 or get_currency(IAOTHADJ.SPPerRent) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPPerRent)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TP403b) != 0 or get_currency(IAOTHADJ.SP403b) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TP403b)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPUDC) != 0 or get_currency(IAOTHADJ.SPUDC) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPUDC)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPWBF) != 0 or get_currency(IAOTHADJ.SPWBF) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPWBF)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TP8873) != 0 or get_currency(IAOTHADJ.SP8873) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TP8873)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPOlympic) != 0 or get_currency(IAOTHADJ.SPOlympic) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPOlympic)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPEducator) != 0 or get_currency(IAOTHADJ.SPEducator) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPEducator)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPTuition) != 0 or get_currency(IAOTHADJ.SPTuition) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPTuition)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPElectric) != 0 or get_currency(IAOTHADJ.SPElectric) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPElectric)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPRapid) != 0 or get_currency(IAOTHADJ.SPRapid) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPRapid)
            count = 99
        else:
            count = count + 1
    if get_currency(IAOTHADJ.TPIAABLE) != 0 or get_currency(IAOTHADJ.SPIAABLE) != 0:
        if Index == count:
            Hold = get_currency(IAOTHADJ.TPIAABLE)
            count = 99
        else:
            count = count + 1
    return Hold

def TPDomProd_Calculation():
    #Iowa expanded instructions - Iowa has not conformed to the repeal of the federal domestic production activities deduction. For Iowa will need to complete a federal 8903 and keep with their records and follow IA instructions for adjustments needed when calcing.
    #return get_currency(USWRec.TDomProd)
    return 0

def TPEducator_Calculation():
    return get_currency(USWRec.TEdExp)

def TPForeign_Calculation():
    return Abs(get_currency(USWOthInc.TP2555))

def TPHealthSav_Calculation():
    return get_currency(USWRec.THealthSav)

def TPJointAmount_Calculation(Index):
    if get_bool(IAF1040.CombMFS) == True:
        return get_currency(IAOTHADJ.TPAmount(Index))
    else:
        return get_currency(IAOTHADJ.TPAmount(Index)) + get_currency(IAOTHADJ.SPAmount(Index))

def TPJury_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthAdj.TPJury)
    else:
        return 0

def TPK1_Calculation():
    if get_bool(USWResidency.F1040NR) == False and get_currency(USWOthInc.TPK1) < 0:
        return Abs(get_currency(USWOthInc.TPK1))
    elif get_bool(USWResidency.F1040NR) == True and get_currency(USWOthIncNR.TPK1) < 0:
        return Abs(get_currency(USWOthIncNR.TPK1))
    else:
        return 0

def TPName_Calculation():
    return get_string(USWBasicInfo.TPCommon)

def TPOlympic_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthAdj.Text1)
    else:
        return 0

def TPPerRent_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthAdj.TPPerRent)
    else:
        return 0

def TPRFST_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthAdj.TPRFST)
    else:
        return get_currency(USWOthAdjNR.TPRFST)

def TPSub_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthAdj.TPSub)
    else:
        return get_currency(USWOthAdjNR.TPSub)

def TPTot_Calculation():
    return get_currency(IAOTHADJ.TOth1) + get_currency(IAOTHADJ.TPActiveMil) + get_currency(IAOTHADJ.TPAltMV) + get_currency(IAOTHADJ.TPInvolConv) + get_currency(IAOTHADJ.TPClaimOfRight) + get_currency(IAOTHADJ.TPIAEd) + get_currency(IAOTHADJ.TPIADis) + get_currency(IAOTHADJ.TPDomProd) + get_currency(IAOTHADJ.TPFirstHmBuy) + get_currency(IAOTHADJ.TPEmployerSS) + get_currency(IAOTHADJ.TPFedFuels) + get_currency(IAOTHADJ.TPForeign) + get_currency(IAOTHADJ.TP2555) + get_currency(IAOTHADJ.TPDistressed) + get_currency(IAOTHADJ.TPHealthSav) + get_currency(IAOTHADJ.TPVet) + get_currency(IAOTHADJ.TPVetGrant) + get_currency(IAOTHADJ.TPHomeHealth) + get_currency(IAOTHADJ.TPIAVetTrust) + get_currency(IAOTHADJ.TPMilitaryExem) + get_currency(IAOTHADJ.TIANOL) + get_currency(IAOTHADJ.TPOrgan) + get_currency(IAOTHADJ.TPK1) + get_currency(IAOTHADJ.TPSegal) + get_currency(IAOTHADJ.TPShell) + get_currency(IAOTHADJ.TStud) + get_currency(IAOTHADJ.TPVictim) + get_currency(IAOTHADJ.TPWages) + get_currency(IAOTHADJ.TPWorkCr) + get_currency(IAOTHADJ.TP2106) + get_currency(IAOTHADJ.TMSA) + get_currency(IAOTHADJ.TPJury) + get_currency(IAOTHADJ.TPRFST) + get_currency(IAOTHADJ.TPSub) + get_currency(IAOTHADJ.TP501c) + get_currency(IAOTHADJ.TPPerRent) + get_currency(IAOTHADJ.TP403b) + get_currency(IAOTHADJ.TPUDC) + get_currency(IAOTHADJ.TPWBF) + get_currency(IAOTHADJ.TP8873) + get_currency(IAOTHADJ.TPEducator) + get_currency(IAOTHADJ.TPTuition) + get_currency(IAOTHADJ.TPElectric) + get_currency(IAOTHADJ.TPRapid) + get_currency(IAOTHADJ.TPOlympic) + get_currency(IAOTHADJ.TPIAABLE)

def TPTuition_Calculation():
    return 0
    #return get_currency(USWRec.TTuitAdj)

def TPUDC_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthAdj.TPUDC)
    else:
        return get_currency(USWOthAdjNR.TPUDC)

def TPWBF_Calculation():
    if get_bool(USWResidency.F1040NR) == False:
        return get_currency(USWOthAdj.TPWBF)
    else:
        return get_currency(USWOthAdjNR.TPWBF)

def TStud_Calculation():
    return get_currency(USWRec.TStudAdj)


