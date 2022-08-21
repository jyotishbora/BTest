# This file is autogenerated, please do not edit directly!
from forms.Base import Form
from forms.Base import FieldSet, Property
from forms.Base import Label, TextBox, Font, CheckBox


class USZINMASTERCBF(Form):
    # Form attributes
    Locked = True
    FormName = "USZINMasterCBF"
    FormHeight = 1500
    FormWidth = 620
    FormListLongDesc = ""
    FormTabName = ""
    TabSequence = True
    SignatureField = "Desc"
    ProSignatureField = ""
    FormPennies = "ROUND_PENNIES|FORCE_PENNIES"
    FreeToPrint = True

    # Form Properties
    CreateForm = Property()
    FormType = Property(FormType="Normal")
    FormListFolder = Property(FormListFolder="Hidden")
    FormListNumber = Property(FormListNumber=1265)
    FormListShortDesc = Property(FormListShortDesc="IN Master Charge By Form")
    MaxCopies = Property(MaxCopies=1)
    NewScript = Property(NewScript="")
    ReviewScript = Property(ReviewScript="")
    HelpTopic = Property(HelpTopic="")
    TaxTutor = Property(TaxTutor="")

    # Form Components
    CBFINDEP = TextBox(FieldName="CBFINDEP", DisplayFieldName="CBFINDEP", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=33, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBFIT9 = TextBox(FieldName="CBFIT9", DisplayFieldName="CBFIT9", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=24, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBFIN2210 = TextBox(FieldName="CBFIN2210", DisplayFieldName="CBFIN2210", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=22, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBFINEIC = TextBox(FieldName="CBFINEIC", DisplayFieldName="CBFINEIC", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=31, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBFIN529 = TextBox(FieldName="CBFIN529", DisplayFieldName="CBFIN529", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=29, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBFCT40PNR = TextBox(FieldName="CBFCT40PNR", DisplayFieldName="CBFCT40PNR", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=27, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBFSchH = TextBox(FieldName="CBFSchH", DisplayFieldName="CBFSchH", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=21, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBFSchF = TextBox(FieldName="CBFSchF", DisplayFieldName="CBFSchF", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=19, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBFSchC = TextBox(FieldName="CBFSchC", DisplayFieldName="CBFSchC", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=16, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBFSchA = TextBox(FieldName="CBFSchA", DisplayFieldName="CBFSchA", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=14, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBFSch6 = TextBox(FieldName="CBFSch6", DisplayFieldName="CBFSch6", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=12, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBFSch3 = TextBox(FieldName="CBFSch3", DisplayFieldName="CBFSch3", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=9, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBFSch1 = TextBox(FieldName="CBFSch1", DisplayFieldName="CBFSch1", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=7, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBFIT40RNR = TextBox(FieldName="CBFIT40RNR", DisplayFieldName="CBFIT40RNR", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=3, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBFIT40 = TextBox(FieldName="CBFIT40", DisplayFieldName="CBFIT40", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=1, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBFFA2 = TextBox(FieldName="CBFFA2", DisplayFieldName="CBFFA2", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=40, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBFFA4 = TextBox(FieldName="CBFFA4", DisplayFieldName="CBFFA4", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=44, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBFA2 = TextBox(FieldName="CBFA2", DisplayFieldName="CBFA2", FieldType="String", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=39, FieldPennies="", MaxLength="40", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBFA4 = TextBox(FieldName="CBFA4", DisplayFieldName="CBFA4", FieldType="String", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=43, FieldPennies="", MaxLength="40", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBFA5 = TextBox(FieldName="CBFA5", DisplayFieldName="CBFA5", FieldType="String", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=45, FieldPennies="", MaxLength="40", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Extra1 = TextBox(FieldName="Extra1", DisplayFieldName="Extra1", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=48, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Extra3 = TextBox(FieldName="Extra3", DisplayFieldName="Extra3", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=50, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Extra5 = TextBox(FieldName="Extra5", DisplayFieldName="Extra5", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=52, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBFEDGER = TextBox(FieldName="CBFEDGER", DisplayFieldName="CBFEDGER", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=35, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBFSch4 = TextBox(FieldName="CBFSch4", DisplayFieldName="CBFSch4", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=10, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBFIT40PNRX = TextBox(FieldName="CBFIT40PNRX", DisplayFieldName="CBFIT40PNRX", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=5, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    CBFOthAmt = FieldSet(fields=[TextBox(FieldName="CBFOthAmt", DisplayFieldName="CBFOthAmt(0)", FieldType="Currency", FieldVersion="", Index="0", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=54, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={}),TextBox(FieldName="CBFOthAmt", DisplayFieldName="CBFOthAmt(1)", FieldType="Currency", FieldVersion="", Index="1", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=56, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={}),TextBox(FieldName="CBFOthAmt", DisplayFieldName="CBFOthAmt(2)", FieldType="Currency", FieldVersion="", Index="2", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=58, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={}),TextBox(FieldName="CBFOthAmt", DisplayFieldName="CBFOthAmt(3)", FieldType="Currency", FieldVersion="", Index="3", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=60, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={}),TextBox(FieldName="CBFOthAmt", DisplayFieldName="CBFOthAmt(4)", FieldType="Currency", FieldVersion="", Index="4", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=62, FieldPennies="ROUND_PENNIES|FORCE_PENNIES", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})], name=CBFOthAmt)
