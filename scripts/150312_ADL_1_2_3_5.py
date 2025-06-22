from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/150312_School/150312_ADL_1/*.tif',  # ADL_177458 - ADL_177681
    '/Volumes/Jedi/Cache/150312_School/150312_ADL_2/*.tif',  # ADL_177695 - ADL_177832
    '/Volumes/Jedi/Cache/150312_School/150312_ADL_5/*.tif',  # ADL_178393 - ADL_178423
    '/Volumes/Jedi/Cache/150312_School/150312_ADL_3/*.tif',  # ADL_177897 - ADL_178329
]
POSTER = '/Volumes/Jedi/Cache/150312_School/150312_ADL_3/ADL_178202.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 24, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
