import importlib

from . import map_data as map
from . import model

from beet import Context, Function, FunctionTag


def beet_default(ctx: Context) -> None:

    model.generate(ctx)

    importlib.reload(map)

    # Set up tick and load functions
    ctx.data["minecraft:load"] = FunctionTag({"values": ["beatblock:load"]})
    # ctx.data["minecraft:tick"] = FunctionTag({"values": ["beatblock:tick"]})

    load_function = Function()

    # Remove The Void platform
    load_function.append("fill -8 -61 -8 24 -61 24 air")
    load_function.append("say hi")

    # Reset existing blocks
    load_function.append(
        "execute as @e[type=armor_stand,tag=block] at @s run fill ~ ~ ~ ~1 ~-1 ~1 air"
    )
    load_function.append("kill @e[type=minecraft:armor_stand,tag=block]")

    load_function.append("from ./spawn_block import spawn_block, spawn_block_solid")

    swizzle = lambda x: x[::-1]  # invert Z and X coordinates
    for block in map.MISSION_2_BLOCKS:
        if block.type == map.BlockType.SOLID:
            command = "spawn_block_solid({}, {}, {})".format(*swizzle(block.coords))
        elif block.type == map.BlockType.BEAT_GREEN:
            command = "spawn_block({}, {}, {}, {})".format(*swizzle(block.coords), 5)
            # command = "setblock {} {} {} emerald_block".format(*swizzle(block.coords))
        elif block.type == map.BlockType.BEAT_YELLOW:
            command = "spawn_block({}, {}, {}, {})".format(*swizzle(block.coords), 2)
        load_function.append(command)

    ctx.data["beatblock:load_map"] = load_function
