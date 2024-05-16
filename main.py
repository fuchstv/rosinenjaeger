from textual.app import App
from ui.main_screen import MainScreen

class RosinenjaegerApp(App):
    def on_mount(self) -> None:
        self.push_screen(MainScreen())

if __name__ == "__main__":
    app = RosinenjaegerApp()
    app.run()
