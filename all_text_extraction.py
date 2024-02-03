from pdf2image import convert_from_path
import pytesseract


def extract_all_text(document):

   # write page number which you want to extract text from
   page_number = 1

   # Convert the PDF to images
   pages = convert_from_path(document, first_page=page_number, last_page=page_number)

   text = []

   for page_image in pages:
    # Recognize text in the page using Tesseract OCR
      result = pytesseract.image_to_string(page_image)
      text.append(result)

   return  print('\n'.join(text))


document = 'NLP Assessment.pdf'

doc = extract_all_text(document)



