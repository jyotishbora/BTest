from forms.out import IA4562BSP
from forms.out import IA4562SP
from forms.out import IAF1040
from forms.out import IAWOTHINC
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *
import datetime



def Balance1_Calculation():
    return get_currency(IA4562BSP.AdjAmt(0))

def Balance10_Calculation():
    if get_currency(IA4562BSP.Balance9) != 0:
        return get_currency(IA4562BSP.Balance9) + get_currency(IA4562BSP.AdjAmt(9))
    else:
        return get_currency(IA4562BSP.AdjAmt(9))

def Balance11_Calculation():
    if get_currency(IA4562BSP.Balance10) != 0:
        return get_currency(IA4562BSP.Balance10) + get_currency(IA4562BSP.AdjAmt(10))
    else:
        return get_currency(IA4562BSP.AdjAmt(10))

def Balance12_Calculation():
    if get_currency(IA4562BSP.Balance11) != 0:
        return get_currency(IA4562BSP.Balance11) + get_currency(IA4562BSP.AdjAmt(11))
    else:
        return get_currency(IA4562BSP.AdjAmt(11))

def Balance13_Calculation():
    if get_currency(IA4562BSP.Balance12) != 0:
        return get_currency(IA4562BSP.Balance12) + get_currency(IA4562BSP.AdjAmt(12))
    else:
        return get_currency(IA4562BSP.AdjAmt(12))

def Balance2_Calculation():
    if get_currency(IA4562BSP.Balance1) != 0:
        return get_currency(IA4562BSP.Balance1) + get_currency(IA4562BSP.AdjAmt(1))
    else:
        return get_currency(IA4562BSP.AdjAmt(1))

def Balance3_Calculation():
    if get_currency(IA4562BSP.Balance2) != 0:
        return get_currency(IA4562BSP.Balance2) + get_currency(IA4562BSP.AdjAmt(2))
    else:
        return get_currency(IA4562BSP.AdjAmt(2))

def Balance4_Calculation():
    if get_currency(IA4562BSP.Balance3) != 0:
        return get_currency(IA4562BSP.Balance3) + get_currency(IA4562BSP.AdjAmt(3))
    else:
        return get_currency(IA4562BSP.AdjAmt(3))

def Balance5_Calculation():
    if get_currency(IA4562BSP.Balance4) != 0:
        return get_currency(IA4562BSP.Balance4) + get_currency(IA4562BSP.AdjAmt(4))
    else:
        return get_currency(IA4562BSP.AdjAmt(4))

def Balance6_Calculation():
    if get_currency(IA4562BSP.Balance5) != 0:
        return get_currency(IA4562BSP.Balance5) + get_currency(IA4562BSP.AdjAmt(5))
    else:
        return get_currency(IA4562BSP.AdjAmt(5))

def Balance7_Calculation():
    if get_currency(IA4562BSP.Balance6) != 0:
        return get_currency(IA4562BSP.Balance6) + get_currency(IA4562BSP.AdjAmt(6))
    else:
        return get_currency(IA4562BSP.AdjAmt(6))

def Balance8_Calculation():
    if get_currency(IA4562BSP.Balance7) != 0:
        return get_currency(IA4562BSP.Balance7) + get_currency(IA4562BSP.AdjAmt(7))
    else:
        return get_currency(IA4562BSP.AdjAmt(7))

def Balance9_Calculation():
    if get_currency(IA4562BSP.Balance8) != 0:
        return get_currency(IA4562BSP.Balance8) + get_currency(IA4562BSP.AdjAmt(8))
    else:
        return get_currency(IA4562BSP.AdjAmt(8))

def Balance14_Calculation():
    if get_currency(IA4562BSP.Balance13) != 0:
        return get_currency(IA4562BSP.Balance13) + get_currency(IA4562BSP.AdjAmt(13))
    else:
        return get_currency(IA4562BSP.AdjAmt(13))

def Balance15_Calculation():
    if get_currency(IA4562BSP.Balance14) != 0:
        return get_currency(IA4562BSP.Balance14) + get_currency(IA4562BSP.AdjAmt(14))
    else:
        return get_currency(IA4562BSP.AdjAmt(14))

def Balance16_Calculation():
    if get_currency(IA4562BSP.Balance15) != 0:
        return get_currency(IA4562BSP.Balance15) + get_currency(IA4562BSP.AdjAmt(15))
    else:
        return get_currency(IA4562BSP.AdjAmt(15))

def Balance17_Calculation():
    if get_currency(IA4562BSP.Balance16) != 0:
        return get_currency(IA4562BSP.Balance16) + get_currency(IA4562BSP.CYAdjAmt)
    else:
        return get_currency(IA4562BSP.CYAdjAmt)

def CYAdjAmt_Calculation():
    if get_bool(IAF1040.CombMFS) == True:
        return get_currency(IAWOTHINC.SPBonus)
    else:
        return 0

def Description_Calculation():
    return CStr(get_currency(IA4562BSP.Balance17)) + ' Balance'

def Names_Calculation():
    return get_string(IA4562SP.Names)

def PeriodEnd_Calculation(Index):
    if Index == 0:
        return datetime.datetime(12, 31, 2002)
    elif Index == 1:
        return datetime.datetime(12, 31, 2003)
    elif Index == 2:
        return datetime.datetime(12, 31, 2004)
    elif Index == 3:
        return datetime.datetime(12, 31, 2005)
    elif Index == 4:
        return datetime.datetime(12, 31, 2006)
    elif Index == 5:
        return datetime.datetime(12, 31, 2007)
    elif Index == 6:
        return datetime.datetime(12, 31, 2008)
    elif Index == 7:
        return datetime.datetime(12, 31, 2009)
    elif Index == 8:
        return datetime.datetime(12, 31, 2010)
    elif Index == 9:
        return datetime.datetime(12, 31, 2011)
    elif Index == 10:
        return datetime.datetime(12, 31, 2012)
    elif Index == 11:
        return datetime.datetime(12, 31, 2013)
    elif Index == 12:
        return datetime.datetime(12, 31, 2014)
    elif Index == 13:
        return datetime.datetime(12, 31, 2015)
    elif Index == 14:
        return datetime.datetime(12, 31, 2016)
    elif Index == 15:
        return datetime.datetime(12, 31, 2017)
    else:
        return datetime.datetime(12, 31, 2018)

def PrAdjAmt_Calculation(Index):
    count = Integer()

    Hold = Currency()
    count = 0
    Hold = 0
    if get_currency(IA4562BSP.AdjAmt(0)) != 0 or get_currency(IA4562BSP.Balance1) != 0:
        if Index == count:
            Hold = get_currency(IA4562BSP.AdjAmt(0))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(1)) != 0 or get_currency(IA4562BSP.Balance2) != 0:
        if Index == count:
            Hold = get_currency(IA4562BSP.AdjAmt(1))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(2)) != 0 or get_currency(IA4562BSP.Balance3) != 0:
        if Index == count:
            Hold = get_currency(IA4562BSP.AdjAmt(2))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(3)) != 0 or get_currency(IA4562BSP.Balance4) != 0:
        if Index == count:
            Hold = get_currency(IA4562BSP.AdjAmt(3))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(4)) != 0 or get_currency(IA4562BSP.Balance5) != 0:
        if Index == count:
            Hold = get_currency(IA4562BSP.AdjAmt(4))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(5)) != 0 or get_currency(IA4562BSP.Balance6) != 0:
        if Index == count:
            Hold = get_currency(IA4562BSP.AdjAmt(5))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(6)) != 0 or get_currency(IA4562BSP.Balance7) != 0:
        if Index == count:
            Hold = get_currency(IA4562BSP.AdjAmt(6))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(7)) != 0 or get_currency(IA4562BSP.Balance8) != 0:
        if Index == count:
            Hold = get_currency(IA4562BSP.AdjAmt(7))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(8)) != 0 or get_currency(IA4562BSP.Balance9) != 0:
        if Index == count:
            Hold = get_currency(IA4562BSP.AdjAmt(8))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(9)) != 0 or get_currency(IA4562BSP.Balance10) != 0:
        if Index == count:
            Hold = get_currency(IA4562BSP.AdjAmt(9))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(10)) != 0 or get_currency(IA4562BSP.Balance11) != 0:
        if Index == count:
            Hold = get_currency(IA4562BSP.AdjAmt(10))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(11)) != 0 or get_currency(IA4562BSP.Balance12) != 0:
        if Index == count:
            Hold = get_currency(IA4562BSP.AdjAmt(11))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(12)) != 0 or get_currency(IA4562BSP.Balance13) != 0:
        if Index == count:
            Hold = get_currency(IA4562BSP.AdjAmt(12))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(13)) != 0 or get_currency(IA4562BSP.Balance14) != 0:
        if Index == count:
            Hold = get_currency(IA4562BSP.AdjAmt(13))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(14)) != 0 or get_currency(IA4562BSP.Balance15) != 0:
        if Index == count:
            Hold = get_currency(IA4562BSP.AdjAmt(14))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(15)) != 0 or get_currency(IA4562BSP.Balance16) != 0:
        if Index == count:
            Hold = get_currency(IA4562BSP.AdjAmt(15))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.CYAdjAmt) != 0 or get_currency(IA4562BSP.Balance17) != 0:
        if Index == count:
            Hold = get_currency(IA4562BSP.CYAdjAmt)
            count = 99
        else:
            count = count + 1
    return Hold

def PrAsterik_Calculation(Index):
    if get_bool(IA4562BSP.PrChangeY(Index)) == True:
        return '*'
    else:
        return ''

def PrBalance_Calculation(Index):
    count = Integer()

    Hold = Currency()
    count = 0
    Hold = 0
    if get_currency(IA4562BSP.AdjAmt(0)) != 0 or get_currency(IA4562BSP.Balance1) != 0:
        if Index == count:
            Hold = get_currency(IA4562BSP.Balance1)
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(1)) != 0 or get_currency(IA4562BSP.Balance2) != 0:
        if Index == count:
            Hold = get_currency(IA4562BSP.Balance2)
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(2)) != 0 or get_currency(IA4562BSP.Balance3) != 0:
        if Index == count:
            Hold = get_currency(IA4562BSP.Balance3)
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(3)) != 0 or get_currency(IA4562BSP.Balance4) != 0:
        if Index == count:
            Hold = get_currency(IA4562BSP.Balance4)
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(4)) != 0 or get_currency(IA4562BSP.Balance5) != 0:
        if Index == count:
            Hold = get_currency(IA4562BSP.Balance5)
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(5)) != 0 or get_currency(IA4562BSP.Balance6) != 0:
        if Index == count:
            Hold = get_currency(IA4562BSP.Balance6)
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(6)) != 0 or get_currency(IA4562BSP.Balance7) != 0:
        if Index == count:
            Hold = get_currency(IA4562BSP.Balance7)
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(7)) != 0 or get_currency(IA4562BSP.Balance8) != 0:
        if Index == count:
            Hold = get_currency(IA4562BSP.Balance8)
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(8)) != 0 or get_currency(IA4562BSP.Balance9) != 0:
        if Index == count:
            Hold = get_currency(IA4562BSP.Balance9)
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(9)) != 0 or get_currency(IA4562BSP.Balance10) != 0:
        if Index == count:
            Hold = get_currency(IA4562BSP.Balance10)
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(10)) != 0 or get_currency(IA4562BSP.Balance11) != 0:
        if Index == count:
            Hold = get_currency(IA4562BSP.Balance11)
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(11)) != 0 or get_currency(IA4562BSP.Balance12) != 0:
        if Index == count:
            Hold = get_currency(IA4562BSP.Balance12)
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(12)) != 0 or get_currency(IA4562BSP.Balance13) != 0:
        if Index == count:
            Hold = get_currency(IA4562BSP.Balance13)
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(13)) != 0 or get_currency(IA4562BSP.Balance14) != 0:
        if Index == count:
            Hold = get_currency(IA4562BSP.Balance14)
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(14)) != 0 or get_currency(IA4562BSP.Balance15) != 0:
        if Index == count:
            Hold = get_currency(IA4562BSP.Balance15)
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(15)) != 0 or get_currency(IA4562BSP.Balance16) != 0:
        if Index == count:
            Hold = get_currency(IA4562BSP.Balance16)
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.CYAdjAmt) != 0 or get_currency(IA4562BSP.Balance17) != 0:
        if Index == count:
            Hold = get_currency(IA4562BSP.Balance17)
            count = 99
        else:
            count = count + 1
    return Hold

def PrChangeY_Calculation(Index):
    count = Integer()

    Hold = Boolean()
    count = 0
    Hold = 0
    if get_currency(IA4562BSP.AdjAmt(0)) != 0 or get_currency(IA4562BSP.Balance1) != 0:
        if Index == count:
            Hold = get_bool(IA4562BSP.ChangeY(0))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(1)) != 0 or get_currency(IA4562BSP.Balance2) != 0:
        if Index == count:
            Hold = get_bool(IA4562BSP.ChangeY(1))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(2)) != 0 or get_currency(IA4562BSP.Balance3) != 0:
        if Index == count:
            Hold = get_bool(IA4562BSP.ChangeY(2))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(3)) != 0 or get_currency(IA4562BSP.Balance4) != 0:
        if Index == count:
            Hold = get_bool(IA4562BSP.ChangeY(3))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(4)) != 0 or get_currency(IA4562BSP.Balance5) != 0:
        if Index == count:
            Hold = get_bool(IA4562BSP.ChangeY(4))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(5)) != 0 or get_currency(IA4562BSP.Balance6) != 0:
        if Index == count:
            Hold = get_bool(IA4562BSP.ChangeY(5))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(6)) != 0 or get_currency(IA4562BSP.Balance7) != 0:
        if Index == count:
            Hold = get_bool(IA4562BSP.ChangeY(6))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(7)) != 0 or get_currency(IA4562BSP.Balance8) != 0:
        if Index == count:
            Hold = get_bool(IA4562BSP.ChangeY(7))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(8)) != 0 or get_currency(IA4562BSP.Balance9) != 0:
        if Index == count:
            Hold = get_bool(IA4562BSP.ChangeY(8))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(9)) != 0 or get_currency(IA4562BSP.Balance10) != 0:
        if Index == count:
            Hold = get_bool(IA4562BSP.ChangeY(9))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(10)) != 0 or get_currency(IA4562BSP.Balance11) != 0:
        if Index == count:
            Hold = get_bool(IA4562BSP.ChangeY(10))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(11)) != 0 or get_currency(IA4562BSP.Balance12) != 0:
        if Index == count:
            Hold = get_bool(IA4562BSP.ChangeY(11))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(12)) != 0 or get_currency(IA4562BSP.Balance13) != 0:
        if Index == count:
            Hold = get_bool(IA4562BSP.ChangeY(12))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(13)) != 0 or get_currency(IA4562BSP.Balance14) != 0:
        if Index == count:
            Hold = get_bool(IA4562BSP.ChangeY(13))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(14)) != 0 or get_currency(IA4562BSP.Balance15) != 0:
        if Index == count:
            Hold = get_bool(IA4562BSP.ChangeY(14))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(15)) != 0 or get_currency(IA4562BSP.Balance16) != 0:
        if Index == count:
            Hold = get_bool(IA4562BSP.ChangeY(15))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.CYAdjAmt) != 0 or get_currency(IA4562BSP.Balance17) != 0:
        if Index == count:
            Hold = get_bool(IA4562BSP.ChangeY(16))
            count = 99
        else:
            count = count + 1
    return Hold

def Print_Calculation():
    if get_currency(IA4562BSP.PrBalance(0)) != 0:
        return 1
    else:
        return 0

def PrPeriodEnd_Calculation(Index):
    count = Integer()

    Hold = String()
    count = 0
    Hold = ''
    if get_currency(IA4562BSP.AdjAmt(0)) != 0 or get_currency(IA4562BSP.Balance1) != 0:
        if Index == count:
            Hold = get_string(IA4562BSP.PeriodEnd(0))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(1)) != 0 or get_currency(IA4562BSP.Balance2) != 0:
        if Index == count:
            Hold = get_string(IA4562BSP.PeriodEnd(1))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(2)) != 0 or get_currency(IA4562BSP.Balance3) != 0:
        if Index == count:
            Hold = get_string(IA4562BSP.PeriodEnd(2))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(3)) != 0 or get_currency(IA4562BSP.Balance4) != 0:
        if Index == count:
            Hold = get_string(IA4562BSP.PeriodEnd(3))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(4)) != 0 or get_currency(IA4562BSP.Balance5) != 0:
        if Index == count:
            Hold = get_string(IA4562BSP.PeriodEnd(4))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(5)) != 0 or get_currency(IA4562BSP.Balance6) != 0:
        if Index == count:
            Hold = get_string(IA4562BSP.PeriodEnd(5))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(6)) != 0 or get_currency(IA4562BSP.Balance7) != 0:
        if Index == count:
            Hold = get_string(IA4562BSP.PeriodEnd(6))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(7)) != 0 or get_currency(IA4562BSP.Balance8) != 0:
        if Index == count:
            Hold = get_string(IA4562BSP.PeriodEnd(7))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(8)) != 0 or get_currency(IA4562BSP.Balance9) != 0:
        if Index == count:
            Hold = get_string(IA4562BSP.PeriodEnd(8))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(9)) != 0 or get_currency(IA4562BSP.Balance10) != 0:
        if Index == count:
            Hold = get_string(IA4562BSP.PeriodEnd(9))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(10)) != 0 or get_currency(IA4562BSP.Balance11) != 0:
        if Index == count:
            Hold = get_string(IA4562BSP.PeriodEnd(10))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(11)) != 0 or get_currency(IA4562BSP.Balance12) != 0:
        if Index == count:
            Hold = get_string(IA4562BSP.PeriodEnd(11))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(12)) != 0 or get_currency(IA4562BSP.Balance13) != 0:
        if Index == count:
            Hold = get_string(IA4562BSP.PeriodEnd(12))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(13)) != 0 or get_currency(IA4562BSP.Balance14) != 0:
        if Index == count:
            Hold = get_string(IA4562BSP.PeriodEnd(13))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(14)) != 0 or get_currency(IA4562BSP.Balance15) != 0:
        if Index == count:
            Hold = get_string(IA4562BSP.PeriodEnd(14))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.AdjAmt(15)) != 0 or get_currency(IA4562BSP.Balance16) != 0:
        if Index == count:
            Hold = get_string(IA4562BSP.PeriodEnd(15))
            count = 99
        else:
            count = count + 1
    if get_currency(IA4562BSP.CYAdjAmt) != 0 or get_currency(IA4562BSP.Balance17) != 0:
        if Index == count:
            Hold = get_string(IA4562BSP.PeriodEnd(16))
            count = 99
        else:
            count = count + 1
    return Hold

def SSN_Calculation():
    return get_string(IA4562SP.SSN)


