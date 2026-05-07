from __future__ import annotations

import pygame
from areas.base import Section, Area, Coordinates
from ui import colors
from ui.ui import UI


class Character:
    def __init__(self, section: Section) -> None:
        self.section = section
        self.coordinates = Coordinates(0, 0)

    def get_actions(self) -> list[tuple[str, str]]:
        return [("arrow keys", "Move")]

    def draw(self, ui: UI) -> None:
        ui.ACTIONS_PANEL.draw(ui)
        x, y = ui.AX + 8, ui.AY + 10
        lh = ui.font.get_linesize()
        for key, label in self.get_actions():
            ui.blit(f"[{key}]", colors.YELLOW, x, y)
            ui.blit(f" {label}", colors.TEXT, x + ui.font.size(f"[{key}]")[0], y)
            y += lh + 2
        self.get_area().render_panel(ui, ui.AREA_PANEL)

    def get_area(self) -> Area:
        return self.section.get_area_from_coordinates(self.coordinates)

    def handle_key(self, key: int, ui: UI) -> bool:
        try:
            if key == pygame.K_UP:
                area, self.coordinates = self.section.get_north(self.coordinates)
            elif key == pygame.K_DOWN:
                area, self.coordinates = self.section.get_south(self.coordinates)
            elif key == pygame.K_LEFT:
                area, self.coordinates = self.section.get_west(self.coordinates)
            elif key == pygame.K_RIGHT:
                area, self.coordinates = self.section.get_east(self.coordinates)
            else:
                return False
            area.enter(ui)
        except (ValueError, IndexError):
            pass
        return True