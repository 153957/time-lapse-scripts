from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERN = '/Volumes/Jedi/Cache/250402_APL_Jordan/250408_APL_1/*.tif'  # APL_269183 - APL_270186
POSTER = '/Volumes/Jedi/Cache/250402_APL_Jordan/250408_APL_1/APL_269330.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 48, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
