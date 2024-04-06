from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERN = '/Volumes/Twin suns/220514_APL_3/*.tif'  # APL_111046 - APL_111236
POSTER = '/Volumes/Twin suns/220514_APL_3/APL_111100.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 30, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
