from pathlib import Path
from .base import Area
from ui import colors
from ui.ui import UI
from ui.panel import Panel


class Forest(Area):
    def __init__(self) -> None:
        super().__init__("forest", "Dense trees surround you.", colors.FOREST, image=Path("assets/forest.png"))


    def render_panel(self, ui: UI, panel: Panel) -> None:
        super().render_panel(ui, panel)
        panel.overlay_image(ui, Path("assets/goblin.png"), panel.w // 3, panel.h // 4, panel.w // 3, panel.h // 4 * 3)
