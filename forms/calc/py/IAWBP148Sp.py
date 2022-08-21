from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def ArrayNonRefCr_Calculation(Index):
    if Index == 0:
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr1)
    elif Index == 1:
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr2)
    elif Index == 2:
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr3)
    elif Index == 3:
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr4)
    elif Index == 4:
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr5)
    elif Index == 5:
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr6)
    elif Index == 6:
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr7)
    elif Index == 7:
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr8)
    elif Index == 8:
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr9)
    elif Index == 9:
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr10)
    elif Index == 10:
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr11)
    elif Index == 11:
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr12)
    elif Index == 12:
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr13)
    elif Index == 13:
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr14)
    elif Index == 14:
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr15)
    elif Index == 15:
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr16)
    elif Index == 16:
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr17)
    elif Index == 17:
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr18)
    elif Index == 18:
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr19)
    elif Index == 19:
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr20)
    elif Index == 20:
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr21)
    elif Index == 21:
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr22)
    elif Index == 22:
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr23)
    elif Index == 23:
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr24)
    elif Index == 24:
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr25)
    elif Index == 25:
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr26)
    elif Index == 26:
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr27)
    elif Index == 27:
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr28)
    else:
        ReturnVal = GetCurrency(IAWBP148Sp.NonRefCr29)

def AvailCr_Calculation(Index):
    if GetString(IAWBP148Sp.NonRefCode(Index)) == '09':
        ReturnVal = GetCurrency(IA8801Sp.AMTCR)
    else:
        ReturnVal = GetCurrency(IAWBP148Sp.PYCarry(Index)) + GetCurrency(IAWBP148Sp.CYCredit(Index))

def CYCarry_Calculation(Index):
    if GetString(IAWBP148Sp.NonRefCode(Index)) == '09':
        ReturnVal = GetCurrency(IA8801Sp.CYCarryforward)
    else:
        ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.AvailCr(Index)) - GetCurrency(IAWBP148Sp.ArrayNonRefCr(Index)) - GetCurrency(IAWBP148Sp.ExpCr(Index)))

def CYCredit_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    strindex = ( ( ( ( GetCopy() - 1 )  * 29 )  + 9 + Index )  * 4 )  + 1
    copystr = Trim(Mid(GetString(IA148Sp.NonRefCopiesStr), strindex, 4))
    if GetNumber(IA148Sp.NonRefNbr) == 10:
        ReturnVal = 0
    elif copystr != '':
        Copy = CLng(copystr)
        if ( Copy > 100 )  and  ( Copy <= 200 ) :
            ReturnVal = GetCurrency(IA147.FranchiseCr, ( Copy )  - 100)
        elif  ( Copy > 200 )  and  ( Copy <= 300 ) :
            ReturnVal = GetCurrency(IA134.Credit, ( Copy )  - 200)
        elif  ( Copy > 300 )  and  ( Copy <= 400 ) :
            ReturnVal = GetCurrency(IACred.CYCredit, ( Copy )  - 300)
        elif  ( Copy > 400 )  and  ( Copy <= 500 ) :
            ReturnVal = GetCurrency(IACred.CYCredit, ( Copy )  - 400)
        elif  ( Copy > 500 )  and  ( Copy <= 600 ) :
            ReturnVal = GetCurrency(IACred.CYCredit, ( Copy )  - 500)
        elif  ( Copy > 600 )  and  ( Copy <= 700 ) :
            ReturnVal = GetCurrency(IACred.CYCredit, ( Copy )  - 600)
        elif  ( Copy > 700 )  and  ( Copy <= 800 ) :
            ReturnVal = GetCurrency(IACred.CYCredit, ( Copy )  - 700)
        elif  ( Copy > 800 )  and  ( Copy <= 900 ) :
            ReturnVal = GetCurrency(IACred.CYCredit, ( Copy )  - 800)
        elif  ( Copy > 900 )  and  ( Copy <= 1000 ) :
            ReturnVal = GetCurrency(IACred.CYCredit, ( Copy )  - 900)
        elif  ( Copy > 1000 )  and  ( Copy <= 1100 ) :
            ReturnVal = GetCurrency(IACred.CYCredit, ( Copy )  - 1000)
        elif  ( Copy > 1100 )  and  ( Copy <= 1200 ) :
            ReturnVal = GetCurrency(IACred.CYCredit, ( Copy )  - 1100)
        elif  ( Copy > 1200 )  and  ( Copy <= 1300 ) :
            ReturnVal = GetCurrency(IACred.CYCredit, ( Copy )  - 1200)
        elif  ( Copy > 1300 )  and  ( Copy <= 1400 ) :
            ReturnVal = GetCurrency(IACred.CYCredit, ( Copy )  - 1300)
        elif  ( Copy > 1400 )  and  ( Copy <= 1500 ) :
            ReturnVal = GetCurrency(IACred.CYCredit, ( Copy )  - 1400)
        elif  ( Copy > 1500 )  and  ( Copy <= 1600 ) :
            ReturnVal = GetCurrency(IACred.CYCredit, ( Copy )  - 1500)
        elif  ( Copy > 1600 )  and  ( Copy <= 1700 ) :
            ReturnVal = GetCurrency(IACred.CYCredit, ( Copy )  - 1600)
        elif  ( Copy > 1700 )  and  ( Copy <= 1800 ) :
            ReturnVal = GetCurrency(IACred.CYCredit, ( Copy )  - 1700)
        elif  ( Copy > 1800 )  and  ( Copy <= 1900 ) :
            ReturnVal = GetCurrency(IACred.CYCredit, ( Copy )  - 1800)
        elif  ( Copy > 1900 )  and  ( Copy <= 2000 ) :
            ReturnVal = GetCurrency(IACred.CYCredit, ( Copy )  - 1900)
        elif  ( Copy > 2000 )  and  ( Copy <= 2100 ) :
            ReturnVal = GetCurrency(IACred.CYCredit, ( Copy )  - 2000)
        elif  ( Copy > 2100 )  and  ( Copy <= 2200 ) :
            ReturnVal = GetCurrency(IACred.CYCredit, ( Copy )  - 2100)
        elif  ( Copy > 2200 )  and  ( Copy <= 2300 ) :
            ReturnVal = GetCurrency(IACred.CYCredit, ( Copy )  - 2200)
        elif  ( Copy > 2300 )  and  ( Copy <= 2400 ) :
            ReturnVal = GetCurrency(IACred.CYCredit, ( Copy )  - 2300)
        elif  ( Copy > 2400 )  and  ( Copy <= 2500 ) :
            ReturnVal = GetCurrency(IA8801Sp.PYAMT)
    ReturnVal = 0

def Desc_Calculation():
    Total1 = Currency()
    Total1 = GetCurrency(IAWBP148Sp.TotNonRefCr)
    ReturnVal = CStr(Total1) + ' Nonrefundable Credits'

def ExpCr_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    strindex = ( ( ( ( GetCopy() - 1 )  * 29 )  + 9 + Index )  * 4 )  + 1
    copystr = Trim(Mid(GetString(IA148Sp.NonRefCopiesStr), strindex, 4))
    if GetNumber(IA148Sp.NonRefNbr) == 10:
        ReturnVal = 0
    elif copystr != '':
        Copy = CLng(copystr)
        if ( Copy > 100 )  and  ( Copy <= 200 ) :
            ReturnVal = MaxValue(0, GetCurrency(IA148Sp.AvailCr(Index)) - GetCurrency(IA148Sp.ArrayNonRefCr(Index)))
        elif  ( Copy > 200 )  and  ( Copy <= 300 ) :
            ReturnVal = MaxValue(0, GetCurrency(IA148Sp.AvailCr(Index)) - GetCurrency(IA148Sp.ArrayNonRefCr(Index)))
        elif  ( Copy > 300 )  and  ( Copy <= 400 ) :
            ReturnVal = GetCurrency(IACred.ExpCr, ( Copy )  - 300)
        elif  ( Copy > 400 )  and  ( Copy <= 500 ) :
            ReturnVal = GetCurrency(IACred.ExpCr, ( Copy )  - 400)
        elif  ( Copy > 500 )  and  ( Copy <= 600 ) :
            ReturnVal = GetCurrency(IACred.ExpCr, ( Copy )  - 500)
        elif  ( Copy > 600 )  and  ( Copy <= 700 ) :
            ReturnVal = GetCurrency(IACred.ExpCr, ( Copy )  - 600)
        elif  ( Copy > 700 )  and  ( Copy <= 800 ) :
            ReturnVal = GetCurrency(IACred.ExpCr, ( Copy )  - 700)
        elif  ( Copy > 800 )  and  ( Copy <= 900 ) :
            ReturnVal = GetCurrency(IACred.ExpCr, ( Copy )  - 800)
        elif  ( Copy > 900 )  and  ( Copy <= 1000 ) :
            ReturnVal = GetCurrency(IACred.ExpCr, ( Copy )  - 900)
        elif  ( Copy > 1000 )  and  ( Copy <= 1100 ) :
            ReturnVal = GetCurrency(IACred.ExpCr, ( Copy )  - 1000)
        elif  ( Copy > 1100 )  and  ( Copy <= 1200 ) :
            ReturnVal = GetCurrency(IACred.ExpCr, ( Copy )  - 1100)
        elif  ( Copy > 1200 )  and  ( Copy <= 1300 ) :
            ReturnVal = GetCurrency(IACred.ExpCr, ( Copy )  - 1200)
        elif  ( Copy > 1300 )  and  ( Copy <= 1400 ) :
            ReturnVal = GetCurrency(IACred.ExpCr, ( Copy )  - 1300)
        elif  ( Copy > 1400 )  and  ( Copy <= 1500 ) :
            ReturnVal = GetCurrency(IACred.ExpCr, ( Copy )  - 1400)
        elif  ( Copy > 1500 )  and  ( Copy <= 1600 ) :
            ReturnVal = GetCurrency(IACred.ExpCr, ( Copy )  - 1500)
        elif  ( Copy > 1600 )  and  ( Copy <= 1700 ) :
            ReturnVal = GetCurrency(IACred.ExpCr, ( Copy )  - 1600)
        elif  ( Copy > 1700 )  and  ( Copy <= 1800 ) :
            ReturnVal = GetCurrency(IACred.ExpCr, ( Copy )  - 1700)
        elif  ( Copy > 1800 )  and  ( Copy <= 1900 ) :
            ReturnVal = GetCurrency(IACred.ExpCr, ( Copy )  - 1800)
        elif  ( Copy > 1900 )  and  ( Copy <= 2000 ) :
            ReturnVal = GetCurrency(IACred.ExpCr, ( Copy )  - 1900)
        elif  ( Copy > 2000 )  and  ( Copy <= 2100 ) :
            ReturnVal = GetCurrency(IACred.ExpCr, ( Copy )  - 2000)
        elif  ( Copy > 2100 )  and  ( Copy <= 2200 ) :
            ReturnVal = GetCurrency(IACred.ExpCr, ( Copy )  - 2100)
        elif  ( Copy > 2200 )  and  ( Copy <= 2300 ) :
            ReturnVal = GetCurrency(IACred.ExpCr, ( Copy )  - 2200)
        elif  ( Copy > 2300 )  and  ( Copy <= 2400 ) :
            ReturnVal = GetCurrency(IACred.ExpCr, ( Copy )  - 2300)
        elif  ( Copy > 2400 )  and  ( Copy <= 2500 ) :
            ReturnVal = 0
    ReturnVal = 0

def Names_Calculation():
    ReturnVal = GetString(IA148Sp.Names)

def NonRefCert_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    strindex = ( ( ( ( GetCopy() - 1 )  * 29 )  + 9 + Index )  * 4 )  + 1
    copystr = Trim(Mid(GetString(IA148Sp.NonRefCopiesStr), strindex, 4))
    if GetNumber(IA148Sp.NonRefNbr) == 10:
        ReturnVal = ''
    elif copystr != '':
        Copy = CLng(copystr)
        if ( Copy > 100 )  and  ( Copy <= 200 ) :
            ReturnVal = ''
        elif  ( Copy > 200 )  and  ( Copy <= 300 ) :
            ReturnVal = ''
        elif  ( Copy > 300 )  and  ( Copy <= 400 ) :
            ReturnVal = GetString(IACred.CertNumber, ( Copy )  - 300)
        elif  ( Copy > 400 )  and  ( Copy <= 500 ) :
            ReturnVal = GetString(IACred.CertNumber, ( Copy )  - 400)
        elif  ( Copy > 500 )  and  ( Copy <= 600 ) :
            ReturnVal = GetString(IACred.CertNumber, ( Copy )  - 500)
        elif  ( Copy > 600 )  and  ( Copy <= 700 ) :
            ReturnVal = GetString(IACred.CertNumber, ( Copy )  - 600)
        elif  ( Copy > 700 )  and  ( Copy <= 800 ) :
            ReturnVal = GetString(IACred.CertNumber, ( Copy )  - 700)
        elif  ( Copy > 800 )  and  ( Copy <= 900 ) :
            ReturnVal = GetString(IACred.CertNumber, ( Copy )  - 800)
        elif  ( Copy > 900 )  and  ( Copy <= 1000 ) :
            ReturnVal = GetString(IACred.CertNumber, ( Copy )  - 900)
        elif  ( Copy > 1000 )  and  ( Copy <= 1100 ) :
            ReturnVal = GetString(IACred.CertNumber, ( Copy )  - 1000)
        elif  ( Copy > 1100 )  and  ( Copy <= 1200 ) :
            ReturnVal = GetString(IACred.CertNumber, ( Copy )  - 1100)
        elif  ( Copy > 1200 )  and  ( Copy <= 1300 ) :
            ReturnVal = GetString(IACred.CertNumber, ( Copy )  - 1200)
        elif  ( Copy > 1300 )  and  ( Copy <= 1400 ) :
            ReturnVal = GetString(IACred.CertNumber, ( Copy )  - 1300)
        elif  ( Copy > 1400 )  and  ( Copy <= 1500 ) :
            ReturnVal = GetString(IACred.CertNumber, ( Copy )  - 1400)
        elif  ( Copy > 1500 )  and  ( Copy <= 1600 ) :
            ReturnVal = GetString(IACred.CertNumber, ( Copy )  - 1500)
        elif  ( Copy > 1600 )  and  ( Copy <= 1700 ) :
            ReturnVal = GetString(IACred.CertNumber, ( Copy )  - 1600)
        elif  ( Copy > 1700 )  and  ( Copy <= 1800 ) :
            ReturnVal = GetString(IACred.CertNumber, ( Copy )  - 1700)
        elif  ( Copy > 1800 )  and  ( Copy <= 1900 ) :
            ReturnVal = GetString(IACred.CertNumber, ( Copy )  - 1800)
        elif  ( Copy > 1900 )  and  ( Copy <= 2000 ) :
            ReturnVal = GetString(IACred.CertNumber, ( Copy )  - 1900)
        elif  ( Copy > 2000 )  and  ( Copy <= 2100 ) :
            ReturnVal = GetString(IACred.CertNumber, ( Copy )  - 2000)
        elif  ( Copy > 2100 )  and  ( Copy <= 2200 ) :
            ReturnVal = GetString(IACred.CertNumber, ( Copy )  - 2100)
        elif  ( Copy > 2200 )  and  ( Copy <= 2300 ) :
            ReturnVal = GetString(IACred.CertNumber, ( Copy )  - 2200)
        elif  ( Copy > 2300 )  and  ( Copy <= 2400 ) :
            ReturnVal = GetString(IACred.CertNumber, ( Copy )  - 2300)
        elif  ( Copy > 2400 )  and  ( Copy <= 2500 ) :
            ReturnVal = ''
    ReturnVal = ''

def NonRefCode_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    strindex = ( ( ( ( GetCopy() - 1 )  * 29 )  + 9 + Index )  * 4 )  + 1
    copystr = Trim(Mid(GetString(IA148Sp.NonRefCopiesStr), strindex, 4))
    if GetNumber(IA148Sp.NonRefNbr) == 10:
        ReturnVal = ''
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

def NonRefCr1_Calculation():
    PriorCopy = Long()

    PriorCopyTax = Currency()
    PriorCopy = GetCopy()
    PriorCopyTax = GetCurrency(IAWBP148Sp.NonRefTax30, PriorCopy - 1)
    if GetCopy() == 1:
        ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(0)), GetCurrency(IA148Sp.NonRefTax10))
    else:
        ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(0)), PriorCopyTax)

def NonRefCr10_Calculation():
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(9)), GetCurrency(IAWBP148Sp.NonRefTax10))

def NonRefCr11_Calculation():
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(10)), GetCurrency(IAWBP148Sp.NonRefTax11))

def NonRefCr12_Calculation():
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(11)), GetCurrency(IAWBP148Sp.NonRefTax12))

def NonRefCr13_Calculation():
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(12)), GetCurrency(IAWBP148Sp.NonRefTax13))

def NonRefCr14_Calculation():
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(13)), GetCurrency(IAWBP148Sp.NonRefTax14))

def NonRefCr15_Calculation():
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(14)), GetCurrency(IAWBP148Sp.NonRefTax15))

def NonRefCr16_Calculation():
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(15)), GetCurrency(IAWBP148Sp.NonRefTax16))

def NonRefCr17_Calculation():
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(16)), GetCurrency(IAWBP148Sp.NonRefTax17))

def NonRefCr18_Calculation():
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(17)), GetCurrency(IAWBP148Sp.NonRefTax18))

def NonRefCr19_Calculation():
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(18)), GetCurrency(IAWBP148Sp.NonRefTax19))

def NonRefCr2_Calculation():
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(1)), GetCurrency(IAWBP148Sp.NonRefTax2))

def NonRefCr20_Calculation():
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(19)), GetCurrency(IAWBP148Sp.NonRefTax20))

def NonRefCr21_Calculation():
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(20)), GetCurrency(IAWBP148Sp.NonRefTax21))

def NonRefCr22_Calculation():
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(21)), GetCurrency(IAWBP148Sp.NonRefTax22))

def NonRefCr23_Calculation():
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(22)), GetCurrency(IAWBP148Sp.NonRefTax23))

def NonRefCr24_Calculation():
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(23)), GetCurrency(IAWBP148Sp.NonRefTax24))

def NonRefCr25_Calculation():
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(24)), GetCurrency(IAWBP148Sp.NonRefTax25))

def NonRefCr26_Calculation():
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(25)), GetCurrency(IAWBP148Sp.NonRefTax26))

def NonRefCr27_Calculation():
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(26)), GetCurrency(IAWBP148Sp.NonRefTax27))

def NonRefCr28_Calculation():
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(27)), GetCurrency(IAWBP148Sp.NonRefTax28))

def NonRefCr29_Calculation():
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(28)), GetCurrency(IAWBP148Sp.NonRefTax29))

def NonRefCr3_Calculation():
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(2)), GetCurrency(IAWBP148Sp.NonRefTax3))

def NonRefCr4_Calculation():
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(3)), GetCurrency(IAWBP148Sp.NonRefTax4))

def NonRefCr5_Calculation():
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(4)), GetCurrency(IAWBP148Sp.NonRefTax5))

def NonRefCr6_Calculation():
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(5)), GetCurrency(IAWBP148Sp.NonRefTax6))

def NonRefCr7_Calculation():
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(6)), GetCurrency(IAWBP148Sp.NonRefTax7))

def NonRefCr8_Calculation():
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(7)), GetCurrency(IAWBP148Sp.NonRefTax8))

def NonRefCr9_Calculation():
    ReturnVal = MinValue(GetCurrency(IAWBP148Sp.AvailCr(8)), GetCurrency(IAWBP148Sp.NonRefTax9))

def NonRefTax10_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax9) - GetCurrency(IAWBP148Sp.NonRefCr9))

def NonRefTax11_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax10) - GetCurrency(IAWBP148Sp.NonRefCr10))

def NonRefTax12_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax11) - GetCurrency(IAWBP148Sp.NonRefCr11))

def NonRefTax13_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax12) - GetCurrency(IAWBP148Sp.NonRefCr12))

def NonRefTax14_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax13) - GetCurrency(IAWBP148Sp.NonRefCr13))

def NonRefTax15_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax14) - GetCurrency(IAWBP148Sp.NonRefCr14))

def NonRefTax16_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax15) - GetCurrency(IAWBP148Sp.NonRefCr15))

def NonRefTax17_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax16) - GetCurrency(IAWBP148Sp.NonRefCr16))

def NonRefTax18_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax17) - GetCurrency(IAWBP148Sp.NonRefCr17))

def NonRefTax19_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax18) - GetCurrency(IAWBP148Sp.NonRefCr18))

def NonRefTax2_Calculation():
    PriorCopy = Long()
    PriorCopy = GetCopy()
    if GetCopy() == 1:
        ReturnVal = MaxValue(0, GetCurrency(IA148Sp.NonRefTax10) - GetCurrency(IAWBP148Sp.NonRefCr1))
    else:
        ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax30, PriorCopy - 1) - GetCurrency(IAWBP148Sp.NonRefCr1))

def NonRefTax20_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax19) - GetCurrency(IAWBP148Sp.NonRefCr19))

def NonRefTax21_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax20) - GetCurrency(IAWBP148Sp.NonRefCr20))

def NonRefTax22_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax21) - GetCurrency(IAWBP148Sp.NonRefCr21))

def NonRefTax23_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax22) - GetCurrency(IAWBP148Sp.NonRefCr22))

def NonRefTax24_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax23) - GetCurrency(IAWBP148Sp.NonRefCr23))

def NonRefTax25_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax24) - GetCurrency(IAWBP148Sp.NonRefCr24))

def NonRefTax26_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax25) - GetCurrency(IAWBP148Sp.NonRefCr25))

def NonRefTax27_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax26) - GetCurrency(IAWBP148Sp.NonRefCr26))

def NonRefTax28_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax27) - GetCurrency(IAWBP148Sp.NonRefCr27))

def NonRefTax29_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax28) - GetCurrency(IAWBP148Sp.NonRefCr28))

def NonRefTax3_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax2) - GetCurrency(IAWBP148Sp.NonRefCr2))

def NonRefTax30_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax29) - GetCurrency(IAWBP148Sp.NonRefCr29))

def NonRefTax4_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax3) - GetCurrency(IAWBP148Sp.NonRefCr3))

def NonRefTax5_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax4) - GetCurrency(IAWBP148Sp.NonRefCr4))

def NonRefTax6_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax5) - GetCurrency(IAWBP148Sp.NonRefCr5))

def NonRefTax7_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax6) - GetCurrency(IAWBP148Sp.NonRefCr6))

def NonRefTax8_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax7) - GetCurrency(IAWBP148Sp.NonRefCr7))

def NonRefTax9_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAWBP148Sp.NonRefTax8) - GetCurrency(IAWBP148Sp.NonRefCr8))

def NonRefTrig_Calculation(Index):
    if GetString(IAWBP148Sp.NonRefCode(Index)) == '04' or GetString(IAWBP148Sp.NonRefCode(Index)) == '11' or GetString(IAWBP148Sp.NonRefCode(Index)) == '09':
        ReturnVal = 0
    elif GetCurrency(IAWBP148Sp.AvailCr(Index)) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Offset_Calculation():
    if GetCopy() == 1:
        ReturnVal = 9
    elif GetCopy() == 2:
        ReturnVal = 38
    else:
        ReturnVal = 67

def Print_Calculation():
    if GetCurrency(IAWBP148Sp.TotNonRefCr) > 0:
        ReturnVal = 1
    elif Trim(GetString(IAWBP148sp.NonRefCode(0))) != '' or GetCurrency(IAWBP148sp.CYCredit(0)) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def PTECode_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + GetNumber(IAWBP148Sp.Offset) + 1
    ReturnVal = GetString(IA148BumpSp.PTECode(Stuff))

def PTEEIN_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + GetNumber(IAWBP148Sp.Offset) + 1
    ReturnVal = GetString(IA148BumpSp.PTEEIN(Stuff))

def PTEName_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + GetNumber(IAWBP148Sp.Offset) + 1
    ReturnVal = GetString(IA148BumpSp.PTEName(Stuff))

def PTENRTrig_Calculation(Index):
    if GetString(IAWBP148Sp.NonRefCode(Index)) == '04' or GetString(IAWBP148Sp.PTECode(Index)) == '11' or GetString(IAWBP148Sp.PTECode(Index)) == '09':
        ReturnVal = 0
    elif Trim(GetString(IAWBP148Sp.PTEName(Index))) != '':
        ReturnVal = 1
    else:
        ReturnVal = 0

def PYCarry_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    strindex = ( ( ( ( GetCopy() - 1 )  * 29 )  + 9 + Index )  * 4 )  + 1
    copystr = Trim(Mid(GetString(IA148Sp.NonRefCopiesStr), strindex, 4))
    if GetNumber(IA148Sp.NonRefNbr) == 10:
        ReturnVal = 0
    elif copystr != '':
        Copy = CLng(copystr)
        if ( Copy > 100 )  and  ( Copy <= 200 ) :
            ReturnVal = 0
        elif  ( Copy > 200 )  and  ( Copy <= 300 ) :
            ReturnVal = 0
        elif  ( Copy > 300 )  and  ( Copy <= 400 ) :
            ReturnVal = GetCurrency(IACred.PYCarry, ( Copy )  - 300)
        elif  ( Copy > 400 )  and  ( Copy <= 500 ) :
            ReturnVal = GetCurrency(IACred.PYCarry, ( Copy )  - 400)
        elif  ( Copy > 500 )  and  ( Copy <= 600 ) :
            ReturnVal = GetCurrency(IACred.PYCarry, ( Copy )  - 500)
        elif  ( Copy > 600 )  and  ( Copy <= 700 ) :
            ReturnVal = GetCurrency(IACred.PYCarry, ( Copy )  - 600)
        elif  ( Copy > 700 )  and  ( Copy <= 800 ) :
            ReturnVal = GetCurrency(IACred.PYCarry, ( Copy )  - 700)
        elif  ( Copy > 800 )  and  ( Copy <= 900 ) :
            ReturnVal = GetCurrency(IACred.PYCarry, ( Copy )  - 800)
        elif  ( Copy > 900 )  and  ( Copy <= 1000 ) :
            ReturnVal = GetCurrency(IACred.PYCarry, ( Copy )  - 900)
        elif  ( Copy > 1000 )  and  ( Copy <= 1100 ) :
            ReturnVal = GetCurrency(IACred.PYCarry, ( Copy )  - 1000)
        elif  ( Copy > 1100 )  and  ( Copy <= 1200 ) :
            ReturnVal = GetCurrency(IACred.PYCarry, ( Copy )  - 1100)
        elif  ( Copy > 1200 )  and  ( Copy <= 1300 ) :
            ReturnVal = GetCurrency(IACred.PYCarry, ( Copy )  - 1200)
        elif  ( Copy > 1300 )  and  ( Copy <= 1400 ) :
            ReturnVal = GetCurrency(IACred.PYCarry, ( Copy )  - 1300)
        elif  ( Copy > 1400 )  and  ( Copy <= 1500 ) :
            ReturnVal = GetCurrency(IACred.PYCarry, ( Copy )  - 1400)
        elif  ( Copy > 1500 )  and  ( Copy <= 1600 ) :
            ReturnVal = GetCurrency(IACred.PYCarry, ( Copy )  - 1500)
        elif  ( Copy > 1600 )  and  ( Copy <= 1700 ) :
            ReturnVal = GetCurrency(IACred.PYCarry, ( Copy )  - 1600)
        elif  ( Copy > 1700 )  and  ( Copy <= 1800 ) :
            ReturnVal = GetCurrency(IACred.PYCarry, ( Copy )  - 1700)
        elif  ( Copy > 1800 )  and  ( Copy <= 1900 ) :
            ReturnVal = GetCurrency(IACred.PYCarry, ( Copy )  - 1800)
        elif  ( Copy > 1900 )  and  ( Copy <= 2000 ) :
            ReturnVal = GetCurrency(IACred.PYCarry, ( Copy )  - 1900)
        elif  ( Copy > 2000 )  and  ( Copy <= 2100 ) :
            ReturnVal = GetCurrency(IACred.PYCarry, ( Copy )  - 2000)
        elif  ( Copy > 2100 )  and  ( Copy <= 2200 ) :
            ReturnVal = GetCurrency(IACred.PYCarry, ( Copy )  - 2100)
        elif  ( Copy > 2200 )  and  ( Copy <= 2300 ) :
            ReturnVal = GetCurrency(IACred.PYCarry, ( Copy )  - 2200)
        elif  ( Copy > 2300 )  and  ( Copy <= 2400 ) :
            ReturnVal = GetCurrency(IACred.PYCarry, ( Copy )  - 2300)
        elif  ( Copy > 2400 )  and  ( Copy <= 2500 ) :
            ReturnVal = GetCurrency(IA8801Sp.PYCarryforward)
    ReturnVal = 0

def SSN_Calculation():
    ReturnVal = GetString(IA148Sp.SSN)

def TotNonRefCr_Calculation():
    NonRefCr1 = Currency()

    NonRefCr2 = Currency()

    NonRefCr3 = Currency()
    NonRefCr1 = GetCurrency(IAWBP148Sp.NonRefCr1) + GetCurrency(IAWBP148Sp.NonRefCr2) + GetCurrency(IAWBP148Sp.NonRefCr3) + GetCurrency(IAWBP148Sp.NonRefCr4) + GetCurrency(IAWBP148Sp.NonRefCr5) + GetCurrency(IAWBP148Sp.NonRefCr6) + GetCurrency(IAWBP148Sp.NonRefCr7) + GetCurrency(IAWBP148Sp.NonRefCr8) + GetCurrency(IAWBP148Sp.NonRefCr9) + GetCurrency(IAWBP148Sp.NonRefCr10)
    NonRefCr2 = GetCurrency(IAWBP148Sp.NonRefCr11) + GetCurrency(IAWBP148Sp.NonRefCr12) + GetCurrency(IAWBP148Sp.NonRefCr13) + GetCurrency(IAWBP148Sp.NonRefCr14) + GetCurrency(IAWBP148Sp.NonRefCr15) + GetCurrency(IAWBP148Sp.NonRefCr16) + GetCurrency(IAWBP148Sp.NonRefCr17) + GetCurrency(IAWBP148Sp.NonRefCr18) + GetCurrency(IAWBP148Sp.NonRefCr19) + GetCurrency(IAWBP148Sp.NonRefCr20)
    NonRefCr3 = GetCurrency(IAWBP148Sp.NonRefCr21) + GetCurrency(IAWBP148Sp.NonRefCr22) + GetCurrency(IAWBP148Sp.NonRefCr23) + GetCurrency(IAWBP148Sp.NonRefCr24) + GetCurrency(IAWBP148Sp.NonRefCr25) + GetCurrency(IAWBP148Sp.NonRefCr26) + GetCurrency(IAWBP148Sp.NonRefCr27) + GetCurrency(IAWBP148Sp.NonRefCr28) + GetCurrency(IAWBP148Sp.NonRefCr29)
    ReturnVal = NonRefCr1 + NonRefCr2 + NonRefCr3

def TPPerc_Calculation(Index):
    Stuff = Integer()
    Stuff = Index + GetNumber(IAWBP148Sp.Offset) + 1
    ReturnVal = GetFloat(IA148BumpSp.TPPerc(Stuff))

