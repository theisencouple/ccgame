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
        self.attack_power = 2
        self.monster_flash = 0
        self._char_dmg_flash = 0
        self._char_dmg_amount = 0
        self._mon_dmg_flash = 0
        self._mon_dmg_amount = 0

    @property
    def in_combat(self) -> bool:
        return self.area.monster is not None

    def get_actions(self) -> list[tuple[str, str]]:
        if self.in_combat:
            return [("a", "Attack")]
        actions: list[tuple[str, str]] = [("arrow keys", "Move")]
        if self.area.travel_to_enter is not None:
            actions.append(("e", "Enter"))
        if self.area.travel_to_exit is not None:
            actions.append(("e", "Exit"))
        return actions

    def draw(self, ui: UI) -> None:
        monster = self.area.monster
        if monster:
            ui.MESSAGES_PANEL.x = ui.LX
            ui.MESSAGES_PANEL.w = ui.LW
        else:
            ui.MESSAGES_PANEL.x = ui.MPX
            ui.MESSAGES_PANEL.w = ui.W - ui.MPX - ui.PAD
        ui.ACTIONS_PANEL.draw(ui)
        x, y = ui.AX + 8, ui.AY + 10
        lh = ui.font.get_linesize()
        for key, label in self.get_actions():
            ui.blit(f"[{key}]", colors.YELLOW, x, y)
            ui.blit(f" {label}", colors.TEXT, x + ui.font.size(f"[{key}]")[0], y)
            y += lh + 2
        self.area.render_panel(ui, ui.AREA_PANEL)
        self._draw_character_panel(ui)
        self._draw_monster_panel(ui)
        self._draw_area_monster(ui)

    def _hp_color(self, hp: int, max_hp: int) -> pygame.Color:
        ratio = hp / max_hp if max_hp > 0 else 0
        if ratio > 0.5:
            return colors.GREEN
        if ratio > 0.25:
            return colors.YELLOW
        return colors.RED

    def _draw_stat_row(self, ui: UI, x: int, y: int, label: str, value: str, color: "pygame.Color") -> None:
        ui.blit(label, colors.TEXT, x, y)
        ui.blit(value, color, x + 40, y)

    def _draw_hp_bar(self, ui: UI, x: int, y: int, hp: int, max_hp: int, bar_w: int, color: pygame.Color) -> None:
        bar_h = 12
        ui.fill_rect(x, y, bar_w, bar_h, colors.BORDER, border_radius=3)
        filled_w = int(bar_w * hp / max_hp) if max_hp > 0 else 0
        if filled_w > 0:
            ui.fill_rect(x, y, filled_w, bar_h, color, border_radius=3)

    def _draw_floating_damage(self, ui: UI, amount: int, counter: int, px: int, py: int, pw: int, ph: int) -> None:
        alpha = int(255 * counter / 30)
        y_off = (30 - counter) * 3
        surf = ui.big_font.render(f"-{amount}", True, colors.RED)
        surf.set_alpha(alpha)
        ui.screen.blit(surf, (px + (pw - surf.get_width()) // 2, py + ph // 2 - y_off))

    def _draw_character_panel(self, ui: UI) -> None:
        ui.CHARACTER_PANEL.draw(ui)
        cx = ui.CPX + 12
        cy = ui.CPY + 14
        hp_color = self._hp_color(self.hp, self.max_hp)
        hp_text = f"{self.hp} / {self.max_hp}"
        text_w = ui.font.size(hp_text)[0]
        bar_w = ui.CPW - 24 - text_w - 8

        self._draw_hp_bar(ui, cx, cy, self.hp, self.max_hp, bar_w, hp_color)
        ui.blit(hp_text, hp_color, cx + bar_w + 8, cy)
        cy += 12 + 6
        self._draw_stat_row(ui, cx, cy, "ATK", str(self.attack_power), colors.YELLOW)
        if self._char_dmg_flash > 0:
            self._draw_floating_damage(ui, self._char_dmg_amount, self._char_dmg_flash, ui.CPX, ui.CPY, ui.CPW, ui.CPH)
            self._char_dmg_flash -= 1

    def _draw_monster_panel(self, ui: UI) -> None:
        monster = self.area.monster
        if monster is None:
            return
        ui.MONSTER_PANEL.title = monster.name
        ui.MONSTER_PANEL.draw(ui)
        cx = ui.MPX + 12
        cy = ui.MPY + 14
        hp_color = self._hp_color(monster.hp, monster.max_hp)
        hp_text = f"{monster.hp} / {monster.max_hp}"
        text_w = ui.font.size(hp_text)[0]
        bar_w = ui.MPW - 24 - text_w - 8

        self._draw_hp_bar(ui, cx, cy, monster.hp, monster.max_hp, bar_w, hp_color)
        ui.blit(hp_text, hp_color, cx + bar_w + 8, cy)
        cy += 12 + 6
        self._draw_stat_row(ui, cx, cy, "ATK", str(monster.attack_power), colors.YELLOW)
        if self._mon_dmg_flash > 0:
            self._draw_floating_damage(ui, self._mon_dmg_amount, self._mon_dmg_flash, ui.MPX, ui.MPY, ui.MPW, ui.MPH)
            self._mon_dmg_flash -= 1

    def _draw_area_monster(self, ui: UI) -> None:
        monster = self.area.monster
        if monster is None:
            self.monster_flash = 0
            return
        panel = ui.AREA_PANEL
        if self.monster_flash > 0:
            base_x = panel.w // 3
            base_y = panel.h // 4
            base_w = panel.w // 3
            base_h = panel.h // 4 * 3
            cx = base_x + base_w // 2
            cy = base_y + base_h // 2
            scale = 1.0 + 0.5 * (self.monster_flash / 10)
            iw, ih = int(base_w * scale), int(base_h * scale)
            scaled = pygame.transform.scale(ui.load_image(monster.image, base_w, base_h), (iw, ih))
            ui.screen.set_clip(pygame.Rect(panel.x, panel.y, panel.w, panel.h))
            ui.screen.blit(scaled, (panel.x + 1 + cx - iw // 2, panel.y + 1 + cy - ih // 2))
            ui.screen.set_clip(None)
            self.monster_flash -= 1
        else:
            monster.render(ui, panel)

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

    def _handle_combat(self, key: int, ui: UI) -> None:
        if key == pygame.K_a:
            monster = self.area.monster
            assert monster is not None
            monster.take_damage(self.attack_power)
            self._mon_dmg_flash = 30
            self._mon_dmg_amount = self.attack_power
            if monster.hp <= 0:
                self.area.monster = None
                ui.say(f"You defeated the {monster.name}!")
            else:
                self.hp = max(0, self.hp - monster.attack_power)
                self.monster_flash = 10
                self._char_dmg_flash = 30
                self._char_dmg_amount = monster.attack_power
                if self.hp <= 0:
                    ui.say("You have died.")

    def handle_key(self, key: int, ui: UI) -> None:
        if self.hp <= 0:
            return
        if self.in_combat:
            self._handle_combat(key, ui)
            return
        try:
            section, dest = self._handle_movement(key)
            self.section, self.area = section, dest
            self._mon_dmg_flash = 0
            self._char_dmg_flash = 0
            self.monster_flash = 0
            self.area.enter(ui)
            if m := self.area.monster:
                ui.say(f"A {m.name} appears!")
        except (NoMovement, IndexError):
            pass
        except ValueError as e:
            ui.say(str(e))
