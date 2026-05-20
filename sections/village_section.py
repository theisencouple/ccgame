from .base import Section
from areas.base import Area
from areas.village_street import VillageStreet
from areas.building_wall import BuildingWall
from areas.village_house import VillageHouseDoor, VillageHouseInterior
from areas.blacksmith import BlacksmithDoor, BlacksmithInterior
from areas.village_gate import VillageGate

_S  = VillageStreet
_HW = BuildingWall
_HD = VillageHouseDoor
_HI = VillageHouseInterior
_BD = BlacksmithDoor
_BI = BlacksmithInterior

gate = VillageGate()

# fmt: off
grid: list[list[Area]] = [
    [_HW(), _HW(), _HW(), _S(),  _HW(), _HW(), _HW()],  # row 0
    [_HW(), _HI(), _HW(), _S(),  _HW(), _HI(), _HW()],  # row 1
    [_HW(), _HD(), _HW(), _S(),  _HW(), _HD(), _HW()],  # row 2
    [_S(),  _S(),  _S(),  _S(),  _S(),  _S(),  _S() ],  # row 3
    [_HW(), _HW(), _HW(), _S(),  _HW(), _HW(), _HW()],  # row 4
    [_HW(), _BI(), _HW(), _S(),  _HW(), _HI(), _HW()],  # row 5
    [_HW(), _BD(), _HW(), _S(),  _HW(), _HD(), _HW()],  # row 6
    [_S(),  _S(),  _S(),  _S(),  _S(),  _S(),  _S() ],  # row 7
    [_S(),  _S(),  gate,  _S(),  _S(),  _S(),  _S() ],  # row 8
]
# fmt: on

village_section = Section(grid)