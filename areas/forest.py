from pathlib import Path
from .base import Area
from ui.ui import UI


class Forest(Area):
    def __init__(self) -> None:
        super().__init__("forest", "Dense trees surround you.", color=UI.FOREST, image=Path("assets/forest.png"))
