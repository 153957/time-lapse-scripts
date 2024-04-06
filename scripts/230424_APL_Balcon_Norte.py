from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Twin suns/230424_2/*.tif',  # APL_158771 - APL_158930
    '/Volumes/Twin suns/230424_3/*.tif',  # APL_158944 - APL_159068
    '/Volumes/Twin suns/230424_6/*.tif',  # APL_159376 - APL_159524
]
POSTER = '/Volumes/Twin suns/230424_3/APL_158969.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 24, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
