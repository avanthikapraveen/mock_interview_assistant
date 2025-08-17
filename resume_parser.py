import pdfplumber
import os
import docx

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
    
def extract_text_from_docx(file_path):
    text = ""

    if not os.path.isfile(file_path):
        return "Error: The specified file does not exist."
    
    try:
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
        return text
    except Exception as e:
        return f"Error extracting text from DOCX: {e}"
    
def extract_resume_text(file_path):
    if file_path.lower().endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.lower().endswith(".docx"):
        return extract_text_from_docx(file_path)
    else:
        return "Error: Unsupported file format."

if __name__ == "__main__":
    resume_path = 'avanthika_resume.pdf'
    extracted_text = extract_resume_text(resume_path)
    print(extracted_text)

