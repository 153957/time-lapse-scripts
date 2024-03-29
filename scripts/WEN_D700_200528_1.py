from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERN = '/Volumes/Falcon/Other/200528_bloem_wen/WEN_*.tif'  # WEN_6525 - WEN_6971


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 24, 6, watermark=True, verbose=False, dryrun=False)
