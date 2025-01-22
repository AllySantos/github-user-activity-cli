class Event:
    def __init__(self, type, message):
        self._type = type
        self._message = message


    def parse(self):
        verb = self._type._verb
        return f'{verb.title()} {self._message}'
