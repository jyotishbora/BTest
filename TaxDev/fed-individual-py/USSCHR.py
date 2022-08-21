# This file is autogenerated, please do not edit directly!
from forms.Base import Form
from forms.Base import FieldSet, Property
from forms.Base import Label, TextBox, Font, CheckBox


class USSCHR(Form):
    # Form attributes
    Locked = True
    FormName = "USSchR"
    FormHeight = 2835
    FormWidth = 620
    FormListLongDesc = "Credit for the Elderly or the Disabled"
    TabSequence = True
    SignatureField = "Desc"
    ProSignatureField = ""
    FormPennies = "ROUND_PENNIES"
    FreeToPrint = True

    # Form Properties
    CreateForm = Property(Create="Create(USWTaxpayer.SchR)")
    FormType = Property(FormType="Normal")
    FormListFolder = Property(FormListFolder="Forms")
    FormListNumber = Property(FormListNumber=130)
    FormListShortDesc = Property(FormListShortDesc="Schedule R")
    MaxCopies = Property(MaxCopies=1)
    NewScript = Property(NewScript="IV_USSCHR_Status")
    ReviewScript = Property(ReviewScript="IV_USSchR_Status")
    HelpTopic = Property(HelpTopic="Schedule R")
    TaxTutor = Property(TaxTutor="Credit for the Elderly or the Disabled")

    # Form Components
    SSB = TextBox(FieldName="SSB", DisplayFieldName="SSB", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=40, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    personFirstName = TextBox(FieldName="personFirstName", DisplayFieldName="personFirstName", FieldType="String", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=42, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    TaxLbLimit = TextBox(FieldName="TaxLbLimit", DisplayFieldName="TaxLbLimit", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Schedule R, Line 21", DefaultVal="", DefaultYear="", PI="", TabSequence=31, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Schedule R Line 21 Credit Limit", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Check5 = CheckBox(FieldName="Check5", FieldType="CheckBox", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", Caption="Extra", PI="", TabSequence=79, DefaultVal="", QuickEntry=True, RadioTag="", TempField=True, HelpLink="", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Check3 = CheckBox(FieldName="Check3", FieldType="CheckBox", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", Caption="Extra", PI="", TabSequence=81, DefaultVal="", QuickEntry=True, RadioTag="", TempField=True, HelpLink="", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Check1 = CheckBox(FieldName="Check1", FieldType="CheckBox", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", Caption="Extra", PI="", TabSequence=83, DefaultVal="", QuickEntry=True, RadioTag="", TempField=True, HelpLink="", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Extra11 = TextBox(FieldName="Extra11", DisplayFieldName="Extra11", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=74, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Extra14 = TextBox(FieldName="Extra14", DisplayFieldName="Extra14", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=77, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Extra6 = TextBox(FieldName="Extra6", DisplayFieldName="Extra6", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=69, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    SNoAge = CheckBox(FieldName="SNoAge", FieldType="CheckBox", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", Caption="SNoAge", PI="", TabSequence=58, DefaultVal="", QuickEntry=True, RadioTag="", TempField=True, HelpLink="", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    MFJNoAge = CheckBox(FieldName="MFJNoAge", FieldType="CheckBox", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", Caption="MFJNoAge", PI="", TabSequence=52, DefaultVal="", QuickEntry=True, RadioTag="", TempField=True, HelpLink="", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Extra9 = TextBox(FieldName="Extra9", DisplayFieldName="Extra9", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=72, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Extra3 = TextBox(FieldName="Extra3", DisplayFieldName="Extra3", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=66, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    DisName2 = TextBox(FieldName="DisName2", DisplayFieldName="DisName2", FieldType="String", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=44, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    SPDis = CheckBox(FieldName="SPDis", FieldType="CheckBox", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", Caption="Spouse", PI="", TabSequence=15, DefaultVal="", QuickEntry=True, RadioTag="", TempField=True, HelpLink="Schedule R Part II - Statement of Permanent and Total Disability", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    TentCred = TextBox(FieldName="TentCred", DisplayFieldName="TentCred", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Schedule R, Line 20", DefaultVal="", DefaultYear="", PI="", TabSequence=30, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Schedule R Part III - Figure Your Credit", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Extra1 = TextBox(FieldName="Extra1", DisplayFieldName="Extra1", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=64, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Extra5 = TextBox(FieldName="Extra5", DisplayFieldName="Extra5", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=68, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    ActLimitCalc = CheckBox(FieldName="ActLimitCalc", FieldType="CheckBox", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", Caption="ActLimitCalc", PI="", TabSequence=38, DefaultVal="", QuickEntry=True, RadioTag="", TempField=True, HelpLink="", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    MFJ265Over = CheckBox(FieldName="MFJ265Over", FieldType="CheckBox", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", Caption="MFJ265Over", PI="", TabSequence=50, DefaultVal="", QuickEntry=True, RadioTag="", TempField=True, HelpLink="", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    MFSUnder65 = CheckBox(FieldName="MFSUnder65", FieldType="CheckBox", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", Caption="MFSUnder65", PI="", TabSequence=54, DefaultVal="", QuickEntry=True, RadioTag="", TempField=True, HelpLink="", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    S65Over = CheckBox(FieldName="S65Over", FieldType="CheckBox", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", Caption="S65Over", PI="", TabSequence=57, DefaultVal="", QuickEntry=True, RadioTag="", TempField=True, HelpLink="", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    AgeDisable = TextBox(FieldName="AgeDisable", DisplayFieldName="AgeDisable", FieldType="Number", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=62, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Disable = CheckBox(FieldName="Disable", FieldType="CheckBox", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", Caption="Disable", PI="", TabSequence=45, DefaultVal="", QuickEntry=True, RadioTag="", TempField=True, HelpLink="", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    FStatus = TextBox(FieldName="FStatus", DisplayFieldName="FStatus", FieldType="String", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=47, FieldPennies="ContRInt", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    SchR = CheckBox(FieldName="SchR", FieldType="CheckBox", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", Caption="SchR", PI="", TabSequence=36, DefaultVal="", QuickEntry=True, RadioTag="", TempField=True, HelpLink="", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Exist = TextBox(FieldName="Exist", DisplayFieldName="Exist", FieldType="Number", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=35, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Exit = TextBox(FieldName="Exit", DisplayFieldName="", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=33, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    SDisInc = TextBox(FieldName="SDisInc", DisplayFieldName="SdIsInc", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Schedule R, Line 11 spouse disability", DefaultVal="", DefaultYear="", PI="", TabSequence=18, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Schedule R Line 11 Chart", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, Spawn="Spawn(USDRRB1099R.SSN, ExistingCopies)")
    CrdInc = TextBox(FieldName="CrdInc", DisplayFieldName="CrdInc", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Schedule R, Line 19", DefaultVal="", DefaultYear="", PI="", TabSequence=29, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Schedule R Part III - Figure Your Credit", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    HalfExcAGI = TextBox(FieldName="HalfExcAGI", DisplayFieldName="HalfExcAGI", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Schedule R, Line 17", DefaultVal="", DefaultYear="", PI="", TabSequence=27, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Schedule R Lines 13a through 18 - Pensions, Annuities, or Disability Income", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    BaseAGI = TextBox(FieldName="BaseAGI", DisplayFieldName="BaseAGI", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Schedule R, Line 15", DefaultVal="", DefaultYear="", PI="", TabSequence=25, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Schedule R Lines 13a through 18 - Pensions, Annuities, or Disability Income", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    MFS65 = CheckBox(FieldName="MFS65", FieldType="CheckBox", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Schedule R, Line 8", Caption="", PI="", TabSequence=10, DefaultVal="", QuickEntry=True, RadioTag="MFSDis", TempField=True, HelpLink="Schedule R Married Persons Filing Separate Returns", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 700, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    GainfulAct = CheckBox(FieldName="GainfulAct", FieldType="CheckBox", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Schedule R, Part II, Line 2", Caption="", PI="", TabSequence=13, DefaultVal="", QuickEntry=True, RadioTag="", TempField=True, HelpLink="Schedule R Part II - Statement of Permanent and Total Disability", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 700, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Joint2Dis = CheckBox(FieldName="Joint2Dis", FieldType="CheckBox", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Schedule R, Line 5", Caption="", PI="", TabSequence=7, DefaultVal="", QuickEntry=True, RadioTag="Joint1651dis", TempField=True, HelpLink="Schedule R Who Can Take The Credit", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 700, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Joint1Dis = CheckBox(FieldName="Joint1Dis", FieldType="CheckBox", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Schedule R, Line 4", Caption="", PI="", TabSequence=6, DefaultVal="", QuickEntry=True, RadioTag="Joint2Dis", TempField=True, HelpLink="Schedule R Who Can Take The Credit", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 700, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Single65 = CheckBox(FieldName="Single65", FieldType="CheckBox", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Schedule R, Line 1", Caption="", PI="", TabSequence=3, DefaultVal="", QuickEntry=True, RadioTag="SingleDis", TempField=True, HelpLink="Schedule R Who Can Take The Credit", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 700, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    lesserbase = TextBox(FieldName="lesserbase", DisplayFieldName="Lesserbase", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Schedule R, Line 12", DefaultVal="", DefaultYear="", PI="", TabSequence=20, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Schedule R Part III - Figure Your Credit", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Base = TextBox(FieldName="Base", DisplayFieldName="Base", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Schedule R, Line 10", DefaultVal="", DefaultYear="", PI="", TabSequence=16, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Schedule R Part III - Figure Your Credit", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    DisInc = TextBox(FieldName="DisInc", DisplayFieldName="DisInc", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Schedule R, Line 11", DefaultVal="", DefaultYear="", PI="", TabSequence=19, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Schedule R Line 11 Chart", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    SSN = TextBox(FieldName="SSN", DisplayFieldName="SSN", FieldType="SSN", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=2, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
