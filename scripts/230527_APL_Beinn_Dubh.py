from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/230527_Edinburgh/230527_APL_04/*.tif',  # APL_163202 - APL_163279
    '/Volumes/Jedi/Cache/230527_Edinburgh/230527_APL_07/*.tif',  # APL_163695 - APL_163893
    '/Volumes/Jedi/Cache/230527_Edinburgh/230527_APL_08/*.tif',  # APL_163912 - APL_164011
    '/Volumes/Jedi/Cache/230527_Edinburgh/230527_APL_09/*.tif',  # APL_164051 - APL_164239
    '/Volumes/Jedi/Cache/230527_Edinburgh/230527_APL_06/*.tif',  # APL_163412 - APL_163588
    '/Volumes/Jedi/Cache/230527_Edinburgh/230527_APL_12/*.tif',  # APL_164552 - APL_164876
]
POSTER = '/Volumes/Jedi/Cache/230527_Edinburgh/230527_APL_07/APL_163737.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 48, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
