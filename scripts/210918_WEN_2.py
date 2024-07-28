from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERN = '/Volumes/Jedi/Cache/210918_WEN_2/*.tif'  # WEN_063505 - WEN_064486
POSTER = '/Volumes/Jedi/Cache/210918_WEN_2/WEN_063888.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 30, 7, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
