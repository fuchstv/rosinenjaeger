from dataclasses import dataclass

@dataclass
class Item:
    name: str
    description: str
    type: str  # "Waffe" oder "Gegenstand"
    effect: str

items = {
    "Rostige Gabel": Item(
        name="Rostige Gabel",
        description="Eine alte, rostige Gabel. Nicht sehr appetitlich, aber effektiv.",
        type="Waffe",
        effect="Verursacht 2-4 Schaden."
    ),
    "Schimmeliger Apfel": Item(
        name="Schimmeliger Apfel",
        description="Ein Apfel, der bessere Tage gesehen hat. Könnte nahrhaft sein, aber auch Bauchschmerzen verursachen.",
        type="Gegenstand",
        effect="Stellt 3-5 Gesundheit wieder her, 50% Chance auf Krankheit."
    ),
    "Nagelbrett": Item(
        name="Nagelbrett",
        description="Ein Brett voller rostiger Nägel. Verursacht schweren Schaden, aber Vorsicht, du könntest dich selbst verletzen!",
        type="Waffe",
        effect="Verursacht 5-8 Schaden, 20% Chance auf Selbstschaden."
    ),
    # ... (füge weitere Gegenstände hinzu)
}
