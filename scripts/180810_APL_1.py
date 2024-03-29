from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERN = '/Volumes/Sith/Store_elsewhere/Falcon/Time-Lapse/180810_APL_1/*.tif'  # APL_033321 - APL_033801
POSTER = 'APL_033611.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 30, 2, watermark=True, verbose=False, dryrun=False)
