from .base import Section
from areas.base import Area
from areas.cave import Cave
from areas.deepercave import DeeperCave
from areas.superdeepcave import SuperDeepCave
from areas.cave_entrance import Entrance

_C = Cave
_DC = DeeperCave
_SDC = SuperDeepCave

cave_opening= Entrance()

grid: list[list[Area]] = [
    [_SDC(), _SDC(), _SDC(),_DC(), _DC()],
    [_SDC(), _SDC(), _DC(),_DC(), _DC()],
    [_DC(), _DC(), _C(), _C(), _C()],
    [_DC(), _C(), cave_opening,_C(), _C()],
]

cave_section = Section(grid)
