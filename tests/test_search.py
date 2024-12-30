import unittest
from src.search import PDFSearch
import fitz  # PyMuPDF

class TestPDFSearch(unittest.TestCase):
    def test_search_text(self):
        doc = fitz.open("test.pdf")
        search = PDFSearch(doc)
        results = search.search_text("test")
        self.assertIsInstance(results, list)
