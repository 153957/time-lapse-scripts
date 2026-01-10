from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/260104_APL_Soestduinen/260104_APL_1/*.tif',  # APL_341940 - APL_342276
    '/Volumes/Jedi/Cache/260104_APL_Soestduinen/260104_APL_2/*.tif',  # APL_342287 - APL_343036
]
POSTER = '/Volumes/Jedi/Cache/260104_APL_Soestduinen/260104_APL_1/APL_342185.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 30, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
