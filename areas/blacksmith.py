from pathlib import Path
from .base import Area, AreaWithOverlay


class BlacksmithDoor(AreaWithOverlay):
    def __init__(self) -> None:
        super().__init__("smithy door", "The entrance to the blacksmith's forge.",
                         Path("assets/village_street_16x16.png"),
                         Path("assets/building_door_16x16.png"),
                         image=Path("assets/blacksmith_door.png"))


class BlacksmithInterior(Area):
    def __init__(self) -> None:
        super().__init__("blacksmith", "Heat and hammering fill the air.",
                         Path("assets/building_interior_16x16.png"),
                         image=Path("assets/blacksmith.png"))