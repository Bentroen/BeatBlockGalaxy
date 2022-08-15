from io import BytesIO
import os
from pathlib import Path
from tempfile import NamedTemporaryFile
from beet import Context
from pigstep import pigstep

import pynbs


def write_song_to_open_file(song: pynbs.File, buff: BytesIO):
    pynbs.Writer(buff).encode_file(song, pynbs.CURRENT_NBS_VERSION)


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

    # tempfile = NamedTemporaryFile()
    # filename = os.path.basename(tempfile.name)
    # write_song_to_open_file(song, tempfile)

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
