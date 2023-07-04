from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERN = '/Volumes/Crimson/Cache/230424_APL_Villa_Carlos_Paz/*.tif'  # APL_159625 - APL_160054
POSTER = 'APL_159625.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 24, 3, watermark=True, verbose=False, dryrun=False)
