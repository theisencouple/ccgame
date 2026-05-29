from __future__ import annotations

import pygame
from sections.base import Section
from areas.base import Area
from areas.direction import Direction
from ui import colors
from ui.ui import UI


class NoMovement(Exception):
    pass


class Character:
    def __init__(self, section: Section, area: Area) -> None:
        self.section = section
        self.area = area
        self.max_hp = 20
        self.hp = self.max_hp

    def get_actions(self) -> list[tuple[str, str]]:
        actions: list[tuple[str, str]] = [("arrow keys", "Move")]
        if self.area.travel_to_enter is not None:
            actions.append(("e", "Enter"))
        if self.area.travel_to_exit is not None:
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
        self._draw_character_panel(ui)

    def _draw_character_panel(self, ui: UI) -> None:
        ui.CHARACTER_PANEL.draw(ui)
        cx = ui.CPX + 12
        cy = ui.CPY + 14
        lh = ui.font.get_linesize()

        ui.blit("HP", colors.TEXT, cx, cy)
        ui.blit(f"{self.hp} / {self.max_hp}", colors.RED, cx + 40, cy)

        bar_x = cx
        bar_y = cy + lh + 6
        bar_w = ui.CPW - 24
        bar_h = 16
        ui.fill_rect(bar_x, bar_y, bar_w, bar_h, colors.BORDER, border_radius=4)
        filled_w = int(bar_w * self.hp / self.max_hp) if self.max_hp > 0 else 0
        if filled_w > 0:
            ui.fill_rect(bar_x, bar_y, filled_w, bar_h, colors.RED, border_radius=4)

    def _handle_movement(self, key: int) -> tuple[Section, Area]:
        if key in Direction.key_map():
            direction = Direction.key_map()[key]
            dest = self.section.get_neighbor(self.area, direction)
            if direction in self.area.barriers:
                raise ValueError(f"The {self.area.name} blocks your path.")
            if direction.opposite in dest.barriers:
                raise ValueError(f"The {dest.name} blocks your path.")
            return self.section, dest
        elif key == pygame.K_e:
            dest = self.area.travel_to_enter or self.area.travel_to_exit
            if dest is not None:
                return dest
        raise NoMovement

    def handle_key(self, key: int, ui: UI) -> None:
        try:
            section, dest = self._handle_movement(key)
            self.section, self.area = section, dest
            self.area.enter(ui)
        except (NoMovement, IndexError):
            pass
        except ValueError as e:
            ui.say(str(e))
