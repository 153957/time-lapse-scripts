from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/250907_Graffiti/250907_APL_1/*.tif',  # APL_308007 - APL_308423
    '/Volumes/Jedi/Cache/250907_Graffiti/250907_APL_2/*.tif',  # APL_308430 - APL_308727
    '/Volumes/Jedi/Cache/250907_Graffiti/250907_APL_3/*.tif',  # APL_308730 - APL_309335
]
POSTER = '/Volumes/Jedi/Cache/250907_Graffiti/250907_APL_3/APL_309276.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 24, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
