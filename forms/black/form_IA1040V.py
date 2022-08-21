# This file is autogenerated, please do not edit directly!
from ..Base import Form
from ..Base import Property
from ..Base import Label, TextBox, Font, CheckBox, Line, Shape, ComboBox


class IA1040V(Form):
    # Form attributes
    Locked = True
    FormName = "IA1040V"
    FormHeight = 635
    FormWidth = 607
    FormListLongDesc = "Individual Income Tax Payment Voucher"
    TabSequence = True
    SignatureField = "Desc"
    FormPennies = "ROUND_PENNIES"
    FreeToPrint = True

    # Form Properties
    CreateForm = Property(Create="Create(IAF1040.TotDue)")
    FormType = Property(FormType="Normal")
    FormListFolder = Property(FormListFolder="Forms")
    FormListNumber = Property(FormListNumber=30)
    FormListShortDesc = Property(FormListShortDesc="Form IA 1040-V")
    MaxCopies = Property(MaxCopies=1)
    NewScript = Property(NewScript="")
    ReviewScript = Property(ReviewScript="")
    HelpTopic = Property(HelpTopic="")
    TaxTutor = Property(TaxTutor="")

    # Form Components
    SSN = TextBox(
        FieldName="SSN",
        DisplayFieldName="SSN",
        FieldType="SSN",
        FieldVersion="",
        Index="",
        VirtualArraySize="",
        FieldDesc="",
        DefaultVal="",
        DefaultYear="",
        TabSequence=2,
        FieldPennies="",
        MaxLength="11",
        SpawnLink=True,
        Top=63,
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
    Add = TextBox(
        FieldName="Add",
        DisplayFieldName="Add",
        FieldType="String",
        FieldVersion="",
        Index="",
        VirtualArraySize="",
        FieldDesc="",
        DefaultVal="",
        DefaultYear="",
        TabSequence=3,
        FieldPennies="",
        MaxLength="25",
        SpawnLink=True,
        Top=95,
        Left=80,
        Height=17,
        Width=360,
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
        TabSequence=8,
        FieldPennies="",
        MaxLength="",
        SpawnLink=True,
        Top=280,
        Left=272,
        Height=57,
        Width=65,
        Alignment="Left Justify",
        BackgroundColor="0x00ffffff",
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
    PrVou = TextBox(
        FieldName="PrVou",
        DisplayFieldName="PrVou",
        FieldType="Number",
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
        Top=400,
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
    Label1 = Label(
        Caption="When you pay by check, you authorize the Department",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=208,
        Left=200,
        Height=14,
        Width=265,
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
    Label2 = Label(
        Caption="Iowa Department or Revenue",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=192,
        Left=8,
        Height=16,
        Width=165,
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
    Label3 = Label(
        Caption="Mail to:",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=176,
        Left=8,
        Height=15,
        Width=40,
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
        Caption="Individual Income Tax Payment Voucher",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=16,
        Left=296,
        Height=19,
        Width=306,
        Font={
            "Name": '"Arial"',
            "Size": 12,
            "Charset": 0,
            "Weight": 700,
            "Underline": True,
            "Italic": True,
            "Strikethrough": True,
        },
    )
    Label5 = Label(
        Caption="Iowa Department of Revenue",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=0,
        Left=8,
        Height=16,
        Width=185,
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
        Y1=368,
        Y2=368,
    )
    Label6 = Label(
        Caption="Description",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=376,
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
    Line1 = Line(
        LineColor="0x00000000",
        LineWidth=1,
        BottomLine=True,
        X1=80,
        X2=440,
        Y1=144,
        Y2=144,
    )
    Label7 = Label(
        Caption="Address:",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=96,
        Left=8,
        Height=14,
        Width=45,
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
    Label8 = Label(
        Caption="SSN:",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=48,
        Left=448,
        Height=14,
        Width=24,
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
    Label9 = Label(
        Caption="Period Ending:",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=80,
        Left=448,
        Height=14,
        Width=68,
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
    Label10 = Label(
        Caption="Make checks payable to:",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=176,
        Left=200,
        Height=15,
        Width=140,
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
    Label11 = Label(
        Caption="Payment Amount",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=112,
        Left=448,
        Height=14,
        Width=81,
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
    CombNames = TextBox(
        FieldName="CombNames",
        DisplayFieldName="CombNames",
        FieldType="String",
        FieldVersion="",
        Index="",
        VirtualArraySize="",
        FieldDesc="",
        DefaultVal="",
        DefaultYear="",
        TabSequence=1,
        FieldPennies="",
        MaxLength="25",
        SpawnLink=True,
        Top=63,
        Left=80,
        Height=17,
        Width=360,
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
    Line2 = Line(
        LineColor="0x00000000",
        LineWidth=1,
        BottomLine=True,
        X1=448,
        X2=600,
        Y1=112,
        Y2=112,
    )
    Label12 = Label(
        Caption="Treasurer, State of Iowa",
        BackgroundColor="0x00ffffff",
        FontColor="0x00000000",
        Alignment="Left Justify",
        Ellipses="",
        AutoSize=True,
        Top=192,
        Left=200,
        Height=15,
        Width=137,
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
