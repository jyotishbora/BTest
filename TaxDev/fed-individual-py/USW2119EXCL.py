# This file is autogenerated, please do not edit directly!
from forms.Base import Form
from forms.Base import FieldSet, Property
from forms.Base import Label, TextBox, Font, CheckBox


class USW2119EXCL(Form):
    # Form attributes
    Locked = True
    FormName = "USW2119Excl"
    FormHeight = 1168
    FormWidth = 620
    FormListLongDesc = "Exclusion of gain"
    TabSequence = True
    SignatureField = "Desc"
    ProSignatureField = ""
    FormPennies = "ROUND_PENNIES"
    FreeToPrint = True

    # Form Properties
    CreateForm = Property(Create="Create(USF2119.SellingPrice)")
    FormType = Property(FormType="Normal")
    FormListFolder = Property(FormListFolder="Worksheets")
    FormListNumber = Property(FormListNumber=270)
    FormListShortDesc = Property(FormListShortDesc="Schedule D Home Sale Exclusion")
    MaxCopies = Property(MaxCopies=1)
    NewScript = Property(NewScript="")
    ReviewScript = Property(ReviewScript="")
    HelpTopic = Property(HelpTopic="Schedule D")
    TaxTutor = Property(TaxTutor="Reduced Exclusion Amount")

    # Form Components
    YAnother = CheckBox(FieldName="YAnother", FieldType="CheckBox", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", Caption="Yes.", PI="", TabSequence=10, DefaultVal="", QuickEntry=True, RadioTag="NAnother", TempField=True, HelpLink="", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 700, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    AskSpouse = TextBox(FieldName="AskSpouse", DisplayFieldName="AskSpouse", FieldType="Number", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=23, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Extra6 = TextBox(FieldName="Extra6", DisplayFieldName="Extra6", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=29, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Extra8 = TextBox(FieldName="Extra8", DisplayFieldName="Extra8", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=31, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    ReducedExclY = CheckBox(FieldName="ReducedExclY", FieldType="CheckBox", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", Caption="Yes", PI="", TabSequence=3, DefaultVal="", QuickEntry=True, RadioTag="ReducedExclN", TempField=True, HelpLink="", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Extra3 = TextBox(FieldName="Extra3", DisplayFieldName="Extra3", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=26, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Extra1 = TextBox(FieldName="Extra1", DisplayFieldName="Extra1", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=24, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Desc = TextBox(FieldName="Desc", DisplayFieldName="Desc", FieldType="String", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=22, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    SMoreDays = TextBox(FieldName="SMoreDays", DisplayFieldName=" SMoreDays", FieldType="Number", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=12, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    TDays = TextBox(FieldName="TDays", DisplayFieldName=" TDays", FieldType="Number", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=7, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    SRata = TextBox(FieldName="SRata", DisplayFieldName=" SRata", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=18, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    TDec = TextBox(FieldName="TDec", DisplayFieldName=" TDec", FieldType="Float", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=15, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    TMoreDays = TextBox(FieldName="TMoreDays", DisplayFieldName=" TMoreDays", FieldType="Number", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=11, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    SDec = TextBox(FieldName="SDec", DisplayFieldName=" SDec", FieldType="Float", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=16, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    SMax = TextBox(FieldName="SMax", DisplayFieldName=" SMax", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=6, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Names = TextBox(FieldName="Names", DisplayFieldName=" Names", FieldType="String", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=1, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
