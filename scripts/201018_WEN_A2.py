from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Sith/Store_elsewhere/Falcon/Time-Lapse/201018_WEN_1/*.tif',  # WEN_058458 - WEN_058786
    '/Volumes/Sith/Store_elsewhere/Falcon/Time-Lapse/201018_WEN_3/*.tif'  # WEN_058987 - WEN_059196
]
# poster: WEN_058458


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 25, 2, watermark=True, verbose=False, dryrun=False)
