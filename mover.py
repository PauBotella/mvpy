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
        help='Fichero o directorio al que le quieres cambiar el nombre, o lo quieres mover'
    )
    parser.add_argument(
        'final',
        help='Nombre nuevo del fichero/directorio o directorio donde se va a mover el origen por el primer argumento'
    )
    return parser.parse_args()

def main():
    argumentos=comando()
    print(argumentos)

if __name__ == '__main__':
    main()