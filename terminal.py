import argparse


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