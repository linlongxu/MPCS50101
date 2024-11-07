from PyPDF2 import PdfFileReader

def extract_text(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PdfFileReader(file)
        text = ""
        for page_num in range(reader.numPages):
            text += reader.getPage(page_num).extract_text() + "\n"
        return text