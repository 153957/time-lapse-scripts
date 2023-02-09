from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERN = '/Volumes/Archive/Other/Time-lapse Wen/timelapse_bloem_wen/Output/200530_D810_bloem/WEN_*.tif',  # WEN_D810_ - WEN_D810_


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 30, 4, watermark=True, verbose=False, dryrun=False)
