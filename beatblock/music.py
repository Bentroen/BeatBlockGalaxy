import os
from pathlib import Path
from beet import Context
from pigstep import pigstep

import pynbs


def beet_default(ctx: Context) -> None:

    song = pynbs.read(Path("songs", "beatblock.nbs"))

    # Set instrument name to sound event name (pigstep uses the sound file field as the sound event)
    for ins in song.instruments:
        new_ins = pynbs.Instrument(
            id=ins.id,
            name=ins.name,
            file=ins.name,
            pitch=ins.pitch,
            press_key=ins.press_key,
        )
        song.instruments[ins.id] = new_ins

    temp_songs_path = Path("songs", ".temp")
    if not os.path.exists(temp_songs_path):
        os.makedirs(temp_songs_path)

    filename = Path(temp_songs_path, "beatblock.nbs")
    song.save(filename)

    ctx.require(
        pigstep(
            load=[str(filename)],
            source="record",
            templates={
                "play": "start.mcfunction",
                "pause": "pause.mcfunction",
                "stop": "stop.mcfunction",
                "tick": "tick.mcfunction",
            },
        )
    )

    for name, func in ctx.data.functions.items():
        if "song" in name:
            for i, line in enumerate(func.lines):
                if line.strip().startswith("playsound"):
                    if "FLASH" in line:
                        func.lines[i] = "function beatblock:flash"
                    elif "SWITCH" in line:
                        func.lines[i] = "function beatblock:switch"
