import sys

import pygame

from ui import UI
from area import Coordinates
from character import Character
from starting_area import starting_section


pygame.init()

ui = UI()
screen = pygame.display.set_mode((UI.W, UI.H))
pygame.display.set_caption("Adventure")
FPS = 30

ui.init(screen)

character = Character(starting_section)
character.coordinates = Coordinates(15, 15)
character.get_area().enter(ui)


def main():
    clock = pygame.time.Clock()

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_PAGEUP:
                    ui.scroll(5)
                elif event.key == pygame.K_PAGEDOWN:
                    ui.scroll(-5)
                character.handle_key(event.key, ui)


        ui.draw(starting_section, character)


if __name__ == "__main__":
    main()
