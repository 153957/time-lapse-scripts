from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Falcon/tl_temp/160813_1_Boot/*.tiff',  # ADL_216004 - ADL_216758
    '/Volumes/Falcon/tl_temp/160813_2_Boot/*.tiff',  # ADL_216765 - ADL_217317
]
POSTER = 'ADL_216065.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 30, 3, watermark=True, verbose=False, dryrun=False)
