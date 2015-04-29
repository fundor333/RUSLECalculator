__author__ = 'fundor333'

class NoDem(Exception):
    def __init__(self, message):
        self.message = message

class NoFieldImage(Exception):
    def __init__(self, message):
        self.message=message
