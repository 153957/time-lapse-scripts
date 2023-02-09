from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Falcon/tl_temp/180901/1/*.tiff',  # ADL_242138 - ADL_242499
    '/Volumes/Falcon/tl_temp/180901/2/*.tiff',  # ADL_242506 - ADL_243212
]


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 10, 2, watermark=True, verbose=False, dryrun=False)
