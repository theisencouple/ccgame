from area import GenericArea, Section

SIZE = 30

FIELD_COLOR = (45, 105, 42)
FOREST_COLOR = (28, 78, 38)
CAVE_COLOR = (75, 65, 55)
LAKE_COLOR = (35, 72, 148)
VILLAGE_COLOR = (135, 100, 55)
STRAWBERRY_COLOR = (148, 52, 72)


def _field():
    return GenericArea("field", "An open field.", color=FIELD_COLOR, image="assets/field.png")


def _forest():
    return GenericArea("forest", "Dense trees surround you.", color=FOREST_COLOR, image="assets/forest.png")


def _cave():
    return GenericArea("cave", "A dark cave.", color=CAVE_COLOR, image="assets/cave.png")


def _lake():
    return GenericArea("lake", "A calm lake.", color=LAKE_COLOR, image="assets/lake.png")


def _village():
    return GenericArea("village", "A small village.", color=VILLAGE_COLOR, image="assets/village.png")


def _strawberry():
    return GenericArea("strawberry field", "Wild strawberries grow here.", color=STRAWBERRY_COLOR, image="assets/strawberry_field.png")


grid = [[_field() for _ in range(SIZE)] for _ in range(SIZE)]

# Forest in the northwest
for r in range(2, 13):
    for c in range(1, 9):
        grid[r][c] = _forest()

# Lake in the southeast
for r in range(19, 27):
    for c in range(19, 28):
        grid[r][c] = _lake()

# Cave cluster east of center
for r in range(8, 12):
    for c in range(20, 24):
        grid[r][c] = _cave()

# Strawberry fields south of center
for r in range(22, 26):
    for c in range(8, 13):
        grid[r][c] = _strawberry()

# Village at center (player start)
grid[15][15] = _village()

starting_section = Section(grid)
