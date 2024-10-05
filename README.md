# PDF Summarization and Keyword Extraction Pipeline

# Overview
This project is task sent by Wasserstoff as a task for the selection AI engineer intern. It processes the pdfs stored in the desktop, desktop folders or subfloders and extracts keywords and summarizes the pdfs.

### Features
- **PDF Text Extraction**: Uses `pdfminer.six` to extract text from PDFs.
- **Summarization**: Summarizes the pdf content using textrank algorith.
- **Keyword Extraction**: Extracts domain-specific keywords using TF-IDF from `scikit-learn`.
- **MongoDB Integration**: Stores the extracted summaries and keywords in MongoDB Atlas.
- **Concurrency**: Uses `ThreadPoolExecutor` for concurrent file searching and processing.
- **Dockerization**: The project can be run inside a Docker container for ease of deployment.

## Project Structure
# rishi-pawar-wasserstoff-AiInternTask
