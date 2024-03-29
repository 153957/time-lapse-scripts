from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERN = '/Volumes/Crimson/Cache/080614_S60_Hibiscus/*.tif'  # S60_080614_015644 - S60_080614_120341
POSTER = 'S60_080614_075141.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 24, 5, watermark=True, verbose=False, dryrun=False)
