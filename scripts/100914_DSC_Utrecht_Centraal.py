from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERN = '/Volumes/Crimson/Cache/100914_DSC_Utrecht_Centraal/*.tif'  # D80_100914_094520 - D80_100914_095806
# poster: D80_100914_094743


if __name__ == '__main__':
    make_movie(
        NAME,
        PATTERN,
        24,
        0,
        watermark=True,
        verbose=False,
        dryrun=False,
        filters=[('tblend', {'all_mode': 'darken', 'all_opacity': 0.33})]
    )
