from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/240906_240907_APL_Eastbourne/240906_APL_1/*.tif',  # APL_230748 - APL_231059
    '/Volumes/Jedi/Cache/240906_240907_APL_Eastbourne/240906_APL_3/*.tif',  # APL_231387 - APL_231653
    '/Volumes/Jedi/Cache/240906_240907_APL_Eastbourne/240907_APL_1/*.tif',  # APL_231851 - APL_232284
    '/Volumes/Jedi/Cache/240906_240907_APL_Eastbourne/240907_APL_2/*.tif',  # APL_232311 - APL_232542
]
POSTER = '/Volumes/Jedi/Cache/240906_240907_APL_Eastbourne/240906_APL_1/APL_231050.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 30, 4, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
