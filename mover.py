import argparse
import shutil
import os
def comando():
    parser = argparse.ArgumentParser(
        prog='mover',
        description='Mueve y renombra ficheros y directorios'
    )
    parser.add_argument(
        'origen',
    )
    parser.add_argument(
        'destino',
    )
    return parser.parse_args()

def main():
    argumentos=comando()
    print(argumentos)

if __name__ == '__main__':
    main()