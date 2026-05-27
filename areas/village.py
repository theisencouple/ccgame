from pathlib import Path
from areas.base import Area


class Village(Area):
    def __init__(self) -> None:
        super().__init__("village", "A small village.", Path("assets/village_16x16.png"),
                         image=Path("assets/village.png"))
