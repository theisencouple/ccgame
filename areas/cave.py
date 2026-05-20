from pathlib import Path
from .base import Area
from ui import colors


class Cave(Area):
    def __init__(self) -> None:
        super().__init__("cave", "A dark cave.", colors.CAVE, image=Path("assets/cave.png"))