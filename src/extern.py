import json
import requests


class pglintExtern():
    '''External component of pglint'''

    def __init__(self):
        pass

    def _get(self, url: str):
        response = requests.get(url)
        return response.text

    def _post(self, url: str, data: any):
        pass

    def _json(self, text: str):
        return json.dumps(text)

    def _read(self, src: str):
        with open(src) as f:
            text = f.read()
        return text

    def _write(self, src: str, msg: str):
        with open(src, 'w') as f:
            f.write(msg)
