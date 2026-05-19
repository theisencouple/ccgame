from pathlib import Path
import pygame
from areas.base import Area
from sections.base import Enterable
from ui import colors
from ui.ui import UI


class Village(Area, Enterable):
    def __init__(self) -> None:
        super().__init__("village", "A small village.", color=colors.VILLAGE, image=Path("assets/village.png"))

    def render_minimap(self, ui: UI):
        surf = ui.load_image(Path("assets/village_16x16.png"), ui.TS, ui.TS).copy()
        if not self.visited:
            dim = pygame.Surface((ui.TS, ui.TS))
            dim.fill((80, 80, 80))
            surf.blit(dim, (0, 0), special_flags=pygame.BLEND_MULT)
        return surf
