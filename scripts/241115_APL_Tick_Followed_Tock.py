from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/241115_APL_1/241115_APL_1/*.tif',  # APL_244457 - APL_244588
    '/Volumes/Jedi/Cache/241115_APL_1/241115_APL_2/*.tif',  # APL_244591 - APL_244746
]
POSTER = '/Volumes/Jedi/Cache/241115_APL_1/241115_APL_2/APL_244604.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 24, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
