from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/240302_240714_Jaarbeurs_/240302_APL_2/*.tif',  # APL_212644 - APL_213156
    '/Volumes/Jedi/Cache/240302_240714_Jaarbeurs_/240302_APL_5/*.tif',  # APL_214534 - APL_214738
    '/Volumes/Jedi/Cache/240302_240714_Jaarbeurs_/240714_APL_1/*.tif',  # APL_223225 - APL_223966
]
POSTER = '/Volumes/Jedi/Cache/240302_240714_Jaarbeurs_/240714_APL_1/APL_223906.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 48, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
