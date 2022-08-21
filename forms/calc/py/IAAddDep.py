from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Description_Calculation():
    if GetNumber(USWAddDep.GrandTotDeps) == 1:
        ReturnVal = CStr(GetNumber(USWAddDep.GrandTotDeps)) + ' Dependent'
    elif GetNumber(USWAddDep.GrandTotDeps) > 1:
        ReturnVal = CStr(GetNumber(USWAddDep.GrandTotDeps)) + ' Dependents'
    else:
        ReturnVal = 'Dependents'

def FDepAge_Calculation(Index):
    max = Long()

    count = Long()

    Hits = Long()
    max = GetAllCopies(USWDependents)
    Hits = 0
    count = 0
    while count < max:
        count = count + 1
        if GetNumber(USWDependents.DepQual, count) == 1:
            if Hits == Index:
                ReturnVal = GetNumber(USWDependents.DepAge, count)
            else:
                Hits = Hits + 1
    ReturnVal = 0

def FDepLast_Calculation(Index):
    max = Long()

    count = Long()

    Hits = Long()
    max = GetAllCopies(USWDependents)
    Hits = 0
    count = 0
    while count < max:
        count = count + 1
        if GetNumber(USWDependents.DepQual, count) == 1:
            if Hits == Index:
                ReturnVal = GetString(USWDependents.DepLast, count)
            else:
                Hits = Hits + 1
    ReturnVal = ''

def FDepName_Calculation(Index):
    max = Long()

    count = Long()

    Hits = Long()
    max = GetAllCopies(USWDependents)
    Hits = 0
    count = 0
    while count < max:
        count = count + 1
        if GetNumber(USWDependents.DepQual, count) == 1:
            if Hits == Index:
                ReturnVal = GetString(USWDependents.DepName, count)
            else:
                Hits = Hits + 1
    ReturnVal = ''

def FDepRel_Calculation(Index):
    max = Long()

    count = Long()

    Hits = Long()
    max = GetAllCopies(USWDependents)
    Hits = 0
    count = 0
    while count < max:
        count = count + 1
        if GetNumber(USWDependents.DepQual, count) == 1:
            if Hits == Index:
                ReturnVal = GetString(USWDependents.DepRel, count)
            else:
                Hits = Hits + 1
    ReturnVal = ''

def FDEPSSN_Calculation(Index):
    max = Long()

    count = Long()

    Hits = Long()
    max = GetAllCopies(USWDependents)
    Hits = 0
    count = 0
    while count < max:
        count = count + 1
        if GetNumber(USWDependents.DepQual, count) == 1:
            if Hits == Index:
                ReturnVal = GetString(USWDependents.DepSSN, count)
            else:
                Hits = Hits + 1
    ReturnVal = ''

def Names_Calculation():
    ReturnVal = GetString(IARequired.CombNames)

def PrintMe_Calculation():
    if GetString(IAF1040.DepNames) == 'See Attached':
        ReturnVal = 1
    else:
        ReturnVal = 0

def SSN_Calculation():
    ReturnVal = GetString(IAF1040.SSN)

