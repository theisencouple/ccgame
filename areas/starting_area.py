from .base import Section, Area
from .field import Field
from .forest import Forest
from .cave import Cave
from .lake import Lake
from .village import Village
from .strawberry_field import StrawberryField
from .deepercave import DeeperCave
from .superdeepcave import SuperDeepCave

SIZE = 30

grid: list[list[Area]] = [[Field() for _ in range(SIZE)] for _ in range(SIZE)]

# Forest in the northwest
for r in range(2, 13):
    for c in range(1, 9):
        grid[r][c] = Forest()

# Lake in the southeast
for r in range(19, 27):
    for c in range(19, 28):
        grid[r][c] = Lake()

#Cave
for r in range(7, 16):
    for c in range(14, 25):
        grid[r][c] = Cave()

#MiddleCave
for r in range(9, 14):
    for c in range(16, 23):
        grid[r][c] = DeeperCave()

#CenterCave
for r in range(10, 13):
    for c in range(18, 21):
        grid[r][c] = SuperDeepCave()

# Strawberry fields south of center
for r in range(22, 26):
    for c in range(8, 13):
        grid[r][c] = StrawberryField()

# Village at center (player start)
grid[15][15] = Village()

starting_section = Section(grid)
