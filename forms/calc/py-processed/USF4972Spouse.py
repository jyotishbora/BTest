from forms.out import USF4972SPOUSE
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def ActValue_Calculation():
    ActValue = Currency()

    count = Integer()
    count = 1
    ActValue = 0
    while count <= GetAllCopies(USD1099R):
        if get_bool(USD1099R.Qual4972, count) == True and get_bool(USD1099R.Spouse, count) == True:
            ActValue = ActValue + Round(get_currency(USD1099R.Other, count))
        else:
            ActValue = ActValue
        count = count + 1
    if get_bool(USF4972SPOUSE.UseForm) == True and get_bool(USF4972SPOUSE.Choose10Year) == True:
        if get_bool(USF4972SPOUSE.MRD) == True and get_bool(USF4972SPOUSE.Box8Perc) != 0:
            return CCur(ActValue /  ( get_float(USF4972SPOUSE.Box8Perc) / 100 ))
        else:
            return ActValue
    else:
        return 0

def AdjTotTaxable_Calculation():
    if get_bool(USF4972SPOUSE.UseForm) == True and get_bool(USF4972SPOUSE.Choose10Year) == True:
        return get_currency(USF4972SPOUSE.TotTaxable) + get_currency(USF4972SPOUSE.ActValue)
    else:
        return 0

def Alert10_Calculation():
    count = Integer()

    Hit = Long()
    count = 1
    Hit = 0
    while count <= GetAllCopies(USD1099R):
        if get_bool(USD1099R.Spouse, count) == True and get_bool(USD1099R.Qual4972, count) == True:
            Hit = Hit + 1
        else:
            Hit = Hit
        count = count + 1
    if get_bool(USF4972SPOUSE.UseForm) == True and get_bool(USF4972SPOUSE.ChooseCapGain) == False and get_bool(USF4972SPOUSE.Choose10Year) == False and Hit != 0:
        return 1
    else:
        return 0

def Alert20_Calculation():
    count = Integer()

    Hit = Long()
    count = 1
    Hit = 0
    while count <= GetAllCopies(USD1099R):
        if get_bool(USD1099R.Spouse, count) == True and get_bool(USD1099R.Qual4972, count) == True:
            Hit = Hit + 1
        else:
            Hit = Hit
        count = count + 1
    if get_number(USF4972SPOUSE.Print) == 1 and Hit > 1:
        return 1
    else:
        return 0

def Alert30_Calculation():
    return 0

def Alert40_Calculation():
    return 0

def Alert5_Calculation():
    if get_number(USWRetirement.SP4972) == 1 and GetStatus(UserModifiedStatus) == False:
        return 1
    else:
        return 0

def Alert50_Calculation():
    if get_bool(USF4972SPOUSE.MRD) == True and get_bool(USF4972SPOUSE.Choose10Year) == True and get_bool(USF4972SPOUSE.UseForm) == True and get_float(USF4972SPOUSE.Box9aPerc) == 0:
        return 1
    else:
        return 0

def Alert60_Calculation():
    count = Integer()

    Hit = Long()
    count = 1
    Hit = 0
    while count <= GetAllCopies(USD1099R):
        if get_currency(USD1099R.Other, count) > 0 and get_bool(USD1099R.Spouse, count) == True and get_bool(USD1099R.Qual4972, count) == True:
            Hit = Hit + 1
        else:
            Hit = Hit
        count = count + 1
    if get_bool(USF4972SPOUSE.MRD) == True and get_bool(USF4972SPOUSE.Choose10Year) == True and get_bool(USF4972SPOUSE.UseForm) == True:
        if Hit != 0 and get_float(USF4972SPOUSE.Box8Perc) == 0:
            return 1
        else:
            return 0
    else:
        return 0

def Alert70_Calculation():
    return 0

def CapGain_Calculation():
    Estate = Currency()
    Estate = c_dollar(get_currency(USF4972SPOUSE.EstateTax) * get_float(USF4972SPOUSE.DBWC))
    if get_bool(USF4972SPOUSE.UseForm) == True and get_bool(USF4972SPOUSE.ChooseCapGain) == True:
        return max_value(0, get_currency(USF4972SPOUSE.DBWF) - Estate)
    else:
        return 0

def CapGainTax_Calculation():
    return c_dollar(get_currency(USF4972SPOUSE.CapGain) * 0.2)

def Common_Calculation():
    return get_string(USWBasicInfo.SPCommon)

def DBWA_Calculation():
    return get_currency(USF4972SPOUSE.NUAG)

def DBWB_Calculation():
    if get_bool(USF4972SPOUSE.NUA) == True:
        return get_currency(USF4972SPOUSE.NUAB) + get_currency(USF4972SPOUSE.NUAD)
    else:
        return get_currency(USF4972SPOUSE.NUAB)

def DBWC_Calculation():
    if get_currency(USF4972SPOUSE.DBWB) == 0:
        return 0
    else:
        return get_float(USF4972SPOUSE.DBWA) / get_float(USF4972SPOUSE.DBWB)

def DBWD_Calculation():
    return get_currency(USF4972SPOUSE.DeathExcl)

def DBWE_Calculation():
    return c_dollar(get_currency(USF4972SPOUSE.DBWD) * get_float(USF4972SPOUSE.DBWC))

def DBWF_Calculation():
    return get_currency(USF4972SPOUSE.DBWA) - get_currency(USF4972SPOUSE.DBWE)

def Death_Calculation():
    TPShare = Currency()
    if get_bool(USF4972SPOUSE.CapGain) == True:
        TPShare = get_currency(USF4972SPOUSE.DBWD) - get_currency(USF4972SPOUSE.DBWE)
    else:
        TPShare = get_currency(USF4972SPOUSE.DeathExcl)
    if get_bool(USF4972SPOUSE.UseForm) == True and get_bool(USF4972SPOUSE.Choose10Year) == True:
        if get_bool(USF4972SPOUSE.MRD) == True and get_float(USF4972SPOUSE.Box9aPerc) != 0:
            return CCur(TPShare /  ( get_float(USF4972SPOUSE.Box9aPerc) / 100 ))
        else:
            return TPShare
    else:
        return 0

def Desc_Calculation():
    return get_string(USF4972SPOUSE.Common)

def Estate_Calculation():
    CapGainEstate = Currency()
    if get_bool(USF4972SPOUSE.ChooseCapGain) == True:
        CapGainEstate = c_dollar(get_currency(USF4972SPOUSE.EstateTax) * get_float(USF4972SPOUSE.DBWC))
    else:
        CapGainEstate = 0
    if get_bool(USF4972SPOUSE.UseForm) == True and get_bool(USF4972SPOUSE.Choose10Year) == True:
        if get_bool(USF4972SPOUSE.MRD) == True and get_float(USF4972SPOUSE.Box9aPerc) != 0:
            return CCur(( get_currency(USF4972SPOUSE.EstateTax) - CapGainEstate )  /  ( get_float(USF4972SPOUSE.Box9aPerc) / 100 ))
        else:
            return get_currency(USF4972SPOUSE.EstateTax) - CapGainEstate
    else:
        return 0

def Exist_Calculation():
    return 1

def Ln13_Calculation():
    if get_currency(USF4972SPOUSE.AdjTotTaxable) > Decimal("69999"):
        return 0
    else:
        return min_value(Decimal("10000"), c_dollar(get_currency(USF4972SPOUSE.AdjTotTaxable) * 0.5))

def Ln14_Calculation():
    if get_currency(USF4972SPOUSE.AdjTotTaxable) > Decimal("69999"):
        return 0
    else:
        return max_value(0, get_currency(USF4972SPOUSE.AdjTotTaxable) - Decimal("20000"))

def Ln15_Calculation():
    return c_dollar(get_currency(USF4972SPOUSE.Ln14) * 0.2)

def Ln17_Calculation():
    return get_currency(USF4972SPOUSE.AdjTotTaxable) - get_currency(USF4972SPOUSE.MinDisAllow)

def Ln19_Calculation():
    if get_bool(USF4972SPOUSE.UseForm) == True and get_bool(USF4972SPOUSE.Choose10Year) == True:
        return max_value(0, get_currency(USF4972SPOUSE.Ln17) - get_currency(USF4972SPOUSE.Estate))
    else:
        return 0

def Ln20_Calculation():
    if get_bool(USF4972SPOUSE.UseForm) == True and get_bool(USF4972SPOUSE.Choose10Year) == True:
        if get_currency(USF4972SPOUSE.ActValue) > 0:
            if get_currency(USF4972SPOUSE.AdjTotTaxable) == 0:
                return 0
            else:
                return get_float(USF4972SPOUSE.ActValue) / get_float(USF4972SPOUSE.AdjTotTaxable)
        else:
            return 0
    else:
        return 0

def Ln21_Calculation():
    return c_dollar(get_currency(USF4972SPOUSE.MinDisAllow) * get_float(USF4972SPOUSE.Ln20))

def Ln22_Calculation():
    if get_bool(USF4972SPOUSE.UseForm) == True and get_bool(USF4972SPOUSE.Choose10Year) == True:
        return max_value(0, get_currency(USF4972SPOUSE.ActValue) - get_currency(USF4972SPOUSE.Ln21))
    else:
        return 0

def Ln23_Calculation():
    return c_dollar(get_currency(USF4972SPOUSE.Ln19) * 0.1)

def Ln26_Calculation():
    return c_dollar(get_currency(USF4972SPOUSE.Ln22) * 0.1)

def MinDisAllow_Calculation():
    return get_currency(USF4972SPOUSE.Ln13) - get_currency(USF4972SPOUSE.Ln15)

def MobDisQual_Calculation():
    if get_bool(USF4972SPOUSE.Print) == True:
        return 1
    else:
        return 0

def MRDText_Calculation():
    if get_number(USF4972SPOUSE.Print) == 1 and get_bool(USF4972SPOUSE.Choose10Year) == True and get_bool(USF4972SPOUSE.MRD) == True:
        return 'MRD'
    else:
        return ''

def Names_Calculation():
    return get_string(USWBasicInfo.SPCombName)

def NUAA_Calculation():
    CapGain = Currency()

    count = Integer()
    count = 1
    CapGain = 0
    while count <= GetAllCopies(USD1099R):
        if get_bool(USD1099R.Qual4972, count) == True and get_bool(USD1099R.Spouse, count) == True:
            CapGain = CapGain + Round(get_currency(USD1099R.CapGain, count))
        else:
            CapGain = CapGain
        count = count + 1
    return CapGain

def NUAAmt_Calculation():
    if get_number(USF4972SPOUSE.Print) == 1 and get_bool(USF4972SPOUSE.NUA) == True and get_bool(USF4972SPOUSE.ChooseCapGain) == True and get_currency(USF4972SPOUSE.NUAD) > 0:
        return get_currency(USF4972SPOUSE.NUAE)
    else:
        return 0

def NUAAmt2_Calculation():
    if get_number(USF4972SPOUSE.Print) == 1 and get_bool(USF4972SPOUSE.NUA) == True and get_bool(USF4972SPOUSE.ChooseCapGain) == False and get_currency(USF4972SPOUSE.NUAD) > 0:
        return get_currency(USF4972SPOUSE.NUAD)
    else:
        return 0

def NUAB_Calculation():
    Taxable = Currency()

    count = Integer()
    count = 1
    Taxable = 0
    while count <= GetAllCopies(USD1099R):
        if get_bool(USD1099R.Qual4972, count) == True and get_bool(USD1099R.Spouse, count) == True:
            Taxable = Taxable + Round(get_currency(USD1099R.LumpSum, count))
        else:
            Taxable = Taxable
        count = count + 1
    return Taxable

def NUAC_Calculation():
    if get_currency(USF4972SPOUSE.NUAB) == 0:
        return 0
    else:
        return get_float(USF4972SPOUSE.NUAA) / get_float(USF4972SPOUSE.NUAB)

def NUAD_Calculation():
    NUA = Currency()

    count = Integer()
    count = 1
    NUA = 0
    while count <= GetAllCopies(USD1099R):
        if get_bool(USD1099R.Qual4972, count) == True and get_bool(USD1099R.Spouse, count) == True:
            NUA = NUA + Round(get_currency(USD1099R.UnRealApp, count))
        else:
            NUA = NUA
        count = count + 1
    return NUA

def NUAE_Calculation():
    NUA = Currency()

    count = Integer()
    #pulls from each R instead of computing the amount in total
    count = 1
    NUA = 0
    while count <= GetAllCopies(USD1099R):
        if get_bool(USD1099R.Qual4972, count) == True and get_bool(USD1099R.Spouse, count) == True:
            NUA = NUA + Round(get_currency(USD1099R.F4972NUA, count))
        else:
            NUA = NUA
        count = count + 1
    return NUA

def NUAF_Calculation():
    return get_currency(USF4972SPOUSE.NUAD) - get_currency(USF4972SPOUSE.NUAE)

def NUAG_Calculation():
    if get_bool(USF4972SPOUSE.NUA) == True:
        return get_currency(USF4972SPOUSE.NUAA) + get_currency(USF4972SPOUSE.NUAE)
    else:
        return get_currency(USF4972SPOUSE.NUAA)

def NUALn6_Calculation():
    if get_string(USF4972SPOUSE.NUAText) != '':
        return get_string(USF4972SPOUSE.NUAText) + ' ' + get_string(USF4972SPOUSE.NUAAmt)
    else:
        return ''

def NUALn8_Calculation():
    if get_string(USF4972SPOUSE.NUAText2) != '':
        return get_string(USF4972SPOUSE.NUAText2) + ' ' + get_string(USF4972SPOUSE.NUAAmt2)
    else:
        return ''

def NUAText_Calculation():
    if get_number(USF4972SPOUSE.Print) == 1 and get_bool(USF4972SPOUSE.NUA) == True and get_bool(USF4972SPOUSE.ChooseCapGain) == True and get_currency(USF4972SPOUSE.NUAD) > 0:
        return 'NUA'
    else:
        return ''

def NUAText2_Calculation():
    if get_number(USF4972SPOUSE.Print) == 1 and get_bool(USF4972SPOUSE.NUA) == True and get_bool(USF4972SPOUSE.ChooseCapGain) == False and get_currency(USF4972SPOUSE.NUAD) > 0:
        return 'NUA'
    else:
        return ''

def OrdInc_Calculation():
    OrdInc = Currency()

    Taxable = Currency()

    CapGain = Currency()
    Taxable = get_currency(USF4972SPOUSE.NUAB)
    CapGain = get_currency(USF4972SPOUSE.NUAA)
    if get_bool(USF4972SPOUSE.NUA) == True and get_bool(USF4972SPOUSE.CapGain) == True:
        OrdInc = max_value(0, Taxable - CapGain) + get_currency(USF4972SPOUSE.NUAF)
    elif get_bool(USF4972SPOUSE.NUA) == True and get_bool(USF4972SPOUSE.CapGain) == False:
        OrdInc = Taxable + get_currency(USF4972SPOUSE.NUAD)
    elif get_bool(USF4972SPOUSE.NUA) == False and get_bool(USF4972SPOUSE.CapGain) == True:
        OrdInc = max_value(0, Taxable - CapGain)
    else:
        OrdInc = Taxable
    if get_bool(USF4972SPOUSE.UseForm) == True and get_bool(USF4972SPOUSE.Choose10Year) == True:
        if get_bool(USF4972SPOUSE.MRD) == True:
            if get_float(USF4972SPOUSE.Box9aPerc) != 0:
                return CCur(OrdInc /  ( get_float(USF4972SPOUSE.Box9aPerc) / 100 ))
            else:
                return OrdInc
        else:
            return OrdInc
    else:
        return 0

def Print_Calculation():
    if get_currency(USF4972SPOUSE.Tax) > 0 and FS() == 2:
        return 1
    else:
        return 0

def SSN_Calculation():
    return get_string(USWBasicInfo.SpouseSSN)

def StopR_Calculation():
    #to stop the calculation of pensions on 1099-R
    if get_bool(USF4972SPOUSE.UseForm) == True and get_bool(USF4972SPOUSE.Choose10Year) == True:
        return 1
    else:
        return 0

def Tax_Calculation():
    return get_currency(USF4972SPOUSE.CapGainTax) + get_currency(USF4972SPOUSE.Tax1MTax2)

def Tax1_Calculation():
    return LumpSumTax(get_currency(USF4972SPOUSE.Ln23))

def Tax1By10_Calculation():
    return c_dollar(get_currency(USF4972SPOUSE.Tax1) * 10)

def Tax1MTax2_Calculation():
    Line29 = Currency()
    Line29 = max_value(0, get_currency(USF4972SPOUSE.Tax1By10) - get_currency(USF4972SPOUSE.Tax2By10))
    if get_bool(USF4972SPOUSE.MRD) == True and get_float(USF4972SPOUSE.Box9aPerc) != 0:
        return c_dollar(Line29 *  ( get_float(USF4972SPOUSE.Box9aPerc) / 100 ))
    else:
        return Line29

def Tax2_Calculation():
    return LumpSumTax(get_currency(USF4972SPOUSE.Ln26))

def Tax2By10_Calculation():
    return c_dollar(get_currency(USF4972SPOUSE.Tax2) * 10)

def TotTaxable_Calculation():
    if get_bool(USF4972SPOUSE.UseForm) == True:
        return max_value(0, get_currency(USF4972SPOUSE.OrdInc) - get_currency(USF4972SPOUSE.Death))
    else:
        return 0

def TPAddback_Calculation():
    return max_value(0, get_currency(USF4972SPOUSE.TPCapGain) + get_currency(USF4972SPOUSE.TPTaxAmt) - get_currency(USF4972SPOUSE.TPEstate))

def TPAddbackNoEx_Calculation():
    return get_currency(USF4972SPOUSE.TPCapGainNoEx) + get_currency(USF4972SPOUSE.TPOrdInc)

def TPCapGain_Calculation():
    return get_currency(USF4972SPOUSE.CapGain)

def TPCapGainNoEx_Calculation():
    Estate = Currency()
    Estate = c_dollar(get_currency(USF4972SPOUSE.EstateTax) * get_float(USF4972SPOUSE.DBWC))
    if get_bool(USF4972SPOUSE.ChooseCapGain) == True and get_bool(USF4972SPOUSE.UseForm) == True:
        return get_currency(USF4972SPOUSE.CapGain) + get_currency(USF4972SPOUSE.DBWE) + Estate
    else:
        return 0

def TPDBE_Calculation():
    CapGainDBE = Currency()
    if get_bool(USF4972SPOUSE.ChooseCapGain) == True:
        CapGainDBE = get_currency(USF4972SPOUSE.DBWE)
    else:
        CapGainDBE = 0
    if get_bool(USF4972SPOUSE.UseForm) == True and get_bool(USF4972SPOUSE.Choose10Year) == True:
        return get_currency(USF4972SPOUSE.DeathExcl) - CapGainDBE
    else:
        return 0

def TPEstate_Calculation():
    CapGainEstate = Currency()
    #to reduce line 10
    if get_bool(USF4972SPOUSE.ChooseCapGain) == True:
        CapGainEstate = c_dollar(get_currency(USF4972SPOUSE.EstateTax) * get_float(USF4972SPOUSE.DBWC))
    else:
        CapGainEstate = 0
    if get_bool(USF4972SPOUSE.UseForm) == True and get_bool(USF4972SPOUSE.Choose10Year) == True:
        return get_currency(USF4972SPOUSE.EstateTax) - CapGainEstate
    else:
        return 0

def TPOrdInc_Calculation():
    Taxable = Currency()

    CapGain = Currency()
    Taxable = get_currency(USF4972SPOUSE.NUAB)
    CapGain = get_currency(USF4972SPOUSE.NUAA)
    if get_bool(USF4972SPOUSE.UseForm) == True and get_bool(USF4972SPOUSE.Choose10Year) == True:
        if get_bool(USF4972SPOUSE.NUA) == True and get_bool(USF4972SPOUSE.CapGain) == True:
            return max_value(0, Taxable - CapGain) + get_currency(USF4972SPOUSE.NUAF)
        elif get_bool(USF4972SPOUSE.NUA) == True and get_bool(USF4972SPOUSE.CapGain) == False:
            return Taxable + get_currency(USF4972SPOUSE.NUAD)
        elif get_bool(USF4972SPOUSE.NUA) == False and get_bool(USF4972SPOUSE.CapGain) == True:
            return max_value(0, Taxable - CapGain)
        else:
            return Taxable
    else:
        return 0

def TPTaxAmt_Calculation():
    if get_bool(USF4972SPOUSE.UseForm) == True and get_bool(USF4972SPOUSE.Choose10Year) == True:
        if get_bool(USF4972SPOUSE.MRD) == True and get_float(USF4972SPOUSE.Box9aPerc) != 0:
            return CCur(get_currency(USF4972SPOUSE.TotTaxable) *  ( get_float(USF4972SPOUSE.Box9aPerc) / 100 ))
        else:
            return get_currency(USF4972SPOUSE.TotTaxable)
    else:
        return 0

def UseForm_Calculation():
    Ln1 = Long()

    Ln2 = Long()

    Ln3and4 = Long()

    Ln5a = Long()

    Ln5b = Long()
    if get_bool(USF4972SPOUSE.Ln1Yes) == True:
        Ln1 = 0
    else:
        Ln1 = 1
    if get_bool(USF4972SPOUSE.Ln2No) == True:
        Ln2 = 0
    else:
        Ln2 = 1
    if get_bool(USF4972SPOUSE.Ln3Yes) == True and get_bool(USF4972SPOUSE.Ln4Yes) == True:
        Ln3and4 = 0
    elif get_bool(USF4972SPOUSE.Ln3Yes) == True and get_bool(USF4972SPOUSE.Ln4No) == True:
        Ln3and4 = 0
    elif get_bool(USF4972SPOUSE.Ln3No) == True and get_bool(USF4972SPOUSE.Ln4Yes) == True:
        Ln3and4 = 0
    else:
        Ln3and4 = 1
    if get_bool(USF4972SPOUSE.Ln5aNo) == True:
        Ln5a = 0
    else:
        Ln5a = 1
    if get_bool(USF4972SPOUSE.Ln5bYes) == True:
        Ln5b = 1
    else:
        Ln5b = 0
    #condition above reversed since it applies only if rec'd as beneficiary
    if Ln1 + Ln2 + Ln3and4 + Ln5a + Ln5b == 0 and FS() == 2:
        return 1
    else:
        return 0


