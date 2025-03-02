#!/usr/bin/env python
import argparse

from pathlib import Path
from shutil import copy2


def move_results(basename: str) -> None:
    # Source directory
    base_directory = Path(__file__).parent / 'scripts'

    # Target directories
    movies_1920_dir = Path('/Volumes/Jedi/TimeLapse/Movies/1920/')
    movies_960_dir = Path('/Volumes/Jedi/TimeLapse/Movies/960/')
    movies_screensaver_dir = Path('/Users/Shared/Time-Lapse/Selected/')
    thumbnail_output_dir = Path('/Volumes/Jedi/TimeLapse/Thumbs/Output/')
    thumbnail_sources_dir = Path('/Volumes/Jedi/TimeLapse/Thumbs/Sources/')
    thumbnail_website_dir = Path('~/Code/153957/153957/theme/static/images_timelapse/thumbs/').expanduser()

    # Ensure all target directories are available
    for directory in [
        movies_1920_dir,
        movies_960_dir,
        movies_screensaver_dir,
        thumbnail_output_dir,
        thumbnail_sources_dir,
        thumbnail_website_dir,
    ]:
        if not directory.is_dir():
            raise FileNotFoundError(f'Target directory "{directory}" does not exist.')

    # Source files
    thumbnail_file = base_directory / f'{basename}@2x.png'
    thumbnail_source = base_directory / f'{basename}.tif'
    video_1920 = base_directory / f'{basename}.mp4'
    video_960 = base_directory / f'{basename}_960.mp4'

    # Ensure all expected source files are available
    for file in [
        thumbnail_file,
        thumbnail_source,
        video_1920,
        video_960,
    ]:
        if not file.is_file():
            raise FileNotFoundError(f'Source file "{file}" does not exist.')

    # Copy files to target directories
    copy2(thumbnail_file, thumbnail_output_dir / thumbnail_file.name)
    copy2(thumbnail_file, thumbnail_website_dir / thumbnail_file.name)
    copy2(thumbnail_source, thumbnail_sources_dir / thumbnail_source.name)
    copy2(video_1920, movies_1920_dir / video_1920.name)
    copy2(video_1920, movies_screensaver_dir / video_1920.name)
    copy2(video_960, movies_960_dir / video_1920.name)

    # Remove source files
    for file in [
        thumbnail_file,
        thumbnail_source,
        video_1920,
        video_960,
    ]:
        file.unlink()


def main() -> None:
    parser = argparse.ArgumentParser(description='Move created output to final locations.')
    parser.add_argument(
        'basename',
        help='Basename of the output.',
    )
    args = parser.parse_args()

    move_results(args.basename)


if __name__ == '__main__':
    main()
