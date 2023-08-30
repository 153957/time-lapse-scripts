from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Crimson/Cache/220319_Mini_Dansstage/220319_1/*.tif',  # APL_103005 - APL_103098
    '/Volumes/Crimson/Cache/220319_Mini_Dansstage/220319_2/*.tif',  # APL_103113 - APL_103260
    '/Volumes/Crimson/Cache/220319_Mini_Dansstage/220319_3/*.tif',  # APL_103262 - APL_103370
]
POSTER = '/Volumes/Crimson/Cache/220319_Mini_Dansstage/220319_1/APL_103022.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 24, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
