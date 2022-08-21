# This file is autogenerated, please do not edit directly!
from forms.Base import Form
from forms.Base import FieldSet, Property
from forms.Base import Label, TextBox, Font, CheckBox


class USF8822(Form):
    # Form attributes
    Locked = True
    FormName = "USF8822"
    FormHeight = 1375
    FormWidth = 620
    FormListLongDesc = "Change of Address"
    TabSequence = True
    SignatureField = "Description"
    ProSignatureField = "Description"
    FormPennies = "ROUND_PENNIES"
    FreeToPrint = True

    # Form Properties
    CreateForm = Property()
    FormType = Property(FormType="OnlineFillableForm")
    FormListFolder = Property(FormListFolder="Forms")
    FormListNumber = Property(FormListNumber=380)
    FormListShortDesc = Property(FormListShortDesc="Form 8822")
    MaxCopies = Property(MaxCopies=2)
    NewScript = Property(NewScript="")
    ReviewScript = Property(ReviewScript="")
    HelpTopic = Property(HelpTopic="Form 8822")
    TaxTutor = Property(TaxTutor="")

    # Form Components
    ForeignProvinceNew = TextBox(FieldName="ForeignProvinceNew", DisplayFieldName="ForeignProvinceNew", FieldType="String", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Form 8822, Line 7", DefaultVal="", DefaultYear="", PI="", TabSequence=22, FieldPennies="", MaxLength="24", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Form 8822", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    ForeignProvinceSPOld = TextBox(FieldName="ForeignProvinceSPOld", DisplayFieldName="ForeignProvinceSPOld", FieldType="String", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Form 8822, Line 6b", DefaultVal="", DefaultYear="", PI="", TabSequence=18, FieldPennies="", MaxLength="24", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Form 8822", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    ForeignProvinceTPOld = TextBox(FieldName="ForeignProvinceTPOld", DisplayFieldName="ForeignProvinceTPOld", FieldType="String", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Form 8822, Line 6a", DefaultVal="", DefaultYear="", PI="", TabSequence=14, FieldPennies="", MaxLength="24", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Form 8822", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Extra5 = TextBox(FieldName="Extra5", DisplayFieldName="Extra5", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=32, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Extra3 = TextBox(FieldName="Extra3", DisplayFieldName="Extra3", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=30, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Extra1 = TextBox(FieldName="Extra1", DisplayFieldName="Extra1", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=28, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Dayphone = TextBox(FieldName="Dayphone", DisplayFieldName="Dayphone", FieldType="Phone", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Form 8822, Part III", DefaultVal="", DefaultYear="", PI="", TabSequence=24, FieldPennies="", MaxLength="20", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Form 8822", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    SPOldAddress = TextBox(FieldName="SPOldAddress", DisplayFieldName="SPOldAddress", FieldType="String", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Form 8822, Line 6b", DefaultVal="", DefaultYear="", PI="", TabSequence=16, FieldPennies="", MaxLength="70", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Form 8822", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    PriorName = TextBox(FieldName="PriorName", DisplayFieldName="PriorName", FieldType="String", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Form 8822, Line 5a", DefaultVal="", DefaultYear="", PI="Taxpayer prior name", TabSequence=10, FieldPennies="", MaxLength="70", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Form 8822", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    SPName = TextBox(FieldName="SPName", DisplayFieldName="SPName", FieldType="String", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Form 8822, Line 4a", DefaultVal="", DefaultYear="", PI="Spouse name", TabSequence=8, FieldPennies="", MaxLength="50", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Form 8822", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    TPName = TextBox(FieldName="TPName", DisplayFieldName="TPName", FieldType="String", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Form 8822, Line 3a", DefaultVal="", DefaultYear="", PI="Taxpayer name", TabSequence=6, FieldPennies="", MaxLength="50", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Form 8822", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    DecedentName = TextBox(FieldName="DecedentName", DisplayFieldName="DecedentName", FieldType="String", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Form 8822, Line 2", DefaultVal="", DefaultYear="", PI="Decedent name", TabSequence=4, FieldPennies="", MaxLength="24", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Form 8822", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    IndTax = CheckBox(FieldName="IndTax", FieldType="CheckBox", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Form 8822, Line 1", Caption="", PI="", TabSequence=1, DefaultVal="", QuickEntry=True, RadioTag="", TempField=True, HelpLink="Form 8822", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 700, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Exit = TextBox(FieldName="Exit", DisplayFieldName="", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=25, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
