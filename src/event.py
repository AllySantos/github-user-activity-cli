class Event:
    def __init__(self, type, message):
        self._type = type
        self._message = message


    def __str__(self):
        verb = self._type._verb
        return f' - {verb} {self._message}'
