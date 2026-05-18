from pathlib import Path
from .base import Area, Interior
from ui import colors


class VillageHouse(Area, Interior):
    def __init__(self) -> None:
        super().__init__("village house", "A modest home with a thatched roof.", color=colors.VILLAGE_HOUSE, image=Path("assets/village_house.png"))