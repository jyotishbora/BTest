from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def DIV_Calculation(Index):
    count = Long()

    max = Long()

    listedcount = Long()
    listedcount = 0
    max = GetAllCopies(USD1099DIV)
    count = 0
    while count < max:
        count = count + 1
        if GetCurrency(USD1099DIV.OrdDiv, count) + GetCurrency(USD1099DIV.FedExmpt, count) > 0:
            if listedcount == Index:
                ReturnVal = count
            else:
                listedcount = listedcount + 1
    ReturnVal = 0

def DIVNbr_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Integer()
    Lim = GetAllCopies(USD1099DIV)
    count = 1
    Total = 0
    while count <= Lim:
        if GetCurrency(USD1099DIV.OrdDiv, count) + GetCurrency(USD1099DIV.FedExmpt, count) > 0:
            Total = Total + 1
        else:
            Total = Total
        count = count + 1
    ReturnVal = Total

def EstK1_Calculation(Index):
    count = Long()

    max = Long()

    listedcount = Long()
    listedcount = 0
    max = GetAllCopies(USDEstK1)
    count = 0
    while count < max:
        count = count + 1
        if GetCurrency(USDEstK1.HaveInt, count) > 0:
            if listedcount == Index:
                ReturnVal = count
            else:
                listedcount = listedcount + 1
    ReturnVal = 0

def EstK1Div_Calculation(Index):
    count = Long()

    max = Long()

    listedcount = Long()
    listedcount = 0
    max = GetAllCopies(USDEstK1)
    count = 0
    while count < max:
        count = count + 1
        if GetCurrency(USDEstK1.Dividends, count) > 0:
            if listedcount == Index:
                ReturnVal = count
            else:
                listedcount = listedcount + 1
    ReturnVal = 0

def EstK1DivNbr_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Integer()
    Lim = GetAllCopies(USDEstK1)
    count = 1
    Total = 0
    while count <= Lim:
        if GetCurrency(USDEstK1.Dividends, count) > 0:
            Total = Total + 1
        else:
            Total = Total
        count = count + 1
    ReturnVal = Total

def EstK1Nbr_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Integer()
    Lim = GetAllCopies(USDEstK1)
    count = 1
    Total = 0
    while count <= Lim:
        if GetCurrency(USDEstK1.HaveInt, count) > 0:
            Total = Total + 1
        else:
            Total = Total
        count = count + 1
    ReturnVal = Total

def F5471_Calculation(Index):
    count = Long()

    max = Long()

    listedcount = Long()
    listedcount = 0
    max = GetAllCopies(USW5471SchI)
    count = 0
    while count < max:
        count = count + 1
        if GetCurrency(USW5471SchI.DivOrd, count) > 0 and  ( ( GetString(USW5471SchI.SchISSN, count) == GetString(USWBasicInfo.SSN) )  or  ( GetString(USW5471SchI.SchISSN, count) == GetString(USWBasicInfo.SpouseSSN) ) ) :
            if listedcount == Index:
                ReturnVal = count
            else:
                listedcount = listedcount + 1
    ReturnVal = 0

def F5471Nbr_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Integer()
    Lim = GetAllCopies(USW5471SchI)
    count = 1
    Total = 0
    while count <= Lim:
        if GetCurrency(USW5471SchI.DivOrd, count) > 0 and  ( ( GetString(USW5471SchI.SchISSN, count) == GetString(USWBasicInfo.SSN) )  or  ( GetString(USW5471SchI.SchISSN, count) == GetString(USWBasicInfo.SpouseSSN) ) ) :
            Total = Total + 1
        else:
            Total = Total
        count = count + 1
    ReturnVal = Total

def F8621_Calculation(Index):
    count = Long()

    max = Long()

    listedcount = Long()
    listedcount = 0
    max = GetAllCopies(USF8621)
    count = 0
    while count < max:
        count = count + 1
        if GetCurrency(USF8621.DivTo1040, count) > 0:
            if listedcount == Index:
                ReturnVal = count
            else:
                listedcount = listedcount + 1
    ReturnVal = 0

def F8621Nbr_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Integer()
    Lim = GetAllCopies(USF8621)
    count = 1
    Total = 0
    while count <= Lim:
        if GetCurrency(USF8621.DivTo1040, count) > 0:
            Total = Total + 1
        else:
            Total = Total
        count = count + 1
    ReturnVal = Total

def F8814_Calculation(Index):
    count = Long()

    max = Long()

    listedcount = Long()
    listedcount = 0
    max = GetAllCopies(USF8814)
    count = 0
    while count < max:
        count = count + 1
        if GetCurrency(USF8814.L6XL7, count) > 0:
            if listedcount == Index:
                ReturnVal = count
            else:
                listedcount = listedcount + 1
    ReturnVal = 0

def F8814Nbr_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Integer()
    Lim = GetAllCopies(USF8814)
    count = 1
    Total = 0
    while count <= Lim:
        if GetCurrency(USF8814.L6XL7, count) > 0:
            Total = Total + 1
        else:
            Total = Total
        count = count + 1
    ReturnVal = Total

def INT_Calculation(Index):
    count = Long()

    max = Long()

    listedcount = Long()
    listedcount = 0
    max = GetAllCopies(USD1099INT)
    count = 0
    while count < max:
        count = count + 1
        if GetCurrency(USD1099INT.BAmtEF, count) + GetCurrency(USD1099INT.FedExmpt, count) > 0:
            if listedcount == Index:
                ReturnVal = count
            else:
                listedcount = listedcount + 1
    ReturnVal = 0

def INTNbr_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Integer()
    Lim = GetAllCopies(USD1099INT)
    count = 1
    Total = 0
    while count <= Lim:
        if GetCurrency(USD1099INT.BAmtEF, count) + GetCurrency(USD1099INT.FedExmpt, count) > 0:
            Total = Total + 1
        else:
            Total = Total
        count = count + 1
    ReturnVal = Total

def Names_Calculation():
    ReturnVal = GetString(IASchB.Names)

def OID_Calculation(Index):
    count = Long()

    max = Long()

    listedcount = Long()
    listedcount = 0
    max = GetAllCopies(USD1099OID)
    count = 0
    while count < max:
        count = count + 1
        if GetCurrency(USD1099OID.BAmt, count) > 0 or Round(GetCurrency(USD1099OID.BOIDAdjAmt, count)) != 0 or Round(GetCurrency(USD1099OID.TaxExempt, count)) != 0:
            if listedcount == Index:
                ReturnVal = count
            else:
                listedcount = listedcount + 1
    ReturnVal = 0

def OIDNbr_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Integer()
    Lim = GetAllCopies(USD1099OID)
    count = 1
    Total = 0
    while count <= Lim:
        if GetCurrency(USD1099OID.BAmt, count) > 0 or Round(GetCurrency(USD1099OID.BOIDAdjAmt, count)) != 0 or Round(GetCurrency(USD1099OID.TaxExempt, count)) != 0:
            Total = Total + 1
        else:
            Total = Total
        count = count + 1
    ReturnVal = Total

def OthSFM_Calculation(Index):
    count = Long()

    max = Long()

    listedcount = Long()
    listedcount = 0
    max = GetAllCopies(USDSFM)
    count = 0
    while count < max:
        count = count + 1
        if GetBool(USDSFM.Residence, count) == False and GetCurrency(USDSFM.Interest, count) > 0:
            if listedcount == Index:
                ReturnVal = count
            else:
                listedcount = listedcount + 1
    ReturnVal = 0

def OthSFMNbr_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Integer()
    Lim = GetAllCopies(USDSFM)
    count = 1
    Total = 0
    while count <= Lim:
        if GetBool(USDSFM.Residence, count) == False and GetCurrency(USDSFM.Interest, count) > 0:
            Total = Total + 1
        else:
            Total = Total
        count = count + 1
    ReturnVal = Total

def PartK1_Calculation(Index):
    count = Long()

    max = Long()

    listedcount = Long()
    listedcount = 0
    max = GetAllCopies(USDPartK1)
    count = 0
    while count < max:
        count = count + 1
        if GetCurrency(USDPartK1.HaveInt, count) > 0:
            if listedcount == Index:
                ReturnVal = count
            else:
                listedcount = listedcount + 1
    ReturnVal = 0

def PartK1Div_Calculation(Index):
    count = Long()

    max = Long()

    listedcount = Long()
    listedcount = 0
    max = GetAllCopies(USDPartK1)
    count = 0
    while count < max:
        count = count + 1
        if GetCurrency(USDPartK1.Dividends, count) > 0:
            if listedcount == Index:
                ReturnVal = count
            else:
                listedcount = listedcount + 1
    ReturnVal = 0

def PartK1DivNbr_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Integer()
    Lim = GetAllCopies(USDPartK1)
    count = 1
    Total = 0
    while count <= Lim:
        if GetCurrency(USDPartK1.Dividends, count) > 0:
            Total = Total + 1
        else:
            Total = Total
        count = count + 1
    ReturnVal = Total

def PartK1Nbr_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Integer()
    Lim = GetAllCopies(USDPartK1)
    count = 1
    Total = 0
    while count <= Lim:
        if GetCurrency(USDPartK1.HaveInt, count) > 0:
            Total = Total + 1
        else:
            Total = Total
        count = count + 1
    ReturnVal = Total

def ResSFM_Calculation(Index):
    count = Long()

    max = Long()

    listedcount = Long()
    listedcount = 0
    max = GetAllCopies(USDSFM)
    count = 0
    while count < max:
        count = count + 1
        if GetBool(USDSFM.Residence, count) == True and GetCurrency(USDSFM.Interest, count) > 0:
            if listedcount == Index:
                ReturnVal = count
            else:
                listedcount = listedcount + 1
    ReturnVal = 0

def ResSFMNbr_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Integer()
    Lim = GetAllCopies(USDSFM)
    count = 1
    Total = 0
    while count <= Lim:
        if GetBool(USDSFM.Residence, count) == True and GetCurrency(USDSFM.Interest, count) > 0:
            Total = Total + 1
        else:
            Total = Total
        count = count + 1
    ReturnVal = Total

def SCorpK1_Calculation(Index):
    count = Long()

    max = Long()

    listedcount = Long()
    listedcount = 0
    max = GetAllCopies(USDSCorpK1)
    count = 0
    while count < max:
        count = count + 1
        if GetCurrency(USDSCorpK1.HaveInt, count) > 0:
            if listedcount == Index:
                ReturnVal = count
            else:
                listedcount = listedcount + 1
    ReturnVal = 0

def SCorpK1Div_Calculation(Index):
    count = Long()

    max = Long()

    listedcount = Long()
    listedcount = 0
    max = GetAllCopies(USDSCorpK1)
    count = 0
    while count < max:
        count = count + 1
        if GetCurrency(USDSCorpK1.Dividends, count) > 0:
            if listedcount == Index:
                ReturnVal = count
            else:
                listedcount = listedcount + 1
    ReturnVal = 0

def SCorpK1DivNbr_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Integer()
    Lim = GetAllCopies(USDSCorpK1)
    count = 1
    Total = 0
    while count <= Lim:
        if GetCurrency(USDSCorpK1.Dividends, count) > 0:
            Total = Total + 1
        else:
            Total = Total
        count = count + 1
    ReturnVal = Total

def SCorpK1Nbr_Calculation():
    count = Integer()

    Lim = Integer()

    Total = Integer()
    Lim = GetAllCopies(USDSCorpK1)
    count = 1
    Total = 0
    while count <= Lim:
        if GetCurrency(USDSCorpK1.HaveInt, count) > 0:
            Total = Total + 1
        else:
            Total = Total
        count = count + 1
    ReturnVal = Total

def SSN_Calculation():
    ReturnVal = GetString(IASchB.SSN)

