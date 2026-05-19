from .base import Section
from areas.base import Area
from areas.village_street import VillageStreet
from areas.village_house import VillageHouseWall, VillageHouseDoor, VillageHouseInterior
from areas.blacksmith import BlacksmithWall, BlacksmithDoor, BlacksmithInterior
from areas.village_gate import VillageGate

_S  = VillageStreet
_HW = VillageHouseWall
_HD = VillageHouseDoor
_HI = VillageHouseInterior
_BW = BlacksmithWall
_BD = BlacksmithDoor
_BI = BlacksmithInterior

gate = VillageGate()

# fmt: off
grid: list[list[Area]] = [
    [_HW(), _HW(), _HW(), _S(),  _HW(), _HW(), _HW()],  # row 0
    [_HW(), _HI(), _HW(), _S(),  _HW(), _HI(), _HW()],  # row 1
    [_HW(), _HD(), _HW(), _S(),  _HW(), _HD(), _HW()],  # row 2
    [_S(),  _S(),  _S(),  _S(),  _S(),  _S(),  _S() ],  # row 3
    [_BW(), _BW(), _BW(), _S(),  _HW(), _HW(), _HW()],  # row 4
    [_BW(), _BI(), _BW(), _S(),  _HW(), _HI(), _HW()],  # row 5
    [_BW(), _BD(), _BW(), _S(),  _HW(), _HD(), _HW()],  # row 6
    [_S(),  _S(),  _S(),  _S(),  _S(),  _S(),  _S() ],  # row 7
    [_S(),  _S(),  gate,  _S(),  _S(),  _S(),  _S() ],  # row 8
]
# fmt: on

village_section = Section(grid)