from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERN = '/Volumes/Crimson/Cache/090727_DSC_Shanghai_Pudong_Airport/*.tif'  # D80_090727_090438 - D80_090727_101136
# poster: D80_090727_092703


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 24, 6, watermark=True, verbose=False, dryrun=False)
