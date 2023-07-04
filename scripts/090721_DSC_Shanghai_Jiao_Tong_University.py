from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERN = '/Volumes/Crimson/Cache/090721_DSC_Shanghai_Jiao_Tong_University/*.tif'  # D80_090721_173414c - D80_090721_174041
POSTER = 'D80_090721_174021.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 24, 3, watermark=True, verbose=False, dryrun=False)
