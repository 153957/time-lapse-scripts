from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/250402_APL_Jordan/250406_APL_3/*.tif',  # APL_266294 - APL_266546
    '/Volumes/Jedi/Cache/250402_APL_Jordan/250406_APL_4/*.tif',  # APL_266552 - APL_266863
]
POSTER = '/Volumes/Jedi/Cache/250402_APL_Jordan/250406_APL_3/APL_266294.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 24, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
