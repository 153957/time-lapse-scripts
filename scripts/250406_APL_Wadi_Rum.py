from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/250402_APL_Jordan/250406_APL_1/*.tif',  # APL_265627 - APL_266032
    '/Volumes/Jedi/Cache/250402_APL_Jordan/250406_APL_2/*.tif',  # APL_266035 - APL_266261
    '/Volumes/Jedi/Cache/250402_APL_Jordan/250407_APL_1/*.tif',  # APL_267765 - APL_268375
    '/Volumes/Jedi/Cache/250402_APL_Jordan/250407_APL_2/*.tif',  # APL_268421 - APL_268763
    '/Volumes/Jedi/Cache/250402_APL_Jordan/250407_APL_3/*.tif',  # APL_268770 - APL_269048
]
POSTER = '/Volumes/Jedi/Cache/250402_APL_Jordan/250407_APL_1/APL_267765.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 30, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
