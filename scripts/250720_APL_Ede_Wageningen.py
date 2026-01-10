from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/250720_APL_Ede_Wageningen/250720_APL_1/*.tif',  # APL_295255 - APL_295489
    '/Volumes/Jedi/Cache/250720_APL_Ede_Wageningen/250720_APL_2/*.tif',  # APL_295494 - APL_296120
]
POSTER = '/Volumes/Jedi/Cache/250720_APL_Ede_Wageningen/250720_APL_2/APL_295637.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 30, 2, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
