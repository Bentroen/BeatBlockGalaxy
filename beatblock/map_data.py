# This module stores the positions for all blocks in the Beat Block Galaxy.

from dataclasses import dataclass
from enum import Enum
from typing import Tuple


BLOCK_SIZE = 2

Coords = Tuple[int, int, int]


class BlockType(Enum):
    SOLID = 1
    BEAT_GREEN = 2
    BEAT_YELLOW = 3


S = BlockType.SOLID
G = BlockType.BEAT_GREEN
Y = BlockType.BEAT_YELLOW


@dataclass
class Block:
    x: int
    y: int
    z: int
    type: BlockType

    @property
    def coords(self) -> Coords:
        return self.x, self.y, self.z


def square(bottom_left: Coords, type: BlockType):
    x, y, z = bottom_left
    return [
        Block(x, y, z, type),
        Block(x + 2, y, z, type),
        Block(x, y, z + 2, type),
        Block(x + 2, y, z + 2, type),
    ]


def fill(bottom_left: Coords, top_right: Coords, type: BlockType):
    x1, y1, z1 = bottom_left
    x2, y2, z2 = top_right
    return [
        Block(x, y, z, type)
        for x in range(x1, x2 + 1, BLOCK_SIZE)
        for y in range(y1, y2 + 1, BLOCK_SIZE)
        for z in range(z1, z2 + 1, BLOCK_SIZE)
    ]


BLOCKS = [
    # Starting bridge
    *fill((0, 0, 0), (2, 0, 8), S),
    # 2 green to the right
    *fill((2, 0, 8), (2, 0, 10), G),
    # 2 yellow to the left
    *fill((0, 0, 12), (0, 0, 14), Y),
    # Solid square
    *fill((0, 0, 16), (2, 0, 18), S),
    # Green and yellow rows
    *fill((2, 0, 20), (2, 0, 26), G),
    *fill((0, 0, 20), (0, 0, 26), Y),
    # Solid square
    *fill((0, 0, 28), (2, 0, 30), S),
]
