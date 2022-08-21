from forms.out import IA137
from forms.out import IA148BUMPSP
from forms.out import IA148SP
from forms.out import IAWBP148REFSP
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Desc_Calculation():
    Total1 = Currency()
    Total1 = get_currency(IAWBP148REFSP.TotRefCr1) + get_currency(IAWBP148REFSP.TotRefCr2)
    return CStr(Total1) + ' Refundable Credits'

def Names_Calculation():
    return get_string(IA148SP.Names)

def Offset_Calculation():
    if GetCopy() == 1:
        return 6
    else:
        return 56

def Print_Calculation():
    if get_currency(IAWBP148REFSP.TotRefCr1) > 0 or get_currency(IAWBP148REFSP.TotRefCr2) > 0:
        return 1
    else:
        return 0

def PTERefTrig_Calculation(Index):
    if get_string(IAWBP148REFSP.RefPTECode(Index)) == '64' or get_string(IAWBP148REFSP.RefPTECode(Index)) == '58' or get_string(IAWBP148REFSP.RefPTECode(Index)) == '55' or get_string(IAWBP148REFSP.RefPTECode(Index)) == '52' or get_string(IAWBP148REFSP.RefPTECode(Index)) == '59' or get_string(IAWBP148REFSP.RefPTECode(Index)) == '65' or get_string(IAWBP148REFSP.RefPTECode(Index)) == '66':
        return 0
    elif trim(get_string(IAWBP148REFSP.RefPTEName(Index))) != '':
        return 1
    else:
        return 0

def RefCert_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    strindex = ( ( ( ( GetCopy() - 1 )  * 50 )  + 6 + Index )  * 4 )  + 1
    copystr = trim(Mid(get_string(IA148SP.RefCopiesStr), strindex, 4))
    if get_number(IA148SP.RefNbr) == 7:
        return ''
    elif copystr != '':
        Copy = CLng(copystr)
        if ( Copy > 100 )  and  ( Copy <= 200 ) :
            return ''
        elif  ( Copy > 200 )  and  ( Copy <= 300 ) :
            return get_string(IACred.CertNumber, ( Copy )  - 200)
        elif  ( Copy > 300 )  and  ( Copy <= 400 ) :
            return ''
        elif  ( Copy > 400 )  and  ( Copy <= 500 ) :
            return get_string(IACred.CertNumber, ( Copy )  - 400)
        elif  ( Copy > 500 )  and  ( Copy <= 600 ) :
            return ''
        elif  ( Copy > 600 )  and  ( Copy <= 700 ) :
            return ''
        elif  ( Copy > 700 )  and  ( Copy <= 800 ) :
            return get_string(IA128.SuppCertNbr, ( Copy )  - 700)
        elif  ( Copy > 800 )  and  ( Copy <= 900 ) :
            return get_string(IA128S.SuppCertNbr, ( Copy )  - 800)
        elif  ( Copy > 900 )  and  ( Copy <= 1000 ) :
            return ''
        elif  ( Copy > 1000 )  and  ( Copy <= 1100 ) :
            return ''
        elif  ( Copy > 1100 )  and  ( Copy <= 1200 ) :
            return ''
        elif  ( Copy > 1200 )  and  ( Copy <= 1300 ) :
            return get_string(IACred.CertNumber, ( Copy )  - 1200)
        elif  ( Copy > 1300 )  and  ( Copy <= 1400 ) :
            return get_string(IACred.CertNumber, ( Copy )  - 1300)
        elif  ( Copy > 1400 )  and  ( Copy <= 1500 ) :
            return get_string(IACred.CertNumber, ( Copy )  - 1400)
    return ''

def RefCode_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    strindex = ( ( ( ( GetCopy() - 1 )  * 50 )  + 6 + Index )  * 4 )  + 1
    copystr = trim(Mid(get_string(IA148SP.RefCopiesStr), strindex, 4))
    if get_number(IA148SP.RefNbr) == 7:
        return ''
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

def RefCr_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    strindex = ( ( ( ( GetCopy() - 1 )  * 50 )  + 6 + Index )  * 4 )  + 1
    copystr = trim(Mid(get_string(IA148SP.RefCopiesStr), strindex, 4))
    if get_number(IA148SP.RefNbr) == 7:
        return 0
    elif copystr != '':
        Copy = CLng(copystr)
        if ( Copy > 100 )  and  ( Copy <= 200 ) :
            return get_currency(IA8864.BiodieselCr, ( Copy )  - 100)
        elif  ( Copy > 200 )  and  ( Copy <= 300 ) :
            return get_currency(IACred.CYCredit, ( Copy )  - 200)
        elif  ( Copy > 300 )  and  ( Copy <= 400 ) :
            return get_currency(IA135.E85Credit, ( Copy )  - 300)
        elif  ( Copy > 400 )  and  ( Copy <= 500 ) :
            return get_currency(IACred.CYCredit, ( Copy )  - 400)
        elif  ( Copy > 500 )  and  ( Copy <= 600 ) :
            return get_currency(IA128.TotResearchCr, ( Copy )  - 500)
        elif  ( Copy > 600 )  and  ( Copy <= 700 ) :
            return get_currency(IA128S.TotResearchCr, ( Copy )  - 600)
        elif  ( Copy > 700 )  and  ( Copy <= 800 ) :
            return get_currency(IA128.TotSuppResearchCr, ( Copy )  - 700)
        elif  ( Copy > 800 )  and  ( Copy <= 900 ) :
            return get_currency(IA128S.TotSuppResearchCr, ( Copy )  - 800)
        elif  ( Copy > 900 )  and  ( Copy <= 1000 ) :
            return get_currency(IA137.EthPromoteCr, ( Copy )  - 900)
        elif  ( Copy > 1000 )  and  ( Copy <= 1100 ) :
            return get_currency(IA138.E15Credit, ( Copy )  - 1000)
        elif  ( Copy > 1100 )  and  ( Copy <= 1200 ) :
            return get_currency(IA177.CYAdoptionTaxCr, ( Copy )  - 1100)
        elif  ( Copy > 1200 )  and  ( Copy <= 1300 ) :
            return get_currency(IACred.CYCredit, ( Copy )  - 1200)
        elif  ( Copy > 1300 )  and  ( Copy <= 1400 ) :
            return get_currency(IACred.CYCredit, ( Copy )  - 1300)
        elif  ( Copy > 1400 )  and  ( Copy <= 1500 ) :
            return get_currency(IACred.CYCredit, ( Copy )  - 1400)
    return 0

def RefPTECode_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + get_number(IAWBP148REFSP.Offset) + 1
    return get_string(IA148BUMPSP.RefPTECode(Stuff))

def RefPTEEIN_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + get_number(IAWBP148REFSP.Offset) + 1
    return get_string(IA148BUMPSP.RefPTEEIN(Stuff))

def RefPTEName_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + get_number(IAWBP148REFSP.Offset) + 1
    return get_string(IA148BUMPSP.RefPTEName(Stuff))

def RefTPPerc_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + get_number(IAWBP148REFSP.Offset) + 1
    return get_float(IA148BUMPSP.RefTPPerc(Stuff))

def RefTrig_Calculation(Index):
    if get_string(IAWBP148REFSP.RefCode(Index)) == '64' or get_string(IAWBP148REFSP.RefCode(Index)) == '58' or get_string(IAWBP148REFSP.RefCode(Index)) == '55' or get_string(IAWBP148REFSP.RefCode(Index)) == '52' or get_string(IAWBP148REFSP.RefCode(Index)) == '59' or get_string(IAWBP148REFSP.RefCode(Index)) == '65' or get_string(IAWBP148REFSP.RefCode(Index)) == '66':
        return 0
    elif get_currency(IAWBP148REFSP.RefCr(Index)) > 0:
        return 1
    else:
        return 0

def SSN_Calculation():
    return get_string(IA148SP.SSN)

def TotRefCr1_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 25:
        SubTot = SubTot + get_currency(IAWBP148REFSP.RefCr(count))
        count = count + 1
    return SubTot

def TotRefCr2_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 25
    SubTot = 0
    while count < 50:
        SubTot = SubTot + get_currency(IAWBP148REFSP.RefCr(count))
        count = count + 1
    return SubTot


