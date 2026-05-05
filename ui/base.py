import pygame

Color = tuple[int, int, int]


class UIBase:
    # ── Colors ────────────────────────────────────────────────────────────────
    BG: Color = (14, 16, 22)
    PANEL: Color = (24, 27, 38)
    BORDER: Color = (55, 60, 80)
    TEXT: Color = (195, 200, 215)
    DIM: Color = (100, 105, 125)
    GREEN: Color = (110, 200, 110)
    YELLOW: Color = (220, 200, 90)
    PLAYER: Color = (255, 225, 60)
    TILE_NONE: Color = (10, 11, 17)
    FIELD: Color = (45, 105, 42)
    FOREST: Color = (28, 78, 38)
    CAVE: Color = (75, 65, 55)
    LAKE: Color = (35, 72, 148)
    VILLAGE: Color = (135, 100, 55)
    STRAWBERRY: Color = (148, 52, 72)

    def __init__(self) -> None:
        self._image_cache: dict[tuple[str, int, int], pygame.Surface] = {}
        self.screen: pygame.Surface | None = None
        self.font: pygame.font.Font | None = None

    def init(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.font = pygame.font.SysFont("monospace", 13)

    def clear(self) -> None:
        self.screen.fill(self.BG)

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

    def load_image(self, path: str, w: int, h: int) -> pygame.Surface:
        key = (path, w, h)
        if key in self._image_cache:
            return self._image_cache[key]
        try:
            raw = pygame.image.load(path).convert()
            self._image_cache[key] = pygame.transform.scale(raw, (w, h))
        except Exception:
            surf = pygame.Surface((w, h))
            surf.fill(self.PANEL)
            self._image_cache[key] = surf
        return self._image_cache[key]
