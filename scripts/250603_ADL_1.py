from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERN = '/Volumes/Jedi/Cache/250603_ADL_1/*.tif'  # ADL_300227 - ADL_301053
POSTER = '/Volumes/Jedi/Cache/250603_ADL_1/ADL_300640.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 30, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
