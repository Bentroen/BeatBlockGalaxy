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
        for y in (
            y / 2 for y in range(round(y1 * 2), round((y2 + 1) * 2), BLOCK_SIZE * 2)
        )  # deal with non-integer y values
        for z in range(z1, z2 + 1, BLOCK_SIZE)
    ]


def pyramid(top: Coords, height: int):
    x, y, z = top
    for i in range(0, height, BLOCK_SIZE):
        for j in range(-i, i + 1, BLOCK_SIZE):
            if i == 0 or (i == height - BLOCK_SIZE and (j == i or j == -i)):
                type = S
            else:
                type = (
                    G
                    if (i % (2 * BLOCK_SIZE) == 0) ^ (j % (2 * BLOCK_SIZE) == 0)
                    else Y
                )
            yield Block(x - j, y - i // 2, z - i, type)


def full_pyramid(top: Coords, height: int):
    x, y, z = top
    for i in range(0, height, BLOCK_SIZE):
        curr_y = y - i // BLOCK_SIZE
        for j in range(-i + BLOCK_SIZE, i + 1, BLOCK_SIZE):
            if (
                i == 0
                or (i == height - BLOCK_SIZE and j == i)
                or (i == height - BLOCK_SIZE * 2 and j == 0)
            ):
                type = S
            else:
                type = (
                    G
                    if (i % (2 * BLOCK_SIZE) == 0) ^ (j % (2 * BLOCK_SIZE) == 0)
                    else Y
                )

            yield (
                Block(x - j, curr_y, z - i, type),  # west
                Block(x + j, curr_y, z + i, type),  # east
                Block(x + i, curr_y, z - j, type),  # south
                Block(x - i, curr_y, z + j, type),  # north
            )


BASE_BLOCKS = [
    # Starting bridge
    *fill((0, 0, 0), (2, 0, 6), S),
    # 2 green to the right
    *fill((0, 0, 8), (0, 0, 10), S),
    *fill((2, 0, 8), (2, 0, 10), G),
    # 2 yellow to the left
    *fill((0, 0, 12), (0, 0, 14), Y),
    *fill((2, 0, 12), (2, 0, 14), S),
    # Solid square
    *fill((0, 0, 16), (2, 0, 18), S),
    # Green and yellow rows
    *fill((2, 0, 20), (2, 0, 26), G),
    *fill((0, 0, 20), (0, 0, 26), Y),
    # Solid square
    *fill((0, 0, 28), (2, 0, 30), S),
    # Green step
    *fill((0, 1, 32), (2, 1, 32), G),
    # Solid bridge
    *fill((0, 2, 34), (2, 2, 40), S),
    # Green square
    *fill((0, 2, 42), (2, 2, 44), G),
    # Yellow square
    *fill((0, 2, 46), (2, 2, 48), Y),
    # Solid square
    *fill((0, 2, 50), (2, 2, 52), S),
    # Green square
    *fill((-4, 1.5, 50), (-2, 1.5, 52), G),
    # Yellow square
    *fill((-8, 1.5, 50), (-6, 1.5, 52), Y),
    # HERE is a square that changes color according to the mission
    #
    # Solid bridge
    *fill((-8, 2, 58), (-6, 2, 64), S),
    # Alternating green and yellow rows
    *fill((-6, 2, 66), (-6, 2, 68), G),
    *fill((-4, 2, 66), (-4, 2, 68), Y),
    *fill((-2, 2, 66), (-2, 2, 68), G),
    *fill((0, 2, 66), (0, 2, 68), Y),
    *fill((2, 2, 66), (2, 2, 68), G),
    *fill((4, 2, 66), (4, 2, 68), Y),
    *fill((6, 2.5, 66), (6, 2.5, 68), G),
    *fill((8, 3, 66), (8, 3, 68), Y),
    # Green and yellow pairs
    *fill((10, 2, 66), (12, 2, 66), Y),
    *fill((10, 2, 68), (12, 2, 68), G),
    *fill((18, 2, 70), (18, 2, 72), Y),
    # Individual green and yellow blocks
    Block(14, 2, 66, G),
    Block(16, 2, 68, Y),
    Block(18, 2, 68, G),
    # Solid bridge
    *fill((22, 2, 66), (24, 2, 72), S),
    # Crossed green and yellow staircase
    Block(26, 2, 70, Y),
    Block(26, 2, 72, G),
    Block(28, 3, 70, G),
    Block(28, 3, 72, Y),
    # Solid bridge
    *fill((30, 4, 70), (32, 4, 76), S),
    # Crossed green and yellow bridge
    *fill((30, 4, 78), (30, 4, 80), Y),
    *fill((32, 4, 78), (32, 4, 80), G),
    *fill((30, 4, 82), (30, 4, 84), G),
    *fill((32, 4, 82), (32, 4, 84), Y),
    # Solid square
    *fill((30, 4, 86), (32, 4, 88), S),
    # Solid block atop pyramid
    Block(31, 8, 99, S),
]


MISSION_1_BLOCKS = [
    *BASE_BLOCKS,
    # Flipping square - Yellow
    *fill((-8, 1.5, 54), (-6, 1.5, 56), Y),
    # Comet Medal bridge
    *fill((10, 2, 72), (12, 2, 72), Y),
    *fill((14, 2, 72), (16, 2, 72), G),
    # Single wall pyramid
    *pyramid((31, 8, 99), 1),
]

MISSION_2_BLOCKS = [
    # Flipping square - Green
    *fill((-8, 1.5, 54), (-6, 1.5, 56), G),
    *BASE_BLOCKS,
    # Full pyramid
    *[block for face in full_pyramid((31, 8, 99), 10) for block in face],
]
