from pathlib import Path
from .base import Area
from ui import colors
from sections.base import Exitable


class Entrance(Area, Exitable):
    def __init__(self) -> None:
        super().__init__("CaveEntrance", "Its a entrance to a cave", colors.CAVE, image=Path("assets/caveentrance.png"))
