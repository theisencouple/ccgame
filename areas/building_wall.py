from .base import Area, Impassable
from ui import colors


class BuildingWall(Area, Impassable):
    def __init__(self) -> None:
        super().__init__("building wall", "", colors.VILLAGE_HOUSE)