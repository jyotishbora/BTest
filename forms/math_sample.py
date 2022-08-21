from .out import IAEFWKSHT, USF4972SPOUSE, IAREQUIRED
import unittest

def acc_calculation(n):
    if IAEFWKSHT.IsStateRPT and IAEFWKSHT.AmtOwed and IAEFWKSHT.DirDepRTN:
        return IAEFWKSHT.StateDCReturn
    elif USF4972SPOUSE.CapGainTax > 0:
        max_account = IAREQUIRED.MaxCopies
        for _ in range(max_account):
            if IAREQUIRED.BalDueAmt.count() > 0:
                return IAEFWKSHT.DD
        return None

def test_acc_calculation(self):
    self.assertEquals(acc_calculation(5), 10)

"""
Private Sub Acct_Calculation()
    If GetBool(IAEFWksht.IsStateRPT) = True And GetBool(USWRALApp.StateRTDD) = True And GetBool(IAEFWksht.DirDeposit) = True Then
        ReturnVal = GetString(USWRALApp.StateAccount)
    ElseIf (GetBool(IAEFWksht.DirDeposit) = True And GetCurrency(IAEFWksht.Refund) > 0) Or (GetBool(IAEFWksht.EFW) = True And GetCurrency(IAEFWksht.AmtOwed) > 0) Then
        Dim count As Integer
        Dim MaxAcct As Integer
        Dim Acct As String

        count = 1
        MaxAcct = GetAllCopies(USWBankAcct)
        Acct = ""

        Do While count <= MaxAcct
            If GetString(USWBankAcct.BankAcct, count) <> "" Then
                If GetBool(USWBankAcct.Default, count) = True Then
                    ReturnVal = GetString(USWBankAcct.BankAcct, count)
                    count = 99
                End If
            End If
            count = count + 1
        Loop
        ReturnVal = ""
    Else
        ReturnVal = ""

    End If

End Sub
"""