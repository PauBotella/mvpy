from sys import stderr,stdout


class Logger:
    def __init__(self,verbose=False):
        self.verbose = verbose

    def set_verbose(self,verbose):
        self.verbose = verbose

    def log(self,mensaje,file=stdout):
        if self.verbose:
            print(f'\033[0;34m{mensaje}\033[0m',file=file)

    def error(self,mensaje,file=stderr):
        print(f'\033[0;31mError: {mensaje}\033[0m',file=file)

