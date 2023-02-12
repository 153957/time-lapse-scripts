from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERN = '/Volumes/Crimson/Cache/220514_APL_Noordermeerdijk/*.tif',  # APL_110607 - APL_110850, APL_110851 - APL_111039
# poster: APL_111039


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 30, 7, watermark=True, verbose=False, dryrun=False)