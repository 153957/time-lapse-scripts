from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/221028_APL_10/*.tif',  # APL_144487 - APL_144807
    '/Volumes/Jedi/Cache/221028_APL_11/*.tif',  # APL_144857 - APL_144977
]
# poster: APL_144857


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 24, 2, watermark=True, verbose=False, dryrun=False)
