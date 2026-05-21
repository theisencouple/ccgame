from pathlib import Path
from .base import Area
from ui import colors


class DeeperCave(Area):
    def __init__(self) -> None:
        super().__init__("DeepCave", "JackBlack lives here", colors.DEEPERCAVE, image=Path("assets/deepercave.png"))
