from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/250317_Gele_brug/250317_APL_01/*.tif',  # APL_257376 - APL_257575
    '/Volumes/Jedi/Cache/250317_Gele_brug/250317_APL_02/*.tif',  # APL_257584 - APL_257665
]
POSTER = '/Volumes/Jedi/Cache/250317_Gele_brug/250317_APL_02/APL_257653.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 30, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
