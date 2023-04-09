from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Crimson/Cache/221102_Boulder Creek/221102_1/*.tif',  # APL_147633 - APL_147919
    '/Volumes/Crimson/Cache/221102_Boulder Creek/221102_2/*.tif',  # APL_147931 - APL_148345
]
# poster: APL_147633


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 30, 0, watermark=True, verbose=False, dryrun=False)
