import pygame
from area import Coordinates
from panel import Panel, MessagePanel


class UI:
    # ── Colors ────────────────────────────────────────────────────────────────
    BG = (14, 16, 22)
    PANEL = (24, 27, 38)
    BORDER = (55, 60, 80)
    TEXT = (195, 200, 215)
    DIM = (100, 105, 125)
    GREEN = (110, 200, 110)
    YELLOW = (220, 200, 90)
    PLAYER = (255, 225, 60)
    TILE_NONE = (10, 11, 17)

    # ── Layout ────────────────────────────────────────────────────────────────
    W = 1100
    H = 700
    PAD = 12
    TS = 16
    MAP_VIEW = 20
    MX = PAD
    MY = PAD
    MW = MAP_VIEW * TS
    MH = MAP_VIEW * TS
    AX = MX
    AY = MY + MH + PAD
    AW = MW
    AH = H - AY - PAD
    PX = MX + MW + PAD
    PY = PAD
    PW = W - PX - PAD
    PH = 350
    LX = PX
    LY = PY + PH + PAD
    LW = PW
    LH = H - LY - PAD

    MAP_PANEL      = Panel(MX, MY, MW, MH, "Map")
    ACTIONS_PANEL  = Panel(AX, AY, AW, AH, "Actions")
    AREA_PANEL     = Panel(PX, PY, PW, PH)
    MESSAGES_PANEL = MessagePanel(LX, LY, LW, LH, "Messages")

    def __init__(self):
        self._image_cache = {}
        self.screen = None
        self.font = None

    def init(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("monospace", 13)

    def say(self, text: str):
        self.MESSAGES_PANEL.say(text)

    def scroll(self, delta: int):
        self.MESSAGES_PANEL.scroll(delta)

    def draw(self, section, character):
        self.screen.fill(self.BG)
        self._draw_map(section, character)
        self._draw_actions(character)
        self._draw_area_panel(character)
        self.MESSAGES_PANEL.draw(self)
        pygame.display.flip()

    # ── Public drawing API ────────────────────────────────────────────────────
    def blit(self, text, color, x, y):
        self.screen.blit(self.font.render(text, True, color), (x, y))

    def fill_rect(self, x, y, w, h, color, **kwargs):
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

    # ── Draw helpers ──────────────────────────────────────────────────────────
    def _draw_map(self, section, character):
        self.MAP_PANEL.draw(self)
        px, py = character.coordinates.row, character.coordinates.col
        half = self.MAP_VIEW // 2

        for row in range(self.MAP_VIEW):
            for col in range(self.MAP_VIEW):
                map_r = px - half + row
                map_c = py - half + col
                sx = self.MX + col * self.TS
                sy = self.MY + row * self.TS

                try:
                    if map_r < 0 or map_c < 0:
                        raise IndexError
                    area = section.areas[map_r][map_c]
                except IndexError:
                    area = None

                if area:
                    area.render_minimap(self, Coordinates(sx, sy))
                else:
                    self.fill_rect(sx, sy, self.TS, self.TS, self.TILE_NONE)

                if map_r == px and map_c == py:
                    cx, cy = sx + self.TS // 2, sy + self.TS // 2
                    self.fill_rect(cx - 3, cy - 3, 6, 6, self.PLAYER)

    def _draw_actions(self, character):
        self.ACTIONS_PANEL.draw(self)
        x, y = self.AX + 8, self.AY + 10
        lh = self.font.get_linesize()

        for key, label in character.get_actions():
            self.blit(f"[{key}]", self.YELLOW, x, y)
            self.blit(f" {label}", self.TEXT, x + self.font.size(f"[{key}]")[0], y)
            y += lh + 2

    def load_image(self, path, w, h) -> pygame.Surface:
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

    def _draw_area_panel(self, character):
        character.get_area().render_panel(self, self.AREA_PANEL)
