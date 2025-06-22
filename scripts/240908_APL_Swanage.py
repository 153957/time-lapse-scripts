from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/240908_APL_Swanage/240908_APL_1/*.tif',  # APL_233084 - APL_233324
    '/Volumes/Jedi/Cache/240908_APL_Swanage/240908_APL_2/*.tif',  # APL_233329 - APL_234019
    '/Volumes/Jedi/Cache/240908_APL_Swanage/240908_APL_3/*.tif',  # APL_234030 - APL_234565
]
POSTER = '/Volumes/Jedi/Cache/240908_APL_Swanage/240908_APL_1/APL_233088.tif'


if __name__ == '__main__':
    make_movie(
        NAME,
        PATTERNS,
        30,
        3,
        watermark=True,
        verbose=False,
        dryrun=False,
        filters=[('tblend', {'all_mode': 'lighten', 'all_opacity': '0.5'})],
    )
    thumbnail.create_thumbnail(NAME, Path(POSTER))
