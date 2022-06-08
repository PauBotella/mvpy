from mvpy import *
from Errores import comprobar_existe


def main():

    argumentos = terminal()
    logger.set_verbose(argumentos.verbose)
    try:

        if os.path.isfile(argumentos.origen) and os.path.isdir(argumentos.destino):
            mover(argumentos.origen, argumentos.destino,argumentos.sobreescribir)

        elif os.path.isdir(argumentos.origen):
            mover_todo(argumentos.origen, argumentos.destino,argumentos.sobreescribir)

        else:
            comprobar_existe(argumentos.destino)
            renombrar(argumentos.origen, argumentos.destino,argumentos.sobreescribir)

    except Exception as ex:
        logger.error(ex)


if __name__ == '__main__':
    main()