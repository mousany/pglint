

class pglintArgs():
    '''Arguement handlers of pglint'''

    __args__ = {
        "--help": "-h", 
        "--intern": "-i",
        "--file": "-f", 
        "--text": "-t", 
        "--save": "-s", 
        "--all": "-a", 
        "--config": '-c', 
    }

    def __init__(self, args: dict = __args__):
        self._args = args

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
       pass

    def _intern(self, url: str):
        pass

    def _file(self, src: str):
        pass

    def _text(self, text: str): 
        pass

    def _save(self, src: str):
        pass

    def _all(self):
        pass

    def _config(self, dic: dict):
        pass

