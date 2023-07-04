from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/221026_APL_1/*.tif',  # APL_140728 - APL_140947
    '/Volumes/Jedi/Cache/221026_APL_2/*.tif',  # APL_140949 - APL_141141
    '/Volumes/Jedi/Cache/221026_APL_3/*.tif',  # APL_141150 - APL_141474
]
POSTER = 'APL_141404.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 24, 0, watermark=True, verbose=False, dryrun=False)
