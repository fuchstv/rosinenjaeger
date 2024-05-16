from textual.app import ComposeResult
from textual.widgets import Static, Button, Label

class MainScreen(Static):
    def __init__(self, district, player):
        super().__init__()
        self.district = district
        self.player = player

    def compose(self) -> ComposeResult:
        yield Static(f"Bezirk: {self.district.name}")
        yield Static(self.district.description)

        # Spielerstatus
        yield Label(f"Gesundheit: {self.player.health}")
        yield Label(f"Rosinen: {len(self.player.inventory)}")
        # ... (weitere Attribute anzeigen)

        # Aktionen
        yield Button("Mülltonne durchsuchen", id="search")
        yield Button("Weitergehen", id="move")
        # ... (weitere Aktionen wie "Inventar anzeigen" oder "Status anzeigen" hinzufügen)
