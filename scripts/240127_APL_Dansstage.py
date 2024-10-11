from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/240127_Dansstage/240127_APL_1/*.tif',  # APL_211248 - APL_211378
    '/Volumes/Jedi/Cache/240127_Dansstage/240127_APL_2/*.tif',  # APL_211385 - APL_211578
]
POSTER = '/Volumes/Jedi/Cache/240127_Dansstage/240127_APL_2/APL_211501.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 24, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
