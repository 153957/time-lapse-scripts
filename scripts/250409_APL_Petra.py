from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/250402_APL_Jordan/250409_APL_1/*.tif',  # APL_270643 - APL_271070
    '/Volumes/Jedi/Cache/250402_APL_Jordan/250409_APL_2/*.tif',  # APL_271082 - APL_271346
    '/Volumes/Jedi/Cache/250402_APL_Jordan/250409_APL_3/*.tif',  # APL_271736 - APL_272008
    '/Volumes/Jedi/Cache/250402_APL_Jordan/250409_APL_4/*.tif',  # APL_272019 - APL_272241
    '/Volumes/Jedi/Cache/250402_APL_Jordan/250409_APL_5/*.tif',  # APL_272520 - APL_273150
    '/Volumes/Jedi/Cache/250402_APL_Jordan/250409_APL_6/*.tif',  # APL_273161 - APL_273545
    '/Volumes/Jedi/Cache/250402_APL_Jordan/250409_APL_7/*.tif',  # APL_273649 - APL_274432
]
POSTER = '/Volumes/Jedi/Cache/250402_APL_Jordan/250409_APL_7/APL_273982.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 30, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
