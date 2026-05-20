import pytest
import pygame
from unittest.mock import MagicMock
from areas.base import Area
from sections.base import Section

_C = pygame.Color


class TestArea:
    def test_enter_marks_visited(self):
        area = Area("field", "An open field.", _C(0, 0, 0))
        area.enter(MagicMock())
        assert area.visited is True

    def test_enter_calls_say(self):
        area = Area("field", "An open field.", _C(0, 0, 0))
        ui = MagicMock()
        area.enter(ui)
        ui.say.assert_called_once_with("An open field.")

    def test_enter_no_say_with_empty_description(self):
        area = Area("field", "", _C(0, 0, 0))
        ui = MagicMock()
        area.enter(ui)
        ui.say.assert_not_called()

    def test_enter_only_says_once(self):
        area = Area("field", "An open field.", _C(0, 0, 0))
        ui = MagicMock()
        area.enter(ui)
        area.enter(ui)
        ui.say.assert_called_once()


class TestSection:
    def _section(self, rows=3, cols=3):
        grid = [[Area(f"{r},{c}", "", _C(0, 0, 0)) for c in range(cols)] for r in range(rows)]
        return Section(grid), grid

    def test_get_north(self):
        section, grid = self._section()
        assert section.get_north(grid[2][1]) is grid[1][1]

    def test_get_south(self):
        section, grid = self._section()
        assert section.get_south(grid[0][1]) is grid[1][1]

    def test_get_west(self):
        section, grid = self._section()
        assert section.get_west(grid[1][2]) is grid[1][1]

    def test_get_east(self):
        section, grid = self._section()
        assert section.get_east(grid[1][0]) is grid[1][1]

    def test_get_north_out_of_bounds_raises(self):
        section, grid = self._section()
        with pytest.raises(IndexError):
            section.get_north(grid[0][0])

    def test_get_south_out_of_bounds_raises(self):
        section, grid = self._section()
        with pytest.raises(IndexError):
            section.get_south(grid[2][0])