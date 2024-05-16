import random
from textual.app import App
from data.districts import districts
from data.items import items
from data.enemies import enemies
from ui.main_screen import MainScreen
from logic.combat import Combat

class RosinenjaegerApp(App):
    def __init__(self):
        super().__init__()
        self.player = Player()
        self.current_district = districts["Kapitalistischer Bezirk"]  # Startbezirk

   
 def on_mount(self) -> None:
        self.push_screen(MainScreen(self.current_district, self.player))  # Übergebe district und player
    async def handle_action(self, action: str) -> None:
        if action == "durchsuchen":
            await self.handle_search()
        elif action == "weitergehen":
            await self.handle_move()
        elif action.startswith("kampf:"):
            enemy_name = action.split(":")[1]
            await self.handle_combat(enemy_name)

    async def handle_search(self) -> None:
        # Logik zum Durchsuchen von Mülltonnen
        found_item = random.choice(self.current_district.trash_items)
        self.player.inventory.append(found_item)
        # ... (Aktualisiere die UI)

    async def handle_move(self) -> None:
        # Logik zum Wechseln des Bezirks
        # ... (Wähle einen neuen Bezirk aus und aktualisiere die UI)

    async def handle_combat(self, enemy_name: str) -> None:
        enemy = enemies[enemy_name]
        combat = Combat(self.player, enemy)
        await self.push_screen(combat)
        # ... (Nach dem Kampf: Beute verteilen, UI aktualisieren, etc.)
 async def handle_move(self) -> None:
        # Liste der verfügbaren Bezirke erstellen
        available_districts = list(districts.keys())
        available_districts.remove(self.current_district.name)

        # Auswahldialog für den neuen Bezirk anzeigen
        dialog = RadioButtons(
            [(district, district) for district in available_districts],
            title="Wähle einen Bezirk:",
        )
        await self.push_screen(dialog)

        # Auf die Auswahl des Spielers warten
        selected_district = await dialog.result

        # Bezirk wechseln und UI aktualisieren
        self.current_district = districts[selected_district]
        await self.app.pop_screen()  # Dialog schließen
        await self.app.push_screen(MainScreen(self.current_district, self.player))
class Player:
    def __init__(self):
        self.health = 50
        self.strength = 5
        self.agility = 4
        # ... (weitere Attribute)
        self.inventory = []

if __name__ == "__main__":
    app = RosinenjaegerApp()
    app.run()
