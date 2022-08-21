from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def ArrayNonRefCr_Calculation(Index):
    if Index == 0:
        ReturnVal = GetCurrency(IA148Sp.NonRefCr1)
    elif Index == 1:
        ReturnVal = GetCurrency(IA148Sp.NonRefCr2)
    elif Index == 2:
        ReturnVal = GetCurrency(IA148Sp.NonRefCr3)
    elif Index == 3:
        ReturnVal = GetCurrency(IA148Sp.NonRefCr4)
    elif Index == 4:
        ReturnVal = GetCurrency(IA148Sp.NonRefCr5)
    elif Index == 5:
        ReturnVal = GetCurrency(IA148Sp.NonRefCr6)
    elif Index == 6:
        ReturnVal = GetCurrency(IA148Sp.NonRefCr7)
    elif Index == 7:
        ReturnVal = GetCurrency(IA148Sp.NonRefCr8)
    elif Index == 8:
        ReturnVal = GetCurrency(IA148Sp.NonRefCr9)
    else:
        ReturnVal = GetCurrency(IA148Sp.NonRefCr10)

def AvailCr_Calculation(Index):
    if GetString(IA148Sp.NonRefCode(Index)) == '09':
        ReturnVal = GetCurrency(IA8801Sp.AMTCR)
    else:
        ReturnVal = GetCurrency(IA148Sp.PYCarry(Index)) + GetCurrency(IA148Sp.CYCredit(Index))

def CreateBPNonRef1_Calculation():
    if GetNumber(IA148Sp.NonRefNbr) > 10:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CreateBPNonRef2_Calculation():
    if GetNumber(IA148Sp.NonRefNbr) > 38:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CreateBPNonRef3_Calculation():
    if GetNumber(IA148Sp.NonRefNbr) > 67:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CreateBPNonRef4_Calculation():
    if GetNumber(IA148Sp.NonRefNbr) > 96:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CreateBPPTE1_Calculation():
    if GetNumber(IA148Sp.TotPTE) > 6:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CreateBPPTE2_Calculation():
    if GetNumber(IA148Sp.TotPTE) > 35:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CreateBPPTE3_Calculation():
    if GetNumber(IA148Sp.TotPTE) > 65:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CreateBPPTE4_Calculation():
    if GetNumber(IA148Sp.TotPTE) > 95:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CreateBPPTE5_Calculation():
    if GetNumber(IA148Sp.TotPTE) > 125:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CreateBPRef1_Calculation():
    if GetNumber(IA148Sp.RefNbr) > 7:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CreateBPRef2_Calculation():
    if GetNumber(IA148Sp.RefNbr) > 56:
        ReturnVal = 1
    else:
        ReturnVal = 0

def CYCarry_Calculation(Index):
    if GetString(IA148Sp.NonRefCode(Index)) == '09':
        ReturnVal = GetCurrency(IA8801Sp.CYCarryforward)
    else:
        ReturnVal = MaxValue(0, GetCurrency(IA148Sp.AvailCr(Index)) - GetCurrency(IA148Sp.ArrayNonRefCr(Index)) - GetCurrency(IA148Sp.ExpCr(Index)))

def CYCredit_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    strindex = ( ( Index )  * 4 )  + 1
    copystr = Trim(Mid(GetString(IA148Sp.NonRefCopiesStr), strindex, 4))
    if Index == 9 and GetNumber(IA148Sp.NonRefNbr) > 10:
        ReturnVal = 0
    elif copystr != '':
        Copy = CLng(copystr)
        if ( Copy > 100 )  and  ( Copy <= 200 ) :
            ReturnVal = GetCurrency(IA147.FranchiseCr, ( Copy )  - 100)
        elif  ( Copy > 200 )  and  ( Copy <= 300 ) :
            ReturnVal = GetCurrency(IA134Sp.Credit, ( Copy )  - 200)
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

    Total2 = Currency()
    Total1 = GetCurrency(IA148Sp.TotNonRefCr)
    Total2 = GetCurrency(IA148Sp.TotRefCr)
    if Total1 > 0 and Total2 == 0:
        ReturnVal = CStr(Total1) + ' Nonrefundable Credits'
    elif Total1 == 0 and Total2 > 0:
        ReturnVal = CStr(Total2) + ' Refundable Credits'
    elif Total1 > 0 and Total2 > 0:
        ReturnVal = CStr(Total1) + ' Nonrefundable Credits ' + CStr(Total2) + ' Refundable Credits'
    else:
        ReturnVal = CStr(Total1) + ' Credits'

def ExpCr_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    strindex = ( ( Index )  * 4 )  + 1
    copystr = Trim(Mid(GetString(IA148Sp.NonRefCopiesStr), strindex, 4))
    if Index == 9 and GetNumber(IA148Sp.NonRefNbr) > 10:
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

def FirstCopy137Site_Calculation():
    count = Long()

    max = Long()
    max = GetAllCopies(IA137)
    count = 0
    while count < max:
        count = count + 1
        if GetBool(IA137.Spouse, count) == True and GetBool(IA137.Site, count) == True and GetCurrency(IA137.TotEthSoldCr, count) > 0:
            ReturnVal = count
        else:
            count = count
    ReturnVal = 0

def Names_Calculation():
    ReturnVal = GetString(IARequired.SPCombName)

def NonRefCert_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    strindex = ( ( Index )  * 4 )  + 1
    copystr = Trim(Mid(GetString(IA148Sp.NonRefCopiesStr), strindex, 4))
    if Index == 9 and GetNumber(IA148Sp.NonRefNbr) > 10:
        ReturnVal = 'Stmt Att.'
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
    strindex = ( ( Index )  * 4 )  + 1
    copystr = Trim(Mid(GetString(IA148Sp.NonRefCopiesStr), strindex, 4))
    if Index == 9 and GetNumber(IA148Sp.NonRefNbr) > 10:
        ReturnVal = 'See'
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

def NonRefCopiesStr_Calculation():
    Copy = Long()

    Copy2 = Long()

    Copy3 = Long()

    Copy4 = Long()

    Copy5 = Long()

    Copy6 = Long()

    Copy7 = Long()

    Copy8 = Long()

    Copy9 = Long()

    Copy10 = Long()

    Copy11 = Long()

    Copy12 = Long()

    Copy13 = Long()

    Copy14 = Long()

    Copy15 = Long()

    Copy16 = Long()

    Copy17 = Long()

    Copy18 = Long()

    Copy19 = Long()

    Copy20 = Long()

    Copy21 = Long()

    Copy22 = Long()

    Copy23 = Long()

    Copy24 = Long()

    max = Long()

    max2 = Long()

    max3 = Long()

    max4 = Long()

    copystr = String()

    copystr2 = String()

    copystr3 = String()

    copystr4 = String()

    copystr5 = String()

    copystr6 = String()

    copystr7 = String()

    copystr8 = String()

    copystr9 = String()

    copystr10 = String()

    copystr11 = String()

    copystr12 = String()

    copystr13 = String()

    copystr14 = String()

    copystr15 = String()

    copystr16 = String()

    copystr17 = String()

    copystr18 = String()

    copystr19 = String()

    copystr20 = String()

    copystr21 = String()

    copystr22 = String()

    copystr23 = String()

    copystr24 = String()

    copiesstr = String()

    copiesstr2 = String()

    copiesstr3 = String()

    copiesstr4 = String()

    copiesstr5 = String()

    copiesstr6 = String()

    copiesstr7 = String()

    copiesstr8 = String()

    copiesstr9 = String()

    copiesstr10 = String()

    copiesstr11 = String()

    copiesstr12 = String()

    copiesstr13 = String()

    copiesstr14 = String()

    copiesstr15 = String()

    copiesstr16 = String()

    copiesstr17 = String()

    copiesstr18 = String()

    copiesstr19 = String()

    copiesstr20 = String()

    copiesstr21 = String()

    copiesstr22 = String()

    copiesstr23 = String()

    copiesstr24 = String()
    #2017 removed credit codes 18 and 19 which were in credit order #10 and #11, re-used Copy10, Copystr10 and copiesstr10 for new credit code #28 and put it last in the order since no new IA Admin Rule is out, left copy11, copystr11 and copiesstr11 for future use
    copiesstr = ''
    Copy = 1
    max = GetAllCopies(IA147)
    while Copy <= max:
        if GetCurrency(IA147.FranchiseCr, Copy) > 0:
            if GetCurrency(IA147.FranchiseCr, Copy) > 0 and GetBool(IA147.Spouse, Copy) == True:
                copystr = CStr(Copy + 100)
                while Len(copystr) < 4:
                    copystr = copystr + ' '
                copiesstr = copiesstr + copystr
        Copy = Copy + 1
    copiesstr2 = ''
    Copy2 = 1
    max2 = GetAllCopies(IA134Sp)
    while Copy2 <= max2:
        if GetCurrency(IA134Sp.Credit, Copy2) > 0:
            if GetCurrency(IA134Sp.Credit, Copy2) > 0:
                copystr2 = CStr(Copy2 + 200) + ' '
                copiesstr2 = copiesstr2 + copystr2
        Copy2 = Copy2 + 1
    max3 = GetAllCopies(IACred)
    copiesstr3 = ''
    copiesstr4 = ''
    copiesstr5 = ''
    copiesstr6 = ''
    copiesstr7 = ''
    copiesstr8 = ''
    copiesstr9 = ''
    copiesstr10 = ''
    copiesstr11 = ''
    copiesstr12 = ''
    copiesstr13 = ''
    copiesstr14 = ''
    copiesstr15 = ''
    copiesstr16 = ''
    copiesstr17 = ''
    copiesstr18 = ''
    copiesstr19 = ''
    copiesstr20 = ''
    copiesstr21 = ''
    copiesstr22 = ''
    copiesstr23 = ''
    copiesstr24 = ''
    Copy3 = 1
    Copy4 = 1
    Copy5 = 1
    Copy6 = 1
    Copy7 = 1
    Copy8 = 1
    Copy9 = 1
    Copy10 = 1
    Copy11 = 1
    Copy12 = 1
    Copy13 = 1
    Copy14 = 1
    Copy15 = 1
    Copy16 = 1
    Copy17 = 1
    Copy18 = 1
    Copy19 = 1
    Copy20 = 1
    Copy21 = 1
    Copy22 = 1
    Copy23 = 1
    while Copy3 <= max3:
        if GetString(IACred.Code, Copy3) == '12':
            if GetBool(IACred.NonRefCr, Copy3) == True and GetBool(IACred.Spouse, Copy3) == True and GetString(IACred.Code, Copy3) == '12':
                copystr3 = CStr(Copy3 + 300) + ' '
                copiesstr3 = copiesstr3 + copystr3
        Copy3 = Copy3 + 1
    while Copy4 <= max3:
        if GetString(IACred.Code, Copy4) == '14':
            if GetBool(IACred.NonRefCr, Copy4) == True and GetBool(IACred.Spouse, Copy4) == True and GetString(IACred.Code, Copy4) == '14':
                copystr4 = CStr(Copy4 + 400) + ' '
                copiesstr4 = copiesstr4 + copystr4
        Copy4 = Copy4 + 1
    while Copy5 <= max3:
        if GetString(IACred.Code, Copy5) == '15':
            if GetBool(IACred.NonRefCr, Copy5) == True and GetBool(IACred.Spouse, Copy5) == True and GetString(IACred.Code, Copy5) == '15':
                copystr5 = CStr(Copy5 + 500) + ' '
                copiesstr5 = copiesstr5 + copystr5
        Copy5 = Copy5 + 1
    while Copy6 <= max3:
        if GetString(IACred.Code, Copy6) == '25':
            if GetBool(IACred.NonRefCr, Copy6) == True and GetBool(IACred.Spouse, Copy6) == True and GetString(IACred.Code, Copy6) == '25':
                copystr6 = CStr(Copy6 + 600) + ' '
                copiesstr6 = copiesstr6 + copystr6
        Copy6 = Copy6 + 1
    while Copy7 <= max3:
        if GetString(IACred.Code, Copy7) == '03':
            if GetBool(IACred.NonRefCr, Copy7) == True and GetBool(IACred.Spouse, Copy7) == True and GetString(IACred.Code, Copy7) == '03':
                copystr7 = CStr(Copy7 + 700) + ' '
                copiesstr7 = copiesstr7 + copystr7
        Copy7 = Copy7 + 1
    while Copy8 <= max3:
        if GetString(IACred.Code, Copy8) == '17':
            if GetBool(IACred.NonRefCr, Copy8) == True and GetBool(IACred.Spouse, Copy8) == True and GetString(IACred.Code, Copy8) == '17':
                copystr8 = CStr(Copy8 + 800) + ' '
                copiesstr8 = copiesstr8 + copystr8
        Copy8 = Copy8 + 1
    while Copy9 <= max3:
        if GetString(IACred.Code, Copy9) == '24':
            if GetBool(IACred.NonRefCr, Copy9) == True and GetBool(IACred.Spouse, Copy9) == True and GetString(IACred.Code, Copy9) == '24':
                copystr9 = CStr(Copy9 + 900) + ' '
                copiesstr9 = copiesstr9 + copystr9
        Copy9 = Copy9 + 1
    while Copy10 <= max3:
        if GetString(IACred.Code, Copy10) == '28':
            if GetBool(IACred.NonRefCr, Copy10) == True and GetBool(IACred.Spouse, Copy10) == True and GetString(IACred.Code, Copy10) == '28':
                copystr10 = CStr(Copy10 + 1000)
                copiesstr10 = copiesstr10 + copystr10
        Copy10 = Copy10 + 1
    while Copy12 <= max3:
        if GetString(IACred.Code, Copy12) == '21':
            if GetBool(IACred.NonRefCr, Copy12) == True and GetBool(IACred.Spouse, Copy12) == True and GetString(IACred.Code, Copy12) == '21':
                copystr12 = CStr(Copy12 + 1200)
                copiesstr12 = copiesstr12 + copystr12
        Copy12 = Copy12 + 1
    while Copy13 <= max3:
        if GetString(IACred.Code, Copy13) == '26':
            if GetBool(IACred.NonRefCr, Copy13) == True and GetBool(IACred.Spouse, Copy13) == True and GetString(IACred.Code, Copy13) == '26':
                copystr13 = CStr(Copy13 + 1300)
                copiesstr13 = copiesstr13 + copystr13
        Copy13 = Copy13 + 1
    while Copy14 <= max3:
        if GetString(IACred.Code, Copy14) == '06':
            if GetBool(IACred.NonRefCr, Copy14) == True and GetBool(IACred.Spouse, Copy14) == True and GetString(IACred.Code, Copy14) == '06':
                copystr14 = CStr(Copy14 + 1400)
                copiesstr14 = copiesstr14 + copystr14
        Copy14 = Copy14 + 1
    while Copy15 <= max3:
        if GetString(IACred.Code, Copy15) == '07':
            if GetBool(IACred.NonRefCr, Copy15) == True and GetBool(IACred.Spouse, Copy15) == True and GetString(IACred.Code, Copy15) == '07':
                copystr15 = CStr(Copy15 + 1500)
                copiesstr15 = copiesstr15 + copystr15
        Copy15 = Copy15 + 1
    while Copy16 <= max3:
        if GetString(IACred.Code, Copy16) == '27':
            if GetBool(IACred.NonRefCr, Copy16) == True and GetBool(IACred.Spouse, Copy16) == True and GetString(IACred.Code, Copy16) == '27':
                copystr16 = CStr(Copy16 + 1600)
                copiesstr16 = copiesstr16 + copystr16
        Copy16 = Copy16 + 1
    while Copy17 <= max3:
        if GetString(IACred.Code, Copy17) == '16':
            if GetBool(IACred.NonRefCr, Copy17) == True and GetBool(IACred.Spouse, Copy17) == True and GetString(IACred.Code, Copy17) == '16':
                copystr17 = CStr(Copy17 + 1700)
                copiesstr17 = copiesstr17 + copystr17
        Copy17 = Copy17 + 1
    while Copy18 <= max3:
        if GetString(IACred.Code, Copy18) == '10':
            if GetBool(IACred.NonRefCr, Copy18) == True and GetBool(IACred.Spouse, Copy18) == True and GetString(IACred.Code, Copy18) == '10':
                copystr18 = CStr(Copy18 + 1800)
                copiesstr18 = copiesstr18 + copystr18
        Copy18 = Copy18 + 1
    while Copy19 <= max3:
        if GetString(IACred.Code, Copy19) == '13':
            if GetBool(IACred.NonRefCr, Copy19) == True and GetBool(IACred.Spouse, Copy19) == True and GetString(IACred.Code, Copy19) == '13':
                copystr19 = CStr(Copy19 + 1900)
                copiesstr19 = copiesstr19 + copystr19
        Copy19 = Copy19 + 1
    while Copy20 <= max3:
        if GetString(IACred.Code, Copy20) == '08':
            if GetBool(IACred.NonRefCr, Copy20) == True and GetBool(IACred.Spouse, Copy20) == True and GetString(IACred.Code, Copy20) == '08':
                copystr20 = CStr(Copy20 + 2000)
                copiesstr20 = copiesstr20 + copystr20
        Copy20 = Copy20 + 1
    while Copy21 <= max3:
        if GetString(IACred.Code, Copy21) == '23':
            if GetBool(IACred.NonRefCr, Copy21) == True and GetBool(IACred.Spouse, Copy21) == True and GetString(IACred.Code, Copy21) == '23':
                copystr21 = CStr(Copy21 + 2100)
                copiesstr21 = copiesstr21 + copystr21
        Copy21 = Copy21 + 1
    while Copy22 <= max3:
        if GetString(IACred.Code, Copy22) == '22':
            if GetBool(IACred.NonRefCr, Copy22) == True and GetBool(IACred.Spouse, Copy22) == True and GetString(IACred.Code, Copy22) == '22':
                copystr22 = CStr(Copy22 + 2200)
                copiesstr22 = copiesstr22 + copystr22
        Copy22 = Copy22 + 1
    while Copy23 <= max3:
        if GetString(IACred.Code, Copy23) == '20':
            if GetBool(IACred.NonRefCr, Copy23) == True and GetBool(IACred.Spouse, Copy23) == True and GetString(IACred.Code, Copy23) == '20':
                copystr23 = CStr(Copy23 + 2300)
                copiesstr23 = copiesstr23 + copystr23
        Copy23 = Copy23 + 1
    copiesstr24 = ''
    Copy24 = 1
    max4 = GetAllCopies(IA8801Sp)
    while Copy24 <= max4:
        if GetCurrency(IA8801Sp.Print, Copy24) > 0:
            if GetCurrency(IA8801Sp.Print, Copy24) > 0:
                copystr24 = CStr(Copy24 + 2400)
                copiesstr24 = copiesstr24 + copystr24
        Copy24 = Copy24 + 1
    ReturnVal = copiesstr + copiesstr2 + copiesstr3 + copiesstr4 + copiesstr5 + copiesstr7 + copiesstr12 + copiesstr13 + copiesstr16 + copiesstr14 + copiesstr15 + copiesstr17 + copiesstr18 + copiesstr19 + copiesstr20 + copiesstr6 + copiesstr8 + copiesstr9 + copiesstr21 + copiesstr22 + copiesstr23 + copiesstr24 + copiesstr10

def NonRefCr1_Calculation():
    ReturnVal = MinValue(GetCurrency(IA148Sp.AvailCr(0)), GetCurrency(IAF1040.BBal3))

def NonRefCr10_Calculation():
    if GetNumber(IA148Sp.NonRefNbr) > 10:
        ReturnVal = GetCurrency(IAWBP148Sp.TotNonRefCr)
    else:
        ReturnVal = MinValue(GetCurrency(IA148Sp.AvailCr(9)), GetCurrency(IA148Sp.NonRefTax10))

def NonRefCr2_Calculation():
    ReturnVal = MinValue(GetCurrency(IA148Sp.AvailCr(1)), GetCurrency(IA148Sp.NonRefTax2))

def NonRefCr3_Calculation():
    ReturnVal = MinValue(GetCurrency(IA148Sp.AvailCr(2)), GetCurrency(IA148Sp.NonRefTax3))

def NonRefCr4_Calculation():
    ReturnVal = MinValue(GetCurrency(IA148Sp.AvailCr(3)), GetCurrency(IA148Sp.NonRefTax4))

def NonRefCr5_Calculation():
    ReturnVal = MinValue(GetCurrency(IA148Sp.AvailCr(4)), GetCurrency(IA148Sp.NonRefTax5))

def NonRefCr6_Calculation():
    ReturnVal = MinValue(GetCurrency(IA148Sp.AvailCr(5)), GetCurrency(IA148Sp.NonRefTax6))

def NonRefCr7_Calculation():
    ReturnVal = MinValue(GetCurrency(IA148Sp.AvailCr(6)), GetCurrency(IA148Sp.NonRefTax7))

def NonRefCr8_Calculation():
    ReturnVal = MinValue(GetCurrency(IA148Sp.AvailCr(7)), GetCurrency(IA148Sp.NonRefTax8))

def NonRefCr9_Calculation():
    ReturnVal = MinValue(GetCurrency(IA148Sp.AvailCr(8)), GetCurrency(IA148Sp.NonRefTax9))

def NonRefNbr_Calculation():
    count2 = Integer()

    Lim2 = Integer()

    Total = Integer()

    count3 = Integer()

    Lim3 = Integer()

    count = Integer()

    Lim = Integer()

    IACredit = String()
    Lim2 = GetAllCopies(IA147)
    count2 = 1
    Total = 0
    while count2 <= Lim2:
        if GetBool(IA147.Spouse, count2) == True and GetCurrency(IA147.FranchiseCr, count2) > 0:
            Total = Total + 1
        else:
            Total = Total
        count2 = count2 + 1
    Lim3 = GetAllCopies(IA134Sp)
    count3 = 1
    while count3 <= Lim3:
        if GetCurrency(IA134Sp.Credit, count3) > 0:
            Total = Total + 1
        else:
            Total = Total
        count3 = count3 + 1
    Lim = GetAllCopies(IACred)
    count = 1
    while count <= Lim:
        IACredit = GetString(IACred.Code, count)
        if GetBool(IACred.NonRefCr, count) == True and GetBool(IACred.Spouse, count) == True and  ( IACredit == '12' or IACredit == '14' or IACredit == '15' or IACredit == '25' or IACredit == '03' or IACredit == '17' or IACredit == '24' or IACredit == '21' or IACredit == '26' or IACredit == '06' or IACredit == '07' or IACredit == '27' or IACredit == '16' or IACredit == '10' or IACredit == '13' or IACredit == '08' or IACredit == '23' or IACredit == '22' or IACredit == '20' or IACredit == '28' ) :
            Total = Total + 1
        else:
            Total = Total
        count = count + 1
    ReturnVal = Total + GetBool(IA8801Sp.Print)

def NonRefTax10_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA148Sp.NonRefTax9) - GetCurrency(IA148Sp.NonRefCr9))

def NonRefTax2_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IAF1040.BBal3) - GetCurrency(IA148Sp.NonRefCr1))

def NonRefTax3_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA148Sp.NonRefTax2) - GetCurrency(IA148Sp.NonRefCr2))

def NonRefTax4_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA148Sp.NonRefTax3) - GetCurrency(IA148Sp.NonRefCr3))

def NonRefTax5_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA148Sp.NonRefTax4) - GetCurrency(IA148Sp.NonRefCr4))

def NonRefTax6_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA148Sp.NonRefTax5) - GetCurrency(IA148Sp.NonRefCr5))

def NonRefTax7_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA148Sp.NonRefTax6) - GetCurrency(IA148Sp.NonRefCr6))

def NonRefTax8_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA148Sp.NonRefTax7) - GetCurrency(IA148Sp.NonRefCr7))

def NonRefTax9_Calculation():
    ReturnVal = MaxValue(0, GetCurrency(IA148Sp.NonRefTax8) - GetCurrency(IA148Sp.NonRefCr8))

def NonRefTrig_Calculation(Index):
    if GetString(IA148Sp.NonRefCode(Index)) == '04' or GetString(IA148Sp.NonRefCode(Index)) == '11' or GetString(IA148Sp.NonRefCode(Index)) == '09':
        ReturnVal = 0
    elif GetCurrency(IA148Sp.AvailCr(Index)) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Print_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 10:
        SubTot = SubTot + GetCurrency(IA148Sp.CYCarry(count))
        count = count + 1
    if GetBool(IAF1040.CombMFS) == False:
        ReturnVal = 0
    elif GetCurrency(IA148Sp.TotNonRefCr) > 0 or GetCurrency(IA148Sp.TotRefCr) > 0:
        ReturnVal = 1
    elif SubTot > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def PTEEIN_Calculation(Index):
    PTE = Integer()

    RefPTE = Integer()

    Stuff = Integer()

    Stuff2 = Integer()
    PTE = GetNumber(IA148BumpSp.TotPTE)
    RefPTE = GetNumber(IA148BumpSp.TotRefPTE)
    if Index == 5 and GetNumber(IA148Sp.TotPTE) > 6:
        ReturnVal = ''
    elif PTE > Index:
        Stuff2 = GetNumber(IA148BumpSp.PTEIndexNbr(Index))
        ReturnVal = GetString(IA148BumpSp.PTEEIN(Stuff2))
    elif PTE + RefPTE > Index:
        Stuff = ( Index )  - PTE
        Stuff2 = GetNumber(IA148BumpSp.RefPTEIndexNbr(Stuff))
        ReturnVal = GetString(IA148BumpSp.RefPTEEIN(Stuff2))
    else:
        ReturnVal = ''

def PTELine_Calculation(Index):
    PTE = Integer()

    RefPTE = Integer()

    Stuff = Integer()

    Stuff2 = Integer()
    PTE = GetNumber(IA148BumpSp.TotPTE)
    RefPTE = GetNumber(IA148BumpSp.TotRefPTE)
    if Index == 5 and GetNumber(IA148Sp.TotPTE) > 6:
        ReturnVal = ''
    elif PTE > Index:
        Stuff2 = GetNumber(IA148BumpSp.PTEIndexNbr(Index))
        ReturnVal = GetString(IA148BumpSp.PTELine(Stuff2))
    elif PTE + RefPTE > Index:
        Stuff = ( Index )  - PTE
        Stuff2 = GetNumber(IA148BumpSp.RefPTEIndexNbr(Stuff))
        ReturnVal = GetString(IA148BumpSp.RefPTELine(Stuff2))
    else:
        ReturnVal = ''

def PTEName_Calculation(Index):
    PTE = Integer()

    RefPTE = Integer()

    Stuff = Integer()

    Stuff2 = Integer()
    PTE = GetNumber(IA148BumpSp.TotPTE)
    RefPTE = GetNumber(IA148BumpSp.TotRefPTE)
    if Index == 5 and GetNumber(IA148Sp.TotPTE) > 6:
        ReturnVal = 'See Statement Attached'
    elif PTE > Index:
        Stuff2 = GetNumber(IA148BumpSp.PTEIndexNbr(Index))
        ReturnVal = GetString(IA148BumpSp.PTEName(Stuff2))
    elif PTE + RefPTE > Index:
        Stuff = ( Index )  - PTE
        Stuff2 = GetNumber(IA148BumpSp.RefPTEIndexNbr(Stuff))
        ReturnVal = GetString(IA148BumpSp.RefPTEName(Stuff2))
    else:
        ReturnVal = ''

def PYCarry_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    strindex = ( ( Index )  * 4 )  + 1
    copystr = Trim(Mid(GetString(IA148Sp.NonRefCopiesStr), strindex, 4))
    if Index == 9 and GetNumber(IA148Sp.NonRefNbr) > 10:
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

def RefCert_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    strindex = ( ( Index )  * 4 )  + 1
    copystr = Trim(Mid(GetString(IA148Sp.RefCopiesStr), strindex, 4))
    if Index == 6 and GetNumber(IA148Sp.RefNbr) > 7:
        ReturnVal = 'See Statement Attached'
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
    strindex = ( ( Index )  * 4 )  + 1
    copystr = Trim(Mid(GetString(IA148Sp.RefCopiesStr), strindex, 4))
    if Index == 6 and GetNumber(IA148Sp.RefNbr) > 7:
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

def RefCopiesStr_Calculation():
    Copy = Long()

    Copy2 = Long()

    Copy3 = Long()

    Copy4 = Long()

    Copy5 = Long()

    Copy6 = Long()

    Copy7 = Long()

    Copy8 = Long()

    Copy9 = Long()

    Copy10 = Long()

    Copy11 = Long()

    Copy12 = Long()

    Copy13 = Long()

    Copy14 = Long()

    max = Long()

    max2 = Long()

    max3 = Long()

    max5 = Long()

    max6 = Long()

    max9 = Long()

    max10 = Long()

    max11 = Long()

    max12 = Long()

    max13 = Long()

    max14 = Long()

    copystr = String()

    copystr2 = String()

    copystr3 = String()

    copystr4 = String()

    copystr5 = String()

    copystr6 = String()

    copystr7 = String()

    copystr8 = String()

    copystr9 = String()

    copystr10 = String()

    copystr11 = String()

    copystr12 = String()

    copystr13 = String()

    copystr14 = String()

    copiesstr = String()

    copiesstr2 = String()

    copiesstr3 = String()

    copiesstr4 = String()

    copiesstr5 = String()

    copiesstr6 = String()

    copiesstr7 = String()

    copiesstr8 = String()

    copiesstr9 = String()

    copiesstr10 = String()

    copiesstr11 = String()

    copiesstr12 = String()

    copiesstr13 = String()

    copiesstr14 = String()
    copiesstr = ''
    Copy = 1
    max = GetAllCopies(IA8864)
    while Copy <= max:
        if GetCurrency(IA8864.BiodieselCr, Copy) > 0:
            if GetCurrency(IA8864.BiodieselCr, Copy) > 0 and GetBool(IA8864.Spouse, Copy) == True:
                copystr = CStr(Copy + 100)
                while Len(copystr) < 4:
                    copystr = copystr + ' '
                copiesstr = copiesstr + copystr
        Copy = Copy + 1
    copiesstr2 = ''
    Copy2 = 1
    max2 = GetAllCopies(IACred)
    while Copy2 <= max2:
        if GetString(IACred.Code, Copy2) == '53':
            if GetBool(IACred.RefCr, Copy2) == True and GetBool(IACred.Spouse, Copy2) == True and GetString(IACred.Code, Copy2) == '53':
                copystr2 = CStr(Copy2 + 200) + ' '
                copiesstr2 = copiesstr2 + copystr2
        Copy2 = Copy2 + 1
    copiesstr3 = ''
    Copy3 = 1
    max3 = GetAllCopies(IA135)
    while Copy3 <= max3:
        if GetCurrency(IA135.E85Credit, Copy3) > 0:
            if GetBool(IA135.Spouse, Copy3) == True and GetCurrency(IA135.E85Credit, Copy3) > 0:
                copystr3 = CStr(Copy3 + 300) + ' '
                copiesstr3 = copiesstr3 + copystr3
        Copy3 = Copy3 + 1
    copiesstr4 = ''
    Copy4 = 1
    while Copy4 <= max2:
        if GetString(IACred.Code, Copy4) == '56':
            if GetBool(IACred.RefCr, Copy4) == True and GetBool(IACred.Spouse, Copy4) == True and GetString(IACred.Code, Copy4) == '56':
                copystr4 = CStr(Copy4 + 400) + ' '
                copiesstr4 = copiesstr4 + copystr4
        Copy4 = Copy4 + 1
    copiesstr5 = ''
    Copy5 = 1
    max5 = GetAllCopies(IA128)
    while Copy5 <= max5:
        if GetCurrency(IA128.TotResearchCr, Copy5) > 0:
            if GetBool(IA128.Spouse, Copy5) == True and GetCurrency(IA128.TotResearchCr, Copy5) > 0:
                copystr5 = CStr(Copy5 + 500) + ' '
                copiesstr5 = copiesstr5 + copystr5
        Copy5 = Copy5 + 1
    copiesstr6 = ''
    Copy6 = 1
    max6 = GetAllCopies(IA128S)
    while Copy6 <= max6:
        if GetCurrency(IA128S.TotResearchCr, Copy6) > 0:
            if GetBool(IA128S.Spouse, Copy6) == True and GetCurrency(IA128S.TotResearchCr, Copy6) > 0:
                copystr6 = CStr(Copy6 + 600) + ' '
                copiesstr6 = copiesstr6 + copystr6
        Copy6 = Copy6 + 1
    copiesstr7 = ''
    Copy7 = 1
    while Copy7 <= max5:
        if GetCurrency(IA128.TotSuppResearchCr, Copy7) > 0:
            if GetBool(IA128.Spouse, Copy7) == True and GetCurrency(IA128.TotSuppResearchCr, Copy7) > 0:
                copystr7 = CStr(Copy7 + 700) + ' '
                copiesstr7 = copiesstr7 + copystr7
        Copy7 = Copy7 + 1
    copiesstr8 = ''
    Copy8 = 1
    while Copy8 <= max6:
        if GetCurrency(IA128S.TotSuppResearchCr, Copy8) > 0:
            if GetBool(IA128S.Spouse, Copy8) == True and GetCurrency(IA128S.TotSuppResearchCr, Copy8) > 0:
                copystr8 = CStr(Copy8 + 800) + ' '
                copiesstr8 = copiesstr8 + copystr8
        Copy8 = Copy8 + 1
    copiesstr9 = ''
    Copy9 = 1
    max9 = GetAllCopies(IA137)
    ## VB2PY (CheckDirective) VB directive took path 1 on INDCALC
    while Copy9 <= max9:
        if GetCurrency(IA137.EthPromoteCr, Copy9) > 0:
            if GetBool(IA137.Spouse, Copy9) == True and GetCurrency(IA137.EthPromoteCr, Copy9) > 0:
                copystr9 = CStr(Copy9 + 900) + ' '
                copiesstr9 = copiesstr9 + copystr9
        Copy9 = Copy9 + 1
    copiesstr10 = ''
    Copy10 = 1
    max10 = GetAllCopies(IA138)
    while Copy10 <= max10:
        if GetCurrency(IA138.E15Credit, Copy10) > 0:
            if GetBool(IA138.Spouse, Copy10) == True and GetCurrency(IA138.E15Credit, Copy10) > 0:
                copystr10 = CStr(Copy10 + 1000)
                copiesstr10 = copiesstr10 + copystr10
        Copy10 = Copy10 + 1
    copiesstr11 = ''
    Copy11 = 1
    max11 = GetAllCopies(IA177)
    while Copy11 <= max11:
        if GetCurrency(IA177.CYAdoptionTaxCr, Copy11) > 0:
            if GetBool(IA177.Spouse, Copy11) == True and GetCurrency(IA177.CYAdoptionTaxCr, Copy11) > 0:
                copystr11 = CStr(Copy11 + 1100)
                copiesstr11 = copiesstr11 + copystr11
        Copy11 = Copy11 + 1
    copiesstr12 = ''
    Copy12 = 1
    max12 = GetAllCopies(IACred)
    while Copy12 <= max12:
        if GetString(IACred.Code, Copy12) == '67':
            if GetBool(IACred.RefCr, Copy12) == True and GetBool(IACred.Spouse, Copy12) == True and GetString(IACred.Code, Copy12) == '67':
                copystr12 = CStr(Copy12 + 1200)
                copiesstr12 = copiesstr12 + copystr12
        Copy12 = Copy12 + 1
    copiesstr13 = ''
    Copy13 = 1
    max13 = GetAllCopies(IACred)
    while Copy13 <= max13:
        if GetString(IACred.Code, Copy13) == '68':
            if GetBool(IACred.RefCr, Copy13) == True and GetBool(IACred.Spouse, Copy13) == True and GetString(IACred.Code, Copy13) == '68':
                copystr13 = CStr(Copy13 + 1300)
                copiesstr13 = copiesstr13 + copystr13
        Copy13 = Copy13 + 1
    copiesstr14 = ''
    Copy14 = 1
    max14 = GetAllCopies(IACred)
    while Copy14 <= max14:
        if GetString(IACred.Code, Copy14) == '69':
            if GetBool(IACred.RefCr, Copy14) == True and GetBool(IACred.Spouse, Copy14) == True and GetString(IACred.Code, Copy14) == '69':
                copystr14 = CStr(Copy14 + 1400)
                copiesstr14 = copiesstr14 + copystr14
        Copy14 = Copy14 + 1
    ReturnVal = copiesstr + copiesstr2 + copiesstr3 + copiesstr4 + copiesstr5 + copiesstr6 + copiesstr7 + copiesstr8 + copiesstr9 + copiesstr10 + copiesstr11 + copiesstr12 + copiesstr13 + copiesstr14

def RefCr_Calculation(Index):
    strindex = Long()

    copystr = String()

    Copy = Long()
    strindex = ( ( Index )  * 4 )  + 1
    copystr = Trim(Mid(GetString(IA148Sp.RefCopiesStr), strindex, 4))
    if Index == 6 and GetNumber(IA148Sp.RefNbr) > 7:
        ReturnVal = GetCurrency(IAWBP148RefSp.TotRefCr1) + GetCurrency(IAWBP148RefSp.TotRefCr2)
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

def RefNbr_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Integer()

    count2 = Integer()

    Lim2 = Integer()

    IACredit = String()

    count3 = Integer()

    Lim3 = Integer()

    count4 = Integer()

    Lim4 = Integer()

    count5 = Integer()

    Lim5 = Integer()

    count6 = Integer()

    Lim6 = Integer()

    count7 = Integer()

    Lim7 = Integer()

    count8 = Integer()

    Lim8 = Integer()

    count9 = Integer()

    Lim9 = Integer()

    count10 = Integer()

    Lim10 = Integer()
    Lim = GetAllCopies(IA8864)
    count = 1
    Total = 0
    while count <= Lim:
        if GetBool(IA8864.Spouse, count) == True and GetCurrency(IA8864.BiodieselCr, count) > 0:
            Total = Total + 1
        else:
            Total = Total
        count = count + 1
    Lim2 = GetAllCopies(IACred)
    count2 = 1
    while count2 <= Lim2:
        IACredit = GetString(IACred.Code, count2)
        if GetBool(IACred.RefCr, count2) == True and GetBool(IACred.Spouse, count2) == True and  ( IACredit == '53' or IACredit == '56' or IACredit == '67' or IACredit == '68' or IACredit == '69' ) :
            Total = Total + 1
        else:
            Total = Total
        count2 = count2 + 1
    Lim3 = GetAllCopies(IA135)
    count3 = 1
    while count3 <= Lim3:
        if GetBool(IA135.Spouse, count3) == True and GetCurrency(IA135.E85Credit, count3) > 0:
            Total = Total + 1
        else:
            Total = Total
        count3 = count3 + 1
    Lim4 = GetAllCopies(IA128)
    count4 = 1
    while count4 <= Lim4:
        if GetBool(IA128.Spouse, count4) == True and GetCurrency(IA128.TotResearchCr, count4) > 0:
            Total = Total + 1
        else:
            Total = Total
        count4 = count4 + 1
    Lim5 = GetAllCopies(IA128)
    count5 = 1
    while count5 <= Lim5:
        if GetBool(IA128.Spouse, count5) == True and GetCurrency(IA128.TotSuppResearchCr, count5) > 0:
            Total = Total + 1
        else:
            Total = Total
        count5 = count5 + 1
    Lim6 = GetAllCopies(IA128S)
    count6 = 1
    while count6 <= Lim6:
        if GetBool(IA128S.Spouse, count6) == True and GetCurrency(IA128S.TotResearchCr, count6) > 0:
            Total = Total + 1
        else:
            Total = Total
        count6 = count6 + 1
    Lim7 = GetAllCopies(IA128S)
    count7 = 1
    while count7 <= Lim7:
        if GetBool(IA128S.Spouse, count7) == True and GetCurrency(IA128S.TotSuppResearchCr, count7) > 0:
            Total = Total + 1
        else:
            Total = Total
        count7 = count7 + 1
    Lim8 = GetAllCopies(IA137)
    count8 = 1
    while count8 <= Lim8:
        ## VB2PY (CheckDirective) VB directive took path 1 on INDCALC
        if GetBool(IA137.Spouse, count8) == True and GetCurrency(IA137.EthPromoteCr, count8) > 0:
            Total = Total + 1
        else:
            Total = Total
        count8 = count8 + 1
    Lim9 = GetAllCopies(IA138)
    count9 = 1
    while count9 <= Lim9:
        if GetBool(IA138.Spouse, count9) == True and GetCurrency(IA138.E15Credit, count9) > 0:
            Total = Total + 1
        else:
            Total = Total
        count9 = count9 + 1
    Lim10 = GetAllCopies(IA177)
    count10 = 1
    while count10 <= Lim10:
        if GetBool(IA177.Spouse, count10) == True and GetCurrency(IA177.CYAdoptionTaxCr, count10) > 0:
            Total = Total + 1
        else:
            Total = Total
        count10 = count10 + 1
    ReturnVal = Total

def RefTrig_Calculation(Index):
    if GetString(IA148Sp.RefCode(Index)) == '64' or GetString(IA148Sp.RefCode(Index)) == '58' or GetString(IA148Sp.RefCode(Index)) == '55' or GetString(IA148Sp.RefCode(Index)) == '52' or GetString(IA148Sp.RefCode(Index)) == '59' or GetString(IA148Sp.RefCode(Index)) == '65' or GetString(IA148Sp.RefCode(Index)) == '66':
        ReturnVal = 0
    elif GetCurrency(IA148Sp.RefCr(Index)) > 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SpouseSSN)

def TotCode64_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Currency()
    Lim = GetAllCopies(IA137)
    count = 1
    Total = 0
    while count <= Lim:
        if GetBool(IA137.Spouse, count) == True:
            Total = Total + GetCurrency(IA137.TotEthSoldCr, count)
        else:
            Total = Total
        count = count + 1
    ReturnVal = Total

def TotNonRefCr_Calculation():
    if GetBool(IAF1040.CombMFS) == False:
        ReturnVal = 0
    else:
        ReturnVal = GetCurrency(IA148Sp.NonRefCr1) + GetCurrency(IA148Sp.NonRefCr2) + GetCurrency(IA148Sp.NonRefCr3) + GetCurrency(IA148Sp.NonRefCr4) + GetCurrency(IA148Sp.NonRefCr5) + GetCurrency(IA148Sp.NonRefCr6) + GetCurrency(IA148Sp.NonRefCr7) + GetCurrency(IA148Sp.NonRefCr8) + GetCurrency(IA148Sp.NonRefCr9) + GetCurrency(IA148Sp.NonRefCr10)

def TotNonRefNo8801_Calculation():
    count = Integer()

    Lim = Integer()

    WSTotal = Currency()

    Total = Currency()
    Lim = GetAllCopies(IACred)
    count = 1
    WSTotal = 0
    while count <= Lim:
        if GetBool(IACred.NonrefCr, count) == True and GetBool(IACred.Spouse, count) == True:
            WSTotal = WSTotal + GetCurrency(IACred.CYCredit, count) + GetCurrency(IACred.PYCarry, count)
        else:
            WSTotal = WSTotal
        count = count + 1
    Total = WSTotal + GetCurrency(IA134Sp.Credit) + GetCurrency(IA147.FranchiseCr, FieldCopies(IA147.Spouse))
    ReturnVal = Total

def TotPTE_Calculation():
    ReturnVal = GetNumber(IA148BumpSp.TotPTE) + GetNumber(IA148BumpSp.TotRefPTE)

def TotRefCr_Calculation():
    count = Integer()

    SubTot = Currency()
    count = 0
    SubTot = 0
    while count < 7:
        SubTot = SubTot + GetCurrency(IA148Sp.RefCr(count))
        count = count + 1
    if GetBool(IAF1040.CombMFS) == False:
        ReturnVal = 0
    else:
        ReturnVal = SubTot

def TPPerc_Calculation(Index):
    PTE = Integer()

    RefPTE = Integer()

    Stuff = Integer()

    Stuff2 = Integer()
    PTE = GetNumber(IA148BumpSp.TotPTE)
    RefPTE = GetNumber(IA148BumpSp.TotRefPTE)
    if Index == 5 and GetNumber(IA148Sp.TotPTE) > 6:
        ReturnVal = 0
    elif PTE > Index:
        Stuff2 = GetNumber(IA148BumpSp.PTEIndexNbr(Index))
        ReturnVal = GetFloat(IA148BumpSp.TPPerc(Stuff2))
    elif PTE + RefPTE > Index:
        Stuff = ( Index )  - PTE
        Stuff2 = GetNumber(IA148BumpSp.RefPTEIndexNbr(Stuff))
        ReturnVal = GetFloat(IA148BumpSp.RefTPPerc(Stuff2))
    else:
        ReturnVal = 0

