import requests
from src.extern import pglintExtern


class pglintArgs():
    '''Arguement handlers of pglint'''

    __args__ = {
        "--help": "-h",
        "--channel": "-c",
        "--file": "-f",
        "--text": "-t",
        "--save": "-s",
        "--all": "-a",
        "--option": '-o',
        "--keys": "-k", 
    }

    __shortArgs__ = "hc:f:t:sao:k"
    __longArgs__ = ["help", "channel=", "file=", "text=", "save", "option=", "keys"]

    __help__ = "This pglint help."
    __defaultSaveSrc__ = "__answer__.txt"
    __defaultAllSrc__ = ""

    def __init__(self, _error, args: dict = __args__):
        self._args = args
        self._error = _error
        self._extern = pglintExtern()

    def __getitem__(self, key: str):
        if key in self._args.keys():
            return getattr(self, '_' + key[2:])
        else:
            _reverseDict = dict(zip(self._args.values(), self._args.keys()))
            if key in _reverseDict.keys():
                return getattr(self, '_' + _reverseDict[key][2:])
            else:
                return None

    def _help(self):
        print(pglintArgs.__help__)

    def _channel(self, url: str):
        try:
            text = self._extern._get(url)
            return text
        except Exception as excepts:
            self._error(str(excepts))

    def _file(self, src: str):
        '''Load in text from local file.'''

        try:
            with open(src) as f:
                text = f.read()
            return text
        except Exception as excepts:
            self._error(str(excepts))

    def _text(self, text: str):
        '''Load in text on console.'''

        return text

    def _save(self, text: str):
        '''Save text to __answer__.txt on disks.'''

        try:
            self._extern._write(pglintArgs.__defaultSaveSrc__, text)
        except Exception as excepts:
            self._error(str(excepts))

    def _all(self):
        try:
            text = self._extern._get(pglintArgs.__defaultAllSrc__)
            dic = self._extern._json(text)
            for key, value in dic.items():
                print(key, value)
        except Exception as excepts:
            self._error(str(excepts))

    def _option(self, text: str):
        return text.split()

    def _keys(self, keys: dict):
        for key, value in keys.items():
            print(key + ":", value)
            
