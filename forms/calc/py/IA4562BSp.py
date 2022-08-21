from vb2py.vbfunctions import *
from vb2py.vbdebug import *
import datetime



def Balance1_Calculation():
    ReturnVal = GetCurrency(IA4562BSp.AdjAmt(0))

def Balance10_Calculation():
    if GetCurrency(IA4562BSp.Balance9) != 0:
        ReturnVal = GetCurrency(IA4562BSp.Balance9) + GetCurrency(IA4562BSp.AdjAmt(9))
    else:
        ReturnVal = GetCurrency(IA4562BSp.AdjAmt(9))

def Balance11_Calculation():
    if GetCurrency(IA4562BSp.Balance10) != 0:
        ReturnVal = GetCurrency(IA4562BSp.Balance10) + GetCurrency(IA4562BSp.AdjAmt(10))
    else:
        ReturnVal = GetCurrency(IA4562BSp.AdjAmt(10))

def Balance12_Calculation():
    if GetCurrency(IA4562BSp.Balance11) != 0:
        ReturnVal = GetCurrency(IA4562BSp.Balance11) + GetCurrency(IA4562BSp.AdjAmt(11))
    else:
        ReturnVal = GetCurrency(IA4562BSp.AdjAmt(11))

def Balance13_Calculation():
    if GetCurrency(IA4562BSp.Balance12) != 0:
        ReturnVal = GetCurrency(IA4562BSp.Balance12) + GetCurrency(IA4562BSp.AdjAmt(12))
    else:
        ReturnVal = GetCurrency(IA4562BSp.AdjAmt(12))

def Balance2_Calculation():
    if GetCurrency(IA4562BSp.Balance1) != 0:
        ReturnVal = GetCurrency(IA4562BSp.Balance1) + GetCurrency(IA4562BSp.AdjAmt(1))
    else:
        ReturnVal = GetCurrency(IA4562BSp.AdjAmt(1))

def Balance3_Calculation():
    if GetCurrency(IA4562BSp.Balance2) != 0:
        ReturnVal = GetCurrency(IA4562BSp.Balance2) + GetCurrency(IA4562BSp.AdjAmt(2))
    else:
        ReturnVal = GetCurrency(IA4562BSp.AdjAmt(2))

def Balance4_Calculation():
    if GetCurrency(IA4562BSp.Balance3) != 0:
        ReturnVal = GetCurrency(IA4562BSp.Balance3) + GetCurrency(IA4562BSp.AdjAmt(3))
    else:
        ReturnVal = GetCurrency(IA4562BSp.AdjAmt(3))

def Balance5_Calculation():
    if GetCurrency(IA4562BSp.Balance4) != 0:
        ReturnVal = GetCurrency(IA4562BSp.Balance4) + GetCurrency(IA4562BSp.AdjAmt(4))
    else:
        ReturnVal = GetCurrency(IA4562BSp.AdjAmt(4))

def Balance6_Calculation():
    if GetCurrency(IA4562BSp.Balance5) != 0:
        ReturnVal = GetCurrency(IA4562BSp.Balance5) + GetCurrency(IA4562BSp.AdjAmt(5))
    else:
        ReturnVal = GetCurrency(IA4562BSp.AdjAmt(5))

def Balance7_Calculation():
    if GetCurrency(IA4562BSp.Balance6) != 0:
        ReturnVal = GetCurrency(IA4562BSp.Balance6) + GetCurrency(IA4562BSp.AdjAmt(6))
    else:
        ReturnVal = GetCurrency(IA4562BSp.AdjAmt(6))

def Balance8_Calculation():
    if GetCurrency(IA4562BSp.Balance7) != 0:
        ReturnVal = GetCurrency(IA4562BSp.Balance7) + GetCurrency(IA4562BSp.AdjAmt(7))
    else:
        ReturnVal = GetCurrency(IA4562BSp.AdjAmt(7))

def Balance9_Calculation():
    if GetCurrency(IA4562BSp.Balance8) != 0:
        ReturnVal = GetCurrency(IA4562BSp.Balance8) + GetCurrency(IA4562BSp.AdjAmt(8))
    else:
        ReturnVal = GetCurrency(IA4562BSp.AdjAmt(8))

def Balance14_Calculation():
    if GetCurrency(IA4562BSp.Balance13) != 0:
        ReturnVal = GetCurrency(IA4562BSp.Balance13) + GetCurrency(IA4562BSp.AdjAmt(13))
    else:
        ReturnVal = GetCurrency(IA4562BSp.AdjAmt(13))

def Balance15_Calculation():
    if GetCurrency(IA4562BSp.Balance14) != 0:
        ReturnVal = GetCurrency(IA4562BSp.Balance14) + GetCurrency(IA4562BSp.AdjAmt(14))
    else:
        ReturnVal = GetCurrency(IA4562BSp.AdjAmt(14))

def Balance16_Calculation():
    if GetCurrency(IA4562BSp.Balance15) != 0:
        ReturnVal = GetCurrency(IA4562BSp.Balance15) + GetCurrency(IA4562BSp.AdjAmt(15))
    else:
        ReturnVal = GetCurrency(IA4562BSp.AdjAmt(15))

def Balance17_Calculation():
    if GetCurrency(IA4562BSp.Balance16) != 0:
        ReturnVal = GetCurrency(IA4562BSp.Balance16) + GetCurrency(IA4562BSp.CYAdjAmt)
    else:
        ReturnVal = GetCurrency(IA4562BSp.CYAdjAmt)

def CYAdjAmt_Calculation():
    if GetBool(IAF1040.CombMFS) == True:
        ReturnVal = GetCurrency(IAWOthInc.SPBonus)
    else:
        ReturnVal = 0

def Description_Calculation():
    ReturnVal = CStr(GetCurrency(IA4562BSp.Balance17)) + ' Balance'

def Names_Calculation():
    ReturnVal = GetString(IA4562Sp.Names)

def PeriodEnd_Calculation(Index):
    if Index == 0:
        ReturnVal = datetime.datetime(12, 31, 2002)
    elif Index == 1:
        ReturnVal = datetime.datetime(12, 31, 2003)
    elif Index == 2:
        ReturnVal = datetime.datetime(12, 31, 2004)
    elif Index == 3:
        ReturnVal = datetime.datetime(12, 31, 2005)
    elif Index == 4:
        ReturnVal = datetime.datetime(12, 31, 2006)
    elif Index == 5:
        ReturnVal = datetime.datetime(12, 31, 2007)
    elif Index == 6:
        ReturnVal = datetime.datetime(12, 31, 2008)
    elif Index == 7:
        ReturnVal = datetime.datetime(12, 31, 2009)
    elif Index == 8:
        ReturnVal = datetime.datetime(12, 31, 2010)
    elif Index == 9:
        ReturnVal = datetime.datetime(12, 31, 2011)
    elif Index == 10:
        ReturnVal = datetime.datetime(12, 31, 2012)
    elif Index == 11:
        ReturnVal = datetime.datetime(12, 31, 2013)
    elif Index == 12:
        ReturnVal = datetime.datetime(12, 31, 2014)
    elif Index == 13:
        ReturnVal = datetime.datetime(12, 31, 2015)
    elif Index == 14:
        ReturnVal = datetime.datetime(12, 31, 2016)
    elif Index == 15:
        ReturnVal = datetime.datetime(12, 31, 2017)
    else:
        ReturnVal = datetime.datetime(12, 31, 2018)

def PrAdjAmt_Calculation(Index):
    count = Integer()

    Hold = Currency()
    count = 0
    Hold = 0
    if GetCurrency(IA4562BSp.AdjAmt(0)) != 0 or GetCurrency(IA4562BSp.Balance1) != 0:
        if Index == count:
            Hold = GetCurrency(IA4562BSp.AdjAmt(0))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(1)) != 0 or GetCurrency(IA4562BSp.Balance2) != 0:
        if Index == count:
            Hold = GetCurrency(IA4562BSp.AdjAmt(1))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(2)) != 0 or GetCurrency(IA4562BSp.Balance3) != 0:
        if Index == count:
            Hold = GetCurrency(IA4562BSp.AdjAmt(2))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(3)) != 0 or GetCurrency(IA4562BSp.Balance4) != 0:
        if Index == count:
            Hold = GetCurrency(IA4562BSp.AdjAmt(3))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(4)) != 0 or GetCurrency(IA4562BSp.Balance5) != 0:
        if Index == count:
            Hold = GetCurrency(IA4562BSp.AdjAmt(4))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(5)) != 0 or GetCurrency(IA4562BSp.Balance6) != 0:
        if Index == count:
            Hold = GetCurrency(IA4562BSp.AdjAmt(5))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(6)) != 0 or GetCurrency(IA4562BSp.Balance7) != 0:
        if Index == count:
            Hold = GetCurrency(IA4562BSp.AdjAmt(6))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(7)) != 0 or GetCurrency(IA4562BSp.Balance8) != 0:
        if Index == count:
            Hold = GetCurrency(IA4562BSp.AdjAmt(7))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(8)) != 0 or GetCurrency(IA4562BSp.Balance9) != 0:
        if Index == count:
            Hold = GetCurrency(IA4562BSp.AdjAmt(8))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(9)) != 0 or GetCurrency(IA4562BSp.Balance10) != 0:
        if Index == count:
            Hold = GetCurrency(IA4562BSp.AdjAmt(9))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(10)) != 0 or GetCurrency(IA4562BSp.Balance11) != 0:
        if Index == count:
            Hold = GetCurrency(IA4562BSp.AdjAmt(10))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(11)) != 0 or GetCurrency(IA4562BSp.Balance12) != 0:
        if Index == count:
            Hold = GetCurrency(IA4562BSp.AdjAmt(11))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(12)) != 0 or GetCurrency(IA4562BSp.Balance13) != 0:
        if Index == count:
            Hold = GetCurrency(IA4562BSp.AdjAmt(12))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(13)) != 0 or GetCurrency(IA4562BSp.Balance14) != 0:
        if Index == count:
            Hold = GetCurrency(IA4562BSp.AdjAmt(13))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(14)) != 0 or GetCurrency(IA4562BSp.Balance15) != 0:
        if Index == count:
            Hold = GetCurrency(IA4562BSp.AdjAmt(14))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(15)) != 0 or GetCurrency(IA4562BSp.Balance16) != 0:
        if Index == count:
            Hold = GetCurrency(IA4562BSp.AdjAmt(15))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.CYAdjAmt) != 0 or GetCurrency(IA4562BSp.Balance17) != 0:
        if Index == count:
            Hold = GetCurrency(IA4562BSp.CYAdjAmt)
            count = 99
        else:
            count = count + 1
    ReturnVal = Hold

def PrAsterik_Calculation(Index):
    if GetBool(IA4562BSp.PrChangeY(Index)) == True:
        ReturnVal = '*'
    else:
        ReturnVal = ''

def PrBalance_Calculation(Index):
    count = Integer()

    Hold = Currency()
    count = 0
    Hold = 0
    if GetCurrency(IA4562BSp.AdjAmt(0)) != 0 or GetCurrency(IA4562BSp.Balance1) != 0:
        if Index == count:
            Hold = GetCurrency(IA4562BSp.Balance1)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(1)) != 0 or GetCurrency(IA4562BSp.Balance2) != 0:
        if Index == count:
            Hold = GetCurrency(IA4562BSp.Balance2)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(2)) != 0 or GetCurrency(IA4562BSp.Balance3) != 0:
        if Index == count:
            Hold = GetCurrency(IA4562BSp.Balance3)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(3)) != 0 or GetCurrency(IA4562BSp.Balance4) != 0:
        if Index == count:
            Hold = GetCurrency(IA4562BSp.Balance4)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(4)) != 0 or GetCurrency(IA4562BSp.Balance5) != 0:
        if Index == count:
            Hold = GetCurrency(IA4562BSp.Balance5)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(5)) != 0 or GetCurrency(IA4562BSp.Balance6) != 0:
        if Index == count:
            Hold = GetCurrency(IA4562BSp.Balance6)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(6)) != 0 or GetCurrency(IA4562BSp.Balance7) != 0:
        if Index == count:
            Hold = GetCurrency(IA4562BSp.Balance7)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(7)) != 0 or GetCurrency(IA4562BSp.Balance8) != 0:
        if Index == count:
            Hold = GetCurrency(IA4562BSp.Balance8)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(8)) != 0 or GetCurrency(IA4562BSp.Balance9) != 0:
        if Index == count:
            Hold = GetCurrency(IA4562BSp.Balance9)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(9)) != 0 or GetCurrency(IA4562BSp.Balance10) != 0:
        if Index == count:
            Hold = GetCurrency(IA4562BSp.Balance10)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(10)) != 0 or GetCurrency(IA4562BSp.Balance11) != 0:
        if Index == count:
            Hold = GetCurrency(IA4562BSp.Balance11)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(11)) != 0 or GetCurrency(IA4562BSp.Balance12) != 0:
        if Index == count:
            Hold = GetCurrency(IA4562BSp.Balance12)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(12)) != 0 or GetCurrency(IA4562BSp.Balance13) != 0:
        if Index == count:
            Hold = GetCurrency(IA4562BSp.Balance13)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(13)) != 0 or GetCurrency(IA4562BSp.Balance14) != 0:
        if Index == count:
            Hold = GetCurrency(IA4562BSp.Balance14)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(14)) != 0 or GetCurrency(IA4562BSp.Balance15) != 0:
        if Index == count:
            Hold = GetCurrency(IA4562BSp.Balance15)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(15)) != 0 or GetCurrency(IA4562BSp.Balance16) != 0:
        if Index == count:
            Hold = GetCurrency(IA4562BSp.Balance16)
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.CYAdjAmt) != 0 or GetCurrency(IA4562BSp.Balance17) != 0:
        if Index == count:
            Hold = GetCurrency(IA4562BSp.Balance17)
            count = 99
        else:
            count = count + 1
    ReturnVal = Hold

def PrChangeY_Calculation(Index):
    count = Integer()

    Hold = Boolean()
    count = 0
    Hold = 0
    if GetCurrency(IA4562BSp.AdjAmt(0)) != 0 or GetCurrency(IA4562BSp.Balance1) != 0:
        if Index == count:
            Hold = GetBool(IA4562BSp.ChangeY(0))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(1)) != 0 or GetCurrency(IA4562BSp.Balance2) != 0:
        if Index == count:
            Hold = GetBool(IA4562BSp.ChangeY(1))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(2)) != 0 or GetCurrency(IA4562BSp.Balance3) != 0:
        if Index == count:
            Hold = GetBool(IA4562BSp.ChangeY(2))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(3)) != 0 or GetCurrency(IA4562BSp.Balance4) != 0:
        if Index == count:
            Hold = GetBool(IA4562BSp.ChangeY(3))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(4)) != 0 or GetCurrency(IA4562BSp.Balance5) != 0:
        if Index == count:
            Hold = GetBool(IA4562BSp.ChangeY(4))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(5)) != 0 or GetCurrency(IA4562BSp.Balance6) != 0:
        if Index == count:
            Hold = GetBool(IA4562BSp.ChangeY(5))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(6)) != 0 or GetCurrency(IA4562BSp.Balance7) != 0:
        if Index == count:
            Hold = GetBool(IA4562BSp.ChangeY(6))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(7)) != 0 or GetCurrency(IA4562BSp.Balance8) != 0:
        if Index == count:
            Hold = GetBool(IA4562BSp.ChangeY(7))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(8)) != 0 or GetCurrency(IA4562BSp.Balance9) != 0:
        if Index == count:
            Hold = GetBool(IA4562BSp.ChangeY(8))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(9)) != 0 or GetCurrency(IA4562BSp.Balance10) != 0:
        if Index == count:
            Hold = GetBool(IA4562BSp.ChangeY(9))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(10)) != 0 or GetCurrency(IA4562BSp.Balance11) != 0:
        if Index == count:
            Hold = GetBool(IA4562BSp.ChangeY(10))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(11)) != 0 or GetCurrency(IA4562BSp.Balance12) != 0:
        if Index == count:
            Hold = GetBool(IA4562BSp.ChangeY(11))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(12)) != 0 or GetCurrency(IA4562BSp.Balance13) != 0:
        if Index == count:
            Hold = GetBool(IA4562BSp.ChangeY(12))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(13)) != 0 or GetCurrency(IA4562BSp.Balance14) != 0:
        if Index == count:
            Hold = GetBool(IA4562BSp.ChangeY(13))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(14)) != 0 or GetCurrency(IA4562BSp.Balance15) != 0:
        if Index == count:
            Hold = GetBool(IA4562BSp.ChangeY(14))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(15)) != 0 or GetCurrency(IA4562BSp.Balance16) != 0:
        if Index == count:
            Hold = GetBool(IA4562BSp.ChangeY(15))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.CYAdjAmt) != 0 or GetCurrency(IA4562BSp.Balance17) != 0:
        if Index == count:
            Hold = GetBool(IA4562BSp.ChangeY(16))
            count = 99
        else:
            count = count + 1
    ReturnVal = Hold

def Print_Calculation():
    if GetCurrency(IA4562BSp.PrBalance(0)) != 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def PrPeriodEnd_Calculation(Index):
    count = Integer()

    Hold = String()
    count = 0
    Hold = ''
    if GetCurrency(IA4562BSp.AdjAmt(0)) != 0 or GetCurrency(IA4562BSp.Balance1) != 0:
        if Index == count:
            Hold = GetString(IA4562BSp.PeriodEnd(0))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(1)) != 0 or GetCurrency(IA4562BSp.Balance2) != 0:
        if Index == count:
            Hold = GetString(IA4562BSp.PeriodEnd(1))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(2)) != 0 or GetCurrency(IA4562BSp.Balance3) != 0:
        if Index == count:
            Hold = GetString(IA4562BSp.PeriodEnd(2))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(3)) != 0 or GetCurrency(IA4562BSp.Balance4) != 0:
        if Index == count:
            Hold = GetString(IA4562BSp.PeriodEnd(3))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(4)) != 0 or GetCurrency(IA4562BSp.Balance5) != 0:
        if Index == count:
            Hold = GetString(IA4562BSp.PeriodEnd(4))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(5)) != 0 or GetCurrency(IA4562BSp.Balance6) != 0:
        if Index == count:
            Hold = GetString(IA4562BSp.PeriodEnd(5))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(6)) != 0 or GetCurrency(IA4562BSp.Balance7) != 0:
        if Index == count:
            Hold = GetString(IA4562BSp.PeriodEnd(6))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(7)) != 0 or GetCurrency(IA4562BSp.Balance8) != 0:
        if Index == count:
            Hold = GetString(IA4562BSp.PeriodEnd(7))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(8)) != 0 or GetCurrency(IA4562BSp.Balance9) != 0:
        if Index == count:
            Hold = GetString(IA4562BSp.PeriodEnd(8))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(9)) != 0 or GetCurrency(IA4562BSp.Balance10) != 0:
        if Index == count:
            Hold = GetString(IA4562BSp.PeriodEnd(9))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(10)) != 0 or GetCurrency(IA4562BSp.Balance11) != 0:
        if Index == count:
            Hold = GetString(IA4562BSp.PeriodEnd(10))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(11)) != 0 or GetCurrency(IA4562BSp.Balance12) != 0:
        if Index == count:
            Hold = GetString(IA4562BSp.PeriodEnd(11))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(12)) != 0 or GetCurrency(IA4562BSp.Balance13) != 0:
        if Index == count:
            Hold = GetString(IA4562BSp.PeriodEnd(12))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(13)) != 0 or GetCurrency(IA4562BSp.Balance14) != 0:
        if Index == count:
            Hold = GetString(IA4562BSp.PeriodEnd(13))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(14)) != 0 or GetCurrency(IA4562BSp.Balance15) != 0:
        if Index == count:
            Hold = GetString(IA4562BSp.PeriodEnd(14))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.AdjAmt(15)) != 0 or GetCurrency(IA4562BSp.Balance16) != 0:
        if Index == count:
            Hold = GetString(IA4562BSp.PeriodEnd(15))
            count = 99
        else:
            count = count + 1
    if GetCurrency(IA4562BSp.CYAdjAmt) != 0 or GetCurrency(IA4562BSp.Balance17) != 0:
        if Index == count:
            Hold = GetString(IA4562BSp.PeriodEnd(16))
            count = 99
        else:
            count = count + 1
    ReturnVal = Hold

def SSN_Calculation():
    ReturnVal = GetString(IA4562Sp.SSN)

