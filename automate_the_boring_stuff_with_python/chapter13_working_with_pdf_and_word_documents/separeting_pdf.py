# It needs Python 3 and the lib PyPDF2
# Take off each page of the PDF in a directory and turn it into many PDFs with each page of the original.

import PyPDF2, os

pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith(".pdf"):
        print("+ PDF", filename, "encontrado.")
        pdfFiles.append(filename)

#pdfWriter = PyPDF2.PdfFileWriter()

for filename in pdfFiles:
    print("- Processando", filename, "...")
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    for pageNum in range(pdfReader.numPages):
        pdfWriter = PyPDF2.PdfFileWriter() # added
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

        pathName = os.getcwd() + '/PDFs/' + filename[:filename.rfind('.')] + '/'
        os.makedirs(os.path.dirname(pathName), exist_ok=True)
        pdfName = pathName + 'page_' + str(pageNum) + '__' + filename

        pdfOutput = open(pdfName, 'wb')
        pdfWriter.write(pdfOutput)
        pdfOutput.close()