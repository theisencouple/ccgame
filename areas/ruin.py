from pathlib import Path
from .base import Area
from ui import colors


class Ruin(Area):
    def __init__(self) -> None:
        super().__init__("Ruin", "A ruin.", colors.GRAY, image=Path("assets/ruin.png"))
