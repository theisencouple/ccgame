from pathlib import Path
from .base import Area
from ui import colors
from sections.base import Enterable


class Cave(Area, Enterable):
    def __init__(self) -> None:
        super().__init__("cave", "A dark cave.", colors.CAVE, image=Path("assets/cave.png"))
