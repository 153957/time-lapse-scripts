from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/140608_ADL_Slot_Zeist/140608_ADL_1/*.tif',  # ADL_158764 - ADL_158905
    '/Volumes/Jedi/Cache/140608_ADL_Slot_Zeist/140608_ADL_2/*.tif',  # ADL_158926 - ADL_159075
]
POSTER = '/Volumes/Jedi/Cache/140608_ADL_Slot_Zeist/140608_ADL_2/ADL_158926.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 24, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
