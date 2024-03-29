from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Sith/Store_elsewhere/Falcon/Time-Lapse/191108_ADL_1/*.tif',  # ADL_265397 - ADL_265696
    '/Volumes/Sith/Store_elsewhere/Falcon/Time-Lapse/191108_ADL_2/*.tif',  # ADL_265701 - ADL_265964
    '/Volumes/Sith/Store_elsewhere/Falcon/Time-Lapse/191108_ADL_3/*.tif',  # ADL_265970 - ADL_266092
]
POSTER = 'ADL_265703.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 30, 4, watermark=True, verbose=False, dryrun=False)
