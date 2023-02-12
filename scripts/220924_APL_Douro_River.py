from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/220924_Porto/220924_Porto_5_Douro_River/*.tif',  # APL_129463 - APL_129662
    '/Volumes/Jedi/Cache/220924_Porto/220924_Porto_3_Douro_River/*.tif',  # APL_128986 - APL_129185
    '/Volumes/Jedi/Cache/220924_Porto/220924_Porto_4_Dom_Luís_Bridge/*.tif',  # APL_129211 - APL_129391
    '/Volumes/Jedi/Cache/220924_Porto/220925_Porto_2_Dom_Luis_I/*.tif',  # APL_132046 - APL_132098
    '/Volumes/Jedi/Cache/220924_Porto/220925_Porto_4_Dom_Luis_I/*.tif',  # APL_132263 - APL_132385
    '/Volumes/Jedi/Cache/220924_Porto/220925_Porto_5_Douro_River/*.tif',  # APL_132390 - APL_132595
    '/Volumes/Jedi/Cache/220924_Porto/220925_Porto_6_Bridges/*.tif',  # APL_132604 - APL_132783
]
# poster: APL_129538


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 24, 3, watermark=True, verbose=False, dryrun=False)
