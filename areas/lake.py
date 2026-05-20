from pathlib import Path
from .base import Area


class Lake(Area):
    _MINIMAP = Path("assets/lake_16x16.png")

    def __init__(self, minimap_rotation: int = 0) -> None:
        super().__init__("lake", "A calm lake.", self._MINIMAP, image=Path("assets/lake.png"), minimap_rotation=minimap_rotation)


class LakeEdge(Lake):
    _MINIMAP = Path("assets/lake_edge_16x16.png")


class LakeCorner(Lake):
    _MINIMAP = Path("assets/lake_corner_16x16.png")