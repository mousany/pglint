import keyboard


class pglintKernel():
    '''Kernel component of pglint, providing keyboard listeners and log function 
    for pglint's smooth running.
    '''

    __color__ = {
        "success": "\033[35m%s\033[0m",
        "error": "\033[31m%s\033[0m",
        "warning": "\033[33m%s\033[0m",
    }

    __invalidKey__ = '-=[]\\'

    def __init__(self, text: str):
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
        '''Log to the console.'''

        print(
            f"[{ pglintKernel.__color__[sig] % sig.upper() }] { msg.capitalize() }"
        )

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

    def _stop(self):
        '''Stop handler, which will never be reached by keyboard.'''

        pass

    def _pause(self):
        '''Pause handler, switch mode for pglint.'''

        self._backspace(1)
        self._active = not self._active

    def _reset(self):
        '''Reset handler, reset text-pointer to the begining.'''

        self._backspace(1)
        self._pointer = 0

    def _all(self):
        '''All handler, print the whole text on keyboard.'''

        self._backspace(1)
        keyboard.write(self._text[self._pointer:])
        self._pointer = len(self._text)
        keyboard.send('end')

    def _next(self):
        '''Next handler, print the next word on keyboard.'''

        self._backspace(1)
        if self._pointer == len(self._text):
            return
        idx = self._match(self._text[self._pointer:], ' .?!,')
        keyboard.write(self._text[self._pointer:self._pointer + idx + 1])
        self._pointer += idx + 1
        keyboard.send('end')

    def _forward(self):
        '''Forward handler, print the next sentence on keyboard.'''

        self._backspace(1)
        if self._pointer == len(self._text):
            return
        idx = self._match(self._text[self._pointer:])
        keyboard.write(self._text[self._pointer:self._pointer + idx + 1])
        self._pointer += idx + 1
        keyboard.send('end')

    def _before(self):
        '''Before handler, move the text-pointer to the last word.'''

        idx = self._match(self._text[:self._pointer][::-1], ' .?!,')
        if self._pointer != 0:
            self._pointer -= idx

    def _after(self):
        '''After handler, move the text-pointer to the next word.'''

        idx = self._match(self._text[self._pointer:], ' .?!,')
        if self._pointer != len(self._text):
            self._pointer += idx

    def _behind(self):
        '''Behind handler, move the text-pointer to the last sentence.'''

        idx = self._match(self._text[:self._pointer][::-1])
        if self._pointer != 0:
            self._pointer -= idx

    def _ahead(self):
        '''Ahead handler, move the text-pointer to the next sentence.'''

        idx = self._match(self._text[self._pointer:])
        if self._pointer != len(self._text):
            self._pointer += idx

    def _callback(self, event: keyboard.KeyboardEvent):
        '''Callback for all keyboard events, only record valid keyboard movements.'''

        if event.name == 'esc':
            return
        if event.event_type == 'down' and self._active:
            if self._pointer == len(self._text):
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

        for key, value in keys.items():
            if self[key] != None:
                keyboard.add_hotkey(value, self[key])

        keyboard.hook(self._callback)
        keyboard.wait('esc')
        keyboard.unhook_all()