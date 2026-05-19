from pathlib import Path
from .base import Area, Interior, Impassable
from ui import colors


class VillageHouseWall(Area, Impassable):
    def __init__(self) -> None:
        super().__init__("house wall", "", color=colors.VILLAGE_HOUSE)


class VillageHouseDoor(Area):
    def __init__(self) -> None:
        super().__init__("house door", "The entrance to a modest home.", color=colors.VILLAGE_HOUSE_DOOR)


class VillageHouseInterior(Area, Interior):
    def __init__(self) -> None:
        super().__init__("house interior", "Inside a warm, thatched-roof home.", color=colors.VILLAGE_HOUSE_FLOOR, image=Path("assets/village_house.png"))