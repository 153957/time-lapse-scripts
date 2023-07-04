from pathlib import Path

import ffmpeg

from time_lapse import output

NAME = Path(__file__).stem
PATTERN1 = '/Volumes/Falcon/tl_temp/120506_1/*.tiff'
PATTERN2 = '/Volumes/Falcon/tl_temp/120506_2/*.tiff'


def create_movie() -> None:
    input1 = (
        ffmpeg
        .input(PATTERN1, pattern_type='glob', framerate=48)
        .filter_('deflicker', mode='pm', size=10)
        .filter_('scale', size='hd1080', force_original_aspect_ratio='increase')
    )
    input2 = (
        ffmpeg
        .input(PATTERN2, pattern_type='glob', framerate=48)
        .filter_('deflicker', mode='pm', size=10)
    )
    combined_inputs = ffmpeg.concat(input1, input2)

    output.create_outputs(combined_inputs, NAME, verbose=True)


if __name__ == '__main__':
    create_movie()
