class PDFSearch:
    def __init__(self, doc):
        self.doc = doc

    def search_text(self, text):
        results = []
        for page_num, page in enumerate(self.doc):
            if text in page.get_text():
                results.append(page_num)
        return results
