# This file is autogenerated, please do not edit directly!
from forms.Base import Form
from forms.Base import FieldSet, Property
from forms.Base import Label, TextBox, Font, CheckBox


class USW6251EXEMPTION(Form):
    # Form attributes
    Locked = True
    FormName = "USW6251Exemption"
    FormHeight = 1500
    FormWidth = 620
    FormListLongDesc = "Exemption"
    FormTabName = ""
    TabSequence = True
    SignatureField = "Desc"
    ProSignatureField = ""
    FormPennies = "ROUND_PENNIES"
    FreeToPrint = True

    # Form Properties
    CreateForm = Property(Create="Create(USF6251.AMTTaxInc)")
    FormType = Property(FormType="Normal")
    FormListFolder = Property(FormListFolder="Worksheets")
    FormListNumber = Property(FormListNumber=647)
    FormListShortDesc = Property(FormListShortDesc="Form 6251 Line 5")
    MaxCopies = Property(MaxCopies=1)
    NewScript = Property(NewScript="")
    ReviewScript = Property(ReviewScript="")
    HelpTopic = Property(HelpTopic="Form 6251")
    TaxTutor = Property(TaxTutor="Alternative Minimum Tax (AMT)")

    # Form Components
    Overhalf = CheckBox(FieldName="Overhalf", FieldType="CheckBox", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", Caption="", PI="", TabSequence=10, DefaultVal="", QuickEntry=True, RadioTag="", TempField=True, HelpLink="Form 6251 Certain Children Under Age 24", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Exemption = TextBox(FieldName="Exemption", DisplayFieldName="Exemption", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=20, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    NoWrksht = CheckBox(FieldName="NoWrksht", FieldType="CheckBox", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", Caption="NoWrksht", PI="", TabSequence=18, DefaultVal="", QuickEntry=True, RadioTag="", TempField=True, HelpLink="", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    ChildLimEx = TextBox(FieldName="ChildLimEx", DisplayFieldName="ChildLimEx", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=15, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Form 6251 Certain Children Under Age 24", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Desc = TextBox(FieldName="Desc", DisplayFieldName="Desc", FieldType="String", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=17, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    ChildEx = TextBox(FieldName="ChildEx", DisplayFieldName="ChildEx", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=12, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Form 6251 Certain Children Under Age 24", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    ExcessInc = TextBox(FieldName="ExcessInc", DisplayFieldName="ExcessInc", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=6, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    AMTI = TextBox(FieldName="AMTI", DisplayFieldName="AMTI", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=4, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    ChildEI = TextBox(FieldName="ChildEI", DisplayFieldName="ChildEI", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=13, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Form 6251 Certain Children Under Age 24", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Names = TextBox(FieldName="Names", DisplayFieldName="Names", FieldType="String", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=1, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Text15 = TextBox(FieldName="Text15", DisplayFieldName="Extra3", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=21, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Text13 = TextBox(FieldName="Text13", DisplayFieldName="Extra1", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=23, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Text11 = TextBox(FieldName="Text11", DisplayFieldName="Extra2", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=25, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Edit1 = TextBox(FieldName="Edit1", DisplayFieldName="Edit1", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=27, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Edit3 = TextBox(FieldName="Edit3", DisplayFieldName="Edit3", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=29, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Edit5 = TextBox(FieldName="Edit5", DisplayFieldName="Edit5", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=31, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Age24 = TextBox(FieldName="Age24", DisplayFieldName="Age24", FieldType="Date", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=33, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    LimEx = TextBox(FieldName="LimEx", DisplayFieldName="LimEx", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=8, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Link = Link(FieldName="Link", FieldType="Link", Caption="Click here to open Form 6251", Ellipses="", AutoSize=True, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 700, 'Underline': True, 'Italic': True, 'Strikethrough': True}, Spawn="Spawn(USF6251.Names)", Link={'LinkType': '""', 'LinkValue': '""'})
