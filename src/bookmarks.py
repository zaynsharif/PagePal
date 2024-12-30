class Bookmarks:
    def __init__(self):
        self.bookmarks = []

    def add_bookmark(self, page_number):
        if page_number not in self.bookmarks:
            self.bookmarks.append(page_number)

    def remove_bookmark(self, page_number):
        if page_number in self.bookmarks:
            self.bookmarks.remove(page_number)

    def get_bookmarks(self):
        return self.bookmarks
