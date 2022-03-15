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
    __longArgs__ = [
        "help", "channel=", "file=", "text=", "save", "option=", "keys", "all"
    ]
    __exitArgs__ = [
        "--help", "-h", "save", "-s", "option", "-o", "--keys", "-k", "--all",
        "-a"
    ]

    __help__ = '''
Usage: 
  pglint [options]

Commands:
  -h --help                   Show help.
  -a --all                    Show all available remote sources.
  -k --keys                   Show keyboard config.
  -s --save                   Save text to local file __answer__.txt, only the text you are using before 
                              this command will be saved.
  -c --channel <link>         Get text from remote source.
  -f --file <path>            Get text from local file.
  -t --text <text>            Get text from console.
  -o --option <string>        Customize keyboard config. Your option string should follows the format of
                              "name key". Name should be in the config, and except stop('esc') key should 
                              be one valid charater ('a') or ended with one valid character ('ctrl+a').
                              And use 'space', 'plus' and 'comma' to replace ' ', '+' and ',' .
                              i.e. "switch ctrl+alt+h"

Notice:
  if your text or link contains space(' '), minus('-') or any invalid characters, please put them into a 
  quotes. 
  i.e. '-t "The Zen of Python."'

    '''

    __defaultSaveSrc__ = "__answer__.txt"
    __defaultAllSrc__ = "https://raw.githubusercontent.com/yanglinshu/pglint/master/index.json"

    def __init__(self, _log, _error, args: dict = __args__):
        '''Initialize pglintArgs.'''
        self._args = args
        self._log = _log
        self._error = _error
        self._extern = pglintExtern()

    def __getitem__(self, key: str):
        '''Set __getitem__ to simplify the procedure of getting handlers.'''

        if key in self._args.keys():
            return getattr(self, '_' + key[2:])
        else:
            _reverseDict = dict(zip(self._args.values(), self._args.keys()))
            if key in _reverseDict.keys():
                return getattr(self, '_' + _reverseDict[key][2:])
            else:
                return None

    def _help(self):
        '''Print handler, print __help__ to console.'''

        print(pglintArgs.__help__)

    def _channel(self, url: str):
        '''Channel handler, get text from remote source.'''

        try:
            text = self._extern._get(url)
            self._log("success", "Get text from remote source successfully.")
            return text
        except Exception as excepts:
            self._error(str(excepts))

    def _file(self, src: str):
        '''File handler, load in text from local file.'''

        try:
            with open(src) as f:
                text = f.read()
            self._log("success", "Get text from local file successfully.")
            return text
        except Exception as excepts:
            self._error(str(excepts))

    def _text(self, text: str):
        '''Text handler, load in text on console.'''

        self._log("success", "Get text from console successfully.")
        return text

    def _save(self, text: str):
        '''Save handler, save text to __answer__.txt on disks.'''

        try:
            self._extern._write(pglintArgs.__defaultSaveSrc__, text)
            self._log("success", "save text into __answer__.txt successfully")
        except Exception as excepts:
            self._error(str(excepts))

    def _all(self):
        '''All handler, print all available remote sources to console.'''

        try:
            text = self._extern._get(pglintArgs.__defaultAllSrc__)
            dic = self._extern._json(text)
            print("Showing all available texts below")
            for key, value in dic.items():
                print("---- " + key + ":", value)
        except Exception as excepts:
            self._error(str(excepts))

    def _option(self, text: str):
        '''Option handler, parse option string.'''

        return text.split()

    def _keys(self, keys: dict):
        '''Keys handler, print current key config to console.'''

        print("Showing keyboard config below")
        for key, value in keys.items():
            print("---- " + key + ":", value)
