from pathlib import Path

import ffmpeg

from time_lapse import output, source, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    ('/Volumes/Jedi/Cache/250113_APL_Duo_Niepold_Cutting/250113_APL_1_a/*.tif', 48),  # APL_250144 - APL_250339
    ('/Volumes/Jedi/Cache/250113_APL_Duo_Niepold_Cutting/250113_APL_2/*.tif', 24),  # APL_250653 - APL_250757
    ('/Volumes/Jedi/Cache/250113_APL_Duo_Niepold_Cutting/250113_APL_1_b/*.tif', 48),  # APL_250340 - APL_250645
]
POSTER = '/Volumes/Jedi/Cache/250113_APL_Duo_Niepold_Cutting/250113_APL_1_a/APL_250169.tif'


if __name__ == '__main__':
    inputs = [
        source.get_input(pattern, fps=framerate, deflicker=0, filters=None) for pattern, framerate in PATTERNS
    ]
    combined_inputs = ffmpeg.concat(*inputs)
    output.create_outputs(combined_inputs, NAME, framerate=48, watermark=True, verbose=False, dryrun=False)

    thumbnail.create_thumbnail(NAME, Path(POSTER))
