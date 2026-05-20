from pathlib import Path
from .base import Area
from ui import colors


class BlacksmithDoor(Area):
    def __init__(self) -> None:
        super().__init__("smithy door", "The entrance to the blacksmith's forge.", colors.BLACKSMITH_DOOR)


class BlacksmithInterior(Area):
    def __init__(self) -> None:
        super().__init__("blacksmith", "Heat and hammering fill the air.", colors.BLACKSMITH_FLOOR, image=Path("assets/blacksmith.png"))