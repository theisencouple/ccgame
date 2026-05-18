import pygame
from unittest.mock import MagicMock
from areas.base import Area
from sections.base import Section
from character import Character


def _make(rows=5, cols=5, start_row=0, start_col=0):
    grid = [[Area(f"{r},{c}", "", color=(0, 0, 0)) for c in range(cols)] for r in range(rows)]
    section = Section(grid)
    return Character(section, grid[start_row][start_col]), section.areas


class TestCharacter:
    def test_initial_area(self):
        c, grid = _make()
        assert c.area is grid[0][0]

    def test_get_actions_returns_strings(self):
        c, _ = _make()
        actions = c.get_actions()
        assert len(actions) > 0
        assert all(isinstance(k, str) and isinstance(v, str) for k, v in actions)

    def test_move_up(self):
        c, grid = _make(start_row=2, start_col=2)
        c.handle_key(pygame.K_UP, MagicMock())
        assert c.area is grid[1][2]

    def test_move_down(self):
        c, grid = _make(start_row=2, start_col=2)
        c.handle_key(pygame.K_DOWN, MagicMock())
        assert c.area is grid[3][2]

    def test_move_left(self):
        c, grid = _make(start_row=2, start_col=2)
        c.handle_key(pygame.K_LEFT, MagicMock())
        assert c.area is grid[2][1]

    def test_move_right(self):
        c, grid = _make(start_row=2, start_col=2)
        c.handle_key(pygame.K_RIGHT, MagicMock())
        assert c.area is grid[2][3]

    def test_move_into_boundary_stays_put(self):
        c, grid = _make(start_row=0, start_col=0)
        c.handle_key(pygame.K_UP, MagicMock())
        assert c.area is grid[0][0]

    def test_move_calls_enter(self):
        c, _ = _make(start_row=2, start_col=2)
        ui = MagicMock()
        c.handle_key(pygame.K_UP, ui)
        ui.say.assert_not_called()