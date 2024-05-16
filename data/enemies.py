from dataclasses import dataclass

@dataclass
class Enemy:
    name: str
    description: str
    health: int
    attack: int

enemies = {
    "Mutierte Ratte": Enemy(
        name="Mutierte Ratte",
        description="Eine riesige, aggressive Ratte mit glühenden Augen.",
        health=10,
        attack=2
    ),
    "Wilde Katze": Enemy(
        name="Wilde Katze",
        description="Eine flinke und hinterhältige Katze mit scharfen Krallen.",
        health=15,
        attack=3
    ),
    "Geschäftstüchtiger Hamster": Enemy(
        name="Geschäftstüchtiger Hamster",
        description="Ein Hamster im Anzug, der versucht, dir deine Rosinen abzuluchsen.",
        health=8,
        attack=1
    ),
    # ... (füge weitere Gegner hinzu)
}
