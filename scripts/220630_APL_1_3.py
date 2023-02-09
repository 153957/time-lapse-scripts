from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/220630_APL_1/*.tif',  # APL_118340 - APL_118702
    '/Volumes/Jedi/Cache/220630_APL_3/*.tif',  # APL_118794 - APL_119385
]
# poster: APL_119385


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 30, 5, watermark=True, verbose=False, dryrun=False)
