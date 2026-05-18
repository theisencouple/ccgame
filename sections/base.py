from ui import colors
from ui.ui import UI

from areas.base import Area, Coordinates


class Section:
    def __init__(self, areas: list[list[Area]]) -> None:
        self.areas = areas

    def draw_map(self, ui: UI, px: int, py: int) -> None:
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
                    area = self.areas[map_r][map_c]
                    area.render_minimap(ui, sx, sy)
                except IndexError:
                    ui.fill_rect(sx, sy, ui.TS, ui.TS, colors.TILE_NONE)

                if map_r == px and map_c == py:
                    cx, cy = sx + ui.TS // 2, sy + ui.TS // 2
                    ui.fill_rect(cx - 3, cy - 3, 6, 6, colors.PLAYER)
        ui.MAP_PANEL.draw_title(ui)

    def get_area_from_coordinates(self, coordinates: Coordinates) -> Area:
        if coordinates.row < 0 or coordinates.col < 0:
            raise IndexError(f"Coordinates out of bounds: {coordinates.row}, {coordinates.col}")
        area = self.areas[coordinates.row][coordinates.col]
        if not area:
            raise ValueError(f"No area at {coordinates.row}, {coordinates.col}")
        return area

    def get_north(self, coordinates: Coordinates) -> tuple[Area, Coordinates]:
        c = Coordinates(coordinates.row - 1, coordinates.col)
        return self.get_area_from_coordinates(c), c

    def get_south(self, coordinates: Coordinates) -> tuple[Area, Coordinates]:
        c = Coordinates(coordinates.row + 1, coordinates.col)
        return self.get_area_from_coordinates(c), c

    def get_west(self, coordinates: Coordinates) -> tuple[Area, Coordinates]:
        c = Coordinates(coordinates.row, coordinates.col - 1)
        return self.get_area_from_coordinates(c), c

    def get_east(self, coordinates: Coordinates) -> tuple[Area, Coordinates]:
        c = Coordinates(coordinates.row, coordinates.col + 1)
        return self.get_area_from_coordinates(c), c

    def find(self, area: Area) -> Coordinates:
        for r, row in enumerate(self.areas):
            for c, a in enumerate(row):
                if a is area:
                    return Coordinates(r, c)
        raise ValueError(f"{area!r} not found in section")


class Enterable:
    """Mixin for areas that transport the player into another section."""
    travel_to: tuple[Section, Area]


class Exitable:
    """Mixin for areas that transport the player out to another section."""
    travel_to: tuple[Section, Area]
