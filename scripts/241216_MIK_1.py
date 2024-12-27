from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERN = '/Volumes/Jedi/Cache/241216_MIK_1/*.tif'  # MIK_021927 - MIK_023911
POSTER = '/Volumes/Jedi/Cache/241216_MIK_1/MIK_022137.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 48, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
