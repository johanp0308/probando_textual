from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static

class MiApp(App):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("¡Hola desde Textual!", id="mensaje")
        yield Footer()

if __name__ == "__main__":
    app = MiApp()
    app.run()