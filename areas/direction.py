from dataclasses import dataclass
from enum import Enum
from typing import Self

import pygame


@dataclass(frozen=True)
class DirectionData:
    row: int
    col: int
    rotation: int
    key: int


class Direction(Enum):
    NORTH = DirectionData(row=-1, col=0,  rotation=0,   key=pygame.K_UP)
    SOUTH = DirectionData(row=1,  col=0,  rotation=180, key=pygame.K_DOWN)
    EAST  = DirectionData(row=0,  col=1,  rotation=270,  key=pygame.K_RIGHT)
    WEST  = DirectionData(row=0,  col=-1, rotation=90, key=pygame.K_LEFT)

    @classmethod
    def key_map(cls) -> dict[int, Self]:
        return {d.key: d for d in cls}

    @property
    def row(self) -> int:      return self.value.row
    @property
    def col(self) -> int:      return self.value.col
    @property
    def rotation(self) -> int: return self.value.rotation
    @property
    def key(self) -> int:      return self.value.key

    def rotated(self, degrees: int) -> Self:
        target = (self.rotation + degrees) % 360
        return next(d for d in type(self) if d.rotation == target)

    @property
    def opposite(self) -> Self:
        return self.rotated(180)

