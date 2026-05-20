from pathlib import Path

import pygame
from ui.ui import UI
from ui.panel import Panel


class Interior:
    """Mixin that blocks direct movement between two Interior areas."""


class Impassable:
    """Mixin for areas that cannot be entered (walls)."""


class Area:
    def __init__(self, name: str, description: str,
                 minimap: Path | pygame.Color,
                 image: Path | None = None,
                 minimap_rotation: int = 0) -> None:
        self.name = name
        self.description = description
        self.minimap = minimap
        self.minimap_rotation = minimap_rotation
        self.image = image
        self.visited = False

    def enter(self, ui: UI) -> None:
        if not self.visited:
            self.visited = True
            if self.description:
                ui.say(self.description)

    def render_minimap(self, ui: UI) -> pygame.Surface:
        if isinstance(self.minimap, Path):
            surf = pygame.transform.rotate(ui.load_image(self.minimap, ui.TS, ui.TS), self.minimap_rotation)
        else:
            surf = pygame.Surface((ui.TS, ui.TS))
            surf.fill(self.minimap)
        if not self.visited:
            dim = pygame.Surface((ui.TS, ui.TS))
            dim.fill(pygame.Color(160, 160, 160))
            surf.blit(dim, (0, 0), special_flags=pygame.BLEND_MULT)
        return surf

    def render_panel(self, ui: UI, panel: Panel) -> None:
        panel.title = self.name.title()
        panel.draw(ui)
        if self.image:
            panel.load_image(ui, self.image)