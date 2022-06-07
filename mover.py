import argparse
from pathlib import Path
import shutil
import os

def mover_directorio(origen, destino):

    for contenido in os.listdir(destino):
            shutil.move(origen,destino)


def comprobar_es_directorio(destino: str):
    esCorrecto = True
    if os.path.isdir(destino):
        esCorrecto = False
    elif os.path.isfile(destino):
        esCorrecto = False
    return esCorrecto


def mover_fichero(origen, destino):
    shutil.move(origen,destino)


def renombrar(origen, destino: str):
    if not comprobar_es_directorio(destino):
        print(f"Nombre invalido, el fichero/directorio {destino} ya existe")
    else:
        os.rename(origen, destino)


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
        'destino',
        help='Nombre nuevo del fichero/directorio o directorio donde se va a mover el origen por el primer argumento'
    )
    return parser.parse_args()


def main():
    argumentos = comando()
    mover_fichero(argumentos.origen, argumentos.destino)


if __name__ == '__main__':
    main()
