import cv2
import numpy as np
import pytesseract
import fitz  # PyMuPDF


def extract_tables_from_pdf(pdf_path):
    tables = []

    # Open the PDF
    pdf_document = fitz.open(pdf_path)

    for page_num in range(pdf_document.page_count):
        #print(f"Processing page {page_num + 1}")

        page = pdf_document[page_num]

        #print(f"Processing page {page_num + 1}")
        # Get the image data from the page
        image_list = page.get_images(full=True)

        for img_index, img_info in enumerate(image_list):
            print(f"Processing image {img_index + 1}")
            # Get the image data
            base_image = pdf_document.extract_image(img_info)
            image_bytes = base_image["image"]

            # Convert the image data to numpy array
            img_array = bytearray(image_bytes)

            # If the image is in color, convert to grayscale
            np_img = cv2.imdecode(
                np.frombuffer(img_array, dtype=np.uint8),
                cv2.IMREAD_GRAYSCALE if len(img_array) == page.width * page.height else cv2.IMREAD_COLOR
            )
            #print(f"Processing image {img_index + 1}")

            # Print page text
            #print(page.get_text())

            # Print image shape
            #print(np_img.shape)

            # Apply thresholding(according to your image) to get a binary image
            binary_img = cv2.adaptiveThreshold(np_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

            # Use pytesseract to perform OCR on the binary image
            custom_config = r'--oem 3 --psm 6'
            text = pytesseract.image_to_string(binary_img, config=custom_config)

            # Extract tables based on identifying characters like '|' or '+'
            extracted_tables = [table.strip() for table in text.split('\n') if '|' in table or '+' in table]

            if extracted_tables:
                tables += extracted_tables
                print(f"Tables found in image {img_index + 1}:\n{extracted_tables}")
            else:
                print(f"No tables found in image {img_index + 1}")

    # Close the PDF
    pdf_document.close()
    return tables


pdf_path = 'path to your PDF file'
tables = extract_tables_from_pdf(pdf_path)

for idx, table in enumerate(tables):
    print(f"Table {idx + 1}:\n{table}\n")