from dataclasses import dataclass

@dataclass
class District:
    name: str
    description: str
    trash_items: list[str]
    enemies: list[str]
    special_events: list[str]

districts = {
    "Kapitalistischer Bezirk": District(
        name="Kapitalistischer Bezirk",
        description="Ein Bezirk voller Luxus und Überfluss, aber auch mit viel Abfall. Hier wimmelt es von abgelaufenen Delikatessen und Designerklamotten, aber Vorsicht vor der hohen Konkurrenz!",
        trash_items=["Abgelaufener Champagner", "Designer-Handtasche (mit Loch)", "Goldener Ring (gefälscht)", "Seltene Gewürze"],
        enemies=["Mutierte Ratte", "Wilde Katze", "Geschäftstüchtiger Hamster"],
        special_events=["Luxus-Mülltonnen-Auktion", "Geheimer Club der Rosinen-Gourmets"]
    ),
    "Sozialistischer Bezirk": District(
        name="Sozialistischer Bezirk",
        description="Ein Bezirk, in dem Teilen und Gleichheit großgeschrieben werden. Die Mülltonnen mögen weniger prunkvoll sein, aber die Gemeinschaft ist stark.",
        trash_items=["Selbstgestrickte Socken", "Propaganda-Flugblätter", "Abgelaufene Konserven", "Einzelne Rosine (mit Glück)"],
        enemies=["Streunender Hund", "Verbitterter Rentner"],
        special_events=["Solidaritäts-Rosinen-Tausch", "Gemeinschaftskompost-Party"]
    ),
    "Anarchistischer Bezirk": District(
        name="Anarchistischer Bezirk",
        description="Ein gesetzloses Gebiet voller Kreativität und Chaos. Hier findet man alles von Schrottteilen bis zu selbstgebauten Waffen.",
        trash_items=["Schrottteile", "Selbstgebaute Waffen", "Anarchistische Manifeste", "Verrückte Erfindungen"],
        enemies=["Punk mit Irokesenschnitt", "Wütende Möwe", "Müllmonster"],
        special_events=["DIY-Workshop", "Untergrund-Konzert"]
    ),
    "Öko-Bezirk": District(
        name="Öko-Bezirk",
        description="Ein Bezirk, der sich der Nachhaltigkeit verschrieben hat. Hier ist der Müll sorgfältig getrennt und kompostiert.",
        trash_items=["Kompostierbare Abfälle", "Bio-Gemüse (manchmal noch genießbar)", "Selbstgemachte Seifen", "Alte Zeitschriften über Nachhaltigkeit"],
        enemies=["Kompostwurm", "Wütender Imker"],
        special_events=["Kräutergarten-Führung", "Upcycling-Workshop"]
    ),
    "Technokratischer Bezirk": District(
        name="Technokratischer Bezirk",
        description="Ein Bezirk, der von Technologie und Effizienz geprägt ist. Die Mülltonnen sind gesichert, aber wer sie knacken kann, findet vielleicht wertvolle Elektronik.",
        trash_items=["Kaputte Elektronik", "Veraltete Software", "High-Tech-Schrott", "Funktionierendes Gadget (selten)"],
        enemies=["Sicherheitsdrohne", "Roboter-Kakerlake"],
        special_events=["Hacker-Challenge", "Zugang zu geheimem Labor"]
    )
}
