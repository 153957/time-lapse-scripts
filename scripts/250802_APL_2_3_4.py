from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/250802_APL_Butterflies/250802_APL_2/*.tif',  # APL_297378 - APL_298014
    '/Volumes/Jedi/Cache/250802_APL_Butterflies/250802_APL_3/*.tif',  # APL_298019 - APL_298164
    '/Volumes/Jedi/Cache/250802_APL_Butterflies/250802_APL_4/*.tif',  # APL_298169 - APL_298319
]
POSTER = '/Volumes/Jedi/Cache/250802_APL_Butterflies/250802_APL_4/APL_298202.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 24, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
