from pathlib import Path

from time_lapse import make_movie

NAME = Path(__file__).stem
PATTERN = '/Volumes/Crimson/Cache/110311_DSC_Holland_Casino/*.tif'  # D80_110311_200019 - D80_110311_225056
# poster: D80_110311_213343


if __name__ == '__main__':
    make_movie(
        NAME,
        PATTERN,
        24,
        0,
        watermark=True,
        verbose=False,
        dryrun=False,
        filters=[('tblend', {'all_mode': 'lighten', 'all_opacity': 0.5})]
    )
