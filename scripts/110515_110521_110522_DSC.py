from pathlib import Path

import ffmpeg

from time_lapse import output

NAME = Path(__file__).stem
PATTERNS = [
    ('/Volumes/Archive/tl_temp/D80_110522_1/*.tiff', 48),  # DSC_163723 - DSC_164490
    ('/Volumes/Archive/tl_temp/D80_110522_2/*.tiff', 48),  # DSC_164783 - DSC_165480
    ('/Volumes/Archive/tl_temp/D80_110521_4/*.tiff', 24),  # DSC_162504 - DSC_162918
    ('/Volumes/Archive/tl_temp/D80_110521_2/*.tiff', 24),  # DSC_162181 - DSC_162301
    ('/Volumes/Archive/tl_temp/D80_110515_3/*.tiff', 24),  # DSC_158888 - DSC_159150
]


def create_movie() -> None:
    inputs = [
        ffmpeg.input(pattern, pattern_type='glob', framerate=rate).filter_('deflicker', mode='pm', size=10)
        for pattern, rate in PATTERNS
    ]
    combined_inputs = ffmpeg.concat(*inputs)

    output.create_outputs(combined_inputs, NAME, verbose=True, framerate=48)


if __name__ == '__main__':
    create_movie()
