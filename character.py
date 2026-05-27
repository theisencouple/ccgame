from __future__ import annotations

import pygame
from sections.base import Section, Enterable, Exitable
from areas.base import Area
from areas.direction import Direction
from ui import colors
from ui.ui import UI


class Character:
    def __init__(self, section: Section, area: Area) -> None:
        self.section = section
        self.area = area

    def get_actions(self) -> list[tuple[str, str]]:
        actions: list[tuple[str, str]] = [("arrow keys", "Move")]
        if isinstance(self.area, Enterable):
            actions.append(("e", "Enter"))
        if isinstance(self.area, Exitable):
            actions.append(("e", "Exit"))
        return actions

    def draw(self, ui: UI) -> None:
        ui.ACTIONS_PANEL.draw(ui)
        x, y = ui.AX + 8, ui.AY + 10
        lh = ui.font.get_linesize()
        for key, label in self.get_actions():
            ui.blit(f"[{key}]", colors.YELLOW, x, y)
            ui.blit(f" {label}", colors.TEXT, x + ui.font.size(f"[{key}]")[0], y)
            y += lh + 2
        self.area.render_panel(ui, ui.AREA_PANEL)

    def _handle_movement(self, key: int) -> tuple[Section, Area]:
        if key in Direction.key_map():
            direction = Direction.key_map()[key]
            dest = self.section.get_neighbor(self.area, direction)
            if direction in self.area.barriers or direction.opposite in dest.barriers:
                raise ValueError(f"The {dest.name} blocks your path.")
            return self.section, dest
        elif key == pygame.K_e and isinstance(self.area, (Enterable, Exitable)):
            return self.area.travel_to
        raise ValueError("no movement")

    def handle_key(self, key: int, ui: UI) -> None:
        try:
            section, dest = self._handle_movement(key)
            self.section, self.area = section, dest
            self.area.enter(ui)
        except ValueError as e:
            if str(e) != "no movement":
                ui.say(str(e))
        except IndexError:
            pass
