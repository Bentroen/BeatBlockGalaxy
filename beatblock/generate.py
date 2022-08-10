import importlib

from . import map_data

from beet import Context, Function, FunctionTag, Model


def beet_default(ctx: Context) -> None:

    importlib.reload(map_data)

    # Set up tick and load functions
    ctx.data["minecraft:load"] = FunctionTag({"values": ["beatblock:load"]})
    # ctx.data["minecraft:tick"] = FunctionTag({"values": ["beatblock:tick"]})

    load_function = Function()

    # function.append("fill 0 ")
    load_function.append("say hi")

    for block in map.SOLID:
        load_function.append("setblock {} {} {} minecraft:purpur_block".format(*block))

    ctx.data["beatblock:load"] = load_function
