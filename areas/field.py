from pathlib import Path
from area import Area
from ui.ui import UI


class Field(Area):
    def __init__(self) -> None:
        super().__init__("field", "An open field.", color=UI.FIELD, image=Path("assets/field.png"))
