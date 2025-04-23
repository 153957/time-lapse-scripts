from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERN = '/Volumes/Jedi/Cache/250421_APL_Draailier_en_Doedelzak//*.tif'  # APL_278251 - APL_278869
POSTER = '/Volumes/Jedi/Cache/250421_APL_Draailier_en_Doedelzak/APL_278251.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 48, 4, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
