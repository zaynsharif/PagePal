import flet as ft
from src.viewer import PDFViewer
from src.toolbar import Toolbar

def main(page: ft.Page):
    page.title = "PagePal - Advanced PDF Viewer"
    page.scroll = "adaptive"
    pdf_viewer = PDFViewer()
    toolbar = Toolbar(pdf_viewer)

    page.add(toolbar, pdf_viewer)
    page.update()

ft.app(target=main)
