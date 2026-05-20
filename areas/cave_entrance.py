from pathlib import Path
from .base import Area
from ui import colors


class Entrance(Area):
    def __init__(self) -> None:
        super().__init__("CaveEntrance", "Its a entrance to a cave", color=colors.CAVE, image=Path("assets/caveentrance.png"))
