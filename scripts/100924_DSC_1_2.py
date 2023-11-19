from pathlib import Path

import ffmpeg

from time_lapse import output

NAME = Path(__file__).stem
PATTERN1 = '/Volumes/Falcon/tl_temp/100924_1/*.tiff'
PATTERN2 = '/Volumes/Falcon/tl_temp/100924_2/*.tiff'


def create_movie() -> None:
    input1 = ffmpeg.input(PATTERN1, pattern_type='glob', framerate=24).filter_('deflicker', mode='pm', size=10)
    input2 = ffmpeg.input(PATTERN2, pattern_type='glob', framerate=48).filter_('deflicker', mode='pm', size=10)
    combined_inputs = ffmpeg.concat(input1, input2)

    output.create_outputs(combined_inputs, NAME, framerate=48, verbose=True)


if __name__ == '__main__':
    create_movie()
