from forms.out import IA137
from forms.out import IA148SP
from forms.out import IAF1040
from forms.out import IAREQUIRED
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Alert10_Calculation():
    RetailZip = Integer()
    if trim(get_string(IA137.StateAbb)) == '':
        RetailZip = 0
    elif  ( IsValidZIP(get_string(IA137.ZipCode), get_string(IA137.StateAbb)) ) :
        RetailZip = 0
    else:
        RetailZip = 1
    if get_bool(IA137.Print) == False or get_bool(IA137.Site) == False:
        return 0
    elif not IsValidEFileString(get_string(IA137.RetailName)):
        return 1
    elif not IsValidEFileString(get_string(IA137.RetailAdd)):
        return 1
    elif not IsValidEFileString(get_string(IA137.City)):
        return 1
    elif trim(get_string(IA137.StateAbb)) == '':
        return 1
    elif RetailZip == 1:
        return 1
    else:
        return 0

def AllSitesTotal_Calculation():
    if get_bool(IA137.Site) == True:
        return 0
    else:
        return get_number(IA137.TotGas)

def BioDisparity_Calculation():
    return max_value(0, Round(get_float(IA137.BioThresPer) - get_float(IA137.BioDistPer), 4))

def BioDistPer_Calculation():
    if get_number(IA137.TotGas) <= 0:
        return 0
    else:
        return Round(get_float(IA137.TotGal) / get_float(IA137.TotGas), 4)

def BioThresPer_Calculation():
    # updated for 2018
    if get_number(IA137.AllSitesTotal) <= 0:
        return 0
    elif get_number(IA137.AllSitesTotal) <= 200000:
        return 0.19
    else:
        return 0.23

def Common_Calculation():
    if get_bool(IAF1040.MFJ) == True:
        return get_string(USWBasicInfo.CombFirst)
    else:
        return get_string(USWBasicInfo.TPCommon)

def CreditRate_Calculation():
    if get_float(IA137.BioDisparity) == 0:
        return '0.080'
    elif get_float(IA137.BioDisparity) >= 0.0001 and get_float(IA137.BioDisparity) <= 0.02:
        return '0.060'
    elif get_float(IA137.BioDisparity) >= 0.0201 and get_float(IA137.BioDisparity) <= 0.04:
        return '0.040'
    else:
        return '0'

def Description_Calculation():
    Total = Currency()
    Total = get_currency(IA137.TotEthSoldCr) + get_currency(IA137.PassThruCr)
    return CStr(Total) + ' Credit'

def EthPromoteCr_Calculation():
    return get_currency(IA137.IndEthPromoteCr) + get_currency(IA137.PassThruCr)

def EthSoldCr_Calculation():
    if get_float(IA137.BioDisparity) == 0:
        return c_dollar(get_float(IA137.TotEth) * 8)
    elif get_float(IA137.BioDisparity) >= 0.0001 and get_float(IA137.BioDisparity) <= 0.02:
        return c_dollar(get_float(IA137.TotEth) * 6)
    elif get_float(IA137.BioDisparity) >= 0.0201 and get_float(IA137.BioDisparity) <= 0.04:
        return c_dollar(get_float(IA137.TotEth) * 4)
    else:
        return 0

def IndEthPromoteCr_Calculation():
    if get_bool(IA137.Company) == True and get_bool(IA137.Taxpayer) == True:
        return get_currency(IA148.TotCode64)
    elif get_bool(IA137.Company) == True and get_bool(IA137.Spouse) == True:
        return get_currency(IA148SP.TotCode64)
    elif GetCopy() == get_number(IA148.FirstCopy137Site) and get_bool(IA137.Taxpayer) == True:
        return get_currency(IA148.TotCode64)
    elif GetCopy() == get_number(IA148SP.FirstCopy137Site) and get_bool(IA137.Spouse) == True:
        return get_currency(IA148SP.TotCode64)
    else:
        return 0

def MEF137SP_Calculation():
    if get_bool(IA137.Spouse) == True and get_currency(IA137.TotEthSoldCr) > 0:
        return 1
    else:
        return 0

def MEF137SPPTE_Calculation():
    if get_bool(IA137.Spouse) == True and get_currency(IA137.PassThruCr) > 0:
        return 1
    else:
        return 0

def MEF137TP_Calculation():
    if get_bool(IA137.Taxpayer) == True and get_currency(IA137.TotEthSoldCr) > 0:
        return 1
    else:
        return 0

def MEF137TPPTE_Calculation():
    if get_bool(IA137.Taxpayer) == True and get_currency(IA137.PassThruCr) > 0:
        return 1
    else:
        return 0

def MeFBioDisparity_Calculation():
    return get_float(IA137.BioDisparity) * 100

def Names_Calculation():
    if get_bool(IA137.Spouse) == True:
        return get_string(IAREQUIRED.SPCombName)
    else:
        return get_string(IAREQUIRED.TPCombName)

def Owner_Calculation():
    if get_bool(IA137.Taxpayer) == True:
        return get_string(USWBasicInfo.TPTheName)
    else:
        return get_string(USWBasicInfo.SPTheName)

def PassThruCr_Calculation():
    return get_currency(IA137.PTECredit(0))

def Print_Calculation():
    if get_bool(IA137.Spouse) == True and get_bool(IAF1040.CombMFS) == False:
        return 0
    elif get_currency(IA137.TotEthSoldCr) > 0 or get_currency(IA137.PassThruCr) > 0:
        return 1
    else:
        return 0

def PTEFEIN_Calculation():
    if get_currency(IA137.PassThruCr) > 0:
        return get_string(IA137.PTEEIN(0))
    else:
        return ''

def PTEName_Calculation(Index):
    if get_currency(IA137.PassThruCr) > 0:
        return get_string(IA137.PTEEntity(0))
    else:
        return ''

def RetailCityStZip_Calculation():
    return get_string(IA137.City) + ', ' + get_string(IA137.StateAbb) + ' ' + get_string(IA137.ZipCode)

def SpouseCommon_Calculation():
    if get_bool(IAF1040.CombMFS) == True:
        return get_string(USWBasicInfo.SPCommon)
    else:
        return 'Not Applicable'

def SSN_Calculation():
    if get_bool(IA137.Spouse) == True:
        return get_string(IAF1040.SpouseSSN)
    else:
        return get_string(IAF1040.SSN)

def TotB10Gal_Calculation():
    return CLng(Round(get_number(IA137.B10Gal) * 0.11))

def TotB20Gal_Calculation():
    return CLng(Round(get_number(IA137.B20Gal) * 0.2))

def TotB2Gal_Calculation():
    return CLng(Round(get_number(IA137.B2Gal) * 0.02))

def TotB5Gal_Calculation():
    return CLng(Round(get_number(IA137.B5Gal) * 0.05))

def TotBTypeGal_Calculation():
    return CLng(Round(get_float(IA137.BTypeGal) *  ( get_float(IA137.BTypeGalPer) / 100 )))

def TotE10Gal_Calculation():
    return CLng(Round(get_number(IA137.E10Gal) * 0.1))

def TotE15Gal_Calculation():
    return CLng(Round(get_number(IA137.E15Gal) * 0.15))

def TotE85Gal_Calculation():
    return CLng(Round(get_number(IA137.E85Gal) * 0.79))

def TotEth_Calculation():
    return get_number(IA137.TotEthGal)

def TotEthGal_Calculation():
    return get_number(IA137.TotE10Gal) + get_number(IA137.TotE15Gal) + get_number(IA137.TotE85Gal) + get_number(IA137.TotOthGal)

def TotEthGalColA_Calculation():
    return get_number(IA137.E10Gal) + get_number(IA137.E15Gal) + get_number(IA137.E85Gal) + get_number(IA137.OthGal)

def TotEthSoldCr_Calculation():
    return get_currency(IA137.EthSoldCr)

def TotGas_Calculation():
    return get_number(IA137.E10Gal) + get_number(IA137.E15Gal) + get_number(IA137.E85Gal) + get_number(IA137.OthGal) + get_number(IA137.NonEthGal)

def TotGal_Calculation():
    return get_number(IA137.TotEthGal) + get_number(IA137.TotB2Gal) + get_number(IA137.TotB5Gal) + get_number(IA137.TotB10Gal) + get_number(IA137.TotB20Gal) + get_number(IA137.TotBTypeGal)

def TotOthGal_Calculation():
    return CLng(Round(get_float(IA137.OthGal) *  ( get_float(IA137.OthGalPer) / 100 )))


