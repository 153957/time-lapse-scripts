from pathlib import Path

import ffmpeg

from time_lapse import output, source

NAME = Path(__file__).stem
PATTERN1 = '/Volumes/Jedi/Cache/220401_1_skydive/*.tif'  # APL_104104 - APL_104314
PATTERN2 = '/Volumes/Jedi/Cache/220401_6_skydive/*.tif'  # APL_105404 - APL_106184
POSTER = 'APL_105558.tif'

if __name__ == '__main__':
    input1 = (
        source
        .get_input(PATTERN1, 24, 0, None)
    )

    input2 = (
        source
        .get_input(PATTERN2, 24, 0, None)
        .filter_('tblend', all_mode='darken', all_opacity=0.33)
        .filter_('tblend', all_mode='darken', all_opacity=0.33)
    )

    inputs = ffmpeg.concat(input1, input2)

    output.create_outputs(inputs, NAME, watermark=True, verbose=False, dryrun=False)
