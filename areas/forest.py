from pathlib import Path
from .base import Area
from ui import colors


class Forest(Area):
    def __init__(self) -> None:
        super().__init__("forest", "Dense trees surround you.", color=colors.FOREST, image=Path("assets/forest.png"))