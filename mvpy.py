import argparse
from  Errores import *
import shutil
import os

logger = Logger()



def mover(origen, destino):

    if not comprobar_existe(destino):
        raise Exception('Error el fichero/directorio ya existe')
    else:
        shutil.move(origen,destino)
        logger.log(f"Se ha movido {origen} -> {destino}")

def renombrar(origen, destino):
    if not comprobar_existe(destino):
        raise Exception('Error el fichero/directorio ya existe')
    else:
        os.rename(origen, destino)
        logger.log(f"{origen} -> {destino}")


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