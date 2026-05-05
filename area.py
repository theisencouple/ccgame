from pathlib import Path
from typing import NamedTuple

from ui.ui import UI
from ui.panel import Panel

_VISITED_DIM = 35


class Coordinates(NamedTuple):
    row: int
    col: int


class Area:
    def __init__(self, name: str, description: str,
                 color: tuple[int, int, int] = (60, 60, 60),
                 image: Path | None = None) -> None:
        self.name = name
        self.description = description
        self.color = color
        self.image = image
        self.visited = False

    def tile_color(self) -> tuple[int, ...]:
        if self.visited:
            return self.color
        return tuple(max(0, c - _VISITED_DIM) for c in self.color)

    def enter(self, ui: UI) -> None:
        if not self.visited:
            self.visited = True
            if self.description:
                ui.say(self.description)

    def render_minimap(self, ui: UI, x: int, y: int) -> None:
        ui.fill_rect(x, y, ui.TS, ui.TS, self.tile_color())

    def render_panel(self, ui: UI, panel: Panel) -> None:
        panel.title = self.name.title()
        panel.draw(ui)
        if self.image:
            panel.load_image(ui, self.image)


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
                except IndexError:
                    area = None

                if area:
                    area.render_minimap(ui, sx, sy)
                else:
                    ui.fill_rect(sx, sy, ui.TS, ui.TS, ui.TILE_NONE)

                if map_r == px and map_c == py:
                    cx, cy = sx + ui.TS // 2, sy + ui.TS // 2
                    ui.fill_rect(cx - 3, cy - 3, 6, 6, ui.PLAYER)

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
