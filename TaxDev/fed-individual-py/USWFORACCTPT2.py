# This file is autogenerated, please do not edit directly!
from forms.Base import Form
from forms.Base import FieldSet, Property
from forms.Base import Label, TextBox, Font, CheckBox


class USWFORACCTPT2(Form):
    # Form attributes
    Locked = True
    FormName = "USWForAcctPt2"
    FormHeight = 2800
    FormWidth = 620
    FormListLongDesc = "Part II Information on Financial Account Owned Separately"
    FormTabName = ""
    TabSequence = True
    SignatureField = "Desc"
    ProSignatureField = ""
    FormPennies = "ROUND_PENNIES"
    FreeToPrint = True

    # Form Properties
    CreateForm = Property()
    FormType = Property(FormType="OnlineFillableForm")
    FormListFolder = Property(FormListFolder="Hidden")
    FormListNumber = Property(FormListNumber=121)
    FormListShortDesc = Property(FormListShortDesc="FBAR")
    MaxCopies = Property(MaxCopies=4)
    NewScript = Property(NewScript="")
    ReviewScript = Property(ReviewScript="")
    HelpTopic = Property(HelpTopic="")
    TaxTutor = Property(TaxTutor="")

    # Form Components
    Alert240 = TextBox(FieldName="Alert240", DisplayFieldName="Alert240", FieldType="Number", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=138, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Alert220 = TextBox(FieldName="Alert220", DisplayFieldName="Alert220", FieldType="Number", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=136, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Alert200 = TextBox(FieldName="Alert200", DisplayFieldName="Alert200", FieldType="Number", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=134, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Alert180 = TextBox(FieldName="Alert180", DisplayFieldName="Alert180", FieldType="Number", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=132, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Alert160 = TextBox(FieldName="Alert160", DisplayFieldName="Alert160", FieldType="Number", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=130, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Alert140 = TextBox(FieldName="Alert140", DisplayFieldName="Alert140", FieldType="Number", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=128, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Alert120 = TextBox(FieldName="Alert120", DisplayFieldName="Alert120", FieldType="Number", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=126, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Alert100 = TextBox(FieldName="Alert100", DisplayFieldName="Alert100", FieldType="Number", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=124, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Alert80 = TextBox(FieldName="Alert80", DisplayFieldName="Alert80", FieldType="Number", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=122, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Alert60 = TextBox(FieldName="Alert60", DisplayFieldName="Alert60", FieldType="Number", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=120, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    TotPg = TextBox(FieldName="TotPg", DisplayFieldName="TotPg", FieldType="Number", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=118, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Alert10 = TextBox(FieldName="Alert10", DisplayFieldName="Alert10", FieldType="Number", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=117, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Alert30 = TextBox(FieldName="Alert30", DisplayFieldName="Alert30", FieldType="Number", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=115, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    LastName = TextBox(FieldName="LastName", DisplayFieldName="LastName", FieldType="String", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 6", DefaultVal="", DefaultYear="", PI="", TabSequence=5, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    FinCity = TextBox(FieldName="FinCity", DisplayFieldName="FinCity", FieldType="String", FieldVersion="", Index="0", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 20", DefaultVal="", DefaultYear="", PI="", TabSequence=16, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Text19 = TextBox(FieldName="Text19", DisplayFieldName="EXTRA", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=111, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    TPID = CheckBox(FieldName="TPID", FieldType="CheckBox", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 3", Caption="Taxpayer Identification Number", PI="", TabSequence=2, DefaultVal="", QuickEntry=True, RadioTag="ForID", TempField=True, HelpLink="", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    ForID = CheckBox(FieldName="ForID", FieldType="CheckBox", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 3", Caption="Foreign Identification Number", PI="", TabSequence=3, DefaultVal="", QuickEntry=True, RadioTag="TPID", TempField=True, HelpLink="", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Check5 = CheckBox(FieldName="Check5", FieldType="CheckBox", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", Caption="EXTRA", PI="", TabSequence=108, DefaultVal="", QuickEntry=True, RadioTag="", TempField=True, HelpLink="", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Check3 = CheckBox(FieldName="Check3", FieldType="CheckBox", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", Caption="EXTRA", PI="", TabSequence=106, DefaultVal="", QuickEntry=True, RadioTag="", TempField=True, HelpLink="", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Check1 = CheckBox(FieldName="Check1", FieldType="CheckBox", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", Caption="EXTRA", PI="", TabSequence=104, DefaultVal="", QuickEntry=True, RadioTag="", TempField=True, HelpLink="", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Text9 = TextBox(FieldName="Text9", DisplayFieldName="EXTRA", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=102, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Text7 = TextBox(FieldName="Text7", DisplayFieldName="EXTRA", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=100, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Text5 = TextBox(FieldName="Text5", DisplayFieldName="EXTRA", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=98, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Text3 = TextBox(FieldName="Text3", DisplayFieldName="EXTRA", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=96, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Text1 = TextBox(FieldName="Text1", DisplayFieldName="EXTRA", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=94, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Print = TextBox(FieldName="Print", DisplayFieldName="Print", FieldType="Number", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=92, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Desc = TextBox(FieldName="Desc", DisplayFieldName="Desc", FieldType="String", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=91, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    FinancialName = FieldSet(fields=[TextBox(FieldName="FinancialName", DisplayFieldName="FinancialName", FieldType="String", FieldVersion="", Index="0", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 17", DefaultVal="", DefaultYear="", PI="", TabSequence=13, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="FinCEN Form 114 Item 17", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={}),TextBox(FieldName="FinancialName", DisplayFieldName="FinancialName", FieldType="String", FieldVersion="", Index="1", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 17", DefaultVal="", DefaultYear="", PI="", TabSequence=27, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={}),TextBox(FieldName="FinancialName", DisplayFieldName="FinancialName", FieldType="String", FieldVersion="", Index="2", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 17", DefaultVal="", DefaultYear="", PI="", TabSequence=41, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={}),TextBox(FieldName="FinancialName", DisplayFieldName="FinancialName", FieldType="String", FieldVersion="", Index="3", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 17", DefaultVal="", DefaultYear="", PI="", TabSequence=55, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={}),TextBox(FieldName="FinancialName", DisplayFieldName="FinancialName", FieldType="String", FieldVersion="", Index="4", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 17", DefaultVal="", DefaultYear="", PI="", TabSequence=69, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={}),TextBox(FieldName="FinancialName", DisplayFieldName="FinancialName", FieldType="String", FieldVersion="", Index="5", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 17", DefaultVal="", DefaultYear="", PI="", TabSequence=83, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})], name=FinancialName)
    AcctNum = FieldSet(fields=[TextBox(FieldName="AcctNum", DisplayFieldName="AcctNum", FieldType="String", FieldVersion="", Index="0", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 18", DefaultVal="", DefaultYear="", PI="", TabSequence=14, FieldPennies="", MaxLength="25", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={}),TextBox(FieldName="AcctNum", DisplayFieldName="AcctNum", FieldType="String", FieldVersion="", Index="1", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 18", DefaultVal="", DefaultYear="", PI="", TabSequence=28, FieldPennies="", MaxLength="25", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={}),TextBox(FieldName="AcctNum", DisplayFieldName="AcctNum", FieldType="String", FieldVersion="", Index="2", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 18", DefaultVal="", DefaultYear="", PI="", TabSequence=42, FieldPennies="", MaxLength="25", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={}),TextBox(FieldName="AcctNum", DisplayFieldName="AcctNum", FieldType="String", FieldVersion="", Index="3", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 18", DefaultVal="", DefaultYear="", PI="", TabSequence=56, FieldPennies="", MaxLength="25", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={}),TextBox(FieldName="AcctNum", DisplayFieldName="AcctNum", FieldType="String", FieldVersion="", Index="4", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 18", DefaultVal="", DefaultYear="", PI="", TabSequence=70, FieldPennies="", MaxLength="25", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={}),TextBox(FieldName="AcctNum", DisplayFieldName="AcctNum", FieldType="String", FieldVersion="", Index="5", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 18", DefaultVal="", DefaultYear="", PI="", TabSequence=84, FieldPennies="", MaxLength="25", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})], name=AcctNum)
    OthAcctType = FieldSet(fields=[TextBox(FieldName="OthAcctType", DisplayFieldName="OthAcctType", FieldType="String", FieldVersion="", Index="0", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 16c", DefaultVal="", DefaultYear="", PI="", TabSequence=12, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={}),TextBox(FieldName="OthAcctType", DisplayFieldName="OthAcctType", FieldType="String", FieldVersion="", Index="1", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 16c", DefaultVal="", DefaultYear="", PI="", TabSequence=26, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={}),TextBox(FieldName="OthAcctType", DisplayFieldName="OthAcctType", FieldType="String", FieldVersion="", Index="2", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 16c", DefaultVal="", DefaultYear="", PI="", TabSequence=40, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={}),TextBox(FieldName="OthAcctType", DisplayFieldName="OthAcctType", FieldType="String", FieldVersion="", Index="3", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 16c", DefaultVal="", DefaultYear="", PI="", TabSequence=54, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={}),TextBox(FieldName="OthAcctType", DisplayFieldName="OthAcctType", FieldType="String", FieldVersion="", Index="4", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 16c", DefaultVal="", DefaultYear="", PI="", TabSequence=68, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={}),TextBox(FieldName="OthAcctType", DisplayFieldName="OthAcctType", FieldType="String", FieldVersion="", Index="5", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 16c", DefaultVal="", DefaultYear="", PI="", TabSequence=82, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})], name=OthAcctType)
    Securities = FieldSet(fields=[CheckBox(FieldName="Securities", FieldType="CheckBox", FieldVersion="", Index="0", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 16b", Caption="", PI="", TabSequence=9, DefaultVal="", QuickEntry=True, RadioTag="Bank", TempField=True, HelpLink="", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}),CheckBox(FieldName="Securities", FieldType="CheckBox", FieldVersion="", Index="1", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 16b", Caption="", PI="", TabSequence=23, DefaultVal="", QuickEntry=True, RadioTag="Bank", TempField=True, HelpLink="", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}),CheckBox(FieldName="Securities", FieldType="CheckBox", FieldVersion="", Index="2", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 16b", Caption="", PI="", TabSequence=37, DefaultVal="", QuickEntry=True, RadioTag="Bank", TempField=True, HelpLink="", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}),CheckBox(FieldName="Securities", FieldType="CheckBox", FieldVersion="", Index="3", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 16b", Caption="", PI="", TabSequence=51, DefaultVal="", QuickEntry=True, RadioTag="Bank", TempField=True, HelpLink="", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}),CheckBox(FieldName="Securities", FieldType="CheckBox", FieldVersion="", Index="4", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 16b", Caption="", PI="", TabSequence=65, DefaultVal="", QuickEntry=True, RadioTag="Bank", TempField=True, HelpLink="", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}),CheckBox(FieldName="Securities", FieldType="CheckBox", FieldVersion="", Index="5", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 16b", Caption="", PI="", TabSequence=79, DefaultVal="", QuickEntry=True, RadioTag="Bank", TempField=True, HelpLink="", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})], name=Securities)
    FinZip = FieldSet(fields=[TextBox(FieldName="FinZip", DisplayFieldName="FinZip", FieldType="String", FieldVersion="", Index="1", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 22", DefaultVal="", DefaultYear="", PI="", TabSequence=32, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={}),TextBox(FieldName="FinZip", DisplayFieldName="FinZip", FieldType="String", FieldVersion="", Index="2", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 22", DefaultVal="", DefaultYear="", PI="", TabSequence=46, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={}),TextBox(FieldName="FinZip", DisplayFieldName="FinZip", FieldType="String", FieldVersion="", Index="3", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 22", DefaultVal="", DefaultYear="", PI="", TabSequence=60, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={}),TextBox(FieldName="FinZip", DisplayFieldName="FinZip", FieldType="String", FieldVersion="", Index="4", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 22", DefaultVal="", DefaultYear="", PI="", TabSequence=74, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={}),TextBox(FieldName="FinZip", DisplayFieldName="FinZip", FieldType="String", FieldVersion="", Index="5", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 22", DefaultVal="", DefaultYear="", PI="", TabSequence=88, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})], name=FinZip)
    AmtUnknow = FieldSet(fields=[CheckBox(FieldName="AmtUnknow", FieldType="CheckBox", FieldVersion="", Index="0", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 15a", Caption="", PI="", TabSequence=7, DefaultVal="", QuickEntry=True, RadioTag="", TempField=True, HelpLink="", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}),CheckBox(FieldName="AmtUnknow", FieldType="CheckBox", FieldVersion="", Index="1", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 15a", Caption="", PI="", TabSequence=21, DefaultVal="", QuickEntry=True, RadioTag="", TempField=True, HelpLink="", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}),CheckBox(FieldName="AmtUnknow", FieldType="CheckBox", FieldVersion="", Index="2", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 15a", Caption="", PI="", TabSequence=35, DefaultVal="", QuickEntry=True, RadioTag="", TempField=True, HelpLink="", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}),CheckBox(FieldName="AmtUnknow", FieldType="CheckBox", FieldVersion="", Index="3", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 15a", Caption="", PI="", TabSequence=49, DefaultVal="", QuickEntry=True, RadioTag="", TempField=True, HelpLink="", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}),CheckBox(FieldName="AmtUnknow", FieldType="CheckBox", FieldVersion="", Index="4", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 15a", Caption="", PI="", TabSequence=63, DefaultVal="", QuickEntry=True, RadioTag="", TempField=True, HelpLink="", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}),CheckBox(FieldName="AmtUnknow", FieldType="CheckBox", FieldVersion="", Index="5", VirtualArraySize="", FieldDesc="FinCEN 114 Part 2 Line 15a", Caption="", PI="", TabSequence=77, DefaultVal="", QuickEntry=True, RadioTag="", TempField=True, HelpLink="", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})], name=AmtUnknow)
