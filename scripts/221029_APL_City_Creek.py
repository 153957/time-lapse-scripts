from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Crimson/Cache/221029_City Creek/221029_1/*.tif',  # APL_145227 - APL_145447
    '/Volumes/Crimson/Cache/221029_City Creek/221029_2/*.tif',  # APL_145463 - APL_145682
    '/Volumes/Crimson/Cache/221029_City Creek/221029_3/*.tif',  # APL_145701 - APL_145979
]
POSTER = 'APL_145227.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 48, 2, watermark=True, verbose=False, dryrun=False)
