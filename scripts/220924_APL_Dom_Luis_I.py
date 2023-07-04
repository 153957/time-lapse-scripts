from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERN = '/Volumes/Jedi/Cache/220924_Porto/220924_Porto_7_Dom_Luís_Bridge/*.tif'  # APL_129740 - APL_129939
POSTER = 'APL_129772.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 24, 3, watermark=True, verbose=False, dryrun=False)
