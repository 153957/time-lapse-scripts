from pathlib import Path

import ffmpeg

from time_lapse import output, source, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    ('/Volumes/Jedi/Cache/230601_Edinburgh/230601_2/*.tif', 60),  # APL_170603 - APL_171399
    ('/Volumes/Jedi/Cache/230601_Edinburgh/230601_6/*.tif', 30),  # APL_171722 - APL_171921
    ('/Volumes/Jedi/Cache/230601_Edinburgh/230601_7/*.tif', 30),  # APL_171924 - APL_172152
    ('/Volumes/Jedi/Cache/230601_Edinburgh/230601_3/*.tif', 30),  # APL_171438 - APL_171530
]
POSTER = '/Volumes/Jedi/Cache/230601_Edinburgh/230601_3/APL_171530.tif'


if __name__ == '__main__':
    inputs = [source.get_input(pattern, fps=framerate, deflicker=3, filters=None) for pattern, framerate in PATTERNS]
    output.create_outputs(ffmpeg.concat(*inputs), NAME, framerate=24, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
