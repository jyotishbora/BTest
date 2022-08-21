# This file is autogenerated, please do not edit directly!
from forms.Base import Form
from forms.Base import FieldSet, Property
from forms.Base import Label, TextBox, Font, CheckBox


class USF8615(Form):
    # Form attributes
    Locked = True
    FormName = "USF8615"
    FormHeight = 2800
    FormWidth = 620
    FormListLongDesc = "Tax For Certain Children Who Have Unearned Income"
    TabSequence = True
    SignatureField = "Desc"
    ProSignatureField = ""
    FormPennies = "ROUND_PENNIES"
    FreeToPrint = True

    # Form Properties
    CreateForm = Property()
    FormType = Property(FormType="Normal")
    FormListFolder = Property(FormListFolder="Forms")
    FormListNumber = Property(FormListNumber=360)
    FormListShortDesc = Property(FormListShortDesc="Form 8615")
    MaxCopies = Property(MaxCopies=1)
    NewScript = Property(NewScript="IV_USF8615_Q1")
    ReviewScript = Property(ReviewScript="IV_USF8615_Q1")
    HelpTopic = Property(HelpTopic="Form 8615 General Instructions")
    TaxTutor = Property(TaxTutor="Tax for Certain Children Who Have Unearned Income")

    # Form Components
    Check6 = CheckBox(FieldName="Check6", FieldType="CheckBox", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", Caption="Extra", PI="", TabSequence=76, DefaultVal="", QuickEntry=True, RadioTag="", TempField=True, HelpLink="", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Check4 = CheckBox(FieldName="Check4", FieldType="CheckBox", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", Caption="Extra", PI="", TabSequence=74, DefaultVal="", QuickEntry=True, RadioTag="", TempField=True, HelpLink="", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    UseMod = CheckBox(FieldName="UseMod", FieldType="CheckBox", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", Caption="Check2", PI="", TabSequence=72, DefaultVal="", QuickEntry=True, RadioTag="", TempField=True, HelpLink="", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Alert9 = TextBox(FieldName="Alert9", DisplayFieldName="Alert9", FieldType="Number", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=55, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Age = TextBox(FieldName="Age", DisplayFieldName="Age", FieldType="Number", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=3, FieldPennies="", MaxLength="25", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Form 8615 Purpose of Form", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Extra8 = TextBox(FieldName="Extra8", DisplayFieldName="Extra8", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=70, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Extra10 = TextBox(FieldName="Extra10", DisplayFieldName="Extra10", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=68, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Extra12 = TextBox(FieldName="Extra12", DisplayFieldName="Extra12", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=66, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Alert80 = TextBox(FieldName="Alert80", DisplayFieldName="Alert80", FieldType="Number", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=58, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    OthQualDiv = TextBox(FieldName="OthQualDiv", DisplayFieldName="OthQualDiv", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=25, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Form 8615 Purpose of Form", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Extra7 = TextBox(FieldName="Extra7", DisplayFieldName="Extra7", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=64, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    PLName = TextBox(FieldName="PLName", DisplayFieldName="PLName", FieldType="String", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Form 8615, Line A", DefaultVal="", DefaultYear="", PI="Parent last name", TabSequence=6, FieldPennies="", MaxLength="15", SpawnLink=True, StringSubType="NoNumbersAllowed", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Form 8615 Lines A and B - Parent's Name and Social Security Number", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    EFFilingStat = TextBox(FieldName="EFFilingStat", DisplayFieldName="EFFilingStat", FieldType="String", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=61, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Interview2 = TextBox(FieldName="Interview2", DisplayFieldName="Interview2", FieldType="String", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=48, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Exist = TextBox(FieldName="Exist", DisplayFieldName="Exist", FieldType="Number", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=45, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Interview1 = TextBox(FieldName="Interview1", DisplayFieldName="Interview1", FieldType="Number", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=49, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    ParNCG = TextBox(FieldName="ParNCG", DisplayFieldName="ParNCG", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=21, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Form 8615 Line 6 - Parent's Taxable Income", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Alert8 = TextBox(FieldName="Alert8", DisplayFieldName="Alert8", FieldType="Number", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=54, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Alert60 = TextBox(FieldName="Alert60", DisplayFieldName="Alert60", FieldType="Number", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=53, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Alert20 = TextBox(FieldName="Alert20", DisplayFieldName="Alert20", FieldType="Number", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=56, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    SchARel = TextBox(FieldName="SchARel", DisplayFieldName="SchARel", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=15, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Form 8615 Line 2 - Itemize Deductions", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    InvExp = TextBox(FieldName="InvExp", DisplayFieldName="InvExp", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=46, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    ProRata = TextBox(FieldName="ProRata", DisplayFieldName="ProRata", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Form 8615, Line 13", DefaultVal="", DefaultYear="", PI="", TabSequence=35, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Form 8615 Purpose of Form", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    ChildNewTax = TextBox(FieldName="ChildNewTax", DisplayFieldName="ChildNewTax", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Form 8615, Line 17", DefaultVal="", DefaultYear="", PI="", TabSequence=41, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Form 8615 Line 17 - Figure The Tax of Line 4 Amount", PYImport="", PYStandardImport="", Font={'Name': '"MS Sans Serif"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, Spawn="Spawn(USSchJ.SchJTax)")
    ChildTax = TextBox(FieldName="ChildTax", DisplayFieldName="ChildTax", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Form 8615, Line 15", DefaultVal="", DefaultYear="", PI="", TabSequence=38, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Form 8615 Line 15 - Figure The Tax of Line 14 Amount", PYImport="", PYStandardImport="", Font={'Name': '"MS Sans Serif"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, Spawn="Spawn(USW8615Ln15.Names)")
    Tot5and7 = TextBox(FieldName="Tot5and7", DisplayFieldName="Tot5and7", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Form 8615, Line 12a", DefaultVal="", DefaultYear="", PI="", TabSequence=33, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Form 8615 Purpose of Form", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    ParTax = TextBox(FieldName="ParTax", DisplayFieldName="ParTax", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Form 8615, Line 10", DefaultVal="", DefaultYear="", PI="", TabSequence=31, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Form 8615 Line 10 - Parent's Tax On Form 1040", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    TotInc = TextBox(FieldName="TotInc", DisplayFieldName="TotInc", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Form 8615, Line 8", DefaultVal="", DefaultYear="", PI="", TabSequence=27, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Form 8615 Line 8 - Totals of Lines 5, 6, and 7", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    ParInc = TextBox(FieldName="ParInc", DisplayFieldName="ParInc", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Form 8615, Line 6", DefaultVal="", DefaultYear="", PI="", TabSequence=23, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="0", MaxRange="999999999@", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Form 8615 Line 6 - Parent's Taxable Income", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    L15DJ = CheckBox(FieldName="L15DJ", FieldType="CheckBox", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Form 8615, Line 15", Caption="", PI="", TabSequence=37, DefaultVal="", QuickEntry=True, RadioTag="", TempField=True, HelpLink="Form 8615 Line 15 - Figure The Tax of Line 14 Amount", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    L9DJ = CheckBox(FieldName="L9DJ", FieldType="CheckBox", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Form 8615, Line 9", Caption="", PI="", TabSequence=28, DefaultVal="", QuickEntry=True, RadioTag="", TempField=True, HelpLink="Form 8615 Line 9 - Figure The Tax of Line 8 Amount", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    TaxInc = TextBox(FieldName="TaxInc", DisplayFieldName="TaxInc", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Form 8615, Line 4", DefaultVal="", DefaultYear="", PI="", TabSequence=18, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Form 8615 Line 4 - If Child Claims Foreign Income Exclusion", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Std = TextBox(FieldName="Std", DisplayFieldName="Std", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Form 8615, Line 2", DefaultVal="", DefaultYear="", PI="", TabSequence=16, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Form 8615 Line 2 - Itemize Deductions", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    HOH = CheckBox(FieldName="HOH", FieldType="CheckBox", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Form 8615, Line C", Caption="Head of household", PI="", TabSequence=11, DefaultVal="", QuickEntry=True, RadioTag="QW", TempField=True, HelpLink="Form 8615 Lines A and B - Parent's Name and Social Security Number", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    MFJ = CheckBox(FieldName="MFJ", FieldType="CheckBox", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Form 8615, Line C", Caption="Married filing jointly", PI="", TabSequence=9, DefaultVal="", QuickEntry=True, RadioTag="MFS", TempField=True, HelpLink="Form 8615 Lines A and B - Parent's Name and Social Security Number", PYImport="", PYStandardImport="", DefaultCalc=True, Protected=True, Font={'Name': '"Arial"', 'Size': 9, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True})
    Names = TextBox(FieldName="Names", DisplayFieldName="Names", FieldType="String", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=1, FieldPennies="", MaxLength="25", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Form 8615 Purpose of Form", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    PSSN = TextBox(FieldName="PSSN", DisplayFieldName="PSSN", FieldType="SSN", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Form 8615, Line B", DefaultVal="", DefaultYear="", PI="Parent first name", TabSequence=7, FieldPennies="", MaxLength="11", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Form 8615 Lines A and B - Parent's Name and Social Security Number", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    L4ML5 = TextBox(FieldName="L4ML5", DisplayFieldName="L4ML5", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="Form 8615, Line 14", DefaultVal="", DefaultYear="", PI="", TabSequence=36, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="Form 8615 Purpose of Form", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
    Threshold = TextBox(FieldName="Threshold", DisplayFieldName="Threshold", FieldType="Currency", FieldVersion="", Index="", VirtualArraySize="", FieldDesc="", DefaultVal="", DefaultYear="", PI="", TabSequence=78, FieldPennies="", MaxLength="", SpawnLink=True, StringSubType="", NoStrings=True, MinRange="", MaxRange="", TempField=True, EFileDetails=True, DefaultCalc=True, Protected=True, HelpLink="", PYImport="", PYStandardImport="", Font={'Name': '"Arial"', 'Size': 8, 'Charset': 0, 'Weight': 400, 'Underline': True, 'Italic': True, 'Strikethrough': True}, SpawnForms={})
