from mvpy import *
from Errores import comprobar_existe

def main():
    argumentos = terminal()
    logger.set_verbose(argumentos.verbose)

    if not comprobar_existe(argumentos.destino):
        renombrar(argumentos.origen,argumentos.destino)
    else:
        mover(argumentos.origen,argumentos.destino)

if __name__ == '__main__':
    main()