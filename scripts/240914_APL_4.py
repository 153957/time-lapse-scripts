from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERN = '/Volumes/Jedi/Cache/240914_Prior_Park/240914_APL_4//*.tif'  # APL_238027 - APL_238133
POSTER = '/Volumes/Jedi/Cache/240914_Prior_Park/240914_APL_4/APL_238063.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 24, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
