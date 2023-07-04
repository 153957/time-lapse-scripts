from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERN = '/Volumes/Crimson/Cache/090712_DSC_Tokyo_Tower/*.tif'  # D80_090712_183805 - D80_090712_195932
POSTER = 'D80_090712_190253.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 24, 3, watermark=True, verbose=False, dryrun=False)
