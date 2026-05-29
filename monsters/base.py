from __future__ import annotations

from pathlib import Path

from ui.ui import UI
from ui.panel import Panel


class Monster:
    def __init__(self, name: str, max_hp: int, attack_power: int, image: Path) -> None:
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.attack_power = attack_power
        self.image = image

    @property
    def is_alive(self) -> bool:
        return self.hp > 0

    def take_damage(self, amount: int) -> None:
        self.hp = max(0, self.hp - amount)

    def render(self, ui: UI, panel: Panel) -> None:
        panel.overlay_image(ui, self.image, panel.w // 3, panel.h // 4, panel.w // 3, panel.h // 4 * 3)
