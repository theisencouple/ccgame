from pathlib import Path
from areas.base import Area
from sections.base import Enterable
from ui import colors


class Village(Area, Enterable):
    def __init__(self) -> None:
        super().__init__("village", "A small village.", color=colors.VILLAGE, image=Path("assets/village.png"))
