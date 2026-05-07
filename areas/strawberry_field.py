from pathlib import Path
from .base import Area
from ui import colors


class StrawberryField(Area):
    def __init__(self) -> None:
        super().__init__("strawberry field", "Wild strawberries grow here.", color=colors.STRAWBERRY, image=Path("assets/strawberry_field.png"))