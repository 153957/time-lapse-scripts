from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERN = '/Volumes/Twin suns/150409_ARN_1/*.tif'  # ARN_091385 - ARN_091699
POSTER = '/Volumes/Twin suns/150409_ARN_1/ARN_091552.tif'


if __name__ == '__main__':
    filters = [
        ('crop', {'w': '1920', 'h': '1280'}),
        ('tblend', {'all_mode': 'lighten', 'all_opacity': '1'}),
        ('tblend', {'all_mode': 'lighten', 'all_opacity': '0.75'}),
    ]
    make_movie(NAME, PATTERN, 24, 3, watermark=True, verbose=False, dryrun=False, filters=filters)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
