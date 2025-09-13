from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/250907_ADL_Vleutensebaan/250907_ADL_1/*.tif',  # ADL_303050 - ADL_303281
    '/Volumes/Jedi/Cache/250907_ADL_Vleutensebaan/250907_ADL_2/*.tif',  # ADL_303284 - ADL_303608
]
POSTER = '/Volumes/Jedi/Cache/250907_ADL_Vleutensebaan/250907_ADL_2/ADL_303322.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 30, 8, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
