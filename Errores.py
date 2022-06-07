from sys import stderr,stdout
import os

class Logger:
    def __init__(self,verbose=False):
        self.verbose = verbose

    def set_verbose(self,verbose):
        self.verbose = verbose

    def log(self,mensaje,file=stdout):
        if self.verbose:
            print(mensaje,file=file)

    def error(self,mensaje,file=stderr):
        print(f'ERROR {mensaje}',file=file)

def comprobar_existe(ruta):
    es_correcto = True
    if not os.path.exists(ruta):
        es_correcto = False
    else:
        es_correcto = True
    return es_correcto