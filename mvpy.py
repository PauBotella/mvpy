import argparse
from Errores import *
import shutil
import os

logger = Logger()


def mover_todo(origen, destino,sobreescribir=False):

    for contenido in os.listdir(origen):
        if comprobar_existe(destino+contenido) and not sobreescribir:
            raise Exception(f"{origen+contenido} ya existe, -s para sobreescribir")
        else:
            shutil.move(origen+contenido,destino)
            logger.log(f"Se ha movido {contenido} -> {destino}")

def mover(origen, destino,sobreescribir=False):

    if not comprobar_existe(destino):
        raise Exception(f"{destino} no existe")

    elif not comprobar_existe(origen):
        raise Exception(f"{origen} no existe")

    else:
        shutil.move(origen,destino)
        logger.log(f"Se ha movido {origen} -> {destino}")


def renombrar(origen, destino,sobreescribir=False):
    if comprobar_existe(destino) and not sobreescribir:
        raise Exception(f"{destino} ya existe, -s para sobreescribir")

    elif not comprobar_existe(origen):
        raise Exception(f"{origen} no existe")

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
        '-s', '--sobreescribir',
        action='store_true',
        help='Si el fichero/'
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