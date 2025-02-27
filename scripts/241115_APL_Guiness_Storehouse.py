from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/241115_APL_3_4_5/241115_APL_3/*.tif',  # APL_244761 - APL_244969
    '/Volumes/Jedi/Cache/241115_APL_3_4_5/241115_APL_5/*.tif',  # APL_245510 - APL_245777
    '/Volumes/Jedi/Cache/241115_APL_3_4_5/241115_APL_4/*.tif',  # APL_244975 - APL_245502
]
POSTER = '/Volumes/Jedi/Cache/241115_APL_3_4_5/241115_APL_5/APL_245773.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 30, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
