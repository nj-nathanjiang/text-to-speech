import pyttsx3
import pdfplumber
import PyPDF2

file = "/Users/nathanj/documents/book.pdf"
pdf = open(file, "rb")
pdf_reader = PyPDF2.PdfFileReader(pdf)

num_pages = pdf_reader.numPages

with pdfplumber.open(file) as book_pdf:
    for n in range(0, num_pages):
        page = book_pdf.pages[n]
        text = page.extract_text()
        print(f"This is the book in text: {text}")
        init_speaker = pyttsx3.init()
        init_speaker.say(text)
        init_speaker.runAndWait()
