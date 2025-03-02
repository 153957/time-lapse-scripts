from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/230527_APL_Loch_Lomond/230527_APL_02/*.tif',  # APL_162970 - APL_163079
    '/Volumes/Jedi/Cache/230527_APL_Loch_Lomond/230527_APL_03/*.tif',  # APL_163084 - APL_163183
    '/Volumes/Jedi/Cache/230527_APL_Loch_Lomond/230527_APL_05/*.tif',  # APL_163286 - APL_163394
    '/Volumes/Jedi/Cache/230527_APL_Loch_Lomond/230527_APL_13/*.tif',  # APL_164907 - APL_165056
]
POSTER = '/Volumes/Jedi/Cache/230527_APL_Loch_Lomond/230527_APL_02/APL_163079.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 30, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
