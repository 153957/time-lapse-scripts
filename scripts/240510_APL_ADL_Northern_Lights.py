from pathlib import Path

import ffmpeg

from time_lapse import output, source, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    ('/Volumes/Jedi/Cache/240510_Aurora/APL_1/*.tif', 12, 2),  # APL_216574 - APL_216598
    ('/Volumes/Jedi/Cache/240510_Aurora/APL_2/*.tif', 24, 2),  # APL_216610 - APL_216917
    ('/Volumes/Jedi/Cache/240510_Aurora/APL_3/*.tif', 24, 4),  # APL_216921 - APL_217044
    ('/Volumes/Jedi/Cache/240510_Aurora/ADL_1/*.tif', 24, 0),  # ADL_289448 - ADL_289527
    ('/Volumes/Jedi/Cache/240510_Aurora/APL_4/*.tif', 48, 4),  # APL_217050 - APL_217571
    ('/Volumes/Jedi/Cache/240510_Aurora/APL_5/*.tif', 48, 0),  # APL_217575 - APL_217934
]
POSTER = '/Volumes/Jedi/Cache/240510_Aurora/ADL_1/ADL_289449.tif'


if __name__ == '__main__':
    inputs = [
        source.get_input(pattern, fps=framerate, deflicker=size, filters=None)
        for pattern, framerate, size in PATTERNS
    ]
    combined_inputs = ffmpeg.concat(*inputs)
    output.create_outputs(combined_inputs, NAME, framerate=48, watermark=True, verbose=False, dryrun=False)

    thumbnail.create_thumbnail(NAME, Path(POSTER))
