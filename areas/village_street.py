from pathlib import Path
from .base import Area


class VillageStreet(Area):
    def __init__(self) -> None:
        super().__init__("village street", "A dusty village street.", Path("assets/village_street_16x16.png"), image=Path("assets/village_street.png"))
