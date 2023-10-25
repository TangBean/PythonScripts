from PyPDF2 import PdfReader, PdfWriter

ori = 'C:\\Users\\Tang_\\Downloads\\Barry 职场英语 实战对话 (raw).pdf'
out = 'C:\\Users\\Tang_\\Downloads\\Barry 职场英语 实战对话.pdf'

with open(ori, 'rb') as input_pdf:
    pdfReader = PdfReader(input_pdf)
    pdfWriter = PdfWriter()

    numPages = len(pdfReader.pages)
    remove = (0,1,2,3,13,49,73,117,119,157,183,185,193)

    for index in range(numPages):
        if index not in remove:
            pageObj = pdfReader.pages[index]
            pdfWriter.add_page(pageObj)

    with open(out, 'wb') as output_pdf:
        pdfWriter.write(output_pdf)
