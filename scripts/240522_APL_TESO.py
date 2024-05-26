from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERN = '/Volumes/Jedi/Cache/240522_APL_TESO/*.tif'  # APL_220058 - APL_221205
POSTER = '/Volumes/Jedi/Cache/240522_APL_TESO/APL_220773.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 48, 4, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
