import pytest
from unittest.mock import MagicMock
from sections.base import Area, Coordinates, Section


class TestCoordinates:
    def test_row_and_col(self):
        c = Coordinates(3, 5)
        assert c.row == 3
        assert c.col == 5

    def test_equality(self):
        assert Coordinates(1, 2) == Coordinates(1, 2)


class TestArea:
    def test_tile_color_unvisited_is_dimmed(self):
        area = Area("field", "desc", color=(45, 105, 42))
        assert area.tile_color() == (10, 70, 7)

    def test_tile_color_visited_is_full(self):
        area = Area("field", "desc", color=(45, 105, 42))
        area.visited = True
        assert area.tile_color() == (45, 105, 42)

    def test_tile_color_clamps_at_zero(self):
        area = Area("dark", "desc", color=(10, 10, 10))
        assert all(c >= 0 for c in area.tile_color())

    def test_enter_marks_visited(self):
        area = Area("field", "An open field.", color=(0, 0, 0))
        area.enter(MagicMock())
        assert area.visited is True

    def test_enter_calls_say(self):
        area = Area("field", "An open field.", color=(0, 0, 0))
        ui = MagicMock()
        area.enter(ui)
        ui.say.assert_called_once_with("An open field.")

    def test_enter_no_say_with_empty_description(self):
        area = Area("field", "", color=(0, 0, 0))
        ui = MagicMock()
        area.enter(ui)
        ui.say.assert_not_called()

    def test_enter_only_says_once(self):
        area = Area("field", "An open field.", color=(0, 0, 0))
        ui = MagicMock()
        area.enter(ui)
        area.enter(ui)
        ui.say.assert_called_once()




class TestSection:
    def _section(self, rows=3, cols=3):
        grid = [[Area(f"{r},{c}", "", color=(0, 0, 0)) for c in range(cols)] for r in range(rows)]
        return Section(grid), grid

    def test_get_area(self):
        section, grid = self._section()
        assert section.get_area_from_coordinates(Coordinates(1, 2)) is grid[1][2]

    def test_negative_row_raises(self):
        section, _ = self._section()
        with pytest.raises(IndexError):
            section.get_area_from_coordinates(Coordinates(-1, 0))

    def test_negative_col_raises(self):
        section, _ = self._section()
        with pytest.raises(IndexError):
            section.get_area_from_coordinates(Coordinates(0, -1))

    def test_get_north(self):
        section, grid = self._section()
        area, coords = section.get_north(Coordinates(2, 1))
        assert area is grid[1][1]
        assert coords == Coordinates(1, 1)

    def test_get_south(self):
        section, grid = self._section()
        area, coords = section.get_south(Coordinates(0, 1))
        assert area is grid[1][1]
        assert coords == Coordinates(1, 1)

    def test_get_west(self):
        section, grid = self._section()
        area, coords = section.get_west(Coordinates(1, 2))
        assert area is grid[1][1]
        assert coords == Coordinates(1, 1)

    def test_get_east(self):
        section, grid = self._section()
        area, coords = section.get_east(Coordinates(1, 0))
        assert area is grid[1][1]
        assert coords == Coordinates(1, 1)

    def test_get_north_out_of_bounds_raises(self):
        section, _ = self._section()
        with pytest.raises(IndexError):
            section.get_north(Coordinates(0, 0))

    def test_get_south_out_of_bounds_raises(self):
        section, _ = self._section()
        with pytest.raises(IndexError):
            section.get_south(Coordinates(2, 0))
