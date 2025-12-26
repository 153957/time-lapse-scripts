from pathlib import Path

from time_lapse import make_movie, thumbnail

NAME = Path(__file__).stem
PATTERN = '/Volumes/Jedi/Cache/251221_APL_Lumineuze_Nachten/*.tif'  # APL_336967 - APL_341478, Excluding shots 08 and 10.
POSTER = '/Volumes/Jedi/Cache/251221_APL_Lumineuze_Nachten/APL_340929.tif'


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 48, 0, watermark=True, verbose=False, dryrun=False)
    thumbnail.create_thumbnail(NAME, Path(POSTER))
