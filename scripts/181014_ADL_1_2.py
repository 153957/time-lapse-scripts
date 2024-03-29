from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Falcon/tl_temp/181014/1/*.tiff',  # ADL_244715 - ADL_244857
    '/Volumes/Falcon/tl_temp/181014/2/*.tiff',  # ADL_244862 - ADL_245077
]


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 24, 10, watermark=True, verbose=False, dryrun=False)
