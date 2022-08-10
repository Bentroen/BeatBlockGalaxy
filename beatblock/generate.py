import importlib

from . import map_data

from beet import Context, Function, FunctionTag, Model


def beet_default(ctx: Context) -> None:

    importlib.reload(map_data)

    # Set up tick and load functions
    ctx.data["minecraft:load"] = FunctionTag({"values": ["beatblock:load"]})
    # ctx.data["minecraft:tick"] = FunctionTag({"values": ["beatblock:tick"]})

    load_function = Function()

    # Remove The Void platform
    load_function.append("fill -8 -61 -8 24 -61 24 air")
    load_function.append("say hi")

    swizzle = lambda x: x[::-1]  # invert Z and X coordinates
    for block in map_data.SOLID:
        load_function.append(
            "setblock {} {} {} minecraft:purpur_block".format(*swizzle(block))
        )
    for block in map_data.BEAT_GREEN:
        load_function.append(
            "setblock {} {} {} minecraft:emerald_block".format(*swizzle(block))
        )
    for block in map_data.BEAT_YELLOW:
        load_function.append(
            "setblock {} {} {} minecraft:gold_block".format(*swizzle(block))
        )

    ctx.data["beatblock:load"] = load_function
