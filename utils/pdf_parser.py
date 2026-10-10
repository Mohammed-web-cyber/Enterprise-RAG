# utils/pdf_parser.py
import fitz  # PyMuPDF


def extract_pdf_text(file_bytes: bytes) -> str:
    """
    Extract all text from a PDF given its raw bytes.
    PyMuPDF handles multi-column layouts and is 3-5x faster than PyPDF2.
    """
    doc = fitz.open(stream=file_bytes, filetype="pdf")
    pages = [page.get_text("text") for page in doc]
    doc.close()
    return "\n".join(pages).strip()
