import argparse

def cli():
    parser = argparse.ArgumentParser(
        prog='mvpy',
        description='Move and rename files and directories'
    )
    parser.add_argument(
        '-v','--verbose',
        action='store_true',
        help='Displays more information about the process to be executed'
    )

    parser.add_argument(
        '-i', '--inside',
        action='store_true',
        help='Move the entire contents of a folder to another folder'
    )

    parser.add_argument(
        '-o', '--override',
        action='store_true',
        help='if the source already exists in the destination, overwrites it'
    )
    parser.add_argument(
        'source',
        help='File or directory to be renamed or moved'
    )
    parser.add_argument(
        'destination',
        help='New name of the file/directory or directory where the source is to be moved by the first argument'
    )
    return parser.parse_args()