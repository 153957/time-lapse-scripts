from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERN = '/Volumes/Jedi/Cache/210113_WEN_1/*.tif'  # WEN_061172 - WEN_061976
POSTER = '/Volumes/Jedi/Cache/210113_WEN_1/WEN_061188.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 48, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
