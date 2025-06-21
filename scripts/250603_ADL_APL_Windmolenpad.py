from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/250603_APL_1/*.tif',  # APL_289053 - APL_289625
    '/Volumes/Jedi/Cache/250603_APL_2/*.tif',  # APL_290155 - APL_290780
    '/Volumes/Jedi/Cache/250603_ADL_2/*.tif',  # ADL_301070 - ADL_301717
    '/Volumes/Jedi/Cache/250603_ADL_3/*.tif',  # ADL_302077 - ADL_302407
    '/Volumes/Jedi/Cache/250603_APL_3/*.tif',  # APL_291178 - APL_291726
    '/Volumes/Jedi/Cache/250603_ADL_4/*.tif',  # ADL_302411 - ADL_302963
]
POSTER = '/Volumes/Jedi/Cache/250603_APL_3/APL_291476.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 30, 5, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
