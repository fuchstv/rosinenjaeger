import random
from textual.app import ComposeResult
from textual.widgets import Static, Button

from data.enemies import Enemy

class Combat(Static):
    # ... (restlicher Code bleibt gleich)

    async def attack(self) -> None:
        # Schadensberechnung
        base_damage = self.player.strength
        crit_chance = self.player.agility * 0.1  # Kritische Trefferchance basierend auf Geschicklichkeit
        crit_multiplier = 1.5  # Schadensmultiplikator bei kritischen Treffern

        if random.random() < crit_chance:
            damage = int(base_damage * crit_multiplier)
            message = f"Kritischer Treffer! Du verursachst {damage} Schaden."
        else:
            damage = base_damage
            message = f"Du verursachst {damage} Schaden."

        self.enemy.health -= damage
        await self.app.bell()  # Soundeffekt für den Treffer
        await self.add_message(message)
        await self.refresh_screen()

        if self.enemy.health <= 0:
            await self.enemy_defeated()
        else:
            await self.enemy_attacks()

    async def enemy_attacks(self) -> None:
        # Schadensberechnung für den Gegner (ähnlich wie beim Spieler)
        base_damage = self.enemy.attack
        crit_chance = 0.1  # Gegner haben eine feste kritische Trefferchance
        crit_multiplier = 1.5

        if random.random() < crit_chance:
            damage = int(base_damage * crit_multiplier)
            message = f"Kritischer Treffer! {self.enemy.name} verursacht {damage} Schaden."
        else:
            damage = base_damage
            message = f"{self.enemy.name} verursacht {damage} Schaden."

        self.player.health -= damage
        await self.app.bell()
        await self.add_message(message)
        await self.refresh_screen()

        if self.player.health <= 0:
            await self.player_defeated()
        else:
            await self.enemy_attacks()

    async def enemy_attacks(self) -> None:
        # Hier kommt die Logik für den Angriff des Gegners
        damage = self.enemy.attack
        self.player.health -= damage
        await self.refresh_screen()
        if self.player.health <= 0:
            await self.player_defeated()

    async def enemy_defeated(self) -> None:
        # Logik für den Fall, dass der Gegner besiegt wurde
        await self.app.pop_screen()  # Kampfbildschirm schließen
        # ... (Beute verteilen, Erfahrungspunkte geben, etc.)

    async def player_defeated(self) -> None:
        # Logik für den Fall, dass der Spieler besiegt wurde
        await self.app.push_screen(Static("Du wurdest besiegt!"))

    async def refresh_screen(self) -> None:
        # Aktualisiert die angezeigten Informationen auf dem Kampfbildschirm
        await self.update(self.compose())
