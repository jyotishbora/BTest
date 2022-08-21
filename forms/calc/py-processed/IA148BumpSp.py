from forms.out import IA137
from forms.out import IA148BUMPSP
from forms.out import IA148SP
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def PTECode_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    if get_number(IA148SP.NonRefNbr) > 10 and Index > 9:
        strindex = ( ( Index - 1 )  * 4 )  + 1
    else:
        strindex = ( ( Index )  * 4 )  + 1
    copystr = trim(Mid(get_string(IA148SP.NonRefCopiesStr), strindex, 4))
    if Index == 9 and get_number(IA148SP.NonRefNbr) > 10:
        return 'Stmt'
    elif copystr != '':
        Copy = CLng(copystr)
        if ( Copy > 100 )  and  ( Copy <= 200 ) :
            return '04'
        elif  ( Copy > 200 )  and  ( Copy <= 300 ) :
            return '11'
        elif  ( Copy > 300 )  and  ( Copy <= 400 ) :
            return get_string(IACred.Code, ( Copy )  - 300)
        elif  ( Copy > 400 )  and  ( Copy <= 500 ) :
            return get_string(IACred.Code, ( Copy )  - 400)
        elif  ( Copy > 500 )  and  ( Copy <= 600 ) :
            return get_string(IACred.Code, ( Copy )  - 500)
        elif  ( Copy > 600 )  and  ( Copy <= 700 ) :
            return get_string(IACred.Code, ( Copy )  - 600)
        elif  ( Copy > 700 )  and  ( Copy <= 800 ) :
            return get_string(IACred.Code, ( Copy )  - 700)
        elif  ( Copy > 800 )  and  ( Copy <= 900 ) :
            return get_string(IACred.Code, ( Copy )  - 800)
        elif  ( Copy > 900 )  and  ( Copy <= 1000 ) :
            return get_string(IACred.Code, ( Copy )  - 900)
        elif  ( Copy > 1000 )  and  ( Copy <= 1100 ) :
            return get_string(IACred.Code, ( Copy )  - 1000)
        elif  ( Copy > 1100 )  and  ( Copy <= 1200 ) :
            return get_string(IACred.Code, ( Copy )  - 1100)
        elif  ( Copy > 1200 )  and  ( Copy <= 1300 ) :
            return get_string(IACred.Code, ( Copy )  - 1200)
        elif  ( Copy > 1300 )  and  ( Copy <= 1400 ) :
            return get_string(IACred.Code, ( Copy )  - 1300)
        elif  ( Copy > 1400 )  and  ( Copy <= 1500 ) :
            return get_string(IACred.Code, ( Copy )  - 1400)
        elif  ( Copy > 1500 )  and  ( Copy <= 1600 ) :
            return get_string(IACred.Code, ( Copy )  - 1500)
        elif  ( Copy > 1600 )  and  ( Copy <= 1700 ) :
            return get_string(IACred.Code, ( Copy )  - 1600)
        elif  ( Copy > 1700 )  and  ( Copy <= 1800 ) :
            return get_string(IACred.Code, ( Copy )  - 1700)
        elif  ( Copy > 1800 )  and  ( Copy <= 1900 ) :
            return get_string(IACred.Code, ( Copy )  - 1800)
        elif  ( Copy > 1900 )  and  ( Copy <= 2000 ) :
            return get_string(IACred.Code, ( Copy )  - 1900)
        elif  ( Copy > 2000 )  and  ( Copy <= 2100 ) :
            return get_string(IACred.Code, ( Copy )  - 2000)
        elif  ( Copy > 2100 )  and  ( Copy <= 2200 ) :
            return get_string(IACred.Code, ( Copy )  - 2100)
        elif  ( Copy > 2200 )  and  ( Copy <= 2300 ) :
            return get_string(IACred.Code, ( Copy )  - 2200)
        elif  ( Copy > 2300 )  and  ( Copy <= 2400 ) :
            return get_string(IACred.Code, ( Copy )  - 2300)
        elif  ( Copy > 2400 )  and  ( Copy <= 2500 ) :
            return '09'
    return ''

def PTEEIN_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    if get_number(IA148SP.NonRefNbr) > 10 and Index > 9:
        strindex = ( ( Index - 1 )  * 4 )  + 1
    else:
        strindex = ( ( Index )  * 4 )  + 1
    copystr = trim(Mid(get_string(IA148SP.NonRefCopiesStr), strindex, 4))
    if Index == 9 and get_number(IA148SP.NonRefNbr) > 10:
        return ''
    elif copystr != '':
        Copy = CLng(copystr)
        if ( Copy > 100 )  and  ( Copy <= 200 ) :
            return ''
        elif  ( Copy > 200 )  and  ( Copy <= 300 ) :
            return get_string(IA134.SCorpEIN, ( Copy )  - 200)
        elif  ( Copy > 300 )  and  ( Copy <= 400 ) :
            return get_string(IACred.PTEEIN, ( Copy )  - 300)
        elif  ( Copy > 400 )  and  ( Copy <= 500 ) :
            return get_string(IACred.PTEEIN, ( Copy )  - 400)
        elif  ( Copy > 500 )  and  ( Copy <= 600 ) :
            return get_string(IACred.PTEEIN, ( Copy )  - 500)
        elif  ( Copy > 600 )  and  ( Copy <= 700 ) :
            return get_string(IACred.PTEEIN, ( Copy )  - 600)
        elif  ( Copy > 700 )  and  ( Copy <= 800 ) :
            return get_string(IACred.PTEEIN, ( Copy )  - 700)
        elif  ( Copy > 800 )  and  ( Copy <= 900 ) :
            return get_string(IACred.PTEEIN, ( Copy )  - 800)
        elif  ( Copy > 900 )  and  ( Copy <= 1000 ) :
            return get_string(IACred.PTEEIN, ( Copy )  - 900)
        elif  ( Copy > 1000 )  and  ( Copy <= 1100 ) :
            return get_string(IACred.PTEEIN, ( Copy )  - 1000)
        elif  ( Copy > 1100 )  and  ( Copy <= 1200 ) :
            return get_string(IACred.PTEEIN, ( Copy )  - 1100)
        elif  ( Copy > 1200 )  and  ( Copy <= 1300 ) :
            return get_string(IACred.PTEEIN, ( Copy )  - 1200)
        elif  ( Copy > 1300 )  and  ( Copy <= 1400 ) :
            return get_string(IACred.PTEEIN, ( Copy )  - 1300)
        elif  ( Copy > 1400 )  and  ( Copy <= 1500 ) :
            return get_string(IACred.PTEEIN, ( Copy )  - 1400)
        elif  ( Copy > 1500 )  and  ( Copy <= 1600 ) :
            return get_string(IACred.PTEEIN, ( Copy )  - 1500)
        elif  ( Copy > 1600 )  and  ( Copy <= 1700 ) :
            return get_string(IACred.PTEEIN, ( Copy )  - 1600)
        elif  ( Copy > 1700 )  and  ( Copy <= 1800 ) :
            return get_string(IACred.PTEEIN, ( Copy )  - 1700)
        elif  ( Copy > 1800 )  and  ( Copy <= 1900 ) :
            return get_string(IACred.PTEEIN, ( Copy )  - 1800)
        elif  ( Copy > 1900 )  and  ( Copy <= 2000 ) :
            return get_string(IACred.PTEEIN, ( Copy )  - 1900)
        elif  ( Copy > 2000 )  and  ( Copy <= 2100 ) :
            return get_string(IACred.PTEEIN, ( Copy )  - 2000)
        elif  ( Copy > 2100 )  and  ( Copy <= 2200 ) :
            return get_string(IACred.PTEEIN, ( Copy )  - 2100)
        elif  ( Copy > 2200 )  and  ( Copy <= 2300 ) :
            return get_string(IACred.PTEEIN, ( Copy )  - 2200)
        elif  ( Copy > 2300 )  and  ( Copy <= 2400 ) :
            return get_string(IACred.PTEEIN, ( Copy )  - 2300)
        elif  ( Copy > 2400 )  and  ( Copy <= 2500 ) :
            return ''
    return ''

def PTEIndexNbr_Calculation(Index):
    count = Long()

    max = Long()

    listedcount = Long()
    listedcount = 0
    count = 0
    while count < 98:
        if trim(get_string(IA148BUMPSP.PTEName(count))) != '':
            if listedcount == Index:
                return count
            else:
                listedcount = listedcount + 1
        count = count + 1
    return 0

def PTELine_Calculation(Index):
    Hold = Long()
    Hold = Index + 1
    if Index > 9:
        return 'Attached stmt'
    else:
        return CStr(Hold)

def PTEName_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    if get_number(IA148SP.NonRefNbr) > 10 and Index > 9:
        strindex = ( ( Index - 1 )  * 4 )  + 1
    else:
        strindex = ( ( Index )  * 4 )  + 1
    copystr = trim(Mid(get_string(IA148SP.NonRefCopiesStr), strindex, 4))
    if Index == 9 and get_number(IA148SP.NonRefNbr) > 10:
        return ''
    elif copystr != '':
        Copy = CLng(copystr)
        if ( Copy > 100 )  and  ( Copy <= 200 ) :
            return ''
        elif  ( Copy > 200 )  and  ( Copy <= 300 ) :
            return get_string(IA134.SCorpName, ( Copy )  - 200)
        elif  ( Copy > 300 )  and  ( Copy <= 400 ) :
            return get_string(IACred.PTEEntity, ( Copy )  - 300)
        elif  ( Copy > 400 )  and  ( Copy <= 500 ) :
            return get_string(IACred.PTEEntity, ( Copy )  - 400)
        elif  ( Copy > 500 )  and  ( Copy <= 600 ) :
            return get_string(IACred.PTEEntity, ( Copy )  - 500)
        elif  ( Copy > 600 )  and  ( Copy <= 700 ) :
            return get_string(IACred.PTEEntity, ( Copy )  - 600)
        elif  ( Copy > 700 )  and  ( Copy <= 800 ) :
            return get_string(IACred.PTEEntity, ( Copy )  - 700)
        elif  ( Copy > 800 )  and  ( Copy <= 900 ) :
            return get_string(IACred.PTEEntity, ( Copy )  - 800)
        elif  ( Copy > 900 )  and  ( Copy <= 1000 ) :
            return get_string(IACred.PTEEntity, ( Copy )  - 900)
        elif  ( Copy > 1000 )  and  ( Copy <= 1100 ) :
            return get_string(IACred.PTEEntity, ( Copy )  - 1000)
        elif  ( Copy > 1100 )  and  ( Copy <= 1200 ) :
            return get_string(IACred.PTEEntity, ( Copy )  - 1100)
        elif  ( Copy > 1200 )  and  ( Copy <= 1300 ) :
            return get_string(IACred.PTEEntity, ( Copy )  - 1200)
        elif  ( Copy > 1300 )  and  ( Copy <= 1400 ) :
            return get_string(IACred.PTEEntity, ( Copy )  - 1300)
        elif  ( Copy > 1400 )  and  ( Copy <= 1500 ) :
            return get_string(IACred.PTEEntity, ( Copy )  - 1400)
        elif  ( Copy > 1500 )  and  ( Copy <= 1600 ) :
            return get_string(IACred.PTEEntity, ( Copy )  - 1500)
        elif  ( Copy > 1600 )  and  ( Copy <= 1700 ) :
            return get_string(IACred.PTEEntity, ( Copy )  - 1600)
        elif  ( Copy > 1700 )  and  ( Copy <= 1800 ) :
            return get_string(IACred.PTEEntity, ( Copy )  - 1700)
        elif  ( Copy > 1800 )  and  ( Copy <= 1900 ) :
            return get_string(IACred.PTEEntity, ( Copy )  - 1800)
        elif  ( Copy > 1900 )  and  ( Copy <= 2000 ) :
            return get_string(IACred.PTEEntity, ( Copy )  - 1900)
        elif  ( Copy > 2000 )  and  ( Copy <= 2100 ) :
            return get_string(IACred.PTEEntity, ( Copy )  - 2000)
        elif  ( Copy > 2100 )  and  ( Copy <= 2200 ) :
            return get_string(IACred.PTEEntity, ( Copy )  - 2100)
        elif  ( Copy > 2200 )  and  ( Copy <= 2300 ) :
            return get_string(IACred.PTEEntity, ( Copy )  - 2200)
        elif  ( Copy > 2300 )  and  ( Copy <= 2400 ) :
            return get_string(IACred.PTEEntity, ( Copy )  - 2300)
        elif  ( Copy > 2400 )  and  ( Copy <= 2500 ) :
            return ''
    return ''

def PTENRTrig_Calculation(Index):
    if get_string(IA148BUMPSP.PTECode(Index)) == '04' or get_string(IA148BUMPSP.PTECode(Index)) == '11' or get_string(IA148BUMPSP.PTECode(Index)) == '09':
        return 0
    elif trim(get_string(IA148BUMPSP.PTEName(Index))) != '':
        return 1
    else:
        return 0

def PTERefTrig_Calculation(Index):
    if get_string(IA148BUMPSP.RefPTECode(Index)) == '64' or get_string(IA148BUMPSP.RefPTECode(Index)) == '58' or get_string(IA148BUMPSP.RefPTECode(Index)) == '55' or get_string(IA148BUMPSP.RefPTECode(Index)) == '52' or get_string(IA148BUMPSP.RefPTECode(Index)) == '59' or get_string(IA148BUMPSP.RefPTECode(Index)) == '65' or get_string(IA148BUMPSP.RefPTECode(Index)) == '66':
        return 0
    elif trim(get_string(IA148BUMPSP.RefPTEName(Index))) != '':
        return 1
    else:
        return 0

def RefPTECode_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    if get_number(IA148SP.NonRefNbr) > 10 and Index > 9:
        strindex = ( ( Index - 1 )  * 4 )  + 1
    else:
        strindex = ( ( Index )  * 4 )  + 1
    copystr = trim(Mid(get_string(IA148SP.RefCopiesStr), strindex, 4))
    if Index == 6 and get_number(IA148SP.RefNbr) > 7:
        return 'See Statement Attached'
    elif copystr != '':
        Copy = CLng(copystr)
        if ( Copy > 100 )  and  ( Copy <= 200 ) :
            return '52'
        elif  ( Copy > 200 )  and  ( Copy <= 300 ) :
            return get_string(IACred.Code, ( Copy )  - 200)
        elif  ( Copy > 300 )  and  ( Copy <= 400 ) :
            return '55'
        elif  ( Copy > 400 )  and  ( Copy <= 500 ) :
            return get_string(IACred.Code, ( Copy )  - 400)
        elif  ( Copy > 500 )  and  ( Copy <= 600 ) :
            return '58'
        elif  ( Copy > 600 )  and  ( Copy <= 700 ) :
            return '58'
        elif  ( Copy > 700 )  and  ( Copy <= 800 ) :
            return '59'
        elif  ( Copy > 800 )  and  ( Copy <= 900 ) :
            return '59'
        elif  ( Copy > 900 )  and  ( Copy <= 1000 ) :
            return '64'
        elif  ( Copy > 1000 )  and  ( Copy <= 1100 ) :
            return '65'
        elif  ( Copy > 1100 )  and  ( Copy <= 1200 ) :
            return '66'
        elif  ( Copy > 1200 )  and  ( Copy <= 1300 ) :
            return get_string(IACred.Code, ( Copy )  - 1200)
        elif  ( Copy > 1300 )  and  ( Copy <= 1400 ) :
            return get_string(IACred.Code, ( Copy )  - 1300)
        elif  ( Copy > 1400 )  and  ( Copy <= 1500 ) :
            return get_string(IACred.Code, ( Copy )  - 1400)
    return ''

def RefPTEEIN_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    if get_number(IA148SP.NonRefNbr) > 10 and Index > 9:
        strindex = ( ( Index - 1 )  * 4 )  + 1
    else:
        strindex = ( ( Index )  * 4 )  + 1
    copystr = trim(Mid(get_string(IA148SP.RefCopiesStr), strindex, 4))
    if Index == 6 and get_number(IA148SP.RefNbr) > 7:
        return ''
    elif copystr != '':
        Copy = CLng(copystr)
        if ( Copy > 100 )  and  ( Copy <= 200 ) :
            return get_string(IA8864.PTEEIN(0), ( Copy )  - 100)
        elif  ( Copy > 200 )  and  ( Copy <= 300 ) :
            return get_string(IACred.PTEEIN, ( Copy )  - 200)
        elif  ( Copy > 300 )  and  ( Copy <= 400 ) :
            return get_string(IA135.PTEEIN(0), ( Copy )  - 300)
        elif  ( Copy > 400 )  and  ( Copy <= 500 ) :
            return get_string(IACred.PTEEIN, ( Copy )  - 400)
        elif  ( Copy > 500 )  and  ( Copy <= 600 ) :
            return get_string(IA128.PTEEIN(0), ( Copy )  - 500)
        elif  ( Copy > 600 )  and  ( Copy <= 700 ) :
            return get_string(IA128S.PTEEIN(0), ( Copy )  - 600)
        elif  ( Copy > 700 )  and  ( Copy <= 800 ) :
            return get_string(IA128.PTEEIN(0), ( Copy )  - 700)
        elif  ( Copy > 800 )  and  ( Copy <= 900 ) :
            return get_string(IA128S.PTEEIN(0), ( Copy )  - 800)
        elif  ( Copy > 900 )  and  ( Copy <= 1000 ) :
            return get_string(IA137.PTEEIN(0), ( Copy )  - 900)
        elif  ( Copy > 1000 )  and  ( Copy <= 1100 ) :
            return get_string(IA138.PTEEIN(0), ( Copy )  - 1000)
        elif  ( Copy > 1100 )  and  ( Copy <= 1200 ) :
            return ''
        elif  ( Copy > 1200 )  and  ( Copy <= 1300 ) :
            return get_string(IACred.PTEEIN, ( Copy )  - 1200)
        elif  ( Copy > 1300 )  and  ( Copy <= 1400 ) :
            return get_string(IACred.PTEEIN, ( Copy )  - 1300)
        elif  ( Copy > 1400 )  and  ( Copy <= 1500 ) :
            return get_string(IACred.PTEEIN, ( Copy )  - 1400)
    return ''

def RefPTEIndexNbr_Calculation(Index):
    count = Long()

    max = Long()

    listedcount = Long()
    listedcount = 0
    count = 0
    while count < 69:
        if trim(get_string(IA148BUMPSP.RefPTEName(count))) != '':
            if listedcount == Index:
                return count
            else:
                listedcount = listedcount + 1
        count = count + 1
    return 0

def RefPTELine_Calculation(Index):
    Hold = Long()
    Hold = Index + 11
    if Index > 9:
        return 'Attached stmt'
    else:
        return CStr(Hold)

def RefPTEName_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    if get_number(IA148SP.NonRefNbr) > 10 and Index > 9:
        strindex = ( ( Index - 1 )  * 4 )  + 1
    else:
        strindex = ( ( Index )  * 4 )  + 1
    copystr = trim(Mid(get_string(IA148SP.RefCopiesStr), strindex, 4))
    if Index == 6 and get_number(IA148SP.RefNbr) > 7:
        return ''
    elif copystr != '':
        Copy = CLng(copystr)
        if ( Copy > 100 )  and  ( Copy <= 200 ) :
            return get_string(IA8864.PTEEntity(0), ( Copy )  - 100)
        elif  ( Copy > 200 )  and  ( Copy <= 300 ) :
            return get_string(IACred.PTEEntity, ( Copy )  - 200)
        elif  ( Copy > 300 )  and  ( Copy <= 400 ) :
            return get_string(IA135.PTEEntity(0), ( Copy )  - 300)
        elif  ( Copy > 400 )  and  ( Copy <= 500 ) :
            return get_string(IACred.PTEEntity, ( Copy )  - 400)
        elif  ( Copy > 500 )  and  ( Copy <= 600 ) :
            return get_string(IA128.PTEEntity(0), ( Copy )  - 500)
        elif  ( Copy > 600 )  and  ( Copy <= 700 ) :
            return get_string(IA128S.PTEEntity(0), ( Copy )  - 600)
        elif  ( Copy > 700 )  and  ( Copy <= 800 ) :
            return get_string(IA128.PTEEntity(0), ( Copy )  - 700)
        elif  ( Copy > 800 )  and  ( Copy <= 900 ) :
            return get_string(IA128S.PTEEntity(0), ( Copy )  - 800)
        elif  ( Copy > 900 )  and  ( Copy <= 1000 ) :
            return get_string(IA137.PTEEntity(0), ( Copy )  - 900)
        elif  ( Copy > 1000 )  and  ( Copy <= 1100 ) :
            return get_string(IA138.PTEEntity(0), ( Copy )  - 1000)
        elif  ( Copy > 1100 )  and  ( Copy <= 1200 ) :
            return ''
        elif  ( Copy > 1200 )  and  ( Copy <= 1300 ) :
            return get_string(IACred.PTEEntity, ( Copy )  - 1200)
        elif  ( Copy > 1300 )  and  ( Copy <= 1400 ) :
            return get_string(IACred.PTEEntity, ( Copy )  - 1300)
        elif  ( Copy > 1400 )  and  ( Copy <= 1500 ) :
            return get_string(IACred.PTEEntity, ( Copy )  - 1400)
    return ''

def RefTPPerc_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    if get_number(IA148SP.NonRefNbr) > 10 and Index > 9:
        strindex = ( ( Index - 1 )  * 4 )  + 1
    else:
        strindex = ( ( Index )  * 4 )  + 1
    copystr = trim(Mid(get_string(IA148SP.RefCopiesStr), strindex, 4))
    if Index == 6 and get_number(IA148SP.RefNbr) > 7:
        return 0
    elif copystr != '':
        Copy = CLng(copystr)
        if ( Copy > 100 )  and  ( Copy <= 200 ) :
            return get_float(IA8864.TPPerc(0), ( Copy )  - 100)
        elif  ( Copy > 200 )  and  ( Copy <= 300 ) :
            return get_float(IACred.TPPerc, ( Copy )  - 200)
        elif  ( Copy > 300 )  and  ( Copy <= 400 ) :
            return get_float(IA135.TPPerc(0), ( Copy )  - 300)
        elif  ( Copy > 400 )  and  ( Copy <= 500 ) :
            return get_float(IACred.TPPerc, ( Copy )  - 400)
        elif  ( Copy > 500 )  and  ( Copy <= 600 ) :
            return get_float(IA128.TPPerc(0), ( Copy )  - 500)
        elif  ( Copy > 600 )  and  ( Copy <= 700 ) :
            return get_float(IA128S.TPPerc(0), ( Copy )  - 600)
        elif  ( Copy > 700 )  and  ( Copy <= 800 ) :
            return get_float(IA128.TPPerc(0), ( Copy )  - 700)
        elif  ( Copy > 800 )  and  ( Copy <= 900 ) :
            return get_float(IA128S.TPPerc(0), ( Copy )  - 800)
        elif  ( Copy > 900 )  and  ( Copy <= 1000 ) :
            return get_float(IA137.TPPerc(0), ( Copy )  - 900)
        elif  ( Copy > 1000 )  and  ( Copy <= 1100 ) :
            return get_float(IA138.TPPerc(0), ( Copy )  - 1000)
        elif  ( Copy > 1100 )  and  ( Copy <= 1200 ) :
            return 0
        elif  ( Copy > 1200 )  and  ( Copy <= 1300 ) :
            return get_float(IACred.TPPerc, ( Copy )  - 1200)
        elif  ( Copy > 1300 )  and  ( Copy <= 1400 ) :
            return get_float(IACred.TPPerc, ( Copy )  - 1300)
        elif  ( Copy > 1400 )  and  ( Copy <= 1500 ) :
            return get_float(IACred.TPPerc, ( Copy )  - 1400)
    return 0

def TotPTE_Calculation():
    count = Integer()

    Total = Integer()
    count = 0
    Total = 0
    while count < 98:
        if trim(get_string(IA148BUMPSP.PTEName(count))) != '':
            Total = Total + 1
        else:
            Total = Total
        count = count + 1
    return Total

def TotRefPTE_Calculation():
    count = Integer()

    Total = Integer()
    count = 0
    Total = 0
    while count < 69:
        if trim(get_string(IA148BUMPSP.RefPTEName(count))) != '':
            Total = Total + 1
        else:
            Total = Total
        count = count + 1
    return Total

def TPPerc_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    if get_number(IA148SP.NonRefNbr) > 10 and Index > 9:
        strindex = ( ( Index - 1 )  * 4 )  + 1
    else:
        strindex = ( ( Index )  * 4 )  + 1
    copystr = trim(Mid(get_string(IA148SP.NonRefCopiesStr), strindex, 4))
    if Index == 9 and get_number(IA148SP.NonRefNbr) > 10:
        return 0
    elif copystr != '':
        Copy = CLng(copystr)
        if ( Copy > 100 )  and  ( Copy <= 200 ) :
            return 0
        elif  ( Copy > 200 )  and  ( Copy <= 300 ) :
            return get_float(IA134.SCorpPerc, ( Copy )  - 200)
        elif  ( Copy > 300 )  and  ( Copy <= 400 ) :
            return get_float(IACred.TPPerc, ( Copy )  - 300)
        elif  ( Copy > 400 )  and  ( Copy <= 500 ) :
            return get_float(IACred.TPPerc, ( Copy )  - 400)
        elif  ( Copy > 500 )  and  ( Copy <= 600 ) :
            return get_float(IACred.TPPerc, ( Copy )  - 500)
        elif  ( Copy > 600 )  and  ( Copy <= 700 ) :
            return get_float(IACred.TPPerc, ( Copy )  - 600)
        elif  ( Copy > 700 )  and  ( Copy <= 800 ) :
            return get_float(IACred.TPPerc, ( Copy )  - 700)
        elif  ( Copy > 800 )  and  ( Copy <= 900 ) :
            return get_float(IACred.TPPerc, ( Copy )  - 800)
        elif  ( Copy > 900 )  and  ( Copy <= 1000 ) :
            return get_float(IACred.TPPerc, ( Copy )  - 900)
        elif  ( Copy > 1000 )  and  ( Copy <= 1100 ) :
            return get_float(IACred.TPPerc, ( Copy )  - 1000)
        elif  ( Copy > 1100 )  and  ( Copy <= 1200 ) :
            return get_float(IACred.TPPerc, ( Copy )  - 1100)
        elif  ( Copy > 1200 )  and  ( Copy <= 1300 ) :
            return get_float(IACred.TPPerc, ( Copy )  - 1200)
        elif  ( Copy > 1300 )  and  ( Copy <= 1400 ) :
            return get_float(IACred.TPPerc, ( Copy )  - 1300)
        elif  ( Copy > 1400 )  and  ( Copy <= 1500 ) :
            return get_float(IACred.TPPerc, ( Copy )  - 1400)
        elif  ( Copy > 1500 )  and  ( Copy <= 1600 ) :
            return get_float(IACred.TPPerc, ( Copy )  - 1500)
        elif  ( Copy > 1600 )  and  ( Copy <= 1700 ) :
            return get_float(IACred.TPPerc, ( Copy )  - 1600)
        elif  ( Copy > 1700 )  and  ( Copy <= 1800 ) :
            return get_float(IACred.TPPerc, ( Copy )  - 1700)
        elif  ( Copy > 1800 )  and  ( Copy <= 1900 ) :
            return get_float(IACred.TPPerc, ( Copy )  - 1800)
        elif  ( Copy > 1900 )  and  ( Copy <= 2000 ) :
            return get_float(IACred.TPPerc, ( Copy )  - 1900)
        elif  ( Copy > 2000 )  and  ( Copy <= 2100 ) :
            return get_float(IACred.TPPerc, ( Copy )  - 2000)
        elif  ( Copy > 2100 )  and  ( Copy <= 2200 ) :
            return get_float(IACred.TPPerc, ( Copy )  - 2100)
        elif  ( Copy > 2200 )  and  ( Copy <= 2300 ) :
            return get_float(IACred.TPPerc, ( Copy )  - 2200)
        elif  ( Copy > 2300 )  and  ( Copy <= 2400 ) :
            return get_float(IACred.TPPerc, ( Copy )  - 2300)
        elif  ( Copy > 2400 )  and  ( Copy <= 2500 ) :
            return 0
    return 0


