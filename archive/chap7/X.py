class X:
    def __init__(self, n):
        if n >= 0:
            self._val = n
        else:
            raise Exception ("n must be positive")