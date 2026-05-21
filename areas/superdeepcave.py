from pathlib import Path
from .base import Area
from ui import colors


class SuperDeepCave(Area):
    def __init__(self) -> None:
        super().__init__("SuperDeepCave", "It looks like a dungeon", colors.SUPERDEEPCAVE, image=Path("assets/superdeepcave.png"))
