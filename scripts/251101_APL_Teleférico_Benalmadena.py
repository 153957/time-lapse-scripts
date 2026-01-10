from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERN = '/Volumes/Jedi/Cache/251101_APL_Teleférico_Benalmadena/*.tif'  # APL_321376 - APL_322183
POSTER = '/Volumes/Jedi/Cache/251101_APL_Teleférico_Benalmadena/APL_321868.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 60, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
