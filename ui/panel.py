import pygame
from pathlib import Path
from .base import UIBase
from . import colors


class Panel:
    def __init__(self, x: int, y: int, w: int, h: int, title: str = "") -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.title = title

    def draw(self, ui: UIBase) -> None:
        pygame.draw.rect(ui.screen, colors.PANEL, (self.x, self.y, self.w, self.h), border_radius=6)
        pygame.draw.rect(ui.screen, colors.BORDER, (self.x, self.y, self.w, self.h), width=1, border_radius=6)
        if self.title:
            lbl = ui.font.render(f" {self.title} ", True, colors.YELLOW, colors.PANEL)
            ui.screen.blit(lbl, (self.x + 10, self.y - 9))

    def load_image(self, ui: UIBase, path: Path) -> None:
        img = ui.load_image(path, self.w - 4, self.h - 16)
        ui.screen.blit(img, (self.x + 2, self.y + 14))


class MessagePanel(Panel):
    def __init__(self, x: int, y: int, w: int, h: int, title: str = "") -> None:
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
