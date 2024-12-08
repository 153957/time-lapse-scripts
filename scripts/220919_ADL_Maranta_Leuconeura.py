from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERN = '/Volumes/Jedi/Cache/220919_ADL_Maranta_Leuconeura/*.tif'  # ADL_281247 - ADL_282239
POSTER = '/Volumes/Jedi/Cache/220919_ADL_Maranta_Leuconeura/ADL_281761.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 48, 4, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
