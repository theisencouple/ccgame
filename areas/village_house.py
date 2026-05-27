from pathlib import Path
from .base import Area, AreaWithOverlay

_STREET = Path("assets/village_street_16x16.png")
_DOOR   = Path("assets/building_door_16x16.png")


class VillageHouseDoor(AreaWithOverlay):
    def __init__(self) -> None:
        super().__init__("house door", "The entrance to a modest home.", _STREET, _DOOR, image=Path("assets/village_house_door.png"))


class VillageHouseInterior(Area):
    def __init__(self) -> None:
        super().__init__("house interior", "Inside a warm, thatched-roof home.", Path("assets/building_interior_16x16.png"), image=Path("assets/village_house.png"))