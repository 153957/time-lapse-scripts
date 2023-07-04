from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERN = '/Volumes/Chiss/Temporary/210306_APL_1/APL_*.tif'  # APL_081153 - APL_081520
POSTER = 'APL_081301.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 25, 2, watermark=True, verbose=False, dryrun=False)
