from pathlib import Path
from .base import Area, Interior, Impassable
from ui import colors


class BlacksmithWall(Area, Impassable):
    def __init__(self) -> None:
        super().__init__("smithy wall", "", color=colors.BLACKSMITH)


class BlacksmithDoor(Area):
    def __init__(self) -> None:
        super().__init__("smithy door", "The entrance to the blacksmith's forge.", color=colors.BLACKSMITH_DOOR)


class BlacksmithInterior(Area, Interior):
    def __init__(self) -> None:
        super().__init__("blacksmith", "Heat and hammering fill the air.", color=colors.BLACKSMITH_FLOOR, image=Path("assets/blacksmith.png"))