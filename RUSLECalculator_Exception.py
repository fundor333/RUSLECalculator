__author__ = 'fundor333'


class NoDem(Exception):
    def __init__(self, message):
        self.message = message


class NoFieldImage(Exception):
    def __init__(self, message):
        self.message = message


class RasterError(Exception):
    def __init__(self, message):
        self.message = message


class RError(Exception):
    def __init__(self, message):
        self.message = message


class LSError(Exception):
    def __init__(self, message):
        self.message = message


class CError(Exception):
    def __init__(self, message):
        self.message = message


class KError(Exception):
    def __init__(self, message):
        self.message = message