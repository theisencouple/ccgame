from ui import colors
from ui.ui import UI

from areas.base import Area


class Section:
    def __init__(self, areas: list[list[Area]]) -> None:
        self.areas = areas

    def draw_map(self, ui: UI, area: Area) -> None:
        px, py = self._find(area)
        ui.MAP_PANEL.draw(ui)
        half = ui.MAP_VIEW // 2

        ui.fill_rect(ui.MX, ui.MY, ui.MAP_VIEW * ui.TS, ui.MAP_VIEW * ui.TS, colors.TILE_NONE)

        for r, row in enumerate(self.areas):
            for c, tile in enumerate(row):
                dr, dc = r - px, c - py
                if abs(dr) > half or abs(dc) > half:
                    continue
                sx = ui.MX + (dc + half) * ui.TS
                sy = ui.MY + (dr + half) * ui.TS
                ui.screen.blit(tile.render_minimap(ui), (sx, sy))
                if r == px and c == py:
                    cx, cy = sx + ui.TS // 2, sy + ui.TS // 2
                    ui.fill_rect(cx - 3, cy - 3, 6, 6, colors.PLAYER)

        ui.MAP_PANEL.draw_title(ui)

    def _get_area_at(self, area: Area, row_offset: int, col_offset: int) -> Area:
        r, c = self._find(area)
        nr, nc = r + row_offset, c + col_offset
        if nr < 0 or nc < 0:
            raise IndexError
        return self.areas[nr][nc]

    def get_north(self, area: Area) -> Area:
        return self._get_area_at(area, -1, 0)

    def get_south(self, area: Area) -> Area:
        return self._get_area_at(area, 1, 0)

    def get_west(self, area: Area) -> Area:
        return self._get_area_at(area, 0, -1)

    def get_east(self, area: Area) -> Area:
        return self._get_area_at(area, 0, 1)

    def _find(self, area: Area) -> tuple[int, int]:
        for r, row in enumerate(self.areas):
            for c, a in enumerate(row):
                if a is area:
                    return r, c
        raise ValueError(f"{area!r} not found in section")


class Enterable:
    """Mixin for areas that transport the player into another section."""
    travel_to: tuple[Section, Area]


class Exitable:
    """Mixin for areas that transport the player out to another section."""
    travel_to: tuple[Section, Area]
