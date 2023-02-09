from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERN = '/Volumes/Falcon/tl_temp/121103_2/*.tiff'  # ARN_020512 - ARN_021511
# poster: ARN_020512


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 30, 0, watermark=True, verbose=False, dryrun=False)
