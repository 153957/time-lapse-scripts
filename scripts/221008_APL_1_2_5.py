from pathlib import Path

import ffmpeg

from time_lapse import output

NAME = Path(__file__).stem
PATTERNS = [
    ('/Volumes/Crimson/Cache/221008_Nijmegen/APL_1/*.tif', 48),  # APL_134754 - APL_135264
    ('/Volumes/Crimson/Cache/221008_Nijmegen/APL_2/*.tif', 12),  # APL_135266 - APL_135384
    ('/Volumes/Crimson/Cache/221008_Nijmegen/APL_5/*.tif', 24),  # APL_135838 - APL_136057
]
# poster: APL_136020


def make_movie():
    inputs = [
        ffmpeg
        .input(pattern, pattern_type='glob', framerate=framerate)
        .filter_('deflicker', mode='pm', size=2)
        for pattern, framerate in PATTERNS
    ]
    input = ffmpeg.concat(*inputs)

    output.create_outputs(input, NAME, verbose=True, framerate=48)


if __name__ == '__main__':
    make_movie()
