import flet as ft

class Toolbar(ft.Row):
    def __init__(self, pdf_viewer):
        super().__init__()
        self.pdf_viewer = pdf_viewer
        self.controls = [
            ft.ElevatedButton("Previous", on_click=lambda _: self.pdf_viewer.prev_page()),
            ft.ElevatedButton("Next", on_click=lambda _: self.pdf_viewer.next_page()),
            ft.ElevatedButton("Open PDF", on_click=self.open_pdf)
        ]

    def open_pdf(self, e):
        # Add file picker functionality here
        pass
