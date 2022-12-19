import PyPDF2
from gtts import gTTS
from langdetect import detect


def detect_language(text):
    try:
        language = detect(text)
        return language
    except:
        return "Could not detect language"


# Open the PDF file in read-binary mode
with open('testfile.pdf', 'rb') as file:
    # Create a PDF object
    pdf = PyPDF2.PdfFileReader(file)

    # Iterate through the pages of the PDF
    for page in range(pdf.getNumPages()):
        # Extract the text from the page
        text = pdf.getPage(page).extractText()
        langage = detect_language(text)

        if langage == "fr":
            # Create a gTTS object and save the audio to an MP3 file
            # Use French language
            audio = gTTS(text, lang="fr")
        else:
            audio = gTTS(text)
        audio.save(f'page{page + 1}.mp3')
