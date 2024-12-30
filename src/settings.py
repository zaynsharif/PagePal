class Settings:
    def __init__(self):
        self.theme = "light"
        self.zoom_level = 1.0

    def toggle_theme(self):
        self.theme = "dark" if self.theme == "light" else "light"

    def set_zoom(self, level):
        self.zoom_level = level
