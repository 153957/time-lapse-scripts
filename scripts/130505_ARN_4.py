from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERN = '/Volumes/Twin suns/130505_ARN_4/*.tif'  # ARN_045762 - ARN_046211
POSTER = '/Volumes/Twin suns/130505_ARN_4/ARN_045770.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 48, 5, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
