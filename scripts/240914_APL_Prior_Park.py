from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/240914_Prior_Park/240914_APL_1/*.tif',  # APL_237355 - APL_237502
    '/Volumes/Jedi/Cache/240914_Prior_Park/240914_APL_5/*.tif',  # APL_238163 - APL_238292
    '/Volumes/Jedi/Cache/240914_Prior_Park/240914_APL_2/*.tif',  # APL_237513 - APL_237754
    '/Volumes/Jedi/Cache/240914_Prior_Park/240914_APL_3/*.tif',  # APL_237758 - APL_238012
]
POSTER = '/Volumes/Jedi/Cache/240914_Prior_Park/240914_APL_3/APL_237758.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 24, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
