from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERN = '/Volumes/Falcon/tl_temp/101129_1/*.tiff'  # D80_101129_171323 - D80_101129_174150


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 24, 10, watermark=True, verbose=False, dryrun=False)
