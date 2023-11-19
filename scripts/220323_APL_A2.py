from pathlib import Path

from time_lapse import output, source

NAME = Path(__file__).stem
PATTERN = '/Volumes/Jedi/Cache/220323_1_APL/*.tif'  # APL_103712 - APL_103931
POSTER = 'APL_103782.tif'


if __name__ == '__main__':
    source_input = (
        source.get_input(PATTERN, 24, 0, None)
        .filter_('tblend', all_mode='lighten', all_opacity=0.33)
        .filter_('tblend', all_mode='lighten', all_opacity=0.33)
    )

    output.create_outputs(source_input, NAME, watermark=True, verbose=False, dryrun=False)
