from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERN = '/Volumes/Jedi/Cache/250503_APL_1/*.tif'  # APL_279651 - APL_280728
POSTER = '/Volumes/Jedi/Cache/250503_APL_1/APL_279991.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 48, 5, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
