import contextlib
import sys

class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__ = self

        for key, value in self.items():
            if isinstance(value, dict):
                self[key] = AttrDict(value)

            if isinstance(value, list):
                for i, item in enumerate(value):
                    if isinstance(item, dict):
                        self[key][i] = AttrDict(item)

@contextlib.contextmanager
def redirect_stdout(stream):
    sys.stdout = stream
    yield
    sys.stdout = sys.__stdout__
