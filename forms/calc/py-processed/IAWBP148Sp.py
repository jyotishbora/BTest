from forms.out import IA148BUMPSP
from forms.out import IA148SP
from forms.out import IA8801SP
from forms.out import IAWBP148SP
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def ArrayNonRefCr_Calculation(Index):
    if Index == 0:
        return get_currency(IAWBP148SP.NonRefCr1)
    elif Index == 1:
        return get_currency(IAWBP148SP.NonRefCr2)
    elif Index == 2:
        return get_currency(IAWBP148SP.NonRefCr3)
    elif Index == 3:
        return get_currency(IAWBP148SP.NonRefCr4)
    elif Index == 4:
        return get_currency(IAWBP148SP.NonRefCr5)
    elif Index == 5:
        return get_currency(IAWBP148SP.NonRefCr6)
    elif Index == 6:
        return get_currency(IAWBP148SP.NonRefCr7)
    elif Index == 7:
        return get_currency(IAWBP148SP.NonRefCr8)
    elif Index == 8:
        return get_currency(IAWBP148SP.NonRefCr9)
    elif Index == 9:
        return get_currency(IAWBP148SP.NonRefCr10)
    elif Index == 10:
        return get_currency(IAWBP148SP.NonRefCr11)
    elif Index == 11:
        return get_currency(IAWBP148SP.NonRefCr12)
    elif Index == 12:
        return get_currency(IAWBP148SP.NonRefCr13)
    elif Index == 13:
        return get_currency(IAWBP148SP.NonRefCr14)
    elif Index == 14:
        return get_currency(IAWBP148SP.NonRefCr15)
    elif Index == 15:
        return get_currency(IAWBP148SP.NonRefCr16)
    elif Index == 16:
        return get_currency(IAWBP148SP.NonRefCr17)
    elif Index == 17:
        return get_currency(IAWBP148SP.NonRefCr18)
    elif Index == 18:
        return get_currency(IAWBP148SP.NonRefCr19)
    elif Index == 19:
        return get_currency(IAWBP148SP.NonRefCr20)
    elif Index == 20:
        return get_currency(IAWBP148SP.NonRefCr21)
    elif Index == 21:
        return get_currency(IAWBP148SP.NonRefCr22)
    elif Index == 22:
        return get_currency(IAWBP148SP.NonRefCr23)
    elif Index == 23:
        return get_currency(IAWBP148SP.NonRefCr24)
    elif Index == 24:
        return get_currency(IAWBP148SP.NonRefCr25)
    elif Index == 25:
        return get_currency(IAWBP148SP.NonRefCr26)
    elif Index == 26:
        return get_currency(IAWBP148SP.NonRefCr27)
    elif Index == 27:
        return get_currency(IAWBP148SP.NonRefCr28)
    else:
        return get_currency(IAWBP148SP.NonRefCr29)

def AvailCr_Calculation(Index):
    if get_string(IAWBP148SP.NonRefCode(Index)) == '09':
        return get_currency(IA8801SP.AMTCR)
    else:
        return get_currency(IAWBP148SP.PYCarry(Index)) + get_currency(IAWBP148SP.CYCredit(Index))

def CYCarry_Calculation(Index):
    if get_string(IAWBP148SP.NonRefCode(Index)) == '09':
        return get_currency(IA8801SP.CYCarryforward)
    else:
        return max_value(0, get_currency(IAWBP148SP.AvailCr(Index)) - get_currency(IAWBP148SP.ArrayNonRefCr(Index)) - get_currency(IAWBP148SP.ExpCr(Index)))

def CYCredit_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    strindex = ( ( ( ( GetCopy() - 1 )  * 29 )  + 9 + Index )  * 4 )  + 1
    copystr = trim(Mid(get_string(IA148SP.NonRefCopiesStr), strindex, 4))
    if get_number(IA148SP.NonRefNbr) == 10:
        return 0
    elif copystr != '':
        Copy = CLng(copystr)
        if ( Copy > 100 )  and  ( Copy <= 200 ) :
            return get_currency(IA147.FranchiseCr, ( Copy )  - 100)
        elif  ( Copy > 200 )  and  ( Copy <= 300 ) :
            return get_currency(IA134.Credit, ( Copy )  - 200)
        elif  ( Copy > 300 )  and  ( Copy <= 400 ) :
            return get_currency(IACred.CYCredit, ( Copy )  - 300)
        elif  ( Copy > 400 )  and  ( Copy <= 500 ) :
            return get_currency(IACred.CYCredit, ( Copy )  - 400)
        elif  ( Copy > 500 )  and  ( Copy <= 600 ) :
            return get_currency(IACred.CYCredit, ( Copy )  - 500)
        elif  ( Copy > 600 )  and  ( Copy <= 700 ) :
            return get_currency(IACred.CYCredit, ( Copy )  - 600)
        elif  ( Copy > 700 )  and  ( Copy <= 800 ) :
            return get_currency(IACred.CYCredit, ( Copy )  - 700)
        elif  ( Copy > 800 )  and  ( Copy <= 900 ) :
            return get_currency(IACred.CYCredit, ( Copy )  - 800)
        elif  ( Copy > 900 )  and  ( Copy <= 1000 ) :
            return get_currency(IACred.CYCredit, ( Copy )  - 900)
        elif  ( Copy > 1000 )  and  ( Copy <= 1100 ) :
            return get_currency(IACred.CYCredit, ( Copy )  - 1000)
        elif  ( Copy > 1100 )  and  ( Copy <= 1200 ) :
            return get_currency(IACred.CYCredit, ( Copy )  - 1100)
        elif  ( Copy > 1200 )  and  ( Copy <= 1300 ) :
            return get_currency(IACred.CYCredit, ( Copy )  - 1200)
        elif  ( Copy > 1300 )  and  ( Copy <= 1400 ) :
            return get_currency(IACred.CYCredit, ( Copy )  - 1300)
        elif  ( Copy > 1400 )  and  ( Copy <= 1500 ) :
            return get_currency(IACred.CYCredit, ( Copy )  - 1400)
        elif  ( Copy > 1500 )  and  ( Copy <= 1600 ) :
            return get_currency(IACred.CYCredit, ( Copy )  - 1500)
        elif  ( Copy > 1600 )  and  ( Copy <= 1700 ) :
            return get_currency(IACred.CYCredit, ( Copy )  - 1600)
        elif  ( Copy > 1700 )  and  ( Copy <= 1800 ) :
            return get_currency(IACred.CYCredit, ( Copy )  - 1700)
        elif  ( Copy > 1800 )  and  ( Copy <= 1900 ) :
            return get_currency(IACred.CYCredit, ( Copy )  - 1800)
        elif  ( Copy > 1900 )  and  ( Copy <= 2000 ) :
            return get_currency(IACred.CYCredit, ( Copy )  - 1900)
        elif  ( Copy > 2000 )  and  ( Copy <= 2100 ) :
            return get_currency(IACred.CYCredit, ( Copy )  - 2000)
        elif  ( Copy > 2100 )  and  ( Copy <= 2200 ) :
            return get_currency(IACred.CYCredit, ( Copy )  - 2100)
        elif  ( Copy > 2200 )  and  ( Copy <= 2300 ) :
            return get_currency(IACred.CYCredit, ( Copy )  - 2200)
        elif  ( Copy > 2300 )  and  ( Copy <= 2400 ) :
            return get_currency(IACred.CYCredit, ( Copy )  - 2300)
        elif  ( Copy > 2400 )  and  ( Copy <= 2500 ) :
            return get_currency(IA8801SP.PYAMT)
    return 0

def Desc_Calculation():
    Total1 = Currency()
    Total1 = get_currency(IAWBP148SP.TotNonRefCr)
    return CStr(Total1) + ' Nonrefundable Credits'

def ExpCr_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    strindex = ( ( ( ( GetCopy() - 1 )  * 29 )  + 9 + Index )  * 4 )  + 1
    copystr = trim(Mid(get_string(IA148SP.NonRefCopiesStr), strindex, 4))
    if get_number(IA148SP.NonRefNbr) == 10:
        return 0
    elif copystr != '':
        Copy = CLng(copystr)
        if ( Copy > 100 )  and  ( Copy <= 200 ) :
            return max_value(0, get_currency(IA148SP.AvailCr(Index)) - get_currency(IA148SP.ArrayNonRefCr(Index)))
        elif  ( Copy > 200 )  and  ( Copy <= 300 ) :
            return max_value(0, get_currency(IA148SP.AvailCr(Index)) - get_currency(IA148SP.ArrayNonRefCr(Index)))
        elif  ( Copy > 300 )  and  ( Copy <= 400 ) :
            return get_currency(IACred.ExpCr, ( Copy )  - 300)
        elif  ( Copy > 400 )  and  ( Copy <= 500 ) :
            return get_currency(IACred.ExpCr, ( Copy )  - 400)
        elif  ( Copy > 500 )  and  ( Copy <= 600 ) :
            return get_currency(IACred.ExpCr, ( Copy )  - 500)
        elif  ( Copy > 600 )  and  ( Copy <= 700 ) :
            return get_currency(IACred.ExpCr, ( Copy )  - 600)
        elif  ( Copy > 700 )  and  ( Copy <= 800 ) :
            return get_currency(IACred.ExpCr, ( Copy )  - 700)
        elif  ( Copy > 800 )  and  ( Copy <= 900 ) :
            return get_currency(IACred.ExpCr, ( Copy )  - 800)
        elif  ( Copy > 900 )  and  ( Copy <= 1000 ) :
            return get_currency(IACred.ExpCr, ( Copy )  - 900)
        elif  ( Copy > 1000 )  and  ( Copy <= 1100 ) :
            return get_currency(IACred.ExpCr, ( Copy )  - 1000)
        elif  ( Copy > 1100 )  and  ( Copy <= 1200 ) :
            return get_currency(IACred.ExpCr, ( Copy )  - 1100)
        elif  ( Copy > 1200 )  and  ( Copy <= 1300 ) :
            return get_currency(IACred.ExpCr, ( Copy )  - 1200)
        elif  ( Copy > 1300 )  and  ( Copy <= 1400 ) :
            return get_currency(IACred.ExpCr, ( Copy )  - 1300)
        elif  ( Copy > 1400 )  and  ( Copy <= 1500 ) :
            return get_currency(IACred.ExpCr, ( Copy )  - 1400)
        elif  ( Copy > 1500 )  and  ( Copy <= 1600 ) :
            return get_currency(IACred.ExpCr, ( Copy )  - 1500)
        elif  ( Copy > 1600 )  and  ( Copy <= 1700 ) :
            return get_currency(IACred.ExpCr, ( Copy )  - 1600)
        elif  ( Copy > 1700 )  and  ( Copy <= 1800 ) :
            return get_currency(IACred.ExpCr, ( Copy )  - 1700)
        elif  ( Copy > 1800 )  and  ( Copy <= 1900 ) :
            return get_currency(IACred.ExpCr, ( Copy )  - 1800)
        elif  ( Copy > 1900 )  and  ( Copy <= 2000 ) :
            return get_currency(IACred.ExpCr, ( Copy )  - 1900)
        elif  ( Copy > 2000 )  and  ( Copy <= 2100 ) :
            return get_currency(IACred.ExpCr, ( Copy )  - 2000)
        elif  ( Copy > 2100 )  and  ( Copy <= 2200 ) :
            return get_currency(IACred.ExpCr, ( Copy )  - 2100)
        elif  ( Copy > 2200 )  and  ( Copy <= 2300 ) :
            return get_currency(IACred.ExpCr, ( Copy )  - 2200)
        elif  ( Copy > 2300 )  and  ( Copy <= 2400 ) :
            return get_currency(IACred.ExpCr, ( Copy )  - 2300)
        elif  ( Copy > 2400 )  and  ( Copy <= 2500 ) :
            return 0
    return 0

def Names_Calculation():
    return get_string(IA148SP.Names)

def NonRefCert_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    strindex = ( ( ( ( GetCopy() - 1 )  * 29 )  + 9 + Index )  * 4 )  + 1
    copystr = trim(Mid(get_string(IA148SP.NonRefCopiesStr), strindex, 4))
    if get_number(IA148SP.NonRefNbr) == 10:
        return ''
    elif copystr != '':
        Copy = CLng(copystr)
        if ( Copy > 100 )  and  ( Copy <= 200 ) :
            return ''
        elif  ( Copy > 200 )  and  ( Copy <= 300 ) :
            return ''
        elif  ( Copy > 300 )  and  ( Copy <= 400 ) :
            return get_string(IACred.CertNumber, ( Copy )  - 300)
        elif  ( Copy > 400 )  and  ( Copy <= 500 ) :
            return get_string(IACred.CertNumber, ( Copy )  - 400)
        elif  ( Copy > 500 )  and  ( Copy <= 600 ) :
            return get_string(IACred.CertNumber, ( Copy )  - 500)
        elif  ( Copy > 600 )  and  ( Copy <= 700 ) :
            return get_string(IACred.CertNumber, ( Copy )  - 600)
        elif  ( Copy > 700 )  and  ( Copy <= 800 ) :
            return get_string(IACred.CertNumber, ( Copy )  - 700)
        elif  ( Copy > 800 )  and  ( Copy <= 900 ) :
            return get_string(IACred.CertNumber, ( Copy )  - 800)
        elif  ( Copy > 900 )  and  ( Copy <= 1000 ) :
            return get_string(IACred.CertNumber, ( Copy )  - 900)
        elif  ( Copy > 1000 )  and  ( Copy <= 1100 ) :
            return get_string(IACred.CertNumber, ( Copy )  - 1000)
        elif  ( Copy > 1100 )  and  ( Copy <= 1200 ) :
            return get_string(IACred.CertNumber, ( Copy )  - 1100)
        elif  ( Copy > 1200 )  and  ( Copy <= 1300 ) :
            return get_string(IACred.CertNumber, ( Copy )  - 1200)
        elif  ( Copy > 1300 )  and  ( Copy <= 1400 ) :
            return get_string(IACred.CertNumber, ( Copy )  - 1300)
        elif  ( Copy > 1400 )  and  ( Copy <= 1500 ) :
            return get_string(IACred.CertNumber, ( Copy )  - 1400)
        elif  ( Copy > 1500 )  and  ( Copy <= 1600 ) :
            return get_string(IACred.CertNumber, ( Copy )  - 1500)
        elif  ( Copy > 1600 )  and  ( Copy <= 1700 ) :
            return get_string(IACred.CertNumber, ( Copy )  - 1600)
        elif  ( Copy > 1700 )  and  ( Copy <= 1800 ) :
            return get_string(IACred.CertNumber, ( Copy )  - 1700)
        elif  ( Copy > 1800 )  and  ( Copy <= 1900 ) :
            return get_string(IACred.CertNumber, ( Copy )  - 1800)
        elif  ( Copy > 1900 )  and  ( Copy <= 2000 ) :
            return get_string(IACred.CertNumber, ( Copy )  - 1900)
        elif  ( Copy > 2000 )  and  ( Copy <= 2100 ) :
            return get_string(IACred.CertNumber, ( Copy )  - 2000)
        elif  ( Copy > 2100 )  and  ( Copy <= 2200 ) :
            return get_string(IACred.CertNumber, ( Copy )  - 2100)
        elif  ( Copy > 2200 )  and  ( Copy <= 2300 ) :
            return get_string(IACred.CertNumber, ( Copy )  - 2200)
        elif  ( Copy > 2300 )  and  ( Copy <= 2400 ) :
            return get_string(IACred.CertNumber, ( Copy )  - 2300)
        elif  ( Copy > 2400 )  and  ( Copy <= 2500 ) :
            return ''
    return ''

def NonRefCode_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    strindex = ( ( ( ( GetCopy() - 1 )  * 29 )  + 9 + Index )  * 4 )  + 1
    copystr = trim(Mid(get_string(IA148SP.NonRefCopiesStr), strindex, 4))
    if get_number(IA148SP.NonRefNbr) == 10:
        return ''
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

def NonRefCr1_Calculation():
    PriorCopy = Long()

    PriorCopyTax = Currency()
    PriorCopy = GetCopy()
    PriorCopyTax = get_currency(IAWBP148SP.NonRefTax30, PriorCopy - 1)
    if GetCopy() == 1:
        return min_value(get_currency(IAWBP148SP.AvailCr(0)), get_currency(IA148SP.NonRefTax10))
    else:
        return min_value(get_currency(IAWBP148SP.AvailCr(0)), PriorCopyTax)

def NonRefCr10_Calculation():
    return min_value(get_currency(IAWBP148SP.AvailCr(9)), get_currency(IAWBP148SP.NonRefTax10))

def NonRefCr11_Calculation():
    return min_value(get_currency(IAWBP148SP.AvailCr(10)), get_currency(IAWBP148SP.NonRefTax11))

def NonRefCr12_Calculation():
    return min_value(get_currency(IAWBP148SP.AvailCr(11)), get_currency(IAWBP148SP.NonRefTax12))

def NonRefCr13_Calculation():
    return min_value(get_currency(IAWBP148SP.AvailCr(12)), get_currency(IAWBP148SP.NonRefTax13))

def NonRefCr14_Calculation():
    return min_value(get_currency(IAWBP148SP.AvailCr(13)), get_currency(IAWBP148SP.NonRefTax14))

def NonRefCr15_Calculation():
    return min_value(get_currency(IAWBP148SP.AvailCr(14)), get_currency(IAWBP148SP.NonRefTax15))

def NonRefCr16_Calculation():
    return min_value(get_currency(IAWBP148SP.AvailCr(15)), get_currency(IAWBP148SP.NonRefTax16))

def NonRefCr17_Calculation():
    return min_value(get_currency(IAWBP148SP.AvailCr(16)), get_currency(IAWBP148SP.NonRefTax17))

def NonRefCr18_Calculation():
    return min_value(get_currency(IAWBP148SP.AvailCr(17)), get_currency(IAWBP148SP.NonRefTax18))

def NonRefCr19_Calculation():
    return min_value(get_currency(IAWBP148SP.AvailCr(18)), get_currency(IAWBP148SP.NonRefTax19))

def NonRefCr2_Calculation():
    return min_value(get_currency(IAWBP148SP.AvailCr(1)), get_currency(IAWBP148SP.NonRefTax2))

def NonRefCr20_Calculation():
    return min_value(get_currency(IAWBP148SP.AvailCr(19)), get_currency(IAWBP148SP.NonRefTax20))

def NonRefCr21_Calculation():
    return min_value(get_currency(IAWBP148SP.AvailCr(20)), get_currency(IAWBP148SP.NonRefTax21))

def NonRefCr22_Calculation():
    return min_value(get_currency(IAWBP148SP.AvailCr(21)), get_currency(IAWBP148SP.NonRefTax22))

def NonRefCr23_Calculation():
    return min_value(get_currency(IAWBP148SP.AvailCr(22)), get_currency(IAWBP148SP.NonRefTax23))

def NonRefCr24_Calculation():
    return min_value(get_currency(IAWBP148SP.AvailCr(23)), get_currency(IAWBP148SP.NonRefTax24))

def NonRefCr25_Calculation():
    return min_value(get_currency(IAWBP148SP.AvailCr(24)), get_currency(IAWBP148SP.NonRefTax25))

def NonRefCr26_Calculation():
    return min_value(get_currency(IAWBP148SP.AvailCr(25)), get_currency(IAWBP148SP.NonRefTax26))

def NonRefCr27_Calculation():
    return min_value(get_currency(IAWBP148SP.AvailCr(26)), get_currency(IAWBP148SP.NonRefTax27))

def NonRefCr28_Calculation():
    return min_value(get_currency(IAWBP148SP.AvailCr(27)), get_currency(IAWBP148SP.NonRefTax28))

def NonRefCr29_Calculation():
    return min_value(get_currency(IAWBP148SP.AvailCr(28)), get_currency(IAWBP148SP.NonRefTax29))

def NonRefCr3_Calculation():
    return min_value(get_currency(IAWBP148SP.AvailCr(2)), get_currency(IAWBP148SP.NonRefTax3))

def NonRefCr4_Calculation():
    return min_value(get_currency(IAWBP148SP.AvailCr(3)), get_currency(IAWBP148SP.NonRefTax4))

def NonRefCr5_Calculation():
    return min_value(get_currency(IAWBP148SP.AvailCr(4)), get_currency(IAWBP148SP.NonRefTax5))

def NonRefCr6_Calculation():
    return min_value(get_currency(IAWBP148SP.AvailCr(5)), get_currency(IAWBP148SP.NonRefTax6))

def NonRefCr7_Calculation():
    return min_value(get_currency(IAWBP148SP.AvailCr(6)), get_currency(IAWBP148SP.NonRefTax7))

def NonRefCr8_Calculation():
    return min_value(get_currency(IAWBP148SP.AvailCr(7)), get_currency(IAWBP148SP.NonRefTax8))

def NonRefCr9_Calculation():
    return min_value(get_currency(IAWBP148SP.AvailCr(8)), get_currency(IAWBP148SP.NonRefTax9))

def NonRefTax10_Calculation():
    return max_value(0, get_currency(IAWBP148SP.NonRefTax9) - get_currency(IAWBP148SP.NonRefCr9))

def NonRefTax11_Calculation():
    return max_value(0, get_currency(IAWBP148SP.NonRefTax10) - get_currency(IAWBP148SP.NonRefCr10))

def NonRefTax12_Calculation():
    return max_value(0, get_currency(IAWBP148SP.NonRefTax11) - get_currency(IAWBP148SP.NonRefCr11))

def NonRefTax13_Calculation():
    return max_value(0, get_currency(IAWBP148SP.NonRefTax12) - get_currency(IAWBP148SP.NonRefCr12))

def NonRefTax14_Calculation():
    return max_value(0, get_currency(IAWBP148SP.NonRefTax13) - get_currency(IAWBP148SP.NonRefCr13))

def NonRefTax15_Calculation():
    return max_value(0, get_currency(IAWBP148SP.NonRefTax14) - get_currency(IAWBP148SP.NonRefCr14))

def NonRefTax16_Calculation():
    return max_value(0, get_currency(IAWBP148SP.NonRefTax15) - get_currency(IAWBP148SP.NonRefCr15))

def NonRefTax17_Calculation():
    return max_value(0, get_currency(IAWBP148SP.NonRefTax16) - get_currency(IAWBP148SP.NonRefCr16))

def NonRefTax18_Calculation():
    return max_value(0, get_currency(IAWBP148SP.NonRefTax17) - get_currency(IAWBP148SP.NonRefCr17))

def NonRefTax19_Calculation():
    return max_value(0, get_currency(IAWBP148SP.NonRefTax18) - get_currency(IAWBP148SP.NonRefCr18))

def NonRefTax2_Calculation():
    PriorCopy = Long()
    PriorCopy = GetCopy()
    if GetCopy() == 1:
        return max_value(0, get_currency(IA148SP.NonRefTax10) - get_currency(IAWBP148SP.NonRefCr1))
    else:
        return max_value(0, get_currency(IAWBP148SP.NonRefTax30, PriorCopy - 1) - get_currency(IAWBP148SP.NonRefCr1))

def NonRefTax20_Calculation():
    return max_value(0, get_currency(IAWBP148SP.NonRefTax19) - get_currency(IAWBP148SP.NonRefCr19))

def NonRefTax21_Calculation():
    return max_value(0, get_currency(IAWBP148SP.NonRefTax20) - get_currency(IAWBP148SP.NonRefCr20))

def NonRefTax22_Calculation():
    return max_value(0, get_currency(IAWBP148SP.NonRefTax21) - get_currency(IAWBP148SP.NonRefCr21))

def NonRefTax23_Calculation():
    return max_value(0, get_currency(IAWBP148SP.NonRefTax22) - get_currency(IAWBP148SP.NonRefCr22))

def NonRefTax24_Calculation():
    return max_value(0, get_currency(IAWBP148SP.NonRefTax23) - get_currency(IAWBP148SP.NonRefCr23))

def NonRefTax25_Calculation():
    return max_value(0, get_currency(IAWBP148SP.NonRefTax24) - get_currency(IAWBP148SP.NonRefCr24))

def NonRefTax26_Calculation():
    return max_value(0, get_currency(IAWBP148SP.NonRefTax25) - get_currency(IAWBP148SP.NonRefCr25))

def NonRefTax27_Calculation():
    return max_value(0, get_currency(IAWBP148SP.NonRefTax26) - get_currency(IAWBP148SP.NonRefCr26))

def NonRefTax28_Calculation():
    return max_value(0, get_currency(IAWBP148SP.NonRefTax27) - get_currency(IAWBP148SP.NonRefCr27))

def NonRefTax29_Calculation():
    return max_value(0, get_currency(IAWBP148SP.NonRefTax28) - get_currency(IAWBP148SP.NonRefCr28))

def NonRefTax3_Calculation():
    return max_value(0, get_currency(IAWBP148SP.NonRefTax2) - get_currency(IAWBP148SP.NonRefCr2))

def NonRefTax30_Calculation():
    return max_value(0, get_currency(IAWBP148SP.NonRefTax29) - get_currency(IAWBP148SP.NonRefCr29))

def NonRefTax4_Calculation():
    return max_value(0, get_currency(IAWBP148SP.NonRefTax3) - get_currency(IAWBP148SP.NonRefCr3))

def NonRefTax5_Calculation():
    return max_value(0, get_currency(IAWBP148SP.NonRefTax4) - get_currency(IAWBP148SP.NonRefCr4))

def NonRefTax6_Calculation():
    return max_value(0, get_currency(IAWBP148SP.NonRefTax5) - get_currency(IAWBP148SP.NonRefCr5))

def NonRefTax7_Calculation():
    return max_value(0, get_currency(IAWBP148SP.NonRefTax6) - get_currency(IAWBP148SP.NonRefCr6))

def NonRefTax8_Calculation():
    return max_value(0, get_currency(IAWBP148SP.NonRefTax7) - get_currency(IAWBP148SP.NonRefCr7))

def NonRefTax9_Calculation():
    return max_value(0, get_currency(IAWBP148SP.NonRefTax8) - get_currency(IAWBP148SP.NonRefCr8))

def NonRefTrig_Calculation(Index):
    if get_string(IAWBP148SP.NonRefCode(Index)) == '04' or get_string(IAWBP148SP.NonRefCode(Index)) == '11' or get_string(IAWBP148SP.NonRefCode(Index)) == '09':
        return 0
    elif get_currency(IAWBP148SP.AvailCr(Index)) > 0:
        return 1
    else:
        return 0

def Offset_Calculation():
    if GetCopy() == 1:
        return 9
    elif GetCopy() == 2:
        return 38
    else:
        return 67

def Print_Calculation():
    if get_currency(IAWBP148SP.TotNonRefCr) > 0:
        return 1
    elif trim(get_string(IAWBP148SP.NonRefCode(0))) != '' or get_currency(IAWBP148SP.CYCredit(0)) > 0:
        return 1
    else:
        return 0

def PTECode_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + get_number(IAWBP148SP.Offset) + 1
    return get_string(IA148BUMPSP.PTECode(Stuff))

def PTEEIN_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + get_number(IAWBP148SP.Offset) + 1
    return get_string(IA148BUMPSP.PTEEIN(Stuff))

def PTEName_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + get_number(IAWBP148SP.Offset) + 1
    return get_string(IA148BUMPSP.PTEName(Stuff))

def PTENRTrig_Calculation(Index):
    if get_string(IAWBP148SP.NonRefCode(Index)) == '04' or get_string(IAWBP148SP.PTECode(Index)) == '11' or get_string(IAWBP148SP.PTECode(Index)) == '09':
        return 0
    elif trim(get_string(IAWBP148SP.PTEName(Index))) != '':
        return 1
    else:
        return 0

def PYCarry_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    strindex = ( ( ( ( GetCopy() - 1 )  * 29 )  + 9 + Index )  * 4 )  + 1
    copystr = trim(Mid(get_string(IA148SP.NonRefCopiesStr), strindex, 4))
    if get_number(IA148SP.NonRefNbr) == 10:
        return 0
    elif copystr != '':
        Copy = CLng(copystr)
        if ( Copy > 100 )  and  ( Copy <= 200 ) :
            return 0
        elif  ( Copy > 200 )  and  ( Copy <= 300 ) :
            return 0
        elif  ( Copy > 300 )  and  ( Copy <= 400 ) :
            return get_currency(IACred.PYCarry, ( Copy )  - 300)
        elif  ( Copy > 400 )  and  ( Copy <= 500 ) :
            return get_currency(IACred.PYCarry, ( Copy )  - 400)
        elif  ( Copy > 500 )  and  ( Copy <= 600 ) :
            return get_currency(IACred.PYCarry, ( Copy )  - 500)
        elif  ( Copy > 600 )  and  ( Copy <= 700 ) :
            return get_currency(IACred.PYCarry, ( Copy )  - 600)
        elif  ( Copy > 700 )  and  ( Copy <= 800 ) :
            return get_currency(IACred.PYCarry, ( Copy )  - 700)
        elif  ( Copy > 800 )  and  ( Copy <= 900 ) :
            return get_currency(IACred.PYCarry, ( Copy )  - 800)
        elif  ( Copy > 900 )  and  ( Copy <= 1000 ) :
            return get_currency(IACred.PYCarry, ( Copy )  - 900)
        elif  ( Copy > 1000 )  and  ( Copy <= 1100 ) :
            return get_currency(IACred.PYCarry, ( Copy )  - 1000)
        elif  ( Copy > 1100 )  and  ( Copy <= 1200 ) :
            return get_currency(IACred.PYCarry, ( Copy )  - 1100)
        elif  ( Copy > 1200 )  and  ( Copy <= 1300 ) :
            return get_currency(IACred.PYCarry, ( Copy )  - 1200)
        elif  ( Copy > 1300 )  and  ( Copy <= 1400 ) :
            return get_currency(IACred.PYCarry, ( Copy )  - 1300)
        elif  ( Copy > 1400 )  and  ( Copy <= 1500 ) :
            return get_currency(IACred.PYCarry, ( Copy )  - 1400)
        elif  ( Copy > 1500 )  and  ( Copy <= 1600 ) :
            return get_currency(IACred.PYCarry, ( Copy )  - 1500)
        elif  ( Copy > 1600 )  and  ( Copy <= 1700 ) :
            return get_currency(IACred.PYCarry, ( Copy )  - 1600)
        elif  ( Copy > 1700 )  and  ( Copy <= 1800 ) :
            return get_currency(IACred.PYCarry, ( Copy )  - 1700)
        elif  ( Copy > 1800 )  and  ( Copy <= 1900 ) :
            return get_currency(IACred.PYCarry, ( Copy )  - 1800)
        elif  ( Copy > 1900 )  and  ( Copy <= 2000 ) :
            return get_currency(IACred.PYCarry, ( Copy )  - 1900)
        elif  ( Copy > 2000 )  and  ( Copy <= 2100 ) :
            return get_currency(IACred.PYCarry, ( Copy )  - 2000)
        elif  ( Copy > 2100 )  and  ( Copy <= 2200 ) :
            return get_currency(IACred.PYCarry, ( Copy )  - 2100)
        elif  ( Copy > 2200 )  and  ( Copy <= 2300 ) :
            return get_currency(IACred.PYCarry, ( Copy )  - 2200)
        elif  ( Copy > 2300 )  and  ( Copy <= 2400 ) :
            return get_currency(IACred.PYCarry, ( Copy )  - 2300)
        elif  ( Copy > 2400 )  and  ( Copy <= 2500 ) :
            return get_currency(IA8801SP.PYCarryforward)
    return 0

def SSN_Calculation():
    return get_string(IA148SP.SSN)

def TotNonRefCr_Calculation():
    NonRefCr1 = Currency()

    NonRefCr2 = Currency()

    NonRefCr3 = Currency()
    NonRefCr1 = get_currency(IAWBP148SP.NonRefCr1) + get_currency(IAWBP148SP.NonRefCr2) + get_currency(IAWBP148SP.NonRefCr3) + get_currency(IAWBP148SP.NonRefCr4) + get_currency(IAWBP148SP.NonRefCr5) + get_currency(IAWBP148SP.NonRefCr6) + get_currency(IAWBP148SP.NonRefCr7) + get_currency(IAWBP148SP.NonRefCr8) + get_currency(IAWBP148SP.NonRefCr9) + get_currency(IAWBP148SP.NonRefCr10)
    NonRefCr2 = get_currency(IAWBP148SP.NonRefCr11) + get_currency(IAWBP148SP.NonRefCr12) + get_currency(IAWBP148SP.NonRefCr13) + get_currency(IAWBP148SP.NonRefCr14) + get_currency(IAWBP148SP.NonRefCr15) + get_currency(IAWBP148SP.NonRefCr16) + get_currency(IAWBP148SP.NonRefCr17) + get_currency(IAWBP148SP.NonRefCr18) + get_currency(IAWBP148SP.NonRefCr19) + get_currency(IAWBP148SP.NonRefCr20)
    NonRefCr3 = get_currency(IAWBP148SP.NonRefCr21) + get_currency(IAWBP148SP.NonRefCr22) + get_currency(IAWBP148SP.NonRefCr23) + get_currency(IAWBP148SP.NonRefCr24) + get_currency(IAWBP148SP.NonRefCr25) + get_currency(IAWBP148SP.NonRefCr26) + get_currency(IAWBP148SP.NonRefCr27) + get_currency(IAWBP148SP.NonRefCr28) + get_currency(IAWBP148SP.NonRefCr29)
    return NonRefCr1 + NonRefCr2 + NonRefCr3

def TPPerc_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + get_number(IAWBP148SP.Offset) + 1
    return get_float(IA148BUMPSP.TPPerc(Stuff))


