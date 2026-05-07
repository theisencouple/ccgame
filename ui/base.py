import pygame
from pathlib import Path

from . import colors
from .colors import Color


class UIBase:

    def __init__(self, screen: pygame.Surface) -> None:
        self._image_cache: dict[tuple[Path, int, int], pygame.Surface] = {}
        self.screen = screen
        self.font = pygame.font.SysFont("monospace", 13)

    def clear(self) -> None:
        self.screen.fill(colors.BG)

    def flip(self) -> None:
        pygame.display.flip()

    def blit(self, text: str, color: Color, x: int, y: int) -> None:
        self.screen.blit(self.font.render(text, True, color), (x, y))

    def fill_rect(self, x: int, y: int, w: int, h: int, color: Color, **kwargs) -> None:
        pygame.draw.rect(self.screen, color, (x, y, w, h), **kwargs)

    def wrap(self, text: str, max_w: int) -> list[str]:
        words = text.split()
        lines, line = [], ""
        for w in words:
            test = (line + " " + w).strip()
            if self.font.size(test)[0] > max_w:
                if line:
                    lines.append(line)
                line = w
            else:
                line = test
        if line:
            lines.append(line)
        return lines or [""]

    def load_image(self, path: Path, w: int, h: int) -> pygame.Surface:
        key = (path, w, h)
        if key in self._image_cache:
            return self._image_cache[key]
        try:
            raw = pygame.image.load(path).convert()
            self._image_cache[key] = pygame.transform.scale(raw, (w, h))
        except Exception:
            surf = pygame.Surface((w, h))
            surf.fill(colors.PANEL)
            self._image_cache[key] = surf
        return self._image_cache[key]
