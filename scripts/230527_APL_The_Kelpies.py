from pathlib import Path

import ffmpeg

from time_lapse import output, source, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    ('/Volumes/Crimson/Cache/230527_The Kelpies/230527_15/*.tif', 24),  # APL_165429 - APL_165918
    ('/Volumes/Crimson/Cache/230527_The Kelpies/230527_17/*.tif', 48),  # APL_166036 - APL_167103
    ('/Volumes/Crimson/Cache/230527_The Kelpies/230527_18/*.tif', 24),  # APL_167122 - APL_167298
    ('/Volumes/Crimson/Cache/230527_The Kelpies/230527_20/*.tif', 24),  # APL_167426 - APL_167853
    ('/Volumes/Crimson/Cache/230527_The Kelpies/230527_21/*.tif', 24),  # APL_167858 - APL_168312
    ('/Volumes/Crimson/Cache/230527_The Kelpies/230527_22/*.tif', 24),  # APL_168318 - APL_168479
    ('/Volumes/Crimson/Cache/230527_The Kelpies/230527_19/*.tif', 24),  # APL_167309 - APL_167420
]
POSTER = '/Volumes/Crimson/Cache/230527_The Kelpies/230527_22/APL_168338.tif'


if __name__ == '__main__':
    inputs = [
        source.get_input(pattern, fps=framerate, deflicker=3, filters=None)
        for pattern, framerate in PATTERNS
    ]
    output.create_outputs(ffmpeg.concat(*inputs), NAME, framerate=24, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
