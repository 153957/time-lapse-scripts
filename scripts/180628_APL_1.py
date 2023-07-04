from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERN = '/Volumes/Falcon/tl_temp/180628_1/*.tiff'  # APL_027178 - APL_027581
POSTER = 'APL_027521.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 25, 0, watermark=True, verbose=False, dryrun=False)
