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

        for row in range(ui.MAP_VIEW):
            for col in range(ui.MAP_VIEW):
                map_r = px - half + row
                map_c = py - half + col
                sx = ui.MX + col * ui.TS
                sy = ui.MY + row * ui.TS

                try:
                    if map_r < 0 or map_c < 0:
                        raise IndexError
                    self.areas[map_r][map_c].render_minimap(ui, sx, sy)
                except IndexError:
                    ui.fill_rect(sx, sy, ui.TS, ui.TS, colors.TILE_NONE)

                if map_r == px and map_c == py:
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
