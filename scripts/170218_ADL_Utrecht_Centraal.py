from pathlib import Path

import ffmpeg

from time_lapse import output

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Archive/tl_temp/D700_170218/2/*.tiff',  # ADL_233232 - ADL_233465
    '/Volumes/Archive/tl_temp/D700_170218/3/*.tiff',  # ADL_233510 - ADL_233465
    '/Volumes/Archive/tl_temp/D700_170218/1/*.tiff',  # ADL_233050 - ADL_233216
]


def create_movie() -> None:
    inputs = [
        ffmpeg.input(pattern, pattern_type='glob', framerate=24).filter_('deflicker', mode='pm', size=5)
        for pattern in PATTERNS
    ]
    combined_inputs = ffmpeg.concat(*inputs)

    output.create_outputs(combined_inputs, NAME, verbose=True)


if __name__ == '__main__':
    create_movie()
