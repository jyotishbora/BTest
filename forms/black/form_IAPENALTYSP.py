# This file is autogenerated, please do not edit directly!
from ..Base import Form
from ..Base import Property
from ..Base import Label, TextBox, Font, CheckBox, Line, Shape, ComboBox


class IAPENALTYSP(Form):
    # Form attributes
    Locked = True
    FormName = "IAPenaltySp"
    FormHeight = 800
    FormWidth = 607
    FormListLongDesc = "Underpayment Penalty Calculations Worksheet"
    TabSequence = True
    SignatureField = "Desc"
    FormPennies = "ROUND_PENNIES"
    FreeToPrint = True

    # Form Properties
    CreateForm = Property(Create="Create(IA2210Sp.Small)")
    FormType = Property(FormType="Normal")
    FormListFolder = Property(FormListFolder="Worksheets")
    FormListNumber = Property(FormListNumber=601)
    FormListShortDesc = Property(
        FormListShortDesc="Form IA 2210 Underpayment Penalty Spouse"
    )
    MaxCopies = Property(MaxCopies=1)
    NewScript = Property(NewScript="")
    ReviewScript = Property(ReviewScript="")
    HelpTopic = Property(HelpTopic="Form IA 2210")
    TaxTutor = Property(TaxTutor="")

    # Form Components
    Q3Pen3 = TextBox(
        FieldName="Q3Pen3",
        DisplayFieldName="Q3Pen3",
        FieldType="Currency",
        FieldVersion="",
        Index="",
        VirtualArraySize="",
        FieldDesc="",
        DefaultVal="",
        DefaultYear="",
        TabSequence=23,
        FieldPennies="STORE_PENNIES",
        MaxLength="",
        SpawnLink=True,
        Top=303,
        Left=512,
        Height=17,
        Width=86,
        Alignment="Left Justify",
        BackgroundColor="0x00ffff00",
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
    Q3Days3 = TextBox(
        FieldName="Q3Days3",
        DisplayFieldName="Q3Days3",
        FieldType="Number",
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
        Top=303,
        Left=352,
        Height=17,
        Width=54,
        Alignment="Left Justify",
        BackgroundColor="0x00ffff00",
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
    Q3Unpay3 = TextBox(
        FieldName="Q3Unpay3",
        DisplayFieldName="Q3UnPay3",
        FieldType="Currency",
        FieldVersion="",
        Index="",
        VirtualArraySize="",
        FieldDesc="",
        DefaultVal="",
        DefaultYear="",
        TabSequence=21,
        FieldPennies="",
        MaxLength="",
        SpawnLink=True,
        Top=303,
        Left=216,
        Height=17,
        Width=86,
        Alignment="Left Justify",
        BackgroundColor="0x00ffff00",
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
        TabSequence=37,
        FieldPennies="",
        MaxLength="",
        SpawnLink=True,
        Top=588,
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
    Exit = TextBox(
        FieldName="Exit",
        DisplayFieldName="",
        FieldType="Currency",
        FieldVersion="",
        Index="",
        VirtualArraySize="",
        FieldDesc="",
        DefaultVal="",
        DefaultYear="",
        TabSequence=35,
        FieldPennies="",
        MaxLength="",
        SpawnLink=True,
        Top=464,
        Left=272,
        Height=57,
        Width=65,
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
    Q2Pen2 = TextBox(
        FieldName="Q2Pen2",
        DisplayFieldName="Q2Pen2",
        FieldType="Currency",
        FieldVersion="",
        Index="",
        VirtualArraySize="",
        FieldDesc="",
        DefaultVal="",
        DefaultYear="",
        TabSequence=14,
        FieldPennies="STORE_PENNIES",
        MaxLength="",
        SpawnLink=True,
        Top=231,
        Left=512,
        Height=17,
        Width=86,
        Alignment="Left Justify",
        BackgroundColor="0x00ffff00",
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
    Q4Pen2 = TextBox(
        FieldName="Q4Pen2",
        DisplayFieldName="Q4Pen2",
        FieldType="Currency",
        FieldVersion="",
        Index="",
        VirtualArraySize="",
        FieldDesc="",
        DefaultVal="",
        DefaultYear="",
        TabSequence=32,
        FieldPennies="STORE_PENNIES",
        MaxLength="",
        SpawnLink=True,
        Top=375,
        Left=512,
        Height=17,
        Width=86,
        Alignment="Left Justify",
        BackgroundColor="0x00ffff00",
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
    Q4Days1 = TextBox(
        FieldName="Q4Days1",
        DisplayFieldName="Q4Days1",
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
        Top=351,
        Left=352,
        Height=17,
        Width=54,
        Alignment="Left Justify",
        BackgroundColor="0x00ffff00",
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
    Q4Days2 = TextBox(
        FieldName="Q4Days2",
        DisplayFieldName="Q4Days2",
        FieldType="Number",
        FieldVersion="",
        Index="",
        VirtualArraySize="",
        FieldDesc="",
        DefaultVal="",
        DefaultYear="",
        TabSequence=31,
        FieldPennies="",
        MaxLength="",
        SpawnLink=True,
        Top=375,
        Left=352,
        Height=17,
        Width=54,
        Alignment="Left Justify",
        BackgroundColor="0x00ffff00",
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
    Q4UnPay1 = TextBox(
        FieldName="Q4UnPay1",
        DisplayFieldName="Q4UnPay1",
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
        Top=351,
        Left=216,
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
    Q3UnPay2 = TextBox(
        FieldName="Q3UnPay2",
        DisplayFieldName="Q3UnPay2",
        FieldType="Currency",
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
        Top=279,
        Left=216,
        Height=17,
        Width=86,
        Alignment="Left Justify",
        BackgroundColor="0x00ffff00",
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
    Q3Days2 = TextBox(
        FieldName="Q3Days2",
        DisplayFieldName="Q3Days2",
        FieldType="Number",
        FieldVersion="",
        Index="",
        VirtualArraySize="",
        FieldDesc="",
        DefaultVal="",
        DefaultYear="",
        TabSequence=19,
        FieldPennies="",
        MaxLength="",
        SpawnLink=True,
        Top=279,
        Left=352,
        Height=17,
        Width=54,
        Alignment="Left Justify",
        BackgroundColor="0x00ffff00",
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
    Q2UnPay1 = TextBox(
        FieldName="Q2UnPay1",
        DisplayFieldName="Q2UnPay1",
        FieldType="Currency",
        FieldVersion="",
        Index="",
        VirtualArraySize="",
        FieldDesc="",
        DefaultVal="",
        DefaultYear="",
        TabSequence=9,
        FieldPennies="",
        MaxLength="",
        SpawnLink=True,
        Top=207,
        Left=216,
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
    Q2Days1 = TextBox(
        FieldName="Q2Days1",
        DisplayFieldName="Q2Days1",
        FieldType="Number",
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
        Top=207,
        Left=352,
        Height=17,
        Width=54,
        Alignment="Left Justify",
        BackgroundColor="0x00ffff00",
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
    Q2Pen1 = TextBox(
        FieldName="Q2Pen1",
        DisplayFieldName="Q2Pen1",
        FieldType="Currency",
        FieldVersion="",
        Index="",
        VirtualArraySize="",
        FieldDesc="",
        DefaultVal="",
        DefaultYear="",
        TabSequence=11,
        FieldPennies="STORE_PENNIES",
        MaxLength="",
        SpawnLink=True,
        Top=207,
        Left=512,
        Height=17,
        Width=86,
        Alignment="Left Justify",
        BackgroundColor="0x00ffff00",
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
    Q1UnPay1 = TextBox(
        FieldName="Q1UnPay1",
        DisplayFieldName="Q1UnPay1",
        FieldType="Currency",
        FieldVersion="",
        Index="",
        VirtualArraySize="",
        FieldDesc="",
        DefaultVal="",
        DefaultYear="",
        TabSequence=3,
        FieldPennies="",
        MaxLength="",
        SpawnLink=True,
        Top=159,
        Left=216,
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
    Q1Days1 = TextBox(
        FieldName="Q1Days1",
        DisplayFieldName="Q1Days1",
        FieldType="Number",
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
        Top=159,
        Left=352,
        Height=17,
        Width=54,
        Alignment="Left Justify",
        BackgroundColor="0x00ffff00",
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
    Q1Pen1 = TextBox(
        FieldName="Q1Pen1",
        DisplayFieldName="Q1Pen1",
        FieldType="Currency",
        FieldVersion="",
        Index="",
        VirtualArraySize="",
        FieldDesc="",
        DefaultVal="",
        DefaultYear="",
        TabSequence=5,
        FieldPennies="STORE_PENNIES",
        MaxLength="",
        SpawnLink=True,
        Top=159,
        Left=512,
        Height=17,
        Width=86,
        Alignment="Left Justify",
        BackgroundColor="0x00ffff00",
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
    Names = TextBox(
        FieldName="Names",
        DisplayFieldName="Names",
        FieldType="String",
        FieldVersion="",
        Index="",
        VirtualArraySize="",
        FieldDesc="",
        DefaultVal="",
        DefaultYear="",
        TabSequence=1,
        FieldPennies="",
        MaxLength="",
        SpawnLink=True,
        Top=47,
        Left=8,
        Height=17,
        Width=424,
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
    Label1 = Label(
        Caption="SPOUSE COPY",
        BackgroundColor="0x00ffffff",
        FontColor="0x000000ff",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=16,
        Left=257,
        Height=16,
        Width=94,
        Font={
            "Name": '"Arial"',
            "Size": 9,
            "Charset": 0,
            "Weight": 700,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
    )
    Label2 = Label(
        Caption="7%",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=328,
        Left=447,
        Height=15,
        Width=16,
        Font={
            "Name": '"Arial"',
            "Size": 9,
            "Charset": 0,
            "Weight": 700,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
    )
    Line1 = Line(
        LineColor="0x00000000",
        LineWidth=1,
        BottomLine=True,
        X1=216,
        X2=600,
        Y1=320,
        Y2=320,
    )
    Label3 = Label(
        Caption="Penalty on underpayment",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=304,
        Left=24,
        Height=16,
        Width=164,
        Font={
            "Name": '"Arial"',
            "Size": 9,
            "Charset": 0,
            "Weight": 700,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
    )
    Label4 = Label(
        Caption="Exist",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=588,
        Left=8,
        Height=16,
        Width=30,
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
    Line2 = Line(
        LineColor="0x00000000",
        LineWidth=1,
        BottomLine=True,
        X1=600,
        X2=8,
        Y1=296,
        Y2=296,
    )
    Line3 = Line(
        LineColor="0x00000000",
        LineWidth=1,
        BottomLine=True,
        X1=504,
        X2=504,
        Y1=152,
        Y2=416,
    )
    Line4 = Line(
        LineColor="0x00000000",
        LineWidth=1,
        BottomLine=True,
        X1=216,
        X2=600,
        Y1=272,
        Y2=272,
    )
    Line5 = Line(
        LineColor="0x00000000",
        LineWidth=1,
        BottomLine=True,
        X1=216,
        X2=600,
        Y1=224,
        Y2=224,
    )
    Line6 = Line(
        LineColor="0x00000000",
        LineWidth=1,
        BottomLine=True,
        X1=216,
        X2=600,
        Y1=176,
        Y2=176,
    )
    Label5 = Label(
        Caption="Amount",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=136,
        Left=531,
        Height=16,
        Width=49,
        Font={
            "Name": '"Arial"',
            "Size": 9,
            "Charset": 0,
            "Weight": 700,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
    )
    Label6 = Label(
        Caption="Of Days",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=136,
        Left=355,
        Height=16,
        Width=48,
        Font={
            "Name": '"Arial"',
            "Size": 9,
            "Charset": 0,
            "Weight": 700,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
    )
    Label7 = Label(
        Caption="Amount",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=136,
        Left=235,
        Height=16,
        Width=49,
        Font={
            "Name": '"Arial"',
            "Size": 9,
            "Charset": 0,
            "Weight": 700,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
    )
    Label8 = Label(
        Caption="from 10-2-<!YEAR> to 12-31-<!YEAR>",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=280,
        Left=24,
        Height=15,
        Width=168,
        Font={
            "Name": '"Arial"',
            "Size": 9,
            "Charset": 0,
            "Weight": 700,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
    )
    Label9 = Label(
        Caption="from 5-1-<!YEAR> to 7-2-<!YEAR>",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=184,
        Left=24,
        Height=15,
        Width=147,
        Font={
            "Name": '"Arial"',
            "Size": 9,
            "Charset": 0,
            "Weight": 700,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
    )
    Bottom = Line(
        LineColor="0x00000000",
        LineWidth=1,
        BottomLine=True,
        X1=0,
        X2=608,
        Y1=560,
        Y2=560,
    )
    Line7 = Line(
        LineColor="0x00000000",
        LineWidth=1,
        BottomLine=True,
        X1=600,
        X2=600,
        Y1=120,
        Y2=416,
    )
    Label10 = Label(
        Caption="Description",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=568,
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
    Label11 = Label(
        Caption="7%",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=352,
        Left=447,
        Height=15,
        Width=16,
        Font={
            "Name": '"Arial"',
            "Size": 9,
            "Charset": 0,
            "Weight": 700,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
    )
    Label12 = Label(
        Caption="6%",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=280,
        Left=447,
        Height=15,
        Width=16,
        Font={
            "Name": '"Arial"',
            "Size": 9,
            "Charset": 0,
            "Weight": 700,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
    )
    Label13 = Label(
        Caption="6%",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=256,
        Left=447,
        Height=15,
        Width=16,
        Font={
            "Name": '"Arial"',
            "Size": 9,
            "Charset": 0,
            "Weight": 700,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
    )
    Label14 = Label(
        Caption="6%",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=232,
        Left=447,
        Height=15,
        Width=16,
        Font={
            "Name": '"Arial"',
            "Size": 9,
            "Charset": 0,
            "Weight": 700,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
    )
    Label15 = Label(
        Caption="7%",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=376,
        Left=447,
        Height=15,
        Width=16,
        Font={
            "Name": '"Arial"',
            "Size": 9,
            "Charset": 0,
            "Weight": 700,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
    )
    Label16 = Label(
        Caption="Annual",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=120,
        Left=433,
        Height=16,
        Width=45,
        Font={
            "Name": '"Arial"',
            "Size": 9,
            "Charset": 0,
            "Weight": 700,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
    )
    Label17 = Label(
        Caption="Supporting Details for IA Form 2210, line 15",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=100,
        Left=168,
        Height=15,
        Width=243,
        Font={
            "Name": '"Arial"',
            "Size": 9,
            "Charset": 0,
            "Weight": 700,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
    )
    Label18 = Label(
        Caption="Your social security  number",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=32,
        Left=448,
        Height=17,
        Width=185,
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
    Line8 = Line(
        LineColor="0x00000000", LineWidth=1, BottomLine=True, X1=0, X2=608, Y1=64, Y2=64
    )
    Line9 = Line(
        LineColor="0x00000000",
        LineWidth=1,
        BottomLine=True,
        X1=8,
        X2=600,
        Y1=120,
        Y2=120,
    )
    Label19 = Label(
        Caption="Underpayment Penalty Calculations",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=80,
        Left=136,
        Height=22,
        Width=353,
        Font={
            "Name": '"Arial"',
            "Size": 14,
            "Charset": 0,
            "Weight": 700,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
    )
