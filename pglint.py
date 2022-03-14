from ast import arg
import sys
from getopt import getopt
from colorama import init
from src.keys import pglintKeys
from src.kernel import pglintKernel
from src.args import pglintArgs

def main():
    '''The main control of pglint, reacting to system args'''

    init(autoreset=True)
    _keys = pglintKeys()
    _kernel = pglintKernel()
    _args = pglintArgs(_kernel._error)

    try:
        opts, args = getopt(sys.argv[1:], pglintArgs.__shortArgs__, pglintArgs.__longArgs__)
    except Exception as excepts:
        _kernel._error(str(excepts))

    if args != []:
        argString = ""
        for arg in args:
            argString = argString + f' "{ arg }"'
        _kernel._error(f"unknown arguments for{ argString }.")

    for opt in opts:
        name, value = opt
        if name in ("--option", "-o"):
            _keys._set(*_args[name](value))
            _kernel._log("success", "update keyboard config successfully.")
            exit()
        elif name in ("--save", "-s"):
            _args[name](_kernel._getText())
            _kernel._log("success", "save text into __answer__.txt successfully.")
            exit()
        elif name in ("--keys", "-k"):
            _args[name](_keys._get())
            exit()
        elif name in ("--help", "-h", "--all", "-a"):
            _args[name]()
            exit()
        else:
            _kernel._setText(_args[name](value))

    _kernel._apply(_keys._get())
    _kernel._log("success", "pglint is closed successfully.")

if __name__ == '__main__':
    main()