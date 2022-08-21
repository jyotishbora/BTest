from forms.out import IAF1040
from forms.out import IAF126
from forms.out import IANROTHADJ
from forms.out import IAOTHADJ
from forms.out import IAREQUIRED
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Code_Calculation(Index):
    count = Integer()

    Hold = String()
    count = 0
    Hold = ''
    if get_currency(IANROTHADJ.TOth1) != 0 or get_currency(IANROTHADJ.SOth1) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPActiveMil) != 0 or get_currency(IANROTHADJ.SPActiveMil) != 0:
        if Index == count:
            Hold = 'b'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPAltMV) != 0 or get_currency(IANROTHADJ.SPAltMV) != 0:
        if Index == count:
            Hold = 'c'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPInvolConv) != 0 or get_currency(IANROTHADJ.SPInvolConv) != 0:
        if Index == count:
            Hold = 'e'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPClaimOfRight) != 0 or get_currency(IANROTHADJ.SPClaimOfRight) != 0:
        if Index == count:
            Hold = 'f'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPIAEd) != 0 or get_currency(IANROTHADJ.SPIAEd) != 0:
        if Index == count:
            Hold = 'g'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPIADis) != 0 or get_currency(IANROTHADJ.SPIADis) != 0:
        if Index == count:
            Hold = 'h'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPDomProd) != 0 or get_currency(IANROTHADJ.SPDomProd) != 0:
        if Index == count:
            Hold = 'i'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPFirstHmBuy) != 0 or get_currency(IANROTHADJ.SPFirstHmBuy) != 0:
        if Index == count:
            Hold = 'j'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPEmployerSS) != 0 or get_currency(IANROTHADJ.SPEmployerSS) != 0:
        if Index == count:
            Hold = 'k'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPFedFuels) != 0 or get_currency(IANROTHADJ.SPFedFuels) != 0:
        if Index == count:
            Hold = 'l'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPForeign) != 0 or get_currency(IANROTHADJ.SPForeign) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TP2555) != 0 or get_currency(IANROTHADJ.SP2555) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPDistressed) != 0 or get_currency(IANROTHADJ.SPDistressed) != 0:
        if Index == count:
            Hold = 'n'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPHealthSav) != 0 or get_currency(IANROTHADJ.SPHealthSav) != 0:
        if Index == count:
            Hold = 'o'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPVet) != 0 or get_currency(IANROTHADJ.SPVet) != 0:
        if Index == count:
            Hold = 'p'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPVetGrant) != 0 or get_currency(IANROTHADJ.SPVetGrant) != 0:
        if Index == count:
            Hold = 'q'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPHomeHealth) != 0 or get_currency(IANROTHADJ.SPHomeHealth) != 0:
        if Index == count:
            Hold = 'r'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPIAVetTrust) != 0 or get_currency(IANROTHADJ.SPIAVetTrust) != 0:
        if Index == count:
            Hold = 's'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPMilitaryExem) != 0 or get_currency(IANROTHADJ.SPMilitaryExem) != 0:
        if Index == count:
            Hold = 't'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TIANOL) != 0 or get_currency(IANROTHADJ.SIANOL) != 0:
        if Index == count:
            Hold = 'u'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPOrgan) != 0 or get_currency(IANROTHADJ.SPOrgan) != 0:
        if Index == count:
            Hold = 'v'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPK1) != 0 or get_currency(IANROTHADJ.SPK1) != 0:
        if Index == count:
            Hold = 'w'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPSegal) != 0 or get_currency(IANROTHADJ.SPSegal) != 0:
        if Index == count:
            Hold = 'x'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPShell) != 0 or get_currency(IANROTHADJ.SPShell) != 0:
        if Index == count:
            Hold = 'y'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TStud) != 0 or get_currency(IANROTHADJ.SStud) != 0:
        if Index == count:
            Hold = 'z'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPVictim) != 0 or get_currency(IANROTHADJ.SPVictim) != 0:
        if Index == count:
            Hold = 'aa'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPWages) != 0 or get_currency(IANROTHADJ.SPWages) != 0:
        if Index == count:
            Hold = 'bb'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPWorkCr) != 0 or get_currency(IANROTHADJ.SPWorkCr) != 0:
        if Index == count:
            Hold = 'cc'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TP2106) != 0 or get_currency(IANROTHADJ.SP2106) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TMSA) != 0 or get_currency(IANROTHADJ.SMSA) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPJury) != 0 or get_currency(IANROTHADJ.SPJury) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPRFST) != 0 or get_currency(IANROTHADJ.SPRFST) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPSub) != 0 or get_currency(IANROTHADJ.SPSub) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TP501c) != 0 or get_currency(IANROTHADJ.SP501c) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPPerRent) != 0 or get_currency(IANROTHADJ.SPPerRent) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TP403b) != 0 or get_currency(IANROTHADJ.SP403b) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPUDC) != 0 or get_currency(IANROTHADJ.SPUDC) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPWBF) != 0 or get_currency(IANROTHADJ.SPWBF) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TP8873) != 0 or get_currency(IANROTHADJ.SP8873) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPOlympic) != 0 or get_currency(IANROTHADJ.SPOlympic) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPEducator) != 0 or get_currency(IANROTHADJ.SPEducator) != 0:
        if Index == count:
            Hold = 'ee'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPTuition) != 0 or get_currency(IANROTHADJ.SPTuition) != 0:
        if Index == count:
            Hold = 'ff'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPElectric) != 0 or get_currency(IANROTHADJ.SPElectric) != 0:
        if Index == count:
            Hold = 'gg'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPRapid) != 0 or get_currency(IANROTHADJ.SPRapid) != 0:
        if Index == count:
            Hold = 'hh'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPIAABLE) != 0 or get_currency(IANROTHADJ.SPIAABLE) != 0:
        if Index == count:
            Hold = 'ii'
            count = 99
        else:
            count = count + 1
    return Hold

def Desc_Calculation():
    Total = Currency()
    Total = get_currency(IANROTHADJ.TPTot) + get_currency(IANROTHADJ.SPTot)
    return CStr(Total)

def Description_Calculation(Index):
    count = Integer()

    Hold = String()
    count = 0
    Hold = ''
    if get_currency(IANROTHADJ.TOth1) != 0 or get_currency(IANROTHADJ.SOth1) != 0:
        if Index == count:
            Hold = get_string(IANROTHADJ.TxtOth1)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPActiveMil) != 0 or get_currency(IANROTHADJ.SPActiveMil) != 0:
        if Index == count:
            Hold = 'Active duty military pay'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPAltMV) != 0 or get_currency(IANROTHADJ.SPAltMV) != 0:
        if Index == count:
            Hold = 'Alternative motor vehicle deduction'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPInvolConv) != 0 or get_currency(IANROTHADJ.SPInvolConv) != 0:
        if Index == count:
            Hold = 'Capital or ordinary gain from involuntary conversion'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPClaimOfRight) != 0 or get_currency(IANROTHADJ.SPClaimOfRight) != 0:
        if Index == count:
            Hold = 'Claim of Right deduction'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPIAEd) != 0 or get_currency(IANROTHADJ.SPIAEd) != 0:
        if Index == count:
            Hold = 'College Savings Iowa or Iowa Advisor 529 Plan'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPIADis) != 0 or get_currency(IANROTHADJ.SPIADis) != 0:
        if Index == count:
            Hold = 'Disability income exclusion'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPDomProd) != 0 or get_currency(IANROTHADJ.SPDomProd) != 0:
        if Index == count:
            Hold = 'Domestic production activities deduction'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPFirstHmBuy) != 0 or get_currency(IANROTHADJ.SPFirstHmBuy) != 0:
        if Index == count:
            Hold = 'First-Time Homebuyer Savings Account qualifying contributions'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPEmployerSS) != 0 or get_currency(IANROTHADJ.SPEmployerSS) != 0:
        if Index == count:
            Hold = 'Employer social security credit, federal Form 8846'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPFedFuels) != 0 or get_currency(IANROTHADJ.SPFedFuels) != 0:
        if Index == count:
            Hold = 'Alcohol and cellulosic biofuel credit, federal Form 6478'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPForeign) != 0 or get_currency(IANROTHADJ.SPForeign) != 0:
        if Index == count:
            Hold = 'Foreign earned income exclusion, federal Form 2555'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TP2555) != 0 or get_currency(IANROTHADJ.SP2555) != 0:
        if Index == count:
            Hold = 'Foreign housing deduction, federal Form 2555'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPDistressed) != 0 or get_currency(IANROTHADJ.SPDistressed) != 0:
        if Index == count:
            Hold = 'Gains or losses from distressed sale transactions'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPHealthSav) != 0 or get_currency(IANROTHADJ.SPHealthSav) != 0:
        if Index == count:
            Hold = 'Health savings account deduction, federal Form 8889'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPVet) != 0 or get_currency(IANROTHADJ.SPVet) != 0:
        if Index == count:
            Hold = 'Injured veterans programs - contributions'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPVetGrant) != 0 or get_currency(IANROTHADJ.SPVetGrant) != 0:
        if Index == count:
            Hold = 'Injured veterans programs - grants'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPHomeHealth) != 0 or get_currency(IANROTHADJ.SPHomeHealth) != 0:
        if Index == count:
            Hold = 'In-home health care'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPIAVetTrust) != 0 or get_currency(IANROTHADJ.SPIAVetTrust) != 0:
        if Index == count:
            Hold = 'Iowa Veterans Trust Fund'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPMilitaryExem) != 0 or get_currency(IANROTHADJ.SPMilitaryExem) != 0:
        if Index == count:
            Hold = 'Military exemptions'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TIANOL) != 0 or get_currency(IANROTHADJ.SIANOL) != 0:
        if Index == count:
            Hold = 'Iowa Net Operating Loss'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPOrgan) != 0 or get_currency(IANROTHADJ.SPOrgan) != 0:
        if Index == count:
            Hold = 'Organ transplant expenses'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPK1) != 0 or get_currency(IANROTHADJ.SPK1) != 0:
        if Index == count:
            Hold = 'Partnership income and/or S Corporation income'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPSegal) != 0 or get_currency(IANROTHADJ.SPSegal) != 0:
        if Index == count:
            Hold = 'Segal Americorps Education Award payments'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPShell) != 0 or get_currency(IANROTHADJ.SPShell) != 0:
        if Index == count:
            Hold = 'Speculative shell buildings'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TStud) != 0 or get_currency(IANROTHADJ.SStud) != 0:
        if Index == count:
            Hold = 'Student loan interest deduction'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPVictim) != 0 or get_currency(IANROTHADJ.SPVictim) != 0:
        if Index == count:
            Hold = 'Victim compensation awards'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPWages) != 0 or get_currency(IANROTHADJ.SPWages) != 0:
        if Index == count:
            Hold = 'Wages paid to certain individuals'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPWorkCr) != 0 or get_currency(IANROTHADJ.SPWorkCr) != 0:
        if Index == count:
            Hold = 'Work opportunity credit, federal Form 5884'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TP2106) != 0 or get_currency(IANROTHADJ.SP2106) != 0:
        if Index == count:
            Hold = 'Business expenses of reservists, QPA, FBO, federal Form 2106'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TMSA) != 0 or get_currency(IANROTHADJ.SMSA) != 0:
        if Index == count:
            Hold = 'Archer MSA deduction, federal Form 8853'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPJury) != 0 or get_currency(IANROTHADJ.SPJury) != 0:
        if Index == count:
            Hold = 'Jury pay repayment to employer'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPRFST) != 0 or get_currency(IANROTHADJ.SPRFST) != 0:
        if Index == count:
            Hold = 'Reforestation amortization and expenses'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPSub) != 0 or get_currency(IANROTHADJ.SPSub) != 0:
        if Index == count:
            Hold = 'Repayment of supplemental unemployment benefits'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TP501c) != 0 or get_currency(IANROTHADJ.SP501c) != 0:
        if Index == count:
            Hold = 'Contributions to a 501(c)(18) pension plan'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPPerRent) != 0 or get_currency(IANROTHADJ.SPPerRent) != 0:
        if Index == count:
            Hold = 'Expenses for personal property rental'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TP403b) != 0 or get_currency(IANROTHADJ.SP403b) != 0:
        if Index == count:
            Hold = 'Contributions by certain chaplains to a 403(b) plan'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPUDC) != 0 or get_currency(IANROTHADJ.SPUDC) != 0:
        if Index == count:
            Hold = 'Qualified attorney/court fees paid after 10/22/2004'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPWBF) != 0 or get_currency(IANROTHADJ.SPWBF) != 0:
        if Index == count:
            Hold = 'Qualified whistleblower fees'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TP8873) != 0 or get_currency(IANROTHADJ.SP8873) != 0:
        if Index == count:
            Hold = 'Extraterritorial Income Exclusion, federal Form 8873'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPOlympic) != 0 or get_currency(IANROTHADJ.SPOlympic) != 0:
        if Index == count:
            Hold = 'Nontaxable amount of Olympic and Paralympic medals and USOC prize money'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPEducator) != 0 or get_currency(IANROTHADJ.SPEducator) != 0:
        if Index == count:
            Hold = 'Educator expenses'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPTuition) != 0 or get_currency(IANROTHADJ.SPTuition) != 0:
        if Index == count:
            Hold = 'Tuition and fees deduction'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPElectric) != 0 or get_currency(IANROTHADJ.SPElectric) != 0:
        if Index == count:
            Hold = 'Nonresident Electric Utility Reciprocity'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPRapid) != 0 or get_currency(IANROTHADJ.SPRapid) != 0:
        if Index == count:
            Hold = 'Rapid Response to State Disasters'
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPIAABLE) != 0 or get_currency(IANROTHADJ.SPIAABLE) != 0:
        if Index == count:
            Hold = 'Iowa ABLE savings plan trust'
            count = 99
        else:
            count = count + 1
    return Hold

def Names_Calculation():
    return get_string(IAREQUIRED.CombNames)

def PrintMe_Calculation():
    if get_currency(IANROTHADJ.TPTot) != 0 or get_currency(IANROTHADJ.SPTot) != 0:
        return 1
    else:
        return 0

def SPAmount_Calculation(Index):
    count = Integer()

    Hold = Currency()
    count = 0
    Hold = 0
    if get_currency(IANROTHADJ.TOth1) != 0 or get_currency(IANROTHADJ.SOth1) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SOth1)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPActiveMil) != 0 or get_currency(IANROTHADJ.SPActiveMil) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPActiveMil)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPAltMV) != 0 or get_currency(IANROTHADJ.SPAltMV) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPAltMV)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPInvolConv) != 0 or get_currency(IANROTHADJ.SPInvolConv) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPInvolConv)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPClaimOfRight) != 0 or get_currency(IANROTHADJ.SPClaimOfRight) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPClaimOfRight)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPIAEd) != 0 or get_currency(IANROTHADJ.SPIAEd) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPIAEd)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPIADis) != 0 or get_currency(IANROTHADJ.SPIADis) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPIADis)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPDomProd) != 0 or get_currency(IANROTHADJ.SPDomProd) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPDomProd)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPFirstHmBuy) != 0 or get_currency(IANROTHADJ.SPFirstHmBuy) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPFirstHmBuy)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPEmployerSS) != 0 or get_currency(IANROTHADJ.SPEmployerSS) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPEmployerSS)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPFedFuels) != 0 or get_currency(IANROTHADJ.SPFedFuels) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPFedFuels)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPForeign) != 0 or get_currency(IANROTHADJ.SPForeign) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPForeign)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TP2555) != 0 or get_currency(IANROTHADJ.SP2555) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SP2555)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPDistressed) != 0 or get_currency(IANROTHADJ.SPDistressed) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPDistressed)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPHealthSav) != 0 or get_currency(IANROTHADJ.SPHealthSav) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPHealthSav)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPVet) != 0 or get_currency(IANROTHADJ.SPVet) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPVet)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPVetGrant) != 0 or get_currency(IANROTHADJ.SPVetGrant) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPVetGrant)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPHomeHealth) != 0 or get_currency(IANROTHADJ.SPHomeHealth) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPHomeHealth)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPIAVetTrust) != 0 or get_currency(IANROTHADJ.SPIAVetTrust) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPIAVetTrust)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPMilitaryExem) != 0 or get_currency(IANROTHADJ.SPMilitaryExem) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPMilitaryExem)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TIANOL) != 0 or get_currency(IANROTHADJ.SIANOL) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SIANOL)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPOrgan) != 0 or get_currency(IANROTHADJ.SPOrgan) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPOrgan)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPK1) != 0 or get_currency(IANROTHADJ.SPK1) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPK1)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPSegal) != 0 or get_currency(IANROTHADJ.SPSegal) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPSegal)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPShell) != 0 or get_currency(IANROTHADJ.SPShell) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPShell)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TStud) != 0 or get_currency(IANROTHADJ.SStud) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SStud)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPVictim) != 0 or get_currency(IANROTHADJ.SPVictim) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPVictim)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPWages) != 0 or get_currency(IANROTHADJ.SPWages) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPWages)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPWorkCr) != 0 or get_currency(IANROTHADJ.SPWorkCr) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPWorkCr)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TP2106) != 0 or get_currency(IANROTHADJ.SP2106) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SP2106)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TMSA) != 0 or get_currency(IANROTHADJ.SMSA) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SMSA)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPJury) != 0 or get_currency(IANROTHADJ.SPJury) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPJury)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPRFST) != 0 or get_currency(IANROTHADJ.SPRFST) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPRFST)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPSub) != 0 or get_currency(IANROTHADJ.SPSub) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPSub)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TP501c) != 0 or get_currency(IANROTHADJ.SP501c) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SP501c)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPPerRent) != 0 or get_currency(IANROTHADJ.SPPerRent) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPPerRent)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TP403b) != 0 or get_currency(IANROTHADJ.SP403b) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SP403b)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPUDC) != 0 or get_currency(IANROTHADJ.SPUDC) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPUDC)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPWBF) != 0 or get_currency(IANROTHADJ.SPWBF) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPWBF)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TP8873) != 0 or get_currency(IANROTHADJ.SP8873) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SP8873)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPOlympic) != 0 or get_currency(IANROTHADJ.SPOlympic) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPOlympic)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPEducator) != 0 or get_currency(IANROTHADJ.SPEducator) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPEducator)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPTuition) != 0 or get_currency(IANROTHADJ.SPTuition) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPTuition)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPElectric) != 0 or get_currency(IANROTHADJ.SPElectric) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPElectric)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPRapid) != 0 or get_currency(IANROTHADJ.SPRapid) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPRapid)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPIAABLE) != 0 or get_currency(IANROTHADJ.SPIAABLE) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.SPIAABLE)
            count = 99
        else:
            count = count + 1
    return Hold

def SPName_Calculation():
    return get_string(USWBasicInfo.SPCommon)

def SPTot_Calculation():
    if get_bool(IAREQUIRED.AskSpouse) == True and get_bool(IAF126.SpRes) == False:
        return get_currency(IANROTHADJ.SOth1) + get_currency(IANROTHADJ.SPActiveMil) + get_currency(IANROTHADJ.SPAltMV) + get_currency(IANROTHADJ.SPInvolConv) + get_currency(IANROTHADJ.SPClaimOfRight) + get_currency(IANROTHADJ.SPIAEd) + get_currency(IANROTHADJ.SPIADis) + get_currency(IANROTHADJ.SPDomProd) + get_currency(IANROTHADJ.SPFirstHmBuy) + get_currency(IANROTHADJ.SPEmployerSS) + get_currency(IANROTHADJ.SPFedFuels) + get_currency(IANROTHADJ.SPForeign) + get_currency(IANROTHADJ.SP2555) + get_currency(IANROTHADJ.SPDistressed) + get_currency(IANROTHADJ.SPHealthSav) + get_currency(IANROTHADJ.SPVet) + get_currency(IANROTHADJ.SPVetGrant) + get_currency(IANROTHADJ.SPHomeHealth) + get_currency(IANROTHADJ.SPIAVetTrust) + get_currency(IANROTHADJ.SPMilitaryExem) + get_currency(IANROTHADJ.SIANOL) + get_currency(IANROTHADJ.SPOrgan) + get_currency(IANROTHADJ.SPK1) + get_currency(IANROTHADJ.SPSegal) + get_currency(IANROTHADJ.SPShell) + get_currency(IANROTHADJ.SStud) + get_currency(IANROTHADJ.SPVictim) + get_currency(IANROTHADJ.SPWages) + get_currency(IANROTHADJ.SPWorkCr) + get_currency(IANROTHADJ.SP2106) + get_currency(IANROTHADJ.SMSA) + get_currency(IANROTHADJ.SPJury) + get_currency(IANROTHADJ.SPRFST) + get_currency(IANROTHADJ.SPSub) + get_currency(IANROTHADJ.SP501c) + get_currency(IANROTHADJ.SPPerRent) + get_currency(IANROTHADJ.SP403b) + get_currency(IANROTHADJ.SPUDC) + get_currency(IANROTHADJ.SPWBF) + get_currency(IANROTHADJ.SP8873) + get_currency(IANROTHADJ.SPOlympic) + get_currency(IANROTHADJ.SPEducator) + get_currency(IANROTHADJ.SPTuition) + get_currency(IANROTHADJ.SPElectric) + get_currency(IANROTHADJ.SPRapid) + get_currency(IANROTHADJ.SPIAABLE)
    else:
        return 0

def SSN_Calculation():
    return get_string(IAF1040.SSN)

def TPAmount_Calculation(Index):
    count = Integer()

    Hold = Currency()
    count = 0
    Hold = 0
    if get_currency(IANROTHADJ.TOth1) != 0 or get_currency(IANROTHADJ.SOth1) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TOth1)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPActiveMil) != 0 or get_currency(IANROTHADJ.SPActiveMil) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPActiveMil)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPAltMV) != 0 or get_currency(IANROTHADJ.SPAltMV) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPAltMV)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPInvolConv) != 0 or get_currency(IANROTHADJ.SPInvolConv) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPInvolConv)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPClaimOfRight) != 0 or get_currency(IANROTHADJ.SPClaimOfRight) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPClaimOfRight)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPIAEd) != 0 or get_currency(IANROTHADJ.SPIAEd) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPIAEd)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPIADis) != 0 or get_currency(IANROTHADJ.SPIADis) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPIADis)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPDomProd) != 0 or get_currency(IANROTHADJ.SPDomProd) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPDomProd)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPFirstHmBuy) != 0 or get_currency(IANROTHADJ.SPFirstHmBuy) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPFirstHmBuy)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPEmployerSS) != 0 or get_currency(IANROTHADJ.SPEmployerSS) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPEmployerSS)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPFedFuels) != 0 or get_currency(IANROTHADJ.SPFedFuels) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPFedFuels)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPForeign) != 0 or get_currency(IANROTHADJ.SPForeign) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPForeign)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TP2555) != 0 or get_currency(IANROTHADJ.SP2555) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TP2555)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPDistressed) != 0 or get_currency(IANROTHADJ.SPDistressed) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPDistressed)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPHealthSav) != 0 or get_currency(IANROTHADJ.SPHealthSav) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPHealthSav)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPVet) != 0 or get_currency(IANROTHADJ.SPVet) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPVet)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPVetGrant) != 0 or get_currency(IANROTHADJ.SPVetGrant) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPVetGrant)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPHomeHealth) != 0 or get_currency(IANROTHADJ.SPHomeHealth) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPHomeHealth)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPIAVetTrust) != 0 or get_currency(IANROTHADJ.SPIAVetTrust) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPIAVetTrust)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPMilitaryExem) != 0 or get_currency(IANROTHADJ.SPMilitaryExem) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPMilitaryExem)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TIANOL) != 0 or get_currency(IANROTHADJ.SIANOL) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TIANOL)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPOrgan) != 0 or get_currency(IANROTHADJ.SPOrgan) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPOrgan)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPK1) != 0 or get_currency(IANROTHADJ.SPK1) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPK1)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPSegal) != 0 or get_currency(IANROTHADJ.SPSegal) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPSegal)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPShell) != 0 or get_currency(IANROTHADJ.SPShell) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPShell)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TStud) != 0 or get_currency(IANROTHADJ.SStud) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TStud)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPVictim) != 0 or get_currency(IANROTHADJ.SPVictim) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPVictim)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPWages) != 0 or get_currency(IANROTHADJ.SPWages) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPWages)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPWorkCr) != 0 or get_currency(IANROTHADJ.SPWorkCr) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPWorkCr)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TP2106) != 0 or get_currency(IANROTHADJ.SP2106) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TP2106)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TMSA) != 0 or get_currency(IANROTHADJ.SMSA) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TMSA)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPJury) != 0 or get_currency(IANROTHADJ.SPJury) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPJury)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPRFST) != 0 or get_currency(IANROTHADJ.SPRFST) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPRFST)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPSub) != 0 or get_currency(IANROTHADJ.SPSub) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPSub)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TP501c) != 0 or get_currency(IANROTHADJ.SP501c) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TP501c)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPPerRent) != 0 or get_currency(IANROTHADJ.SPPerRent) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPPerRent)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TP403b) != 0 or get_currency(IANROTHADJ.SP403b) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TP403b)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPUDC) != 0 or get_currency(IANROTHADJ.SPUDC) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPUDC)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPWBF) != 0 or get_currency(IANROTHADJ.SPWBF) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPWBF)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TP8873) != 0 or get_currency(IANROTHADJ.SP8873) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TP8873)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPOlympic) != 0 or get_currency(IANROTHADJ.SPOlympic) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPOlympic)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPEducator) != 0 or get_currency(IANROTHADJ.SPEducator) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPEducator)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPTuition) != 0 or get_currency(IANROTHADJ.SPTuition) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPTuition)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPElectric) != 0 or get_currency(IANROTHADJ.SPElectric) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPElectric)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPRapid) != 0 or get_currency(IANROTHADJ.SPRapid) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPRapid)
            count = 99
        else:
            count = count + 1
    if get_currency(IANROTHADJ.TPIAABLE) != 0 or get_currency(IANROTHADJ.SPIAABLE) != 0:
        if Index == count:
            Hold = get_currency(IANROTHADJ.TPIAABLE)
            count = 99
        else:
            count = count + 1
    return Hold

def TPJointAmount_Calculation(Index):
    if get_bool(IAF1040.CombMFS) == True:
        return get_currency(IANROTHADJ.TPAmount(Index))
    else:
        return get_currency(IANROTHADJ.TPAmount(Index)) + get_currency(IANROTHADJ.SPAmount(Index))

def TPName_Calculation():
    return get_string(USWBasicInfo.TPCommon)

def TPTot_Calculation():
    if get_bool(IAF126.TpPYRes) == True or get_bool(IAF126.TpNonRes) == True:
        return get_currency(IANROTHADJ.TOth1) + get_currency(IANROTHADJ.TPActiveMil) + get_currency(IANROTHADJ.TPAltMV) + get_currency(IANROTHADJ.TPInvolConv) + get_currency(IANROTHADJ.TPClaimOfRight) + get_currency(IANROTHADJ.TPIAEd) + get_currency(IANROTHADJ.TPIADis) + get_currency(IANROTHADJ.TPDomProd) + get_currency(IANROTHADJ.TPFirstHmBuy) + get_currency(IANROTHADJ.TPEmployerSS) + get_currency(IANROTHADJ.TPFedFuels) + get_currency(IANROTHADJ.TPForeign) + get_currency(IANROTHADJ.TP2555) + get_currency(IANROTHADJ.TPDistressed) + get_currency(IANROTHADJ.TPHealthSav) + get_currency(IANROTHADJ.TPVet) + get_currency(IANROTHADJ.TPVetGrant) + get_currency(IANROTHADJ.TPHomeHealth) + get_currency(IANROTHADJ.TPIAVetTrust) + get_currency(IANROTHADJ.TPMilitaryExem) + get_currency(IANROTHADJ.TIANOL) + get_currency(IANROTHADJ.TPOrgan) + get_currency(IANROTHADJ.TPK1) + get_currency(IANROTHADJ.TPSegal) + get_currency(IANROTHADJ.TPShell) + get_currency(IANROTHADJ.TStud) + get_currency(IANROTHADJ.TPVictim) + get_currency(IANROTHADJ.TPWages) + get_currency(IANROTHADJ.TPWorkCr) + get_currency(IANROTHADJ.TP2106) + get_currency(IANROTHADJ.TMSA) + get_currency(IANROTHADJ.TPJury) + get_currency(IANROTHADJ.TPRFST) + get_currency(IANROTHADJ.TPSub) + get_currency(IANROTHADJ.TP501c) + get_currency(IANROTHADJ.TPPerRent) + get_currency(IANROTHADJ.TP403b) + get_currency(IANROTHADJ.TPUDC) + get_currency(IANROTHADJ.TPWBF) + get_currency(IANROTHADJ.TP8873) + get_currency(IANROTHADJ.TPOlympic) + get_currency(IANROTHADJ.TPEducator) + get_currency(IANROTHADJ.TPTuition) + get_currency(IANROTHADJ.TPElectric) + get_currency(IANROTHADJ.TPRapid) + get_currency(IANROTHADJ.TPIAABLE)
    else:
        return 0

def TxtOth1_Calculation():
    return get_string(IAOTHADJ.TxtOth1)


