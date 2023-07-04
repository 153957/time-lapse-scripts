from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/220924_Porto/220924_Porto_8_She_Changes/*.tif',  # APL_130064 - APL_130363
    '/Volumes/Jedi/Cache/220924_Porto/220924_Porto_9_Trees/*.tif',  # APL_130364 - APL_130438
    '/Volumes/Jedi/Cache/220924_Porto/220924_Porto_11_She_Changes/*.tif',  # APL_130592 - APL_130731
]
POSTER = 'APL_130592.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 24, 6, watermark=True, verbose=False, dryrun=False)
