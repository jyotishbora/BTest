from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def ExpressCantFile_Calculation():
    if GetBool(IAF1040.HOH) == True:
        ReturnVal = 1
    elif GetBool(IAF1040.QualWidow) == True:
        ReturnVal = 1
    elif GetBool(IAF126.SpPYNR) == True:
        ReturnVal = 1
    elif GetBool(IAF126.TpPYNR) == True:
        ReturnVal = 1
    elif GetBool(IAF1040.ItemCheck) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

def NotQualifyEF_Calculation():
    if GetBool(IAWEFQual.QualifiesForEF) == True:
        ReturnVal = 0
    else:
        ReturnVal = 1

def Qual10_Calculation():
    #State now allows
    #If GetBool(USWResidency.F1040NR) = True Then
    #    ReturnVal = 1
    #Else
    ReturnVal = 0
    #End If

def Qual20_Calculation():
    if GetCurrency(IAF1040.AGainDed) != 0:
        ReturnVal = 1
    elif GetCurrency(IAF1040.BGainDed) != 0 and GetBool(IAF1040.CombMFS) == True:
        ReturnVal = 1
    else:
        ReturnVal = 0

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
        if GetBool(IACred.NonRefCr, count) == True and GetBool(IACred.Taxpayer, count) == True and GetString(IACred.Code, count) == '08':
            Total = Total + 1
        else:
            Total = Total
        count = count + 1
    Lim2 = GetAllCopies(IACred)
    count2 = 1
    Total2 = 0
    while count2 <= Lim2:
        if GetBool(IACred.NonRefCr, count2) == True and GetBool(IACred.Spouse, count2) == True and GetString(IACred.Code, count2) == '08':
            Total2 = Total2 + 1
        else:
            Total2 = Total2
        count2 = count2 + 1
    if Total != 0:
        ReturnVal = 1
    elif GetBool(IAF1040.CombMFS) == False:
        ReturnVal = 0
    elif Total2 != 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Qual40_Calculation():
    ReturnVal = 0

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
        if GetBool(IACred.NonRefCr, count) == True and GetBool(IACred.Taxpayer, count) == True and GetString(IACred.Code, count) == '28':
            Total = Total + 1
        else:
            Total = Total
        count = count + 1
    Lim2 = GetAllCopies(IACred)
    count2 = 1
    Total2 = 0
    while count2 <= Lim2:
        if GetBool(IACred.NonRefCr, count2) == True and GetBool(IACred.Spouse, count2) == True and GetString(IACred.Code, count2) == '28':
            Total2 = Total2 + 1
        else:
            Total2 = Total2
        count2 = count2 + 1
    if Total != 0:
        ReturnVal = 1
    elif GetBool(IAF1040.CombMFS) == False:
        ReturnVal = 0
    elif Total2 != 0:
        ReturnVal = 1
    else:
        ReturnVal = 0

def Qual50_Calculation():
    if ( GetCurrency(IA2210.Penalty) > 0 )  or  ( GetCurrency(IA2210Sp.Penalty) > 0 ) :
        ReturnVal = 1
    else:
        ReturnVal = 0

def QualifiesForEF_Calculation():
    if IsPhone() == True:
        if GetBool(IAWEFQual.Qual10) == True or GetBool(IAWEFQual.Qual20) == True or GetBool(IAWEFQual.Qual30) == True or GetBool(IAWEFQual.Qual40) == True or GetBool(IAWEFQual.Qual45) == True or GetBool(IAWEFQual.Qual50) == True:
            ReturnVal = 0
        else:
            ReturnVal = 1
    elif GetBool(IAWEFQual.Qual10) == True or GetBool(IAWEFQual.Qual20) == True or GetBool(IAWEFQual.Qual30) == True or GetBool(IAWEFQual.Qual40) == True or GetBool(IAWEFQual.Qual45) == True:
        ReturnVal = 0
    else:
        ReturnVal = 1

def Names_Calculation():
    ReturnVal = GetString(IARequired.CombNames)

def Reject10_Calculation():
    SameRTN = Integer()

    SameDAN = Integer()

    SameType = Integer()
    if GetString(USWRALApp.StateRTRTN) == GetString(IAEFWksht.DirDepRTN):
        SameRTN = 1
    else:
        SameRTN = 0
    if GetString(USWRALApp.StateRTDAN) == GetString(IAEFWksht.DirDepDan):
        SameDAN = 1
    else:
        SameDAN = 0
    if GetBool(USWRALApp.StRTCheck) == True and GetBool(IAEFWksht.DirDepChecking) == True:
        SameType = 1
    elif GetBool(USWRALApp.StRTSave) == True and GetBool(IAEFWksht.DirDepSavings) == True:
        SameType = 1
    else:
        SameType = 0
    if GetBool(USWBankProd.IsStateRPT) == True and GetBool(IAEFWksht.IsStateRPT) == True and GetBool(USWRALApp.StateRTDD) == True:
        if SameRTN + SameDAN + SameType != 3:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def Reject20_Calculation():
    if GetBool(IAEFWksht.IsStateRPT) == True:
        if GetBool(USWRALApp.StateRTDD) == True and GetBool(IAEFWksht.DirDeposit) == False:
            ReturnVal = 1
        elif GetBool(USWRALApp.StateRTDC) == True and GetBool(IAEFWksht.DebitCard) == False and GetBool(IAEFWksht.AskDebitCard) == True:
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def Reject50_Calculation():
    if GetBool(IAEFWksht.PrepBPTrans) == True:
        ReturnVal = 0
    elif GetBool(IAEFWksht.DebitCard) == True and GetCurrency(IAEFWksht.Refund) > 0:
        ReturnVal = 0
    elif GetNumber(IAEFWksht.EFDDCode) != 0:
        if Trim(GetString(IAEFWksht.Acct)) == '':
            ReturnVal = 1
        else:
            ReturnVal = 0
    else:
        ReturnVal = 0

def Reject60_Calculation():
    if GetNumber(IAEFWksht.EFDDCode) == 2:
        if GetYear(GetDate(IAEFWksht.EFWDate)) == YearNumber + 1:
            ReturnVal = 0
        else:
            ReturnVal = 1
    else:
        ReturnVal = 0

