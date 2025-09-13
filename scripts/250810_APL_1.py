from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERN = '/Volumes/Jedi/Cache/250810_APL_1/*.tif'  # APL_298365 - APL_298541
POSTER = '/Volumes/Jedi/Cache/250810_APL_1/APL_298432.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 24, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
