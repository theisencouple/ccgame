from pathlib import Path
from .base import Area, Interior
from ui import colors


class Blacksmith(Area, Interior):
    def __init__(self) -> None:
        super().__init__("blacksmith", "Heat and hammering fill the air.", color=colors.BLACKSMITH, image=Path("assets/blacksmith.png"))