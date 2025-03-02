from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/230531_APL_Stramash/230531_APL_Stramash_1/*.tif',  # APL_168681 - APL_169237
    '/Volumes/Jedi/Cache/230531_APL_Stramash/230531_APL_Stramash_2/*.tif',  # APL_169243 - APL_169987
]
POSTER = '/Volumes/Jedi/Cache/230531_APL_Stramash/230531_APL_Stramash_2/APL_169951.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 24, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
