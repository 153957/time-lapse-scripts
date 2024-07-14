from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERN = '/Volumes/Jedi/Cache/240714_APL_Neoliet/*.tif'  # APL_222660 - APL_223186
POSTER = '/Volumes/Jedi/Cache/240714_APL_Neoliet/APL_222694.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 24, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
