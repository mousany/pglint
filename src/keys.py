from typing import overload


class pglintKeys():
    '''Keyboard component of pglint, to use it, you need to create an instance of it.

    And after you finish modify keyboard config, you are required to apply it to add it 
    
    to keyboard event listener. 

    keys: 

        stop: deactivate pglint.

        pause: activate / deactivate pglint per-charater mode.

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
        "pause": "\\",
        "reset": "[",
        "all": "]",
        "next": "-",
        "forward": "=",
        "before": "alt+-",
        "after": "alt+plus",
        "ahead": "alt+[",
        "behind": "alt+]"
    }

    def __init__(self, keys: dict = __keys__):
        '''Initialize pglintKey, use the default key above when initualizing.'''

        self._keys = keys

    def _set(self, name: str, key: str):
        '''Set a key from keyboard config, function name and keyboard string are required.'''

        self._keys[name] = key

    @overload
    def _set(self, dic: dict):
        '''Set keyboard config from a dict, probably parsed from JSON.'''

        for key, value in dic.items():
            if key in self._keys.keys():
                self._keys[key] = value

    def _get(self):
        return self._keys
