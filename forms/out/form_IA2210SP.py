# This file is autogenerated, please do not edit directly!
from ..Base import Form
from ..Base import Property
from ..Base import Label, TextBox, Font, CheckBox, Line, Shape, ComboBox


class IA2210SP(Form):
    # Form attributes
    Locked = True
    FormName = "IA2210Sp"
    FormHeight = 1635
    FormWidth = 615
    FormListLongDesc = "Underpayment of Estimated Tax by Individuals"
    TabSequence = True
    SignatureField = "Description"
    FormPennies = "ROUND_PENNIES"
    FreeToPrint = True

    # Form Properties
    CreateForm = Property(Create="Create(IAF1040.CombMFS)")
    FormType = Property(FormType="Normal")
    FormListFolder = Property(FormListFolder="Forms")
    FormListNumber = Property(FormListNumber=151)
    FormListShortDesc = Property(FormListShortDesc="Form IA 2210 Spouse")
    MaxCopies = Property(MaxCopies=1)
    NewScript = Property(NewScript="")
    ReviewScript = Property(ReviewScript="")
    HelpTopic = Property(HelpTopic="Form IA 2210")
    TaxTutor = Property(TaxTutor="")

    # Form Components
    EFile = TextBox(FieldName="EFile", DisplayFieldName="EFile", FieldType="Number", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=44, FieldPennies="", MaxLength="", SpawnLink=True, Top=1168, Left=200, Height=17, Width=86, Alignment="Left Justify", BackgroundColor="0x00c0ffff", FontColor="0x00000000", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    EFStQ1 = TextBox(FieldName="EFStQ1", DisplayFieldName="EFStQ1", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=42, FieldPennies="", MaxLength="", SpawnLink=True, Top=1320, Left=200, Height=17, Width=86, Alignment="Left Justify", BackgroundColor="0x00c0ffff", FontColor="0x00000000", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Description = TextBox(FieldName="Description", DisplayFieldName="Description", FieldType="String", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=41, FieldPennies="", MaxLength="", SpawnLink=True, Top=1128, Left=200, Height=17, Width=400, Alignment="Left Justify", BackgroundColor="0x00c0ffff", FontColor="0x00000000", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Exit = TextBox(FieldName="Exit", DisplayFieldName="", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=30, FieldPennies="", MaxLength="", SpawnLink=True, Top=1000, Left=264, Height=57, Width=65, Alignment="Left Justify", BackgroundColor="0x00ffffff", FontColor="0x00000000", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Q4WH = TextBox(FieldName="Q4WH", DisplayFieldName="Q4WH", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=38, FieldPennies="", MaxLength="", SpawnLink=True, Top=1224, Left=520, Height=17, Width=86, Alignment="Left Justify", BackgroundColor="0x00c0ffff", FontColor="0x00000000", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Q2WH = TextBox(FieldName="Q2WH", DisplayFieldName="Q2WH", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=36, FieldPennies="", MaxLength="", SpawnLink=True, Top=1224, Left=304, Height=17, Width=86, Alignment="Left Justify", BackgroundColor="0x00c0ffff", FontColor="0x00000000", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Q2AnInc = TextBox(FieldName="Q2AnInc", DisplayFieldName="Q2AnInc", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=19, FieldPennies="", MaxLength="", SpawnLink=True, Top=555, Left=368, Height=17, Width=78, Alignment="Left Justify", BackgroundColor="0x00c0ffff", FontColor="0x00000000", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, Spawn="Spawn(IA2210AnSp.Names)")
    Q2Install = TextBox(FieldName="Q2Install", DisplayFieldName="Q2Install", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=14, FieldPennies="", MaxLength="", SpawnLink=True, Top=515, Left=368, Height=17, Width=78, Alignment="Left Justify", BackgroundColor="0x00c0ffff", FontColor="0x00000000", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Small = TextBox(FieldName="Small", DisplayFieldName="Small", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=12, FieldPennies="", MaxLength="", SpawnLink=True, Top=447, Left=520, Height=17, Width=86, Alignment="Left Justify", BackgroundColor="0x00c0ffff", FontColor="0x00000000", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Q1Install = TextBox(FieldName="Q1Install", DisplayFieldName="Q1Install", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=13, FieldPennies="", MaxLength="", SpawnLink=True, Top=515, Left=288, Height=17, Width=78, Alignment="Left Justify", BackgroundColor="0x00c0ffff", FontColor="0x00000000", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Q3AnInc = TextBox(FieldName="Q3AnInc", DisplayFieldName="Q3AnInc", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=20, FieldPennies="", MaxLength="", SpawnLink=True, Top=555, Left=448, Height=17, Width=78, Alignment="Left Justify", BackgroundColor="0x00c0ffff", FontColor="0x00000000", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Q4Est = TextBox(FieldName="Q4Est", DisplayFieldName="Q4Est", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=34, FieldPennies="", MaxLength="", SpawnLink=True, Top=1244, Left=520, Height=17, Width=86, Alignment="Left Justify", BackgroundColor="0x00c0ffff", FontColor="0x00000000", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Q3Ln11 = TextBox(FieldName="Q3Ln11", DisplayFieldName="Q3Ln11", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=24, FieldPennies="", MaxLength="", SpawnLink=True, Top=591, Left=448, Height=17, Width=78, Alignment="Left Justify", BackgroundColor="0x00c0ffff", FontColor="0x00000000", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Q4Ln11 = TextBox(FieldName="Q4Ln11", DisplayFieldName="Q4Ln11", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=25, FieldPennies="", MaxLength="", SpawnLink=True, Top=591, Left=528, Height=17, Width=78, Alignment="Left Justify", BackgroundColor="0x00c0ffff", FontColor="0x00000000", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Q2est = TextBox(FieldName="Q2est", DisplayFieldName="Q2est", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=32, FieldPennies="", MaxLength="", SpawnLink=True, Top=1244, Left=304, Height=17, Width=86, Alignment="Left Justify", BackgroundColor="0x00c0ffff", FontColor="0x00000000", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Penalty = TextBox(FieldName="Penalty", DisplayFieldName="Penalty", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=29, FieldPennies="", MaxLength="", SpawnLink=True, Top=927, Left=528, Height=17, Width=80, Alignment="Left Justify", BackgroundColor="0x00c0ffff", FontColor="0x00000000", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, Spawn="Spawn(IAPenaltySp.Names)")
    Q1Est = TextBox(FieldName="Q1Est", DisplayFieldName="Q1Est", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=31, FieldPennies="", MaxLength="", SpawnLink=True, Top=1244, Left=200, Height=17, Width=86, Alignment="Left Justify", BackgroundColor="0x00c0ffff", FontColor="0x00000000", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Amt8 = TextBox(FieldName="Amt8", DisplayFieldName="Amt8", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=10, FieldPennies="", MaxLength="", SpawnLink=True, Top=367, Left=520, Height=17, Width=86, Alignment="Left Justify", BackgroundColor="0x00c0ffff", FontColor="0x00000000", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CYTax = TextBox(FieldName="CYTax", DisplayFieldName="CYTax", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=3, FieldPennies="", MaxLength="", SpawnLink=True, Top=167, Left=520, Height=17, Width=86, Alignment="Left Justify", BackgroundColor="0x00c0ffff", FontColor="0x00000000", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    SSN = TextBox(FieldName="SSN", DisplayFieldName="SSN", FieldType="SSN", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=2, FieldPennies="", MaxLength="", SpawnLink=True, Top=127, Left=448, Height=17, Width=152, Alignment="Center Justify", BackgroundColor="0x00c0ffff", FontColor="0x00000000", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Label1 = Label(Caption="EF condition", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=1168, Left=8, Height=16, Width=73, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Line1 = Line(LineColor="0x00000000", LineWidth=1, BottomLine=True, X1=0, X2=608, Y1=32, Y2=32)
    Label2 = Label(Caption="ONLY USED BY MARRIED FILING SEPARATELY ON THIS COMBINED RETURN FILERS", BackgroundColor="0x00ffffff", FontColor="0x000000ff", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=0, Left=39, Height=16, Width=530, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 700, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label3 = Label(Caption="FIELDS USED FOR ELECTRONIC FILING", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=1296, Left=0, Height=16, Width=249, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 700, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Line2 = Line(LineColor="0x00000000", LineWidth=1, BottomLine=True, X1=287, X2=608, Y1=608, Y2=608)
    Label4 = Label(Caption="FORM CALCULATIONS", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=1200, Left=0, Height=16, Width=143, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 700, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label5 = Label(Caption="Total Iowa tax payments", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=1244, Left=8, Height=16, Width=141, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label6 = Label(Caption="balance. Any overpayment is carried", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=656, Left=24, Height=16, Width=210, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Line3 = Line(LineColor="0x00000000", LineWidth=1, BottomLine=True, X1=528, X2=608, Y1=944, Y2=944)
    Line4 = Line(LineColor="0x00000000", LineWidth=1, BottomLine=True, X1=136, X2=483, Y1=80, Y2=80)
    Line5 = Line(LineColor="0x00000000", LineWidth=1, BottomLine=True, X1=527, X2=527, Y1=632, Y2=944)
    Line6 = Line(LineColor="0x00000000", LineWidth=1, BottomLine=True, X1=367, X2=367, Y1=632, Y2=920)
    Bottom = Line(LineColor="0x00000000", LineWidth=1, BottomLine=True, X1=0, X2=608, Y1=1120, Y2=1120)
    Line7 = Line(LineColor="0x00000000", LineWidth=1, BottomLine=True, X1=287, X2=287, Y1=632, Y2=920)
    Line8 = Line(LineColor="0x00000000", LineWidth=1, BottomLine=True, X1=447, X2=447, Y1=488, Y2=608)
    Line9 = Line(LineColor="0x00000000", LineWidth=1, BottomLine=True, X1=287, X2=287, Y1=472, Y2=608)
    Label7 = Label(Caption="How to Figure the Penalty: Complete lines 10 through 15.", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=616, Left=128, Height=15, Width=317, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 700, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label8 = Label(Caption="Required installment. Enter the amount", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=580, Left=24, Height=16, Width=226, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Line10 = Line(LineColor="0x00000000", LineWidth=1, BottomLine=True, X1=287, X2=608, Y1=532, Y2=532)
    Label9 = Label(Caption="9", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=592, Left=276, Height=15, Width=7, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 700, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label10 = Label(Caption="Divide the amount on line 6 by the number", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=504, Left=24, Height=15, Width=230, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label11 = Label(Caption="(a) Number of days inclusively from due", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=716, Left=24, Height=16, Width=227, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label12 = Label(Caption="date of installment to date of payment", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=728, Left=40, Height=16, Width=218, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label13 = Label(Caption="04/30/<!NEXTYEAR>, whichever is earlier", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="263", AutoSize=True, Top=792, Left=44, Height=15, Width=174, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label14 = Label(Caption="due date of installment, whichever is", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=768, Left=44, Height=16, Width=209, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label15 = Label(Caption="11", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=692, Left=0, Height=15, Width=14, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 700, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Line11 = Line(LineColor="0x00000000", LineWidth=1, BottomLine=True, X1=287, X2=608, Y1=712, Y2=712)
    Line12 = Line(LineColor="0x00000000", LineWidth=1, BottomLine=True, X1=0, X2=608, Y1=632, Y2=632)
    Line13 = Line(LineColor="0x00000000", LineWidth=1, BottomLine=True, X1=287, X2=608, Y1=896, Y2=896)
    Label16 = Label(Caption="13a", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=840, Left=264, Height=15, Width=21, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 700, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Line14 = Line(LineColor="0x00000000", LineWidth=1, BottomLine=True, X1=287, X2=608, Y1=760, Y2=760)
    Label17 = Label(Caption="15", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=928, Left=509, Height=15, Width=14, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 700, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label18 = Label(Caption="15", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=928, Left=0, Height=15, Width=14, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 700, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label19 = Label(Caption="12b", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=792, Left=264, Height=15, Width=21, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 700, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label20 = Label(Caption="on line 10, for the number of days", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=828, Left=44, Height=15, Width=182, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Line15 = Line(LineColor="0x00000000", LineWidth=1, BottomLine=True, X1=288, X2=608, Y1=504, Y2=504)
    Label21 = Label(Caption="June 30, <!YEAR>", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=488, Left=371, Height=14, Width=72, Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 700, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label22 = Label(Caption="Sept. 30, <!YEAR>", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=488, Left=452, Height=14, Width=73, Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 700, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label23 = Label(Caption="shown on line 12(b)", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="263", AutoSize=True, Top=880, Left=44, Height=15, Width=109, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label24 = Label(Caption="on line 10, for the number of days", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=868, Left=44, Height=15, Width=182, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label25 = Label(Caption="Installment payments. Payments are", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=632, Left=24, Height=16, Width=213, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label26 = Label(Caption="8", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=540, Left=8, Height=15, Width=7, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 700, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label27 = Label(Caption="8", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=556, Left=276, Height=15, Width=7, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 700, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label28 = Label(Caption="7", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=504, Left=8, Height=15, Width=7, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 700, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label29 = Label(Caption="on line 7 or line 8, if applicable", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="272", AutoSize=True, Top=592, Left=24, Height=15, Width=166, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label30 = Label(Caption="6", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=448, Left=504, Height=15, Width=7, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 700, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Line16 = Line(LineColor="0x00000000", LineWidth=1, BottomLine=True, X1=512, X2=608, Y1=360, Y2=360)
    Label31 = Label(Caption="6", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=448, Left=8, Height=15, Width=7, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 700, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label32 = Label(Caption="Enter the smaller amount of line 4 or line 5", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="504", AutoSize=True, Top=448, Left=24, Height=15, Width=232, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label33 = Label(Caption="Balance.  Subtract line 2 from line 1", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="504", AutoSize=True, Top=344, Left=24, Height=15, Width=193, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label34 = Label(Caption="3", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=344, Left=504, Height=15, Width=7, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 700, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Line17 = Line(LineColor="0x00000000", LineWidth=1, BottomLine=True, X1=288, X2=608, Y1=472, Y2=472)
    Line18 = Line(LineColor="0x00000000", LineWidth=1, BottomLine=True, X1=0, X2=608, Y1=160, Y2=160)
    Label35 = Label(Caption="<!YEAR> IA 2210", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=64, Left=484, Height=22, Width=116, Font={'Name': '"Arial"', 'Size': 14, 'Charset': 0, 'Weight': 700, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label36 = Label(Caption="5", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=425, Left=504, Height=15, Width=7, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 700, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label37 = Label(Caption="Enter 90% of the amount shown on line 3. If less than $200 see instructions", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="504", AutoSize=True, Top=368, Left=24, Height=15, Width=413, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Line19 = Line(LineColor="0x00000000", LineWidth=1, BottomLine=True, X1=416, X2=416, Y1=184, Y2=312)
    Label38 = Label(Caption="How to Figure Your Underpayment", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=144, Left=192, Height=16, Width=219, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 700, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label39 = Label(Caption="Social Security Number", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=112, Left=448, Height=17, Width=185, Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Line20 = Line(LineColor="0x00000000", LineWidth=1, BottomLine=True, X1=0, X2=608, Y1=144, Y2=144)
    Line21 = Line(LineColor="0x00000000", LineWidth=1, BottomLine=True, X1=0, X2=608, Y1=112, Y2=112)
    Label40 = Label(Caption="Iowa Department of Revenue", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=56, Left=40, Height=15, Width=159, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label41 = Label(Caption="<!YEAR> Tax from Form IA 1040, line 53", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="493", AutoSize=True, Top=168, Left=24, Height=15, Width=197, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label42 = Label(Caption="credit from Form IA 1040 line 60", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="408", AutoSize=True, Top=248, Left=32, Height=15, Width=174, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label43 = Label(Caption="b", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=232, Left=24, Height=15, Width=7, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 700, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label44 = Label(Caption="a", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=208, Left=408, Height=15, Width=7, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 700, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label45 = Label(Caption="Child and dependent care credit or Early childhood development", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=232, Left=32, Height=15, Width=350, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label46 = Label(Caption="a", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=208, Left=24, Height=15, Width=7, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 700, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label47 = Label(Caption="2", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=192, Left=8, Height=16, Width=7, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 700, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label48 = Label(Caption="Credits", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=192, Left=24, Height=15, Width=40, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label49 = Label(Caption="d", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=296, Left=24, Height=15, Width=7, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 700, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    ChildC = TextBox(FieldName="ChildC", DisplayFieldName="ChildC", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=5, FieldPennies="", MaxLength="", SpawnLink=True, Top=247, Left=424, Height=17, Width=86, Alignment="Left Justify", BackgroundColor="0x00c0ffff", FontColor="0x00000000", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Line22 = Line(LineColor="0x00000000", LineWidth=1, BottomLine=True, X1=416, X2=512, Y1=264, Y2=264)
    Line23 = Line(LineColor="0x00000000", LineWidth=1, BottomLine=True, X1=416, X2=512, Y1=288, Y2=288)
    Label50 = Label(Caption="2", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=320, Left=504, Height=15, Width=7, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 700, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    PYZero = CheckBox(FieldName="PYZero", FieldType="CheckBox", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", Caption="Check here if your <!LASTYEAR> tax was zero.", Alignment="Left Justify", BackgroundColor="0x00ffffff", BoxOutline="3D", FontColor="0x00000000", TabSequence=46, DefaultVal="", QuickEntry=True, RadioTag="", TempField=True, Top=432, Left=256, Height=14, Width=207, HelpLink="", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label51 = Label(Caption="Enter your <!LASTYEAR> tax. (less applicable credits)", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="223", AutoSize=True, Top=392, Left=24, Height=15, Width=242, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Label52 = Label(Caption="depreciation/section 179 adjustment from line 14 of the IA 1040 and all other Iowa net income ", BackgroundColor="0x00ffffff", FontColor="0x00000000", Alignment="Left Justify", Ellipses="", AutoSize=True, Top=404, Left=24, Height=14, Width=450, Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
