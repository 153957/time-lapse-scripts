from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERN = '/Volumes/Chiss/Archive/Time-Lapse/201118_3_APL/*.tif'  # APL_077370 - APL_078182
POSTER = 'APL_077399.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 30, 0, watermark=True, verbose=False, dryrun=False)
