import importlib

from . import map_data as map

from beet import Context, Function, FunctionTag, Model


def beet_default(ctx: Context) -> None:

    importlib.reload(map)

    # Set up tick and load functions
    ctx.data["minecraft:load"] = FunctionTag({"values": ["beatblock:load"]})
    # ctx.data["minecraft:tick"] = FunctionTag({"values": ["beatblock:tick"]})

    load_function = Function()

    # Remove The Void platform
    load_function.append("fill -8 -61 -8 24 -61 24 air")
    load_function.append("say hi")

    swizzle = lambda x: x[::-1]  # invert Z and X coordinates
    for block in map.BLOCKS:
        if block.type == map.BlockType.SOLID:
            command = "setblock {} {} {} purpur_block".format(*swizzle(block.coords))
        elif block.type == map.BlockType.BEAT_GREEN:
            command = "setblock {} {} {} emerald_block".format(*swizzle(block.coords))
        elif block.type == map.BlockType.BEAT_YELLOW:
            command = "setblock {} {} {} gold_block".format(*swizzle(block.coords))
        load_function.append(command)

    ctx.data["beatblock:load"] = load_function
