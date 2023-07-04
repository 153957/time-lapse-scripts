from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERNS = '/Volumes/Falcon/tl_temp/110209_1/*.tiff'  # D700_110209_081219 - D700_110209_081737
POSTER = 'D700_110209_081233.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 25, 0, watermark=True, verbose=False, dryrun=False)
