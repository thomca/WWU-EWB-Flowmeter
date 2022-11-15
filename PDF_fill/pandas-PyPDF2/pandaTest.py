# example at https://hridai.medium.com/filling-out-pdf-fields-automatically-with-excel-data-is-easy-17a11902d48b

import pandas as pd
from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2.generic import BooleanObject, NameObject, IndirectObject

if __name__ == '__main__':
    csv_filename = "EISAutoFill.csv"
    pdf_filename = "EIS 3 Certificate - Autofilled.pdf"

    csvin = os.path.normpath(os.path.join(os.getcwd(),'in',csv_filename))
    pdfin = os.path.normpath(os.path.join(os.getcwd(),'in',pdf_filename))
    pdfout = os.path.normpath(os.path.join(os.getcwd(),'out'))
    data = pd.read_csv(csvin)
    pdf = PdfFileReader(open(pdfin, "rb"), strict=False)
    # List of all pdf field names - use this in the dictionary below to populate pdf
    pdf_fields = [str(x) for x in pdf.getFields().keys()]
    csv_fields = data.columns.tolist()

    for j, rows in data.iterrows():
        pdf2 = PdfFileWriter()
        # Below you must define the field names as keys in this dictionary
        # Field names found by running and printing line 15
        # Key = pdf_field_name : Value = csv_field_value
        field_dictionary_1 = {"Full Name": str(rows['FullName']),
                            "Address Line 1": rows['AddressLine1'],
                            "Address Line 2": rows['AddressLine2'],
                            "Address Line 3": rows['AddressLine3'],
                            "Post Code": rows['PostCode'],
                            "Description of Shares": rows['DescriptionOfShares'],
                            }

        temp_out_dir = os.path.normpath(os.path.join(pdfout,str(i) + 'out.pdf'))
        pdf2.addPage(pdf.getPage(0)) # Makes a copy of pdf template page
        pdf2.updatePageFormFieldValues(pdf2.getPage(0), field_dictionary_1) # Updates fields
        pdf2.addPage(pdf.getPage(1)) # Adds page 2 of template Pdf
        outputStream = open(temp_out_dir, "wb")
        pdf2.write(outputStream) # Saves copy of enhanced template
        outputStream.close()