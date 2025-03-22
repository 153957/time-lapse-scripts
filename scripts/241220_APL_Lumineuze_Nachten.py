from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/241220_Lumineuze_Nachten/241220_APL_1/*.tif',  # APL_247484 - APL_247695
    '/Volumes/Jedi/Cache/241220_Lumineuze_Nachten/241220_APL_2/*.tif',  # APL_247721 - APL_247885
    '/Volumes/Jedi/Cache/241220_Lumineuze_Nachten/241220_APL_3/*.tif',  # APL_247901 - APL_248129
    '/Volumes/Jedi/Cache/241220_Lumineuze_Nachten/241220_APL_4/*.tif',  # APL_248155 - APL_248272
    '/Volumes/Jedi/Cache/241220_Lumineuze_Nachten/241220_APL_6/*.tif',  # APL_248636 - APL_249257
]
POSTER = '/Volumes/Jedi/Cache/241220_Lumineuze_Nachten/241220_APL_3/APL_247901.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 30, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
