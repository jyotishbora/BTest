# This file is autogenerated, please do not edit directly!
from ..Base import Form
from ..Base import Property
from ..Base import Label, TextBox, Font, CheckBox, Line, Shape, ComboBox


class IAWHEALTH(Form):
    # Form attributes
    Locked = True
    FormName = "IAWHealth"
    FormHeight = 768
    FormWidth = 607
    FormListLongDesc = "Health Insurance Deduction Worksheet"
    TabSequence = True
    SignatureField = "Description"
    FormPennies = "ROUND_PENNIES"
    FreeToPrint = True

    # Form Properties
    CreateForm = Property(Create="Create(USWRec.PYRepayPTC)")
    FormType = Property(FormType="Normal")
    FormListFolder = Property(FormListFolder="Worksheets")
    FormListNumber = Property(FormListNumber=40)
    FormListShortDesc = Property(
        FormListShortDesc="Form IA 1040 Health Insurance Deduction"
    )
    MaxCopies = Property(MaxCopies=1)
    NewScript = Property(NewScript="")
    ReviewScript = Property(ReviewScript="")
    HelpTopic = Property(HelpTopic="Form 1040 STEP 5 GROSS INCOME")
    TaxTutor = Property(TaxTutor="")

    # Form Components
    TotHealth = TextBox(
        FieldName="TotHealth",
        DisplayFieldName="TotHealth",
        FieldType="Currency",
        FieldVersion="",
        Index="",
        VirtualArraySize="",
        FieldDesc="",
        DefaultVal="",
        DefaultYear="",
        TabSequence=26,
        FieldPennies="",
        MaxLength="",
        SpawnLink=True,
        Top=626,
        Left=392,
        Height=17,
        Width=86,
        Alignment="Left Justify",
        BackgroundColor="0x00c0ffff",
        FontColor="0x00000000",
        StringSubType="",
        NoStrings=True,
        MinRange="",
        MaxRange="",
        TempField=True,
        EFileDetails=True,
        DefaultCalc=True,
        Protected=True,
        HelpLink="",
        PYImport="",
        PYStandardImport="",
        Font={
            "Name": '"Arial"',
            "Size": 8,
            "Charset": 0,
            "Weight": 400,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
        SpawnForms={},
    )
    SPSE = TextBox(
        FieldName="SPSE",
        DisplayFieldName="SPSE",
        FieldType="Currency",
        FieldVersion="",
        Index="",
        VirtualArraySize="",
        FieldDesc="",
        DefaultVal="",
        DefaultYear="",
        TabSequence=24,
        FieldPennies="",
        MaxLength="",
        SpawnLink=True,
        Top=554,
        Left=200,
        Height=17,
        Width=86,
        Alignment="Left Justify",
        BackgroundColor="0x00c0ffff",
        FontColor="0x00000000",
        StringSubType="",
        NoStrings=True,
        MinRange="",
        MaxRange="",
        TempField=True,
        EFileDetails=True,
        DefaultCalc=True,
        Protected=True,
        HelpLink="",
        PYImport="",
        PYStandardImport="",
        Font={
            "Name": '"Arial"',
            "Size": 8,
            "Charset": 0,
            "Weight": 400,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
        SpawnForms={},
    )
    SPTotSE = TextBox(
        FieldName="SPTotSE",
        DisplayFieldName="SPTotSE",
        FieldType="Currency",
        FieldVersion="",
        Index="",
        VirtualArraySize="",
        FieldDesc="",
        DefaultVal="",
        DefaultYear="",
        TabSequence=22,
        FieldPennies="",
        MaxLength="",
        SpawnLink=True,
        Top=578,
        Left=200,
        Height=17,
        Width=86,
        Alignment="Left Justify",
        BackgroundColor="0x00c0ffff",
        FontColor="0x00000000",
        StringSubType="",
        NoStrings=True,
        MinRange="",
        MaxRange="",
        TempField=True,
        EFileDetails=True,
        DefaultCalc=True,
        Protected=True,
        HelpLink="",
        PYImport="",
        PYStandardImport="",
        Font={
            "Name": '"Arial"',
            "Size": 8,
            "Charset": 0,
            "Weight": 400,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
        SpawnForms={},
    )
    SERatio = TextBox(
        FieldName="SERatio",
        DisplayFieldName="SERatio",
        FieldType="Float",
        FieldVersion="",
        Index="",
        VirtualArraySize="",
        FieldDesc="",
        DefaultVal="",
        DefaultYear="",
        TabSequence=20,
        FieldPennies="",
        MaxLength="",
        SpawnLink=True,
        Top=602,
        Left=392,
        Height=17,
        Width=86,
        Alignment="Left Justify",
        BackgroundColor="0x00c0ffff",
        FontColor="0x00000000",
        StringSubType="",
        NoStrings=True,
        MinRange="",
        MaxRange="",
        TempField=True,
        EFileDetails=True,
        DefaultCalc=True,
        Protected=True,
        HelpLink="",
        PYImport="",
        PYStandardImport="",
        Font={
            "Name": '"Arial"',
            "Size": 8,
            "Charset": 0,
            "Weight": 400,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
        SpawnForms={},
    )
    TPLTC = TextBox(
        FieldName="TPLTC",
        DisplayFieldName="TPLTC",
        FieldType="Currency",
        FieldVersion="",
        Index="",
        VirtualArraySize="",
        FieldDesc="",
        DefaultVal="",
        DefaultYear="",
        TabSequence=10,
        FieldPennies="",
        MaxLength="",
        SpawnLink=True,
        Top=215,
        Left=474,
        Height=17,
        Width=124,
        Alignment="Left Justify",
        BackgroundColor="0x00c0ffff",
        FontColor="0x00000000",
        StringSubType="",
        NoStrings=True,
        MinRange="",
        MaxRange="",
        TempField=True,
        EFileDetails=True,
        DefaultCalc=True,
        Protected=True,
        HelpLink="",
        PYImport="",
        PYStandardImport="",
        Font={
            "Name": '"Arial"',
            "Size": 8,
            "Charset": 0,
            "Weight": 400,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
        SpawnForms={},
    )
    TPMedicare = TextBox(
        FieldName="TPMedicare",
        DisplayFieldName="TPMedicare",
        FieldType="Currency",
        FieldVersion="",
        Index="",
        VirtualArraySize="",
        FieldDesc="",
        DefaultVal="",
        DefaultYear="",
        TabSequence=8,
        FieldPennies="",
        MaxLength="",
        SpawnLink=True,
        Top=191,
        Left=474,
        Height=17,
        Width=124,
        Alignment="Left Justify",
        BackgroundColor="0x00c0ffff",
        FontColor="0x00000000",
        StringSubType="",
        NoStrings=True,
        MinRange="",
        MaxRange="",
        TempField=True,
        EFileDetails=True,
        DefaultCalc=True,
        Protected=True,
        HelpLink="",
        PYImport="",
        PYStandardImport="",
        Font={
            "Name": '"Arial"',
            "Size": 8,
            "Charset": 0,
            "Weight": 400,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
        SpawnForms={},
    )
    Exist = TextBox(
        FieldName="Exist",
        DisplayFieldName="Exist",
        FieldType="Number",
        FieldVersion="",
        Index="",
        VirtualArraySize="",
        FieldDesc="",
        DefaultVal="",
        DefaultYear="",
        TabSequence=18,
        FieldPennies="",
        MaxLength="",
        SpawnLink=True,
        Top=482,
        Left=200,
        Height=17,
        Width=86,
        Alignment="Left Justify",
        BackgroundColor="0x00c0ffff",
        FontColor="0x00000000",
        StringSubType="",
        NoStrings=True,
        MinRange="",
        MaxRange="",
        TempField=True,
        EFileDetails=True,
        DefaultCalc=True,
        Protected=True,
        HelpLink="",
        PYImport="",
        PYStandardImport="",
        Font={
            "Name": '"Arial"',
            "Size": 8,
            "Charset": 0,
            "Weight": 400,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
        SpawnForms={},
    )
    TPName = TextBox(
        FieldName="TPName",
        DisplayFieldName=" TPName",
        FieldType="String",
        FieldVersion="",
        Index="",
        VirtualArraySize="",
        FieldDesc="",
        DefaultVal="",
        DefaultYear="",
        TabSequence=17,
        FieldPennies="",
        MaxLength="",
        SpawnLink=True,
        Top=103,
        Left=474,
        Height=17,
        Width=124,
        Alignment="Center Justify",
        BackgroundColor="0x00c0ffff",
        FontColor="0x00000000",
        StringSubType="",
        NoStrings=True,
        MinRange="",
        MaxRange="",
        TempField=True,
        EFileDetails=True,
        DefaultCalc=True,
        Protected=True,
        HelpLink="",
        PYImport="",
        PYStandardImport="",
        Font={
            "Name": '"Arial"',
            "Size": 8,
            "Charset": 0,
            "Weight": 400,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
        SpawnForms={},
    )
    SPTotal = TextBox(
        FieldName="SPTotal",
        DisplayFieldName="SPTotal",
        FieldType="Currency",
        FieldVersion="",
        Index="",
        VirtualArraySize="",
        FieldDesc="",
        DefaultVal="",
        DefaultYear="",
        TabSequence=13,
        FieldPennies="",
        MaxLength="",
        SpawnLink=True,
        Top=263,
        Left=346,
        Height=17,
        Width=124,
        Alignment="Left Justify",
        BackgroundColor="0x00c0ffff",
        FontColor="0x00000000",
        StringSubType="",
        NoStrings=True,
        MinRange="",
        MaxRange="",
        TempField=True,
        EFileDetails=True,
        DefaultCalc=True,
        Protected=True,
        HelpLink="",
        PYImport="",
        PYStandardImport="",
        Font={
            "Name": '"Arial"',
            "Size": 8,
            "Charset": 0,
            "Weight": 400,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
        SpawnForms={},
    )
    TPSEHealth = TextBox(
        FieldName="TPSEHealth",
        DisplayFieldName="TPSEHealth",
        FieldType="Currency",
        FieldVersion="",
        Index="",
        VirtualArraySize="",
        FieldDesc="",
        DefaultVal="",
        DefaultYear="",
        TabSequence=4,
        FieldPennies="",
        MaxLength="",
        SpawnLink=True,
        Top=127,
        Left=474,
        Height=17,
        Width=124,
        Alignment="Left Justify",
        BackgroundColor="0x00c0ffff",
        FontColor="0x00000000",
        StringSubType="",
        NoStrings=True,
        MinRange="",
        MaxRange="",
        TempField=True,
        EFileDetails=True,
        DefaultCalc=True,
        Protected=True,
        HelpLink="",
        PYImport="",
        PYStandardImport="",
        Font={
            "Name": '"Arial"',
            "Size": 8,
            "Charset": 0,
            "Weight": 400,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
        SpawnForms={},
    )
    SPInsPrem = TextBox(
        FieldName="SPInsPrem",
        DisplayFieldName="SPInsPrem",
        FieldType="Currency",
        FieldVersion="",
        Index="",
        VirtualArraySize="",
        FieldDesc="",
        DefaultVal="",
        DefaultYear="",
        TabSequence=5,
        FieldPennies="",
        MaxLength="",
        SpawnLink=True,
        Top=167,
        Left=346,
        Height=17,
        Width=124,
        Alignment="Left Justify",
        BackgroundColor="0x00c0ffff",
        FontColor="0x00000000",
        StringSubType="",
        NoStrings=True,
        MinRange="",
        MaxRange="",
        TempField=True,
        EFileDetails=True,
        DefaultCalc=True,
        Protected=True,
        HelpLink="",
        PYImport="",
        PYStandardImport="",
        Font={
            "Name": '"Arial"',
            "Size": 8,
            "Charset": 0,
            "Weight": 400,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
        SpawnForms={},
    )
    SSN = TextBox(
        FieldName="SSN",
        DisplayFieldName=" SSN",
        FieldType="SSN",
        FieldVersion="",
        Index="",
        VirtualArraySize="",
        FieldDesc="",
        DefaultVal="",
        DefaultYear="",
        TabSequence=2,
        FieldPennies="",
        MaxLength="",
        SpawnLink=True,
        Top=15,
        Left=448,
        Height=17,
        Width=152,
        Alignment="Center Justify",
        BackgroundColor="0x00c0ffff",
        FontColor="0x00000000",
        StringSubType="",
        NoStrings=True,
        MinRange="",
        MaxRange="",
        TempField=True,
        EFileDetails=True,
        DefaultCalc=True,
        Protected=True,
        HelpLink="",
        PYImport="",
        PYStandardImport="",
        Font={
            "Name": '"Arial"',
            "Size": 8,
            "Charset": 0,
            "Weight": 400,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
        SpawnForms={},
    )
    Label1 = Label(
        Caption="Self-employed income ratio",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=602,
        Left=8,
        Height=16,
        Width=157,
        Font={
            "Name": '"Arial"',
            "Size": 9,
            "Charset": 0,
            "Weight": 400,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
    )
    Label2 = Label(
        Caption="Spouse",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=538,
        Left=200,
        Height=14,
        Width=37,
        Font={
            "Name": '"Arial"',
            "Size": 8,
            "Charset": 0,
            "Weight": 400,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
    )
    Label3 = Label(
        Caption="Total SE insurance paid",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=626,
        Left=8,
        Height=16,
        Width=138,
        Font={
            "Name": '"Arial"',
            "Size": 9,
            "Charset": 0,
            "Weight": 400,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
    )
    Label4 = Label(
        Caption="Self-employed income",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=578,
        Left=8,
        Height=16,
        Width=128,
        Font={
            "Name": '"Arial"',
            "Size": 9,
            "Charset": 0,
            "Weight": 400,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
    )
    Line1 = Line(
        LineColor="0x00000000",
        LineWidth=1,
        BottomLine=True,
        X1=344,
        X2=600,
        Y1=232,
        Y2=232,
    )
    Line2 = Line(
        LineColor="0x00000000",
        LineWidth=1,
        BottomLine=True,
        X1=344,
        X2=600,
        Y1=208,
        Y2=208,
    )
    Label5 = Label(
        Caption="self-employed)",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="344",
        AutoSize=True,
        Top=168,
        Left=16,
        Height=16,
        Width=84,
        Font={
            "Name": '"Arial"',
            "Size": 9,
            "Charset": 0,
            "Weight": 400,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
    )
    Label6 = Label(
        Caption="Description",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=458,
        Left=8,
        Height=16,
        Width=65,
        Font={
            "Name": '"Arial"',
            "Size": 9,
            "Charset": 0,
            "Weight": 400,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
    )
    Line3 = Line(
        LineColor="0x00000000",
        LineWidth=1,
        BottomLine=True,
        X1=344,
        X2=600,
        Y1=96,
        Y2=96,
    )
    Label7 = Label(
        Caption="Self-employed health insurance premiums",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="344",
        AutoSize=True,
        Top=128,
        Left=16,
        Height=16,
        Width=242,
        Font={
            "Name": '"Arial"',
            "Size": 9,
            "Charset": 0,
            "Weight": 400,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
    )
    Label8 = Label(
        Caption="Medical and dental care insurance premiums (other than",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=152,
        Left=16,
        Height=16,
        Width=325,
        Font={
            "Name": '"Arial"',
            "Size": 9,
            "Charset": 0,
            "Weight": 400,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
    )
    Line4 = Line(
        LineColor="0x00000000",
        LineWidth=1,
        BottomLine=True,
        X1=472,
        X2=472,
        Y1=96,
        Y2=280,
    )
    Bottom = Line(
        LineColor="0x00000000",
        LineWidth=1,
        BottomLine=True,
        X1=0,
        X2=608,
        Y1=450,
        Y2=450,
    )
    Label9 = Label(
        Caption="Enter 100% of the amount paid for health and dental",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="0",
        AutoSize=True,
        Top=80,
        Left=16,
        Height=16,
        Width=300,
        Font={
            "Name": '"Arial"',
            "Size": 9,
            "Charset": 0,
            "Weight": 400,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
    )
    Line5 = Line(
        LineColor="0x00000000",
        LineWidth=1,
        BottomLine=True,
        X1=344,
        X2=600,
        Y1=144,
        Y2=144,
    )
    Line6 = Line(
        LineColor="0x00000000",
        LineWidth=1,
        BottomLine=True,
        X1=440,
        X2=440,
        Y1=0,
        Y2=32,
    )
    Label10 = Label(
        Caption="Name(s) shown on Form 1040",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=0,
        Left=8,
        Height=14,
        Width=147,
        Font={
            "Name": '"Arial"',
            "Size": 8,
            "Charset": 0,
            "Weight": 400,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
    )
    Line7 = Line(
        LineColor="0x00000000",
        LineWidth=1,
        BottomLine=True,
        X1=8,
        X2=600,
        Y1=280,
        Y2=280,
    )
    Label11 = Label(
        Caption="insurance premiums.  Do not enter amounts paid for ",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="0",
        AutoSize=True,
        Top=92,
        Left=16,
        Height=16,
        Width=304,
        Font={
            "Name": '"Arial"',
            "Size": 9,
            "Charset": 0,
            "Weight": 400,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
    )
    MobDisQual = TextBox(
        FieldName="MobDisQual",
        DisplayFieldName="MobDisQual",
        FieldType="Number",
        FieldVersion="",
        Index="",
        VirtualArraySize="",
        FieldDesc="",
        DefaultVal="",
        DefaultYear="",
        TabSequence=28,
        FieldPennies="",
        MaxLength="",
        SpawnLink=True,
        Top=672,
        Left=200,
        Height=17,
        Width=86,
        Alignment="Left Justify",
        BackgroundColor="0x00c0ffff",
        FontColor="0x00000000",
        StringSubType="",
        NoStrings=True,
        MinRange="",
        MaxRange="",
        TempField=True,
        EFileDetails=True,
        DefaultCalc=True,
        Protected=True,
        HelpLink="",
        PYImport="",
        PYStandardImport="",
        Font={
            "Name": '"Arial"',
            "Size": 8,
            "Charset": 0,
            "Weight": 400,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
        SpawnForms={},
    )
    SPPYRepayPTC = TextBox(
        FieldName="SPPYRepayPTC",
        DisplayFieldName="SPPYRepayPTC",
        FieldType="Currency",
        FieldVersion="",
        Index="",
        VirtualArraySize="",
        FieldDesc="",
        DefaultVal="",
        DefaultYear="",
        TabSequence=11,
        FieldPennies="",
        MaxLength="",
        SpawnLink=True,
        Top=239,
        Left=346,
        Height=17,
        Width=124,
        Alignment="Left Justify",
        BackgroundColor="0x00c0ffff",
        FontColor="0x00000000",
        StringSubType="",
        NoStrings=True,
        MinRange="",
        MaxRange="",
        TempField=True,
        EFileDetails=True,
        DefaultCalc=True,
        Protected=True,
        HelpLink="",
        PYImport="",
        PYStandardImport="",
        Font={
            "Name": '"Arial"',
            "Size": 8,
            "Charset": 0,
            "Weight": 400,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
        SpawnForms={},
    )
    Line8 = Line(
        LineColor="0x00000000",
        LineWidth=1,
        BottomLine=True,
        X1=344,
        X2=600,
        Y1=256,
        Y2=256,
    )
    TotLTC = TextBox(
        FieldName="TotLTC",
        DisplayFieldName="TotLTC",
        FieldType="Currency",
        FieldVersion="",
        Index="",
        VirtualArraySize="",
        FieldDesc="",
        DefaultVal="",
        DefaultYear="",
        TabSequence=27,
        FieldPennies="",
        MaxLength="",
        SpawnLink=True,
        Top=648,
        Left=392,
        Height=17,
        Width=86,
        Alignment="Left Justify",
        BackgroundColor="0x00c0ffff",
        FontColor="0x00000000",
        StringSubType="",
        NoStrings=True,
        MinRange="",
        MaxRange="",
        TempField=True,
        EFileDetails=True,
        DefaultCalc=True,
        Protected=True,
        HelpLink="",
        PYImport="",
        PYStandardImport="",
        Font={
            "Name": '"Arial"',
            "Size": 8,
            "Charset": 0,
            "Weight": 400,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
        SpawnForms={},
    )
