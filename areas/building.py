from pathlib import Path
from .base import AreaWithOverlay
from .direction import Direction


_STREET = Path("assets/village_street_16x16.png")
_WALL   = Path("assets/building_wall_16x16.png")
_CORNER = Path("assets/building_corner_16x16.png")


class BuildingWall(AreaWithOverlay):
    def __init__(self, rotation: int = 0) -> None:
        super().__init__("building wall", "", _STREET, _WALL,
                         image=Path("assets/building_wall.png"),
                         rotation=rotation, overlay_rotation=rotation,
                         barriers=[Direction.NORTH])


class BuildingCorner(AreaWithOverlay):
    def __init__(self, rotation: int = 0) -> None:
        super().__init__("building wall", "", _STREET, _CORNER,
                         image=Path("assets/building_corner.png"),
                         rotation=rotation, overlay_rotation=rotation)
