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
    CPX = PX
    CPY = PY + PH + PAD
    CPW = 250
    CPH = H - CPY - PAD
    LX = CPX + CPW + PAD
    LY = CPY
    LW = W - LX - PAD
    LH = CPH

    MAP_PANEL = PanelWithTitle(MX, MY, MW, MH, "Map")
    ACTIONS_PANEL = PanelWithTitle(AX, AY, AW, AH, "Actions")
    AREA_PANEL = Panel(PX, PY, PW, PH)
    CHARACTER_PANEL = PanelWithTitle(CPX, CPY, CPW, CPH, "Character")
    MESSAGES_PANEL = MessagePanel(LX, LY, LW, LH, "Messages")

    def say(self, text: str) -> None:
        self.MESSAGES_PANEL.say(text)

    def scroll(self, delta: int) -> None:
        self.MESSAGES_PANEL.scroll(delta)
