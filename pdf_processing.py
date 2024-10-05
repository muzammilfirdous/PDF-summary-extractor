import os
from concurrent.futures import ThreadPoolExecutor
from pdfminer.high_level import extract_text
from pdfminer.pdfpage import PDFPage
import re

def find_pdfs_in_directory(directory):
    """
    Finds a pdf at a time
    """
    pdf_files = []
    for file in os.listdir(directory):
        full_path = os.path.join(directory, file)
        if os.path.isfile(full_path) and file.endswith('.pdf'):
            pdf_files.append(full_path)
    return pdf_files

def find_pdfs_concurrently(directory):
    """
    Finds all the pdfs concurrently 
    """
    pdf_files = []
    directories = []

    # Collect all directories and subdirectories
    for root, dirs, files in os.walk(directory):
        directories.append(root)

    # Use ThreadPoolExecutor to search each directory concurrently
    with ThreadPoolExecutor(max_workers=5) as executor:
        # For each directory, run the find_pdfs_in_directory() function concurrently
        results = executor.map(find_pdfs_in_directory, directories)
        
        # Gather all results
        for result in results:
            pdf_files.extend(result)

    return pdf_files

def get_pdf_page_count(pdf_path):
    """
    This function returns the number of pages in the pdf
    """
    with open(pdf_path, 'rb') as f:
        page_count = len(list(PDFPage.get_pages(f)))
    return page_count

def extract_text_from_pdf(pdf_path):
    """
    This funtion extracts text and cleans the unwanted newlines and spaces
    """
    try:
        text = extract_text(pdf_path)
        # Clean up excessive spaces and line breaks
        clean_text = re.sub(r'(\n\s*\n)+', '\n\n', text)
        clean_text = re.sub(r'\s+', ' ', clean_text)
        return clean_text
    except Exception as e:
        print(f"Error extracting text: {e}")
        return None

def get_desktop_pdf_directory():
    """
    This function returns the path of desktop
    """
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'OneDrive\\Desktop')
    return desktop
