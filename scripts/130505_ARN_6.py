from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERN = '/Volumes/Jedi/Cache/130505_ARN_6/*.tif'  # ARN_046391 - ARN_046862
POSTER = '/Volumes/Jedi/Cache/130505_ARN_6/ARN_046640.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 30, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
