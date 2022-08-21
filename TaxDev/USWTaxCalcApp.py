import datetime
from decimal import Decimal

SSWageBase = 0
StdDedHOH = 1
StdDedAddSingle = 1
YearNumber = datetime.datetime.now().year


def c_dollar(x):
    return Decimal(x)


def CLng(x):
    return Decimal(x)


def CCur(x):
    return Decimal(x)


def CDbl(x):
    return int(x)


def SingleTax(x):
    return x


def MFSTax(x):
    return x


def HohTax(x):
    return x


def JointTax(x):
    return x


# StatusS = CheckBox(FieldName="StatusS", FieldType="CheckBox", Index="", DefaultVal="")
# HOHY = CheckBox(FieldName="HOHY", FieldType="CheckBox", Index="", DefaultVal="")
# QWY = CheckBox(FieldName="QWY", FieldType="CheckBox", Index="", DefaultVal="")


class USWTaxCalcApp:
    def __init__(self, TPWage):
        self.TPWage = TPWage

    Taxes = 0
    MortInt = 0
    MedDent = 0
    QBID = 0
    QWY = False
    DOPR = False
    OthDed = 0
    StudLoan = 0
    SPIRCont = 0
    SPDOB = None
    SPIRACont = 0
    TPCovered = False
    MFS = False
    TPIRACont = 0
    TPDOB = datetime.datetime.now() - datetime.timedelta(weeks=52 * 30)
    MFJ = False
    CharCont = 0
    StatusS = True
    StatusM = False
    HOHY = True
    IRAN = False
    Sm2or14 = 0
    TaxAdj = 0
    QualDiv = 0
    LTCapGain = 0
    STCapGain = 0
    OthInc = 0
    TotSSB = 0
    IntInc = 0
    DivInc = 0
    TPWH = 1
    TPBus = 0  # Not Sure of source.. Business Income Deduction?
    StRef = 0
    IRAPen = 0
    Unem = 0

    def Tax_Calculation(self):
        Mid = Decimal()
        MidInt = int()
        TaxInc = Decimal()
        Tax = Decimal()

        TaxInc = self.TaxInc_Calculation()
        if TaxInc > Decimal("99999"):
            Mid = TaxInc
        elif TaxInc > Decimal("2999"):
            MidInt = CLng(TaxInc / Decimal("50"))
            Mid = (CCur(MidInt) * Decimal("50")) + Decimal("25")
        elif TaxInc > Decimal("24"):
            MidInt = CLng(TaxInc / Decimal("25"))
            Mid = (CCur(MidInt) * Decimal("25")) + Decimal("12.5")
        elif TaxInc > Decimal("14"):
            Mid = Decimal("20")
        elif TaxInc > Decimal("4"):
            Mid = Decimal("10")
        else:
            Mid = Decimal("0")
        if self.Single_Calculation:
            Tax = SingleTax(Mid)
        elif self.MFS:
            Tax = MFSTax(Mid)
        elif self.HOH:
            Tax = HOHTax(Mid)
        else:
            Tax = JointTax(Mid)
        if Decimal(self.QualDiv) > 0:
            return Decimal(self.DTax)
        elif Decimal(self.LTCapGain) > 0 and Decimal(self.NetD_Calculation()) > 0:
            return Decimal(self.DTax)
        else:
            return Tax

    def DTax_Calculation(self):
        if Decimal(self.QualDiv) == 0 and Decimal(self.LTCapGain) == 0:
            return Decimal(self.Ln25)
        else:
            return min(Decimal(self.Ln28), Decimal(self.Ln25))

    def Refund_Calculation(self):
        return max(
            0, Decimal(self.TotCredits) + Decimal(self.TotWH) - Decimal(self.TotTax)
        )

    def TotCredits_Calculation(self):
        return (
            Decimal(self.RefEduCred)
            + Decimal(self.ACTC)
            + Decimal(self.EIC)
            + Decimal(self.DCC)
        )

    def TotWH_Calculation(self):
        if self.MFJ:
            return Decimal(self.TPWH) + Decimal(self.SPWH)
        else:
            return Decimal(self.TPWH)

    def TotTax_Calculation(self):
        return Decimal(self.NetTax) + Decimal(self.OthTax)

    def TaxInc_Calculation(self):
        calc = (
            self.AGI_Calculation()
            - Decimal(self.StdDed_Calculation())
            - Decimal(self.CharContDed_Calculation())
            - Decimal(self.QBID)
        )
        return max(0, calc)

    def AGI_Calculation(self):
        return self.TotInc_Calculation() - self.TotDed_Calculation()

    def TotInc_Calculation(self):
        # Spouse = Decimal()
        if self.MFJ:
            Spouse = Decimal(self.SPWage) + Decimal(self.SPBus)
        else:
            Spouse = 0
        return (
            self.TPWage
            + self.TPBus
            + Spouse
            + Decimal(self.IntInc)
            + Decimal(self.DivInc)
            + Decimal(self.NetD_Calculation())
            + Decimal(self.StRef)
            + Decimal(self.IRAPen)
            + Decimal(self.Unem)
            + Decimal(self.TaxSSB_Calculation())
            + Decimal(self.OthInc)
        )

    def TotDed_Calculation(self):
        return (
            Decimal(self.HalfSE_Calculation())
            + Decimal(self.IRADed_Calculation())
            + Decimal(self.StudLoanDed_Calculation())
            + Decimal(self.OthDed)
        )

    def IRADed_Calculation(self):
        return Decimal(self.TPIRA_Calculation()) + Decimal(self.SPIRA_Calculation())

    def TPIRA_Calculation(self):
        if not self.IRAN:
            return Decimal(self.TPMaxDed_Calculation())
        else:
            return 0

    def TPMaxDed_Calculation(self):
        ContLimit = Decimal()

        EILimit = Decimal()
        # Updated for 2021
        if int(self.TPAge_Calculation()) > 49:
            ContLimit = min(Decimal("7000"), Decimal(self.TPIRACont))
        else:
            ContLimit = min(Decimal("6000"), Decimal(self.TPIRACont))
        EILimit = max(0, min(ContLimit, Decimal(self.TPIRAEI_Calculation())))
        if self.MFJ and self.TPCovered and not self.SPCovered:
            return EILimit
        elif not self.MFJ and not self.TPCovered:
            return EILimit
        else:
            return min(Decimal(self.TPMaxIRA), EILimit)

    def TPIRAEI_Calculation(self):
        return Decimal(self.TPWage) + max(
            0, Decimal(self.TPBus) - Decimal(self.TPHalfSE_Calculation())
        )

    def TPAge_Calculation(self):
        if self.TPDOB:
            return YearNumber - self.TPDOB.year
        else:
            return 0

    def SPIRA_Calculation(self):
        if not self.IRAN:
            return Decimal(self.SPMaxDed_Calculation())
        else:
            return 0

    def SPMaxDed_Calculation(self):
        ContLimit = Decimal()

        EILimit = Decimal()
        # Updated for 2021
        if self.SPAge_Calculation() > 49:
            ContLimit = min(Decimal("7000"), Decimal(self.SPIRACont))
        else:
            ContLimit = min(Decimal("6000"), Decimal(self.SPIRACont))
        EILimit = max(0, min(ContLimit, Decimal(self.SPIRAEI_Calculation())))
        if self.MFJ and not self.SPCovered and not self.TPCovered:
            return EILimit
        else:
            return min(Decimal(self.SPMaxIRA_Calculation()), EILimit)

    def SPTopLim_Calculation(self):
        # Updated for 2021
        if self.MFJ and not self.SPCovered and not self.TPCovered:
            return 0
        elif self.MFJ and not self.SPCovered and self.TPCovered:
            return Decimal("208000")
        elif self.MFJ and self.SPCovered:
            return Decimal("125000")
        else:
            return 0

    def SPMAGI_Calculation(self):
        if self.MFJ:
            return max(
                0,
                Decimal(self.TotInc_Calculation())
                - Decimal(self.HalfSE_Calculation())
                - Decimal(self.OthDed),
            )
        else:
            return 0

    def StudLoanDed_Calculation(self):
        StudLoanInt = Decimal()

        MAGI = Decimal()

        Excess = Decimal()

        Ratio = int()

        PhaseOut = Decimal()
        StudLoanInt = min(Decimal("2500"), Decimal(self.StudLoan))
        MAGI = (
            Decimal(self.TotInc_Calculation())
            - Decimal(self.HalfSE_Calculation())
            - Decimal(self.IRADed_Calculation())
            - Decimal(self.OthDed)
        )
        if self.MFS or self.DOPR:
            return 0
        elif self.MFJ:
            Excess = max(0, MAGI - Decimal("140000"))
            Ratio = min(1, CDbl(Excess) / 3000000)
        else:
            Excess = max(0, MAGI - Decimal("70000"))
            Ratio = min(1, CDbl(Excess) / 1500000)
        PhaseOut = c_dollar(Ratio * CDbl(StudLoanInt))
        return StudLoanInt - PhaseOut

    def SPExcInc_Calculation(self):
        return max(
            0, Decimal(self.SPTopLim_Calculation()) - Decimal(self.SPMAGI_Calculation())
        )

    def SPMaxIRA_Calculation(self):
        Frac = float()

        IntFrac = Decimal()
        # Updated for 2021
        if Decimal(self.SPExcInc_Calculation()) == 0:
            return 0
        elif self.MFJ and self.SPCovered:
            if int(self.SPAge) > 49 and int(self.SPExcInc_Calculation()) > Decimal(
                "20000"
            ):
                return Decimal("7000")
            elif Decimal(self.SPExcInc_Calculation()) > Decimal("20000"):
                return Decimal("6000")
            else:
                if int(self.SPAge) > 49:
                    Frac = float(self.SPExcInc_Calculation()) * 0.35
                    IntFrac = CCur(Frac)
                    if (IntFrac % Decimal("10")) == 0:
                        return max(Decimal("200"), IntFrac)
                    else:
                        return max(
                            Decimal("200"),
                            IntFrac + Decimal("10") - (IntFrac % Decimal("10")),
                        )
                else:
                    Frac = float(self.SPExcInc_Calculation()) * 0.30
                    IntFrac = CCur(Frac)
                    if (IntFrac % Decimal("10")) == 0:
                        return max(Decimal("200"), IntFrac)
                    else:
                        return max(
                            Decimal("200"),
                            IntFrac + Decimal("10") - (IntFrac % Decimal("10")),
                        )
        elif int(self.SPAge) > 49 and Decimal(self.SPExcInc_Calculation()) > Decimal(
            "10000"
        ):
            return Decimal("7000")
        elif Decimal(self.SPExcInc_Calculation()) > Decimal("10000"):
            return Decimal("6000")
        else:
            if int(self.SPAge) > 49:
                Frac = float(self.SPExcInc_Calculation()) * 0.70
                IntFrac = CCur(Frac)
                if (IntFrac % Decimal("10")) == 0:
                    return max(Decimal("200"), IntFrac)
                else:
                    return max(
                        Decimal("200"),
                        IntFrac + Decimal("10") - (IntFrac % Decimal("10")),
                    )
            else:
                Frac = float(self.SPExcInc) * 0.60
                IntFrac = CCur(Frac)
                if (IntFrac % Decimal("10")) == 0:
                    return max(Decimal("200"), IntFrac)
                else:
                    return max(
                        Decimal("200"),
                        IntFrac + Decimal("10") - (IntFrac % Decimal("10")),
                    )

    def SPIRAEI_Calculation(self):
        if self.MFJ:
            return Decimal(self.SPWage) + max(
                0, Decimal(self.SPBus) - Decimal(self.SPHalfSE)
            )
        else:
            return 0

    def Single_Calculation(self):
        if self.StatusS:
            if not self.HOHY and self.QWY:
                return 1
            else:
                return 0
        else:
            return 0

    def AllowableDed_Calculation(self):
        return Decimal(self.ItemDed_Calculation())

    def NetTax_Calculation(self):
        # return max(0, Decimal(self.Tax) + Decimal(self.AMT) - Decimal(self.CTC) - Decimal(self.DCC) - Decimal(self.ResEnergy) - Decimal(self.NonrefEduCred) - Decimal(self.OthCredits))
        return max(
            0,
            Decimal(self.Tax)
            + Decimal(self.AMT)
            - Decimal(self.CTC)
            - Decimal(self.ResEnergy)
            - Decimal(self.NonrefEduCred)
            - Decimal(self.OthCredits),
        )

    def RefEduCred_Calculation(self):
        if self.EduN:
            return Decimal(self.RefAOC)
        else:
            return 0

    def ACTC_Calculation(self):
        # return Decimal(self.AddChildCr)
        return Decimal(self.ChildTaxCredit)

    def ChildTaxCredit_Calculation(self):
        CROthDep = Decimal()
        if Decimal(self.P1BCalcCr) - Decimal(self.P1BAdvCrRecd) < 0:
            CROthDep = 0
        else:
            CROthDep = min(Decimal(self.P1BSmaller), Decimal(self.P1BAvailCr))
        if Decimal(self.P1BCalcCr) - Decimal(self.P1BAdvCrRecd) < 0:
            return 0
        else:
            return Decimal(self.P1BAvailCr) - CROthDep

    def P1BCalcCr_Calculation(self):
        return Decimal(self.P1BTempCr) + Decimal(self.P1BSmaller)

    def P1BTempCr_Calculation(self):
        return Decimal(self.PhaseCR) - Decimal(self.LowCr)

    def P1BSmaller_Calculation(self):
        return min(Decimal(self.LowCr), Decimal(self.CTCNetTax))

    def LowCr_Calculation(self):
        return min(Decimal(self.OthCred), Decimal(self.PhaseCR))

    def CTCNetTax_Calculation(self):
        TaxLiab = Decimal()

        TaxCreds = Decimal()
        TaxLiab = Decimal(self.Tax) + Decimal(self.AMT)
        TaxCreds = (
            Decimal(self.DCC) + Decimal(self.NonrefEduCred) + Decimal(self.ResEnergy)
        )
        if Decimal(self.PhaseCR) > 0:
            return max(0, TaxLiab - TaxCreds)
        else:
            return 0

    def OthCred_Calculation(self):
        if self.DOPR or self.DepN:
            return 0
        else:
            return (Decimal(self.StudDeps) * Decimal("500")) + (
                Decimal(self.OthDeps) * Decimal("500")
            )

    def TaxSSB_Calculation(self):
        return min(
            Decimal(self.L15andL16_Calculation()), Decimal(self.FullAmt_Calculation())
        )

    def HalfSE_Calculation(self):
        return Decimal(self.TPHalfSE_Calculation()) + Decimal(
            self.SPHalfSE_Calculation()
        )

    def TPHalfSE_Calculation(self):
        NetSE = Decimal()

        RedThd = Decimal()

        Excess = Decimal()
        NetSE = c_dollar(Decimal(self.TPBus) * Decimal(0.9235))
        if self.MFJ:
            RedThd = max(
                0, Decimal("250000") - Decimal(self.TPWage) - Decimal(self.SPWage)
            )
        elif self.MFS_Calculation():
            RedThd = max(0, Decimal("125000") - Decimal(self.TPWage))
        else:
            RedThd = max(0, Decimal("200000") - Decimal(self.TPWage))
        Excess = c_dollar(max(0, CDbl(NetSE - RedThd)) * Decimal(0.009))
        return c_dollar(
            (Decimal(self.TPSETax_Calculation()) - CDbl(Excess)) * Decimal(0.5)
        )

    def TPSETax_Calculation(self):
        NetSE = Decimal()

        RedThd = Decimal()

        Excess = Decimal()

        MedTax = Decimal()

        ExcessSS = Decimal()

        SSTax = Decimal()
        NetSE = c_dollar(Decimal(self.TPBus) * Decimal(0.9235))
        if self.MFJ:
            RedThd = max(
                0,
                Decimal("250000") - get_Decimal(self.TPWage) - get_Decimal(self.SPWage),
            )
        elif self.MFS_Calculation():
            RedThd = max(0, Decimal("125000") - Decimal(self.TPWage))
        else:
            RedThd = max(0, Decimal("200000") - Decimal(self.TPWage))
        Excess = c_dollar(max(0, CDbl(NetSE - RedThd)) * 0.009)
        MedTax = c_dollar(CDbl(NetSE) * 0.029) + Excess
        ExcessSS = max(0, SSWageBase - Decimal(self.TPWage))
        SSTax = c_dollar(CDbl(min(NetSE, ExcessSS)) * 0.124)
        if NetSE < Decimal("400"):
            return 0
        else:
            return MedTax + SSTax

    def SPHalfSE_Calculation(self):
        NetSE = Decimal()

        RedThd = Decimal()

        Excess = Decimal()
        if self.MFJ == False:
            return 0
        NetSE = c_dollar(Decimal(self.SPBus) * Decimal(0.9235))
        RedThd = max(0, Decimal("250000") - Decimal(self.TPWage) - Decimal(self.SPWage))
        Excess = c_dollar(max(0, CDbl(NetSE - RedThd)) * Decimal(0.009))
        return c_dollar((Decimal(self.SPSETax) - CDbl(Excess)) * Decimal(0.5))

    def SPSETax_Calculation(self):
        NetSE = Decimal()

        RedThd = Decimal()

        Excess = Decimal()

        MedTax = Decimal()

        ExcessSS = Decimal()

        SSTax = Decimal()
        if self.MFJ:
            return 0
        NetSE = c_dollar(Decimal(self.SPBus) * Decimal(0.9235))
        RedThd = max(0, Decimal("250000") - Decimal(self.TPWage) - Decimal(self.SPWage))
        Excess = c_dollar(max(0, CDbl(NetSE - RedThd)) * Decimal(0.009))
        MedTax = c_dollar(CDbl(NetSE) * Decimal(0.029)) + Excess
        ExcessSS = max(0, SSWageBase - Decimal(self.SPWage))
        SSTax = c_dollar(CDbl(min(NetSE, ExcessSS)) * Decimal(0.124))
        if NetSE < Decimal("400"):
            return 0
        else:
            return MedTax + SSTax

    def StdDed_Calculation(self):
        Std = Decimal()

        EI = Decimal()

        DoPREI = Decimal()

        DoprMax = Decimal()

        DoprAmt = Decimal()

        Allowance = Decimal()

        TP65 = int()

        SP65 = int()
        # Updated Custom
        if int(self.TPAge_Calculation()) > 64:
            TP65 = 1
        else:
            TP65 = 0
        if self.SPAge_Calculation() > 64:
            SP65 = 1
        else:
            SP65 = 0
        if self.MFJ:
            Allowance = c_dollar((TP65 + SP65) * StdDedAdd)
        elif self.MFS or self.QW_Calculation():
            Allowance = c_dollar(TP65 * StdDedAdd)
        else:
            Allowance = c_dollar(TP65 * StdDedAddSingle)
        if self.Single_Calculation() or self.MFS:
            Std = StdDedSingle
        elif self.HOH_Calculation():
            Std = StdDedHOH
        else:
            Std = StdDedMFJ
        if self.DOPR:
            DoprAmt = StdDedDOPR
            EI = (
                Decimal(self.TPWage)
                + Decimal(self.SPWage)
                + Decimal(self.TPBus)
                + Decimal(self.SPBus)
                - Decimal(self.HalfSE_Calculation())
                + StdDedDOPRAdd
            )
            DoPREI = min(Std, EI)
            DoprMax = max(DoprAmt, DoPREI)
            return DoprMax + Allowance
        else:
            return Std + Allowance

    def SPAge_Calculation(self):
        if self.SPDOB:
            return YearNumber - self.SPDOB
        else:
            return 0

    def MFS_Calculation(self):
        if self.StatusM:
            if self.JointN:
                return 1
            else:
                return 0
        else:
            return 0

    def QW_Calculation(self):
        if self.StatusS:
            if not self.HOHY and self.QWY:
                return 1
            else:
                return 0
        else:
            return 0

    def HOH_Calculation(self):
        if self.StatusS and self.HOHY:
            return 1
        else:
            return 0

    def CharContDed_Calculation(self):
        CharContSD = Decimal()
        if self.MFJ:
            CharContSD = min(Decimal("600"), Decimal(self.CharCont))
            # ElseIf get_bool(self.MFS) = True Then
            #    CharContSD = min(150@, Decimal(self.CharCont))
        else:
            CharContSD = min(Decimal("300"), Decimal(self.CharCont))
        if (CharContSD + Decimal(self.StdDed_Calculation())) >= Decimal(
            self.ItemDed_Calculation()
        ):
            return CharContSD
        else:
            return Decimal("0")

    def ItemDed_Calculation(self):
        MedDent = Decimal()

        CharCont = Decimal()

        AGI = Decimal()
        AGI = max(0, Decimal(self.AGI_Calculation()))
        MedDent = max(0, Decimal(self.MedDent) - c_dollar(CDbl(AGI) * Decimal(0.075)))
        CharCont = min(Decimal(self.CharCont), c_dollar(CDbl(AGI) * Decimal(0.6)))
        return (
            MedDent
            + min(Decimal("10000"), Decimal(self.Taxes))
            + Decimal(self.MortInt)
            + CharCont
        )

    def AGI_Calculation(self):
        return Decimal(self.TotInc_Calculation()) - Decimal(self.TotDed_Calculation())

    def QBID_Calculation(self):
        TI = Decimal()

        QBI = Decimal()
        # Updated Custom
        TI = max(
            0,
            Decimal(self.AGI)
            - Decimal(self.QualDiv)
            - max(0, Decimal(self.Net))
            - max(Decimal(self.StdDed_Calculation()), Decimal(self.AllowableDed)),
        )
        QBI = max(
            0,
            Decimal(self.TPBus)
            + Decimal(self.SPBus)
            - Decimal(self.HalfSE_Calculation()),
        )
        if self.MFJ and TI > QBIDLowLimMFJ:
            return 0
        elif self.MFS and TI > QBIDLowLimMFS:
            return 0
        elif self.MFJ and not self.MFS and TI > QBIDLowLimSingle:
            return 0
        else:
            return c_dollar(CDbl(min(QBI, TI)) * Decimal(0.2))

    def Net_Calculation(self):
        if Decimal(self.LTCapGain) > 0 and Decimal(self.NetD_Calculation()) > 0:
            return min(Decimal(self.LTCapGain), Decimal(self.NetD_Calculation()))
        else:
            return 0

    def NetD_Calculation(self):
        if Decimal(self.STCapGain) + Decimal(self.LTCapGain) > 0:
            return Decimal(self.STCapGain) + Decimal(self.LTCapGain)
        elif self.MFS_Calculation():
            return max(
                -Decimal("1500"), Decimal(self.STCapGain) + Decimal(self.LTCapGain)
            )
        else:
            return max(
                -Decimal("3000"), Decimal(self.STCapGain) + Decimal(self.LTCapGain)
            )

    def L15andL16_Calculation(self):
        return Decimal(self.Sm2or14) + Decimal(self.TaxAdj)

    def FullAmt_Calculation(self):
        return c_dollar(Decimal(self.TotSSB) * Decimal(0.85))
