from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERN = '/Volumes/Jedi/Cache/110101_DSC_1/*.tif'  # D80_110101_002432 - D80_110101_005106
POSTER = '/Volumes/Jedi/Cache/110101_DSC_1/D80_110101_002936.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 24, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
