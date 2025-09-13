from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERNS = [
    '/Volumes/Jedi/Cache/250907_Eclipse/250907_ADL_4/*.tif',  # ADL_303664 - ADL_303861
    '/Volumes/Jedi/Cache/250907_Eclipse/250907_APL_4/*.tif',  # APL_309409 - APL_309772
    '/Volumes/Jedi/Cache/250907_Eclipse/250907_ADL_5a/*.tif',  # ADL_303876 - ADL_304195
    '/Volumes/Jedi/Cache/250907_Eclipse/250907_APL_5/*.tif',  # APL_309814 - APL_310132
    '/Volumes/Jedi/Cache/250907_Eclipse/250907_ADL_5b/*.tif',  # ADL_304196 - ADL_304524
    '/Volumes/Jedi/Cache/250907_Eclipse/250907_APL_6/*.tif',  # APL_310155 - APL_310277
]
POSTER = '/Volumes/Jedi/Cache/250907_Eclipse/250907_APL_4/APL_309615.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 30, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
