import unittest
from pdf_processing import extract_text_from_pdf, get_pdf_page_count
from summarization import text_rank_summary, extract_keywords

class TestPDFPipeline(unittest.TestCase):

    def test_extract_text(self):
        """Test PDF text extraction."""
        text = extract_text_from_pdf('test.pdf')
        self.assertIsNotNone(text)

    def test_page_count(self):
        """Test PDF page count."""
        page_count = get_pdf_page_count('test.pdf')
        self.assertTrue(page_count > 0)

    def test_summarization(self):
        """Test summarization."""
        text = "This is a simple test paragraph. The second sentence is also here."
        summary = text_rank_summary(text)
        self.assertTrue(len(summary.split()) > 0)

    def test_keyword_extraction(self):
        """Test keyword extraction."""
        text = "This is a document containing important keywords like AI, machine learning."
        keywords = extract_keywords(text)
        self.assertTrue(len(keywords) > 0)

if __name__ == '__main__':
    unittest.main()
