from pathlib import Path
from .base import Area
from ui import colors


class Field(Area):
    def __init__(self) -> None:
        super().__init__("field", "An open field.", color=colors.FIELD, image=Path("assets/field.png"))