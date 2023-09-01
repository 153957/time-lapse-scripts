from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Crimson/Cache/201118_1_ADL/*.tif',  # ADL_273757 - ADL_274224
    '/Volumes/Crimson/Cache/201118_1_APL/*.tif',  # APL_076362 - APL_076961
]
POSTER = '/Volumes/Crimson/Cache/201118_1_APL/APL_076572.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 24, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
