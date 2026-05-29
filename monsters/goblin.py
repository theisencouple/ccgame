from pathlib import Path
from monsters.monster import Monster


class Goblin(Monster):
    def __init__(self) -> None:
        super().__init__("Goblin", max_hp=10, image=Path("assets/goblin.png"))