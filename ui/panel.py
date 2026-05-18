import pygame
from pathlib import Path
from .base import UIBase
from . import colors


class Panel:
    def __init__(self, x: int, y: int, w: int, h: int) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self, ui: UIBase) -> None:
        pygame.draw.rect(ui.screen, colors.PANEL, (self.x, self.y, self.w, self.h), border_radius=6)
        pygame.draw.rect(ui.screen, colors.BORDER, (self.x, self.y, self.w, self.h), width=1, border_radius=6)

    def load_image(self, ui: UIBase, path: Path) -> None:
        w, h = self.w - 2, self.h - 2
        img = ui.load_image(path, w, h).copy().convert_alpha()
        mask = pygame.Surface((w, h), pygame.SRCALPHA)
        pygame.draw.rect(mask, (255, 255, 255, 255), (0, 0, w, h), border_radius=5)
        img.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        ui.screen.blit(img, (self.x + 1, self.y + 1))

    def overlay_image(self, ui: UIBase, path: Path, x: int, y: int, w: int, h: int) -> None:
        img = ui.load_image(path, w, h)
        ui.screen.blit(img, (self.x + 1 + x, self.y + 1 + y))


class PanelWithTitle(Panel):
    def __init__(self, x: int, y: int, w: int, h: int, title: str) -> None:
        super().__init__(x, y, w, h)
        self.title = title

    def draw_title(self, ui: UIBase) -> None:
        lbl = ui.font.render(f" {self.title} ", True, colors.YELLOW, colors.PANEL)
        ui.screen.blit(lbl, (self.x + 10, self.y - 9))

    def draw(self, ui: UIBase) -> None:
        super().draw(ui)
        self.draw_title(ui)


class MessagePanel(PanelWithTitle):
    def __init__(self, x: int, y: int, w: int, h: int, title: str) -> None:
        super().__init__(x, y, w, h, title)
        self.messages: list[str] = []
        self._scroll: int = 0

    def say(self, text: str) -> None:
        lines = [line.strip() for line in text.strip().split('\n') if line.strip()]
        self.messages.extend(lines)

    def scroll(self, delta: int) -> None:
        self._scroll = max(0, self._scroll + delta)

    def draw(self, ui: UIBase) -> None:
        super().draw(ui)
        inner_x, inner_y = self.x + 8, self.y + 10
        lh = ui.font.get_linesize()
        max_lines = (self.h - 16) // lh

        all_lines = []
        for msg in self.messages:
            all_lines.extend(ui.wrap(msg, self.w - 16))

        max_scroll = max(0, len(all_lines) - max_lines)
        self._scroll = min(self._scroll, max_scroll)

        end = len(all_lines) - self._scroll
        start = max(0, end - max_lines)
        for i, line in enumerate(all_lines[start:end]):
            ui.blit(line, colors.GREEN, inner_x, inner_y + i * lh)

        if self._scroll > 0:
            ui.blit(
                f"▲ {self._scroll} lines above (PgUp/PgDn)",
                colors.DIM, inner_x, self.y + self.h - lh - 4,
            )
