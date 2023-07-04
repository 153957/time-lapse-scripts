from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Sith/Store_elsewhere/Falcon/Time-Lapse/171119_APL_3/*.tif',  # APL_010583 - APL_010757
    '/Volumes/Sith/Store_elsewhere/Falcon/Time-Lapse/171119_APL_2/*.tif',  # APL_009696 - APL_010553
]
POSTER = 'APL_009714.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 25, 2, watermark=True, verbose=False, dryrun=False)
