import argparse
from  Errores import mvpyError,Logger
from sys import stderr,stdout
from pathlib import Path
import shutil
import os

def mover_directorio(origen, destino):

    for contenido in os.listdir(destino):
        shutil.move(origen,destino)
        print(f"{origen} -> {destino}")


def comprobar_existe(ruta):
    es_correcto = True
    if os.path.isdir(ruta):
        es_correcto = False
    elif os.path.isfile(ruta):
        es_correcto = False
    else:
        es_correcto = False
    return es_correcto


def mover_fichero(origen, destino):
    shutil.move(origen,destino)
    print(f"{origen} -> {destino}")


def renombrar(origen, destino):
    if not comprobar_existe(destino):
        raise Errores.mvpyError('Error el fichero/directorio ya existe')
    else:
        os.rename(origen, destino)


def terminal():
    parser = argparse.ArgumentParser(
        prog='mover',
        description='Mueve y renombra ficheros y directorios'
    )
    parser.add_argument(
        '-v','--verbose',
        action='store_true',
        help='Te muestra todo lo que hace el programa por la terminal'
    )

    parser.add_argument(
        'origen',
        help='Fichero o directorio al que le quieres cambiar el nombre, o lo quieres mover'
    )
    parser.add_argument(
        'destino',
        help='Nombre nuevo del fichero/directorio o directorio donde se va a mover el origen por el primer argumento'
    )
    return parser.parse_args()


def main():
    argumentos = terminal()
    try:

        mover_fichero(argumentos.origen, argumentos.destino)
    except Errores.mvpyError as err:
        print(err,file=stderr)
        exit(1)


if __name__ == '__main__':
    main()
