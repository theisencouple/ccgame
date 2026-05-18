from pathlib import Path
from area import Area
from ui.ui import UI


class Village(Area):
    def __init__(self) -> None:
        super().__init__("village", "A small village.", color=UI.VILLAGE, image=Path("assets/village.png"))
 