from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERN = '/Volumes/Jedi/Cache/220517_APL_1/*.tif'  # APL_112805 - APL_113025
POSTER = 'APL_112805.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 25, 2, watermark=True, verbose=False, dryrun=False)
