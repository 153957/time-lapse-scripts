from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Twin suns/240113_1/*.tif',  # APL_209810 - APL_209947
    '/Volumes/Twin suns/240114_1/*.tif',  # APL_210052 - APL_210191
]
POSTER = '/Volumes/Twin suns/240114_1/APL_210191.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 30, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
