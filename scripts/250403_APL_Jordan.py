from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/250402_APL_Jordan/250403_APL_1/*.tif',  # APL_260777 - APL_261078
    '/Volumes/Jedi/Cache/250402_APL_Jordan/250405_APL_1/*.tif',  # APL_264799 - APL_265000
    '/Volumes/Jedi/Cache/250402_APL_Jordan/250403_APL_3/*.tif',  # APL_261891 - APL_262422
    '/Volumes/Jedi/Cache/250402_APL_Jordan/250403_APL_4/*.tif',  # APL_262469 - APL_262675
    '/Volumes/Jedi/Cache/250402_APL_Jordan/250404_APL_1/*.tif',  # APL_263237 - APL_263787
]
POSTER = '/Volumes/Jedi/Cache/250402_APL_Jordan/250403_APL_1/APL_260777.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 30, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
