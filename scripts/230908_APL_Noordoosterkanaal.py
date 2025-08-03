from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/230908_APL_1/*.tif',  # APL_199607 - APL_199749
    '/Volumes/Jedi/Cache/230908_APL_2/*.tif',  # APL_200108 - APL_200324
]
POSTER = '/Volumes/Jedi/Cache/230908_APL_1/APL_199732.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 30, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
