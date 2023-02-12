from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERN = '/Volumes/Jedi/Cache/220924_Porto/220925_Porto_1_Via_Catarina/*.tif'  # APL_131728 - APL_131999
# poster: APL_131728


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 24, 3, watermark=True, verbose=False, dryrun=False)
