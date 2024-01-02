from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERN = '/Volumes/Twin suns/240101_APL_1/*.tif'  # APL_208575 - APL_209217
POSTER = '/Volumes/Twin suns/240101_APL_1/APL_208896.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 30, 0, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
