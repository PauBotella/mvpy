from sys import stderr,stdout

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


class mvpyError(Exception):
    pass