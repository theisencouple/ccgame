from pathlib import Path
from .base import Area
from ui.ui import UI


class Cave(Area):
    def __init__(self) -> None:
        super().__init__("cave", "A dark cave.", color=UI.CAVE, image=Path("assets/cave.png"))
