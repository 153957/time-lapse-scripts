from pathlib import Path

import ffmpeg

from time_lapse import output

NAME = Path(__file__).stem
PATTERNS = [
    ('/Volumes/Falcon/tl_temp/120524/D90_1/*.tiff', 48),  # ARN_003613 - ARN_004715
    ('/Volumes/Falcon/tl_temp/120524/D700_1/*.tiff', 24),  # ADL_101173 - ADL_102042
    ('/Volumes/Falcon/tl_temp/120524/D90_2/*.tiff', 48),  # ARN_004855 - ARN_005341
    ('/Volumes/Falcon/tl_temp/120524/D90_3/*.tiff', 24),  # ARN_005342 - ARN_005515
    ('/Volumes/Falcon/tl_temp/120524/D90_4/*.tiff', 48),  # ARN_005520 - ARN_005983
    ('/Volumes/Falcon/tl_temp/120524/D700_2/*.tiff', 24),  # ADL_102058 - ADL_102240
]


def create_movie() -> None:
    inputs = [
        ffmpeg.input(pattern, pattern_type='glob', framerate=framerate).filter_('deflicker', mode='pm', size=10)
        for pattern, framerate in PATTERNS
    ]
    combined_inputs = ffmpeg.concat(*inputs)

    output.create_outputs(combined_inputs, NAME, verbose=True, framerate=48)


if __name__ == '__main__':
    create_movie()
