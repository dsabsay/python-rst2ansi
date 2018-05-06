import sys
import argparse
import io

from . import rst2ansi


def main():
    """ The entry point for the commandline interface. """

    parser = argparse.ArgumentParser(
        description='Prints a reStructuredText input in an ansi-decorated '
                    'format suitable for console output.'
    )
    parser.add_argument('file', type=str, nargs='?',
                        help='A path to the file to open')

    args = parser.parse_args()

    if args.file:
        # with io.open(args.file, 'rb') as f:
        #     process_file(f)
        with open(args.file, 'r') as f:
            process_file(f)
    else:
        process_file(sys.stdin)


def process_file(f):
    out = rst2ansi(f.read())
    if out:
        try:
            print(out)
        except UnicodeEncodeError:
            print(out.encode('ascii', errors='backslashreplace').decode('ascii'))


if __name__ == '__main__':
    main()
