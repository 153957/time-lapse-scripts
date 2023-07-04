from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERN = '/Volumes/Chiss/Archive/Time-Lapse/220130_2_APL/*.tif'  # APL_098953 - APL_099267
POSTER = 'APL_099267.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 30, 2, watermark=True, verbose=False, dryrun=False)
