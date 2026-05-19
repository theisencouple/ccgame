from pathlib import Path
import pygame
from .base import Area
from ui import colors
from ui.ui import UI


class Field(Area):
    def __init__(self) -> None:
        super().__init__("field", "An open field.", color=colors.FIELD, image=Path("assets/field.png"))

    def render_minimap(self, ui: UI):
        surf = ui.load_image(Path("assets/plains_16x16.png"), ui.TS, ui.TS).copy()
        if not self.visited:
            dim = pygame.Surface((ui.TS, ui.TS))
            dim.fill((80, 80, 80))
            surf.blit(dim, (0, 0), special_flags=pygame.BLEND_MULT)
        return surf