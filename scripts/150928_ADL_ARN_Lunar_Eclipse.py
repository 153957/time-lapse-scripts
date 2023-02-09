from pathlib import Path

import ffmpeg

from time_lapse import output, source

NAME = Path(__file__).stem
CLOSE_PATTERNS = [
    '/Volumes/Jedi/Cache/ADL_150928_1/*.tif',  # ADL_190234 - ADL_190288
    '/Volumes/Jedi/Cache/ADL_150928_2/*.tif',  # ADL_190329 - ADL_190573
    '/Volumes/Jedi/Cache/ADL_150928_4/*.tif',  # ADL_190676 - ADL_190877
]
WIDE_PATTERN = '/Volumes/Jedi/Cache/ARN_150928_1/*.tif',  # ARN_096978 - ARN_097711
# poster = ADL_190444

if __name__ == '__main__':
    wide_source = source.get_input(WIDE_PATTERN, 30, 0).filter_multi_output('split')

    close_source1 = source.get_input(CLOSE_PATTERNS[0], 30, 0)
    close_source2 = source.get_input(CLOSE_PATTERNS[1], 30, 0)
    close_source3 = source.get_input(CLOSE_PATTERNS[2], 30, 0)

    source = ffmpeg.concat(
        close_source1,
        wide_source[0].trim(end_frame=165).setpts('PTS-STARTPTS'),
        close_source2,
        wide_source[1].trim(start_frame=166, end_frame=405).setpts('PTS-STARTPTS'),
        close_source3,
        wide_source[2].trim(start_frame=406).setpts('PTS-STARTPTS'),
    )

    output.create_outputs(source, NAME, watermark=True, verbose=False, dryrun=False)
