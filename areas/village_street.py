from pathlib import Path
from .base import Area
from ui import colors


class VillageStreet(Area):
    def __init__(self) -> None:
        super().__init__("village street", "A dusty village street.", colors.VILLAGE_STREET, image=Path("assets/village_street.png"))