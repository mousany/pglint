import sys
import keyboard


class pglintKernel():
    '''Kernel component of pglint, providing keyboard listeners and log function 
    for pglint's smooth running.
    '''

    __color__ = {
        "success": "\033[32m%s\033[0m",
        "error": "\033[31m%s\033[0m",
        "warning": "\033[33m%s\033[0m",
    }

    __invalidKey__ = '-=[]\\'

    __defaultText__ = '''The Zen of Python,by Tim Peters.Beautiful is better than ugly.'''
    __defaultTextSrc__ = "https://raw.githubusercontent.com/undwtpal/pglint-lib/master/__answer__.txt"

    def __init__(self, text: str = __defaultText__):
        '''Initialize pglint kernel, set roaming variables.'''

        self._active = False
        self._pointer = 0
        self._text = text

    def __getitem__(self, key: str):
        '''Set __getitem__ to simplify the procedure of getting handlers.'''

        if ('_' + key) in dir(self):
            return getattr(self, '_' + key)
        else:
            return None

    def _log(self, sig: str, msg: str):
        '''Log on the console.'''

        if sig in pglintKernel.__color__.keys():
            print(
                f"{ pglintKernel.__color__[sig] % sig.upper() } { msg.capitalize() }"
            )

    def _error(self, msg: str):
        '''Print error and exit the program.'''

        self._log("error", msg)
        # self._log("error", "pglint is closed for errors")
        sys.exit()

    def _setText(self, text: str):
        '''Set text for pglint kernel.'''

        if text != None:
            self._text = text

    def _getText(self):
        '''Get text from pglint kernel'''

        return self._text

    def _backspace(self, length: int):
        '''Write certain backspace on console.'''

        keyboard.write('\b' * length)

    def _match(self, origin: str, keys: str = '.?!', excepts: str = ' .?!,'):
        '''Match function for feature-matching.'''

        idx = 0
        while idx < len(origin) and (origin[idx] in excepts):
            idx += 1
        loc = len(origin[idx:])
        for key in keys:
            pos = origin[idx:].find(key)
            if pos != -1:
                loc = min(loc, pos)
        return loc + idx

    def _show(self):
        '''Show the sentence from the text-pointer to the next sub-clause.'''

        if self._pointer < len(self._text):
            idx = self._match(self._text[self._pointer:], ',.?!')
            self._log(
                "success", "text pointer now starts with: " +
                self._text[self._pointer:self._pointer + idx + 1])

    def _stop(self):
        '''Stop handler, which will never be reached by keyboard.'''

        pass

    def _switch(self):
        '''Switch handler, switch mode for pglint.'''

        self._backspace(1)
        self._active = not self._active

    def _reset(self):
        '''Reset handler, reset text-pointer to the begining.'''

        self._backspace(1)
        self._pointer = 0
        self._log("success", "text-pointer is now at the begining")

    def _all(self):
        '''All handler, print the whole text on keyboard.'''

        self._backspace(1)
        keyboard.write(self._text[self._pointer:])
        self._pointer = len(self._text)
        self._log("success", "text-pointer is now at the end")
        keyboard.send('end')

    def _next(self):
        '''Next handler, print the next word on keyboard.'''

        self._backspace(1)
        if self._pointer < len(self._text):
            idx = self._match(self._text[self._pointer:], ' .?!,')
            keyboard.write(self._text[self._pointer:self._pointer + idx + 1])
            self._pointer += idx + 1
            self._show()
        else:
            self._log("warning", "text-pointer is now at the end")
        keyboard.send('end')

    def _forward(self):
        '''Forward handler, print the next sentence on keyboard.'''

        self._backspace(1)
        if self._pointer < len(self._text):
            idx = self._match(self._text[self._pointer:])
            keyboard.write(self._text[self._pointer:self._pointer + idx + 1])
            self._pointer += idx + 1
            self._show()
        else:
            self._log("warning", "text-pointer is now at the end")
        keyboard.send('end')

    def _before(self):
        '''Before handler, move the text-pointer to the last word.'''

        idx = self._match(self._text[:self._pointer][::-1], ' .?!,')
        if self._pointer > 0:
            self._pointer -= idx
            self._show()
        else:
            self._log("warning", "text-pointer is now at the begining")

    def _after(self):
        '''After handler, move the text-pointer to the next word.'''

        idx = self._match(self._text[self._pointer:], ' .?!,')
        if self._pointer < len(self._text):
            self._pointer += idx
            self._show()
        else:
            self._log("warning", "text-pointer is now at the end")

    def _behind(self):
        '''Behind handler, move the text-pointer to the last sentence.'''

        idx = self._match(self._text[:self._pointer][::-1])
        if self._pointer > 0:
            self._pointer -= idx
            self._show()
        else:
            self._log("warning", "text-pointer is now at the begining")

    def _ahead(self):
        '''Ahead handler, move the text-pointer to the next sentence.'''

        idx = self._match(self._text[self._pointer:])
        if self._pointer < len(self._text):
            self._pointer += idx
            self._show()
        else:
            self._log("warning", "text-pointer is now at the end")

    def _callback(self, event: keyboard.KeyboardEvent):
        '''Callback for all keyboard events, only record valid keyboard movements.'''

        if event.name == 'esc':
            return
        if event.event_type == 'down' and self._active:
            if self._pointer >= len(self._text):
                return
            if event.name == "space":
                self._backspace(1)
                keyboard.write(self._text[self._pointer])
                self._pointer += 1
            elif len(event.name) == 1 and (event.name
                                           not in pglintKernel.__invalidKey__):
                self._backspace(1)
                keyboard.write(self._text[self._pointer])
                self._pointer += 1

    def _apply(self, keys: dict):
        '''Apply keyboard config by adding hotkeys to keyboard and activate the whole process.'''

        self._log("success", "pglint kernel is now activated")
        for key, value in keys.items():
            if self[key] != None:
                keyboard.add_hotkey(value, self[key])

        keyboard.hook(self._callback)
        keyboard.wait('esc')
        keyboard.unhook_all()