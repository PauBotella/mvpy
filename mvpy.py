import argparse
from Errores import *
import shutil
import os

logger = Logger()


def mover_todo(origen, destino,sobreescribir=False,dentro=False):

    if comprobar_existe(destino) and not sobreescribir:
        raise Exception(f"{destino} ya existe, -s para sobreescribir")

    elif not comprobar_existe(origen):
        raise Exception(f"{origen} no existe")

    elif not comprobar_existe(destino):
        raise Exception(f"{destino} no existe")

    elif dentro:

        for contenido in os.listdir(origen):
            if comprobar_existe(destino + contenido) and not sobreescribir:
                raise Exception(f"{origen + contenido} ya existe, -s para sobreescribir")

            else:
                os.remove(destino+contenido)
                shutil.move(origen + contenido, destino)
                logger.log(f"Se ha movido {contenido} -> {destino}")

    else:
        if comprobar_existe(destino):
            os.remove(destino)
        shutil.move(origen,destino)
        logger.log(f"Se ha movido {origen} -> {destino}")


def mover(origen, destino,sobreescribir=False):

    dividir_ruta=origen.split("/")
    ultimo=dividir_ruta.pop()

    if not comprobar_existe(destino):
        raise Exception(f"{destino} no existe")

    elif not comprobar_existe(origen):
        raise Exception(f"{origen} no existe")

    elif comprobar_existe(destino + ultimo) and not sobreescribir:
        raise Exception(f"{destino+ultimo} ya existe, -s para sobreescribir")

    else:
        os.remove(destino+ultimo)
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
        help='Te muestra todo lo que hace el programa por detrás en la terminal'
    )

    parser.add_argument(
        '-d', '--dentro',
        action='store_true',
        help='Mueve el contenido de dentro un directorio a otro (Equivalente a por ejemplo mv /home/pau/dir1/* /home/pau/dir2/)'
    )

    parser.add_argument(
        '-s', '--sobreescribir',
        action='store_true',
        help='si el origen ya existe en el destino, lo sobreescribe'
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