from pathlib import Path
from .base import Area


class Field(Area):
    def __init__(self) -> None:
        super().__init__("field", "An open field.", Path("assets/plains_16x16.png"),
                         image=Path("assets/field.png"))