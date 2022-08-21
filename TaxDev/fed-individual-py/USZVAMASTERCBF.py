# This file is autogenerated, please do not edit directly!
from forms.Base import Form
from forms.Base import FieldSet, Property
from forms.Base import Label, TextBox, Font, CheckBox


class USZVAMASTERCBF(Form):
    # Form attributes
    Locked = True
    FormName = "USZVAMasterCBF"
    FormType = "Normal"
    FormHeight = 1301
    FormWidth = 620
    FormListFolder = "Hidden"
    FormListNumber = 1400
    FormListLongDesc = ""
    TabSequence = True
    SignatureField = "Desc"
    FormPennies = "ROUND_PENNIES|FORCE_PENNIES"
    TaxTutor = ""

    # Form Properties
    CreateForm = Property()
    FormListShortDesc = Property(FormListShortDesc="VA Master Charge By Form")
    MaxCopies = Property(MaxCopies=1)
    NewScript = Property(NewScript="")
    ReviewScript = Property(ReviewScript="")
    HelpTopic = Property(HelpTopic="")

    # Form Components
    CBF760PYINC = TextBox(FieldName="CBF760PYINC", DisplayFieldName="CBF760PYINC", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=12, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, PYImport="", PYStandardImport="", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBF760C = TextBox(FieldName="CBF760C", DisplayFieldName="CBF760C", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=10, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, PYImport="", PYStandardImport="", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBF760PYADJ = TextBox(FieldName="CBF760PYADJ", DisplayFieldName="CBF760PYADJ", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=13, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, PYImport="", PYStandardImport="", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBF760PY = TextBox(FieldName="CBF760PY", DisplayFieldName="CBF760PY", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=2, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, PYImport="", PYStandardImport="", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBF760X = TextBox(FieldName="CBF760X", DisplayFieldName="CBF760X", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=4, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, PYImport="", PYStandardImport="", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBF760ES = TextBox(FieldName="CBF760ES", DisplayFieldName="CBF760ES", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=7, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, PYImport="", PYStandardImport="", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBF763S = TextBox(FieldName="CBF763S", DisplayFieldName="CBF763S", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=9, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, PYImport="", PYStandardImport="", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBF760ADJ = TextBox(FieldName="CBF760ADJ", DisplayFieldName="CBF760ADJ", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=11, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, PYImport="", PYStandardImport="", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBF760 = TextBox(FieldName="CBF760", DisplayFieldName="CBF760", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=1, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, PYImport="", PYStandardImport="", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBFFA2 = TextBox(FieldName="CBFFA2", DisplayFieldName="CBFFA2", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=22, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, PYImport="", PYStandardImport="", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBFFA4 = TextBox(FieldName="CBFFA4", DisplayFieldName="CBFFA4", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=26, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, PYImport="", PYStandardImport="", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBFA2 = TextBox(FieldName="CBFA2", DisplayFieldName="CBFA2", FieldType="String", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=21, FieldPennies="", MaxLength="40", SpawnLink=True, PYImport="", PYStandardImport="", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBFA4 = TextBox(FieldName="CBFA4", DisplayFieldName="CBFA4", FieldType="String", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=25, FieldPennies="", MaxLength="40", SpawnLink=True, PYImport="", PYStandardImport="", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBFA5 = TextBox(FieldName="CBFA5", DisplayFieldName="CBFA5", FieldType="String", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=27, FieldPennies="", MaxLength="40", SpawnLink=True, PYImport="", PYStandardImport="", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Extra1 = TextBox(FieldName="Extra1", DisplayFieldName="Extra1", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=30, FieldPennies="", MaxLength="", SpawnLink=True, PYImport="", PYStandardImport="", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Extra3 = TextBox(FieldName="Extra3", DisplayFieldName="Extra3", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=32, FieldPennies="", MaxLength="", SpawnLink=True, PYImport="", PYStandardImport="", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Extra5 = TextBox(FieldName="Extra5", DisplayFieldName="Extra5", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=34, FieldPennies="", MaxLength="", SpawnLink=True, PYImport="", PYStandardImport="", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBFOthAmt = FieldSet(fields=[TextBox(FieldName="CBFOthAmt", DisplayFieldName="CBFOthAmt(0)", FieldType="Currency", FieldVersion="", Index="0", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=36, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, PYImport="", PYStandardImport="", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={}),TextBox(FieldName="CBFOthAmt", DisplayFieldName="CBFOthAmt(1)", FieldType="Currency", FieldVersion="", Index="1", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=38, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, PYImport="", PYStandardImport="", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={}),TextBox(FieldName="CBFOthAmt", DisplayFieldName="CBFOthAmt(2)", FieldType="Currency", FieldVersion="", Index="2", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=40, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, PYImport="", PYStandardImport="", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={}),TextBox(FieldName="CBFOthAmt", DisplayFieldName="CBFOthAmt(3)", FieldType="Currency", FieldVersion="", Index="3", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=42, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, PYImport="", PYStandardImport="", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={}),TextBox(FieldName="CBFOthAmt", DisplayFieldName="CBFOthAmt(4)", FieldType="Currency", FieldVersion="", Index="4", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", TabSequence=44, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, PYImport="", PYStandardImport="", StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})], name=CBFOthAmt)
