from pathlib import Path
from areas.base import Area
from sections.base import Exitable
from ui import colors


class VillageGate(Area, Exitable):
    def __init__(self) -> None:
        super().__init__("village gate", "A worn gate at the village edge.", color=colors.VILLAGE_GATE, image=Path("assets/village_gate.png"))
