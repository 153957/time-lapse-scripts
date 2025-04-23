from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERN = '/Volumes/Jedi/Cache/110912_ADL_1/*.tif'  # D700_110912_211105 - D700_110912_220541
POSTER = '/Volumes/Jedi/Cache/110912_ADL_1/D700_110912_211105.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 24, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
