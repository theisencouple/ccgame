import pygame
from area import Section, Area, Coordinates


class Character:
    def __init__(self, section: Section):
        self.section = section
        self.coordinates = Coordinates(0, 0)

    def get_actions(self) -> list[tuple]:
        return [("arrow keys", "Move")]

    def get_area(self) -> Area:
        return self.section.get_area_from_coordinates(self.coordinates)

    def handle_key(self, key: int, ui) -> bool:
        try:
            if key == pygame.K_UP:
                area, self.coordinates = self.section.get_north(self.coordinates)
            elif key == pygame.K_DOWN:
                area, self.coordinates = self.section.get_south(self.coordinates)
            elif key == pygame.K_LEFT:
                area, self.coordinates = self.section.get_west(self.coordinates)
            elif key == pygame.K_RIGHT:
                area, self.coordinates = self.section.get_east(self.coordinates)
            else:
                return False
            area.enter(ui)
        except (ValueError, IndexError):
            pass
        return True


