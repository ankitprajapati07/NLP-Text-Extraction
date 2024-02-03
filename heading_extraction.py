import fitz


def extract_headings_from_pdf(pdf_path):
    headings = []

    pdf_document = fitz.open(pdf_path)

    for page_num in range(pdf_document.page_count):

        page = pdf_document[page_num]

        #print(f"Processing page {page_num + 1}")

        # Get the text-data from the page
        text = page.get_text()

        # Extract lines that seem like headings based on criteria
        page_headings = [
            line.strip() for line in text.split('\n') if is_heading(line)
        ]

        if page_headings:
            headings += page_headings
            print(f"Headings found on page {page_num + 1}:\n{page_headings}")
        else:
            print(f"No headings found on page {page_num + 1}")

    # Close the PDF
    pdf_document.close()
    return headings


def is_heading(line):
    # Custom criteria to identify headings
    # Check if the line is in uppercase
    return line.isupper()


pdf_path = 'path to your PDF file'
extracted_headings = extract_headings_from_pdf(pdf_path)

for idx, heading in enumerate(extracted_headings):
    print(f"Heading {idx + 1}: {heading}")
