from actions import *
from cli import cli

def main():

    arguments = cli()
    logger.set_verbose(arguments.verbose)
    try:

        if os.path.isfile(arguments.source) and os.path.isdir(arguments.destination):
            move(arguments.source, arguments.destination,arguments.override)

        elif os.path.isdir(arguments.source) and os.path.isdir(arguments.destination):
            move_all(arguments.source, arguments.destination,arguments.override,arguments.inside)

        else:
            rename(arguments.source, arguments.destination,arguments.override)

    except Exception as ex:
        logger.error(ex)
        exit(1)


if __name__ == '__main__':
    main()