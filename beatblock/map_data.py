# This module stores the positions for all blocks in the Beat Block Galaxy.

from enum import Enum


class BlockType(Enum):
    SOLID = 1
    BEAT_GREEN = 2
    BEAT_YELLOW = 3


S = BlockType.SOLID
G = BlockType.BEAT_GREEN
Y = BlockType.BEAT_YELLOW


BLOCKS = {
    # Starting bridge
    (0, 0, 0): S,
    (2, 0, 0): S,
    (0, 0, 2): S,
    (2, 0, 2): S,
    (0, 0, 4): S,
    (2, 0, 4): S,
    (0, 0, 6): S,
    (2, 0, 6): S,
    (0, 0, 8): S,
    # 2 green to the right
    (2, 0, 8): G,
    (2, 0, 10): G,
    # 2 yellow to the left
    (0, 0, 12): Y,
    (0, 0, 14): Y,
    # Solid square
    (0, 0, 10): S,
    (2, 0, 12): S,
    (2, 0, 14): S,
    (0, 0, 16): S,
    (2, 0, 16): S,
    (0, 0, 18): S,
    (2, 0, 18): S,
    # Green row
    (2, 0, 20): S,
    (2, 0, 22): S,
    (2, 0, 24): S,
    (2, 0, 26): S,
    # Yellow row
    (0, 0, 20): Y,
    (0, 0, 22): Y,
    (0, 0, 24): Y,
    (0, 0, 26): Y,
    # Solid square
    (0, 0, 28): S,
    (2, 0, 28): S,
    (0, 0, 30): S,
    (2, 0, 30): S,
}
