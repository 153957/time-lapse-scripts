from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Chiss/Archive/Time-Lapse/220219_1_APL/*.tif',  # APL_099992 - APL_100107
    '/Volumes/Chiss/Archive/Time-Lapse/220219_4_APL/*.tif',  # APL_100698 - APL_101023
]
POSTER = 'APL_100698.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 30, 3, watermark=True, verbose=False, dryrun=False)
