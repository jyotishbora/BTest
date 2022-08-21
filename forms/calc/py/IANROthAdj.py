from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Code_Calculation(Index):
    count = Integer()

    Hold = String()
    count = 0
    Hold = ''
    if GetCurrency(IANROthAdj.TOth1) != 0 or GetCurrency(IANROthAdj.SOth1) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPActiveMil) != 0 or GetCurrency(IANROthAdj.SPActiveMil) != 0:
        if Index == count:
            Hold = 'b'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPAltMV) != 0 or GetCurrency(IANROthAdj.SPAltMV) != 0:
        if Index == count:
            Hold = 'c'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPInvolConv) != 0 or GetCurrency(IANROthAdj.SPInvolConv) != 0:
        if Index == count:
            Hold = 'e'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPClaimOfRight) != 0 or GetCurrency(IANROthAdj.SPClaimOfRight) != 0:
        if Index == count:
            Hold = 'f'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPIAEd) != 0 or GetCurrency(IANROthAdj.SPIAEd) != 0:
        if Index == count:
            Hold = 'g'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPIADis) != 0 or GetCurrency(IANROthAdj.SPIADis) != 0:
        if Index == count:
            Hold = 'h'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPDomProd) != 0 or GetCurrency(IANROthAdj.SPDomProd) != 0:
        if Index == count:
            Hold = 'i'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPFirstHmBuy) != 0 or GetCurrency(IANROthAdj.SPFirstHmBuy) != 0:
        if Index == count:
            Hold = 'j'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPEmployerSS) != 0 or GetCurrency(IANROthAdj.SPEmployerSS) != 0:
        if Index == count:
            Hold = 'k'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPFedFuels) != 0 or GetCurrency(IANROthAdj.SPFedFuels) != 0:
        if Index == count:
            Hold = 'l'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPForeign) != 0 or GetCurrency(IANROthAdj.SPForeign) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TP2555) != 0 or GetCurrency(IANROthAdj.SP2555) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPDistressed) != 0 or GetCurrency(IANROthAdj.SPDistressed) != 0:
        if Index == count:
            Hold = 'n'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPHealthSav) != 0 or GetCurrency(IANROthAdj.SPHealthSav) != 0:
        if Index == count:
            Hold = 'o'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPVet) != 0 or GetCurrency(IANROthAdj.SPVet) != 0:
        if Index == count:
            Hold = 'p'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPVetGrant) != 0 or GetCurrency(IANROthAdj.SPVetGrant) != 0:
        if Index == count:
            Hold = 'q'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPHomeHealth) != 0 or GetCurrency(IANROthAdj.SPHomeHealth) != 0:
        if Index == count:
            Hold = 'r'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPIAVetTrust) != 0 or GetCurrency(IANROthAdj.SPIAVetTrust) != 0:
        if Index == count:
            Hold = 's'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPMilitaryExem) != 0 or GetCurrency(IANROthAdj.SPMilitaryExem) != 0:
        if Index == count:
            Hold = 't'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TIANOL) != 0 or GetCurrency(IANROthAdj.SIANOL) != 0:
        if Index == count:
            Hold = 'u'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPOrgan) != 0 or GetCurrency(IANROthAdj.SPOrgan) != 0:
        if Index == count:
            Hold = 'v'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPK1) != 0 or GetCurrency(IANROthAdj.SPK1) != 0:
        if Index == count:
            Hold = 'w'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPSegal) != 0 or GetCurrency(IANROthAdj.SPSegal) != 0:
        if Index == count:
            Hold = 'x'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPShell) != 0 or GetCurrency(IANROthAdj.SPShell) != 0:
        if Index == count:
            Hold = 'y'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TStud) != 0 or GetCurrency(IANROthAdj.SStud) != 0:
        if Index == count:
            Hold = 'z'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPVictim) != 0 or GetCurrency(IANROthAdj.SPVictim) != 0:
        if Index == count:
            Hold = 'aa'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPWages) != 0 or GetCurrency(IANROthAdj.SPWages) != 0:
        if Index == count:
            Hold = 'bb'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPWorkCr) != 0 or GetCurrency(IANROthAdj.SPWorkCr) != 0:
        if Index == count:
            Hold = 'cc'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TP2106) != 0 or GetCurrency(IANROthAdj.SP2106) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TMSA) != 0 or GetCurrency(IANROthAdj.SMSA) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPJury) != 0 or GetCurrency(IANROthAdj.SPJury) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPRFST) != 0 or GetCurrency(IANROthAdj.SPRFST) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPSub) != 0 or GetCurrency(IANROthAdj.SPSub) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TP501c) != 0 or GetCurrency(IANROthAdj.SP501c) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPPerRent) != 0 or GetCurrency(IANROthAdj.SPPerRent) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TP403b) != 0 or GetCurrency(IANROthAdj.SP403b) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPUDC) != 0 or GetCurrency(IANROthAdj.SPUDC) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPWBF) != 0 or GetCurrency(IANROthAdj.SPWBF) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TP8873) != 0 or GetCurrency(IANROthAdj.SP8873) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPOlympic) != 0 or GetCurrency(IANROthAdj.SPOlympic) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPEducator) != 0 or GetCurrency(IANROthAdj.SPEducator) != 0:
        if Index == count:
            Hold = 'ee'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPTuition) != 0 or GetCurrency(IANROthAdj.SPTuition) != 0:
        if Index == count:
            Hold = 'ff'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPElectric) != 0 or GetCurrency(IANROthAdj.SPElectric) != 0:
        if Index == count:
            Hold = 'gg'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPRapid) != 0 or GetCurrency(IANROthAdj.SPRapid) != 0:
        if Index == count:
            Hold = 'hh'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPIAABLE) != 0 or GetCurrency(IANROthAdj.SPIAABLE) != 0:
        if Index == count:
            Hold = 'ii'
            count = 99
        else:
            count = count + 1
    ReturnVal = Hold

def Desc_Calculation():
    Total = Currency()
    Total = GetCurrency(IANROthAdj.TPTot) + GetCurrency(IANROthAdj.SPTot)
    ReturnVal = CStr(Total)

def Description_Calculation(Index):
    count = Integer()

    Hold = String()
    count = 0
    Hold = ''
    if GetCurrency(IANROthAdj.TOth1) != 0 or GetCurrency(IANROthAdj.SOth1) != 0:
        if Index == count:
            Hold = GetString(IANROthAdj.TxtOth1)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPActiveMil) != 0 or GetCurrency(IANROthAdj.SPActiveMil) != 0:
        if Index == count:
            Hold = 'Active duty military pay'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPAltMV) != 0 or GetCurrency(IANROthAdj.SPAltMV) != 0:
        if Index == count:
            Hold = 'Alternative motor vehicle deduction'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPInvolConv) != 0 or GetCurrency(IANROthAdj.SPInvolConv) != 0:
        if Index == count:
            Hold = 'Capital or ordinary gain from involuntary conversion'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPClaimOfRight) != 0 or GetCurrency(IANROthAdj.SPClaimOfRight) != 0:
        if Index == count:
            Hold = 'Claim of Right deduction'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPIAEd) != 0 or GetCurrency(IANROthAdj.SPIAEd) != 0:
        if Index == count:
            Hold = 'College Savings Iowa or Iowa Advisor 529 Plan'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPIADis) != 0 or GetCurrency(IANROthAdj.SPIADis) != 0:
        if Index == count:
            Hold = 'Disability income exclusion'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPDomProd) != 0 or GetCurrency(IANROthAdj.SPDomProd) != 0:
        if Index == count:
            Hold = 'Domestic production activities deduction'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPFirstHmBuy) != 0 or GetCurrency(IANROthAdj.SPFirstHmBuy) != 0:
        if Index == count:
            Hold = 'First-Time Homebuyer Savings Account qualifying contributions'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPEmployerSS) != 0 or GetCurrency(IANROthAdj.SPEmployerSS) != 0:
        if Index == count:
            Hold = 'Employer social security credit, federal Form 8846'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPFedFuels) != 0 or GetCurrency(IANROthAdj.SPFedFuels) != 0:
        if Index == count:
            Hold = 'Alcohol and cellulosic biofuel credit, federal Form 6478'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPForeign) != 0 or GetCurrency(IANROthAdj.SPForeign) != 0:
        if Index == count:
            Hold = 'Foreign earned income exclusion, federal Form 2555'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TP2555) != 0 or GetCurrency(IANROthAdj.SP2555) != 0:
        if Index == count:
            Hold = 'Foreign housing deduction, federal Form 2555'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPDistressed) != 0 or GetCurrency(IANROthAdj.SPDistressed) != 0:
        if Index == count:
            Hold = 'Gains or losses from distressed sale transactions'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPHealthSav) != 0 or GetCurrency(IANROthAdj.SPHealthSav) != 0:
        if Index == count:
            Hold = 'Health savings account deduction, federal Form 8889'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPVet) != 0 or GetCurrency(IANROthAdj.SPVet) != 0:
        if Index == count:
            Hold = 'Injured veterans programs - contributions'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPVetGrant) != 0 or GetCurrency(IANROthAdj.SPVetGrant) != 0:
        if Index == count:
            Hold = 'Injured veterans programs - grants'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPHomeHealth) != 0 or GetCurrency(IANROthAdj.SPHomeHealth) != 0:
        if Index == count:
            Hold = 'In-home health care'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPIAVetTrust) != 0 or GetCurrency(IANROthAdj.SPIAVetTrust) != 0:
        if Index == count:
            Hold = 'Iowa Veterans Trust Fund'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPMilitaryExem) != 0 or GetCurrency(IANROthAdj.SPMilitaryExem) != 0:
        if Index == count:
            Hold = 'Military exemptions'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TIANOL) != 0 or GetCurrency(IANROthAdj.SIANOL) != 0:
        if Index == count:
            Hold = 'Iowa Net Operating Loss'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPOrgan) != 0 or GetCurrency(IANROthAdj.SPOrgan) != 0:
        if Index == count:
            Hold = 'Organ transplant expenses'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPK1) != 0 or GetCurrency(IANROthAdj.SPK1) != 0:
        if Index == count:
            Hold = 'Partnership income and/or S Corporation income'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPSegal) != 0 or GetCurrency(IANROthAdj.SPSegal) != 0:
        if Index == count:
            Hold = 'Segal Americorps Education Award payments'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPShell) != 0 or GetCurrency(IANROthAdj.SPShell) != 0:
        if Index == count:
            Hold = 'Speculative shell buildings'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TStud) != 0 or GetCurrency(IANROthAdj.SStud) != 0:
        if Index == count:
            Hold = 'Student loan interest deduction'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPVictim) != 0 or GetCurrency(IANROthAdj.SPVictim) != 0:
        if Index == count:
            Hold = 'Victim compensation awards'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPWages) != 0 or GetCurrency(IANROthAdj.SPWages) != 0:
        if Index == count:
            Hold = 'Wages paid to certain individuals'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPWorkCr) != 0 or GetCurrency(IANROthAdj.SPWorkCr) != 0:
        if Index == count:
            Hold = 'Work opportunity credit, federal Form 5884'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TP2106) != 0 or GetCurrency(IANROthAdj.SP2106) != 0:
        if Index == count:
            Hold = 'Business expenses of reservists, QPA, FBO, federal Form 2106'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TMSA) != 0 or GetCurrency(IANROthAdj.SMSA) != 0:
        if Index == count:
            Hold = 'Archer MSA deduction, federal Form 8853'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPJury) != 0 or GetCurrency(IANROthAdj.SPJury) != 0:
        if Index == count:
            Hold = 'Jury pay repayment to employer'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPRFST) != 0 or GetCurrency(IANROthAdj.SPRFST) != 0:
        if Index == count:
            Hold = 'Reforestation amortization and expenses'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPSub) != 0 or GetCurrency(IANROthAdj.SPSub) != 0:
        if Index == count:
            Hold = 'Repayment of supplemental unemployment benefits'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TP501c) != 0 or GetCurrency(IANROthAdj.SP501c) != 0:
        if Index == count:
            Hold = 'Contributions to a 501(c)(18) pension plan'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPPerRent) != 0 or GetCurrency(IANROthAdj.SPPerRent) != 0:
        if Index == count:
            Hold = 'Expenses for personal property rental'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TP403b) != 0 or GetCurrency(IANROthAdj.SP403b) != 0:
        if Index == count:
            Hold = 'Contributions by certain chaplains to a 403(b) plan'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPUDC) != 0 or GetCurrency(IANROthAdj.SPUDC) != 0:
        if Index == count:
            Hold = 'Qualified attorney/court fees paid after 10/22/2004'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPWBF) != 0 or GetCurrency(IANROthAdj.SPWBF) != 0:
        if Index == count:
            Hold = 'Qualified whistleblower fees'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TP8873) != 0 or GetCurrency(IANROthAdj.SP8873) != 0:
        if Index == count:
            Hold = 'Extraterritorial Income Exclusion, federal Form 8873'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPOlympic) != 0 or GetCurrency(IANROthAdj.SPOlympic) != 0:
        if Index == count:
            Hold = 'Nontaxable amount of Olympic and Paralympic medals and USOC prize money'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPEducator) != 0 or GetCurrency(IANROthAdj.SPEducator) != 0:
        if Index == count:
            Hold = 'Educator expenses'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPTuition) != 0 or GetCurrency(IANROthAdj.SPTuition) != 0:
        if Index == count:
            Hold = 'Tuition and fees deduction'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPElectric) != 0 or GetCurrency(IANROthAdj.SPElectric) != 0:
        if Index == count:
            Hold = 'Nonresident Electric Utility Reciprocity'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPRapid) != 0 or GetCurrency(IANROthAdj.SPRapid) != 0:
        if Index == count:
            Hold = 'Rapid Response to State Disasters'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPIAABLE) != 0 or GetCurrency(IANROthAdj.SPIAABLE) != 0:
        if Index == count:
            Hold = 'Iowa ABLE savings plan trust'
            count = 99
        else:
            count = count + 1
    ReturnVal = Hold

def Names_Calculation():
    ReturnVal = GetString(IARequired.CombNames)

def PrintMe_Calculation():
    if GetCurrency(IANROthAdj.TPTot) != 0 or GetCurrency(IANROthAdj.SPTot) != 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def SPAmount_Calculation(Index):
    count = Integer()

    Hold = Currency()
    count = 0
    Hold = 0
    if GetCurrency(IANROthAdj.TOth1) != 0 or GetCurrency(IANROthAdj.SOth1) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SOth1)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPActiveMil) != 0 or GetCurrency(IANROthAdj.SPActiveMil) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPActiveMil)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPAltMV) != 0 or GetCurrency(IANROthAdj.SPAltMV) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPAltMV)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPInvolConv) != 0 or GetCurrency(IANROthAdj.SPInvolConv) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPInvolConv)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPClaimOfRight) != 0 or GetCurrency(IANROthAdj.SPClaimOfRight) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPClaimOfRight)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPIAEd) != 0 or GetCurrency(IANROthAdj.SPIAEd) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPIAEd)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPIADis) != 0 or GetCurrency(IANROthAdj.SPIADis) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPIADis)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPDomProd) != 0 or GetCurrency(IANROthAdj.SPDomProd) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPDomProd)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPFirstHmBuy) != 0 or GetCurrency(IANROthAdj.SPFirstHmBuy) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPFirstHmBuy)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPEmployerSS) != 0 or GetCurrency(IANROthAdj.SPEmployerSS) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPEmployerSS)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPFedFuels) != 0 or GetCurrency(IANROthAdj.SPFedFuels) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPFedFuels)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPForeign) != 0 or GetCurrency(IANROthAdj.SPForeign) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPForeign)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TP2555) != 0 or GetCurrency(IANROthAdj.SP2555) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SP2555)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPDistressed) != 0 or GetCurrency(IANROthAdj.SPDistressed) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPDistressed)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPHealthSav) != 0 or GetCurrency(IANROthAdj.SPHealthSav) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPHealthSav)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPVet) != 0 or GetCurrency(IANROthAdj.SPVet) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPVet)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPVetGrant) != 0 or GetCurrency(IANROthAdj.SPVetGrant) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPVetGrant)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPHomeHealth) != 0 or GetCurrency(IANROthAdj.SPHomeHealth) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPHomeHealth)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPIAVetTrust) != 0 or GetCurrency(IANROthAdj.SPIAVetTrust) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPIAVetTrust)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPMilitaryExem) != 0 or GetCurrency(IANROthAdj.SPMilitaryExem) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPMilitaryExem)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TIANOL) != 0 or GetCurrency(IANROthAdj.SIANOL) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SIANOL)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPOrgan) != 0 or GetCurrency(IANROthAdj.SPOrgan) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPOrgan)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPK1) != 0 or GetCurrency(IANROthAdj.SPK1) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPK1)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPSegal) != 0 or GetCurrency(IANROthAdj.SPSegal) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPSegal)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPShell) != 0 or GetCurrency(IANROthAdj.SPShell) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPShell)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TStud) != 0 or GetCurrency(IANROthAdj.SStud) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SStud)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPVictim) != 0 or GetCurrency(IANROthAdj.SPVictim) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPVictim)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPWages) != 0 or GetCurrency(IANROthAdj.SPWages) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPWages)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPWorkCr) != 0 or GetCurrency(IANROthAdj.SPWorkCr) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPWorkCr)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TP2106) != 0 or GetCurrency(IANROthAdj.SP2106) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SP2106)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TMSA) != 0 or GetCurrency(IANROthAdj.SMSA) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SMSA)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPJury) != 0 or GetCurrency(IANROthAdj.SPJury) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPJury)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPRFST) != 0 or GetCurrency(IANROthAdj.SPRFST) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPRFST)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPSub) != 0 or GetCurrency(IANROthAdj.SPSub) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPSub)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TP501c) != 0 or GetCurrency(IANROthAdj.SP501c) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SP501c)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPPerRent) != 0 or GetCurrency(IANROthAdj.SPPerRent) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPPerRent)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TP403b) != 0 or GetCurrency(IANROthAdj.SP403b) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SP403b)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPUDC) != 0 or GetCurrency(IANROthAdj.SPUDC) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPUDC)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPWBF) != 0 or GetCurrency(IANROthAdj.SPWBF) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPWBF)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TP8873) != 0 or GetCurrency(IANROthAdj.SP8873) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SP8873)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPOlympic) != 0 or GetCurrency(IANROthAdj.SPOlympic) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPOlympic)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPEducator) != 0 or GetCurrency(IANROthAdj.SPEducator) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPEducator)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPTuition) != 0 or GetCurrency(IANROthAdj.SPTuition) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPTuition)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPElectric) != 0 or GetCurrency(IANROthAdj.SPElectric) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPElectric)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPRapid) != 0 or GetCurrency(IANROthAdj.SPRapid) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPRapid)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPIAABLE) != 0 or GetCurrency(IANROthAdj.SPIAABLE) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.SPIAABLE)
            count = 99
        else:
            count = count + 1
    ReturnVal = Hold

def SPName_Calculation():
    ReturnVal = GetString(USWBasicInfo.SPCommon)

def SPTot_Calculation():
    if GetBool(IARequired.AskSpouse) == True and GetBool(IAF126.SpRes) == False:
        ReturnVal = GetCurrency(IANROthAdj.SOth1) + GetCurrency(IANROthAdj.SPActiveMil) + GetCurrency(IANROthAdj.SPAltMV) + GetCurrency(IANROthAdj.SPInvolConv) + GetCurrency(IANROthAdj.SPClaimOfRight) + GetCurrency(IANROthAdj.SPIAEd) + GetCurrency(IANROthAdj.SPIADis) + GetCurrency(IANROthAdj.SPDomProd) + GetCurrency(IANROthAdj.SPFirstHmBuy) + GetCurrency(IANROthAdj.SPEmployerSS) + GetCurrency(IANROthAdj.SPFedFuels) + GetCurrency(IANROthAdj.SPForeign) + GetCurrency(IANROthAdj.SP2555) + GetCurrency(IANROthAdj.SPDistressed) + GetCurrency(IANROthAdj.SPHealthSav) + GetCurrency(IANROthAdj.SPVet) + GetCurrency(IANROthAdj.SPVetGrant) + GetCurrency(IANROthAdj.SPHomeHealth) + GetCurrency(IANROthAdj.SPIAVetTrust) + GetCurrency(IANROthAdj.SPMilitaryExem) + GetCurrency(IANROthAdj.SIANOL) + GetCurrency(IANROthAdj.SPOrgan) + GetCurrency(IANROthAdj.SPK1) + GetCurrency(IANROthAdj.SPSegal) + GetCurrency(IANROthAdj.SPShell) + GetCurrency(IANROthAdj.SStud) + GetCurrency(IANROthAdj.SPVictim) + GetCurrency(IANROthAdj.SPWages) + GetCurrency(IANROthAdj.SPWorkCr) + GetCurrency(IANROthAdj.SP2106) + GetCurrency(IANROthAdj.SMSA) + GetCurrency(IANROthAdj.SPJury) + GetCurrency(IANROthAdj.SPRFST) + GetCurrency(IANROthAdj.SPSub) + GetCurrency(IANROthAdj.SP501c) + GetCurrency(IANROthAdj.SPPerRent) + GetCurrency(IANROthAdj.SP403b) + GetCurrency(IANROthAdj.SPUDC) + GetCurrency(IANROthAdj.SPWBF) + GetCurrency(IANROthAdj.SP8873) + GetCurrency(IANROthAdj.SPOlympic) + GetCurrency(IANROthAdj.SPEducator) + GetCurrency(IANROthAdj.SPTuition) + GetCurrency(IANROthAdj.SPElectric) + GetCurrency(IANROthAdj.SPRapid) + GetCurrency(IANROthAdj.SPIAABLE)
    else:
        ReturnVal = 0

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

def TPAmount_Calculation(Index):
    count = Integer()

    Hold = Currency()
    count = 0
    Hold = 0
    if GetCurrency(IANROthAdj.TOth1) != 0 or GetCurrency(IANROthAdj.SOth1) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TOth1)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPActiveMil) != 0 or GetCurrency(IANROthAdj.SPActiveMil) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPActiveMil)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPAltMV) != 0 or GetCurrency(IANROthAdj.SPAltMV) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPAltMV)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPInvolConv) != 0 or GetCurrency(IANROthAdj.SPInvolConv) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPInvolConv)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPClaimOfRight) != 0 or GetCurrency(IANROthAdj.SPClaimOfRight) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPClaimOfRight)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPIAEd) != 0 or GetCurrency(IANROthAdj.SPIAEd) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPIAEd)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPIADis) != 0 or GetCurrency(IANROthAdj.SPIADis) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPIADis)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPDomProd) != 0 or GetCurrency(IANROthAdj.SPDomProd) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPDomProd)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPFirstHmBuy) != 0 or GetCurrency(IANROthAdj.SPFirstHmBuy) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPFirstHmBuy)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPEmployerSS) != 0 or GetCurrency(IANROthAdj.SPEmployerSS) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPEmployerSS)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPFedFuels) != 0 or GetCurrency(IANROthAdj.SPFedFuels) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPFedFuels)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPForeign) != 0 or GetCurrency(IANROthAdj.SPForeign) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPForeign)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TP2555) != 0 or GetCurrency(IANROthAdj.SP2555) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TP2555)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPDistressed) != 0 or GetCurrency(IANROthAdj.SPDistressed) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPDistressed)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPHealthSav) != 0 or GetCurrency(IANROthAdj.SPHealthSav) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPHealthSav)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPVet) != 0 or GetCurrency(IANROthAdj.SPVet) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPVet)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPVetGrant) != 0 or GetCurrency(IANROthAdj.SPVetGrant) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPVetGrant)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPHomeHealth) != 0 or GetCurrency(IANROthAdj.SPHomeHealth) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPHomeHealth)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPIAVetTrust) != 0 or GetCurrency(IANROthAdj.SPIAVetTrust) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPIAVetTrust)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPMilitaryExem) != 0 or GetCurrency(IANROthAdj.SPMilitaryExem) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPMilitaryExem)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TIANOL) != 0 or GetCurrency(IANROthAdj.SIANOL) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TIANOL)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPOrgan) != 0 or GetCurrency(IANROthAdj.SPOrgan) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPOrgan)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPK1) != 0 or GetCurrency(IANROthAdj.SPK1) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPK1)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPSegal) != 0 or GetCurrency(IANROthAdj.SPSegal) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPSegal)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPShell) != 0 or GetCurrency(IANROthAdj.SPShell) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPShell)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TStud) != 0 or GetCurrency(IANROthAdj.SStud) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TStud)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPVictim) != 0 or GetCurrency(IANROthAdj.SPVictim) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPVictim)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPWages) != 0 or GetCurrency(IANROthAdj.SPWages) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPWages)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPWorkCr) != 0 or GetCurrency(IANROthAdj.SPWorkCr) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPWorkCr)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TP2106) != 0 or GetCurrency(IANROthAdj.SP2106) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TP2106)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TMSA) != 0 or GetCurrency(IANROthAdj.SMSA) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TMSA)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPJury) != 0 or GetCurrency(IANROthAdj.SPJury) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPJury)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPRFST) != 0 or GetCurrency(IANROthAdj.SPRFST) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPRFST)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPSub) != 0 or GetCurrency(IANROthAdj.SPSub) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPSub)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TP501c) != 0 or GetCurrency(IANROthAdj.SP501c) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TP501c)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPPerRent) != 0 or GetCurrency(IANROthAdj.SPPerRent) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPPerRent)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TP403b) != 0 or GetCurrency(IANROthAdj.SP403b) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TP403b)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPUDC) != 0 or GetCurrency(IANROthAdj.SPUDC) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPUDC)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPWBF) != 0 or GetCurrency(IANROthAdj.SPWBF) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPWBF)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TP8873) != 0 or GetCurrency(IANROthAdj.SP8873) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TP8873)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPOlympic) != 0 or GetCurrency(IANROthAdj.SPOlympic) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPOlympic)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPEducator) != 0 or GetCurrency(IANROthAdj.SPEducator) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPEducator)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPTuition) != 0 or GetCurrency(IANROthAdj.SPTuition) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPTuition)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPElectric) != 0 or GetCurrency(IANROthAdj.SPElectric) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPElectric)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPRapid) != 0 or GetCurrency(IANROthAdj.SPRapid) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPRapid)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IANROthAdj.TPIAABLE) != 0 or GetCurrency(IANROthAdj.SPIAABLE) != 0:
        if Index == count:
            Hold = GetCurrency(IANROthAdj.TPIAABLE)
            count = 99
        else:
            count = count + 1
    ReturnVal = Hold

def TPJointAmount_Calculation(Index):
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetCurrency(IANROthAdj.TPAmount(Index))
    else:
        ReturnVal = GetCurrency(IANROthAdj.TPAmount(Index)) + GetCurrency(IANROthAdj.SPAmount(Index))

def TPName_Calculation():
    ReturnVal = GetString(USWBasicInfo.TPCommon)

def TPTot_Calculation():
    if GetBool(IAF126.TpPYRes) == True or GetBool(IAF126.TpNonRes) == True:
        ReturnVal = GetCurrency(IANROthAdj.TOth1) + GetCurrency(IANROthAdj.TPActiveMil) + GetCurrency(IANROthAdj.TPAltMV) + GetCurrency(IANROthAdj.TPInvolConv) + GetCurrency(IANROthAdj.TPClaimOfRight) + GetCurrency(IANROthAdj.TPIAEd) + GetCurrency(IANROthAdj.TPIADis) + GetCurrency(IANROthAdj.TPDomProd) + GetCurrency(IANROthAdj.TPFirstHmBuy) + GetCurrency(IANROthAdj.TPEmployerSS) + GetCurrency(IANROthAdj.TPFedFuels) + GetCurrency(IANROthAdj.TPForeign) + GetCurrency(IANROthAdj.TP2555) + GetCurrency(IANROthAdj.TPDistressed) + GetCurrency(IANROthAdj.TPHealthSav) + GetCurrency(IANROthAdj.TPVet) + GetCurrency(IANROthAdj.TPVetGrant) + GetCurrency(IANROthAdj.TPHomeHealth) + GetCurrency(IANROthAdj.TPIAVetTrust) + GetCurrency(IANROthAdj.TPMilitaryExem) + GetCurrency(IANROthAdj.TIANOL) + GetCurrency(IANROthAdj.TPOrgan) + GetCurrency(IANROthAdj.TPK1) + GetCurrency(IANROthAdj.TPSegal) + GetCurrency(IANROthAdj.TPShell) + GetCurrency(IANROthAdj.TStud) + GetCurrency(IANROthAdj.TPVictim) + GetCurrency(IANROthAdj.TPWages) + GetCurrency(IANROthAdj.TPWorkCr) + GetCurrency(IANROthAdj.TP2106) + GetCurrency(IANROthAdj.TMSA) + GetCurrency(IANROthAdj.TPJury) + GetCurrency(IANROthAdj.TPRFST) + GetCurrency(IANROthAdj.TPSub) + GetCurrency(IANROthAdj.TP501c) + GetCurrency(IANROthAdj.TPPerRent) + GetCurrency(IANROthAdj.TP403b) + GetCurrency(IANROthAdj.TPUDC) + GetCurrency(IANROthAdj.TPWBF) + GetCurrency(IANROthAdj.TP8873) + GetCurrency(IANROthAdj.TPOlympic) + GetCurrency(IANROthAdj.TPEducator) + GetCurrency(IANROthAdj.TPTuition) + GetCurrency(IANROthAdj.TPElectric) + GetCurrency(IANROthAdj.TPRapid) + GetCurrency(IANROthAdj.TPIAABLE)
    else:
        ReturnVal = 0

def TxtOth1_Calculation():
    ReturnVal = GetString(IAOthAdj.TxtOth1)

