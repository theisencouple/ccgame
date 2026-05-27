from pathlib import Path
from areas.base import AreaWithOverlay


class VillageGate(AreaWithOverlay):
    def __init__(self) -> None:
        super().__init__("village gate", "A worn gate at the village edge.",
                         Path("assets/village_street_16x16.png"),
                         Path("assets/bottom_grass_16x16.png"),
                         image=Path("assets/village_gate.png"))
