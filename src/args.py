

class pglintArgs():
    '''Arguement handlers of pglint'''

    def __init__(self):
        self._pointer = 0
        self._buffer = ""
        self._argDict = {
            "--help": "-h", 
            "--channel": "-c",
            "--file": "-f", 
            "--text": "-t", 
            "--save": "-s", 
            "--live": "-l", 
        }

    def __getitem__(self, key: str):
        if key in self._argDict.keys():
            return getattr(self, '__' + key[2:] + '__')
        else:
            _reverseDict = dict(zip(self._argDict.values(), self._argDict.keys()))
            if key in _reverseDict.keys():
                return getattr(self, '__' + _reverseDict[key] + '__')
            else:
                return None

    def __help__(self):
       pass

    def __channel__(self, src: str):
        pass

    def __file__(self, src: str):
        pass

    def __text__(self, text: str): 
        pass

    def __save__(self, src: str):
        pass

    def __live__(self, src: str):
        pass

