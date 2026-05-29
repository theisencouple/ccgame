from .base import Section
from .village_section import village_section, gate
from areas.base import Area
from areas.field import Field
from areas.forest import Forest
from areas.cave import Cave
from areas.lake import Lake, LakeEdge, LakeCorner
from areas.village import Village
from areas.strawberry_field import StrawberryField
from areas.ruin import Ruin
from monsters.goblin import Goblin

SIZE = 30

grid: list[list[Area]] = [[Field() for _ in range(SIZE)] for _ in range(SIZE)]

# Forest in the northwest
for r in range(2, 13):
    for c in range(1, 9):
        grid[r][c] = Forest()

grid[12][8].monster = Goblin()
grid[12][7].monster = Goblin()

# Lake in the southeast — interior, edges, corners
for r in range(19, 27):
    for c in range(19, 28):
        grid[r][c] = Lake()

for c in range(20, 27):
    grid[19][c] = LakeEdge(0)    # top
    grid[26][c] = LakeEdge(180)  # bottom
for r in range(20, 26):
    grid[r][19] = LakeEdge(90)   # left
    grid[r][27] = LakeEdge(270)  # right

grid[19][19] = LakeCorner(0)    # top-left
grid[19][27] = LakeCorner(270)  # top-right
grid[26][19] = LakeCorner(90)   # bottom-left
grid[26][27] = LakeCorner(180)  # bottom-right

# Cave cluster east of center
for r in range(8, 12):
    for c in range(20, 24):
        grid[r][c] = Cave()

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

village.travel_to_enter = (village_section, gate)
gate.travel_to_exit = (starting_section, village)
