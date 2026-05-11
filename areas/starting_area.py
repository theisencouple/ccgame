from .base import Section, Area
from .field import Field
from .forest import Forest
from .cave import Cave
from .lake import Lake
from .village import Village
from .strawberry_field import StrawberryField
from .deepercave import DeeperCave
from .superdeepcave import SuperDeepCave

from noise import pnoise2
import random

SIZE = 64
SCALE = 18.0  # controls biome size

# generate terrain grid
grid: list[list[Area]] = []

for r in range(SIZE):
    row: list[Area] = []

    for c in range(SIZE):

        # Perlin noise value (-1 to 1)
        biome = pnoise2(r / SCALE, c / SCALE, octaves=3)

        # stretch the noise so high values are more common
        biome *= 1.4

        if biome < -0.3:
            tile = Lake()

        elif biome < -0.05:
            tile = Field()

        elif biome < 0.15:
            tile = Forest()

        elif biome < 0.30:
            tile = StrawberryField()

        elif biome < 0.45:
            tile = Cave()

        elif biome < 0.65:
            tile = DeeperCave()

        else:
            tile = SuperDeepCave()

        row.append(tile)

    grid.append(row)


# ------------------------------------------------
# Guarantee at least one of each biome
# ------------------------------------------------
required_biomes = [
    Forest,
    Lake,
    Cave,
    StrawberryField,
    DeeperCave,
    SuperDeepCave
]

for biome_class in required_biomes:

    found = False

    for row in grid:
        for tile in row:
            if isinstance(tile, biome_class):
                found = True
                break
        if found:
            break

    if not found:
        r = random.randint(0, SIZE - 1)
        c = random.randint(0, SIZE - 1)
        grid[r][c] = biome_class()


# village always at center
grid[SIZE // 2][SIZE // 2] = Village()

starting_section = Section(grid)
