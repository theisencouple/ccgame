_VISITED_DIM = 35


from typing import NamedTuple


class Coordinates(NamedTuple):
    row: int
    col: int


class Area:
    def __init__(self, name: str, description: str = None,
                 color=(60, 60, 60), title=None, icon=None, image=None):
        self.name = name
        self.description = description
        self.color = color
        self.title = title or name.title()
        self.icon = icon
        self.image = image
        self.visited = False

    def tile_color(self):
        if self.visited:
            return self.color
        return tuple(max(0, c - _VISITED_DIM) for c in self.color)

    def enter(self, ui):
        if not self.visited:
            self.visited = True
            if self.description:
                ui.say(self.description)

    def render_minimap(self, ui, pos: Coordinates):
        ui.fill_rect(pos.row, pos.col, ui.TS, ui.TS, self.tile_color())

    def render(self, ui, pos: Coordinates, size: int):
        ui.fill_rect(pos.row + 1, pos.col + 1, size - 2, size - 2, self.tile_color(), border_radius=4)
        for i, ln in enumerate(ui.wrap(self.title, size - 8)):
            ui.blit(ln, ui.TEXT, pos.row + 5, pos.col + 5 + i * 15)
        if self.icon:
            ui.blit(self.icon, ui.TEXT, pos.row + size // 2, pos.col + size // 2)

    def render_panel(self, ui, panel):
        panel.title = self.title
        panel.draw(ui)
        if self.image:
            panel.load_image(ui, self.image)


class GenericArea(Area):
    pass


class Section:
    def __init__(self, areas: list[list[Area]]):
        self.areas = areas

    def get_area_from_coordinates(self, coordinates: Coordinates) -> Area:
        if coordinates.row < 0 or coordinates.col < 0:
            raise IndexError(f"Coordinates out of bounds: {coordinates.row}, {coordinates.col}")
        area = self.areas[coordinates.row][coordinates.col]
        if not area:
            raise ValueError(f"No area at {coordinates.row}, {coordinates.col}")
        return area

    def get_north(self, coordinates: Coordinates):
        c = Coordinates(coordinates.row - 1, coordinates.col)
        return self.get_area_from_coordinates(c), c

    def get_south(self, coordinates: Coordinates):
        c = Coordinates(coordinates.row + 1, coordinates.col)
        return self.get_area_from_coordinates(c), c

    def get_west(self, coordinates: Coordinates):
        c = Coordinates(coordinates.row, coordinates.col - 1)
        return self.get_area_from_coordinates(c), c

    def get_east(self, coordinates: Coordinates):
        c = Coordinates(coordinates.row, coordinates.col + 1)
        return self.get_area_from_coordinates(c), c
