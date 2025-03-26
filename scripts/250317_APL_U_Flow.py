from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/250317_U_Flow/250317_APL_05/*.tif',  # APL_258308 - APL_258601
    '/Volumes/Jedi/Cache/250317_U_Flow/250317_APL_06/*.tif',  # APL_258622 - APL_258889
    '/Volumes/Jedi/Cache/250317_U_Flow/250317_APL_07/*.tif',  # APL_258893 - APL_259130
    '/Volumes/Jedi/Cache/250317_U_Flow/250317_APL_08/*.tif',  # APL_259175 - APL_259373
    '/Volumes/Jedi/Cache/250317_U_Flow/250317_APL_09/*.tif',  # APL_259411 - APL_259505
    '/Volumes/Jedi/Cache/250317_U_Flow/250317_APL_10/*.tif',  # APL_259509 - APL_259634
    '/Volumes/Jedi/Cache/250317_U_Flow/250317_APL_11/*.tif',  # APL_259639 - APL_259683
]
POSTER = '/Volumes/Jedi/Cache/250317_U_Flow/250317_APL_08/APL_259190.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 15, 0, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
