from pathlib import Path
import pygame
from .base import Area
from ui import colors
from ui.ui import UI


class Lake(Area):
    _MINIMAP = Path("assets/lake_16x16.png")

    def __init__(self, rotation: int = 0) -> None:
        super().__init__("lake", "A calm lake.", color=colors.LAKE, image=Path("assets/lake.png"))
        self._rotation = rotation

    def render_minimap(self, ui: UI):
        surf = pygame.transform.rotate(ui.load_image(self._MINIMAP, ui.TS, ui.TS), self._rotation)
        if not self.visited:
            dim = pygame.Surface((ui.TS, ui.TS))
            dim.fill((160, 160, 160))
            surf.blit(dim, (0, 0), special_flags=pygame.BLEND_MULT)
        return surf


class LakeEdge(Lake):
    _MINIMAP = Path("assets/lake_edge_16x16.png")


class LakeCorner(Lake):
    _MINIMAP = Path("assets/lake_corner_16x16.png")