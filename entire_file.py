import pyttsx3, PyPDF2

pdf_file_name = 'testFile'
pdfreader = PyPDF2.PdfFileReader(open(pdf_file_name+'.pdf', 'rb'))
speaker = pyttsx3.init()

for page_num in range(pdfreader.numPages):
    text = pdfreader.getPage(page_num).extractText()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)

speaker.save_to_file(clean_text, f'{pdf_file_name}.mp3')
speaker.runAndWait()

speaker.stop()