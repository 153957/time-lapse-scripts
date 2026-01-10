from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERN = '/Volumes/Jedi/Cache/251209_APL_Oliebollen_Neude/251209_APL_2/*.tif'  # APL_335694 - APL_336621
POSTER = '/Volumes/Jedi/Cache/251209_APL_Oliebollen_Neude/251209_APL_2/APL_336069.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 48, 3, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
