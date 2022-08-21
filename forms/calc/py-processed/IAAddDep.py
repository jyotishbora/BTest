from forms.out import IAF1040
from forms.out import IAREQUIRED
from forms.calc.tools import *
from vb2py.vbfunctions import *
from vb2py.vbdebug import *



def Description_Calculation():
    if get_number(USWAddDep.GrandTotDeps) == 1:
        return CStr(get_number(USWAddDep.GrandTotDeps)) + ' Dependent'
    elif get_number(USWAddDep.GrandTotDeps) > 1:
        return CStr(get_number(USWAddDep.GrandTotDeps)) + ' Dependents'
    else:
        return 'Dependents'

def FDepAge_Calculation(Index):
    max = Long()

    count = Long()

    Hits = Long()
    max = GetAllCopies(USWDependents)
    Hits = 0
    count = 0
    while count < max:
        count = count + 1
        if get_number(USWDependents.DepQual, count) == 1:
            if Hits == Index:
                return get_number(USWDependents.DepAge, count)
            else:
                Hits = Hits + 1
    return 0

def FDepLast_Calculation(Index):
    max = Long()

    count = Long()

    Hits = Long()
    max = GetAllCopies(USWDependents)
    Hits = 0
    count = 0
    while count < max:
        count = count + 1
        if get_number(USWDependents.DepQual, count) == 1:
            if Hits == Index:
                return get_string(USWDependents.DepLast, count)
            else:
                Hits = Hits + 1
    return ''

def FDepName_Calculation(Index):
    max = Long()

    count = Long()

    Hits = Long()
    max = GetAllCopies(USWDependents)
    Hits = 0
    count = 0
    while count < max:
        count = count + 1
        if get_number(USWDependents.DepQual, count) == 1:
            if Hits == Index:
                return get_string(USWDependents.DepName, count)
            else:
                Hits = Hits + 1
    return ''

def FDepRel_Calculation(Index):
    max = Long()

    count = Long()

    Hits = Long()
    max = GetAllCopies(USWDependents)
    Hits = 0
    count = 0
    while count < max:
        count = count + 1
        if get_number(USWDependents.DepQual, count) == 1:
            if Hits == Index:
                return get_string(USWDependents.DepRel, count)
            else:
                Hits = Hits + 1
    return ''

def FDEPSSN_Calculation(Index):
    max = Long()

    count = Long()

    Hits = Long()
    max = GetAllCopies(USWDependents)
    Hits = 0
    count = 0
    while count < max:
        count = count + 1
        if get_number(USWDependents.DepQual, count) == 1:
            if Hits == Index:
                return get_string(USWDependents.DepSSN, count)
            else:
                Hits = Hits + 1
    return ''

def Names_Calculation():
    return get_string(IAREQUIRED.CombNames)

def PrintMe_Calculation():
    if get_string(IAF1040.DepNames) == 'See Attached':
        return 1
    else:
        return 0

def SSN_Calculation():
    return get_string(IAF1040.SSN)


