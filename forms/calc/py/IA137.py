from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Alert10_Calculation():
    RetailZip = Integer()
    if Trim(GetString(IA137.StateAbb)) == '':
        RetailZip = 0
    elif  ( IsValidZIP(GetString(IA137.ZipCode), GetString(IA137.StateAbb)) ) :
        RetailZip = 0
    else:
        RetailZip = 1
    if GetBool(IA137.Print) == False or GetBool(IA137.Site) == False:
        ReturnVal = 0
    elif not IsValidEFileString(GetString(IA137.RetailName)):
        ReturnVal = 1
    elif not IsValidEFileString(GetString(IA137.RetailAdd)):
        ReturnVal = 1
    elif not IsValidEFileString(GetString(IA137.City)):
        ReturnVal = 1
    elif Trim(GetString(IA137.StateAbb)) == '':
        ReturnVal = 1
    elif RetailZip == 1:
        ReturnVal = 1
    else:
        ReturnVal = 0

def AllSitesTotal_Calculation():
    if GetBool(IA137.Site) == True:
        ReturnVal = 0
    else:
        ReturnVal = GetNumber(IA137.TotGas)

def BioDisparity_Calculation():
    ReturnVal = MaxValue(0, Round(GetFloat(IA137.BioThresPer) - GetFloat(IA137.BioDistPer), 4))

def BioDistPer_Calculation():
    if GetNumber(IA137.TotGas) <= 0:
        ReturnVal = 0
    else:
        ReturnVal = Round(GetFloat(IA137.TotGal) / GetFloat(IA137.TotGas), 4)

def BioThresPer_Calculation():
    # updated for 2018
    if GetNumber(IA137.AllSitesTotal) <= 0:
        ReturnVal = 0
    elif GetNumber(IA137.AllSitesTotal) <= 200000:
        ReturnVal = 0.19
    else:
        ReturnVal = 0.23

def Common_Calculation():
    if GetBool(IAF1040.MFJ) == True:
        ReturnVal = GetString(USWBasicInfo.CombFirst)
    else:
        ReturnVal = GetString(USWBasicInfo.TPCommon)

def CreditRate_Calculation():
    if GetFloat(IA137.BioDisparity) == 0:
        ReturnVal = '0.080'
    elif GetFloat(IA137.BioDisparity) >= 0.0001 and GetFloat(IA137.BioDisparity) <= 0.02:
        ReturnVal = '0.060'
    elif GetFloat(IA137.BioDisparity) >= 0.0201 and GetFloat(IA137.BioDisparity) <= 0.04:
        ReturnVal = '0.040'
    else:
        ReturnVal = '0'

def Description_Calculation():
    Total = Currency()
    Total = GetCurrency(IA137.TotEthSoldCr) + GetCurrency(IA137.PassThruCr)
    ReturnVal = CStr(Total) + ' Credit'

def EthPromoteCr_Calculation():
    ReturnVal = GetCurrency(IA137.IndEthPromoteCr) + GetCurrency(IA137.PassThruCr)

def EthSoldCr_Calculation():
    if GetFloat(IA137.BioDisparity) == 0:
        ReturnVal = CDollar(GetFloat(IA137.TotEth) * 8)
    elif GetFloat(IA137.BioDisparity) >= 0.0001 and GetFloat(IA137.BioDisparity) <= 0.02:
        ReturnVal = CDollar(GetFloat(IA137.TotEth) * 6)
    elif GetFloat(IA137.BioDisparity) >= 0.0201 and GetFloat(IA137.BioDisparity) <= 0.04:
        ReturnVal = CDollar(GetFloat(IA137.TotEth) * 4)
    else:
        ReturnVal = 0

def IndEthPromoteCr_Calculation():
    if GetBool(IA137.Company) == True and GetBool(IA137.Taxpayer) == True:
        ReturnVal = GetCurrency(IA148.TotCode64)
    elif GetBool(IA137.Company) == True and GetBool(IA137.Spouse) == True:
        ReturnVal = GetCurrency(IA148Sp.TotCode64)
    elif GetCopy() == GetNumber(IA148.FirstCopy137Site) and GetBool(IA137.Taxpayer) == True:
        ReturnVal = GetCurrency(IA148.TotCode64)
    elif GetCopy() == GetNumber(IA148Sp.FirstCopy137Site) and GetBool(IA137.Spouse) == True:
        ReturnVal = GetCurrency(IA148Sp.TotCode64)
    else:
        ReturnVal = 0

def MEF137SP_Calculation():
    if GetBool(IA137.Spouse) == True and GetCurrency(IA137.TotEthSoldCr) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def MEF137SPPTE_Calculation():
    if GetBool(IA137.Spouse) == True and GetCurrency(IA137.PassThruCr) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def MEF137TP_Calculation():
    if GetBool(IA137.Taxpayer) == True and GetCurrency(IA137.TotEthSoldCr) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def MEF137TPPTE_Calculation():
    if GetBool(IA137.Taxpayer) == True and GetCurrency(IA137.PassThruCr) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def MeFBioDisparity_Calculation():
    ReturnVal = GetFloat(IA137.BioDisparity) * 100

def Names_Calculation():
    if GetBool(IA137.Spouse) == True:
        ReturnVal = GetString(IARequired.SPCombName)
    else:
        ReturnVal = GetString(IARequired.TPCombName)

def Owner_Calculation():
    if GetBool(IA137.Taxpayer) == True:
        ReturnVal = GetString(USWBasicInfo.TPTheName)
    else:
        ReturnVal = GetString(USWBasicInfo.SPTheName)

def PassThruCr_Calculation():
    ReturnVal = GetCurrency(IA137.PTECredit(0))

def Print_Calculation():
    if GetBool(IA137.Spouse) == True and GetBool(IAF1040.CombMFS) == False:
        ReturnVal = 0
    elif GetCurrency(IA137.TotEthSoldCr) > 0 or GetCurrency(IA137.PassThruCr) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def PTEFEIN_Calculation():
    if GetCurrency(IA137.PassThruCr) > 0:
        ReturnVal = GetString(IA137.PTEEIN(0))
    else:
        ReturnVal = ''

def PTEName_Calculation(Index):
    if GetCurrency(IA137.PassThruCr) > 0:
        ReturnVal = GetString(IA137.PTEEntity(0))
    else:
        ReturnVal = ''

def RetailCityStZip_Calculation():
    ReturnVal = GetString(IA137.City) + ', ' + GetString(IA137.StateAbb) + ' ' + GetString(IA137.ZipCode)

def SpouseCommon_Calculation():
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetString(USWBasicInfo.SPCommon)
    else:
        ReturnVal = 'Not Applicable'

def SSN_Calculation():
    if GetBool(IA137.Spouse) == True:
        ReturnVal = GetString(IAF1040.SpouseSSN)
    else:
        ReturnVal = GetString(IAF1040.SSN)

def TotB10Gal_Calculation():
    ReturnVal = CLng(Round(GetNumber(IA137.B10Gal) * 0.11))

def TotB20Gal_Calculation():
    ReturnVal = CLng(Round(GetNumber(IA137.B20Gal) * 0.2))

def TotB2Gal_Calculation():
    ReturnVal = CLng(Round(GetNumber(IA137.B2Gal) * 0.02))

def TotB5Gal_Calculation():
    ReturnVal = CLng(Round(GetNumber(IA137.B5Gal) * 0.05))

def TotBTypeGal_Calculation():
    ReturnVal = CLng(Round(GetFloat(IA137.BTypeGal) *  ( GetFloat(IA137.BTypeGalPer) / 100 )))

def TotE10Gal_Calculation():
    ReturnVal = CLng(Round(GetNumber(IA137.E10Gal) * 0.1))

def TotE15Gal_Calculation():
    ReturnVal = CLng(Round(GetNumber(IA137.E15Gal) * 0.15))

def TotE85Gal_Calculation():
    ReturnVal = CLng(Round(GetNumber(IA137.E85Gal) * 0.79))

def TotEth_Calculation():
    ReturnVal = GetNumber(IA137.TotEthGal)

def TotEthGal_Calculation():
    ReturnVal = GetNumber(IA137.TotE10Gal) + GetNumber(IA137.TotE15Gal) + GetNumber(IA137.TotE85Gal) + GetNumber(IA137.TotOthGal)

def TotEthGalColA_Calculation():
    ReturnVal = GetNumber(IA137.E10Gal) + GetNumber(IA137.E15Gal) + GetNumber(IA137.E85Gal) + GetNumber(IA137.OthGal)

def TotEthSoldCr_Calculation():
    ReturnVal = GetCurrency(IA137.EthSoldCr)

def TotGas_Calculation():
    ReturnVal = GetNumber(IA137.E10Gal) + GetNumber(IA137.E15Gal) + GetNumber(IA137.E85Gal) + GetNumber(IA137.OthGal) + GetNumber(IA137.NonEthGal)

def TotGal_Calculation():
    ReturnVal = GetNumber(IA137.TotEthGal) + GetNumber(IA137.TotB2Gal) + GetNumber(IA137.TotB5Gal) + GetNumber(IA137.TotB10Gal) + GetNumber(IA137.TotB20Gal) + GetNumber(IA137.TotBTypeGal)

def TotOthGal_Calculation():
    ReturnVal = CLng(Round(GetFloat(IA137.OthGal) *  ( GetFloat(IA137.OthGalPer) / 100 )))

