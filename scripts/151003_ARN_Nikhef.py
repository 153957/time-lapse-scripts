from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERN = '/Volumes/Jedi/Cache/151003_ARN_Nikhef/*.tif'  # ARN_097717 - ARN_099423
POSTER = '/Volumes/Jedi/Cache/151003_ARN_Nikhef/ARN_098756.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 48, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
