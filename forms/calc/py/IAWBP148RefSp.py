from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Desc_Calculation():
    Total1 = Currency()
    Total1 = GetCurrency(IAWBP148RefSp.TotRefCr1) + GetCurrency(IAWBP148RefSp.TotRefCr2)
    ReturnVal = CStr(Total1) + ' Refundable Credits'

def Names_Calculation():
    ReturnVal = GetString(IA148Sp.Names)

def Offset_Calculation():
    if GetCopy() == 1:
        ReturnVal = 6
    else:
        ReturnVal = 56

def Print_Calculation():
    if GetCurrency(IAWBP148RefSp.TotRefCr1) > 0 or GetCurrency(IAWBP148RefSp.TotRefCr2) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def PTERefTrig_Calculation(Index):
    if GetString(IAWBP148RefSp.RefPTECode(Index)) == '64' or GetString(IAWBP148RefSp.RefPTECode(Index)) == '58' or GetString(IAWBP148RefSp.RefPTECode(Index)) == '55' or GetString(IAWBP148RefSp.RefPTECode(Index)) == '52' or GetString(IAWBP148RefSp.RefPTECode(Index)) == '59' or GetString(IAWBP148RefSp.RefPTECode(Index)) == '65' or GetString(IAWBP148RefSp.RefPTECode(Index)) == '66':
        ReturnVal = 0
    elif Trim(GetString(IAWBP148RefSp.RefPTEName(Index))) != '':
        ReturnVal = 1
    else:
        ReturnVal = 0

def RefCert_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    strindex = ( ( ( ( GetCopy() - 1 )  * 50 )  + 6 + Index )  * 4 )  + 1
    copystr = Trim(Mid(GetString(IA148Sp.RefCopiesStr), strindex, 4))
    if GetNumber(IA148Sp.RefNbr) == 7:
        ReturnVal = ''
    elif copystr != '':
        Copy = CLng(copystr)
        if ( Copy > 100 )  and  ( Copy <= 200 ) :
            ReturnVal = ''
        elif  ( Copy > 200 )  and  ( Copy <= 300 ) :
            ReturnVal = GetString(IACred.CertNumber, ( Copy )  - 200)
        elif  ( Copy > 300 )  and  ( Copy <= 400 ) :
            ReturnVal = ''
        elif  ( Copy > 400 )  and  ( Copy <= 500 ) :
            ReturnVal = GetString(IACred.CertNumber, ( Copy )  - 400)
        elif  ( Copy > 500 )  and  ( Copy <= 600 ) :
            ReturnVal = ''
        elif  ( Copy > 600 )  and  ( Copy <= 700 ) :
            ReturnVal = ''
        elif  ( Copy > 700 )  and  ( Copy <= 800 ) :
            ReturnVal = GetString(IA128.SuppCertNbr, ( Copy )  - 700)
        elif  ( Copy > 800 )  and  ( Copy <= 900 ) :
            ReturnVal = GetString(IA128S.SuppCertNbr, ( Copy )  - 800)
        elif  ( Copy > 900 )  and  ( Copy <= 1000 ) :
            ReturnVal = ''
        elif  ( Copy > 1000 )  and  ( Copy <= 1100 ) :
            ReturnVal = ''
        elif  ( Copy > 1100 )  and  ( Copy <= 1200 ) :
            ReturnVal = ''
        elif  ( Copy > 1200 )  and  ( Copy <= 1300 ) :
            ReturnVal = GetString(IACred.CertNumber, ( Copy )  - 1200)
        elif  ( Copy > 1300 )  and  ( Copy <= 1400 ) :
            ReturnVal = GetString(IACred.CertNumber, ( Copy )  - 1300)
        elif  ( Copy > 1400 )  and  ( Copy <= 1500 ) :
            ReturnVal = GetString(IACred.CertNumber, ( Copy )  - 1400)
    ReturnVal = ''

def RefCode_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    strindex = ( ( ( ( GetCopy() - 1 )  * 50 )  + 6 + Index )  * 4 )  + 1
    copystr = Trim(Mid(GetString(IA148Sp.RefCopiesStr), strindex, 4))
    if GetNumber(IA148Sp.RefNbr) == 7:
        ReturnVal = ''
    elif copystr != '':
        Copy = CLng(copystr)
        if ( Copy > 100 )  and  ( Copy <= 200 ) :
            ReturnVal = '52'
        elif  ( Copy > 200 )  and  ( Copy <= 300 ) :
            ReturnVal = GetString(IACred.Code, ( Copy )  - 200)
        elif  ( Copy > 300 )  and  ( Copy <= 400 ) :
            ReturnVal = '55'
        elif  ( Copy > 400 )  and  ( Copy <= 500 ) :
            ReturnVal = GetString(IACred.Code, ( Copy )  - 400)
        elif  ( Copy > 500 )  and  ( Copy <= 600 ) :
            ReturnVal = '58'
        elif  ( Copy > 600 )  and  ( Copy <= 700 ) :
            ReturnVal = '58'
        elif  ( Copy > 700 )  and  ( Copy <= 800 ) :
            ReturnVal = '59'
        elif  ( Copy > 800 )  and  ( Copy <= 900 ) :
            ReturnVal = '59'
        elif  ( Copy > 900 )  and  ( Copy <= 1000 ) :
            ReturnVal = '64'
        elif  ( Copy > 1000 )  and  ( Copy <= 1100 ) :
            ReturnVal = '65'
        elif  ( Copy > 1100 )  and  ( Copy <= 1200 ) :
            ReturnVal = '66'
        elif  ( Copy > 1200 )  and  ( Copy <= 1300 ) :
            ReturnVal = GetString(IACred.Code, ( Copy )  - 1200)
        elif  ( Copy > 1300 )  and  ( Copy <= 1400 ) :
            ReturnVal = GetString(IACred.Code, ( Copy )  - 1300)
        elif  ( Copy > 1400 )  and  ( Copy <= 1500 ) :
            ReturnVal = GetString(IACred.Code, ( Copy )  - 1400)
    ReturnVal = ''

def RefCr_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    strindex = ( ( ( ( GetCopy() - 1 )  * 50 )  + 6 + Index )  * 4 )  + 1
    copystr = Trim(Mid(GetString(IA148Sp.RefCopiesStr), strindex, 4))
    if GetNumber(IA148Sp.RefNbr) == 7:
        ReturnVal = 0
    elif copystr != '':
        Copy = CLng(copystr)
        if ( Copy > 100 )  and  ( Copy <= 200 ) :
            ReturnVal = GetCurrency(IA8864.BiodieselCr, ( Copy )  - 100)
        elif  ( Copy > 200 )  and  ( Copy <= 300 ) :
            ReturnVal = GetCurrency(IACred.CYCredit, ( Copy )  - 200)
        elif  ( Copy > 300 )  and  ( Copy <= 400 ) :
            ReturnVal = GetCurrency(IA135.E85Credit, ( Copy )  - 300)
        elif  ( Copy > 400 )  and  ( Copy <= 500 ) :
            ReturnVal = GetCurrency(IACred.CYCredit, ( Copy )  - 400)
        elif  ( Copy > 500 )  and  ( Copy <= 600 ) :
            ReturnVal = GetCurrency(IA128.TotResearchCr, ( Copy )  - 500)
        elif  ( Copy > 600 )  and  ( Copy <= 700 ) :
            ReturnVal = GetCurrency(IA128S.TotResearchCr, ( Copy )  - 600)
        elif  ( Copy > 700 )  and  ( Copy <= 800 ) :
            ReturnVal = GetCurrency(IA128.TotSuppResearchCr, ( Copy )  - 700)
        elif  ( Copy > 800 )  and  ( Copy <= 900 ) :
            ReturnVal = GetCurrency(IA128S.TotSuppResearchCr, ( Copy )  - 800)
        elif  ( Copy > 900 )  and  ( Copy <= 1000 ) :
            ReturnVal = GetCurrency(IA137.EthPromoteCr, ( Copy )  - 900)
        elif  ( Copy > 1000 )  and  ( Copy <= 1100 ) :
            ReturnVal = GetCurrency(IA138.E15Credit, ( Copy )  - 1000)
        elif  ( Copy > 1100 )  and  ( Copy <= 1200 ) :
            ReturnVal = GetCurrency(IA177.CYAdoptionTaxCr, ( Copy )  - 1100)
        elif  ( Copy > 1200 )  and  ( Copy <= 1300 ) :
            ReturnVal = GetCurrency(IACred.CYCredit, ( Copy )  - 1200)
        elif  ( Copy > 1300 )  and  ( Copy <= 1400 ) :
            ReturnVal = GetCurrency(IACred.CYCredit, ( Copy )  - 1300)
        elif  ( Copy > 1400 )  and  ( Copy <= 1500 ) :
            ReturnVal = GetCurrency(IACred.CYCredit, ( Copy )  - 1400)
    ReturnVal = 0

def RefPTECode_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + GetNumber(IAWBP148RefSp.Offset) + 1
    ReturnVal = GetString(IA148BumpSp.RefPTECode(Stuff))

def RefPTEEIN_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + GetNumber(IAWBP148RefSp.Offset) + 1
    ReturnVal = GetString(IA148BumpSp.RefPTEEIN(Stuff))

def RefPTEName_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + GetNumber(IAWBP148RefSp.Offset) + 1
    ReturnVal = GetString(IA148BumpSp.RefPTEName(Stuff))

def RefTPPerc_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + GetNumber(IAWBP148RefSp.Offset) + 1
    ReturnVal = GetFloat(IA148BumpSp.RefTPPerc(Stuff))

def RefTrig_Calculation(Index):
    if GetString(IAWBP148RefSp.RefCode(Index)) == '64' or GetString(IAWBP148RefSp.RefCode(Index)) == '58' or GetString(IAWBP148RefSp.RefCode(Index)) == '55' or GetString(IAWBP148RefSp.RefCode(Index)) == '52' or GetString(IAWBP148RefSp.RefCode(Index)) == '59' or GetString(IAWBP148RefSp.RefCode(Index)) == '65' or GetString(IAWBP148RefSp.RefCode(Index)) == '66':
        ReturnVal = 0
    elif GetCurrency(IAWBP148RefSp.RefCr(Index)) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def SSN_Calculation():
    ReturnVal = GetString(IA148Sp.SSN)

def TotRefCr1_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 25:
        SubTot = SubTot + GetCurrency(IAWBP148RefSp.RefCr(count))
        count = count + 1
    ReturnVal = SubTot

def TotRefCr2_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 25
    SubTot = 0
    while count < 50:
        SubTot = SubTot + GetCurrency(IAWBP148RefSp.RefCr(count))
        count = count + 1
    ReturnVal = SubTot

