from .base import Section
from areas.base import Area
from areas.village_street import VillageStreet
from areas.building import BuildingWall, BuildingCorner
from areas.village_house import VillageHouseDoor, VillageHouseInterior
from areas.blacksmith import BlacksmithDoor, BlacksmithInterior
from areas.village_gate import VillageGate

_S   = VillageStreet
_BN  = lambda: BuildingWall(180)    # south face — blocks NORTH entry
_BS  = lambda: BuildingWall(0)      # north face — blocks SOUTH entry
_BW  = lambda: BuildingWall(270)    # east face  — blocks WEST entry
_BE  = lambda: BuildingWall(90)     # west face  — blocks EAST entry
_CTL = lambda: BuildingCorner(0)    # top-left corner
_CBL = lambda: BuildingCorner(90)  # bottom-left corner
_CBR = lambda: BuildingCorner(180)  # bottom-right corner
_CTR = lambda: BuildingCorner(270)   # top-right corner
_HD  = VillageHouseDoor
_HI  = VillageHouseInterior
_BD  = BlacksmithDoor
_BI  = BlacksmithInterior

gate = VillageGate()

# fmt: off
grid: list[list[Area]] = [
    [_CTL(), _BN(), _CTR(), _S(),  _CTL(), _BN(), _CTR()],  # row 0 - top of north buildings
    [_BW(),  _HI(), _BE(),  _S(),  _BW(),  _HI(), _BE() ],  # row 1 - sides
    [_CBL(), _HD(), _CBR(), _S(),  _CBL(), _HD(), _CBR()],  # row 2 - south face of north buildings
    [_S(),   _S(),  _S(),   _S(),  _S(),   _S(),  _S()  ],  # row 3 - street
    [_CTL(), _BN(), _CTR(), _S(),  _CTL(), _BN(), _CTR()],  # row 4 - north face of south buildings
    [_BW(),  _BI(), _BE(),  _S(),  _BW(),  _HI(), _BE() ],  # row 5 - sides
    [_CBL(), _BD(), _CBR(), _S(),  _CBL(), _HD(), _CBR()],  # row 6 - south face of south buildings
    [_S(),   _S(),  _S(),   _S(),  _S(),   _S(),  _S()  ],  # row 7 - street
    [_S(),   _S(),  gate,   _S(),  _S(),   _S(),  _S()  ],  # row 8 - gate
]
# fmt: on

village_section = Section(grid)
