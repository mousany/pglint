import sys
from src.keys import pglintKeys
from src.kernel import pglintKernel


def main():
    '''The main control of pglint, reacting to system args'''

    keys = pglintKeys()
    kernel = pglintKernel(
        '''The Zen of Python,by Tim Peters.Beautiful is better than ugly.  Explicit is better than implicit.\nSimple is better than complex! Complex is better than complicated.Flat is better than nested ?  .Sparse is better than dense.'''
    )
    kernel._apply(keys._get())

if __name__ == '__main__':
    main()