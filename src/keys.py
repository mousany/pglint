import json


class pglintKeys():
    '''Keyboard component of pglint, to use it, you need to create an instance of it.

    And after you finish modify keyboard config, you are required to apply it to add it 
    
    to keyboard event listener. 

    keys: 

        stop: deactivate pglint.

        switch: activate / deactivate pglint per-charater mode.

        reset: reset text-pointer to the begining.

        all: print the whole text at once.

        next: write a word from the text which is pointed by the text-pointer, 

            and move it to the next word.

        forword: write a sentence from the text which is pointed by the text-pointer, 

            and move it to the first word of the next sentence.

        before: move the text-pointer to the next word.

        after: move the text-pointer to the previous word.

        ahead: move the text-pointer to the first word of the next sentence.
        
        behind:  move the text-pointer to the first word of the last sentence.
    '''

    __keys__ = {
        "stop": "esc",
        "switch": "\\",
        "reset": "[",
        "all": "]",
        "next": "-",
        "forward": "=",
        "before": "alt+-",
        "after": "alt+plus",
        "behind": "alt+[",
        "ahead": "alt+]",
    }

    __defaultSaveSrc__ = "config.json"

    def __init__(self, keys: dict = __keys__):
        '''Initialize pglintKey, use the default key above when initualizing.'''

        self._keys = keys

        try:
            with open(pglintKeys.__defaultSaveSrc__) as f:
                self._keys = json.load(f)
        except Exception as excepts:
            self._save()

    def _set(self, name: str, key: str):
        '''Set a key from keyboard config, function name and keyboard string are required.'''

        self._keys[name] = key
        self._save()

    def _get(self):
        '''Get keyboard config from pglintKeys instance.'''

        return self._keys

    def _reset(self):
        '''Reset keyboard config to default.'''

        self._keys = pglintKeys.__keys__
        self._save()

    def _save(self):
        '''Save keyboard config to local JSON file.'''
        try:
            with open(pglintKeys.__defaultSaveSrc__, "w") as f:
                json.dump(self._keys, f)
        except Exception as excepts:
            print(
                '\033[33mWARNING\033[0m Unable to save keyboard config, your customized config will be lost once pglint is closed'
            )
