from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def ANet_Calculation():
    ATotAdj = Currency()
    ATotAdj = GetCurrency(IAF1040.AKeogh) + GetCurrency(IAF1040.ABusIncL) + GetCurrency(IAF1040.AHealth) + GetCurrency(IAF1040.APenalty) + GetCurrency(IAF1040.AAlimonyP) + GetCurrency(IAF1040.APenExcl) + GetCurrency(IAF1040.AMove) + GetCurrency(IAF1040.AGainDed) + GetCurrency(IAOthAdj.ModTPTot)
    ReturnVal = GetCurrency(IAF1040.AGross) - ATotAdj

def BNet_Calculation():
    BTotAdj = Currency()
    BTotAdj = GetCurrency(IAF1040.BKeogh) + GetCurrency(IAF1040.BBusIncL) + GetCurrency(IAF1040.BHealth) + GetCurrency(IAF1040.BPenalty) + GetCurrency(IAF1040.BAlimonyP) + GetCurrency(IAF1040.BPenExcl) + GetCurrency(IAF1040.BMove) + GetCurrency(IAF1040.BGainDed) + GetCurrency(IAOthAdj.ModSPTot)
    ReturnVal = GetCurrency(IAF1040.BGross) - BTotAdj

def BProRate_Calculation():
    if IAFS() == 3:
        if GetCurrency(IAOthAdj.BNet) < 0 and GetCurrency(IAOthAdj.ANet) < 0:
            if GetCurrency(IAOthAdj.BNet) < GetCurrency(IAOthAdj.ANet):
                ReturnVal = 0
            else:
                ReturnVal = 1
        elif GetCurrency(IAOthAdj.BNet) < 0:
            ReturnVal = 0
        elif GetCurrency(IAOthAdj.BNet) > 0 and GetCurrency(IAOthAdj.TotNI) <= 0:
            ReturnVal = 1
        elif GetCurrency(IAOthAdj.TotNI) == 0:
            ReturnVal = 0
        else:
            ReturnVal = MaxValue(0, ( MinValue(1, GetFloat(IAOthAdj.BNet) / GetFloat(IAOthAdj.TotNI)) ))
    else:
        ReturnVal = 0

def Code_Calculation(Index):
    count = Integer()

    Hold = String()
    count = 0
    Hold = ''
    if GetCurrency(IAOthAdj.TOth1) != 0 or GetCurrency(IAOthAdj.SOth1) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPActiveMil) != 0 or GetCurrency(IAOthAdj.SPActiveMil) != 0:
        if Index == count:
            Hold = 'b'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPAltMV) != 0 or GetCurrency(IAOthAdj.SPAltMV) != 0:
        if Index == count:
            Hold = 'c'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPInvolConv) != 0 or GetCurrency(IAOthAdj.SPInvolConv) != 0:
        if Index == count:
            Hold = 'e'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPClaimOfRight) != 0 or GetCurrency(IAOthAdj.SPClaimOfRight) != 0:
        if Index == count:
            Hold = 'f'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPIAEd) != 0 or GetCurrency(IAOthAdj.SPIAEd) != 0:
        if Index == count:
            Hold = 'g'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPIADis) != 0 or GetCurrency(IAOthAdj.SPIADis) != 0:
        if Index == count:
            Hold = 'h'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPDomProd) != 0 or GetCurrency(IAOthAdj.SPDomProd) != 0:
        if Index == count:
            Hold = 'i'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPFirstHmBuy) != 0 or GetCurrency(IAOthAdj.SPFirstHmBuy) != 0:
        if Index == count:
            Hold = 'j'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPEmployerSS) != 0 or GetCurrency(IAOthAdj.SPEmployerSS) != 0:
        if Index == count:
            Hold = 'k'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPFedFuels) != 0 or GetCurrency(IAOthAdj.SPFedFuels) != 0:
        if Index == count:
            Hold = 'l'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPForeign) != 0 or GetCurrency(IAOthAdj.SPForeign) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TP2555) != 0 or GetCurrency(IAOthAdj.SP2555) != 0:
        if Index == count:
            Hold = 'm'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPDistressed) != 0 or GetCurrency(IAOthAdj.SPDistressed) != 0:
        if Index == count:
            Hold = 'n'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPHealthSav) != 0 or GetCurrency(IAOthAdj.SPHealthSav) != 0:
        if Index == count:
            Hold = 'o'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPVet) != 0 or GetCurrency(IAOthAdj.SPVet) != 0:
        if Index == count:
            Hold = 'p'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPVetGrant) != 0 or GetCurrency(IAOthAdj.SPVetGrant) != 0:
        if Index == count:
            Hold = 'q'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPHomeHealth) != 0 or GetCurrency(IAOthAdj.SPHomeHealth) != 0:
        if Index == count:
            Hold = 'r'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPIAVetTrust) != 0 or GetCurrency(IAOthAdj.SPIAVetTrust) != 0:
        if Index == count:
            Hold = 's'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPMilitaryExem) != 0 or GetCurrency(IAOthAdj.SPMilitaryExem) != 0:
        if Index == count:
            Hold = 't'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TIANOL) != 0 or GetCurrency(IAOthAdj.SIANOL) != 0:
        if Index == count:
            Hold = 'u'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPOrgan) != 0 or GetCurrency(IAOthAdj.SPOrgan) != 0:
        if Index == count:
            Hold = 'v'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPK1) != 0 or GetCurrency(IAOthAdj.SPK1) != 0:
        if Index == count:
            Hold = 'w'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPSegal) != 0 or GetCurrency(IAOthAdj.SPSegal) != 0:
        if Index == count:
            Hold = 'x'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPShell) != 0 or GetCurrency(IAOthAdj.SPShell) != 0:
        if Index == count:
            Hold = 'y'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TStud) != 0 or GetCurrency(IAOthAdj.SStud) != 0:
        if Index == count:
            Hold = 'z'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPVictim) != 0 or GetCurrency(IAOthAdj.SPVictim) != 0:
        if Index == count:
            Hold = 'aa'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPWages) != 0 or GetCurrency(IAOthAdj.SPWages) != 0:
        if Index == count:
            Hold = 'bb'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPWorkCr) != 0 or GetCurrency(IAOthAdj.SPWorkCr) != 0:
        if Index == count:
            Hold = 'cc'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TP2106) != 0 or GetCurrency(IAOthAdj.SP2106) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TMSA) != 0 or GetCurrency(IAOthAdj.SMSA) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPJury) != 0 or GetCurrency(IAOthAdj.SPJury) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPRFST) != 0 or GetCurrency(IAOthAdj.SPRFST) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPSub) != 0 or GetCurrency(IAOthAdj.SPSub) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TP501c) != 0 or GetCurrency(IAOthAdj.SP501c) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPPerRent) != 0 or GetCurrency(IAOthAdj.SPPerRent) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TP403b) != 0 or GetCurrency(IAOthAdj.SP403b) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPUDC) != 0 or GetCurrency(IAOthAdj.SPUDC) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPWBF) != 0 or GetCurrency(IAOthAdj.SPWBF) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TP8873) != 0 or GetCurrency(IAOthAdj.SP8873) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPOlympic) != 0 or GetCurrency(IAOthAdj.SPOlympic) != 0:
        if Index == count:
            Hold = 'dd'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPEducator) != 0 or GetCurrency(IAOthAdj.SPEducator) != 0:
        if Index == count:
            Hold = 'ee'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPTuition) != 0 or GetCurrency(IAOthAdj.SPTuition) != 0:
        if Index == count:
            Hold = 'ff'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPElectric) != 0 or GetCurrency(IAOthAdj.SPElectric) != 0:
        if Index == count:
            Hold = 'gg'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPRapid) != 0 or GetCurrency(IAOthAdj.SPRapid) != 0:
        if Index == count:
            Hold = 'hh'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPIAABLE) != 0 or GetCurrency(IAOthAdj.SPIAABLE) != 0:
        if Index == count:
            Hold = 'ii'
            count = 99
        else:
            count = count + 1
    ReturnVal = Hold

def Desc_Calculation():
    Total = Currency()
    Total = GetCurrency(IAOthAdj.TPTot) + GetCurrency(IAOthAdj.SPTot)
    ReturnVal = CStr(Total)

def Description_Calculation(Index):
    count = Integer()

    Hold = String()
    count = 0
    Hold = ''
    if GetCurrency(IAOthAdj.TOth1) != 0 or GetCurrency(IAOthAdj.SOth1) != 0:
        if Index == count:
            Hold = GetString(IAOthAdj.TxtOth1)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPActiveMil) != 0 or GetCurrency(IAOthAdj.SPActiveMil) != 0:
        if Index == count:
            Hold = 'Active duty military pay'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPAltMV) != 0 or GetCurrency(IAOthAdj.SPAltMV) != 0:
        if Index == count:
            Hold = 'Alternative motor vehicle deduction'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPInvolConv) != 0 or GetCurrency(IAOthAdj.SPInvolConv) != 0:
        if Index == count:
            Hold = 'Capital or ordinary gain from involuntary conversion'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPClaimOfRight) != 0 or GetCurrency(IAOthAdj.SPClaimOfRight) != 0:
        if Index == count:
            Hold = 'Claim of Right deduction'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPIAEd) != 0 or GetCurrency(IAOthAdj.SPIAEd) != 0:
        if Index == count:
            Hold = 'College Savings Iowa or Iowa Advisor 529 Plan'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPIADis) != 0 or GetCurrency(IAOthAdj.SPIADis) != 0:
        if Index == count:
            Hold = 'Disability income exclusion'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPDomProd) != 0 or GetCurrency(IAOthAdj.SPDomProd) != 0:
        if Index == count:
            Hold = 'Domestic production activities deduction'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPFirstHmBuy) != 0 or GetCurrency(IAOthAdj.SPFirstHmBuy) != 0:
        if Index == count:
            Hold = 'First-Time Homebuyer Savings Account qualifying contributions'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPEmployerSS) != 0 or GetCurrency(IAOthAdj.SPEmployerSS) != 0:
        if Index == count:
            Hold = 'Employer social security credit, federal Form 8846'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPFedFuels) != 0 or GetCurrency(IAOthAdj.SPFedFuels) != 0:
        if Index == count:
            Hold = 'Alcohol and cellulosic biofuel credit, federal Form 6478'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPForeign) != 0 or GetCurrency(IAOthAdj.SPForeign) != 0:
        if Index == count:
            Hold = 'Foreign earned income exclusion, federal Form 2555'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TP2555) != 0 or GetCurrency(IAOthAdj.SP2555) != 0:
        if Index == count:
            Hold = 'Foreign housing deduction, federal Form 2555'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPDistressed) != 0 or GetCurrency(IAOthAdj.SPDistressed) != 0:
        if Index == count:
            Hold = 'Gains or losses from distressed sale transactions'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPHealthSav) != 0 or GetCurrency(IAOthAdj.SPHealthSav) != 0:
        if Index == count:
            Hold = 'Health savings account deduction, federal Form 8889'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPVet) != 0 or GetCurrency(IAOthAdj.SPVet) != 0:
        if Index == count:
            Hold = 'Injured veterans programs - contributions'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPVetGrant) != 0 or GetCurrency(IAOthAdj.SPVetGrant) != 0:
        if Index == count:
            Hold = 'Injured veterans programs - grants'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPHomeHealth) != 0 or GetCurrency(IAOthAdj.SPHomeHealth) != 0:
        if Index == count:
            Hold = 'In-home health care'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPIAVetTrust) != 0 or GetCurrency(IAOthAdj.SPIAVetTrust) != 0:
        if Index == count:
            Hold = 'Iowa Veterans Trust Fund'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPMilitaryExem) != 0 or GetCurrency(IAOthAdj.SPMilitaryExem) != 0:
        if Index == count:
            Hold = 'Military exemptions'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TIANOL) != 0 or GetCurrency(IAOthAdj.SIANOL) != 0:
        if Index == count:
            Hold = 'Iowa Net Operating Loss'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPOrgan) != 0 or GetCurrency(IAOthAdj.SPOrgan) != 0:
        if Index == count:
            Hold = 'Organ transplant expenses'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPK1) != 0 or GetCurrency(IAOthAdj.SPK1) != 0:
        if Index == count:
            Hold = 'Partnership income and/or S Corporation income'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPSegal) != 0 or GetCurrency(IAOthAdj.SPSegal) != 0:
        if Index == count:
            Hold = 'Segal Americorps Education Award payments'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPShell) != 0 or GetCurrency(IAOthAdj.SPShell) != 0:
        if Index == count:
            Hold = 'Speculative shell buildings'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TStud) != 0 or GetCurrency(IAOthAdj.SStud) != 0:
        if Index == count:
            Hold = 'Student loan interest deduction'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPVictim) != 0 or GetCurrency(IAOthAdj.SPVictim) != 0:
        if Index == count:
            Hold = 'Victim compensation awards'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPWages) != 0 or GetCurrency(IAOthAdj.SPWages) != 0:
        if Index == count:
            Hold = 'Wages paid to certain individuals'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPWorkCr) != 0 or GetCurrency(IAOthAdj.SPWorkCr) != 0:
        if Index == count:
            Hold = 'Work opportunity credit, federal Form 5884'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TP2106) != 0 or GetCurrency(IAOthAdj.SP2106) != 0:
        if Index == count:
            Hold = 'Business expenses of reservists, QPA, FBO, federal Form 2106'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TMSA) != 0 or GetCurrency(IAOthAdj.SMSA) != 0:
        if Index == count:
            Hold = 'Archer MSA deduction, federal Form 8853'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPJury) != 0 or GetCurrency(IAOthAdj.SPJury) != 0:
        if Index == count:
            Hold = 'Jury pay repayment to employer'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPRFST) != 0 or GetCurrency(IAOthAdj.SPRFST) != 0:
        if Index == count:
            Hold = 'Reforestation amortization and expenses'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPSub) != 0 or GetCurrency(IAOthAdj.SPSub) != 0:
        if Index == count:
            Hold = 'Repayment of supplemental unemployment benefits'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TP501c) != 0 or GetCurrency(IAOthAdj.SP501c) != 0:
        if Index == count:
            Hold = 'Contributions to a 501(c)(18) pension plan'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPPerRent) != 0 or GetCurrency(IAOthAdj.SPPerRent) != 0:
        if Index == count:
            Hold = 'Expenses for personal property rental'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TP403b) != 0 or GetCurrency(IAOthAdj.SP403b) != 0:
        if Index == count:
            Hold = 'Contributions by certain chaplains to a 403(b) plan'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPUDC) != 0 or GetCurrency(IAOthAdj.SPUDC) != 0:
        if Index == count:
            Hold = 'Qualified attorney/court fees paid after 10/22/2004'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPWBF) != 0 or GetCurrency(IAOthAdj.SPWBF) != 0:
        if Index == count:
            Hold = 'Qualified whistleblower fees'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TP8873) != 0 or GetCurrency(IAOthAdj.SP8873) != 0:
        if Index == count:
            Hold = 'Extraterritorial Income Exclusion, federal Form 8873'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPOlympic) != 0 or GetCurrency(IAOthAdj.SPOlympic) != 0:
        if Index == count:
            Hold = 'Nontaxable amount of Olympic and Paralympic medals and USOC prize money'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPEducator) != 0 or GetCurrency(IAOthAdj.SPEducator) != 0:
        if Index == count:
            Hold = 'Educator expenses'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPTuition) != 0 or GetCurrency(IAOthAdj.SPTuition) != 0:
        if Index == count:
            Hold = 'Tuition and fees deduction'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPElectric) != 0 or GetCurrency(IAOthAdj.SPElectric) != 0:
        if Index == count:
            Hold = 'Nonresident Electric Utility Reciprocity'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPRapid) != 0 or GetCurrency(IAOthAdj.SPRapid) != 0:
        if Index == count:
            Hold = 'Rapid Response to State Disasters'
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPIAABLE) != 0 or GetCurrency(IAOthAdj.SPIAABLE) != 0:
        if Index == count:
            Hold = 'Iowa ABLE savings plan trust'
            count = 99
        else:
            count = count + 1
    ReturnVal = Hold

def Exist_Calculation():
    ReturnVal = 1

def ModSPTot_Calculation():
    ReturnVal = GetCurrency(IAOthAdj.SOth1) + GetCurrency(IAOthAdj.SPActiveMil) + GetCurrency(IAOthAdj.SPInvolConv) + GetCurrency(IAOthAdj.SPClaimOfRight) + GetCurrency(IAOthAdj.SPIAEd) + GetCurrency(IAOthAdj.SPIADis) + GetCurrency(IAOthAdj.SPDomProd) + GetCurrency(IAOthAdj.SPFirstHmBuy) + GetCurrency(IAOthAdj.SPEmployerSS) + GetCurrency(IAOthAdj.SPFedFuels) + GetCurrency(IAOthAdj.SPForeign) + GetCurrency(IAOthAdj.SP2555) + GetCurrency(IAOthAdj.SPDistressed) + GetCurrency(IAOthAdj.SPHealthSav) + GetCurrency(IAOthAdj.SPVet) + GetCurrency(IAOthAdj.SPVetGrant) + GetCurrency(IAOthAdj.SPHomeHealth) + GetCurrency(IAOthAdj.SPIAVetTrust) + GetCurrency(IAOthAdj.SPMilitaryExem) + GetCurrency(IAOthAdj.SIANOL) + GetCurrency(IAOthAdj.SPOrgan) + GetCurrency(IAOthAdj.SPK1) + GetCurrency(IAOthAdj.SPSegal) + GetCurrency(IAOthAdj.SPShell) + GetCurrency(IAOthAdj.SStud) + GetCurrency(IAOthAdj.SPVictim) + GetCurrency(IAOthAdj.SPWages) + GetCurrency(IAOthAdj.SPWorkCr) + GetCurrency(IAOthAdj.SP2106) + GetCurrency(IAOthAdj.SMSA) + GetCurrency(IAOthAdj.SPJury) + GetCurrency(IAOthAdj.SPRFST) + GetCurrency(IAOthAdj.SPSub) + GetCurrency(IAOthAdj.SP501c) + GetCurrency(IAOthAdj.SPPerRent) + GetCurrency(IAOthAdj.SP403b) + GetCurrency(IAOthAdj.SPUDC) + GetCurrency(IAOthAdj.SPWBF) + GetCurrency(IAOthAdj.SP8873) + GetCurrency(IAOthAdj.SPOlympic) + GetCurrency(IAOthAdj.SPEducator) + GetCurrency(IAOthAdj.SPTuition) + GetCurrency(IAOthAdj.SPElectric) + GetCurrency(IAOthAdj.SPRapid) + GetCurrency(IAOthAdj.SPIAABLE)

def ModTPTot_Calculation():
    ReturnVal = GetCurrency(IAOthAdj.TOth1) + GetCurrency(IAOthAdj.TPActiveMil) + GetCurrency(IAOthAdj.TPInvolConv) + GetCurrency(IAOthAdj.TPClaimOfRight) + GetCurrency(IAOthAdj.TPIAEd) + GetCurrency(IAOthAdj.TPIADis) + GetCurrency(IAOthAdj.TPDomProd) + GetCurrency(IAOthAdj.TPFirstHmBuy) + GetCurrency(IAOthAdj.TPEmployerSS) + GetCurrency(IAOthAdj.TPFedFuels) + GetCurrency(IAOthAdj.TPForeign) + GetCurrency(IAOthAdj.TP2555) + GetCurrency(IAOthAdj.TPDistressed) + GetCurrency(IAOthAdj.TPHealthSav) + GetCurrency(IAOthAdj.TPVet) + GetCurrency(IAOthAdj.TPVetGrant) + GetCurrency(IAOthAdj.TPHomeHealth) + GetCurrency(IAOthAdj.TPIAVetTrust) + GetCurrency(IAOthAdj.TPMilitaryExem) + GetCurrency(IAOthAdj.TIANOL) + GetCurrency(IAOthAdj.TPOrgan) + GetCurrency(IAOthAdj.TPK1) + GetCurrency(IAOthAdj.TPSegal) + GetCurrency(IAOthAdj.TPShell) + GetCurrency(IAOthAdj.TStud) + GetCurrency(IAOthAdj.TPVictim) + GetCurrency(IAOthAdj.TPWages) + GetCurrency(IAOthAdj.TPWorkCr) + GetCurrency(IAOthAdj.TP2106) + GetCurrency(IAOthAdj.TMSA) + GetCurrency(IAOthAdj.TPJury) + GetCurrency(IAOthAdj.TPRFST) + GetCurrency(IAOthAdj.TPSub) + GetCurrency(IAOthAdj.TP501c) + GetCurrency(IAOthAdj.TPPerRent) + GetCurrency(IAOthAdj.TP403b) + GetCurrency(IAOthAdj.TPUDC) + GetCurrency(IAOthAdj.TPWBF) + GetCurrency(IAOthAdj.TP8873) + GetCurrency(IAOthAdj.TPOlympic) + GetCurrency(IAOthAdj.TPEducator) + GetCurrency(IAOthAdj.TPTuition) + GetCurrency(IAOthAdj.TPElectric) + GetCurrency(IAOthAdj.TPRapid) + GetCurrency(IAOthAdj.TPIAABLE)

def Names_Calculation():
    ReturnVal = GetString(IARequired.CombNames)

def PrintMe_Calculation():
    if GetCurrency(IAOthAdj.TPTot) != 0 or GetCurrency(IAOthAdj.SPTot) != 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def SIANOL_Calculation():
    if GetBool(IAF126.SpNonRes) == True:
        ReturnVal = 0
    elif GetBool(USWResidency.F1040NR) == False:
        ReturnVal = Abs(GetCurrency(USWOthInc.SPNOL))
    else:
        ReturnVal = 0

def SMSA_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthAdj.SP8853)
    else:
        ReturnVal = 0

def SP2106_Calculation():
    ReturnVal = GetCurrency(USWRec.SBusExp2106)

def SP2555_Calculation():
    ReturnVal = GetCurrency(USWOthAdj.SP2555)

def SP403b_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthAdj.SP403b)
    else:
        ReturnVal = 0

def SP501c_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthAdj.SPTotal501)
    else:
        ReturnVal = 0

def SP8873_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthAdj.SP8873)
    else:
        ReturnVal = 0

def SPAltMV_Calculation():
    #2018 expanded instructions - deduction does not apply to purchases on or after 1/1/2015 due to nonconformity, federal does not ask for a purchase date, believe will be very uncommon for ability to take this credit on Iowa, remove calc and make user entered
    #If IAFS() = 3 And GetBool(USF8910.Print) = True Then
    #    ReturnVal = CDollar(GetFloat(IAOthAdj.BProRate) * 2000@)
    #Else
    ReturnVal = 0
    #End If

def SPAmount_Calculation(Index):
    count = Integer()

    Hold = Currency()
    count = 0
    Hold = 0
    if GetCurrency(IAOthAdj.TOth1) != 0 or GetCurrency(IAOthAdj.SOth1) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SOth1)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPActiveMil) != 0 or GetCurrency(IAOthAdj.SPActiveMil) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPActiveMil)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPAltMV) != 0 or GetCurrency(IAOthAdj.SPAltMV) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPAltMV)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPInvolConv) != 0 or GetCurrency(IAOthAdj.SPInvolConv) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPInvolConv)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPClaimOfRight) != 0 or GetCurrency(IAOthAdj.SPClaimOfRight) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPClaimOfRight)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPIAEd) != 0 or GetCurrency(IAOthAdj.SPIAEd) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPIAEd)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPIADis) != 0 or GetCurrency(IAOthAdj.SPIADis) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPIADis)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPDomProd) != 0 or GetCurrency(IAOthAdj.SPDomProd) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPDomProd)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPFirstHmBuy) != 0 or GetCurrency(IAOthAdj.SPFirstHmBuy) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPFirstHmBuy)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPEmployerSS) != 0 or GetCurrency(IAOthAdj.SPEmployerSS) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPEmployerSS)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPFedFuels) != 0 or GetCurrency(IAOthAdj.SPFedFuels) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPFedFuels)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPForeign) != 0 or GetCurrency(IAOthAdj.SPForeign) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPForeign)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TP2555) != 0 or GetCurrency(IAOthAdj.SP2555) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SP2555)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPDistressed) != 0 or GetCurrency(IAOthAdj.SPDistressed) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPDistressed)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPHealthSav) != 0 or GetCurrency(IAOthAdj.SPHealthSav) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPHealthSav)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPVet) != 0 or GetCurrency(IAOthAdj.SPVet) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPVet)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPVetGrant) != 0 or GetCurrency(IAOthAdj.SPVetGrant) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPVetGrant)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPHomeHealth) != 0 or GetCurrency(IAOthAdj.SPHomeHealth) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPHomeHealth)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPIAVetTrust) != 0 or GetCurrency(IAOthAdj.SPIAVetTrust) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPIAVetTrust)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPMilitaryExem) != 0 or GetCurrency(IAOthAdj.SPMilitaryExem) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPMilitaryExem)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TIANOL) != 0 or GetCurrency(IAOthAdj.SIANOL) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SIANOL)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPOrgan) != 0 or GetCurrency(IAOthAdj.SPOrgan) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPOrgan)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPK1) != 0 or GetCurrency(IAOthAdj.SPK1) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPK1)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPSegal) != 0 or GetCurrency(IAOthAdj.SPSegal) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPSegal)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPShell) != 0 or GetCurrency(IAOthAdj.SPShell) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPShell)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TStud) != 0 or GetCurrency(IAOthAdj.SStud) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SStud)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPVictim) != 0 or GetCurrency(IAOthAdj.SPVictim) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPVictim)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPWages) != 0 or GetCurrency(IAOthAdj.SPWages) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPWages)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPWorkCr) != 0 or GetCurrency(IAOthAdj.SPWorkCr) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPWorkCr)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TP2106) != 0 or GetCurrency(IAOthAdj.SP2106) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SP2106)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TMSA) != 0 or GetCurrency(IAOthAdj.SMSA) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SMSA)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPJury) != 0 or GetCurrency(IAOthAdj.SPJury) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPJury)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPRFST) != 0 or GetCurrency(IAOthAdj.SPRFST) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPRFST)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPSub) != 0 or GetCurrency(IAOthAdj.SPSub) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPSub)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TP501c) != 0 or GetCurrency(IAOthAdj.SP501c) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SP501c)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPPerRent) != 0 or GetCurrency(IAOthAdj.SPPerRent) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPPerRent)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TP403b) != 0 or GetCurrency(IAOthAdj.SP403b) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SP403b)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPUDC) != 0 or GetCurrency(IAOthAdj.SPUDC) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPUDC)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPWBF) != 0 or GetCurrency(IAOthAdj.SPWBF) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPWBF)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TP8873) != 0 or GetCurrency(IAOthAdj.SP8873) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SP8873)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPOlympic) != 0 or GetCurrency(IAOthAdj.SPOlympic) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPOlympic)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPEducator) != 0 or GetCurrency(IAOthAdj.SPEducator) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPEducator)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPTuition) != 0 or GetCurrency(IAOthAdj.SPTuition) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPTuition)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPElectric) != 0 or GetCurrency(IAOthAdj.SPElectric) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPElectric)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPRapid) != 0 or GetCurrency(IAOthAdj.SPRapid) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPRapid)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPIAABLE) != 0 or GetCurrency(IAOthAdj.SPIAABLE) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.SPIAABLE)
            count = 99
        else:
            count = count + 1
    ReturnVal = Hold

def SPDomProd_Calculation():
    #Iowa expanded instructions - Iowa has not conformed to the repeal of the federal domestic production activities deduction. For Iowa will need to complete a federal 8903 and keep with their records and follow IA instructions for adjustments needed when calcing.
    #ReturnVal = GetCurrency(USWRec.SDomProd)
    ReturnVal = 0

def SPEducator_Calculation():
    ReturnVal = GetCurrency(USWRec.SEdExp)

def SPForeign_Calculation():
    ReturnVal = Abs(GetCurrency(USWOthInc.SP2555))

def SPHealthSav_Calculation():
    ReturnVal = GetCurrency(USWRec.SHealthSav)

def SPJury_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthAdj.SPJury)
    else:
        ReturnVal = 0

def SPK1_Calculation():
    if GetBool(USWResidency.F1040NR) == False and GetCurrency(USWOthInc.SPK1) < 0:
        ReturnVal = Abs(GetCurrency(USWOthInc.SPK1))
    else:
        ReturnVal = 0

def SPName_Calculation():
    ReturnVal = GetString(USWBasicInfo.SPCommon)

def SPOlympic_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthAdj.Text2)
    else:
        ReturnVal = 0

def SPPerRent_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthAdj.SPPerRent)
    else:
        ReturnVal = 0

def SPRFST_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthAdj.SPRFST)
    else:
        ReturnVal = 0

def SPSub_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthAdj.SPSub)
    else:
        ReturnVal = 0

def SPTot_Calculation():
    ReturnVal = GetCurrency(IAOthAdj.SOth1) + GetCurrency(IAOthAdj.SPActiveMil) + GetCurrency(IAOthAdj.SPAltMV) + GetCurrency(IAOthAdj.SPInvolConv) + GetCurrency(IAOthAdj.SPClaimOfRight) + GetCurrency(IAOthAdj.SPIAEd) + GetCurrency(IAOthAdj.SPIADis) + GetCurrency(IAOthAdj.SPDomProd) + GetCurrency(IAOthAdj.SPFirstHmBuy) + GetCurrency(IAOthAdj.SPEmployerSS) + GetCurrency(IAOthAdj.SPFedFuels) + GetCurrency(IAOthAdj.SPForeign) + GetCurrency(IAOthAdj.SP2555) + GetCurrency(IAOthAdj.SPDistressed) + GetCurrency(IAOthAdj.SPHealthSav) + GetCurrency(IAOthAdj.SPVet) + GetCurrency(IAOthAdj.SPVetGrant) + GetCurrency(IAOthAdj.SPHomeHealth) + GetCurrency(IAOthAdj.SPIAVetTrust) + GetCurrency(IAOthAdj.SPMilitaryExem) + GetCurrency(IAOthAdj.SIANOL) + GetCurrency(IAOthAdj.SPOrgan) + GetCurrency(IAOthAdj.SPK1) + GetCurrency(IAOthAdj.SPSegal) + GetCurrency(IAOthAdj.SPShell) + GetCurrency(IAOthAdj.SStud) + GetCurrency(IAOthAdj.SPVictim) + GetCurrency(IAOthAdj.SPWages) + GetCurrency(IAOthAdj.SPWorkCr) + GetCurrency(IAOthAdj.SP2106) + GetCurrency(IAOthAdj.SMSA) + GetCurrency(IAOthAdj.SPJury) + GetCurrency(IAOthAdj.SPRFST) + GetCurrency(IAOthAdj.SPSub) + GetCurrency(IAOthAdj.SP501c) + GetCurrency(IAOthAdj.SPPerRent) + GetCurrency(IAOthAdj.SP403b) + GetCurrency(IAOthAdj.SPUDC) + GetCurrency(IAOthAdj.SPWBF) + GetCurrency(IAOthAdj.SP8873) + GetCurrency(IAOthAdj.SPEducator) + GetCurrency(IAOthAdj.SPTuition) + GetCurrency(IAOthAdj.SPElectric) + GetCurrency(IAOthAdj.SPRapid) + GetCurrency(IAOthAdj.SPOlympic) + GetCurrency(IAOthAdj.SPIAABLE)

def SPTuition_Calculation():
    ReturnVal = 0
    #ReturnVal = GetCurrency(USWRec.STuitAdj)

def SPUDC_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthAdj.SPUDC)
    else:
        ReturnVal = 0

def SPWBF_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthAdj.SPWBF)
    else:
        ReturnVal = 0

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

def SStud_Calculation():
    ReturnVal = GetCurrency(USWRec.SStudAdj)

def TIANOL_Calculation():
    if GetBool(IAF126.TpNonRes) == True:
        ReturnVal = 0
    elif GetBool(USWResidency.F1040NR) == False:
        ReturnVal = Abs(GetCurrency(USWOthInc.TPNOL))
    else:
        ReturnVal = Abs(GetCurrency(USWOthIncNR.TPNOL))

def TMSA_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthAdj.TP8853)
    else:
        ReturnVal = GetCurrency(USWOthAdjNR.TP8853)

def TotNI_Calculation():
    ReturnVal = GetCurrency(IAOthAdj.ANet) + GetCurrency(IAOthAdj.BNet)

def TP2106_Calculation():
    ReturnVal = GetCurrency(USWRec.TBusExp2106)

def TP2555_Calculation():
    ReturnVal = GetCurrency(USWOthAdj.TP2555)

def TP403b_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthAdj.TP403b)
    else:
        ReturnVal = GetCurrency(USWOthAdjNR.TP403b)

def TP501c_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthAdj.TPTotal501)
    else:
        ReturnVal = GetCurrency(USWOthAdjNR.Total501)

def TP8873_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthAdj.TP8873)
    else:
        ReturnVal = GetCurrency(USWOthAdjNR.TP8873)

def TPAltMV_Calculation():
    #2018 expanded instructions - deduction does not apply to purchases on or after 1/1/2015 due to nonconformity, federal does not ask for a purchase date, believe will be very uncommon for ability to take this credit on Iowa, remove calc and make user entered
    #If GetBool(USF8910.Print) = False Then
    ReturnVal = 0
    #ElseIf IAFS() = 3 Then
    #    ReturnVal = MaxValue(0, 2000@ - GetCurrency(IAOthAdj.SPAltMV))
    #Else
    #    ReturnVal = 2000@
    #End If

def TPAmount_Calculation(Index):
    count = Integer()

    Hold = Currency()
    count = 0
    Hold = 0
    if GetCurrency(IAOthAdj.TOth1) != 0 or GetCurrency(IAOthAdj.SOth1) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TOth1)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPActiveMil) != 0 or GetCurrency(IAOthAdj.SPActiveMil) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPActiveMil)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPAltMV) != 0 or GetCurrency(IAOthAdj.SPAltMV) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPAltMV)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPInvolConv) != 0 or GetCurrency(IAOthAdj.SPInvolConv) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPInvolConv)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPClaimOfRight) != 0 or GetCurrency(IAOthAdj.SPClaimOfRight) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPClaimOfRight)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPIAEd) != 0 or GetCurrency(IAOthAdj.SPIAEd) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPIAEd)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPIADis) != 0 or GetCurrency(IAOthAdj.SPIADis) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPIADis)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPDomProd) != 0 or GetCurrency(IAOthAdj.SPDomProd) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPDomProd)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPFirstHmBuy) != 0 or GetCurrency(IAOthAdj.SPFirstHmBuy) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPFirstHmBuy)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPEmployerSS) != 0 or GetCurrency(IAOthAdj.SPEmployerSS) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPEmployerSS)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPFedFuels) != 0 or GetCurrency(IAOthAdj.SPFedFuels) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPFedFuels)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPForeign) != 0 or GetCurrency(IAOthAdj.SPForeign) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPForeign)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TP2555) != 0 or GetCurrency(IAOthAdj.SP2555) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TP2555)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPDistressed) != 0 or GetCurrency(IAOthAdj.SPDistressed) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPDistressed)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPHealthSav) != 0 or GetCurrency(IAOthAdj.SPHealthSav) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPHealthSav)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPVet) != 0 or GetCurrency(IAOthAdj.SPVet) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPVet)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPVetGrant) != 0 or GetCurrency(IAOthAdj.SPVetGrant) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPVetGrant)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPHomeHealth) != 0 or GetCurrency(IAOthAdj.SPHomeHealth) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPHomeHealth)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPIAVetTrust) != 0 or GetCurrency(IAOthAdj.SPIAVetTrust) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPIAVetTrust)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPMilitaryExem) != 0 or GetCurrency(IAOthAdj.SPMilitaryExem) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPMilitaryExem)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TIANOL) != 0 or GetCurrency(IAOthAdj.SIANOL) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TIANOL)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPOrgan) != 0 or GetCurrency(IAOthAdj.SPOrgan) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPOrgan)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPK1) != 0 or GetCurrency(IAOthAdj.SPK1) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPK1)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPSegal) != 0 or GetCurrency(IAOthAdj.SPSegal) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPSegal)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPShell) != 0 or GetCurrency(IAOthAdj.SPShell) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPShell)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TStud) != 0 or GetCurrency(IAOthAdj.SStud) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TStud)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPVictim) != 0 or GetCurrency(IAOthAdj.SPVictim) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPVictim)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPWages) != 0 or GetCurrency(IAOthAdj.SPWages) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPWages)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPWorkCr) != 0 or GetCurrency(IAOthAdj.SPWorkCr) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPWorkCr)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TP2106) != 0 or GetCurrency(IAOthAdj.SP2106) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TP2106)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TMSA) != 0 or GetCurrency(IAOthAdj.SMSA) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TMSA)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPJury) != 0 or GetCurrency(IAOthAdj.SPJury) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPJury)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPRFST) != 0 or GetCurrency(IAOthAdj.SPRFST) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPRFST)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPSub) != 0 or GetCurrency(IAOthAdj.SPSub) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPSub)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TP501c) != 0 or GetCurrency(IAOthAdj.SP501c) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TP501c)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPPerRent) != 0 or GetCurrency(IAOthAdj.SPPerRent) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPPerRent)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TP403b) != 0 or GetCurrency(IAOthAdj.SP403b) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TP403b)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPUDC) != 0 or GetCurrency(IAOthAdj.SPUDC) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPUDC)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPWBF) != 0 or GetCurrency(IAOthAdj.SPWBF) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPWBF)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TP8873) != 0 or GetCurrency(IAOthAdj.SP8873) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TP8873)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPOlympic) != 0 or GetCurrency(IAOthAdj.SPOlympic) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPOlympic)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPEducator) != 0 or GetCurrency(IAOthAdj.SPEducator) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPEducator)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPTuition) != 0 or GetCurrency(IAOthAdj.SPTuition) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPTuition)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPElectric) != 0 or GetCurrency(IAOthAdj.SPElectric) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPElectric)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPRapid) != 0 or GetCurrency(IAOthAdj.SPRapid) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPRapid)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IAOthAdj.TPIAABLE) != 0 or GetCurrency(IAOthAdj.SPIAABLE) != 0:
        if Index == count:
            Hold = GetCurrency(IAOthAdj.TPIAABLE)
            count = 99
        else:
            count = count + 1
    ReturnVal = Hold

def TPDomProd_Calculation():
    #Iowa expanded instructions - Iowa has not conformed to the repeal of the federal domestic production activities deduction. For Iowa will need to complete a federal 8903 and keep with their records and follow IA instructions for adjustments needed when calcing.
    #ReturnVal = GetCurrency(USWRec.TDomProd)
    ReturnVal = 0

def TPEducator_Calculation():
    ReturnVal = GetCurrency(USWRec.TEdExp)

def TPForeign_Calculation():
    ReturnVal = Abs(GetCurrency(USWOthInc.TP2555))

def TPHealthSav_Calculation():
    ReturnVal = GetCurrency(USWRec.THealthSav)

def TPJointAmount_Calculation(Index):
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetCurrency(IAOthAdj.TPAmount(Index))
    else:
        ReturnVal = GetCurrency(IAOthAdj.TPAmount(Index)) + GetCurrency(IAOthAdj.SPAmount(Index))

def TPJury_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthAdj.TPJury)
    else:
        ReturnVal = 0

def TPK1_Calculation():
    if GetBool(USWResidency.F1040NR) == False and GetCurrency(USWOthInc.TPK1) < 0:
        ReturnVal = Abs(GetCurrency(USWOthInc.TPK1))
    elif GetBool(USWResidency.F1040NR) == True and GetCurrency(USWOthIncNR.TPK1) < 0:
        ReturnVal = Abs(GetCurrency(USWOthIncNR.TPK1))
    else:
        ReturnVal = 0

def TPName_Calculation():
    ReturnVal = GetString(USWBasicInfo.TPCommon)

def TPOlympic_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthAdj.Text1)
    else:
        ReturnVal = 0

def TPPerRent_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthAdj.TPPerRent)
    else:
        ReturnVal = 0

def TPRFST_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthAdj.TPRFST)
    else:
        ReturnVal = GetCurrency(USWOthAdjNR.TPRFST)

def TPSub_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthAdj.TPSub)
    else:
        ReturnVal = GetCurrency(USWOthAdjNR.TPSub)

def TPTot_Calculation():
    ReturnVal = GetCurrency(IAOthAdj.TOth1) + GetCurrency(IAOthAdj.TPActiveMil) + GetCurrency(IAOthAdj.TPAltMV) + GetCurrency(IAOthAdj.TPInvolConv) + GetCurrency(IAOthAdj.TPClaimOfRight) + GetCurrency(IAOthAdj.TPIAEd) + GetCurrency(IAOthAdj.TPIADis) + GetCurrency(IAOthAdj.TPDomProd) + GetCurrency(IAOthAdj.TPFirstHmBuy) + GetCurrency(IAOthAdj.TPEmployerSS) + GetCurrency(IAOthAdj.TPFedFuels) + GetCurrency(IAOthAdj.TPForeign) + GetCurrency(IAOthAdj.TP2555) + GetCurrency(IAOthAdj.TPDistressed) + GetCurrency(IAOthAdj.TPHealthSav) + GetCurrency(IAOthAdj.TPVet) + GetCurrency(IAOthAdj.TPVetGrant) + GetCurrency(IAOthAdj.TPHomeHealth) + GetCurrency(IAOthAdj.TPIAVetTrust) + GetCurrency(IAOthAdj.TPMilitaryExem) + GetCurrency(IAOthAdj.TIANOL) + GetCurrency(IAOthAdj.TPOrgan) + GetCurrency(IAOthAdj.TPK1) + GetCurrency(IAOthAdj.TPSegal) + GetCurrency(IAOthAdj.TPShell) + GetCurrency(IAOthAdj.TStud) + GetCurrency(IAOthAdj.TPVictim) + GetCurrency(IAOthAdj.TPWages) + GetCurrency(IAOthAdj.TPWorkCr) + GetCurrency(IAOthAdj.TP2106) + GetCurrency(IAOthAdj.TMSA) + GetCurrency(IAOthAdj.TPJury) + GetCurrency(IAOthAdj.TPRFST) + GetCurrency(IAOthAdj.TPSub) + GetCurrency(IAOthAdj.TP501c) + GetCurrency(IAOthAdj.TPPerRent) + GetCurrency(IAOthAdj.TP403b) + GetCurrency(IAOthAdj.TPUDC) + GetCurrency(IAOthAdj.TPWBF) + GetCurrency(IAOthAdj.TP8873) + GetCurrency(IAOthAdj.TPEducator) + GetCurrency(IAOthAdj.TPTuition) + GetCurrency(IAOthAdj.TPElectric) + GetCurrency(IAOthAdj.TPRapid) + GetCurrency(IAOthAdj.TPOlympic) + GetCurrency(IAOthAdj.TPIAABLE)

def TPTuition_Calculation():
    ReturnVal = 0
    #ReturnVal = GetCurrency(USWRec.TTuitAdj)

def TPUDC_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthAdj.TPUDC)
    else:
        ReturnVal = GetCurrency(USWOthAdjNR.TPUDC)

def TPWBF_Calculation():
    if GetBool(USWResidency.F1040NR) == False:
        ReturnVal = GetCurrency(USWOthAdj.TPWBF)
    else:
        ReturnVal = GetCurrency(USWOthAdjNR.TPWBF)

def TStud_Calculation():
    ReturnVal = GetCurrency(USWRec.TStudAdj)

