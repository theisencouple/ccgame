from .base import Area
from .direction import Direction
from ui import colors


class BuildingWall(Area):
    def __init__(self, rotation: int = 0) -> None:
        super().__init__("building wall", "", colors.VILLAGE_HOUSE,
                         rotation=rotation, barriers=[Direction.NORTH])


class BuildingCorner(Area):
    def __init__(self, rotation: int = 0) -> None:
        super().__init__("building wall", "", colors.VILLAGE_HOUSE,
                         rotation=rotation)
