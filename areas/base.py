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

    def base_minimap(self, ui: UI) -> pygame.Surface:
        if isinstance(self.minimap, Path):
            return pygame.transform.rotate(ui.load_image(self.minimap, ui.TS, ui.TS), self.minimap_rotation).copy()
        surf = pygame.Surface((ui.TS, ui.TS))
        surf.fill(self.minimap)
        return surf

    def render_minimap(self, ui: UI) -> pygame.Surface:
        surf = self.base_minimap(ui)
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


class AreaWithOverlay(Area):
    def __init__(self, name: str, description: str,
                 minimap: Path | pygame.Color,
                 minimap_overlay: Path,
                 image: Path | None = None,
                 minimap_rotation: int = 0,
                 overlay_rotation: int = 0) -> None:
        super().__init__(name, description, minimap, image, minimap_rotation)
        self.minimap_overlay = minimap_overlay
        self.overlay_rotation = overlay_rotation

    def base_minimap(self, ui: UI) -> pygame.Surface:
        surf = super().base_minimap(ui)
        surf.blit(pygame.transform.rotate(ui.load_image(self.minimap_overlay, ui.TS, ui.TS), self.overlay_rotation), (0, 0))
        return surf