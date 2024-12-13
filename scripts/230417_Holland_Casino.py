from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/230417_Holland_Casino/230417_ADL_1/*.tif',  # ADL_282349 - ADL_282826
    '/Volumes/Jedi/Cache/230417_Holland_Casino/230417_APL_2_1/*.tif',  # APL_155371 - APL_155590
    '/Volumes/Jedi/Cache/230417_Holland_Casino/230417_ADL_2/*.tif',  # ADL_282830 - ADL_283315
    '/Volumes/Jedi/Cache/230417_Holland_Casino/230417_APL_2_2/*.tif',  # APL_155591 - APL_156156
    '/Volumes/Jedi/Cache/230417_Holland_Casino/230417_APL_2_3/*.tif',  # APL_156432 - APL_156540
    '/Volumes/Jedi/Cache/230417_Holland_Casino/230417_ADL_3/*.tif',  # ADL_283318 - ADL_283765
]
POSTER = '/Volumes/Jedi/Cache/230417_Holland_Casino/230417_APL_2_1/APL_155555.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 48, 0, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
