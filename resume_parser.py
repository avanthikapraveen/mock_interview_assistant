import pdfplumber
import os

def extract_text_from_pdf(file_path):
    text = ""

    if not os.path.isfile(file_path):
        return "Error: The specified file does not exist."
    
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text
    except Exception as e:
        return f"Error extracting text from PDF: {e}"
    
if __name__ == "__main__":
    resume_path = 'avanthika.pdf'
    extracted_text = extract_text_from_pdf(resume_path)
    print(extracted_text)

