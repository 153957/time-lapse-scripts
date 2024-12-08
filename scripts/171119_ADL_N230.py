from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERN = '/Volumes/Jedi/Cache/171119_ADL_N230/*.tif'  # ADL_239529 - ADL_239710
POSTER = '/Volumes/Jedi/Cache/171119_ADL_N230/ADL_239571.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 24, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
