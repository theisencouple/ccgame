from pathlib import Path
from area import Area
from ui.ui import UI


class Lake(Area):
    def __init__(self) -> None:
        super().__init__("lake", "A calm lake.", color=UI.LAKE, image=Path("assets/lake.png"))
