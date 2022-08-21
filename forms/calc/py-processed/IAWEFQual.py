from forms.out import IA2210
from forms.out import IA2210SP
from forms.out import IAEFWKSHT
from forms.out import IAF1040
from forms.out import IAF126
from forms.out import IAREQUIRED
from forms.out import IAWEFQUAL
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def ExpressCantFile_Calculation():
    if get_bool(IAF1040.HOH) == True:
        return 1
    elif get_bool(IAF1040.QualWidow) == True:
        return 1
    elif get_bool(IAF126.SpPYNR) == True:
        return 1
    elif get_bool(IAF126.TpPYNR) == True:
        return 1
    elif get_bool(IAF1040.ItemCheck) == True:
        return 1
    else:
        return 0

def NotQualifyEF_Calculation():
    if get_bool(IAWEFQUAL.QualifiesForEF) == True:
        return 0
    else:
        return 1

def Qual10_Calculation():
    #State now allows
    #If get_bool(USWResidency.F1040NR) = True Then
    #    return 1
    #Else
    return 0
    #End If

def Qual20_Calculation():
    if get_currency(IAF1040.AGainDed) != 0:
        return 1
    elif get_currency(IAF1040.BGainDed) != 0 and get_bool(IAF1040.CombMFS) == True:
        return 1
    else:
        return 0

def Qual30_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Integer()

    count2 = Integer()

    Lim2 = Integer()

    Total2 = Integer()
    Lim = GetAllCopies(IACred)
    count = 1
    Total = 0
    while count <= Lim:
        if get_bool(IACred.NonRefCr, count) == True and get_bool(IACred.Taxpayer, count) == True and get_string(IACred.Code, count) == '08':
            Total = Total + 1
        else:
            Total = Total
        count = count + 1
    Lim2 = GetAllCopies(IACred)
    count2 = 1
    Total2 = 0
    while count2 <= Lim2:
        if get_bool(IACred.NonRefCr, count2) == True and get_bool(IACred.Spouse, count2) == True and get_string(IACred.Code, count2) == '08':
            Total2 = Total2 + 1
        else:
            Total2 = Total2
        count2 = count2 + 1
    if Total != 0:
        return 1
    elif get_bool(IAF1040.CombMFS) == False:
        return 0
    elif Total2 != 0:
        return 1
    else:
        return 0

def Qual40_Calculation():
    return 0

def Qual45_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Integer()

    count2 = Integer()

    Lim2 = Integer()

    Total2 = Integer()
    Lim = GetAllCopies(IACred)
    count = 1
    Total = 0
    while count <= Lim:
        if get_bool(IACred.NonRefCr, count) == True and get_bool(IACred.Taxpayer, count) == True and get_string(IACred.Code, count) == '28':
            Total = Total + 1
        else:
            Total = Total
        count = count + 1
    Lim2 = GetAllCopies(IACred)
    count2 = 1
    Total2 = 0
    while count2 <= Lim2:
        if get_bool(IACred.NonRefCr, count2) == True and get_bool(IACred.Spouse, count2) == True and get_string(IACred.Code, count2) == '28':
            Total2 = Total2 + 1
        else:
            Total2 = Total2
        count2 = count2 + 1
    if Total != 0:
        return 1
    elif get_bool(IAF1040.CombMFS) == False:
        return 0
    elif Total2 != 0:
        return 1
    else:
        return 0

def Qual50_Calculation():
    if ( get_currency(IA2210.Penalty) > 0 )  or  ( get_currency(IA2210SP.Penalty) > 0 ) :
        return 1
    else:
        return 0

def QualifiesForEF_Calculation():
    if IsPhone() == True:
        if get_bool(IAWEFQUAL.Qual10) == True or get_bool(IAWEFQUAL.Qual20) == True or get_bool(IAWEFQUAL.Qual30) == True or get_bool(IAWEFQUAL.Qual40) == True or get_bool(IAWEFQUAL.Qual45) == True or get_bool(IAWEFQUAL.Qual50) == True:
            return 0
        else:
            return 1
    elif get_bool(IAWEFQUAL.Qual10) == True or get_bool(IAWEFQUAL.Qual20) == True or get_bool(IAWEFQUAL.Qual30) == True or get_bool(IAWEFQUAL.Qual40) == True or get_bool(IAWEFQUAL.Qual45) == True:
        return 0
    else:
        return 1

def Names_Calculation():
    return get_string(IAREQUIRED.CombNames)

def Reject10_Calculation():
    SameRTN = Integer()

    SameDAN = Integer()

    SameType = Integer()
    if get_string(USWRALApp.StateRTRTN) == get_string(IAEFWKSHT.DirDepRTN):
        SameRTN = 1
    else:
        SameRTN = 0
    if get_string(USWRALApp.StateRTDAN) == get_string(IAEFWKSHT.DirDepDan):
        SameDAN = 1
    else:
        SameDAN = 0
    if get_bool(USWRALApp.StRTCheck) == True and get_bool(IAEFWKSHT.DirDepChecking) == True:
        SameType = 1
    elif get_bool(USWRALApp.StRTSave) == True and get_bool(IAEFWKSHT.DirDepSavings) == True:
        SameType = 1
    else:
        SameType = 0
    if get_bool(USWBankProd.IsStateRPT) == True and get_bool(IAEFWKSHT.IsStateRPT) == True and get_bool(USWRALApp.StateRTDD) == True:
        if SameRTN + SameDAN + SameType != 3:
            return 1
        else:
            return 0
    else:
        return 0

def Reject20_Calculation():
    if get_bool(IAEFWKSHT.IsStateRPT) == True:
        if get_bool(USWRALApp.StateRTDD) == True and get_bool(IAEFWKSHT.DirDeposit) == False:
            return 1
        elif get_bool(USWRALApp.StateRTDC) == True and get_bool(IAEFWKSHT.DebitCard) == False and get_bool(IAEFWKSHT.AskDebitCard) == True:
            return 1
        else:
            return 0
    else:
        return 0

def Reject50_Calculation():
    if get_bool(IAEFWKSHT.PrepBPTrans) == True:
        return 0
    elif get_bool(IAEFWKSHT.DebitCard) == True and get_currency(IAEFWKSHT.Refund) > 0:
        return 0
    elif get_number(IAEFWKSHT.EFDDCode) != 0:
        if trim(get_string(IAEFWKSHT.Acct)) == '':
            return 1
        else:
            return 0
    else:
        return 0

def Reject60_Calculation():
    if get_number(IAEFWKSHT.EFDDCode) == 2:
        if GetYear(GetDate(IAEFWKSHT.EFWDate)) == YearNumber + 1:
            return 0
        else:
            return 1
    else:
        return 0


