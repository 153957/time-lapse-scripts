from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERN = '/Volumes/Jedi/Cache/210918_WEN_1/*.tif'  # WEN_062601 - WEN_063468
POSTER = '/Volumes/Jedi/Cache/210918_WEN_1/WEN_062601.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 30, 7, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
