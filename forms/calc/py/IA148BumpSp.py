from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def PTECode_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    if GetNumber(IA148Sp.NonRefNbr) > 10 and Index > 9:
        strindex = ( ( Index - 1 )  * 4 )  + 1
    else:
        strindex = ( ( Index )  * 4 )  + 1
    copystr = Trim(Mid(GetString(IA148Sp.NonRefCopiesStr), strindex, 4))
    if Index == 9 and GetNumber(IA148Sp.NonRefNbr) > 10:
        ReturnVal = 'Stmt'
    elif copystr != '':
        Copy = CLng(copystr)
        if ( Copy > 100 )  and  ( Copy <= 200 ) :
            ReturnVal = '04'
        elif  ( Copy > 200 )  and  ( Copy <= 300 ) :
            ReturnVal = '11'
        elif  ( Copy > 300 )  and  ( Copy <= 400 ) :
            ReturnVal = GetString(IACred.Code, ( Copy )  - 300)
        elif  ( Copy > 400 )  and  ( Copy <= 500 ) :
            ReturnVal = GetString(IACred.Code, ( Copy )  - 400)
        elif  ( Copy > 500 )  and  ( Copy <= 600 ) :
            ReturnVal = GetString(IACred.Code, ( Copy )  - 500)
        elif  ( Copy > 600 )  and  ( Copy <= 700 ) :
            ReturnVal = GetString(IACred.Code, ( Copy )  - 600)
        elif  ( Copy > 700 )  and  ( Copy <= 800 ) :
            ReturnVal = GetString(IACred.Code, ( Copy )  - 700)
        elif  ( Copy > 800 )  and  ( Copy <= 900 ) :
            ReturnVal = GetString(IACred.Code, ( Copy )  - 800)
        elif  ( Copy > 900 )  and  ( Copy <= 1000 ) :
            ReturnVal = GetString(IACred.Code, ( Copy )  - 900)
        elif  ( Copy > 1000 )  and  ( Copy <= 1100 ) :
            ReturnVal = GetString(IACred.Code, ( Copy )  - 1000)
        elif  ( Copy > 1100 )  and  ( Copy <= 1200 ) :
            ReturnVal = GetString(IACred.Code, ( Copy )  - 1100)
        elif  ( Copy > 1200 )  and  ( Copy <= 1300 ) :
            ReturnVal = GetString(IACred.Code, ( Copy )  - 1200)
        elif  ( Copy > 1300 )  and  ( Copy <= 1400 ) :
            ReturnVal = GetString(IACred.Code, ( Copy )  - 1300)
        elif  ( Copy > 1400 )  and  ( Copy <= 1500 ) :
            ReturnVal = GetString(IACred.Code, ( Copy )  - 1400)
        elif  ( Copy > 1500 )  and  ( Copy <= 1600 ) :
            ReturnVal = GetString(IACred.Code, ( Copy )  - 1500)
        elif  ( Copy > 1600 )  and  ( Copy <= 1700 ) :
            ReturnVal = GetString(IACred.Code, ( Copy )  - 1600)
        elif  ( Copy > 1700 )  and  ( Copy <= 1800 ) :
            ReturnVal = GetString(IACred.Code, ( Copy )  - 1700)
        elif  ( Copy > 1800 )  and  ( Copy <= 1900 ) :
            ReturnVal = GetString(IACred.Code, ( Copy )  - 1800)
        elif  ( Copy > 1900 )  and  ( Copy <= 2000 ) :
            ReturnVal = GetString(IACred.Code, ( Copy )  - 1900)
        elif  ( Copy > 2000 )  and  ( Copy <= 2100 ) :
            ReturnVal = GetString(IACred.Code, ( Copy )  - 2000)
        elif  ( Copy > 2100 )  and  ( Copy <= 2200 ) :
            ReturnVal = GetString(IACred.Code, ( Copy )  - 2100)
        elif  ( Copy > 2200 )  and  ( Copy <= 2300 ) :
            ReturnVal = GetString(IACred.Code, ( Copy )  - 2200)
        elif  ( Copy > 2300 )  and  ( Copy <= 2400 ) :
            ReturnVal = GetString(IACred.Code, ( Copy )  - 2300)
        elif  ( Copy > 2400 )  and  ( Copy <= 2500 ) :
            ReturnVal = '09'
    ReturnVal = ''

def PTEEIN_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    if GetNumber(IA148Sp.NonRefNbr) > 10 and Index > 9:
        strindex = ( ( Index - 1 )  * 4 )  + 1
    else:
        strindex = ( ( Index )  * 4 )  + 1
    copystr = Trim(Mid(GetString(IA148Sp.NonRefCopiesStr), strindex, 4))
    if Index == 9 and GetNumber(IA148Sp.NonRefNbr) > 10:
        ReturnVal = ''
    elif copystr != '':
        Copy = CLng(copystr)
        if ( Copy > 100 )  and  ( Copy <= 200 ) :
            ReturnVal = ''
        elif  ( Copy > 200 )  and  ( Copy <= 300 ) :
            ReturnVal = GetString(IA134.SCorpEIN, ( Copy )  - 200)
        elif  ( Copy > 300 )  and  ( Copy <= 400 ) :
            ReturnVal = GetString(IACred.PTEEIN, ( Copy )  - 300)
        elif  ( Copy > 400 )  and  ( Copy <= 500 ) :
            ReturnVal = GetString(IACred.PTEEIN, ( Copy )  - 400)
        elif  ( Copy > 500 )  and  ( Copy <= 600 ) :
            ReturnVal = GetString(IACred.PTEEIN, ( Copy )  - 500)
        elif  ( Copy > 600 )  and  ( Copy <= 700 ) :
            ReturnVal = GetString(IACred.PTEEIN, ( Copy )  - 600)
        elif  ( Copy > 700 )  and  ( Copy <= 800 ) :
            ReturnVal = GetString(IACred.PTEEIN, ( Copy )  - 700)
        elif  ( Copy > 800 )  and  ( Copy <= 900 ) :
            ReturnVal = GetString(IACred.PTEEIN, ( Copy )  - 800)
        elif  ( Copy > 900 )  and  ( Copy <= 1000 ) :
            ReturnVal = GetString(IACred.PTEEIN, ( Copy )  - 900)
        elif  ( Copy > 1000 )  and  ( Copy <= 1100 ) :
            ReturnVal = GetString(IACred.PTEEIN, ( Copy )  - 1000)
        elif  ( Copy > 1100 )  and  ( Copy <= 1200 ) :
            ReturnVal = GetString(IACred.PTEEIN, ( Copy )  - 1100)
        elif  ( Copy > 1200 )  and  ( Copy <= 1300 ) :
            ReturnVal = GetString(IACred.PTEEIN, ( Copy )  - 1200)
        elif  ( Copy > 1300 )  and  ( Copy <= 1400 ) :
            ReturnVal = GetString(IACred.PTEEIN, ( Copy )  - 1300)
        elif  ( Copy > 1400 )  and  ( Copy <= 1500 ) :
            ReturnVal = GetString(IACred.PTEEIN, ( Copy )  - 1400)
        elif  ( Copy > 1500 )  and  ( Copy <= 1600 ) :
            ReturnVal = GetString(IACred.PTEEIN, ( Copy )  - 1500)
        elif  ( Copy > 1600 )  and  ( Copy <= 1700 ) :
            ReturnVal = GetString(IACred.PTEEIN, ( Copy )  - 1600)
        elif  ( Copy > 1700 )  and  ( Copy <= 1800 ) :
            ReturnVal = GetString(IACred.PTEEIN, ( Copy )  - 1700)
        elif  ( Copy > 1800 )  and  ( Copy <= 1900 ) :
            ReturnVal = GetString(IACred.PTEEIN, ( Copy )  - 1800)
        elif  ( Copy > 1900 )  and  ( Copy <= 2000 ) :
            ReturnVal = GetString(IACred.PTEEIN, ( Copy )  - 1900)
        elif  ( Copy > 2000 )  and  ( Copy <= 2100 ) :
            ReturnVal = GetString(IACred.PTEEIN, ( Copy )  - 2000)
        elif  ( Copy > 2100 )  and  ( Copy <= 2200 ) :
            ReturnVal = GetString(IACred.PTEEIN, ( Copy )  - 2100)
        elif  ( Copy > 2200 )  and  ( Copy <= 2300 ) :
            ReturnVal = GetString(IACred.PTEEIN, ( Copy )  - 2200)
        elif  ( Copy > 2300 )  and  ( Copy <= 2400 ) :
            ReturnVal = GetString(IACred.PTEEIN, ( Copy )  - 2300)
        elif  ( Copy > 2400 )  and  ( Copy <= 2500 ) :
            ReturnVal = ''
    ReturnVal = ''

def PTEIndexNbr_Calculation(Index):
    count = Long()

    max = Long()

    listedcount = Long()
    listedcount = 0
    count = 0
    while count < 98:
        if Trim(GetString(IA148BumpSp.PTEName(count))) != '':
            if listedcount == Index:
                ReturnVal = count
            else:
                listedcount = listedcount + 1
        count = count + 1
    ReturnVal = 0

def PTELine_Calculation(Index):
    Hold = Long()
    Hold = Index + 1
    if Index > 9:
        ReturnVal = 'Attached stmt'
    else:
        ReturnVal = CStr(Hold)

def PTEName_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    if GetNumber(IA148Sp.NonRefNbr) > 10 and Index > 9:
        strindex = ( ( Index - 1 )  * 4 )  + 1
    else:
        strindex = ( ( Index )  * 4 )  + 1
    copystr = Trim(Mid(GetString(IA148Sp.NonRefCopiesStr), strindex, 4))
    if Index == 9 and GetNumber(IA148Sp.NonRefNbr) > 10:
        ReturnVal = ''
    elif copystr != '':
        Copy = CLng(copystr)
        if ( Copy > 100 )  and  ( Copy <= 200 ) :
            ReturnVal = ''
        elif  ( Copy > 200 )  and  ( Copy <= 300 ) :
            ReturnVal = GetString(IA134.SCorpName, ( Copy )  - 200)
        elif  ( Copy > 300 )  and  ( Copy <= 400 ) :
            ReturnVal = GetString(IACred.PTEEntity, ( Copy )  - 300)
        elif  ( Copy > 400 )  and  ( Copy <= 500 ) :
            ReturnVal = GetString(IACred.PTEEntity, ( Copy )  - 400)
        elif  ( Copy > 500 )  and  ( Copy <= 600 ) :
            ReturnVal = GetString(IACred.PTEEntity, ( Copy )  - 500)
        elif  ( Copy > 600 )  and  ( Copy <= 700 ) :
            ReturnVal = GetString(IACred.PTEEntity, ( Copy )  - 600)
        elif  ( Copy > 700 )  and  ( Copy <= 800 ) :
            ReturnVal = GetString(IACred.PTEEntity, ( Copy )  - 700)
        elif  ( Copy > 800 )  and  ( Copy <= 900 ) :
            ReturnVal = GetString(IACred.PTEEntity, ( Copy )  - 800)
        elif  ( Copy > 900 )  and  ( Copy <= 1000 ) :
            ReturnVal = GetString(IACred.PTEEntity, ( Copy )  - 900)
        elif  ( Copy > 1000 )  and  ( Copy <= 1100 ) :
            ReturnVal = GetString(IACred.PTEEntity, ( Copy )  - 1000)
        elif  ( Copy > 1100 )  and  ( Copy <= 1200 ) :
            ReturnVal = GetString(IACred.PTEEntity, ( Copy )  - 1100)
        elif  ( Copy > 1200 )  and  ( Copy <= 1300 ) :
            ReturnVal = GetString(IACred.PTEEntity, ( Copy )  - 1200)
        elif  ( Copy > 1300 )  and  ( Copy <= 1400 ) :
            ReturnVal = GetString(IACred.PTEEntity, ( Copy )  - 1300)
        elif  ( Copy > 1400 )  and  ( Copy <= 1500 ) :
            ReturnVal = GetString(IACred.PTEEntity, ( Copy )  - 1400)
        elif  ( Copy > 1500 )  and  ( Copy <= 1600 ) :
            ReturnVal = GetString(IACred.PTEEntity, ( Copy )  - 1500)
        elif  ( Copy > 1600 )  and  ( Copy <= 1700 ) :
            ReturnVal = GetString(IACred.PTEEntity, ( Copy )  - 1600)
        elif  ( Copy > 1700 )  and  ( Copy <= 1800 ) :
            ReturnVal = GetString(IACred.PTEEntity, ( Copy )  - 1700)
        elif  ( Copy > 1800 )  and  ( Copy <= 1900 ) :
            ReturnVal = GetString(IACred.PTEEntity, ( Copy )  - 1800)
        elif  ( Copy > 1900 )  and  ( Copy <= 2000 ) :
            ReturnVal = GetString(IACred.PTEEntity, ( Copy )  - 1900)
        elif  ( Copy > 2000 )  and  ( Copy <= 2100 ) :
            ReturnVal = GetString(IACred.PTEEntity, ( Copy )  - 2000)
        elif  ( Copy > 2100 )  and  ( Copy <= 2200 ) :
            ReturnVal = GetString(IACred.PTEEntity, ( Copy )  - 2100)
        elif  ( Copy > 2200 )  and  ( Copy <= 2300 ) :
            ReturnVal = GetString(IACred.PTEEntity, ( Copy )  - 2200)
        elif  ( Copy > 2300 )  and  ( Copy <= 2400 ) :
            ReturnVal = GetString(IACred.PTEEntity, ( Copy )  - 2300)
        elif  ( Copy > 2400 )  and  ( Copy <= 2500 ) :
            ReturnVal = ''
    ReturnVal = ''

def PTENRTrig_Calculation(Index):
    if GetString(IA148BumpSp.PTECode(Index)) == '04' or GetString(IA148BumpSp.PTECode(Index)) == '11' or GetString(IA148BumpSp.PTECode(Index)) == '09':
        ReturnVal = 0
    elif Trim(GetString(IA148BumpSp.PTEName(Index))) != '':
        ReturnVal = 1
    else:
        ReturnVal = 0

def PTERefTrig_Calculation(Index):
    if GetString(IA148BumpSp.RefPTECode(Index)) == '64' or GetString(IA148BumpSp.RefPTECode(Index)) == '58' or GetString(IA148BumpSp.RefPTECode(Index)) == '55' or GetString(IA148BumpSp.RefPTECode(Index)) == '52' or GetString(IA148BumpSp.RefPTECode(Index)) == '59' or GetString(IA148BumpSp.RefPTECode(Index)) == '65' or GetString(IA148BumpSp.RefPTECode(Index)) == '66':
        ReturnVal = 0
    elif Trim(GetString(IA148BumpSp.RefPTEName(Index))) != '':
        ReturnVal = 1
    else:
        ReturnVal = 0

def RefPTECode_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    if GetNumber(IA148Sp.NonRefNbr) > 10 and Index > 9:
        strindex = ( ( Index - 1 )  * 4 )  + 1
    else:
        strindex = ( ( Index )  * 4 )  + 1
    copystr = Trim(Mid(GetString(IA148Sp.RefCopiesStr), strindex, 4))
    if Index == 6 and GetNumber(IA148Sp.RefNbr) > 7:
        ReturnVal = 'See Statement Attached'
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

def RefPTEEIN_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    if GetNumber(IA148Sp.NonRefNbr) > 10 and Index > 9:
        strindex = ( ( Index - 1 )  * 4 )  + 1
    else:
        strindex = ( ( Index )  * 4 )  + 1
    copystr = Trim(Mid(GetString(IA148Sp.RefCopiesStr), strindex, 4))
    if Index == 6 and GetNumber(IA148Sp.RefNbr) > 7:
        ReturnVal = ''
    elif copystr != '':
        Copy = CLng(copystr)
        if ( Copy > 100 )  and  ( Copy <= 200 ) :
            ReturnVal = GetString(IA8864.PTEEIN(0), ( Copy )  - 100)
        elif  ( Copy > 200 )  and  ( Copy <= 300 ) :
            ReturnVal = GetString(IACred.PTEEIN, ( Copy )  - 200)
        elif  ( Copy > 300 )  and  ( Copy <= 400 ) :
            ReturnVal = GetString(IA135.PTEEIN(0), ( Copy )  - 300)
        elif  ( Copy > 400 )  and  ( Copy <= 500 ) :
            ReturnVal = GetString(IACred.PTEEIN, ( Copy )  - 400)
        elif  ( Copy > 500 )  and  ( Copy <= 600 ) :
            ReturnVal = GetString(IA128.PTEEIN(0), ( Copy )  - 500)
        elif  ( Copy > 600 )  and  ( Copy <= 700 ) :
            ReturnVal = GetString(IA128S.PTEEIN(0), ( Copy )  - 600)
        elif  ( Copy > 700 )  and  ( Copy <= 800 ) :
            ReturnVal = GetString(IA128.PTEEIN(0), ( Copy )  - 700)
        elif  ( Copy > 800 )  and  ( Copy <= 900 ) :
            ReturnVal = GetString(IA128S.PTEEIN(0), ( Copy )  - 800)
        elif  ( Copy > 900 )  and  ( Copy <= 1000 ) :
            ReturnVal = GetString(IA137.PTEEIN(0), ( Copy )  - 900)
        elif  ( Copy > 1000 )  and  ( Copy <= 1100 ) :
            ReturnVal = GetString(IA138.PTEEIN(0), ( Copy )  - 1000)
        elif  ( Copy > 1100 )  and  ( Copy <= 1200 ) :
            ReturnVal = ''
        elif  ( Copy > 1200 )  and  ( Copy <= 1300 ) :
            ReturnVal = GetString(IACred.PTEEIN, ( Copy )  - 1200)
        elif  ( Copy > 1300 )  and  ( Copy <= 1400 ) :
            ReturnVal = GetString(IACred.PTEEIN, ( Copy )  - 1300)
        elif  ( Copy > 1400 )  and  ( Copy <= 1500 ) :
            ReturnVal = GetString(IACred.PTEEIN, ( Copy )  - 1400)
    ReturnVal = ''

def RefPTEIndexNbr_Calculation(Index):
    count = Long()

    max = Long()

    listedcount = Long()
    listedcount = 0
    count = 0
    while count < 69:
        if Trim(GetString(IA148BumpSp.RefPTEName(count))) != '':
            if listedcount == Index:
                ReturnVal = count
            else:
                listedcount = listedcount + 1
        count = count + 1
    ReturnVal = 0

def RefPTELine_Calculation(Index):
    Hold = Long()
    Hold = Index + 11
    if Index > 9:
        ReturnVal = 'Attached stmt'
    else:
        ReturnVal = CStr(Hold)

def RefPTEName_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    if GetNumber(IA148Sp.NonRefNbr) > 10 and Index > 9:
        strindex = ( ( Index - 1 )  * 4 )  + 1
    else:
        strindex = ( ( Index )  * 4 )  + 1
    copystr = Trim(Mid(GetString(IA148Sp.RefCopiesStr), strindex, 4))
    if Index == 6 and GetNumber(IA148Sp.RefNbr) > 7:
        ReturnVal = ''
    elif copystr != '':
        Copy = CLng(copystr)
        if ( Copy > 100 )  and  ( Copy <= 200 ) :
            ReturnVal = GetString(IA8864.PTEEntity(0), ( Copy )  - 100)
        elif  ( Copy > 200 )  and  ( Copy <= 300 ) :
            ReturnVal = GetString(IACred.PTEEntity, ( Copy )  - 200)
        elif  ( Copy > 300 )  and  ( Copy <= 400 ) :
            ReturnVal = GetString(IA135.PTEEntity(0), ( Copy )  - 300)
        elif  ( Copy > 400 )  and  ( Copy <= 500 ) :
            ReturnVal = GetString(IACred.PTEEntity, ( Copy )  - 400)
        elif  ( Copy > 500 )  and  ( Copy <= 600 ) :
            ReturnVal = GetString(IA128.PTEEntity(0), ( Copy )  - 500)
        elif  ( Copy > 600 )  and  ( Copy <= 700 ) :
            ReturnVal = GetString(IA128S.PTEEntity(0), ( Copy )  - 600)
        elif  ( Copy > 700 )  and  ( Copy <= 800 ) :
            ReturnVal = GetString(IA128.PTEEntity(0), ( Copy )  - 700)
        elif  ( Copy > 800 )  and  ( Copy <= 900 ) :
            ReturnVal = GetString(IA128S.PTEEntity(0), ( Copy )  - 800)
        elif  ( Copy > 900 )  and  ( Copy <= 1000 ) :
            ReturnVal = GetString(IA137.PTEEntity(0), ( Copy )  - 900)
        elif  ( Copy > 1000 )  and  ( Copy <= 1100 ) :
            ReturnVal = GetString(IA138.PTEEntity(0), ( Copy )  - 1000)
        elif  ( Copy > 1100 )  and  ( Copy <= 1200 ) :
            ReturnVal = ''
        elif  ( Copy > 1200 )  and  ( Copy <= 1300 ) :
            ReturnVal = GetString(IACred.PTEEntity, ( Copy )  - 1200)
        elif  ( Copy > 1300 )  and  ( Copy <= 1400 ) :
            ReturnVal = GetString(IACred.PTEEntity, ( Copy )  - 1300)
        elif  ( Copy > 1400 )  and  ( Copy <= 1500 ) :
            ReturnVal = GetString(IACred.PTEEntity, ( Copy )  - 1400)
    ReturnVal = ''

def RefTPPerc_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    if GetNumber(IA148Sp.NonRefNbr) > 10 and Index > 9:
        strindex = ( ( Index - 1 )  * 4 )  + 1
    else:
        strindex = ( ( Index )  * 4 )  + 1
    copystr = Trim(Mid(GetString(IA148Sp.RefCopiesStr), strindex, 4))
    if Index == 6 and GetNumber(IA148Sp.RefNbr) > 7:
        ReturnVal = 0
    elif copystr != '':
        Copy = CLng(copystr)
        if ( Copy > 100 )  and  ( Copy <= 200 ) :
            ReturnVal = GetFloat(IA8864.TPPerc(0), ( Copy )  - 100)
        elif  ( Copy > 200 )  and  ( Copy <= 300 ) :
            ReturnVal = GetFloat(IACred.TPPerc, ( Copy )  - 200)
        elif  ( Copy > 300 )  and  ( Copy <= 400 ) :
            ReturnVal = GetFloat(IA135.TPPerc(0), ( Copy )  - 300)
        elif  ( Copy > 400 )  and  ( Copy <= 500 ) :
            ReturnVal = GetFloat(IACred.TPPerc, ( Copy )  - 400)
        elif  ( Copy > 500 )  and  ( Copy <= 600 ) :
            ReturnVal = GetFloat(IA128.TPPerc(0), ( Copy )  - 500)
        elif  ( Copy > 600 )  and  ( Copy <= 700 ) :
            ReturnVal = GetFloat(IA128S.TPPerc(0), ( Copy )  - 600)
        elif  ( Copy > 700 )  and  ( Copy <= 800 ) :
            ReturnVal = GetFloat(IA128.TPPerc(0), ( Copy )  - 700)
        elif  ( Copy > 800 )  and  ( Copy <= 900 ) :
            ReturnVal = GetFloat(IA128S.TPPerc(0), ( Copy )  - 800)
        elif  ( Copy > 900 )  and  ( Copy <= 1000 ) :
            ReturnVal = GetFloat(IA137.TPPerc(0), ( Copy )  - 900)
        elif  ( Copy > 1000 )  and  ( Copy <= 1100 ) :
            ReturnVal = GetFloat(IA138.TPPerc(0), ( Copy )  - 1000)
        elif  ( Copy > 1100 )  and  ( Copy <= 1200 ) :
            ReturnVal = 0
        elif  ( Copy > 1200 )  and  ( Copy <= 1300 ) :
            ReturnVal = GetFloat(IACred.TPPerc, ( Copy )  - 1200)
        elif  ( Copy > 1300 )  and  ( Copy <= 1400 ) :
            ReturnVal = GetFloat(IACred.TPPerc, ( Copy )  - 1300)
        elif  ( Copy > 1400 )  and  ( Copy <= 1500 ) :
            ReturnVal = GetFloat(IACred.TPPerc, ( Copy )  - 1400)
    ReturnVal = 0

def TotPTE_Calculation():
    count = Integer()

    Total = Integer()
    count = 0
    Total = 0
    while count < 98:
        if Trim(GetString(IA148BumpSp.PTEName(count))) != '':
            Total = Total + 1
        else:
            Total = Total
        count = count + 1
    ReturnVal = Total

def TotRefPTE_Calculation():
    count = Integer()

    Total = Integer()
    count = 0
    Total = 0
    while count < 69:
        if Trim(GetString(IA148BumpSp.RefPTEName(count))) != '':
            Total = Total + 1
        else:
            Total = Total
        count = count + 1
    ReturnVal = Total

def TPPerc_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    if GetNumber(IA148Sp.NonRefNbr) > 10 and Index > 9:
        strindex = ( ( Index - 1 )  * 4 )  + 1
    else:
        strindex = ( ( Index )  * 4 )  + 1
    copystr = Trim(Mid(GetString(IA148Sp.NonRefCopiesStr), strindex, 4))
    if Index == 9 and GetNumber(IA148Sp.NonRefNbr) > 10:
        ReturnVal = 0
    elif copystr != '':
        Copy = CLng(copystr)
        if ( Copy > 100 )  and  ( Copy <= 200 ) :
            ReturnVal = 0
        elif  ( Copy > 200 )  and  ( Copy <= 300 ) :
            ReturnVal = GetFloat(IA134.SCorpPerc, ( Copy )  - 200)
        elif  ( Copy > 300 )  and  ( Copy <= 400 ) :
            ReturnVal = GetFloat(IACred.TPPerc, ( Copy )  - 300)
        elif  ( Copy > 400 )  and  ( Copy <= 500 ) :
            ReturnVal = GetFloat(IACred.TPPerc, ( Copy )  - 400)
        elif  ( Copy > 500 )  and  ( Copy <= 600 ) :
            ReturnVal = GetFloat(IACred.TPPerc, ( Copy )  - 500)
        elif  ( Copy > 600 )  and  ( Copy <= 700 ) :
            ReturnVal = GetFloat(IACred.TPPerc, ( Copy )  - 600)
        elif  ( Copy > 700 )  and  ( Copy <= 800 ) :
            ReturnVal = GetFloat(IACred.TPPerc, ( Copy )  - 700)
        elif  ( Copy > 800 )  and  ( Copy <= 900 ) :
            ReturnVal = GetFloat(IACred.TPPerc, ( Copy )  - 800)
        elif  ( Copy > 900 )  and  ( Copy <= 1000 ) :
            ReturnVal = GetFloat(IACred.TPPerc, ( Copy )  - 900)
        elif  ( Copy > 1000 )  and  ( Copy <= 1100 ) :
            ReturnVal = GetFloat(IACred.TPPerc, ( Copy )  - 1000)
        elif  ( Copy > 1100 )  and  ( Copy <= 1200 ) :
            ReturnVal = GetFloat(IACred.TPPerc, ( Copy )  - 1100)
        elif  ( Copy > 1200 )  and  ( Copy <= 1300 ) :
            ReturnVal = GetFloat(IACred.TPPerc, ( Copy )  - 1200)
        elif  ( Copy > 1300 )  and  ( Copy <= 1400 ) :
            ReturnVal = GetFloat(IACred.TPPerc, ( Copy )  - 1300)
        elif  ( Copy > 1400 )  and  ( Copy <= 1500 ) :
            ReturnVal = GetFloat(IACred.TPPerc, ( Copy )  - 1400)
        elif  ( Copy > 1500 )  and  ( Copy <= 1600 ) :
            ReturnVal = GetFloat(IACred.TPPerc, ( Copy )  - 1500)
        elif  ( Copy > 1600 )  and  ( Copy <= 1700 ) :
            ReturnVal = GetFloat(IACred.TPPerc, ( Copy )  - 1600)
        elif  ( Copy > 1700 )  and  ( Copy <= 1800 ) :
            ReturnVal = GetFloat(IACred.TPPerc, ( Copy )  - 1700)
        elif  ( Copy > 1800 )  and  ( Copy <= 1900 ) :
            ReturnVal = GetFloat(IACred.TPPerc, ( Copy )  - 1800)
        elif  ( Copy > 1900 )  and  ( Copy <= 2000 ) :
            ReturnVal = GetFloat(IACred.TPPerc, ( Copy )  - 1900)
        elif  ( Copy > 2000 )  and  ( Copy <= 2100 ) :
            ReturnVal = GetFloat(IACred.TPPerc, ( Copy )  - 2000)
        elif  ( Copy > 2100 )  and  ( Copy <= 2200 ) :
            ReturnVal = GetFloat(IACred.TPPerc, ( Copy )  - 2100)
        elif  ( Copy > 2200 )  and  ( Copy <= 2300 ) :
            ReturnVal = GetFloat(IACred.TPPerc, ( Copy )  - 2200)
        elif  ( Copy > 2300 )  and  ( Copy <= 2400 ) :
            ReturnVal = GetFloat(IACred.TPPerc, ( Copy )  - 2300)
        elif  ( Copy > 2400 )  and  ( Copy <= 2500 ) :
            ReturnVal = 0
    ReturnVal = 0

