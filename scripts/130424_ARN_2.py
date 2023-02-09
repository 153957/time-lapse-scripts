from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERN = '/Volumes/Jedi/Cache/ARN_130424_2/*.tif'  # ARN_039923 - ARN_040393
# poster: ARN_039923


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 30, 0, watermark=True, verbose=False, dryrun=False)
