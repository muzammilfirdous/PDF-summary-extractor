from pdf_processing import find_pdfs_concurrently, get_desktop_pdf_directory, extract_text_from_pdf, get_pdf_page_count
from summarization import text_rank_summary, extract_keywords
from mongodb import store_pdf_metadata, update_pdf_summary
from performance_metrics import PerformanceMetrics  # Import the new module
from concurrent.futures import ThreadPoolExecutor

def summarize_and_extract_keywords(text, page_count, metrics):
    """
    Summarizes and extracts keywords based on the number of pages in the document.
    Logs execution time for summarization and keyword extraction.
    """
    # Measure time for summarization
    metrics.start_timer('summarization')
    if page_count < 3:  # Short documents (1-2 pages)
        summary = text_rank_summary(text, num_sentences=3)
    elif 3 <= page_count < 10:  # Medium documents (3-10 pages)
        summary = text_rank_summary(text, num_sentences=5)
    else:  # Long documents (10+ pages)
        summary = text_rank_summary(text, num_sentences=10)
    metrics.stop_timer('summarization')

    # Measure time for keyword extraction
    metrics.start_timer('keyword extraction')
    keywords = extract_keywords(text)
    metrics.stop_timer('keyword extraction')
    
    return summary, keywords

def process_single_pdf(pdf_file, metrics):
    """
    Processes a single PDF file: extracts text, summarizes it, and stores metadata in MongoDB.
    Logs execution time for each step.
    """
    print(f"Processing: {pdf_file}")

    # Measure time for page counting
    metrics.start_timer('page counting')
    page_count = get_pdf_page_count(pdf_file)
    metrics.stop_timer('page counting')
    
    # Measure time for text extraction
    metrics.start_timer('text extraction')
    text = extract_text_from_pdf(pdf_file)
    metrics.stop_timer('text extraction')
    
    if text:
        summary, keywords = summarize_and_extract_keywords(text, page_count, metrics)
        filename = pdf_file.split('/')[-1]

        # Measure time for MongoDB operations
        metrics.start_timer('mongodb operations')
        store_pdf_metadata(filename, pdf_file, len(text))
        update_pdf_summary(filename, summary, keywords)
        metrics.stop_timer('mongodb operations')

def process_pdf_pipeline_concurrently():
    """
    Main pipeline to process PDFs on the desktop concurrently using ThreadPoolExecutor.
    Logs total execution time for the entire process.
    """
    metrics = PerformanceMetrics()  # Initialize the performance metrics

    # Measure total time for the pipeline
    pdf_directory = get_desktop_pdf_directory()
    pdf_files = find_pdfs_concurrently(pdf_directory)  # Concurrent PDF search

    # Use ThreadPoolExecutor for concurrent PDF processing
    with ThreadPoolExecutor(max_workers=5) as executor:  # You can adjust the number of workers
        for pdf_file in pdf_files:
            executor.submit(process_single_pdf, pdf_file, metrics)

    # Print the final processing time report
    metrics.print_report()

if __name__ == "__main__":
    process_pdf_pipeline_concurrently()
