import unittest
from src.viewer import PDFViewer

class TestPDFViewer(unittest.TestCase):
    def test_load_pdf(self):
        viewer = PDFViewer()
        viewer.load_pdf("test.pdf")
        self.assertIsNotNone(viewer.doc)

    def test_page_navigation(self):
        viewer = PDFViewer()
        viewer.load_pdf("test.pdf")
        viewer.next_page()
        self.assertEqual(viewer.current_page, 1)
        viewer.prev_page()
        self.assertEqual(viewer.current_page, 0)
