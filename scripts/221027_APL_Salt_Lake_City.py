from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/221027_APL_Salt_Lake/221027_APL_3/*.tif',  # APL_142141 - APL_142356
    '/Volumes/Jedi/Cache/221027_APL_Salt_Lake/221028_APL_6/*.tif',  # APL_143447 - APL_143752
    '/Volumes/Jedi/Cache/221027_APL_Salt_Lake/221027_APL_1/*.tif',  # APL_141580 - APL_141884
    '/Volumes/Jedi/Cache/221027_APL_Salt_Lake/221028_APL_7/*.tif',  # APL_143761 - APL_143949
    '/Volumes/Jedi/Cache/221027_APL_Salt_Lake/221028_APL_2/*.tif',  # APL_142680 - APL_142724
    '/Volumes/Jedi/Cache/221027_APL_Salt_Lake/221028_APL_1/*.tif',  # APL_142465 - APL_142666
    '/Volumes/Jedi/Cache/221027_APL_Salt_Lake/221028_APL_4/*.tif',  # APL_142826 - APL_142967
    '/Volumes/Jedi/Cache/221027_APL_Salt_Lake/221028_APL_3/*.tif',  # APL_142729 - APL_142821
]
POSTER = '/Volumes/Jedi/Cache/221027_APL_Salt_Lake/221028_APL_1/APL_142465.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 30, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
