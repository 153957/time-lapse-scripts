from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERN = '/Volumes/Jedi/Cache/230527_APL_1/*.tif'  # APL_162781 - APL_162941
POSTER = '/Volumes/Jedi/Cache/230527_APL_1/APL_162937.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 48, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
