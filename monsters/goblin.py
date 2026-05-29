from pathlib import Path
from monsters.base import Monster


class Goblin(Monster):
    def __init__(self) -> None:
        super().__init__("Goblin", max_hp=10, attack_power=3, image=Path("assets/goblin.png"))
