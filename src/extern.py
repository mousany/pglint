import json
import requests


class pglintExtern():
    '''External component of pglint'''

    def __init__(self):
        '''Initialize pglintExtern.'''

        pass

    def _get(self, url: str):
        '''Get content from remote source.'''

        response = requests.get(url)
        return response.text

    def _post(self, url: str, data: any):
        '''Post content to remote sourse.'''

        pass

    def _json(self, text: str):
        '''Parse JSON from plain text.'''

        return json.loads(text)

    def _read(self, src: str):
        '''Read content from local file.'''

        with open(src) as f:
            text = f.read()
        return text

    def _write(self, src: str, msg: str):
        '''Save content to local file.'''

        with open(src, 'w') as f:
            f.write(msg)
