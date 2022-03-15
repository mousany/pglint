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
    _args = pglintArgs(_kernel._log, _kernel._error)

    try:
        opts, args = getopt(sys.argv[1:], pglintArgs.__shortArgs__,
                            pglintArgs.__longArgs__)
    except Exception as excepts:
        _kernel._error(str(excepts))

    if args != []:
        argString = ""
        for arg in args:
            argString = argString + f' "{ arg }"'
        _kernel._error(f"unknown arguments for{ argString }")

    names = []
    for opt in opts:
        name, value = opt
        names.append(name)
        if name in ("--option", "-o"):
            if value == "default":
                _keys._reset()
            else:
                _keys._set(*_args[name](value))
            _kernel._log("success", "update keyboard config successfully")
        elif name in ("--save", "-s"):
            _args[name](_kernel._getText())
        elif name in ("--keys", "-k"):
            _args[name](_keys._get())
        elif name in ("--help", "-h", "--all", "-a"):
            _args[name]()
        else:
            _kernel._setText(_args[name](value))

    if set(names) <= set(pglintArgs.__exitArgs__):
        sys.exit()

    if _kernel._text == pglintKernel.__defaultText__:
        try:
            text = _args._extern._get(pglintKernel.__defaultTextSrc__)
            _kernel._setText(text)
            _kernel._log("success", "Get default remote text successfully")
        except Exception as excepts:
            _kernel._log("warning", str(excepts))
            _kernel._log(
                "warning",
                "Unable to launch default remote text, using local default text now"
            )

    _kernel._apply(_keys._get())
    _kernel._log("success", "pglint is closed successfully")


if __name__ == '__main__':
    main()