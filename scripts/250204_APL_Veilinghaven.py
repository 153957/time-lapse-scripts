from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/250204_Veilinghaven/250204_APL_1/*.tif',  # APL_253262 - APL_253675
    '/Volumes/Jedi/Cache/250204_Veilinghaven/250204_APL_2/*.tif',  # APL_253687 - APL_253988
    '/Volumes/Jedi/Cache/250204_Veilinghaven/250204_APL_3/*.tif',  # APL_254002 - APL_254172
    '/Volumes/Jedi/Cache/250204_Veilinghaven/250204_APL_4/*.tif',  # APL_254178 - APL_254430
]
POSTER = '/Volumes/Jedi/Cache/250204_Veilinghaven/250204_APL_3/APL_254054.tif'


if __name__ == '__main__':
#     make_movie(NAME, PATTERNS, 24, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
