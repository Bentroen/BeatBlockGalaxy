from beet import Context
from pigstep import pigstep


def beet_default(ctx: Context) -> None:

    ctx.require(
        pigstep(
            load=["songs/beatblock.nbs"],
            source="record",
            templates={
                "play": "start.mcfunction",
                "pause": "pause.mcfunction",
                "stop": "stop.mcfunction",
                "tick": "tick.mcfunction",
            },
        )
    )
