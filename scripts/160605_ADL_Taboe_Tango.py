from pathlib import Path

from time_lapse import output, source

NAME = Path(__file__).stem
PATTERN = '/Volumes/Crimson/Cache/160605_ADL_Tango/*.tif'  # ADL_183879 - ADL_184093
POSTER = 'ADL_183879.tif'

if __name__ == '__main__':
    source_input = source.get_input(PATTERN, 24, 0, None).filter_('tblend', all_mode='darken', all_opacity=0.5)

    output.create_outputs(source_input, NAME, watermark=True, verbose=False, dryrun=False)
