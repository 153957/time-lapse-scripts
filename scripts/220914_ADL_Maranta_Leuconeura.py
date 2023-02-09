from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERN = '/Volumes/Crimson/Cache/220914_ADL_1/*.tif'  # ADL_280229 - ADL_281226
# poster: ADL_281226


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 60, 8, watermark=True, verbose=False, dryrun=False)
