from pathlib import Path
from .base import Area
from ui import colors


class VillageHouseDoor(Area):
    def __init__(self) -> None:
        super().__init__("house door", "The entrance to a modest home.", colors.VILLAGE_HOUSE_DOOR)


class VillageHouseInterior(Area):
    def __init__(self) -> None:
        super().__init__("house interior", "Inside a warm, thatched-roof home.", colors.VILLAGE_HOUSE_FLOOR, image=Path("assets/village_house.png"))