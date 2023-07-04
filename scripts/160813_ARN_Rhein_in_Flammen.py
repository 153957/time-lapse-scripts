from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERN = '/Volumes/Falcon/tl_temp/160813_1_Rhein_am_Flammen/*.tiff'  # ARN_105144 - ARN_106213
POSTER = 'ARN_105611.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 60, 0, watermark=True, verbose=False, dryrun=False)
