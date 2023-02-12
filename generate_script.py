import argparse

from os.path import commonprefix
from pathlib import Path
from random import choice
from textwrap import dedent


def save_script(name: str, script: str) -> None:
    script_path = Path(__file__).parent / 'scripts' / f'{name}.py'
    script_path.write_text(script)
    print(f'Saved to {script_path}')


def single(path: str) -> None:
    """Simple single shot movie"""
    path = Path(path).resolve()
    sorted_images = sorted(image_path.stem for image_path in path.iterdir() if image_path.is_file())
    first = sorted_images[0]
    last = sorted_images[-1]
    poster = choice(sorted_images)

    fps = 24
    deflicker = 3

    script = dedent(f"""
        from pathlib import Path

        from time_lapse import make_movie

        NAME = Path(__file__).stem
        PATTERN = '{path}/*.tif'  # {first} - {last}
        # poster: {poster}


        if __name__ == '__main__':
            make_movie(NAME, PATTERN, {fps}, {deflicker}, watermark=True, verbose=False, dryrun=False)
    """).lstrip()
    save_script(path.name, script)


def multiple(*paths: str) -> None:
    """Simple multiple shots stitched together"""
    paths = [Path(path).resolve() for path in paths]
    firsts = []
    lasts = []

    for path in paths:
        sorted_images = sorted(image_path.stem for image_path in path.iterdir() if image_path.is_file())
        firsts.append(sorted_images[0])
        lasts.append(sorted_images[-1])

    poster = choice(firsts)

    fps = 24
    deflicker = 3

    patterns = '\n        '.join(
        f"    '{path}/*.tif',  # {first} - {last}"
        for path, first, last in zip(paths, firsts, lasts, strict=True)
    )

    script = dedent(f"""
        from pathlib import Path

        from time_lapse import make_movie

        NAME = Path(__file__).stem
        PATTERNS = [
        {patterns}
        ]
        # poster: {poster}


        if __name__ == '__main__':
            make_movie(NAME, PATTERNS, {fps}, {deflicker}, watermark=True, verbose=False, dryrun=False)
    """).lstrip()

    prefix = commonprefix([path.name for path in paths])
    name = '_'.join(path.name.removeprefix(prefix) for path in paths)
    if prefix:
        name = f'{prefix}{name}'
    save_script(name, script)


def main() -> None:
    parser = argparse.ArgumentParser(description='Generate a script for creating a time-lapse movie.')
    parser.add_argument(
        'paths',
        help='Paths to directories containing the frames for the movie.',
        default='.',
        nargs='+',
    )
    args = parser.parse_args()

    if len(args.paths) == 1:
        single(args.paths[0])
    else:
        multiple(*args.paths)


if __name__ == '__main__':
    main()
