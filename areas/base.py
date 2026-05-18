from pathlib import Path

import pygame
from ui.ui import UI
from ui.panel import Panel


class Interior:
    """Mixin that blocks direct movement between two Interior areas."""


class Area:
    def __init__(self, name: str, description: str,
                 color: pygame.Color,
                 image: Path | None = None) -> None:
        self.name = name
        self.description = description
        self.color = color
        self.image = image
        self.visited = False

    def _dim_color(self, c: int) -> int:
        _VISITED_DIM = 35
        return max(0, c - _VISITED_DIM)

    def tile_color(self) -> pygame.Color:
        if self.visited:
            return self.color

        return pygame.Color(self._dim_color(self.color[0]),
                            self._dim_color(self.color[1]),
                            self._dim_color(self.color[2]))

    def enter(self, ui: UI) -> None:
        if not self.visited:
            self.visited = True
            if self.description:
                ui.say(self.description)

    def render_minimap(self, ui: UI, x: int, y: int) -> None:
        ui.fill_rect(x, y, ui.TS, ui.TS, self.tile_color())

    def render_panel(self, ui: UI, panel: Panel) -> None:
        panel.title = self.name.title()
        panel.draw(ui)
        if self.image:
            panel.load_image(ui, self.image)
