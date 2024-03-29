from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERN = '/Volumes/Sith/Store_elsewhere/Falcon/Time-Lapse/101203_DSC_2/*.tif'  # D80_101203_130438 - D80_101203_131442
POSTER = 'D80_101203_130516.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 30, 2, watermark=True, verbose=False, dryrun=False)
