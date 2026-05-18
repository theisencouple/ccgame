from .base import UIBase
from .panel import Panel, PanelWithTitle, MessagePanel


class UI(UIBase):
    # ── Layout ────────────────────────────────────────────────────────────────
    W = 1100
    H = 700
    PAD = 12
    TS = 16
    MAP_VIEW = 20
    MX = PAD
    MY = PAD
    MW = MAP_VIEW * TS
    MH = MAP_VIEW * TS
    AX = MX
    AY = MY + MH + PAD
    AW = MW
    AH = H - AY - PAD
    PX = MX + MW + PAD
    PY = PAD
    PW = W - PX - PAD
    PH = 350
    LX = PX
    LY = PY + PH + PAD
    LW = PW
    LH = H - LY - PAD

    MAP_PANEL = PanelWithTitle(MX, MY, MW, MH, "Map")
    ACTIONS_PANEL = PanelWithTitle(AX, AY, AW, AH, "Actions")
    AREA_PANEL = Panel(PX, PY, PW, PH)
    MESSAGES_PANEL = MessagePanel(LX, LY, LW, LH, "Messages")

    def say(self, text: str) -> None:
        self.MESSAGES_PANEL.say(text)

    def scroll(self, delta: int) -> None:
        self.MESSAGES_PANEL.scroll(delta)
