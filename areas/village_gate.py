from pathlib import Path
from areas.base import Area
from ui import colors


class VillageGate(Area):
    def __init__(self) -> None:
        super().__init__("village gate", "A worn gate at the village edge.", colors.VILLAGE_GATE, image=Path("assets/village_gate.png"))
