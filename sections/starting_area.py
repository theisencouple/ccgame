from .base import Section
from .village_section import village_section, gate
from areas.base import Area
from areas.field import Field
from areas.forest import Forest
from areas.cave import Cave
from areas.deepercave import DeeperCave
from areas.superdeepcave import SuperDeepCave
from areas.lake import Lake
from areas.village import Village
from areas.strawberry_field import StrawberryField
from areas.ruin import Ruin

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

grid[6][15] = Ruin()
grid[6][16] = Ruin()
grid[7][15] = Ruin()

# Village at center (player start)
village = Village()
grid[15][15] = village

starting_section = Section(grid)

village.travel_to = (village_section, gate)
gate.travel_to = (starting_section, village)