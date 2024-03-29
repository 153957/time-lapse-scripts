from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Sith/Store_elsewhere/Falcon/Time-Lapse/210207_ADL_1/*.tif',  # ADL_276254
    '/Volumes/Sith/Store_elsewhere/Falcon/Time-Lapse/210207_ADL_2/*.tif',  # ADL_277263
]
POSTER = 'ADL_276254.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 60, 4, watermark=True, verbose=False, dryrun=False)
