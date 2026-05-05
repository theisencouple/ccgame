from pathlib import Path
from area import Area
from ui.ui import UI


class StrawberryField(Area):
    def __init__(self) -> None:
        super().__init__("strawberry field", "Wild strawberries grow here.", color=UI.STRAWBERRY, image=Path("assets/strawberry_field.png"))
