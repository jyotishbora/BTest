from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def ActValue_Calculation():
    ActValue = Currency()

    count = Integer()
    count = 1
    ActValue = 0
    while count <= GetAllCopies(USD1099R):
        if GetBool(USD1099R.Qual4972, count) == True and GetBool(USD1099R.Spouse, count) == True:
            ActValue = ActValue + Round(GetCurrency(USD1099R.Other, count))
        else:
            ActValue = ActValue
        count = count + 1
    if GetBool(USF4972Spouse.UseForm) == True and GetBool(USF4972Spouse.Choose10Year) == True:
        if GetBool(USF4972Spouse.MRD) == True and GetBool(USF4972Spouse.Box8Perc) != 0:
            ReturnVal = CCur(ActValue /  ( GetFloat(USF4972Spouse.Box8Perc) / 100 ))
        else:
            ReturnVal = ActValue
    else:
        ReturnVal = 0

def AdjTotTaxable_Calculation():
    if GetBool(USF4972Spouse.UseForm) == True and GetBool(USF4972Spouse.Choose10Year) == True:
        ReturnVal = GetCurrency(USF4972Spouse.TotTaxable) + GetCurrency(USF4972Spouse.ActValue)
    else:
        ReturnVal = 0

def Alert10_Calculation():
    count = Integer()

    Hit = Long()
    count = 1
    Hit = 0
    while count <= GetAllCopies(USD1099R):
        if GetBool(USD1099R.Spouse, count) == True and GetBool(USD1099R.Qual4972, count) == True:
            Hit = Hit + 1
        else:
            Hit = Hit
        count = count + 1
    if GetBool(USF4972Spouse.UseForm) == True and GetBool(USF4972Spouse.ChooseCapGain) == False and GetBool(USF4972Spouse.Choose10Year) == False and Hit != 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert20_Calculation():
    count = Integer()

    Hit = Long()
    count = 1
    Hit = 0
    while count <= GetAllCopies(USD1099R):
        if GetBool(USD1099R.Spouse, count) == True and GetBool(USD1099R.Qual4972, count) == True:
            Hit = Hit + 1
        else:
            Hit = Hit
        count = count + 1
    if GetNumber(USF4972Spouse.Print) == 1 and Hit > 1:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert30_Calculation():
    ReturnVal = 0

def Alert40_Calculation():
    ReturnVal = 0

def Alert5_Calculation():
    if GetNumber(USWRetirement.SP4972) == 1 and GetStatus(UserModifiedStatus) == False:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert50_Calculation():
    if GetBool(USF4972Spouse.MRD) == True and GetBool(USF4972Spouse.Choose10Year) == True and GetBool(USF4972Spouse.UseForm) == True and GetFloat(USF4972Spouse.Box9aPerc) == 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Alert60_Calculation():
    count = Integer()

    Hit = Long()
    count = 1
    Hit = 0
    while count <= GetAllCopies(USD1099R):
        if GetCurrency(USD1099R.Other, count) > 0 and GetBool(USD1099R.Spouse, count) == True and GetBool(USD1099R.Qual4972, count) == True:
            Hit = Hit + 1
        else:
            Hit = Hit
        count = count + 1
    if GetBool(USF4972Spouse.MRD) == True and GetBool(USF4972Spouse.Choose10Year) == True and GetBool(USF4972Spouse.UseForm) == True:
        if Hit != 0 and GetFloat(USF4972Spouse.Box8Perc) == 0:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def Alert70_Calculation():
    ReturnVal = 0

def CapGain_Calculation():
    Estate = Currency()
    Estate = CDollar(GetCurrency(USF4972Spouse.EstateTax) * GetFloat(USF4972Spouse.DBWC))
    if GetBool(USF4972Spouse.UseForm) == True and GetBool(USF4972Spouse.ChooseCapGain) == True:
        ReturnVal = MaxValue(0, GetCurrency(USF4972Spouse.DBWF) - Estate)
    else:
        ReturnVal = 0

def CapGainTax_Calculation():
    ReturnVal = CDollar(GetCurrency(USF4972Spouse.CapGain) * 0.2)

def Common_Calculation():
    ReturnVal = GetString(USWBasicInfo.SPCommon)

def DBWA_Calculation():
    ReturnVal = GetCurrency(USF4972Spouse.NUAG)

def DBWB_Calculation():
    if GetBool(USF4972Spouse.NUA) == True:
        ReturnVal = GetCurrency(USF4972Spouse.NUAB) + GetCurrency(USF4972Spouse.NUAD)
    else:
        ReturnVal = GetCurrency(USF4972Spouse.NUAB)

def DBWC_Calculation():
    if GetCurrency(USF4972Spouse.DBWB) == 0:
        ReturnVal = 0
    else:
        ReturnVal = GetFloat(USF4972Spouse.DBWA) / GetFloat(USF4972Spouse.DBWB)

def DBWD_Calculation():
    ReturnVal = GetCurrency(USF4972Spouse.DeathExcl)

def DBWE_Calculation():
    ReturnVal = CDollar(GetCurrency(USF4972Spouse.DBWD) * GetFloat(USF4972Spouse.DBWC))

def DBWF_Calculation():
    ReturnVal = GetCurrency(USF4972Spouse.DBWA) - GetCurrency(USF4972Spouse.DBWE)

def Death_Calculation():
    TPShare = Currency()
    if GetBool(USF4972Spouse.CapGain) == True:
        TPShare = GetCurrency(USF4972Spouse.DBWD) - GetCurrency(USF4972Spouse.DBWE)
    else:
        TPShare = GetCurrency(USF4972Spouse.DeathExcl)
    if GetBool(USF4972Spouse.UseForm) == True and GetBool(USF4972Spouse.Choose10Year) == True:
        if GetBool(USF4972Spouse.MRD) == True and GetFloat(USF4972Spouse.Box9aPerc) != 0:
            ReturnVal = CCur(TPShare /  ( GetFloat(USF4972Spouse.Box9aPerc) / 100 ))
        else:
            ReturnVal = TPShare
    else:
        ReturnVal = 0

def Desc_Calculation():
    ReturnVal = GetString(USF4972Spouse.Common)

def Estate_Calculation():
    CapGainEstate = Currency()
    if GetBool(USF4972Spouse.ChooseCapGain) == True:
        CapGainEstate = CDollar(GetCurrency(USF4972Spouse.EstateTax) * GetFloat(USF4972Spouse.DBWC))
    else:
        CapGainEstate = 0
    if GetBool(USF4972Spouse.UseForm) == True and GetBool(USF4972Spouse.Choose10Year) == True:
        if GetBool(USF4972Spouse.MRD) == True and GetFloat(USF4972Spouse.Box9aPerc) != 0:
            ReturnVal = CCur(( GetCurrency(USF4972Spouse.EstateTax) - CapGainEstate )  /  ( GetFloat(USF4972Spouse.Box9aPerc) / 100 ))
        else:
            ReturnVal = GetCurrency(USF4972Spouse.EstateTax) - CapGainEstate
    else:
        ReturnVal = 0

def Exist_Calculation():
    ReturnVal = 1

def Ln13_Calculation():
    if GetCurrency(USF4972Spouse.AdjTotTaxable) > Decimal("69999"):
        ReturnVal = 0
    else:
        ReturnVal = MinValue(Decimal("10000"), CDollar(GetCurrency(USF4972Spouse.AdjTotTaxable) * 0.5))

def Ln14_Calculation():
    if GetCurrency(USF4972Spouse.AdjTotTaxable) > Decimal("69999"):
        ReturnVal = 0
    else:
        ReturnVal = MaxValue(0, GetCurrency(USF4972Spouse.AdjTotTaxable) - Decimal("20000"))

def Ln15_Calculation():
    ReturnVal = CDollar(GetCurrency(USF4972Spouse.Ln14) * 0.2)

def Ln17_Calculation():
    ReturnVal = GetCurrency(USF4972Spouse.AdjTotTaxable) - GetCurrency(USF4972Spouse.MinDisAllow)

def Ln19_Calculation():
    if GetBool(USF4972Spouse.UseForm) == True and GetBool(USF4972Spouse.Choose10Year) == True:
        ReturnVal = MaxValue(0, GetCurrency(USF4972Spouse.Ln17) - GetCurrency(USF4972Spouse.Estate))
    else:
        ReturnVal = 0

def Ln20_Calculation():
    if GetBool(USF4972Spouse.UseForm) == True and GetBool(USF4972Spouse.Choose10Year) == True:
        if GetCurrency(USF4972Spouse.ActValue) > 0:
            if GetCurrency(USF4972Spouse.AdjTotTaxable) == 0:
                ReturnVal = 0
            else:
                ReturnVal = GetFloat(USF4972Spouse.ActValue) / GetFloat(USF4972Spouse.AdjTotTaxable)
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def Ln21_Calculation():
    ReturnVal = CDollar(GetCurrency(USF4972Spouse.MinDisAllow) * GetFloat(USF4972Spouse.Ln20))

def Ln22_Calculation():
    if GetBool(USF4972Spouse.UseForm) == True and GetBool(USF4972Spouse.Choose10Year) == True:
        ReturnVal = MaxValue(0, GetCurrency(USF4972Spouse.ActValue) - GetCurrency(USF4972Spouse.Ln21))
    else:
        ReturnVal = 0

def Ln23_Calculation():
    ReturnVal = CDollar(GetCurrency(USF4972Spouse.Ln19) * 0.1)

def Ln26_Calculation():
    ReturnVal = CDollar(GetCurrency(USF4972Spouse.Ln22) * 0.1)

def MinDisAllow_Calculation():
    ReturnVal = GetCurrency(USF4972Spouse.Ln13) - GetCurrency(USF4972Spouse.Ln15)

def MobDisQual_Calculation():
    if GetBool(USF4972Spouse.Print) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

def MRDText_Calculation():
    if GetNumber(USF4972Spouse.Print) == 1 and GetBool(USF4972Spouse.Choose10Year) == True and GetBool(USF4972Spouse.MRD) == True:
        ReturnVal = 'MRD'
    else:
        ReturnVal = ''

def Names_Calculation():
    ReturnVal = GetString(USWBasicInfo.SPCombName)

def NUAA_Calculation():
    CapGain = Currency()

    count = Integer()
    count = 1
    CapGain = 0
    while count <= GetAllCopies(USD1099R):
        if GetBool(USD1099R.Qual4972, count) == True and GetBool(USD1099R.Spouse, count) == True:
            CapGain = CapGain + Round(GetCurrency(USD1099R.CapGain, count))
        else:
            CapGain = CapGain
        count = count + 1
    ReturnVal = CapGain

def NUAAmt_Calculation():
    if GetNumber(USF4972Spouse.Print) == 1 and GetBool(USF4972Spouse.NUA) == True and GetBool(USF4972Spouse.ChooseCapGain) == True and GetCurrency(USF4972Spouse.NUAD) > 0:
        ReturnVal = GetCurrency(USF4972Spouse.NUAE)
    else:
        ReturnVal = 0

def NUAAmt2_Calculation():
    if GetNumber(USF4972Spouse.Print) == 1 and GetBool(USF4972Spouse.NUA) == True and GetBool(USF4972Spouse.ChooseCapGain) == False and GetCurrency(USF4972Spouse.NUAD) > 0:
        ReturnVal = GetCurrency(USF4972Spouse.NUAD)
    else:
        ReturnVal = 0

def NUAB_Calculation():
    Taxable = Currency()

    count = Integer()
    count = 1
    Taxable = 0
    while count <= GetAllCopies(USD1099R):
        if GetBool(USD1099R.Qual4972, count) == True and GetBool(USD1099R.Spouse, count) == True:
            Taxable = Taxable + Round(GetCurrency(USD1099R.LumpSum, count))
        else:
            Taxable = Taxable
        count = count + 1
    ReturnVal = Taxable

def NUAC_Calculation():
    if GetCurrency(USF4972Spouse.NUAB) == 0:
        ReturnVal = 0
    else:
        ReturnVal = GetFloat(USF4972Spouse.NUAA) / GetFloat(USF4972Spouse.NUAB)

def NUAD_Calculation():
    NUA = Currency()

    count = Integer()
    count = 1
    NUA = 0
    while count <= GetAllCopies(USD1099R):
        if GetBool(USD1099R.Qual4972, count) == True and GetBool(USD1099R.Spouse, count) == True:
            NUA = NUA + Round(GetCurrency(USD1099R.UnRealApp, count))
        else:
            NUA = NUA
        count = count + 1
    ReturnVal = NUA

def NUAE_Calculation():
    NUA = Currency()

    count = Integer()
    #pulls from each R instead of computing the amount in total
    count = 1
    NUA = 0
    while count <= GetAllCopies(USD1099R):
        if GetBool(USD1099R.Qual4972, count) == True and GetBool(USD1099R.Spouse, count) == True:
            NUA = NUA + Round(GetCurrency(USD1099R.F4972NUA, count))
        else:
            NUA = NUA
        count = count + 1
    ReturnVal = NUA

def NUAF_Calculation():
    ReturnVal = GetCurrency(USF4972Spouse.NUAD) - GetCurrency(USF4972Spouse.NUAE)

def NUAG_Calculation():
    if GetBool(USF4972Spouse.NUA) == True:
        ReturnVal = GetCurrency(USF4972Spouse.NUAA) + GetCurrency(USF4972Spouse.NUAE)
    else:
        ReturnVal = GetCurrency(USF4972Spouse.NUAA)

def NUALn6_Calculation():
    if GetString(USF4972Spouse.NUAText) != '':
        ReturnVal = GetString(USF4972Spouse.NUAText) + ' ' + GetString(USF4972Spouse.NUAAmt)
    else:
        ReturnVal = ''

def NUALn8_Calculation():
    if GetString(USF4972Spouse.NUAText2) != '':
        ReturnVal = GetString(USF4972Spouse.NUAText2) + ' ' + GetString(USF4972Spouse.NUAAmt2)
    else:
        ReturnVal = ''

def NUAText_Calculation():
    if GetNumber(USF4972Spouse.Print) == 1 and GetBool(USF4972Spouse.NUA) == True and GetBool(USF4972Spouse.ChooseCapGain) == True and GetCurrency(USF4972Spouse.NUAD) > 0:
        ReturnVal = 'NUA'
    else:
        ReturnVal = ''

def NUAText2_Calculation():
    if GetNumber(USF4972Spouse.Print) == 1 and GetBool(USF4972Spouse.NUA) == True and GetBool(USF4972Spouse.ChooseCapGain) == False and GetCurrency(USF4972Spouse.NUAD) > 0:
        ReturnVal = 'NUA'
    else:
        ReturnVal = ''

def OrdInc_Calculation():
    OrdInc = Currency()

    Taxable = Currency()

    CapGain = Currency()
    Taxable = GetCurrency(USF4972Spouse.NUAB)
    CapGain = GetCurrency(USF4972Spouse.NUAA)
    if GetBool(USF4972Spouse.NUA) == True and GetBool(USF4972Spouse.CapGain) == True:
        OrdInc = MaxValue(0, Taxable - CapGain) + GetCurrency(USF4972Spouse.NUAF)
    elif GetBool(USF4972Spouse.NUA) == True and GetBool(USF4972Spouse.CapGain) == False:
        OrdInc = Taxable + GetCurrency(USF4972Spouse.NUAD)
    elif GetBool(USF4972Spouse.NUA) == False and GetBool(USF4972Spouse.CapGain) == True:
        OrdInc = MaxValue(0, Taxable - CapGain)
    else:
        OrdInc = Taxable
    if GetBool(USF4972Spouse.UseForm) == True and GetBool(USF4972Spouse.Choose10Year) == True:
        if GetBool(USF4972Spouse.MRD) == True:
            if GetFloat(USF4972Spouse.Box9aPerc) != 0:
                ReturnVal = CCur(OrdInc /  ( GetFloat(USF4972Spouse.Box9aPerc) / 100 ))
            else:
                ReturnVal = OrdInc
        else:
            ReturnVal = OrdInc
    else:
        ReturnVal = 0

def Print_Calculation():
    if GetCurrency(USF4972Spouse.Tax) > 0 and FS() == 2:
        ReturnVal = 1
    else:
        ReturnVal = 0

def SSN_Calculation():
    ReturnVal = GetString(USWBasicInfo.SpouseSSN)

def StopR_Calculation():
    #to stop the calculation of pensions on 1099-R
    if GetBool(USF4972Spouse.UseForm) == True and GetBool(USF4972Spouse.Choose10Year) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Tax_Calculation():
    ReturnVal = GetCurrency(USF4972Spouse.CapGainTax) + GetCurrency(USF4972Spouse.Tax1MTax2)

def Tax1_Calculation():
    ReturnVal = LumpSumTax(GetCurrency(USF4972Spouse.Ln23))

def Tax1By10_Calculation():
    ReturnVal = CDollar(GetCurrency(USF4972Spouse.Tax1) * 10)

def Tax1MTax2_Calculation():
    Line29 = Currency()
    Line29 = MaxValue(0, GetCurrency(USF4972Spouse.Tax1By10) - GetCurrency(USF4972Spouse.Tax2By10))
    if GetBool(USF4972Spouse.MRD) == True and GetFloat(USF4972Spouse.Box9aPerc) != 0:
        ReturnVal = CDollar(Line29 *  ( GetFloat(USF4972Spouse.Box9aPerc) / 100 ))
    else:
        ReturnVal = Line29

def Tax2_Calculation():
    ReturnVal = LumpSumTax(GetCurrency(USF4972Spouse.Ln26))

def Tax2By10_Calculation():
    ReturnVal = CDollar(GetCurrency(USF4972Spouse.Tax2) * 10)

def TotTaxable_Calculation():
    if GetBool(USF4972Spouse.UseForm) == True:
        ReturnVal = MaxValue(0, GetCurrency(USF4972Spouse.OrdInc) - GetCurrency(USF4972Spouse.Death))
    else:
        ReturnVal = 0

def TPAddback_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(USF4972Spouse.TPCapGain) + GetCurrency(USF4972Spouse.TPTaxAmt) - GetCurrency(USF4972Spouse.TPEstate))

def TPAddbackNoEx_Calculation():
    ReturnVal = GetCurrency(USF4972Spouse.TPCapGainNoEx) + GetCurrency(USF4972Spouse.TPOrdInc)

def TPCapGain_Calculation():
    ReturnVal = GetCurrency(USF4972Spouse.CapGain)

def TPCapGainNoEx_Calculation():
    Estate = Currency()
    Estate = CDollar(GetCurrency(USF4972Spouse.EstateTax) * GetFloat(USF4972Spouse.DBWC))
    if GetBool(USF4972Spouse.ChooseCapGain) == True and GetBool(USF4972Spouse.UseForm) == True:
        ReturnVal = GetCurrency(USF4972Spouse.CapGain) + GetCurrency(USF4972Spouse.DBWE) + Estate
    else:
        ReturnVal = 0

def TPDBE_Calculation():
    CapGainDBE = Currency()
    if GetBool(USF4972Spouse.ChooseCapGain) == True:
        CapGainDBE = GetCurrency(USF4972Spouse.DBWE)
    else:
        CapGainDBE = 0
    if GetBool(USF4972Spouse.UseForm) == True and GetBool(USF4972Spouse.Choose10Year) == True:
        ReturnVal = GetCurrency(USF4972Spouse.DeathExcl) - CapGainDBE
    else:
        ReturnVal = 0

def TPEstate_Calculation():
    CapGainEstate = Currency()
    #to reduce line 10
    if GetBool(USF4972Spouse.ChooseCapGain) == True:
        CapGainEstate = CDollar(GetCurrency(USF4972Spouse.EstateTax) * GetFloat(USF4972Spouse.DBWC))
    else:
        CapGainEstate = 0
    if GetBool(USF4972Spouse.UseForm) == True and GetBool(USF4972Spouse.Choose10Year) == True:
        ReturnVal = GetCurrency(USF4972Spouse.EstateTax) - CapGainEstate
    else:
        ReturnVal = 0

def TPOrdInc_Calculation():
    Taxable = Currency()

    CapGain = Currency()
    Taxable = GetCurrency(USF4972Spouse.NUAB)
    CapGain = GetCurrency(USF4972Spouse.NUAA)
    if GetBool(USF4972Spouse.UseForm) == True and GetBool(USF4972Spouse.Choose10Year) == True:
        if GetBool(USF4972Spouse.NUA) == True and GetBool(USF4972Spouse.CapGain) == True:
            ReturnVal = MaxValue(0, Taxable - CapGain) + GetCurrency(USF4972Spouse.NUAF)
        elif GetBool(USF4972Spouse.NUA) == True and GetBool(USF4972Spouse.CapGain) == False:
            ReturnVal = Taxable + GetCurrency(USF4972Spouse.NUAD)
        elif GetBool(USF4972Spouse.NUA) == False and GetBool(USF4972Spouse.CapGain) == True:
            ReturnVal = MaxValue(0, Taxable - CapGain)
        else:
            ReturnVal = Taxable
    else:
        ReturnVal = 0

def TPTaxAmt_Calculation():
    if GetBool(USF4972Spouse.UseForm) == True and GetBool(USF4972Spouse.Choose10Year) == True:
        if GetBool(USF4972Spouse.MRD) == True and GetFloat(USF4972Spouse.Box9aPerc) != 0:
            ReturnVal = CCur(GetCurrency(USF4972Spouse.TotTaxable) *  ( GetFloat(USF4972Spouse.Box9aPerc) / 100 ))
        else:
            ReturnVal = GetCurrency(USF4972Spouse.TotTaxable)
    else:
        ReturnVal = 0

def UseForm_Calculation():
    Ln1 = Long()

    Ln2 = Long()

    Ln3and4 = Long()

    Ln5a = Long()

    Ln5b = Long()
    if GetBool(USF4972Spouse.Ln1Yes) == True:
        Ln1 = 0
    else:
        Ln1 = 1
    if GetBool(USF4972Spouse.Ln2No) == True:
        Ln2 = 0
    else:
        Ln2 = 1
    if GetBool(USF4972Spouse.Ln3Yes) == True and GetBool(USF4972Spouse.Ln4Yes) == True:
        Ln3and4 = 0
    elif GetBool(USF4972Spouse.Ln3Yes) == True and GetBool(USF4972Spouse.Ln4No) == True:
        Ln3and4 = 0
    elif GetBool(USF4972Spouse.Ln3No) == True and GetBool(USF4972Spouse.Ln4Yes) == True:
        Ln3and4 = 0
    else:
        Ln3and4 = 1
    if GetBool(USF4972Spouse.Ln5aNo) == True:
        Ln5a = 0
    else:
        Ln5a = 1
    if GetBool(USF4972Spouse.Ln5bYes) == True:
        Ln5b = 1
    else:
        Ln5b = 0
    #condition above reversed since it applies only if rec'd as beneficiary
    if Ln1 + Ln2 + Ln3and4 + Ln5a + Ln5b == 0 and FS() == 2:
        ReturnVal = 1
    else:
        ReturnVal = 0

