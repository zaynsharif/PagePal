import fitz  # PyMuPDF
import flet as ft

class PDFViewer(ft.Column):
    def __init__(self):
        super().__init__()
        self.doc = None
        self.current_page = 0

    def load_pdf(self, file_path):
        self.doc = fitz.open(file_path)
        self.show_page(self.current_page)

    def show_page(self, page_number):
        if self.doc:
            page = self.doc[page_number]
            pix = page.get_pixmap()
            img_data = pix.tobytes("png")
            self.controls = [ft.Image(src_base64=img_data)]
            self.update()

    def next_page(self):
        if self.current_page < len(self.doc) - 1:
            self.current_page += 1
            self.show_page(self.current_page)

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.show_page(self.current_page)
