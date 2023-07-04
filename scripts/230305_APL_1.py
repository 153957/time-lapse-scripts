from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERN = '/Volumes/Jedi/Cache/230305_Pannekoek/*.tif'  # APL_152633 - APL_153621
POSTER = 'APL_153157.tif'


if __name__ == '__main__':
    filters = [('crop', {'w': 'in_w * 2304 / 3712', 'h': 'in_h * 2304 / 3712', 'x': '0', 'y': 'in_h'})]
    make_movie(NAME, PATTERN, fps=24, deflicker=3, watermark=True, verbose=False, dryrun=False, filters=filters)
