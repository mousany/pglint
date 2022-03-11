import keyboard

class pglintKeys():

    '''Keyboard component of pglint, to use it, you need to create an instance of it.

    And after you finish modify keyboard config, you are required to apply it to add it 
    
    to keyboard event listener. 

    keys: 

        stop: deactivate pglint.

        pause: pause / unpause pglint.

        reset: reset text-pointer to the begining.

        all: print the whole text at once.

        next: write a word from the text which is pointed by the text-pointer, 

            and move it to the next word.

        forword: write a sentence from the text which is pointed by the text-pointer, 

            and move it to the first word of the next sentence.

        last: erase one word you have written.

        backward: erase one sentense you have written.

        before: move the text-pointer to the next word.

        after: move the text-pointer to the previous word.

        ahead: move the text-pointer to the first word of the next sentence.
        
        behind:  move the text-pointer to the first word of the last sentence.
    '''

    def __init__(self):

        '''Initialize pglintKey, use the default key above when initualizing.'''

        self._hotkeys = {
            "stop": ['', ], 
            "pause": ['', ], 
            "reset": ['', ], 
            "all": ['', ], 
            "next": ['', ],
            "forward": ['', ], 
            "last": ['', ], 
            "backward": ['', ],
            "before": ['', ], 
            "after": ['', ], 
            "ahead": ['', ], 
            "behind": ['', ], 
        }

    def modifyKey(self, name: str, key: str): 

        '''Modify a key from keyboard config, function name and keyboard string are required.'''
        
        self._hotkeys[name][0] = key

    def modifyKeys(self, dic: dict):

        '''Modify keyboard config from a dict, probably parsed from JSON.'''

        for key, value in dic:
            if key in self._hotkeys.keys():
                self._hotkeys[key][0] = value

    def apply(self):

        '''Apply keyboard config by adding hotkeys to keyboard.'''

        for key, value in self._hotkeys:
            keyboard.add_hotkey(*value)