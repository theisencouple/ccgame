from pathlib import Path
from .base import Area
from ui import colors


class Village(Area):
    def __init__(self) -> None:
        super().__init__("village", "A small village.", color=colors.VILLAGE, image=Path("assets/village.png"))