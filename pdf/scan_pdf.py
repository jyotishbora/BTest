from PyPDF2 import PdfReader



def show_fields(file):
    reader = PdfReader(file)
    fields = reader.get_fields()
    for f in fields:
        print(f, fields[f])

show_fields('./inputs/f1040.pdf')
