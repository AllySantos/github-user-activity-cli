class UserNotFound(Exception):

    def __init__(self, username):
        self.message = f"{username} don't exist on GitHub"
        super().__init__(self.message)

class ResponseEmpty(Exception):
    def __init__(self):
        self.message = "API hasn't return any event"
        super().__init__(self.message)