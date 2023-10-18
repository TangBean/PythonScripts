from PyPDF2 import PdfReader, PdfWriter

ori = 'C:\\Users\\Tang_\\Downloads\\123.pdf'
out = 'C:\\Users\\Tang_\\Downloads\\Barry 职场英语 实战对话.pdf'

with open(ori, 'rb') as input_pdf:
    pdfReader = PdfReader(input_pdf)
    pdfWriter = PdfWriter()

    numPages = len(pdfReader.pages)
    remove = (0, 1, 12, 48, 72, 116, 118, 156, 182, 184, 192)

    for index in range(numPages):
        if index not in remove:
            pageObj = pdfReader.pages[index]
            pdfWriter.add_page(pageObj)

    with open(out, 'wb') as output_pdf:
        pdfWriter.write(output_pdf)
