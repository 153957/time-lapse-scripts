from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/120827_ADL_Europalaan/120827_ADL_1/*.tif',  # ADL_114227 - ADL_114643
    '/Volumes/Jedi/Cache/120827_ADL_Europalaan/120827_ADL_3/*.tif',  # ADL_114893 - ADL_115129
    '/Volumes/Jedi/Cache/120827_ADL_Europalaan/120827_ADL_2/*.tif',  # ADL_114644 - ADL_114892
]
POSTER = '/Volumes/Jedi/Cache/120827_ADL_Europalaan/120827_ADL_3/ADL_115113.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 30, 4, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
