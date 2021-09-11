import os
from PIL import Image
from termcolor import colored
import argparse
from typing import List


def convert(files: List[str], type: str, replace: bool, verbose: bool):
    for file in files:
        if not file.endswith('.webp'):
            print(colored(f'{file} does not appear to be a webp image', color='yellow'))
        else:
            target = file.replace('.webp', f'.{type}')
            if verbose:
                print(colored(f'Converting {file} to {target}', color='green'))

            image = Image.open(file)
            image.save(target, type, save_all=True, optimize=True, background=0)
            if replace:
                if verbose:
                    print(colored(f'Removing {file}\n', color='green'))

                os.remove(file)


def main():
    parser = argparse.ArgumentParser(description='Converts webp images into other formats [e.g gifs]')
    parser.add_argument('-f', '--files', nargs='+', help='the files to be converted')
    parser.add_argument('-d', '--directory', help='the directory containing the files to be converted')
    parser.add_argument('-t', '--type', help='the output file type [default=gif]', default='gif')
    parser.add_argument('-v', '--verbose', help='prints information [default=false]',
                        default=False, action='store_true')
    parser.add_argument('-r', '--replace', help='deletes the old webp images [default=false]',
                        default=False, action='store_true')
    args = parser.parse_args()

    if args.files is None and args.directory is None:
        raise RuntimeError('Nothing to convert. See --help.')
    else:
        if args.files is not None:
            convert(args.files, type=args.type, replace=args.replace, verbose=args.verbose)
        else:
            if args.directory is not None:
                convert([f'{args.directory}/{item}' for item in os.listdir(args.directory)],
                        type=args.type, replace=args.replace, verbose=args.verbose)


if __name__ == '__main__':
    main()
