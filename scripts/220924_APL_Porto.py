from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/220924_Porto/220924_Porto_1_Market/*.tif',  # APL_128579 - APL_128759
    '/Volumes/Jedi/Cache/220924_Porto/220924_Porto_2_Protest/*.tif',  # APL_128775 - APL_128970
    '/Volumes/Jedi/Cache/220924_Porto/220924_Porto_6_Jardim_do_Morro/*.tif',  # APL_129665 - APL_129737
    '/Volumes/Jedi/Cache/220924_Porto/220925_Porto_3_Vimara_Peres/*.tif',  # APL_132124 - APL_132250
]
# poster: APL_128579


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 24, 3, watermark=True, verbose=False, dryrun=False)
