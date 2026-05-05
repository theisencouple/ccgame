import pygame
from unittest.mock import MagicMock
from area import GenericArea, Section, Coordinates
from character import Character


def _section(rows=5, cols=5):
    grid = [[GenericArea(f"{r},{c}") for c in range(cols)] for r in range(rows)]
    return Section(grid)


class TestCharacter:
    def test_initial_coordinates(self):
        assert Character(_section()).coordinates == Coordinates(0, 0)

    def test_get_area(self):
        section = _section()
        c = Character(section)
        c.coordinates = Coordinates(2, 3)
        assert c.get_area() is section.areas[2][3]

    def test_get_actions_returns_strings(self):
        actions = Character(_section()).get_actions()
        assert len(actions) > 0
        assert all(isinstance(k, str) and isinstance(v, str) for k, v in actions)

    def test_move_up(self):
        c = Character(_section())
        c.coordinates = Coordinates(2, 2)
        c.handle_key(pygame.K_UP, MagicMock())
        assert c.coordinates == Coordinates(1, 2)

    def test_move_down(self):
        c = Character(_section())
        c.coordinates = Coordinates(2, 2)
        c.handle_key(pygame.K_DOWN, MagicMock())
        assert c.coordinates == Coordinates(3, 2)

    def test_move_left(self):
        c = Character(_section())
        c.coordinates = Coordinates(2, 2)
        c.handle_key(pygame.K_LEFT, MagicMock())
        assert c.coordinates == Coordinates(2, 1)

    def test_move_right(self):
        c = Character(_section())
        c.coordinates = Coordinates(2, 2)
        c.handle_key(pygame.K_RIGHT, MagicMock())
        assert c.coordinates == Coordinates(2, 3)

    def test_move_into_boundary_stays_put(self):
        c = Character(_section())
        c.coordinates = Coordinates(0, 0)
        c.handle_key(pygame.K_UP, MagicMock())
        assert c.coordinates == Coordinates(0, 0)

    def test_unknown_key_returns_false(self):
        c = Character(_section())
        assert c.handle_key(pygame.K_SPACE, MagicMock()) is False

    def test_valid_move_returns_true(self):
        c = Character(_section())
        c.coordinates = Coordinates(2, 2)
        assert c.handle_key(pygame.K_UP, MagicMock()) is True

    def test_move_calls_enter(self):
        section = _section()
        c = Character(section)
        c.coordinates = Coordinates(2, 2)
        ui = MagicMock()
        c.handle_key(pygame.K_UP, ui)
        ui.say.assert_not_called()
        c.handle_key(pygame.K_UP, ui)
