from pathlib import Path
from .base import Area
from ui import colors


class Lake(Area):
    def __init__(self) -> None:
        super().__init__("lake", "A calm lake.", color=colors.LAKE, image=Path("assets/lake.png"))