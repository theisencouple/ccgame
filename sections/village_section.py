from .base import Section
from areas.base import Area
from areas.village_street import VillageStreet
from areas.blacksmith import Blacksmith
from areas.village_house import VillageHouse
from areas.village_gate import VillageGate

# Layout (row, col):
#   col:  0        1        2        3        4
# row 0: house    house    street   house    house
# row 1: street   street   street   street   street   <- main road
# row 2: smith    street   street   house    house
# row 3: house    street   exit     street   house   <- entry/exit

_S = VillageStreet
_H = VillageHouse

gate = VillageGate()

grid: list[list[Area]] = [
    [_H(), _H(), _S(),         _H(), _H()],
    [_S(), _S(), _S(),         _S(), _S()],
    [Blacksmith(), _S(), _S(), _H(), _H()],
    [_H(), _S(), gate,         _S(), _H()],
]

village_section = Section(grid)