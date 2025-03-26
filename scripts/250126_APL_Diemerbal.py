from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/250126_Diemerbal/250126_APL_1/*.tif',  # APL_251975 - APL_252364
    '/Volumes/Jedi/Cache/250126_Diemerbal/250126_APL_2/*.tif',  # APL_252367 - APL_252596
]
POSTER = '/Volumes/Jedi/Cache/250126_Diemerbal/250126_APL_1/APL_252343.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 30, 0, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
