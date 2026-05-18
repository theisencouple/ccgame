from pathlib import Path
from area import Area
from ui.ui import UI


class Ruin(Area):
    def __init__(self) -> None:
        super().__init__("Ruin", "A ruin.", color=UI.GRAY, image="assets/ruin.png")
